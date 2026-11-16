#!/usr/bin/env python3
"""I8 held-table addendum: NEDD4-family ligases, WWOX and PPxY-binding partners by region (P47T knock-in mRNA, four regions) and the P17 neuron-deletion rows.

    python3 i8_ligases_regions.py --repo <repo root> --out <file.tsv>      (read-only; no network)

Columns: region, gene, mean normalised count in wild type, log2FC (centred), FDR (no sex term), n. mRNA only: a competition at a PY motif changes protein surface level, which no row here measures. Not medical advice.
"""
import argparse, csv, gzip
from pathlib import Path

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter); ap.add_argument("--repo"); ap.add_argument("--out"); a = ap.parse_args()
if not (a.repo and a.out):
    ap.print_help(); raise SystemExit(0)
RES = Path(a.repo) / "disease-models/wwox/research/drug_repurposing/wwox_data_it24_p4_20261104/results"
G = ["Wwox", "Nedd4", "Nedd4l", "Itch", "Wwp1", "Wwp2", "Smurf1", "Smurf2", "Wbp1", "Wbp2", "Wbp4", "Yap1", "Hcn1", "Scn1a", "Scn2a", "Scn3a", "Scn8a", "Kcnh7", "Trpm3", "Kcnt2", "Neto1", "Neto2", "Slc17a7", "Scnn1a"]
rows = {}
for r in csv.DictReader(gzip.open(RES / "p47t_all_regions_tested_genes.tsv.gz", "rt"), delimiter="\t"):
    if r["symbol"] in G: rows[(r["symbol"], r["region"])] = r
with open(a.out, "w", newline="") as fh:
    w = csv.writer(fh, delimiter="\t", lineterminator="\n"); w.writerow(["gene", "region", "mean_norm_count_WT", "log2FC_centred", "FDR_no_sex", "n_WT", "n_P47T"])
    for g in G:
        for rg in ("CTX", "HPC", "PFC", "CB"):
            r = rows.get((g, rg))
            w.writerow([g, rg] + ([r["mean_norm_count_WT"], r["log2FC_centred"], r["FDR_no_sex"], r["n_WT"], r["n_P47T"]] if r else ["NA"] * 5))
print("rows", len(G) * 4)
