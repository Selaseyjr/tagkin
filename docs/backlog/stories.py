"""Tagkin product backlog: single source for BACKLOG.md and the GitHub issues.

Each story: id, epic, title, as/want/so, acceptance criteria, priority (MoSCoW), size (S, M, L), milestone.
Run: python3 docs/backlog/stories.py            -> writes docs/BACKLOG.md
     python3 docs/backlog/stories.py --issues   -> prints issue payloads (used by create_issues.sh)
"""
import json
import sys
from pathlib import Path

EPICS = {
    "E1": ("Accounts and sign-in", "Owners can create an account, sign in on any device, recover access and control their data."),
    "E2": ("Finder web", "Anyone who finds a tagged item can report it from a browser, privately, without an app."),
    "E3": ("Tags", "Owners create, customise, test and manage tags for their belongings."),
    "E4": ("Lost mode and returns", "Owners and finders coordinate a return through relayed, translated messages."),
    "E5": ("Ordering and payment", "Owners order printed tags, pay and track delivery."),
    "E6": ("Gifting and activation", "People gift blank tags; recipients activate them safely with a PIN."),
    "E7": ("Notifications", "The right person hears about the right event, with fallbacks."),
    "E8": ("Website, legal and owner web", "Public website, legal pages and the owner dashboard on the web."),
    "E9": ("Platform and operations", "Moderation, scheduled jobs, languages, accessibility and analytics."),
}

MILESTONES = {
    "M1": ("M1 Finder web and accounts", "A finder can report a tag; an owner can sign in and receive it."),
    "M2": ("M2 Web beta: create, order and pay", "Guests create and customise on the web, sign up when needed, order and pay. Web beta release."),
    "M3": ("M3 Owner app core", "Owners create and manage tags, run Lost mode and returns in the app."),
    "M4": ("M4 Gifting and activation", "Blank tags can be gifted (guest checkout) and activated with a PIN."),
    "M5": ("M5 Launch readiness", "Website, legal, accessibility, languages, operations and store submission."),
}

S = []


def story(id, epic, title, who, want, so, ac, pri, size, ms):
    S.append(dict(id=id, epic=epic, title=title, who=who, want=want, so=so, ac=ac, pri=pri, size=size, ms=ms))


# ---------- E1 Accounts and sign-in ----------
story("TK-1", "E1", "Sign up and sign in with an email code", "new owner", "to sign up with my email and a one-time code only when it's needed", "I don't need a password or an account just to look around",
      ["Sign-up is asked only at Make it live, Continue to payment or before an activation PIN; returning owners use Welcome back", "Email is required and verified with a 6-digit code valid for 10 minutes", "After 5 wrong attempts the user waits before trying again", "Resend is possible after 30 seconds; the screen suggests checking spam or using another email", "Terms must be accepted before the account is created; guest drafts are attached to the new account"], "Must", "M", "M1")
story("TK-2", "E1", "First launch intro", "new owner", "to understand Tagkin in two screens", "I know what I'm signing up for",
      ["Welcome and 'Private by default' screens, then terms", "'I have an account' skips to sign-in"], "Should", "S", "M3")
story("TK-3", "E1", "Sign in on the web", "owner whose phone is lost", "to sign in at tagkin.app on any device", "I can still use Lost mode and reply",
      ["Same email-code sign-in as the app", "After sign-in the owner sees My tags with Lost mode and messages"], "Must", "M", "M1")
story("TK-4", "E1", "Account recovery", "owner who lost access to my email", "to recover my account with a recovery phone or backup email", "I don't lose my tags",
      ["Recovery phone receives an SMS code; backup email receives an email code", "Prompted after the first tag via a banner on My tags", "Support can recover an account with an order number (manual process)"], "Must", "M", "M3")
story("TK-5", "E1", "Signed-in devices", "owner", "to see and sign out devices", "I stay in control if a device is lost",
      ["List shows device and last use", "Sign out ends that session immediately"], "Should", "S", "M3")
story("TK-6", "E1", "Delete my account", "owner", "to delete my account in the app", "my data is gone when I leave",
      ["Shows what happens: tags retired, messages and photos deleted, invoices kept as the law requires", "Requires confirmation; sends a confirmation email", "Warns if a return is still open"], "Must", "M", "M3")
story("TK-7", "E1", "Download my data", "owner", "to download my data", "I can see what Tagkin stores",
      ["Request in Privacy and data; email with a download link valid 24 hours"], "Must", "S", "M5")
