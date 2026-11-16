#!/usr/bin/env python3
"""I4: metabolic, ketone and adenosine axis on held tables. Panel table plus a composition check.

    python3 i4_axis.py --repo <root> --files <files dir> --xlrd <dir with xlrd> --out <dir>
    python3 i4_axis.py --help

Held inputs, read-only: P47T knock-in all-region mRNA table (GSE215425; n 5 v 5; mRNA of a missense line), the P17 neuron-deletion descriptive rows (only |centred log2 ratio| >= 0.585:
absence is NOT 'unchanged'), the GSE52564 cell-class RNA (neurons, astrocytes, OPC, NFO, MO, microglia, endothelium; FPKM). The composition check asks what the P47T bulk change of a gene would be
if it were only a shift in astrocyte share: genes are split by their class-table astrocyte/neuron ratio, and the observed change of a panel gene is placed against the distribution of the
astrocyte-enriched genes' changes. It is a descriptive check, not a deconvolution. Not medical advice.
"""
import argparse, csv, gzip, hashlib, json, math, os, statistics, sys
from pathlib import Path

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
for k in ("--repo", "--files", "--xlrd", "--out"): ap.add_argument(k)
a = ap.parse_args()
if not all([a.repo, a.files, a.xlrd, a.out]):
    ap.print_help(); sys.exit(0)
sys.path.insert(0, a.xlrd); import xlrd
repo, files, out = Path(a.repo), Path(a.files), Path(a.out); out.mkdir(parents=True, exist_ok=True)
RES = repo / "disease-models/wwox/research/drug_repurposing/wwox_data_it24_p4_20261104/results"
PANEL = {
 "adenosine": "Adora1 Adora2a Adk Slc29a1 Slc29a2 Nt5e Entpd1 Entpd2 Ada Ak1 Ak2",
 "ketone_energy": "Slc16a1 Slc16a7 Slc16a3 Bdh1 Oxct1 Acat1 Hmgcs2 Hmgcl Hcar2 Kcnj11 Abcc8 Cpt1a Ppargc1a Ppara Prkaa1 Prkaa2 Sirt1 Sirt3",
 "glycolysis_lactate_module": "Hk1 Hk2 Ldha Ldhb Slc2a1 Slc2a3 Pdk1 Pdk2 Pdk3 Pdk4 Pdha1 Pfkp Pkm Bnip3 Hif1a",
 "glial_reactivity": "Gfap Vim Aqp4 S100b Aldh1l1 Slc1a2 Slc1a3 Glul",
}
panel = {g: grp for grp, s in PANEL.items() for g in s.split()}
CL = {"Astrocyte": "astro", "Neuron": "neuron", "OPC": "OPC", "NFO": "NFO", "MO": "MO", "Microglia": "microglia", "Endothelial": "endo"}
raw = files / "geo/GSE52564_raw"; expr = {}; shas = {}
for fn in sorted(os.listdir(raw)):
    if not fn.endswith(".xls.gz") or "WC" in fn: continue
    key = CL.get(fn.split("_")[1].split(".")[0].rstrip("12"))
    if not key: continue
    blob = open(raw / fn, "rb").read(); shas[fn] = hashlib.sha256(blob).hexdigest()
    wb = xlrd.open_workbook(file_contents=gzip.decompress(blob)); sh = wb.sheet_by_name("UCSC Genes FPKM") if "UCSC Genes FPKM" in wb.sheet_names() else wb.sheet_by_index(0)
    for r in range(1, sh.nrows):
        v = sh.row_values(r); expr.setdefault(str(v[0]), {}).setdefault(key, []).append(float(v[1]))
mean = lambda x: sum(x) / len(x) if x else float("nan")
cls = {g: {k: mean(v) for k, v in e.items()} for g, e in expr.items()}
p47 = {}
for r in csv.DictReader(gzip.open(RES / "p47t_all_regions_tested_genes.tsv.gz", "rt"), delimiter="\t"):
    p47[(r["symbol"], r["region"])] = (float(r["log2FC_centred"]), float(r["FDR_no_sex"]), float(r["mean_norm_count_WT"]))
