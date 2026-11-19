#!/usr/bin/env python3
"""Mouse brain marker time course from E-MTAB-6798 Mouse.RPKM.txt, per the frozen ADV-088 pre-registration.

Read-only. Two steps, both with plain clients:
  ids    SYMBOLS_JSON_OUT           look up Ensembl gene ids of the pre-registered symbols (Ensembl REST, symbol only)
  run    RPKM_TXT IDS_JSON OUT_TSV  per-sample RPKM, per-age mean and fraction of plateau (mean of P28 and P63)
Markers and definitions are those of PREREG_EXPRESSION_TIMECOURSE_ADV088_SCI_20261119.md; nothing else is computed.
"""
import argparse
import csv
import json
import re
import sys
import urllib.request

MARKERS = [
    "Wwox", "Pvalb", "Gad1", "Gad2", "Sst", "Vip", "Lhx6", "Nkx2-1",
    "Slc12a5", "Slc12a2", "Kcnc1", "Syt2", "Acan", "Gabra1", "Gabra2",
    "Mbp", "Plp1", "Mog", "Mobp", "Mag", "Cnp",
]
AGES = ["P0", "P3", "P14", "P28", "P63"]


def cmd_ids(out):
    ids = {}
    for sym in MARKERS:
        # Ensembl REST answered 403 to a plain client; mygene.info (public, symbol only) is the second route.
        url = f"https://mygene.info/v3/query?q=symbol:{sym}&species=mouse&fields=ensembl.gene,symbol&size=5"
        with urllib.request.urlopen(url, timeout=40) as r:
            d = json.load(r)
        hits = [h for h in d["hits"] if h.get("symbol", "").lower() == sym.lower()]
        ens = hits[0]["ensembl"] if hits else []
        ens = ens if isinstance(ens, list) else [ens]
        gid = [e["gene"] for e in ens if e["gene"].startswith("ENSMUSG")][0]
        ids[sym] = {"id": gid, "display_name": hits[0]["symbol"]}
        print(sym, gid, hits[0]["symbol"])
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(ids, fh, indent=1)


def read_rows(path, wanted):
    with open(path, encoding="utf-8") as fh:
        header = fh.readline().replace('"', "").split()
        cols = [i for i, h in enumerate(header) if re.match(r"Brain\.P\d+\.\d+$", h)]
        names = [header[i] for i in cols]
        rows = {}
        for line in fh:
            parts = line.replace('"', "").split()
            if parts[0] in wanted:
                rows[parts[0]] = [float(parts[1 + i]) for i in cols]
    return names, rows


def cmd_run(rpkm, ids_json, out):
    ids = json.load(open(ids_json, encoding="utf-8"))
    names, rows = read_rows(rpkm, {v["id"] for v in ids.values()})
    age_of = [re.match(r"Brain\.(P\d+)\.", n).group(1) for n in names]
    out_rows = []
    for sym in MARKERS:
        gid = ids[sym]["id"]
        if gid not in rows:
            out_rows.append({"symbol": sym, "ensembl": gid, "note": "ABSENT from matrix"})
            continue
        vals = rows[gid]
        mean = {a: sum(v for v, x in zip(vals, age_of) if x == a) / sum(1 for x in age_of if x == a) for a in AGES}
        plateau = (mean["P28"] + mean["P63"]) / 2
        rec = {"symbol": sym, "ensembl": gid, "plateau_mean_rpkm_P28_P63": round(plateau, 3)}
        for a in AGES:
            rec[f"mean_{a}"] = round(mean[a], 3)
            rec[f"frac_{a}"] = round(mean[a] / plateau, 3) if plateau > 0 else ""
            rec[f"samples_{a}"] = ";".join(f"{v:.2f}" for v, x in zip(vals, age_of) if x == a)
        out_rows.append(rec)
    keys = []
    for r in out_rows:
        for k in r:
            if k not in keys:
                keys.append(k)
    with open(out, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=keys, delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(out_rows)
    print("samples", len(names), "markers", len(out_rows))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("ids")
    a.add_argument("out")
    b = sub.add_parser("run")
    b.add_argument("rpkm")
    b.add_argument("ids_json")
    b.add_argument("out")
    args = ap.parse_args()
    if args.cmd == "ids":
        cmd_ids(args.out)
    else:
        cmd_run(args.rpkm, args.ids_json, args.out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