story("TK-8", "E1", "Language and appearance", "owner", "to choose my language and light, dark or system appearance", "the app suits me",
      ["Core languages: English (UK, US), German, French, Dutch, Polish, Spanish, Italian", "Appearance default is match system"], "Should", "S", "M3")

# ---------- E2 Finder web ----------
story("TK-10", "E2", "Open a tag from its QR code", "finder", "to see the owner's message when I scan a tag", "I know what to do",
      ["tagkin.app/TK-… shows the photo, message translated to my browser language and Show original", "No app or account is needed", "Lost tags show 'This item is missing'; never the word stolen", "Travel tags show destination and operator only; pet tags hide care notes behind a tap"], "Must", "M", "M1")
story("TK-11", "E2", "Type a code when the QR won't scan", "finder", "to type the code printed on the tag", "I can still report it",
      ["Case- and dash-insensitive", "Wrong code shows a clear error; lookups are rate-limited", "Retired tags show 'no longer active'; unclaimed tags show 'not set up yet'"], "Must", "S", "M1")
story("TK-12", "E2", "Report where the item is", "finder", "to say where the item is now and where exactly", "the owner can get it back",
      ["Choose with me, handed to staff, or left in a safe place", "Place suggestions after 2 letters; free text always allowed", "Share item location asks browser permission; denied means city only"], "Must", "M", "M1")
story("TK-13", "E2", "Leave it in a safe place with a photo", "finder who can't keep the item", "to add a photo, note and address", "the owner can find the exact spot",
      ["Only for 'left in a safe place'", "Photo location data (EXIF) removed before upload", "Address from shared location or typed text, editable"], "Should", "M", "M1")
story("TK-14", "E2", "Add a note safely", "finder", "to add an optional note", "the owner has useful details",
      ["Phone number or email in the note shows a share warning; continuing requires a tick", "Emoji picker available"], "Must", "S", "M1")
story("TK-15", "E2", "Choose how to get replies", "finder", "to get replies by email, phone or stay anonymous", "my details stay private",
      ["Email or phone is hidden from the owner and relayed", "Anonymous finders see replies only while the page is open"], "Must", "M", "M1")
story("TK-16", "E2", "Thank-you page with live reply", "finder", "to see and answer the owner's reply", "we can arrange the return",
      ["Owner reply appears live; finder can reply with emoji", "Link to the handover check", "Report link to copy; the same link is in every email or text; the same device is remembered", "Invite card: protect your own things, first tag offer"], "Must", "M", "M1")
story("TK-17", "E2", "Check the handover code", "finder or desk staff", "to check the owner's handover code before handing over", "only the real owner gets it",
      ["Anyone holding the item can check it from the tag page while a return is open ('Check a handover code'); no session needed", "6-digit code checked against the open return; clear match or no-match message with tries left", "5 attempts, then a 15-minute wait", "After a match, 'I've handed it over' closes the conversation and shows a thank-you page with the protect-your-things offer; from then on the report page only shows the closed state (phone and desktop)"], "Should", "S", "M3")
story("TK-18", "E2", "No reply yet", "finder", "to know what to do if the owner doesn't answer", "I'm not left waiting",
      ["After the wait time the page explains the backup contact was alerted and offers 'I handed it to staff'"], "Should", "S", "M3")
story("TK-19", "E2", "Report a tag or message", "finder", "to report abuse", "the platform stays safe",
      ["Reasons list; choosing one opens a details box (required for 'Something else') with a Report button under it", "After sending, a confirmation sheet: thanks, we review it, the owner won't know who reported; Done returns to the previous page", "112 note for emergencies; report goes to moderation"], "Must", "S", "M1")
story("TK-20", "E2", "Legal footer on finder pages", "finder", "to reach Impressum, privacy and terms", "Tagkin meets German law",
      ["Footer on every finder page"], "Must", "S", "M1")

