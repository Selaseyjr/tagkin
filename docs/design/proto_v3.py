"""Prototype round 3 (11 Nov 2026): sample photos, draft and navigation rules, photo preview,
product preview, optional travel trip. Loaded by build_screens.py after proto_logic."""
import base64
from pathlib import Path

_S = Path(__file__).resolve().parent / "assets" / "samples"
SAMPLES = {p.stem: "data:image/jpeg;base64," + base64.b64encode(p.read_bytes()).decode() for p in sorted(_S.glob("*.jpg"))}
SAMPLES_JS = "var SAMPLE=" + repr(SAMPLES).replace("'", '"') + ";\n"

PICK = '<label class="add{cls} ph-pick"><input type="file" accept="image/*" class="ph-in" hidden><span>{t}</span></label>'
T_DETAILS = ('''    ("t-details", "Type 1 · Travel details", hdr(backto("type"), "2 of 4") + '<h1>About your luggage</h1><input class="in" id="t-name" value="Blue suitcase" maxlength="40" placeholder="Name, e.g. Blue suitcase" aria-label="Luggage name">'''
             + PICK.format(cls=" sm", t="+ Add a photo of your luggage")
             + '''<label class="check" id="t-trip-on"><i>✓</i><span>Add a trip now <small class="xs">(optional)</small><small class="xs tdesc">Helps airline or hotel staff route it. Finders see destination and carrier only. It hides when the trip ends.</small></span></label><div id="t-trip" hidden><div class="chips modes scrollx"><span class="chip on" data-mode="plane">✈️ Plane</span><span class="chip" data-mode="train">🚆 Train</span><span class="chip" data-mode="bus">🚌 Bus</span><span class="chip" data-mode="ferry">⛴️ Ferry</span><span class="chip" data-mode="hotel">🏨 Hotel</span></div><input class="in sm" id="t-a" placeholder="Airline, e.g. Lufthansa" aria-label="Carrier"><input class="in sm" id="t-c" placeholder="Destination, e.g. Accra (ACC)" aria-label="Destination"><input class="in sm" id="t-d" placeholder="Trip ends, e.g. 20 Nov (hides it after)" aria-label="Trip ends"><input id="t-b" hidden></div><p class="xs">You can add or change a trip any time from the tag.</p><div class="sp"></div><div class="btn pri"' + go("message") + '>Next</div>'),''')

CSS4 = r"""
.ph-pick.has{background:center/cover no-repeat;border-style:solid;border-color:transparent;color:#fff;position:relative}
.ph-pick.has span{position:absolute;right:8px;bottom:8px;background:rgb(0 0 0 / .55);padding:4px 10px;border-radius:99px;font-size:12px}
.ph-pick.err{border-color:var(--tk-lost)}
.fielderr{color:var(--tk-lost-text);font-size:13px;margin:-6px 0 0}
#t-trip{display:flex;flex-direction:column;gap:8px}#t-trip[hidden]{display:none}
.tdesc{display:block;margin-top:2px}
.ov{position:fixed;inset:0;z-index:50;display:flex;align-items:flex-end;justify-content:center;background:rgb(0 0 0 / .55);padding:12px}
.ov[hidden]{display:none}
.ov.full{align-items:center;background:rgb(5 10 8 / .92)}
.ov-c{background:var(--tk-surface);border-radius:28px;padding:22px;width:100%;max-width:400px;display:flex;flex-direction:column;gap:12px;animation:up var(--tk-slow) var(--tk-ease)}
.ov.full .ov-c{background:transparent;padding:0;max-width:440px}
.ov-img{width:100%;max-height:62vh;object-fit:contain;border-radius:20px;background:#000}
.ov-svg{width:100%;aspect-ratio:1;border-radius:24px;overflow:hidden}
.ov-cap{color:#fff;text-align:center;font-size:14px;margin:0}
.ov h2{font:650 20px/1.2 var(--tk-font-display);margin:0}
.samp{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}
.samp img{width:100%;aspect-ratio:1;object-fit:cover;border-radius:12px;cursor:pointer}
.ov .btn.sec.dark{background:rgb(255 255 255 / .12);color:#fff;border-color:rgb(255 255 255 / .3)}
#design .pm-wrap.cz{cursor:zoom-in;position:relative}
#design .pm-wrap.cz::after{content:"Tap to preview";position:absolute;right:10px;bottom:10px;background:rgb(0 0 0 / .55);color:#fff;font-size:11px;padding:3px 8px;border-radius:99px}
"""

