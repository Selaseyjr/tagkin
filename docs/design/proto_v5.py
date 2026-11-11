"""Prototype round 5: owner journey speed-ups (one-tap message, saved address, undo, quick actions,
suggested replies, set up packs in a row, order timeline, nudges)."""

OWNER_JS5 = r"""
var SAVEDADDR=true,ADDREDIT=false,NUDGEOFF={},UNDO=null,UT;
// undo bar
(function(){const u=document.createElement('div');u.className='undo';u.id='undo';u.hidden=true;u.setAttribute('role','status');u.innerHTML='<span></span><button type="button">Undo</button>';document.body.appendChild(u);})();
function undoBar(text,fn){UNDO=fn;const u=$('#undo');u.querySelector('span').textContent=text;u.hidden=false;clearTimeout(UT);UT=setTimeout(()=>{u.hidden=true;UNDO=null;},5000);}
// 1. one-tap suggested message
function msgBtn(){const b=$('#message .btn.pri');b.textContent=st().msgEdited?'Next':'Use this message';}
// 2. saved address card on Order details
(function(){const g=$('#order .grp.cmp');const c=document.createElement('div');c.className='addr saved-addr';c.innerHTML='<span><small>Deliver to · saved address</small><b>Alex Mensah</b><span class="a-line">Musterstraße 1, 64283 Darmstadt, Germany</span></span><span class="link" id="addr-change">Change</span>';g.before(c);})();
function addrView(){const ed=!signedIn||ADDREDIT;$('#order .grp.cmp').hidden=!ed;$('#order .saved-addr').hidden=ed;}
// 5. suggested replies
(function(){const c=$('#thread .compose');const s=document.createElement('div');s.className='chips sugg scrollx';s.innerHTML=['Thank you so much!','I’ll pick it up today','Please hand it to staff','Where exactly is it?'].map(t=>'<span class="chip">'+t+'</span>').join('');c.before(s);})();
// 4b. reply from the notification
(function(){const n=$('#alert .notif');const r=document.createElement('div');r.className='compose nreply';r.innerHTML='<input class="in" id="nr-in" placeholder="Reply from the notification" aria-label="Quick reply"><span class="send" id="nr-send">↑</span>';n.after(r);})();
// 8. nudges + 4a. quick actions on My tags
const _rt5=renderTags;renderTags=function(){_rt5();const s=$('#tags');s.querySelectorAll('.nudge').forEach(x=>x.remove());
 all('#tags .item').forEach(el=>{if(el.querySelector('.more'))return;const m=document.createElement('span');m.className='more';m.setAttribute('role','button');m.setAttribute('aria-label','More actions');m.textContent='⋯';el.querySelector('.qrb').before(m);});
 const np=TAGS.findIndex(t=>t.st==='normal'&&!t.photo);let h='';
 if(np>=0&&!NUDGEOFF.photo)h='<div class="nudge" data-nudge="photo" data-i="'+np+'"><span>📷</span><span><b>Add a photo of '+TAGS[np].name.replace(/[<&]/g,'')+'</b><small>Finders and staff recognise it faster.</small></span><em>Add</em><i data-x="photo" aria-label="Dismiss">✕</i></div>';
 else if(!NUDGEOFF.backup)h='<div class="nudge" data-nudge="backup"><span>👤</span><span><b>Add a backup contact</b><small>Alerted if you don’t reply to a finder.</small></span><em>Add</em><i data-x="backup" aria-label="Dismiss">✕</i></div>';
 const rb=s.querySelector('.recban');if(rb)rb.hidden=!!h;
 if(h)s.querySelector('h1').insertAdjacentHTML('afterend',h);};
function quickSheet(i){CUR=i;bind();const t=TAGS[i];const lost=t.st==='lost',ret=t.st==='return';
 ov('<h2>'+t.name.replace(/[<&]/g,'')+'</h2>'+(t.st==='normal'?'<div class="btn lostb" data-q="lost">Mark as lost</div>':lost?'<div class="btn pri" data-q="found">I found it myself</div>':ret?'<div class="btn pri" data-q="conv">Open conversation</div>':'')+'<div class="btn sec" data-q="qr">Show QR code</div>'+(t.st==='normal'?'<div class="btn sec" data-q="edit">Edit name and photo</div>':'')+'<div class="btn ghost" data-ph="close">Cancel</div>');}
// 7. order timeline
function orderSheet(o){const steps=['Paid','In production','Shipped','Delivered'];const k=Math.max(0,steps.indexOf(o.st));
 ov('<h2>Order TK-'+o.id+'</h2><p class="m">'+o.t+'</p><ol class="tl">'+steps.map((s,i)=>'<li class="'+(i<=k?'on':'')+'"><b>'+s+'</b><small>'+(i<k?'Done':i===k?'Now':'Next')+'</small></li>').join('')+'</ol>'+(k>=2?'<div class="btn sec" data-toast="Opens tracking">Track parcel</div>':'')+'<div class="btn ghost" data-ph="close">Close</div>');}
const _ro5=renderOrders;renderOrders=function(){_ro5();all('#orders .item').forEach((el,i)=>{el.dataset.oi=i;el.setAttribute('role','button');});};
const _show5=show;show=function(id){_show5(id);
 if(id==='message')msgBtn();
 if(id==='order'){ADDREDIT=false;addrView();}
 if(id==='act-live'){const left=TAGS.filter(t=>t.st==='unset').length;let b=$('#act-live .next-blank');if(!b){b=document.createElement('div');b.className='btn sec next-blank';$('#act-live .btn.pri').after(b);}b.hidden=!left;b.textContent='Set up next blank tag ('+left+' left)';}};
document.addEventListener('input',e=>{if(e.target.id==='it-msg')msgBtn();});
document.addEventListener('click',e=>{const q=s=>e.target.closest(s);
 if(q('#undo button')){if(UNDO)UNDO();UNDO=null;$('#undo').hidden=true;renderTags();bind();toast('Undone');return;}
 if(q('#addr-change')){ADDREDIT=true;addrView();return;}
 const sc=q('.sugg .chip');if(sc){$('#reply').value=sc.textContent;$('#reply').focus();return;}
 if(q('#nr-send')){const v=$('#nr-in').value.trim();if(!v)return;const b=document.createElement('div');b.className='bub out';b.textContent=v;$('#thread .thread').appendChild(b);$('#nr-in').value='';toast('Reply sent, translated for the finder');return;}
 const mo=q('#tags .more');if(mo){e.stopImmediatePropagation();quickSheet(+mo.closest('[data-ti]').dataset.ti);return;}
 const qa=q('[data-q]');if(qa){e.stopImmediatePropagation();const a=qa.dataset.q,t=TAGS[CUR];ovClose();
  if(a==='lost')show('confirm');if(a==='qr')show('qr');if(a==='conv')show('locked');if(a==='edit'){show('detail');editSheet();}
  if(a==='found'){t.st='normal';renderTags();undoBar(t.name+' marked as found',()=>{t.st='lost';});}return;}
 const nx=q('[data-x]');if(nx){e.stopImmediatePropagation();NUDGEOFF[nx.dataset.x]=true;renderTags();return;}
 const nu=q('.nudge');if(nu){e.stopImmediatePropagation();if(nu.dataset.nudge==='photo'){CUR=+nu.dataset.i;bind();show('detail');EDITT=CUR;photoSheet();}else show('edit-contacts');return;}
 const oi=q('#orders [data-oi]');if(oi){orderSheet(ORDERS[+oi.dataset.oi]);return;}
 if(q('#act-live .next-blank')){e.stopImmediatePropagation();const i=TAGS.findIndex(t=>t.st==='unset');if(i>=0){CUR=i;SETUPI=i;blankDraft();D.setup=true;D.saved=true;H=['tags'];_show2('type');CURS='type';}return;}
 if(q('#scans .btn.pri')){const t=TAGS[CUR];setTimeout(()=>undoBar(t.name+' marked as found',()=>{t.st='lost';}),0);}
 if(q('#returned .btn.pri')){const t=TAGS[CUR];setTimeout(()=>undoBar(t.name+' marked as returned',()=>{t.st='return';t.ret=false;}),0);}
},true);
"""

