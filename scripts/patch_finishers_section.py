from pathlib import Path

path = Path('index.html')
html = path.read_text(encoding='utf-8')

marker = 'FEATURE CARDS — 3 key differentiators'
if marker not in html:
    raise SystemExit('Feature cards marker not found')

marker_pos = html.index(marker)
section_start = html.index('<section', marker_pos)
section_end = html.index('</section>', section_start) + len('</section>')

new_section = r'''<section class="site-finishers-sec" style="background:var(--white);padding:74px 24px 82px">
  <div style="max-width:760px;margin:0 auto">
    <h2 style="font-family:var(--fh);font-size:clamp(48px,6vw,68px);color:var(--teal);line-height:.94;letter-spacing:.4px;margin:0 0 34px">SWMS.</h2>

    <p style="font-size:clamp(17px,2vw,21px);color:#70798a;line-height:1.72;margin:0 0 42px;max-width:700px">Customer mentioned an EV charger or switchboard upgrade? Tag it before you leave — it'll be waiting when things go quiet.</p>

    <div style="display:flex;flex-direction:column;gap:22px">
      <div style="background:#fff;border:1px solid #e3e7ec;border-radius:28px;padding:29px 30px;box-shadow:0 12px 30px rgba(28,43,58,.09)">
        <h3 style="font-family:var(--fb);font-size:clamp(20px,2.5vw,25px);font-weight:900;color:var(--navy);line-height:1.34;margin:0 0 14px">Get the 5-star review before you're back in the van.</h3>
        <p style="font-size:clamp(16px,2vw,19px);color:#788190;line-height:1.55;margin:0">One tap. While you're packing up.</p>
      </div>

      <div style="background:#fff;border:1px solid #e3e7ec;border-radius:28px;padding:29px 30px;box-shadow:0 12px 30px rgba(28,43,58,.09)">
        <h3 style="font-family:var(--fb);font-size:clamp(20px,2.5vw,25px);font-weight:900;color:var(--navy);line-height:1.34;margin:0 0 14px">Fill the gaps when you're quiet.</h3>
        <p style="font-size:clamp(16px,2vw,19px);color:#788190;line-height:1.55;margin:0">Tag future work. Call them when things slow down.</p>
      </div>

      <div style="background:#fff;border:1px solid #e3e7ec;border-radius:28px;padding:29px 30px;box-shadow:0 12px 30px rgba(28,43,58,.09)">
        <h3 style="font-family:var(--fb);font-size:clamp(20px,2.5vw,25px);font-weight:900;color:var(--navy);line-height:1.34;margin:0 0 14px">Pre-filled SWMS. Sent in 60 seconds.</h3>
        <p style="font-size:clamp(16px,2vw,19px);color:#788190;line-height:1.55;margin:0">Sign with your finger. Email the builder. Done.</p>
      </div>
    </div>
  </div>
</section>'''

html = html[:section_start] + new_section + html[section_end:]
path.write_text(html, encoding='utf-8')
print('Replaced differentiator block with light on-brand finishers section')
