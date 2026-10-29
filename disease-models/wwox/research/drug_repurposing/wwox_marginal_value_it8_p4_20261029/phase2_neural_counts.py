#!/usr/bin/env python3
"""IT8 P4: extract the phase II (GSE70138) neural compound perturbagens and their overlap with the IT7 universe.
Usage: phase2_neural_counts.py --sig-info GSE70138_..._sig_info.txt.gz --p3 network_comparison_it7_p3_20261029 --out TSV ; --help answers without work.
Input metadata only (public GEO table, not committed); prints its sha256. No outcome is opened."""
import sys, csv, gzip, hashlib, collections
if "--help" in sys.argv or len(sys.argv) == 1:
    print(__doc__); sys.exit(0)
a = lambda n: sys.argv[sys.argv.index(n) + 1]
NEURAL = ("NPC", "NPC.CAS9", "NPC.TAK", "NEU", "MNEU.E")
raw = open(a("--sig-info"), "rb").read(); print("sig_info sha256", hashlib.sha256(raw).hexdigest())
cells = collections.defaultdict(collections.Counter)
with gzip.open(a("--sig-info"), "rt") as f:
    for r in csv.DictReader(f, delimiter="\t"):
        if r["pert_type"] == "trt_cp" and r["cell_id"] in NEURAL: cells[r["pert_id"]][r["cell_id"]] += 1
P3 = a("--p3")
fp = collections.defaultdict(set)
for r in csv.DictReader(open(f"{P3}/inputs/pilot_lincs_contexts.tsv"), delimiter="\t"): fp[r["pert_id"]].add(r["family_id"])
U = {r["family_id"] for r in csv.DictReader(open(f"{P3}/results/family_scores.tsv"), delimiter="\t")}
with open(a("--out"), "w", newline="") as o:
    w = csv.writer(o, delimiter="\t", lineterminator="\n"); w.writerow(["pert_id", "neural_signatures_by_cell", "n_signatures", "universe_families"])
    for p in sorted(cells):
        fu = sorted(fp.get(p, set()) & U); w.writerow([p, ";".join(f"{c}:{n}" for c, n in sorted(cells[p].items())), sum(cells[p].values()), ";".join(fu)])
print("perturbagens", len(cells), "universe families covered", len({f for p in cells for f in fp.get(p, set()) & U}))
