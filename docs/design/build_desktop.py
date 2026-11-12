"""Desktop web prototype: owner web (tagkin.app/my-tags) and finder page at desktop width.
Run: python3 docs/design/build_desktop.py -> docs/design/desktop-prototype.html"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from proto_v3 import SAMPLES_JS
from desktop_v6 import DCSS6, DJS6

ROOT = Path(__file__).resolve().parents[2]
TOKENS = (ROOT / "docs/brand/tokens.css").read_text()
OUT = ROOT / "docs/design/desktop-prototype.html"
MARK = '<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs><mask id="mk" maskUnits="userSpaceOnUse" x="0" y="0" width="64" height="64"><rect width="64" height="64" fill="#fff"/><circle cx="22" cy="32" r="5" fill="#000"/><path d="M31 14 h5 v20 l8 -8 h7 l-9 9 l10 13 h-7 l-7 -9 l-2 2 v7 h-5 Z" fill="#000"/></mask><symbol id="mark" viewBox="0 0 64 64"><g mask="url(#mk)"><path fill="currentColor" stroke="currentColor" stroke-width="4" stroke-linejoin="round" d="M8 23 L23 9 H56 V55 H23 L8 41 Z"/></g></symbol></defs></svg>'

CSS = r"""
*{box-sizing:border-box}html,body{margin:0}
body{background:var(--tk-bg);color:var(--tk-ink);font:15px/1.5 var(--tk-font-body)}
button,input,textarea{font:inherit;color:inherit}
.top{position:sticky;top:0;z-index:5;display:flex;align-items:center;gap:16px;padding:12px 24px;background:var(--tk-surface);border-bottom:1px solid var(--tk-line)}
.logo{display:flex;align-items:center;gap:8px;font:700 20px var(--tk-font-brand);letter-spacing:-.02em}
.seg{display:inline-flex;background:var(--tk-sunken);border-radius:99px;padding:4px;gap:4px}
.seg button{border:0;background:none;padding:8px 16px;border-radius:99px;cursor:pointer;font-weight:500;color:var(--tk-ink-2)}
.seg button.on{background:var(--tk-surface);color:var(--tk-ink);font-weight:600;box-shadow:var(--tk-shadow)}
.sp{flex:1}.muted{color:var(--tk-ink-2)}.xs{font-size:12px;color:var(--tk-ink-2);margin:0}.m{color:var(--tk-ink-2);margin:0}
h1{font:650 28px/1.15 var(--tk-font-display);letter-spacing:-.025em;margin:0}h2{font:650 20px/1.2 var(--tk-font-display);letter-spacing:-.02em;margin:0}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;min-height:44px;padding:0 20px;border-radius:99px;border:1px solid transparent;font-weight:600;cursor:pointer;background:none}
.pri{background:var(--tk-brand);color:var(--tk-on-brand)}.sec{background:var(--tk-surface);border-color:var(--tk-line)}.lostb{background:var(--tk-lost);color:var(--tk-on-lost)}.ghost{color:var(--tk-ink-2)}
.btn:focus-visible,.card:focus-visible{outline:3px solid var(--tk-brand);outline-offset:2px}
.btn.off{opacity:.45;pointer-events:none}
.in{width:100%;min-height:46px;border:0;border-radius:14px;background:var(--tk-sunken);padding:0 14px;outline:none}
textarea.in{padding:12px 14px;min-height:90px;resize:vertical}
.in:focus{background:var(--tk-surface);box-shadow:inset 0 0 0 2px var(--tk-brand)}
.badge{display:inline-flex;align-items:center;gap:6px;font:600 12px/1 var(--tk-font-body);padding:6px 10px;border-radius:99px;white-space:nowrap}
.badge::before{content:"";width:6px;height:6px;border-radius:50%;background:currentColor}
.b-n{background:var(--tk-sunken);color:var(--tk-ink-2)}.b-l{background:var(--tk-lost);color:var(--tk-on-lost)}.b-r{background:var(--tk-brand-soft);color:var(--tk-brand-text)}
.view{display:none}.view.on{display:block}
.wrap{max-width:1200px;margin:0 auto;padding:28px 24px 64px}
.signin{max-width:420px;margin:72px auto;background:var(--tk-surface);border:1px solid var(--tk-line);border-radius:28px;padding:32px;display:flex;flex-direction:column;gap:14px;box-shadow:var(--tk-shadow)}
.codei{letter-spacing:.5em;text-align:center;font-size:22px;font-weight:600}
.app{display:grid;grid-template-columns:220px 1fr;gap:24px}
.nav{display:flex;flex-direction:column;gap:4px;position:sticky;top:84px;align-self:start}
.nav button{border:0;background:none;text-align:left;padding:10px 14px;border-radius:12px;cursor:pointer;font-weight:500;color:var(--tk-ink-2);display:flex;justify-content:space-between}
.nav button.on{background:var(--tk-brand-soft);color:var(--tk-brand-text);font-weight:600}
.nav .dot{width:8px;height:8px;border-radius:50%;background:var(--tk-lost);align-self:center}
.split{display:grid;grid-template-columns:minmax(0,1fr) 400px;gap:24px;align-items:start}
.split.closed{grid-template-columns:1fr}.split.closed .panel{display:none}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:16px}
.card{background:var(--tk-surface);border:1px solid var(--tk-line);border-radius:20px;overflow:hidden;cursor:pointer;text-align:left;padding:0;display:flex;flex-direction:column}
.card.sel{border-color:var(--tk-brand);box-shadow:0 0 0 2px var(--tk-brand)}
.card .ph{aspect-ratio:4/3;background:var(--tk-sunken) center/cover;display:grid;place-items:center;font-size:44px}
.card .bd{padding:12px 14px;display:flex;flex-direction:column;gap:6px}
.card b{font-size:16px}
.panel{background:var(--tk-surface);border:1px solid var(--tk-line);border-radius:24px;padding:20px;display:flex;flex-direction:column;gap:14px;position:sticky;top:84px;max-height:calc(100vh - 110px);overflow:auto}
.panel .ph{height:180px;border-radius:16px;background:var(--tk-sunken) center/cover}
.row{display:flex;gap:10px;align-items:center}.row.wrapx{flex-wrap:wrap}
.li{display:flex;justify-content:space-between;padding:10px 0;border-bottom:1px solid var(--tk-line);font-size:14px}
.note{border-radius:14px;padding:12px 14px;font-size:14px;margin:0}.info{background:var(--tk-sunken);color:var(--tk-ink-2)}.okn{background:var(--tk-brand-soft);color:var(--tk-brand-text);font-weight:600}.warn{background:var(--tk-warn-soft);color:var(--tk-warn)}
.thread{display:flex;flex-direction:column;gap:8px}
.bub{max-width:88%;padding:10px 14px;border-radius:18px;font-size:14px}
.bub.in2{background:var(--tk-sunken);border-bottom-left-radius:6px}.bub.out{background:var(--tk-brand);color:var(--tk-on-brand);align-self:flex-end;border-bottom-right-radius:6px}
.bub small{display:block;font-size:12px;color:var(--tk-brand-text);margin-top:4px}
.compose{display:flex;gap:8px}
.hcode{display:flex;justify-content:space-between;align-items:center;border:1px dashed var(--tk-brand);border-radius:14px;padding:10px 14px}.hcode b{letter-spacing:.12em;font-size:18px}
.table{width:100%;border-collapse:collapse;background:var(--tk-surface);border-radius:20px;overflow:hidden;border:1px solid var(--tk-line)}
.table th,.table td{text-align:left;padding:14px 16px;border-bottom:1px solid var(--tk-line);font-size:14px}.table th{color:var(--tk-ink-2);font-weight:600;font-size:12px;text-transform:uppercase;letter-spacing:.05em}
.msgs{display:grid;grid-template-columns:320px 1fr;gap:20px}
.mrow{display:flex;gap:12px;align-items:center;padding:12px;border-radius:16px;cursor:pointer;border:1px solid transparent}
.mrow.on{background:var(--tk-surface);border-color:var(--tk-line)}
.av{width:44px;height:44px;border-radius:12px;background:var(--tk-sunken) center/cover;flex:none}
.box{background:var(--tk-surface);border:1px solid var(--tk-line);border-radius:24px;padding:24px;display:flex;flex-direction:column;gap:14px}
.finder{display:grid;grid-template-columns:1.1fr 1fr;gap:28px;align-items:start}
.hero{border-radius:24px;aspect-ratio:4/3;background:var(--tk-sunken) center/cover}
.urgent{background:var(--tk-lost);color:var(--tk-on-lost);border-radius:14px;padding:12px 14px;font-weight:600}
.opts{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}
.opt{border:1px solid var(--tk-line);border-radius:14px;padding:12px;cursor:pointer;font-weight:500;background:var(--tk-surface);text-align:left}
.opt.on{border-color:var(--tk-brand);background:var(--tk-brand-soft);font-weight:600}
.sugs div{padding:8px 4px;border-bottom:1px solid var(--tk-line);cursor:pointer;font-size:14px}
.check{display:flex;gap:10px;font-size:14px;cursor:pointer}.check[hidden]{display:none}
.legal{font-size:12px;color:var(--tk-ink-2);text-align:center;margin-top:28px}
.link{color:var(--tk-brand-text);text-decoration:underline;cursor:pointer;background:none;border:0;padding:0}
.modal{position:fixed;inset:0;background:rgb(0 0 0 / .5);display:grid;place-items:center;z-index:20;padding:16px}.modal[hidden]{display:none}
.modal .box{max-width:440px;width:100%}
.toast{position:fixed;left:50%;bottom:24px;transform:translateX(-50%);background:var(--tk-ink);color:var(--tk-surface);padding:10px 16px;border-radius:99px;font-size:14px;opacity:0;transition:opacity .3s;pointer-events:none}.toast.show{opacity:1}
.errt{color:var(--tk-lost-text);font-size:13px;margin:0}
[hidden]{display:none!important}
@media (max-width:900px){.app,.split,.msgs,.finder{grid-template-columns:1fr}.nav{flex-direction:row;overflow:auto;position:static}.opts{grid-template-columns:1fr}}
"""

HTML = r"""
<header class="top"><span class="logo"><svg width="26" height="26"><use href="#mark"/></svg>tagkin</span>
<div class="seg" role="tablist" aria-label="Prototype"><button class="on" data-mode="owner">Owner web</button><button data-mode="finder">Finder page</button></div>
<span class="sp"></span><span class="xs" id="url">tagkin.app/my-tags</span></header>

