# Tagkin: system logic for engineers

How Tagkin behaves underneath the screens: data, states, events, providers and failure handling. Read with BUSINESS-RULES.md (what must be true) and docs/design/tagkin-screens.html (what users see; each screen has a note). Where this document and the screens disagree, raise it; don't guess.

Version 1 · 11 Nov 2026 · written from a full user walk-through of every journey, including the moments a provider handles.

## 1. Parts of the system

| Part | Users | Notes |
|---|---|---|
| **Finder web** (tagkin.app/TK-…) | Finders, no account | Mobile-first web page. Report, photo, location, replies, handover check. Never requires an app. |
| **Owner app** (iOS, Android) | Owners | One codebase (recommended: React Native with Expo). |
| **Owner web** (tagkin.app/signin, /my-tags) | Owners | Same account. Needed when the lost item is the phone. Lost mode, messages, tags, account. |
| **Website** (tagkin.app, /privacy, /support, /shop later) | Everyone | Required by the stores (privacy and support URLs). |
| **Backend API** | All of the above | Accounts, tags, scans, reports, relay, orders, notifications, jobs. |
| **Admin** | Selasey | Reports and moderation, orders, refunds, recovery requests. Minimal at launch. |

## 2. Data model (entities and key fields)

| Entity | Key fields | Notes |
|---|---|---|
| **Account** | id, email (required, unique, verified), recovery_phone?, backup_email?, language, appearance, notification prefs, created_at, deleted_at | Email is the sign-in. |
| **Session / Device** | id, account_id, platform, push_token?, last_seen | Listed in Sign-in and recovery; can be signed out remotely. |
| **Tag** | code (TK-XXXX-XXXX), owner_account_id?, state, product (sticker, keychain, pet_tag, luggage_label, lock_screen), colour, type (item, travel, pet), is_free, activation_pin_hash?, created_at, retired_at | Code alphabet excludes 0 O 1 I L. Never reused. |
| **Item** (the belonging) | tag_code, name, photo_url?, description?, finder_message (≤160), finder_message_lang, care_notes? (pet), temperament? (pet), trip? (travel: mode, operator, destination, dates) | One item per tag. Name, photo and description lock in Lost and Return states. |
| **Contact** | account_id, kind (backup_person), name, email/phone, alert_after_minutes | Never shown to finders. |
| **Status update** | tag_code, text (city level), visible, expires_at | No dates or times in text (validated). |
| **Scan** | id, tag_code, at, city (from IP), is_test, user_agent_class | Exact location never from a scan alone. |
| **Report** (finder) | id, tag_code, where_now (with_me, staff, safe_place), place_text?, lat/lng? (only if shared), address?, photo_url? (EXIF removed), note?, finder_contact_kind (email, phone, none), finder_contact (encrypted)?, lang, created_at | Creates or joins a Return. |
| **Return** (thread) | id, tag_code, state, opened_at, closed_at, handover_code_hash | Relay messages live here. |
| **Message** | id, return_id, from (owner, finder, system), text, original_text, original_lang, translated_lang, delivered_via (push, email, sms, web), status (sent, failed, delivered) | Contact details in text trigger the share warning before sending. |
| **Order** | id, account_id, kind (own, gift), items[], shipping_address, recipient_name?, gift_note?, hide_prices, subtotal, shipping, discount, total, currency, payment_method, stripe_payment_id, partner_order_id, state, tracking_url? | Own orders link tag codes at payment; gift orders create unclaimed codes. |
| **Order item** | product, colour, copies, tag_code (own) or tag_codes[] (gift), unit_price | Copies = same code printed n times. |
| **Abuse report / block** | reporter, target (message, tag, finder thread), reason, state | Reviewed by admin. |

## 3. State machines

**Tag**

```
unclaimed ──activate (code + PIN)──▶ normal
(created on order, own) ───────────▶ normal
normal ──owner: mark lost──▶ lost ──owner: found it myself──▶ normal
normal|lost ──finder report──▶ return_active ──owner: returned | 14 days silent──▶ normal
any ──owner: retire | account deleted──▶ retired (final)
```
- `lost` and `return_active` lock name, photo, description.
- `retired`: finder page shows "This tag is no longer active"; no owner data.
- Test mode is a flag (10 minutes), not a state: scans are marked `is_test`, no alerts.

**Return**: `open` → (`handed_over` via handover code, optional) → `closed` (owner marks returned, or 14 days without messages).

**Order**: `pending_payment` → `paid` → `sent_to_partner` → `in_production` → `shipped` → `delivered`. Branches: `payment_failed` (retry), `partner_failed` (admin; refund), `cancelled` (before production only), `refunded`. Own-order tags go live at `paid`.

**Activation (unclaimed tag)**: scan or code → tag found and unclaimed → PIN (5 attempts, then 15-minute wait) → owner chooses type, details, message → `normal`. Wrong PIN never reveals whether a code exists beyond "unclaimed".

## 4. Events and who hears about them

