from pathlib import Path

path = Path('index.html')
html = path.read_text(encoding='utf-8')

# Keep final CTA within the established SoleTasker type scale.
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

old = '''<section class="close-sec">
  <div class="rev">
    <h2 class="close-h">
      Say it.<br/>It's done.<br/>
      <span class="a">Not forgotten.</span>
    </h2>
    <p class="close-p">
      Speak the job. It's captured. Tasks created. Nothing slips. No more invoices forgotten. No more jobs lost in your head.
    </p>
    <a href="https://app.soletasker.com.au/signup" class="btn-teal lg" style="display:inline-flex;margin:0 auto">Count Me In</a>
    <p class="close-tagline"><span>say it once</span> · done · not forgotten</p>
  </div>
</section>'''

new = '''<section class="close-sec">
  <div class="rev">
    <span class="s-eyebrow" style="color:var(--teal);margin-bottom:14px">LIGHTWEIGHT BY DESIGN</span>
    <h2 class="close-h">
      KEEP THE JOB ADMIN<br/>
      <span class="a">OUT OF YOUR HEAD.</span>
    </h2>
    <p class="close-p">
      SoleTasker gives tasks, reminders, job notes, photos and follow-ups one place to live. Capture them as they come up, link them to the job, assign the action and come back to it when it's time.
    </p>
    <a href="https://app.soletasker.com.au/signup" class="btn-teal lg" style="display:inline-flex;margin:0 auto">Start free trial</a>
    <p class="close-tagline"><span>7 days free</span> · no card required</p>
  </div>
</section>'''

if old not in html:
    raise SystemExit('Final CTA block not found')

html = html.replace(old, new, 1)
path.write_text(html, encoding='utf-8')
print('Updated final CTA copy and reduced typography')
