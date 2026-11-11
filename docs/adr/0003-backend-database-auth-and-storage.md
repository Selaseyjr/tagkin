# ADR 0003: Backend, database, auth and storage: Supabase in Frankfurt

**Status:** Accepted · **Date:** 11 Nov 2026

## Context
The data is relational (accounts, tags, items, returns, messages, orders). Owners sign in with an email code. Finders need live replies on the thank-you page. Photos need storage. Data must stay in the EU. Earlier brief suggested Cloudflare Workers, D1 and R2.

## Options
| Option | For | Against |
|---|---|---|
| Supabase (Postgres) in eu-central-1, Frankfurt | Postgres fits the model and the state machines; built-in email one-time-code sign-in; row-level security; Realtime for live replies; Storage for photos; scheduled jobs (pg_cron) and Edge Functions; database, auth and storage stay in the chosen EU region. | Vendor dependency (mitigated: it is standard Postgres); free plan pauses idle projects, so a paid plan is needed before launch. |
| Cloudflare Workers, D1, R2 | Very cheap, fast edge. | D1 is SQLite with limits; auth, realtime and jobs must be built by hand; more work for one developer. |
| Own Node API with managed Postgres | Full control. | Most work: auth, realtime, storage, jobs all custom. |

## Decision
Use Supabase in eu-central-1 (Frankfurt): Postgres, Auth (email OTP), Realtime, Storage, pg_cron, Edge Functions. Business logic in Postgres functions and Next.js route handlers; row-level security on every table.

## Consequences
Replaces the brief's Cloudflare suggestion. Fastest route to a secure MVP. Auth emails go through our own EU email provider (ADR 0005).

**Related:** All epics; state machines and jobs in SYSTEM-LOGIC.md.
