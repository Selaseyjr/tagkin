# Sprint 0 · Foundations

Step 7 (build) of the product owner flow. Dates: **Thu 12 Nov to Wed 18 Nov 2026** (one-week sprints from here on).

**Goal:** an empty but real system. A pull request runs CI and deploys a preview; a seeded tag opens at a preview URL; a sign-in email arrives from tagkin.app.

No user stories are built in Sprint 0. It makes M1 buildable.

## Backlog

| # | Item | Done when | Blocked by |
|---|---|---|---|
| S0-1 ✓ | Monorepo (pnpm + Turborepo): `apps/web`, `apps/mobile`, `packages/shared`, `packages/tokens`, `packages/i18n` (`supabase/` comes with S0-3) | `pnpm build` and `pnpm lint` pass from a clean clone. **Done 12 Nov:** Node 24, pnpm 12, Next 16.4, Expo SDK 58, TypeScript 6.0 everywhere; app ids `app.tagkin`, scheme `tagkin://`; 13 checks green, web builds, Expo doctor 20/20, iOS bundle resolves the shared package | |
| S0-2 | CI on GitHub Actions: lint, type check, unit tests, migration check | Required check on `main`; red on a broken migration | S0-1 |
| S0-3 | Supabase: staging and production projects in Frankfurt; local dev with the CLI | `supabase start` works; staging linked | |
| S0-4 | Core migrations: accounts, devices, tags, items, contacts, scans, reports, returns, messages, abuse_reports; tag members, entitlements, prices with currency, transfers as empty tables | Migrations apply clean; row-level security on every table; tests for owner-only access | S0-3 |
| S0-5 | State machines in Postgres: tag (`mark_lost`, `mark_found`) and return (open, closed) | Illegal transitions rejected in tests | S0-4 |
| S0-6 | Seed data: 7 tags covering active, lost, travel, pet, unclaimed, unlinked (blank), retired, each with its own scans | Each opens at `/{code}` locally | S0-4 |
| S0-7 | `packages/tokens` generated from docs/brand/tokens.css; `packages/shared` with code alphabet, limits, shape-fit table, Zod schemas | Web renders a token-styled page; code parser and shape fit tested | S0-1 |
| S0-8 | Vercel project for `apps/web`, preview per pull request against staging | A PR comment shows the preview URL | S0-1, S0-3 |
| S0-9 | Expo app shell builds with EAS (development build only) | Opens the splash on a simulator | S0-1 |
| S0-10 | Domain tagkin.app (Cloudflare Registrar): DNS stays on Cloudflare, records point to Vercel with the proxy off; hello@ forwarded by Cloudflare Email Routing; Brevo inbound on a reply subdomain; Brevo verified (SPF, DKIM, DMARC); Supabase Auth sends codes through Brevo SMTP; inbound route set | A sign-in code arrives in Gmail inbox, not spam; a reply reaches the inbound webhook | Domain ✓ (bought 12 Nov) |
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
