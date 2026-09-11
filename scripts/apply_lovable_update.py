from pathlib import Path
import re

path = Path('index.html')
html = path.read_text(encoding='utf-8')

CSS = r'''
<style id="lovable-product-update-styles">
/* Product mock refresh — follows current SoleTasker UI, not invented product features */
.product-mock-deck{max-width:1000px;gap:18px;align-items:flex-start}
.product-mock-deck .screen-card{width:190px}
.product-mock-deck .screen-card:nth-child(1){--drot:-3deg;--dty:8px}
.product-mock-deck .screen-card:nth-child(2){--drot:-1deg;--dty:0}
.product-mock-deck .screen-card:nth-child(3){--drot:1deg;--dty:0}
.product-mock-deck .screen-card:nth-child(4){--drot:3deg;--dty:8px}
.mock-phone{height:382px;background:#fff;border:7px solid #182838;border-radius:29px;overflow:hidden;box-shadow:0 18px 42px rgba(17,24,39,.17);text-align:left;color:#1f2937;font-family:var(--fb)}
.mock-phone *{box-sizing:border-box}
.mock-top{height:43px;padding:13px 12px 8px;display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid #e6eaf0;font-size:10px;font-weight:800;color:#162638}
.mock-top small{font-size:8px;font-weight:600;color:#7b8795}
.mock-body{padding:11px 10px 13px}
.mock-chips{display:flex;gap:4px;margin-bottom:9px;overflow:hidden}
.mock-chip{border:1px solid #dfe5ec;color:#667085;background:#fff;border-radius:100px;padding:4px 7px;font-size:7px;white-space:nowrap}
.mock-chip.active{background:#17293b;color:#fff;border-color:#17293b}
.mock-list{display:grid;gap:6px}
.mock-row{border:1px solid #e3e7ec;border-radius:9px;padding:8px 8px;background:#fff;font-size:8px;line-height:1.28}
.mock-row.done{opacity:.7}.mock-row.done .mock-title{text-decoration:line-through}
.mock-title{font-weight:800;color:#152337;margin-bottom:4px}
.mock-meta{display:flex;align-items:center;gap:4px;color:#7c8795;font-size:6.6px;line-height:1.2}
.mock-pill{display:inline-flex;border-radius:100px;padding:2px 5px;font-weight:800;background:#edf2ff;color:#3166d9}
.mock-pill.red{background:#fff0ef;color:#f04a42}.mock-pill.green{background:#e6f8f3;color:#18a88e}.mock-pill.amber{background:#fff3d7;color:#a87300}.mock-pill.gray{background:#f1f3f5;color:#75808e}
.mock-note{font-size:6.6px;color:#8a96a3;line-height:1.45;margin-top:9px}
.voice-box{background:#f3f6ff;border:1px solid #b7c9ff;border-radius:12px;padding:11px;margin-bottom:10px}
.voice-head{display:flex;align-items:center;gap:8px;margin-bottom:9px}
.mock-mic{width:31px;height:31px;border-radius:50%;background:#2d5be3;color:#fff;display:grid;place-items:center;font-size:14px;flex:0 0 auto}
.voice-wave{display:flex;align-items:center;gap:2px;height:19px}
.voice-wave i{display:block;width:2px;border-radius:3px;background:#2d5be3}.voice-wave i:nth-child(1){height:7px}.voice-wave i:nth-child(2){height:15px}.voice-wave i:nth-child(3){height:11px}.voice-wave i:nth-child(4){height:18px}.voice-wave i:nth-child(5){height:9px}.voice-wave i:nth-child(6){height:14px}.voice-wave i:nth-child(7){height:6px}
.voice-copy{font-size:7.4px;line-height:1.55;color:#354052}
.mock-label{font-size:6.4px;color:#7c8795;text-transform:uppercase;letter-spacing:.05em;margin:8px 0 5px;font-weight:800}
.mock-actions{display:flex;gap:6px;margin-top:9px}.mock-btn{height:27px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:7px;font-weight:800;flex:1;border:1px solid #dfe5ec;color:#596575}.mock-btn.primary{background:#17293b;color:#fff;border-color:#17293b}.mock-btn.blue{background:#2d5be3;border-color:#2d5be3;color:#fff}
.field-stack{display:grid;gap:6px}.mock-field{border:1px solid #e1e6ec;border-radius:9px;padding:7px 8px}.mock-field .lbl{font-size:6px;color:#83909d;text-transform:uppercase;margin-bottom:3px}.mock-field .val{font-size:7.5px;font-weight:700;color:#273548;line-height:1.3}.mock-field.notes .val{font-weight:500;color:#647181}
.link-box{border:1px solid #cbd8ff;background:#f3f6ff;border-radius:10px;padding:8px;margin-bottom:9px}.link-row{font-size:6.5px;color:#2d5be3;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;margin-bottom:6px}.copy-bar{background:#2d5be3;color:#fff;border-radius:7px;padding:6px;text-align:center;font-weight:800;font-size:7px}
.request-card{border:1px solid #e1e6ec;border-radius:10px;padding:9px}.request-card h4{font-size:8px;margin-bottom:5px}.request-card p{font-size:6.7px;line-height:1.45;color:#6f7c89}.request-actions{display:flex;gap:5px;margin-top:9px}
.product-mock-deck .screen-cap{margin-top:13px}.product-mock-deck .sc-t{font-size:14px}.product-mock-deck .sc-d{font-size:11px;max-width:180px;margin:3px auto 0}

/* My Day feature section — deliberately mirrors the supplied Lovable layout */
.myday-feature{background:#1c2e40;color:#fff;padding:82px 32px 76px;position:relative;overflow:hidden}
.myday-feature:before{content:'';position:absolute;right:-180px;top:-220px;width:650px;height:650px;border-radius:50%;background:radial-gradient(circle,rgba(44,185,157,.07),transparent 67%);pointer-events:none}
.myday-inner{max-width:1100px;margin:0 auto;display:grid;grid-template-columns:1.12fr .88fr;gap:72px;align-items:center;position:relative;z-index:1}
.myday-eyebrow{display:flex;align-items:center;gap:8px;color:var(--teal);font-family:var(--fh);font-size:16px;letter-spacing:.06em;margin-bottom:19px}.myday-eyebrow svg{width:16px;height:16px;stroke:currentColor;fill:none;stroke-width:2}
.myday-feature h2{font-family:var(--fh);font-size:clamp(46px,5vw,70px);line-height:.92;letter-spacing:.3px;margin:0 0 25px;color:#fff}.myday-feature h2 span{display:block;color:var(--teal)}
.myday-lead{font-size:17px;line-height:1.68;color:rgba(255,255,255,.76);max-width:620px;margin-bottom:27px}
.myday-points{list-style:none;display:grid;gap:15px;margin:0 0 27px}.myday-points li{font-size:15px;line-height:1.55;color:rgba(255,255,255,.78);display:flex;gap:13px;align-items:flex-start}.myday-points li:before{content:'';width:6px;height:6px;border-radius:50%;background:var(--teal);margin-top:8px;flex:0 0 auto}
.myday-note{border-left:2px solid var(--teal);padding:3px 0 3px 16px;font-size:14px;color:rgba(255,255,255,.62);line-height:1.5;margin-bottom:30px}
.myday-cta{display:inline-flex;align-items:center;justify-content:center;background:var(--teal);color:#fff;border-radius:100px;padding:14px 27px;font-size:15px;font-weight:800;transition:.18s}.myday-cta:hover{background:var(--teal-dk);transform:translateY(-1px)}
.myday-device-wrap{text-align:center}.myday-device{width:300px;height:586px;margin:0 auto;background:#fff;border:8px solid #182838;border-radius:37px;overflow:hidden;box-shadow:0 28px 65px rgba(0,0,0,.28);color:#1f2937;text-align:left}.myday-device .mock-top{height:49px;padding:17px 15px 9px;font-size:13px}.myday-device .mock-top small{font-size:9px}.myday-device .mock-body{padding:13px 12px}.myday-device .mock-chip{font-size:9px;padding:5px 10px}.myday-device .mock-list{gap:9px}.myday-device .mock-row{padding:11px 10px;border-radius:11px;font-size:10px}.myday-device .mock-meta{font-size:8px}.myday-device .mock-pill{padding:2px 6px}.myday-device .mock-note{font-size:8px;margin-top:12px}.myday-caption{font-size:12px;color:rgba(255,255,255,.34);margin-top:14px}
@media(max-width:900px){.product-mock-deck .screen-card{width:178px}.myday-inner{grid-template-columns:1fr;gap:48px}.myday-copy{max-width:680px}.myday-device{width:280px;height:548px}}
@media(max-width:640px){.product-mock-deck{gap:0}.product-mock-deck .screen-card{width:200px}.mock-phone{height:402px}.myday-feature{padding:68px 24px 64px}.myday-feature h2{font-size:48px}.myday-lead{font-size:15.5px}.myday-points li{font-size:14px}.myday-device{width:264px;height:518px}.myday-cta{width:100%}}
</style>
'''

