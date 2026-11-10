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
    "M2": ("M2 Owner app core", "Owners create and manage tags, run Lost mode and returns in the app."),
    "M3": ("M3 Ordering and payment", "Printed tags can be ordered, paid and tracked."),
    "M4": ("M4 Gifting and activation", "Blank tags can be gifted and activated with a PIN."),
    "M5": ("M5 Launch readiness", "Website, legal, accessibility, languages, operations and store submission."),
}

S = []


def story(id, epic, title, who, want, so, ac, pri, size, ms):
    S.append(dict(id=id, epic=epic, title=title, who=who, want=want, so=so, ac=ac, pri=pri, size=size, ms=ms))


# ---------- E1 Accounts and sign-in ----------
story("TK-1", "E1", "Sign up and sign in with an email code", "new owner", "to sign in with my email and a one-time code", "I don't need a password",
      ["Email is required and verified with a 6-digit code valid for 10 minutes", "After 5 wrong attempts the user waits before trying again", "Resend is possible after 30 seconds; the screen suggests checking spam or using another email", "Terms must be accepted before the account is created"], "Must", "M", "M1")
story("TK-2", "E1", "First launch intro", "new owner", "to understand Tagkin in two screens", "I know what I'm signing up for",
      ["Welcome and 'Private by default' screens, then terms", "'I have an account' skips to sign-in"], "Should", "S", "M2")
story("TK-3", "E1", "Sign in on the web", "owner whose phone is lost", "to sign in at tagkin.app on any device", "I can still use Lost mode and reply",
      ["Same email-code sign-in as the app", "After sign-in the owner sees My tags with Lost mode and messages"], "Must", "M", "M1")
story("TK-4", "E1", "Account recovery", "owner who lost access to my email", "to recover my account with a recovery phone or backup email", "I don't lose my tags",
      ["Recovery phone receives an SMS code; backup email receives an email code", "Prompted after the first tag via a banner on My tags", "Support can recover an account with an order number (manual process)"], "Must", "M", "M2")
story("TK-5", "E1", "Signed-in devices", "owner", "to see and sign out devices", "I stay in control if a device is lost",
      ["List shows device and last use", "Sign out ends that session immediately"], "Should", "S", "M2")
story("TK-6", "E1", "Delete my account", "owner", "to delete my account in the app", "my data is gone when I leave",
      ["Shows what happens: tags retired, messages and photos deleted, invoices kept as the law requires", "Requires confirmation; sends a confirmation email", "Warns if a return is still open"], "Must", "M", "M2")
story("TK-7", "E1", "Download my data", "owner", "to download my data", "I can see what Tagkin stores",
      ["Request in Privacy and data; email with a download link valid 24 hours"], "Must", "S", "M5")
story("TK-8", "E1", "Language and appearance", "owner", "to choose my language and light, dark or system appearance", "the app suits me",
      ["Core languages: English (UK, US), German, French, Dutch, Polish, Spanish, Italian", "Appearance default is match system"], "Should", "S", "M2")

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
      ["Owner reply appears live; finder can reply with emoji", "Link to the handover check", "Invite card: protect your own things, first tag offer"], "Must", "M", "M1")
story("TK-17", "E2", "Check the handover code", "finder or desk staff", "to check the owner's handover code before handing over", "only the real owner gets it",
      ["6-digit code checked against the return; clear match or no-match message", "Attempts are rate-limited"], "Should", "S", "M2")
story("TK-18", "E2", "No reply yet", "finder", "to know what to do if the owner doesn't answer", "I'm not left waiting",
      ["After the wait time the page explains the backup contact was alerted and offers 'I handed it to staff'"], "Should", "S", "M2")
story("TK-19", "E2", "Report a tag or message", "finder", "to report abuse", "the platform stays safe",
      ["Reasons list; 112 note for emergencies; report goes to moderation"], "Must", "S", "M1")
story("TK-20", "E2", "Legal footer on finder pages", "finder", "to reach Impressum, privacy and terms", "Tagkin meets German law",
      ["Footer on every finder page"], "Must", "S", "M1")

# ---------- E3 Tags ----------
story("TK-30", "E3", "Create a tag: type, details, message", "owner", "to create a tag for a belonging", "finders know what to do",
      ["Choose type of tag (sticker, keychain, pet tag, luggage label, lock screen); tag type item, travel or pet is locked after creation", "Details per type: name and photo; travel fields change with transport mode; pet temperament and care notes", "Finder message: template or own text, 160 characters, warning on contact details, emoji picker, live preview"], "Must", "L", "M2")
story("TK-31", "E3", "Customise the tag", "owner", "to choose shape and colour and see the result", "I know what I'll receive",
      ["Six colours fill the tag; QR stays black on white", "Size, material and price shown", "Lock screen leads to 'Make it live'; printed types lead to ordering"], "Must", "M", "M2")
