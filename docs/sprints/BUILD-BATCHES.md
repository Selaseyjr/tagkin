# Stage 7 build: batches and gates

Step 7 of the product owner flow, done in batches. A batch starts only when the previous gate is met, so nothing that shapes the pipeline (CI, data model, environments, secrets) gets added late. Each item is its own branch and pull request.

| # | Batch | Items | Needs from Selasey | Gate before the next batch |
|---|---|---|---|---|
| 1 | Monorepo | S0-1 | Nothing | ✓ Clean clone installs, checks and builds (PR 73) |
| 2 | Quality gates | S0-7 shared rules and tokens (shape fit, code alphabet, limits, schemas, tests), S0-2 CI, branch protection on main, dependency updates, secret scanning | OK for the branch protection change | CI required on main; no feature code before this |
| 3 | Data foundation | S0-3 Supabase local and projects, S0-4 migrations with row-level security, S0-5 state machines, S0-6 seed data, migration check in CI, database types into `packages/shared` | Docker Desktop; Supabase account with two Frankfurt projects; `supabase login` | Migrations apply clean; access and state tests pass in CI |
| 4 | Environments and providers | S0-8 Vercel previews, S0-10 DNS, Brevo, sign-in email and hello@ routing, S0-11 keys per environment with a checked env schema, S0-9 EAS dev build, S0-12 tracking plan | Accounts (Vercel, Brevo, Stripe test, Expo, PostHog EU, Sentry EU, DeepL, Google Cloud); CLI logins; paste keys into prompts | Sprint 0 demo: seeded tag on a preview URL on a phone; sign-in code from tagkin.app in the inbox |
| 5 | Sprint 1: finder path | TK-10, 11, 12, 14, 15, 20, 103 | Review the PRs | A finder can report a seeded tag end to end on staging |
| 6 | Sprint 2: owner web | TK-1, 3, 82, 104, 16, 13, 19 | Test on your phone | M1 done: owner signs in, sees the report, replies |
| 7 | M2 web beta | TK-100, 102, 30, 31, 50 to 55, 105 (web) and the print partner adapter | Print partner choice from samples; final prices | Web beta release on tagkin.app |
| 8 | M3 owner app | App shell and the M3 stories | Apple and Google developer accounts before TestFlight | TestFlight and internal testing build |
| 9 | M4 gifting and activation | TK-60, 61, 62, 101 | Gift card and PIN printing with the partner | Gift order to activation works end to end |
| 10 | M5 launch readiness | Website, legal, languages, accessibility, moderation, analytics, store listings | Legal review; store submission | Live in both stores |

Every batch also: tests for new rules, PR review before merge, board and Sprint doc updated, decisions logged in the brief.
