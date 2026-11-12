-- Tagkin core schema (Sprint 0: S0-4 tables and access rules, S0-5 state machines).
-- Source of truth: docs/SYSTEM-LOGIC.md sections 2, 3 and 6; docs/BUSINESS-RULES.md 3b, 3c and 4.
-- Rules mirrored from packages/shared (codes, shape fit, limits); database tests keep them equal.

create schema if not exists private;
revoke all on schema private from public, anon, authenticated;

-- ---------- Types ----------
create type public.tag_state as enum ('unclaimed', 'unlinked', 'normal', 'lost', 'return_active', 'retired');
create type public.product as enum ('sticker', 'keychain', 'pet_tag', 'luggage_label', 'lock_screen');
create type public.tag_type as enum ('item', 'travel', 'pet');
create type public.return_state as enum ('open', 'handed_over', 'closed');
create type public.where_now as enum ('with_me', 'staff', 'safe_place');
create type public.message_sender as enum ('owner', 'finder', 'system');
create type public.member_role as enum ('owner');

-- ---------- Code rules (BUSINESS-RULES 4.1, mirrors packages/shared/src/codes.ts) ----------
create function private.code_alphabet() returns text
language sql immutable parallel safe set search_path = '' as $$ select '23456789ABCDEFGHJKMNPQRSTVWXYZ' $$;

-- Luhn mod 30 over the 8 body characters.
create function private.code_has_valid_check(body text) returns boolean
language plpgsql immutable parallel safe set search_path = '' as $$
declare
  a text := private.code_alphabet();
  n int := 30;
  factor int := 1;
  total int := 0;
  v int;
  addend int;
begin
  if body is null or length(body) <> 8 then return false; end if;
  for i in reverse 8..1 loop
    v := strpos(a, substr(body, i, 1)) - 1;
    if v < 0 then return false; end if;
    addend := factor * v;
    factor := case when factor = 2 then 1 else 2 end;
    addend := addend / n + addend % n;
    total := total + addend;
  end loop;
  return total % n = 0;
end $$;

create function private.code_check_character(random7 text) returns text
language plpgsql immutable parallel safe set search_path = '' as $$
declare
  a text := private.code_alphabet();
  n int := 30;
  factor int := 2;
  total int := 0;
  addend int;
begin
  for i in reverse length(random7)..1 loop
    addend := factor * (strpos(a, substr(random7, i, 1)) - 1);
    factor := case when factor = 2 then 1 else 2 end;
    addend := addend / n + addend % n;
    total := total + addend;
  end loop;
  return substr(a, ((n - total % n) % n) + 1, 1);
end $$;

create function private.code_is_blocked(body text) returns boolean
language sql immutable parallel safe set search_path = '' as $$
  select exists (
    select 1 from unnest(array['SEX','ASS','XXX','KKK','FCK','FKK','WTF','TWAT','DCK','ARSCH','KACK','NAZ','NGGR','SS','HH','88']) w
    where strpos(body, w) > 0)
$$;

create function private.code_is_valid(code text) returns boolean
language sql immutable parallel safe set search_path = '' as $$
  select code ~ '^TK-[23456789ABCDEFGHJKMNPQRSTVWXYZ]{4}-[23456789ABCDEFGHJKMNPQRSTVWXYZ]{4}$'
     and private.code_has_valid_check(replace(substr(code, 4), '-', ''))
$$;

-- New unique code; never blocked. Uses rejection sampling for a uniform alphabet.
create function private.generate_tag_code() returns text
language plpgsql volatile set search_path = '' as $$
declare
  a text := private.code_alphabet();
  random7 text;
  body text;
  b int;
begin
  for attempt in 1..1000 loop
    random7 := '';
    while length(random7) < 7 loop
      b := get_byte(extensions.gen_random_bytes(1), 0);
      if b < 240 then random7 := random7 || substr(a, b % 30 + 1, 1); end if;
    end loop;
    body := random7 || private.code_check_character(random7);
    if not private.code_is_blocked(body)
       and not exists (select 1 from public.tags t where t.code = 'TK-' || substr(body, 1, 4) || '-' || substr(body, 5, 4)) then
      return 'TK-' || substr(body, 1, 4) || '-' || substr(body, 5, 4);
    end if;
  end loop;
  raise exception 'code_space_exhausted';