MYDAY_PHONE = r'''
<div class="myday-device" aria-label="SoleTasker My Day mock based on the current app">
  <div class="mock-top"><span>My Day</span><small>Thu 10 Sep</small></div>
  <div class="mock-body">
    <div class="mock-chips"><span class="mock-chip active">Me</span><span class="mock-chip">Dave</span><span class="mock-chip">Sam</span><span class="mock-chip">Everyone</span></div>
    <div class="mock-list">
      <div class="mock-row"><div class="mock-title">Run new sub-circuit to garage bench</div><div class="mock-meta"><span class="mock-pill red">Overdue</span><span>14 Kingston St</span></div></div>
      <div class="mock-row"><div class="mock-title">Fit 3 downlights, lounge</div><div class="mock-meta"><span class="mock-pill">High</span><span>7 Marra Ct · Me</span></div></div>
      <div class="mock-row"><div class="mock-title">Terminate switchboard, unit 4</div><div class="mock-meta"><span class="mock-pill gray">Today</span><span>Bayside Units · Me</span></div></div>
      <div class="mock-row done"><div class="mock-title">Pick up cable from wholesaler</div><div class="mock-meta"><span class="mock-pill green">Done</span><span>Me</span></div></div>
    </div>
    <div class="mock-note">Tasks only. Reminders stay in their own list.</div>
  </div>
</div>
'''

