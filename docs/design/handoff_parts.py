# Hand-off sections for docs/design/tagkin-screens.html.
# Executed inside build_screens.py (shares its globals: hdr, LOGO, PRIV, SBAR, opt, lists of screens).
# Adds: cover, flow map, screen notes, component states and loading, emails and push,
# finder on desktop, tagkin.app website, marketing visuals and Community cover.
import re as _re

FINDER_PROTO_URL = "https://claude.ai/artifact/HyxUDEDyaY5EMghCdDWC6C"

# ---------- Screen notes (spec) ----------
NOTES = {
    "Finder 0 · Enter code": "Reached by typing tagkin.app (printed on every tag). Code is case- and space-insensitive. Wrong code → Finder 0b. Retired → Finder X. Unclaimed → Finder U.",
    "Finder 0b · Code not found": "Inline error, field keeps the typed code. No hint whether similar codes exist (prevents guessing).",
    "Finder 1 · Owner message": "Shown in the browser's language; Show original toggles. I found it → Finder 2. Photo date shows last edit (edit history rule).",
    "Finder 1b · Lost mode": "Owner turned on Lost mode. Never says \"stolen\", even in Stolen mode. Same report flow.",
    "Finder 1t · Travel tag": "Shows destination and operator only. Dates and home address are never shown. Hidden after the last travel date.",
    "Finder 1p · Pet tag": "Care notes stay behind a tap.",
    "Finder T · Owner test scan": "Owner turned on test mode (10 min). Nothing is sent, no alerts.",
    "Finder 2 · Where is it now?": "One choice required. Next is disabled until chosen.",
    "Finder 3 · Where exactly?": "Suggestions after 2 letters (places API). Share item location uses browser location; otherwise only the city is stored.",
    "Finder 4 · Anything else?": "Optional. Phone or email in the text (libphonenumber-js) shows the share warning; Next needs Continue.",
    "Finder 5 · Want a reply?": "Email or phone, hidden from the owner and relayed. Send anonymously skips it.",
    "Finder 6 · Thank you": "Owner reply appears live while the page is open. Invite card: first tag offer for the finder.",
    "Finder U · Tag not set up yet": "Unclaimed shop or gift tag. Activate opens the app or the store.",
    "Finder X · Tag not active": "Retired tag. No owner data is shown.",
    "Finder R · Report this tag": "Goes to moderation. 112 note for emergencies.",
    "Setup 5b · Pick your tag": "Each card preselects style and type: sticker, keychain and lock screen → item; luggage label → travel; pet tag → pet. A live preview card follows through details and message.",
    "Manage 7 · Status update": "Opt-in note on the finder page. City only, no dates or times. Hides automatically after the trip or 7 days.",
    "Owner 2 · Enter code": "6-digit email code, valid 10 minutes, 5 attempts.",
    "Owner 3 · Tag type": "Type is locked after creation. Item → details, Travel → Type 1, Pet → Type 2.",
    "Owner 5 · Finder message": "Template or own text, 160 characters, live count. Warns on phone or email; blocks abusive words.",
    "Owner 6 · Customise": "Preselected from type: item → sticker, travel → luggage label, pet → pet tag. Address and code always printed.",
    "Owner 7c · Order your tag": "For me / Gift a tag switch. Prices are samples until the print partner is chosen.",
    "Owner 7e · Review and pay": "First tag offer as a discount line (not a struck-through price, EU rule). Payment by Stripe or the print partner.",
    "Owner 10 · Confirm Lost": "Locks name, photo, description until found or returned.",
    "Owner 13 · Message thread": "Relayed and translated both ways. Report · Block in the header.",
    "Owner 14 · Mark returned": "Return also closes after 14 days with no messages.",
    "Manage 1 · Tag during a return": "Locked fields shown greyed with a lock. Message and contacts stay editable.",
    "Manage 5 · Retire tag": "Irreversible. Code never reused. Frees the free-tag slot.",
    "Manage 6 · QR code and test": "Test mode lasts 10 minutes: Test banner on the finder page, no alerts.",
    "Account 2 · Delete account": "Required by Apple and Google. Tags retired, data deleted, invoices kept as the law requires.",
    "Safety 1 · Report or block": "Blocked finder can't message about this tag. Reports reviewed within 24 h.",
    "Account 4 · Plan": "No Premium at launch. Notify me measures demand.",
    "Account 7 · Appearance": "Light, dark or match system. Default: match system.",
}

_ALL_KEYED = SETUP + OWNER + GIFT + LOST + STATES + EXTRA
_KEY2NAME = {k: n for k, n, _ in _ALL_KEYED}