<main id="owner" class="view on">
 <section id="o-signin" class="signin">
  <h1>Sign in</h1><p class="m">Use your Tagkin email. No password: we send you a code.</p>
  <div id="si-1"><input class="in" id="si-email" type="email" value="alex@example.com" aria-label="Email"><p class="errt" id="si-err" hidden>Enter a valid email.</p><div style="height:10px"></div><button class="btn pri" id="si-send" style="width:100%">Send code</button></div>
  <div id="si-2" hidden><p class="m">Code sent to <b id="si-to"></b></p><input class="in codei" id="si-code" maxlength="6" inputmode="numeric" placeholder="······" aria-label="6-digit code"><p class="xs">Prototype: any 6 digits work.</p><div class="row"><button class="btn ghost" id="si-back">Back</button><span class="sp"></span><button class="btn pri off" id="si-go">Continue</button></div></div>
 </section>
 <div id="o-app" class="wrap" hidden><div class="app">
  <nav class="nav" aria-label="Owner"><button class="on" data-nav="tags">My tags</button><button data-nav="msgs">Messages <span class="dot"></span></button><button data-nav="orders">Orders</button><button data-nav="account">Account</button></nav>
  <div>
   <section id="v-tags" class="view on"><div class="row" style="margin-bottom:18px"><h1>My tags</h1><span class="sp"></span><button class="btn sec" data-toast="Opens tagkin.app/create (web beta, M2)">+ New tag</button></div>
    <div class="split closed" id="split"><div class="grid" id="grid"></div><aside class="panel" id="panel" aria-live="polite"></aside></div></section>
   <section id="v-msgs" class="view"><h1 style="margin-bottom:18px">Messages</h1><div class="msgs"><div id="mlist"></div><div class="box" id="mthread"></div></div></section>
   <section id="v-orders" class="view"><div class="row" style="margin-bottom:18px"><h1>Orders</h1><span class="sp"></span><button class="btn sec" data-toast="Ordering on the web arrives with the web beta (M2)">Order a tag</button></div>
    <table class="table"><thead><tr><th>Order</th><th>Items</th><th>Date</th><th>Status</th><th>Total</th></tr></thead><tbody><tr><td>TK-10482</td><td>2 × sticker (mint)</td><td>Today</td><td><span class="badge b-r">Printing</span></td><td>€7.80</td></tr><tr><td>TK-10311</td><td>1 × keychain (ink)</td><td>2 Nov</td><td><span class="badge b-n">Delivered</span></td><td>€12.40</td></tr></tbody></table></section>
   <section id="v-account" class="view"><h1 style="margin-bottom:18px">Account</h1><div class="box" style="max-width:520px"><div class="li"><span>Sign-in email</span><span class="muted">a•••@example.com</span></div><div class="li"><span>Recovery phone</span><span class="muted">Add in the app</span></div><div class="li"><span>Language</span><span class="muted">English</span></div><button class="btn sec" id="signout">Sign out</button></div></section>
  </div></div></div>
