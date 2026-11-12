begin;
create extension if not exists pgtap with schema extensions;
select plan(10);

set local role anon;
select is(public.get_finder_page('tk-7q4m-9xrd') ->> 'result', 'ok', 'finder opens a tag by typed code');
select is(public.get_finder_page('TK-7Q4M-9XRD') ->> 'name', 'Black backpack', 'finder sees the item name');
select is(public.get_finder_page('TK-M3PF-2KWM') ->> 'state', 'lost', 'lost tag shows as lost');
select ok(public.get_finder_page('TK-M3PF-2KWM') ->> 'care_notes' is null, 'care notes are not sent with the page');
select is(public.get_finder_page('TK-B7KD-3QW7') ->> 'result', 'not_set_up', 'blank tag shows not set up');
select is(public.get_finder_page('TK-5VJ2-QA7V') ->> 'result', 'inactive', 'retired tag shows inactive');
select is(public.get_finder_page('TK-7Q4M-9XRA') ->> 'result', 'check_the_code', 'typo caught by the check character');
select is(public.get_finder_page('hello') ->> 'result', 'not_a_code', 'nonsense input is not a code');
select is(public.get_finder_page('TK-H8RC-4TNQ') -> 'trip' ->> 'destination', 'Accra (ACC)', 'travel tag shows destination only');
select throws_ok($$ select public.mark_lost('TK-7Q4M-9XRD') $$, '42501', null, 'anonymous visitors cannot change tags');

select * from finish();
rollback;
