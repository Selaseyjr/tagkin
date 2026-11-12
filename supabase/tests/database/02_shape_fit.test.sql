begin;
create extension if not exists pgtap with schema extensions;
select plan(6);

select ok(private.fits('sticker', 'travel'), 'sticker fits travel');
select ok(not private.fits('keychain', 'travel'), 'keychain does not fit travel');
select ok(not private.fits('lock_screen', 'pet'), 'lock screen does not fit a pet');
select throws_ok(format($$ insert into public.tags (code, state, product, type) values (%L, 'normal', 'pet_tag', 'item') $$,
  private.generate_tag_code()), '23514', null, 'pet tag saved as an item tag is refused');
select throws_ok(format($$ insert into public.tags (code, state, product) values (%L, 'unlinked', 'lock_screen') $$,
  private.generate_tag_code()), '23514', null, 'lock screen can never be a blank tag');
select throws_ok(format($$ insert into public.tags (code, state, product) values (%L, 'normal', 'sticker') $$,
  private.generate_tag_code()), '23514', null, 'a set-up tag must have a type');

select * from finish();
rollback;
