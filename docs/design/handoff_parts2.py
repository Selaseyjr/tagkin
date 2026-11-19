# Hand-off part 2 (11 Nov 2026): sign-in email, printed tag artwork, lock-screen image,
# printable PDF sheet, permission recovery, languages, accessibility rules, Android icon,
# and the public showcase page for Figma Community.
# Executed inside build_screens.py after handoff_parts.py (shares its globals).

CODE = "TK-7Q4M-9XRA"

# ---------- Sign-in email ----------
EMAILS = EMAILS.replace('</div></section>', email("Email 0 · Sign-in code", "Your Tagkin sign-in code", '<h3>Your sign-in code</h3><div class="mcard codebox"><b>482 917</b></div><p class="m">Enter this code in the app. It works for 10 minutes. If you didn’t ask for it, you can ignore this email; nobody can sign in without the code.</p>') + '</div></section>', 1)


EMAILS = EMAILS.replace('</div></section>', email("Email 5 · Order shipped", "Your Tagkin tags have shipped", '<h3>Your tags are on their way.</h3><div class="mcard"><b>2 × sticker, mint</b><span>DHL · tracking 00340434 1234 5678 · arrives Friday</span></div><div class="btn pri">Track parcel</div><p class="m">Your tag already works. Stick it on as soon as it arrives, then try a test scan with another phone.</p>') + '</div></section>', 1)

# ---------- Printed tag artwork ----------
def qrblock(size):
    return f'<div class="qr" style="width:{size}px;height:{size}px;background-size:{size // 9}px {size // 9}px"></div>'


def art(name, shape, body, spec):
    return f'<figure data-name="{name}" style="max-width:300px"><figcaption>{name}</figcaption><div class="artbox"><div class="bleed {shape}"><div class="trim {shape}">{body}</div></div></div><p class="artspec">{spec}</p></figure>'


_MK = '<svg width="22" height="22" class="amk"><use href="#mark"/></svg>'
PRINT = f"""<section class="flow"><h2>Printed tags</h2><p>Print artwork for the print partner. Dashed line = trim, outer area = 3 mm bleed. The QR stays black on white with a quiet zone of 4 modules, whatever the style.</p><div class="row">
{art("Print · Sticker", "circ", _MK + qrblock(120) + '<b>Found me? Scan to return</b><small>tagkin.app · ' + CODE + '</small>', "Round sticker, 50 mm, waterproof vinyl. QR at least 22 mm.")}
{art("Print · Keychain", "rect", _MK + qrblock(110) + '<small>tagkin.app<br>' + CODE + '</small>', "Acrylic, 30 × 45 mm, 4 mm hole top centre. Print both sides: QR front, logo back.")}
{art("Print · Pet tag", "disc", qrblock(96) + '<small>' + CODE + '</small>', "Metal disc, 32 mm, engraved or UV printed. Code engraved below the QR.")}
{art("Print · Luggage label", "lug", _MK + qrblock(130) + '<b>I’m travelling. Scan to return.</b><small>tagkin.app · ' + CODE + '</small>', "PVC label, 55 × 90 mm with strap slot. Destination is never printed.")}
</div></section>"""


# ---------- Lock-screen image and printable PDF ----------
LOCKIMG = f"""<figure data-name="Export · Lock screen image" style="max-width:360px"><figcaption>Export · Lock screen image</figcaption><div class="scr lock lockimg" style="height:760px">{SBAR}<p class="ltime">9:41</p><p class="ldate">Monday 16 November</p><div class="sp"></div><div class="lockcard"><div class="qr" style="width:96px;height:96px;background-size:11px 11px"></div><div><b>Found this phone?</b><span>Scan to message the owner privately.</span><small>tagkin.app · TK-W6QB-8MZT</small></div></div></div><p class="artspec">1290 × 2796 PNG. Card sits above the home indicator, clear of the clock and widgets.</p></figure>"""

PDF = '<figure data-name="Export · Printable PDF (A4)" style="max-width:520px"><figcaption>Export · Printable PDF (A4)</figcaption><div class="a4"><div class="a4h">' + LOGO + '<span>Black backpack · ' + CODE + '</span></div><div class="a4g">' + ''.join('<div class="a4t">' + _MK + qrblock(70) + '<small>tagkin.app<br>' + CODE + '</small></div>' for _ in range(6)) + '</div><p class="a4f">Cut along the dashed lines. Cover with clear tape to keep it dry. Printed tags from the shop last longer.</p></div></figure>'

