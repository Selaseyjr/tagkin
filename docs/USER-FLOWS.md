> **Superseded (11 Nov 2026).** This is the first draft of 8 Nov. Current flows: the flow map in docs/design/tagkin-screens.html, the prototypes, BUSINESS-RULES.md and SYSTEM-LOGIC.md. Changed since this draft, among others: Lost mode no longer locks details (only a return does); one free phone tag instead of 3; no PNG or PDF downloads; shapes follow the shape-fit table; blank tags; orders with a full lifecycle.

# Tagkin: user flows (MVP)

Phase 3, step 1. Scope: Item, Travel and Pet tags. Care tags are phase 2.
All flow decisions signed off on 8 Nov 2026 (brief section 14).

## Return states

A tag is always in one state. These drive the lock rules in brief section 7.

| State | Starts when | Locked | Ends when |
|---|---|---|---|
| Normal | Registration | Type, ID | Owner taps Lost, or a finder reports it |
| Lost | Owner taps Lost | + name, photo, description | Owner marks Found, or a finder reports it |
| Return active | First finder report | + name, photo, description | Owner marks Returned, or 14 days pass with no messages |
| Retired | Owner retires the tag | Everything; ID dead forever | Never |

## Flow 1: Owner registration

```mermaid
flowchart TD
  A[Scan new tag or tap Create digital tag] --> B{Signed in?}
  B -- No --> C[Email, then one-time code<br/>no passwords]
  B -- Yes --> D
  C --> D[Choose type: Item, Travel, Pet<br/>Note: type cannot change later]
  D --> E[Name and optional photo]
  E --> F{Type}
  F -- Travel --> G[Luggage name and photo, optional trip]
  F -- Pet --> H[Temperament, care notes]
  F -- Item --> I
  G --> I[Finder message: template or custom, 160 chars, live preview]
  H --> I
  I --> J{Contact or abusive words in text?}
  J -- Contact --> K[Warn: public to anyone who scans] --> L
  J -- Abuse --> I
  J -- Clean --> L[Tag design: style, colour, preview]
  L --> M{Free limit of 3 reached?}
  M -- Yes --> N[Retire a tag or wait for Premium]
  M -- No --> O[Tag live]
  O --> P[Download PNG or PDF]
  O --> Q[Order printed tag]
```

Screens: sign in, type, details, finder message, design, done. Privacy line on sign in: "Your contact is never shown. Finders message you through Tagkin."

## Flow 2: Finder

```mermaid
flowchart TD
  A[Scan QR] --> C
  B[Camera fails: enter code at tagkin.app] --> C
  C{Tag state}
  C -- Retired or unknown --> X[This tag is no longer active]
  C -- Normal --> D[Owner message in finder's language, photo, show original]
  C -- Lost --> E[Urgent: This item is missing]
  D --> F[Where is it now? With me, Handed to staff, Left where I found it]
  E --> F
  F --> G[Where exactly? Live suggestions + Share item location]
  G --> H[Anything else? Optional note]
  H --> I{Phone or email in note?}
  I -- Yes --> J[This will share your number with the owner. Continue?]
  I -- No --> K
  J --> K[Want a reply? Optional email or phone, hidden.<br/>Nudge: without it, keep this page open for replies]
  K --> L[Thank you. Owner is alerted. State: Return active]
```

Target: under 10 seconds to the first tap, no app, no sign-up. Every screen shows "🔒 Your details stay private unless you choose to share them." Report abuse in the footer.

## Flow 3: Lost mode

```mermaid
flowchart TD
  A[Owner opens tag, taps Lost] --> B[Confirm: name, photo, description lock until found]
  B --> C[Finder page turns urgent]
  C --> D[Each scan: alert with time and approximate place]
  D --> E{Finder reports?}
  E -- Yes --> F[Return active, go to Flow 4]
  E -- No --> D
  F --> G[Owner marks Returned]
  A2[Owner finds it alone] --> H[Taps Found: back to Normal, locks lift]
```

No reward amount anywhere. After a return the owner can send a private thank-you.

## Flow 4: Messages (relay)

```mermaid
sequenceDiagram
  participant F as Finder
  participant T as Tagkin relay
  participant O as Owner
  F->>T: Report (status, place, note, optional email)
  T->>O: Push or email alert, translated, show original
  O->>T: Reply in own language
  alt Finder left email
    T->>F: Email with reply link, translated
    F->>T: Reply via link, no account
  else Anonymous
    T-->>F: Reply waits on the thank-you page while it is open
  end
  O->>T: Mark Returned, optional private thank-you
  Note over T: Neither side sees the other's address or number.<br/>Messages deleted after retention period.
```

Safety: phone or email typed by either side triggers the share warning. Both sides can report abuse; the owner can block a finder thread.

## Decisions (8 Nov 2026)

1. Sign-in: email one-time code, no passwords.
2. A return ends when the owner marks Returned, or after 14 days with no messages.
3. Owner verification before handover: after the MVP.
4. Anonymous finders see replies only while the thank-you page is open; a gentle nudge suggests leaving an email.
5. Scan location: city level unless the finder shares exact location.
