# ADR 0006: SMS for account recovery: Bird via Supabase

**Status:** Accepted (approved by Selasey, 11 Nov 2026) · **Date:** 11 Nov 2026

## Context
At launch SMS sends account recovery codes only, so volume is tiny (estimate: a few per month). Supabase Auth has built-in phone sign-in providers, including Twilio, Twilio Verify, MessageBird and Vonage (to confirm when setting up). Research 11 Nov 2026: Twilio Verify charges about $0.05 per successful verification plus the SMS to Germany (sources range from about $0.025 to $0.11), so roughly $0.08 to $0.16 each; Bird Verify has no verification fee and charges only the SMS at the destination's rate; Bird is a Dutch (EU) company.

## Options
| Option | For | Against |
|---|---|---|
| Bird (MessageBird) via Supabase's built-in provider | EU company; no verify fee, pay per SMS; little code, since Supabase handles sending and checking the code. | Country SMS rates not published as one table; check in the dashboard. |
| Twilio Verify via Supabase | Most mature; fraud protection built in. | US company; verify fee on top of SMS. |
| Sinch (Sweden) or Infobip (Croatia) | EU companies; EU routing options. | Not a Supabase built-in provider: more code. |

## Decision
**Recommend Bird through Supabase's built-in phone provider**, used only for recovery codes. Twilio Verify is the fallback if Bird delivery to key countries (Germany, Ghana) proves unreliable in testing.

## Consequences
Cost negligible at launch volume. Rate-limit recovery attempts. Data processing agreement at Stage E.

**Related:** TK-4.
