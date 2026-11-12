"""Desktop round 6 (12 Nov 2026): owner web with a Get the app card for instant alerts (create and
order stay on the web beta), blank tags set up on the web with the shape-fit rule, photo and name edit, order details
with the full lifecycle, and a finder page that closes after the handover."""

DCSS6 = r"""
.warnb{background:var(--tk-warn-soft);color:var(--tk-warn)}
.card .ph.blank{font-size:44px}
.getapp{margin-top:16px;border:1px solid var(--tk-line);border-radius:16px;padding:14px;display:flex;flex-direction:column;gap:8px;background:var(--tk-surface)}
.getapp b{font-size:14px}.getapp .xs{line-height:1.4}
.stores{display:flex;gap:8px;flex-wrap:wrap}.stores .btn{min-height:40px;font-size:14px}
.samp{display:grid;grid-template-columns:repeat(6,1fr);gap:6px}.samp img{width:100%;aspect-ratio:1;object-fit:cover;border-radius:10px;cursor:pointer;border:2px solid transparent}.samp img.on{border-color:var(--tk-brand)}
.edph{height:150px;border-radius:16px;background:var(--tk-sunken) center/cover;display:grid;place-items:center;font-size:40px}
.tl{list-style:none;margin:0;padding:0}.tl li{position:relative;padding:0 0 10px 26px;display:flex;justify-content:space-between;color:var(--tk-ink-2);font-size:14px}
.tl li::before{content:"";position:absolute;left:3px;top:5px;width:11px;height:11px;border-radius:50%;background:var(--tk-line)}
.tl li::after{content:"";position:absolute;left:8px;top:17px;bottom:0;width:2px;background:var(--tk-line)}.tl li:last-child::after{display:none}
.tl li.on{color:var(--tk-ink)}.tl li.on::before{background:var(--tk-brand)}.tl li.now b{font-weight:700}
.demo{border:1px dashed var(--tk-line);border-radius:14px;padding:10px;display:flex;gap:8px;flex-wrap:wrap;align-items:center}
.table tbody tr{cursor:pointer}.table tbody tr:hover{background:var(--tk-sunken)}
.modal .box{max-height:calc(100vh - 32px);overflow:auto}
.closed{text-align:center;align-items:center}.closed .done{width:64px;height:64px;border-radius:50%;background:var(--tk-brand);color:var(--tk-on-brand);display:grid;place-items:center;font-size:30px}
"""