DECK = r'''
<!-- SoleTasker product mock deck — current product flows, styled from supplied Lovable reference -->
<div style="margin:0 auto 32px;text-align:center" class="rev">
  <p style="font-size:11px;font-weight:800;letter-spacing:3px;text-transform:uppercase;color:var(--teal);margin-bottom:24px">What it looks like</p>
  <div class="screens-deck product-mock-deck">
    <div class="screen-card" data-i="0">
      <div class="mock-phone">
        <div class="mock-top"><span>My Day</span><small>Thu 10 Sep</small></div>
        <div class="mock-body">
          <div class="mock-chips"><span class="mock-chip active">Me</span><span class="mock-chip">Dave</span><span class="mock-chip">Sam</span><span class="mock-chip">Everyone</span></div>
          <div class="mock-list">
            <div class="mock-row"><div class="mock-title">Run new sub-circuit to garage bench</div><div class="mock-meta"><span class="mock-pill red">Overdue</span><span>14 Kingston St</span></div></div>
            <div class="mock-row"><div class="mock-title">Fit 3 downlights, lounge</div><div class="mock-meta"><span class="mock-pill">High</span><span>7 Marra Ct · Me</span></div></div>
            <div class="mock-row"><div class="mock-title">Terminate switchboard, unit 4</div><div class="mock-meta"><span class="mock-pill gray">Today</span><span>Bayside Units · Me</span></div></div>
            <div class="mock-row done"><div class="mock-title">Pick up cable from wholesaler</div><div class="mock-meta"><span class="mock-pill green">Done</span><span>Me</span></div></div>
          </div>
          <div class="mock-note">Tasks only. Reminders stay in their own list.</div>
        </div>
      </div>
      <p class="screen-cap"><span class="sc-t">My Day</span><span class="sc-d">The tasks you want in front of you today</span></p>
    </div>

    <div class="screen-card" data-i="1">
      <div class="mock-phone">
        <div class="mock-top"><span>Voice capture</span><small>Recording</small></div>
        <div class="mock-body">
          <div class="voice-box"><div class="voice-head"><span class="mock-mic">⌁</span><span class="voice-wave"><i></i><i></i><i></i><i></i><i></i><i></i><i></i></span></div><div class="voice-copy">“Reminder Thursday — order two 63 amp curve C breakers for the Kingston Street switchboard, and get Dave to test the RCDs before we hand over.”</div></div>
          <div class="mock-label">Review before saving</div>
          <div class="mock-list">
            <div class="mock-row"><div class="mock-title">Order 2 × 63A curve C breakers</div><div class="mock-meta"><span class="mock-pill amber">Reminder · Thu</span><span>Kingston St</span></div></div>
            <div class="mock-row"><div class="mock-title">Test RCDs before handover</div><div class="mock-meta"><span class="mock-pill">Task</span><span>Assigned: Dave</span></div></div>
          </div>
          <div class="mock-actions"><span class="mock-btn">Edit</span><span class="mock-btn primary">Save both</span></div>
        </div>
      </div>
      <p class="screen-cap"><span class="sc-t">Voice Capture</span><span class="sc-d">Speak it, review it, save it where it belongs</span></p>
    </div>

    <div class="screen-card" data-i="2">
      <div class="mock-phone">
        <div class="mock-top"><span>New task</span><small>Manual or voice</small></div>
        <div class="mock-body">
          <div class="field-stack">
            <div class="mock-field"><div class="lbl">Task</div><div class="val">Terminate switchboard, unit 4</div></div>
            <div class="mock-field"><div class="lbl">Job</div><div class="val">Bayside Units — 22 Esplanade</div></div>
            <div class="mock-field"><div class="lbl">Type</div><div class="val">On-site work</div></div>
            <div class="mock-field"><div class="lbl">Priority</div><div class="val">High</div></div>
            <div class="mock-field"><div class="lbl">Due</div><div class="val">Thu 10 Sep</div></div>
            <div class="mock-field"><div class="lbl">Assigned to</div><div class="val">Dave (worker)</div></div>
            <div class="mock-field notes"><div class="lbl">Notes</div><div class="val">Main switch labelled wrong — relabel while you're in there.</div></div>
          </div>
          <div class="mock-actions"><span class="mock-btn blue">Save task</span></div>
        </div>
      </div>
      <p class="screen-cap"><span class="sc-t">Tasks</span><span class="sc-d">Job, priority, due date and assignee together</span></p>
    </div>

    <div class="screen-card" data-i="3">
      <div class="mock-phone">
        <div class="mock-top"><span>Job requests</span><small>Intake</small></div>
        <div class="mock-body">
          <div class="link-box"><div class="link-row">soletasker.app/i/calec-electrical</div><div class="copy-bar">Copy job link</div></div>
          <div class="request-card"><h4>Harding Construction</h4><p><strong>Site:</strong> 9 Verdon St, lot 12</p><p style="margin-top:5px">Switchboard relocation. Access via rear. Wants it started week of 21 Sep.</p><div class="request-actions"><span class="mock-btn">Decline</span><span class="mock-btn primary">Review</span></div></div>
          <div class="mock-note">Accepted requests become jobs with the details already entered.</div>
        </div>
      </div>
      <p class="screen-cap"><span class="sc-t">Job Intake</span><span class="sc-d">Send a link, review the request, create the job</span></p>
    </div>
  </div>
  <p class="deck-hint">Swipe to see the workflow</p>
</div>
'''

