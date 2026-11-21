"""Write the blind-check pairs file of one ADV-131 batch: source passage + three renderings, nothing else.
Usage: python3 -I make_pairs.py <selected50.json> <batchN_translations.json> <out.md>"""
import json, sys
sel = {str(o["n"]): o for o in json.load(open(sys.argv[1], encoding="utf-8"))}
tr = json.load(open(sys.argv[2], encoding="utf-8"))
out = ["# Translation pairs for a blind check", "", "Each block is one source passage (English) and its renderings into French (FR), German (DE) and Spanish (ES). Row ids are `<passage>-<language>`.", ""]
for n in sorted(tr, key=int):
    out += [f"## Passage {n}", f"SOURCE: {sel[n]['text']}", ""]
    for lang in ("fr", "de", "es"):
        out.append(f"{n}-{lang.upper()}: {tr[n][lang]}")
    out.append("")
open(sys.argv[3], "w", encoding="utf-8").write("\n".join(out))
print(len(tr) * 3, "rows")