# ---------- E3 Tags ----------
story("TK-30", "E3", "Create a tag: type, details, message", "owner", "to create a tag for a belonging", "finders know what to do",
      ["Choose type of tag (sticker, keychain, pet tag, luggage label, lock screen); 'What is it for?' only offers item types that fit the shape (shape-fit table, BUSINESS-RULES 3c) and is skipped when only one fits (keychain, pet tag, luggage label, lock screen); tag type item, travel or pet is locked after creation", "Details per type: name required (2 to 40 characters), photo optional but prompted, description optional (120); travel adds a luggage photo and an optional trip (mode, carrier, destination, end date); pet temperament and care notes", "Photos: JPEG, PNG, WebP or HEIC up to 10 MB; resized to 1600 px and location data removed; the chosen photo fills its box, opens full screen to check, with Use, Replace and Remove", "Draft rules: back keeps what was entered; choosing a different type or tag style clears the item details; leaving the flow with unsaved input asks Discard or Keep editing; a new flow starts blank", "Customise preview opens full screen and returns to the same choices", "Finder message: suggested text per type, accepted with one tap (Use this message), or own text, 160 characters, warning on contact details, emoji picker, live preview"], "Must", "L", "M3")
story("TK-31", "E3", "Customise the tag", "owner", "to choose shape, size, colour, finish and a short label and see the result", "my tag feels like mine and I know what I'll receive",
      ["Shape, size (where offered), 8 colours and 2 gradients, finish by product (matte, gloss, holo, glow, reflective) and an optional label of up to 12 characters", "Live preview; QR stays black on white; label blocks phone numbers and emails", "Size, material, finish and price shown; extra finishes priced before checkout", "Lock screen leads to 'Make it live'; printed types lead to ordering", "Shape only offers shapes that fit the item type (item: sticker, keychain; travel: luggage label, sticker; pet: pet tag, so no shape choice); the lock-screen tag shows no shape choice; a blank tag offers every printed shape"], "Must", "M", "M3")
story("TK-32", "E3", "Free phone tag and lock screen image", "new owner", "a free lock-screen tag", "I can try Tagkin before buying",
      ["One free tag per account: the phone lock-screen tag", "Set as lock screen saves the image", "Retiring it frees the slot; codes never return"], "Must", "M", "M3")
story("TK-33", "E3", "My tags list", "owner", "to see all my tags and their state", "I know what's protected",
      ["Each row: name, code, state badge (normal, lost, return active), QR button", "+ New starts a printed tag when the free tag is used"], "Must", "M", "M3")
story("TK-34", "E3", "Edit message and contacts", "owner", "to edit the finder message and contacts any time", "details stay current",
      ["Always editable, also during Lost mode or a return", "Backup contact with alert-after time; never shown to finders"], "Must", "M", "M3")
story("TK-35", "E3", "Locked details during a return", "finder", "the item details not to change during a return", "I can trust what I see",
      ["Name, photo and description locked in return_active only; UI shows the lock; in Lost mode they stay editable"], "Must", "S", "M3")
story("TK-36", "E3", "QR code and test scan", "owner", "to show my QR and test it with another phone", "I know it works",
      ["Test mode for 10 minutes: finder page shows a Test banner, no alerts", "Save image and share"], "Must", "S", "M3")
story("TK-37", "E3", "Status update for finders", "owner", "to post a short status like 'Arrived in Dubai'", "finders know where to bring it",
      ["City level only; dates and times rejected", "Hides after the trip or 7 days; can be turned off"], "Should", "S", "M3")
story("TK-38", "E3", "Retire a tag", "owner", "to retire a tag I no longer need", "it stops working for good",
      ["Confirmation explains the code never returns", "Retired tags keep no personal data"], "Must", "S", "M3")
story("TK-39", "E3", "Scan history", "owner", "to see when and where my tag was scanned", "I have a clue where it is",
      ["Time and city per scan; exact place only if a finder shared it", "Each tag shows only its own scans; a new tag starts with 'No scans yet' and a prompt to test it", "Lost mode lists scans since it was marked lost; test scans are labelled and send no alert"], "Should", "S", "M3")

# ---------- E4 Lost mode and returns ----------
story("TK-40", "E4", "Mark as lost", "owner", "to mark a tag as lost in the app or on the web", "finders see it's missing and I get alerts",
      ["Confirmation explains locks and no public reward", "Every scan alerts with city; can't be turned off while lost", "'I found it myself' returns to normal"], "Must", "M", "M3")
story("TK-41", "E4", "Relayed, translated conversation", "owner and finder", "to message each other without sharing contact details", "we stay private",
      ["Messages relayed by Tagkin; translated both ways with Show original", "Contact details in text trigger a share warning", "Emoji in every message box", "Failed messages show 'Not sent · Tap to retry'"], "Must", "L", "M3")
story("TK-42", "E4", "Safe place report with photo and map", "owner", "to see the finder's photo, map pin and address", "I can collect it",
      ["Open in Maps; 'I picked it up' closes the return", "Exact pin only when the finder shared location"], "Should", "M", "M3")
