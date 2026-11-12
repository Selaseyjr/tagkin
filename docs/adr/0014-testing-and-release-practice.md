# ADR 0014: Testing and release practice

**Status:** Accepted · **Date:** 12 Nov 2026

## Context
CI arrives in batch 2. Without agreed tests and release rules it has nothing meaningful to check, and database changes can break production (audit 12 Nov, B5 to B7, F1).

## Decision
- **Tests:** Vitest for logic (`packages/*`, web); **pgTAP** through `supabase test db` for row-level security and state machines; **Playwright** with axe for web journeys and accessibility; **Maestro** for app journeys from M3.
- **Migrations:** written as files, reviewed in the pull request, applied only by CI (staging from main, production after approval). Never edited in the dashboard. Breaking changes in two steps (expand, switch, contract). Migrate first, then deploy.
- **App releases:** EAS Update with preview and production channels; runtime version from the native fingerprint; the app checks a minimum supported version.
- **Environment:** each app validates its environment with Zod at build time; public and secret keys separate.
- **Main is protected:** pull requests only, CI required.

## Consequences
The Definition of Done includes these checks. Slower first set-up, far fewer production surprises.
