from pathlib import Path

path = Path('index.html')
html = path.read_text(encoding='utf-8')

# Update electrician task examples in the My Day mocks.
html = html.replace('Run new sub-circuit to garage bench', 'Wire and install new aircon')
html = html.replace('Fit 3 downlights, lounge', 'Fit off switchboard and test house')

# Add the actual app footer structure to the full My Day phone mock only.
if 'class="myday-app-footer"' not in html:
    css = r'''
<style id="myday-footer-styles">
.myday-device{display:flex;flex-direction:column}
.myday-device .mock-body{flex:1;overflow:hidden}
.myday-app-footer{height:55px;background:#fff;border-top:1px solid #e7ebef;display:grid;grid-template-columns:repeat(5,1fr);align-items:end;padding:4px 5px 5px;flex:0 0 auto}
.myday-app-nav{display:flex;flex-direction:column;align-items:center;justify-content:flex-end;gap:2px;color:#929eaa;font-size:7px;font-weight:750;height:45px}
.myday-app-nav svg{width:15px;height:15px;stroke:currentColor;fill:none;stroke-width:1.8}
.myday-app-nav.active{color:#2D5BE3}
.myday-app-nav.memo{position:relative}
.myday-app-nav.memo .myday-memo-circle{width:30px;height:30px;border-radius:50%;background:#2D5BE3;display:grid;place-items:center;color:#fff;margin-top:-13px;box-shadow:0 4px 11px rgba(45,91,227,.28)}
.myday-app-nav.memo .myday-memo-circle svg{width:16px;height:16px}
.myday-app-nav.memo span{margin-top:0}
</style>
'''
    html = html.replace('</head>', css + '\n</head>', 1)

    old = '''    <div class="mock-note">Tasks only. Reminders stay in their own list.</div>\n  </div>\n</div>'''
    footer = '''    <div class="mock-note">Tasks only. Reminders stay in their own list.</div>\n  </div>\n  <div class="myday-app-footer" aria-label="SoleTasker app footer navigation">\n    <div class="myday-app-nav active"><svg viewBox="0 0 24 24"><rect x="4" y="4" width="6" height="6" rx="1"/><rect x="14" y="4" width="6" height="6" rx="1"/><rect x="4" y="14" width="6" height="6" rx="1"/><rect x="14" y="14" width="6" height="6" rx="1"/></svg><span>Home</span></div>\n    <div class="myday-app-nav"><svg viewBox="0 0 24 24"><path d="M4 7h16v13H4z"/><path d="M8 7V4h8v3"/></svg><span>Jobs</span></div>\n    <div class="myday-app-nav memo"><div class="myday-memo-circle"><svg viewBox="0 0 24 24"><rect x="9" y="3" width="6" height="12" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v3"/></svg></div><span>Memo</span></div>\n    <div class="myday-app-nav"><svg viewBox="0 0 24 24"><path d="M9 11l2 2 4-4"/><rect x="4" y="4" width="16" height="16" rx="2"/></svg><span>Tasks</span></div>\n    <div class="myday-app-nav"><svg viewBox="0 0 24 24"><path d="M5 7h14M5 12h14M5 17h14"/></svg><span>More</span></div>\n  </div>\n</div>'''

    # The first matching note belongs to the compact deck mock. Target the full My Day device
    # by locating it first, then replace within that slice only.
    device_start = html.find('<div class="myday-device"')
    if device_start == -1:
        raise SystemExit('Full My Day device not found')
    tail = html[device_start:]
    note_pos = tail.find(old)
    if note_pos == -1:
        raise SystemExit('My Day footer insertion point not found')
    absolute = device_start + note_pos
    html = html[:absolute] + footer + html[absolute + len(old):]