def auto_links(body):
    out = []
    for key, inner in _re.findall(r'data-go="([\w-]+)"[^>]*>(.*?)</(?:div|span|label)>', body):
        text = _re.sub(r"<[^>]+>", " ", inner)
        text = _re.sub(r"\s+", " ", text).strip()[:40] or "Tap"
        if key in _KEY2NAME:
            pair = f"{text} → {_KEY2NAME[key].split(' · ', 1)[-1]}"
            if pair not in out:
                out.append(pair)
    return out


def note_html(name, body):
    parts = []
    if name in NOTES:
        parts.append(f"<p>{NOTES[name]}</p>")
    links = auto_links(body)
    if links:
        parts.append("<ul>" + "".join(f"<li>{l}</li>" for l in links[:6]) + "</ul>")
    return f'<div class="spec">{"".join(parts)}</div>' if parts else ""


# ---------- Component states and loading ----------
def frame(name, body, w=360, h=760, cls="scr"):
    return f'<figure data-name="{name}" style="max-width:{w}px"><figcaption>{name}</figcaption><div class="{cls}" style="height:{h}px">{body}</div></figure>'


STATES_UI = f"""<section class="flow"><h2>Component states and loading</h2><p>Every interactive component in each state, and loading screens.</p><div class="row">
{frame("States · Buttons and inputs", '<div class="sgrid"><span class="lbl">Primary</span><div class="btn pri">Default</div><div class="btn pri pressed">Pressed</div><div class="btn pri off">Disabled</div><div class="btn pri"><i class="spin"></i>Loading</div><span class="lbl">Secondary and danger</span><div class="btn sec">Secondary</div><div class="btn lostb">Danger</div><span class="lbl">Input</span><div class="in">Empty placeholder</div><div class="in focus">Focused</div><div class="in val">Filled value</div><div class="in errin val">Error</div><p class="errt">Explain what went wrong and how to fix it.</p></div>', 360, 800)}
{frame("States · Choices and toggles", '<div class="sgrid"><span class="lbl">Option</span>' + opt("Default") + opt("Selected", True) + '<span class="lbl">Switch</span><div class="li"><span>Off</span><span class="sw"><i></i></span></div><div class="li"><span>On</span><span class="sw on"><i></i></span></div><span class="lbl">Checkbox</span><label class="check"><i></i><span>Unchecked</span></label><label class="check on"><i>✓</i><span>Checked</span></label><span class="lbl">Segmented</span><div class="seg"><span class="on">Selected</span><span>Other</span></div><span class="lbl">Toast</span><div class="toastx">Saved</div></div>', 360, 760)}
{frame("Loading · My tags", SBAR + hdr(LOGO, "") + '<h1>My tags</h1>' + ''.join('<div class="item"><span class="ic sk"></span><span class="tx"><b class="sk skl"></b><span class="sk sks"></span></span><span class="sk skb"></span></div>' for _ in range(3)) + '<div class="sp"></div>' + tabbar("tags"))}
{frame("Loading · Finder page", SBAR + hdr() + '<div class="photo sk"></div><b class="sk skh"></b><b class="sk skh2"></b><span class="sk sks"></span><div class="sp"></div><div class="btn pri off">I found it</div>' + PRIV)}
{frame("Loading · Sending report", SBAR + hdr() + '<div class="sp"></div><div class="hero"><i class="spin big"></i></div><h1 class="center">Sending to the owner…</h1><p class="m center">This takes a second. Please keep this page open.</p><div class="sp"></div>')}
</div></section>"""


# ---------- Emails and push ----------
def email(name, subject, body):
    return f'<figure data-name="{name}" style="max-width:600px"><figcaption>{name}</figcaption><div class="mail"><div class="mhead"><b>{subject}</b><span>From Tagkin &lt;hello@tagkin.app&gt;</span></div><div class="mbody"><div class="mlogo"><svg width="22" height="22"><use href="#mark"/></svg>tagkin</div>{body}<p class="mfoot">You get this because you own a Tagkin tag. Tagkin relays messages so nobody sees your address. <u>Notification settings</u> · <u>Privacy</u> · Impressum</p></div></div></figure>'


