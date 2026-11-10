# Tagkin: product backlog

Step 5 of the product owner flow (ROADMAP.md). Generated from docs/backlog/stories.py; GitHub issues are created from the same source. Board: https://github.com/users/Selaseyjr/projects/2 (Stage: Backlog, Ready, In progress, Review, Done).

60 stories in 9 epics. Priorities use MoSCoW; the MVP is every Must story. Sizes: S (≤1 day), M (2–3 days), L (about a week).

## Milestones

- **M1 Finder web and accounts**: A finder can report a tag; an owner can sign in and receive it. (12 stories)
- **M2 Owner app core**: Owners create and manage tags, run Lost mode and returns in the app. (28 stories)
- **M3 Ordering and payment**: Printed tags can be ordered, paid and tracked. (6 stories)
- **M4 Gifting and activation**: Blank tags can be gifted and activated with a PIN. (3 stories)
- **M5 Launch readiness**: Website, legal, accessibility, languages, operations and store submission. (11 stories)

## Summary

| Priority | Stories |
|---|---|
| Must | 42 |
| Should | 16 |
| Could | 2 |
| Won't (this release) | 5 items, listed below |

## Definition of Ready

- Story written as 'As a … I want … so that …'
- Acceptance criteria agreed
- Screens linked (tagkin-screens.html frame names)
- Business rules and SYSTEM-LOGIC.md sections checked
- Dependencies known; size estimated (S, M, L)

## Definition of Done

- Acceptance criteria met and demoed
- Works on iOS, Android and web where relevant; checked at phone and desktop widths
- Copy checked against the copy rules (no speed, any-language or fixed-time promises)
- Accessibility basics: labels, contrast, text scaling
- Errors and provider failures handled as in SYSTEM-LOGIC.md
- Tests for the logic; no new warnings
- Documentation updated (brief change log, rules or system logic if affected)

## E1 · Accounts and sign-in

Owners can create an account, sign in on any device, recover access and control their data.

### TK-1 · Sign up and sign in with an email code

*Must · M · M1 Finder web and accounts*

As a new owner, I want to sign in with my email and a one-time code, so that I don't need a password.

- Email is required and verified with a 6-digit code valid for 10 minutes
- After 5 wrong attempts the user waits before trying again
- Resend is possible after 30 seconds; the screen suggests checking spam or using another email
- Terms must be accepted before the account is created

### TK-2 · First launch intro

*Should · S · M2 Owner app core*

As a new owner, I want to understand Tagkin in two screens, so that I know what I'm signing up for.

- Welcome and 'Private by default' screens, then terms
- 'I have an account' skips to sign-in

### TK-3 · Sign in on the web

*Must · M · M1 Finder web and accounts*

As a owner whose phone is lost, I want to sign in at tagkin.app on any device, so that I can still use Lost mode and reply.

- Same email-code sign-in as the app
- After sign-in the owner sees My tags with Lost mode and messages

### TK-4 · Account recovery

*Must · M · M2 Owner app core*

As a owner who lost access to my email, I want to recover my account with a recovery phone or backup email, so that I don't lose my tags.

- Recovery phone receives an SMS code; backup email receives an email code
- Prompted after the first tag via a banner on My tags
- Support can recover an account with an order number (manual process)

### TK-5 · Signed-in devices

*Should · S · M2 Owner app core*

As a owner, I want to see and sign out devices, so that I stay in control if a device is lost.

- List shows device and last use
- Sign out ends that session immediately

### TK-6 · Delete my account

*Must · M · M2 Owner app core*

As a owner, I want to delete my account in the app, so that my data is gone when I leave.

- Shows what happens: tags retired, messages and photos deleted, invoices kept as the law requires
- Requires confirmation; sends a confirmation email
- Warns if a return is still open

### TK-7 · Download my data

*Must · S · M5 Launch readiness*

As a owner, I want to download my data, so that I can see what Tagkin stores.

- Request in Privacy and data; email with a download link valid 24 hours

### TK-8 · Language and appearance

*Should · S · M2 Owner app core*

As a owner, I want to choose my language and light, dark or system appearance, so that the app suits me.

- Core languages: English (UK, US), German, French, Dutch, Polish, Spanish, Italian
- Appearance default is match system


## E2 · Finder web

Anyone who finds a tagged item can report it from a browser, privately, without an app.

### TK-10 · Open a tag from its QR code

*Must · M · M1 Finder web and accounts*

As a finder, I want to see the owner's message when I scan a tag, so that I know what to do.

- tagkin.app/TK-… shows the photo, message translated to my browser language and Show original
- No app or account is needed
- Lost tags show 'This item is missing'; never the word stolen
- Travel tags show destination and operator only; pet tags hide care notes behind a tap

### TK-11 · Type a code when the QR won't scan

