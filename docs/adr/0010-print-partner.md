# ADR 0010: Print partner: decide after samples

**Status:** Proposed · **Date:** 11 Nov 2026

## Context
Printed tags (sticker, keychain, pet tag, luggage label) and gift cards are made and shipped by a print-on-demand partner with an API, shipping to the EU (and Ghana later).

## Options
| Option | For | Against |
|---|---|---|
| Gelato | Local production in many countries; API. | Check product range for keychains, pet tags and luggage labels. |
| Printful | Wide range; API; EU facilities. | Check engraved metal pet tags. |
| Printify | Many print providers. | Quality varies by provider. |

## Decision
Order samples from at least two partners; score quality, durability, QR scan reliability, cost, delivery time, API and gift card support. Build behind a fulfilment adapter so the partner can change.

## Consequences
Product list and prices are final only after this decision (roadmap reminder A3).

**Related:** TK-53, TK-61.