EMAILS = f"""<section class="flow"><h2>Emails and push notifications</h2><p>The message relay in words. Emails go from hello@tagkin.app; replies are relayed, never forwarded with addresses.</p><div class="row">
{email("Email 1 · Owner: item found", "Someone found your Black backpack", '<h3>Good news. Someone found your Black backpack.</h3><div class="mcard"><b>With me</b><span>Darmstadt Hbf, Lost &amp; Found desk · today 14:02</span><p>“I left it with the staff at counter 2.”</p><small>Translated from French</small></div><div class="btn pri">Reply in the app</div><p class="m">The tag is now in Return active. Name, photo and description are locked until you mark it returned.</p>')}
{email("Email 2 · Finder: owner replied", "The owner replied about the backpack you found", '<h3>The owner replied.</h3><div class="mcard"><p>“Thank you so much! I’ll pick it up tonight.”</p><small>Translated from German</small></div><div class="btn pri">Reply</div><p class="m">Your email stays hidden from the owner. Want to protect your own things? Your first printed tag is €2 off.</p>')}
{email("Email 3 · Order confirmed", "Your Tagkin order TK-10482", '<h3>Thanks for your order.</h3><div class="mcard"><div class="li"><span>Sticker × 2</span><span>€9.80</span></div><div class="li"><span>Shipping</span><span>€2.50</span></div><div class="li"><span>First tag offer</span><span>−€2.00</span></div><div class="li total"><span>Total</span><span>€10.30</span></div></div><p class="m">Arrives in 3 to 5 working days. Your tags arrive already linked. We’ll email tracking when it ships.</p>')}
{email("Email 4 · Gift shipped", "Your gift for Kofi is on its way", '<h3>Your gift is on its way.</h3><p class="m">Sticker 3-pack for Kofi Boateng, Frankfurt. Prices are hidden on the packing slip. The tags stay unclaimed until Kofi activates them.</p><div class="btn sec">Track parcel</div>')}
<figure data-name="Push · Lock screen" style="max-width:360px"><figcaption>Push · Lock screen</figcaption><div class="scr lock" style="height:760px">{SBAR}<p class="ltime">14:03</p><p class="ldate">Wednesday 11 November</p><div class="pushl">{''.join(f'<div class="push"><span class="pic"><svg width="18" height="18"><use href="#mark"/></svg></span><span><b>{t}</b><small>{d}</small></span><em>{w}</em></div>' for t, d, w in [("Someone found Black backpack", "With me · Darmstadt Hbf. Tap to reply.", "now"), ("Milo's tag was scanned", "Lost mode · near Griesheim", "2 min"), ("New message about Blue suitcase", "“I left it with the staff at counter 2.”", "1 h"), ("Your tags have shipped", "TK-10482 · arrives Friday", "Mon")])}</div></div></figure>
</div></section>"""


# ---------- Finder on desktop ----------
def desk(name, body, h=760, url="tagkin.app/TK-7Q4M-9XRA"):
    if name.startswith('Desktop · Finder') or name.startswith('Web'):
        body = body + '<p class="legal dleg">Impressum · Privacy · Terms · Support</p>'
    return f'<figure data-name="{name}" class="wide" style="max-width:1200px"><figcaption>{name}</figcaption><div class="desk" style="height:{h}px"><div class="dbar"><i></i><i></i><i></i><span>{url}</span></div><div class="dbody">{body}</div></div></figure>'


DESK_FINDER = f"""<section class="flow"><h2>Finder on a computer</h2><p>Same steps as the phone, centred in a card. People often type tagkin.app on a laptop.</p><div class="row">
{desk("Desktop · Finder owner message", '<div class="dnav">' + LOGO + '<span>EN ▾</span></div><div class="dcard"><div class="photo">🎒<small>Photo updated 3 days ago</small></div><div class="dcol"><h1>Found me? Thank you! Tap below to tell my owner where I am.</h1><span class="link">Translated from German · Show original</span><div class="btn pri">I found it</div>' + PRIV + '</div></div>')}
{desk("Desktop · Finder where exactly", '<div class="dnav">' + LOGO + '<span>Step 2 of 4</span></div><div class="dcard one"><h1>Where exactly?</h1><div class="in focus">hbf</div><div><div class="sug">📍<span><b>Darmstadt Hbf</b>, Lost &amp; Found desk</span></div><div class="sug">📍<span><b>Darmstadt Hbf</b>, Platform 4</span></div></div><div class="two"><div class="btn sec">📍 Share item location</div><div class="btn pri">Next</div></div><p class="xs">Only the city is shown unless you share the item location.</p></div>')}
</div></section>"""