story("TK-43", "E4", "Handover code", "owner", "a handover code to show when I collect", "nobody else can claim my item",
      ["6-digit code per return, can be regenerated", "Never shown in messages"], "Should", "S", "M3")
story("TK-44", "E4", "Close a return", "owner", "to mark the item as returned, with a private thank-you", "the tag goes back to normal",
      ["Locks lift; return also closes after 14 days without messages"], "Must", "S", "M3")
story("TK-45", "E4", "Report or block a finder", "owner", "to block or report a finder", "I'm protected from abuse and scams",
      ["Block stops messages about that tag", "Anti-scam note: never pay before you have the item"], "Must", "S", "M3")

# ---------- E5 Ordering and payment ----------
story("TK-50", "E5", "Order a printed tag", "owner", "to order my customised tag in copies", "I get a durable tag",
      ["Shows my design, colour and size; copies of the same code", "Free shipping over €15; first-tag offer once per account as a discount line"], "Must", "M", "M2")
story("TK-51", "E5", "Order details: copies and delivery on one page", "owner", "to enter my address on the same page as my order", "ordering is quick and I know where it goes",
      ["Order details holds copies and delivery details on one page, before any pay button", "Signed-in owners see their saved address as a card with Change; guests see the form", "Name, street, postcode, city, country, optional courier phone", "Address shared only with the print partner"], "Must", "S", "M2")
story("TK-52", "E5", "Choose how to pay", "owner", "to pay with Apple Pay or Google Pay, card, PayPal or Klarna", "I can use what I trust",
      ["Stripe payment sheet; button names amount and method", "Personalised goods notice (no 14-day return; faulty replaced) and Terms before paying", "Declined payment shows a clear error; card not charged"], "Must", "L", "M2")
story("TK-53", "E5", "Send paid orders to the print partner", "Tagkin", "paid orders sent to the print partner automatically", "tags are printed without manual work",
      ["Order created at the partner after payment webhook", "Partner status and tracking update the order", "Partner failure alerts admin and triggers refund"], "Must", "L", "M2")
story("TK-54", "E5", "Tag live from order", "owner", "my new tag to work as soon as I order", "I'm protected before it arrives",
      ["Own-order tags become normal at payment", "'Your tag is live and on its way'"], "Must", "S", "M2")
story("TK-55", "E5", "Orders list and emails", "owner", "to follow my orders", "I know when tags arrive",
      ["A paid order appears at the top of Orders straight away (own, blank and gift orders)", "Stages: Paid, Sent to print, Printing, Quality check, Shipped, Out for delivery, Delivered, each with a date or expected date", "Problems shown with a plain reason: Reprinting (failed print check, +2 days, free), Delayed, Delivery failed (owner checks the address, free resend), Cancelled (refund), Replacement on its way", "Tapping an order opens Order details: timeline, items and colour, which tag it is for, delivery address, amount and payment method", "Actions by stage: cancel before printing; change address until shipped; track once shipped; send again after a failed delivery; report a problem after delivery (damaged, never arrived, wrong colour or size, QR won't scan) gets a free replacement with no return", "Order a tag and Gift a tag start a fresh journey with empty fields", "Emails: order confirmed, shipped with tracking, delayed, delivery failed, cancelled and refunded"], "Must", "L", "M2")

# ---------- E6 Gifting and activation ----------
story("TK-60", "E6", "Gift blank tags", "buyer", "to gift blank tags of a chosen type and colour", "someone I care about can protect their things",
      ["From Create a tag: For myself / Gift a tag", "Gift note, recipient address, hide prices on packing slip", "Same payment step as orders"], "Should", "M", "M4")
story("TK-61", "E6", "Gift card with activation PIN", "recipient", "a PIN on the gift card, not on the tag", "only I can claim the tags",
      ["Unclaimed codes and a hashed PIN created per gift order", "PIN printed on the gift card by the print partner"], "Should", "M", "M4")
story("TK-62", "E6", "Activate a tag with a PIN", "recipient", "to scan or type the code and enter the PIN", "the tag becomes mine",
      ["Unclaimed → normal after PIN; 5 attempts then wait", "Then type, details and message; style and order steps skipped", "Activate another tag from the success screen", "Unclaimed tag scanned by a phone camera deep-links to the app with the code"], "Should", "M", "M4")

