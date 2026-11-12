begin;
create extension if not exists pgtap with schema extensions;
select plan(12);

select is((select count(*)::int from public.tags t join public.tag_members m on m.tag_code = t.code
           where m.account_id = 'd0000000-0000-4000-8000-00000000d3e0'), 4, 'demo owner has 4 demo tags');

set local role anon;
select throws_ok($$ select public.submit_report('TK-D3M7-BKPB', 'with_me', 'Darmstadt Hbf', null, null, 'en', 'x') $$,
  '42501', null, 'visitors cannot file reports through the public API (server only)');

set local role service_role;
select isnt(public.submit_report('TK-D3M7-BKPB', 'staff', 'Darmstadt Hbf, Lost & Found desk', 'Counter 2', null, 'en', 'tok1'),
  null, 'the server files a report');
select is((select state::text from public.tags where code = 'TK-D3M7-BKPB'), 'return_active', 'a report starts the return');
select is(jsonb_array_length(public.get_report_view('tok1') -> 'messages'), 1, 'the finder sees their report');
select throws_ok($$ select public.submit_report('TK-D3M7-KYC4', 'with_me', 'Park', null, null, 'en', 'tok2') $$,
  'P0001', 'tag_not_reportable', 'a blank tag cannot be reported');
select throws_ok($$ select public.submit_report('TK-D3M7-PTGR', 'with_me', '  ', null, null, 'en', 'tok3') $$,
  'P0001', 'place_required', 'the place is required');

set local role authenticated;
set local request.jwt.claims = '{"sub":"d0000000-0000-4000-8000-00000000d3e0","role":"authenticated"}';
select lives_ok($$ select public.owner_reply('TK-D3M7-BKPB', 'Thank you! I''ll pick it up tonight.') $$, 'the owner replies');
set local request.jwt.claims = '{"sub":"11111111-1111-1111-1111-111111111111","role":"authenticated"}';
select throws_ok($$ select public.owner_reply('TK-D3M7-BKPB', 'Hi') $$, '42501', 'not_owner', 'another owner cannot reply');

set local role service_role;
select lives_ok($$ select public.finder_reply('tok1', 'Great, see you then') $$, 'the finder answers');
select is(jsonb_array_length(public.get_report_view('tok1') -> 'messages'), 3, 'both sides see the whole conversation');

reset role;
select private.reset_demo();
select is((select state::text from public.tags where code = 'TK-D3M7-BKPB'), 'normal', 'the nightly reset restores the demo');

select * from finish();
rollback;