GIFTCARD = '<figure data-name="Print · Gift card with PIN" style="max-width:360px"><figcaption>Print · Gift card with PIN</figcaption><div class="gcardp"><div class="logo"><svg width="20" height="20"><use href="#mark"/></svg>tagkin</div><p class="gnote">“Happy birthday! For your new camera bag 📷 – Alex”</p><div class="gpin"><span>Activation PIN</span><b>528 146</b></div><p class="xs">Open the Tagkin app, tap Activate it, scan a tag and enter this PIN. Keep it private: whoever has the PIN can claim the tags.</p></div><p class="artspec">A6 card in the box. The PIN is never printed on the tags.</p></figure>'
EXPORTS = f'<section class="flow"><h2>Phone tag and gift card</h2><p>The free phone tag image, and the card that carries a gift’s activation PIN.</p><div class="row">{LOCKIMG}{GIFTCARD}</div></section>'


# ---------- Permission recovery, languages ----------
def ph(name, body, rtl=False):
    d = ' dir="rtl" lang="ar"' if rtl else ""
    return f'<figure data-name="{name}"><figcaption>{name}</figcaption><div class="scr"{d}>{SBAR}{body}</div></figure>'


RECOVER = f"""<section class="flow"><h2>Permissions turned off, and languages</h2><p>Recovery when someone taps “Don’t allow”, a long-text check in German, and a right-to-left check in Arabic.</p><div class="row">
{ph("Recover · Camera is off", hdr(back(), "") + '<div class="sp"></div><div class="hero"><span class="bell">📷</span></div><h1 class="center">Camera access is off</h1><p class="m center">To scan a tag, turn on Camera for Tagkin in your phone’s Settings. You can also type the code instead.</p><div class="sp"></div><div class="btn pri">Open Settings</div><div class="btn ghost">Enter code instead</div>')}
{ph("Recover · Notifications are off", hdr(LOGO, "") + '<div class="note warn">Notifications are off, so you won’t hear when a tag is scanned. <u>Turn on</u></div><h1>My tags</h1><div class="item"><span class="ic">🎒</span><span class="tx"><b>Black backpack</b><span>' + CODE + '</span></span><span class="badge b-n">Normal</span></div><div class="sp"></div>' + tabbar("tags"))}
{ph("Language · German, long text", hdr(back("Zurück"), "") + '<h1 class="md">Diesen Anhänger dauerhaft deaktivieren?</h1><p class="m">Schwarzer Rucksack · ' + CODE + '</p><div class="grpl"><div class="li"><span>Der Code funktioniert nicht mehr</span><span>Endgültig</span></div><div class="li"><span>Nachrichten und Scans</span><span>Gelöscht</span></div></div><p class="note info">Längere Wörter wie „Benachrichtigungseinstellungen“ müssen umbrechen dürfen, ohne Text abzuschneiden.</p><div class="sp"></div><div class="btn lostb">Anhänger deaktivieren</div><div class="btn sec">Anhänger behalten</div>')}
{ph("Language · Arabic, right to left", hdr(LOGO, "AR ▾") + '<div class="photo sm">🎒</div><h1>هل وجدتني؟ شكرًا لك! اضغط أدناه لإخبار صاحبي بمكاني.</h1><span class="link">مترجم من الألمانية · عرض الأصل</span><div class="sp"></div><div class="btn pri">لقد وجدته</div><p class="priv"><svg width="14" height="14"><use href="#lock"/></svg>تبقى بياناتك خاصة ما لم تختر مشاركتها.</p>', rtl=True)}
</div></section>"""


# ---------- Accessibility rules ----------
A11Y = """<section class="flow"><h2>Accessibility rules</h2><p>Built in from the first line of code. Checked again before launch.</p><div class="rules">
<div><b>Contrast</b><span>All text and icons meet WCAG AA (4.5:1 text, 3:1 large text and controls), light and dark.</span></div>
<div><b>Touch targets</b><span>At least 44 × 44 pt (iOS) and 48 × 48 dp (Android). Primary buttons are 52 high.</span></div>
<div><b>Text size</b><span>Supports Dynamic Type and Android font scaling up to 200%. Layouts reflow; nothing is cut off.</span></div>
<div><b>Screen readers</b><span>Every control has a label (“Show QR code for Black backpack”). Status badges are read as words, not colours.</span></div>
<div><b>Focus order</b><span>Top to bottom, header first, primary action last. Sheets and dialogs trap focus until closed.</span></div>
<div><b>Colour is never the only signal</b><span>Lost uses red plus the word Lost and an icon. Errors have text, not just a red border.</span></div>
<div><b>Motion</b><span>Respects Reduce Motion: no parallax, spinners become static, transitions shorten.</span></div>
<div><b>Language</b><span>Right-to-left layouts mirror. Long German words wrap. Translated text is marked with its language for screen readers.</span></div>
</div></section>"""


