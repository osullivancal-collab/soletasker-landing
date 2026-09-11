from pathlib import Path

path = Path('index.html')
html = path.read_text(encoding='utf-8')

# 1) Job Intake: remove only the CTA shown between the intake steps and the visual.
html = html.replace(
    '      <a href="https://app.soletasker.com.au/signup" class="btn-teal lg">Get Started</a>\n',
    '',
    1,
)

# 2) Job Intake terminology: the accepted/reviewable requests are seen on Home, not a dashboard.
html = html.replace(
    'A fully structured job card is waiting in your dashboard before you\'ve even called them back.',
    'A fully structured job card is waiting on Home before you\'ve even called them back.'
)
html = html.replace('<!-- CARD 2: What you see in your dashboard -->', '<!-- CARD 2: What you see on Home -->')
html = html.replace('>What you see in your dashboard</p>', '>What you see on Home</p>')
html = html.replace('>Dashboard</span>', '>Home</span>')
html = html.replace(
    'Client fills it in → lands in your dashboard ready to review',
    'Client fills it in → lands on Home ready to review'
)

# 3) Brand rule: on light sections, title/headline text uses the blue from the "Sole" wordmark.
# Dark feature sections keep their existing white/teal heading colours.
STYLE_ID = 'sole-blue-title-rule'
if f'id="{STYLE_ID}"' not in html:
    css = r'''
<style id="sole-blue-title-rule">
:root{--sole-blue:#53617C}
section:not(.hero):not(.intake-sec):not(.myday-feature):not(.lovable-real-cost):not(.close-sec) h1,
section:not(.hero):not(.intake-sec):not(.myday-feature):not(.lovable-real-cost):not(.close-sec) h2,
section:not(.hero):not(.intake-sec):not(.myday-feature):not(.lovable-real-cost):not(.close-sec) h3,
section:not(.hero):not(.intake-sec):not(.myday-feature):not(.lovable-real-cost):not(.close-sec) h4{
  color:var(--sole-blue)!important;
}
/* Keep teal accent spans/labels teal when nested inside a blue title. */
section h1 .a,section h2 .a,section h3 .a,section h4 .a,
section h1 .hl,section h2 .hl,section h3 .hl,section h4 .hl{
  color:var(--teal)!important;
}
</style>
'''
    html = html.replace('</head>', css + '\n</head>', 1)

path.write_text(html, encoding='utf-8')
print('Removed intake CTA, changed Dashboard to Home, and applied Sole-blue light-section titles')