de = {}
for r in csv.DictReader(open(RES / "mouse_p17_descriptive_genes_cLFC_ge0.585_separated.tsv"), delimiter="\t"):
    de.setdefault(r["symbol"], []).append(f"{r['contrast']}:{float(r['centred_log2_ratio']):+.2f}")
# composition check: astro-enriched genes (class-table astro/neuron >= 3, both >= 2 FPKM floor on the larger) among genes tested in the region
astro = {g for g, c in cls.items() if "astro" in c and "neuron" in c and max(c["astro"], c["neuron"]) >= 5 and c["astro"] >= 3 * max(c["neuron"], 0.1)}
neur = {g for g, c in cls.items() if "astro" in c and "neuron" in c and max(c["astro"], c["neuron"]) >= 5 and c["neuron"] >= 3 * max(c["astro"], 0.1)}
regions = ("CTX", "HPC", "PFC", "CB"); comp = {}
for rg in regions:
    a_l = sorted(p47[(g, rg)][0] for g in astro if (g, rg) in p47); n_l = sorted(p47[(g, rg)][0] for g in neur if (g, rg) in p47)
    comp[rg] = {"n_astro_enriched": len(a_l), "median_astro_enriched_log2FC": round(statistics.median(a_l), 3), "n_neuron_enriched": len(n_l), "median_neuron_enriched_log2FC": round(statistics.median(n_l), 3),
                "sorted_astro": a_l, "sorted_neuron": n_l}
def pct(v, xs):  # share of the reference distribution at or below v
    return sum(1 for x in xs if x <= v) / len(xs)
with open(out / "panel_table.tsv", "w", newline="") as fh:
    w = csv.writer(fh, delimiter="\t", lineterminator="\n")
    w.writerow(["group", "gene", "neuron_FPKM", "astro_FPKM", "compartment"] + [f"P47T_{rg}_log2FC(FDR)" for rg in regions] + ["P47T_CTX_pct_among_astro_enriched", "P47T_CTX_pct_among_neuron_enriched", "P17_deletion_rows"])
    for g, grp in panel.items():
        c = cls.get(g, {}); n, an = c.get("neuron", float("nan")), c.get("astro", float("nan"))
        comp_lab = "NA" if n != n else ("astro-enriched" if an >= 3 * max(n, .1) else "neuron-enriched" if n >= 3 * max(an, .1) else "shared")
        cells = [f"{p47[(g, rg)][0]:+.2f} ({p47[(g, rg)][1]:.2g})" if (g, rg) in p47 else "NA" for rg in regions]
        pa = f"{pct(p47[(g, 'CTX')][0], comp['CTX']['sorted_astro']):.2f}" if (g, "CTX") in p47 else "NA"; pn = f"{pct(p47[(g, 'CTX')][0], comp['CTX']['sorted_neuron']):.2f}" if (g, "CTX") in p47 else "NA"
        w.writerow([grp, g, f"{n:.1f}", f"{an:.1f}", comp_lab] + cells + [pa, pn, ";".join(de.get(g, [])) or "none among |cLFC|>=0.585"])
with open(out / "composition_check.json", "w") as fh:
    json.dump({rg: {k: v for k, v in d.items() if not k.startswith("sorted")} for rg, d in comp.items()} | {"inputs_sha256": shas, "p47t_sha256": hashlib.sha256(open(RES / "p47t_all_regions_tested_genes.tsv.gz", "rb").read()).hexdigest(),
              "astro_enriched_rule": "astro/neuron FPKM ratio >= 3, larger class >= 5 FPKM", "neuron_enriched_rule": "neuron/astro ratio >= 3, same floor"}, fh, indent=1, sort_keys=True); fh.write("\n")
print("panel genes", len(panel), "| astro-enriched", len(astro), "neuron-enriched", len(neur))
