"""Prototype behaviour added on top of build_screens.py (12 Nov 2026 review).

CSS2 is shared by the hand-off file and both prototypes. OWNER_JS and FINDER_JS run after the
original prototype scripts and replace show(), setDesign() and updateTotal() there.
"""

CZ_COLS = [("Mint", "#00c48c"), ("Ink", "#0b1712"), ("White", "#ffffff"), ("Sand", "#e9dcc3"),
           ("Sunny", "#ffd23f"), ("Coral", "#ff7a6b"), ("Sky", "#6ec6ff"), ("Lilac", "#b9a6ff"),
           ("Aura", "linear-gradient(135deg,#b9a6ff,#6ec6ff)"), ("Sunset", "linear-gradient(135deg,#ffd23f,#ff7a6b)")]

CSS2 = r"""
.logo,.brand b,.splash b{font-family:var(--tk-font-brand)}
h1{font-weight:650;letter-spacing:-.025em}
.btn{border-radius:999px;letter-spacing:-.005em}
.in,textarea.in{border-radius:14px}
.opt{border-radius:16px}
.m{font-size:15px;line-height:1.45}
.label2{letter-spacing:.06em;font-size:11px}
.lp-img{font-size:22px;background:var(--tk-sunken);border:0;overflow:hidden}
.lp-img img,.ic img,.photo img{width:100%;height:100%;object-fit:cover;border-radius:inherit}
.item .ic,.photo{overflow:hidden}
.ph-pick{cursor:pointer;text-align:center}
.pm-wrap.sm{position:relative;display:block}
.pm-wrap.sm .pm{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%) scale(.5)}
.pm.pet .pmk,.pm.lock .pmk{display:block}
.pm.pet .pmb{gap:2px;width:118px;height:118px}.pm.pet .pmb .qr{width:52px;height:52px;background-size:6.5px 6.5px}
.pm.lock .pmb .pmk{width:14px;height:14px}
.pml{font:800 9px/1 var(--tk-font-body);letter-spacing:.12em;text-transform:uppercase;color:var(--fg,#0b1712)}.pml:empty{display:none}
.pm.sz-s{transform:scale(.82)}.pm.sz-l{transform:scale(1.12)}
.pm.f-gloss{background:linear-gradient(155deg,rgb(255 255 255 / .55),transparent 42%),var(--c)}
.pm.f-holo{background:linear-gradient(115deg,rgb(255 255 255 / .5),rgb(185 166 255 / .55) 30%,rgb(110 198 255 / .5) 50%,rgb(255 210 63 / .5) 70%,rgb(255 255 255 / .5)),var(--c)}
.pm.f-glow{box-shadow:0 0 0 3px rgb(160 255 210 / .8),0 0 28px 8px rgb(80 255 180 / .45)}
.pm.f-reflective{background:repeating-linear-gradient(135deg,rgb(255 255 255 / .35) 0 4px,transparent 4px 9px),var(--c)}
.pm-wrap.cz{height:150px;min-height:0;overflow:hidden}
.pm-wrap.cz .pm{transform:scale(.7)}.pm-wrap.cz .pm.sz-s{transform:scale(.58)}.pm-wrap.cz .pm.sz-l{transform:scale(.82)}
#design,#order{gap:10px}#design .pm-spec{font-size:13px;margin:-2px 0 0}#design .xs{margin:0}
.czr{display:flex;flex-direction:column;gap:6px;flex:none}.czr[hidden]{display:none}
.czr .label2 small{text-transform:none;letter-spacing:0;font-weight:500}
.scrollx{flex-wrap:nowrap;overflow-x:auto;justify-content:flex-start;scrollbar-width:none;padding:3px 3px 5px}.scrollx::-webkit-scrollbar{display:none}
.chips .chip[hidden],.seg span[hidden]{display:none}
.scrollx .chip{white-space:nowrap}
.in.sm{min-height:44px}
.grp.cmp .two .sel{flex:0 0 38%}.grp.cmp{gap:8px}.grp.cmp .in{min-height:46px}
.ord-for{color:var(--tk-ink-2);font-size:12px}
.rowr{display:flex;justify-content:flex-end;margin-top:8px}.btn.sm{min-height:42px;padding:0 22px;font-size:15px;display:inline-flex}
.sheet{position:fixed;inset:0;background:rgb(0 0 0 / .45);display:flex;align-items:flex-end;justify-content:center;z-index:20;padding:12px}
.sheet[hidden],#f-repmore[hidden],#ro-more[hidden],#f-hdone[hidden],#f-hcheck[hidden]{display:none}
.sheet-c{background:var(--tk-surface);border-radius:28px;padding:28px 22px 22px;width:100%;max-width:400px;display:flex;flex-direction:column;gap:12px;text-align:center;animation:up var(--tk-slow) var(--tk-ease)}
.sheet-c h2{font:650 22px/1.2 var(--tk-font-display);letter-spacing:-.02em;margin:0}
@keyframes up{from{transform:translateY(24px);opacity:0}}
"""