# ---------- E7 Notifications ----------
story("TK-70", "E7", "Notification permission at the right time", "owner", "to be asked for notifications after my first tag", "I understand why",
      ["Asked after the first tag is live or ordered", "Off: banner on My tags explains how to turn on"], "Must", "S", "M3")
story("TK-71", "E7", "Event notifications with fallback", "owner", "push for scans, reports and messages, email if push fails", "I never miss a find",
      ["Matrix in SYSTEM-LOGIC.md section 4", "Settings: scans, messages, email copy, orders, product news"], "Must", "M", "M3")
story("TK-72", "E7", "Backup contact alert", "owner", "my backup contact alerted if I don't reply", "a finder isn't left waiting",
      ["Scheduled job after the wait time; finder page updated"], "Should", "M", "M3")

# ---------- E8 Website, legal and owner web ----------
story("TK-80", "E8", "Website home, privacy and support", "visitor", "to learn what Tagkin is and get help", "I can decide and get support",
      ["Home, privacy in plain words, support with FAQ and email", "Required URLs for the stores"], "Must", "M", "M5")
story("TK-81", "E8", "Legal texts and Impressum", "Tagkin", "privacy policy, terms and Impressum published", "we can launch legally",
      ["Linked from website, finder pages, emails and the app"], "Must", "M", "M5")
story("TK-82", "E8", "Owner web dashboard", "owner", "to see my tags and finder reports on the web", "I can act without my phone",
      ["My tags shows each tag's photo, name and state (active, lost)", "Mark as lost and Mark as found work on the web through the same database functions as the app", "Finder reports appear per tag with place, time (city level unless shared) and note", "Orders appear here from M2; account shows email and sign out", "Edit a tag's name and photo (not during a return); set up blank tags with the shape-fit rule", "Order rows open the same Order details as the app", "Creating tags and ordering stay in the app: web buttons open a Get the app sheet; a sidebar card offers instant alerts in the app"], "Must", "M", "M1")
story("TK-103", "E7", "Finder report alert by email", "owner", "an email when someone reports my tag", "I hear about a find before the app exists",
      ["A new report emails the owner within the event flow: item, where now, place, note, translated to the owner's language with the original kept", "The email links to the report on tagkin.app (sign-in if needed); no finder contact details in the email", "Sent through Brevo from tagkin.app; a failed send is retried and logged", "Push takes over in M3 (TK-71); email stays the fallback"], "Must", "S", "M1")
story("TK-104", "E4", "Reply to a finder on the web", "owner", "to reply to a finder from tagkin.app", "we can arrange the return without the app",
      ["Owner writes in their language; the finder sees it translated with Show original", "Finder gets the reply live on the open page, else by email if chosen; anonymous finders on the page only", "Finder email replies come back into the conversation (Brevo inbound)", "Contact details typed in a message show the share warning", "Messages are rate-limited per return"], "Must", "M", "M1")

# ---------- E9 Platform and operations ----------
story("TK-90", "E9", "Moderation queue", "Tagkin", "to review reports and blocks", "abuse is handled",
      ["Admin list of reports with actions; every report reviewed"], "Must", "M", "M5")
story("TK-91", "E9", "Scheduled jobs", "Tagkin", "returns, test mode, status updates, retention and reconciliation handled automatically", "the system stays correct",
      ["Jobs listed in SYSTEM-LOGIC.md section 7"], "Must", "M", "M3")
story("TK-92", "E9", "Core languages", "user", "the app and finder pages in my language", "I understand every step",
      ["All UI text externalised; core languages translated; right-to-left layout supported"], "Must", "M", "M5")
story("TK-93", "E9", "Accessibility", "user with a disability", "to use Tagkin with a screen reader and large text", "Tagkin works for me",
      ["WCAG AA contrast; labels; focus order; text scaling to 200%; reduced motion"], "Must", "M", "M5")
story("TK-94", "E9", "Privacy-friendly analytics", "product owner", "to measure activation, scans, returns and orders", "I can learn what works",
      ["Only what the store privacy labels declare; no data selling"], "Should", "S", "M5")
story("TK-95", "E9", "Invite a friend", "owner", "to share an invite link", "friends can protect their things too",
      ["Share link; referral discount on a printed tag"], "Could", "S", "M5")
story("TK-96", "E9", "Tablet layout", "owner on a tablet", "list and detail side by side", "the app uses the screen well",
      ["Layout from the tablet frame; phone layout otherwise"], "Could", "S", "M5")

