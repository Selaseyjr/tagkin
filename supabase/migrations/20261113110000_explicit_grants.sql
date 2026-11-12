-- Explicit table privileges (12 Nov 2026). The hosted project does not expose new tables
-- automatically, while local Supabase grants everything by default; that difference hid all
-- owner data on tagkin.app. Privileges are now declared here, least privilege, identical everywhere.
-- Row-level security still decides which rows each owner sees.

revoke all on all tables in schema public from anon, authenticated;
revoke all on all sequences in schema public from anon, authenticated;
alter default privileges in schema public revoke all on tables from anon, authenticated;
alter default privileges in schema public revoke all on sequences from anon, authenticated;

-- Visitors: only the public price list.
grant select on public.prices to anon, authenticated;

-- Owners read their own rows (row-level security filters them).
grant select on public.profiles, public.devices, public.tags, public.tag_members, public.items,
  public.contacts, public.status_updates, public.returns, public.reports, public.scans,
  public.messages, public.entitlements to authenticated;

-- Owners change only what the screens allow.
grant update (language, appearance, recovery_phone, backup_email) on public.profiles to authenticated;
grant update (name, photo_path, description, finder_message, finder_message_lang, care_notes, temperament, trip)
  on public.items to authenticated;
grant insert, update, delete on public.devices, public.contacts, public.status_updates to authenticated;

-- Everything else (tag state, reports, messages, orders later) changes only through database functions.
