from pathlib import Path

path = Path('index.html')
html = path.read_text(encoding='utf-8')

start_marker = '<section class="site-finishers-sec"'
if start_marker not in html:
    raise SystemExit('Current on-site section not found')
start = html.index(start_marker)
end = html.index('</section>', start) + len('</section>')

new = r'''<section class="smart-onsite-sec" id="smart-onsite">
  <style id="smart-onsite-styles">
    .smart-onsite-sec{background:#fff;padding:92px 32px 96px;position:relative;overflow:hidden}
    .smart-onsite-wrap{max-width:1100px;margin:0 auto}
    .smart-onsite-head{max-width:760px;margin-bottom:42px}
    .smart-onsite-eyebrow{font-size:11px;font-weight:850;letter-spacing:3px;text-transform:uppercase;color:var(--teal);display:block;margin-bottom:12px}
    .smart-onsite-sec h2{font-family:var(--fh);font-size:clamp(42px,4.8vw,58px);line-height:.96;color:#1B2B6B!important;margin:0 0 18px;letter-spacing:.2px}
    .smart-onsite-sec h2 span{color:var(--teal)!important}
    .smart-onsite-intro{font-size:17px;line-height:1.7;color:#6f7887;max-width:660px;margin:0}

    .smart-tools-shell{display:grid;grid-template-columns:minmax(0,1fr) 430px;gap:74px;align-items:center}
    .smart-tools-rail{max-width:510px}
    .smart-rail-group+.smart-rail-group{margin-top:28px}
    .smart-rail-label{font-size:10px;font-weight:900;letter-spacing:2px;text-transform:uppercase;color:#8c96a3;margin-bottom:10px}

    .smart-quick-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:8px}
    .smart-quick{height:70px;border:1px solid #e1e6eb;background:#fff;border-radius:14px;color:#1B2B6B;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px;font-size:11px;font-weight:850;transition:.18s ease;box-shadow:0 2px 8px rgba(28,43,58,.035)}
    .smart-quick svg{width:18px;height:18px;stroke:var(--teal);fill:none;stroke-width:1.9}
    .smart-quick:hover,.smart-quick:focus-visible{transform:translateY(-2px);border-color:#b9ddd5;background:#fbfefd}
    .smart-quick.tapped{animation:smartQuickTap .38s ease}
    @keyframes smartQuickTap{0%{transform:scale(1)}45%{transform:scale(.95);background:var(--teal-lt);border-color:var(--teal)}100%{transform:scale(1)}}

    .smart-feature-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:9px}
    .smart-feature-btn{height:54px;border:1px solid #dfe5ea;background:#fff;border-radius:12px;padding:0 14px;color:#1B2B6B;display:flex;align-items:center;gap:9px;text-align:left;font-size:12px;font-weight:850;transition:.18s ease;position:relative;overflow:hidden}
    .smart-feature-btn .sf-ic{width:28px;height:28px;border-radius:8px;background:#f4f8f8;display:grid;place-items:center;color:var(--teal);flex:0 0 auto}
    .smart-feature-btn .sf-ic svg{width:16px;height:16px;stroke:currentColor;fill:none;stroke-width:1.8}
    .smart-feature-btn:hover,.smart-feature-btn:focus-visible{border-color:#b9ddd5;background:#fbfefd}
    .smart-feature-btn.active{background:var(--teal-lt);border-color:rgba(44,185,157,.55);color:#16344d}
    .smart-feature-btn.active .sf-ic{background:#fff}
    .smart-feature-btn.active:after{content:'';position:absolute;left:0;bottom:0;height:3px;background:var(--teal);width:100%;transform-origin:left;animation:smartProgress 4.8s linear forwards}
    @keyframes smartProgress{from{transform:scaleX(0)}to{transform:scaleX(1)}}

    .smart-phone-wrap{display:flex;justify-content:center;position:relative}
    .smart-phone{width:100%;max-width:410px;height:640px;background:#f7f9fb;border:8px solid #17293a;border-radius:30px;box-shadow:0 18px 48px rgba(28,43,58,.14);overflow:hidden;display:flex;flex-direction:column;color:#18283a;position:relative}
    .smart-phone-top{height:58px;background:#fff;border-bottom:1px solid #e7ebef;display:flex;align-items:center;justify-content:space-between;padding:0 14px;flex:0 0 auto}
    .smart-phone-job{display:flex;align-items:center;gap:9px;min-width:0}.smart-phone-back{width:27px;height:27px;border-radius:8px;border:1px solid #e1e6eb;display:grid;place-items:center;color:#596878;font-size:13px}.smart-phone-title{font-size:12px;font-weight:900;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:225px}.smart-phone-sub{font-size:9px;color:#8994a0;margin-top:1px}.smart-phone-status{font-size:9px;font-weight:900;color:var(--teal)}
    .smart-phone-body{flex:1;padding:16px;background:#f7f9fb;overflow:hidden;display:flex;align-items:flex-start;justify-content:center;position:relative}
    .smart-state{width:100%;animation:smartStateIn .26s ease both}
    @keyframes smartStateIn{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:none}}
    .smart-screen-title{font-size:10px;font-weight:900;letter-spacing:1.5px;text-transform:uppercase;color:#82909f;margin:0 0 10px}
    .smart-card{width:100%;background:#fff;border:1px solid #e1e6eb;border-radius:16px;padding:17px;box-shadow:0 4px 14px rgba(28,43,58,.045)}
    .smart-card+.smart-card{margin-top:10px}.smart-card h3{font-family:var(--fb)!important;font-size:17px!important;line-height:1.25;color:#1B2B6B!important;margin:0 0 6px;font-weight:900}.smart-card p{font-size:12px;line-height:1.5;color:#6d7886;margin:0}
    .smart-meta{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-bottom:10px}.smart-meta-box{background:#fff;border:1px solid #e2e7ec;border-radius:12px;padding:10px}.smart-meta-box span{display:block;font-size:8px;font-weight:900;letter-spacing:.8px;text-transform:uppercase;color:#8995a1;margin-bottom:3px}.smart-meta-box strong{font-size:11px;color:#243548}
    .smart-action-row{display:flex;gap:8px;flex-wrap:wrap;margin-top:14px}.smart-action{height:36px;border-radius:9px;padding:0 12px;display:inline-flex;align-items:center;justify-content:center;font-size:11px;font-weight:900}.smart-action.primary{background:var(--teal);color:#fff}.smart-action.secondary{border:1px solid #dce3e9;color:#526170;background:#fff}
    .smart-note-box{margin-top:13px;border-left:3px solid var(--teal);background:#f5f8fa;border-radius:0 10px 10px 0;padding:11px 12px}.smart-note-box strong{display:block;color:#1B2B6B;font-size:11px;margin-bottom:3px}.smart-note-box span{font-size:11px;color:#657382;line-height:1.45}
    .smart-status-strip{margin-top:13px;border:1px solid rgba(44,185,157,.25);background:var(--teal-lt);color:var(--teal-dk);border-radius:10px;padding:9px 10px;font-size:10px;font-weight:850;display:flex;align-items:center;gap:7px}
    .smart-fields{display:grid;gap:7px;margin-top:12px}.smart-field{border:1px solid #e1e6ec;border-radius:10px;padding:9px 10px;background:#fff}.smart-field label{display:block;font-size:8px;font-weight:900;letter-spacing:.8px;text-transform:uppercase;color:#84909d;margin-bottom:2px}.smart-field div{font-size:10px;font-weight:800;color:#25364a}
    .smart-scan-drop{border:1.5px dashed #9bcdf6;background:#f3f9ff;border-radius:13px;min-height:118px;display:flex;align-items:center;justify-content:center;text-align:center;padding:14px;color:#4c86bd;margin-bottom:10px}.smart-scan-drop svg{width:26px;height:26px;stroke:#3b93df;fill:none;stroke-width:1.8;margin-bottom:6px}.smart-scan-drop strong{display:block;font-size:11px;color:#3c7db8;margin-bottom:2px}.smart-scan-drop span{font-size:9px;color:#7f9bb5}
    .smart-toast{position:absolute;left:50%;top:13px;transform:translate(-50%,-10px);background:#17293a;color:#fff;border-radius:999px;padding:8px 12px;font-size:10px;font-weight:850;opacity:0;pointer-events:none;transition:.2s ease;z-index:4;white-space:nowrap;box-shadow:0 8px 20px rgba(28,43,58,.2)}.smart-toast.show{opacity:1;transform:translate(-50%,0)}.smart-toast strong{color:var(--teal)}

    .smart-phone-footer{height:62px;background:#fff;border-top:1px solid #e7ebef;display:grid;grid-template-columns:repeat(5,1fr);align-items:end;padding:5px 5px 6px;flex:0 0 auto}
    .smart-nav-item{display:flex;flex-direction:column;align-items:center;justify-content:flex-end;gap:2px;color:#929eaa;font-size:7.5px;font-weight:750;height:49px}.smart-nav-item svg{width:16px;height:16px;stroke:currentColor;fill:none;stroke-width:1.8}.smart-nav-item.active{color:#2D5BE3}.smart-nav-item.memo{position:relative}.smart-nav-item.memo .memo-circle{width:34px;height:34px;border-radius:50%;background:#2D5BE3;display:grid;place-items:center;color:#fff;margin-top:-15px;box-shadow:0 5px 14px rgba(45,91,227,.3)}.smart-nav-item.memo svg{width:18px;height:18px}.smart-nav-item.memo span{margin-top:0}
    .smart-phone-caption{text-align:center;margin-top:12px;font-size:11px;color:#8c96a3}.smart-phone-caption strong{color:var(--teal)}

    @media(max-width:900px){.smart-tools-shell{grid-template-columns:1fr;gap:38px}.smart-tools-rail{max-width:none}.smart-phone-wrap{justify-content:flex-start}.smart-phone{max-width:410px}}
    @media(max-width:640px){.smart-onsite-sec{padding:68px 20px 74px}.smart-onsite-head{margin-bottom:30px}.smart-onsite-sec h2{font-size:42px}.smart-onsite-intro{font-size:16px}.smart-tools-shell{gap:30px}.smart-quick-grid{gap:6px}.smart-quick{height:62px;border-radius:12px;font-size:10px}.smart-feature-grid{gap:7px}.smart-feature-btn{height:52px;padding:0 10px;font-size:10.5px}.smart-feature-btn .sf-ic{width:26px;height:26px}.smart-phone-wrap{justify-content:center}.smart-phone{height:605px;max-width:380px;border-width:7px;border-radius:27px}.smart-phone-body{padding:13px}.smart-card{padding:14px}.smart-card h3{font-size:16px!important}.smart-phone-title{max-width:205px}}
    @media(prefers-reduced-motion:reduce){.smart-feature-btn.active:after{animation:none}.smart-state{animation:none}}
  </style>

  <div class="smart-onsite-wrap">
    <div class="smart-onsite-head rev">
      <span class="smart-onsite-eyebrow">On-site tools</span>
      <h2>SMART TOOLS WHILE YOU'RE <span>STILL ON SITE.</span></h2>
      <p class="smart-onsite-intro">Call, message or open Maps in one tap. Then handle the bigger follow-up from the job while the details are still in front of you.</p>
    </div>

    <div class="smart-tools-shell rev">
      <div class="smart-tools-rail">
        <div class="smart-rail-group">
          <div class="smart-rail-label">Quick actions</div>
          <div class="smart-quick-grid">
            <button class="smart-quick" type="button" data-quick="Call" aria-label="Call"><svg viewBox="0 0 24 24"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.8 19.8 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.12 4.18 2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.12.9.33 1.78.62 2.63a2 2 0 0 1-.45 2.11L8 9.73a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.85.29 1.73.5 2.63.62A2 2 0 0 1 22 16.92z"/></svg><span>Call</span></button>
            <button class="smart-quick" type="button" data-quick="SMS" aria-label="SMS"><svg viewBox="0 0 24 24"><path d="M21 15a4 4 0 0 1-4 4H8l-5 3V7a4 4 0 0 1 4-4h10a4 4 0 0 1 4 4z"/></svg><span>SMS</span></button>
            <button class="smart-quick" type="button" data-quick="Email" aria-label="Email"><svg viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg><span>Email</span></button>
            <button class="smart-quick" type="button" data-quick="Maps" aria-label="Maps"><svg viewBox="0 0 24 24"><path d="M20 10c0 5-8 12-8 12S4 15 4 10a8 8 0 1 1 16 0z"/><circle cx="12" cy="10" r="2.5"/></svg><span>Maps</span></button>
          </div>
        </div>

        <div class="smart-rail-group">
          <div class="smart-rail-label">Smart job tools</div>
          <div class="smart-feature-grid">
            <button class="smart-feature-btn active" type="button" data-smart="review"><span class="sf-ic"><svg viewBox="0 0 24 24"><path d="m12 2 3 6 6.5.9-4.7 4.6 1.1 6.5-5.9-3.1L6.1 20l1.1-6.5L2.5 8.9 9 8z"/></svg></span><span>Review</span></button>
            <button class="smart-feature-btn" type="button" data-smart="future"><span class="sf-ic"><svg viewBox="0 0 24 24"><path d="M12 20h9"/><path d="M16.5 3.5a2.1 2.1 0 0 1 3 3L8 18l-4 1 1-4z"/></svg></span><span>Future Work</span></button>
            <button class="smart-feature-btn" type="button" data-smart="swms"><span class="sf-ic"><svg viewBox="0 0 24 24"><path d="M6 2h9l3 3v17H6z"/><path d="M14 2v5h5M9 12h6M9 16h6"/></svg></span><span>SWMS</span></button>
            <button class="smart-feature-btn" type="button" data-smart="scan"><span class="sf-ic"><svg viewBox="0 0 24 24"><path d="M4 7V4h3M17 4h3v3M20 17v3h-3M7 20H4v-3"/><rect x="7" y="8" width="10" height="8" rx="1"/></svg></span><span>Scan Doc</span></button>
          </div>
        </div>
      </div>

      <div class="smart-phone-wrap">
        <div>
          <div class="smart-phone" aria-live="polite">
            <div class="smart-phone-top">
              <div class="smart-phone-job"><div class="smart-phone-back">‹</div><div><div class="smart-phone-title">29 Sherwood Ave, Mornington</div><div class="smart-phone-sub">Job detail</div></div></div>
              <div class="smart-phone-status">Active</div>
            </div>
            <div class="smart-phone-body"><div class="smart-toast" data-smart-toast></div><div class="smart-state" data-smart-state></div></div>
            <div class="smart-phone-footer" aria-label="SoleTasker app footer navigation">
              <div class="smart-nav-item active"><svg viewBox="0 0 24 24"><rect x="4" y="4" width="6" height="6" rx="1"/><rect x="14" y="4" width="6" height="6" rx="1"/><rect x="4" y="14" width="6" height="6" rx="1"/><rect x="14" y="14" width="6" height="6" rx="1"/></svg><span>Home</span></div>
              <div class="smart-nav-item"><svg viewBox="0 0 24 24"><path d="M4 7h16v13H4z"/><path d="M8 7V4h8v3"/></svg><span>Jobs</span></div>
              <div class="smart-nav-item memo"><div class="memo-circle"><svg viewBox="0 0 24 24"><rect x="9" y="3" width="6" height="12" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v3"/></svg></div><span>Memo</span></div>
              <div class="smart-nav-item"><svg viewBox="0 0 24 24"><path d="M9 11l2 2 4-4"/><rect x="4" y="4" width="16" height="16" rx="2"/></svg><span>Tasks</span></div>
              <div class="smart-nav-item"><svg viewBox="0 0 24 24"><path d="M5 7h14M5 12h14M5 17h14"/></svg><span>More</span></div>
            </div>
          </div>
          <div class="smart-phone-caption">Auto-cycling through the smart tools. <strong>Tap any tool to jump to it.</strong></div>
        </div>
      </div>
    </div>
  </div>

  <script>
  (()=>{
    const root=document.currentScript.closest('.smart-onsite-sec');
    if(!root) return;
    const state=root.querySelector('[data-smart-state]');
    const toast=root.querySelector('[data-smart-toast]');
    const buttons=[...root.querySelectorAll('[data-smart]')];
    const quick=[...root.querySelectorAll('[data-quick]')];
    const states={
      review:`<div><div class="smart-screen-title">Job detail</div><div class="smart-meta"><div class="smart-meta-box"><span>Customer</span><strong>Sarah Thornton</strong></div><div class="smart-meta-box"><span>Mobile</span><strong>0412 908 331</strong></div></div><div class="smart-card"><h3>Request review</h3><p>Send the review link while the job is still fresh.</p><div class="smart-action-row"><span class="smart-action primary">Send review</span><span class="smart-action secondary">Copy link</span></div><div class="smart-status-strip">✓ Review link ready</div></div></div>`,
      future:`<div><div class="smart-screen-title">Job detail</div><div class="smart-card"><h3>Future work</h3><p>Keep the next opportunity attached to this job.</p><div class="smart-note-box"><strong>Saved for later</strong><span>EV charger and garage sub-board — follow up after handover.</span></div><div class="smart-action-row"><span class="smart-action primary">Save note</span></div></div></div>`,
      swms:`<div><div class="smart-screen-title">SWMS</div><div class="smart-card"><h3>Ready to check and send</h3><div class="smart-fields"><div class="smart-field"><label>Site</label><div>29 Sherwood Ave, Mornington</div></div><div class="smart-field"><label>Work</label><div>Electrical fit-off and switchboard works</div></div><div class="smart-field"><label>Builder</label><div>Harding Constructions</div></div></div><div class="smart-action-row"><span class="smart-action primary">Sign &amp; send</span><span class="smart-action secondary">Preview PDF</span></div></div></div>`,
      scan:`<div><div class="smart-screen-title">Doc scan</div><div class="smart-scan-drop"><div><svg viewBox="0 0 24 24"><path d="M9 3h6l1 3h3v14H5V6h3z"/><circle cx="12" cy="13" r="4"/></svg><strong>Point your camera at the work order</strong><span>Photo or PDF</span></div></div><div class="smart-card"><h3>Extracted — check before saving</h3><div class="smart-fields"><div class="smart-field"><label>Site address</label><div>9 Verdon St, lot 12</div></div><div class="smart-field"><label>Contact</label><div>Trent Harding · 0412 908 331</div></div><div class="smart-field"><label>Order no.</label><div>WO-20418</div></div></div></div></div>`
    };
    let current=0;
    let timer=null;
    let resumeTimer=null;
    const show=(key)=>{
      state.innerHTML=states[key];
      buttons.forEach((b,i)=>{const on=b.dataset.smart===key;b.classList.toggle('active',on);if(on){current=i;b.style.animation='none';void b.offsetWidth;b.style.animation='';}});
    };
    const startAuto=()=>{
      clearInterval(timer);
      timer=setInterval(()=>{current=(current+1)%buttons.length;show(buttons[current].dataset.smart);},4800);
    };
    const manual=(key)=>{
      show(key);
      clearInterval(timer);
      clearTimeout(resumeTimer);
      resumeTimer=setTimeout(startAuto,6500);
    };
    buttons.forEach(b=>b.addEventListener('click',()=>manual(b.dataset.smart)));
    quick.forEach(b=>b.addEventListener('click',()=>{
      b.classList.remove('tapped');void b.offsetWidth;b.classList.add('tapped');
      const messages={Call:'Calling Sarah Thornton…',SMS:'Opening message…',Email:'Opening email…',Maps:'Opening 29 Sherwood Ave in Maps…'};
      toast.innerHTML='<strong>'+b.dataset.quick+'</strong> · '+messages[b.dataset.quick].replace(b.dataset.quick,'');
      toast.classList.add('show');
      setTimeout(()=>toast.classList.remove('show'),1300);
    }));
    show('review');
    if(!window.matchMedia('(prefers-reduced-motion: reduce)').matches) startAuto();
  })();
  </script>
</section>'''

html = html[:start] + new + html[end:]
path.write_text(html, encoding='utf-8')
print('Refined smart tools to white section with portrait full-screen app mock and resumable autoplay')
