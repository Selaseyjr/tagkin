# Tagkin: roadmap to the App Store and Google Play

Every open item, grouped by the stage where it belongs. Each item says **when** it comes into the workflow. Tick items here and log decisions in PRODUCT-BRIEF.md.

Target: a fully working live app on the App Store and Google Play. Owners use the app; finders use the web (no install).

## Stage A · Design completion (done 11 Nov 2026)

Trigger: start now. The Figma import and Community publish wait until this stage is done.

- [x] Activate a printed tag: scan the QR on a new tag to link it to the account (registration entry point)
- [x] Delete account inside the app (Apple and Google requirement)
- [x] Permission explainers before camera and notifications (photos use the system picker, which needs no permission; location is asked on the finder web page)
- [x] First launch: 2 to 3 intro screens and terms acceptance
- [x] Empty states: no tags, no messages, no orders
- [x] Error states: offline, failed payment, failed send, tag code not found
- [x] Tag management: edit finder message, edit contacts, scan history, retire tag with confirmation, locked fields during Lost mode or a return
- [x] Travel tag: trip fields (destination or hotel, operator, dates) and its finder page; trip details expire
- [x] Pet tag: temperament and care notes, and its finder page
- [x] Report and block flow with moderation, for both owner and finder (Apple guideline on user content)
- [x] Account sub-screens: plan, contacts and backup contact, notifications, language, privacy and data (export, delete)
- [x] App icon (1024 px) from the D2 mark, and splash screen
- [x] Re-run contrast and overflow checks on all new screens

## Stage B · Figma import and Community publish

Trigger: Stage A done. **Reached 11 Nov 2026.**

- [ ] One import of docs/design/tagkin-screens.html with generate_figma_design (exempt from the MCP limit)
- [ ] Selasey adds prototype links by hand in Figma
- [ ] Selasey publishes to Figma Community
- [ ] Optional: short "work in progress" portfolio post

## Stage C · Decisions before building

Trigger: right after Stage B, before any app code.

- [ ] Tech stack. Recommended: React Native with Expo (one codebase for iPhone and Android), a backend (brief suggests Cloudflare Workers, D1, R2), and the finder website
- [ ] Authentication provider for email one-time codes
- [ ] Payments split: printed tags through Stripe or the print partner; Premium subscription through Apple and Google in-app purchase (they take 15 to 30 percent)
- [ ] Print partner (Printful, Printify or Gelato: stickers, keychains, pet tags, shipping to Europe and Ghana)
- [ ] Translation provider (Google, DeepL or an AI model; check prices)
- [ ] SMS provider for phone replies, and in which markets
- [ ] Places search provider for location suggestions
- [ ] Message retention period (screens show 90 days as a sample)
- [ ] Final prices for tags and Premium

## Stage D · Build

Trigger: Stage C decided.

- [ ] Project setup, environments, CI
- [ ] Turn tokens.css into the app theme
- [ ] Finder website (scan page, code entry, report flow, replies)
- [ ] Owner app, flow by flow: auth, registration and activation, tags, Lost mode, messages, orders, account
- [ ] Message relay (email and SMS), translation both ways, phone and email detection (libphonenumber-js)
- [ ] Push notifications for scans and messages
- [ ] Ordering through the print partner, and Premium in-app purchase
- [ ] Modern motion: screen transitions, micro-interactions, haptics (noted after the finder test)
- [ ] Accessibility: screen readers, dynamic text size, contrast
- [ ] Data retention jobs; retired tags keep no personal data
- [ ] Analytics without selling data (only what the privacy labels declare)

## Stage E · Legal and compliance

Trigger: start drafting during Stage D; must be final before Stage F.

- [ ] Privacy policy and terms of use (in the app and store listings)
- [ ] Impressum (German law)
- [ ] GDPR: consent for location, export and deletion, records of processing
- [ ] Data processing agreements with every provider (email, SMS, translation, print, payment, hosting)
- [ ] Apple privacy labels and Google Data safety form, matching the app exactly
- [ ] Age rating questionnaires
- [ ] Image search on the logo against registered marks

## Stage F · Store launch

Trigger: Stages D and E done, app tested on real devices.

- [ ] Buy tagkin.app (planned around 14 Nov 2026; needed before printing real tags)
- [ ] Apple Developer account ($99 a year) and Google Play Console ($25 once)
- [ ] Store listings: name, subtitle, description, keywords, screenshots, preview video
- [ ] TestFlight and Google internal testing with the earlier testers
- [ ] Review account and notes for Apple and Google reviewers
- [ ] Submit, fix review feedback, release

## Stage G · After launch

Trigger: live in both stores.

- [ ] Measure: tags registered, scans, items returned, registration drop-off
- [ ] Polished case study with real results
- [ ] Figma v2 import if the design changed (the import tool is exempt)
- [ ] Phase 2: Care tags (children, older relatives), with extra safety and legal review
- [ ] Later channels: WhatsApp, SMS-only finders, NFC tags, family sharing
