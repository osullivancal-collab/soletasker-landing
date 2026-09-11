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
print('Applied canonical SoleTasker title blue, dark-section contrast, and canonical logo reference')
