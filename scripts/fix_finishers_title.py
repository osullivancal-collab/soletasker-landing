from pathlib import Path

path = Path('index.html')
html = path.read_text(encoding='utf-8')
old = '''<h2 style="font-family:var(--fh);font-size:clamp(48px,6vw,68px);color:var(--teal);line-height:.94;letter-spacing:.4px;margin:0 0 34px">SWMS.</h2>'''
new = '''<h2 style="font-family:var(--fh);font-size:clamp(48px,6vw,68px);color:var(--navy);line-height:.94;letter-spacing:.4px;margin:0 0 34px">WHILE YOU'RE STILL ON SITE.<span style="display:block;color:var(--teal)">REQUEST THE REVIEW. TAG THE FUTURE WORK. SEND THE SWMS.</span></h2>'''
if old not in html:
    raise SystemExit('Expected finishers heading not found')
html = html.replace(old, new, 1)
path.write_text(html, encoding='utf-8')
print('Corrected finishers title')
