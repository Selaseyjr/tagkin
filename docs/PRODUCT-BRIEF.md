# Tagkin: product brief

Name: Tagkin (chosen 8 Nov 2026; EUIPO and USPTO searches clear; buy tagkin.app before launch). Owner: Selasey Gbeddy. Started 8 Nov 2026. This file is the single source of truth: every decision goes here as it is made.

## 1. The idea in one line

A QR tag for your belongings, pets and loved ones. Anyone who finds them can reach you in seconds, and nobody's private details are shown.

## 2. Principles

- **Private by default.** Neither owner nor finder sees the other's contact unless they choose to share it.
- **Ten seconds for the finder.** No app, no sign-up, no stress.
- **Universal.** Works in any country, any language, any phone.
- **One tag, one thing.** A tag ID is permanent and never reused.
- **Safe for people.** Care tags show the minimum, and every scan alerts the guardian.

## 3. Tag types

Type is chosen at registration and **locked** afterwards.

| Type | Purpose | Finder page focus |
|---|---|---|
| **Item** | Return | "Please help me get back to my owner" |
| **Travel** | Return during a journey (plane, train, bus, ferry, taxi or ride, hotel) | Destination or hotel, operator, "hand to staff or message the owner". Trip details expire after the travel dates |
| **Pet** | Help and return | Name, temperament, care notes, "please call my owner" |
| **Care (child or older relative)** | Help, not return | "I may need help. Please contact my guardian." Minimal info; emergency details behind a tap; every view logged and alerts the guardian |

**Out of scope:** professional identification of students, patients or clients by teachers, doctors, vets or carers. That is a different, regulated product (medical and child-safety law), and a public tag with full identity details is a safety risk.

## 4. Owner-written finder message

- **Templates per type.** The owner picks one, or writes their own.
  - Item: "Found me? Thank you! Tap below to tell my owner where I am."
  - Travel: "I'm travelling to [destination]. Please hand me to staff or message my owner."
  - Pet: "Hi, I'm [name]. I'm friendly. Please message my owner. I may be scared."
  - Care: "I may need help. Please contact my guardian using the button below."
- **Custom text.** Up to 160 characters, with a live preview.
- **Safety checks on custom text.** A warning if it contains a phone number, email or address ("This will be public to anyone who scans"). A block on abusive words.
- **Translation.** The message is shown in the finder's language, with the original one tap away.

## 5. Finder flow

1. Scan the QR (or type the short code on the website).
2. See the owner's message and optional photo.
3. **Where is it now?** With me · Handed to staff · Left where I found it.
4. **Where exactly?** One field ("Input location here") with place suggestions as the finder types, plus a **Share item location** button.
5. **Anything else?** Optional note, prompted with examples (who the item was left with, exact landmark).
6. **Want a reply?** Optional email or phone number, kept hidden and relayed. Otherwise anonymous: "Without an email or phone number, keep this page open to receive replies."
7. Thank-you screen.

## 6. Privacy in the interface

- Owner setup: "Your contact is never shown. Finders message you through Tagkin."
- Finder page: "🔒 Your details stay private unless you choose to share them."
- Message box: "Only add your number or email if you want the owner to contact you directly."
- Phone or email detected in a message: "This will share your number with the owner. Continue?"
- Messages are relayed: neither side sees the other's email or number.
- One short, plain privacy page.

