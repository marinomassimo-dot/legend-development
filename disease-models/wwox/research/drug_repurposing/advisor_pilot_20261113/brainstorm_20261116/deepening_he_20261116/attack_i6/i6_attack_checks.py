#!/usr/bin/env python3
"""HE's attack on SCI's I6 (chloride headroom): two checks on held numbers.

    python3 i6_attack_checks.py --repo <root> --files <files dir> --xlrd <dir> --out <dir>
    python3 i6_attack_checks.py --help

Check 1: in which cell classes are Slc12a5 (KCC2) and Slc12a2 (NKCC1) read in the held cell-class table (GSE52564), and what do the held P47T and P17 rows say? A bulk transcript ratio carries the composition of the tissue.
Check 2: the chloride level at which E_Cl equals the resting potential, with the HELD resting potentials of the S-KO pyramidal neurons (-79.25, -75.51, -73.62 mV) instead of one assumed value. Nernst: E_Cl = 61.5 mV * log10([Cl]i/[Cl]o) at about 37 C; [Cl]o = 130 mM is ASSUMED
(and scanned 120 to 140). GABA-A hyperpolarises while E_Cl < Vrest, so the threshold chloride is [Cl]o * 10^(Vrest/61.5). Not medical advice.
"""
import argparse, csv, gzip, math, os, sys
from pathlib import Path

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
for k in ("--repo", "--files", "--xlrd", "--out"): ap.add_argument(k)
a = ap.parse_args()
if not all([a.repo, a.files, a.xlrd, a.out]):
    ap.print_help(); sys.exit(0)
sys.path.insert(0, a.xlrd); import xlrd
out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
RES = Path(a.repo) / "disease-models/wwox/research/drug_repurposing/wwox_data_it24_p4_20261104/results"
CL = {"Astrocyte": "astro", "Neuron": "neuron", "OPC": "OPC", "NFO": "NFO", "MO": "MO", "Microglia": "microglia", "Endothelial": "endo"}
GENES = ["Slc12a5", "Slc12a2", "Mbp", "Mobp", "Plp1"]
raw = Path(a.files) / "geo/GSE52564_raw"; expr = {}
for fn in sorted(os.listdir(raw)):
    if not fn.endswith(".xls.gz") or "WC" in fn: continue
    key = CL.get(fn.split("_")[1].split(".")[0].rstrip("12"))
    if not key: continue
    wb = xlrd.open_workbook(file_contents=gzip.decompress(open(raw / fn, "rb").read())); sh = wb.sheet_by_name("UCSC Genes FPKM") if "UCSC Genes FPKM" in wb.sheet_names() else wb.sheet_by_index(0)
    for r in range(1, sh.nrows):
        v = sh.row_values(r)
        if str(v[0]) in GENES: expr.setdefault((str(v[0]), key), []).append(float(v[1]))
mean = lambda x: sum(x) / len(x)
de = {}
for r in csv.DictReader(open(RES / "mouse_p17_descriptive_genes_cLFC_ge0.585_separated.tsv"), delimiter="\t"):
    if r["symbol"] in GENES: de.setdefault(r["symbol"], []).append(f"{r['contrast']}:{float(r['centred_log2_ratio']):+.2f}")
p47 = {}
for r in csv.DictReader(gzip.open(RES / "p47t_all_regions_tested_genes.tsv.gz", "rt"), delimiter="\t"):
    if r["symbol"] in GENES and r["region"] in ("CTX", "HPC"): p47[(r["symbol"], r["region"])] = f"{float(r['log2FC_centred']):+.2f} (FDR {float(r['FDR_no_sex']):.2g})"
with open(out / "check1_cell_class_slc12.tsv", "w", newline="") as fh:
    w = csv.writer(fh, delimiter="\t", lineterminator="\n"); w.writerow(["gene", "neuron", "astro", "OPC", "NFO", "MO", "microglia", "endo", "P47T_CTX", "P47T_HPC", "P17_deletion_rows"])
    for g in GENES:
        w.writerow([g] + [f"{mean(expr[(g, k)]):.1f}" if (g, k) in expr else "NA" for k in ("neuron", "astro", "OPC", "NFO", "MO", "microglia", "endo")] + [p47.get((g, "CTX"), "NA"), p47.get((g, "HPC"), "NA"), ";".join(de.get(g, [])) or "none among |cLFC|>=0.585"])
with open(out / "check2_chloride_threshold.tsv", "w", newline="") as fh:
    w = csv.writer(fh, delimiter="\t", lineterminator="\n"); w.writerow(["resting_potential_mV", "source", "Cl_out_mM", "Cl_in_at_E_Cl_equals_Vrest_mM"])
    for v, src in ((-65.0, "I6 assumed value"), (-79.25, "held S-WT"), (-75.51, "held S-HET"), (-73.62, "held S-KO")):
        for co in (120.0, 130.0, 140.0):
            w.writerow([v, src, co, f"{co * 10 ** (v / 61.5):.2f}"])
print(open(out / "check1_cell_class_slc12.tsv").read()); print(open(out / "check2_chloride_threshold.tsv").read())