end $$;

-- Normalise what a finder types: any case, spaces, dashes, with or without TK- or the address.
create function private.normalize_code(input text) returns text
language plpgsql immutable parallel safe set search_path = '' as $$
declare s text;
begin
  s := upper(trim(coalesce(input, '')));
  s := regexp_replace(s, '^(HTTPS?://)?(WWW\.)?TAGKIN\.APP/?', '');
  s := regexp_replace(s, '[\s\-_.]', '', 'g');
  if length(s) = 10 and left(s, 2) = 'TK' then s := substr(s, 3); end if;
  if length(s) <> 8 then return null; end if;
  return 'TK-' || substr(s, 1, 4) || '-' || substr(s, 5, 4);
end $$;

-- ---------- Shape fit (BUSINESS-RULES 3c, mirrors packages/shared/src/shape-fit.ts) ----------
create function private.fits(p public.product, t public.tag_type) returns boolean
language sql immutable parallel safe set search_path = '' as $$
  select case p
    when 'sticker' then t in ('item', 'travel')
    when 'keychain' then t = 'item'
    when 'luggage_label' then t = 'travel'
    when 'pet_tag' then t = 'pet'
    when 'lock_screen' then t = 'item'
  end
$$;

-- ---------- Tables ----------
create table public.profiles (
  id uuid primary key references auth.users (id) on delete cascade,
  language text not null default 'en',
  appearance text not null default 'system' check (appearance in ('system', 'light', 'dark')),
  recovery_phone text,
  backup_email text,
  created_at timestamptz not null default now()
);

create table public.devices (
  id uuid primary key default gen_random_uuid(),
  account_id uuid not null references public.profiles (id) on delete cascade,
  platform text not null check (platform in ('ios', 'android', 'web')),
  push_token text,
  last_seen timestamptz not null default now()
);

create table public.tags (
  code text primary key check (private.code_is_valid(code)),
  state public.tag_state not null,
  product public.product not null,
  type public.tag_type,
  colour text,
  size text check (size in ('s', 'm', 'l')),
  finish text check (finish in ('matte', 'gloss', 'holo', 'glow', 'reflective')),
  label text check (char_length(label) <= 12),
  is_free boolean not null default false,
  activation_pin_hash text,
  lost_at timestamptz,
  test_until timestamptz,
  created_at timestamptz not null default now(),
  retired_at timestamptz,
  -- Type is chosen at set-up; only unclaimed and unlinked tags may lack it.
  constraint tags_type_when_set_up check (type is not null or state in ('unclaimed', 'unlinked', 'retired')),
  constraint tags_shape_fits check (type is null or private.fits(product, type)),
  -- The lock-screen tag is digital: never blank, never gifted (rule 3b).
  constraint tags_lock_screen_not_blank check (product <> 'lock_screen' or state not in ('unclaimed', 'unlinked'))
);

create table public.tag_members (
  tag_code text not null references public.tags (code) on delete cascade,
  account_id uuid not null references public.profiles (id) on delete cascade,
  role public.member_role not null default 'owner',
  added_at timestamptz not null default now(),
  primary key (tag_code, account_id)
);
create unique index tag_members_one_owner on public.tag_members (tag_code) where role = 'owner';
create index tag_members_account on public.tag_members (account_id);

create table public.items (
  tag_code text primary key references public.tags (code) on delete cascade,
  name text not null check (char_length(btrim(name)) between 2 and 40),
  photo_path text,
  description text check (char_length(description) <= 120),
  finder_message text not null check (char_length(btrim(finder_message)) between 1 and 160),
  finder_message_lang text not null default 'en',
  care_notes text check (char_length(care_notes) <= 300),
  temperament text[],
  trip jsonb,
  updated_at timestamptz not null default now()
);

create table public.contacts (
  id uuid primary key default gen_random_uuid(),
  account_id uuid not null references public.profiles (id) on delete cascade,
  name text not null check (char_length(name) between 1 and 40),
  email text,
  phone text,
  alert_after_minutes int not null default 120 check (alert_after_minutes between 15 and 1440)
);

create table public.status_updates (
  id uuid primary key default gen_random_uuid(),
  tag_code text not null references public.tags (code) on delete cascade,
  body text not null check (char_length(btrim(body)) between 1 and 60),
  visible boolean not null default true,
  expires_at timestamptz not null default now() + interval '7 days'
);

