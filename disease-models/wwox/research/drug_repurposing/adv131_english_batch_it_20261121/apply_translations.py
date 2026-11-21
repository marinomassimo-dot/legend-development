"""Apply one batch of ADV-131 translations to the content catalogue (view/i18n/content_<lang>.json), keyed by the passage hash of selected50.json.
Usage: python3 -I apply_translations.py <selected50.json> <batchN_translations.json>   (run from the repository root)"""
import json, sys
I = "disease-models/wwox/research/drug_repurposing/view/i18n/"
sel = {str(o["n"]): o for o in json.load(open(sys.argv[1], encoding="utf-8"))}
tr = json.load(open(sys.argv[2], encoding="utf-8"))
for lang in ("fr", "de", "es"):
    path = I + f"content_{lang}.json"
    d = json.load(open(path, encoding="utf-8"))
    for n, t in tr.items():
        d[sel[n]["hash"]] = t[lang]
    open(path, "w", encoding="utf-8").write(json.dumps(dict(sorted(d.items())), indent=1, ensure_ascii=False))
print("applied", len(tr), "passages x 3 languages")