</main>

<main id="finder" class="view"><div class="wrap"><div class="finder">
 <div><div id="f-banner"></div><div class="hero" id="f-hero" style="margin-top:12px"></div><h1 id="f-title" style="margin-top:18px">Found me? Thank you! Tell my owner where I am.</h1><button class="link" id="f-orig" style="margin-top:8px">Translated from German · Show original</button></div>
 <div class="box" id="f-form"><h2>Tell the owner where it is</h2>
  <span class="xs">WHERE IS IT NOW?</span><div class="opts" id="f-where"><button class="opt">With me</button><button class="opt">Handed to staff</button><button class="opt">Left in a safe place</button></div>
  <span class="xs">WHERE EXACTLY?</span><input class="in" id="f-place" placeholder="Type a place, e.g. Darmstadt Hbf" autocomplete="off" aria-label="Place"><div class="sugs" id="f-sugs"></div><button class="btn sec" id="f-loc">📍 Share item location</button>
  <span class="xs">ANYTHING ELSE? (OPTIONAL)</span><textarea class="in" id="f-note" maxlength="500" placeholder="e.g. Left it with the staff at counter 2" aria-label="Note"></textarea>
  <label class="check" id="f-share" hidden><input type="checkbox" id="f-sharecb"> This shares your contact with the owner. Continue?</label>
  <span class="xs">HOW SHOULD WE PASS ON REPLIES?</span><div class="row"><input class="in" id="f-mail" type="email" placeholder="Email (kept hidden from the owner)" aria-label="Email"></div>
  <div class="row"><button class="btn pri off" id="f-send">Send to owner</button><button class="btn ghost off" id="f-anon">Send anonymously</button></div>
  <p class="xs">🔒 Your details stay private unless you choose to share them.</p></div>
 <div class="box" id="f-done" hidden><h2>Thank you. The owner has been told.</h2><p class="m" id="f-donesub"></p><div class="thread" id="f-thread"><div class="bub in2" id="f-reply">Waiting for the owner’s reply…</div></div>
  <div class="compose"><input class="in" id="f-rmsg" placeholder="Reply to the owner" aria-label="Reply"><button class="btn pri" id="f-rsend">Send</button></div>
  <div class="hcode"><span>🔗 Your report link</span><button class="link" data-toast="Link copied">Copy</button></div>
  <div class="row wrapx"><button class="btn sec" id="f-hopen">Check a handover code</button><button class="link" id="f-ropen">Report abuse</button></div></div>
