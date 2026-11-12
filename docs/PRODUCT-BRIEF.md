# Tagkin: product brief

Name: Tagkin (chosen 8 Nov 2026; EUIPO and USPTO searches clear; tagkin.app bought 12 Nov 2026). Owner: Selasey Gbeddy. Started 8 Nov 2026. This file is the single source of truth: every decision goes here as it is made. Open work and when it starts: docs/ROADMAP.md. The rules Tagkin runs by: docs/BUSINESS-RULES.md (update it whenever a rule here changes).

## 1. The idea in one line

A QR tag for your belongings and pets (loved ones in phase 2, with Care tags). Anyone who finds them can scan the tag and alert you, and nobody's private details are shown.

## 1b. Positioning and marketing (updated 11 Nov 2026)

Two audiences, one promise: **protect what you value and help it find its way back.** Never promise speed: Tagkin cannot control how long a return takes. It connects finder and owner and shows where a tag was last scanned.
- **Protectors:** people who value their belongings (gear, luggage, pets) and buy tags deliberately. Message: security, privacy, proof of ownership.
- **Forgetters:** people who often misplace things. Message: relief and speed, with humour, never shame ("We all do it.").
Lead with protection in brand copy; use the forgetful angle in playful campaigns, gifts and social posts. Never make the user feel careless.

Marketing plan (business advisor recommendations):
1. **Every return is an advert.** The finder thank-you page invites the finder to get their own tag (first tag offer). Finders are warm leads.
2. **Return stories.** With both sides' consent, share anonymised real return stories; these are the best social proof.
3. **Moments of high risk:** target travel season, back to school, moving house, new pet, new phone or camera. Gift a tag at Christmas and birthdays.
4. **Partners where things go missing:** train and bus operators, airports, hotels, gyms, universities, vets and pet shops. Offer free staff lookup at lost-and-found desks; partners can stock ready-made packs.
5. **Pets first in ads:** a lost pet is the most emotional story and the clearest proof of value.
6. **Referral:** Invite a friend gives both people a discount on a printed tag.
7. **Measure:** activation rate, first scan to report time, returns, printed tags per user, Notify me for Premium, finder to owner conversion.

## 2. Principles

- **Private by default.** Neither owner nor finder sees the other's contact unless they choose to share it.
- **Ten seconds for the finder.** No app, no sign-up, no stress.
- **Universal.** Works in any country and on any phone, in as many languages as we can support. Core languages: English (UK, US and more), German, French, Dutch, Polish, Spanish, Italian; more added where tags sell.
- **One tag, one thing.** A tag ID is permanent and never reused.
- **Safe for people.** Care tags show the minimum, and every scan alerts the guardian.

## 3. Tag types

Type is chosen at registration and **locked** afterwards.

| Type | Purpose | Finder page focus |
|---|---|---|
| **Item** | Return | "Please help me get back to my owner" |
| **Travel** | Return during a journey (plane, train, bus, ferry, taxi or ride, hotel) | Luggage name and photo; optional trip (destination or hotel, carrier) shown as "hand to staff or message the owner". The trip hides when it ends |
| **Pet** | Help and return | Name, temperament, care notes, "please call my owner" |
| **Care (child or older relative), phase 2** | Help, not return | "I may need help. Please contact my guardian." Minimal info; emergency details behind a tap; every view logged and alerts the guardian |

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
3. **Where is it now?** With me · Handed to staff · Left it in a safe place (then a photo, note and address).
4. **Where exactly?** One field ("Input location here") with place suggestions as the finder types, plus a **Share item location** button.
5. **Anything else?** Optional note, prompted with examples (who the item was left with, exact landmark).
6. **Want a reply?** Optional email or phone number, kept hidden and relayed. Otherwise anonymous: "Without an email or phone number, keep this page open to receive replies."
7. Thank-you screen: live owner reply, finder can reply, check the owner's handover code, and see the first-tag offer. If the owner doesn't reply in time, the backup contact is alerted and the finder is offered a staff handover.

## 6. Privacy in the interface

- Owner setup: "Your contact is never shown. Finders message you through Tagkin."
- Finder page: "🔒 Your details stay private unless you choose to share them."
- Message box: "Only add your number or email if you want the owner to contact you directly."
- Phone or email detected in a message: "This will share your number with the owner. Continue?"
- Messages are relayed: neither side sees the other's email or number.
- One short, plain privacy page.