create table public.returns (
  id uuid primary key default gen_random_uuid(),
  tag_code text not null references public.tags (code) on delete cascade,
  state public.return_state not null default 'open',
  opened_at timestamptz not null default now(),
  closed_at timestamptz,
  handover_code_hash text
);
create unique index returns_one_open on public.returns (tag_code) where state <> 'closed';

create table public.reports (
  id uuid primary key default gen_random_uuid(),
  tag_code text not null references public.tags (code) on delete cascade,
  return_id uuid not null references public.returns (id) on delete cascade,
  where_now public.where_now not null,
  place_text text check (char_length(place_text) <= 200),
  lat double precision,
  lng double precision,
  address text,
  photo_path text,
  note text check (char_length(note) <= 500),
  finder_contact_kind text not null default 'none' check (finder_contact_kind in ('email', 'none')),
  finder_contact text, -- encrypted at the application layer before storage (SYSTEM-LOGIC 10)
  lang text not null default 'en',
  token_hash text not null unique,
  created_at timestamptz not null default now()
);

create table public.scans (
  id bigint generated always as identity primary key,
  tag_code text not null references public.tags (code) on delete cascade,
  at timestamptz not null default now(),
  city text,
  is_test boolean not null default false,
  user_agent_class text,
  report_id uuid references public.reports (id) on delete set null
);
create index scans_tag_at on public.scans (tag_code, at desc);

create table public.messages (
  id uuid primary key default gen_random_uuid(),
  return_id uuid not null references public.returns (id) on delete cascade,
  sender public.message_sender not null,
  body text not null check (char_length(btrim(body)) between 1 and 1000),
  original_text text,
  original_lang text,
  translated_lang text,
  delivered_via text check (delivered_via in ('push', 'email', 'web')),
  status text not null default 'sent' check (status in ('sent', 'failed', 'delivered')),
  created_at timestamptz not null default now()
);
create index messages_return on public.messages (return_id, created_at);

create table public.abuse_reports (
  id uuid primary key default gen_random_uuid(),
  reporter_kind text not null check (reporter_kind in ('owner', 'finder')),
  reporter_account uuid references public.profiles (id) on delete set null,
  target_kind text not null check (target_kind in ('message', 'tag', 'thread')),
  target_id text not null,
  reason text not null,
  details text check (char_length(details) <= 500),
  state text not null default 'open' check (state in ('open', 'reviewed', 'actioned')),
  created_at timestamptz not null default now()
);

-- Designed now, used later (SYSTEM-LOGIC 2).
create table public.entitlements (
  id uuid primary key default gen_random_uuid(),
  account_id uuid not null references public.profiles (id) on delete cascade,
  key text not null,
  source text not null check (source in ('free', 'purchase', 'subscription')),
  valid_until timestamptz,
  unique (account_id, key)
);

create table public.prices (
  id uuid primary key default gen_random_uuid(),
  product public.product not null,
  colour text,
  market text not null default 'eu',
  currency text not null default 'EUR',
  amount_cents int not null check (amount_cents >= 0),
  valid_from timestamptz not null default now()
);

create table public.ownership_transfers (
  id uuid primary key default gen_random_uuid(),
  tag_code text not null references public.tags (code) on delete cascade,
  from_account uuid not null references public.profiles (id) on delete cascade,
  to_email text not null,
  token_hash text not null unique,
  state text not null default 'pending' check (state in ('pending', 'accepted', 'cancelled')),
  created_at timestamptz not null default now()
);

-- ---------- Helpers ----------
create function private.is_owner(p_code text) returns boolean
language sql stable security definer set search_path = '' as $$
  select exists (
    select 1 from public.tag_members m
    where m.tag_code = p_code and m.account_id = (select auth.uid()) and m.role = 'owner')
$$;
grant usage on schema private to authenticated;
grant execute on function private.is_owner(text) to authenticated;

-- New accounts get a profile.
create function private.handle_new_user() returns trigger
language plpgsql security definer set search_path = '' as $$
begin
  insert into public.profiles (id) values (new.id) on conflict do nothing;
  return new;