</div><p class="legal">Impressum · Privacy · Terms</p></div></main>

<div class="modal" id="modal" hidden role="dialog" aria-modal="true"><div class="box" id="mbox"></div></div>
<div class="toast" role="status" aria-live="polite"></div>
"""

JS = r"""
const $=s=>document.querySelector(s),all=s=>document.querySelectorAll(s);
let tt;function toast(t){const e=$('.toast');e.textContent=t;e.classList.add('show');clearTimeout(tt);tt=setTimeout(()=>e.classList.remove('show'),1800);}
const esc=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
let TAGS=[{n:'Black backpack',p:'backpack',code:'TK-7Q4M-9XRA',st:'normal',scans:[['3 Nov 09:41','Frankfurt']]},{n:'Milo',p:'dog',code:'TK-M3PF-2KWD',st:'lost',scans:[['Today 14:02','Darmstadt'],['Yesterday 18:20','Griesheim']]},{n:'Blue suitcase',p:'suitcase',code:'TK-H8RC-4TNE',st:'return',scans:[['Today 11:05','Darmstadt']],rep:{where:'Handed to staff',place:'Darmstadt Hbf, Lost & Found desk',note:'Je l’ai laissée au guichet 2.',tr:'I left it at counter 2.',lang:'French'},msgs:[]},{n:'House keys',p:'keys',code:'TK-Q2LP-7HNC',st:'normal',ret:true,scans:[]}];
let SEL=-1,MSEL=-1;
let BADGE=t=>t.st==='lost'?'<span class="badge b-l">Lost</span>':t.st==='return'?'<span class="badge b-r">Return active</span>':t.ret?'<span class="badge b-r">Returned</span>':'<span class="badge b-n">Active</span>';
function grid(){$('#grid').innerHTML=TAGS.map((t,i)=>'<button class="card'+(i===SEL?' sel':'')+'" data-t="'+i+'" aria-label="'+esc(t.n)+'"><span class="ph" style="background-image:url('+SAMPLE[t.p]+')"></span><span class="bd"><b>'+esc(t.n)+'</b><span class="xs">'+t.code+'</span>'+BADGE(t)+'</span></button>').join('');
 $('.nav .dot').hidden=!TAGS.some(t=>t.st==='return');}