story("TK-32", "E3", "Free phone tag and lock screen image", "new owner", "a free lock-screen tag", "I can try Tagkin before buying",
      ["One free tag per account: the phone lock-screen tag", "Set as lock screen saves the image", "Retiring it frees the slot; codes never return"], "Must", "M", "M2")
story("TK-33", "E3", "My tags list", "owner", "to see all my tags and their state", "I know what's protected",
      ["Each row: name, code, state badge (normal, lost, return active), QR button", "+ New starts a printed tag when the free tag is used"], "Must", "M", "M2")
story("TK-34", "E3", "Edit message and contacts", "owner", "to edit the finder message and contacts any time", "details stay current",
      ["Always editable, also during Lost mode or a return", "Backup contact with alert-after time; never shown to finders"], "Must", "M", "M2")
story("TK-35", "E3", "Locked details during Lost mode or a return", "finder", "the item details not to change during a return", "I can trust what I see",
      ["Name, photo and description locked in lost and return_active states; UI shows the lock"], "Must", "S", "M2")
story("TK-36", "E3", "QR code and test scan", "owner", "to show my QR and test it with another phone", "I know it works",
      ["Test mode for 10 minutes: finder page shows a Test banner, no alerts", "Save image and share"], "Must", "S", "M2")
story("TK-37", "E3", "Status update for finders", "owner", "to post a short status like 'Arrived in Dubai'", "finders know where to bring it",
      ["City level only; dates and times rejected", "Hides after the trip or 7 days; can be turned off"], "Should", "S", "M2")
story("TK-38", "E3", "Retire a tag", "owner", "to retire a tag I no longer need", "it stops working for good",
      ["Confirmation explains the code never returns", "Retired tags keep no personal data"], "Must", "S", "M2")
story("TK-39", "E3", "Scan history", "owner", "to see when and where my tag was scanned", "I have a clue where it is",
      ["Time and city per scan; exact place only if a finder shared it"], "Should", "S", "M2")

# ---------- E4 Lost mode and returns ----------
story("TK-40", "E4", "Mark as lost", "owner", "to mark a tag as lost in the app or on the web", "finders see it's missing and I get alerts",
      ["Confirmation explains locks and no public reward", "Every scan alerts with city; can't be turned off while lost", "'I found it myself' returns to normal"], "Must", "M", "M2")
story("TK-41", "E4", "Relayed, translated conversation", "owner and finder", "to message each other without sharing contact details", "we stay private",
      ["Messages relayed by Tagkin; translated both ways with Show original", "Contact details in text trigger a share warning", "Emoji in every message box", "Failed messages show 'Not sent · Tap to retry'"], "Must", "L", "M2")
story("TK-42", "E4", "Safe place report with photo and map", "owner", "to see the finder's photo, map pin and address", "I can collect it",
      ["Open in Maps; 'I picked it up' closes the return", "Exact pin only when the finder shared location"], "Should", "M", "M2")
story("TK-43", "E4", "Handover code", "owner", "a handover code to show when I collect", "nobody else can claim my item",
      ["6-digit code per return, can be regenerated", "Never shown in messages"], "Should", "S", "M2")
story("TK-44", "E4", "Close a return", "owner", "to mark the item as returned, with a private thank-you", "the tag goes back to normal",
      ["Locks lift; return also closes after 14 days without messages"], "Must", "S", "M2")
story("TK-45", "E4", "Report or block a finder", "owner", "to block or report a finder", "I'm protected from abuse and scams",
      ["Block stops messages about that tag", "Anti-scam note: never pay before you have the item"], "Must", "S", "M2")

# ---------- E5 Ordering and payment ----------
story("TK-50", "E5", "Order a printed tag", "owner", "to order my customised tag in copies", "I get a durable tag",
      ["Shows my design, colour and size; copies of the same code", "Free shipping over €15; first-tag offer once per account as a discount line"], "Must", "M", "M3")
story("TK-51", "E5", "Delivery details before payment", "owner", "to enter my address before any pay button", "I know where it goes",
      ["Name, street, postcode, city, country, optional courier phone", "Address shared only with the print partner"], "Must", "S", "M3")
story("TK-52", "E5", "Choose how to pay", "owner", "to pay with Apple Pay or Google Pay, card, PayPal or Klarna", "I can use what I trust",
      ["Stripe payment sheet; button names amount and method", "Personalised goods notice (no 14-day return; faulty replaced) and Terms before paying", "Declined payment shows a clear error; card not charged"], "Must", "L", "M3")