# ---------- Website ----------
WEB = f"""<section class="flow"><h2>tagkin.app website</h2><p>Home, privacy and support. Apple and Google require privacy and support links before approval.</p><div class="row">
{desk("Web · Home", '<div class="dnav">' + LOGO + '<span class="navl"><a>How it works</a><a>Shop tags</a><a>Gift a tag</a><a>Support</a><b class="btn pri sm">Get the app</b></span></div><div class="whero"><div><p class="eyebrow">QR tags for bags, keys, gear and pets</p><h1 class="wh">Protect what you value.</h1><p class="m">Whoever finds it scans the tag and alerts you privately, and you see where it was last scanned. No app needed for finders.</p><div class="two stores"><div class="btn pri">App Store</div><div class="btn sec">Google Play</div></div><p class="xs">For the careful and the forgetful. We all misplace things.</p></div><div class="wphone"><div class="scr mini">' + SBAR + hdr() + '<div class="urgent"><i>!</i>This item is missing</div><div class="photo sm">🎒</div><h1 class="md">Black backpack</h1><div class="sp"></div><div class="btn pri">I found it</div></div></div></div><div class="wsteps"><div><b>1</b><strong>Create your tag</strong><span>Link a QR code to a belonging.</span></div><div><b>2</b><strong>Get it printed</strong><span>Order it, or print it yourself.</span></div><div><b>3</b><strong>Stick it on</strong><span>It arrives ready, already linked.</span></div></div>', 900, "tagkin.app")}
{desk("Web · Privacy", '<div class="dnav">' + LOGO + '<span class="navl"><a>Home</a><a>Support</a></span></div><div class="dcard one doc"><h1>Privacy, in plain words</h1><p class="m">Last updated 11 Nov 2026. Full policy below.</p><div class="li"><span>Your contact details</span><span>Never shown to finders</span></div><div class="li"><span>Finder details</span><span>Hidden unless they share them</span></div><div class="li"><span>Location</span><span>City only, unless a finder shares the item location</span></div><div class="li"><span>Messages</span><span>Relayed, deleted after a set period</span></div><div class="li"><span>Selling data</span><span>Never</span></div><div class="li"><span>Your rights</span><span>Download or delete your data in the app</span></div><p class="xs">Full privacy policy · Terms of use · Impressum</p></div>', 760, "tagkin.app/privacy")}
{desk("Web · Support", '<div class="dnav">' + LOGO + '<span class="navl"><a>Home</a><a>Privacy</a></span></div><div class="dcard one doc"><h1>How can we help?</h1><div class="in">🔍 Search help</div><div class="li"><span>I found an item with a Tagkin tag</span><span>›</span></div><div class="li"><span>How do I activate a tag from a shop?</span><span>›</span></div><div class="li"><span>Where is my order?</span><span>›</span></div><div class="li"><span>How do I delete my account?</span><span>›</span></div><div class="li"><span>Report a tag or message</span><span>›</span></div><p class="m">Still stuck? Email <b>support@tagkin.app</b>. We reply within one working day.</p></div>', 760, "tagkin.app/support")}
</div></section>"""


# ---------- Flow map ----------
def fl(title, steps):
    return f'<div class="fl"><b>{title}</b><div class="flr">' + '<i>→</i>'.join(f'<span>{s}</span>' for s in steps) + '</div></div>'


FLOWMAP = f"""<section class="flow"><h2>Flow map</h2><p>Every journey at a glance. Screen names below match the frames.</p><div class="map">
{fl("Finder (web)", ["Scan QR or type code", "Owner message", "Where is it now?", "Where exactly?", "Anything else?", "Want a reply?", "Thank you + reply"])}
{fl("First launch", ["Welcome", "Private by default", "Terms", "Sign in", "Email code", "Notifications", "Add your first tag"])}
{fl("Create a tag", ["Create a tag", "Type", "Details (item, travel, pet)", "Finder message", "Style", "Tag is live", "Order or gift"])}
{fl("Activate a ready-made tag", ["Activate it", "Camera", "Scan or code", "New tag found", "Type, details, message", "Tag is live", "Activate another"])}
{fl("Order", ["For me / Gift a tag", "Product and quantity", "Delivery details", "Review and pay", "Order placed"])}
{fl("Lost and return", ["Mark as lost", "Scan alerts", "Finder report", "Messages", "Mark returned"])}
{fl("Manage", ["My tags", "Tag detail", "Edit message, contacts", "QR and test scan", "Retire"])}
{fl("Account", ["Plan", "Notifications", "Language", "Appearance", "Privacy and data", "Delete account"])}
<p class="xs">Tag states: Unclaimed → Normal ⇄ Lost → Return active → Normal · any state → Retired (permanent).</p>
</div></section>"""


# ---------- Marketing visuals ----------
def phone_mini(inner):
    return f'<div class="scr mini">{SBAR}{inner}</div>'


