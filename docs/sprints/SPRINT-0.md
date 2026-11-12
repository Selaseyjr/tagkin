# Sprint 0 · Foundations

Step 7 (build) of the product owner flow. Dates: **Thu 12 Nov to Wed 18 Nov 2026** (one-week sprints from here on).

**Goal:** an empty but real system. A pull request runs CI and deploys a preview; a seeded tag opens at a preview URL; a sign-in email arrives from tagkin.app.

No user stories are built in Sprint 0. It makes M1 buildable.

## Backlog

| # | Item | Done when | Blocked by |
|---|---|---|---|
| S0-1 ✓ | Monorepo (pnpm + Turborepo): `apps/web`, `apps/mobile`, `packages/shared`, `packages/tokens`, `packages/i18n` (`supabase/` comes with S0-3) | `pnpm build` and `pnpm lint` pass from a clean clone. **Done 12 Nov:** Node 24, pnpm 12, Next 16.4, Expo SDK 58, TypeScript 6.0 everywhere; app ids `app.tagkin`, scheme `tagkin://`; 13 checks green, web builds, Expo doctor 20/20, iOS bundle resolves the shared package | |
| S0-2 ✓ | CI on GitHub Actions: lint, type check, unit tests, migration check | Required check on `main`; red on a broken migration. **Done 12 Nov:** format, lint, typecheck, tests and build on every PR and push to main; gitleaks secret scan (GitHub's own secret and code scanning need a paid plan for private repos); Dependabot weekly (Expo SDK upgrades excluded); PR template with the Definition of Done. Migration check arrives with S0-3. Branch protection waits for Selasey's OK | S0-1 |
| S0-3 ✓ | Supabase: one Frankfurt project (`tagkin`, demo-first: no separate staging yet); local dev with the CLI | `supabase start` works. **Done 12 Nov:** Postgres 17 local and hosted; email code 6 digits, 10 min, resend after 30 s. Linking and remote migrations come with batch 4 (CI secrets) | |
| S0-4 ✓ | Core migrations with row-level security on every table; tag members, entitlements, prices, transfers ready | **Done 12 Nov:** 15 tables; RLS on all (tested); owners read only their own rows; finders read only through `get_finder_page`; code format and shape fit enforced by constraints | S0-3 |
| S0-5 ✓ | State machines in Postgres: `mark_lost`, `mark_found`, `mark_returned`, `retire_tag`, `setup_blank_tag`; item lock during a return | **Done 12 Nov:** illegal moves and non-owners rejected (tested) | S0-4 |
| S0-6 ✓ | Seed data: 7 tags (active, lost, travel in return, blank, unclaimed gift, free phone tag, retired), each with its own scans | **Done 12 Nov:** codes carry valid check characters; demo people only | S0-4 |
| S0-7 ✓ | `packages/tokens` generated from docs/brand/tokens.css; `packages/shared` with code alphabet, limits, shape-fit table, Zod schemas | Web renders a token-styled page; code parser and shape fit tested. **Done 12 Nov:** codes (check character catches every single typo, blocklist, permanent capitalised QR address), shape fit, limits, schemas (links, contact details, dates blocked where public), tag and order state rules; tokens generated with a sync test; i18next package; 35 tests | S0-1 |
| S0-8 ✓ | Vercel project for `apps/web`, preview per pull request | **Done 12 Nov:** project `tagkin` (Hobby, functions in Frankfurt); tagkin.app live with HTTPS, www redirects to it; previews per pull request; public Supabase values set for production, preview and development | S0-1, S0-3 |
| S0-9 | Expo app shell builds with EAS (development build only) | Opens the splash on a simulator | S0-1 |
| S0-10 ✓ | Domain, DNS on Cloudflare, Brevo, sign-in email, inbound route | **Done 12 Nov:** Brevo domain authenticated (DKIM, DMARC at p=none); hosted Supabase Auth sends through Brevo SMTP; first email reached the Gmail inbox; sign-in email is a 6-digit code without links (set in the dashboard, checked read-only by CI). hello@tagkin.app forwards to Gmail. Not yet: the Brevo inbound route (with TK-104) | Domain ✓ |
| S0-11 | Provider accounts and keys in env per environment: DeepL, Google Places (quota + billing alert), Stripe test, PostHog EU, Sentry EU | Keys in Vercel and Supabase secrets, none in the repo; billing alerts on | |
| S0-12 | Tracking plan for the MVP success measures (brief 13b): event names, properties, no personal data | Reviewed against ADR 0012 | |

Not in Sprint 0: Bird SMS (needed for TK-4, M3), print partner (ADR 0010, after samples), Apple and Google developer accounts (before TestFlight).

## Exit criteria

- Every item above is done or carried with a reason.
- Demo: open a seeded tag on a preview URL on a phone, receive a sign-in code from tagkin.app.
- Board: Sprint 1 picked from M1 Ready stories.

## Proposed Sprint 1 (19 to 25 Nov): finder path end to end

TK-10, TK-11, TK-12, TK-14, TK-15, TK-20, TK-103. Sprint 2: TK-1, TK-3, TK-82, TK-104, TK-16, TK-13, TK-19.

## Risks

- ~~Domain late~~: resolved, tagkin.app bought 12 Nov.
- **Brevo deliverability:** a new domain may land in spam; DMARC at `p=none` first, warm with test sends.
- **Solo capacity:** 12 items in a week is tight; S0-9 and S0-12 can carry.

**Reminders:** Brevo SMTP key `supabase-auth` expires 12 Nov 2027. DMARC: move from p=none to p=quarantine around 10 Dec 2026 after reviewing reports. Supabase Free has no backups: decide Pro or a nightly encrypted export before the Demo release. Hosted sign-ups are off (invite-only demo).

**Credentials to renew:** Supabase CI token (`SUPABASE_ACCESS_TOKEN`, scoped to the tagkin project) expires around **10 Feb 2027**; generate a new one with the same five permissions and replace the GitHub secret.
