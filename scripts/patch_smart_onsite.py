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
    .smart-onsite-sec{background:var(--navy);padding:88px 32px 92px;position:relative;overflow:hidden}
    .smart-onsite-sec:before{content:'';position:absolute;inset:0;background-image:radial-gradient(circle,rgba(255,255,255,.035) 1px,transparent 1px);background-size:34px 34px;pointer-events:none}
    .smart-onsite-sec:after{content:'';position:absolute;right:-170px;top:-170px;width:600px;height:600px;border-radius:50%;background:radial-gradient(circle,rgba(44,185,157,.09),transparent 68%);pointer-events:none}
    .smart-onsite-wrap{max-width:1100px;margin:0 auto;position:relative;z-index:1}
    .smart-onsite-head{max-width:760px;margin-bottom:38px}
    .smart-onsite-eyebrow{font-size:11px;font-weight:850;letter-spacing:3px;text-transform:uppercase;color:var(--teal);display:block;margin-bottom:12px}
    .smart-onsite-sec h2{font-family:var(--fh);font-size:clamp(42px,4.8vw,58px);line-height:.96;color:#fff!important;margin:0 0 18px;letter-spacing:.2px}
    .smart-onsite-sec h2 span{color:var(--teal)!important}
    .smart-onsite-intro{font-size:17px;line-height:1.7;color:rgba(255,255,255,.62);max-width:650px;margin:0}

    .smart-tools-shell{display:grid;grid-template-columns:260px 1fr;gap:22px;align-items:stretch}
    .smart-tools-rail{display:flex;flex-direction:column;gap:16px}
    .smart-rail-label{font-size:10px;font-weight:900;letter-spacing:2px;text-transform:uppercase;color:rgba(255,255,255,.36)}
    .smart-quick-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:9px}
    .smart-quick{min-height:76px;border:1px solid rgba(255,255,255,.11);background:rgba(255,255,255,.045);border-radius:14px;color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:7px;font-size:12px;font-weight:800;transition:.18s ease;position:relative;overflow:hidden}
    .smart-quick svg{width:19px;height:19px;stroke:var(--teal);fill:none;stroke-width:1.9}
    .smart-quick:hover,.smart-quick:focus-visible{transform:translateY(-2px);background:rgba(255,255,255,.075);border-color:rgba(44,185,157,.35)}
    .smart-quick.tapped{animation:smartQuickTap .42s ease}
    @keyframes smartQuickTap{0%{transform:scale(1)}45%{transform:scale(.94);background:rgba(44,185,157,.14)}100%{transform:scale(1)}}

    .smart-feature-grid{display:grid;grid-template-columns:1fr;gap:9px}
    .smart-feature-btn{min-height:62px;border:1px solid rgba(255,255,255,.11);background:rgba(255,255,255,.035);border-radius:14px;padding:13px 14px;color:rgba(255,255,255,.72);display:flex;align-items:center;gap:11px;text-align:left;font-size:13px;font-weight:800;transition:.2s ease;position:relative;overflow:hidden}
    .smart-feature-btn .sf-ic{width:30px;height:30px;border-radius:9px;background:rgba(44,185,157,.1);display:grid;place-items:center;color:var(--teal);flex:0 0 auto}
    .smart-feature-btn .sf-ic svg{width:17px;height:17px;stroke:currentColor;fill:none;stroke-width:1.8}
    .smart-feature-btn.active{background:#fff;color:#1c2b3a;border-color:#fff;box-shadow:0 10px 28px rgba(0,0,0,.16)}
    .smart-feature-btn.active .sf-ic{background:var(--teal-lt)}
    .smart-feature-btn.active:after{content:'';position:absolute;inset:-3px;border:2px solid rgba(44,185,157,.5);border-radius:16px;animation:smartSelectPulse 2.3s ease-out infinite;pointer-events:none}
    @keyframes smartSelectPulse{0%,45%{opacity:0;transform:scale(.98)}58%{opacity:.9}85%,100%{opacity:0;transform:scale(1.05)}}

    .smart-device{background:#f8fafc;border-radius:24px;border:1px solid rgba(255,255,255,.14);box-shadow:0 28px 70px rgba(0,0,0,.28);overflow:hidden;min-height:525px;display:flex;flex-direction:column;color:#18283a}
    .smart-device-top{height:58px;background:#fff;border-bottom:1px solid #e9edf2;display:flex;align-items:center;justify-content:space-between;padding:0 18px}
    .smart-device-job{display:flex;align-items:center;gap:10px;min-width:0}.smart-device-back{width:27px;height:27px;border-radius:8px;border:1px solid #e1e6eb;display:grid;place-items:center;color:#596878;font-size:13px}.smart-device-title{font-size:13px;font-weight:900;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}.smart-device-sub{font-size:10px;color:#8893a0;margin-top:1px}.smart-device-status{font-size:10px;font-weight:900;color:var(--teal);white-space:nowrap}
    .smart-device-body{flex:1;padding:20px;display:flex;align-items:stretch;justify-content:center;background:#f7f9fb}
    .smart-state{width:100%;display:flex;align-items:center;justify-content:center;animation:smartStateIn .28s ease both}
    @keyframes smartStateIn{from{opacity:0;transform:translateY(7px)}to{opacity:1;transform:none}}
    .smart-card{width:100%;max-width:590px;background:#fff;border:1px solid #e2e7ec;border-radius:18px;padding:22px;box-shadow:0 6px 22px rgba(28,43,58,.06)}
    .smart-card-kicker{font-size:10px;font-weight:900;letter-spacing:1.7px;text-transform:uppercase;color:#7a8796;margin-bottom:10px}.smart-card h3{font-size:20px!important;color:#1B2B6B!important;margin:0 0 8px;line-height:1.25;font-family:var(--fb)!important;font-weight:900}.smart-card p{font-size:14px;line-height:1.6;color:#687584;margin:0}
    .smart-action-row{display:flex;gap:9px;flex-wrap:wrap;margin-top:18px}.smart-action{height:38px;border-radius:10px;padding:0 14px;display:inline-flex;align-items:center;justify-content:center;font-size:12px;font-weight:900}.smart-action.primary{background:var(--teal);color:#fff}.smart-action.secondary{border:1px solid #dce3e9;color:#526170;background:#fff}
    .smart-note-box{margin-top:16px;border-left:3px solid var(--teal);background:#f5f8fa;border-radius:0 11px 11px 0;padding:12px 14px}.smart-note-box strong{display:block;color:#1B2B6B;font-size:12px;margin-bottom:3px}.smart-note-box span{font-size:13px;color:#657382;line-height:1.5}
    .smart-status-strip{margin-top:16px;border:1px solid rgba(44,185,157,.25);background:var(--teal-lt);color:var(--teal-dk);border-radius:11px;padding:10px 12px;font-size:12px;font-weight:850;display:flex;align-items:center;gap:8px}
    .smart-fields{display:grid;gap:8px;margin-top:15px}.smart-field{border:1px solid #e1e6ec;border-radius:11px;padding:10px 12px;background:#fff}.smart-field label{display:block;font-size:9px;font-weight:900;letter-spacing:1px;text-transform:uppercase;color:#84909d;margin-bottom:3px}.smart-field div{font-size:12px;font-weight:750;color:#25364a}
    .smart-scan-grid{display:grid;grid-template-columns:.82fr 1.18fr;gap:12px;margin-top:15px}.smart-scan-drop{border:1.5px dashed #9bcdf6;background:#f3f9ff;border-radius:14px;min-height:180px;display:flex;align-items:center;justify-content:center;text-align:center;padding:20px;color:#4c86bd}.smart-scan-drop svg{width:30px;height:30px;stroke:#3b93df;fill:none;stroke-width:1.8;margin-bottom:8px}.smart-scan-drop strong{display:block;font-size:12px;color:#3c7db8;margin-bottom:3px}.smart-scan-drop span{font-size:10px;color:#7f9bb5}.smart-scan-fields{display:grid;gap:8px}

    .smart-device-footer{height:60px;background:#fff;border-top:1px solid #e7ebef;display:grid;grid-template-columns:repeat(5,1fr);align-items:end;padding:5px 6px 6px}
    .smart-nav-item{display:flex;flex-direction:column;align-items:center;justify-content:flex-end;gap:2px;color:#929eaa;font-size:8px;font-weight:750;height:48px}.smart-nav-item svg{width:17px;height:17px;stroke:currentColor;fill:none;stroke-width:1.8}.smart-nav-item.active{color:#2D5BE3}.smart-nav-item.memo{position:relative}.smart-nav-item.memo .memo-circle{width:34px;height:34px;border-radius:50%;background:#2D5BE3;display:grid;place-items:center;color:#fff;margin-top:-15px;box-shadow:0 5px 14px rgba(45,91,227,.3)}.smart-nav-item.memo svg{width:18px;height:18px}.smart-nav-item.memo span{margin-top:0}
    .smart-tap-note{height:25px;background:#15283a;color:rgba(255,255,255,.52);font-size:10px;display:flex;align-items:center;justify-content:center}.smart-tap-note strong{color:var(--teal);margin-left:4px}

    @media(max-width:900px){.smart-tools-shell{grid-template-columns:1fr}.smart-tools-rail{display:grid;grid-template-columns:1fr 1.35fr;gap:14px}.smart-feature-grid{grid-template-columns:repeat(2,1fr)}.smart-quick-grid{grid-template-columns:repeat(4,1fr)}.smart-quick{min-height:68px}.smart-device{min-height:500px}}
    @media(max-width:640px){.smart-onsite-sec{padding:68px 20px 72px}.smart-onsite-head{margin-bottom:28px}.smart-onsite-sec h2{font-size:42px}.smart-onsite-intro{font-size:16px}.smart-tools-rail{display:block}.smart-rail-label{margin:0 0 9px}.smart-feature-grid{grid-template-columns:repeat(2,1fr);margin-top:16px}.smart-quick-grid{grid-template-columns:repeat(4,1fr);gap:7px}.smart-quick{min-height:61px;border-radius:12px;font-size:10px}.smart-quick svg{width:17px;height:17px}.smart-feature-btn{min-height:58px;padding:11px 10px;font-size:11px;gap:8px}.smart-feature-btn .sf-ic{width:27px;height:27px}.smart-device{border-radius:20px;min-height:475px}.smart-device-top{padding:0 12px}.smart-device-body{padding:13px}.smart-card{padding:17px;border-radius:15px}.smart-card h3{font-size:18px!important}.smart-card p{font-size:13px}.smart-scan-grid{grid-template-columns:1fr}.smart-scan-drop{min-height:112px}.smart-device-footer{height:57px}.smart-nav-item{font-size:7.5px}.smart-nav-item.memo .memo-circle{width:32px;height:32px}}
    @media(prefers-reduced-motion:reduce){.smart-feature-btn.active:after{animation:none}.smart-state{animation:none}}
  </style>

  <div class="smart-onsite-wrap">
    <div class="smart-onsite-head rev">
      <span class="smart-onsite-eyebrow">On-site tools</span>
      <h2>SMART TOOLS WHILE YOU'RE <span>STILL ON SITE.</span></h2>
      <p class="smart-onsite-intro">Quick actions are one tap. For the admin that matters, open the job and handle the next step while the details are still in front of you.</p>
    </div>

    <div class="smart-tools-shell rev">
      <div class="smart-tools-rail">
        <div>
          <div class="smart-rail-label">Quick actions</div>
          <div class="smart-quick-grid">
            <button class="smart-quick" type="button" data-quick="Call" aria-label="Call"><svg viewBox="0 0 24 24"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.8 19.8 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.12 4.18 2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.12.9.33 1.78.62 2.63a2 2 0 0 1-.45 2.11L8 9.73a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.85.29 1.73.5 2.63.62A2 2 0 0 1 22 16.92z"/></svg><span>Call</span></button>
            <button class="smart-quick" type="button" data-quick="SMS" aria-label="SMS"><svg viewBox="0 0 24 24"><path d="M21 15a4 4 0 0 1-4 4H8l-5 3V7a4 4 0 0 1 4-4h10a4 4 0 0 1 4 4z"/></svg><span>SMS</span></button>
            <button class="smart-quick" type="button" data-quick="Email" aria-label="Email"><svg viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg><span>Email</span></button>
            <button class="smart-quick" type="button" data-quick="Maps" aria-label="Maps"><svg viewBox="0 0 24 24"><path d="M20 10c0 5-8 12-8 12S4 15 4 10a8 8 0 1 1 16 0z"/><circle cx="12" cy="10" r="2.5"/></svg><span>Maps</span></button>
          </div>
        </div>

        <div>
          <div class="smart-rail-label">Job tools</div>
          <div class="smart-feature-grid">
            <button class="smart-feature-btn active" type="button" data-smart="review"><span class="sf-ic"><svg viewBox="0 0 24 24"><path d="m12 2 3 6 6.5.9-4.7 4.6 1.1 6.5-5.9-3.1L6.1 20l1.1-6.5L2.5 8.9 9 8z"/></svg></span><span>Review</span></button>
            <button class="smart-feature-btn" type="button" data-smart="future"><span class="sf-ic"><svg viewBox="0 0 24 24"><path d="M12 20h9"/><path d="M16.5 3.5a2.1 2.1 0 0 1 3 3L8 18l-4 1 1-4z"/></svg></span><span>Future Work</span></button>
            <button class="smart-feature-btn" type="button" data-smart="swms"><span class="sf-ic"><svg viewBox="0 0 24 24"><path d="M6 2h9l3 3v17H6z"/><path d="M14 2v5h5M9 12h6M9 16h6"/></svg></span><span>SWMS</span></button>
            <button class="smart-feature-btn" type="button" data-smart="scan"><span class="sf-ic"><svg viewBox="0 0 24 24"><path d="M4 7V4h3M17 4h3v3M20 17v3h-3M7 20H4v-3"/><rect x="7" y="8" width="10" height="8" rx="1"/></svg></span><span>Scan Doc</span></button>
          </div>
        </div>
      </div>

      <div class="smart-device" aria-live="polite">
        <div class="smart-device-top">
          <div class="smart-device-job"><div class="smart-device-back">‹</div><div><div class="smart-device-title">29 Sherwood Ave, Mornington</div><div class="smart-device-sub">Job detail</div></div></div>
          <div class="smart-device-status">Active</div>
        </div>
        <div class="smart-device-body"><div class="smart-state" data-smart-state></div></div>
        <div class="smart-tap-note">Tap a tool to change the preview <strong>• auto-playing</strong></div>
        <div class="smart-device-footer" aria-label="SoleTasker app footer navigation">
          <div class="smart-nav-item active"><svg viewBox="0 0 24 24"><rect x="4" y="4" width="6" height="6" rx="1"/><rect x="14" y="4" width="6" height="6" rx="1"/><rect x="4" y="14" width="6" height="6" rx="1"/><rect x="14" y="14" width="6" height="6" rx="1"/></svg><span>Home</span></div>
          <div class="smart-nav-item"><svg viewBox="0 0 24 24"><path d="M4 7h16v13H4z"/><path d="M8 7V4h8v3"/></svg><span>Jobs</span></div>
          <div class="smart-nav-item memo"><div class="memo-circle"><svg viewBox="0 0 24 24"><rect x="9" y="3" width="6" height="12" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v3"/></svg></div><span>Memo</span></div>
          <div class="smart-nav-item"><svg viewBox="0 0 24 24"><path d="M9 11l2 2 4-4"/><rect x="4" y="4" width="16" height="16" rx="2"/></svg><span>Tasks</span></div>
          <div class="smart-nav-item"><svg viewBox="0 0 24 24"><path d="M5 7h14M5 12h14M5 17h14"/></svg><span>More</span></div>
        </div>
      </div>
    </div>
  </div>

  <script>
  (()=>{
    const root=document.currentScript.closest('.smart-onsite-sec');
    if(!root) return;
    const state=root.querySelector('[data-smart-state]');
    const buttons=[...root.querySelectorAll('[data-smart]')];
    const quick=[...root.querySelectorAll('[data-quick]')];
    const note=root.querySelector('.smart-tap-note');
    const states={
      review:`<div class="smart-card"><div class="smart-card-kicker">Request review</div><h3>Send the review before you leave.</h3><p>The job already has the customer details. Open the review action, send it, and keep moving.</p><div class="smart-action-row"><span class="smart-action primary">Send review request</span><span class="smart-action secondary">Copy link</span></div><div class="smart-status-strip">✓ Review link ready for this job</div></div>`,
      future:`<div class="smart-card"><div class="smart-card-kicker">Future work</div><h3>Keep the next opportunity with the job.</h3><p>Save the work worth coming back to without turning it into a sales pipeline.</p><div class="smart-note-box"><strong>Future work</strong><span>Owner asked about an EV charger and garage sub-board — follow up after handover.</span></div><div class="smart-action-row"><span class="smart-action primary">Save future work</span></div></div>`,
      swms:`<div class="smart-card"><div class="smart-card-kicker">SWMS</div><h3>Job details already filled in.</h3><p>Open the SWMS, check the job details, sign on the phone and send it to the builder.</p><div class="smart-fields"><div class="smart-field"><label>Site</label><div>29 Sherwood Ave, Mornington</div></div><div class="smart-field"><label>Work</label><div>Electrical fit-off and switchboard works</div></div><div class="smart-field"><label>Builder</label><div>Harding Constructions</div></div></div><div class="smart-action-row"><span class="smart-action primary">Sign &amp; send</span><span class="smart-action secondary">Preview PDF</span></div></div>`,
      scan:`<div class="smart-card"><div class="smart-card-kicker">Scan work order</div><h3>Point your camera at the work order.</h3><p>Photograph it or upload the file, then check the details before anything is saved.</p><div class="smart-scan-grid"><div class="smart-scan-drop"><div><svg viewBox="0 0 24 24"><path d="M9 3h6l1 3h3v14H5V6h3z"/><circle cx="12" cy="13" r="4"/></svg><strong>Work order</strong><span>Photo or PDF</span></div></div><div class="smart-scan-fields"><div class="smart-field"><label>Site address</label><div>9 Verdon St, lot 12</div></div><div class="smart-field"><label>Contact</label><div>Trent Harding · 0412 908 331</div></div><div class="smart-field"><label>Order no.</label><div>WO-20418</div></div></div></div></div>`
    };
    let current=0;
    let timer;
    const show=(key,manual=false)=>{
      state.innerHTML=states[key];
      buttons.forEach((b,i)=>{b.classList.toggle('active',b.dataset.smart===key);if(b.dataset.smart===key)current=i;});
      if(manual){clearInterval(timer);note.innerHTML='Selected <strong>'+buttons[current].textContent.trim()+'</strong> • tap another tool';}
    };
    const autoplay=()=>{timer=setInterval(()=>{current=(current+1)%buttons.length;show(buttons[current].dataset.smart,false);},4200)};
    buttons.forEach(b=>b.addEventListener('click',()=>show(b.dataset.smart,true)));
    quick.forEach(b=>b.addEventListener('click',()=>{b.classList.remove('tapped');void b.offsetWidth;b.classList.add('tapped');note.innerHTML='<strong>'+b.dataset.quick+'</strong> opens from the job';setTimeout(()=>{note.innerHTML='Tap a tool to change the preview <strong>• auto-playing</strong>';},1400)}));
    show('review');
    if(!window.matchMedia('(prefers-reduced-motion: reduce)').matches) autoplay();
  })();
  </script>
</section>'''

html = html[:start] + new + html[end:]
path.write_text(html, encoding='utf-8')
print('Replaced on-site cards with interactive smart tools section')
