-- Audit 12 Nov 2026: close access loopholes found by probing the database as an owner and as an
-- anonymous visitor, and by Supabase's security advisor.

-- 1. A code never moves to a different belonging (rule 4.9): owners may edit item fields, never tag_code.
revoke update on public.items from anon, authenticated;
grant update (name, photo_path, description, finder_message, finder_message_lang, care_notes, temperament, trip)
  on public.items to authenticated;

create or replace function private.items_lock() returns trigger
language plpgsql set search_path = '' as $$
begin
  if new.tag_code is distinct from old.tag_code then
    raise exception 'item_cannot_move_to_another_tag' using errcode = 'P0001';
  end if;
  if (new.name, new.photo_path, new.description) is distinct from (old.name, old.photo_path, old.description)
     and exists (select 1 from public.tags t where t.code = old.tag_code and t.state = 'return_active') then
    raise exception 'item_locked_during_return' using errcode = 'P0001';
  end if;
  new.updated_at := now();
  return new;
end $$;

-- 2. No links in public text on finder pages (audit C2; mirrors containsUrl in packages/shared).
create function private.contains_link(t text) returns boolean
language sql immutable parallel safe set search_path = '' as $$
  select coalesce(t ~* '(https?://|www\.)\S+|\m[a-z0-9-]+\.(com|de|net|org|io|app|me|link|ly|co|info|xyz)\M', false)
$$;
alter table public.items add constraint items_finder_message_no_links check (not private.contains_link(finder_message));
alter table public.items add constraint items_description_no_links check (not private.contains_link(description));

-- 3. Status updates: city level, no dates or times, hidden within 7 days (rule 7.2), only on active tags.
create function private.contains_date_or_time(t text) returns boolean
language sql immutable parallel safe set search_path = '' as $$
  select coalesce(t ~* (
    '\m\d{1,2}[./-]\d{1,2}([./-]\d{2,4})?\M|\m\d{1,2}:\d{2}\M|'
    '\m(today|tomorrow|tonight|yesterday|heute|morgen|gestern|monday|tuesday|wednesday|thursday|friday|saturday|sunday|'
    'montag|dienstag|mittwoch|donnerstag|freitag|samstag|sonntag|jan|january|januar|feb|february|februar|mar|march|märz|'
    'apr|april|may|mai|jun|june|juni|jul|july|juli|aug|august|sep|sept|september|oct|october|okt|oktober|nov|november|'
    'dec|december|dez|dezember)\M'), false)
$$;

create function private.status_rules() returns trigger
language plpgsql set search_path = '' as $$
begin
  if private.contains_date_or_time(new.body) then
    raise exception 'status_no_dates_or_times' using errcode = 'P0001';
  end if;
  if private.contains_link(new.body) then
    raise exception 'links_not_allowed' using errcode = 'P0001';
  end if;
  if new.expires_at > now() + interval '7 days' then
    new.expires_at := now() + interval '7 days';
  end if;
  if not exists (select 1 from public.tags t where t.code = new.tag_code and t.state in ('normal', 'lost', 'return_active')) then
    raise exception 'tag_not_active' using errcode = 'P0001';
  end if;
  return new;
end $$;
create trigger status_rules before insert or update on public.status_updates
  for each row execute function private.status_rules();

-- 4. The finder page is served by our server only, so rate limits cannot be bypassed by calling the
--    database API directly (security advisor; audit B10).
revoke execute on function public.get_finder_page(text) from anon, authenticated;
grant execute on function public.get_finder_page(text) to service_role;

-- 5. Private helpers: no default access for everyone; only what the access rules need.
revoke execute on all functions in schema private from public;
alter default privileges in schema private revoke execute on functions from public;
grant execute on function private.is_owner(text), private.contains_link(text), private.contains_date_or_time(text)
  to authenticated;
