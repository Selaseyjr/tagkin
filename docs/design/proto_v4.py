"""Prototype round 4: live orders list, fresh order journeys, blank tags (set up later),
edit item details later, reorder copies, skip the redundant type step."""

OWNER_JS4 = r"""
var ORDERS=[{id:10482,e:'🏷️',t:'2 × sticker',d:'ordered 2 Nov',st:'In production',c:'b-r'},{id:10311,e:'🔑',t:'1 × keychain',d:'28 Oct',st:'Delivered',c:'b-n'}];
var NEXTO=10490,BLANKNEXT=false,SETUPI=null,EDITT=null;
function renderOrders(){const s=$('#orders');s.querySelectorAll('.item').forEach(x=>x.remove());const a=s.querySelector('.two');
 ORDERS.forEach(o=>{const el=document.createElement('div');el.className='item';el.innerHTML='<span class="ic">'+o.e+'</span><span class="tx"><b></b><span></span></span><span class="badge '+o.c+'">'+o.st+'</span>';el.querySelector('b').textContent=o.t;el.querySelector('.tx span').textContent='TK-'+o.id+' · '+o.d;s.insertBefore(el,a);});}
function addOrder(t,e){ORDERS.unshift({id:NEXTO,e:e,t:t,d:'ordered today',st:'Paid',c:'b-r'});NEXTO++;}
// fresh journeys from Orders and the empty state
all('#orders [data-go=order],#e-orders [data-go=order]').forEach(b=>{b.dataset.go='start';b.textContent='Order a tag';});
all('#gift-delivery input').forEach(i=>{if(!i.placeholder)i.placeholder=i.getAttribute('aria-label');});$('#gift textarea').placeholder='Gift note (optional)';
// blank tag entry on Create a tag
(function(){const s=$('#start');const p=document.createElement('div');p.className='btn sec';p.id='blank-go';p.dataset.go='pick';p.innerHTML='Order a blank tag <small class="xs">· link it to something later</small>';s.querySelector('.two').after(p);})();
// detail: edit item details, reorder copies
(function(){const l=$('#detail [data-go=edit-msg]');const r=document.createElement('div');r.className='li';r.id='ed-row';r.innerHTML='<span>Item name and photo</span><span>Edit ›</span>';l.before(r);
 const o=$('#detail [data-go=order]');o.querySelector('span').textContent='Order more copies';})();
function editSheet(){const t=TAGS[CUR];ov('<h2>Item details</h2><div class="ed-ph" role="button" aria-label="Change photo">'+(t.photo?'<img alt="" src="'+t.photo+'">':'<span>'+t.e+'</span>')+'<em>'+(t.photo?'Change photo':'Add a photo')+'</em></div><input class="in" id="ed-name" maxlength="40" aria-label="Name"><p class="fielderr" id="ed-err" hidden>Give it a name, at least 2 characters.</p><textarea class="in ta sm" id="ed-desc" maxlength="120" placeholder="Description (optional)" aria-label="Description"></textarea><div class="btn pri" id="ed-save">Save</div><div class="btn ghost" data-ph="close">Cancel</div>');$('#ed-name').value=t.name;$('#ed-desc').value=t.desc||'';}
const _photoSet=photoSet;photoSet=function(src){if(EDITT!==null){const t=TAGS[EDITT];t.photo=src;EDITT=null;bind();renderTags();editSheet();return;}_photoSet(src);};
const _photoView=photoView;photoView=function(){if($('#ed-save'))return;_photoView();};
const _addTag=addTag;addTag=function(){const d=st();if(d.saved)return;if(d.blank){d.saved=true;TAGS.unshift({name:'Blank '+d.style.toLowerCase(),e:'🏷️',code:newCode(),st:'unset'});CUR=0;return;}_addTag();};
const _badge=badge;badge=function(t){return t.st==='unset'?'<span class="badge warnb">Set up</span>':_badge(t);};
const _renderTags=renderTags;renderTags=function(){_renderTags();all('#tags .item').forEach(el=>{const t=TAGS[+el.dataset.ti];if(t&&t.st!=='unset'&&!t.photo){el.querySelector('.tx span').textContent+=' · add a photo';}});};
const _show4=show;show=function(id){const from=CURS;
 if(id==='ordered'){const d=st();if(!d.saved||d.reorder||d.blank){}const q=+$('#order .step i').textContent;addOrder(q+' × '+d.style.toLowerCase()+(d.blank?' (blank)':d.reorder?' (copies of '+d.name+')':''),d.blank?'🏷️':itemEmo(d));$('#ordered .xs').textContent='Order TK-'+(NEXTO-1)+' · '+q+' × '+d.style.toLowerCase()+(d.blank?' · blank, set it up when it arrives':' for '+(d.name||'your item'));}
 if(id==='gift-sent')addOrder('Gift · '+$('#gift .opt.on span:nth-child(2)').firstChild.textContent.toLowerCase(),'🎁');
 _show4(id);
 if(id==='pick'&&BLANKNEXT){BLANKNEXT=false;st().blank=true;}
 if(id==='pick'){const b=st().blank;all('.gcard').forEach(g=>{g.hidden=b&&g.dataset.style==='Lock screen';g.dataset.go=b?'design':g.dataset.style==='Pet tag'?'p-details':g.dataset.style==='Luggage label'?'t-details':'type';});$('#pick h1').textContent=b?'Choose your blank tag':'Choose your type of tag';}
 if(id==='orders')renderOrders();
 if(id==='gift'&&!['gift-delivery','gift-review'].includes(from)){all('#gift-delivery input:not([type=email])').forEach(i=>{i.value='';});$('#gift-delivery input[type=email]').value='';$('#gift textarea').value='';}
 if(id==='gift-review'){const v=[...all('#gift-delivery input')].map(i=>i.value.trim());$('#gift-review .addr b').textContent=v[0]||'Recipient';$('#gift-review .a-line').textContent=[v[1],[v[2],v[3]].filter(Boolean).join(' ')].filter(Boolean).join(', ');$('#gift-sent .m').textContent='It arrives in 3 to 5 working days. The activation PIN is on the gift card inside, so only '+(v[0]||'they')+' can claim the tags.';}
 if(id==='order'){const d=st();$('#order .ord-for').innerHTML=d.blank?'<span class="av-s">🏷️</span><span>Blank · link it to an item when it arrives</span>':$('#order .ord-for').innerHTML;}
 if(id==='ordered'||id==='act-live'){const d=st();if(id==='act-live'&&SETUPI!==null){const t=TAGS[SETUPI];$('#act-live .m').innerHTML='';$('#act-live .m').append(t.code+' now belongs to ',Object.assign(document.createElement('b'),{textContent:t.name}),'.');SETUPI=null;}}};
document.addEventListener('click',e=>{const q=s=>e.target.closest(s);
 if(q('#blank-go'))BLANKNEXT=true;
 if(q('#ed-row')){e.stopImmediatePropagation();editSheet();return;}
 if(q('.ed-ph')){e.stopImmediatePropagation();EDITT=CUR;ovClose();photoSheet();return;}
 if(q('#ed-save')){const n=$('#ed-name').value.trim();if(n.length<2){$('#ed-err').hidden=false;return;}const t=TAGS[CUR];t.name=n;t.desc=$('#ed-desc').value.trim();ovClose();bind();renderTags();toast('Saved');return;}
 if(q('[data-ph=close]')&&EDITT!==null&&!q('#ed-save'))EDITT=null;
 const ti=q('[data-ti]');if(ti&&!q('[data-qr]')){const t=TAGS[+ti.dataset.ti];if(t&&t.st==='unset'){e.stopImmediatePropagation();CUR=+ti.dataset.ti;SETUPI=CUR;blankDraft();D.setup=true;D.saved=true;CURS='tags';H=['tags'];_show2('type');CURS='type';toast('Set up '+t.code+': what will it be on?');return;}}
 const mn=q('#message .btn.pri');if(mn&&st().setup){e.stopImmediatePropagation();const d=st(),t=TAGS[SETUPI];t.name=d.name;t.photo=d.photo;t.e=itemEmo(d);t.st='normal';t.fresh=true;show('act-live');return;}
 const ro=q('#detail [data-go=order]');if(ro){const t=TAGS[CUR];D=null;st();D.name=t.name;D.photo=t.photo;D.saved=true;D.reorder=true;render();}
},true);
"""

CSS5 = r"""
.badge.warnb{background:var(--tk-warn-soft);color:var(--tk-warn)}
#blank-go{flex-direction:column;gap:0;line-height:1.2}#blank-go small{font-weight:400}
.ed-ph{height:150px;border-radius:18px;background:var(--tk-sunken);display:grid;place-items:center;font-size:48px;position:relative;overflow:hidden;cursor:pointer}
.ed-ph img{width:100%;height:100%;object-fit:cover}
.ed-ph em{position:absolute;right:10px;bottom:10px;font:600 12px var(--tk-font-body);font-style:normal;background:rgb(0 0 0 / .55);color:#fff;padding:4px 10px;border-radius:99px}
"""