Phone detection: **libphonenumber-js** (open-source port of Google's libphonenumber) finds phone numbers in free text for any country. A simple pattern catches emails.

## 7. Editing rules

| Locked forever | Locked during Lost mode or an active return | Always editable |
|---|---|---|
| Tag ID and QR link | Item name, photo, description | Contacts, names, numbers |
| Tag type | | Emergency and medical notes |
| | | Finder message, language, Lost mode, tag on or off |

- Edit history is visible to the finder ("Photo updated 3 days ago").
- The QR code holds only a permanent link with the tag ID, so details change without reprinting.

## 8. Lost mode

Owner taps **Lost**. The finder page turns urgent: "This item is missing", with photo and a clear call to action. Scans show time and place. **No public reward amount** (it could invite theft); the owner can thank or reward privately after the return.

## 9. Short code and channels

| Channel | Solves | Needs internet | Phase |
|---|---|---|---|
| QR scan | Normal case | Yes | MVP |
| Website code (e.g. FND-4821) | Damaged QR, camera trouble | Yes | MVP |
| WhatsApp | People who prefer WhatsApp | Yes | Later |
| SMS | No data at all | **No** | Later, starting in markets that need it |

## 10. Tag IDs and monetisation

- Each tag ID is random, at least 8 characters, unguessable and **never reused**.
- A tag belongs to one item. If the item is gone, the owner **retires** the tag; the ID stays dead.
- **No own printing company needed.** Recommended order:
  1. **Print on demand (main revenue):** orders go through Tagkin; a print-on-demand partner prints and ships under our brand; we set the price and keep the margin. Candidates to check: Printful, Printify, Gelato (sticker and keychain support, API, shipping to Europe and Ghana).
  2. **Affiliate links (quick start):** link to a printer with a referral programme and earn a commission per order. Lower income, zero stock.
  3. **Wholesale NFC or QR tags later:** buy blank tags in bulk, sell activated tags when volume justifies it.
- **Digital tags** (phone lock screen, digital card) are free and count towards the free limit of 3 tags. Premium (later): unlimited tags, SMS fallback, family sharing, extra contacts.
- Never sell or share user data. Privacy is the product.

## 11. Tag design and preview

- A **live preview** step in registration: the QR code inside a frame with the chosen line underneath ("Found me? Scan to return", or custom).
- 4 to 6 styles (rounded sticker, keychain, pet tag, luggage label), a few colour themes, the item's icon.
- QR stays high contrast and scannable whatever the style.
- **Every tag prints the address and code under the QR** (e.g. tagkin.app · FND-4821), whatever the style. It is the only way in when the QR will not scan or the finder's camera cannot read QR codes.
- Download as PNG or PDF, or **Order this tag** through a print partner (to be confirmed; check which services accept an uploaded design and offer partner links).

## 12. Translation

- Pages appear in the phone's language; a picker covers 100+ languages.
- Messages are translated both ways, with "show original".
- Service: Google Cloud Translation, DeepL or an AI model. Check current prices before choosing.

## 13. More additions agreed in principle

- Owner verification before handover (a question only the real owner can answer).
- Safe meeting point suggestions (staff desks, shops, police).
- Backup contact if the owner does not reply within a set time.
- Report abuse on any message or tag.
- Scan alerts and a simple scan history per tag.
- Accessibility: large text, high contrast, works with screen readers.
- Data retention: messages deleted after a set period; retired tags keep no personal data.

## 14. Open decisions

- [x] Name: **Tagkin** (chosen 8 Nov). Trademark search on EUIPO and USPTO: no results (8 Nov). Earlier shortlist: Shortlist (8 Nov, .com all taken; .app looked unregistered in a quick DNS check, not confirmed): Tagkin, Kindtag, Hellotag, Homingtag, Findmeback, Lostless, Tagback. Check trademarks and app stores before choosing. 8 Nov: Hellotag rejected (HelloTag app by Hellotag Corporation, France, already on the App Store). Tagkin: no app or product found in a web search; trademark search still to do.
- [x] MVP scope: Item, Travel and Pet. Care tags in phase 2 (8 Nov).
- [x] Flow decisions (8 Nov): sign-in by email one-time code, no passwords. A return ends when the owner marks Returned, or after 14 days with no messages. Owner verification before handover comes after the MVP. Anonymous finders see replies only while the thank-you page is open, with a gentle nudge to leave an email. Scan location is city level unless the finder shares exact location.
- [x] Wireframe method (8 Nov): static HTML wireframes in docs/wireframes/ (screens side by side, not yet clickable); Figma for the final UI once the plan allows.
- [ ] Budget: buy tagkin.app and consider Figma Professional around 14 Nov 2026, when funds allow.
- [x] Logo (10 Nov): **D2**, a solid tag with the hole and a lowercase k cut out, next to the lowercase wordmark "tagkin". Master file docs/brand/tagkin-mark.svg. Colour, final type and a trademark image search still to do.
- [x] Design-to-Figma plan (10 Nov): all design is finished in HTML first (tokens, components, every screen, clickable prototype, tested). Then one combined page is imported into Figma with generate_figma_design, which Figma lists as exempt from the MCP limit (Starter View seat: 20 counted calls a month; reset date not published). Prototype links, Community publishing and tidy-up are done by hand in Figma, which needs no tool calls. The HTML tokens and components become the starting code for the app.
- [x] Visual design pass A (10 Nov): tokens in docs/brand/tokens.css, previewed in docs/brand/design-system.html. Palette **Fresh mint** (chosen 11 Nov over Signal blue and Tag yellow, after the first green was judged dull): mint #00C48C for fills with dark text on it, #007A57 for mint text and links (dark mode #1FE0A6); red #E02A17 only for Lost mode; amber only for privacy warnings; clean neutrals with a faint mint tint. Type: Bricolage Grotesque for titles, Inter for body; inputs at least 16 px. 4-point spacing; radius 8 / 14 / 22; controls at least 52 px tall. All text and colour pairs pass WCAG AA (4.5:1) in light and dark. Components: buttons, input, choice, status badges, notes, privacy line, Lost banner, message bubbles, tag list item, printed tag.
- [x] Visual design pass B (11 Nov): all 25 MVP screens styled on one page, docs/design/tagkin-screens.html, generated by docs/design/build_screens.py from tokens.css. This page is what gets imported into Figma once.
- [x] Tag ordering in the owner flow (11 Nov): after a tag goes live (and from tag detail), the owner can order it printed: choose sticker, keychain or pet tag and a quantity, then check and pay. Payment is handed to the print partner; Tagkin never sees card details. Prices are samples until the partner is chosen. Clickable owner prototype: docs/design/owner-prototype.html, generated with the screens page.
- [x] Owner app navigation (11 Nov): bottom tab bar with My tags, Messages, Orders, Account. Account holds plan and subscription (Premium later), contacts and backup contact, notifications, language, privacy and data, help and sign out. Settings live inside Account rather than as a separate icon.
- [x] Target (11 Nov): a fully functional live app on the Apple App Store and Google Play, built to their review standards. Finders stay on the web (no app needed); owners use the app.
- [ ] Print partner
- [ ] Translation provider
- [ ] Tech stack (recommended: Cloudflare Pages, Workers, D1, R2 for photos)

## 14b. Competitors to beat

Similar QR lost-and-found tags already exist: Tile Lost and Found labels, PingTag (anonymous messaging), LostTags, MyTags, HeyOwner, Animal ID pet tags. Our edge must be clear: owner-written finder messages, Care and Travel modes, translation in both directions, editing rules with lock during returns, and beautiful tags.

## 15. Validation

Nov 2026: Selasey spoke with 3 people about losing and returning belongings. Combined themes below, summarised by Selasey after the conversations; not verbatim quotes, and not split by person.

| Theme raised | What it changed |
|---|---|
| Finders also want privacy, not only owners | Relayed messages; finder details hidden unless shared; warning when a number is typed |
| A public reward could tempt people to take things | No reward amount on the tag; owner thanks privately |
| "I have it" is not enough to find the item | Three short steps: status, exact place with location, optional note |
| Details change after a tag is printed | Permanent QR link; contacts and notes always editable |
| Editing a photo mid-return could confuse or mislead | Name, photo and description locked during Lost mode or a return; visible edit history |
| Luggage travels by train, bus, ferry and taxi too | Travel mode for every transport type; trip details expire |
| Pets and people need help, not "return me" | Pet and Care tags with their own messages |
| Owners want to choose what the finder reads | Templates per type plus custom text with preview |
| Cutting out printed tags is messy | Order ready-made tags (print on demand) |
| A photo helps the finder confirm the item | Optional photo on the finder page |
| Used worldwide, in any language | Translation of pages and messages, 100+ languages |

Participants (anonymous at their request; no names or identifying details kept):
- Ages: two aged 20 to 26, one aged 33.
- Countries: one German living in Germany, one Ghanaian living in Germany, one Ghanaian living in Ghana.
- How they lost things: left something on a train; left a bag on a bench while waiting for a bus at a station. The third person had no loss; they gave their view of the idea and recommendations.

## 15b. Prototype test

Nov 2026: the clickable finder prototype was tested on phones by Selasey and 4 other people. No concerns or corrections raised. For the build phase: more modern transitions, animations and components (motion is a build-stage concern, not a wireframe one).

## 16. Change log

- 8 Nov 2026: Brief created from discussion: privacy messaging, universal use, travel mode, care tags, editing rules, short code correction, translator, owner-written finder message, permanent tag IDs and monetisation, tag preview.
- 8 Nov 2026: Monetisation revised (print on demand first, affiliate as quick start, digital tags free within the limit). Validation recorded. Moved to its own repo.
- 8 Nov 2026: Validation themes recorded. Repo moved to ~/Desktop/found-it. Name shortlist added.
- 8 Nov 2026: Hellotag rejected (name in use). Tagkin recommended. Competitor list added.
- 8 Nov 2026: Name chosen: Tagkin. Folder renamed to ~/Desktop/tagkin.
- 8 Nov 2026: Validation corrected to 3 people. Trademark search clear on EUIPO and USPTO.
- 8 Nov 2026: MVP scope confirmed. Phase 3 started: user flows drafted in docs/USER-FLOWS.md, with tag states and five open questions.
- 8 Nov 2026: Five flow decisions accepted (sign-in, return end, verification later, anonymous replies, city-level scan location).
- 8 Nov 2026: Finder flow wireframes (9 low-fi mobile screens, incl. Lost mode and inactive tag) built in Figma: https://www.figma.com/design/VIZaDBqDAKPsPWEmCY3Kog. Figma MCP limit hit again straight after; visual check pending.
- 8 Nov 2026: Address and code always printed on the tag. Wireframes move to HTML (Figma Starter limit); domain and Figma upgrade planned for around 14 Nov.
- 8 Nov 2026: Lost mode and messages wireframes added (docs/wireframes/lost-mode-and-messages.html, 8 screens).
- 8 Nov 2026: Finder flow rebuilt in HTML (docs/wireframes/finder-flow.html, 9 screens). All MVP wireframes now in docs/wireframes/; the Figma file is superseded until the UI phase.
- 8 Nov 2026: Validation participants described anonymously. Wireframe wording corrected: static screens, not click-through.
- 8 Nov 2026: Third participant clarified: no loss, gave views and recommendations.
- 8 Nov 2026: Three logo concepts sketched (docs/brand/logo-concepts.html).
- 10 Nov 2026: Logo concepts redrawn as solid marks (v2), tested as app icon, dark tile, 16 px and printed tag.
- 10 Nov 2026: D2 added (tag with lowercase k).
- 10 Nov 2026: Logo chosen: D2 (tag with lowercase k). Mark exported as SVG.
- 10 Nov 2026: Plan set: finish design in HTML, one-time import into Figma, then build.
- 10 Nov 2026: Clickable finder prototype built (docs/wireframes/finder-prototype.html): QR, Lost mode and typed-code paths, contact warning, anonymous and email replies, retired tag. Every path clicked through.
- 10 Nov 2026: Finder flow refined after prototype review: live place suggestions, "Share item location", note examples, reply by email or phone. Replies by phone need an SMS relay (cost, provider to choose).
- 10 Nov 2026: Figma limit confirmed from Figma's docs: 20 counted calls a month for a View seat; generate_figma_design, create_new_file and whoami are listed as exempt.
- 10 Nov 2026: Finder prototype published as a private link for testers: https://claude.ai/artifact/HyxUDEDyaY5EMghCdDWC6C (share it from the page's Share menu).
- 10 Nov 2026: Finder prototype tested by 4 people plus Selasey; no concerns. Modern motion noted for the build phase.
- 10 Nov 2026: Visual design pass A done: colour, type, spacing and components, light and dark, contrast checked.
- 11 Nov 2026: Palette changed to Fresh mint; tokens updated; contrast rechecked (lowest 4.7:1 light, 6.9:1 dark).
- 11 Nov 2026: Pass B done: 25 screens (finder 9, owner registration 8, Lost mode and messages 8) in light and dark, no overflow.
- 11 Nov 2026: Ordering screens added (order, checkout, order placed); 28 screens in total. Clickable owner prototype built from the same source; every path clicked through.
- 11 Nov 2026: Tab bar and three screens added (Messages, Orders, Account); 31 screens in total.
- 11 Nov 2026: Goal set: live app on App Store and Google Play. Store-readiness gap list drafted.