OWNER_JS = r"""
var D,H,CURS,NB=false,TAGS,CUR=0;
var ROOTS=['tags','inbox','orders','account','launch1','start','e-tags','e-inbox','e-orders','err-offline'];
var TERM=['ordered','gift-sent','live','act-live','deleted','report-done','perm-notif'];
var AUTH=['launch3','code','signin'];
var SZ={'Sticker':{S:['38 mm round',3.90],M:['50 mm round',4.90],L:['70 mm round',6.40]},'Keychain':{M:['30 × 45 mm acrylic',9.90]},'Pet tag':{S:['25 mm disc',11.90],M:['32 mm disc',12.90],L:['38 mm disc',13.90]},'Luggage label':{M:['55 × 90 mm with strap',11.90]},'Lock screen':{M:['phone lock screen · digital',0]}};
var FIN={'Sticker':['Matte','Gloss','Holo','Glow'],'Keychain':['Gloss','Holo','Glow'],'Pet tag':['Matte','Gloss','Glow'],'Luggage label':['Matte','Gloss','Reflective'],'Lock screen':[]};
var FINP={Matte:0,Gloss:0,Holo:1,Glow:1.5,Reflective:1};
var CLS={'Sticker':'sticker','Keychain':'keychain','Pet tag':'pet','Luggage label':'luggage','Lock screen':'lock'};
var EMO=['🎒','🧳','🐾'];
function st(){if(!D)D={type:0,name:'Black backpack',photo:null,msgEdited:false,style:'Sticker',col:'#00c48c',size:'M',fin:'Matte',label:'',saved:false};return D;}
function colName(c){const s=[...all('#design .swc')].find(x=>x.dataset.c===c);return s?s.title:'Mint';}
function itemEmo(d){return d.style==='Lock screen'&&d.type===0?'📱':EMO[d.type];}
function MSG(d){return d.type===2?'Hi, I’m '+(d.name||'your pet')+'. Please message my family. I may be scared.':d.type===1?'I’m travelling. Please hand me to airline or hotel staff, or message my owner.':'Found me? Thank you! Tap below to tell my owner where I am.';}
function unitPrice(){const d=st();const s=SZ[d.style][d.size]||SZ[d.style].M;return s[1]?s[1]+(FINP[d.fin]||0):0;}
function setDesign(stl,col){const d=st();if(stl){d.style=stl;if(!SZ[stl][d.size])d.size='M';if(!FIN[stl].includes(d.fin))d.fin=FIN[stl][0]||'';}if(col)d.col=col;render();}
function render(){const d=st();const nf=[$('#it-name'),$('#t-name'),$('#p-name')][d.type];if(nf)d.name=nf.value.trim();
 const sizes=Object.keys(SZ[d.style]);const sz=SZ[d.style][d.size]||SZ[d.style].M;const u=unitPrice();const fins=FIN[d.style];
 all('#design .styles .chip').forEach(c=>c.classList.toggle('on',c.textContent===d.style));
 $('#design .cz-size').hidden=sizes.length<2;all('#design .sizes span').forEach(x=>{x.hidden=!sizes.includes(x.dataset.s);x.classList.toggle('on',x.dataset.s===d.size);});
 $('#design .cz-fin').hidden=!fins.length;all('#design .fins .chip').forEach(x=>{x.hidden=!fins.includes(x.dataset.f);x.classList.toggle('on',x.dataset.f===d.fin);});
 all('#design .swc').forEach(x=>x.classList.toggle('on',x.dataset.c===d.col));
 const fg=d.col==='#0b1712'?'#ffffff':'#0b1712';
 all('#design .pm,#order .pm').forEach(m=>{const mini=m.classList.contains('mini');m.className='pm '+CLS[d.style]+(mini?' mini':' sz-'+d.size.toLowerCase())+(d.fin?' f-'+d.fin.toLowerCase():'');m.style.setProperty('--c',d.col);m.style.setProperty('--fg',fg);const l=m.querySelector('.pml');if(l)l.textContent=d.label;});
 $('#design .pm-spec').textContent=d.style+(sizes.length>1?' · '+d.size:'')+' · '+sz[0]+(d.fin?' · '+d.fin:'')+(u?' · €'+u.toFixed(2):' · free');
 const lock=d.style==='Lock screen';const b=$('#design .btn.pri');b.dataset.go=lock?'live':'order';b.textContent=lock?'Make it live':'Continue to order';
 $('#order .ord-name').textContent=d.style+' · '+colName(d.col);$('#order .ord-spec').textContent=(sizes.length>1?d.size+' · ':'')+sz[0]+(d.fin?' · '+d.fin:'')+' · €'+u.toFixed(2)+' each';$('#order .ord-for').textContent='For: '+(d.name||'your item');
 all('.lp-style').forEach(x=>x.textContent=d.style);all('.lp-name').forEach(x=>x.textContent=d.name||'Your item');
 all('.lp-img').forEach(x=>{x.innerHTML=d.photo?'<img alt="" src="'+d.photo+'">':itemEmo(d);});
 const m=$('#it-msg');if(!d.msgEdited){m.value=MSG(d);$('#it-count').textContent=m.value.length+' / 160';}
 all('.lp-msg').forEach(x=>x.textContent=m.value);
 const an=$('.act-name');if(an)an.textContent=d.name;
 updateTotal(u);}
function updateTotal(u){if(u!==undefined)unit=u;const d=st();const q=+$('#order .step i').textContent;const name=d.style+' ('+colName(d.col).toLowerCase()+')';const ship=unit*q>=15?0:2.5;const sub=unit*q,tot=Math.max(0,sub+ship-2);
 const rows=$('#checkout').querySelectorAll('.li');rows[0].innerHTML='<span>'+name+' × '+q+'</span><span>€'+sub.toFixed(2)+'</span>';rows[1].innerHTML='<span>Shipping to Germany</span><span>'+(ship?'€2.50':'Free')+'</span>';rows[3].innerHTML='<span>Total</span><span>€'+tot.toFixed(2)+'</span>';
 $('#checkout .paybtn').textContent='Pay €'+tot.toFixed(2)+' with '+payWith;$('#ordered .xs').textContent='Order TK-10482 · '+q+' × '+d.style.toLowerCase()+' for '+(d.name||'your item');}
function newCode(){const A='23456789ABCDEFGHJKMNPQRSTVWXYZ';const p=()=>Array.from({length:4},()=>A[Math.floor(Math.random()*A.length)]).join('');return 'TK-'+p()+'-'+p();}
function tagsInit(){TAGS=[{name:'Black backpack',e:'🎒',code:'TK-7Q4M-9XRA',st:'normal'},{name:'Milo',e:'🐾',code:'TK-M3PF-2KWD',st:'lost'},{name:'Blue suitcase',e:'🧳',code:'TK-H8RC-4TNE',st:'return',sub:' · trip ends 20 Nov'}];}
function addTag(){const d=st();if(d.saved)return;d.saved=true;TAGS.unshift({name:d.name||'My tag',e:itemEmo(d),photo:d.photo,code:newCode(),st:'normal',fresh:true});CUR=0;}
function badge(t){return t.st==='lost'?'<span class="badge b-l">Lost</span>':t.st==='return'?'<span class="badge b-r">Return active</span>':t.ret?'<span class="badge b-r">Returned</span>':t.fresh?'<span class="badge b-r">New</span>':'<span class="badge b-n">Active</span>';}
function img(t){return t.photo?'<img alt="" src="'+t.photo+'">':t.e;}
function renderTags(){const s=$('#tags');s.querySelectorAll('.item').forEach(x=>x.remove());const anchor=s.querySelector('p.xs');
 TAGS.forEach((t,i)=>{const el=document.createElement('div');el.className='item';el.dataset.ti=i;el.innerHTML='<span class="ic">'+img(t)+'</span><span class="tx"><b></b><span></span></span>'+badge(t)+'<span class="qrb" data-qr aria-label="Show QR code"><svg width="20" height="20"><use href="#i-qr"/></svg></span>';el.querySelector('b').textContent=t.name;el.querySelector('.tx span').textContent=t.code+(t.sub||'');s.insertBefore(el,anchor);});}
function idx(n){const i=TAGS.findIndex(t=>t.name===n);return i<0?0:i;}
function bind(){const t=TAGS[CUR];if(!t)return;const n=t.name;const set=(s,v)=>{const e=$(s);if(e)e.textContent=v;};
 set('#detail h1',n);$('#detail .photo').innerHTML=img(t);set('#detail .hdr .badge','Active');
 set('#confirm h1','Mark '+n+' as lost?');set('#scans .ttl',n);set('#locked h1',n);$('#locked .photo').innerHTML=img(t)+'<small>🔒 Locked during the return</small>';
 set('#qr h1',n);set('#qr .bigqr small','tagkin.app · '+t.code);set('#history .m',n+' · '+t.code);set('#retire .m',n+' · '+t.code);set('#alert .notif b','Someone found '+n);all('.ro-name').forEach(x=>x.textContent=n);}
function show(id){H=H||[];if(CURS&&id!==CURS&&!NB){if(ROOTS.includes(id)||TERM.includes(id))H=[];else if(H[H.length-1]===id)H.pop();else{H.push(CURS);if(CURS==='code')H=H.filter(x=>!AUTH.includes(x));}}
 NB=false;CURS=id;all('.stage .scr').forEach(x=>x.classList.toggle('on',x.id===id));window.scrollTo(0,0);onShow(id);}
function onShow(id){if(['ordered','live','act-live'].includes(id))addTag();
 if(id==='tags'){renderTags();}
 if(TERM.includes(id))all('#'+id+' .back').forEach(b=>b.style.visibility='hidden');
 if(['details','message','design','order','checkout'].includes(id))render();
 if(id==='checkout'){$('#checkout .a-name').textContent=$('#d-name').value;$('#checkout .a-line').textContent=$('#d-street').value+', '+$('#d-zip').value+' '+$('#d-city').value+', Germany';}
 if(id==='report-owner'){all('#ro-opts .opt').forEach((o,i)=>o.classList.toggle('on',i===0));$('#ro-more').hidden=true;$('#ro-go').textContent='Block finder';window.RO=false;}
 if(id==='report-done'){$('#rd-t').textContent=window.RO?'Thanks for reporting':'Finder blocked';$('#rd-m').textContent=window.RO?'We’ll review this message. If it breaks our rules, we’ll act on it. The finder won’t know you reported them.':'They can no longer message you about this tag. We review every report.';}}
document.addEventListener('click',e=>{
 const b=e.target.closest('.back');if(b){e.stopImmediatePropagation();e.preventDefault();H=H||[];if(H.length){NB=true;show(H.pop());}else show(signedIn?'tags':'start');return;}
 if(e.target.closest('[data-start]')){H=[];CURS=null;}
 const ti=e.target.closest('[data-ti]');if(ti){CUR=+ti.dataset.ti;bind();const t=TAGS[CUR];show(e.target.closest('[data-qr]')?'qr':t.st==='lost'?'scans':t.st==='return'?'locked':'detail');return;}
 const ib=e.target.closest('#inbox .item');if(ib){CUR=idx(ib.querySelector('b').textContent);bind();}
 const ty=e.target.closest('#type .grp .opt');if(ty){st().type=[...ty.parentElement.children].indexOf(ty);}
 const gc=e.target.closest('.gcard');if(gc){st().type=+gc.dataset.type;}
 const sz=e.target.closest('#design .sizes span');if(sz){st().size=sz.dataset.s;render();}
 const fi=e.target.closest('#design .fins .chip');if(fi){st().fin=fi.dataset.f;render();}
 if(e.target.closest('#confirm .btn.lostb')){TAGS[CUR].st='lost';TAGS[CUR].ret=false;}
 if(e.target.closest('#scans .btn.pri')){TAGS[CUR].st='normal';TAGS[CUR].ret=false;toast('Marked as found');}
 if(e.target.closest('#scans .proto')){TAGS[CUR].st='return';}
 if(e.target.closest('#safe .btn.pri')){CUR=idx('Black backpack');}
 if(e.target.closest('#returned .btn.pri')){TAGS[CUR].st='normal';TAGS[CUR].ret=true;}
 if(e.target.closest('#retire .btn.lostb')){TAGS.splice(CUR,1);CUR=0;}
 const ro=e.target.closest('#ro-opts .opt');if(ro){window.RO=[...ro.parentElement.children].indexOf(ro)===1;$('#ro-more').hidden=!window.RO;$('#ro-go').textContent=window.RO?'Report message':'Block finder';}
},true);
document.addEventListener('input',e=>{const id=e.target.id;
 if(['it-name','t-name','p-name'].includes(id))render();
 if(id==='it-msg')st().msgEdited=true;
 if(id==='cz-label'){const v=e.target.value;if(/\d{5,}|@/.test(v)){e.target.value='';toast('Labels can’t include phone numbers or emails');}st().label=e.target.value;render();}});
document.addEventListener('change',e=>{if(e.target.classList.contains('ph-in')&&e.target.files[0]){const r2=new FileReader();r2.onload=()=>{st().photo=r2.result;e.target.parentElement.querySelector('span').textContent='✓ Photo added · tap to change';render();};r2.readAsDataURL(e.target.files[0]);}});
"""
OWNER_INIT = "tagsInit();setDesign('Sticker');show('launch1');"

