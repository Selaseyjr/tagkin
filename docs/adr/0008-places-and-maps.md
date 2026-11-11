# ADR 0008: Places and maps

**Status:** Proposed · **Date:** 11 Nov 2026

## Context
Finders get place suggestions and an address from a shared location; owners see a map pin.

## Options
| Option | For | Against |
|---|---|---|
| Google Places Autocomplete and Geocoding | Best place data, including stations and shops. | Cost per session; use session tokens. |
| Mapbox Search and Geocoding | Good price, nice maps. | Place data weaker for small venues. |

## Decision
Start with Google Places (session tokens, field masks to limit cost) and reverse geocoding; open the owner's map app for directions instead of embedding heavy maps.

## Consequences
Keep calls to the finder flow only; free text always works if the API fails.

**Related:** TK-12, TK-13, TK-42.
