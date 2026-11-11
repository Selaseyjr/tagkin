# ADR 0012: Analytics and error tracking: PostHog EU and Sentry EU

**Status:** Recommended, awaiting approval · **Date:** 11 Nov 2026

## Context
Tagkin must measure its success measures (activation, test scans, conversion, finder completion, owner response, returns, Notify me) across the app and the web, and catch errors in the app, finder pages and server, without profiling people or needing a cookie banner. Research 11 Nov 2026: PostHog Cloud EU runs in Frankfurt (AWS eu-central-1) as a separate instance, with about 1 million free events a month and a React Native SDK. Sentry offers storage in Frankfurt on every plan, including the free Developer plan; some account metadata stays in the US. Plausible is web-only. Both PostHog and Sentry are US-incorporated companies with EU data storage.

## Options
| Option | For | Against |
|---|---|---|
| **PostHog Cloud EU** (analytics) | App and web in one tool; funnels for every success measure; EU storage; generous free tier; can run without cookies on the web | US company (EU-US Data Privacy Framework applies); must be configured carefully to avoid personal data |
| TelemetryDeck (Germany) | EU-owned, privacy-first, built for apps | Weaker web support and funnels for our measures |
| Plausible or Matomo | Simple, cookieless web analytics | Plausible has no app SDK; Matomo heavier, less suited to the app |
| **Sentry with EU storage** (errors) | Best error tracking for React Native and Next.js; Frankfurt storage on the free plan | US company; some metadata in the US; personal data must be scrubbed |
| Bugsink or GlitchTip, self-hosted in the EU | Fully EU | We run and maintain it |

## Decision
Recommend **PostHog Cloud EU** for product analytics and **Sentry (EU data storage, Frankfurt)** for error tracking. Rules:
- Events only for the success measures and key steps, named in a tracking plan; no names, emails, phone numbers, codes, addresses or message text in events.
- Finder pages: anonymous, cookieless events (in-memory persistence), no session recording, no autocapture of text inputs.
- Owner app: pseudonymous account ID only after sign-in; session recording off at launch.
- Sentry: scrub personal data before sending, no request bodies, IP addresses not stored.
- One tool for web analytics (PostHog); no separate website tool at launch.

## Consequences
No cookie banner needed if no tracking cookies are set. Both providers need data processing agreements (Stage E legal review). If a fully EU-owned stack is wanted later, TelemetryDeck and a self-hosted Bugsink are the fallback.

**Related:** TK-94, TK-99, NFR monitoring.
