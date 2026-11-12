-- Demo sprint, day 1: finder reports and replies (TK-12, 14, 15, 16, 104), scans (TK-39),
-- rate limiting (audit B10) and a resettable demo owner (docs/sprints/DEMO-SPRINT.md).
-- Finder-side functions run only with the service role, from our server, behind rate limits.

-- ---------- Rate limiting (Postgres counters; audit B10) ----------
create table private.rate_limits (
  key text primary key,
  window_start timestamptz not null,
  hits int not null
);

-- True when the call is allowed. Keys are hashed by the caller (no raw IPs stored).
create function private.rate_limit_ok(p_key text, p_max int, p_window interval) returns boolean
language plpgsql security definer set search_path = '' as $$
declare r private.rate_limits;
begin
  insert into private.rate_limits as rl (key, window_start, hits) values (p_key, now(), 1)
  on conflict (key) do update set
    hits = case when rl.window_start < now() - p_window then 1 else rl.hits + 1 end,
    window_start = case when rl.window_start < now() - p_window then now() else rl.window_start end
  returning * into r;
  return r.hits <= p_max;
end $$;

create function public.check_rate_limit(p_key text, p_max int, p_window_seconds int) returns boolean
language sql security definer set search_path = '' as $$
  select private.rate_limit_ok(p_key, p_max, make_interval(secs => p_window_seconds))
$$;

-- ---------- Scans (a real page view by a person; bots filtered by the server) ----------
create function public.record_scan(p_code text, p_city text, p_ua_class text) returns void
language plpgsql security definer set search_path = '' as $$
begin
  insert into public.scans (tag_code, city, is_test, user_agent_class)
  select t.code, left(p_city, 80), coalesce(t.test_until > now(), false), left(p_ua_class, 20)
  from public.tags t where t.code = p_code and t.state in ('normal', 'lost', 'return_active');
end $$;

-- ---------- Finder report (opens or joins the return; TK-12, 14, 15) ----------
create function public.submit_report(
  p_code text, p_where public.where_now, p_place text, p_note text,
  p_contact_email text, p_lang text, p_token_hash text
) returns uuid
language plpgsql security definer set search_path = '' as $$
declare
  t public.tags;
  r_id uuid;
  rep_id uuid;
  summary text;
begin
  select * into t from public.tags where code = p_code for update;
  if not found or t.state not in ('normal', 'lost', 'return_active') then
    raise exception 'tag_not_reportable' using errcode = 'P0001';
  end if;
  if coalesce(btrim(p_place), '') = '' then
    raise exception 'place_required' using errcode = 'P0001';
  end if;

  select id into r_id from public.returns where tag_code = p_code and state <> 'closed';
  if r_id is null then
    insert into public.returns (tag_code) values (p_code) returning id into r_id;
  end if;

  insert into public.reports (tag_code, return_id, where_now, place_text, note, finder_contact_kind,
                              finder_contact, lang, token_hash)
  values (p_code, r_id, p_where, left(btrim(p_place), 200), nullif(left(btrim(coalesce(p_note, '')), 500), ''),
          case when nullif(btrim(coalesce(p_contact_email, '')), '') is null then 'none' else 'email' end,
          nullif(btrim(coalesce(p_contact_email, '')), ''), coalesce(p_lang, 'en'), p_token_hash)
  returning id into rep_id;

  summary := case p_where when 'with_me' then 'With me' when 'staff' then 'Handed to staff' else 'Left in a safe place' end
             || ' · ' || left(btrim(p_place), 200)
             || coalesce(E'\n' || nullif(btrim(coalesce(p_note, '')), ''), '');
  insert into public.messages (return_id, sender, body, original_lang) values (r_id, 'finder', left(summary, 1000), p_lang);

  insert into public.scans (tag_code, report_id, city) values (p_code, rep_id, null);
  update public.tags set state = 'return_active' where code = p_code and state in ('normal', 'lost');
  return r_id;
end $$;

-- What the finder's report page shows (no owner details; TK-16).
create function public.get_report_view(p_token_hash text) returns jsonb
language sql stable security definer set search_path = '' as $$
  select jsonb_build_object(
    'code', rep.tag_code,
    'item', i.name,
    'care_notes', i.care_notes,
    'return_state', ret.state,
    'messages', coalesce((select jsonb_agg(jsonb_build_object('from', m.sender, 'body', m.body, 'at', m.created_at)
                                           order by m.created_at)
                          from public.messages m where m.return_id = ret.id), '[]'::jsonb))
  from public.reports rep
  join public.returns ret on ret.id = rep.return_id
  left join public.items i on i.tag_code = rep.tag_code
  where rep.token_hash = p_token_hash
$$;

create function public.finder_reply(p_token_hash text, p_body text) returns void
language plpgsql security definer set search_path = '' as $$
declare r_id uuid;
begin
  select ret.id into r_id from public.reports rep join public.returns ret on ret.id = rep.return_id
  where rep.token_hash = p_token_hash and ret.state <> 'closed';
  if r_id is null then raise exception 'return_closed' using errcode = 'P0001'; end if;
  insert into public.messages (return_id, sender, body) values (r_id, 'finder', left(btrim(p_body), 1000));
