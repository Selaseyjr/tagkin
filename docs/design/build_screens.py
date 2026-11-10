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
.tabs{display:flex;justify-content:space-around;border-top:1px solid var(--tk-line);margin:0 -20px -22px;padding:8px 8px 14px;background:var(--tk-surface);flex:none}
.tab{display:flex;flex-direction:column;align-items:center;gap:2px;font-size:11px;font-weight:500;color:var(--tk-ink-2);position:relative;min-width:64px;padding:4px 0}
.tab.on{color:var(--tk-brand-text);font-weight:600}
.dot2{position:absolute;top:2px;right:16px;width:8px;height:8px;border-radius:50%;background:var(--tk-lost)}
.unread{min-width:22px;height:22px;border-radius:11px;background:var(--tk-brand);color:var(--tk-on-brand);font-size:12px;font-weight:700;display:grid;place-items:center;flex:none}
.item .tx b,.item .tx span{display:block;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.acct{display:flex;gap:12px;align-items:center;flex:none}.acct .av{width:48px;height:48px;border-radius:50%;background:var(--tk-brand);color:var(--tk-on-brand);display:grid;place-items:center;font:700 20px var(--tk-font-display)}
.acct b{display:block}.acct span span{font-size:13px;color:var(--tk-ink-2)}
.grpl .li:last-child{border-bottom:0}
.hero{display:grid;place-items:center;color:var(--tk-ink);flex:none}
.hero.lockh{width:110px;height:110px;margin:auto;border-radius:50%;background:var(--tk-brand-soft);color:var(--tk-brand-text)}
.bell{width:110px;height:110px;border-radius:50%;background:var(--tk-brand-soft);display:grid;place-items:center;font-size:48px}
.pager{display:flex;gap:6px;justify-content:center;flex:none}.pager i{width:8px;height:8px;border-radius:4px;background:var(--tk-line)}.pager i.on{width:22px;background:var(--tk-brand)}
.check{display:flex;gap:12px;align-items:flex-start;font-size:14px;flex:none;cursor:pointer}
.check i{width:22px;height:22px;border-radius:6px;border:2px solid var(--tk-line);flex:none;display:grid;place-items:center;font-style:normal;font-size:13px;font-weight:700;color:transparent}
.check.on i{background:var(--tk-brand);border-color:var(--tk-brand);color:var(--tk-on-brand)}
.cam{margin:0 -20px -22px;flex:1;display:flex;flex-direction:column;gap:14px;padding:22px 20px;background:linear-gradient(#1b2a24,#0a1410);color:#fff;border-radius:0 0 34px 34px}
.cam-h,.cam-h .back{color:#fff}.cam-t{color:#d8e6e0}
.frame{width:220px;height:220px;margin:auto;position:relative;flex:none}
.frame i{position:absolute;width:44px;height:44px;border:4px solid var(--tk-brand)}
.frame i:nth-child(1){top:0;left:0;border-right:0;border-bottom:0;border-radius:14px 0 0 0}
.frame i:nth-child(2){top:0;right:0;border-left:0;border-bottom:0;border-radius:0 14px 0 0}
.frame i:nth-child(3){bottom:0;left:0;border-right:0;border-top:0;border-radius:0 0 0 14px}
.frame i:nth-child(4){bottom:0;right:0;border-left:0;border-top:0;border-radius:0 0 14px 0}
.cam .btn.sec{background:rgb(255 255 255 / .12);border-color:rgb(255 255 255 / .25);color:#fff}
.warnc{background:var(--tk-warn-soft);color:var(--tk-warn);font-weight:700}
.dangert{color:var(--tk-lost-text)}
.errin{box-shadow:inset 0 0 0 2px var(--tk-lost)}
.errt{color:var(--tk-lost-text);font-size:13px;margin:-6px 0 0}
.errc{background:var(--tk-lost-soft);color:var(--tk-lost-text);font-weight:700}
.offl{background:var(--tk-ink);color:var(--tk-surface)}
.dim{opacity:.6}
.bub.failed{opacity:.6}
.failt{align-self:flex-end;font-size:12px;color:var(--tk-lost-text);font-weight:600;cursor:pointer}
.lockedp{filter:grayscale(.6)}
.savet{color:var(--tk-brand-text);font-weight:600}
.label2{font:600 12px var(--tk-font-body);color:var(--tk-ink-2);letter-spacing:.04em;text-transform:uppercase;flex:none}
.preview{border:1px dashed var(--tk-line);border-radius:var(--tk-radius-md);padding:12px 14px;flex:none}
.preview b{display:block;font:700 16px/1.3 var(--tk-font-display)}.preview span{font-size:12px;color:var(--tk-ink-2)}
.btn.proto-l{min-height:32px}
.proto-l{text-decoration:underline dashed;color:var(--tk-ink-2)}
.trip{display:flex;gap:12px;align-items:center;background:var(--tk-brand-soft);border-radius:var(--tk-radius-md);padding:12px 14px;flex:none}
.trip>span:first-child{font-size:24px}.trip b{display:block}.trip small{color:var(--tk-ink-2);font-size:13px}
.plan{border:1px solid var(--tk-line);border-radius:var(--tk-radius-lg);padding:14px 16px;flex:none}
.plan b{font:700 18px var(--tk-font-display)}.plan span{display:block;font-size:13px;color:var(--tk-ink-2)}
.plan ul{margin:8px 0 0;padding-left:18px;font-size:14px}.plan li{margin:2px 0}
.plan.prem{background:var(--tk-brand-soft);border-color:var(--tk-brand)}
.plan em{font:600 11px var(--tk-font-body);font-style:normal;background:var(--tk-brand);color:var(--tk-on-brand);border-radius:99px;padding:3px 8px;margin-left:6px;vertical-align:middle}
.sw{width:46px;height:28px;border-radius:14px;background:var(--tk-line);position:relative;flex:none;cursor:pointer;transition:background var(--tk-fast)}
.sw i{position:absolute;top:3px;left:3px;width:22px;height:22px;border-radius:50%;background:#fff;box-shadow:0 1px 3px rgb(0 0 0 / .2);transition:left var(--tk-fast) var(--tk-ease)}
.sw.on{background:var(--tk-brand)}.sw.on i{left:21px}
.li.on{font-weight:600}.li.on span:last-child{color:var(--tk-brand-text)}
.splash{margin:0 -20px -22px;flex:1;background:var(--tk-brand);color:var(--tk-on-brand);display:flex;flex-direction:column;align-items:center;gap:12px;padding:24px;border-radius:0 0 34px 34px}
.splash b{font:700 40px var(--tk-font-display);letter-spacing:-.02em}
.splash small{font-size:12px;opacity:.8}
.icons{display:flex;gap:16px}
.appicon{width:76px;height:76px;border-radius:18px;background:var(--tk-brand);color:#03261a;display:grid;place-items:center;box-shadow:0 0 0 2px rgb(3 38 26 / .25)}
.appicon.dk{background:#0b1712;color:#1fe0a6}
.photo.sm{height:130px;font-size:44px}.add.sm{height:72px}.ta.sm{min-height:76px}h1.md{font-size:22px}
input.in{font:400 16px var(--tk-font-body);color:var(--tk-ink);border:0;width:100%;outline:none}
input.in::placeholder{color:var(--tk-ink-2)}
input.in:focus{background:var(--tk-surface);box-shadow:inset 0 0 0 2px var(--tk-brand)}
.two{display:flex;gap:10px;flex:none}.two>*{flex:1;min-width:0}.two input.in:first-child{flex:0 0 38%}
.sel{justify-content:space-between}
.addr{display:flex;justify-content:space-between;align-items:flex-start;gap:12px;border:1px solid var(--tk-line);border-radius:var(--tk-radius-md);padding:12px 14px;flex:none}
.addr small{display:block;font-size:12px;color:var(--tk-ink-2)}.addr b{display:block}.addr .a-line{font-size:14px;color:var(--tk-ink-2)}
.prod .opt{min-height:54px}
#t-details .chip,figure[data-name="Type 1 · Travel details"] .chip{padding:6px 10px;font-size:12px}
.themes{display:flex;gap:10px;flex:none}
.th{flex:1;border:1px solid var(--tk-line);border-radius:var(--tk-radius-md);padding:12px 8px;display:flex;flex-direction:column;align-items:center;gap:8px;font-size:13px;text-align:center;cursor:pointer}
.th.on{border:2px solid var(--tk-brand);background:var(--tk-brand-soft);padding:11px 7px}
.thp{width:56px;height:72px;border-radius:12px;display:grid;place-items:center;border:1px solid var(--tk-line)}
.thp.light{background:#fff;color:#0b1712}.thp.dark{background:#0b1712;color:#1fe0a6}.thp.auto{background:linear-gradient(90deg,#fff 50%,#0b1712 50%);color:#00c48c}
.qrb{width:36px;height:36px;border-radius:10px;border:1px solid var(--tk-line);display:grid;place-items:center;color:var(--tk-ink);flex:none;margin-left:-4px}
.bigqr{align-self:center;background:#fff;border-radius:var(--tk-radius-lg);padding:18px;text-align:center;box-shadow:var(--tk-shadow);flex:none}
.bigqr .qr{width:170px;height:170px;background-size:17px 17px;margin:0 auto 8px}
.bigqr small{font-weight:600;font-size:13px;color:#4f5e57}
.testbox{display:flex;gap:12px;align-items:flex-start;background:var(--tk-sunken);border-radius:var(--tk-radius-md);padding:12px 14px;flex:none}
.testbox b{display:block}.testbox small{font-size:13px;color:var(--tk-ink-2)}
.testban{background:var(--tk-warn-soft);color:var(--tk-warn);border-radius:var(--tk-radius-md);padding:10px 12px;font-size:13px;font-weight:600;flex:none}
.emo{width:44px;height:44px;border-radius:50%;display:grid;place-items:center;font-size:24px;color:var(--tk-ink-2);flex:none;cursor:pointer}
.emo.on{background:var(--tk-brand-soft);color:var(--tk-brand-text)}
.picker{background:var(--tk-sunken);border-radius:var(--tk-radius-lg);padding:10px;display:flex;flex-direction:column;gap:8px;flex:none}
.picker[hidden]{display:none}
.pk-s{min-height:40px;background:var(--tk-surface);font-size:14px}
.pk-cats{display:flex;justify-content:space-between;padding:0 4px}.pk-cats span{font-size:18px;padding:4px 6px;border-radius:8px;opacity:.6}.pk-cats span.on{opacity:1;background:var(--tk-surface)}
.pk-grid{display:grid;grid-template-columns:repeat(8,1fr);gap:2px}.pk-grid span{font-size:24px;text-align:center;padding:4px 0;border-radius:8px;cursor:pointer}
.pk-grid span:hover{background:var(--tk-surface)}
.how{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:14px;flex:none}.how li{display:flex;gap:14px;align-items:flex-start}.how b{width:32px;height:32px;border-radius:50%;background:var(--tk-brand-soft);color:var(--tk-brand-text);display:grid;place-items:center;font:700 16px var(--tk-font-display);flex:none}.how strong{display:block;font-weight:600}.how span{font-size:14px;color:var(--tk-ink-2)}.how strong{color:var(--tk-ink);font-size:16px}
.steps3{display:flex;gap:8px;flex:none}.steps3 span{flex:1;background:var(--tk-sunken);border-radius:var(--tk-radius-md);padding:10px 8px;font-size:12px;text-align:center;color:var(--tk-ink-2)}.steps3 b{display:block;font:700 18px var(--tk-font-display);color:var(--tk-brand-text)}
.link.center{text-align:center;display:block}
.li.offer span{color:var(--tk-brand-text);font-weight:600}
figure .proto-l,figure .proto{display:none}
.acct.tight~.grpl .li{padding:10px 2px}
.invite{border:1px solid var(--tk-brand);background:var(--tk-brand-soft);border-radius:var(--tk-radius-md);padding:12px 14px;flex:none}.invite b{display:block}.invite span{font-size:13px;color:var(--tk-ink-2)}
.legal{font-size:11px;color:var(--tk-ink-2);text-align:center;margin:0;flex:none;text-decoration:underline;text-underline-offset:2px}
.gal{display:grid;grid-template-columns:1fr 1fr;gap:10px;flex:none}
.gcard{border:1px solid var(--tk-line);border-radius:var(--tk-radius-md);padding:10px;display:flex;flex-direction:column;gap:2px;cursor:pointer}
.gcard:last-child{grid-column:span 2;flex-direction:row;align-items:center;gap:10px}.gcard:last-child .gobj{height:56px;width:70px}
.gcard b{font-size:14px}.gcard small{font-size:11px;color:var(--tk-ink-2)}
.gcard.on{border:2px solid var(--tk-brand);padding:9px;background:var(--tk-brand-soft)}
.gobj{height:76px;border-radius:12px;background:var(--tk-sunken);display:grid;place-items:center;font-size:40px;position:relative;margin-bottom:6px}
.gtag{position:absolute;right:16px;bottom:12px;width:24px;height:24px;border-radius:50%;background:#fff;border:2px solid #0b1712;color:#0b1712;display:grid;place-items:center;font-style:normal}
.gtag.kc{border-radius:6px;right:22px;bottom:8px}.gtag.pt{border-radius:50%;background:#e6ebe9;bottom:6px}.gtag.lb{border-radius:4px;width:18px;height:28px;right:12px}.gtag.ls{border-radius:4px;width:16px;height:22px;right:24px;bottom:16px}
.livepv{display:flex;gap:10px;align-items:center;background:var(--tk-sunken);border-radius:var(--tk-radius-md);padding:8px 10px;flex:none}
.lpt{width:42px;height:42px;border-radius:10px;background:#fff;border:1.5px solid #0b1712;color:#0b1712;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:1px;flex:none}
.lpt .qr{width:16px;height:16px;background-size:4px 4px;margin:0}
.lpx{flex:1;min-width:0}.lpx b,.lpx small{display:block;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}.lpx b{font-size:13px}.lpx small{font-size:11px;color:var(--tk-ink-2)}
.lp-style{font-style:normal;font-size:11px;font-weight:600;color:var(--tk-brand-text);flex:none}
.qty small{display:block;font-size:12px;color:var(--tk-ink-2)}
.stat{margin:0;font-size:13px;font-weight:600;color:var(--tk-brand-text);flex:none}
textarea.in{font:400 16px var(--tk-font-body);color:var(--tk-ink);border:0;width:100%;outline:none;resize:none;padding:14px 16px}
textarea.in:focus{background:var(--tk-surface);box-shadow:inset 0 0 0 2px var(--tk-brand)}
.proto{border-style:dashed;color:var(--tk-ink-2);font-weight:500;font-size:14px}
@media (prefers-reduced-motion:reduce){.dots i{animation:none}}
"""

SVG = """<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
<mask id="mk" maskUnits="userSpaceOnUse" x="0" y="0" width="64" height="64"><rect width="64" height="64" fill="#fff"/><circle cx="22" cy="32" r="5" fill="#000"/><path d="M31 14 h5 v20 l8 -8 h7 l-9 9 l10 13 h-7 l-7 -9 l-2 2 v7 h-5 Z" fill="#000"/></mask>
<symbol id="mark" viewBox="0 0 64 64"><g mask="url(#mk)"><path fill="currentColor" stroke="currentColor" stroke-width="4" stroke-linejoin="round" d="M8 23 L23 9 H56 V55 H23 L8 41 Z"/></g></symbol>
<symbol id="i-tag" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round" d="M3 9 8 4h13v16H8l-5-5Z"/><circle cx="9" cy="12" r="1.6" fill="currentColor"/></symbol>
<symbol id="i-chat" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round" d="M4 5h16v11H9l-5 4Z"/></symbol>
<symbol id="i-box" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round" d="M3 7.5 12 3l9 4.5v9L12 21l-9-4.5Z M3 7.5 12 12l9-4.5 M12 12v9"/></symbol>
<symbol id="i-user" viewBox="0 0 24 24"><circle cx="12" cy="8" r="4" fill="none" stroke="currentColor" stroke-width="2"/><path fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" d="M4 21c1.5-4 4.5-6 8-6s6.5 2 8 6"/></symbol>
<symbol id="i-sun" viewBox="0 0 24 24"><circle cx="12" cy="12" r="4.5" fill="none" stroke="currentColor" stroke-width="2"/><path stroke="currentColor" stroke-width="2" stroke-linecap="round" d="M12 2v2M12 20v2M2 12h2M20 12h2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></symbol>
<symbol id="i-moon" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round" d="M20 14.5A8 8 0 0 1 9.5 4a8 8 0 1 0 10.5 10.5Z"/></symbol>
<symbol id="i-auto" viewBox="0 0 24 24"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="2"/><path fill="currentColor" d="M12 3.5a8.5 8.5 0 0 1 0 17Z"/></symbol>
<symbol id="i-qr" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="2" d="M4 4h6v6H4ZM14 4h6v6h-6ZM4 14h6v6H4Z"/><path fill="currentColor" d="M14 14h3v3h-3ZM17 17h3v3h-3ZM14 19h2v1h-2ZM19 14h1v2h-1Z"/></symbol>
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


LEGAL = '<p class="legal">Impressum · Privacy · Terms</p>'


def screen(name, body):
    if name.startswith("Finder"):
        body = body + LEGAL
    note = note_html(name, body) if "note_html" in globals() and SHOW_NOTES else ""
    return f'<figure data-name="{name}"><figcaption>{name}</figcaption><div class="scr">{SBAR}{body}</div>{note}</figure>'


FINDER = [
    ("Finder 0 · Enter code", hdr() + '<h1>Found something with a Tagkin tag?</h1><p class="m">Type the code printed under the QR.</p><div class="in focus">TK-7Q4M-9XRA</div><div class="btn pri">Find tag</div><div class="sp"></div>' + PRIV),
    ("Finder 0b · Code not found", hdr() + '<h1>Found something with a Tagkin tag?</h1><p class="m">Type the code printed under the QR.</p><div class="in focus errin">TK-7Q4M-9XAR</div><p class="errt">No tag with that code. Check the letters and numbers and try again.</p><div class="btn pri">Find tag</div><div class="sp"></div>' + PRIV),
    ("Finder 1 · Owner message", hdr() + '<div class="photo">🎒<small>Photo updated 3 days ago</small></div><h1>Found me? Thank you! Tap below to tell my owner where I am.</h1><span class="link">Translated from German · Show original</span><div class="sp"></div><div class="btn pri">I found it</div>' + PRIV),
    ("Finder 1b · Lost mode", hdr() + '<div class="urgent"><i>!</i>This item is missing</div><div class="photo">🎒</div><h1>Black backpack</h1><p class="m">The owner is looking for it. Please tell them where it is.</p><div class="sp"></div><div class="btn pri">I found it</div>' + PRIV),
    ("Finder 2 · Where is it now?", hdr(back(), steps(1)) + '<h1>Where is it now?</h1>' + opt("With me", True) + opt("Handed to staff") + opt("Left where I found it") + '<div class="sp"></div><div class="btn pri">Next</div>'),
    ("Finder 3 · Where exactly?", hdr(back(), steps(2)) + '<h1>Where exactly?</h1><div class="in focus">hbf</div><div><div class="sug">📍<span><b>Darmstadt Hbf</b>, Lost &amp; Found desk</span></div><div class="sug">📍<span><b>Darmstadt Hbf</b>, Platform 4</span></div><div class="sug">📍<span><b>Darmstadt Hbf</b>, bus stop A</span></div></div><div class="btn sec">📍 Share item location</div><p class="xs">Only the city is shown unless you share the item location.</p><div class="sp"></div><div class="btn pri">Next</div>'),
    ("Finder 4 · Anything else?", hdr(back(), steps(3)) + '<h1>Anything else?</h1><div class="in ta val">Left it with the staff at counter 2. Call me on +49 151 2345678</div><p class="xs">Only add your number or email if you want the owner to contact you directly.</p><p class="note warn">This will share your number with the owner. Continue?</p><div class="sp"></div><div class="btn pri">Next</div><div class="btn ghost">Skip</div>'),
    ("Finder 5 · Want a reply?", hdr(back(), steps(4)) + '<h1>Want a reply?</h1><div class="seg"><span class="on">Email</span><span>Phone</span></div><div class="in">Email (kept hidden)</div><p class="xs">The owner never sees it. Replies are passed on by Tagkin.</p><p class="note info">Without an email or phone number, keep this page open to receive replies.</p><div class="sp"></div><div class="btn pri">Send to owner</div><div class="btn sec">Send anonymously</div>'),
    ("Finder 6 · Thank you", hdr() + '<div class="sp"></div><div class="done">✓</div><h1 class="big center">Thank you.</h1><p class="m center">The owner has been told where it is. Keep this page open to see their reply.</p><div class="thread"><div class="bub in2"><b>Owner</b><br>Thank you so much! I\'ll pick it up tonight.</div></div><div class="sp"></div><div class="invite"><b>Protect your own things</b><span>Your first printed tag is €2 off.</span></div><span class="xs center">Report abuse</span>'),
    ("Finder 1t · Travel tag", hdr() + '<div class="trip"><span>✈️</span><span><b>I\'m travelling to Accra</b><small>With Lufthansa · from Frankfurt</small></span></div><p class="stat">✓ Owner update: arrived in Accra</p><div class="photo sm">🧳</div><h1 class="md">Please hand me to airline or hotel staff, or message my owner.</h1><span class="link">Translated from German · Show original</span><div class="sp"></div><div class="btn pri">I found it</div>' + PRIV),
    ("Finder 1p · Pet tag", hdr() + '<div class="photo sm">🐕<small>Photo updated 1 week ago</small></div><h1 class="md">Hi, I\'m Milo. I\'m friendly. Please message my owner. I may be scared.</h1><div class="chips"><span class="chip">Friendly</span><span class="chip">Shy with dogs</span></div><div class="li"><span>Care notes</span><span>Show ›</span></div><div class="sp"></div><div class="btn pri">I found Milo</div>' + PRIV),
    ("Finder R · Report this tag", hdr(back(), "") + '<h1>Report this tag</h1><p class="m">Tell us what\'s wrong. Your report is private.</p>' + '<div class="grp">' + opt("The message is abusive or spam") + opt("It looks fake or misleading", True) + opt("Something else") + '</div><p class="note warn">If someone is in danger, call 112 now.</p><div class="sp"></div><div class="btn pri">Send report</div>'),
    ("Finder T · Owner test scan", hdr() + '<div class="testban">Test scan · The owner is testing this tag. Nothing you send here reaches anyone.</div><div class="photo">🎒<small>Photo updated 3 days ago</small></div><h1>Found me? Thank you! Tap below to tell my owner where I am.</h1><div class="sp"></div><div class="btn pri">I found it</div>' + PRIV),
    ("Finder U · Tag not set up yet", hdr() + '<div class="sp"></div><div class="hero"><span class="bell"><svg width="52" height="52"><use href="#mark"/></svg></span></div><h1 class="center">This tag isn\'t set up yet.</h1><p class="m center">If you found it on something, please hand it to staff or a lost-and-found desk.</p><div class="sp"></div><p class="xs center">Is this your tag?</p><div class="btn pri">Activate it in the Tagkin app</div>'),
    ("Finder X · Tag not active", hdr() + '<div class="sp"></div><h1 class="center">This tag is no longer active.</h1><p class="m center">Please hand the item to staff or a lost-and-found desk.</p><div class="sp"></div><div class="btn sec">Enter another code</div>'),
]

def go(key):
    """Prototype link: harmless on the static page, used by the clickable prototype."""
    return f' data-go="{key}"'


def backto(key, label="Back"):
    return f'<span class="back"{go(key)}>‹ {label}</span>'


def livepv(name="Black backpack", msg="Found me? Thank you! Tap below…", style="Sticker"):
    return f'<div class="livepv"><span class="lpt"><svg width="16" height="16"><use href="#mark"/></svg><i class="qr"></i></span><span class="lpx"><b class="lp-name">{name}</b><small class="lp-msg">{msg}</small></span><em class="lp-style">{style}</em></div>'


def tabbar(active):
    tabs = [("tags", "i-tag", "My tags"), ("inbox", "i-chat", "Messages"), ("orders", "i-box", "Orders"), ("account", "i-user", "Account")]
    items = "".join(
        f'<span class="tab{" on" if k == active else ""}"{go(k)}><svg width="24" height="24"><use href="#{ic}"/></svg>{label}{"<b class=dot2></b>" if k == "inbox" and active != "inbox" else ""}</span>'
        for k, ic, label in tabs)
    return f'<nav class="tabs" aria-label="Main">{items}</nav>'


# (key, name, body). Keys are the prototype's screen ids.
OWNER = [
    ("signin", "Owner 1 · Sign in", hdr() + '<div class="sp"></div><h1 class="big">Make your first tag</h1><p class="m">No password. We send you a code.</p><div class="in val">alex@example.com</div><div class="btn pri"' + go("code") + '>Send code</div><div class="sp"></div><p class="priv"><svg width="14" height="14"><use href="#lock"/></svg>Your contact is never shown. Finders message you through Tagkin.</p>'),
    ("code", "Owner 2 · Enter code", hdr(backto("signin")) + '<h1>Check your email</h1><p class="m">We sent a 6-digit code to a•••@example.com</p><div class="code"><i>4</i><i>8</i><i>2</i><i>9</i><i>1</i><i class="on">7</i></div><div class="btn pri"' + go("perm-notif") + '>Continue</div><p class="xs">Resend code in 30 s</p>'),
    ("pick", "Setup 5b · Pick your tag", hdr(backto("start"), "") + '<h1>Pick your tag</h1><p class="m">See how it will look. You can change it later.</p><div class="gal">' + ''.join(f'<div class="gcard" data-style="{st}" data-type="{ty}"' + go("type") + f'><span class="gobj">{ob}<i class="gtag {cl}"><svg width="12" height="12"><use href="#mark"/></svg></i></span><b>{st}</b><small>{sub}</small></div>' for st, ty, ob, cl, sub in [("Sticker", 0, "🎒", "", "Bags, laptops, cases"), ("Keychain", 0, "🔑", "kc", "Keys and fobs"), ("Pet tag", 2, "🐕", "pt", "Collars"), ("Luggage label", 1, "🧳", "lb", "Suitcases"), ("Lock screen", 0, "📱", "ls", "Your phone, free")]) + '</div>'),
    ("type", "Owner 3 · Tag type", hdr(backto("code"), "1 of 5") + '<h1>What is it for?</h1><div class="grp">' + opt("Item", True, "🎒", "Keys, bag, laptop") + opt("Travel", False, "🧳", "Luggage on a journey") + opt("Pet", False, "🐾", "Collar tag") + '</div><p class="note info">You can\'t change the type later.</p><div class="sp"></div><div class="btn pri"' + go("details") + '>Next</div>'),
    ("details", "Owner 4 · Details", hdr(backto("type"), "2 of 5") + livepv() + '<h1>Tell us about it</h1><input class="in" id="it-name" value="Black backpack" aria-label="Name"><div class="add">+ Add photo (optional)</div><input class="in" placeholder="Description (optional)" aria-label="Description"><div class="sp"></div><div class="btn pri"' + go("message") + '>Next</div>'),
    ("message", "Owner 5 · Finder message", hdr(backto("details"), "3 of 5") + livepv() + '<h1>What should a finder read?</h1><div class="seg"><span class="on">Template</span><span>Write my own</span></div><textarea class="in ta sm" id="it-msg" maxlength="160" aria-label="Finder message">Found me? Thank you! Tap below to tell my owner where I am.</textarea><p class="count" id="it-count">58 / 160</p><p class="note warn">If you add a phone number here, it will be public to anyone who scans.</p><p class="xs">Finders see it in their own language.</p><div class="sp"></div><div class="btn pri"' + go("design") + '>Next</div>'),
    ("design", "Owner 6 · Design", hdr(backto("message"), "4 of 5") + '<h1>Pick a style</h1><p class="m pick">Suggested for an item: <b>Sticker</b>. You can choose another.</p><div class="chips styles"><span class="chip on">Sticker</span><span class="chip">Keychain</span><span class="chip">Pet tag</span><span class="chip">Luggage label</span><span class="chip">Lock screen</span></div><div class="tag"><svg width="24" height="24" style="margin:auto;display:block;color:#0b1712"><use href="#mark"/></svg><div class="qr"></div><p class="tagline">Found me? Scan to return</p><small>tagkin.app · TK-7Q4M-9XRA</small></div><p class="xs center">Address and code are always printed.</p><div class="sp"></div><div class="btn pri"' + go("live") + '>Next</div>'),
    ("live", "Owner 7 · Tag is live", hdr(backto("design"), "5 of 5") + '<div class="sp"></div><div class="done">✓</div><h1 class="center">Your tag is live.</h1><p class="m center">Black backpack · TK-7Q4M-9XRA</p><div class="btn pri"' + go("order") + '>Order printed tag</div><div class="btn sec" data-toast="Saved: tagkin-TK-7Q4M-9XRA.pdf">Download PNG or PDF</div><div class="btn sec" data-toast="Lock screen image saved to Photos">Save to phone lock screen</div><div class="btn ghost"' + go("tags") + '>Go to my tags</div><div class="sp"></div><span class="link center"' + go("gift") + '>🎁 Gift a tag to someone who values their things</span><p class="xs center">This is your free tag. Printed tags you buy are always free to use.</p>'),
    ("order", "Owner 7c · Order your tag", hdr(backto("live"), "1 of 3") + '<div class="seg"><span class="on">For me</span><span' + go("gift") + '>Gift a tag</span></div><h1>Order your tag</h1><p class="m ordfor">Sticker style · TK-7Q4M-9XRA</p><div class="grp prod">' + opt("Sticker", True, "🏷️", "Waterproof vinyl · €4.90") + opt("Keychain", False, "🔑", "Acrylic, 4 cm · €9.90") + opt("Pet tag", False, "🐾", "Metal, engraved · €12.90") + opt("Luggage label", False, "🧳", "Strap and tag · €11.90") + '</div><div class="qty"><span>Copies of this tag<small>Same code on each, e.g. phone and case</small></span><span class="step"><b>−</b><i>2</i><b>+</b></span></div><div class="sp"></div><div class="btn pri"' + go("delivery") + '>Continue to delivery</div><p class="xs center">🎁 First printed tag: €2 off at checkout · sample prices</p>'),
    ("delivery", "Owner 7d · Delivery details", hdr(backto("order"), "2 of 3") + '<h1>Where should we send it?</h1><input class="in" id="d-name" value="Alex Mensah" aria-label="Full name"><input class="in" id="d-street" value="Musterstraße 1" aria-label="Street and number"><div class="two"><input class="in" id="d-zip" value="64283" aria-label="Postcode"><input class="in" id="d-city" value="Darmstadt" aria-label="City"></div><div class="in val sel">Germany <span>▾</span></div><input class="in" id="d-phone" placeholder="Phone for the courier (optional)" aria-label="Phone for the courier"><p class="xs">Tracking goes to a•••@example.com. Your address is shared only with the print partner, to deliver this order.</p><div class="sp"></div><div class="btn pri"' + go("checkout") + '>Continue to payment</div>'),
    ("checkout", "Owner 7e · Review and pay", hdr(backto("delivery"), "3 of 3") + '<h1>Review and pay</h1><div><div class="li"><span>Sticker × 2</span><span>€9.80</span></div><div class="li"><span>Shipping to Germany</span><span>€2.50</span></div><div class="li offer"><span>First tag offer</span><span>−€2.00</span></div><div class="li total"><span>Total</span><span>€10.30</span></div></div><div class="addr"' + go("delivery") + '><span><small>Deliver to</small><b class="a-name">Alex Mensah</b><span class="a-line">Musterstraße 1, 64283 Darmstadt, Germany</span></span><span class="link">Change</span></div><p class="xs">🔒 Card, Apple Pay, Google Pay or PayPal, handled by our print partner. Tagkin never sees card details.</p><div class="sp"></div><div class="btn pri paybtn"' + go("ordered") + '>Pay €10.30</div><div class="btn ghost proto-l"' + go("err-pay") + '>Simulate: payment fails</div>'),
    ("ordered", "Owner 7f · Order placed", hdr() + '<div class="sp"></div><div class="done">✓</div><h1 class="center">Your tags are on the way.</h1><p class="m center">Arrives in 3 to 5 working days. Tracking comes by email.</p><p class="xs center">Order TK-10482 · 2 stickers</p><div class="sp"></div><div class="btn pri"' + go("tags") + '>Go to my tags</div>'),
    ("limit", "Owner 7b · Free tag in use", hdr(backto("tags")) + '<div class="sp"></div><h1 class="center">Your free tag is in use.</h1><p class="m center">Every printed tag you buy works for life, at no extra cost. Or retire your free tag to start a new one.</p><div class="btn pri"' + go("order") + '>Order a printed tag</div><div class="btn sec"' + go("tags") + '>Manage my tags</div><div class="sp"></div>'),
]

LOST = [
    ("tags", "Owner 8 · My tags", hdr(LOGO, '<span' + go("limit") + '>+ New</span>') + '<h1>My tags</h1><div class="item"' + go("detail") + '><span class="ic">🎒</span><span class="tx"><b>Black backpack</b><span>TK-7Q4M-9XRA</span></span><span class="qrb"' + go("qr") + ' aria-label="Show QR code"><svg width="20" height="20"><use href="#i-qr"/></svg></span></div><div class="item"' + go("scans") + ' data-title="Milo"><span class="ic">🐾</span><span class="tx"><b>Milo</b><span>TK-M3PF-2KWD</span></span><span class="badge b-l">Lost</span><span class="qrb"' + go("qr") + ' aria-label="Show QR code"><svg width="20" height="20"><use href="#i-qr"/></svg></span></div><div class="item"' + go("locked") + '><span class="ic">🧳</span><span class="tx"><b>Blue suitcase</b><span>TK-H8RC-4TNE · trip ends 20 Nov</span></span><span class="badge b-r">Return active</span><span class="qrb"' + go("qr") + ' aria-label="Show QR code"><svg width="20" height="20"><use href="#i-qr"/></svg></span></div><p class="xs center">1 free tag in use · printed tags never count</p><div class="sp"></div>' + tabbar("tags")),
    ("detail", "Owner 9 · Tag detail", hdr(backto("tags", "My tags"), '<span class="badge b-n">Normal</span>') + '<div class="photo sm">🎒</div><h1>Black backpack</h1><div><div class="li"' + go("edit-msg") + '><span>Finder message</span><span>Edit ›</span></div><div class="li"' + go("edit-contacts") + '><span>Contacts</span><span>Edit ›</span></div><div class="li"' + go("status") + '><span>Status update</span><span>Off ›</span></div><div class="li"' + go("qr") + '><span>QR code and test scan</span><span>›</span></div><div class="li"' + go("history") + '><span>Scan history</span><span>2 scans ›</span></div><div class="li"' + go("order") + '><span>Order printed tags</span><span>›</span></div></div><div class="sp"></div><div class="btn lostb"' + go("confirm") + '>Mark as lost</div><div class="btn ghost"' + go("retire") + '>Retire tag</div>'),
    ("confirm", "Owner 10 · Confirm Lost", hdr(backto("detail")) + '<h1>Mark Black backpack as lost?</h1><p class="m">Finders see an urgent page. You get an alert with the city every time it is scanned.</p><p class="note info">🔒 Name, photo and description lock until it is found. Contacts and message stay editable.</p><p class="note info">No reward amount is shown. You can thank the finder privately later.</p><div class="sp"></div><div class="btn lostb"' + go("scans") + ' data-title="Black backpack">Mark as lost</div><div class="btn sec"' + go("detail") + '>Cancel</div>'),
    ("scans", "Owner 11 · Lost: scans", hdr(backto("tags", "My tags"), '<span class="badge b-l">Lost</span>') + '<h1 class="ttl">Milo</h1><p class="m">Scans since marked lost</p><div><div class="li"><span>Today 14:02</span><span>Darmstadt</span></div><div class="li"><span>Today 09:41</span><span>Darmstadt</span></div><div class="li"><span>Yesterday 18:20</span><span>Griesheim</span></div></div><p class="xs">City only, unless a finder shares the item location.</p><p class="lockrow">🔒 Name and photo locked while lost</p><div class="sp"></div><div class="btn sec proto"' + go("alert") + '>Simulate: a finder reports it</div><div class="btn pri"' + go("tags") + '>I found it myself</div>'),
    ("alert", "Owner 12 · Finder report alert", '<div class="hdr"><span></span><span>now</span></div><div class="notif"' + go("thread") + '><span class="ic"><svg width="22" height="22"><use href="#mark"/></svg></span><span><b>Someone found Black backpack</b><span>With me · Darmstadt Hbf, Lost &amp; Found desk</span></span></div><div class="sp"></div><p class="m center">The tag is now in Return active. Name, photo and description are locked.</p><div class="btn pri"' + go("thread") + '>Open message</div>'),
    ("thread", "Owner 13 · Message thread", hdr(backto("tags", "My tags"), '<span' + go("report-owner") + '>Report · Block</span>') + '<div class="thread"><div class="bub in2"><b>With me</b> · Darmstadt Hbf, Lost &amp; Found desk<br>I left it with the staff at counter 2.<span class="meta">Translated from French · Show original</span></div><div class="bub out">Thank you so much! I\'ll pick it up tonight.</div></div><span class="proto-l xs center"' + go("err-send") + '>Simulate: reply fails to send</span><p class="xs center">The finder left an email. Your reply reaches them translated.</p><div class="sp"></div><div class="btn sec"' + go("returned") + '>Got it back? Mark as returned</div><div class="picker" hidden><div class="in pk-s">🔍 Search emoji</div><div class="pk-cats"><span class="on">😀</span><span>👍</span><span>❤️</span><span>🎒</span><span>🚆</span><span>🐾</span></div><div class="pk-grid"><span>😀</span><span>😊</span><span>🙏</span><span>🙌</span><span>👍</span><span>👋</span><span>🎉</span><span>😅</span><span>😍</span><span>🥹</span><span>🤝</span><span>💚</span><span>✅</span><span>📍</span><span>🕕</span><span>🚉</span><span>🎒</span><span>🧳</span><span>🔑</span><span>🐶</span><span>😺</span><span>☕</span><span>🌧️</span><span>🙂</span></div></div><div class="compose"><span class="emo" aria-label="Emoji">☺</span><input class="in" id="reply" placeholder="Write a reply" aria-label="Write a reply"><span class="send" id="sendbtn">↑</span></div>'),
    ("emoji", "Owner 13c · Emoji picker", hdr(backto("thread", "Finder"), "") + '<div class="thread"><div class="bub in2"><b>With me</b> · Darmstadt Hbf, Lost &amp; Found desk</div><div class="bub out">Thank you so much 🙏 I\'ll pick it up at 6 🕕</div></div><div class="sp"></div><div class="compose"><span class="emo on">☺</span><div class="in val">See you there 👋</div><span class="send">↑</span></div>' + '<div class="picker" hidden><div class="in pk-s">🔍 Search emoji</div><div class="pk-cats"><span class="on">😀</span><span>👍</span><span>❤️</span><span>🎒</span><span>🚆</span><span>🐾</span></div><div class="pk-grid"><span>😀</span><span>😊</span><span>🙏</span><span>🙌</span><span>👍</span><span>👋</span><span>🎉</span><span>😅</span><span>😍</span><span>🥹</span><span>🤝</span><span>💚</span><span>✅</span><span>📍</span><span>🕕</span><span>🚉</span><span>🎒</span><span>🧳</span><span>🔑</span><span>🐶</span><span>😺</span><span>☕</span><span>🌧️</span><span>🙂</span></div></div>'.replace(' hidden','')),
    ("anon", "Owner 13b · Anonymous finder", hdr(backto("tags", "My tags"), '<span' + go("report-owner") + '>Report · Block</span>') + '<div class="thread"><div class="bub in2"><b>Left where I found it</b> · Luisenplatz, bench by the fountain</div></div><p class="note info">This finder is anonymous. They see your reply only while their page is open.</p><div class="sp"></div><div class="compose"><span class="emo">☺</span><div class="in">Write a reply</div><span class="send">↑</span></div>'),
    ("inbox", "Owner 15 · Messages", hdr(LOGO, "") + '<h1>Messages</h1><div class="item"' + go("thread") + '><span class="ic">🧳</span><span class="tx"><b>Blue suitcase</b><span>Finder: "I left it with the staff at counter 2."</span></span><span class="unread">1</span></div><div class="item"' + go("anon") + '><span class="ic">🎒</span><span class="tx"><b>Black backpack</b><span>Anonymous finder · Luisenplatz</span></span><span class="xs">2 d</span></div><p class="xs center">Messages are deleted 90 days after a return.</p><div class="sp"></div>' + tabbar("inbox")),
    ("orders", "Owner 16 · Orders", hdr(LOGO, "") + '<h1>Orders</h1><div class="item"><span class="ic">🏷️</span><span class="tx"><b>2 × sticker</b><span>TK-10482 · ordered today</span></span><span class="badge b-r">On the way</span></div><div class="item"><span class="ic">🔑</span><span class="tx"><b>1 × keychain</b><span>TK-10311 · 2 Nov</span></span><span class="badge b-n">Delivered</span></div><div class="two"><div class="btn sec"' + go("order") + '>Order tags</div><div class="btn sec"' + go("gift") + '>🎁 Gift a tag</div></div><div class="sp"></div>' + tabbar("orders")),
    ("account", "Owner 17 · Account", hdr(LOGO, "") + '<h1>Account</h1><div class="acct tight"><span class="av">A</span><span class="tx"><b>Alex M.</b><span>a•••@example.com</span></span></div><div class="grpl"><div class="li"' + go("plan") + '><span>Plan</span><span>Free ›</span></div><div class="li"><span>Contacts and backup contact</span><span>›</span></div><div class="li"' + go("notif-settings") + '><span>Notifications</span><span>Push, email ›</span></div><div class="li"' + go("language") + '><span>Language</span><span>English ›</span></div><div class="li"' + go("privacy") + '><span>Privacy and data</span><span>›</span></div><div class="li"' + go("appearance") + '><span>Appearance</span><span>Match system ›</span></div><div class="li" data-toast="Invite link copied: tagkin.app/i/alex"><span>Invite a friend</span><span>Share ›</span></div><div class="li"><span>Help</span><span>›</span></div></div><div class="btn ghost" data-toast="Signed out"' + go("signin") + '>Sign out</div><div class="sp"></div>' + tabbar("account")),
    ("returned", "Owner 14 · Mark returned", hdr(backto("thread"), '<span class="badge b-r">Return active</span>') + '<h1>Got it back?</h1><p class="m">Locks lift and the tag goes back to Normal. The return closes on its own after 14 days with no messages.</p><div class="in ta">Private thank-you (optional)</div><div class="sp"></div><div class="btn pri"' + go("tags") + ' data-toast="Marked as returned">Mark as returned</div>'),
]

SETUP = [
    ("launch1", "Setup 1 · Welcome", '<div class="sp"></div><div class="hero"><svg width="96" height="96"><use href="#mark"/></svg></div><h1 class="big center">Protect what you value.</h1><p class="m center">Tag your bags, keys, gear and pets. If one ever goes missing, whoever finds it can scan the tag and alert you, privately and in their own language.</p><div class="sp"></div><div class="pager"><i class="on"></i><i></i><i></i></div><div class="btn pri"' + go("launch2") + '>Next</div><div class="btn ghost"' + go("signin") + '>I have an account</div>'),
    ("launch2", "Setup 2 · Private by default", '<div class="sp"></div><div class="hero lockh"><svg width="64" height="64"><use href="#lock"/></svg></div><h1 class="big center">Private by default.</h1><p class="m center">Finders message you through Tagkin. Nobody sees your number or email unless you choose to share it.</p><div class="sp"></div><div class="pager"><i></i><i class="on"></i><i></i></div><div class="btn pri"' + go("launch3") + '>Next</div>'),
    ("launch3", "Setup 3 · Terms", '<div class="sp"></div><h1 class="big">Before you start</h1><p class="m">Tagkin relays messages between owners and finders. We never sell or share your data.</p><label class="check on"><i>✓</i><span>I agree to the <u>Terms of use</u> and have read the <u>Privacy policy</u>.</span></label><label class="check"><i></i><span>Send me product news (optional)</span></label><div class="sp"></div><div class="pager"><i></i><i></i><i class="on"></i></div><div class="btn pri"' + go("signin") + '>Get started</div>'),
    ("perm-notif", "Setup 4 · Notifications", '<div class="sp"></div><div class="hero"><span class="bell">🔔</span></div><h1 class="center">Know the moment it\'s found</h1><p class="m center">We\'ll tell you when someone scans your tag or sends a message. Nothing else.</p><div class="sp"></div><div class="btn pri"' + go("start") + ' data-toast="Notifications on">Turn on notifications</div><div class="btn ghost"' + go("start") + '>Not now</div>'),
    ("start", "Setup 5 · Add a tag", hdr(LOGO, "") + '<h1>Add your first tag</h1><ol class="how"><li><b>1</b><span><strong>Create your tag</strong>Make a QR code and link it to a belonging.</span></li><li><b>2</b><span><strong>Get it printed</strong>Order it from us, or print it yourself, whenever you like.</span></li><li><b>3</b><span><strong>Stick it on</strong>It arrives ready to use, already linked.</span></li></ol><div class="btn pri"' + go("pick") + '>Create a tag</div><div class="sp"></div><p class="xs center">Got a ready-made Tagkin tag from a shop or a friend?</p><span class="link center"' + go("perm-camera") + '>Activate it</span>'),
    ("perm-camera", "Setup 6 · Activate: camera", hdr(backto("start"), "") + '<div class="sp"></div><div class="hero"><span class="bell">📷</span></div><h1 class="center">Activate your tag</h1><p class="m center">Scan the QR on your ready-made tag to link it to your account. The camera is used only to read the QR. No photos are saved.</p><div class="sp"></div><div class="btn pri"' + go("scan") + '>Allow camera</div><div class="btn ghost"' + go("enter-tag") + '>Enter code instead</div>'),
    ("scan", "Setup 7 · Activate: scanning", '<div class="cam"><div class="hdr cam-h"><span class="back"' + go("start") + '>‹ Back</span><span>🔦</span></div><div class="sp"></div><div class="frame"><i></i><i></i><i></i><i></i></div><p class="center cam-t">Point at the QR on your tag</p><div class="sp"></div><div class="btn sec"' + go("found-new") + '>Simulate: tag scanned</div><div class="btn ghost cam-t"' + go("enter-tag") + '>Enter code instead</div></div>'),
    ("enter-tag", "Setup 8 · Activate: enter code", hdr(backto("start"), "") + '<h1>Enter the tag code</h1><p class="m">It\'s printed under the QR, after tagkin.app.</p><div class="in focus">TK-5VJ2-QA7L</div><div class="btn pri"' + go("found-new") + '>Find tag</div><div class="btn ghost"' + go("taken") + '>Try a tag that\'s already linked</div>'),
    ("found-new", "Setup 9 · New tag found", hdr(backto("start"), "") + '<div class="sp"></div><div class="done">✓</div><h1 class="center">New tag found</h1><p class="m center">Sticker · TK-5VJ2-QA7L · ready to set up</p><p class="note info">Next, tell us what it\'s for: an item, luggage or a pet. Once set up, this code belongs to that belonging for good.</p><div class="sp"></div><div class="btn pri act-go"' + go("type") + '>Set up this tag</div>'),
    ("act-live", "Setup 9b · Activated tag is live", hdr(LOGO, "") + '<div class="sp"></div><div class="done">✓</div><h1 class="center">Your tag is live.</h1><p class="m center">TK-5VJ2-QA7L now belongs to <b class="act-name">Black backpack</b>.</p><p class="note info">Stick it somewhere visible. Then test it: scan it with another phone to see what a finder sees.</p><div class="sp"></div><div class="btn pri"' + go("qr") + '>Test my tag</div><div class="btn sec act-again"' + go("perm-camera") + '>Activate another tag</div><div class="btn ghost"' + go("tags") + '>Go to my tags</div>'),
    ("taken", "Setup 10 · Tag already linked", hdr(backto("start"), "") + '<div class="sp"></div><div class="done warnc">!</div><h1 class="center">This tag belongs to someone else</h1><p class="m center">If you found it, you can tell the owner where it is. Your details stay private.</p><div class="sp"></div><div class="btn pri" data-toast="Opens the finder page">Tell the owner I found it</div><div class="btn ghost"' + go("start") + '>Scan a different tag</div>'),
    ("privacy", "Account 1 · Privacy and data", hdr(backto("account", "Account"), "") + '<h1>Privacy and data</h1><div class="grpl"><div class="li" data-toast="We\'ll email you a download link within 24 h"><span>Download my data</span><span>›</span></div><div class="li"><span>Privacy policy</span><span>↗</span></div><div class="li"><span>Terms of use</span><span>↗</span></div><div class="li"><span>Location sharing</span><span>Only when finders choose</span></div></div><p class="xs">Messages are deleted after a set period once a return ends. Retired tags keep no personal data.</p><div class="sp"></div><div class="btn ghost dangert"' + go("delete") + '>Delete account</div>'),
    ("delete", "Account 2 · Delete account", hdr(backto("privacy"), "") + '<h1>Delete your account?</h1><p class="m">This can\'t be undone.</p><div class="grpl"><div class="li"><span>Your tags</span><span>Retired for good</span></div><div class="li"><span>Messages and scans</span><span>Deleted</span></div><div class="li"><span>Contacts and photos</span><span>Deleted</span></div><div class="li"><span>Order invoices</span><span>Kept as the law requires</span></div></div><label class="check on"><i>✓</i><span>I understand my tags will stop working.</span></label><div class="sp"></div><div class="btn lostb"' + go("deleted") + '>Delete account</div><div class="btn sec"' + go("privacy") + '>Keep my account</div>'),
    ("deleted", "Account 3 · Account deleted", '<div class="sp"></div><div class="done">✓</div><h1 class="center">Your account is deleted.</h1><p class="m center">Your tags no longer show any of your details. Thank you for using Tagkin.</p><div class="sp"></div><div class="btn sec"' + go("launch1") + '>Back to start</div>'),
]

STATES = [
    ("e-tags", "State 1 · No tags yet", hdr(LOGO, '<span' + go("start") + '>+ New</span>') + '<div class="sp"></div><div class="hero"><span class="bell"><svg width="52" height="52"><use href="#mark"/></svg></span></div><h1 class="center">No tags yet</h1><p class="m center">Protect what matters to you: bags, keys, gear or your pet. If it ever goes missing, the finder can scan the tag and alert you, privately.</p><div class="btn pri"' + go("start") + '>Add a tag</div><div class="sp"></div>' + tabbar("tags")),
    ("e-inbox", "State 2 · No messages", hdr(LOGO, "") + '<h1>Messages</h1><div class="sp"></div><div class="hero"><span class="bell">💬</span></div><p class="m center">No messages yet. When someone finds one of your items, their message appears here.</p><div class="sp"></div>' + tabbar("inbox")),
    ("e-orders", "State 3 · No orders", hdr(LOGO, "") + '<h1>Orders</h1><div class="sp"></div><div class="hero"><span class="bell">📦</span></div><p class="m center">No orders yet. Printed stickers, keychains and pet tags ship in 3 to 5 days.</p><div class="btn sec"' + go("order") + '>Order a printed tag</div><div class="sp"></div>' + tabbar("orders")),
    ("err-offline", "State 4 · Offline", hdr(LOGO, "") + '<div class="note offl">You\'re offline. Your tags still work for finders. New messages appear when you\'re back online.</div><h1>My tags</h1><div class="item dim"><span class="ic">🎒</span><span class="tx"><b>Black backpack</b><span>TK-7Q4M-9XRA</span></span><span class="badge b-n">Normal</span></div><div class="item dim"><span class="ic">🐾</span><span class="tx"><b>Milo</b><span>TK-M3PF-2KWD</span></span><span class="badge b-l">Lost</span></div><div class="sp"></div>' + tabbar("tags")),
    ("err-pay", "State 5 · Payment failed", hdr(backto("checkout"), "Order") + '<div class="sp"></div><div class="done errc">!</div><h1 class="center">Payment didn\'t go through</h1><p class="m center">Your card was not charged. Check the card details or try another payment method.</p><div class="sp"></div><div class="btn pri"' + go("checkout") + '>Try again</div><div class="btn ghost"' + go("tags") + '>Cancel order</div>'),
    ("err-send", "State 6 · Message not sent", hdr(backto("inbox", "Messages"), '<span' + go("report-owner") + '>Report · Block</span>') + '<div class="thread"><div class="bub in2"><b>With me</b> · Darmstadt Hbf, Lost &amp; Found desk</div><div class="bub out failed">Thank you! I\'ll be there at 6.</div><span class="failt" data-toast="Sent">Not sent · Tap to retry</span></div><div class="sp"></div><div class="compose"><span class="emo">☺</span><div class="in">Write a reply</div><span class="send">↑</span></div>'),
    ("locked", "Manage 1 · Tag during a return", hdr(backto("tags", "My tags"), '<span class="badge b-r">Return active</span>') + '<div class="photo lockedp">🧳<small>🔒 Locked during the return</small></div><h1>Blue suitcase</h1><p class="lockrow">🔒 Name, photo and description are locked until the return ends, so the finder sees what they expect.</p><div><div class="li"' + go("edit-msg") + '><span>Finder message</span><span>Edit ›</span></div><div class="li"' + go("edit-contacts") + '><span>Contacts</span><span>Edit ›</span></div><div class="li"' + go("history") + '><span>Scan history</span><span>4 scans ›</span></div></div><div class="sp"></div><div class="btn pri"' + go("thread") + '>Open conversation</div>'),
    ("edit-msg", "Manage 2 · Edit finder message", hdr(backto("detail"), '<span class="savet" data-toast="Saved"' + go("detail") + '>Save</span>') + '<h1>Finder message</h1><div class="seg"><span>Template</span><span class="on">Write my own</span></div><div class="in ta val">Thanks for finding my backpack! It has my laptop inside. Please hand it to station staff or message me.</div><p class="count">104 / 160</p><p class="xs">You can edit this at any time, even during Lost mode or a return.</p><span class="label2">Finder sees</span><div class="preview"><b>Thanks for finding my backpack! It has my laptop inside…</b><span>Shown in the finder\'s language</span></div>'),
    ("edit-contacts", "Manage 3 · Contacts", hdr(backto("detail"), '<span class="savet" data-toast="Saved"' + go("detail") + '>Save</span>') + '<h1>Contacts</h1><p class="m">Who Tagkin alerts when this tag is scanned. Finders never see these.</p><div class="grpl"><div class="li"><span>You</span><span>Push and email</span></div><div class="li"><span>Phone for SMS alerts</span><span>Add ›</span></div></div><span class="label2">Backup contact</span><div class="item"><span class="ic">👤</span><span class="tx"><b>Ama G.</b><span>Alerted if you don\'t reply</span></span></div><div class="li"><span>Alert backup after</span><span>2 hours ›</span></div><div class="sp"></div>'),
    ("qr", "Manage 6 · QR code and test", hdr(backto("tags", "My tags"), "") + '<h1>Black backpack</h1><div class="bigqr"><div class="qr"></div><small>tagkin.app · TK-7Q4M-9XRA</small></div><div class="testbox"><span><b>Test your tag</b><small>Scan it with another phone to see exactly what a finder sees. For 10 minutes, scans show a Test banner and send no alerts.</small></span><span class="sw"><i></i></span></div><div class="sp"></div><div class="two"><div class="btn sec" data-toast="QR image saved to Photos">Save image</div><div class="btn sec" data-toast="Share sheet opens">Share</div></div>'),
    ("status", "Manage 7 · Status update", hdr(backto("detail"), '<span class="savet" data-toast="Status shown to finders"' + go("detail") + '>Save</span>') + '<h1>Status update</h1><p class="m">A short note finders see on the tag page. Helpful when you travel or think you know where it went missing.</p><div class="chips">' + ''.join(f'<span class="chip{" on" if i == 1 else ""}">{t}</span>' for i, t in enumerate(["On the way to Dubai", "Arrived in Dubai", "At my hotel in Dubai", "Lost it near the gym"])) + '</div><input class="in" id="st-text" value="Arrived in Dubai" aria-label="Status"><div class="li"><span>Show to finders</span><span class="sw on"><i></i></span></div><div class="li"><span>Hide automatically</span><span>After the trip ›</span></div><p class="xs">🔒 City only. Never add dates, times or your home address.</p>'),
    ("history", "Manage 4 · Scan history", hdr(backto("detail"), "") + '<h1>Scan history</h1><p class="m">Black backpack · TK-7Q4M-9XRA</p><div><div class="li"><span>Today 14:02<br><small class="xs">Report sent · with finder</small></span><span>Darmstadt</span></div><div class="li"><span>3 Nov 09:41<br><small class="xs">Viewed, no report</small></span><span>Frankfurt</span></div></div><p class="xs">City only, unless a finder shared the item location. History is deleted with the tag.</p>'),
    ("retire", "Manage 5 · Retire tag", hdr(backto("detail"), "") + '<h1>Retire this tag?</h1><p class="m">Black backpack · TK-7Q4M-9XRA</p><div class="grpl"><div class="li"><span>The code stops working</span><span>For good</span></div><div class="li"><span>It can\'t be reused</span><span>Ever</span></div><div class="li"><span>Messages and scans</span><span>Deleted</span></div></div><p class="note info">Lost the item for good? If this is your free tag, retiring it lets you create a new one. The old code never comes back.</p><div class="sp"></div><div class="btn lostb"' + go("tags") + ' data-toast="Tag retired">Retire tag</div><div class="btn sec"' + go("detail") + '>Keep tag</div>'),
]

EXTRA = [
    ("t-details", "Type 1 · Travel details", hdr(backto("type"), "2 of 5") + '<h1>Trip details</h1><input class="in" value="Blue suitcase" aria-label="Item name"><div class="chips modes"><span class="chip on" data-mode="plane">✈️ Plane</span><span class="chip" data-mode="train">🚆 Train</span><span class="chip" data-mode="bus">🚌 Bus</span><span class="chip" data-mode="ferry">⛴️ Ferry</span><span class="chip" data-mode="taxi">🚕 Taxi or ride</span><span class="chip" data-mode="hotel">🏨 Hotel</span></div><input class="in" id="t-a" placeholder="Airline, e.g. Lufthansa, Ryanair" aria-label="Airline"><input class="in" id="t-b" placeholder="Flight number, e.g. LH 566" aria-label="Flight number"><input class="in" id="t-c" placeholder="Destination airport, e.g. Accra (ACC)" aria-label="Destination"><input class="in" id="t-d" placeholder="Travel dates, e.g. 14 to 20 Nov" aria-label="Travel dates"><p class="xs">🔒 Finders see destination and operator only, never dates.</p><div class="sp"></div><div class="btn pri"' + go("message") + '>Next</div>'),
    ("p-details", "Type 2 · Pet details", hdr(backto("type"), "2 of 5") + '<h1>About your pet</h1><div class="in val">Milo</div><div class="add sm">+ Add a photo of Milo</div><span class="label2">Temperament</span><div class="chips"><span class="chip on">Friendly</span><span class="chip">Shy</span><span class="chip">Nervous with dogs</span><span class="chip">Don\'t chase</span></div><div class="in ta sm val">Care notes: needs daily medication at 8 pm. Allergic to chicken.</div><p class="xs">Care notes stay behind a tap on the finder page.</p><div class="sp"></div><div class="btn pri"' + go("message") + '>Next</div>'),
    ("report-owner", "Safety 1 · Report or block", hdr(backto("thread"), "") + '<h1>Report or block</h1><p class="m">About this finder\'s messages on Blue suitcase.</p><div class="grp">' + opt("Block this finder", True, "🚫", "They can\'t message you about this tag again") + opt("Report a message", False, "⚑", "Abuse, spam or a scam attempt") + '</div><p class="note warn">Never pay a finder before you have your item back. Tagkin will never ask for payment in a message.</p><div class="sp"></div><div class="btn lostb"' + go("report-done") + '>Block finder</div><div class="btn sec"' + go("thread") + '>Cancel</div>'),
    ("report-done", "Safety 2 · Blocked", hdr() + '<div class="sp"></div><div class="done">✓</div><h1 class="center">Finder blocked</h1><p class="m center">They can no longer message you about this tag. Our team reviews every report within 24 hours.</p><div class="sp"></div><div class="btn pri"' + go("inbox") + '>Back to messages</div>'),
    ("plan", "Account 4 · Plan", hdr(backto("account", "Account"), "") + '<h1>Your plan</h1><div class="plan"><b>Free</b><span>No subscription needed</span><ul><li>1 free tag, digital or self-printed</li><li>Every tag you buy, free to use for life</li><li>Relayed messages and translation</li><li>Lost mode and scan alerts</li></ul></div><div class="plan prem"><b>Premium <em>Later</em></b><ul><li>Unlimited tags</li><li>SMS alerts and SMS replies</li><li>Family sharing and extra contacts</li></ul></div><div class="sp"></div><div class="btn pri" data-toast="We\'ll email you when Premium launches">Notify me</div>'),
    ("notif-settings", "Account 5 · Notifications", hdr(backto("account", "Account"), "") + '<h1>Notifications</h1><div class="grpl"><div class="li"><span>Someone scans my tag</span><span class="sw on"><i></i></span></div><div class="li"><span>New message</span><span class="sw on"><i></i></span></div><div class="li"><span>Email copy of messages</span><span class="sw on"><i></i></span></div><div class="li"><span>Order updates</span><span class="sw on"><i></i></span></div><div class="li"><span>Product news</span><span class="sw"><i></i></span></div></div><p class="xs">Alerts for a tag in Lost mode can\'t be turned off while it\'s lost.</p>'),
    ("language", "Account 6 · Language", hdr(backto("account", "Account"), "") + '<h1>Language</h1><div class="in">🔍 Search languages</div><div class="grpl"><div class="li on"><span>English</span><span>✓</span></div><div class="li"><span>Deutsch</span><span></span></div><div class="li"><span>Français</span><span></span></div><div class="li"><span>Twi</span><span></span></div><div class="li"><span>Español</span><span></span></div></div><p class="xs">Messages from finders are translated into this language, with the original one tap away.</p>'),
    ("appearance", "Account 7 · Appearance", hdr(backto("account", "Account"), "") + '<h1>Appearance</h1><p class="m">Choose how Tagkin looks.</p><div class="themes"><div class="th" data-theme-set="light"><span class="thp light"><svg width="28" height="28"><use href="#i-sun"/></svg></span><b>Light</b></div><div class="th" data-theme-set="dark"><span class="thp dark"><svg width="28" height="28"><use href="#i-moon"/></svg></span><b>Dark</b></div><div class="th on" data-theme-set="system"><span class="thp auto"><svg width="28" height="28"><use href="#i-auto"/></svg></span><b>Match system</b></div></div><p class="xs">Match system follows your phone\'s day and night setting.</p>'),
    ("splash", "Brand · Splash and app icon", '<div class="splash"><div class="sp"></div><svg width="120" height="120"><use href="#mark"/></svg><b>tagkin</b><div class="sp"></div><div class="icons"><span class="appicon"><svg width="44" height="44"><use href="#mark"/></svg></span><span class="appicon dk"><svg width="44" height="44"><use href="#mark"/></svg></span></div><small>App icon, light and dark</small></div>'),
]

GIFT = [
    ("gift", "Gift 1 · Gift a tag", hdr(backto("orders", "Orders"), "1 of 3") + '<div class="seg"><span' + go("order") + '>For me</span><span class="on">Gift a tag</span></div><h1>Gift a tag</h1><p class="m">They activate it in the app and make it theirs: name, photo and message.</p><div class="grp prod">' + opt("Sticker 3-pack", True, "🏷️", "Waterproof vinyl · €12.90") + opt("Keychain", False, "🔑", "Acrylic, 4 cm · €9.90") + opt("Pet tag", False, "🐾", "Metal, engraved · €12.90") + '</div><div class="in ta sm val">Happy birthday! For your new camera bag 📷 – Alex</div><div class="sp"></div><div class="btn pri"' + go("gift-delivery") + '>Continue to delivery</div>'),
    ("gift-delivery", "Gift 2 · Who is it for?", hdr(backto("gift"), "2 of 3") + '<h1>Who is it for?</h1><div class="seg"><span class="on">Send to them</span><span>Send to me</span></div><input class="in" value="Kofi Boateng" aria-label="Recipient name"><input class="in" value="Am Markt 5" aria-label="Street and number"><div class="two"><input class="in" value="60311" aria-label="Postcode"><input class="in" value="Frankfurt" aria-label="City"></div><div class="in val sel">Germany <span>▾</span></div><label class="check on"><i>✓</i><span>Hide prices on the packing slip</span></label><p class="xs">The address is shared only with the print partner, to deliver this gift.</p><div class="sp"></div><div class="btn pri"' + go("gift-review") + '>Continue to payment</div>'),
    ("gift-review", "Gift 3 · Review and pay", hdr(backto("gift-delivery"), "3 of 3") + '<h1>Review your gift</h1><div><div class="li"><span>Sticker 3-pack</span><span>€12.90</span></div><div class="li"><span>Shipping to Germany</span><span>€2.50</span></div><div class="li total"><span>Total</span><span>€15.40</span></div></div><div class="addr"' + go("gift-delivery") + '><span><small>Gift for</small><b>Kofi Boateng</b><span class="a-line">Am Markt 5, 60311 Frankfurt</span></span><span class="link">Change</span></div><div class="preview"><b>“Happy birthday! For your new camera bag…”</b><span>Printed on a card in the box · prices hidden</span></div><div class="sp"></div><div class="btn pri"' + go("gift-sent") + '>Pay €15.40</div>'),
    ("gift-sent", "Gift 4 · Gift on its way", hdr() + '<div class="sp"></div><div class="done">🎁</div><h1 class="center">Your gift is on its way.</h1><p class="m center">It reaches Kofi in 3 to 5 working days. The tags stay unclaimed until Kofi activates them, so only Kofi can link them.</p><p class="xs center">Order TK-10517 · tracking comes to you by email</p><div class="sp"></div><div class="btn pri"' + go("orders") + '>Done</div>'),
]


def flow(title, desc, screens):
    figs = "".join(screen(t[-2], t[-1]) for t in screens)
    return f'<section class="flow"><h2>{title}</h2><p>{desc}</p><div class="row">{figs}</div></section>'


SHOW_NOTES = True
exec((Path(__file__).parent / "handoff_parts.py").read_text())
exec((Path(__file__).parent / "handoff_parts2.py").read_text())

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
<style>{CSS}{HANDOFF_CSS}{STORE_CSS}{PARTS2_CSS}</style>
</head>
<body>
{SVG}
<div class="page">
<header class="top"><div class="brand"><svg width="36" height="36"><use href="#mark"/></svg><b>tagkin</b></div><button class="toggle" type="button" id="theme"><svg width="16" height="16" style="vertical-align:-3px"><use href="#i-moon"/></svg> <span>Switch to dark</span></button></header>
{COVER}
{FLOWMAP}
{flow("Finder flow", "No app, no sign-up. Tested with 5 people, no concerns.", FINDER)}
{flow("First launch, activation and account", "Welcome, terms, permission explainers, linking a printed tag, data and account deletion.", SETUP)}
{flow("Owner registration and ordering", "Email code sign-in, five steps to a live tag, then order it printed.", OWNER)}
{flow("Gift a tag", "Order printed tags for someone else. They activate and personalise them.", GIFT)}
{flow("Lost mode and messages", "Urgent finder page, scan alerts, relayed messages.", LOST)}
{flow("Travel, Pet, safety and settings", "Tag-type details, report and block, plan, notifications, language, splash and app icon.", EXTRA)}
{flow("States and tag management", "Empty and error states, locked fields during a return, editing, history and retiring.", STATES)}
{STATES_UI}
{RECOVER}
{EMAILS}
{DESK_FINDER}
{WEB}
{STORE}
{PRINT}
{EXPORTS}
{ICONS}
{A11Y}
{MKT}
</div>
<script>
const b=document.getElementById('theme'),r=document.documentElement;
b.onclick=()=>{{const d=r.getAttribute('data-theme')!=='dark';r.setAttribute('data-theme',d?'dark':'light');b.querySelector('span').textContent=d?'Switch to light':'Switch to dark';b.querySelector('use').setAttribute('href',d?'#i-sun':'#i-moon');}};
</script>
</body>
</html>
"""

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(html)
build_showcase()
print(f"wrote {OUT.relative_to(ROOT)}: {len(FINDER) + len(SETUP) + len(OWNER) + len(GIFT) + len(LOST) + len(STATES) + len(EXTRA)} screens")

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
    if(o.closest('#type')){const i=[...o.parentElement.children].indexOf(o);$('#type .btn.pri').dataset.go=['details','t-details','p-details'][i];setType(i);}
    const price=o.closest('#order')&&o.querySelector('small').textContent.match(/€([\\d.]+)/);if(price)updateTotal(parseFloat(price[1]));}
  const sw=e.target.closest('.sw');if(sw){sw.classList.toggle('on');}
  const ck=e.target.closest('.check');if(ck){ck.classList.toggle('on');}
  const c=e.target.closest('.chip');if(c){c.parentElement.querySelectorAll('.chip').forEach(x=>x.classList.toggle('on',x===c));}
  const g=e.target.closest('.seg span');if(g){g.parentElement.querySelectorAll('span').forEach(x=>x.classList.toggle('on',x===g));}
  const st=e.target.closest('.step b');if(st){const q=st.parentElement.querySelector('i');let n=+q.textContent+(st.textContent==='+'?1:-1);q.textContent=Math.max(1,Math.min(20,n));updateTotal();}
  const t=e.target.closest('[data-title]');if(t){$('#scans .ttl').textContent=t.dataset.title;}
  const m=e.target.closest('[data-toast]');if(m)toast(m.dataset.toast);
  const l=e.target.closest('[data-go]');if(l)show(l.dataset.go);
});
let unit=4.90;
function updateTotal(u){if(u)unit=u;const q=+$('#order .step i').textContent;const name=$('#order .prod .opt.on span:last-child').firstChild.textContent;
  const sub=(unit*q).toFixed(2),tot=(unit*q+2.5-2).toFixed(2);
  const rows=$('#checkout').querySelectorAll('.li');rows[0].innerHTML='<span>'+name+' × '+q+'</span><span>€'+sub+'</span>';rows[3].innerHTML='<span>Total</span><span>€'+tot+'</span>';$('#checkout .paybtn').textContent='Pay €'+tot;
  $('#ordered .xs').textContent='Order TK-10482 · '+q+' × '+name.toLowerCase();}
all('[data-start]').forEach(b=>b.onclick=()=>show(b.dataset.start));
const MODES={plane:['Airline, e.g. Lufthansa, Ryanair','Flight number, e.g. LH 566','Destination airport, e.g. Accra (ACC)','Travel dates, e.g. 14 to 20 Nov'],
 train:['Rail company, e.g. Deutsche Bahn, Flixtrain, ÖBB','Train number, e.g. ICE 571','Destination station, e.g. Berlin Hbf','Travel dates'],
 bus:['Bus company, e.g. FlixBus, BlaBlaCar Bus, city bus','Line or route, e.g. N1 or Frankfurt to Paris','Destination stop or city','Travel dates'],
 ferry:['Ferry company, e.g. Stena Line, DFDS','Route, e.g. Kiel to Gothenburg','Destination port','Travel dates'],
 taxi:['Service, e.g. taxi, Uber, Bolt, FREENOW','Driver or car (optional)','Drop-off city','Date of the ride'],
 hotel:['Hotel name','City, e.g. Accra','Room number (optional, never shown to finders)','Check-in and check-out dates']};
const TYPE_STYLE={0:['Sticker','an item','Found me? Scan to return'],1:['Luggage label','travel','I’m travelling. Scan to return'],2:['Pet tag','a pet','Hi! Scan to reach my family']};
function setType(i){const [st,lab,line]=TYPE_STYLE[i];
  $('#design .styles').querySelectorAll('.chip').forEach(c=>c.classList.toggle('on',c.textContent===st));
  $('#design .pick').innerHTML='Suggested for '+lab+': <b>'+st+'</b>. You can choose another.';$('#design .tagline').textContent=line;
  $('#order .ordfor').textContent=st+' style · TK-7Q4M-9XRA';
  const ps=[...$('#order .prod').children];ps.forEach(o=>o.classList.toggle('on',o.querySelector('span:last-child').firstChild.textContent===st));
  const pr=ps.find(o=>o.classList.contains('on')).querySelector('small').textContent.match(/€([\d.]+)/);updateTotal(parseFloat(pr[1]));}
document.addEventListener('click',e=>{
  const md=e.target.closest('.modes .chip');if(md){const f=MODES[md.dataset.mode];['t-a','t-b','t-c','t-d'].forEach((id,i)=>{const x=document.getElementById(id);x.value='';x.placeholder=f[i];x.setAttribute('aria-label',f[i].split(',')[0]);});}
  const th=e.target.closest('[data-theme-set]');if(th){th.parentElement.querySelectorAll('.th').forEach(x=>x.classList.toggle('on',x===th));const v=th.dataset.themeSet;if(v==='system')r.removeAttribute('data-theme');else r.setAttribute('data-theme',v);$('#account [data-go=appearance] span:last-child').textContent=({light:'Light',dark:'Dark',system:'Match system'})[v]+' ›';}
  const em=e.target.closest('#thread .emo');if(em){const pk=$('#thread .picker');pk.hidden=!pk.hidden;em.classList.toggle('on',!pk.hidden);}
  const ge=e.target.closest('#thread .pk-grid span');if(ge){const i=$('#reply');i.value+=ge.textContent;}
  if(e.target.closest('#sendbtn')){const i=$('#reply');if(i.value.trim()){const b=document.createElement('div');b.className='bub out';b.textContent=i.value;$('#thread .thread').appendChild(b);i.value='';$('#thread .picker').hidden=true;$('#thread .emo').classList.remove('on');}}
  if(e.target.closest('#delivery .btn.pri')){$('#checkout .a-name').textContent=$('#d-name').value;$('#checkout .a-line').textContent=$('#d-street').value+', '+$('#d-zip').value+' '+$('#d-city').value+', Germany';}
});
const r=document.documentElement;
let picked=null;
function applyStyle(st){if(!st)return;
  $('#design .styles').querySelectorAll('.chip').forEach(c=>c.classList.toggle('on',c.textContent===st));
  $('#design .pick').innerHTML='Your pick: <b>'+st+'</b>. You can choose another.';
  all('.lp-style').forEach(x=>x.textContent=st);}
document.addEventListener('click',e=>{
  const g=e.target.closest('.gcard');if(g){all('.gcard').forEach(x=>x.classList.toggle('on',x===g));picked=g.dataset.style;const i=+g.dataset.type;
    const opts=$('#type .grp').children;[...opts].forEach((o,k)=>o.classList.toggle('on',k===i));$('#type .btn.pri').dataset.go=['details','t-details','p-details'][i];setType(i);applyStyle(picked);}
  const dc=e.target.closest('#design .styles .chip');if(dc){all('.lp-style').forEach(x=>x.textContent=dc.textContent);}
},true);
document.addEventListener('input',e=>{
  if(e.target.id==='it-name')all('.lp-name').forEach(x=>x.textContent=e.target.value||'Your item');
  if(e.target.id==='it-msg'){all('.lp-msg').forEach(x=>x.textContent=e.target.value||'Your message');$('#it-count').textContent=e.target.value.length+' / 160';}
});
let activating=false;
document.addEventListener('click',e=>{
  if(e.target.closest('.act-go')){activating=true;}
  if(e.target.closest('#start .btn.pri')){activating=false;}
  if(e.target.closest('.act-go')||e.target.closest('#start .btn.pri')){const act=!!e.target.closest('.act-go');[['#type',1],['#details',2],['#t-details',2],['#p-details',2],['#message',3]].forEach(([id,n])=>{const sp=document.querySelector(id+' .hdr>span:last-child');if(sp)sp.textContent=n+(act?' of 3':' of 5');});}
  const n=e.target.closest('#message .btn.pri');if(n){n.dataset.go=activating?'act-live':'design';}
},true);
updateTotal();show('launch1');
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
<button type="button" data-start="launch1">First launch</button>
<button type="button" data-start="start">Add a tag</button>
<button type="button" data-start="tags">My tags</button>
<button type="button" data-start="account">Account</button>
<button type="button" data-start="e-tags">Empty account</button>
<button type="button" data-start="err-offline">Offline</button>
<button type="button" data-start="order">Order a tag</button>
<button type="button" data-start="gift">Gift a tag</button>
</div>
<main class="stage">{"".join(proto_screen(t[0], t[2]) for t in SETUP + OWNER + GIFT + LOST + STATES + EXTRA)}</main>
<div class="toast" role="status" aria-live="polite"></div>
<script>{PROTO_JS}</script>
</body>
</html>
"""
PROTO_OUT.write_text(proto)
print(f"wrote {PROTO_OUT.relative_to(ROOT)}: {len(SETUP) + len(OWNER) + len(GIFT) + len(LOST) + len(STATES) + len(EXTRA)} screens")


# ---------- Clickable finder prototype (web, no app) ----------
FINDER_OUT = ROOT / "docs/design/finder-prototype.html"
FP = PRIV
F_SCREENS = [
    ("f-code", hdr() + '<h1>Found something with a Tagkin tag?</h1><p class="m">Type the code printed under the QR.</p><input class="in" id="f-codein" placeholder="TK-7Q4M-9XRA" autocomplete="off" aria-label="Tag code"><p class="errt" id="f-codeerr" hidden>No tag with that code. Check the letters and numbers and try again.</p><div class="btn pri" id="f-codego">Find tag</div><p class="xs">Try TK-7Q4M-9XRA, TK-K2WB-6YHD (retired) or TK-P5NT-3CVG (not set up yet).</p><div class="sp"></div>' + FP),
    ("f-msg", hdr() + '<div id="f-banner"></div><div class="photo" id="f-photo">🎒<small>Photo updated 3 days ago</small></div><h1 id="f-title">Found me? Thank you! Tap below to tell my owner where I am.</h1><span class="link" id="f-orig">Translated from German · Show original</span><div id="f-extra"></div><div class="sp"></div><div class="btn pri"' + go("f-where") + ' id="f-found">I found it</div>' + FP),
    ("f-where", hdr(backto("f-msg"), steps(1)) + '<h1>Where is it now?</h1><div class="grp" id="f-whereopts">' + opt("With me") + opt("Handed to staff") + opt("Left where I found it") + '</div><div class="sp"></div><div class="btn pri off" id="f-wherenext">Next</div>'),
    ("f-place", hdr(backto("f-where"), steps(2)) + '<h1>Where exactly?</h1><input class="in" id="f-placein" placeholder="Input location here" autocomplete="off" aria-label="Location"><div id="f-sugs"></div><div class="btn sec" id="f-loc">📍 Share item location</div><p class="xs" id="f-locnote">Only the city is shown unless you share the item location.</p><div class="sp"></div><div class="btn pri off" id="f-placenext">Next</div>'),
    ("f-note", hdr(backto("f-place"), steps(3)) + '<h1>Anything else?</h1><textarea class="in ta" id="f-notein" placeholder="Optional note, e.g. name of who you are leaving the item with, exact landmark" aria-label="Note"></textarea><p class="xs">Only add your number or email if you want the owner to contact you directly.</p><label class="check" id="f-share" hidden><i>✓</i><span>This will share your contact with the owner. Continue?</span></label><div class="sp"></div><div class="btn pri" id="f-notenext">Next</div><div class="btn ghost"' + go("f-reply") + '>Skip</div>'),
    ("f-reply", hdr(backto("f-note"), steps(4)) + '<h1>Want a reply?</h1><div class="seg" id="f-ch"><span class="on" data-ch="email">Email</span><span data-ch="phone">Phone</span></div><input class="in" id="f-mail" type="email" placeholder="Email (kept hidden)" aria-label="Email or phone"><p class="xs">The owner never sees it. Replies are passed on by Tagkin.</p><p class="note info">Without an email or phone number, keep this page open to receive replies.</p><div class="sp"></div><div class="btn pri" id="f-send">Send to owner</div><div class="btn sec" id="f-anon">Send anonymously</div>'),
    ("f-thanks", hdr() + '<div class="sp"></div><div class="done">✓</div><h1 class="big center">Thank you.</h1><p class="m center" id="f-thanksub">The owner has been told where it is.</p><div class="thread"><div class="bub in2" id="f-replybox"><span class="dots"><i></i><i></i><i></i> Waiting for the owner\'s reply</span></div></div><div class="sp"></div><div class="invite"><b>Protect your own things</b><span>Your first printed tag is €2 off.</span></div><span class="link center"' + go("f-report") + '>Report abuse</span>'),
    ("f-report", hdr(backto("f-msg"), "") + '<h1>Report this tag</h1><p class="m">Tell us what\'s wrong. Your report is private.</p><div class="grp">' + opt("The message is abusive or spam") + opt("It looks fake or misleading") + opt("Something else") + '</div><p class="note warn">If someone is in danger, call 112 now.</p><div class="sp"></div><div class="btn pri" data-toast="Report sent. Thank you."' + go("f-msg") + '>Send report</div>'),
    ("f-retired", hdr() + '<div class="sp"></div><h1 class="center">This tag is no longer active.</h1><p class="m center">Please hand the item to staff or a lost-and-found desk.</p><div class="sp"></div><div class="btn sec"' + go("f-code") + '>Enter another code</div>'),
    ("f-new", hdr() + '<div class="sp"></div><div class="hero"><span class="bell"><svg width="52" height="52"><use href="#mark"/></svg></span></div><h1 class="center">This tag isn\'t set up yet.</h1><p class="m center">If you found it on something, please hand it to staff or a lost-and-found desk.</p><div class="sp"></div><p class="xs center">Is this your tag?</p><div class="btn pri" data-toast="Opens the Tagkin app">Activate it in the Tagkin app</div>'),
]
F_JS = """
const $=s=>document.querySelector(s),all=s=>document.querySelectorAll(s);
function show(id){all('.stage .scr').forEach(x=>x.classList.toggle('on',x.id===id));window.scrollTo(0,0);}
let tt;function toast(t){const e=$('.toast');e.textContent=t;e.classList.add('show');clearTimeout(tt);tt=setTimeout(()=>e.classList.remove('show'),1800);}
const V={
 item:{photo:'🎒<small>Photo updated 3 days ago</small>',title:'Found me? Thank you! Tap below to tell my owner where I am.',orig:'Gefunden? Danke! Tippe unten, um meinem Besitzer zu sagen, wo ich bin.',banner:'',extra:'',btn:'I found it'},
 lost:{photo:'🎒',title:'Black backpack',orig:'',banner:'<div class="urgent"><i>!</i>This item is missing</div>',extra:'<p class="m">The owner is looking for it. Please tell them where it is.</p>',btn:'I found it'},
 travel:{photo:'🧳',title:'Please hand me to airline or hotel staff, or message my owner.',orig:'Bitte gib mich dem Personal der Airline oder des Hotels oder schreib meinem Besitzer.',banner:'<div class="trip"><span>✈️</span><span><b>I’m travelling to Accra</b><small>With Lufthansa · from Frankfurt</small></span></div><p class="stat">✓ Owner update: arrived in Accra</p>',extra:'',btn:'I found it'},
 pet:{photo:'🐕<small>Photo updated 1 week ago</small>',title:'Hi, I’m Milo. I’m friendly. Please message my owner. I may be scared.',orig:'Hallo, ich bin Milo. Ich bin freundlich. Bitte schreib meiner Familie. Ich habe vielleicht Angst.',banner:'',extra:'<div class="chips"><span class="chip">Friendly</span><span class="chip">Shy with dogs</span></div><div class="li" id="f-care"><span>Care notes</span><span>Show ›</span></div>',btn:'I found Milo'},
 test:{photo:'🎒<small>Photo updated 3 days ago</small>',title:'Found me? Thank you! Tap below to tell my owner where I am.',orig:'',banner:'<div class="testban">Test scan · The owner is testing this tag. Nothing you send here reaches anyone.</div>',extra:'',btn:'I found it'}};
let cur='item',orig=false,shared=false,ch='email',timer;
function reset(){all('#f-whereopts .opt').forEach(o=>o.classList.remove('on'));$('#f-wherenext').classList.add('off');
 $('#f-placein').value='';$('#f-sugs').innerHTML='';shared=false;$('#f-loc').textContent='📍 Share item location';$('#f-locnote').textContent='Only the city is shown unless you share the item location.';$('#f-placenext').classList.add('off');
 $('#f-notein').value='';$('#f-share').hidden=true;$('#f-share').classList.remove('on');$('#f-notenext').classList.remove('off');
 $('#f-mail').value='';setCh('email');$('#f-codein').value='';$('#f-codeerr').hidden=true;}
function scan(v){cur=v;orig=false;reset();const d=V[v];$('#f-photo').innerHTML=d.photo;$('#f-title').textContent=d.title;$('#f-banner').innerHTML=d.banner;$('#f-extra').innerHTML=d.extra;$('#f-found').textContent=d.btn;
 $('#f-orig').hidden=!d.orig;$('#f-orig').textContent='Translated from German · Show original';show('f-msg');}
function setCh(c){ch=c;all('#f-ch span').forEach(x=>x.classList.toggle('on',x.dataset.ch===c));const i=$('#f-mail');i.value='';i.type=c==='email'?'email':'tel';i.placeholder=c==='email'?'Email (kept hidden)':'Phone number (kept hidden)';}
const PLACES=['Darmstadt Hbf, Lost & Found desk','Darmstadt Hbf, Platform 4','Darmstadt Hbf, bus stop A','Luisenplatz, Darmstadt','Luisencenter, Darmstadt','Herrngarten, Darmstadt','Frankfurt (Main) Hbf, Lost & Found','Frankfurt Airport, Terminal 1'];
const placeOk=()=>$('#f-placenext').classList.toggle('off',!($('#f-placein').value.trim()||shared));
$('#f-placein').addEventListener('input',()=>{const q=$('#f-placein').value.trim().toLowerCase(),b=$('#f-sugs');b.innerHTML='';
 if(q.length>=2)PLACES.filter(p=>p.toLowerCase().includes(q)).slice(0,5).forEach(p=>{const d=document.createElement('div');d.className='sug';d.textContent='📍 '+p;d.onclick=()=>{$('#f-placein').value=p;b.innerHTML='';placeOk();};b.appendChild(d);});placeOk();});
const contactRe=/(\\+?\\d[\\d\\s\\-()]{6,}\\d)|([^\\s@]+@[^\\s@]+\\.[^\\s@]+)/;
$('#f-notein').addEventListener('input',()=>{const hit=contactRe.test($('#f-notein').value);$('#f-share').hidden=!hit;if(!hit)$('#f-share').classList.remove('on');$('#f-notenext').classList.toggle('off',hit&&!$('#f-share').classList.contains('on'));});
function finish(anon){show('f-thanks');clearTimeout(timer);
 $('#f-thanksub').textContent=cur==='test'?'Test scan: nothing was sent.':anon?'The owner has been told where it is. Keep this page open to see their reply.':(ch==='email'?'The owner has been told where it is. Their reply will come to your email.':'The owner has been told where it is. Their reply will come by text message.');
 $('#f-replybox').innerHTML='<span class="dots"><i></i><i></i><i></i> Waiting for the owner\\'s reply</span>';
 if(cur!=='test')timer=setTimeout(()=>{$('#f-replybox').innerHTML='<b>Owner</b><br>Thank you so much! I\\'ll pick it up tonight.';},3000);else $('#f-replybox').textContent='No reply in a test.';}
document.addEventListener('click',e=>{
 const st=e.target.closest('[data-scan]');if(st){scan(st.dataset.scan);return;}
 if(e.target.closest('[data-start=f-code]')){reset();show('f-code');return;}
 if(e.target.closest('#f-codego')){const v=$('#f-codein').value.trim().toUpperCase().replace(/\\s/g,'');
   if(v==='TK-7Q4M-9XRA'||v==='TK7Q4M9XRA')scan('item');else if(v==='TK-K2WB-6YHD'||v==='TKK2WB6YHD')show('f-retired');else if(v==='TK-P5NT-3CVG'||v==='TKP5NT3CVG')show('f-new');else $('#f-codeerr').hidden=false;}
 if(e.target.closest('#f-orig')){const d=V[cur];orig=!orig;$('#f-title').textContent=orig?d.orig:d.title;$('#f-orig').textContent=orig?'Original in German · Show translation':'Translated from German · Show original';}
 if(e.target.closest('#f-care')){$('#f-care').outerHTML='<p class="note info">Needs daily medication at 8 pm. Allergic to chicken.</p>';}
 const o=e.target.closest('.grp .opt');if(o){o.parentElement.querySelectorAll('.opt').forEach(x=>x.classList.toggle('on',x===o));if(o.closest('#f-whereopts'))$('#f-wherenext').classList.remove('off');}
 if(e.target.closest('#f-wherenext')&&!$('#f-wherenext').classList.contains('off'))show('f-place');
 if(e.target.closest('#f-loc')){shared=true;$('#f-loc').textContent='✓ Item location shared';$('#f-locnote').textContent='The owner will see the exact spot where the item is.';placeOk();}
 if(e.target.closest('#f-placenext')&&!$('#f-placenext').classList.contains('off'))show('f-note');
 const ck=e.target.closest('#f-share');if(ck){ck.classList.toggle('on');$('#f-notenext').classList.toggle('off',!ck.classList.contains('on'));}
 if(e.target.closest('#f-notenext')&&!$('#f-notenext').classList.contains('off'))show('f-reply');
 const c=e.target.closest('#f-ch span');if(c)setCh(c.dataset.ch);
 if(e.target.closest('#f-send')){const v=$('#f-mail').value.trim();const ok=ch==='email'?/^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/.test(v):/^\\+?[\\d\\s\\-()]{7,}$/.test(v);if(v&&!ok){$('#f-mail').focus();toast(ch==='email'?'Check the email address':'Check the phone number');return;}finish(!v);}
 if(e.target.closest('#f-anon'))finish(true);
 const m=e.target.closest('[data-toast]');if(m)toast(m.dataset.toast);
 const l=e.target.closest('[data-go]');if(l)show(l.dataset.go);
});
const r=document.documentElement;
scan('item');
"""
finder_proto = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Tagkin finder prototype</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700&family=Inter:wght@400;500;600;700&display=swap">
<style id="tokens">
/* Generated from docs/brand/tokens.css by build_screens.py. Do not edit here. */
{TOKENS}</style>
<style>{CSS}{PROTO_CSS}
.off{{opacity:.4;pointer-events:auto}}
textarea.in{{font:400 16px var(--tk-font-body);color:var(--tk-ink);border:0;width:100%;outline:none;resize:vertical;padding:14px 16px}}
textarea.in:focus{{background:var(--tk-surface);box-shadow:inset 0 0 0 2px var(--tk-brand)}}
.check[hidden],.errt[hidden],.link[hidden]{{display:none}}
.sug{{cursor:pointer}}
</style>
</head>
<body>
{SVG}
<div class="ctl" aria-label="Prototype controls"><span>Prototype:</span>
<button type="button" data-scan="item">Scan QR</button>
<button type="button" data-scan="lost">Lost mode</button>
<button type="button" data-scan="travel">Travel</button>
<button type="button" data-scan="pet">Pet</button>
<button type="button" data-start="f-code">Typed tagkin.app</button>
<button type="button" data-scan="test">Owner test scan</button>
</div>
<main class="stage">{"".join(proto_screen(k, b + LEGAL) for k, b in F_SCREENS)}</main>
<div class="toast" role="status" aria-live="polite"></div>
<script>{F_JS}</script>
</body>
</html>
"""
FINDER_OUT.write_text(finder_proto)
print(f"wrote {FINDER_OUT.relative_to(ROOT)}: {len(F_SCREENS)} screens")
