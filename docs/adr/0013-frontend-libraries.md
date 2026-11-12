# ADR 0013: Frontend libraries shared by web and app

**Status:** Accepted · **Date:** 12 Nov 2026

## Context
Web (Next.js) and app (Expo) must show the same rules, texts and design. Choosing libraries per screen later makes the two drift and is costly to undo (audit 12 Nov, B1 to B4).

## Decision
| Need | Choice | Why |
|---|---|---|
| Texts and languages | **i18next** (react-i18next) with JSON in `packages/i18n` | One library and one set of files on web and app; plurals, interpolation, RTL |
| Design tokens and theme | Generated from `docs/brand/tokens.css` into CSS variables (web) and a typed object (app); a small theme hook for light, dark and system | No UI kit lock-in; one source |
| App navigation | **Expo Router** with universal links (iOS) and App Links (Android) on tagkin.app | File-based, deep links built in |
| Forms and validation | **react-hook-form** with the Zod schemas from `packages/shared` | Same validation on client and server |
| Server data | **TanStack Query** with supabase-js | Caching, retries and offline behaviour on both platforms |

## Consequences
Libraries are added when the first screen needs them; nothing else may be introduced for the same job without a new ADR.