MKT = f"""<section class="flow"><h2>Marketing visuals</h2><p>Figma Community cover (1920 × 960) and square social posts (1080 × 1080, shown at half size).</p><div class="row">
<figure data-name="Community cover" class="wide" style="max-width:960px"><figcaption>Community cover</figcaption><div class="mk cover"><div><svg width="72" height="72"><use href="#mark"/></svg><h1>Protect what you value.</h1><p>Tagkin · QR tags for bags, keys, gear and pets. Scan, alert, return. Private by default.</p><small>78 screens · design system · prototypes</small></div><div class="mphones">{phone_mini(hdr() + '<div class="photo sm">🎒</div><h1 class="md">Found me? Thank you!</h1><div class="sp"></div><div class="btn pri">I found it</div>')}{phone_mini(hdr(LOGO, "") + '<h1 class="md">My tags</h1><div class="item"><span class="tx"><b>Milo 🐾</b><span>TK-M3PF-2KWD</span></span><span class="badge b-l">Lost</span></div><div class="item"><span class="tx"><b>Suitcase 🧳</b><span>TK-H8RC-4TNE</span></span><span class="badge b-r">Back</span></div>')}</div></div></figure>
<figure data-name="Social · For the careful" style="max-width:540px"><figcaption>Social · For the careful</figcaption><div class="mk sq dark"><p class="eyebrow">For the careful</p><h1>Your gear deserves a way home.</h1><div class="mtag"><svg width="28" height="28" style="color:#0b1712"><use href="#mark"/></svg><div class="qr"></div><small>tagkin.app · TK-7Q4M-9XRA</small></div><p>Private by default. No app needed to return it.</p></div></figure>
<figure data-name="Social · For the forgetful" style="max-width:540px"><figcaption>Social · For the forgetful</figcaption><div class="mk sq mint"><p class="eyebrow">For the forgetful</p><h1>We all forget things on the train.</h1><div class="bubble2">“Found your backpack at Darmstadt Hbf. It’s at counter 2.”</div><p>The finder scans it. You get the message.</p></div></figure>
<figure data-name="Social · Pets" style="max-width:540px"><figcaption>Social · Pets</figcaption><div class="mk sq soft"><p class="eyebrow">Pet tags</p><h1>Hi, I’m Milo. Please message my family.</h1><div class="pet">🐕</div><p>Care notes, translated messages, an alert for every scan.</p></div></figure>
</div></section>"""


# ---------- Cover / how to read ----------
COVER = f"""<section class="flow coverp"><div class="cov"><div><p class="eyebrow">Tagkin · design hand-off v1 · 11 Nov 2026</p><h1 class="wh">Protect what you value.</h1><p class="m">QR tags for bags, keys, gear and pets. Finders report without an app; owners manage tags in the app. Private by default, in many languages.</p></div><div class="covgrid">
<div><b>Read this file</b><span>Flow map → screens by journey → states → emails → web → marketing. Grey notes under each screen say what every button does.</span></div>
<div><b>Try it</b><span>Finder prototype: {FINDER_PROTO_URL}<br>Owner prototype: docs/design/owner-prototype.html in the repo</span></div>
<div><b>Source of truth</b><span>Rules: docs/PRODUCT-BRIEF.md · Tokens: docs/brand/tokens.css · Screens: docs/design/build_screens.py</span></div>
<div><b>Design system</b><span>Fresh mint, Bricolage Grotesque and Inter, 4-point spacing, radius 8/14/22, light and dark. WCAG AA checked.</span></div>
</div></div></section>"""

