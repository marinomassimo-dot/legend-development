#!/usr/bin/env python3
"""PROVISIONAL seed table derived from the IT7 P1 subnetwork (gene-level WWOX-loss observations in the three human build systems).

Used only to build and test the IT9 P2 engine while the question-specific P1 seeds (IT9 P1) were not yet available. Not the answer to any
question. Rules (fixed in PRE_REGISTRATION.md section 3 text and here): module genes of the glycolysis/PDH/lactate set except WWOX itself; value = mean
of the centred log2 ratio over the human systems in which the gene is measurable; seed if |mean| >= 0.25 (the P1 descriptive bin) or the direction is defined;
level = min(|mean|, 2) / 2; direction 'defined' iff the organoid AND the progenitor library both have |R| >= 0.25 in the same direction (the P1 rule), else 'uncertain'.
Myelin genes are not seeds (P1 positive control; mouse-mostly). Output columns follow seed_engine.py.

  provisional_seeds.py --p1 DIR --out FILE
"""
import sys
if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
    print(__doc__); raise SystemExit(0)
import argparse, csv, collections
from pathlib import Path
ap = argparse.ArgumentParser(); ap.add_argument("--p1", required=True); ap.add_argument("--out", required=True)
a = ap.parse_args()
P1 = Path(a.p1)
nodes = {r["symbol"]: r for r in csv.DictReader(open(P1 / "nodes.tsv", encoding="utf-8"), delimiter="\t")}
vals = collections.defaultdict(dict)
for r in csv.DictReader(open(P1 / "derived_gene_values.tsv", encoding="utf-8"), delimiter="\t"):
    if r["measurable"] == "True" and r["R_centred"] != "":
        vals[r["gene"]][r["system_id"]] = float(r["R_centred"])
cols = ["seed_id", "gene", "kind", "members", "direction", "level", "direction_status", "readout_level", "evidence_class", "species", "ortholog_map", "source_ref", "note"]
out = []
for g, v in sorted(vals.items()):
    if g == "WWOX" or nodes.get(g, {}).get("module") != "glycolysis_pdh_lactate":
        continue
    m = sum(v.values()) / len(v)
    o, h = v.get("organoid_ko_w15"), v.get("hnpc_shwwox_cage")
    defined = o is not None and h is not None and ((o >= 0.25 and h >= 0.25) or (o <= -0.25 and h <= -0.25))
    if abs(m) < 0.25 and not defined:
        continue
    d = ("up" if o > 0 else "down") if defined else "uncertain"
    out.append(dict(seed_id=f"PROV-{g}", gene=g, kind="gene", members="", direction=d, level=f"{min(abs(m), 2) / 2:.4f}",
                    direction_status="defined" if defined else "uncertain", readout_level="transcript", evidence_class="transcript_contrast", species="human", ortholog_map="",
                    source_ref="subnetwork_it7_p1_20261029/derived_gene_values.tsv", note=f"mean centred log2 over {len(v)} human systems = {m:.3f}; PROVISIONAL"))
with open(a.out, "w", encoding="utf-8", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=cols, delimiter="\t", lineterminator="\n"); w.writeheader(); [w.writerow(r) for r in out]
print(len(out), "provisional seeds;", sum(1 for r in out if r["direction_status"] == "defined"), "defined direction")