end $$;
create trigger on_auth_user_created after insert on auth.users
  for each row execute function private.handle_new_user();

-- Name, photo and description lock during a return (rule 4.4).
create function private.items_lock() returns trigger
language plpgsql set search_path = '' as $$
begin
  if (new.name, new.photo_path, new.description) is distinct from (old.name, old.photo_path, old.description)
     and exists (select 1 from public.tags t where t.code = old.tag_code and t.state = 'return_active') then
    raise exception 'item_locked_during_return' using errcode = 'P0001';
  end if;
  new.updated_at := now();
  return new;
end $$;
create trigger items_lock before update on public.items
  for each row execute function private.items_lock();

-- ---------- Row-level security ----------
alter table public.profiles enable row level security;
alter table public.devices enable row level security;
alter table public.tags enable row level security;
alter table public.tag_members enable row level security;
alter table public.items enable row level security;
alter table public.contacts enable row level security;
alter table public.status_updates enable row level security;
alter table public.returns enable row level security;
alter table public.reports enable row level security;
alter table public.scans enable row level security;
alter table public.messages enable row level security;
alter table public.abuse_reports enable row level security;
alter table public.entitlements enable row level security;
alter table public.prices enable row level security;
alter table public.ownership_transfers enable row level security;

create policy profiles_own_read on public.profiles for select to authenticated using (id = (select auth.uid()));
create policy profiles_own_update on public.profiles for update to authenticated
  using (id = (select auth.uid())) with check (id = (select auth.uid()));

create policy devices_own on public.devices for all to authenticated
  using (account_id = (select auth.uid())) with check (account_id = (select auth.uid()));

-- Tags change state only through the functions below; owners can read and style them.
create policy tags_owner_read on public.tags for select to authenticated using (private.is_owner(code));

create policy tag_members_own_read on public.tag_members for select to authenticated
  using (account_id = (select auth.uid()));

create policy items_owner_read on public.items for select to authenticated using (private.is_owner(tag_code));
create policy items_owner_update on public.items for update to authenticated
  using (private.is_owner(tag_code)) with check (private.is_owner(tag_code));

create policy contacts_own on public.contacts for all to authenticated
  using (account_id = (select auth.uid())) with check (account_id = (select auth.uid()));

create policy status_owner on public.status_updates for all to authenticated
  using (private.is_owner(tag_code)) with check (private.is_owner(tag_code));

create policy returns_owner_read on public.returns for select to authenticated using (private.is_owner(tag_code));
create policy reports_owner_read on public.reports for select to authenticated using (private.is_owner(tag_code));
create policy scans_owner_read on public.scans for select to authenticated using (private.is_owner(tag_code));
create policy messages_owner_read on public.messages for select to authenticated
  using (exists (select 1 from public.returns r where r.id = return_id and private.is_owner(r.tag_code)));

create policy entitlements_own_read on public.entitlements for select to authenticated
  using (account_id = (select auth.uid()));

create policy prices_public_read on public.prices for select to anon, authenticated using (true);
-- abuse_reports and ownership_transfers: no client access; the server writes them.

-- ---------- State machines (SYSTEM-LOGIC 3, mirrors packages/shared/src/states.ts) ----------
create function private.require_owner(p_code text) returns void
language plpgsql stable security definer set search_path = '' as $$
begin
  if not private.is_owner(p_code) then
    raise exception 'not_owner' using errcode = '42501';
  end if;
end $$;

create function public.mark_lost(p_code text) returns public.tag_state
language plpgsql security definer set search_path = '' as $$
declare s public.tag_state;
begin
  perform private.require_owner(p_code);
  update public.tags set state = 'lost', lost_at = now() where code = p_code and state = 'normal' returning state into s;
  if s is null then raise exception 'transition_not_allowed' using errcode = 'P0001'; end if;
  return s;
end $$;

create function public.mark_found(p_code text) returns public.tag_state
language plpgsql security definer set search_path = '' as $$
declare s public.tag_state;
begin
  perform private.require_owner(p_code);
  update public.tags set state = 'normal', lost_at = null where code = p_code and state = 'lost' returning state into s;
  if s is null then raise exception 'transition_not_allowed' using errcode = 'P0001'; end if;
  return s;
end $$;

