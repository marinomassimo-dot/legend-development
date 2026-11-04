#!/usr/bin/env python3
"""IT24 P10: per-target signed contribution mass of a family, read from the committed engine contributions (eng_merged, written 2026-11-03, BEFORE the IT24 P1 action refresh).
Usage: target_mass_it24_p10.py OUT.tsv   (read-only; no engine re-run). Marks targets named in source_exclusions_it24.tsv as WITHHELD_AT_ACTION_TABLE."""
import sys
if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
    print(__doc__); raise SystemExit(0)
import csv, gzip, collections
from pathlib import Path
DR = Path(__file__).resolve().parent.parent
ENG = DR / "generation_it22_p1_20261103" / "eng_merged"
FAM = {"vorinostat_DGIdb_twin": "FAM:CAT:DGIDB:316b73312895", "vorinostat_ChEMBL_sibling": "FAM:CAT:CHEMBL98", "panobinostat_DGIdb": "FAM:CAT:DGIDB:be0d8ea27925",
       "idronoxil_DGIdb": "FAM:CAT:DGIDB:b34c953dc1fa", "sorafenib_DGIdb": "FAM:CAT:DGIDB:0bc1cf72f3bb"}
EX = {(r["family_id"], r["gene"]) for r in csv.DictReader(open(DR / "generation_it21_p2_20261103" / "source_exclusions_it24.tsv"), delimiter="\t")}
out = []
for f in sorted(ENG.glob("contributions_p1_Q*_*.tsv.gz")):
    ss = f.name[len("contributions_p1_"):-7]
    if ss.endswith(("_adm", "_indeg", "_reach")):
        continue
    by = collections.defaultdict(lambda: collections.defaultdict(float))
    for r in csv.DictReader(gzip.open(f, "rt"), delimiter="\t"):
        for lab, fam in FAM.items():
            if r["family_id"] == fam:
                for t in {r["main_target_hop0"], r["main_target_hops1to3"]} - {""}:
                    by[lab][t] += float(r["contrib_total"])
    for lab, d in by.items():
        pos = sum(v for v in d.values() if v > 0); neg = sum(-v for v in d.values() if v < 0)
        for t, v in sorted(d.items(), key=lambda kv: -abs(kv[1])):
            out.append(dict(seed_set=ss, family=lab, target=t, net_contrib=f"{v:.3e}", share_of_abs_mass=f"{abs(v) / (pos + neg):.4f}" if pos + neg else "",
                            withheld=("WITHHELD_AT_ACTION_TABLE" if (FAM[lab], t) in EX else "")))
with open(sys.argv[1], "w", newline="") as fh:
    w = csv.DictWriter(fh, list(out[0]), delimiter="\t", lineterminator="\n"); w.writeheader(); w.writerows(out)
print(len(out), "rows")