*Must · S · M1 Finder web and accounts*

As a finder, I want to type the code printed on the tag, so that I can still report it.

- Case- and dash-insensitive
- Wrong code shows a clear error; lookups are rate-limited
- Retired tags show 'no longer active'; unclaimed tags show 'not set up yet'

### TK-12 · Report where the item is

*Must · M · M1 Finder web and accounts*

As a finder, I want to say where the item is now and where exactly, so that the owner can get it back.

- Choose with me, handed to staff, or left in a safe place
- Place suggestions after 2 letters; free text always allowed
- Share item location asks browser permission; denied means city only

### TK-13 · Leave it in a safe place with a photo

*Should · M · M1 Finder web and accounts*

As a finder who can't keep the item, I want to add a photo, note and address, so that the owner can find the exact spot.

- Only for 'left in a safe place'
- Photo location data (EXIF) removed before upload
- Address from shared location or typed text, editable

### TK-14 · Add a note safely

*Must · S · M1 Finder web and accounts*

As a finder, I want to add an optional note, so that the owner has useful details.

- Phone number or email in the note shows a share warning; continuing requires a tick
- Emoji picker available

### TK-15 · Choose how to get replies

*Must · M · M1 Finder web and accounts*

As a finder, I want to get replies by email, phone or stay anonymous, so that my details stay private.

- Email or phone is hidden from the owner and relayed
- Anonymous finders see replies only while the page is open

### TK-16 · Thank-you page with live reply

*Must · M · M1 Finder web and accounts*

As a finder, I want to see and answer the owner's reply, so that we can arrange the return.

- Owner reply appears live; finder can reply with emoji
- Link to the handover check
- Invite card: protect your own things, first tag offer

### TK-17 · Check the handover code

*Should · S · M2 Owner app core*

As a finder or desk staff, I want to check the owner's handover code before handing over, so that only the real owner gets it.

- 6-digit code checked against the return; clear match or no-match message
- Attempts are rate-limited

### TK-18 · No reply yet

*Should · S · M2 Owner app core*

As a finder, I want to know what to do if the owner doesn't answer, so that I'm not left waiting.

- After the wait time the page explains the backup contact was alerted and offers 'I handed it to staff'

### TK-19 · Report a tag or message

*Must · S · M1 Finder web and accounts*

As a finder, I want to report abuse, so that the platform stays safe.

- Reasons list; 112 note for emergencies; report goes to moderation

### TK-20 · Legal footer on finder pages

*Must · S · M1 Finder web and accounts*

As a finder, I want to reach Impressum, privacy and terms, so that Tagkin meets German law.

- Footer on every finder page


## E3 · Tags

Owners create, customise, test and manage tags for their belongings.

### TK-30 · Create a tag: type, details, message

*Must · L · M2 Owner app core*

As a owner, I want to create a tag for a belonging, so that finders know what to do.

- Choose type of tag (sticker, keychain, pet tag, luggage label, lock screen); tag type item, travel or pet is locked after creation
- Details per type: name and photo; travel fields change with transport mode; pet temperament and care notes
- Finder message: template or own text, 160 characters, warning on contact details, emoji picker, live preview

### TK-31 · Customise the tag

*Must · M · M2 Owner app core*

As a owner, I want to choose shape and colour and see the result, so that I know what I'll receive.

- Six colours fill the tag; QR stays black on white
- Size, material and price shown
- Lock screen leads to 'Make it live'; printed types lead to ordering

### TK-32 · Free phone tag and lock screen image

*Must · M · M2 Owner app core*

As a new owner, I want a free lock-screen tag, so that I can try Tagkin before buying.

- One free tag per account: the phone lock-screen tag
- Set as lock screen saves the image
- Retiring it frees the slot; codes never return

### TK-33 · My tags list

*Must · M · M2 Owner app core*

As a owner, I want to see all my tags and their state, so that I know what's protected.

- Each row: name, code, state badge (normal, lost, return active), QR button
- + New starts a printed tag when the free tag is used

### TK-34 · Edit message and contacts

*Must · M · M2 Owner app core*

As a owner, I want to edit the finder message and contacts any time, so that details stay current.

- Always editable, also during Lost mode or a return
- Backup contact with alert-after time; never shown to finders

### TK-35 · Locked details during Lost mode or a return

*Must · S · M2 Owner app core*

As a finder, I want the item details not to change during a return, so that I can trust what I see.

- Name, photo and description locked in lost and return_active states; UI shows the lock

### TK-36 · QR code and test scan

*Must · S · M2 Owner app core*

As a owner, I want to show my QR and test it with another phone, so that I know it works.

- Test mode for 10 minutes: finder page shows a Test banner, no alerts
- Save image and share

### TK-37 · Status update for finders

*Should · S · M2 Owner app core*

