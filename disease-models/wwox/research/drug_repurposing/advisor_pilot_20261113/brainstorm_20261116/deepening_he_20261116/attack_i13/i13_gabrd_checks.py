#!/usr/bin/env python3
"""HE's composition check on I13's Gabrd observation: which classes read the delta subunit, and what do interneuron and projection-neuron markers do in the same P47T regions?

    python3 i13_gabrd_checks.py --repo <root> --files <files dir> --xlrd <dir> --out <file.tsv>
    python3 i13_gabrd_checks.py --help

Read-only on the held class table (GSE52564) and the P47T all-region table (GSE215425; mRNA of a missense line, n 5 v 5). If the delta subunit tracks a cell subtype whose marker also moves, a bulk fall is partly a composition statement. Descriptive. Not medical advice.
"""
import argparse, csv, gzip, os, sys
from pathlib import Path

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
for k in ("--repo", "--files", "--xlrd", "--out"): ap.add_argument(k)
a = ap.parse_args()
if not all([a.repo, a.files, a.xlrd, a.out]):
    ap.print_help(); sys.exit(0)
sys.path.insert(0, a.xlrd); import xlrd
G = ["Gabrd", "Gabra5", "Gabra4", "Gabra1", "Gabrg2", "Slc6a1", "Slc6a11", "Pvalb", "Sst", "Vip", "Lamp5", "Npy", "Gad1", "Gad2", "Slc17a7", "Neurod6", "Cux2", "Rorb", "Grin2b"]
CL = {"Astrocyte": "astro", "Neuron": "neuron", "OPC": "OPC", "NFO": "NFO", "MO": "MO", "Microglia": "microglia", "Endothelial": "endo"}
raw = Path(a.files) / "geo/GSE52564_raw"; expr = {}
for fn in sorted(os.listdir(raw)):
    if not fn.endswith(".xls.gz") or "WC" in fn: continue
    key = CL.get(fn.split("_")[1].split(".")[0].rstrip("12"))
    if not key: continue
    wb = xlrd.open_workbook(file_contents=gzip.decompress(open(raw / fn, "rb").read())); sh = wb.sheet_by_name("UCSC Genes FPKM") if "UCSC Genes FPKM" in wb.sheet_names() else wb.sheet_by_index(0)
    for r in range(1, sh.nrows):
        v = sh.row_values(r)
        if str(v[0]) in G: expr.setdefault((str(v[0]), key), []).append(float(v[1]))
mean = lambda g, k: f"{sum(expr[(g, k)]) / len(expr[(g, k)]):.1f}" if (g, k) in expr else "NA"
RES = Path(a.repo) / "disease-models/wwox/research/drug_repurposing/wwox_data_it24_p4_20261104/results/p47t_all_regions_tested_genes.tsv.gz"
p = {}
for r in csv.DictReader(gzip.open(RES, "rt"), delimiter="\t"):
    if r["symbol"] in G: p[(r["symbol"], r["region"])] = f"{float(r['log2FC_centred']):+.2f} ({float(r['FDR_no_sex']):.2g})"
with open(a.out, "w", newline="") as fh:
    w = csv.writer(fh, delimiter="\t", lineterminator="\n"); w.writerow(["gene", "neuron_FPKM", "astro_FPKM", "OPC_FPKM", "NFO_FPKM", "MO_FPKM", "microglia_FPKM", "endo_FPKM", "P47T_CTX_log2FC(FDR)", "P47T_PFC_log2FC(FDR)", "P47T_HPC_log2FC(FDR)", "P47T_CB_log2FC(FDR)"])
    for g in G: w.writerow([g] + [mean(g, k) for k in ("neuron", "astro", "OPC", "NFO", "MO", "microglia", "endo")] + [p.get((g, rg), "NA") for rg in ("CTX", "PFC", "HPC", "CB")])
print(open(a.out).read())
