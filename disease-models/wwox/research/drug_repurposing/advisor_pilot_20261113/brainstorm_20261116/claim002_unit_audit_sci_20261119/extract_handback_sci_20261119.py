"""SCI 2026-11-19 (ADV-083): extract the delegate's final report (the `message` of its SubagentHandback tool_use, else its last assistant text) from the delegate's transcript
file, write it verbatim to the path given, and print its word count.   Run:  python3 -I extract_handback_sci_20261119.py <transcript.jsonl> <out.md>"""
import json
import sys
from pathlib import Path

if len(sys.argv) != 3 or any(a in ("-h", "--help") for a in sys.argv[1:]):
    print(__doc__)
    raise SystemExit(0 if any(a in ("-h", "--help") for a in sys.argv[1:]) else 2)
msg = None
last_text = None
for line in Path(sys.argv[1]).read_text(encoding="utf-8").splitlines():
    try:
        o = json.loads(line)
    except Exception:
        continue
    m = o.get("message") if isinstance(o, dict) else None
    if not isinstance(m, dict) or m.get("role") != "assistant" or not isinstance(m.get("content"), list):
        continue
    for c in m["content"]:
        if c.get("type") == "tool_use" and c.get("name") == "SubagentHandback":
            msg = (c.get("input") or {}).get("message")
        if c.get("type") == "text" and c.get("text"):
            last_text = c["text"]
out = msg or last_text
if not out:
    raise SystemExit("no report found")
Path(sys.argv[2]).write_text(out, encoding="utf-8")
print("source:", "SubagentHandback" if msg else "last text", "| words:", len(out.split()), "| chars:", len(out))
