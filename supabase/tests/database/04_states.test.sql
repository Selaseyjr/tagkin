begin;
create extension if not exists pgtap with schema extensions;
select plan(11);

set local role authenticated;
set local request.jwt.claims = '{"sub":"22222222-2222-2222-2222-222222222222","role":"authenticated"}';
select throws_ok($$ select public.mark_lost('TK-7Q4M-9XRD') $$, '42501', 'not_owner', 'Sam cannot mark Alex''s tag lost');

set local request.jwt.claims = '{"sub":"11111111-1111-1111-1111-111111111111","role":"authenticated"}';
select is(public.mark_lost('TK-7Q4M-9XRD'), 'lost'::public.tag_state, 'normal → lost');
select throws_ok($$ select public.mark_lost('TK-7Q4M-9XRD') $$, 'P0001', 'transition_not_allowed', 'lost cannot be marked lost again');
select lives_ok($$ update public.items set name = 'Black rucksack' where tag_code = 'TK-7Q4M-9XRD' $$,
  'name stays editable in Lost mode');
select is(public.mark_found('TK-7Q4M-9XRD'), 'normal'::public.tag_state, 'lost → normal');

select throws_ok($$ update public.items set name = 'Other' where tag_code = 'TK-H8RC-4TNQ' $$,
  'P0001', 'item_locked_during_return', 'name is locked during a return');
select lives_ok($$ update public.items set finder_message = 'Please hand me to staff.' where tag_code = 'TK-H8RC-4TNQ' $$,
  'finder message stays editable during a return');
select is(public.mark_returned('TK-H8RC-4TNQ'), 'normal'::public.tag_state, 'return_active → normal');

select throws_ok($$ select public.setup_blank_tag('TK-B7KD-3QW7', 'pet', 'Luna', 'Hi!') $$,
  'P0001', 'shape_does_not_fit_type', 'a blank keychain cannot become a pet tag');
select is(public.setup_blank_tag('TK-B7KD-3QW7', 'item', 'House keys', 'Found my keys? Thank you!'),
  'normal'::public.tag_state, 'blank keychain set up as an item');

select public.retire_tag('TK-7Q4M-9XRD');
select is((select count(*) from public.items where tag_code = 'TK-7Q4M-9XRD'), 0::bigint, 'retiring removes the item details');

select * from finish();
rollback;
