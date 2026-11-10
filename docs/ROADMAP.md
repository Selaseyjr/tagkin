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

## Audit fixes (done 11 Nov 2026)

- [x] Free tag = phone lock-screen tag; home printing removed (A1)
- [x] Activation PIN for unclaimed tags (B1)
- [x] Owner sign-in at tagkin.app on any device; email required (B2)
- [x] Account recovery: recovery phone, backup email, signed-in devices (B3)
- [x] No anti-theft, speed or fixed-time promises (B4, E1)
- [x] Free handover code (B6)
- [x] Owner never replies: backup contact alerted, finder offered staff handover (C1)
- [x] Second-tag path ends in ordering; tag live from order (D1, D3)
- [x] Notifications asked after the first tag (D7)
- [x] Packs and free shipping over €15 (A2)

## Reminders (Claude raises these at the trigger)

| When | Reminder |
|---|---|
| **This weekend (by 15 Nov 2026), before Community publish** | Buy tagkin.app (E4). Do not publish the showcase until the domain is owned. |
| **Stage C, before choosing prices** | Confirm every product with print partners: sticker, keychain, pet tag, luggage label, gift card, scratch-panel packs; sizes, colours, costs, shipping (A3). |
| **Stage C** | Decide message retention (suggest 90 days after a return), the no-reply wait time, and the free shipping threshold. |
| **Stage E, before going live** | File the EU trademark for Tagkin and do the logo image search (E5). |
| **Stage F, before submitting** | Re-shoot store screenshots with the real app; recheck all copy against the copy rules. |

## Stage B · Figma import and Community publish

Trigger: Stage A done. **Reached 11 Nov 2026.**

- [x] Hand-off page complete: cover, flow map, screen notes, states, emails, desktop finder, website, marketing visuals
- [x] Pre-import audit done: codes, legal footer, sign-in email, print artwork, exports, permission recovery, languages, accessibility, Android icon, showcase
- [ ] Import two pages: docs/design/tagkin-screens.html (private hand-off file) and docs/design/tagkin-showcase.html (public Community file). One import each with generate_figma_design (exempt from the MCP limit)
- [ ] Selasey adds prototype links by hand in Figma for the finder flow (about 9 screens); the cover links to the full prototypes
- [ ] Selasey publishes to Figma Community
- [ ] Optional: short "work in progress" portfolio post

## Stage C · Decisions before building

Trigger: right after Stage B, before any app code.

- [ ] Tech stack. Recommended: React Native with Expo (one codebase for iPhone and Android), a backend (brief suggests Cloudflare Workers, D1, R2), and the finder website
- [ ] Authentication provider for email one-time codes
- [ ] Payments: printed tags through Stripe or the print partner. No Premium at launch; when it comes, it goes through Apple and Google in-app purchase (15 percent in their small business programmes)
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
- [ ] Store listings: name, subtitle, description, keywords, preview video; re-shoot the 5 screenshot concepts (docs/design) with the real app
- [ ] TestFlight and Google internal testing with the earlier testers
- [ ] Review account and notes for Apple and Google reviewers
- [ ] Submit, fix review feedback, release

## Stage G · After launch

Trigger: live in both stores.

- [ ] Measure: tags registered, scans, items returned, registration drop-off
- [ ] Polished case study with real results
- [ ] Figma v2 import if the design changed (the import tool is exempt)
- [ ] Premium: pick from the ideas in the brief (vault, Stolen mode, verified handover, courier return, household) based on Notify me demand
- [ ] Phase 2: Care tags (children, older relatives), with extra safety and legal review
- [ ] Later channels: WhatsApp, SMS-only finders, NFC tags, family sharing
- [x] Gift a tag designed: For me / Gift a tag in ordering, gift note, delivery to recipient, link on Tag is live, finder page for an unclaimed tag
- [ ] Price ready-made packs against single in-app tags (same price per tag in every channel)
- [x] Invite a friend: designed in Account (share link)
- [ ] First printed tag offer at checkout (decide amount)
- [ ] Ready-made tags for shops and gift packs (pre-printed blank codes, activated by scan; the screens already exist)
