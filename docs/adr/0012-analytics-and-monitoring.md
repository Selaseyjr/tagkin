# ADR 0012: Analytics and monitoring: EU-hosted

**Status:** Proposed · **Date:** 11 Nov 2026

## Context
Success measures must be tracked without profiling users; errors must be caught.

## Options
| Option | For | Against |
|---|---|---|
| PostHog EU cloud + Sentry (EU region) | Product analytics and error tracking with EU hosting options. | Configure to avoid personal data. |
| Plausible for the website | Privacy-first, no cookies. | Website only. |

## Decision
PostHog EU for product events (no session recording of finder pages, no personal data), Sentry for errors, Plausible optional for the website. Events match the success measures in the brief.

## Consequences
No cookie banner needed if no tracking cookies are used.

**Related:** TK-94, TK-99, NFR monitoring.
