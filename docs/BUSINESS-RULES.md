# Tagkin: business rules

The rules Tagkin runs by. Product, design, build, support and marketing follow this document. Decisions and their reasons are logged in PRODUCT-BRIEF.md; when a rule changes, update it here and add a change-log line there.

Last updated: 11 Nov 2026. Open findings that may change these rules: docs/AUDIT-2026-11-11.md.

## 1. Business model

1. Tagkin earns money by selling **printed tags** (ordered in the app, on the website, or ready-made in shops). This is the main income.
2. There is **no subscription at launch**. Premium comes later, only for extras, and only if Notify me sign-ups show demand.
3. Tagkin never sells or shares user data.

## 1b. Accounts, guests and markets

1. **Explore without an account.** Anyone can browse, choose a tag type, fill in details and the finder message, and customise a tag before signing up. Drafts are kept on the device.
2. **Sign up at the moment it's needed**, with email and a 6-digit code: when a tag goes live ("Make it live"), before payment for an order ("Continue to payment" on Order details, where copies and delivery details share one page), and before the PIN when activating a gift or shop tag. Drafts are attached to the new account.
3. **Gift a tag works as a guest checkout**: only an email for the receipt and tracking; no account, because the buyer never owns the tags.
4. **Launch markets (pilot):** only countries where Stripe can take payment and the print partner delivers (Germany and the EU), prices in euro. Other countries are listed as future markets; checkout shows only supported delivery countries. Ghana follows later with a local payment provider (such as Paystack and mobile money) and local prices.
5. **Launch sequence:** a web beta first (finder pages and the owner web at tagkin.app: create, customise, order and pay, Lost mode, messages), then the iOS and Android app after store review.

## 2. Free tag

1. Every account gets **1 free tag: the phone lock-screen tag**. It protects the phone and lets owners test a real find with another phone before buying printed tags.
2. Tags are never downloadable for home printing. Every printed tag is ordered, so every printed tag meets our quality.
3. Retiring the free phone tag frees the slot (for example for a new phone). The old code never comes back.
4. Extra digital tags are not sold at launch (in-app digital sales would need Apple and Google payments).
5. A new printed tag goes live the moment it is ordered; the code works before the tag arrives.

## 3. Printed tags

1. A bought tag is **free to use for life**: no subscription, no activation fee, and it never counts toward the free tag.
2. Owners choose the type (sticker, keychain, pet tag, luggage label), size (where the product has sizes), colour, finish (matte, gloss, holo, glow or reflective, by product) and an optional label of up to 12 characters (a name or initials), plus the number of copies, and see the result before paying.
   - The QR always prints black on white with its margin, and the code and tagkin.app always print. Colour and finish never touch the QR.
   - Labels never carry a phone number, email or address; the app blocks them.
   - Options per product follow what the print partner can make; extra finishes cost extra and show in the price before checkout.
3. **Copies:** one code can be printed several times for **one belonging** (phone and case, suitcase outside and inside). Separate belongings get separate tags.
4. The same price per tag applies in the app, on the website and in shops. Shop packs use a standard design; the app offers colours and personal messages.
5. Prices shown before checkout are final, including shipping. Discounts appear as a separate line (EU price rules), never as a struck-through price.
6. Delivery details are asked before any payment button, on the same page as the copies (Order details).
7. Packs lead the range; shipping is free over €15 (sample threshold, set with the print partner).
8. **Payment:** Tagkin is the seller. Customers choose how to pay on the review screen: Apple Pay (iPhone) or Google Pay (Android), card, PayPal or Klarna, processed by Stripe. Tagkin never sees card details. The print partner only prints and ships, and bills Tagkin.
9. The first-tag offer applies to an account's first printed order only.
10. Tags are made to order with the customer's code, so the EU 14-day return right does not apply; checkout says so before payment. Faulty or damaged tags are replaced free.

## 3b. Lock-screen tag

1. The lock-screen tag is a digital product for the phone itself. It is set up like any tag (type, details, finder message, colour) and works the same way for finders.
2. It is never printed or shipped, and never swapped for a physical product.
3. It fits the phone only. It is never offered as a blank tag, a gift, or a shape when customising another item. A printed tag for the phone itself (for example a sticker on the case) is ordered as an item tag.

## 3c. Shape fit

One table decides which item types each shape can go on. Every screen reads from it: Choose your type of tag, What is it for?, Customise, blank-tag set-up, gifts and activation.

| Shape | Item | Travel | Pet |
|---|---|---|---|
| Sticker | yes | yes | no |
| Keychain | yes | no | no |
| Luggage label | no | yes | no |
| Pet tag | no | no | yes |
| Lock screen (digital) | phone only | no | no |

1. Only shapes that fit are shown; shapes that don't fit are hidden, not greyed out.
2. When only one type fits a shape, the type step is skipped. When only one shape fits a type (pet), Customise shows no shape choice.
3. A blank tag keeps the shape chosen at order; set-up only offers the types that fit it.
4. Changing the shape or the type clears only the choices that no longer fit.

## 3d. Orders after payment

