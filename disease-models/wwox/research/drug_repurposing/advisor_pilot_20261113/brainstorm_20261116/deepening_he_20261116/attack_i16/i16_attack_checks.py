#!/usr/bin/env python3
"""HE's checks on SCI's I16 (astroglial K+ buffering) against the original tables.

    python3 i16_attack_checks.py --repo <root> --files <files dir> --xlrd <dir> --out <dir>
    python3 i16_attack_checks.py --help

Check 1: SCI's raw knockout/control ratios (regional_astro.tsv) re-expressed after the library-wide median shift that the IT24 analysis removes (mouse_p17_summary.json: C_S -0.2023, H_S -0.3892 log2),
the same centring as the descriptive rows (verified on Gfap hippocampus: raw 4.34 -> +2.51, the value in the IT24 row). Check 2: how the astrocyte-enriched genes (class table GSE52564: astro/neuron FPKM >= 3, larger >= 5)
distribute among the descriptive rows of each contrast against neuron-enriched genes (rows also require animal separation and TPM >= 1: absence from them is not 'unchanged'). Descriptive. Not medical advice.
"""
import argparse, csv, gzip, json, math, os, statistics, sys
from pathlib import Path
ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
for k in ("--repo", "--files", "--xlrd", "--out"): ap.add_argument(k)
a = ap.parse_args()
if not all([a.repo, a.files, a.xlrd, a.out]):
    ap.print_help(); sys.exit(0)
sys.path.insert(0, a.xlrd); import xlrd
repo, out = Path(a.repo), Path(a.out); out.mkdir(parents=True, exist_ok=True)
DR = repo / "disease-models/wwox/research/drug_repurposing"; RES = DR / "wwox_data_it24_p4_20261104/results"
summ = json.load(open(RES / "mouse_p17_summary.json"))["contrasts"]; shift = {"cortex": summ["C_S"]["median_shift"], "hippocampus": summ["H_S"]["median_shift"]}
ra = list(csv.DictReader(open(DR / "advisor_pilot_20261113/brainstorm_20261116/deepening_sci_20261116/regional_astro.tsv"), delimiter="\t"))
with open(out / "check1_centred_ratios.tsv", "w", newline="") as fh:
    w = csv.writer(fh, delimiter="\t", lineterminator="\n"); w.writerow(["gene", "cortex_raw_ratio", "cortex_raw_log2", "cortex_centred_log2", "hippocampus_raw_ratio", "hippocampus_raw_log2", "hippocampus_centred_log2"])
    for r in ra:
        c, h = float(r["cortex_S_KO_over_ctrl"]), float(r["hippo_S_KO_over_ctrl"])
        w.writerow([r["gene"], c, f"{math.log2(c):+.2f}", f"{math.log2(c) - shift['cortex']:+.2f}", h, f"{math.log2(h):+.2f}", f"{math.log2(h) - shift['hippocampus']:+.2f}"])
CL = {"Astrocyte": "astro", "Neuron": "neuron"}; raw = Path(a.files) / "geo/GSE52564_raw"; ex = {}
for fn in sorted(os.listdir(raw)):
    if not fn.endswith(".xls.gz") or "WC" in fn: continue
    k = CL.get(fn.split("_")[1].split(".")[0].rstrip("12"))
    if not k: continue
    wb = xlrd.open_workbook(file_contents=gzip.decompress(open(raw / fn, "rb").read())); sh = wb.sheet_by_name("UCSC Genes FPKM") if "UCSC Genes FPKM" in wb.sheet_names() else wb.sheet_by_index(0)
    for r in range(1, sh.nrows):
        v = sh.row_values(r); ex.setdefault(str(v[0]), {}).setdefault(k, []).append(float(v[1]))
m = lambda g, k: sum(ex[g][k]) / len(ex[g][k]) if g in ex and k in ex[g] else None
ok = [g for g in ex if m(g, "astro") is not None and m(g, "neuron") is not None and max(m(g, "astro"), m(g, "neuron")) >= 5]
astro = {g for g in ok if m(g, "astro") >= 3 * max(m(g, "neuron"), 0.1)}; neur = {g for g in ok if m(g, "neuron") >= 3 * max(m(g, "astro"), 0.1)}
rows = list(csv.DictReader(open(RES / "mouse_p17_descriptive_genes_cLFC_ge0.585_separated.tsv"), delimiter="\t"))
with open(out / "check2_class_direction.tsv", "w", newline="") as fh:
    w = csv.writer(fh, delimiter="\t", lineterminator="\n"); w.writerow(["contrast", "descriptive_rows", "astro_enriched_rows", "astro_down", "astro_up", "astro_median_centred_log2", "neuron_enriched_rows", "neuron_down", "neuron_up", "neuron_median_centred_log2"])
    for c in ("C_S", "H_S", "H_N", "H_null"):
        rr = [r for r in rows if r["contrast"] == c]; A = [float(r["centred_log2_ratio"]) for r in rr if r["symbol"] in astro]; N = [float(r["centred_log2_ratio"]) for r in rr if r["symbol"] in neur]
        w.writerow([c, len(rr), len(A), sum(x < 0 for x in A), sum(x > 0 for x in A), f"{statistics.median(A):+.2f}", len(N), sum(x < 0 for x in N), sum(x > 0 for x in N), f"{statistics.median(N):+.2f}"])
print(open(out / "check1_centred_ratios.tsv").read()); print(open(out / "check2_class_direction.tsv").read())
print("astro-enriched genes", len(astro), "neuron-enriched", len(neur))
