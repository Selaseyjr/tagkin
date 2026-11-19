# Tagkin case study (draft, 17 Nov 2026)

Draft for the portfolio (selasey-gbeddy.vercel.app). Written in the same fields the portfolio's case studies use (content.js: tag, title, card, sum, facts, opening, challenge, did, result, credit, problems, shots), so it can be dropped in as one entry. Stage 1 links the clickable prototype; stage 2 adds the live app once the owner journey is built.

---

**Tag:** Product case study · Prototype tested, build in progress

**Title:** Lost, then found. *Privately.*

**Card:** A QR tag for belongings and pets. Whoever finds them can alert the owner, and nobody's details are shown.

**Summary:** From an idea to a tested, clickable product in 10 days: research, rules, 68 screens, a finder flow and an owner app, now being built on a real backend.

**Facts**
| | |
|---|---|
| Role | Product owner · idea, research, rules, design direction, backlog |
| When | Since November 2026 |
| Built with | Claude Code, directed and reviewed by me · Next.js · Supabase |
| Link | Clickable prototype: owner app · finder flow · desktop |

## Opening

You leave your backpack on a train. Someone finds it. They want to help, but there is no way to reach you that doesn't mean exposing a phone number on a label, or them handing over theirs.

## Challenge

QR lost-and-found tags already exist. Most print the owner's contact on the tag, or stop at "someone scanned it". Finders don't know what to do next, owners don't know where their things are, and both sides give up privacy to make a return happen.

## What I did

- Spoke with 3 people about losing and returning things. Each theme became a rule: finders want privacy too, a public reward invites theft, "I have it" isn't enough to find an item.
- Wrote the product as rules before screens: a single brief, a business-rules document and a system logic spec. Every decision is logged with a date.
- Designed 68 owner screens, the finder flow and a desktop version as one clickable prototype, including the moments that go wrong: offline, failed payment, lost pet, a tag scanned mid-trip.
- Tested it: the finder flow with 5 people, the owner app with one tester. Each of Eli's 8 findings changed a rule or a screen.
- Built the backlog and Sprint 0: monorepo, CI, a Supabase database where the rules are enforced in the data itself, and 80 database tests.
- Stopped the first web build when it drifted from the tested prototype, archived it, and restarted the build to match the design.

## Result

A tested, clickable prototype and a working backend: database, sign-in by email code, finder reports and owner replies. The app is being rebuilt screen by screen against the prototype. Not launched; no customers, and I don't claim any.

## Credit

The idea, the research, the rules and every product decision are mine. Claude Code wrote the code and proposed technical options. I set the guardrails (no merge without green checks, no direct pushes to main, rules enforced in the database), reviewed every result as a user, and rejected work that didn't match.

## Problems and decisions

| Problem | Decision | Why |
|---|---|---|
| Finders give up privacy to help | Messages go through Tagkin. Neither side sees the other's contact unless they choose to share it | Privacy is the product. Raised by a finder, not an owner |
| "I have it" doesn't find anything | Three short steps: where it is now, the exact place, an optional note | Owners need a place, not a promise |
| A reward on the tag tempts people to keep things | No reward amount on the tag; owners thank privately | Raised in research; removes a bad incentive |
| A photo changed mid-return could mislead the finder | Name, photo and description lock during a return, with a visible history | Trust on both sides while the item is out of the owner's hands |
| Luggage travels by more than plane | Travel mode for every transport type; trip details expire | A bag on a bus needs the same help as one at an airport |
| Pets need help, not "return me" | Pet tags with temperament and care notes | A lost pet is the most urgent case |
| The first web build didn't match what was tested | Archived it and rebuilt against the prototype | A tested design is a spec, not a suggestion |

## Shots (to capture)

- Finder page on a phone: the owner's message, photo and "I found it"
- Finder report: three steps
- Owner: My tags with a lost pet
- Owner: conversation with a finder
- Create a tag: choose a design, live preview
- Desktop owner view

---

## Before publishing

1. **Prototype links are private.** The three claude.ai links (owner 9Xrte4UA56N8LCefx6Zycm, finder HyxUDEDyaY5EMghCdDWC6C, desktop 7VZer2dHF7HKYbQeQzMyy9) open only for you. Turn on link sharing from each page's Share menu, or publish one combined public prototype.
2. **German version** for content.js `de`.
3. **Check the numbers** before going live: 68 screens, 80 tests, 10 days (8 Nov idea → 17 Nov).
