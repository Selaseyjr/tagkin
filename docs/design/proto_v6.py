"""Prototype round 6 (12 Nov 2026): one shape-fit table drives every screen, blank tags keep
their shape, each tag has its own scan history, photo edit on tag screens, order details with
the full order lifecycle and a demo control for stages and problems."""

OWNER_JS6 = r"""
// ---- 1. shape fit: which item types each shape can go on (BUSINESS-RULES 3c)
var FIT={'Sticker':[0,1],'Keychain':[0],'Pet tag':[2],'Luggage label':[1],'Lock screen':[0]};
var PHYS=['Sticker','Keychain','Pet tag','Luggage label'];
var DSCR=['details','t-details','p-details'];
function shapesFor(ty){return PHYS.filter(s=>FIT[s].includes(ty));}
setType=function(i){const d=st();if(!(FIT[d.style]||[]).includes(i))setDesign(shapesFor(i)[0]);};
function typeFilter(){const d=st();const ok=FIT[d.style]||[0,1,2];if(!ok.includes(d.type))d.type=ok[0];
 const opts=[...$('#type .grp').children];opts.forEach((o,k)=>{o.hidden=!ok.includes(k);o.classList.toggle('on',k===d.type);});
 $('#type .btn.pri').dataset.go=DSCR[d.type];let n=$('#type .fitnote');if(!n){n=document.createElement('p');n.className='xs fitnote';$('#type .grp').after(n);}
 n.textContent=ok.length>1?'A '+d.style.toLowerCase()+' works on '+ok.map(k=>['items','luggage','pets'][k]).join(' or ')+'.':'';}
const _r6=render;render=function(){_r6();const d=st();const lock=d.style==='Lock screen';const ok=lock?[]:d.blank?PHYS:shapesFor(d.type);
 all('#design .styles .chip').forEach(c=>{c.hidden=!ok.includes(c.textContent);});const row=$('#design .styles').closest('.czr');if(row)row.hidden=lock||ok.length<2;};

// ---- 2. every tag carries its own type, shape and scan history
const _ti6=tagsInit;tagsInit=function(){_ti6();
 Object.assign(TAGS[0],{type:0,style:'Sticker',scans:[['Today 14:02','Darmstadt','Report sent · with finder'],['3 Nov 09:41','Frankfurt','Viewed, no report']],lostScans:[]});
 Object.assign(TAGS[1],{type:2,style:'Pet tag',scans:[['Today 14:02','Darmstadt','Viewed, no report'],['Today 09:41','Darmstadt','Viewed, no report'],['Yesterday 18:20','Griesheim','Viewed, no report'],['28 Oct 10:15','Darmstadt','Test scan']],lostScans:[['Today 14:02','Darmstadt'],['Today 09:41','Darmstadt'],['Yesterday 18:20','Griesheim']]});
 Object.assign(TAGS[2],{type:1,style:'Luggage label',scans:[['Today 11:05','Darmstadt','Report sent · handed to staff'],['Yesterday 21:40','Frankfurt Airport','Viewed, no report'],['Yesterday 16:02','Frankfurt Airport','Viewed, no report'],['1 Nov 08:30','Darmstadt','Test scan']],lostScans:[]});};
const _add6=addTag;addTag=function(){const d=st();if(d.saved)return;
 if(d.blank){d.saved=true;const q=+$('#order .step i').textContent||1;for(let k=0;k<q;k++)TAGS.unshift({name:'Blank '+d.style.toLowerCase(),e:'🏷️',code:newCode(),st:'unset',style:d.style,type:null,scans:[],lostScans:[]});CUR=0;return;}
 _add6();const t=TAGS[0];if(t){t.type=d.type;t.style=d.style;t.scans=[];t.lostScans=[];t.desc=(descF()&&descF().value.trim())||'';}};
function li(a,b,c){return '<div class="li"><span>'+a+(c?'<br><small class="xs">'+c+'</small>':'')+'</span><span>'+b+'</span></div>';}
function nScans(t){const n=(t.scans||[]).length;return n?n+(n>1?' scans':' scan')+' ›':'None yet ›';}
function photoBox(t,locked){return img(t)+(locked?'<small>🔒 Locked during the return</small>':'<em class="ph-edit">'+(t.photo?'Edit photo':'Add a photo')+'</em>');}
const _bind6=bind;bind=function(){_bind6();const t=TAGS[CUR];if(!t)return;
 const dp=$('#detail .photo');dp.innerHTML=photoBox(t);dp.classList.add('editable');dp.setAttribute('role','button');
 const db=$('#detail .hdr .badge');if(db){db.textContent=t.fresh?'New':'Active';db.className='badge '+(t.fresh?'b-r':'b-n');}
 const hl=$('#detail [data-go=history] span:last-child');if(hl)hl.textContent=nScans(t);
 const ll=$('#locked [data-go=history] span:last-child');if(ll)ll.textContent=nScans(t);
 const ro=$('#detail [data-go=order] span');if(ro)ro.textContent=t.style==='Lock screen'?'Order a printed tag':'Order more copies';
 const hs=$('#history');hs.querySelector('.m').textContent=t.name+' · '+t.code;let hb=hs.querySelector('.hlist');if(!hb){hb=hs.querySelector('.m').nextElementSibling;hb.classList.add('hlist');}
 hb.innerHTML=(t.scans||[]).length?t.scans.map(s=>li(s[0],s[1],s[2])).join(''):'<p class="note info">No scans yet. Test it: open QR code and test scan, then scan it with another phone.</p>';
 const sc=$('#scans');let sp=sc.querySelector('.photo');if(!sp){sp=document.createElement('div');sp.className='photo sm editable';sp.setAttribute('role','button');sc.querySelector('.ttl').before(sp);}sp.innerHTML=photoBox(t);
 const sl=sc.querySelector('.ttl').nextElementSibling.nextElementSibling;sl.classList.add('slist');const L=t.lostScans||[];
 sl.innerHTML=L.length?L.map(s=>li(s[0],s[1])).join(''):'<p class="note info">No scans since you marked it lost. We alert you the moment someone scans it.</p>';
 const lr=sc.querySelector('.lockrow');if(lr)lr.textContent='📷 You can still update the name and photo. A clear, recent photo helps finders.';
 const lp=$('#locked .photo');if(lp)lp.innerHTML=photoBox(t,true);};
// photos everywhere the item appears (My tags, Messages)
const _rt6=renderTags;renderTags=function(){_rt6();all('#inbox .item').forEach(el=>{const b=el.querySelector('b');if(!b)return;if(!el.dataset.tk){const f=TAGS.find(x=>x.name===b.textContent);if(f)el.dataset.tk=f.code;}const t=TAGS.find(x=>x.code===el.dataset.tk);if(!t)return;b.textContent=t.name;el.querySelector('.ic').innerHTML=img(t);});};
// a tag a finder reports gets its own conversation in Messages
function inboxAdd(t){if([...all('#inbox .item b')].some(b=>b.textContent===t.name))return;const el=document.createElement('div');el.className='item';el.dataset.go='thread';el.innerHTML='<span class="ic">'+img(t)+'</span><span class="tx"><b></b><span>With me · Darmstadt Hbf, Lost &amp; Found desk</span></span><span class="unread">1</span>';el.querySelector('b').textContent=t.name;el.dataset.tk=t.code;$('#inbox h1').after(el);}

// ---- 3. orders: full lifecycle (SYSTEM-LOGIC 3)
var STG=['Paid','Sent to print','Printing','Quality check','Shipped','Out for delivery','Delivered'];
var PLAN=[0,0,1,2,3,5,5];
var EXC={cancelled:['Cancelled','b-n','Cancelled before printing. Refunded to your payment method in 3 to 5 working days.'],
 reprint:['Reprinting','warnb','It failed our print check, so we’re printing it again. About 2 days extra, no cost to you.'],
 delayed:['Delayed','warnb','The carrier is running late. New estimate below.'],
 failed:['Delivery failed','b-l','The carrier couldn’t deliver it and is returning it to us. Check your address and we’ll send it again for free.'],
 problem:['Replacement on its way','warnb','Sorry about that. A free replacement is being printed. You don’t need to send anything back.']};
var OSEL=null;
function dt(o,off){const d=new Date(2026,10,12-(o.ago||0)+off);return d.getDate()+' '+['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'][d.getMonth()];}
function oLabel(o){return o.exc?EXC[o.exc][0]:STG[o.k];}
function oCls(o){return o.exc?EXC[o.exc][1]:o.k===6?'b-n':'b-r';}
function oExtra(o){return (o.exc==='reprint'||o.exc==='delayed'||o.exc==='failed'||o.exc==='problem')?2:0;}
ORDERS=[{id:10482,e:'🏷️',t:'2 × sticker',q:2,style:'Sticker',col:'Mint',for:'Black backpack',ago:2,k:2,total:7.30,pay:'Apple Pay',addr:'Alex Mensah, Musterstraße 1, 64283 Darmstadt',exc:null},
 {id:10311,e:'🔑',t:'1 × keychain',q:1,style:'Keychain',col:'Ink',for:'House keys',ago:15,k:6,total:10.40,pay:'Card',addr:'Alex Mensah, Musterstraße 1, 64283 Darmstadt',exc:null}];
addOrder=function(t,e){const d=st();const gift=/^Gift/.test(t);const tot=(($('#checkout .paybtn')||{}).textContent||'').match(/€([\d.]+)/);
 const sa=$('#order .saved-addr');const addr=gift?(()=>{const v=[...all('#gift-delivery input')].map(i=>i.value.trim());return [v[0],v[1],[v[2],v[3]].filter(Boolean).join(' ')].filter(Boolean).join(', ')||'Gift recipient';})():(sa&&!sa.hidden?sa.querySelector('b').textContent+', '+sa.querySelector('.a-line').textContent:($('#checkout .a-name').textContent+', '+$('#checkout .a-line').textContent));
 const EM={'Sticker':'🏷️','Keychain':'🔑','Pet tag':'🐾','Luggage label':'🧳'};ORDERS.unshift({id:NEXTO,e:gift?e:(EM[d.style]||e),t:t,q:gift?1:+$('#order .step i').textContent,style:gift?t.replace(/^Gift · /,'').replace(/^./,c=>c.toUpperCase()):d.style,col:colName(d.col),for:gift?'a gift':d.blank?'blank, set up when it arrives':(d.name||'your item'),ago:0,k:0,total:tot?+tot[1]:0,pay:typeof payWith!=='undefined'?payWith:'Card',addr:addr,exc:null,gift:gift,blank:!!d.blank});NEXTO++;};
renderOrders=function(){const s=$('#orders');s.querySelectorAll('.item').forEach(x=>x.remove());const a=s.querySelector('.two');
 ORDERS.forEach((o,i)=>{const el=document.createElement('div');el.className='item';el.dataset.oi=i;el.setAttribute('role','button');el.innerHTML='<span class="ic">'+o.e+'</span><span class="tx"><b></b><span></span></span><span class="badge '+oCls(o)+'">'+oLabel(o)+'</span><span class="chev">›</span>';el.querySelector('b').textContent=o.t;el.querySelector('.tx span').textContent='TK-'+o.id+' · '+(o.ago?dt(o,0):'today');s.insertBefore(el,a);});};
(function(){const s=document.createElement('section');s.className='scr';s.id='ord-view';s.innerHTML='<div class="sbar"><span>9:41</span><span>●●● ▮</span></div><div class="hdr"><span class="back" data-go="orders">‹ Orders</span><span></span></div><div class="ovb"></div>';$('#orders').after(s);})();
function orderView(){const o=OSEL;if(!o)return;const ex=oExtra(o);const eta=dt(o,PLAN[6]+ex);let h='';
 h+='<div class="row2"><h1 class="md">Order TK-'+o.id+'</h1><span class="badge '+oCls(o)+'">'+oLabel(o)+'</span></div>';
 h+='<p class="m">'+(o.exc==='cancelled'?'Cancelled on '+dt(o,o.k):o.k===6&&!o.exc?'Delivered on '+dt(o,PLAN[6]+ex):'Arrives by '+eta)+'</p>';
 if(o.exc)h+='<p class="note '+(o.exc==='failed'?'warn':'info')+'">'+EXC[o.exc][2]+'</p>';
 if(o.exc!=='cancelled')h+='<ol class="tl">'+STG.map((s,i)=>{const done=i<o.k||(i===o.k&&!['reprint','failed'].includes(o.exc));const now=i===o.k;
  const sub=done?dt(o,i<=1?0:PLAN[i]+(i>2?ex:0)):'Expected '+dt(o,PLAN[i]+ex);return '<li class="'+(done?'on':'')+(now?' now':'')+'"><b>'+s+(now&&o.exc&&o.exc!=='problem'?' · '+EXC[o.exc][0]:'')+'</b><small>'+sub+'</small></li>';}).join('')+'</ol>';
 h+='<div class="ocard"><span class="ic">'+o.e+'</span><span class="tx"><b>'+o.t.replace(/[<&]/g,'')+'</b><span>'+o.style+' · '+o.col+' · for '+String(o.for).replace(/[<&]/g,'')+'</span></span></div>';
 if(!o.gift)h+='<p class="xs">'+(o.blank?'Your blank tags are in My tags. Set each one up when it arrives.':'The code already works. This order is only the printed tag.')+'</p>';
 h+='<div class="li"><span>Deliver to</span><span class="oaddr">'+o.addr.replace(/[<&]/g,'')+'</span></div><div class="li"><span>Paid with '+o.pay+'</span><span>€'+o.total.toFixed(2)+'</span></div>';
 const A=[];if(!o.exc&&o.k<=1)A.push('<div class="btn sec" data-oa="addr">Change delivery address</div>','<div class="btn ghost lostt" data-oa="cancel">Cancel order</div>');
 else if(!o.exc&&o.k<=3)A.push('<div class="btn sec" data-oa="addr">Change delivery address</div><p class="xs center">You can change the address until it ships. Printing has started, so it can no longer be cancelled.</p>');
 if(o.k>=4&&o.k<=5&&o.exc!=='failed')A.push('<div class="btn sec" data-toast="Opens DHL tracking">Track parcel</div>');
 if(o.exc==='failed')A.push('<div class="btn pri" data-oa="resend">Check address and send again</div>');
 if(o.k===6&&!o.exc)A.push('<div class="btn sec" data-oa="problem">Report a problem</div>');
 A.push('<span class="link center" data-toast="Opens help: orders and delivery">Get help with this order</span>');
 h+=A.join('');
 if(o.exc!=='cancelled'&&!(o.k===6&&!o.exc))h+='<div class="demo"><span class="label2">Prototype only</span><div class="two"><div class="btn sec sm2" data-oa="next">Next stage</div><div class="btn sec sm2" data-oa="sim">Simulate a problem</div></div></div>';
 $('#ord-view .ovb').innerHTML=h;}
orderSheet=function(o){OSEL=o;show('ord-view');};
function oAdvance(o){if(o.exc==='failed'){toast('Waiting for you: check the address');return;}
 if(o.exc==='reprint'){o.exc=null;o.k=3;toast('Reprinted and checked');}
 else if(o.exc==='problem'){o.exc=null;o.k=6;toast('Replacement delivered');}
 else{if(o.exc==='delayed')o.exc=null;if(o.k<6)o.k++;toast(STG[o.k]);}
}
function oSim(o){if(o.k<=1){o.exc='reprint';o.k=Math.max(o.k,2);}else if(o.k<=3)o.exc='reprint';else if(o.k===4)o.exc='delayed';else if(o.k===5)o.exc='failed';toast(EXC[o.exc][0]);}

// ---- shared show() hook
const _show6=show;show=function(id){
 if(id==='order'&&D&&D.reorder&&!D.rt){const t=TAGS[CUR];D.rt=true;D.type=t.type||0;setDesign(t.style&&t.style!=='Lock screen'?t.style:shapesFor(D.type)[0]);}
 _show6(id);
 if(id==='type')typeFilter();
 if(id==='pick'){const b=st().blank;all('.gcard').forEach(g=>{const s=g.dataset.style;if(b)return;const ty=FIT[s];g.dataset.type=ty[0];g.dataset.go=ty.length>1?'type':DSCR[ty[0]];});
  let n=$('#pick .blanknote');if(!n){n=document.createElement('p');n.className='xs blanknote';$('#pick .gal').after(n);}n.hidden=!b;n.textContent='The lock-screen tag is digital and free, so there’s nothing to ship or set up later. Make it any time from Create a tag.';}
 if(['detail','scans','history','locked'].includes(id))bind();
 if(id==='orders')renderOrders();
 if(id==='inbox')renderTags();
 if(id==='ord-view')orderView();};

// ---- blank tags keep their shape; set-up only offers types that fit it
function setupBlank(i){const t=TAGS[i];CUR=i;SETUPI=i;blankDraft();D.setup=true;D.saved=true;setDesign(t.style||'Sticker');const ok=FIT[t.style]||[0];D.type=ok[0];SELT=ok[0];SELS=t.style;H=[];CURS='tags';
 if(ok.length>1){_show2('type');typeFilter();}else _show2(DSCR[ok[0]]);
 toast('Set up '+t.code+(ok.length>1?': what will it go on?':': add the details'));}
window.addEventListener('click',e=>{const q=s=>e.target.closest(s);
 const ti=q('#tags [data-ti]');if(ti){const i=+ti.dataset.ti,t=TAGS[i];if(t&&t.st==='unset'&&!q('[data-qr]')){e.stopImmediatePropagation();if(q('.more')){quickSheet(i);return;}setupBlank(i);return;}}
 const qs=q('[data-q=setup]');if(qs){e.stopImmediatePropagation();ovClose();setupBlank(CUR);return;}
 if(q('#act-live .next-blank')){e.stopImmediatePropagation();const i=TAGS.findIndex(t=>t.st==='unset');if(i>=0)setupBlank(i);return;}
 const mn=q('#message .btn.pri');if(mn&&D&&D.setup&&SETUPI!==null){const t=TAGS[SETUPI];t.type=D.type;t.scans=[];t.lostScans=[];}
},true);
const _qs6=quickSheet;quickSheet=function(i){const t=TAGS[i];if(t&&t.st==='unset'){CUR=i;ov('<h2>'+t.code+'</h2><p class="m">Blank '+String(t.style).toLowerCase()+' · not linked to anything yet</p><div class="btn pri" data-q="setup">Set up this tag</div><div class="btn sec" data-q="qr">Show QR code</div><div class="btn ghost" data-ph="close">Cancel</div>');return;}_qs6(i);};

document.addEventListener('click',e=>{const q=s=>e.target.closest(s);
 if(q('#detail .photo.editable,#scans .photo.editable')){e.stopImmediatePropagation();EDITT=null;editSheet();return;}
 if(q('#locked .photo')){toast('Locked until the return ends');return;}
 if(q('#confirm .btn.lostb')){const t=TAGS[CUR];t.lostScans=[];t.fresh=false;}
 if(q('#scans .proto')){const t=TAGS[CUR];(t.scans=t.scans||[]).unshift(['Today, just now','Darmstadt','Report sent · with finder']);t.lostScans.unshift(['Today, just now','Darmstadt']);inboxAdd(t);}
 const sw=q('#qr .testbox .sw');if(sw){const t=TAGS[CUR];if(!sw.classList.contains('on')&&t){(t.scans=t.scans||[]).unshift(['Today, just now','Darmstadt','Test scan · no alert sent']);setTimeout(()=>toast('Test mode on for 10 minutes'),0);}}
 const oa=q('[data-oa]');if(oa&&OSEL){const o=OSEL,a=oa.dataset.oa;
  if(a==='next')oAdvance(o);if(a==='sim')oSim(o);
  if(a==='cancel'){ov('<h2>Cancel order TK-'+o.id+'?</h2><p class="m">Printing hasn’t started, so you get a full refund. '+(o.blank?'The blank tags are removed from My tags.':'Your tag stays in My tags, so you can order the print again later.')+'</p><div class="btn lostb" data-oa="cancel-yes">Cancel order</div><div class="btn sec" data-ph="close">Keep order</div>');return;}
  if(a==='cancel-yes'){o.exc='cancelled';ovClose();if(o.blank){TAGS=TAGS.filter((t,k)=>!(t.st==='unset'&&k<o.q));}toast('Order cancelled. Refund on its way.');}
  if(a==='addr'||a==='resend'){ov('<h2>Delivery address</h2><input class="in" id="oa-in" aria-label="Address"><div class="btn pri" data-oa="addr-save">'+(a==='resend'?'Send again':'Save address')+'</div><div class="btn ghost" data-ph="close">Cancel</div>');$('#oa-in').value=o.addr;OSEL._rs=a==='resend';return;}
  if(a==='addr-save'){const v=$('#oa-in').value.trim();if(v.length<8){toast('Enter the full address');return;}o.addr=v;ovClose();if(o._rs){o.exc=null;o.k=4;o._rs=false;toast('Sent again. New tracking by email.');}else toast('Address updated');}
  if(a==='problem'){ov('<h2>What went wrong?</h2><div class="grp">'+['Arrived damaged','Never arrived','Wrong colour or size','The QR won’t scan'].map(x=>'<div class="opt" data-oa="prob-pick"><span class="r"></span><span>'+x+'</span></div>').join('')+'</div><div class="btn ghost" data-ph="close">Cancel</div>');return;}
  if(a==='prob-pick'){o.exc='problem';o.k=4;ovClose();toast('Free replacement on its way');}
  renderOrders();orderView();return;}
},true);
"""