CSS6 = r"""
.undo{position:fixed;left:50%;bottom:calc(24px + env(safe-area-inset-bottom,0px));transform:translateX(-50%);z-index:40;display:flex;gap:16px;align-items:center;background:var(--tk-ink);color:var(--tk-surface);padding:10px 12px 10px 18px;border-radius:99px;font-size:14px;box-shadow:var(--tk-shadow)}
.undo[hidden]{display:none}.undo button{border:0;background:none;color:var(--tk-brand);font:700 14px var(--tk-font-body);cursor:pointer;padding:4px 8px}
.recban[hidden],.saved-addr[hidden],.grp.cmp[hidden],.next-blank[hidden]{display:none}
.sugg{flex:none}.sugg .chip{font-size:13px;padding:7px 12px;white-space:nowrap}
.nreply{margin-top:-4px}
.more{width:32px;height:36px;display:grid;place-items:center;font-size:20px;color:var(--tk-ink-2);cursor:pointer;flex:none;border-radius:10px}
.nudge{display:flex;gap:10px;align-items:center;border:1px solid var(--tk-line);border-radius:var(--tk-radius-md);padding:10px 12px;flex:none;cursor:pointer;background:var(--tk-surface)}
.nudge b{display:block;font-size:14px}.nudge small{font-size:12px;color:var(--tk-ink-2)}.nudge em{margin-left:auto;font-style:normal;font-weight:700;color:var(--tk-brand-text)}.nudge i{font-style:normal;color:var(--tk-ink-2);padding:4px;cursor:pointer}
.tl{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:0}
.tl li{position:relative;padding:0 0 16px 28px;color:var(--tk-ink-2)}.tl li::before{content:"";position:absolute;left:4px;top:5px;width:12px;height:12px;border-radius:50%;background:var(--tk-line)}
.tl li::after{content:"";position:absolute;left:9px;top:19px;bottom:0;width:2px;background:var(--tk-line)}.tl li:last-child::after{display:none}
.tl li.on{color:var(--tk-ink)}.tl li.on::before{background:var(--tk-brand)}.tl b{display:block;font-size:15px}.tl small{font-size:12px}
"""
