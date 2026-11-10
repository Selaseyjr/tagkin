# Hand-off part 2 (11 Nov 2026): sign-in email, printed tag artwork, lock-screen image,
# printable PDF sheet, permission recovery, languages, accessibility rules, Android icon,
# and the public showcase page for Figma Community.
# Executed inside build_screens.py after handoff_parts.py (shares its globals).

CODE = "TK-7Q4M-9XRA"

# ---------- Sign-in email ----------
EMAILS = EMAILS.replace('</div></section>', email("Email 0 · Sign-in code", "Your Tagkin sign-in code", '<h3>Your sign-in code</h3><div class="mcard codebox"><b>482 917</b></div><p class="m">Enter this code in the app. It works for 10 minutes. If you didn’t ask for it, you can ignore this email; nobody can sign in without the code.</p>') + '</div></section>', 1)


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

EXPORTS = f'<section class="flow"><h2>Downloads and lock screen</h2><p>What “Save to phone lock screen” and “Print at home (free tag)” produce. Only the free tag can be downloaded.</p><div class="row">{LOCKIMG}{PDF}</div></section>'


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
.legal.dleg{padding:12px 32px;text-align:left;margin-top:auto}
"""


# ---------- Public showcase for Figma Community ----------
def build_showcase():
    global SHOW_NOTES
    SHOW_NOTES = False
    pick = lambda lst, names: [t for t in lst if t[-2] in names]
    finder_pick = pick(FINDER, ["Finder 1 · Owner message", "Finder 1b · Lost mode", "Finder 2 · Where is it now?", "Finder 3 · Where exactly?", "Finder 5 · Want a reply?", "Finder 6 · Thank you", "Finder 1t · Travel tag", "Finder 1p · Pet tag"])
    owner_pick = pick(SETUP + OWNER + GIFT + LOST + EXTRA, ["Setup 1 · Welcome", "Setup 5 · Create a tag", "Owner 3 · Tag type", "Owner 6 · Customise", "Owner 7 · Tag is live", "Gift 1 · Gift a tag", "Owner 8 · My tags", "Owner 11 · Lost: scans", "Owner 13 · Message thread", "Manage 6 · QR code and test", "Account 7 · Appearance"])
    cover = """<section class="flow coverp"><div class="cov"><div><p class="eyebrow">Tagkin · app design</p><h1 class="wh">Protect what you value.</h1><p class="m">QR tags for bags, keys, gear and pets. Whoever finds something scans the tag and alerts the owner, privately. No app needed for finders.</p></div><div class="covgrid">
<div><b>What’s inside</b><span>Finder web flow, owner app, Gift a tag, store screenshots, printed tags and marketing visuals.</span></div>
<div><b>Design system</b><span>Fresh mint, Bricolage Grotesque and Inter, light and dark, WCAG AA contrast.</span></div>
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
