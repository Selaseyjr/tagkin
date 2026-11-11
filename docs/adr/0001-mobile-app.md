# ADR 0001: Mobile app: React Native with Expo

**Status:** Accepted · **Date:** 11 Nov 2026

## Context
Tagkin needs one owner app on iOS and Android, built by a small team (initially one developer with AI help), with push notifications, camera QR scanning, Apple Pay and Google Pay, deep links, and frequent small updates.

## Options
| Option | For | Against |
|---|---|---|
| React Native with Expo | One TypeScript codebase for iOS and Android; shares types and validation with the web; Expo builds in the cloud (EAS) without maintaining native projects; over-the-air updates for copy and small fixes; mature Stripe, camera and push libraries. | Some native modules need a development build; very custom native UI is harder. |
| Flutter | Excellent performance and UI control. | Dart is not shared with the web; second language and toolchain for one developer. |
| Native Swift and Kotlin | Best platform fit. | Two codebases; roughly double the work. |

## Decision
Use React Native with Expo (managed workflow, development builds where needed). TypeScript everywhere.

## Consequences
Fast delivery on both platforms; shared code with the web. Expo SDK upgrades must be planned. tokens.css becomes the app theme.

**Related:** Owner app: TK-1 to TK-99 where the app is involved.
