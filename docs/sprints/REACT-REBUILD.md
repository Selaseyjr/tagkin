# React rebuild of the approved wireframe

Decided 16 Nov 2026: recreate the full approved wireframe (docs/design: owner-prototype, finder-prototype, desktop-prototype) as one React web app (Next.js, apps/web) on the existing Supabase database. Built on branch `app/react-rebuild`, reviewed on protected Vercel previews, **not published to tagkin.app until approved**. The previous web build is kept on `archive/web-v1-before-rebuild`.

Principle: each screen is the prototype screen, same layout, copy and states, now backed by real data. Styles are ported from the prototype source, not redrawn.

## Batches

| # | Batch | Prototype screens | Backend needed |
|---|---|---|---|
| R1 | Foundation | Design system (all prototype CSS), phone frame with tabs, splash, empty, offline and error states (desktop shell moves to R10) | none |
| R2 | First launch and sign-in | launch1–3, signin, code, perm-notif | Supabase Auth (exists); terms acceptance stored |
| R3 | Create a tag | start, pick, type, details, t-details, p-details, message, design (customise with product mock-ups), live (lock-screen tag), limit | `create_tag`, photo upload (Storage, EXIF stripped), finder message rules, free-tag entitlement |
| R4 | Order and pay | order (copies + address), checkout, ordered, err-pay, orders + order details lifecycle | orders, order items, shipments, prices; payment in Stripe test mode (needs a Stripe test account) or a simulated payment step |
| R5 | My tags and manage | tags, detail, confirm, scans, locked, qr, history, edit-msg, edit-contacts, status, retire, blank set-up, edit item and photo | contacts, status updates, retire (exist); item edit (exists) |
| R6 | Returns and messages | alert, inbox, thread, emoji, anon, safe, handover, returned, err-send, report-owner, report-done | handover codes, block and report, safe-place photo |
| R7 | Gifting and activation | gift, gift-delivery, gift-review, gift-sent, perm-camera, scan, enter-tag, found-new, act-pin, act-live, taken | gift orders, unclaimed codes with PIN, activation |
| R8 | Account | account, plan, notif-settings, language, appearance, recovery, privacy, delete, deleted | profile settings, data export, account deletion |
| R9 | Finder flow | all finder prototype screens (code entry, tag page per state, where now, where exactly, safe-place photo, note, reply choice, thank-you with live reply, handover check, report abuse, not set up, retired, test scan) | exists (report, reply, view); handover check |
| R10 | Desktop layouts | desktop prototype: owner web (sidebar, tag grid, detail panel, messages, orders, account) and finder desktop page | none |

Each batch: one pull request into `app/react-rebuild`, previewed and compared side by side with the prototype at phone and desktop width, all checks green.

## Open decisions (asked when the batch starts)
- R4: Stripe test mode (real card form, test cards) or a simulated payment step.
- R3/R7: photo storage limits and retention.