# Latest approved landing-page copy.
html = html.replace('garage sub-board', 'switchboard upgrade')
html = html.replace(
    '''LIGHTWEIGHT JOB MANAGEMENT
      <span class="hl">FOR SOLE TRADERS AND SMALL TEAMS.</span>''',
    '''VOICE TO TASK JOB MANAGEMENT
      <span class="hl">FOR SOLE TRADERS AND SMALL TEAMS</span>'''
)
html = html.replace(
    '''VOICE TO TASK JOB MANAGEMENT
      <span class="hl">FOR SOLE TRADERS AND SMALL TEAMS.</span>''',
    '''VOICE TO TASK JOB MANAGEMENT
      <span class="hl">FOR SOLE TRADERS AND SMALL TEAMS</span>'''
)

# Reorder the lower landing-page story without redesigning any feature content.
# Old: Intake -> Smart Tools -> Real Cost -> Pricing -> Use Cases -> Built by Tradies
# New: Smart Tools -> Real Cost -> Use Cases -> Built by Tradies -> Intake -> Pricing
# Search only inside <body> so similarly named CSS comments in <head> cannot be mistaken for sections.
body_start = html.find('<body')
if body_start == -1:
    raise SystemExit('Body start not found')

def comment_start(keyword: str) -> int:
    keyword_pos = html.find(keyword, body_start)
    if keyword_pos == -1:
        raise SystemExit(f'Section marker not found: {keyword}')
    start = html.rfind('<!--', body_start, keyword_pos)
    if start == -1:
        raise SystemExit(f'Section comment start not found: {keyword}')
    return start

intake_start = comment_start('JOB INTAKE — dark, high presence')
smart_start = comment_start('FEATURE CARDS — 3 key differentiators')
pain_start = comment_start('PAIN — editorial two-col layout')
pricing_start = html.find('<!-- pricing teaser -->', body_start)
use_cases_start = comment_start('CTA INTERRUPT — use cases band')
bbt_start = comment_start('BUILT BY TRADIES + FORM')
close_start = comment_start('CLOSE')

if pricing_start == -1:
    raise SystemExit('Pricing teaser marker not found')

old_order = intake_start < smart_start < pain_start < pricing_start < use_cases_start < bbt_start < close_start
new_order = smart_start < pain_start < use_cases_start < bbt_start < intake_start < pricing_start < close_start

if old_order:
    intake_block = html[intake_start:smart_start]
    smart_block = html[smart_start:pain_start]
    pain_block = html[pain_start:pricing_start]
    pricing_block = html[pricing_start:use_cases_start]
    use_cases_block = html[use_cases_start:bbt_start]
    bbt_block = html[bbt_start:close_start]

    html = (
        html[:intake_start]
        + smart_block
        + pain_block
        + use_cases_block
        + bbt_block
        + intake_block
        + pricing_block
        + html[close_start:]
    )
elif not new_order:
    raise SystemExit('Landing sections are in an unexpected order; refusing to reshuffle them')

# Background-only visual rhythm pass for the reordered sections.
# Use Cases becomes a clean white break after the long dark Real Cost section.
body_start = html.find('<body')
use_start = comment_start('CTA INTERRUPT — use cases band')
built_start = comment_start('BUILT BY TRADIES + FORM')
use_block = html[use_start:built_start]
use_block = use_block.replace('background:var(--navy);padding:56px 32px;text-align:center', 'background:var(--white);padding:56px 32px;text-align:center', 1)
use_block = use_block.replace('color:var(--white)!important', 'color:var(--sole-blue)!important', 1)
use_block = use_block.replace('color:rgba(255,255,255,.55)', 'color:var(--ink-soft)', 1)
use_block = use_block.replace('color:rgba(255,255,255,.3);margin-top:14px', 'color:var(--ink-ghost);margin-top:14px', 1)
html = html[:use_start] + use_block + html[built_start:]

# Give the Built by Tradies / Why We Built It section a very light blue-grey background
# so it stays distinct from the new white Use Cases band without changing its content.
html = html.replace(
    '.bbt-sec{\n  background:var(--white);padding:100px 32px;',
    '.bbt-sec{\n  background:#F4F7FB;padding:100px 32px;',
    1,
)

path.write_text(html, encoding='utf-8')
print('Updated My Day mock, approved copy, section order and landing colour rhythm')
