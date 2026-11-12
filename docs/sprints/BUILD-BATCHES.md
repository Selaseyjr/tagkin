# Stage 7 build: batches and gates

Step 7 of the product owner flow, done in batches. A batch starts only when the previous gate is met, so nothing that shapes the pipeline (CI, data model, environments, secrets) gets added late. Each item is its own branch and pull request.

| # | Batch | Items | Needs from Selasey | Gate before the next batch |
|---|---|---|---|---|
| 1 | Monorepo | S0-1 | Nothing | ✓ Clean clone installs, checks and builds (PR 73) |
| 2 | Quality gates | S0-7 shared rules and tokens (shape fit, code alphabet, limits, schemas, tests), S0-2 CI, branch protection on main, dependency updates, secret scanning | OK for the branch protection change | CI green on every PR; main protection needs a paid plan, so: PRs only by practice, and hosted deploys run only after CI passes on main |
| 3 | Data foundation | S0-3 Supabase local and projects, S0-4 migrations with row-level security, S0-5 state machines, S0-6 seed data, migration check in CI, database types into `packages/shared` | Docker Desktop; Supabase account with two Frankfurt projects; `supabase login` | Migrations apply clean; access and state tests pass in CI |
| 4 | Environments and providers | S0-8 Vercel previews, S0-10 DNS, Brevo, sign-in email and hello@ routing, S0-11 keys per environment with a checked env schema, S0-9 EAS dev build, S0-12 tracking plan | Accounts (Vercel, Brevo, Stripe test, Expo, PostHog EU, Sentry EU, DeepL, Google Cloud); CLI logins; paste keys into prompts | Sprint 0 demo: seeded tag on a preview URL on a phone; sign-in code from tagkin.app in the inbox |
| 5 | Sprint 1: finder path | TK-10, 11, 12, 14, 15, 20, 103 | Review the PRs | A finder can report a seeded tag end to end on staging |
| 6 | Sprint 2: owner web | TK-1, 3, 82, 104, 16, 13, 19 | Test on your phone | M1 done: owner signs in, sees the report, replies |
| 7 | M2 web beta (demo mode) | TK-100, 102, 30, 31, 50 to 55, 105 (web); Stripe **test mode**; a simulated print partner behind the fulfilment adapter | Nothing | Owner can create, customise, order with a test card and follow the order |
| 8 | **Demo release** | Demo banner, invite-only sign-up, noindex, simple Impressum and privacy, demo tags and data, keep-alive ping for Supabase Free, Android build by link (EAS), app in the browser for iPhone, short demo video | Optional: recruiters and testers to invite | **Portfolio and investor demo live on tagkin.app** |
| 9 | Owner app (demo scope) | App shell and the M3 stories that demo well: tags, Lost mode, chat, push on Android | Nothing | Android app installed from a link works end to end |

## Funding gate

Everything below waits for funding. Nothing built before it needs redoing: payments and printing are switched by settings, not faked in the screens.

| # | Batch | Items | Needs |
|---|---|---|---|
| 10 | Business and legal | Legal entity, tax and VAT, terms of sale, GPSR, LUCID, trademark, insurance, live Stripe, real print partner (samples) | Funding, tax advisor, lawyer |
| 11 | Store readiness | Remaining M3, M4 gifting and activation, M5 (languages, accessibility, moderation, analytics), Vercel Pro, Supabase Pro | Apple ($99/year), Google ($25), 12-tester closed test |
| 12 | Store launch | Listings, review account, submission | Live in both stores |

Every batch also: tests for new rules, PR review before merge, board and Sprint doc updated, decisions logged in the brief.