1. Stages: Paid, Sent to print, Printing, Quality check, Shipped, Out for delivery, Delivered. Each shows a date or an expected date.
2. **Cancel:** possible until printing starts, with a full refund. A linked tag stays in My tags (the code keeps working); blank tags from that order are removed.
3. **Address:** can be changed until the order ships.
4. **Failed print check:** we reprint at our cost (about 2 days extra) and tell the owner.
5. **Delivery failed:** the parcel returns to us; the owner checks the address and we send it again for free.
6. **Problem after delivery** (damaged, never arrived, wrong colour or size, QR won't scan): free replacement, nothing to send back.

## 4. Codes and ownership

1. Every tag has a random code (TK-7Q4M-9XRA format), at least 8 characters, never reused.
2. A tag belongs to **one account** (its owner) and **one belonging**. The owner receives every alert and message and controls Lost mode.
3. A tag code cannot move to another account. (A later feature may allow a transfer the new owner must accept, e.g. when selling a bike.)
4. Tag type is locked after set-up. Name, photo and description lock only during a return (once a finder has reported it), so the finder sees what they expect. In Lost mode they stay editable, because a better photo helps finders. Contacts, finder message and status updates are always editable.
5. Unclaimed tags (shop packs, gifts) have no owner until someone activates them with the **activation PIN**, which is never printed on the tag: it is on the gift card or under a scratch panel on the pack. A finder who scans an unclaimed tag sees "This tag isn't set up yet".
6. **Email is required** to sign up; it is the sign-in. Owners can sign in on the app or at tagkin.app on any device (for example when the phone itself is lost). **Web and app:** the web manages what the owner already has (tags, Lost mode, messages, orders, editing details, setting up blank tags). Creating tags, ordering, scanning to activate, push alerts and the lock-screen tag stay in the app, and the web always offers the app for instant alerts. A recovery phone or backup email is recommended and prompted after the first tag. At launch, SMS is used only for recovery codes.
7. **Handover code (free for everyone):** before handing an item over, finders or desk staff can check the owner's 6-digit handover code.
8. **Blank tags for yourself:** owners can order a tag without linking it to an item (for something not yet bought, a pet not yet home, or a pack to use later). It belongs to the owner's account from payment, shows "Set up" in My tags and is set up later with type (only types that fit its shape, see 3c), name and photo, no PIN needed, in the app or on the web. Until then a finder sees "This tag isn't set up yet" and the owner gets a scan alert.
9. **Item details stay editable:** name, photo and description can be changed later (not during a return). A change shows everywhere the item appears. A photo is optional at creation; tags without one show a reminder. A code never moves to a different belonging; for a new item, retire the tag and create a new one.

## 5. Gift a tag

1. **Gifts are always blank, unclaimed tags.** Gift a tag is a choice on Create a tag (For myself / Gift a tag). The buyer chooses the product (sticker, keychain, pet tag, luggage label), colour, quantity, a gift note and delivery. The recipient chooses which belonging each tag protects, activates it and becomes the owner.
2. A tag that is already set up cannot be gifted. To protect someone else's things, gift blank tags.
3. The buyer never receives alerts or messages for gifted tags and has no access to them after delivery.
4. Free tags cannot be gifted. Invite a friend is the free way to share Tagkin.
5. Gift a tag starts from Create a tag, Orders, "Your tag is live", and later the website. It is never a switch inside ordering a set-up tag.
6. The product shape suggests a tag type, but the recipient sets the type at set-up; after that it is locked.

## 6. Finders

1. Finders never need an app or an account.
2. Neither side sees the other's contact details unless they choose to share them. Messages are relayed and translated.
3. If the owner doesn't reply within a set time, the backup contact is alerted and the finder is offered to hand the item to staff or a lost-and-found desk.
4. The finder page always uses helper wording ("This item is missing"). It never says "stolen".
5. No public reward amount. Owners can thank finders privately after a return.
6. **Left in a safe place:** when a finder can't keep the item or hand it to staff, they can leave it somewhere safe, add a photo, a short note and the address. Photos have their location data removed. The owner sees an exact map pin only if the finder shared the item location; otherwise the place the finder typed.
7. **Handover check:** while a return is open, anyone holding the item (the finder or desk staff) can scan the tag and check the owner's handover code. No session or account is needed; attempts are limited (5, then a 15-minute wait). After a match, the finder confirms the handover and the conversation closes.
8. **Coming back later:** finders reopen their report from the link in every email or text, or by scanning the tag again on the same device. Anonymous finders get a link to save; without it they can still check the handover code from the tag.

## 7. Privacy and safety

1. Scan locations are stored at city level unless the finder shares the item location.
2. Travel tags show destination and operator only, never dates or the home address. **The trip is optional:** a travel tag works with just the luggage name and photo; the trip (mode, carrier, destination, end date) can be added at creation or later, and hides when the trip ends. The end date is used only to hide it. Owner status updates are city level only, with no dates or times, and hide automatically.
3. Messages are deleted after a set retention period once a return ends. Retired tags keep no personal data.
4. Owners and finders can report and block. Every report is reviewed (no fixed response time is promised).
5. Owners can download and delete their data and delete their account in the app.

## 8. How we talk about Tagkin

1. Never promise speed ("in seconds", "fast"), "any language", fixed support or review times, or anti-theft protection. Say what Tagkin does: finders scan the tag and alert the owner privately; owners see where it was last scanned. Tags help honest finders return things; they do not stop theft.
2. Two audiences: people who protect what they value, and people who often misplace things. Never make users feel careless.
3. Core languages: English (UK, US and more), German, French, Dutch, Polish, Spanish, Italian. More are added where tags sell.