# ---------- Android adaptive icon ----------
ICONS = f"""<section class="flow"><h2>App icons</h2><p>iOS uses one full square; Android uses separate foreground and background layers that the phone crops into different shapes.</p><div class="row icrow">
<div class="icx"><span class="appicon ios"><svg width="58" height="58"><use href="#mark"/></svg></span><small>iOS · 1024 × 1024</small></div>
<div class="icx"><span class="layer bg"></span><small>Android background · mint</small></div>
<div class="icx"><span class="layer fg"><svg width="58" height="58"><use href="#mark"/></svg><i class="safe"></i></span><small>Android foreground · 108 dp, mark inside the 66 dp safe zone</small></div>
<div class="icx"><span class="appicon circle"><svg width="50" height="50"><use href="#mark"/></svg></span><small>Circle mask</small></div>
<div class="icx"><span class="appicon squircle"><svg width="54" height="54"><use href="#mark"/></svg></span><small>Squircle mask</small></div>
<div class="icx"><span class="appicon mono"><svg width="54" height="54"><use href="#mark"/></svg></span><small>Android 13 themed (monochrome)</small></div>
</div></section>"""

PARTS2 = PRINT + EXPORTS + RECOVER + A11Y + ICONS

PARTS2_CSS = """
.codebox b{font:700 34px/1 var(--tk-font-display);letter-spacing:.2em;text-align:center}
.artbox{background:var(--tk-sunken);border-radius:16px;padding:20px;display:grid;place-items:center;height:330px}
.bleed{background:#d9f7ec;padding:10px;display:grid;place-items:center}
.trim{background:#fff;color:#0b1712;outline:2px dashed #7f8c87;outline-offset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px;text-align:center;padding:14px}
.trim b{font-size:12px}.trim small{font-size:10px;font-weight:600;color:#4f5e57}
.circ{border-radius:50%}.bleed.circ .trim{width:230px;height:230px}
.rect .trim,.trim.rect{border-radius:18px}.bleed.rect{border-radius:24px}.bleed.rect .trim{width:170px;height:250px;position:relative}
.bleed.rect .trim::before{content:"";position:absolute;top:10px;width:16px;height:16px;border-radius:50%;border:2px solid #7f8c87}
.disc{border-radius:50%}.bleed.disc .trim{width:200px;height:200px;background:#e6ebe9}
.lug{border-radius:20px}.bleed.lug .trim{width:180px;height:280px;border-radius:16px;position:relative;padding-top:34px}
.bleed.lug .trim::before{content:"";position:absolute;top:10px;width:60px;height:12px;border-radius:6px;border:2px solid #7f8c87}
.amk{color:#0b1712}
.artspec{font-size:12px;color:var(--tk-ink-2);margin:8px 0 0}
.lockimg{background:linear-gradient(170deg,#2b3b52,#0d1311 70%)}
.lockcard{display:flex;gap:12px;align-items:center;background:#fff;color:#0b1712;border-radius:20px;padding:12px;margin-bottom:30px}
.lockcard b{display:block;font-size:15px}.lockcard span{display:block;font-size:12px;color:#4f5e57}.lockcard small{display:block;font-size:10px;font-weight:600;margin-top:4px;color:#4f5e57}
.a4{background:#fff;color:#0b1712;aspect-ratio:210/297;border:1px solid var(--tk-line);border-radius:6px;padding:22px;display:flex;flex-direction:column;gap:14px;box-shadow:var(--tk-shadow)}
.a4h{display:flex;justify-content:space-between;align-items:center;font-size:12px;color:#4f5e57}.a4h .logo{color:#0b1712}
.a4g{display:grid;grid-template-columns:repeat(2,1fr);gap:0;flex:1}
.a4t{border:1.5px dashed #9aa6a1;margin:-0.75px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px;padding:10px;text-align:center}
.a4t small{font-size:9px;font-weight:600;color:#4f5e57}
.a4f{font-size:11px;color:#4f5e57;margin:0}
[dir="rtl"] .hdr,[dir="rtl"] .priv{direction:rtl}
.rules{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:12px}
.rules div{background:var(--tk-surface);border:1px solid var(--tk-line);border-radius:16px;padding:16px;display:flex;flex-direction:column;gap:4px}
.rules b{font:700 16px var(--tk-font-display)}.rules span{font-size:14px;color:var(--tk-ink-2)}
.icrow{align-items:flex-start;gap:28px}
.icx{display:flex;flex-direction:column;align-items:center;gap:8px;max-width:150px;text-align:center}.icx small{font-size:12px;color:var(--tk-ink-2)}
.appicon.ios{width:96px;height:96px;border-radius:22px}
.layer{width:96px;height:96px;border:1px dashed var(--tk-line);display:grid;place-items:center;position:relative}
.layer.bg{background:#00c48c}.layer.fg{background:repeating-conic-gradient(var(--tk-sunken) 0 25%,var(--tk-surface) 0 50%) 0 0/12px 12px;color:#03261a}
.safe{position:absolute;inset:15px;border-radius:50%;border:1.5px dashed #e02a17}
.appicon.circle{width:96px;height:96px;border-radius:50%}.appicon.squircle{width:96px;height:96px;border-radius:34%}
.appicon.mono{width:96px;height:96px;border-radius:50%;background:#d9f7ec;color:#007a57}
.gcardp{background:#fff;color:#0b1712;border:1px solid var(--tk-line);border-radius:16px;padding:22px;display:flex;flex-direction:column;gap:12px;aspect-ratio:105/148;box-shadow:var(--tk-shadow)}.gnote{font:600 18px/1.3 var(--tk-font-display);margin:0}.gpin{background:#d9f7ec;border-radius:12px;padding:12px;display:flex;flex-direction:column;gap:2px}.gpin span{font-size:11px;color:#4f5e57;text-transform:uppercase;letter-spacing:.05em}.gpin b{font:700 22px var(--tk-font-display);letter-spacing:.08em}
.legal.dleg{padding:12px 32px;text-align:left;margin-top:auto}
"""


