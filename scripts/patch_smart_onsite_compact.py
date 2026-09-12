from pathlib import Path

path = Path('index.html')
html = path.read_text(encoding='utf-8')

STYLE_ID = 'smart-onsite-compact-overrides'
if f'id="{STYLE_ID}"' in html:
    start = html.index(f'<style id="{STYLE_ID}">')
    end = html.index('</style>', start) + len('</style>')
    html = html[:start] + html[end:]

css = r'''
<style id="smart-onsite-compact-overrides">
/* Smart-tools extracted-panel pass: preserve interaction, remove duplicate phone chrome. */
.smart-onsite-sec{padding:66px 32px 72px!important}
.smart-onsite-head{margin-bottom:26px!important;max-width:720px!important}
.smart-onsite-intro{font-size:16px!important;line-height:1.62!important;max-width:620px!important;color:#667385!important}
.smart-tools-shell{grid-template-columns:minmax(0,1fr) 460px!important;gap:58px!important;align-items:start!important}
.smart-tools-rail{max-width:520px!important;padding-top:0!important;align-self:start!important}
.smart-rail-group+.smart-rail-group{margin-top:16px!important}
.smart-rail-label{color:#6f7f91!important;margin-bottom:8px!important}

.smart-quick{height:60px!important;border:1.5px solid #c8d2dc!important;background:#f8fafc!important;color:#1B2B6B!important;border-radius:12px!important;font-weight:900!important;box-shadow:0 2px 7px rgba(28,43,58,.05)!important}
.smart-quick svg{stroke:#1E9C83!important;stroke-width:2!important}
.smart-quick:hover,.smart-quick:focus-visible{background:#fff!important;border-color:#2CB99D!important;box-shadow:0 7px 18px rgba(28,43,58,.09)!important}

.smart-feature-btn{height:54px!important;border:1.5px solid #bbc7d2!important;background:#fff!important;color:#1B2B6B!important;font-weight:900!important;box-shadow:0 2px 8px rgba(28,43,58,.045)!important}
.smart-feature-btn .sf-ic{background:#e8f6f3!important;color:#1E9C83!important}
.smart-feature-btn:hover,.smart-feature-btn:focus-visible{border-color:#2CB99D!important;transform:translateY(-1px)!important}
.smart-feature-btn.active{background:#1C2B3A!important;border-color:#1C2B3A!important;color:#fff!important;box-shadow:0 8px 20px rgba(28,43,58,.16)!important}
.smart-feature-btn.active .sf-ic{background:rgba(44,185,157,.14)!important;color:#2CB99D!important}

/* Extract the useful app containers instead of showing another full device mock. */
.smart-phone-wrap{justify-content:center!important;align-items:flex-start!important;position:relative!important;height:500px!important;min-height:500px!important;padding:10px 0 0!important}
.smart-phone-wrap:before{content:'';position:absolute;inset:30px 18px 112px;border-radius:30px;background:linear-gradient(145deg,rgba(45,91,227,.045),rgba(44,185,157,.055));border:1px solid rgba(28,43,58,.055);transform:rotate(-1deg);pointer-events:none}
.smart-phone-wrap>div{width:100%!important;max-width:440px!important;display:flex!important;flex-direction:column!important;height:100%!important;position:relative!important;z-index:1!important}
.smart-phone{width:100%!important;max-width:440px!important;height:auto!important;min-height:0!important;background:transparent!important;border:0!important;border-radius:0!important;box-shadow:none!important;overflow:visible!important;display:block!important;color:#18283a!important;position:relative!important;z-index:1!important}
.smart-phone-top,.smart-phone-footer{display:none!important}
.smart-phone-body{height:382px!important;min-height:382px!important;flex:none!important;padding:18px!important;background:transparent!important;overflow:visible!important;display:flex!important;align-items:flex-start!important;justify-content:center!important;position:relative!important}
.smart-phone-body:after{display:none!important}
.smart-state{width:100%!important;height:auto!important;overflow:visible!important}
.smart-state>div{width:100%;animation:smartPanelIn .32s cubic-bezier(.2,.72,.2,1) both}
@keyframes smartPanelIn{from{opacity:0;transform:translateY(10px) scale(.988)}to{opacity:1;transform:none}}

.smart-screen-title{display:inline-flex!important;align-items:center!important;gap:7px!important;margin:0 0 10px 4px!important;padding:6px 10px!important;border:1px solid rgba(44,185,157,.2)!important;border-radius:999px!important;background:rgba(255,255,255,.88)!important;color:#647486!important;box-shadow:0 4px 12px rgba(28,43,58,.045)!important}
.smart-screen-title:before{content:'';width:6px;height:6px;border-radius:50%;background:#2CB99D;box-shadow:0 0 0 4px rgba(44,185,157,.1)}
.smart-card{min-height:0!important;padding:18px!important;border:1px solid #dce4ea!important;border-radius:20px!important;background:rgba(255,255,255,.97)!important;box-shadow:0 20px 48px rgba(28,43,58,.105)!important}
.smart-card+.smart-card{margin-top:10px!important}
.smart-meta{gap:9px!important;margin-bottom:10px!important}
.smart-meta-box{border-color:#dde5eb!important;border-radius:13px!important;box-shadow:0 9px 24px rgba(28,43,58,.055)!important}
.smart-note-box{background:#f7fafb!important;border-left-color:#2CB99D!important}
.smart-status-strip{background:#eef9f6!important}
.smart-field{border-color:#dfe6ec!important;background:#fff!important}
.smart-scan-drop{border-color:#a7cfee!important;background:rgba(247,251,255,.96)!important;box-shadow:0 12px 30px rgba(28,43,58,.055)!important}
.smart-toast{top:3px!important;box-shadow:0 12px 28px rgba(28,43,58,.2)!important}

/* Fixed copy zone prevents layout shift while explaining each active tool. */
.smart-phone-caption{display:none!important}
.smart-tool-copy{height:98px;min-height:98px;padding:12px 20px 0;text-align:left;transition:opacity .18s ease,transform .18s ease}
.smart-tool-copy.swap{opacity:.25;transform:translateY(3px)}
.smart-tool-copy strong{display:block;font-size:14px;line-height:1.35;color:#1B2B6B;margin-bottom:5px;font-weight:900}
.smart-tool-copy span{display:block;font-size:12.5px;line-height:1.55;color:#697786;max-width:410px}

@media(max-width:900px){
  .smart-tools-shell{grid-template-columns:1fr!important;gap:28px!important}
  .smart-tools-rail{max-width:none!important}
  .smart-phone-wrap{justify-content:center!important;height:500px!important;min-height:500px!important}
}
@media(max-width:640px){
  .smart-onsite-sec{padding:54px 20px 60px!important}
  .smart-onsite-head{margin-bottom:20px!important}
  .smart-tools-shell{gap:20px!important}
  .smart-quick{height:56px!important;font-size:9.5px!important}
  .smart-feature-btn{height:50px!important;font-size:10.5px!important;padding:0 10px!important}
  .smart-phone-wrap{height:530px!important;min-height:530px!important;padding:2px 0 0!important}
  .smart-phone-wrap:before{inset:26px 4px 122px;border-radius:24px!important}
  .smart-phone-wrap>div{max-width:100%!important}
  .smart-phone{max-width:100%!important}
  .smart-phone-body{height:402px!important;min-height:402px!important;padding:14px 8px!important}
  .smart-card{padding:15px!important;border-radius:17px!important}
  .smart-card h3{font-size:16px!important}
  .smart-meta{grid-template-columns:1fr 1fr!important;gap:7px!important}
  .smart-screen-title{margin-left:2px!important}
  .smart-tool-copy{height:112px;min-height:112px;padding:12px 12px 0}
  .smart-tool-copy strong{font-size:13.5px}
  .smart-tool-copy span{font-size:12px;line-height:1.5}
}
@media(prefers-reduced-motion:reduce){.smart-state>div{animation:none!important}.smart-tool-copy{transition:none!important}}
</style>
'''