FINDER_JS = r"""
var H,CURS,NB=false,RET=false,RETTAG=null,MINE=false,TRIES=5;
var FROOTS=['f-code','f-msg','f-thanks','f-handed','f-retired','f-new'];
function show(id){H=H||[];if(CURS&&id!==CURS&&!NB){if(FROOTS.includes(id))H=[];else if(H[H.length-1]===id)H.pop();else H.push(CURS);}
 NB=false;CURS=id;all('.stage .scr').forEach(x=>x.classList.toggle('on',x.id===id));window.scrollTo(0,0);
 if(id==='f-handover')hreset();if(id==='f-report')repReset();}
const _scan=scan;scan=function(v){_scan(v);const f=$('#f-found');
 if(RET&&v===RETTAG){$('#f-banner').innerHTML='<div class="note okn">✓ Reported found · the owner is arranging to collect it</div>';
  $('#f-extra').innerHTML='<div class="btn pri" data-go="f-handover">Check a handover code</div>'+(MINE?'<div class="btn sec" data-go="f-thanks">Continue my report</div>':'<p class="xs">Reported this yourself on another device? Open the link we emailed or texted you.</p>');
  f.className='btn ghost';f.textContent='I have this item now';}
 else{f.className='btn pri';}};
const _finish=finish;finish=function(a){_finish(a);if(cur!=='test'){RET=true;RETTAG=cur;MINE=true;}
 $('#f-savenote').textContent=a?'You stayed anonymous: save this link to come back. Without it, scan the tag again to check the handover code.':(ch==='email'?'We also emailed you this link.':'We also texted you this link.');};
function hreset(){$('#f-hcode').value='';$('#f-hok').hidden=true;$('#f-hbad').hidden=true;$('#f-hdone').hidden=true;$('#f-hcheck').hidden=false;}
function repReset(){all('#f-rep .opt').forEach(o=>o.classList.remove('on'));$('#f-repmore').hidden=true;$('#f-reptext').value='';$('#f-repsend').classList.add('off');$('#f-sheet').hidden=true;}
function repOk(){const i=[...all('#f-rep .opt')].findIndex(x=>x.classList.contains('on'));$('#f-repsend').classList.toggle('off',i<0||(i===2&&!$('#f-reptext').value.trim()));}
document.addEventListener('click',e=>{
 const b=e.target.closest('.back');if(b){e.stopImmediatePropagation();e.preventDefault();H=H||[];if(H.length){NB=true;show(H.pop());}else show('f-msg');return;}
 if(e.target.closest('[data-newdev]')){MINE=false;scan(RETTAG||'item');e.stopImmediatePropagation();return;}
 if(e.target.closest('#f-hcheck')){e.stopImmediatePropagation();if(TRIES<=0){toast('Too many tries. Wait 15 minutes.');return;}
  const ok=$('#f-hcode').value.replace(/\s/g,'')==='739204';
  if(ok){$('#f-hok').hidden=false;$('#f-hbad').hidden=true;$('#f-hdone').hidden=false;$('#f-hcheck').hidden=true;}
  else{TRIES--;$('#f-hbad').hidden=false;$('#f-hbad').textContent=TRIES?'That code doesn’t match. Don’t hand it over. '+TRIES+' tries left.':'Too many tries. Wait 15 minutes, and ask the owner to open their handover code in the app.';}return;}
 if(e.target.closest('#f-hdone')){RET=false;TRIES=5;show('f-handed');return;}
 if(e.target.closest('#f-save')){try{navigator.clipboard.writeText('https://tagkin.app/r/demo-report');}catch(_){}toast('Link copied');}
},true);
document.addEventListener('click',e=>{
 if(e.target.closest('#f-rep .opt')){const i=[...all('#f-rep .opt')].findIndex(x=>x.classList.contains('on'));$('#f-repmore').hidden=false;$('#f-reptext').placeholder=i===2?'Tell us what’s wrong (required)':'Add details (optional)';repOk();}
 if(e.target.closest('#f-repsend')&&!$('#f-repsend').classList.contains('off'))$('#f-sheet').hidden=false;
 if(e.target.closest('#f-sheetok')){$('#f-sheet').hidden=true;H=H||[];const prev=H.length?H.pop():'f-msg';NB=true;show(prev);toast('Report sent');}
});
document.addEventListener('input',e=>{if(e.target.id==='f-reptext')repOk();});
scan('item');
"""

