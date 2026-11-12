# Tagkin: system audit, 12 Nov 2026

Scope: what is actually built and configured after batches 1 to 4: database and access rules, CI and deploys, hosting, domain and email, accounts, docs. Method: exploits tried against the local database as an owner and as an anonymous visitor; Supabase's security advisor on the hosted project; live checks of tagkin.app, DNS, Vercel and GitHub settings.

## Findings and status

| # | Loophole | Risk | Fix | Status |
|---|---|---|---|---|
| 1 | An owner could move an item to another of their tags (including onto a blank tag, leaving it `unlinked` with an item) | Breaks rule 4.9 (a code never moves to a different belonging); corrupts tag state | Column-level update rights on `items` (no `tag_code`); trigger refuses any move | Fixed, tested |
| 2 | Status updates accepted dates, times and a 5-year expiry; allowed on blank tags | Breaks rule 7.2 (privacy: no dates, hides within 7 days) | Database trigger: refuses dates, times and links, caps expiry at 7 days, only on active tags | Fixed, tested |
| 3 | Finder message accepted links ("claim-prize.com") | Phishing through public tag pages (audit 12 Nov C2) | Check constraint mirrors `containsUrl` from packages/shared | Fixed, tested |
| 4 | Anyone could call the finder lookup straight through the database API | Code guessing with no rate limit (bypasses the server) | Lookup is server-only (service role); public API returns 401 | Fixed, tested |
| 5 | Private helper functions were executable by everyone by default | Defence in depth | Revoked; only what access rules need is granted | Fixed, tested |
| 6 | Hosted sign-ups were open to anyone | Strangers create accounts and drain the Brevo quota (300/day); demo is meant to be invite-only | Public sign-ups off in Supabase; existing accounts still sign in | Fixed |
| 7 | Database deploys on main did not wait for CI; a manual run on any branch could apply migrations to production | A failing migration could reach production | Deploy runs only after CI passed on that exact commit; manual runs are dry runs | Fixed |
| 8 | GitHub Actions referenced by movable tags | Supply-chain risk (a moved tag runs new code with our secrets) | Pinned to commit SHAs; Dependabot updates them | Fixed |
| 9 | tagkin.app had no security headers, no robots.txt and was indexable | Clickjacking; a placeholder in search results; finder pages could be indexed later | Security headers on every page; noindex and robots block until the Demo release; tag pages never indexed | Fixed |
| 10 | Vercel built with Node 26 while the repo pins Node 24 | Builds differ from local and CI | Vercel project set to Node 24.x | Fixed |
| 11 | Supabase Free pauses after a week without activity | Demo unreachable for a recruiter | Keep-alive workflow (read query twice a week) | Fixed |
| 12 | No DNSSEC on tagkin.app | DNS answers can be forged (redirecting finders to a fake page) | Enable DNSSEC in Cloudflare (one click; protected action, so Selasey does it) | **Open: Selasey** |
| 13 | Account two-factor sign-in not confirmed for GitHub, Cloudflare, Brevo, Vercel | Account takeover = control of domain, code and email | Turn on two-factor sign-in everywhere; store recovery codes offline | **Open: Selasey** |
| 14 | Merged branches piled up | Confusion about what is live | Local merged branches deleted; GitHub now deletes branches on merge | Fixed |
| 15 | Main cannot be protected on the free plan | A direct push skips review | Practice: PRs only (CLAUDE.md); deploys still gated on CI (finding 7) | Accepted |
| 16 | Signed-in users can call state functions (advisor warning) | None: each function checks ownership and is covered by tests | Kept by design; documented | Accepted |
| 17 | Brevo: open tracking cannot be switched off; unsubscribe header could block sign-in codes | Privacy; locked-out users | Anonymous tracking, no previews; unsubscribe risk handled in TK-1 | Partly fixed, TK-1 |

## Reminders added

- Supabase CI token expires around **10 Feb 2027**.
- Brevo SMTP key (`supabase-auth`) expires **12 Nov 2027**.
- DMARC: review reports and move from `p=none` to `p=quarantine` around **10 Dec 2026**.
- Supabase Free has no backups: before real users (Demo release), move to Pro or add a nightly encrypted export.
