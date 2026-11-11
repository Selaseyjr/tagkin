# ADR 0004: Payments: Stripe

**Status:** Accepted · **Date:** 11 Nov 2026

## Context
Printed tags are physical goods, so they may be paid outside Apple and Google in-app purchase. Customers expect Apple Pay or Google Pay, cards, PayPal and Klarna in Germany.

## Options
| Option | For | Against |
|---|---|---|
| Stripe (Payment Sheet in the app, Payment Element on the web) | One integration for Apple Pay, Google Pay, cards, PayPal and Klarna in Germany; strong 3-D Secure handling; webhooks; EU entity. | Per-transaction fees; PayPal and Klarna need enabling and approval in the dashboard. |
| PayPal Braintree | PayPal native. | Weaker fit for Klarna and the overall stack. |
| Mollie | Strong in the EU, EU company. | Smaller React Native ecosystem. |

## Decision
Use Stripe. Tagkin is the merchant of record; the print partner bills Tagkin. No in-app purchase at launch (no digital goods sold).

## Consequences
Order state driven by Stripe webhooks; reconciliation job as a safety net.

**Related:** E5 Ordering and payment (TK-50 to TK-55), E6 gifting (TK-60).