story("TK-53", "E5", "Send paid orders to the print partner", "Tagkin", "paid orders sent to the print partner automatically", "tags are printed without manual work",
      ["Order created at the partner after payment webhook", "Partner status and tracking update the order", "Partner failure alerts admin and triggers refund"], "Must", "L", "M3")
story("TK-54", "E5", "Tag live from order", "owner", "my new tag to work as soon as I order", "I'm protected before it arrives",
      ["Own-order tags become normal at payment", "'Your tag is live and on its way'"], "Must", "S", "M3")
story("TK-55", "E5", "Orders list and emails", "owner", "to follow my orders", "I know when tags arrive",
      ["States: in production, shipped, delivered", "Emails: order confirmed, shipped with tracking"], "Must", "M", "M3")

# ---------- E6 Gifting and activation ----------
story("TK-60", "E6", "Gift blank tags", "buyer", "to gift blank tags of a chosen type and colour", "someone I care about can protect their things",
      ["From Create a tag: For myself / Gift a tag", "Gift note, recipient address, hide prices on packing slip", "Same payment step as orders"], "Should", "M", "M4")
story("TK-61", "E6", "Gift card with activation PIN", "recipient", "a PIN on the gift card, not on the tag", "only I can claim the tags",
      ["Unclaimed codes and a hashed PIN created per gift order", "PIN printed on the gift card by the print partner"], "Should", "M", "M4")
story("TK-62", "E6", "Activate a tag with a PIN", "recipient", "to scan or type the code and enter the PIN", "the tag becomes mine",
      ["Unclaimed → normal after PIN; 5 attempts then wait", "Then type, details and message; style and order steps skipped", "Activate another tag from the success screen", "Unclaimed tag scanned by a phone camera deep-links to the app with the code"], "Should", "M", "M4")

# ---------- E7 Notifications ----------
story("TK-70", "E7", "Notification permission at the right time", "owner", "to be asked for notifications after my first tag", "I understand why",
      ["Asked after the first tag is live or ordered", "Off: banner on My tags explains how to turn on"], "Must", "S", "M2")
story("TK-71", "E7", "Event notifications with fallback", "owner", "push for scans, reports and messages, email if push fails", "I never miss a find",
      ["Matrix in SYSTEM-LOGIC.md section 4", "Settings: scans, messages, email copy, orders, product news"], "Must", "M", "M2")
story("TK-72", "E7", "Backup contact alert", "owner", "my backup contact alerted if I don't reply", "a finder isn't left waiting",
      ["Scheduled job after the wait time; finder page updated"], "Should", "M", "M2")

# ---------- E8 Website, legal and owner web ----------
story("TK-80", "E8", "Website home, privacy and support", "visitor", "to learn what Tagkin is and get help", "I can decide and get support",
      ["Home, privacy in plain words, support with FAQ and email", "Required URLs for the stores"], "Must", "M", "M5")
story("TK-81", "E8", "Legal texts and Impressum", "Tagkin", "privacy policy, terms and Impressum published", "we can launch legally",
      ["Linked from website, finder pages, emails and the app"], "Must", "M", "M5")
story("TK-82", "E8", "Owner web dashboard", "owner", "to see my tags, messages and orders on the web", "I can act without my phone",
      ["My tags with Mark as lost; messages; account"], "Must", "M", "M1")

# ---------- E9 Platform and operations ----------
story("TK-90", "E9", "Moderation queue", "Tagkin", "to review reports and blocks", "abuse is handled",
      ["Admin list of reports with actions; every report reviewed"], "Must", "M", "M5")
story("TK-91", "E9", "Scheduled jobs", "Tagkin", "returns, test mode, status updates, retention and reconciliation handled automatically", "the system stays correct",
      ["Jobs listed in SYSTEM-LOGIC.md section 7"], "Must", "M", "M2")
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
      ["Designs: empty tags, messages and orders; loading skeletons; offline banner; payment failed; message not sent; code not found", "Permission turned off: camera and notifications recovery screens"], "Must", "M", "M2")
story("TK-98", "E8", "Store listings and privacy labels", "Tagkin", "complete App Store and Google Play listings", "the app passes review",
      ["Name, subtitle, description, keywords, screenshots re-shot from the real app, support and privacy URLs", "Apple privacy labels and Google Data safety match what the app collects", "Age rating questionnaires; review notes and a test account"], "Must", "M", "M5")

WONT = [
    "Premium subscription (later; Notify me measures demand)",
    "Shop packs with scratch panels (later; PIN flow is ready)",
    "SMS replies and WhatsApp (later)",
    "NFC tags, family sharing, ownership transfer (later)",
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
            f"Screens: docs/design/tagkin-screens.html · Rules: docs/BUSINESS-RULES.md · Logic: docs/SYSTEM-LOGIC.md")


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
