# ADR 0011: Repository and delivery setup

**Status:** Accepted · **Date:** 11 Nov 2026

## Context
App, web and shared code must stay in step; one developer needs fast, safe releases.

## Options
| Option | For | Against |
|---|---|---|
| Monorepo with Turborepo and pnpm | Shared packages: tokens, types, validation (Zod), translations; one place for CI. | Some setup. |
| Separate repositories | Simple per app. | Shared code drifts. |

## Decision
Monorepo: apps/mobile (Expo), apps/web (Next.js), packages/shared (types, Zod schemas, state machines), packages/ui-tokens (from tokens.css), packages/i18n. GitHub Actions for lint, type check, tests; EAS for app builds; Vercel previews per pull request.

## Consequences
Board automations already link pull requests to stories.

**Related:** All stories; Definition of Done.
