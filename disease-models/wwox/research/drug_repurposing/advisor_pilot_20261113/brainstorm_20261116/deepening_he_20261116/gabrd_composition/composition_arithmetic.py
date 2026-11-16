#!/usr/bin/env python3
"""Composition arithmetic for bulk Gabrd (ADV's question), as PREMISES_BEFORE_THE_P47T_NUMBERS.md fixes it. Run only after that file is committed.

    python3 composition_arithmetic.py --hpa <rna_single_nuclei_cluster_type.tsv.zip> --out <dir>
    python3 composition_arithmetic.py --help

Reads human single-nuclei cluster-type nCPM (HPA) for GABRD, LAMP5, SST, NPY, CCK, PVALB, VIP, SLC17A7, GAD1; scans ASSUMED cortical nucleus shares; prints (1) each class's share of bulk Gabrd and the
share fall needed for log2 -0.8, (2) the composition-only Gabrd change implied by the observed marker changes (Lamp5 down, Sst, Npy, Cck up) per scenario, with the reading rule applied. Not medical advice.
"""
import argparse, csv, io, itertools, json, math, sys, zipfile
from pathlib import Path

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter); ap.add_argument("--hpa"); ap.add_argument("--out"); a = ap.parse_args()
if not (a.hpa and a.out):
    ap.print_help(); sys.exit(0)
GENES = ["GABRD", "LAMP5", "SST", "NPY", "CCK", "PVALB", "VIP", "SLC17A7", "GAD1"]
z = zipfile.ZipFile(a.hpa); t = io.TextIOWrapper(z.open(z.namelist()[0]), encoding="utf-8"); next(t)
E = {}
for line in t:
    r = line.rstrip("\n").split("\t")
    if len(r) >= 4 and r[1] in GENES: E.setdefault(r[1], {})[r[2]] = float(r[3])
CLUSTERS = sorted(E["GABRD"])
out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
with open(out / "hpa_cluster_nCPM.tsv", "w", newline="") as fh:
    w = csv.writer(fh, delimiter="\t", lineterminator="\n"); w.writerow(["cluster_type"] + GENES)
    for c in CLUSTERS: w.writerow([c] + [E[g].get(c, "NA") for g in GENES])
# cortical classes used in the arithmetic (cluster types of the table; the names are the table's)
CTX = {"excit": [c for c in CLUSTERS if ("intratelencephalic" in c or "extratelencephalic" in c or "corticothalamic" in c or "near-projecting" in c or "excitatory" in c) and "ca" not in c.split()[0][:2] and "brainstem" not in c and "cerebell" not in c and "amygdala" not in c and "thalamic" not in c and "hippocamp" not in c],
       "cge": [c for c in CLUSTERS if c.startswith("cge")], "mge": [c for c in CLUSTERS if c.startswith("mge")],
       "astro": [c for c in CLUSTERS if c == "astrocytes"], "oligo": [c for c in CLUSTERS if c == "oligodendrocytes"], "opc": [c for c in CLUSTERS if "opc" in c or "precursor" in c],
       "micro": [c for c in CLUSTERS if "microglia" in c]}
print("classes used:", json.dumps(CTX))
def e(cls, g):
    cs = CTX[cls]
    return sum(E[g].get(c, 0.0) for c in cs) / len(cs) if cs else 0.0
