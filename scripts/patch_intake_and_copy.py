from pathlib import Path

path = Path('index.html')
html = path.read_text(encoding='utf-8')

# 1) Sharpen workflow step 4 copy.
html = html.replace(
    "The invoice follow-up. The quote you owe. The callback you meant to make. It stays there until it's done. You don't forget it because you can't — it's not in your head anymore.",
    "Quotes, callbacks and follow-ups stay visible until they're handled. You can see what still needs action without carrying the whole job in your head."
)

# 2) Remove the extra 'get it out of your head' callout from Why We Built It.
old_callout = '<p style="font-size:17px;font-weight:800;color:var(--ink);border-left:4px solid var(--teal);padding:12px 18px;background:var(--bg);border-radius:0 var(--r1) var(--r1) 0;margin-bottom:24px">Get it out of your head and into something you won\'t forget.</p>\n'
html = html.replace(old_callout, '')

# 3) Replace the whole Job Intake section with a tighter, animated dark flow.
start_marker = '<section class="intake-sec" id="intake">'
if start_marker not in html:
    raise SystemExit('Job Intake section not found')
start = html.index(start_marker)
end = html.index('</section>', start) + len('</section>')

new_section = r'''<section class="intake-sec" id="intake">
  <style id="intake-flow-refresh">
    .intake-sec{background:var(--navy);padding:92px 32px;position:relative;overflow:hidden}
    .intake-sec:after{content:'';position:absolute;right:-140px;bottom:-160px;width:520px;height:520px;border-radius:50%;background:radial-gradient(circle,rgba(44,185,157,.08),transparent 66%);pointer-events:none}
    .intake-refresh{max-width:1100px;margin:0 auto;display:grid;grid-template-columns:.92fr 1.08fr;gap:72px;align-items:center;position:relative;z-index:1}
    .intake-copy{max-width:520px}
    .intake-eyebrow{font-size:11px;font-weight:800;letter-spacing:3px;text-transform:uppercase;color:var(--teal);display:block;margin-bottom:16px}
    .intake-h{font-family:var(--fh);font-size:clamp(46px,5.2vw,68px);line-height:.94;color:#fff;margin-bottom:22px}.intake-h .a{color:var(--teal)}
    .intake-desc{font-size:17px;line-height:1.72;color:rgba(255,255,255,.66);margin-bottom:28px}.intake-desc strong{color:#fff;font-weight:800}
    .intake-steps{display:grid;gap:12px}.intake-step{display:grid;grid-template-columns:34px 1fr;gap:13px;align-items:start;padding:13px 0;border-top:1px solid rgba(255,255,255,.09)}.intake-step:first-child{border-top:0}.intake-n{width:28px;height:28px;border:1px solid rgba(44,185,157,.35);border-radius:50%;display:grid;place-items:center;color:var(--teal);font-size:12px;font-weight:900}.intake-step h3{color:#fff;font-size:15px;margin:2px 0 3px}.intake-step p{color:rgba(255,255,255,.52);font-size:13px;line-height:1.5}

    .intake-flow-demo{border:1px solid rgba(255,255,255,.12);border-radius:24px;background:rgba(255,255,255,.035);padding:26px;box-shadow:0 24px 60px rgba(0,0,0,.18);position:relative;overflow:hidden}
    .flow-label{font-size:10px;font-weight:900;letter-spacing:2px;text-transform:uppercase;color:rgba(255,255,255,.38);margin-bottom:11px}
    .flow-link{display:flex;align-items:center;gap:10px;background:#fff;border-radius:14px;padding:13px 14px;margin-bottom:18px;color:#243247;position:relative}.flow-url{font-size:12px;flex:1;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;color:#53617c}.flow-send{background:var(--teal);color:#fff;border-radius:10px;padding:9px 13px;font-size:11px;font-weight:900;position:relative;overflow:visible}.flow-send:after{content:'';position:absolute;inset:-7px;border:2px solid rgba(44,185,157,.45);border-radius:14px;animation:intakeTap 2.8s ease-out infinite}
    .flow-status{display:flex;align-items:center;gap:9px;color:var(--teal);font-size:12px;font-weight:850;margin:0 0 18px;opacity:.35;animation:intakeStatus 5.6s ease-in-out infinite}.flow-status-dot{width:8px;height:8px;border-radius:50%;background:var(--teal)}
    .flow-home{background:#fff;border-radius:16px;overflow:hidden;transform:translateY(18px);opacity:.3;animation:intakeHome 5.6s ease-in-out infinite}.flow-home-head{background:#15283a;padding:11px 14px;display:flex;align-items:center;justify-content:space-between}.flow-home-head span:first-child{font-size:10px;font-weight:900;letter-spacing:1px;text-transform:uppercase;color:rgba(255,255,255,.58)}.flow-home-head span:last-child{font-size:10px;font-weight:900;color:var(--teal)}.flow-request{padding:16px;display:flex;align-items:center;gap:12px}.flow-avatar{width:38px;height:38px;border-radius:50%;background:#497f72;color:#fff;display:grid;place-items:center;font-size:12px;font-weight:900;flex:0 0 auto}.flow-request-body{min-width:0;flex:1}.flow-request-name{font-size:14px;font-weight:900;color:#1f2b3a;margin-bottom:2px}.flow-request-meta{font-size:11px;color:#7c8795;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}.flow-review{border:1px solid #f2a11d;color:#e18d08;border-radius:8px;padding:7px 10px;font-size:10px;font-weight:900;white-space:nowrap}
    .flow-caption{text-align:center;color:rgba(255,255,255,.46);font-size:12px;margin-top:16px}.flow-caption strong{color:var(--teal)}
    @keyframes intakeTap{0%,18%{transform:scale(.8);opacity:0}26%{opacity:1}42%{transform:scale(1.08);opacity:0}100%{opacity:0}}
    @keyframes intakeStatus{0%,28%{opacity:.25;transform:translateY(4px)}38%,72%{opacity:1;transform:translateY(0)}84%,100%{opacity:.25;transform:translateY(4px)}}
    @keyframes intakeHome{0%,38%{opacity:.25;transform:translateY(18px)}48%,82%{opacity:1;transform:translateY(0)}94%,100%{opacity:.25;transform:translateY(18px)}}
    @media(max-width:900px){.intake-refresh{grid-template-columns:1fr;gap:44px}.intake-copy{max-width:650px}}
    @media(max-width:640px){.intake-sec{padding:68px 24px}.intake-h{font-size:46px}.intake-desc{font-size:16px}.intake-flow-demo{padding:19px;border-radius:20px}.flow-link{padding:11px 11px}.flow-url{font-size:11px}.flow-send{padding:8px 10px}.flow-request{padding:13px}.flow-request-name{font-size:13px}.flow-request-meta{font-size:10px}}
    @media(prefers-reduced-motion:reduce){.flow-send:after,.flow-status,.flow-home{animation:none!important}.flow-status,.flow-home{opacity:1;transform:none}}
  </style>
  <div class="intake-refresh">
    <div class="intake-copy rev">
      <span class="intake-eyebrow">Job intake link</span>
      <h2 class="intake-h">Send a link.<br/>Client fills it in.<br/><span class="a">You're done.</span></h2>
      <p class="intake-desc">Send your intake link and let the client enter the address, job details and photos. <strong>The request lands on Home ready for review, with the information already together.</strong></p>
      <div class="intake-steps">
        <div class="intake-step"><div class="intake-n">1</div><div><h3>Send the link</h3><p>Share it by SMS, WhatsApp or email.</p></div></div>
        <div class="intake-step"><div class="intake-n">2</div><div><h3>Client adds the details</h3><p>Address, job description and photos come back together.</p></div></div>
        <div class="intake-step"><div class="intake-n">3</div><div><h3>Review it on Home</h3><p>Open the request, check the details and move into the job.</p></div></div>
      </div>
    </div>

    <div class="intake-flow-demo rev" style="transition-delay:.12s" aria-label="Animated SoleTasker job intake flow">
      <div class="flow-label">Send your intake link</div>
      <div class="flow-link"><span aria-hidden="true">↗</span><div class="flow-url">soletasker.app/i/calec-electrical</div><div class="flow-send">Send</div></div>
      <div class="flow-status"><span class="flow-status-dot"></span><span>Client submitted job details + photos</span></div>
      <div class="flow-label">What appears on Home</div>
      <div class="flow-home">
        <div class="flow-home-head"><span>Home</span><span>Job request ready</span></div>
        <div class="flow-request"><div class="flow-avatar">ST</div><div class="flow-request-body"><div class="flow-request-name">Sarah Thornton</div><div class="flow-request-meta">14 Webb St · 4 photos · Switchboard upgrade</div></div><div class="flow-review">Review →</div></div>
      </div>
      <div class="flow-caption"><strong>Client fills it in</strong> → lands on Home ready to review</div>
    </div>
  </div>
</section>'''

html = html[:start] + new_section + html[end:]
path.write_text(html, encoding='utf-8')
print('Sharpened copy, removed extra founder callout, and rebuilt Job Intake as animated dark flow')
