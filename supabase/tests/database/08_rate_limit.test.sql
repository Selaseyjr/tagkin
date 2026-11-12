begin;
create extension if not exists pgtap with schema extensions;
select plan(3);
set local role service_role;
select ok(public.check_rate_limit('test-key', 2, 60), 'first call allowed');
select ok(public.check_rate_limit('test-key', 2, 60), 'second call allowed');
select ok(not public.check_rate_limit('test-key', 2, 60), 'third call within the window is refused');
select * from finish();
rollback;