DJS6 = r"""
var FIT={'Sticker':[0,1],'Keychain':[0],'Pet tag':[2],'Luggage label':[1],'Lock screen':[0]};
var TYN=['Item','Travel','Pet'],TYS=['Keys, bag, laptop','Luggage on a journey','Collar tag'];
TAGS.push({n:'Blank keychain',p:null,code:'TK-B7KD-3QWE',st:'unset',style:'Keychain',scans:[]},{n:'Blank sticker',p:null,code:'TK-C4RM-8PZA',st:'unset',style:'Sticker',scans:[]});
function PH(t){return t.ph||(t.p?SAMPLE[t.p]:'');}
const _B=BADGE;BADGE=t=>t.st==='unset'?'<span class="badge warnb">Set up</span>':t.fresh?'<span class="badge b-r">New</span>':_B(t);
function grid(){$('#grid').innerHTML=TAGS.map((t,i)=>'<button class="card'+(i===SEL?' sel':'')+'" data-t="'+i+'" aria-label="'+esc(t.n)+'"><span class="ph'+(PH(t)?'':' blank')+'" style="'+(PH(t)?'background-image:url('+PH(t)+')':'')+'">'+(PH(t)?'':'🏷️')+'</span><span class="bd"><b>'+esc(t.n)+'</b><span class="xs">'+t.code+(t.st==='unset'?' · '+t.style.toLowerCase():'')+'</span>'+BADGE(t)+'</span></button>').join('');
 $('.nav .dot').hidden=!TAGS.some(t=>t.st==='return');}
var STP=null,EDP=null;
function sampPick(cur){return '<div class="samp">'+Object.keys(SAMPLE).map(k=>'<img alt="'+k+'" data-sp="'+k+'" src="'+SAMPLE[k]+'"'+(cur===SAMPLE[k]?' class="on"':'')+'>').join('')+'</div><label class="btn sec" style="width:100%">Upload a photo<input type="file" accept="image/*" id="up-in" hidden></label><p class="xs">Up to 10 MB. We remove location data.</p>';}
function panel(){const t=TAGS[SEL];$('#split').classList.toggle('closed',!t);if(!t)return;
 let h='<div class="row"><h2>'+esc(t.n)+'</h2><span class="sp"></span><button class="btn ghost" data-close aria-label="Close">✕</button></div>';
 if(t.st==='unset'){const ok=FIT[t.style];if(STP===null||!ok.includes(STP))STP=ok[0];
  h+='<div class="row">'+BADGE(t)+'<span class="xs">'+t.code+' · blank '+t.style.toLowerCase()+'</span></div><p class="m">Link it to something. A '+t.style.toLowerCase()+' fits '+ok.map(k=>TYN[k].toLowerCase()).join(' or ')+'.</p>';
  h+=ok.length>1?'<div class="opts" style="grid-template-columns:repeat('+ok.length+',1fr)">'+ok.map(k=>'<button class="opt'+(k===STP?' on':'')+'" data-sty="'+k+'">'+TYN[k]+'<br><span class="xs">'+TYS[k]+'</span></button>').join('')+'</div>':'<p class="note info">Type: '+TYN[ok[0]]+'</p>';
  h+='<input class="in" id="su-name" maxlength="40" placeholder="'+(STP===2?'Your pet’s name':'Name, e.g. Black backpack')+'" aria-label="Name"><p class="errt" id="su-err" hidden>Give it a name, at least 2 characters.</p><span class="xs">PHOTO (OPTIONAL)</span>'+sampPick(EDP)+'<button class="btn pri" data-act="setup">Make it live</button><p class="xs">You can write the finder message later. We use a friendly default until then.</p>';
  $('#panel').innerHTML=h;return;}
 h+='<div class="ph" style="background-image:url('+PH(t)+')"></div><div class="row">'+BADGE(t)+'<span class="xs">'+t.code+'</span><span class="sp"></span>'+(t.st==='return'?'<span class="xs">🔒 Name and photo locked</span>':'<button class="link" data-act="edit">Edit name and photo</button>')+'</div>';
 if(t.st==='normal')h+='<button class="btn lostb" data-act="lost">Mark as lost</button><p class="xs">Finders then see “This item is missing” and you get an alert at every scan.</p>';
 if(t.st==='lost')h+='<p class="m">Scans since marked lost (city only)</p>'+((t.lost||t.scans).map(s=>'<div class="li"><span>'+s[0]+'</span><span class="muted">'+s[1]+'</span></div>').join('')||'<p class="note info">No scans since you marked it lost. We alert you the moment someone scans it.</p>')+'<button class="btn pri" data-act="found">I found it myself</button><button class="btn sec" data-act="simulate">Simulate: a finder reports it</button>';
 if(t.st==='return')h+='<p class="note okn">A finder reported it. Name, photo and description are locked until the return ends.</p>'+thread(t)+'<button class="btn sec" data-act="returned">Got it back? Mark as returned</button>';
 if(t.st==='normal')h+='<p class="m">Scan history</p>'+(t.scans.map(s=>'<div class="li"><span>'+s[0]+'</span><span class="muted">'+s[1]+'</span></div>').join('')||'<p class="note info">No scans yet. Scan the QR with your phone to test it.</p>');
 h+='<button class="link" data-toast="QR image downloaded">Download QR code</button>';$('#panel').innerHTML=h;}
function editModal(){const t=TAGS[SEL];EDP=PH(t)||null;modal('<h2>Item details</h2><div class="edph" id="ed-ph" style="'+(EDP?'background-image:url('+EDP+')':'')+'">'+(EDP?'':'🏷️')+'</div>'+sampPick(EDP)+'<input class="in" id="ed-name" maxlength="40" aria-label="Name"><p class="errt" id="ed-err" hidden>Give it a name, at least 2 characters.</p><div class="row"><button class="btn ghost" data-mclose>Cancel</button><span class="sp"></span><button class="btn pri" id="ed-save">Save</button></div>');$('#ed-name').value=t.n;}
function appModal(what){modal('<h2>Get instant alerts</h2><p class="m">Everything works here on the web. The app adds what needs a phone: an alert the second someone scans a lost tag, your free lock-screen tag, and scanning gift or shop tags to activate them.</p><div class="stores"><button class="btn pri" data-toast="Opens the App Store">App Store</button><button class="btn pri" data-toast="Opens Google Play">Google Play</button></div><p class="xs">Or scan the QR on this page with your phone.</p><button class="btn ghost" data-mclose>Close</button>');}
// orders
var STG=['Paid','Sent to print','Printing','Quality check','Shipped','Out for delivery','Delivered'],PLAN=[0,0,1,2,3,5,5];
var EXC={cancelled:['Cancelled','b-n','Cancelled before printing. Refunded in 3 to 5 working days.'],reprint:['Reprinting','warnb','It failed our print check, so we’re printing it again. About 2 days extra, no cost to you.'],delayed:['Delayed','warnb','The carrier is running late.'],failed:['Delivery failed','b-l','The carrier couldn’t deliver it. Check your address and we’ll send it again for free.'],problem:['Replacement on its way','warnb','A free replacement is being printed. No need to send anything back.']};
var ORD=[{id:10482,t:'2 × sticker (mint)',for:'Black backpack',ago:2,k:2,total:7.30,addr:'Alex Mensah, Musterstraße 1, 64283 Darmstadt',exc:null},{id:10471,t:'2 × keychain, sticker (blank)',for:'blank tags, set up when they arrive',ago:6,k:4,total:16.30,addr:'Alex Mensah, Musterstraße 1, 64283 Darmstadt',exc:null},{id:10311,t:'1 × keychain (ink)',for:'House keys',ago:15,k:6,total:10.40,addr:'Alex Mensah, Musterstraße 1, 64283 Darmstadt',exc:null}],OS=null;
function dt(o,off){const d=new Date(2026,10,12-o.ago+off);return d.getDate()+' '+['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'][d.getMonth()];}
const oL=o=>o.exc?EXC[o.exc][0]:STG[o.k],oC=o=>o.exc?EXC[o.exc][1]:o.k===6?'b-n':'b-r',oX=o=>o.exc&&o.exc!=='cancelled'?2:0;
function orders(){$('#v-orders tbody').innerHTML=ORD.map((o,i)=>'<tr data-o="'+i+'" tabindex="0"><td>TK-'+o.id+'</td><td>'+esc(o.t)+'</td><td>'+dt(o,0)+'</td><td><span class="badge '+oC(o)+'">'+oL(o)+'</span></td><td>€'+o.total.toFixed(2)+'</td></tr>').join('');}
function orderModal(){const o=OS,x=oX(o);let h='<div class="row"><h2>Order TK-'+o.id+'</h2><span class="sp"></span><span class="badge '+oC(o)+'">'+oL(o)+'</span></div><p class="m">'+(o.exc==='cancelled'?'Cancelled':o.k===6&&!o.exc?'Delivered on '+dt(o,PLAN[6]):'Arrives by '+dt(o,PLAN[6]+x))+' · '+esc(o.t)+' for '+esc(o.for)+'</p>';
 if(o.exc)h+='<p class="note '+(o.exc==='failed'?'warn':'info')+'">'+EXC[o.exc][2]+'</p>';
 if(o.exc!=='cancelled')h+='<ol class="tl">'+STG.map((s,i)=>{const done=i<o.k||(i===o.k&&!['reprint','failed'].includes(o.exc));return '<li class="'+(done?'on':'')+(i===o.k?' now':'')+'"><b>'+s+'</b><span class="xs">'+(done?dt(o,PLAN[i]+(i>2?x:0)):'Expected '+dt(o,PLAN[i]+x))+'</span></li>';}).join('')+'</ol>';
 h+='<div class="li"><span>Deliver to</span><span class="muted">'+esc(o.addr)+'</span></div><div class="li"><span>Total paid</span><span>€'+o.total.toFixed(2)+'</span></div>';
 if(!o.exc&&o.k<=3)h+='<button class="btn sec" data-oa="addr">Change delivery address</button>';
 if(!o.exc&&o.k<=1)h+='<button class="btn ghost" data-oa="cancel" style="color:var(--tk-lost-text)">Cancel order</button>';
 if(o.k>=4&&o.k<=5&&o.exc!=='failed')h+='<button class="btn sec" data-toast="Opens DHL tracking">Track parcel</button>';
 if(o.exc==='failed')h+='<button class="btn pri" data-oa="addr">Check address and send again</button>';
 if(o.k===6&&!o.exc)h+='<button class="btn sec" data-oa="problem">Report a problem</button>';
 if(o.exc!=='cancelled'&&!(o.k===6&&!o.exc))h+='<div class="demo"><span class="xs">PROTOTYPE</span><button class="btn sec" data-oa="next">Next stage</button><button class="btn sec" data-oa="sim">Simulate a problem</button></div>';
 h+='<button class="btn ghost" data-mclose>Close</button>';modal(h);}
// sidebar: get the app
(function(){const g=document.createElement('div');g.className='getapp';g.innerHTML='<b>Get instant alerts</b><span class="xs">The app tells you the second someone scans a lost tag. The web only shows it when you look.</span><button class="btn pri" data-app="Get alerts">Get the app</button>';$('.nav').appendChild(g);})();
all('#v-tags .btn.sec[data-toast]').forEach(b=>{b.dataset.toast='Opens tagkin.app/create: the same steps as the app (web beta)';});
all('#v-orders .btn.sec[data-toast]').forEach(b=>{b.dataset.toast='Opens tagkin.app/create to order a tag (web beta)';});
const _nav=nav;nav=function(v){_nav(v);if(v==='orders')orders();};
// finder: the handover closes the report
(function(){const c=document.createElement('div');c.className='box closed';c.id='f-closed';c.hidden=true;c.innerHTML='<div class="done">✓</div><h2>Handed over. Thank you.</h2><p class="m">The owner has their item back and this conversation is closed. Nothing else to do.</p><div class="note okn">Protect your own things: your first printed tag is €2 off.</div><button class="btn sec" data-toast="Opens tagkin.app">Discover Tagkin</button>';$('#f-done').after(c);})();
document.addEventListener('click',e=>{const q=s=>e.target.closest(s);
 const ap=q('[data-app]');if(ap){appModal(ap.dataset.app==='Get alerts'?'Get alerts':ap.dataset.app);return;}
 if(q('#h-done')){setTimeout(()=>{$('#f-done').hidden=true;$('#f-form').hidden=true;$('#f-closed').hidden=false;$('#f-title').textContent='This item is back with its owner.';$('#f-orig').hidden=true;$('#url').textContent='tagkin.app/r/…  (closed)';closeModal();},0);}
 const sy=q('[data-sty]');if(sy){STP=+sy.dataset.sty;const v=$('#su-name').value;panel();$('#su-name').value=v;return;}
 const sp=q('[data-sp]');if(sp){EDP=SAMPLE[sp.dataset.sp];all('.samp img').forEach(x=>x.classList.toggle('on',x===sp));const ep=$('#ed-ph');if(ep){ep.style.backgroundImage='url('+EDP+')';ep.textContent='';}return;}
 const a=q('[data-act]');if(a&&a.dataset.act==='setup'){e.stopImmediatePropagation();const t=TAGS[SEL],n=$('#su-name').value.trim();if(n.length<2){$('#su-err').hidden=false;$('#su-name').focus();return;}
  Object.assign(t,{n:n,ph:EDP,st:'normal',fresh:true,type:STP,scans:[]});STP=null;EDP=null;grid();panel();toast(n+' is live');return;}
 if(a&&a.dataset.act==='edit'){e.stopImmediatePropagation();editModal();return;}
  if(q('[data-confirm=lost]')){TAGS[SEL].lost=[];TAGS[SEL].fresh=false;}
 if(a&&a.dataset.act==='simulate'){const t=TAGS[SEL];t.scans.unshift(['Today, just now','Darmstadt']);}
 if(q('#ed-save')){const n=$('#ed-name').value.trim();if(n.length<2){$('#ed-err').hidden=false;return;}const t=TAGS[SEL];t.n=n;if(EDP)t.ph=EDP;closeModal();grid();panel();toast('Saved everywhere this item appears');return;}
 const r=q('[data-o]');if(r){OS=ORD[+r.dataset.o];orderModal();return;}
 const oa=q('[data-oa]');if(oa&&OS){const o=OS,k=oa.dataset.oa;
  if(k==='next'){if(o.exc==='failed'){toast('Waiting for you: check the address');return;}if(o.exc==='reprint'){o.exc=null;o.k=3;}else if(o.exc==='problem'){o.exc=null;o.k=6;}else{if(o.exc==='delayed')o.exc=null;if(o.k<6)o.k++;}}
  if(k==='sim'){o.exc=o.k<=3?'reprint':o.k===4?'delayed':'failed';if(o.k<2)o.k=2;}
  if(k==='cancel'){o.exc='cancelled';toast('Order cancelled. Refund on its way.');}
  if(k==='problem'){o.exc='problem';o.k=4;toast('Free replacement on its way');}
  if(k==='addr'){modal('<h2>Delivery address</h2><input class="in" id="oa-in" aria-label="Address"><div class="row"><button class="btn ghost" data-oa="back">Cancel</button><span class="sp"></span><button class="btn pri" data-oa="save">'+(o.exc==='failed'?'Send again':'Save')+'</button></div>');$('#oa-in').value=o.addr;return;}
  if(k==='save'){const v=$('#oa-in').value.trim();if(v.length<8){toast('Enter the full address');return;}o.addr=v;if(o.exc==='failed'){o.exc=null;o.k=4;toast('Sent again');}else toast('Address updated');}
  orders();orderModal();return;}
},true);
document.addEventListener('change',e=>{if(e.target.id==='up-in'&&e.target.files[0]){const f=e.target.files[0];if(f.size>10*1024*1024){toast('That photo is over 10 MB.');return;}const fr=new FileReader();fr.onload=()=>{EDP=fr.result;const ep=$('#ed-ph');if(ep){ep.style.backgroundImage='url('+EDP+')';ep.textContent='';}toast('Photo added');};fr.readAsDataURL(f);}});
document.addEventListener('keydown',e=>{if(e.key==='Enter'&&e.target.matches('[data-o]'))e.target.click();});
"""