story("TK-97", "E9", "Empty, loading, offline and error states", "user", "clear screens when there's nothing yet, while loading, offline or when something fails", "I always know what's happening and what to do",
      ["Designs: empty tags, messages and orders; loading skeletons; offline banner; payment failed; message not sent; code not found", "Permission turned off: camera and notifications recovery screens"], "Must", "M", "M3")
story("TK-98", "E8", "Store listings and privacy labels", "Tagkin", "complete App Store and Google Play listings", "the app passes review",
      ["Name, subtitle, description, keywords, screenshots re-shot from the real app, support and privacy URLs", "Apple privacy labels and Google Data safety match what the app collects", "Age rating questionnaires; review notes and a test account"], "Must", "M", "M5")

story("TK-99", "E9", "Premium interest: Notify me", "product owner", "owners to register interest in Premium", "I build Premium only if there is demand",
      ["Plan screen shows Free and Premium (later) with Notify me", "Count of Notify me taps visible in analytics; confirmation message to the owner"], "Should", "S", "M5")

story("TK-100", "E1", "Explore and create without an account", "visitor", "to explore, create and customise a tag before signing up", "I see my tag before giving my email",
      ["Welcome leads straight to Create a tag; no sign-in screen first", "Drafts kept on the device (app) or in the browser (web) until sign-up", "On sign-up, drafts become tags in one transaction; nothing is stored on the server before"], "Must", "M", "M2")
story("TK-101", "E6", "Guest gift checkout", "gift buyer without an account", "to buy a gift with only my email", "I don't need an account for tags I won't own",
      ["Email for receipt and tracking; order status page by link", "Same payment step and personalised-goods notice as other orders"], "Should", "M", "M4")
story("TK-102", "E8", "Create, customise and order on the web", "visitor on tagkin.app", "to create, customise and order a tag in the browser", "the web beta can sell tags before the apps launch",
      ["tagkin.app/create mirrors the app flow: type, details, message, customise, order, delivery, pay", "Sign-up at Continue to payment; tags live from order", "Works on phone and desktop browsers"], "Must", "L", "M2")
story("TK-105", "E3", "Order a blank tag and set it up later", "owner", "to order a tag before I have the item", "it's ready when my new bag, phone or pet arrives",
      ["'Order a blank tag' on Create a tag: choose style and design, no item details", "Order and pay as usual; the tag is mine from payment and shows 'Set up' in My tags", "The blank tag keeps the shape chosen at order; set-up only offers item types that fit it and skips the type step when only one fits", "Ordering n blank tags creates n tags in My tags", "The lock-screen tag is never offered as a blank (it is digital and free)", "Set up later in the app or on the web: type, name, photo, message; no PIN", "Until set up, finders see 'not set up yet' and I get a scan alert", "After setting one up, 'Set up next blank tag (n left)' continues straight to the next"], "Should", "M", "M2")
story("TK-106", "E3", "Edit item name, photo and description later", "owner", "to update my item details after creating the tag", "I can add a photo once the item arrives",
      ["Item name and photo row, or tapping the photo on the tag (active or lost), opens an edit sheet with the photo preview", "A new photo or name shows everywhere the item appears: My tags, tag screens, Messages and the finder page", "Name required (2 to 40), description optional (120)", "Locked only during a return (a finder has reported it); in Lost mode a better photo helps finders", "Tags without a photo show 'add a photo' in My tags", "My tags shows one nudge card at a time (photo, then backup contact, then recovery phone); each can be dismissed"], "Must", "S", "M3")
story("TK-107", "E3", "Undo instead of confirm for reversible actions", "owner", "to undo a quick action for a few seconds", "I move fast without fear of mistakes",
      ["I found it myself and Mark as returned apply at once with a 5-second Undo bar", "Mark as lost, retire and delete keep a confirmation", "Undo restores the previous state exactly"], "Should", "S", "M3")
story("TK-108", "E3", "Quick actions from My tags and notifications", "owner", "to act on a tag without opening it", "urgent things take one tap",
      ["⋯ on each tag: Mark as lost or I found it myself, Show QR, Edit name and photo", "Reply to a finder from the notification; the reply is relayed and translated"], "Should", "M", "M3")