end $$;

-- ---------- Owner reply (TK-104) ----------
create function public.owner_reply(p_code text, p_body text) returns void
language plpgsql security definer set search_path = '' as $$
declare r_id uuid;
begin
  perform private.require_owner(p_code);
  select id into r_id from public.returns where tag_code = p_code and state <> 'closed';
  if r_id is null then raise exception 'no_open_return' using errcode = 'P0001'; end if;
  insert into public.messages (return_id, sender, body) values (r_id, 'owner', left(btrim(p_body), 1000));
end $$;

-- ---------- Demo owner (shared account, reset nightly) ----------
create function private.reset_demo() returns void
language plpgsql security definer set search_path = '' as $$
declare demo uuid := 'd0000000-0000-4000-8000-00000000d3e0'::uuid;
begin
  insert into auth.users (instance_id, id, aud, role, email, encrypted_password, email_confirmed_at,
    raw_app_meta_data, raw_user_meta_data, created_at, updated_at, confirmation_token, recovery_token,
    email_change_token_new, email_change, email_change_token_current, reauthentication_token, phone_change, phone_change_token)
  values ('00000000-0000-0000-0000-000000000000', demo, 'authenticated', 'authenticated', 'demo@tagkin.app', '', now(),
    '{"provider":"email","providers":["email"],"demo":true}', '{}', now(), now(), '', '', '', '', '', '', '', '')
  on conflict (id) do nothing;
  insert into public.profiles (id) values (demo) on conflict do nothing;

  delete from public.tags where code in (select tag_code from public.tag_members where account_id = demo);

  insert into public.tags (code, state, product, type, colour, size, finish, lost_at) values
    ('TK-D3M7-BKPB', 'normal', 'sticker', 'item', '#00c48c', 'm', 'matte', null),
    ('TK-D3M7-PTGR', 'lost', 'pet_tag', 'pet', '#ffd23f', 'm', 'gloss', now() - interval '1 day'),
    ('TK-D3M7-TRVS', 'normal', 'luggage_label', 'travel', '#6ec6ff', null, 'matte', null),
    ('TK-D3M7-KYC4', 'unlinked', 'keychain', null, '#0b1712', null, 'gloss', null);
  insert into public.tag_members (tag_code, account_id)
    select c, demo from unnest(array['TK-D3M7-BKPB','TK-D3M7-PTGR','TK-D3M7-TRVS','TK-D3M7-KYC4']) c;

  insert into public.items (tag_code, name, photo_path, description, finder_message, care_notes, temperament, trip) values
    ('TK-D3M7-BKPB', 'Black backpack', '/demo/backpack.jpg', 'Laptop inside, mint tag on the front pocket',
     'Found me? Thank you! Tap below to tell my owner where I am.', null, null, null),
    ('TK-D3M7-PTGR', 'Milo', '/demo/dog.jpg', 'Golden retriever, red collar',
     'Hi, I''m Milo. I''m friendly. Please message my family. I may be scared.',
     'Needs daily medication at 8 pm. Allergic to chicken.', array['Friendly'], null),
    ('TK-D3M7-TRVS', 'Blue suitcase', '/demo/suitcase.jpg', 'Hard shell, mint strap',
     'I''m travelling. Please hand me to airline or hotel staff, or message my owner.', null, null,
     jsonb_build_object('mode', 'plane', 'carrier', 'Lufthansa', 'destination', 'Accra (ACC)',
                        'ends_on', to_char(current_date + 10, 'YYYY-MM-DD')));
  insert into public.status_updates (tag_code, body) values ('TK-D3M7-TRVS', 'On the way to Accra');
  insert into public.scans (tag_code, at, city) values
    ('TK-D3M7-BKPB', now() - interval '9 days', 'Frankfurt'),
    ('TK-D3M7-PTGR', now() - interval '3 hours', 'Darmstadt'),
    ('TK-D3M7-PTGR', now() - interval '20 hours', 'Griesheim');
  delete from private.rate_limits where window_start < now() - interval '1 day';
end $$;

-- ---------- Access: finder-side and demo functions are server-only ----------
revoke execute on function public.check_rate_limit(text, int, int), public.record_scan(text, text, text),
  public.submit_report(text, public.where_now, text, text, text, text, text), public.get_report_view(text),
  public.finder_reply(text, text) from public, anon, authenticated;
grant execute on function public.check_rate_limit(text, int, int), public.record_scan(text, text, text),
  public.submit_report(text, public.where_now, text, text, text, text, text), public.get_report_view(text),
  public.finder_reply(text, text) to service_role;
revoke execute on function public.owner_reply(text, text) from public, anon;
grant execute on function public.owner_reply(text, text) to authenticated;
revoke execute on function private.rate_limit_ok(text, int, interval), private.reset_demo() from public;

-- Demo data exists from the first deploy; refreshed nightly by .github/workflows/reset-demo.yml.
select private.reset_demo();
