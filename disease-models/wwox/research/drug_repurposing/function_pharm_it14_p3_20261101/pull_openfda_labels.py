#!/usr/bin/env python3
"""openFDA drug-label (US, key-less) consultation facts: for each generic name, the label's
effective_time, brand, and verbatim leading text of indications_and_usage and mechanism_of_action
(first 500 chars), plus any sentence mentioning 'active' with 'metabolite' or 'enantiomer'.
Jurisdiction US only; a label is a regulatory fact, not evidence of benefit. Usage: pull_openfda_labels.py <out.tsv>"""
import json, sys, urllib.request, urllib.parse, re, time
NAMES = ["vigabatrin","clobazam","tiagabine","ezogabine","ganaxolone"]
def main():
    if len(sys.argv) != 2 or sys.argv[1] in ("-h","--help"):
        print(__doc__); return 0 if len(sys.argv) > 1 else 2
    rows = []
    for n in NAMES:
        u = "https://api.fda.gov/drug/label.json?" + urllib.parse.urlencode({"search": f"openfda.generic_name:\"{n}\"", "limit": 3})
        try:
            d = json.load(urllib.request.urlopen(u, timeout=60))
        except Exception as e:
            rows.append([n, "NO_RESULT", str(e), "", "", "", ""]); continue
        for r in d["results"][:3]:
            f = lambda k: re.sub(r"\s+", " ", " ".join(r.get(k, [""])))
            txt = " ".join(" ".join(v) for v in r.values() if isinstance(v, list) and v and isinstance(v[0], str))
            hits = [s.strip()[:300] for s in re.split(r"(?<=[.])\s", txt) if re.search(r"(active metabolite|pharmacologically active|enantiomer)", s, re.I)][:2]
            rows.append([n, ",".join(r["openfda"].get("brand_name", [])[:2]), r.get("effective_time",""), f("indications_and_usage")[:500], f("mechanism_of_action")[:500], " || ".join(hits), f("boxed_warning")[:200]])
        time.sleep(0.3)
    with open(sys.argv[1], "w", encoding="utf8") as fh:
        fh.write("generic_query\tbrand\teffective_time\tindications_start\tmechanism_start\tactive_moiety_sentences\tboxed_warning_start\n")
        for r in rows: fh.write("\t".join(str(x).replace("\t"," ") for x in r) + "\n")
    print(len(rows), "rows"); return 0
if __name__ == "__main__": sys.exit(main())