function thread(t){const r=t.rep;return '<div class="thread"><div class="bub in2"><b>'+esc(r.where)+'</b> · '+esc(r.place)+'<br>'+esc(r.tr)+'<small>Translated from '+r.lang+' · original: “'+esc(r.note)+'”</small></div>'+t.msgs.map(m=>'<div class="bub out">'+esc(m)+'</div>').join('')+'</div><div class="compose"><input class="in" data-reply placeholder="Write a reply (sent translated)" aria-label="Reply"><button class="btn pri" data-send>Send</button></div><div class="hcode"><span>🔑 Handover code</span><b>739 204</b></div><p class="xs">Show this code when you collect it. Never share it in a message.</p>';}
function panel(){const t=TAGS[SEL];$('#split').classList.toggle('closed',!t);if(!t)return;let h='<div class="row"><h2>'+esc(t.n)+'</h2><span class="sp"></span><button class="btn ghost" data-close aria-label="Close">✕</button></div><div class="ph" style="background-image:url('+SAMPLE[t.p]+')"></div><div class="row">'+BADGE(t)+'<span class="xs">'+t.code+'</span></div>';
 if(t.st==='normal')h+='<button class="btn lostb" data-act="lost">Mark as lost</button><p class="xs">Finders then see “This item is missing” and you get an alert at every scan.</p>';
 if(t.st==='lost')h+='<p class="m">Scans since marked lost (city only)</p>'+(t.scans.map(s=>'<div class="li"><span>'+s[0]+'</span><span class="muted">'+s[1]+'</span></div>').join('')||'<p class="xs">No scans yet.</p>')+'<button class="btn pri" data-act="found">I found it myself</button><button class="btn sec" data-act="simulate">Simulate: a finder reports it</button>';
 if(t.st==='return')h+='<p class="note okn">A finder reported it. Name, photo and description are locked until the return ends.</p>'+thread(t)+'<button class="btn sec" data-act="returned">Got it back? Mark as returned</button>';
 if(t.st==='normal')h+='<p class="m">Scan history</p>'+(t.scans.map(s=>'<div class="li"><span>'+s[0]+'</span><span class="muted">'+s[1]+'</span></div>').join('')||'<p class="xs">No scans yet.</p>');
 h+='<button class="link" data-toast="QR image downloaded">Download QR code</button>';$('#panel').innerHTML=h;}