As a owner, I want to post a short status like 'Arrived in Dubai', so that finders know where to bring it.

- City level only; dates and times rejected
- Hides after the trip or 7 days; can be turned off

### TK-38 · Retire a tag

*Must · S · M2 Owner app core*

As a owner, I want to retire a tag I no longer need, so that it stops working for good.

- Confirmation explains the code never returns
- Retired tags keep no personal data

### TK-39 · Scan history

*Should · S · M2 Owner app core*

As a owner, I want to see when and where my tag was scanned, so that I have a clue where it is.

- Time and city per scan; exact place only if a finder shared it


## E4 · Lost mode and returns

Owners and finders coordinate a return through relayed, translated messages.

### TK-40 · Mark as lost

*Must · M · M2 Owner app core*

As a owner, I want to mark a tag as lost in the app or on the web, so that finders see it's missing and I get alerts.

- Confirmation explains locks and no public reward
- Every scan alerts with city; can't be turned off while lost
- 'I found it myself' returns to normal

### TK-41 · Relayed, translated conversation

*Must · L · M2 Owner app core*

As a owner and finder, I want to message each other without sharing contact details, so that we stay private.

- Messages relayed by Tagkin; translated both ways with Show original
- Contact details in text trigger a share warning
- Emoji in every message box
- Failed messages show 'Not sent · Tap to retry'

### TK-42 · Safe place report with photo and map

*Should · M · M2 Owner app core*

As a owner, I want to see the finder's photo, map pin and address, so that I can collect it.

- Open in Maps; 'I picked it up' closes the return
- Exact pin only when the finder shared location

### TK-43 · Handover code

*Should · S · M2 Owner app core*

As a owner, I want a handover code to show when I collect, so that nobody else can claim my item.

- 6-digit code per return, can be regenerated
- Never shown in messages

### TK-44 · Close a return

*Must · S · M2 Owner app core*

As a owner, I want to mark the item as returned, with a private thank-you, so that the tag goes back to normal.

- Locks lift; return also closes after 14 days without messages

### TK-45 · Report or block a finder

*Must · S · M2 Owner app core*

As a owner, I want to block or report a finder, so that I'm protected from abuse and scams.

- Block stops messages about that tag
- Anti-scam note: never pay before you have the item


## E5 · Ordering and payment

Owners order printed tags, pay and track delivery.

### TK-50 · Order a printed tag

*Must · M · M3 Ordering and payment*

As a owner, I want to order my customised tag in copies, so that I get a durable tag.

- Shows my design, colour and size; copies of the same code
- Free shipping over €15; first-tag offer once per account as a discount line

### TK-51 · Delivery details before payment

*Must · S · M3 Ordering and payment*

As a owner, I want to enter my address before any pay button, so that I know where it goes.

- Name, street, postcode, city, country, optional courier phone
- Address shared only with the print partner

### TK-52 · Choose how to pay

*Must · L · M3 Ordering and payment*

As a owner, I want to pay with Apple Pay or Google Pay, card, PayPal or Klarna, so that I can use what I trust.

- Stripe payment sheet; button names amount and method
- Personalised goods notice (no 14-day return; faulty replaced) and Terms before paying
- Declined payment shows a clear error; card not charged

### TK-53 · Send paid orders to the print partner

*Must · L · M3 Ordering and payment*

As a Tagkin, I want paid orders sent to the print partner automatically, so that tags are printed without manual work.

- Order created at the partner after payment webhook
- Partner status and tracking update the order
- Partner failure alerts admin and triggers refund

### TK-54 · Tag live from order

*Must · S · M3 Ordering and payment*

As a owner, I want my new tag to work as soon as I order, so that I'm protected before it arrives.

- Own-order tags become normal at payment
- 'Your tag is live and on its way'

### TK-55 · Orders list and emails

*Must · M · M3 Ordering and payment*

As a owner, I want to follow my orders, so that I know when tags arrive.

- States: in production, shipped, delivered
- Emails: order confirmed, shipped with tracking


## E6 · Gifting and activation

People gift blank tags; recipients activate them safely with a PIN.

### TK-60 · Gift blank tags

*Should · M · M4 Gifting and activation*

As a buyer, I want to gift blank tags of a chosen type and colour, so that someone I care about can protect their things.

- From Create a tag: For myself / Gift a tag
- Gift note, recipient address, hide prices on packing slip
- Same payment step as orders

### TK-61 · Gift card with activation PIN

*Should · M · M4 Gifting and activation*

As a recipient, I want a PIN on the gift card, not on the tag, so that only I can claim the tags.

- Unclaimed codes and a hashed PIN created per gift order
- PIN printed on the gift card by the print partner

### TK-62 · Activate a tag with a PIN

*Should · M · M4 Gifting and activation*