# ---------- Public showcase for Figma Community ----------
def build_showcase():
    global SHOW_NOTES
    SHOW_NOTES = False
    pick = lambda lst, names: [t for t in lst if t[-2] in names]
    finder_pick = pick(FINDER, ["Finder 1 · Owner message", "Finder 1b · Lost mode", "Finder 2 · Where is it now?", "Finder 3 · Where exactly?", "Finder 5 · Want a reply?", "Finder 6 · Thank you", "Finder H · Before you hand it over", "Finder 1t · Travel tag", "Finder 1p · Pet tag"])
    owner_pick = pick(SETUP + OWNER + GIFT + LOST + EXTRA, ["Setup 1 · Welcome", "Setup 5 · Create a tag", "Owner 3 · Tag type", "Owner 6 · Customise", "Owner 7 · Phone tag is live", "Gift 1 · Gift a tag", "Owner 8 · My tags", "Owner 11 · Lost: scans", "Owner 13 · Message thread", "Manage 6 · QR code and test", "Account 7 · Appearance"])
    cover = """<section class="flow coverp"><div class="cov"><div><p class="eyebrow">Tagkin · app design</p><h1 class="wh">Protect what you value.</h1><p class="m">QR tags for bags, keys, gear and pets. Whoever finds something scans the tag and alerts the owner, privately. No app needed for finders.</p></div><div class="covgrid">
<div><b>What’s inside</b><span>Finder web flow, owner app, Gift a tag, store screenshots, printed tags and marketing visuals.</span></div>
<div><b>Design system</b><span>Fresh mint, Geist (Bricolage Grotesque for the wordmark), light and dark, WCAG AA contrast.</span></div>
<div><b>Designed by</b><span>Selasey Gbeddy · Technical Product Owner</span></div>
<div><b>Status</b><span>Design v1, November 2026. App in development.</span></div>
</div></div></section>"""
    body = cover + STORE + flow("Finder: no app needed", "Scan, report where it is, get a reply.", finder_pick) + flow("Owner app", "Create, protect, get alerted.", owner_pick) + PRINT + MKT
    page = html.split('<div class="page">')[0] + '<div class="page">\n<header class="top"><div class="brand"><svg width="36" height="36"><use href="#mark"/></svg><b>tagkin</b></div></header>\n' + body + '\n</div>\n</body>\n</html>\n'
    page = page.replace("<title>Tagkin screens</title>", "<title>Tagkin showcase</title>")
    out = ROOT / "docs/design/tagkin-showcase.html"
    out.write_text(page)
    SHOW_NOTES = True
    print(f"wrote {out.relative_to(ROOT)}: {len(finder_pick) + len(owner_pick)} screens, no spec notes")