story("TK-109", "E4", "Suggested replies in the conversation", "owner", "to answer a finder with one tap", "I reply quickly on the move",
      ["Chips above the composer: Thank you so much!, I'll pick it up today, Please hand it to staff, Where exactly is it?", "A chip fills the reply box; I can edit before sending", "Chips are translated for the finder like any message"], "Could", "S", "M3")

# Definition of Ready evidence per story (step 7 refinement). Stories listed here are Ready.
READY = {
    "TK-1": dict(screens=["Setup 3 · Save your tag (sign up when needed)", "Owner 1 · Welcome back (sign in)", "Owner 2 · Enter code", "Email 0 · Sign-in code"], rules=["1b"], logic=["4", "6", "8"], deps=["Sprint 0: Supabase Auth with email OTP; Brevo SMTP on tagkin.app (domain by 15 Nov)", "Guest draft claim (TK-100) lands in M2; M1 covers sign-in only"]),
    "TK-3": dict(screens=["Web · Owner sign-in", "Owner 2 · Enter code"], rules=["1b"], logic=["4", "8"], deps=["TK-1"]),
    "TK-10": dict(screens=["Finder 1 · Owner message", "Finder 1b · Lost mode", "Finder 1t · Travel tag", "Finder 1p · Pet tag", "Finder T · Owner test scan", "Loading · Finder page", "Desktop · Finder owner message"], rules=["4", "6", "7"], logic=["2", "3", "5", "8"], deps=["Sprint 0: tag and item tables with seed tags (no create flow until M2)", "DeepL key (ADR 0007); cache translations per message and language"]),
    "TK-11": dict(screens=["Finder 0 · Enter code", "Finder 0b · Code not found", "Finder U · Tag not set up yet", "Finder X · Tag not active"], rules=["4"], logic=["6", "8"], deps=["TK-10", "Code alphabet in packages/shared"]),
    "TK-12": dict(screens=["Finder 2 · Where is it now?", "Finder 3 · Where exactly?", "Desktop · Finder where exactly", "Loading · Sending report"], rules=["6", "7"], logic=["2", "3", "5", "6"], deps=["TK-10", "Google Places (New) key with quota and billing alert (ADR 0008)"]),
    "TK-13": dict(screens=["Finder 3b · Show where you left it"], rules=["6"], logic=["2", "5", "6"], deps=["TK-12", "Private storage bucket and EXIF-strip function"]),
    "TK-14": dict(screens=["Finder 4 · Anything else?"], rules=["6", "7"], logic=["6"], deps=["TK-12", "Phone and email detection (libphonenumber-js) in packages/shared"]),
    "TK-15": dict(screens=["Finder 5 · Want a reply?"], rules=["6"], logic=["2", "4", "6"], deps=["TK-12", "Encryption at rest for finder contacts"]),
    "TK-16": dict(screens=["Finder 6 · Thank you", "Email 2 · Finder: owner replied"], rules=["6"], logic=["4", "5"], deps=["TK-15", "TK-104 for owner replies", "Handover link shows from M3 (TK-17)"]),
    "TK-19": dict(screens=["Finder R · Report this tag"], rules=["7"], logic=["2", "4"], deps=["TK-10", "Moderation review is manual until TK-90"]),
    "TK-20": dict(screens=["Finder 1 · Owner message", "Web · Privacy"], rules=["7"], logic=["9"], deps=["Placeholder legal texts until TK-81 (M5)"]),
    "TK-82": dict(screens=["Web · Owner dashboard", "Owner 12 · Finder report alert"], rules=["6", "7"], logic=["3", "8"], deps=["TK-3", "mark_lost and mark_found database functions"]),
    "TK-103": dict(screens=["Email 1 · Owner: item found", "Owner 12 · Finder report alert"], rules=["6"], logic=["4", "5"], deps=["TK-12", "Brevo verified on tagkin.app (ADR 0005)"]),
    "TK-104": dict(screens=["Owner 5 · Finder message", "Owner 13b · Anonymous finder", "Email 2 · Finder: owner replied"], rules=["6", "7"], logic=["2", "4", "5", "6"], deps=["TK-82", "TK-15", "Brevo inbound parsing (ADR 0005)", "DeepL (ADR 0007)"]),
}

WONT = [
    "Premium subscription (later; Notify me measures demand)",
    "Ghana launch with a local payment provider and cedi prices (later; data model ready)",
    "Family sharing and ownership transfer screens (later; data model ready)",
    "Shop packs with scratch panels (later; PIN flow is ready)",
    "SMS replies and WhatsApp (later)",
    "NFC tags (later)",
    "Care tags for children and older relatives (phase 2)",
]

