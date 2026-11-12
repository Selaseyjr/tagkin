begin;
create extension if not exists pgtap with schema extensions;
select plan(10);

set local role authenticated;
set local request.jwt.claims = '{"sub":"11111111-1111-1111-1111-111111111111","role":"authenticated"}';

select throws_ok($$ update public.items set tag_code = 'TK-B7KD-3QW7' where tag_code = 'TK-M3PF-2KWM' $$,
  '42501', null, 'an item cannot be moved to another tag');
select throws_ok($$ update public.items set finder_message = 'Reward! Visit claim-prize.com' where tag_code = 'TK-7Q4M-9XRD' $$,
  '23514', null, 'links are refused in the finder message');
select lives_ok($$ update public.items set finder_message = 'Found me? Thank you!' where tag_code = 'TK-7Q4M-9XRD' $$,
  'a normal finder message is accepted');
select throws_ok($$ insert into public.status_updates (tag_code, body) values ('TK-7Q4M-9XRD', 'Back on 20.11') $$,
  'P0001', 'status_no_dates_or_times', 'dates are refused in status updates');
select throws_ok($$ insert into public.status_updates (tag_code, body) values ('TK-7Q4M-9XRD', 'Landing 14:30') $$,
  'P0001', 'status_no_dates_or_times', 'times are refused in status updates');
select lives_ok($$ insert into public.status_updates (tag_code, body, expires_at) values ('TK-7Q4M-9XRD', 'Arrived in Dubai', now() + interval '5 years') $$,
  'a city-level status is accepted');
select ok((select max(expires_at) from public.status_updates where tag_code = 'TK-7Q4M-9XRD') <= now() + interval '7 days',
  'status updates hide within 7 days, whatever the client asks');
select throws_ok($$ insert into public.status_updates (tag_code, body) values ('TK-B7KD-3QW7', 'Arrived in Accra') $$,
  'P0001', 'tag_not_active', 'no status updates on a blank tag');

set local role anon;
select throws_ok($$ select private.generate_tag_code() $$, '42501', null, 'private helpers are closed to visitors');

reset role;
select is((select count(*)::int from information_schema.routine_privileges
           where routine_schema = 'private' and grantee = 'PUBLIC'), 0, 'no private function is open to everyone');

select * from finish();
rollback;
