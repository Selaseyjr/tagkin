begin;
create extension if not exists pgtap with schema extensions;
select plan(9);

-- Every table in public has row-level security on.
select is((select count(*) from pg_tables where schemaname = 'public' and not rowsecurity), 0::bigint,
  'row-level security is on for every public table');

set local role anon;
select is((select count(*) from public.tags), 0::bigint, 'anonymous visitors read no tags');
select is((select count(*) from public.items), 0::bigint, 'anonymous visitors read no items');
select is((select count(*) from public.prices), 5::bigint, 'anonymous visitors can read prices');

set local role authenticated;
set local request.jwt.claims = '{"sub":"11111111-1111-1111-1111-111111111111","role":"authenticated"}';
select is((select count(*) from public.tags), 5::bigint, 'Alex sees only Alex''s 5 tags');
select is((select count(*) from public.messages), 2::bigint, 'Alex sees the messages of Alex''s return');
select is((select count(*) from public.profiles), 1::bigint, 'Alex sees only Alex''s profile');

set local request.jwt.claims = '{"sub":"22222222-2222-2222-2222-222222222222","role":"authenticated"}';
select is((select count(*) from public.items), 0::bigint, 'Sam cannot read Alex''s items');
select is((select count(*) from public.scans), 0::bigint, 'Sam cannot read Alex''s scans');

select * from finish();
rollback;
