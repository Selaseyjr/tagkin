begin;
create extension if not exists pgtap with schema extensions;
select plan(9);

select ok(private.code_is_valid('TK-7Q4M-9XRD'), 'seed code computed in TypeScript is valid in Postgres');
select ok(not private.code_is_valid('TK-7Q4M-9XRA'), 'wrong check character is rejected');
select ok(not private.code_is_valid('TK-7Q4M-9XR0'), 'characters outside the alphabet are rejected');
select is(private.code_check_character('7Q4M9XR'), 'D', 'check character matches packages/shared');
select is(private.normalize_code(' https://tagkin.app/tk-7q4m-9xrd '), 'TK-7Q4M-9XRD', 'pasted address is normalised');
select is(private.normalize_code('7q4m 9xrd'), 'TK-7Q4M-9XRD', 'typed code without prefix is normalised');
select ok(private.code_is_blocked('AB88CDEF'), 'blocklist matches');

select is(
  (select count(*) from (select private.generate_tag_code() c from generate_series(1, 300)) g
   where private.code_is_valid(g.c) and not private.code_is_blocked(replace(substr(g.c, 4), '-', ''))),
  300::bigint, '300 generated codes are valid and never blocked');
select throws_ok($$ insert into public.tags (code, state, product) values ('TK-AAAA-AAAA', 'unclaimed', 'sticker') $$,
  '23514', null, 'a table row with an invalid code is refused');

select * from finish();
rollback;