function modal(h){$('#mbox').innerHTML=h;$('#modal').hidden=false;const f=$('#mbox .btn');if(f)f.focus();}
function closeModal(){$('#modal').hidden=true;}
function msgs(){const R=TAGS.map((t,i)=>[t,i]).filter(([t])=>t.rep);if(MSEL<0&&R.length)MSEL=R[0][1];
 $('#mlist').innerHTML=R.map(([t,i])=>'<div class="mrow'+(i===MSEL?' on':'')+'" data-m="'+i+'"><span class="av" style="background-image:url('+SAMPLE[t.p]+')"></span><span><b>'+esc(t.n)+'</b><br><span class="xs">'+esc(t.rep.where)+' · '+esc(t.rep.place)+'</span></span></div>').join('')||'<p class="m">No messages yet.</p>';
 const t=TAGS[MSEL];$('#mthread').innerHTML=t&&t.rep?'<h2>'+esc(t.n)+'</h2>'+thread(t):'<p class="m">When someone finds one of your items, their message appears here.</p>';}
function nav(v){all('.nav button').forEach(b=>b.classList.toggle('on',b.dataset.nav===v));all('#o-app .view').forEach(x=>x.classList.toggle('on',x.id==='v-'+v));$('#url').textContent='tagkin.app/'+({tags:'my-tags',msgs:'messages',orders:'orders',account:'account'})[v];if(v==='msgs')msgs();if(v==='tags'){grid();panel();}history.replaceState(null,'','#'+v);}
function mode(m){all('.seg button').forEach(b=>b.classList.toggle('on',b.dataset.mode===m));$('#owner').classList.toggle('on',m==='owner');$('#finder').classList.toggle('on',m==='finder');$('#url').textContent=m==='owner'?'tagkin.app/my-tags':'tagkin.app/TK-7Q4M-9XRA';}
const PLACES=['Darmstadt Hbf, Lost & Found desk','Darmstadt Hbf, Platform 4','Luisenplatz, Darmstadt','Frankfurt (Main) Hbf, Lost & Found','Frankfurt Airport, Terminal 1'];
let where=-1,shared=false,REPORTED=false,TRIES=5,orig=false;
function fok(){const hit=/(\+?\d[\d\s\-()]{6,}\d)|([^\s@]+@[^\s@]+\.[^\s@]+)/.test($('#f-note').value);$('#f-share').hidden=!hit;const ok=where>=0&&($('#f-place').value.trim()||shared)&&(!hit||$('#f-sharecb').checked);$('#f-send').classList.toggle('off',!ok);$('#f-anon').classList.toggle('off',!ok);}
function report(anon){const v=$('#f-mail').value.trim();if(!anon&&v&&!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v)){toast('Check the email address');return;}
 REPORTED=true;$('#f-form').hidden=true;$('#f-done').hidden=false;$('#f-donesub').textContent=anon||!v?'Keep this page open to see their reply, or save your report link.':'Their reply also comes to your email, with your report link.';
 TAGS[0].st='return';TAGS[0].rep={where:['With me','Handed to staff','Left in a safe place'][where],place:$('#f-place').value||'Shared location',note:$('#f-note').value||'(no note)',tr:$('#f-note').value||'(no note)',lang:'English'};TAGS[0].msgs=[];
 setTimeout(()=>{$('#f-reply').innerHTML='<b>Owner</b><br>Thank you so much! I’ll pick it up tonight.';},2500);}
