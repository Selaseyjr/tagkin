# Architecture decision records

Short records of key technical choices: the context, the options compared, the decision and its consequences. Status: Accepted, or Proposed (decided after a practical check). Step 6 of the product owner flow.

| ADR | Decision | Status |
|---|---|---|
| [0001](0001-mobile-app.md) | Mobile app: React Native with Expo | Accepted |
| [0002](0002-web.md) | Web: Next.js on Vercel (Frankfurt) | Accepted |
| [0003](0003-backend-database-auth-and-storage.md) | Backend, database, auth and storage: Supabase in Frankfurt | Accepted |
| [0004](0004-payments.md) | Payments: Stripe | Accepted |
| [0005](0005-transactional-email.md) | Transactional email: Brevo | Accepted (deliverability test after the domain) |
| [0006](0006-sms-for-account-recovery.md) | SMS for account recovery: Bird via Supabase | Accepted |
| [0007](0007-translation.md) | Translation: DeepL, with a fallback | Accepted |
| [0008](0008-places-and-maps.md) | Places and maps: Google Places (New) | Accepted |
| [0009](0009-push-notifications.md) | Push notifications: Expo push service | Accepted |
| [0010](0010-print-partner.md) | Print partner: decide after samples | Proposed |
| [0011](0011-repository-and-delivery-setup.md) | Repository and delivery setup | Accepted |
| [0012](0012-analytics-and-monitoring.md) | Analytics and error tracking: PostHog EU and Sentry EU | Accepted |
| [0013](0013-frontend-libraries.md) | Frontend libraries shared by web and app | Accepted |
| [0014](0014-testing-and-release-practice.md) | Testing and release practice | Accepted |
