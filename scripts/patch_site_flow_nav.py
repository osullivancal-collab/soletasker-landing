from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def read(name: str) -> str:
    return (ROOT / name).read_text(encoding="utf-8")


def write(name: str, text: str) -> None:
    (ROOT / name).write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old in text:
        return text.replace(old, new, 1)
    if new in text:
        return text
    raise RuntimeError(f"Could not find expected source for {label}")


def replace_regex_once(text: str, pattern: str, replacement: str, label: str) -> str:
    out, count = re.subn(pattern, replacement, text, count=1, flags=re.S)
    if count == 1:
        return out
    if replacement in text:
        return text
    raise RuntimeError(f"Could not find expected block for {label}")


LANDING_DESKTOP_NAV = '''<div class="nav-links">
      <a href="/#workflow">How it works</a>
      <a href="/use-cases">Use Cases</a>
      <a href="/#intake">Job intake</a>
      <a href="/pricing">Pricing</a>
      <a href="/#faq-page">FAQ</a>
      <a href="/#access">Contact us</a>
    </div>'''

USE_CASES_DESKTOP_NAV = '''<div class="nav-links">
      <a href="/#workflow">How it works</a>
      <a href="/use-cases" class="active">Use Cases</a>
      <a href="/#intake">Job intake</a>
      <a href="/pricing">Pricing</a>
      <a href="/#faq-page">FAQ</a>
      <a href="/#access">Contact us</a>
    </div>'''

PRICING_DESKTOP_NAV = '''<div class="nav-links">
      <a href="/#workflow">How it works</a>
      <a href="/use-cases">Use Cases</a>
      <a href="/#intake">Job intake</a>
      <a href="/pricing" class="active">Pricing</a>
      <a href="/#faq-page">FAQ</a>
      <a href="/#access">Contact us</a>
    </div>'''

MOBILE_NAV = '''<div class="mob-menu" id="mobMenu">
  <a href="/" onclick="closeMenu()">Home</a>
  <a href="/#workflow" onclick="closeMenu()">How it works</a>
  <a href="/use-cases" onclick="closeMenu()">Use Cases</a>
  <a href="/#intake" onclick="closeMenu()">Job intake</a>
  <a href="/pricing" onclick="closeMenu()">Pricing</a>
  <a href="/#faq-page" onclick="closeMenu()">FAQ</a>
  <a href="/#access" onclick="closeMenu()">Contact us</a>
  <a href="https://app.soletasker.com.au" onclick="closeMenu()" style="color:var(--navy);font-weight:800;border-top:1px solid var(--line);margin-top:8px;padding-top:16px">Log in to app →</a>
</div>'''


def patch_nav(text: str, desktop: str, label: str) -> str:
    text = replace_regex_once(
        text,
        r'<div class="nav-links">.*?</div>(?=\s*<div class="nav-r">)',
        desktop,
        f"{label} desktop nav",
    )
    text = replace_regex_once(
        text,
        r'<div class="mob-menu" id="mobMenu">.*?</div>',
        MOBILE_NAV,
        f"{label} mobile nav",
    )
    return text


def patch_footer(text: str) -> str:
    # Global footer navigation should mirror the real site journey. Keep the
    # existing layout/styling and only normalize destinations/labels.
    text = re.sub(
        r'<a href="/#pain"([^>]*)>The problem</a>',
        r'<a href="/#faq-page"\1>FAQ</a>',
        text,
    )
    text = text.replace('>Job intake link</a>', '>Job intake</a>')
    return text


def marker_start(text: str, tag: str) -> int:
    tag_pos = text.index(tag)
    comment_pos = text.rfind('<!--', 0, tag_pos)
    if comment_pos != -1 and tag_pos - comment_pos < 500:
        return comment_pos
    return tag_pos


