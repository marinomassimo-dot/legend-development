#!/usr/bin/env python3
"""POST HOC look (not pre-registered) at target-family transcripts in the same E-MTAB-6798 mouse brain file.

ADV-088/090 follow-up (SCI, 2026-11-19), requested by ADV after the result was delivered. Same file, same
unit, same plateau definition (mean RPKM at P28 and P63) as the pre-registered analysis; only the gene list
differs: Cacna1g, Cacna1h, Cacna1i (T-type), Kcnq2, Kcnq3 (Kv7), Grin2b, Grin2a (NMDA receptor).
Usage: python3 -I posthoc_targets.py RPKM_TXT OUT_TSV   (symbol to Ensembl id through mygene.info, symbol only)
"""
import csv
import json
import re
import sys
import urllib.request

GENES = ["Cacna1g", "Cacna1h", "Cacna1i", "Kcnq2", "Kcnq3", "Grin2b", "Grin2a"]
AGES = ["P0", "P3", "P14", "P28", "P63"]


def ensembl_id(sym):
    url = f"https://mygene.info/v3/query?q=symbol:{sym}&species=mouse&fields=ensembl.gene,symbol&size=5"
    with urllib.request.urlopen(url, timeout=40) as r:
        d = json.load(r)
    hit = [h for h in d["hits"] if h.get("symbol", "").lower() == sym.lower()][0]
    ens = hit["ensembl"] if isinstance(hit["ensembl"], list) else [hit["ensembl"]]
    return [e["gene"] for e in ens if e["gene"].startswith("ENSMUSG")][0]


def main(argv):
    if len(argv) != 3 or argv[1] in ("-h", "--help"):
        print(__doc__)
        return 0 if len(argv) > 1 and argv[1] in ("-h", "--help") else 2
    ids = {g: ensembl_id(g) for g in GENES}
    with open(argv[1], encoding="utf-8") as fh:
        header = fh.readline().replace('"', "").split()
        cols = [i for i, h in enumerate(header) if re.match(r"Brain\.P\d+\.\d+$", h)]
        age = [re.match(r"Brain\.(P\d+)\.", header[i]).group(1) for i in cols]
        rows = {}
        for line in fh:
            parts = line.replace('"', "").split()
            if parts[0] in ids.values():
                rows[parts[0]] = [float(parts[1 + i]) for i in cols]
    out = []
    for g in GENES:
        vals = rows.get(ids[g])
        if vals is None:
            out.append({"symbol": g, "ensembl": ids[g], "note": "ABSENT"})
            continue
        mean = {a: sum(v for v, x in zip(vals, age) if x == a) / age.count(a) for a in AGES}
        plateau = (mean["P28"] + mean["P63"]) / 2
        rec = {"symbol": g, "ensembl": ids[g], "plateau_rpkm": round(plateau, 3)}
        for a in AGES:
            rec["mean_" + a] = round(mean[a], 3)
            rec["frac_" + a] = round(mean[a] / plateau, 3)
        rec["P14_samples"] = ";".join(f"{v:.2f}" for v, x in zip(vals, age) if x == "P14")
        rec["P28_samples"] = ";".join(f"{v:.2f}" for v, x in zip(vals, age) if x == "P28")
        out.append(rec)
    keys = []
    for r in out:
        for k in r:
            if k not in keys:
                keys.append(k)
    with open(argv[2], "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=keys, delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(out)
    for r in out:
        print(r["symbol"], r.get("plateau_rpkm"), *(r.get("frac_" + a) for a in AGES))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
