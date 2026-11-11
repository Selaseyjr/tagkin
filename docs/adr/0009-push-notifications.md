# ADR 0009: Push notifications: Expo push service

**Status:** Accepted · **Date:** 11 Nov 2026

## Context
Owners get alerts for scans, reports and messages on iOS and Android.

## Options
| Option | For | Against |
|---|---|---|
| Expo push service (wraps APNs and FCM) | One API for both platforms; fits Expo. | Depends on Expo's service. |
| Direct APNs and FCM | No middle layer. | Two integrations to build and maintain. |

## Decision
Use Expo push; send from the backend; fall back to email when a token is invalid or push is off.

## Consequences
Simple; can move to direct APNs/FCM later if needed.

**Related:** TK-70, TK-71.
