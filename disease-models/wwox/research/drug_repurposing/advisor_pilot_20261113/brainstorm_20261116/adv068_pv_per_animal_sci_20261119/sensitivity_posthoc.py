"""ADV-068 POST-HOC sensitivity (not pre-registered; written after the primary verdict was read). Reads only out/per_gene_per_animal.tsv.

    python3 sensitivity_posthoc.py run <adv068_dir>

It does not change the primary verdict; it shows how fragile it is. Contents: (1) leave-one-gene-out re-application of the pre-registered
rule to each contrast, for each of the PV_SET, LATE_NONPV and REF_STABLE sets; (2) an exact label-permutation count for the cortex contrast
(descriptive, 35 labelings, no p-value used as a verdict); (3) per-animal Wwox log2 change against the PV and late-set values.
"""
import sys

if len(sys.argv) != 3 or sys.argv[1] != "run":
    print(__doc__)
    raise SystemExit(0)

import csv
import itertools
from pathlib import Path

import numpy as np

D = Path(sys.argv[2])
SETS = {
    "REF_STABLE": ["Snap25", "Rbfox3", "Syt1", "Stmn2", "Tubb3", "Map2"],
    "PV_SET": ["Pvalb", "Syt2", "Kcnc1", "Kcnc2"],
    "INT_NONPV": ["Gad1", "Gad2", "Slc32a1", "Sst", "Vip", "Npy", "Cck", "Calb2", "Htr3a", "Lhx6", "Dlx1", "Dlx2", "Dlx5"],
    "LATE_NONPV": ["Grin2a", "Slc12a5", "Nrgn", "Camk2a", "Scn8a"],
}
data = {}  # contrast -> gene -> sample -> (arm, log2)
for r in csv.DictReader(open(D / "out/per_gene_per_animal.tsv"), delimiter="\t"):
    data.setdefault(r["contrast"], {}).setdefault(r["gene"], {})[r["sample"]] = (r["arm"], float(r["log2_TPM_plus1"]))


def arms(contrast):
    any_gene = next(iter(data[contrast].values()))
    return [s for s, (a, _) in any_gene.items() if a == "ctrl"], [s for s, (a, _) in any_gene.items() if a == "KO"]


def sigs(contrast, sets, omit=None):
    """per-animal log2FC signature for the KO animals (against control mean) and ctrl animals (leave-one-out); returns dict sample->{set:value}"""
    ctrl, ko = arms(contrast)
    out = {}
    for s in ctrl + ko:
        out[s] = {}
        for k, genes in sets.items():
            vals = []
            for g in genes:
                if omit and (k, g) == omit or g not in data[contrast]:
                    continue
                gd = data[contrast][g]
                if s in ko:
                    base = np.mean([gd[c][1] for c in ctrl])
                else:
                    base = np.mean([gd[c][1] for c in ctrl if c != s])
                vals.append(gd[s][1] - base)
            out[s][k] = float(np.mean(vals))
    return ctrl, ko, out


def verdict(contrast, sets, omit=None):
    ctrl, ko, o = sigs(contrast, sets, omit)
    nrm = lambda s, k: o[s][k] - o[s]["REF_STABLE"]
    pv = float(np.mean([nrm(s, "PV_SET") for s in ko]))
    lt = float(np.mean([nrm(s, "LATE_NONPV") for s in ko]))
    it = float(np.mean([nrm(s, "INT_NONPV") for s in ko]))
    sep = max(nrm(s, "PV_SET") for s in ko) < min(nrm(s, "PV_SET") for s in ctrl)
    if len(ctrl) < 3 or len(ko) < 3:
        v = "STOP_S"
    elif pv > -0.5:
        v = "R-C"
    elif lt <= -0.25:
        v = "R-B"
    elif abs(lt) <= 0.2 and abs(it) <= 0.2 and sep:
        v = "R-A"
    else:
        v = "R-D"
    return v, pv, lt, it, sep


rows = []
for c in data:
    base_v = verdict(c, SETS)
    rows.append([c, "none (pre-registered sets)", base_v[0], round(base_v[1], 3), round(base_v[2], 3), round(base_v[3], 3), base_v[4]])
    for k in ("PV_SET", "LATE_NONPV", "REF_STABLE"):
        for g in SETS[k]:
            v = verdict(c, SETS, (k, g))
            rows.append([c, f"omit {g} from {k}", v[0], round(v[1], 3), round(v[2], 3), round(v[3], 3), v[4]])
with open(D / "out/sensitivity_leave_one_gene_out.tsv", "w", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n")
    w.writerow(["contrast", "omitted", "verdict_if_n_allowed(STOP_S means fewer than 3 animals per arm)", "PV_refnorm", "LATE_refnorm", "INT_refnorm", "every_KO_PV_below_lowest_ctrl"])
    w.writerows(rows)

# exact permutation count, cortex contrast: all 35 choices of 3 of the 7 animals as 'KO' (descriptive)
ctrl, ko = arms("cortex_S")
samples = ctrl + ko
# signature per animal against the mean of ALL 7 animals (label-free), reference-normalised
def label_free(sample, setname):
    vals = []
    for g in SETS[setname]:
        gd = data["cortex_S"].get(g)
        if gd:
            vals.append(gd[sample][1] - np.mean([gd[s][1] for s in samples]))
    return float(np.mean(vals))
sv = {s: {k: label_free(s, k) for k in ("PV_SET", "LATE_NONPV", "REF_STABLE", "INT_NONPV")} for s in samples}
nv = {s: {k: sv[s][k] - sv[s]["REF_STABLE"] for k in ("PV_SET", "LATE_NONPV", "INT_NONPV")} for s in samples}
perm = {}
for k in ("PV_SET", "LATE_NONPV", "INT_NONPV"):
    obs = np.mean([nv[s][k] for s in ko]) - np.mean([nv[s][k] for s in ctrl])
    stats = []
    for comb in itertools.combinations(samples, 3):
        rest = [s for s in samples if s not in comb]
        stats.append(np.mean([nv[s][k] for s in comb]) - np.mean([nv[s][k] for s in rest]))
    perm[k] = (round(float(obs), 3), sum(1 for x in stats if x <= obs + 1e-12), len(stats))

# deletion depth against PV and late values (descriptive, n = 3)
lines = []
for s in ko:
    wg = data["cortex_S"]["Wwox"]
    base = np.mean([wg[c][1] for c in ctrl])
    lines.append((s, round(float(wg[s][1] - base), 2), round(float(nv[s]["PV_SET"] - np.mean([nv[c]["PV_SET"] for c in ctrl])), 3),
                  round(float(nv[s]["LATE_NONPV"] - np.mean([nv[c]["LATE_NONPV"] for c in ctrl])), 3)))
with open(D / "out/sensitivity_permutation_and_depth.txt", "w") as f:
    f.write("exact label permutation, cortex S (3 of 7 animals labelled KO, 35 labelings); observed KO-minus-rest value, labelings at least as low (including the observed one), total\n")
    for k, v in perm.items():
        f.write(f"{k}\t{v[0]}\t{v[1]}\t{v[2]}\n")
    f.write("\nper KO animal: Wwox log2 change vs control mean, PV_SET refnorm (minus control mean), LATE_NONPV refnorm (minus control mean); label-free centring\n")
    for l in lines:
        f.write("\t".join(map(str, l)) + "\n")
print(open(D / "out/sensitivity_permutation_and_depth.txt").read())
for r in rows:
    if r[0] == "cortex_S":
        print("\t".join(map(str, r)))
