from pathlib import Path

path = Path('index.html')
html = path.read_text(encoding='utf-8')

# Keep the final CTA within SoleTasker's existing typography scale.
html = html.replace(
    ".close-sec{\n  background:var(--navy);padding:100px 32px;",
    ".close-sec{\n  background:var(--navy);padding:78px 32px;"
)
html = html.replace(
    "font-family:var(--fh);font-size:clamp(60px,8.5vw,112px);",
    "font-family:var(--fh);font-size:clamp(40px,4.8vw,58px);"
)
html = html.replace(
    "font-size:19px;color:rgba(255,255,255,.45);\n  max-width:420px;margin:0 auto 40px;line-height:1.7;",
    "font-size:17px;color:rgba(255,255,255,.62);\n  max-width:620px;margin:0 auto 32px;line-height:1.68;"
)

# Replace only the final closing section content. Keep the original title and CTA language.
start_marker = '<section class="close-sec">'
if start_marker not in html:
    raise SystemExit('Final CTA section not found')
start = html.index(start_marker)
end = html.index('</section>', start) + len('</section>')

new = '''<section class="close-sec">
  <div class="rev">
    <h2 class="close-h">
      Say it.<br/>It's done.<br/>
      <span class="a">Not forgotten.</span>
    </h2>
    <p class="close-p">
      Running a small trade business already means carrying enough. SoleTasker gives the admin somewhere to land, so work keeps moving, follow-ups happen when they should, and the important things aren't left relying on memory.
    </p>
    <a href="https://app.soletasker.com.au/signup" class="btn-teal lg" style="display:inline-flex;margin:0 auto">Count Me In</a>
    <p class="close-tagline"><span>say it once</span> · done · not forgotten</p>
  </div>
</section>'''

html = html[:start] + new + html[end:]
path.write_text(html, encoding='utf-8')
print('Restored final CTA title and updated closing business-value copy')