As a recipient, I want to scan or type the code and enter the PIN, so that the tag becomes mine.

- Unclaimed → normal after PIN; 5 attempts then wait
- Then type, details and message; style and order steps skipped
- Activate another tag from the success screen
- Unclaimed tag scanned by a phone camera deep-links to the app with the code


## E7 · Notifications

The right person hears about the right event, with fallbacks.

### TK-70 · Notification permission at the right time

*Must · S · M2 Owner app core*

As a owner, I want to be asked for notifications after my first tag, so that I understand why.

- Asked after the first tag is live or ordered
- Off: banner on My tags explains how to turn on

### TK-71 · Event notifications with fallback

*Must · M · M2 Owner app core*

As a owner, I want push for scans, reports and messages, email if push fails, so that I never miss a find.

- Matrix in SYSTEM-LOGIC.md section 4
- Settings: scans, messages, email copy, orders, product news

### TK-72 · Backup contact alert

*Should · M · M2 Owner app core*

As a owner, I want my backup contact alerted if I don't reply, so that a finder isn't left waiting.

- Scheduled job after the wait time; finder page updated


## E8 · Website, legal and owner web

Public website, legal pages and the owner dashboard on the web.

### TK-80 · Website home, privacy and support

*Must · M · M5 Launch readiness*

As a visitor, I want to learn what Tagkin is and get help, so that I can decide and get support.

- Home, privacy in plain words, support with FAQ and email
- Required URLs for the stores

### TK-81 · Legal texts and Impressum

*Must · M · M5 Launch readiness*

As a Tagkin, I want privacy policy, terms and Impressum published, so that we can launch legally.

- Linked from website, finder pages, emails and the app

### TK-82 · Owner web dashboard

*Must · M · M1 Finder web and accounts*

As a owner, I want to see my tags, messages and orders on the web, so that I can act without my phone.

- My tags with Mark as lost; messages; account

### TK-98 · Store listings and privacy labels

*Must · M · M5 Launch readiness*

As a Tagkin, I want complete App Store and Google Play listings, so that the app passes review.

- Name, subtitle, description, keywords, screenshots re-shot from the real app, support and privacy URLs
- Apple privacy labels and Google Data safety match what the app collects
- Age rating questionnaires; review notes and a test account


## E9 · Platform and operations

Moderation, scheduled jobs, languages, accessibility and analytics.

### TK-90 · Moderation queue

*Must · M · M5 Launch readiness*

As a Tagkin, I want to review reports and blocks, so that abuse is handled.

- Admin list of reports with actions; every report reviewed

### TK-91 · Scheduled jobs

*Must · M · M2 Owner app core*

As a Tagkin, I want returns, test mode, status updates, retention and reconciliation handled automatically, so that the system stays correct.

- Jobs listed in SYSTEM-LOGIC.md section 7

### TK-92 · Core languages

*Must · M · M5 Launch readiness*

As a user, I want the app and finder pages in my language, so that I understand every step.

- All UI text externalised; core languages translated; right-to-left layout supported

### TK-93 · Accessibility

*Must · M · M5 Launch readiness*

As a user with a disability, I want to use Tagkin with a screen reader and large text, so that Tagkin works for me.

- WCAG AA contrast; labels; focus order; text scaling to 200%; reduced motion

### TK-94 · Privacy-friendly analytics

*Should · S · M5 Launch readiness*

As a product owner, I want to measure activation, scans, returns and orders, so that I can learn what works.

- Only what the store privacy labels declare; no data selling

### TK-95 · Invite a friend

*Could · S · M5 Launch readiness*

As a owner, I want to share an invite link, so that friends can protect their things too.

- Share link; referral discount on a printed tag

### TK-96 · Tablet layout

*Could · S · M5 Launch readiness*

As a owner on a tablet, I want list and detail side by side, so that the app uses the screen well.

- Layout from the tablet frame; phone layout otherwise

### TK-97 · Empty, loading, offline and error states

*Must · M · M2 Owner app core*

As a user, I want clear screens when there's nothing yet, while loading, offline or when something fails, so that I always know what's happening and what to do.

- Designs: empty tags, messages and orders; loading skeletons; offline banner; payment failed; message not sent; code not found
- Permission turned off: camera and notifications recovery screens

### TK-99 · Premium interest: Notify me

*Should · S · M5 Launch readiness*

As a product owner, I want owners to register interest in Premium, so that I build Premium only if there is demand.

- Plan screen shows Free and Premium (later) with Notify me
- Count of Notify me taps visible in analytics; confirmation message to the owner

## Won't have in this release

- Premium subscription (later; Notify me measures demand)
- Shop packs with scratch panels (later; PIN flow is ready)
- SMS replies and WhatsApp (later)
- NFC tags, family sharing, ownership transfer (later)
- Care tags for children and older relatives (phase 2)
