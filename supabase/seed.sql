-- Local and demo seed (S0-6): two owners, 7 tags covering every state, each with its own scans.
-- Codes carry valid check characters (computed with packages/shared). Demo data only; no real people.

insert into auth.users (instance_id, id, aud, role, email, encrypted_password, email_confirmed_at,
  raw_app_meta_data, raw_user_meta_data, created_at, updated_at,
  confirmation_token, recovery_token, email_change_token_new, email_change, email_change_token_current, reauthentication_token, phone_change, phone_change_token)
values
  ('00000000-0000-0000-0000-000000000000', '11111111-1111-1111-1111-111111111111', 'authenticated', 'authenticated',
   'alex@example.com', '', now(), '{"provider":"email","providers":["email"]}', '{}', now(), now(), '', '', '', '', '', '', '', ''),
  ('00000000-0000-0000-0000-000000000000', '22222222-2222-2222-2222-222222222222', 'authenticated', 'authenticated',
   'sam@example.com', '', now(), '{"provider":"email","providers":["email"]}', '{}', now(), now(), '', '', '', '', '', '', '', '');

insert into public.tags (code, state, product, type, colour, size, finish, is_free) values
  ('TK-7Q4M-9XRD', 'normal',        'sticker',       'item',   '#00c48c', 'm', 'matte', false),
  ('TK-M3PF-2KWM', 'lost',          'pet_tag',       'pet',    '#ffd23f', 'm', 'gloss', false),
  ('TK-H8RC-4TNQ', 'return_active', 'luggage_label', 'travel', '#6ec6ff', null, 'matte', false),
  ('TK-B7KD-3QW7', 'unlinked',      'keychain',      null,     '#0b1712', null, 'gloss', false),
  ('TK-C4RM-8PZ6', 'unclaimed',     'sticker',       null,     '#ff7a6b', 'm', 'matte', false),
  ('TK-W6QB-8MZE', 'normal',        'lock_screen',   'item',   '#00c48c', null, null,    true),
  ('TK-5VJ2-QA7V', 'retired',       'sticker',       null,     '#e9dcc3', 's', 'matte', false);
update public.tags set lost_at = now() - interval '1 day' where code = 'TK-M3PF-2KWM';
update public.tags set retired_at = now() - interval '20 days' where code = 'TK-5VJ2-QA7V';

insert into public.tag_members (tag_code, account_id) values
  ('TK-7Q4M-9XRD', '11111111-1111-1111-1111-111111111111'),
  ('TK-M3PF-2KWM', '11111111-1111-1111-1111-111111111111'),
  ('TK-H8RC-4TNQ', '11111111-1111-1111-1111-111111111111'),
  ('TK-B7KD-3QW7', '11111111-1111-1111-1111-111111111111'),
  ('TK-W6QB-8MZE', '11111111-1111-1111-1111-111111111111'),
  ('TK-5VJ2-QA7V', '22222222-2222-2222-2222-222222222222');

insert into public.items (tag_code, name, description, finder_message, care_notes, temperament, trip) values
  ('TK-7Q4M-9XRD', 'Black backpack', 'Laptop inside, mint tag on the front pocket',
   'Found me? Thank you! Tap below to tell my owner where I am.', null, null, null),
  ('TK-M3PF-2KWM', 'Milo', 'Golden retriever, red collar',
   'Hi, I''m Milo. I''m friendly. Please message my family. I may be scared.',
   'Needs daily medication at 8 pm. Allergic to chicken.', array['Friendly'], null),
  ('TK-H8RC-4TNQ', 'Blue suitcase', 'Hard shell, mint strap',
   'I''m travelling. Please hand me to airline or hotel staff, or message my owner.', null, null,
   '{"mode":"plane","carrier":"Lufthansa","destination":"Accra (ACC)","ends_on":"2026-11-20"}'),
  ('TK-W6QB-8MZE', 'Alex''s phone', null,
   'Found my phone? Thank you! Tap below to tell me where it is.', null, null, null);

insert into public.scans (tag_code, at, city, is_test) values
  ('TK-7Q4M-9XRD', now() - interval '9 days', 'Frankfurt', false),
  ('TK-7Q4M-9XRD', now() - interval '15 days', 'Darmstadt', true),
  ('TK-M3PF-2KWM', now() - interval '3 hours', 'Darmstadt', false),
  ('TK-M3PF-2KWM', now() - interval '7 hours', 'Darmstadt', false),
  ('TK-M3PF-2KWM', now() - interval '20 hours', 'Griesheim', false),
  ('TK-H8RC-4TNQ', now() - interval '2 hours', 'Darmstadt', false);

with r as (
  insert into public.returns (tag_code, opened_at) values ('TK-H8RC-4TNQ', now() - interval '2 hours') returning id
), rep as (
  insert into public.reports (tag_code, return_id, where_now, place_text, note, lang, token_hash)
  select 'TK-H8RC-4TNQ', r.id, 'staff', 'Darmstadt Hbf, Lost & Found desk', 'Je l''ai laissée au guichet 2.', 'fr',
         encode(extensions.digest('demo-report-token', 'sha256'), 'hex') from r returning return_id
)
insert into public.messages (return_id, sender, body, original_text, original_lang, translated_lang)
select return_id, 'finder'::public.message_sender, 'I left it at counter 2.', 'Je l''ai laissée au guichet 2.', 'fr', 'en' from rep
union all
select return_id, 'owner'::public.message_sender, 'Thank you so much! I''ll pick it up tonight.', null, 'en', null from rep;

insert into public.status_updates (tag_code, body) values ('TK-H8RC-4TNQ', 'On the way to Accra');

insert into public.entitlements (account_id, key, source) values
  ('11111111-1111-1111-1111-111111111111', 'free_phone_tag', 'free');

-- Sample prices until the print partner confirms (ADR 0010).
insert into public.prices (product, amount_cents) values
  ('sticker', 490), ('keychain', 990), ('pet_tag', 1290), ('luggage_label', 1190), ('lock_screen', 0);