def reorder_landing(text: str) -> str:
    tags = {
        "intake": '<section class="intake-sec" id="intake">',
        "smart": '<section class="smart-onsite-sec" id="smart-onsite">',
        "pain": '<section class="pain-sec lovable-real-cost" id="pain">',
        "pricing": '<!-- pricing teaser -->',
        "use": '<section style="background:var(--navy);padding:56px 32px;text-align:center">',
        "bbt": '<section class="bbt-sec" id="access">',
        "close": '<section class="close-sec">',
    }
    for name, tag in tags.items():
        if tag not in text and name == "use":
            tags[name] = '<section style="background:var(--white);border-top:1px solid var(--line);border-bottom:1px solid var(--line);padding:56px 32px;text-align:center">'
        elif tag not in text:
            raise RuntimeError(f"Missing landing marker: {name}")

    starts = {name: marker_start(text, tag) for name, tag in tags.items()}

    # If already in the approved order, do nothing.
    approved = ["smart", "pain", "use", "bbt", "intake", "pricing", "close"]
    if all(starts[approved[i]] < starts[approved[i + 1]] for i in range(len(approved) - 1)):
        return text

    current = ["intake", "smart", "pain", "pricing", "use", "bbt", "close"]
    if not all(starts[current[i]] < starts[current[i + 1]] for i in range(len(current) - 1)):
        raise RuntimeError("Landing source order changed; refusing to reorder blindly")

    prefix = text[:starts["intake"]]
    intake = text[starts["intake"]:starts["smart"]]
    smart = text[starts["smart"]:starts["pain"]]
    pain = text[starts["pain"]:starts["pricing"]]
    pricing = text[starts["pricing"]:starts["use"]]
    use = text[starts["use"]:starts["bbt"]]
    bbt = text[starts["bbt"]:starts["close"]]
    suffix = text[starts["close"]:]

    return prefix + smart + pain + use + bbt + intake + pricing + suffix


def patch_use_cases_band(text: str) -> str:
    text = replace_once(
        text,
        '<section style="background:var(--navy);padding:56px 32px;text-align:center">',
        '<section style="background:var(--white);border-top:1px solid var(--line);border-bottom:1px solid var(--line);padding:56px 32px;text-align:center">',
        "Use Cases light section",
    )
    text = replace_once(
        text,
        'color:var(--white)!important;line-height:.93;margin-bottom:16px">See exactly how',
        'color:var(--sole-blue)!important;line-height:.93;margin-bottom:16px">See exactly how',
        "Use Cases heading colour",
    )
    text = replace_once(
        text,
        'font-size:16px;color:rgba(255,255,255,.55);line-height:1.7;margin-bottom:28px;max-width:480px;',
        'font-size:16px;color:var(--ink-soft);line-height:1.7;margin-bottom:28px;max-width:480px;',
        "Use Cases body colour",
    )
    text = replace_once(
        text,
        'font-size:13px;color:rgba(255,255,255,.3);margin-top:14px">Electricians',
        'font-size:13px;color:var(--ink-ghost);margin-top:14px">Electricians',
        "Use Cases trade colour",
    )
    return text


def patch_hash_routing(text: str) -> str:
    anchor = "function closeMenu(){document.getElementById('mobMenu').classList.remove('open')}"
    addition = """function closeMenu(){document.getElementById('mobMenu').classList.remove('open')}

function openHashDestination(){
  if(location.hash==='#faq-page'){
    const faq=document.getElementById('faq-page');
    if(faq){faq.style.display='block';requestAnimationFrame(()=>faq.scrollIntoView({behavior:'smooth',block:'start'}));}
  }
}
window.addEventListener('DOMContentLoaded',openHashDestination);
window.addEventListener('hashchange',openHashDestination);"""
    return replace_once(text, anchor, addition, "landing hash routing")


def patch_landing() -> None:
    html = read("index.html")
    html = patch_nav(html, LANDING_DESKTOP_NAV, "landing")
    html = patch_footer(html)
    html = patch_hash_routing(html)
    html = replace_once(
        html,
        '.bbt-sec{\n  background:var(--white);padding:100px 32px;',
        '.bbt-sec{\n  background:var(--bg);padding:100px 32px;',
        "Why We Built background",
    )
    html = patch_use_cases_band(html)
    html = reorder_landing(html)

    # Safety checks: the problem remains as valuable content, but is no longer
    # exposed as a global navigation destination.
    nav_zone = html[html.index('<!-- NAV -->'):html.index('<!-- HERO -->')]
    if 'The problem' in nav_zone:
        raise RuntimeError("The problem still appears in landing global nav")
    for required in ['/#workflow', '/use-cases', '/#intake', '/pricing', '/#faq-page', '/#access']:
        if required not in nav_zone:
            raise RuntimeError(f"Missing landing nav destination: {required}")
    write("index.html", html)


def patch_subpage(name: str, desktop: str, label: str) -> None:
    html = read(name)
    html = patch_nav(html, desktop, label)
    html = patch_footer(html)
    if 'The problem</a>' in html:
        raise RuntimeError(f"The problem still appears in {label} navigation/footer")
    write(name, html)


def main() -> None:
    patch_landing()
    patch_subpage("use-cases.html", USE_CASES_DESKTOP_NAV, "Use Cases")
    patch_subpage("pricing.html", PRICING_DESKTOP_NAV, "Pricing")
    print("Updated landing flow, colours, and shared marketing navigation")


if __name__ == "__main__":
    main()