HANDOFF_CSS = """
.spec{margin-top:10px;font-size:12px;color:var(--tk-ink-2);background:var(--tk-sunken);border-radius:12px;padding:10px 12px}
.spec p{margin:0 0 6px}.spec ul{margin:0;padding-left:16px}.spec li{margin:2px 0}
.sgrid{display:flex;flex-direction:column;gap:10px}.lbl{font:600 11px var(--tk-font-body);letter-spacing:.05em;text-transform:uppercase;color:var(--tk-ink-2);margin-top:6px}
.pressed{background:var(--tk-brand-press);transform:scale(.98)}
.spin{width:16px;height:16px;border-radius:50%;border:2px solid currentColor;border-right-color:transparent;display:inline-block;animation:sp .8s linear infinite}
.spin.big{width:44px;height:44px;border-width:4px;color:var(--tk-brand)}
@keyframes sp{to{transform:rotate(360deg)}}
@media (prefers-reduced-motion:reduce){.spin{animation:none}}
.toastx{align-self:center;background:var(--tk-ink);color:var(--tk-surface);border-radius:99px;padding:10px 16px;font-size:14px}
.sk{background:linear-gradient(90deg,var(--tk-sunken),var(--tk-line),var(--tk-sunken));background-size:200% 100%;animation:sh 1.4s infinite;border-radius:8px;display:block}
@keyframes sh{to{background-position:-200% 0}}
@media (prefers-reduced-motion:reduce){.sk{animation:none}}
.skl{height:14px;width:60%;margin-bottom:6px}.sks{height:10px;width:40%}.skb{width:64px;height:24px;border-radius:99px;flex:none}.skh{height:22px;width:90%}.skh2{height:22px;width:70%}
.mail{background:var(--tk-surface);border:1px solid var(--tk-line);border-radius:16px;overflow:hidden;box-shadow:var(--tk-shadow)}
.mhead{padding:14px 18px;border-bottom:1px solid var(--tk-line);display:flex;flex-direction:column;gap:2px}.mhead span{font-size:12px;color:var(--tk-ink-2)}
.mbody{padding:24px;display:flex;flex-direction:column;gap:14px}.mlogo{display:flex;gap:6px;align-items:center;font:700 16px var(--tk-font-display)}
.mbody h3{font:700 22px/1.25 var(--tk-font-display);margin:0}.mcard{background:var(--tk-sunken);border-radius:12px;padding:14px;display:flex;flex-direction:column;gap:4px}
.mcard span,.mcard small{font-size:13px;color:var(--tk-ink-2)}.mcard p{margin:4px 0 0}.mbody .btn{align-self:flex-start;padding:0 24px}
.mfoot{font-size:11px;color:var(--tk-ink-2);border-top:1px solid var(--tk-line);padding-top:12px;margin:0}
.scr.lock{background:linear-gradient(160deg,#0f3a2c,#07110d);color:#fff}.scr.lock .sbar{color:#fff}
.ltime{font:600 64px/1 var(--tk-font-display);text-align:center;margin:20px 0 0}.ldate{text-align:center;margin:0;opacity:.8}
.pushl{display:flex;flex-direction:column;gap:8px;margin-top:20px}.push{display:flex;gap:10px;align-items:flex-start;background:rgb(255 255 255 / .14);backdrop-filter:blur(10px);border-radius:16px;padding:10px 12px;font-size:13px}
.push b{display:block}.push small{opacity:.85}.push em{margin-left:auto;font-style:normal;font-size:11px;opacity:.7;flex:none}.pic{width:28px;height:28px;border-radius:7px;background:#00c48c;color:#03261a;display:grid;place-items:center;flex:none}
figure.wide{width:100%}
.desk{border:1px solid var(--tk-line);border-radius:14px;overflow:hidden;background:var(--tk-bg);box-shadow:var(--tk-shadow);display:flex;flex-direction:column}
.dbar{display:flex;gap:6px;align-items:center;padding:10px 14px;background:var(--tk-sunken);border-bottom:1px solid var(--tk-line)}.dbar i{width:10px;height:10px;border-radius:50%;background:var(--tk-line)}.dbar span{margin-left:12px;font-size:12px;color:var(--tk-ink-2);background:var(--tk-surface);border-radius:8px;padding:4px 12px;flex:1;max-width:420px}
.dbody{flex:1;display:flex;flex-direction:column;overflow:hidden}
.dnav{display:flex;justify-content:space-between;align-items:center;padding:16px 32px;font-size:14px;color:var(--tk-ink-2)}
.navl{display:flex;gap:20px;align-items:center}.navl a{color:var(--tk-ink)}.btn.sm{min-height:40px;padding:0 16px;font-size:14px}
.dcard{margin:auto;width:min(860px,92%);background:var(--tk-surface);border-radius:24px;padding:32px;display:grid;grid-template-columns:1fr 1fr;gap:28px;box-shadow:var(--tk-shadow)}
.dcard.one{grid-template-columns:1fr;max-width:620px;gap:14px}.dcard .photo{height:100%;min-height:260px}.dcol{display:flex;flex-direction:column;gap:16px;justify-content:center}
.doc .li span:last-child{text-align:right}
.whero{display:grid;grid-template-columns:1.2fr 1fr;gap:40px;padding:24px 64px;align-items:center}
.eyebrow{font:600 12px var(--tk-font-body);letter-spacing:.06em;text-transform:uppercase;color:var(--tk-brand-text);margin:0}
.wh{font:700 56px/1.05 var(--tk-font-display);letter-spacing:-.03em;margin:8px 0 12px}
.stores{max-width:360px;margin:16px 0 8px}
.wphone{display:flex;justify-content:center}
.scr.mini{width:240px;height:480px;padding:14px 14px;gap:10px;border-radius:30px;font-size:13px}.scr.mini .btn{min-height:42px;font-size:14px}.scr.mini .photo.sm{height:110px}
.wsteps{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;padding:16px 64px 32px}.wsteps div{background:var(--tk-surface);border-radius:18px;padding:18px;display:flex;flex-direction:column;gap:4px}
.wsteps b{width:30px;height:30px;border-radius:50%;background:var(--tk-brand-soft);color:var(--tk-brand-text);display:grid;place-items:center;font:700 15px var(--tk-font-display)}.wsteps span{font-size:14px;color:var(--tk-ink-2)}
.map{display:flex;flex-direction:column;gap:12px;background:var(--tk-surface);border:1px solid var(--tk-line);border-radius:20px;padding:20px;overflow-x:auto}
.fl{display:flex;flex-direction:column;gap:6px}.fl>b{font:700 15px var(--tk-font-display)}
.flr{display:flex;flex-wrap:wrap;gap:6px;align-items:center}.flr span{background:var(--tk-brand-soft);color:var(--tk-ink);border-radius:10px;padding:6px 10px;font-size:13px}.flr i{font-style:normal;color:var(--tk-ink-2)}
.mk{border-radius:20px;overflow:hidden;position:relative;display:flex;flex-direction:column;gap:14px;padding:36px}
.mk h1{font:700 40px/1.05 var(--tk-font-display);letter-spacing:-.02em;margin:0}.mk p{margin:0;font-size:16px}
.mk.cover{min-height:480px;background:linear-gradient(120deg,#00c48c,#5cebc0);color:#03261a;flex-direction:row;align-items:center;justify-content:space-between}
.mk.cover>div:first-child{display:flex;flex-direction:column;gap:12px;max-width:46%}.mk.cover small{opacity:.75}
.mphones{display:flex;gap:16px}.mphones .scr.mini{width:200px;height:420px;color:var(--tk-ink);overflow:hidden}.mphones .scr.mini h1.md{font-size:18px}.mphones .scr.mini:last-child{margin-top:40px}
.mk.sq{aspect-ratio:1/1;justify-content:space-between}
.mk.dark{background:#0b1712;color:#eefaf5}.mk.dark .eyebrow{color:#1fe0a6}
.mk.mint{background:#00c48c;color:#03261a}.mk.mint .eyebrow{color:#03261a}
.mk.soft{background:#d9f7ec;color:#0b1712}
.mtag{align-self:center;background:#fff;border:3px solid #0b1712;border-radius:22px;padding:14px;text-align:center}.mtag .qr{width:110px;height:110px;margin:8px auto}.mtag small{font-size:11px;font-weight:600;color:#4f5e57}
.bubble2{align-self:flex-start;background:#fff;color:#0b1712;border-radius:22px 22px 22px 6px;padding:16px 18px;font-size:18px;max-width:85%;box-shadow:0 8px 24px rgb(0 0 0 / .12)}
.pet{font-size:120px;text-align:center;line-height:1}
.coverp .cov{background:var(--tk-surface);border:1px solid var(--tk-line);border-radius:24px;padding:32px;display:grid;grid-template-columns:1fr 1.3fr;gap:32px;margin-top:32px}
.covgrid{display:grid;grid-template-columns:1fr 1fr;gap:12px}.covgrid div{background:var(--tk-sunken);border-radius:14px;padding:14px;display:flex;flex-direction:column;gap:4px;font-size:13px;color:var(--tk-ink-2);overflow-wrap:anywhere}.covgrid b{color:var(--tk-ink);font-size:14px}
@media (max-width:900px){.coverp .cov,.whero,.dcard,.covgrid,.wsteps{grid-template-columns:1fr}.mk.cover{flex-direction:column;aspect-ratio:auto}.mk.cover>div:first-child{max-width:none}.desk{height:auto!important}.wh{font-size:40px}}
"""


