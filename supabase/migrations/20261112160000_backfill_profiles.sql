-- Accounts created before the profile trigger existed (the hosted test sign-in on 12 Nov) get a profile.
insert into public.profiles (id)
select u.id from auth.users u
where not exists (select 1 from public.profiles p where p.id = u.id);