DOR = ["Story written as 'As a … I want … so that …'", "Acceptance criteria agreed", "Screens linked (tagkin-screens.html frame names)", "Business rules and SYSTEM-LOGIC.md sections checked", "Dependencies known; size estimated (S, M, L)"]
DOD = ["Acceptance criteria met and demoed", "Works on iOS, Android and web where relevant; checked at phone and desktop widths", "Copy checked against the copy rules (no speed, any-language or fixed-time promises)", "Accessibility basics: labels, contrast, text scaling", "Errors and provider failures handled as in SYSTEM-LOGIC.md", "Tests for the logic; no new warnings", "Documentation updated (brief change log, rules or system logic if affected)"]


def body(st):
    e = EPICS[st["epic"]][0]
    ac = "\n".join(f"- [ ] {a}" for a in st["ac"])
    return (f"**As a** {st['who']}, **I want** {st['want']}, **so that** {st['so']}.\n\n"
            f"### Acceptance criteria\n{ac}\n\n"
            f"**Epic:** {st['epic']} {e} · **Priority:** {st['pri']} · **Size:** {st['size']} · **Milestone:** {MILESTONES[st['ms']][0]}\n\n"
            + ready_md(st["id"]))


def ready_md(i):
    r = READY.get(i)
    if not r:
        return "Screens: docs/design/tagkin-screens.html · Rules: docs/BUSINESS-RULES.md · Logic: docs/SYSTEM-LOGIC.md"
    return ("### Ready\n"
            f"- Screens: {'; '.join(r['screens'])}\n"
            f"- Rules: BUSINESS-RULES.md sections {', '.join(r['rules'])}\n"
            f"- Logic: SYSTEM-LOGIC.md sections {', '.join(r['logic'])}\n"
            f"- Depends on: {'; '.join(r['deps'])}")


def write_md():
    out = ["# Tagkin: product backlog", "", "Step 5 of the product owner flow (ROADMAP.md). Generated from docs/backlog/stories.py; GitHub issues are created from the same source. Board: https://github.com/users/Selaseyjr/projects/2 (Stage: Backlog, Ready, In progress, Review, Done).", "",
           f"{len(S)} stories in {len(EPICS)} epics. Priorities use MoSCoW; the MVP is every Must story. Sizes: S (≤1 day), M (2–3 days), L (about a week).", "",
           "## Milestones", ""]
    for k, (n, d) in MILESTONES.items():
        cnt = sum(1 for x in S if x["ms"] == k)
        out.append(f"- **{n}**: {d} ({cnt} stories)")
    out += ["", "## Summary", "", "| Priority | Stories |", "|---|---|"]
    for p in ["Must", "Should", "Could"]:
        out.append(f"| {p} | {sum(1 for x in S if x['pri'] == p)} |")
    out += [f"| Won't (this release) | {len(WONT)} items, listed below |", "", "## Definition of Ready", ""] + [f"- {d}" for d in DOR] + ["", "## Definition of Done", ""] + [f"- {d}" for d in DOD]
    for ek, (en, ed) in EPICS.items():
        out += ["", f"## {ek} · {en}", "", ed, ""]
        for st in [x for x in S if x["epic"] == ek]:
            out += [f"### {st['id']} · {st['title']}", "", f"*{st['pri']} · {st['size']} · {MILESTONES[st['ms']][0]}*", "",
                    f"As a {st['who']}, I want {st['want']}, so that {st['so']}.", ""] + [f"- {a}" for a in st["ac"]] + [""]
            if st["id"] in READY:
                out += [ready_md(st["id"]).replace("### Ready", "**Ready**"), ""]
    out += ["## Won't have in this release", ""] + [f"- {w}" for w in WONT] + [""]
    Path(__file__).resolve().parents[1].joinpath("BACKLOG.md").write_text("\n".join(out))
    print(f"wrote docs/BACKLOG.md: {len(S)} stories")


if __name__ == "__main__":
    if "--issues" in sys.argv:
        print(json.dumps([dict(title=f"{x['id']} · {x['title']}", body=body(x), labels=[f"epic:{x['epic']}", x["pri"].lower(), f"size:{x['size']}", "story"], milestone=MILESTONES[x["ms"]][0]) for x in S]))
    elif "--meta" in sys.argv:
        print(json.dumps(dict(epics=EPICS, milestones=MILESTONES)))
    else:
        write_md()
