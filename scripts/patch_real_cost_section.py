from pathlib import Path

path = Path('index.html')
html = path.read_text(encoding='utf-8')
start_marker = '<section class="pain-sec" id="pain">'
if start_marker not in html:
    raise SystemExit('Pain section not found')
start = html.index(start_marker)
end = html.index('</section>', start) + len('</section>')

new = r'''<section class="pain-sec lovable-real-cost" id="pain">
  <style>
    .lovable-real-cost{background:#1c2a39;padding:84px 32px 94px;color:#fff}
    .lovable-real-cost .real-cost-wrap{max-width:1100px;margin:0 auto}
    .lovable-real-cost .real-cost-kicker{font-family:var(--fh);font-size:18px;letter-spacing:.18em;color:#5ec4af;margin-bottom:34px}
    .lovable-real-cost .real-cost-title{font-family:var(--fh);font-size:clamp(52px,7vw,82px);line-height:.92;letter-spacing:.01em;color:#fff;max-width:900px;margin:0 0 38px}
    .lovable-real-cost .real-cost-title span{display:block;color:#5ec4af}
    .lovable-real-cost .real-cost-copy{max-width:820px;color:rgba(255,255,255,.72);font-size:clamp(18px,2vw,22px);line-height:1.72;margin-bottom:34px}
    .lovable-real-cost .real-cost-copy strong{color:#fff;font-weight:800}
    .lovable-real-cost .real-cost-quote{max-width:860px;border-left:4px solid #5ec4af;padding:0 0 0 28px;margin:0 0 34px;font-size:clamp(24px,3vw,34px);line-height:1.38;color:#fff}
    .lovable-real-cost .real-cost-follow{max-width:820px;color:rgba(255,255,255,.62);font-size:clamp(17px,1.9vw,21px);line-height:1.72;margin-bottom:34px}
    .lovable-real-cost .real-cost-cta{display:inline-flex;align-items:center;justify-content:center;background:#62c0ad;color:#fff;font-weight:900;font-size:18px;border-radius:999px;padding:16px 30px;margin-bottom:64px;box-shadow:0 10px 26px rgba(44,185,157,.18)}
    .lovable-real-cost .real-cost-cards{display:grid;gap:22px}
    .lovable-real-cost .real-cost-card{background:#2b3948;border:1px solid rgba(255,255,255,.14);border-radius:28px;padding:30px 32px}
    .lovable-real-cost .real-cost-card h3{font-family:var(--fb);font-size:clamp(21px,2.4vw,27px);line-height:1.32;font-weight:900;color:#fff;margin:0 0 14px}
    .lovable-real-cost .real-cost-card p{font-size:clamp(17px,1.9vw,21px);line-height:1.72;color:rgba(255,255,255,.68);margin:0 0 18px}
    .lovable-real-cost .real-cost-card .impact{font-size:clamp(14px,1.6vw,17px);font-weight:900;letter-spacing:.03em;color:#5ec4af;text-transform:uppercase;margin:0}
    @media(min-width:900px){.lovable-real-cost .real-cost-cards{grid-template-columns:1fr 1fr}.lovable-real-cost .real-cost-card:last-child{grid-column:1 / -1}}
    @media(max-width:640px){.lovable-real-cost{padding:44px 24px 70px}.lovable-real-cost .real-cost-kicker{font-size:14px;margin-bottom:28px}.lovable-real-cost .real-cost-title{font-size:56px;margin-bottom:30px}.lovable-real-cost .real-cost-copy{font-size:18px}.lovable-real-cost .real-cost-quote{font-size:27px;padding-left:22px}.lovable-real-cost .real-cost-follow{font-size:18px}.lovable-real-cost .real-cost-cta{font-size:17px;padding:15px 28px;margin-bottom:46px}.lovable-real-cost .real-cost-card{padding:25px 24px;border-radius:26px}.lovable-real-cost .real-cost-card h3{font-size:22px}.lovable-real-cost .real-cost-card p{font-size:17px}.lovable-real-cost .real-cost-card .impact{font-size:15px}}
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
path.write_text(html, encoding='utf-8')
print('Replaced live white pain section with Lovable real-cost design')