document.addEventListener('click',e=>{const q=s=>e.target.closest(s);
 if(q('[data-mode]'))mode(q('[data-mode]').dataset.mode);
 if(q('[data-toast]'))toast(q('[data-toast]').dataset.toast);
 if(q('#si-send')){const v=$('#si-email').value.trim();const ok=/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v);$('#si-err').hidden=ok;if(ok){$('#si-1').hidden=true;$('#si-2').hidden=false;$('#si-to').textContent=v;$('#si-code').value='';$('#si-code').focus();}}
 if(q('#si-back')){$('#si-2').hidden=true;$('#si-1').hidden=false;}
 if(q('#si-go')&&!q('.off')){$('#o-signin').hidden=true;$('#o-app').hidden=false;nav('tags');}
 if(q('#signout')){$('#o-app').hidden=true;$('#o-signin').hidden=false;$('#si-2').hidden=true;$('#si-1').hidden=false;SEL=-1;toast('Signed out');}
 if(q('[data-nav]'))nav(q('[data-nav]').dataset.nav);
 if(q('[data-t]')){SEL=+q('[data-t]').dataset.t;grid();panel();}
 if(q('[data-close]')){SEL=-1;grid();panel();}
 const a=q('[data-act]');if(a){const t=TAGS[SEL],k=a.dataset.act;
  if(k==='lost')modal('<h2>Mark '+esc(t.n)+' as lost?</h2><p class="m">Finders see an urgent page. You get an alert with the city every time it’s scanned. You can still update the photo.</p><button class="btn lostb" data-confirm="lost">Mark as lost</button><button class="btn sec" data-mclose>Cancel</button>');
  if(k==='found'){t.st='normal';toast('Marked as found');}
  if(k==='simulate'){t.st='return';t.rep={where:'With me',place:'Herrngarten, Darmstadt',note:'Ich habe ihn. Er ist ruhig.',tr:'I have him. He is calm.',lang:'German'};t.msgs=[];toast('New report: '+t.n);}
  if(k==='returned')modal('<h2>Got '+esc(t.n)+' back?</h2><p class="m">The return closes and the tag goes back to Active. You can thank the finder privately.</p><textarea class="in" placeholder="Private thank-you (optional)" aria-label="Thank-you"></textarea><button class="btn pri" data-confirm="returned">Mark as returned</button><button class="btn sec" data-mclose>Cancel</button>');
  grid();panel();}
 const cf=q('[data-confirm]');if(cf){const t=TAGS[SEL];if(cf.dataset.confirm==='lost'){t.st='lost';t.ret=false;toast('Marked as lost');}else{t.st='normal';t.ret=true;delete t.rep;toast('Marked as returned');}closeModal();grid();panel();}
 if(q('[data-mclose]')||e.target.id==='modal')closeModal();
 if(q('[data-m]')){MSEL=+q('[data-m]').dataset.m;msgs();}
 if(q('[data-send]')){const box=q('.box,.panel');const i=box.querySelector('[data-reply]');const t=TAGS[box.id==='mthread'?MSEL:SEL];if(i.value.trim()){t.msgs.push(i.value.trim());box.id==='mthread'?msgs():panel();toast('Sent, translated for the finder');}}
 const o=q('#f-where .opt');if(o){all('#f-where .opt').forEach((x,i)=>{x.classList.toggle('on',x===o);if(x===o)where=i;});fok();}
 if(q('#f-loc')){shared=true;$('#f-loc').textContent='✓ Item location shared';fok();}
 if(q('#f-sugs div')){$('#f-place').value=q('#f-sugs div').textContent;$('#f-sugs').innerHTML='';fok();}
 if(q('#f-send')&&!q('.off'))report(false);if(q('#f-anon')&&!q('.off'))report(true);
 if(q('#f-rsend')){const i=$('#f-rmsg');if(i.value.trim()){const d=document.createElement('div');d.className='bub out';d.textContent=i.value;$('#f-thread').appendChild(d);i.value='';}}
 if(q('#f-orig')){orig=!orig;$('#f-title').textContent=orig?'Gefunden? Danke! Sag meinem Besitzer, wo ich bin.':'Found me? Thank you! Tell my owner where I am.';$('#f-orig').textContent=orig?'Original in German · Show translation':'Translated from German · Show original';}
 if(q('#f-hopen'))modal('<h2>Before you hand it over</h2><p class="m">Ask the person collecting it for the owner’s 6-digit handover code.</p><input class="in" id="h-in" inputmode="numeric" placeholder="6-digit code" aria-label="Handover code"><p class="errt" id="h-bad" hidden></p><p class="note okn" id="h-ok" hidden>✓ Code matches. You can hand it over.</p><button class="btn pri" id="h-check">Check code</button><button class="btn pri" id="h-done" hidden>I’ve handed it over</button><p class="xs">Try 739 204.</p>');
 if(q('#h-check')){if(TRIES<=0){toast('Too many tries. Wait 15 minutes.');return;}const ok=$('#h-in').value.replace(/\s/g,'')==='739204';$('#h-ok').hidden=!ok;$('#h-done').hidden=!ok;$('#h-check').hidden=ok;if(!ok){TRIES--;$('#h-bad').hidden=false;$('#h-bad').textContent=TRIES?'That code doesn’t match. Don’t hand it over. '+TRIES+' tries left.':'Too many tries. Wait 15 minutes.';}}
 if(q('#h-done')){$('#mbox').innerHTML='<h2>It’s back with its owner.</h2><p class="m">Thank you for helping. We’ve told the owner and closed this conversation.</p><div class="note okn">Protect your own things: your first printed tag is €2 off.</div><button class="btn pri" data-mclose>Done</button>';TAGS[0].st='normal';TAGS[0].ret=true;delete TAGS[0].rep;}
 if(q('#f-ropen'))modal('<h2>Report this tag</h2><p class="m">Tell us what’s wrong. Your report is private.</p><div class="opts" id="r-opts" style="grid-template-columns:1fr"><button class="opt">The message is abusive or spam</button><button class="opt">It looks fake or misleading</button><button class="opt">Something else</button></div><textarea class="in" id="r-text" placeholder="Add details" hidden></textarea><p class="note warn">If someone is in danger, call 112 now.</p><div class="row"><button class="btn ghost" data-mclose>Cancel</button><span class="sp"></span><button class="btn pri off" id="r-send">Report</button></div>');
 const ro=q('#r-opts .opt');if(ro){all('#r-opts .opt').forEach(x=>x.classList.toggle('on',x===ro));$('#r-text').hidden=false;$('#r-send').classList.toggle('off',ro===all('#r-opts .opt')[2]&&!$('#r-text').value.trim());}
 if(q('#r-send')&&!q('.off'))$('#mbox').innerHTML='<h2>Thanks for reporting</h2><p class="m">We’ll review this tag. If it breaks our rules, we’ll act on it. The owner won’t know who reported it.</p><button class="btn pri" data-mclose>Done</button>';
});
document.addEventListener('input',e=>{const id=e.target.id;
 if(id==='si-code'){e.target.value=e.target.value.replace(/\D/g,'');$('#si-go').classList.toggle('off',e.target.value.length!==6);}
 if(id==='f-place'){const v=e.target.value.trim().toLowerCase();$('#f-sugs').innerHTML=v.length>=2?PLACES.filter(p=>p.toLowerCase().includes(v)).map(p=>'<div>'+esc(p)+'</div>').join(''):'';fok();}
 if(id==='f-note')fok();
 if(id==='r-text'){const on=$('#r-opts .opt.on');$('#r-send').classList.toggle('off',!on||(on===all('#r-opts .opt')[2]&&!e.target.value.trim()));}});
document.addEventListener('change',e=>{if(e.target.id==='f-sharecb')fok();});
document.addEventListener('keydown',e=>{if(e.key==='Escape')closeModal();if(e.key==='Enter'&&e.target.matches('[data-reply]'))e.target.closest('.box,.panel').querySelector('[data-send]').click();});
$('#f-hero').style.backgroundImage='url('+SAMPLE.backpack+')';
"""

page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Tagkin desktop prototype</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700&family=Geist:wght@400;500;600;700&display=swap">
<style>{TOKENS}</style>
<style>{CSS}{DCSS6}</style>
</head>
<body>
{MARK}{HTML}
<script>{SAMPLES_JS}{JS}{DJS6}</script>
</body>
</html>
"""
OUT.write_text(page)
print(f"wrote {OUT.relative_to(ROOT)}")
