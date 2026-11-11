# ADR 0008: Places and maps: Google Places (New)

**Status:** Accepted (approved by Selasey, 11 Nov 2026) · **Date:** 11 Nov 2026

## Context
Finders type a place (stations, cafés, shops) and can share the item location, which becomes an address; owners open the spot in their map app. Research 11 Nov 2026: Google Places Autocomplete (New) is free within a session when the session ends with a Place Details call (otherwise the first 12 requests are billed); each SKU has a free monthly cap (Autocomplete requests 10,000; Essentials SKUs about 10,000), replacing the old $200 credit since March 2025. Mapbox Search Box offers about 500 to 2,500 free sessions a month depending on the plan, then a few dollars per 1,000; its data for small venues is weaker.

## Options
| Option | For | Against |
|---|---|---|
| Google Places (New) Autocomplete + Place Details + Geocoding | Best coverage of stations, shops and cafés, which is exactly what finders type; session pricing makes typing free; generous free caps per SKU. | US provider (transfer basis: EU-US Data Privacy Framework); billing must be capped. |
| Mapbox Search Box and Geocoding | Good prices; nice maps. | Weaker venue data; fewer free sessions. |
| Open data (Photon or Nominatim on OpenStreetMap, self-hosted in the EU) | EU-hosted, no per-call cost. | Weaker autocomplete for venues; we would run and maintain it. |

## Decision
**Recommend Google Places (New)**, called only from our server: session tokens on every autocomplete, end each session with a Place Details call using the narrowest field mask, reverse geocoding only when the finder shares location. Set billing alerts and daily quota caps. No embedded maps; 'Open in Maps' hands off to the owner's map app.

## Consequences
Expected MVP cost close to zero within free caps. Only typed text and finder-consented coordinates are sent; no account data. Free-text input always works if the API is down.

**Related:** TK-12, TK-13, TK-42.
