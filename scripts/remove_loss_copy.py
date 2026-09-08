from pathlib import Path

path = Path('index.html')
text = path.read_text(encoding='utf-8')
old = """      <p class=\"bbt-body\">\n        We were losing money we'd already earned. Forgetting jobs. Losing certs. Invoices never going out. <strong>SoleTasker was built by Calec Electrical — a working Australian electrical business — because every other tool felt like software. We needed something that just worked on-site.</strong>\n      </p>"""
new = """      <p class=\"bbt-body\">\n        SoleTasker was built by Calec Electrical — a working Australian electrical business — around the way we actually work: on site, in the van and on the phone. It gives us a simple place to capture jobs, tasks, reminders and site admin without turning the day into more software.\n      </p>"""
if old not in text:
    raise SystemExit('Expected founder paragraph not found')
path.write_text(text.replace(old, new, 1), encoding='utf-8')