# shares of nuclei: ASSUMED scan. neurons 30-60% of nuclei, interneurons 10-25% of neurons, cge-derived 30-50% of interneurons, glia split astro 35% / oligo 45% / opc 10% / micro 10%
rows = []
for nf, inf, cgef in itertools.product((0.30, 0.45, 0.60), (0.10, 0.18, 0.25), (0.30, 0.40, 0.50)):
    f = {"excit": nf * (1 - inf), "cge": nf * inf * cgef, "mge": nf * inf * (1 - cgef)}
    g = 1 - nf
    f.update(astro=g * 0.35, oligo=g * 0.45, opc=g * 0.10, micro=g * 0.10)
    bulk = {gene: sum(f[c] * e(c, gene) for c in f) for gene in GENES}
    s = {c: f[c] * e(c, "GABRD") / bulk["GABRD"] for c in f}
    sL = f["cge"] * e("cge", "LAMP5") / bulk["LAMP5"]
    # observed marker factors (bulk): Lamp5 0.64 (cortex) and 0.55 (PFC); Sst 1.79 / 1.92; Npy 3.0 / 2.2; Cck 1.62 / 1.87 (2**log2). The class factors needed to give them, each marker from the class that carries it
    obs = {"CTX": {"LAMP5": 2 ** -0.65, "SST": 2 ** 0.84, "NPY": 2 ** 1.59, "CCK": 2 ** 0.70}, "PFC": {"LAMP5": 2 ** -0.86, "SST": 2 ** 0.94, "NPY": 2 ** 1.12, "CCK": 2 ** 0.90}}
    for region, o in obs.items():
        r_cge = max(0.0, 1 - (1 - o["LAMP5"]) / sL) if sL > 0 else 1.0                       # the cge-derived class carries a share sL of bulk Lamp5 and accounts for all of its fall
        sS = f["mge"] * e("mge", "SST") / bulk["SST"]; r_mge = 1 + (o["SST"] - 1) / sS if sS > 0 else 1.0       # the mge-derived class carries a share sS of bulk Sst and accounts for all of its rise
        f2 = dict(f); f2["cge"] *= r_cge; f2["mge"] *= r_mge
        new = sum(f2[c] * e(c, "GABRD") for c in f2); d = math.log2(new / bulk["GABRD"])
        d_cge_only = math.log2(1 - s["cge"] * (1 - r_cge))                                    # ADDED AFTER THE FIRST RUN (disclosed in the result note): the Lamp5-implied fall of the cge-derived class alone, mge unchanged
        d_cge_gone, d_mge_gone, d_both_gone = math.log2(1 - s["cge"]), math.log2(1 - s["mge"]), math.log2(1 - s["cge"] - s["mge"])      # bounds: a class removed entirely
        rows.append({"neurons": nf, "interneuron_share_of_neurons": inf, "cge_share_of_interneurons": cgef, "region": region, "share_of_bulk_GABRD_cge": round(s["cge"], 3), "share_of_bulk_GABRD_mge": round(s["mge"], 3),
                     "share_of_bulk_GABRD_excit": round(s["excit"], 3), "share_of_bulk_LAMP5_from_cge": round(sL, 3), "r_cge_implied": round(r_cge, 3), "r_mge_implied": round(r_mge, 3), "composition_only_log2_GABRD": round(d, 3), "cge_fall_only_log2_GABRD": round(d_cge_only, 3), "bound_cge_removed_log2": round(d_cge_gone, 3), "bound_mge_removed_log2": round(d_mge_gone, 3), "bound_both_removed_log2": round(d_both_gone, 3),
                     "cge_fall_alone_needed_for_log2_-0.8_if_it_vanished": "impossible" if s["cge"] < 0.426 else "possible"})
with open(out / "scenarios.tsv", "w", newline="") as fh:
    w = csv.DictWriter(fh, list(rows[0]), delimiter="\t", lineterminator="\n"); w.writeheader(); w.writerows(rows)
vals = [r["composition_only_log2_GABRD"] for r in rows]
print(f"scenarios {len(rows)}; composition-only Gabrd log2: min {min(vals):+.2f}, median {sorted(vals)[len(vals)//2]:+.2f}, max {max(vals):+.2f}")
for reg in ("CTX", "PFC"):
    v = sorted(r["composition_only_log2_GABRD"] for r in rows if r["region"] == reg); print(reg, "range", v[0], v[-1], "median", v[len(v)//2])
for k in ("cge_fall_only_log2_GABRD", "bound_cge_removed_log2", "bound_mge_removed_log2", "bound_both_removed_log2"):
    v = sorted(r[k] for r in rows); print(k, "range", v[0], v[-1], "median", v[len(v)//2])
print("share of bulk GABRD carried by the cge-derived class: ", min(r["share_of_bulk_GABRD_cge"] for r in rows), "to", max(r["share_of_bulk_GABRD_cge"] for r in rows))
print("share of bulk GABRD carried by the mge-derived class:", min(r["share_of_bulk_GABRD_mge"] for r in rows), "to", max(r["share_of_bulk_GABRD_mge"] for r in rows))
print("share of bulk GABRD carried by excitatory neurons:   ", min(r["share_of_bulk_GABRD_excit"] for r in rows), "to", max(r["share_of_bulk_GABRD_excit"] for r in rows))
print("Lamp5 share from cge:", min(r["share_of_bulk_LAMP5_from_cge"] for r in rows), "to", max(r["share_of_bulk_LAMP5_from_cge"] for r in rows))