| Event | Owner | Finder | Backup contact | Notes |
|---|---|---|---|---|
| Sign-in requested | Email code (10 min, 5 tries) | | | Recovery: SMS code to recovery phone, or backup email. |
| Tag scanned (normal) | Push "scanned near {city}" (if enabled) | | | Not in test mode. |
| Tag scanned (lost) | Push every scan, city | | | Can't be turned off while lost. |
| Finder report | Push + email, translated | Thank-you page | After `alert_after_minutes` without owner reply: email (SMS later) | Report starts or joins a Return. |
| Owner reply | | Live on page if open; else email or SMS (as chosen); anonymous: page only | | Translated both ways; original kept. |
| Finder reply | Push + email | | | |
| No owner reply after the wait (suggest 2 h) | Reminder push | Page offers staff handover | Alert | Wait time decided in Stage C. |
| Order paid | Email: order confirmed | | | Gift: buyer only. |
| Order shipped | Email: tracking | | | Gift: buyer only, recipient never emailed by us. |
| Payment failed | In-app error, retry | | | Stripe decline reason shown in plain words. |
| Account deletion | Email confirmation | | | Tags retired; invoices kept as the law requires. |
| Data export | Email with download link (24 h) | | | |

Push falls back to email when push is off or the token is invalid. Every email has a footer with settings, privacy and Impressum.

## 5. Providers and what happens when they fail

| Moment | Provider (to choose in Stage C) | Normal path | If it fails |
|---|---|---|---|
| Sign-in code | Transactional email (e.g. Postmark, Resend) | Code arrives within a minute | "Not there? Check spam or use a different email"; resend after 30 s; recovery phone. |
| Recovery code | SMS (e.g. Twilio, MessageBird) | Used only for account recovery at launch | Backup email; support with an order number. |
| Payment | Stripe (Apple Pay, Google Pay, card, PayPal, Klarna) | Payment sheet, 3-D Secure if needed, webhook confirms | Decline: error screen, card not charged. Webhook missing: order stays `pending_payment`, reconcile job checks Stripe. |
| Printing and shipping | Print-on-demand partner API | Order sent after `paid`; status and tracking by webhook | Partner rejects: admin alert, customer email, refund in Stripe. |
| Translation | Translation API (Google, DeepL or AI) | Owner message translated once per language and cached; chat translated per message | Show the original with "Translation unavailable". |
| Place suggestions | Places API (Google, Mapbox) | Suggestions after 2 letters | Free text still accepted. |
| Exact location | Browser geolocation (finder's consent) + reverse geocoding | Pin and address | Permission denied: city only, note shown; address field editable. |
| City from scan | IP geolocation | City stored with each scan | Unknown: "Location unknown". |
| Photos | Object storage (Cloudflare R2) | Upload, EXIF stripped server-side, resized | Upload fails: retry; report can be sent without the photo. |
| Push | APNs and FCM | Alert in seconds of the event | Fallback to email. |
| Phone number and email detection | libphonenumber-js | Share warning before sending | Regex fallback for email. |

## 6. Validation and limits

- Finder message, gift note: 1–160 characters; contact details → public warning; abusive words → blocked with a reason.
- Status update: ≤60 characters; reject dates and times (pattern check) with a friendly message.
- Names ≤40, descriptions ≤200, care notes ≤300, chat messages ≤1,000.
- Tag code input: case- and dash-insensitive; rate limit code lookups per IP (e.g. 20 per hour) and globally.
- Activation PIN: 6 characters, hashed; 5 attempts per tag per 15 minutes.
- Handover code: 6 digits, per return, owner can regenerate.
- Email code: 6 digits, 10 minutes, 5 attempts, then wait.
- Photo: JPEG, PNG or HEIC, ≤10 MB, EXIF removed.
- Shipping: free over €15 (configurable). First-tag offer: once per account.
- Emoji allowed in every free-text field (owner and finder); counts use characters, not bytes.

## 7. Scheduled jobs

| Job | Frequency | Does |
|---|---|---|
| Close silent returns | Hourly | `return_active` with no message for 14 days → `closed`, tag → `normal`. |
| Backup contact alert | Every 5 min | Finder report without owner reply after the wait → alert backup, update finder page. |
| Expire status updates and trips | Hourly | Hide after trip end or 7 days. |
| End test mode | Every minute | Clear flags older than 10 minutes. |
| Message retention | Daily | Delete messages a set period after a return closes (Stage C decision). |
| Order reconciliation | Every 15 min | Match Stripe and partner states. |
| Data export | On request | Build archive, email link. |

## 8. URLs and deep links

- `tagkin.app/TK-XXXX-XXXX` (printed in the QR): finder page; if the tag is unclaimed, "Not set up yet" with a deep link that opens the app (or the store) with the code prefilled for activation.
- `tagkin.app/TK-…/handover`: handover check for finders and desk staff.
- `tagkin.app/r/{token}`: finder reply link from email (no account).
- `tagkin.app/signin`, `/my-tags`: owner web.
- App deep links: `tagkin://tag/{code}`, `tagkin://activate/{code}`, `tagkin://return/{id}`.

## 9. Legal touchpoints the build must include

- Checkout: personalised goods notice (no 14-day withdrawal; faulty tags replaced free), Terms link, clear pay button with amount.
- Impressum, privacy and terms links on every web page and in the app (Account → Privacy and data).
- Consent before location sharing (finder) and before notifications (owner).
- Account deletion and data export in the app.

## 10. Still to decide (Stage C)

Provider choices above; message retention period; no-reply wait time; final prices and shipping threshold; print partner product list; SMS markets.