create function public.mark_returned(p_code text) returns public.tag_state
language plpgsql security definer set search_path = '' as $$
declare s public.tag_state;
begin
  perform private.require_owner(p_code);
  update public.tags set state = 'normal', lost_at = null where code = p_code and state = 'return_active' returning state into s;
  if s is null then raise exception 'transition_not_allowed' using errcode = 'P0001'; end if;
  update public.returns set state = 'closed', closed_at = now() where tag_code = p_code and state <> 'closed';
  return s;
end $$;

-- Retired tags keep no personal data (rule 7.3).
create function public.retire_tag(p_code text) returns public.tag_state
language plpgsql security definer set search_path = '' as $$
declare s public.tag_state;
begin
  perform private.require_owner(p_code);
  update public.tags set state = 'retired', retired_at = now(), lost_at = null
    where code = p_code and state <> 'retired' returning state into s;
  if s is null then raise exception 'transition_not_allowed' using errcode = 'P0001'; end if;
  delete from public.items where tag_code = p_code;
  delete from public.status_updates where tag_code = p_code;
  update public.returns set state = 'closed', closed_at = now() where tag_code = p_code and state <> 'closed';
  return s;
end $$;

-- Blank tag set-up: only types that fit the shape (rule 4.8, 3c).
create function public.setup_blank_tag(p_code text, p_type public.tag_type, p_name text, p_finder_message text)
returns public.tag_state
language plpgsql security definer set search_path = '' as $$
declare t public.tags;
begin
  perform private.require_owner(p_code);
  select * into t from public.tags where code = p_code for update;
  if t.state <> 'unlinked' then raise exception 'transition_not_allowed' using errcode = 'P0001'; end if;
  if not private.fits(t.product, p_type) then raise exception 'shape_does_not_fit_type' using errcode = 'P0001'; end if;
  insert into public.items (tag_code, name, finder_message) values (p_code, btrim(p_name), btrim(p_finder_message));
  update public.tags set state = 'normal', type = p_type where code = p_code;
  return 'normal'::public.tag_state;
end $$;

-- ---------- Finder page (no account; TK-10, TK-11) ----------
-- Returns only what a finder may see. Never owner contact details.
create function public.get_finder_page(p_input text) returns jsonb
language plpgsql stable security definer set search_path = '' as $$
declare
  c text := private.normalize_code(p_input);
  t public.tags;
  i public.items;
begin
  if c is null then return jsonb_build_object('result', 'not_a_code'); end if;
  if not private.code_has_valid_check(replace(substr(c, 4), '-', '')) then
    return jsonb_build_object('result', 'check_the_code');
  end if;
  select * into t from public.tags where code = c;
  if not found then return jsonb_build_object('result', 'not_found'); end if;
  if t.state = 'retired' then return jsonb_build_object('result', 'inactive', 'code', c); end if;
  if t.state in ('unclaimed', 'unlinked') then return jsonb_build_object('result', 'not_set_up', 'code', c); end if;
  select * into i from public.items where tag_code = c;
  return jsonb_build_object(
    'result', 'ok',
    'code', c,
    'state', case when t.state = 'lost' then 'lost' when t.state = 'return_active' then 'return_active' else 'normal' end,
    'type', t.type,
    'product', t.product,
    'test', coalesce(t.test_until > now(), false),
    'name', i.name,
    'photo_path', i.photo_path,
    'message', i.finder_message,
    'message_lang', i.finder_message_lang,
    'has_care_notes', i.care_notes is not null,
    'temperament', to_jsonb(i.temperament),
    'trip', case when i.trip is not null and coalesce((i.trip ->> 'ends_on')::date >= current_date, true)
                 then jsonb_build_object('mode', i.trip ->> 'mode', 'carrier', i.trip ->> 'carrier', 'destination', i.trip ->> 'destination')
                 end,
    'status', (select s.body from public.status_updates s
               where s.tag_code = c and s.visible and s.expires_at > now() order by s.expires_at desc limit 1)
  );
end $$;

-- ---------- Function access ----------
revoke execute on all functions in schema public from public, anon;
grant execute on function public.mark_lost(text), public.mark_found(text), public.mark_returned(text),
  public.retire_tag(text), public.setup_blank_tag(text, public.tag_type, text, text) to authenticated;
grant execute on function public.get_finder_page(text) to anon, authenticated;