MOCK_JS = r"""
function hexes(c){return (c.match(/#[0-9a-f]{6}/gi)||[c]);}
function qr(x,y,s,seed){let p='',r=seed||7;const m=s/25;
 for(let j=0;j<21;j++)for(let i=0;i<21;i++){const ii=i>13?i-14:i,jj=j>13?j-14:j;const fin=(i<7&&j<7)||(i>13&&j<7)||(i<7&&j>13);let on;
  if(fin)on=ii===0||ii===6||jj===0||jj===6||(ii>=2&&ii<=4&&jj>=2&&jj<=4);else{r=(r*1103515245+12345)&0x7fffffff;on=(r>>16)&1;}
  if(on)p+='M'+(x+(i+2)*m).toFixed(2)+' '+(y+(j+2)*m).toFixed(2)+'h'+m.toFixed(2)+'v'+m.toFixed(2)+'h-'+m.toFixed(2)+'z';}
 return '<rect x="'+x+'" y="'+y+'" width="'+s+'" height="'+s+'" rx="'+(s*.07)+'" fill="#fff"/><path d="'+p+'" fill="#0b1712"/>';}
function seedOf(s){let h=0;for(const ch of s)h=(h*31+ch.charCodeAt(0))|0;return Math.abs(h)||7;}
function mock(d,code,uid){const u='m'+uid,h=hexes(d.col),c1=h[0],c2=h[1]||h[0],fg=d.col==='#0b1712'?'#ffffff':'#0b1712';
 const k={S:.82,M:.92,L:1}[d.size]||.92,fin=(d.fin||'').toLowerCase(),seed=seedOf(code);
 const defs='<defs><linearGradient id="'+u+'f" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="'+c1+'"/><stop offset="1" stop-color="'+c2+'"/></linearGradient>'
  +'<linearGradient id="'+u+'met" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#f4f6f7"/><stop offset=".45" stop-color="#9aa3a8"/><stop offset=".55" stop-color="#d9dee0"/><stop offset="1" stop-color="#6d767b"/></linearGradient>'
  +'<linearGradient id="'+u+'holo" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".6"/><stop offset=".3" stop-color="#b9a6ff" stop-opacity=".55"/><stop offset=".5" stop-color="#6ec6ff" stop-opacity=".5"/><stop offset=".7" stop-color="#ffd23f" stop-opacity=".5"/><stop offset="1" stop-color="#fff" stop-opacity=".6"/></linearGradient>'
  +'<pattern id="'+u+'refl" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="3" height="8" fill="#fff" opacity=".35"/></pattern>'
  +'<filter id="'+u+'sh" x="-30%" y="-30%" width="160%" height="160%"><feDropShadow dx="0" dy="6" stdDeviation="6" flood-color="#000" flood-opacity=".35"/></filter>'
  +'<filter id="'+u+'glow" x="-40%" y="-40%" width="180%" height="180%"><feDropShadow dx="0" dy="0" stdDeviation="7" flood-color="#5dffb8" flood-opacity=".9"/></filter></defs>';
 const F='url(#'+u+'f)',flt=fin==='glow'?'url(#'+u+'glow)':'url(#'+u+'sh)';
 const over=(shape)=>(fin==='holo'?shape.replace('FILL','url(#'+u+'holo)'):'')+(fin==='reflective'?shape.replace('FILL','url(#'+u+'refl)'):'');
 const logo=(x,y,s)=>'<svg x="'+x+'" y="'+y+'" width="'+s+'" height="'+s+'" style="color:'+fg+'"><use href="#mark"/></svg>';
 const txt=(x,y,t,sz,w)=>'<text x="'+x+'" y="'+y+'" text-anchor="middle" font-family="Geist,system-ui,sans-serif" font-size="'+sz+'" font-weight="'+(w||700)+'" letter-spacing=".08em" fill="'+fg+'">'+t.replace(/[<&]/g,'')+'</text>';
 const lab=(d.label||'').toUpperCase();let bg='',body='';
 if(d.style==='Sticker'){const R=66*k;bg='<rect width="200" height="200" fill="#2a2e33"/><rect width="200" height="200" fill="url(#'+u+'lap)"/><linearGradient id="'+u+'lap" x2="0" y2="1"><stop offset="0" stop-color="#4a4f56"/><stop offset="1" stop-color="#1f2226"/></linearGradient><path d="M0 40 L200 10 L200 14 L0 44Z" fill="#fff" opacity=".05"/>';
  const sh='<circle cx="100" cy="100" r="'+R+'" fill="FILL"/>';
  body='<g filter="'+flt+'"><circle cx="100" cy="100" r="'+(R+5)+'" fill="#f5f5f2"/>'+sh.replace('FILL',F)+'</g>'+over(sh)+(fin==='gloss'?'<ellipse cx="80" cy="70" rx="'+R*.6+'" ry="'+R*.3+'" fill="#fff" opacity=".22" transform="rotate(-30 80 70)"/>':'')
   +logo(100-7,100-R*.78,14)+qr(100-R*.44,100-R*.5,R*.88,seed)+txt(100,100+R*.52,code,6.5)+(lab?txt(100,100+R*.7,lab,9,800):'');}
 else if(d.style==='Keychain'){bg='<rect width="200" height="200" fill="#c9a37b"/><path d="M0 60 Q100 50 200 70 M0 120 Q100 110 200 130 M0 170 Q100 165 200 180" stroke="#b08a63" stroke-width="3" fill="none" opacity=".6"/>';
  const sh='<rect x="58" y="48" width="84" height="132" rx="20" fill="FILL"/>';
  body='<circle cx="100" cy="30" r="20" fill="none" stroke="url(#'+u+'met)" stroke-width="5"/><g filter="'+flt+'">'+sh.replace('FILL',F)+'</g>'+over(sh)+'<rect x="58.5" y="48.5" width="83" height="131" rx="19.5" fill="none" stroke="#fff" stroke-opacity=".55"/><circle cx="100" cy="62" r="6" fill="#c9a37b" stroke="#0003"/><path d="M100 50 L100 56" stroke="url(#'+u+'met)" stroke-width="4"/>'
   +(fin==='gloss'?'<path d="M64 60 Q70 52 90 52 L70 120Z" fill="#fff" opacity=".25"/>':'')+logo(93,72,14)+qr(70,90,60,seed)+txt(100,160,code,6.5)+(lab?txt(100,172,lab,8,800):'');}
 else if(d.style==='Pet tag'){const R=56*k;bg='<rect width="200" height="200" fill="#efe7dc"/><rect y="14" width="200" height="34" fill="#a0522d"/><path d="M0 19 H200 M0 43 H200" stroke="#f3d9b5" stroke-width="1.5" stroke-dasharray="5 4"/><rect x="88" y="10" width="24" height="42" rx="6" fill="none" stroke="url(#'+u+'met)" stroke-width="4"/>';
  const cy=60+R+10,sh='<circle cx="100" cy="'+cy+'" r="'+R+'" fill="FILL"/>';
  body='<circle cx="100" cy="'+(cy-R-6)+'" r="9" fill="none" stroke="url(#'+u+'met)" stroke-width="3.5"/><g filter="'+flt+'"><circle cx="100" cy="'+cy+'" r="'+(R+5)+'" fill="url(#'+u+'met)"/>'+sh.replace('FILL',F)+'</g>'+over(sh)
   +'<ellipse cx="'+(100-R*.35)+'" cy="'+(cy-R*.45)+'" rx="'+R*.45+'" ry="'+R*.18+'" fill="#fff" opacity=".3" transform="rotate(-30 '+(100-R*.35)+' '+(cy-R*.45)+')"/>'+logo(100-6,cy-R*.82,12)+qr(100-R*.42,cy-R*.52,R*.84,seed)+(lab?txt(100,cy+R*.5,lab,10,800):txt(100,cy+R*.5,code,6));}
 else if(d.style==='Luggage label'){bg='<rect width="200" height="200" fill="#34495e"/>'+Array.from({length:9},(_,i)=>'<rect x="'+(i*24)+'" width="10" height="200" fill="#2c3e50" opacity=".6"/>').join('')+'<rect x="70" y="0" width="60" height="16" rx="6" fill="#1b2631"/>';
  const sh='<rect x="58" y="42" width="84" height="146" rx="14" fill="FILL"/>';
  body='<path d="M92 0 V52 M108 0 V52" stroke="#111" stroke-width="7"/><g filter="'+flt+'">'+sh.replace('FILL',F)+'</g>'+over(sh)+'<rect x="88" y="50" width="24" height="7" rx="3.5" fill="#0006"/><rect x="70" y="72" width="60" height="86" rx="6" fill="#fff" opacity=".18"/>'
   +(fin==='gloss'?'<path d="M62 50 L100 46 L64 140Z" fill="#fff" opacity=".2"/>':'')+logo(93,62,14)+qr(70,82,60,seed)+txt(100,154,code,6.5)+(lab?txt(100,172,lab,9,800):'');}
 else{bg='<rect width="200" height="200" fill="#e9eef0"/>';
  body='<g filter="url(#'+u+'sh)"><rect x="50" y="8" width="100" height="184" rx="18" fill="#0b1712"/><rect x="54" y="12" width="92" height="176" rx="15" fill="'+F+'"/></g><text x="100" y="52" text-anchor="middle" font-family="Geist,system-ui" font-size="22" font-weight="600" fill="'+fg+'">9:41</text><rect x="64" y="128" width="72" height="50" rx="10" fill="#fff" opacity=".92"/>'+qr(68,131,44,seed)+'<text x="118" y="146" font-family="Geist,system-ui" font-size="5.5" font-weight="700" fill="#0b1712">Found</text><text x="118" y="153" font-family="Geist,system-ui" font-size="5.5" font-weight="700" fill="#0b1712">this?</text><text x="118" y="163" font-family="Geist,system-ui" font-size="4" fill="#4f5e57">Scan me</text>';}
 return '<svg viewBox="0 0 200 200" class="mk" role="img" aria-label="'+d.style+' preview" preserveAspectRatio="xMidYMid slice">'+defs+bg+body+'</svg>';}
var MID=0;
function avatar(d){return '<span class="av-s" role="button" aria-label="Change photo">'+(d.photo?'<img alt="" src="'+d.photo+'">':itemEmo(d))+'</span>';}
function paint(){const d=st();const c='TK-7Q4M-9XRA';
 const w=$('#design .pm-wrap');if(w)w.innerHTML=mock(d,c,++MID);
 const o=$('#order .pm-wrap');if(o)o.innerHTML=mock(d,c,++MID);
 $('#order .ord-for').innerHTML=avatar(d)+'<span>For: '+(d.name||'your item').replace(/[<&]/g,'')+'</span>';
 let ck=$('#checkout .ck-item');if(!ck){ck=document.createElement('div');ck.className='ordrow ck-item';$('#checkout .tight').before(ck);}
 ck.innerHTML='<div class="pm-wrap sm ck-mock">'+mock(d,c,++MID)+'</div><div class="ordinfo"><b>'+$('#order .ord-name').textContent+'</b><small>'+$('#order .ord-spec').textContent+'</small><small class="ord-for">'+avatar(d)+'<span>For: '+(d.name||'your item').replace(/[<&]/g,'')+'</span></small></div>';
 let od=$('#ordered .ord-mock');if(!od){od=document.createElement('div');od.className='pm-wrap ord-mock';$('#ordered .done').replaceWith(od);}od.innerHTML=mock(d,c,++MID);}
const _render=render;render=function(){_render();paint();};
var GPH=document.createElement('input');GPH.type='file';GPH.accept='image/*';GPH.hidden=true;document.body.appendChild(GPH);
GPH.addEventListener('change',()=>{const f=GPH.files[0];if(!f)return;const fr=new FileReader();fr.onload=()=>{st().photo=fr.result;render();toast('Photo added');};fr.readAsDataURL(f);GPH.value='';});
document.addEventListener('click',e=>{if(e.target.closest('.lp-img,.av-s')){e.stopPropagation();GPH.click();}},true);
"""

CSS3 = r"""
.mk{width:100%;height:100%;display:block}
.pm-wrap.cz,.pm-wrap.sm,.pm-wrap.ord-mock{overflow:hidden;padding:0}
.pm-wrap.cz{height:170px}
.pm-wrap.sm{width:88px;height:88px;border-radius:16px}
.ck-item .pm-wrap.sm{width:64px;height:64px;border-radius:14px}
.pm-wrap.ord-mock{width:150px;height:150px;margin:0 auto;border-radius:24px;min-height:0;box-shadow:var(--tk-shadow)}
.ord-for{display:flex;align-items:center;gap:6px}
.av-s{width:24px;height:24px;border-radius:7px;background:var(--tk-sunken);display:inline-grid;place-items:center;font-size:13px;overflow:hidden;flex:none;cursor:pointer}
.av-s img{width:100%;height:100%;object-fit:cover}
.lp-img{cursor:pointer}
"""
