"""IT59 (2026-11-20): delegate-brief guard. Builds a blind-audit packet from a JSON spec and REFUSES any statement whose anchor list is empty, whose repository anchor path is missing on disk, or whose anchor text is blank
(the first unit B audit lost its repository anchors to a shell expansion that left the anchor fields empty). Usage: audit_packet_builder_it59.py SPEC.json OUT.md  (SPEC: {"repo": ..., "title": ..., "preamble": ..., "items": [{"id", "statement", "anchors": [{"path": "repo-relative" | "label": "external paper id"}]}]}).
Run from the repository root; python3 -I. Writes OUT.md and OUT.sha256 only when every anchor is present."""
import hashlib, json, sys
from pathlib import Path

spec = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8")); out = Path(sys.argv[2])
repo = Path(spec.get("repo", ".")); bad = []
for it in spec["items"]:
    if not it.get("statement", "").strip(): bad.append((it["id"], "empty statement"))
    if not it.get("anchors"): bad.append((it["id"], "no anchors"))
    for a in it.get("anchors", []):
        if "path" in a:
            if not a["path"].strip() or not (repo / a["path"]).is_file(): bad.append((it["id"], "missing path: " + repr(a["path"])))
        elif not a.get("label", "").strip(): bad.append((it["id"], "blank anchor label"))
if bad:
    print("REFUSED:", *bad, sep="\n  "); sys.exit(3)
text = "# " + spec["title"] + "\n\n" + spec["preamble"].strip() + "\n\n"
for it in spec["items"]:
    anch = "; ".join(("repository file " + a["path"]) if "path" in a else a["label"] for a in it["anchors"])
    text += "## %s\nAnchor: %s\nStatement: %s\n\n" % (it["id"], anch, it["statement"].strip())
out.write_text(text, encoding="utf-8"); out.with_suffix(".sha256").write_text(hashlib.sha256(text.encode()).hexdigest() + "  " + out.name + "\n")
print("OK", len(spec["items"]), "items,", sum(len(i["anchors"]) for i in spec["items"]), "anchors, all present")
