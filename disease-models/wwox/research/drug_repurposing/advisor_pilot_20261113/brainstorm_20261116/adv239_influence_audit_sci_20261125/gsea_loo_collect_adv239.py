"""ADV-239: collect leave-one-animal-out runs of the IT12 GSEA re-implementation on GSE215425 (P47T).

Each run is p47t_it12_20261031/p47t_reanalysis_it12.py on the count table with one animal's libraries removed
(same arguments as the full run). Threshold, as ADV-233: positive NES and BH q < 0.05 (gene-label permutation,
anti-conservative). Cerebellum runs drop the animal only if it has a cerebellar library.

Usage: python3 -I gsea_loo_collect_adv239.py <runs_dir> <out.tsv>
  <runs_dir> holds out_full/ and out_<animal>/ directories
"""
import sys

if len(sys.argv) != 3 or sys.argv[1] in ("-h", "--help"):
    print(__doc__)
    raise SystemExit(0)

import csv, os

RUNS, OUT = sys.argv[1:3]
ANIMALS = ["M3", "M2", "M1", "F5", "F4", "M7", "M6", "F9", "F8", "F10"]
CB = {"M3", "M2", "F5", "F4", "M6", "F8", "F10"}
SETS = ["HYPOXIA", "GLYCOLYSIS", "APOPTOSIS", "TNFA_SIGNALING_VIA_NFKB", "IL6_JAK_STAT3_SIGNALING",
        "INFLAMMATORY_RESPONSE", "MTORC1_SIGNALING", "CHOLESTEROL_HOMEOSTASIS", "FATTY_ACID_METABOLISM",
        "REACTIVE_OXIGEN_SPECIES_PATHWAY", "ADIPOGENESIS", "OXIDATIVE_PHOSPHORYLATION"]


def load(d):
    out = {}
    with open(os.path.join(d, "gsea_reimpl_it12.tsv")) as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            out[(r["region"], r["hallmark"].replace("HALLMARK_", ""))] = (float(r["NES"]), float(r["BH_q_over_50"]))
    return out


def met(x):
    return x[0] > 0 and x[1] < 0.05


full = load(os.path.join(RUNS, "out_full"))
runs = {a: load(os.path.join(RUNS, "out_" + a)) for a in ANIMALS}
rows = []
for reg in ("HPC", "CTX", "PFC", "CB"):
    drops = [a for a in ANIMALS if reg != "CB" or a in CB]
    for s in SETS:
        key = (reg, s)
        if key not in full:
            continue
        f = full[key]
        vals = {a: runs[a][key] for a in drops}
        lost = [a for a in drops if met(f) and not met(vals[a])]
        gained = [a for a in drops if not met(f) and met(vals[a])]
        nes = [vals[a][0] for a in drops]
        lo = min(drops, key=lambda a: vals[a][0])
        flips = [a for a in drops if (vals[a][0] > 0) != (f[0] > 0)]
        rows.append([reg, s, "%.2f" % f[0], "%.3g" % f[1], "yes" if met(f) else "no", len(drops), "%.2f" % min(nes),
                     lo, "%.2f" % max(nes), ";".join(lost), ";".join(gained), ";".join(flips)])
with open(OUT, "w") as o:
    o.write("region\thallmark\tNES_all\tq_all\tthreshold_met_all\tn_single_drops\tmin_NES_drop\tanimal_at_min\t"
            "max_NES_drop\tthreshold_lost_when_dropping\tthreshold_gained_when_dropping\tsign_flip_when_dropping\n")
    for r in rows:
        o.write("\t".join(str(x) for x in r) + "\n")
print("wrote", len(rows))