# ---------- Owner web dashboard and tablet ----------
_ROWS = ''.join(f'<div class="drow"><span class="ic">{ic}</span><span class="tx"><b>{n}</b><span>{c}</span></span><span class="badge {b}">{st}</span><span class="dact">{a}</span></div>' for ic, n, c, b, st, a in [
    ("🎒", "Black backpack", "TK-7Q4M-9XRA · last scan Luisenplatz, today 16:20", "b-r", "Return active", "Open"),
    ("📱", "Phone tag", "TK-W6QB-8MZT · lock screen", "b-n", "Normal", "<b class=\"btn lostb sm\">Mark as lost</b>"),
    ("🐾", "Milo", "TK-M3PF-2KWD · 3 scans since lost", "b-l", "Lost", "Open"),
    ("🧳", "Blue suitcase", "TK-H8RC-4TNE · trip ends 20 Nov", "b-n", "Normal", "Open")])

DASH = desk("Web · Owner dashboard", '<div class="dash"><aside>' + LOGO + '<a class="on">My tags</a><a>Messages <i class="unread">1</i></a><a>Orders</a><a>Account</a><small>Signed in as a•••@example.com</small></aside><main><div class="dhead"><h1>My tags</h1><b class="btn pri sm">Create a tag</b></div>' + _ROWS + '<div class="dmsg"><b>New: Black backpack was left in a safe place</b><span>Café Extrablatt, Luisenplatz 4 · photo and map in Messages</span></div></main></div>', 760, "tagkin.app/my-tags")

WEB = WEB.replace('</div></section>', DASH + '</div></section>', 1)

TABLET = f"""<section class="flow"><h2>Tablet</h2><p>On tablets the app shows the list and the detail side by side. The finder web page uses the centred desktop card.</p><div class="row">
<figure data-name="Tablet · My tags and messages" class="wide" style="max-width:1000px"><figcaption>Tablet · My tags and messages</figcaption><div class="tablet"><div class="tl">{SBAR}{hdr(LOGO, '<span>+ New</span>')}<h1 class="md">My tags</h1>{''.join(f'<div class="item{" sel" if i == 0 else ""}"><span class="ic">{ic}</span><span class="tx"><b>{n}</b><span>{c}</span></span><span class="badge {b}">{st}</span></div>' for i, (ic, n, c, b, st) in enumerate([("🎒", "Black backpack", "TK-7Q4M-9XRA", "b-r", "Return"), ("📱", "Phone tag", "TK-W6QB-8MZT", "b-n", "Normal"), ("🐾", "Milo", "TK-M3PF-2KWD", "b-l", "Lost"), ("🧳", "Blue suitcase", "TK-H8RC-4TNE", "b-n", "Normal")]))}<div class="sp"></div>{tabbar("tags")}</div><div class="tr"><div class="hdr"><b>Black backpack</b><span class="badge b-r">Return active</span></div><div class="thread"><div class="bub in2 wide2"><b>Left in a safe place</b><div class="minimap"><i class="pin"></i><span>Café Extrablatt, Luisenplatz 4, Darmstadt</span></div><span>“Gave it to the barista, Mia. Ask at the counter.”</span></div></div><div class="hcode"><span>🔑 Your handover code</span><b>739 204</b></div><div class="sp"></div><div class="two"><div class="btn sec">Open in Maps</div><div class="btn pri">I picked it up</div></div></div></div></figure>
</div></section>"""