# ---------- App Store and Google Play screenshot panels ----------
# Store size 1290 x 2796 (iPhone 6.9"), shown at 300 x 650. Concept panels: final store
# screenshots must use the real app UI, so these get re-shot from the build before launch.
def tilt_phone(inner, deg=-8, cls=""):
    return f'<div class="tphone {cls}" style="transform:rotate({deg}deg)"><div class="scr mini">{SBAR}{inner}</div></div>'


_P_FINDER = hdr() + '<div class="urgent"><i>!</i>This item is missing</div><div class="photo sm">🎒</div><h1 class="md">Black backpack</h1><p class="m">The owner is looking for it.</p><div class="sp"></div><div class="btn pri">I found it</div>'
_P_THREAD = hdr(back("Finder"), "") + '<div class="thread"><div class="bub in2"><b>With me</b> · Darmstadt Hbf<br>I left it at counter 2.<span class="meta">Translated from French</span></div><div class="bub out">Thank you so much 🙏</div></div><div class="sp"></div>'
_P_TAGS = hdr(LOGO, "") + '<h1 class="md">My tags</h1><div class="item"><span class="tx"><b>Camera bag 📷</b><span>TK-7Q4M-9XRA</span></span><span class="badge b-n">Safe</span></div><div class="item"><span class="tx"><b>Milo 🐾</b><span>TK-M3PF-2KWD</span></span><span class="badge b-l">Lost</span></div><div class="item"><span class="tx"><b>Suitcase 🧳</b><span>TK-H8RC-4TNE</span></span><span class="badge b-r">Return</span></div><div class="sp"></div>'
_P_TRAVEL = hdr() + '<div class="trip"><span>✈️</span><span><b>Travelling to Accra</b><small>With Lufthansa</small></span></div><div class="photo sm">🧳</div><h1 class="md">Please hand me to airline staff.</h1><div class="sp"></div><div class="btn pri">I found it</div>'