OWNER_JS3 = r"""
var FLOW=['pick','type','details','t-details','p-details','message','design','order','checkout'];
var PENDING=null,FORCE=false,SELT=null,SELS=null;
var NAMEF={0:'#it-name',1:'#t-name',2:'#p-name'};
function descF(){return $('#details input[aria-label=Description]');}
function dirty(){const d=st();return !!(d.photo||$(NAMEF[d.type]).value.trim()||d.msgEdited||d.label);}
function clearItem(){const d=st();d.photo=null;d.msgEdited=false;d.label='';[...Object.values(NAMEF),'#t-a','#t-c','#t-d','#cz-label'].forEach(s=>{const e=$(s);if(e)e.value='';});const de=descF();if(de)de.value='';
 $('#t-trip-on').classList.remove('on');$('#t-trip').hidden=true;all('.ph-pick').forEach(p=>{p.classList.remove('has','err');p.style.backgroundImage='';p.querySelector('span').textContent=p.dataset.t;});all('.fielderr').forEach(x=>x.remove());}
function blankDraft(){SELT=null;SELS=null;D=null;st();D.name='';clearItem();D.size='M';D.col='#00c48c';D.fin='Matte';render();}
function photoSet(src){const d=st();d.photo=src;all('.ph-pick').forEach(p=>{p.classList.toggle('has',!!src);p.style.backgroundImage=src?'url('+src+')':'';p.querySelector('span').textContent=src?'Tap to view':p.dataset.t;p.classList.remove('err');});render();}
function ov(html,full){let o=$('#ov');if(!o){o=document.createElement('div');o.id='ov';o.className='ov';o.setAttribute('role','dialog');o.setAttribute('aria-modal','true');document.body.appendChild(o);}
 o.className='ov'+(full?' full':'');o.innerHTML='<div class="ov-c">'+html+'</div>';o.hidden=false;}
function ovClose(){const o=$('#ov');if(o)o.hidden=true;}
function photoSheet(){ov('<h2>Add a photo</h2><p class="m">A clear photo helps finders and staff recognise it.</p><div class="btn pri" data-ph="lib">Choose or take a photo</div><span class="label2">Or use a sample (prototype only)</span><div class="samp">'+Object.keys(SAMPLE).map(k=>'<img alt="'+k+'" data-samp="'+k+'" src="'+SAMPLE[k]+'">').join('')+'</div><p class="xs">JPEG, PNG, WebP or HEIC, up to 10 MB. We resize it and remove location data.</p><div class="btn ghost" data-ph="close">Cancel</div>');}
function photoView(){ov('<img class="ov-img" alt="Your photo" src="'+st().photo+'"><p class="ov-cap">This is how your photo will look.</p><div class="btn pri" data-ph="close">Use this photo</div><div class="two"><div class="btn sec dark" data-ph="sheet">Replace</div><div class="btn sec dark" data-ph="remove">Remove</div></div>',true);}
function productView(){const d=st();ov('<div class="ov-svg">'+mock(d,'TK-7Q4M-9XRA',++MID)+'</div><p class="ov-cap">'+$('#design .pm-spec').textContent+'</p><div class="btn pri" data-ph="close">Looks good</div><div class="btn sec dark" data-ph="close">Keep customising</div>',true);}
function loadFile(f){if(!f)return;if(!/^image\//.test(f.type)&&!/\.heic$/i.test(f.name)){toast('Choose an image file');return;}if(f.size>10*1024*1024){toast('That photo is over 10 MB. Choose a smaller one.');return;}
 const fr=new FileReader();fr.onload=()=>{const im=new Image();im.onload=()=>{const k=Math.min(1,1600/Math.max(im.width,im.height));const c=document.createElement('canvas');c.width=Math.round(im.width*k);c.height=Math.round(im.height*k);c.getContext('2d').drawImage(im,0,0,c.width,c.height);photoSet(c.toDataURL('image/jpeg',.85));ovClose();photoView();};im.onerror=()=>toast('This photo format isn’t supported here. Try JPEG or PNG.');im.src=fr.result;};fr.readAsDataURL(f);}
GPH.replaceWith(GPH=GPH.cloneNode());GPH.addEventListener('change',()=>{loadFile(GPH.files[0]);GPH.value='';});
function nameOk(){const d=st();const f=$(NAMEF[d.type]);const v=f.value.trim();const scr=f.closest('.scr');scr.querySelectorAll('.fielderr').forEach(x=>x.remove());
 if(v.length<2){const p=document.createElement('p');p.className='fielderr';p.textContent=d.type===2?'Add your pet’s name.':'Give it a name, e.g. Black backpack.';f.after(p);f.focus();return false;}return true;}
document.addEventListener('click',e=>{
 const pp=e.target.closest('.ph-pick,.lp-img,.av-s');if(pp){e.preventDefault();e.stopImmediatePropagation();st().photo?photoView():photoSheet();return;}
 const ph=e.target.closest('[data-ph]');if(ph){const a=ph.dataset.ph;if(a==='lib')GPH.click();if(a==='close')ovClose();if(a==='sheet')photoSheet();if(a==='remove'){photoSet(null);ovClose();}return;}
 const sp=e.target.closest('[data-samp]');if(sp){photoSet(SAMPLE[sp.dataset.samp]);ovClose();photoView();return;}
 if(e.target.closest('#ov')&&e.target.id==='ov'){ovClose();return;}
 if(e.target.closest('#design .pm-wrap.cz')){productView();return;}
 const nx=e.target.closest('#details .btn.pri,#t-details .btn.pri,#p-details .btn.pri');if(nx&&!nameOk()){e.stopImmediatePropagation();return;}
 const tt=e.target.closest('#t-trip-on');if(tt){e.stopImmediatePropagation();tt.classList.toggle('on');$('#t-trip').hidden=!tt.classList.contains('on');return;}
 const gc=e.target.closest('.gcard'),ty=e.target.closest('#type .grp .opt');
 if(gc||ty){const d=st();const nt=gc?+gc.dataset.type:[...ty.parentElement.children].indexOf(ty);const ns=gc?gc.dataset.style:null;
  if(SELT!==null&&(nt!==SELT||(gc&&ns!==SELS))){clearItem();}SELT=nt;if(gc)SELS=ns;}
},true);
const _show2=show;show=function(id){
 if(!FORCE&&FLOW.includes(CURS)&&ROOTS.includes(id)&&!D.saved&&dirty()){PENDING=id;ov('<h2>Discard this tag?</h2><p class="m">You’ll lose the name, photo and design you added.</p><div class="btn lostb" data-discard>Discard</div><div class="btn sec" data-ph="close">Keep editing</div>');return;}
 FORCE=false;const from=CURS;
 if((id==='pick'||id==='start')&&!FLOW.includes(from))blankDraft();
 if(id==='start'&&D&&D.saved)blankDraft();
 if(id==='code')all('#code .code i').forEach((x,i)=>x.classList.toggle('on',i===0));
 _show2(id);};
document.addEventListener('click',e=>{if(e.target.closest('[data-discard]')){ovClose();blankDraft();FORCE=true;show(PENDING);}},true);
document.addEventListener('input',e=>{if(Object.values(NAMEF).includes('#'+e.target.id)){e.target.closest('.scr').querySelectorAll('.fielderr').forEach(x=>x.remove());}});
Object.values(MODES).forEach(m=>{m[1]='';m[3]='Trip ends, e.g. 20 Nov (hides it after)';});MODES.plane[0]='Airline, e.g. Lufthansa';MODES.plane[2]='Destination, e.g. Accra (ACC)';
all('.ph-pick').forEach(p=>p.dataset.t=p.querySelector('span').textContent);
all('#it-name,#p-name').forEach(x=>{x.maxLength=40;});const _de=descF();if(_de)_de.maxLength=120;
$('#it-name').placeholder='Name, e.g. Black backpack';$('#p-name').placeholder='Your pet’s name';
const _ti=tagsInit;tagsInit=function(){_ti();TAGS[0].photo=SAMPLE.backpack;TAGS[1].photo=SAMPLE.dog;TAGS[2].photo=SAMPLE.suitcase;};
"""

OWNER_INIT3 = "tagsInit();blankDraft();CURS=null;show('launch1');"

FINDER_JS3 = r"""
const PH={item:'backpack',lost:'backpack',travel:'suitcase',pet:'dog',test:'backpack'};
const _scan3=scan;scan=function(v){_scan3(v);const s=SAMPLE[PH[v]];if(s){const cap=$('#f-photo small');$('#f-photo').innerHTML='<img alt="" src="'+s+'">'+(cap?cap.outerHTML:'');}};
document.addEventListener('change',ev=>{if(ev.target.id==='f-photoin'&&ev.target.files[0]){const f=ev.target.files[0];if(f.size>10*1024*1024){toast('That photo is over 10 MB.');ev.target.value='';return;}const fr=new FileReader();fr.onload=()=>{const l=ev.target.closest('label');l.style.background='center/cover url('+fr.result+')';l.querySelector('b').textContent='✓ Photo added · tap to change';};fr.readAsDataURL(f);}});
scan('item');
"""