PARTS2 = PARTS2 + TABLET
PARTS2_CSS += """
.dash{display:grid;grid-template-columns:220px 1fr;height:100%}
.dash aside{background:var(--tk-surface);border-right:1px solid var(--tk-line);padding:20px;display:flex;flex-direction:column;gap:8px}
.dash aside a{padding:10px 12px;border-radius:10px;color:var(--tk-ink);display:flex;justify-content:space-between;align-items:center}.dash aside a.on{background:var(--tk-brand-soft);font-weight:600}
.dash aside small{margin-top:auto;font-size:12px;color:var(--tk-ink-2)}.dash aside .unread{font-style:normal}
.dash main{padding:24px 32px;display:flex;flex-direction:column;gap:10px;overflow:hidden}
.dhead{display:flex;justify-content:space-between;align-items:center}.dhead h1{margin:0}
.drow{display:grid;grid-template-columns:44px 1fr 120px 140px;gap:12px;align-items:center;background:var(--tk-surface);border:1px solid var(--tk-line);border-radius:14px;padding:12px 14px}
.drow .ic{width:40px;height:40px;border-radius:12px;background:var(--tk-sunken);display:grid;place-items:center;font-size:20px}.drow .tx b{display:block}.drow .tx span{font-size:12px;color:var(--tk-ink-2)}
.dact{text-align:right;font-size:14px;color:var(--tk-brand-text);font-weight:600}.dact .btn{display:inline-flex;width:auto}
.dmsg{background:var(--tk-brand-soft);border-radius:14px;padding:12px 14px;display:flex;flex-direction:column;gap:2px}.dmsg span{font-size:13px;color:var(--tk-ink-2)}
.tablet{display:grid;grid-template-columns:360px 1fr;height:700px;border:1px solid var(--tk-line);border-radius:28px;overflow:hidden;background:var(--tk-surface);box-shadow:var(--tk-shadow)}
.tablet .tl{border-right:1px solid var(--tk-line);padding:22px 20px;display:flex;flex-direction:column;gap:12px}
.tablet .tl .tabs{margin:0 -20px -22px}
.tablet .tr{padding:56px 28px 24px;display:flex;flex-direction:column;gap:14px;background:var(--tk-bg)}
.item.sel{border-color:var(--tk-brand);background:var(--tk-brand-soft)}
@media (max-width:900px){.dash,.tablet{grid-template-columns:1fr;height:auto}.drow{grid-template-columns:44px 1fr}}
"""


# ---------- Real-life scenes (11 Nov 2026) ----------
# CSS-drawn settings (station, café, airport, park, home desk) behind phones and visuals,
# plus floating notification banners, so presentations look like real use, not blank frames.
def notif(title, body, when="now"):
    return f'<div class="fnotif"><span class="pic"><svg width="16" height="16"><use href="#mark"/></svg></span><span><b>{title}</b><small>{body}</small></span><em>{when}</em></div>'


def scene(kind):
    props = {
        "station": '<i class="sky"></i><i class="train"></i><i class="platform"></i><i class="edge"></i><span class="prop p1">🎒</span><span class="sign">Gleis 4</span>',
        "cafe": '<i class="wall"></i><i class="table"></i><span class="prop p1">☕</span><span class="prop p2">🎒</span><span class="prop p3">🪴</span>',
        "airport": '<i class="hall"></i><i class="belt"></i><span class="prop p1">🧳</span><span class="prop p2">🧳</span><span class="sign">Baggage 7 · FRA</span>',
        "park": '<i class="skyd"></i><i class="trees"></i><i class="grass"></i><span class="prop p1">🐕</span><span class="prop p2">🌳</span>',
        "home": '<i class="wall2"></i><i class="desktop"></i><span class="prop p1">💻</span><span class="prop p2">🔑</span><span class="prop p3">📷</span>',
    }[kind]
    return f'<div class="scene {kind}" aria-hidden="true">{props}</div>'


# Store panels: scene behind the phone + a live notification
_SC = {"s2": ("station", notif("Someone found your backpack", "With me · Darmstadt Hbf, platform 4")),
       "s3": ("cafe", notif("New message about your backpack", "“Left it with the barista, Mia.”", "2m")),
       "s4": ("park", notif("Milo’s tag was scanned", "Lost mode · near Herrngarten", "now")),
       "s5": ("airport", notif("Your suitcase was found", "Handed to staff · Baggage 7, FRA", "5m"))}
for k, (kind, n) in _SC.items():
    STORE = STORE.replace(f'<div class="st {k}">', f'<div class="st {k}">{scene(kind)}{n}', 1)
STORE = STORE.replace('<div class="st s1">', '<div class="st s1">' + scene("home"), 1)