MYDAY = r'''
<!-- My Day feature section — supplied Lovable composition, SoleTasker content -->
<section class="myday-feature" id="my-day">
  <div class="myday-inner">
    <div class="myday-copy rev">
      <div class="myday-eyebrow"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="16" rx="2"></rect><path d="M8 3v4M16 3v4M3 10h18"></path></svg><span>NEW — MY DAY</span></div>
      <h2>OPEN YOUR PHONE.<span>TODAY'S WORK IS RIGHT THERE.</span></h2>
      <p class="myday-lead">One short list of the tasks that are actually on today — each still carrying the job it belongs to and the person it's assigned to. Overdue at the top, done at the bottom, nothing else in the way.</p>
      <ul class="myday-points">
        <li>Tasks only — reminders stay in their own list, so today stays clean.</li>
        <li>Filter to you, one worker, or everyone on the team.</li>
        <li>Overdue, today and coming up, grouped for you.</li>
        <li>Tick it off on site — no going back to the office to update anything.</li>
      </ul>
      <div class="myday-note">It's a plan for your day, not a dispatch board. You decide what's on it.</div>
      <a class="myday-cta" href="https://app.soletasker.com.au/signup">Try My Day free</a>
    </div>
    <div class="myday-device-wrap rev">
''' + MYDAY_PHONE + r'''
      <div class="myday-caption">My Day — filtered to you</div>
    </div>
  </div>
</section>
'''


def matching_div_end(text: str, start: int) -> int:
    open_pos = text.find('<div', start)
    if open_pos < 0:
        raise RuntimeError('Could not find deck wrapper div')
    token_re = re.compile(r'<div\b[^>]*>|</div\s*>', re.I)
    depth = 0
    for m in token_re.finditer(text, open_pos):
        if m.group(0).lower().startswith('</div'):
            depth -= 1
            if depth == 0:
                return m.end()
        else:
            depth += 1
    raise RuntimeError('Could not balance deck wrapper div')

# 1) Replace old screenshot deck with clean current-product HTML mocks.
old_marker = '<!-- App screens — real screenshots from the live app -->'
new_marker = '<!-- SoleTasker product mock deck — current product flows, styled from supplied Lovable reference -->'
if old_marker in html:
    marker_pos = html.index(old_marker)
    div_start = html.find('<div', marker_pos)
    div_end = matching_div_end(html, div_start)
    html = html[:marker_pos] + DECK + html[div_end:]
elif new_marker not in html:
    raise RuntimeError('Could not locate existing product screenshot deck')

# 2) Add the My Day section immediately after the How It Works section.
if 'id="my-day"' not in html:
    workflow_start = html.index('<section class="workflow-sec" id="workflow">')
    workflow_end = html.index('</section>', workflow_start) + len('</section>')
    html = html[:workflow_end] + '\n\n' + MYDAY + html[workflow_end:]

# 3) Add isolated styles once, preserving every existing site style and route.
if 'id="lovable-product-update-styles"' not in html:
    html = html.replace('</head>', CSS + '\n</head>', 1)

path.write_text(html, encoding='utf-8')
print('Updated index.html: product mocks + My Day section')
