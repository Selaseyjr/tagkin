# ADR 0006: SMS for account recovery

**Status:** Proposed · **Date:** 11 Nov 2026

## Context
At launch SMS is used only for recovery codes.

## Options
| Option | For | Against |
|---|---|---|
| Twilio Verify | Reliable, global, simple. | US company; per-verification cost. |
| MessageBird (Bird) | EU company. | Check API stability and pricing. |

## Decision
Use a verification API (Twilio Verify or Bird) only for recovery; keep volume tiny.

## Consequences
Low cost; more SMS later only if a market needs it.

**Related:** TK-4.
