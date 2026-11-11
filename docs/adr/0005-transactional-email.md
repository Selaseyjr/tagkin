# ADR 0005: Transactional email: EU-based provider

**Status:** Recommended, awaiting approval · **Date:** 11 Nov 2026

## Context
Sign-in codes, report alerts, replies and order emails, plus **inbound** email so finders can reply to relay emails without an account. Tagkin prefers EU storage (a choice, not a GDPR requirement: transfers are lawful with an adequacy decision such as the EU-US Data Privacy Framework, or standard contractual clauses). Research 11 Nov 2026: Resend sends from Ireland but stores account data in the US; Scaleway Transactional Email is outbound-only (no inbound); Brevo offers inbound parsing to a webhook.

## Options
| Option | For | Against |
|---|---|---|
| Brevo (France) | EU company; transactional API and SMTP (works as Supabase Auth's custom SMTP); **inbound parsing** to a webhook for finder replies; free tier for testing. | Inbound parsing can't guarantee 100% success, so the finder page stays the main reply path; deliverability to be tested. |
| Scaleway Transactional Email (France) | EU, simple, cheap. | **No inbound email**: would need a second provider for replies. |
| Twilio SendGrid with EU data residency | Mature; inbound parse. | EU residency depends on plan; US parent. |
| Resend | Excellent developer experience. | Account data stored in the US; not our preference. |

## Decision
**Recommend Brevo** as the single email provider: outbound (Supabase Auth SMTP and our own emails) and inbound parsing for finder replies. Test after tagkin.app is bought (sending and inbound both need a verified domain with SPF, DKIM and DMARC).

## Consequences
One EU provider for both directions. Scaleway is no longer needed. Before launch: data processing agreement with Brevo (Stage E legal review).

**Related:** TK-1, TK-15, TK-55, TK-71.