CSS7 = r"""
.grp .opt[hidden],.blanknote[hidden]{display:none}
.photo.editable{position:relative;cursor:pointer}
.photo .ph-edit{position:absolute;right:10px;bottom:10px;font:600 12px var(--tk-font-body);font-style:normal;background:rgb(0 0 0 / .55);color:#fff;padding:4px 10px;border-radius:99px}
#ord-view .ovb{display:flex;flex-direction:column;gap:12px}
#ord-view .row2{display:flex;align-items:center;justify-content:space-between;gap:10px}#ord-view h1{margin:0}
#ord-view .tl li{padding-bottom:9px;display:flex;justify-content:space-between;align-items:baseline;gap:8px}#ord-view .tl li::after{top:17px}#ord-view .tl b{font-size:14px}#ord-view .tl li.now b{color:var(--tk-ink)}
#ord-view .ocard{display:flex;gap:12px;align-items:center;border:1px solid var(--tk-line);border-radius:var(--tk-radius-md);padding:10px 12px}
#ord-view .ocard .ic{font-size:24px}#ord-view .ocard b{display:block}#ord-view .ocard .tx span{font-size:13px;color:var(--tk-ink-2)}
#ord-view .oaddr{text-align:right;max-width:60%}
#ord-view .lostt{color:var(--tk-lost-text)}
#ord-view .demo{border:1px dashed var(--tk-line);border-radius:var(--tk-radius-md);padding:10px;display:flex;flex-direction:column;gap:8px}
#ord-view .sm2{min-height:40px;font-size:14px}
#orders .chev{color:var(--tk-ink-2);font-size:18px;margin-left:4px}
"""