Phone detection: **libphonenumber-js** (open-source port of Google's libphonenumber) finds phone numbers in free text for any country. A simple pattern catches emails.

## 7. Editing rules

| Locked forever | Locked during an active return | Always editable |
|---|---|---|
| Tag ID and QR link | Item name, photo, description | Contacts, names, numbers |
| Tag type | | Emergency and medical notes |
| | | Finder message, language, Lost mode, tag on or off |

- Edit history is visible to the finder ("Photo updated 3 days ago").
- The QR code holds only a permanent link with the tag ID, so details change without reprinting.

## 8. Lost mode

Owner taps **Lost**. The finder page turns urgent: "This item is missing", with photo and a clear call to action. Each scan alerts the owner with the time and city (exact place only if a finder shares it). The finder page never says "stolen". **No public reward amount** (it could invite theft); the owner can thank or reward privately after the return.

## 9. Short code and channels

| Channel | Solves | Needs internet | Phase |
|---|---|---|---|
| QR scan | Normal case | Yes | MVP |
| Website code (e.g. TK-7Q4M-9XRA) | Damaged QR, camera trouble | Yes | MVP |
| WhatsApp | People who prefer WhatsApp | Yes | Later |
| SMS | No data at all | **No** | Later, starting in markets that need it |

## 10. Tag IDs and monetisation

- Each tag ID is random, at least 8 characters, unguessable and **never reused**. Format (11 Nov, refined 12 Nov): TK- plus 8 characters in two groups (TK-7Q4M-9XRA): 7 random and 1 check character, from an alphabet without 0, 1, I, L, O and U so it can be read aloud and typed; rude words are blocked; the QR address is permanent and encoded in capitals. Typing is case- and dash-insensitive. Code lookups are rate-limited to stop guessing.
- A tag belongs to one item. If the item is gone, the owner **retires** the tag; the ID stays dead.
- **No own printing company needed.** Recommended order:
  1. **Print on demand (main revenue):** orders go through Tagkin; a print-on-demand partner prints and ships under our brand; we set the price and keep the margin. Candidates to check: Printful, Printify, Gelato (sticker and keychain support, API, shipping to Europe and Ghana).
  2. **Affiliate links (quick start):** link to a printer with a referral programme and earn a commission per order. Lower income, zero stock.
  3. **Wholesale NFC or QR tags later:** buy blank tags in bulk, sell activated tags when volume justifies it.
- **Free tag (11 Nov):** one free phone lock-screen tag per account; every printed tag is bought and free to use for life; no home printing; no subscription at launch. Details in BUSINESS-RULES.md.
- Affiliate links and wholesale (points 2 and 3) are later options, not part of launch.
- Never sell or share user data. Privacy is the product.

## 11. Tag design and preview

- A **live preview** step in registration: the QR code inside a frame with the chosen line underneath ("Found me? Scan to return", or custom).
- Five shapes: sticker, keychain, pet tag, luggage label (printed) and the lock-screen tag (digital, phone only). Which shapes an item can have follows the shape-fit table (BUSINESS-RULES 3c).
- QR stays high contrast and scannable whatever the style.
- **Every tag prints the address and code under the QR** (e.g. tagkin.app · TK-7Q4M-9XRA), whatever the style. It is the only way in when the QR will not scan or the finder's camera cannot read QR codes.
- **Customise:** shape (only shapes that fit the item type; none to choose for pets or the lock-screen tag), size (where offered), 8 colours and 2 gradients, finish (matte, gloss, holo, glow, reflective by product) and an optional 12-character label, on a realistic product preview with price; the QR stays black on white. No downloads for home printing; tags are ordered. Print partner to be confirmed (Stage C).

## 12. Translation

- Pages appear in the phone's language when supported. Core languages: English (UK, US and more), German, French, Dutch, Polish, Spanish, Italian. More languages are added where tags sell. Never claim "any language" in copy.
- Messages are translated both ways, with "show original".
- Service: Google Cloud Translation, DeepL or an AI model. Check current prices before choosing.

## 13. More additions agreed in principle

- Owner verification before handover: done as a free 6-digit handover code.
- Safe meeting point suggestions (staff desks, shops, police): later.
- Backup contact if the owner does not reply within a set time.
- Report abuse on any message or tag.
- Scan alerts and a simple scan history per tag.
- Accessibility: large text, high contrast, works with screen readers.
- Data retention: messages deleted after a set period; retired tags keep no personal data.

## 13b. Success measures (hypotheses for the MVP)

How Tagkin will know the MVP works. Targets are first guesses to test, reviewed after launch (step 10).

| Measure | What it shows | First target |
|---|---|---|
| **Activation** | New accounts that make the free phone tag live | 60% |
| **Test scan** | New owners who try a test scan with another phone | 30% |
| **Conversion** | Owners who order a printed tag within 30 days | 15% |
| **Finder completion** | Finders who open a tag page and send a report | 50% |
| **Owner response** | Reports answered by the owner within 24 hours | 80% |
| **Returns** | Returns marked returned out of reports | Tracked from launch |
| **Premium interest** | Owners who tap Notify me | Decides whether to build Premium |
| **Finder to owner** | Finders who create an account | Tracked from launch |

These are internal targets, never public claims.

## 14. Open decisions

- [x] Name: **Tagkin** (chosen 8 Nov). Trademark search on EUIPO and USPTO: no results (8 Nov). Earlier shortlist: Shortlist (8 Nov, .com all taken; .app looked unregistered in a quick DNS check, not confirmed): Tagkin, Kindtag, Hellotag, Homingtag, Findmeback, Lostless, Tagback. Check trademarks and app stores before choosing. 8 Nov: Hellotag rejected (HelloTag app by Hellotag Corporation, France, already on the App Store). Tagkin: no app or product found in a web search; trademark search still to do.
- [x] MVP scope: Item, Travel and Pet. Care tags in phase 2 (8 Nov).
- [x] Flow decisions (8 Nov): sign-in by email one-time code, no passwords. A return ends when the owner marks Returned, or after 14 days with no messages. Owner verification before handover comes after the MVP. Anonymous finders see replies only while the thank-you page is open, with a gentle nudge to leave an email. Scan location is city level unless the finder shares exact location.
- [x] Wireframe method (8 Nov): static HTML wireframes, then Figma for the final UI. *Superseded 10 to 11 Nov: design lives in docs/design (screens, prototypes) and is imported to Figma once.*
- [x] tagkin.app bought 12 Nov 2026 through Cloudflare Registrar (Community publish now unblocked). Figma Professional is optional; the import tool is exempt from the MCP limit.
- [x] Logo (10 Nov): **D2**, a solid tag with the hole and a lowercase k cut out, next to the lowercase wordmark "tagkin". Master file docs/brand/tagkin-mark.svg. Colour, final type and a trademark image search still to do.
- [x] Design-to-Figma plan (10 Nov): all design is finished in HTML first (tokens, components, every screen, clickable prototype, tested). Then one combined page is imported into Figma with generate_figma_design, which Figma lists as exempt from the MCP limit (Starter View seat: 20 counted calls a month; reset date not published). Prototype links, Community publishing and tidy-up are done by hand in Figma, which needs no tool calls. The HTML tokens and components become the starting code for the app.
- [x] Visual design pass A (10 Nov): tokens in docs/brand/tokens.css, previewed in docs/brand/design-system.html. Palette **Fresh mint** (chosen 11 Nov over Signal blue and Tag yellow, after the first green was judged dull): mint #00C48C for fills with dark text on it, #007A57 for mint text and links (dark mode #1FE0A6); red #E02A17 only for Lost mode; amber only for privacy warnings; clean neutrals with a faint mint tint. Type: Bricolage Grotesque for titles, Inter for body (*superseded 11 Nov: Geist for headings and body, Bricolage for the wordmark only*); inputs at least 16 px. 4-point spacing; radius 8 / 14 / 22; controls at least 52 px tall. All text and colour pairs pass WCAG AA (4.5:1) in light and dark. Components: buttons, input, choice, status badges, notes, privacy line, Lost banner, message bubbles, tag list item, printed tag.
- [x] Visual design pass B (11 Nov): all 25 MVP screens styled on one page, docs/design/tagkin-screens.html, generated by docs/design/build_screens.py from tokens.css. This page is what gets imported into Figma once.
- [x] Tag ordering in the owner flow (11 Nov): after a tag goes live (and from tag detail), the owner can order it printed: choose sticker, keychain or pet tag and a quantity, then check and pay. Payment is handed to the print partner; Tagkin never sees card details. *Superseded: Tagkin is the seller through Stripe (rule 3.8); all four printed shapes can be ordered.* Prices are samples until the partner is chosen. Clickable owner prototype: docs/design/owner-prototype.html, generated with the screens page.
- [x] Owner app navigation (11 Nov): bottom tab bar with My tags, Messages, Orders, Account. Account holds plan and subscription (Premium later), contacts and backup contact, notifications, language, privacy and data, help and sign out. Settings live inside Account rather than as a separate icon.
- [x] Target (11 Nov): a fully functional live app on the Apple App Store and Google Play, built to their review standards. Finders stay on the web (no app needed); owners use the app.
- [x] How tags get linked (11 Nov): tags ordered in the app are printed with the owner's own code, so they arrive already linked; no scan needed. The main path is Create a tag (digital now, order printed later). Scanning or typing a code is only for activating ready-made tags (sold in shops, gifts, bulk packs later), reached from a small "Activate it" link.
- [x] Adopted (11 Nov): **a bought tag is free to use for life.** Every printed tag, ordered in the app or bought ready-made in a shop or online, works fully without a subscription and does not count toward the free tag (*the allowance became 1 free phone tag, see below*). Premium sells extras only (unlimited digital tags, SMS, family sharing, extra contacts). Check Apple and Google rules on physical products unlocking app features at Stage C.
- [x] Adopted (11 Nov): **Gift a tag** (this wording, not "This is a gift"). Entry points: the Tag is live screen after the owner's first tag, a For me / Gift a tag choice on Create a tag (*not in ordering, see below*), and later the website for people without the app. Only printed (paid) tags can be gifted; free digital tags cannot, and "Invite a friend" covers that instead. Order printed tags without linking them; codes stay unclaimed until the recipient activates them in the app (activation screens already exist). Needs: a gift option in ordering, a gift note, delivery to the recipient, and a finder page for an unclaimed tag ("Not set up yet").
- [x] Decided (11 Nov): **1 free active tag instead of 3.** *Refined the same day: the free tag is the phone lock-screen tag and nothing is self-printed (rule 2).* Retiring it frees the slot (codes are still never reused). Bought tags never count. Reason: free self-printed tags compete with paid tags, and 1 is enough to try Tagkin.
- [x] Decided (11 Nov): **launch without Premium.** Income at launch is tag sales only; no subscriptions or in-app purchase at first. The Plan screen keeps Premium as "Later" with Notify me, so sign-ups measure real demand before building it.
- [x] Recipients of gifted or shop tags need an account to activate: they become the owner and must receive alerts and messages. Sign-in stays light (email code). Shop and gifted tags can be personalised digitally at activation (type, name, photo, finder message); the printed design is fixed.
- [x] Adopted (11 Nov): **first printed tag offer**, shown as a discount line at checkout ("First tag offer −€2.00"), once per account; no struck-through prices (EU price rules). Amount confirmed with final prices in step 6 / Stage C.
- [ ] Premium ideas (11 Nov), for after launch, to validate with Notify me sign-ups: **Ownership vault** (serial numbers, receipts, photos; one-tap police report and insurance claim PDF), **Stolen mode** (owner side only: police reference, every scan logged as evidence, police-ready report; the finder page never says "stolen", see below), **Verified handover** (one-time handover code so only the real owner can collect), **Return by courier** (finder taps Send it back, a courier collects, owner pays), **Household** (shared tags, escalation chain of contacts, SMS and WhatsApp alerts). Decide later which, if any, stay free for safety reasons (Stolen mode is a candidate).
- [x] Stolen mode and finders (11 Nov): a finder who reads "stolen" may fear being dragged into a case, asked to be a witness, or wasting time, and may walk away. So the finder page always shows the helper framing ("This item is missing"), whatever the owner's mode. The stolen status, police reference and evidence log stay on the owner's side. Finders can always choose to hand the item to staff or police anonymously.
- [x] Copy rule (11 Nov): never promise speed or "any language". Tagkin connects finder and owner and shows where a tag was last scanned; how long a return takes is outside our control. Say "many languages"; core languages are English (UK, US and more), German, French, Dutch, Polish, Spanish, Italian.
- [x] Two Figma pages (11 Nov): the full hand-off (docs/design/tagkin-screens.html, kept private) and a public showcase for Community (docs/design/tagkin-showcase.html: cover, store panels, selected screens, printed tags, marketing). Community files can be copied by anyone, so spec notes, flow map, business rules and private links stay out of the showcase.
- [x] Adopted (11 Nov): **Pick your tag visually.** A gallery of tag styles on real objects (sticker on a bag, keychain on keys, pet tag on a collar, luggage label, phone lock screen) when adding a tag, and a live preview card that updates as the owner types name and message, through to ordering.
- [x] Adopted (11 Nov): **Status updates by the owner.** Owners can post a short update the finder page shows, for example a trip leg ("On the way to Dubai" → "Arrived in Dubai") or a hint in Lost mode. Opt-in, city level only, no dates, expires automatically.
- [x] Adopted (11 Nov): **No self-printing for sale.** At launch, extra tags come only as printed tags (from €4.90; no extra digital or self-printed tags for sale). Reason: selling digital tags inside the iOS and Android apps must go through Apple and Google payments (15 to 30% fee) and adds review work, while physical tags can use normal payments. Revisit paid extra digital tags with Premium.
- [x] Copies of one tag (11 Nov): one code can be ordered as several copies (e.g. phone and phone case, suitcase outside and inside). Use copies for one belonging; give separate belongings separate tags, so the owner knows which item was found and can put each in Lost mode on its own.
- [x] Business rules document (11 Nov): docs/BUSINESS-RULES.md holds every operating rule (model, free tag, printed tags, codes and ownership, gifting, finders, privacy, copy).
- [x] Download only for the free tag (11 Nov). *Superseded by the audit fixes (11 Nov): no home printing at all; the free tag is the lock-screen image (rule 2.2).* Colours and shapes are for ordered tags.
- [x] Gift a tag is always blank tags (11 Nov): set-up tags can't be gifted or moved; the owner account gets all alerts and controls Lost mode; gift buyers never see the recipient's alerts. The For me / Gift a tag switch was removed from ordering a set-up tag.
- [x] Customise your tag (11 Nov; extended later on 11 Nov with size, 10 colours, finish and label): type, colours and size shown on a realistic preview; the order screen shows the same tag. Gallery renamed "Choose your type of tag". QR always black on white.
- [x] Decided (11 Nov, before build): **guest exploration, light version** (explore and customise without an account; email-code sign-up at Make it live, Continue to payment (*was Continue to delivery before Order details merged*) or activation; guest gift checkout); **launch markets** Germany and the EU first, Ghana later with a local payment provider; **web beta first**, then the apps; **future-proof data model** (tag members, currency, entitlements, transfers) without their screens. Correction: Apple does not require guest access for account-based apps; the reason is conversion.
- [ ] Print partner
- [x] Translation provider: DeepL, Google Cloud Translation as fallback (docs/adr/0007)
- [x] Tech stack (11 Nov, step 6): React Native with Expo, Next.js on Vercel (fra1), Supabase in Frankfurt, Stripe, DeepL with Google fallback, Expo push, monorepo. Replaces the earlier Cloudflare suggestion (see docs/adr/0003). *Later approved: Brevo (email), Bird via Supabase (SMS recovery), Google Places, PostHog EU and Sentry EU; print partner still open.*

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
| Editing a photo mid-return could confuse or mislead | Name, photo and description locked during a return; visible edit history |
| Luggage travels by train, bus, ferry and taxi too | Travel mode for every transport type; trip details expire |
| Pets and people need help, not "return me" | Pet and Care tags with their own messages |
| Owners want to choose what the finder reads | Templates per type plus custom text with preview |
| Cutting out printed tags is messy | Order ready-made tags (print on demand) |
| A photo helps the finder confirm the item | Optional photo on the finder page |
| Used worldwide, in many languages | Translation of pages and messages, starting with the core languages |

Participants (anonymous at their request; no names or identifying details kept):
- Ages: two aged 20 to 26, one aged 33.
- Countries: one German living in Germany, one Ghanaian living in Germany, one Ghanaian living in Ghana.
- How they lost things: left something on a train; left a bag on a bench while waiting for a bus at a station. The third person had no loss; they gave their view of the idea and recommendations.

## 15b. Prototype test

Nov 2026: the clickable finder prototype was tested on phones by Selasey and 4 other people. No concerns or corrections raised. For the build phase: more modern transitions, animations and components (motion is a build-stage concern, not a wireframe one).

12 Nov 2026: the owner app and desktop prototypes were tested by **Eli**, one owner tester. The planned 5-person owner round was skipped (decided 12 Nov); Eli's findings were enough to act on, and wider testing moves to the web beta and TestFlight. What Eli found and what it changed:

| Finding | What it changed |
|---|---|
| No way to order a blank tag and set it up later | Blank tags keep their shape; set-up offers only types that fit; n blanks create n tags (rule 4.8, TK-105) |
| New tags showed other tags' scans and history | Every tag has its own scan history; new tags start with "No scans yet" (TK-39) |
| Photos could not be changed from the tag | Tap the photo to edit; the change shows everywhere; locked only during a return (rule 4.4, TK-106) |
| New orders didn't show in Orders; orders weren't clickable | Order details page with seven stages, problems and actions (rule 3d, TK-55) |
| Desktop finder page stayed on "Thank you" after the handover | Report closes after the handover (TK-17) |
| Should the owner web match the app? | Web keeps create, order and manage (web beta); push alerts, lock-screen tag and scan-to-activate stay in the app |
| Lock screen offered as a shape for bags and pets | Shape-fit table (rule 3c) drives every screen |

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
- 11 Nov 2026: docs/ROADMAP.md created: every open item, staged A to G with a trigger for each.
- 11 Nov 2026: Stage A batch 1: welcome and terms, notification and camera explainers, add a tag (scan, digital, code), tag found and tag already linked, privacy and data, delete account. A linked tag code can never move to another account. 44 screens.
- 11 Nov 2026: Stage A batch 2: empty states (tags, messages, orders), offline, payment failed, message not sent, finder code not found, tag during a return (locked fields), edit message, contacts with backup contact, scan history, retire tag. 56 screens.
- 11 Nov 2026: Stage A batch 3: Travel details (finders see destination and operator only; dates and home address never shown), Pet details with care notes behind a tap, finder pages for Travel and Pet, finder report form (112 for emergencies), owner report or block with an anti-scam warning, plan (Premium billed through the stores), notifications, language, splash and app icon (docs/brand/app-icon.svg). Stage A complete: 67 screens, no overflow, light and dark checked.
- 11 Nov 2026: Review changes: ordering is now three steps (choose, delivery details, review and pay), so the address is asked before any payment button; added luggage label as a product. Appearance setting (light, dark, match system) with sun and moon icons. Trip fields change with the transport type (airline, rail company, bus company, ferry, ride service, hotel). Pick a style is preselected from the tag type (item: sticker, travel: luggage label, pet: pet tag). Every tag shows its QR, with a 10-minute test mode: test scans show a Test banner and send no alerts. Emoji picker in the chat. Sample names replace real ones in screens. 72 screens.
- 11 Nov 2026: Add a tag reworked: one main option, Create a tag; activation of ready-made tags moved to a secondary link.
- 11 Nov 2026: Activation path: scan or type the code, "Set up this tag", choose type, details, finder message, then "Your tag is live" with Test my tag. The style and order steps are skipped, since the tag already exists. 73 screens.
- 11 Nov 2026: Add your first tag rewritten as three steps (create, get it printed, stick it on). Ready-made tag pricing and gift tags proposed.
- 11 Nov 2026: Bought tags free for life and Gift a tag adopted. Free tags not giftable. Free allowance of 1 active tag proposed.
- 11 Nov 2026: One free active tag; launch without Premium; Activate another tag added after activation; recipients need an account; first-tag offer proposed.
- 11 Nov 2026: Gift a tag designed (choose with gift note, who it's for with hidden prices, review, on its way), reachable from ordering (For me / Gift a tag), Tag is live and Orders. First tag offer shown as a sample −€2.00 line at checkout (amount still to decide). Invite a friend in Account. Finder page for a tag that isn't set up yet. 78 screens.
- 11 Nov 2026: Positioning changed to protecting what you value; welcome, empty state and gift copy rewritten. Activation path shows its own step count (of 3). Premium ideas recorded.
- 11 Nov 2026: Positioning widened to both protectors and forgetters; marketing plan added; Stolen mode never shown to finders.
- 11 Nov 2026: Finder prototype rebuilt in the final design from build_screens.py (docs/design/finder-prototype.html) and republished to the same link (version 2): item, Lost mode, travel, pet, typed code, retired, not set up, owner test scan, report. Thank-you page now invites finders to protect their own things (first tag offer).
- 11 Nov 2026: Hand-off completed for the one-time Figma import (docs/design/handoff_parts.py): cover with how to read the file, flow map with tag states, a spec note under 77 screens (rules plus button → destination), component states and loading screens, 4 email templates and push notifications, finder on desktop, tagkin.app website (home, privacy, support, required by the stores), Community cover and 3 social visuals for both audiences.
- 11 Nov 2026: App Store and Google Play screenshot concepts (5 panels, 1290 × 2796): brand, Finder alerts you, Private by default, every belonging, every trip and many languages with Gift a tag. Red stays reserved for Lost mode. Final store screenshots are re-shot from the real app before submission.
- 11 Nov 2026: Pre-import fixes: copy no longer promises speed or any language; secure tag codes (TK-7Q4M-9XRA) everywhere; Impressum, privacy and terms footer on every finder and web page; sign-in code email; printed tag artwork (sticker, keychain, pet tag, luggage label with trim and bleed); lock-screen image and printable A4 sheet; camera and notification recovery screens; German long-text and Arabic right-to-left checks; accessibility rules; Android adaptive icon; public showcase page. Finder prototype republished (version 3).
- 11 Nov 2026: Proposals recorded: visual tag picker with live preview, owner status updates, self-printing pricing.
- 11 Nov 2026: Pick your tag gallery, live preview card, owner status updates (shown on the finder page), and copies of one tag designed. 80 screens.
- 11 Nov 2026: Business rules document; free-tag-only download; customise screen with colours and sizes; gifting limited to blank tags.
- 11 Nov 2026: Colour fills the whole tag (QR keeps a white quiet zone). Lock screen treated as its own digital product (no sticker swap; "Set as lock screen"). Create a tag offers For myself / Gift a tag; gift buyer picks product and colour, recipient picks the belonging. Full audit written: docs/AUDIT-2026-11-11.md (5 critical, 9 high findings).
- 11 Nov 2026: Audit fixes adopted and designed: free tag is the phone lock-screen tag (doubles as a self-test before buying); no home printing; activation PIN on gift cards and shop packs; email required, owner sign-in at tagkin.app, account recovery; free handover code; finder no-reply help; second tag goes straight to ordering and is live from order; notifications asked after the first tag; packs and free shipping over €15; softer support and report promises. Domain to be bought by 15 Nov, before Community publish. 85 screens.
- 11 Nov 2026: Finder can leave an item in a safe place with photo, note and address (exact pin only when the finder shares location; photo location data removed). Owner sees photo, map and address with Open in Maps and I picked it up. Added the owner web dashboard (tagkin.app/my-tags) and a tablet layout (list and detail side by side). 87 screens.
- 11 Nov 2026: Visuals made real-life: drawn scenes (station, café, airport, park, desk) and live notification banners behind phones in store panels, Community cover, social posts and the website hero; photo-like lock-screen wallpapers. Step-by-step logic check of all journeys: step counters fixed (4 create steps, 3 order or activation steps), first printed tag now leads to the notifications prompt, recovery banner on My tags after the first tag.
- 11 Nov 2026: Pay with step added to order and gift checkout (Apple Pay/Google Pay, card, PayPal, Klarna via Stripe; Tagkin is the seller). Removed leftover print-it-yourself copy. Website menu works on narrow screens; brand store panel and social posts decluttered. Checked at 375, 768 and 1400 px: no overflow, no sideways scrolling.
- 11 Nov 2026: Emoji picker in every free-text box (finder message, edit message, gift note, status, pet notes, thank-you, finder note and place, all chat boxes on both sides), inserting at the cursor. Full user walk-through including provider moments: code email help text, personalised-goods notice at checkout, order states (in production, shipped), shipped email, finder can reply and check the handover code from the thank-you page. New docs/SYSTEM-LOGIC.md for engineers. All screens searched against the rules.
- 11 Nov 2026: Product owner flow defined in ROADMAP.md (10 steps). Steps 1 to 4 done; next is step 5, the backlog (epics, stories, acceptance criteria, MVP scope), then step 6, technical design.
- 11 Nov 2026: Step 5 started: backlog of 57 user stories (40 Must = MVP, 15 Should, 2 Could; Won't listed) in 9 epics and 5 milestones, with Definition of Ready and Done. Source docs/backlog/stories.py generates docs/BACKLOG.md; all 57 stories created as GitHub issues with labels and milestones.
- 11 Nov 2026: Step 5 done: GitHub project board "Tagkin backlog" (users/Selaseyjr/projects/2) linked to the repo, all 57 stories in Stage = Backlog. Next: step 6, technical design.
- 11 Nov 2026: Board uses one Status field (Backlog, Ready, In progress, Review, Done); Stage field removed; 5 automations need re-enabling in the GitHub UI. System audit: README and outdated brief sections updated (free tag, customise, finder flow, Lost mode, Care = phase 2), USER-FLOWS.md marked superseded, rules numbering fixed, two Must stories added (TK-97 states, TK-98 store listings; 59 stories), build warning fixed, finder link republished.
- 11 Nov 2026: All 6 board automations on with the new Status options (item added → Backlog, PR linked → In progress, item closed and PR merged → Done, Done closes the issue, sub-issues auto-added). Step 5 complete.
- 11 Nov 2026: Final check before step 6: every screen maps to a story; added non-functional requirements (SYSTEM-LOGIC.md section 10), MVP success measures (brief 13b) and TK-99 Notify me (60 stories). Ready for step 6.
- 11 Nov 2026: Final pre-step-6 check passed (build, backlog, copy search; two stale brief items fixed). Step 6 started: docs/TECH-DESIGN.md and 12 decision records in docs/adr. Research: Resend stores account data in the US, so transactional email goes to an EU provider (shortlist Brevo, Scaleway TEM); Supabase Frankfurt keeps database, auth and storage in the EU; Stripe covers PayPal and Klarna in Germany; DeepL covers 100+ languages.
- 11 Nov 2026: Research for step 6: email → Brevo recommended (EU, outbound plus inbound parsing for finder replies; Scaleway is outbound-only), SMS recovery → Bird via Supabase's built-in provider (EU, no verify fee; Twilio Verify fallback), places → Google Places (New) with session tokens and server-side calls (near-zero cost within free caps). Awaiting approval; email test after the domain is bought.
- 11 Nov 2026: Approved: Brevo (email, outbound and inbound), Bird via Supabase (recovery SMS), Google Places (New) (places). 11 of 12 decisions accepted or approved; open: analytics (0012), print partner (0010, samples).
- 11 Nov 2026: Approved PostHog Cloud EU (analytics) and Sentry with EU storage (errors), no personal data in events, no cookies on finder pages. 11 of 12 technical decisions made; only the print partner remains (after samples).
- 11 Nov 2026: Four pre-build decisions: guest exploration (light), EU-first markets, web beta first, future-proof data model.
- 11 Nov 2026: Applied the four decisions: guest flow in screens and prototype (sign-up sheet at Make it live, Continue to delivery, activation; guest gift checkout email), rules section 1b, system logic (tag members, drafts, entitlements, transfers, prices per market and currency, guest orders), tech design (draft claim, guest gift API, build order with web beta as M2). Backlog: TK-100 to TK-102 (63 stories), milestones reordered in GitHub.
- 11 Nov 2026: Pilot limited to countries where Stripe and the print partner work; others noted as future markets.
- 11 Nov 2026: Step 7 started. Refinement: all 14 M1 stories Ready (screens, rules, logic sections and dependencies on each). Added TK-103 report alert by email and TK-104 reply to a finder on the web (M1 needed both for an owner to receive and answer a report before the app); TK-82 narrowed to tags and reports (orders from M2). 65 stories. Sprint 0 planned (docs/sprints/SPRINT-0.md, 12 to 18 Nov, one-week sprints).
- 11 Nov 2026: Owner app prototype published as a private link for demos: https://claude.ai/artifact/9Xrte4UA56N8LCefx6Zycm (share from the page's Share menu).
- 11 Nov 2026: Prototype review fixes. Owner: the details you enter (type, name, photo) carry through every later screen; My tags is live (new tags appear, Lost / Return active / Returned / Active badges update, retire removes); every hard-coded "Black backpack" title now follows the chosen tag. Order and delivery merged into one Order details page ("Continue to payment" is now the sign-up point). Customise offers shape, size, 8 colours plus 2 gradients, finish (matte, gloss, holo, glow, reflective by product) and an optional 12-character label; logo shown on pet and lock-screen tags; order preview centred. Finder: handover check open from the tag page during a return (no session, 5 tries then 15 min), confirmed handover closes the conversation with a thank-you page; report link to resume; report flow has a details box and a confirmation sheet. Back returns to the previous screen, except after a completed irreversible step (history cleared). Type: Geist for headings and body, Bricolage kept for the wordmark; pill buttons. Rules 3 and 6, system logic 8, tech design API and stories TK-1, 16, 17, 19, 31, 51, 102 updated.
- 11 Nov 2026: Prototype: realistic product mockups (sticker on laptop, acrylic keychain, metal pet tag on collar, luggage label on suitcase, lock screen) drawn live from the chosen shape, size, colour, finish and label, used on Customise, Order details, Review and pay and Order placed. Item photo shown on order and checkout; tapping the item picture anywhere uploads the tester's own photo. List badges New and Returned defined in SYSTEM-LOGIC 3.
- 11 Nov 2026: Decided: travel trip details are optional (luggage name and photo are enough; trip can be added later and hides when it ends). Item name required; photos up to 10 MB, resized to 1600 px. Draft and navigation rules added (SYSTEM-LOGIC 8). Prototype: 6 Unsplash sample photos (docs/design/assets/samples, licence in SOURCES.txt), photo sheet with full-screen preview, product preview on Customise, luggage photo. Desktop web prototype built (docs/design/build_desktop.py): owner sign-in, My tags with detail panel, Lost mode, replies, Mark as returned, messages, orders, account; finder desktop page with report, live reply, handover check and report abuse.
- 11 Nov 2026: Desktop prototype published: https://claude.ai/artifact/7VZer2dHF7HKYbQeQzMyy9
- 11 Nov 2026: Consistency pass before build: data model gains size, finish, label and optional trip (ends_on); validation limits for name, description and photos; brief, user flows, design-system text and TK-51 title brought in line.
- 11 Nov 2026: Owner journey fixes: paid orders appear in Orders (own, blank, gift); Order a tag and Gift a tag start fresh with empty fields; blank tags for yourself (order now, set up later, state unlinked, shown as Set up); item name, photo and description editable later (TK-106); Order more copies from a tag; pet tag and luggage label skip the redundant type step. Rules 4.8 and 4.9, SYSTEM-LOGIC tag states, stories TK-105, TK-106, TK-30, TK-55.
- 11 Nov 2026: Owner speed-ups added to prototype and backlog: one-tap suggested message, saved address card, Undo bar for found and returned, quick actions (⋯ and reply from notification), suggested replies, set up blank tags in a row, order timeline, one nudge card at a time. New stories TK-107 to TK-109; TK-30, TK-51, TK-55, TK-105, TK-106 updated. Express wallet-first payment was already in place (Apple Pay default).
- 12 Nov 2026: Shape fit decided (BUSINESS-RULES 3c): one table sets which item types each shape fits (sticker: item or travel; keychain: item; luggage label: travel; pet tag: pet; lock screen: phone only, never blank or gift). Type step, Customise and blank set-up only show what fits.
- 12 Nov 2026: Name, photo and description now lock only during a return, not in Lost mode (a better photo helps finders). Photo edit from the tag screen updates every place the item appears.
- 12 Nov 2026: Order lifecycle decided (BUSINESS-RULES 3d): seven stages from Paid to Delivered, cancel before printing, address change until shipped, free reprint, free resend after failed delivery, free replacement for problems. Order details page in app and web (TK-55 now L).
- 12 Nov 2026: Owner web is the lighter companion: manage tags, Lost mode, messages, orders, edits and blank set-up; creating, ordering, scanning, push alerts and the lock-screen tag stay in the app, with a Get the app prompt. Each tag now has its own scan history; desktop finder page closes after the handover.
- 12 Nov 2026: Owner prototype test by Eli recorded (15b); 5-person round skipped. Web scope corrected: the web beta keeps create, customise, order and gift (TK-102 stands); only push alerts, the lock-screen tag and scan-to-activate are app-only. Full consistency audit of every project file against the current rules and prototypes; superseded brief decisions marked.
- 12 Nov 2026: Domain plan: tagkin.app bought through Cloudflare Registrar on Selasey's existing personal account (at-cost renewal, free WHOIS privacy). Cloudflare Registrar keeps DNS on Cloudflare, so Vercel, Brevo and Supabase records are added there (Vercel records unproxied). hello@tagkin.app forwards to Gmail through Cloudflare Email Routing; Brevo inbound replies use a subdomain so the two never clash. Sprint 0 S0-10 updated.
- 12 Nov 2026: tagkin.app bought (Cloudflare Registrar, auto-renew on); nameservers confirmed on Cloudflare. Unblocks Sprint 0 S0-10 (Brevo, sign-in emails) and Stage B (Figma import and Community publish).
- 12 Nov 2026: Stage 7 runs in 10 batches with a gate each (docs/sprints/BUILD-BATCHES.md): CI, data model and environments come before any feature code. S0-1 monorepo done (Node 24, pnpm 12, Next 16.4, Expo SDK 58, TypeScript 6.0; app id app.tagkin).
- 12 Nov 2026: Audit before batch 2 (docs/AUDIT-2026-11-12.md): 60 findings across product rules, architecture, security, business and law, design, pipeline and store launch, prioritised P0 to P5 with 9 decisions for Selasey. Top risks: code and QR format not frozen, cross-platform libraries and test stack not chosen, legal pages planned after finder pages go live, no legal entity or tax set-up, no print-file pipeline, EU product and packaging rules, Google Play 12-tester requirement.
- 12 Nov 2026: Audit decisions accepted: code format frozen (check character, blocklist, permanent capitalised QR address; rule 4.1); libraries chosen (ADR 0013: i18next, Expo Router with universal links, react-hook-form with shared Zod schemas, TanStack Query, generated tokens with a light/dark theme hook); testing and release practice (ADR 0014: Vitest, pgTAP, Playwright with axe, Maestro later; migrations only through CI, expand and contract, EAS Update channels); finder replies by email or anonymous at launch, phone replies later (TK-15); Definition of Done extended with pipeline checks.
- 12 Nov 2026: Demo first: until funding, Tagkin ships as a working demo (finder pages, owner web, Android app by link, iPhone in the browser) with Stripe test mode and a simulated print partner, at about €0 a month. Store launch, sales and business set-up wait behind a funding gate. Batches 7 to 9 and the funding gate in docs/sprints/BUILD-BATCHES.md.
- 12 Nov 2026: Batch 3 (data foundation): Supabase project in Frankfurt (one project while demo-first); 15 tables with row-level security on every table; code format, check character and shape fit enforced in Postgres; state machines and the item lock as database functions; finder page served by one restricted function; 7 seed tags; 45 database tests and SQL lint in CI.
- 12 Nov 2026: Batch 4 (environments) in progress: tagkin.app live on Vercel (Frankfurt), www redirects to it; Brevo authenticated for tagkin.app and used by Supabase Auth; sign-in email is a 6-digit code with no links; database migrations and auth settings reach the hosted project only through CI (dry run on pull requests, applied on main) with a project-scoped token.
