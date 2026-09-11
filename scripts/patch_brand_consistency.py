from pathlib import Path
import re

path = Path('index.html')
html = path.read_text(encoding='utf-8')

# Light-section title blue: use the same deep SoleTasker blue family as the app,
# rather than the previous grey-blue.
html = html.replace(':root{--sole-blue:#53617C}', ':root{--sole-blue:#1B2B6B}')
html = html.replace(':root{--sole-blue:#405F8A}', ':root{--sole-blue:#1B2B6B}')

# Dark navy sections must never inherit the light-section Sole-blue heading rule.
# Keep their main title white, while existing teal accent spans remain teal.
dark_override = '''
/* Dark-section title contrast: white title, teal accent. */
section[style*="background:var(--navy)"] h1,
section[style*="background:var(--navy)"] h2,
section[style*="background:var(--navy)"] h3,
section[style*="background:var(--navy)"] h4{
  color:var(--white)!important;
}
'''
if 'Dark-section title contrast: white title, teal accent.' not in html:
    marker = '</style>\n\n</head>'
    if marker in html:
        html = html.replace(marker, dark_override + '</style>\n\n</head>', 1)
    else:
        html = html.replace('</head>', '<style>' + dark_override + '</style>\n</head>', 1)

# Force the Use Cases interrupt heading white. Its original inline white colour can
# otherwise lose to the later global light-section heading rule because that rule
# uses !important.
use_cases_h2 = '<h2 style="font-family:var(--fh);font-size:clamp(32px,5vw,56px);color:var(--white);line-height:.93;margin-bottom:16px">'
use_cases_h2_fixed = '<h2 style="font-family:var(--fh);font-size:clamp(32px,5vw,56px);color:var(--white)!important;line-height:.93;margin-bottom:16px">'
html = html.replace(use_cases_h2, use_cases_h2_fixed)

# Hero copy: small teams is enough; remove the relationship-specific wording.
html = html.replace(
    'Assign it to yourself, your partner, admin or worker.',
    'Assign it to yourself, admin or worker.'
)

# Voice-demo copy: keep the example focused on the actual task being created.
html = html.replace(
    '"Call Dave back about the Webb St quote — it\'s urgent. Assign it to Jake and flag it for follow up on the rewire job."',
    '"Call Dave back about the Webb St quote — it\'s urgent. Assign it to Jake."'
)
html = html.replace('          <span class="vd-chip vc-va">VA Follow-up</span>\n', '')

# Re-centre the shortened voice example and its remaining structured result.
voice_demo_override = '''
/* Shortened voice-demo copy is centred after removing the extra follow-up line. */
.vd-quote{text-align:center!important;}
.vd-task-body{text-align:center;}
.vd-chips{justify-content:center;}
'''
if 'Shortened voice-demo copy is centred after removing the extra follow-up line.' not in html:
    marker = '</style>\n\n</head>'
    if marker in html:
        html = html.replace(marker, voice_demo_override + '</style>\n\n</head>', 1)
    else:
        html = html.replace('</head>', '<style>' + voice_demo_override + '</style>\n</head>', 1)

# Use the canonical SoleTasker wordmark asset instead of the older embedded copy.
# Target only the navigation logo image by its alt text.
pattern = re.compile(
    r'(<img\b[^>]*?)src="data:image/png;base64,[^"]+"([^>]*alt="SoleTasker"[^>]*>)',
    re.S,
)
html, count = pattern.subn(r'\1src="/logo.png"\2', html, count=1)
if count:
    # The old embedded logo was intentionally faded; canonical wordmark should be full strength.
    html = html.replace('opacity:.75', 'opacity:1', 1)

path.write_text(html, encoding='utf-8')
print('Applied canonical brand colours/logo plus requested hero and voice-demo copy polish')