# Marketing visuals
MKT = MKT.replace('<div class="mk cover">', '<div class="mk cover">' + scene("station") + notif("Someone found your backpack", "With me · Darmstadt Hbf, platform 4"), 1)
MKT = MKT.replace('<div class="mk sq dark">', '<div class="mk sq dark">' + scene("home"), 1)
MKT = MKT.replace('<div class="mk sq mint">', '<div class="mk sq mint">' + scene("station"), 1)
MKT = MKT.replace('<div class="mk sq soft">', '<div class="mk sq soft">' + scene("park"), 1)

# Lock screens get a wallpaper photo-like scene
EMAILS = EMAILS.replace('<div class="scr lock"', '<div class="scr lock wall-photo"', 1)
EXPORTS = EXPORTS.replace('<div class="scr lock lockimg"', '<div class="scr lock lockimg wall-photo"', 1)

# Website hero: phone in a café with a notification
WEB = WEB.replace('<div class="wphone">', '<div class="wphone">' + scene("cafe") + notif("New message about your backpack", "“Left it with the barista, Mia.”", "2m"), 1)

PARTS2_CSS += """
.scene{position:absolute;inset:0;overflow:hidden;z-index:0;pointer-events:none}
.scene i{position:absolute;display:block}
.scene .prop{position:absolute;font-size:56px;filter:drop-shadow(0 6px 8px rgb(0 0 0 / .25))}
.scene .sign{position:absolute;top:33%;right:7%;background:#0b3d91;color:#fff;font:700 12px var(--tk-font-body);padding:6px 10px;border-radius:4px;box-shadow:0 2px 0 rgb(0 0 0 / .2)}
.station .sky{inset:0 0 45% 0;background:linear-gradient(#bcd6e8,#e8eef0)}
.station .train{left:-10%;right:-10%;top:30%;height:22%;background:linear-gradient(#e9eef1 0 18%,#c41e2a 18% 24%,#e9eef1 24% 70%,#9aa6a1 70%);border-radius:18px}
.station .platform{inset:55% 0 0 0;background:linear-gradient(#a8aca9,#7f8582)}
.station .edge{left:0;right:0;top:55%;height:10px;background:repeating-linear-gradient(90deg,#f2c400 0 22px,#2b2b2b 22px 44px)}
.station .p1{left:10%;bottom:12%}
.cafe .wall{inset:0;background:linear-gradient(160deg,#6b4a35,#3a271b)}
.cafe .table{left:-10%;right:-10%;bottom:-8%;height:42%;background:linear-gradient(#b07a4f,#8a5a36);border-radius:50% 50% 0 0/20% 20% 0 0}
.cafe .p1{right:12%;bottom:20%}.cafe .p2{left:8%;bottom:16%}.cafe .p3{left:14%;top:12%;font-size:44px}
.airport .hall{inset:0;background:linear-gradient(#dfe6ea,#c7d0d4)}
.airport .belt{left:-10%;right:-10%;bottom:6%;height:24%;background:repeating-linear-gradient(90deg,#4d5558 0 26px,#3c4346 26px 52px);border-top:8px solid #9aa6a1}
.airport .p1{left:8%;bottom:16%}.airport .p2{right:10%;bottom:20%;font-size:46px}
.park .skyd{inset:0 0 40% 0;background:linear-gradient(#9fd3f0,#dff1e4)}
.park .trees{left:-10%;right:-10%;top:42%;height:22%;background:radial-gradient(circle at 15% 60%,#3f8f5a 0 18%,transparent 19%),radial-gradient(circle at 45% 50%,#2f7a4a 0 22%,transparent 23%),radial-gradient(circle at 80% 60%,#3f8f5a 0 20%,transparent 21%)}
.park .grass{inset:60% 0 0 0;background:linear-gradient(#7cc47f,#4f9c56)}
.park .p1{left:10%;bottom:10%}.park .p2{right:8%;top:30%;font-size:64px;filter:none;opacity:.9}
.home .wall2{inset:0;background:linear-gradient(160deg,#f3eee6,#e2d8c8)}
.home .desktop{left:-10%;right:-10%;bottom:-6%;height:38%;background:linear-gradient(#d9c3a2,#c2a57d)}
.home .p1{left:10%;bottom:16%}.home .p2{right:14%;bottom:12%;font-size:40px}.home .p3{right:10%;top:16%;font-size:44px}
.st>*:not(.scene),.mk>*:not(.scene){position:relative;z-index:1}
.st .tphone{position:absolute;z-index:2}
.st .fnotif,.mk .fnotif,.wphone .fnotif{position:absolute;z-index:4}
.st .sgift,.st .sicons,.st .bigtag{position:absolute;z-index:3}
.mk.cover .mphones{z-index:2}
.mk.cover .scene{opacity:.4}
.mk.sq.soft .eyebrow{color:#0b1712}
.mk.sq .scene{top:48%}
@media (max-width:600px){.mk.sq{aspect-ratio:auto;min-height:420px}.mk.sq h1{font-size:28px}}
.mk.sq.mint::after,.mk.sq.soft::after{display:none}
.mk.sq.dark .scene{top:0}
.st.s1 .home .p1{display:none}.st.s1 .home .p3{left:10%;right:auto;top:6%;font-size:36px}.st.s1 .home .p2{bottom:30%}
.st.s1 .bigtag{top:80px;width:210px;height:210px}
.mk.sq.dark .mtag .qr{width:88px;height:88px;background-size:11px 11px}.mk.sq h1{font-size:36px}
.st .fnotif{top:auto;bottom:250px;left:12px;right:12px}
.st.s1 .slogo,.st.s1 .ssub{background:rgb(255 255 255 / .85);border-radius:14px;padding:4px 10px}
.st .sh,.st .sp2{text-shadow:0 1px 12px rgb(0 0 0 / .25)}
.st.s2 .sh,.st.s2 .sp2{color:#fff}.st.s3 .sh,.st.s3 .sp2,.st.s5 .sh,.st.s5 .sp2{color:#fff}.st.s4 .sh,.st.s4 .sp2{color:#fff}
.st.s2::after,.st.s3::after,.st.s4::after,.st.s5::after,.mk.sq::after{content:"";position:absolute;inset:0 0 55% 0;background:linear-gradient(rgb(7 17 13 / .65),transparent);z-index:0}
.st .scene{opacity:.95}
.fnotif{position:absolute;z-index:3;left:14px;right:14px;top:46%;display:flex;gap:10px;align-items:flex-start;background:rgb(255 255 255 / .92);backdrop-filter:blur(14px);color:#0b1712;border-radius:18px;padding:10px 12px;box-shadow:0 12px 30px rgb(0 0 0 / .28);font-size:12px;text-align:left}
.fnotif b{display:block;font-size:13px}.fnotif small{color:#4f5e57}.fnotif em{margin-left:auto;font-style:normal;font-size:11px;color:#4f5e57;flex:none}
.fnotif .pic{width:26px;height:26px;border-radius:7px;background:#00c48c;color:#03261a;display:grid;place-items:center;flex:none}
.st.s1 .fnotif{display:none}
.mk.cover .fnotif{left:auto;right:28px;top:22px;width:300px}
.mk.cover::after{content:"";position:absolute;inset:0 45% 0 0;background:linear-gradient(90deg,rgb(0 196 140 / .95),rgb(0 196 140 / .75) 70%,transparent);z-index:0}
.mk.sq.dark .scene{opacity:.35}.mk.sq.mint .scene{opacity:.55}.mk.sq.soft .scene{opacity:.6}
.mk.sq .mtag,.mk.sq .bubble2{z-index:2}
.wall-photo{background:linear-gradient(rgb(0 0 0 / .15),rgb(0 0 0 / .35)),radial-gradient(circle at 70% 25%,#ffd9a0 0 8%,transparent 9%),linear-gradient(#f4a261 0%,#e76f51 28%,#2a3d66 62%,#0d1b2a 100%)!important}
.wall-photo::after{content:"";position:absolute;left:0;right:0;bottom:0;height:30%;background:linear-gradient(transparent,rgb(13 27 42 / .9)),repeating-linear-gradient(90deg,#14243a 0 30px,#1b2f4a 30px 46px,#14243a 46px 70px);opacity:.8;z-index:0}
.scr.lock{position:relative}.scr.lock>*{position:relative;z-index:1}
.wphone{position:relative;border-radius:28px;overflow:hidden;padding:40px 30px;min-height:520px;display:flex;align-items:center;justify-content:center}
.wphone .scr.mini{position:relative;z-index:2}.wphone .fnotif{top:auto;bottom:24px;left:auto;right:12px;width:260px}
"""
