"""Builds docs/design/tagkin-screens.html: all MVP screens with the Tagkin design applied.
Run: python3 docs/design/build_screens.py
Tokens come from docs/brand/tokens.css and are inlined so the page is self-contained
(needed for the browser preview and the one-time Figma import)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TOKENS = (ROOT / "docs/brand/tokens.css").read_text()
OUT = ROOT / "docs/design/tagkin-screens.html"

CSS = """
*{box-sizing:border-box}
body{margin:0;background:var(--tk-bg);color:var(--tk-ink);font:var(--tk-text-md)/1.5 var(--tk-font-body)}
.page{max-width:1600px;margin:auto;padding:32px max(16px,env(safe-area-inset-left,0px)) 64px}
.top{display:flex;justify-content:space-between;align-items:center;gap:16px;flex-wrap:wrap}
.brand{display:flex;align-items:center;gap:10px}
.brand b{font:700 26px/1 var(--tk-font-display);letter-spacing:-.02em}
.toggle{font:500 14px var(--tk-font-body);border:1px solid var(--tk-line);background:var(--tk-surface);color:var(--tk-ink);border-radius:99px;padding:8px 14px;cursor:pointer}
.flow h2{font:700 22px/1.2 var(--tk-font-display);margin:48px 0 4px;letter-spacing:-.01em}
.flow>p{margin:0 0 20px;color:var(--tk-ink-2);font-size:14px}
.row{display:flex;flex-wrap:wrap;gap:28px}
figure{margin:0;width:100%;max-width:360px}
figcaption{font:600 12px var(--tk-font-body);color:var(--tk-ink-2);letter-spacing:.04em;text-transform:uppercase;margin-bottom:8px}
.scr{background:var(--tk-surface);border:1px solid var(--tk-line);border-radius:36px;height:760px;padding:22px 20px 22px;display:flex;flex-direction:column;gap:14px;box-shadow:var(--tk-shadow);overflow:hidden}
.sbar{display:flex;justify-content:space-between;font:600 12px var(--tk-font-body);color:var(--tk-ink);padding:0 6px 4px}
.hdr{display:flex;justify-content:space-between;align-items:center;font-size:13px;color:var(--tk-ink-2);min-height:28px}
.logo{display:flex;align-items:center;gap:6px;color:var(--tk-ink);font:700 16px var(--tk-font-display);letter-spacing:-.01em}
.back{color:var(--tk-ink);font-weight:500}
.steps{display:flex;gap:4px}.steps i{width:22px;height:4px;border-radius:2px;background:var(--tk-line)}.steps i.on{background:var(--tk-brand)}
h1{font:700 var(--tk-text-xl)/1.2 var(--tk-font-display);letter-spacing:-.015em;margin:4px 0 0;text-wrap:balance}
h1.big{font-size:var(--tk-text-2xl)}
.m{color:var(--tk-ink-2);font-size:14px;margin:0}
.xs{color:var(--tk-ink-2);font-size:12px;margin:0}
.sp{flex:1}
.btn{font:600 16px/1 var(--tk-font-body);min-height:var(--tk-tap);border-radius:var(--tk-radius-md);display:flex;align-items:center;justify-content:center;gap:8px;border:1px solid transparent;flex:none}
.pri{background:var(--tk-brand);color:var(--tk-on-brand)}
.sec{background:var(--tk-surface);color:var(--tk-ink);border-color:var(--tk-line)}
.lostb{background:var(--tk-lost);color:var(--tk-on-lost)}
.ghost{color:var(--tk-ink-2);min-height:40px;font-weight:500}
.off{opacity:.4}
.in{background:var(--tk-sunken);border-radius:var(--tk-radius-md);min-height:var(--tk-tap);padding:0 16px;display:flex;align-items:center;color:var(--tk-ink-2);flex:none}
.in.val{color:var(--tk-ink)}
.in.focus{background:var(--tk-surface);box-shadow:inset 0 0 0 2px var(--tk-brand);color:var(--tk-ink)}
.ta{min-height:120px;align-items:flex-start;padding-top:14px}
.opt{border:1px solid var(--tk-line);border-radius:var(--tk-radius-md);min-height:60px;padding:0 16px;display:flex;align-items:center;gap:12px;font-weight:500;flex:none}
.opt .r{width:20px;height:20px;border-radius:50%;border:2px solid var(--tk-line);flex:none;display:grid;place-items:center}
.opt.on{border-color:var(--tk-brand);background:var(--tk-brand-soft);font-weight:600}
.opt.on .r{border-color:var(--tk-brand)}.opt.on .r::after{content:"";width:10px;height:10px;border-radius:50%;background:var(--tk-brand)}
.opt .ic{width:40px;height:40px;border-radius:12px;background:var(--tk-sunken);display:grid;place-items:center;font-size:20px;flex:none}
.opt.on .ic{background:var(--tk-surface)}
.opt small{display:block;font-weight:400;color:var(--tk-ink-2);font-size:13px}
.seg{display:flex;background:var(--tk-sunken);border-radius:var(--tk-radius-md);padding:4px;gap:4px;flex:none}
.seg span{flex:1;text-align:center;padding:10px;border-radius:10px;font-weight:500;font-size:14px;color:var(--tk-ink-2)}
.seg span.on{background:var(--tk-surface);color:var(--tk-ink);font-weight:600;box-shadow:var(--tk-shadow)}
.sug{display:flex;gap:10px;align-items:center;padding:12px 4px;border-bottom:1px solid var(--tk-line);font-size:15px}
.sug b{font-weight:600}
.badge{display:inline-flex;align-items:center;gap:6px;font:600 12px/1 var(--tk-font-body);padding:6px 10px;border-radius:99px;white-space:nowrap;flex:none}
.badge::before{content:"";width:6px;height:6px;border-radius:50%;background:currentColor}
.b-n{background:var(--tk-sunken);color:var(--tk-ink-2)}.b-l{background:var(--tk-lost);color:var(--tk-on-lost)}.b-r{background:var(--tk-brand-soft);color:var(--tk-brand-text)}
.note{border-radius:var(--tk-radius-md);padding:12px 14px;font-size:14px;margin:0;flex:none}
.warn{background:var(--tk-warn-soft);color:var(--tk-warn)}
.info{background:var(--tk-sunken);color:var(--tk-ink-2)}
.priv{display:flex;gap:8px;align-items:flex-start;font-size:12px;color:var(--tk-ink-2);margin:0;flex:none}
.priv svg{flex:none;margin-top:1px}
.urgent{background:var(--tk-lost);color:var(--tk-on-lost);border-radius:var(--tk-radius-md);padding:12px 14px;font-weight:600;display:flex;gap:10px;align-items:center;flex:none}
.urgent i{width:22px;height:22px;border-radius:50%;background:var(--tk-on-lost);color:var(--tk-lost);display:grid;place-items:center;font-style:normal;font-size:14px;font-weight:700}
.photo{height:200px;border-radius:var(--tk-radius-lg);background:linear-gradient(140deg,var(--tk-brand-soft),var(--tk-sunken) 60%);display:grid;place-items:center;font-size:56px;flex:none;position:relative}
.photo small{position:absolute;left:12px;bottom:10px;font-size:11px;color:var(--tk-ink-2);background:var(--tk-surface);padding:3px 8px;border-radius:99px}
.add{height:120px;border-radius:var(--tk-radius-lg);border:2px dashed var(--tk-line);display:grid;place-items:center;color:var(--tk-ink-2);font-size:14px;flex:none}
.link{color:var(--tk-brand-text);font-size:14px;text-decoration:underline;text-underline-offset:3px}
.item{display:flex;align-items:center;gap:12px;padding:12px 14px;border:1px solid var(--tk-line);border-radius:var(--tk-radius-md);flex:none}
.item .ic{width:42px;height:42px;border-radius:12px;background:var(--tk-sunken);display:grid;place-items:center;font-size:20px;flex:none}
.item .tx{flex:1;min-width:0}.item .tx b{display:block}.item .tx span{font-size:12px;color:var(--tk-ink-2)}
.li{display:flex;justify-content:space-between;align-items:center;padding:14px 2px;border-bottom:1px solid var(--tk-line);font-size:15px}
.li span:last-child{color:var(--tk-ink-2);font-size:14px}
.thread{display:flex;flex-direction:column;gap:10px}
.bub{max-width:86%;padding:10px 14px;border-radius:18px;font-size:14px}
.bub.in2{background:var(--tk-sunken);border-bottom-left-radius:6px}
.bub.out{background:var(--tk-brand);color:var(--tk-on-brand);align-self:flex-end;border-bottom-right-radius:6px}
.bub .meta{display:block;font-size:12px;color:var(--tk-brand-text);margin-top:4px;text-decoration:underline}
.compose{display:flex;gap:8px;align-items:center;flex:none}
.compose .in{flex:1}
.send{width:52px;height:52px;border-radius:50%;background:var(--tk-brand);color:var(--tk-on-brand);display:grid;place-items:center;font-size:20px;flex:none}
.notif{background:var(--tk-sunken);border-radius:20px;padding:14px;display:flex;gap:12px;flex:none}
.notif .ic{width:38px;height:38px;border-radius:10px;background:var(--tk-brand);color:var(--tk-on-brand);display:grid;place-items:center;flex:none}
.notif b{display:block;font-size:14px}.notif span{font-size:13px;color:var(--tk-ink-2)}
.code{display:flex;gap:8px;flex:none}.code i{flex:1;height:56px;border-radius:12px;background:var(--tk-sunken);display:grid;place-items:center;font:600 22px var(--tk-font-body);font-style:normal}
.code i.on{box-shadow:inset 0 0 0 2px var(--tk-brand);background:var(--tk-surface)}
.count{text-align:right;font-size:12px;color:var(--tk-ink-2);margin:-8px 0 0}
.chips{display:flex;gap:8px;flex-wrap:wrap;flex:none}
.chip{border:1px solid var(--tk-line);border-radius:99px;padding:8px 12px;font-size:13px;font-weight:500}
.chip.on{background:var(--tk-ink);color:var(--tk-surface);border-color:var(--tk-ink)}
.tag{width:200px;margin:4px auto 0;background:#fff;color:#0b1712;border:2px solid #0b1712;border-radius:var(--tk-radius-lg);padding:16px;text-align:center;flex:none}
.qr{width:120px;height:120px;margin:10px auto;background:repeating-conic-gradient(#0b1712 0 25%,#fff 0 50%) 0 0/15px 15px}
.tag p{margin:0;font-weight:600;font-size:14px}.tag small{display:block;font-weight:600;font-size:11px;color:#4f5e57;margin-top:4px;white-space:nowrap}
.done{width:84px;height:84px;border-radius:50%;background:var(--tk-brand-soft);color:var(--tk-brand-text);display:grid;place-items:center;font-size:40px;margin:0 auto;flex:none}
.center{text-align:center}
.lockrow{display:flex;gap:8px;align-items:center;font-size:13px;color:var(--tk-ink-2)}
.dots{display:flex;gap:6px;align-items:center;color:var(--tk-ink-2);font-size:13px}
.dots i{width:7px;height:7px;border-radius:50%;background:var(--tk-brand);animation:p 1.2s infinite}
.dots i:nth-child(2){animation-delay:.2s}.dots i:nth-child(3){animation-delay:.4s}
@keyframes p{50%{opacity:.25}}
.grp{display:flex;flex-direction:column;gap:10px;flex:none}
.tag.mini{width:150px;padding:10px;margin-top:0}.tag.mini .qr{width:70px;height:70px;background-size:10px 10px;margin:6px auto}
.qty{display:flex;justify-content:space-between;align-items:center;font-size:15px;flex:none}
.step{display:flex;align-items:center;gap:14px;background:var(--tk-sunken);border-radius:99px;padding:4px}
.step b{width:34px;height:34px;border-radius:50%;background:var(--tk-surface);display:grid;place-items:center;font-size:18px}
.step i{font-style:normal;font-weight:600;min-width:12px;text-align:center}
.li.total{font-weight:700}.li.total span:last-child{color:var(--tk-ink);font-size:16px}
.proto{border-style:dashed;color:var(--tk-ink-2);font-weight:500;font-size:14px}
@media (prefers-reduced-motion:reduce){.dots i{animation:none}}
"""

SVG = """<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
<mask id="mk" maskUnits="userSpaceOnUse" x="0" y="0" width="64" height="64"><rect width="64" height="64" fill="#fff"/><circle cx="22" cy="32" r="5" fill="#000"/><path d="M31 14 h5 v20 l8 -8 h7 l-9 9 l10 13 h-7 l-7 -9 l-2 2 v7 h-5 Z" fill="#000"/></mask>
<symbol id="mark" viewBox="0 0 64 64"><g mask="url(#mk)"><path fill="currentColor" stroke="currentColor" stroke-width="4" stroke-linejoin="round" d="M8 23 L23 9 H56 V55 H23 L8 41 Z"/></g></symbol>
<symbol id="lock" viewBox="0 0 16 16"><path fill="currentColor" d="M5 7V5a3 3 0 1 1 6 0v2h.5A1.5 1.5 0 0 1 13 8.5v5A1.5 1.5 0 0 1 11.5 15h-7A1.5 1.5 0 0 1 3 13.5v-5A1.5 1.5 0 0 1 4.5 7H5Zm1.5 0h3V5a1.5 1.5 0 1 0-3 0v2Z"/></symbol>
</defs></svg>"""

LOGO = '<span class="logo"><svg width="20" height="20"><use href="#mark"/></svg>tagkin</span>'
PRIV = '<p class="priv"><svg width="14" height="14"><use href="#lock"/></svg>Your details stay private unless you choose to share them.</p>'
SBAR = '<div class="sbar"><span>9:41</span><span>●●● ▮</span></div>'


def hdr(left=LOGO, right="EN ▾"):
    return f'<div class="hdr">{left}<span>{right}</span></div>'


def steps(n, total=4):
    bars = "".join(f'<i class="{"on" if i < n else ""}"></i>' for i in range(total))
    return f'<span class="steps" aria-label="Step {n} of {total}">{bars}</span>'


def back(to="Back"):
    return f'<span class="back">‹ {to}</span>'


def opt(label, on=False, ic=None, sub=None):
    left = f'<span class="ic">{ic}</span>' if ic else '<span class="r"></span>'
    sub = f"<small>{sub}</small>" if sub else ""
    return f'<div class="opt{" on" if on else ""}">{left}<span>{label}{sub}</span></div>'


def screen(name, body):
    return f'<figure data-name="{name}"><figcaption>{name}</figcaption><div class="scr">{SBAR}{body}</div></figure>'


FINDER = [
    ("Finder 0 · Enter code", hdr() + '<h1>Found something with a Tagkin tag?</h1><p class="m">Type the code printed under the QR.</p><div class="in focus">FND-4821</div><div class="btn pri">Find tag</div><div class="sp"></div>' + PRIV),
    ("Finder 1 · Owner message", hdr() + '<div class="photo">🎒<small>Photo updated 3 days ago</small></div><h1>Found me? Thank you! Tap below to tell my owner where I am.</h1><span class="link">Translated from German · Show original</span><div class="sp"></div><div class="btn pri">I found it</div>' + PRIV),
    ("Finder 1b · Lost mode", hdr() + '<div class="urgent"><i>!</i>This item is missing</div><div class="photo">🎒</div><h1>Black backpack</h1><p class="m">The owner is looking for it. Please tell them where it is.</p><div class="sp"></div><div class="btn pri">I found it</div>' + PRIV),
    ("Finder 2 · Where is it now?", hdr(back(), steps(1)) + '<h1>Where is it now?</h1>' + opt("With me", True) + opt("Handed to staff") + opt("Left where I found it") + '<div class="sp"></div><div class="btn pri">Next</div>'),
    ("Finder 3 · Where exactly?", hdr(back(), steps(2)) + '<h1>Where exactly?</h1><div class="in focus">hbf</div><div><div class="sug">📍<span><b>Darmstadt Hbf</b>, Lost &amp; Found desk</span></div><div class="sug">📍<span><b>Darmstadt Hbf</b>, Platform 4</span></div><div class="sug">📍<span><b>Darmstadt Hbf</b>, bus stop A</span></div></div><div class="btn sec">📍 Share item location</div><p class="xs">Only the city is shown unless you share the item location.</p><div class="sp"></div><div class="btn pri">Next</div>'),
    ("Finder 4 · Anything else?", hdr(back(), steps(3)) + '<h1>Anything else?</h1><div class="in ta val">Left it with the staff at counter 2. Call me on +49 151 2345678</div><p class="xs">Only add your number or email if you want the owner to contact you directly.</p><p class="note warn">This will share your number with the owner. Continue?</p><div class="sp"></div><div class="btn pri">Next</div><div class="btn ghost">Skip</div>'),
    ("Finder 5 · Want a reply?", hdr(back(), steps(4)) + '<h1>Want a reply?</h1><div class="seg"><span class="on">Email</span><span>Phone</span></div><div class="in">Email (kept hidden)</div><p class="xs">The owner never sees it. Replies are passed on by Tagkin.</p><p class="note info">Without an email or phone number, keep this page open to receive replies.</p><div class="sp"></div><div class="btn pri">Send to owner</div><div class="btn sec">Send anonymously</div>'),
    ("Finder 6 · Thank you", hdr() + '<div class="sp"></div><div class="done">✓</div><h1 class="big center">Thank you.</h1><p class="m center">The owner has been told where it is. Keep this page open to see their reply.</p><div class="thread"><div class="bub in2"><b>Owner</b><br>Thank you so much! I\'ll pick it up tonight.</div></div><div class="sp"></div><span class="xs center">Report abuse</span>'),
    ("Finder X · Tag not active", hdr() + '<div class="sp"></div><h1 class="center">This tag is no longer active.</h1><p class="m center">Please hand the item to staff or a lost-and-found desk.</p><div class="sp"></div><div class="btn sec">Enter another code</div>'),
]

def go(key):
    """Prototype link: harmless on the static page, used by the clickable prototype."""
    return f' data-go="{key}"'


def backto(key, label="Back"):
    return f'<span class="back"{go(key)}>‹ {label}</span>'


# (key, name, body). Keys are the prototype's screen ids.
OWNER = [
    ("signin", "Owner 1 · Sign in", hdr() + '<div class="sp"></div><h1 class="big">Make your first tag</h1><p class="m">No password. We send you a code.</p><div class="in val">selasey@example.com</div><div class="btn pri"' + go("code") + '>Send code</div><div class="sp"></div><p class="priv"><svg width="14" height="14"><use href="#lock"/></svg>Your contact is never shown. Finders message you through Tagkin.</p>'),
    ("code", "Owner 2 · Enter code", hdr(backto("signin")) + '<h1>Check your email</h1><p class="m">We sent a 6-digit code to s•••@example.com</p><div class="code"><i>4</i><i>8</i><i>2</i><i>9</i><i>1</i><i class="on">7</i></div><div class="btn pri"' + go("type") + '>Continue</div><p class="xs">Resend code in 30 s</p>'),
    ("type", "Owner 3 · Tag type", hdr(backto("code"), "1 of 5") + '<h1>What is it for?</h1><div class="grp">' + opt("Item", True, "🎒", "Keys, bag, laptop") + opt("Travel", False, "🧳", "Luggage on a journey") + opt("Pet", False, "🐾", "Collar tag") + '</div><p class="note info">You can\'t change the type later.</p><div class="sp"></div><div class="btn pri"' + go("details") + '>Next</div>'),
    ("details", "Owner 4 · Details", hdr(backto("type"), "2 of 5") + '<h1>Tell us about it</h1><div class="in val">Black backpack</div><div class="add">+ Add photo (optional)</div><div class="in">Description (optional)</div><div class="sp"></div><div class="btn pri"' + go("message") + '>Next</div>'),
    ("message", "Owner 5 · Finder message", hdr(backto("details"), "3 of 5") + '<h1>What should a finder read?</h1><div class="seg"><span class="on">Template</span><span>Write my own</span></div><div class="in ta val">Found me? Thank you! Tap below to tell my owner where I am.</div><p class="count">58 / 160</p><p class="note warn">If you add a phone number here, it will be public to anyone who scans.</p><p class="xs">Finders see it in their own language.</p><div class="sp"></div><div class="btn pri"' + go("design") + '>Next</div>'),
    ("design", "Owner 6 · Design", hdr(backto("message"), "4 of 5") + '<h1>Pick a style</h1><div class="chips"><span class="chip on">Sticker</span><span class="chip">Keychain</span><span class="chip">Pet tag</span><span class="chip">Luggage</span></div><div class="tag"><svg width="24" height="24" style="margin:auto;display:block;color:#0b1712"><use href="#mark"/></svg><div class="qr"></div><p>Found me? Scan to return</p><small>tagkin.app · FND-4821</small></div><p class="xs center">Address and code are always printed.</p><div class="sp"></div><div class="btn pri"' + go("live") + '>Next</div>'),
    ("live", "Owner 7 · Tag is live", hdr(backto("design"), "5 of 5") + '<div class="sp"></div><div class="done">✓</div><h1 class="center">Your tag is live.</h1><p class="m center">Black backpack · FND-4821</p><div class="btn pri"' + go("order") + '>Order printed tag</div><div class="btn sec" data-toast="Saved: tagkin-FND-4821.pdf">Download PNG or PDF</div><div class="btn sec" data-toast="Lock screen image saved to Photos">Save to phone lock screen</div><div class="btn ghost"' + go("tags") + '>Go to my tags</div><div class="sp"></div><p class="xs center">1 of 3 free tags used</p>'),
    ("order", "Owner 7c · Order your tag", hdr(backto("live"), "Order") + '<h1>Order your tag</h1><div class="tag mini"><svg width="18" height="18" style="margin:auto;display:block;color:#0b1712"><use href="#mark"/></svg><div class="qr"></div><small>tagkin.app · FND-4821</small></div><div class="grp">' + opt("Sticker", True, "🏷️", "Waterproof vinyl · €4.90") + opt("Keychain", False, "🔑", "Acrylic, 4 cm · €9.90") + opt("Pet tag", False, "🐾", "Metal, engraved · €12.90") + '</div><div class="qty"><span>Quantity</span><span class="step"><b>−</b><i>2</i><b>+</b></span></div><div class="sp"></div><div class="btn pri"' + go("checkout") + '>Continue · €9.80</div><p class="xs center">Sample prices until the print partner is chosen.</p>'),
    ("checkout", "Owner 7d · Checkout", hdr(backto("order"), "Order") + '<h1>Check and pay</h1><div><div class="li"><span>Sticker × 2</span><span>€9.80</span></div><div class="li"><span>Shipping to Germany</span><span>€2.50</span></div><div class="li total"><span>Total</span><span>€12.30</span></div></div><div class="in val">Selasey G., Musterstraße 1, 64283 Darmstadt</div><p class="note info">🔒 Payment is handled by our print partner. Tagkin never sees or stores card details.</p><div class="sp"></div><div class="btn pri"' + go("ordered") + '>Pay securely</div>'),
    ("ordered", "Owner 7e · Order placed", hdr() + '<div class="sp"></div><div class="done">✓</div><h1 class="center">Your tags are on the way.</h1><p class="m center">Arrives in 3 to 5 working days. Tracking comes by email.</p><p class="xs center">Order TK-10482 · 2 stickers</p><div class="sp"></div><div class="btn pri"' + go("tags") + '>Go to my tags</div>'),
    ("limit", "Owner 7b · Free limit reached", hdr(backto("tags")) + '<div class="sp"></div><h1 class="center">You\'ve used your 3 free tags.</h1><p class="m center">Retire a tag you no longer need, or wait for Premium.</p><div class="btn pri"' + go("tags") + '>Manage my tags</div><div class="btn sec" data-toast="We\'ll email you when Premium launches">Notify me about Premium</div><div class="sp"></div>'),
]

LOST = [
    ("tags", "Owner 8 · My tags", hdr(LOGO, '<span' + go("limit") + '>+ New</span>') + '<h1>My tags</h1><div class="item"' + go("detail") + '><span class="ic">🎒</span><span class="tx"><b>Black backpack</b><span>FND-4821</span></span><span class="badge b-n">Normal</span></div><div class="item"' + go("scans") + ' data-title="Milo"><span class="ic">🐾</span><span class="tx"><b>Milo</b><span>FND-7730</span></span><span class="badge b-l">Lost</span></div><div class="item"' + go("thread") + '><span class="ic">🧳</span><span class="tx"><b>Blue suitcase</b><span>FND-2196 · trip ends 20 Nov</span></span><span class="badge b-r">Return active</span></div><div class="sp"></div><p class="xs center">3 of 3 free tags used</p>'),
    ("detail", "Owner 9 · Tag detail", hdr(backto("tags", "My tags"), '<span class="badge b-n">Normal</span>') + '<div class="photo">🎒</div><h1>Black backpack</h1><div><div class="li"><span>Finder message</span><span>Edit ›</span></div><div class="li"><span>Contacts</span><span>Edit ›</span></div><div class="li"' + go("order") + '><span>Order printed tags</span><span>›</span></div></div><div class="sp"></div><div class="btn lostb"' + go("confirm") + '>Mark as lost</div><div class="btn ghost">Retire tag</div>'),
    ("confirm", "Owner 10 · Confirm Lost", hdr(backto("detail")) + '<h1>Mark Black backpack as lost?</h1><p class="m">Finders see an urgent page. You get an alert with the city every time it is scanned.</p><p class="note info">🔒 Name, photo and description lock until it is found. Contacts and message stay editable.</p><p class="note info">No reward amount is shown. You can thank the finder privately later.</p><div class="sp"></div><div class="btn lostb"' + go("scans") + ' data-title="Black backpack">Mark as lost</div><div class="btn sec"' + go("detail") + '>Cancel</div>'),
    ("scans", "Owner 11 · Lost: scans", hdr(backto("tags", "My tags"), '<span class="badge b-l">Lost</span>') + '<h1 class="ttl">Milo</h1><p class="m">Scans since marked lost</p><div><div class="li"><span>Today 14:02</span><span>Darmstadt</span></div><div class="li"><span>Today 09:41</span><span>Darmstadt</span></div><div class="li"><span>Yesterday 18:20</span><span>Griesheim</span></div></div><p class="xs">City only, unless a finder shares the item location.</p><p class="lockrow">🔒 Name and photo locked while lost</p><div class="sp"></div><div class="btn sec proto"' + go("alert") + '>Simulate: a finder reports it</div><div class="btn pri"' + go("tags") + '>I found it myself</div>'),
    ("alert", "Owner 12 · Finder report alert", '<div class="hdr"><span></span><span>now</span></div><div class="notif"' + go("thread") + '><span class="ic"><svg width="22" height="22"><use href="#mark"/></svg></span><span><b>Someone found Black backpack</b><span>With me · Darmstadt Hbf, Lost &amp; Found desk</span></span></div><div class="sp"></div><p class="m center">The tag is now in Return active. Name, photo and description are locked.</p><div class="btn pri"' + go("thread") + '>Open message</div>'),
    ("thread", "Owner 13 · Message thread", hdr(backto("tags", "My tags"), "Report · Block") + '<div class="thread"><div class="bub in2"><b>With me</b> · Darmstadt Hbf, Lost &amp; Found desk<br>I left it with the staff at counter 2.<span class="meta">Translated from French · Show original</span></div><div class="bub out">Thank you so much! I\'ll pick it up tonight.</div></div><p class="xs center">The finder left an email. Your reply reaches them translated.</p><div class="sp"></div><div class="btn sec"' + go("returned") + '>Got it back? Mark as returned</div><div class="compose"><div class="in">Write a reply</div><span class="send">↑</span></div>'),
    ("anon", "Owner 13b · Anonymous finder", hdr(backto("tags", "My tags"), "Report · Block") + '<div class="thread"><div class="bub in2"><b>Left where I found it</b> · Luisenplatz, bench by the fountain</div></div><p class="note info">This finder is anonymous. They see your reply only while their page is open.</p><div class="sp"></div><div class="compose"><div class="in">Write a reply</div><span class="send">↑</span></div>'),
    ("returned", "Owner 14 · Mark returned", hdr(backto("thread"), '<span class="badge b-r">Return active</span>') + '<h1>Got it back?</h1><p class="m">Locks lift and the tag goes back to Normal. The return closes on its own after 14 days with no messages.</p><div class="in ta">Private thank-you (optional)</div><div class="sp"></div><div class="btn pri"' + go("tags") + ' data-toast="Marked as returned">Mark as returned</div>'),
]


def flow(title, desc, screens):
    figs = "".join(screen(t[-2], t[-1]) for t in screens)
    return f'<section class="flow"><h2>{title}</h2><p>{desc}</p><div class="row">{figs}</div></section>'


html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Tagkin screens</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700&family=Inter:wght@400;500;600;700&display=swap">
<style id="tokens">
/* Generated from docs/brand/tokens.css by build_screens.py. Do not edit here. */
{TOKENS}</style>
<style>{CSS}</style>
</head>
<body>
{SVG}
<div class="page">
<header class="top"><div class="brand"><svg width="36" height="36"><use href="#mark"/></svg><b>tagkin</b></div><button class="toggle" type="button" id="theme">Switch to dark</button></header>
{flow("Finder flow", "No app, no sign-up. Tested with 5 people, no concerns.", FINDER)}
{flow("Owner registration and ordering", "Email code sign-in, five steps to a live tag, then order it printed.", OWNER)}
{flow("Lost mode and messages", "Urgent finder page, scan alerts, relayed messages.", LOST)}
</div>
<script>
const b=document.getElementById('theme'),r=document.documentElement;
b.onclick=()=>{{const d=r.getAttribute('data-theme')!=='dark';r.setAttribute('data-theme',d?'dark':'light');b.textContent=d?'Switch to light':'Switch to dark';}};
</script>
</body>
</html>
"""

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(html)
print(f"wrote {OUT.relative_to(ROOT)}: {len(FINDER) + len(OWNER) + len(LOST)} screens")

# ---------- Clickable owner prototype (same screens, one at a time) ----------
PROTO_OUT = ROOT / "docs/design/owner-prototype.html"
PROTO_CSS = """
body{display:flex;flex-direction:column;align-items:center;min-height:100vh;padding:0 max(16px,env(safe-area-inset-left,0px))}
.ctl{width:100%;max-width:420px;display:flex;flex-wrap:wrap;gap:8px;padding:12px 0;font-size:12px;color:var(--tk-ink-2);align-items:center}
.ctl button{font:500 12px var(--tk-font-body);border:1px solid var(--tk-line);background:var(--tk-surface);color:var(--tk-ink);border-radius:99px;padding:6px 10px;cursor:pointer}
.stage{width:100%;max-width:420px;position:relative}
.stage .scr{display:none;height:auto;min-height:760px;box-shadow:none}
.stage .scr.on{display:flex}
@media (max-width:500px){.stage .scr{min-height:calc(100vh - 60px);border-radius:24px}}
[data-go],[data-toast],.grp .opt,.chip,.seg span{cursor:pointer}
.btn[data-go]:active,.btn[data-toast]:active{transform:scale(.98)}
.toast{position:fixed;left:50%;bottom:calc(24px + env(safe-area-inset-bottom,0px));transform:translateX(-50%);background:var(--tk-ink);color:var(--tk-surface);padding:10px 16px;border-radius:99px;font-size:14px;opacity:0;transition:opacity var(--tk-slow);pointer-events:none}
.toast.show{opacity:1}
"""
PROTO_JS = """
const $=s=>document.querySelector(s),all=s=>document.querySelectorAll(s);
function show(id){all('.stage .scr').forEach(x=>x.classList.toggle('on',x.id===id));window.scrollTo(0,0);}
let tt;function toast(t){const e=$('.toast');e.textContent=t;e.classList.add('show');clearTimeout(tt);tt=setTimeout(()=>e.classList.remove('show'),1800);}
document.addEventListener('click',e=>{
  const o=e.target.closest('.grp .opt');if(o){o.parentElement.querySelectorAll('.opt').forEach(x=>x.classList.toggle('on',x===o));
    const price=o.querySelector('small')&&o.querySelector('small').textContent.match(/€([\\d.]+)/);if(price)updateTotal(parseFloat(price[1]));}
  const c=e.target.closest('.chip');if(c){c.parentElement.querySelectorAll('.chip').forEach(x=>x.classList.toggle('on',x===c));}
  const g=e.target.closest('.seg span');if(g){g.parentElement.querySelectorAll('span').forEach(x=>x.classList.toggle('on',x===g));}
  const st=e.target.closest('.step b');if(st){const q=st.parentElement.querySelector('i');let n=+q.textContent+(st.textContent==='+'?1:-1);q.textContent=Math.max(1,Math.min(20,n));updateTotal();}
  const t=e.target.closest('[data-title]');if(t){$('#scans .ttl').textContent=t.dataset.title;}
  const m=e.target.closest('[data-toast]');if(m)toast(m.dataset.toast);
  const l=e.target.closest('[data-go]');if(l)show(l.dataset.go);
});
let unit=4.90;
function updateTotal(u){if(u)unit=u;const q=+$('#order .step i').textContent;const name=$('#order .grp .opt.on span:last-child').firstChild.textContent;
  const sub=(unit*q).toFixed(2),tot=(unit*q+2.5).toFixed(2);
  $('#order .btn.pri').textContent='Continue · €'+sub;
  const rows=$('#checkout').querySelectorAll('.li');rows[0].innerHTML='<span>'+name+' × '+q+'</span><span>€'+sub+'</span>';rows[2].innerHTML='<span>Total</span><span>€'+tot+'</span>';
  $('#ordered .xs').textContent='Order TK-10482 · '+q+' × '+name.toLowerCase();}
all('[data-start]').forEach(b=>b.onclick=()=>show(b.dataset.start));
updateTotal();show('signin');
"""


def proto_screen(key, body):
    return f'<section class="scr" id="{key}">{SBAR}{body}</section>'


proto = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Tagkin owner prototype</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700&family=Inter:wght@400;500;600;700&display=swap">
<style id="tokens">
/* Generated from docs/brand/tokens.css by build_screens.py. Do not edit here. */
{TOKENS}</style>
<style>{CSS}{PROTO_CSS}</style>
</head>
<body>
{SVG}
<div class="ctl" aria-label="Prototype controls"><span>Prototype:</span>
<button type="button" data-start="signin">Register a tag</button>
<button type="button" data-start="tags">My tags</button>
<button type="button" data-start="anon">Anonymous finder</button>
</div>
<main class="stage">{"".join(proto_screen(t[0], t[2]) for t in OWNER + LOST)}</main>
<div class="toast" role="status" aria-live="polite"></div>
<script>{PROTO_JS}</script>
</body>
</html>
"""
PROTO_OUT.write_text(proto)
print(f"wrote {PROTO_OUT.relative_to(ROOT)}: {len(OWNER) + len(LOST)} screens")
