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
/* Compact smart-tools pass: same interaction, tighter section, uniform mock crop */
.smart-onsite-sec{padding:66px 32px 68px!important}
.smart-onsite-head{margin-bottom:24px!important;max-width:720px!important}
.smart-onsite-intro{font-size:16px!important;line-height:1.62!important;max-width:620px!important;color:#667385!important}
.smart-tools-shell{grid-template-columns:minmax(0,1fr) 420px!important;gap:48px!important;align-items:start!important}
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

/* Same outer size for every state. Do not show a full blank phone. */
.smart-phone{height:468px!important;max-width:420px!important;border-width:7px!important;border-radius:28px!important}
.smart-phone-top{height:55px!important;flex:0 0 55px!important}
.smart-phone-body{height:346px!important;flex:0 0 346px!important;padding:14px!important;overflow:hidden!important;position:relative!important;align-items:flex-start!important}
.smart-state{height:100%!important;overflow:hidden!important}
.smart-card{min-height:232px!important;padding:15px!important}
.smart-phone-footer{height:60px!important;flex:0 0 60px!important;position:relative!important;z-index:8!important}

/* Soft crop so every state ends consistently rather than exposing blank white space. */
.smart-phone-body:after{content:'';position:absolute;left:0;right:0;bottom:0;height:64px;background:linear-gradient(to bottom,rgba(247,249,251,0),rgba(247,249,251,.76) 46%,#f7f9fb 100%);pointer-events:none;z-index:7}
.smart-phone-caption{margin-top:8px!important;font-size:10px!important}

@media(max-width:900px){
  .smart-tools-shell{grid-template-columns:1fr!important;gap:26px!important}
  .smart-tools-rail{max-width:none!important}
  .smart-phone-wrap{justify-content:flex-start!important}
}
@media(max-width:640px){
  .smart-onsite-sec{padding:54px 20px 58px!important}
  .smart-onsite-head{margin-bottom:20px!important}
  .smart-tools-shell{gap:22px!important}
  .smart-quick{height:56px!important;font-size:9.5px!important}
  .smart-feature-btn{height:50px!important;font-size:10.5px!important;padding:0 10px!important}
  .smart-phone-wrap{justify-content:center!important}
  .smart-phone{height:440px!important;max-width:380px!important;border-width:6px!important;border-radius:25px!important}
  .smart-phone-top{height:53px!important;flex-basis:53px!important}
  .smart-phone-body{height:322px!important;flex-basis:322px!important;padding:12px!important}
  .smart-phone-footer{height:59px!important;flex-basis:59px!important}
  .smart-card{min-height:214px!important;padding:13px!important}
}
</style>
'''

html = html.replace('</head>', css + '\n</head>', 1)
path.write_text(html, encoding='utf-8')
print('Applied compact smart-tools layout overrides')
