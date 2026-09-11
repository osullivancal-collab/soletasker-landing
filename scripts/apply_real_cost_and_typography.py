from pathlib import Path

path = Path('index.html')
html = path.read_text(encoding='utf-8')

# Replace the current problem/pain section with the supplied Lovable Real Cost direction.
start_marker = '<section class="pain-sec" id="pain">'
new_marker = '<section class="pain-sec lovable-real-cost" id="pain">'

if start_marker in html:
    start = html.index(start_marker)
    end = html.index('</section>', start) + len('</section>')
    new = r'''<section class="pain-sec lovable-real-cost" id="pain">
  <style>
    .lovable-real-cost{background:#1c2a39;padding:76px 32px 88px;color:#fff}
    .lovable-real-cost .real-cost-wrap{max-width:1100px;margin:0 auto}
    .lovable-real-cost .real-cost-kicker{font-family:var(--fh);font-size:14px;letter-spacing:.18em;color:#5ec4af;margin-bottom:24px}
    .lovable-real-cost .real-cost-title{font-family:var(--fh);font-size:clamp(42px,4.8vw,58px);line-height:.96;letter-spacing:.01em;color:#fff;max-width:860px;margin:0 0 28px}
    .lovable-real-cost .real-cost-title span{display:block;color:#5ec4af}
    .lovable-real-cost .real-cost-copy{max-width:780px;color:rgba(255,255,255,.72);font-size:17px;line-height:1.72;margin-bottom:28px}
    .lovable-real-cost .real-cost-copy strong{color:#fff;font-weight:800}
    .lovable-real-cost .real-cost-quote{max-width:820px;border-left:3px solid #5ec4af;padding:0 0 0 22px;margin:0 0 28px;font-size:22px;line-height:1.45;color:#fff}
    .lovable-real-cost .real-cost-follow{max-width:780px;color:rgba(255,255,255,.62);font-size:17px;line-height:1.72;margin-bottom:28px}
    .lovable-real-cost .real-cost-cta{display:inline-flex;align-items:center;justify-content:center;background:#62c0ad;color:#fff;font-weight:900;font-size:16px;border-radius:999px;padding:14px 28px;margin-bottom:52px;box-shadow:0 10px 26px rgba(44,185,157,.18)}
    .lovable-real-cost .real-cost-cards{display:grid;gap:18px}
    .lovable-real-cost .real-cost-card{background:#2b3948;border:1px solid rgba(255,255,255,.14);border-radius:24px;padding:26px 28px}
    .lovable-real-cost .real-cost-card h3{font-family:var(--fb);font-size:21px;line-height:1.34;font-weight:900;color:#fff;margin:0 0 10px}
    .lovable-real-cost .real-cost-card p{font-size:16px;line-height:1.7;color:rgba(255,255,255,.68);margin:0 0 15px}
    .lovable-real-cost .real-cost-card .impact{font-size:14px;font-weight:900;letter-spacing:.03em;color:#5ec4af;text-transform:uppercase;margin:0}
    @media(min-width:900px){.lovable-real-cost .real-cost-cards{grid-template-columns:1fr 1fr}.lovable-real-cost .real-cost-card:last-child{grid-column:1 / -1}}
    @media(max-width:640px){
      .lovable-real-cost{padding:52px 24px 68px}
      .lovable-real-cost .real-cost-kicker{font-size:12px;margin-bottom:20px}
      .lovable-real-cost .real-cost-title{font-size:42px;margin-bottom:24px}
      .lovable-real-cost .real-cost-copy{font-size:16px;line-height:1.68}
      .lovable-real-cost .real-cost-quote{font-size:20px;padding-left:18px}
      .lovable-real-cost .real-cost-follow{font-size:16px}
      .lovable-real-cost .real-cost-cta{font-size:15px;padding:13px 24px;margin-bottom:40px}
      .lovable-real-cost .real-cost-card{padding:22px 22px;border-radius:22px}
      .lovable-real-cost .real-cost-card h3{font-size:20px}
      .lovable-real-cost .real-cost-card p{font-size:16px}
      .lovable-real-cost .real-cost-card .impact{font-size:13px}
    }
  </style>
  <div class="real-cost-wrap">
    <div class="real-cost-kicker">THE REAL COST</div>
    <h2 class="real-cost-title">YOU'RE ALREADY DOING THE HARD PART.<span>THE PAPERWORK JUST NEEDS SOMEWHERE TO LIVE.</span></h2>
    <p class="real-cost-copy">Between jobs, calls and quotes, the follow-ups end up in your head. That's normal — there's only so much one person can hold. <strong>You don't need to try harder. You need a place to put it.</strong></p>
    <div class="real-cost-quote">“We don't manage your jobs. We make sure nothing in them gets missed.”</div>
    <p class="real-cost-follow">Capture it when it happens. Action it when it's due. Keep work moving. Keep cashflow moving.</p>
    <a class="real-cost-cta" href="https://app.soletasker.com.au/signup">Get Started</a>
    <div class="real-cost-cards">
      <article class="real-cost-card"><h3>Invoice you forgot to send</h3><p>Job done. On to the next one. Six weeks later — it hits you. That invoice never went out. That money is yours. It's just not in your account.</p><p class="impact">↑ THAT'S REAL MONEY GONE</p></article>
      <article class="real-cost-card"><h3>Photos buried in your camera roll</h3><p>Before shots, after shots, damage proof — mixed in with 4,000 personal photos. Client disputes the job. You spend an hour finding nothing.</p><p class="impact">↑ A LIABILITY YOU CAN'T DEFEND</p></article>
      <article class="real-cost-card"><h3>Cert saved somewhere — but where</h3><p>Email? Screenshot? WhatsApp? The inspector wants it now. You're digging. It's somewhere. You hope.</p><p class="impact">↑ THAT'S A COMPLIANCE RISK</p></article>
      <article class="real-cost-card"><h3>Job details on a receipt in the van</h3><p>Client name, address, what they need — written on the nearest scrap. It's in the van. Or it was. Either way, it's not where you need it right now.</p><p class="impact">↑ EVERY WEEK, SAME STORY</p></article>
      <article class="real-cost-card"><h3>Cashflow slower than it should be</h3><p>Work's done and you're flat out, but invoices go out late and follow-ups wait. Nothing wrong with the business — the admin just has nowhere to sit.</p><p class="impact">↑ THIS IS THE FIX</p></article>
    </div>
  </div>
</section>'''
    html = html[:start] + new + html[end:]

# Normalise the approved on-site / review / future-work / SWMS section so it uses
# the same hierarchy as the rest of SoleTasker instead of the oversized Lovable scale.
finish_start_marker = '<section class="site-finishers-sec"'
if finish_start_marker in html:
    fs = html.index(finish_start_marker)
    fe = html.index('</section>', fs) + len('</section>')
    section = html[fs:fe]
    section = section.replace('font-size:clamp(48px,6vw,68px)', 'font-size:clamp(40px,4.6vw,54px)')
    section = section.replace('font-size:clamp(17px,2vw,21px)', 'font-size:17px')
    section = section.replace('font-size:clamp(20px,2.5vw,25px)', 'font-size:21px')
    section = section.replace('font-size:clamp(16px,2vw,19px)', 'font-size:16px')
    html = html[:fs] + section + html[fe:]

path.write_text(html, encoding='utf-8')
print('Applied cumulative Real Cost section and normalized recent-section typography')