# Replace the generic cycling caption with state-specific explanatory copy.
caption = '<div class="smart-phone-caption">Auto-cycling through the smart tools. <strong>Tap any tool to jump to it.</strong></div>'
copy_block = '<div class="smart-tool-copy" data-smart-copy aria-live="polite"><strong>Get the review while the job is fresh.</strong><span>Send or copy your review link before you leave site, instead of remembering to chase it later.</span></div>'
if caption in html:
    html = html.replace(caption, copy_block, 1)
elif 'data-smart-copy' not in html:
    raise RuntimeError('Smart tools caption anchor not found')

# Extend the existing interaction script so the explanation follows the active state.
copy_anchor = "const toast=root.querySelector('[data-smart-toast]');"
if "const copy=root.querySelector('[data-smart-copy]');" not in html:
    html = html.replace(copy_anchor, copy_anchor + "\n    const copy=root.querySelector('[data-smart-copy]');", 1)

states_anchor = "    let current=0;"
copy_texts = """    const copyTexts={
      review:['Get the review while the job is fresh.','Send or copy your review link before you leave site, instead of remembering to chase it later.'],
      future:[\"Don't lose the ‘maybe later’ work.\",'Customer mentions an EV charger, garage sub-board or another future job? Tag it against the job so you can come back to it later.'],
      swms:['Check it, sign it, send it.','Keep the site and work details together, review the SWMS, then sign and send it from the job.'],
      scan:['Turn a work order into usable details.','Scan a work order or upload a PDF to pull out the site, contact and order details fast — then check them before saving.']
    };
"""
if 'const copyTexts={' not in html:
    html = html.replace(states_anchor, copy_texts + states_anchor, 1)

show_anchor = "      state.innerHTML=states[key];"
show_copy = """      state.innerHTML=states[key];
      if(copy&&copyTexts[key]){
        copy.classList.add('swap');
        window.setTimeout(()=>{
          copy.innerHTML='<strong>'+copyTexts[key][0]+'</strong><span>'+copyTexts[key][1]+'</span>';
          copy.classList.remove('swap');
        },90);
      }"""
if "copy.classList.add('swap')" not in html:
    html = html.replace(show_anchor, show_copy, 1)

html = html.replace('</head>', css + '\n</head>', 1)
path.write_text(html, encoding='utf-8')
print('Applied stable extracted smart-tools panels with descriptions')
