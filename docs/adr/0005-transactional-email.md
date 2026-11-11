# ADR 0005: Transactional email: EU-based provider

**Status:** Proposed (verify at sign-up) · **Date:** 11 Nov 2026

## Context
Sign-in codes, report alerts, replies and order emails. Personal data must stay in the EU where possible. Research (11 Nov 2026): Resend can send from Ireland but stores account data in the US.

## Options
| Option | For | Against |
|---|---|---|
| EU-based provider, e.g. Brevo (France) or Scaleway Transactional Email (France) | Data processed and stored in the EU; SMTP for Supabase Auth plus API for our own emails. | Check deliverability, inbound email for replies, and pricing. |
| Twilio SendGrid with EU data residency | Mature, inbound parse for replies. | EU residency tied to plan; US parent. |
| Resend | Excellent developer experience. | Account data stored in the US. Lawful under GDPR with the EU-US Data Privacy Framework or standard contractual clauses, but not our preference (see Note). |

## Note on the EU requirement
GDPR does not require data to stay in the EU; it allows transfers with safeguards (adequacy decisions such as the EU-US Data Privacy Framework, or standard contractual clauses). Keeping data in the EU is Tagkin's own choice: privacy is the product, it simplifies compliance, and it avoids risk if a transfer framework is struck down again (as Privacy Shield was in 2020).

## Decision
Choose an EU-based provider (shortlist Brevo, Scaleway TEM) that supports custom SMTP for Supabase Auth and inbound email for finder replies. Decide after a deliverability test.

## Consequences
Inbound email lets finders reply to relay emails without an account.

**Related:** TK-1, TK-15, TK-55, TK-71.
