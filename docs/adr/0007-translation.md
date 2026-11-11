# ADR 0007: Translation: DeepL, with a fallback

**Status:** Accepted · **Date:** 11 Nov 2026

## Context
Owner messages and chat are translated both ways. Core languages are European; owners and finders may use others (for example Twi).

## Options
| Option | For | Against |
|---|---|---|
| DeepL API | High quality for European languages; EU company; 100+ languages. | Not every language (check Twi and others). |
| Google Cloud Translation | Widest coverage. | Lower quality for some European pairs. |
| LLM translation | Flexible tone. | Cost and consistency. |

## Decision
Use DeepL for supported pairs; fall back to Google Cloud Translation for languages DeepL lacks; cache owner messages per language; always keep the original.

## Consequences
Lower cost through caching; consistent quality in core markets.

**Related:** TK-10, TK-41, TK-92.