def store(name, cls, body):
    return f'<figure data-name="{name}" style="max-width:300px"><figcaption>{name}</figcaption><div class="st {cls}">{body}</div></figure>'


STORE = f"""<section class="flow"><h2>App Store and Google Play screenshots</h2><p>Concept set, 1290 × 2796 (shown at 300 × 650). The background pattern runs across panels like one strip. Re-shoot with the real app before submitting.</p><div class="row strip">
{store("Store 1 · Brand", "s1", '<div class="bigtag"><svg viewBox="0 0 64 64"><use href="#mark"/></svg></div><div class="slogo"><svg width="40" height="40"><use href="#mark"/></svg>tagkin</div><p class="ssub">Protect what you value.<br>Help it find its way back.</p>')}
{store("Store 2 · Finder alerts you", "s2", '<h2 class="sh">Someone finds it. You get alerted.</h2><p class="sp2">Whoever finds it scans the tag. No app, no sign-up.</p>' + tilt_phone(_P_FINDER, -7))}
{store("Store 3 · Private by default", "s3", '<h2 class="sh">Private<br>by default.</h2><p class="sp2">Messages are relayed. Nobody sees your number or email.</p>' + tilt_phone(_P_THREAD, 6) + '<div class="sicons"><span>🔒</span><span>💬</span><span>🌍</span><span>🛡️</span></div>')}
{store("Store 4 · Every belonging", "s4", '<h2 class="sh">Bags, keys, gear and pets.</h2><p class="sp2">Lost mode, scan alerts and a QR you can test anytime.</p>' + tilt_phone(_P_TAGS, -6))}
{store("Store 5 · Travel and languages", "s5", '<h2 class="sh">Every trip. Many languages.</h2><p class="sp2">Travel tags show where it’s going, never when you’re away. Messages translate both ways.</p>' + tilt_phone(_P_TRAVEL, 7) + '<div class="sgift">🎁 Gift a tag</div>')}
</div></section>"""

STORE_CSS = """
.strip{gap:0!important}
.strip figure{margin-right:12px}
.st{width:300px;height:650px;border-radius:22px;overflow:hidden;position:relative;display:flex;flex-direction:column;padding:34px 24px;gap:12px;
 background-image:radial-gradient(circle at center,transparent 26px,rgb(255 255 255 / .09) 27px,rgb(255 255 255 / .09) 29px,transparent 30px);background-size:72px 72px}
.st .sh{font:700 34px/1.02 var(--tk-font-display);letter-spacing:-.025em;margin:0;position:relative;z-index:1}
.st .sp2{font-size:15px;line-height:1.4;margin:0;opacity:.9;position:relative;z-index:1}
.s1{background-color:#00c48c;color:#03261a;justify-content:flex-end;align-items:center;text-align:center}
.s2{background-color:#0b1712;color:#eefaf5}.s2 .sh{color:#1fe0a6}
.s3{background-color:#00c48c;color:#03261a}
.s4{background-color:#0f3a2c;color:#eefaf5}.s4 .sh{color:#5cebc0}
.s5{background-color:#d9f7ec;color:#0b1712;background-image:radial-gradient(circle at center,transparent 26px,rgb(0 122 87 / .1) 27px,rgb(0 122 87 / .1) 29px,transparent 30px)}.s5 .sh{color:#007a57}.s5 .sgift{background:#0b1712;color:#fff}
.bigtag{position:absolute;top:60px;left:50%;width:250px;height:250px;transform:translateX(-50%) rotate(-14deg);color:#03261a;filter:drop-shadow(0 30px 40px rgb(3 38 26 / .35))}
.bigtag svg{width:100%;height:100%}
.slogo{display:flex;align-items:center;gap:10px;font:700 48px/1 var(--tk-font-display);letter-spacing:-.03em}
.ssub{font:600 18px/1.35 var(--tk-font-body);margin:0 0 30px}
.tphone{position:absolute;left:44px;bottom:-60px;filter:drop-shadow(0 24px 36px rgb(0 0 0 / .35))}
.tphone .scr.mini{width:230px;height:470px;color:var(--tk-ink);background:#fff;border:0}
.s3 .tphone,.s5 .tphone{left:auto;right:-16px}
.sicons{position:absolute;left:20px;bottom:24px;display:flex;flex-direction:column;gap:8px;z-index:2}
.sicons span{width:44px;height:44px;border-radius:12px;background:#03261a;display:grid;place-items:center;font-size:20px}
.sgift{position:absolute;left:20px;bottom:28px;background:#fff;color:#0b1712;border-radius:99px;padding:10px 16px;font-weight:700;z-index:2;box-shadow:0 8px 20px rgb(0 0 0 / .2)}
"""
