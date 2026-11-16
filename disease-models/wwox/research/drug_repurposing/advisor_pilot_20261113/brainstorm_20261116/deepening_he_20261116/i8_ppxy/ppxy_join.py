#!/usr/bin/env python3
"""I8 join: PPxY scan x held expression x held null contrasts x matrix classes.

    python3 ppxy_join.py --scan <out dir of ppxy_scan.py> --repo <repo root> --files <files dir> --xlrd <dir holding xlrd> --out <dir>
    python3 ppxy_join.py --help

Held inputs (read-only): GSE52564 cell-class RNA (neurons P7, astrocytes P7, OPC, NFO, MO, microglia, endothelium; FPKM), the P47T knock-in all-region table
(GSE215425; mRNA of the missense line, n 5 v 5), the P17 neuron-deletion descriptive rows (|centred log2 ratio| >= 0.585 only: absence is NOT 'unchanged').
The question 'does WWOX loss change the SURFACE LEVEL of a PY-motif channel' is a protein-level question; every RNA column here is context, not a test.
Ranking is lexicographic and written in the header of candidates_ranked.tsv; it carries no weights. Not medical advice; mechanism labels only.
"""
import argparse, csv, gzip, hashlib, json, math, os, sys
from pathlib import Path

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument("--scan"); ap.add_argument("--repo"); ap.add_argument("--files"); ap.add_argument("--xlrd"); ap.add_argument("--out")
a = ap.parse_args()
if not all([a.scan, a.repo, a.files, a.xlrd, a.out]):
    ap.print_help(); sys.exit(0)
sys.path.insert(0, a.xlrd)
import xlrd
scan, repo, files, out = Path(a.scan), Path(a.repo), Path(a.files), Path(a.out); out.mkdir(parents=True, exist_ok=True)
HERE = Path(__file__).resolve().parent
DR = repo / "disease-models/wwox/research/drug_repurposing"; RES = DR / "wwox_data_it24_p4_20261104/results"
rows = lambda p, **k: list(csv.DictReader(open(p, newline=""), delimiter="\t"))
genes = [g for g in rows(scan / "ppxy_genes.tsv") if g["species"] == "mouse"]
# Benjamini-Hochberg over the mouse proteins that carry at least one core motif (p from the seeded shuffle; the family size is the number of tested proteins with a motif)
tested = sorted([g for g in genes if g["n_core_PPxY"] != "0"], key=lambda g: float(g["shuffle_p_core"]))
m = len(tested); q = {}; prev = 1.0
for i in range(m, 0, -1):
    g = tested[i - 1]; prev = min(prev, float(g["shuffle_p_core"]) * m / i); q[g["accession"]] = prev
# cell-class RNA for every motif-bearing gene (+ ligases, ligands and WWOX itself as controls)
CONTROL = ["Wwox", "Nedd4", "Nedd4l", "Itch", "Wwp1", "Wwp2", "Smurf1", "Smurf2", "Wbp1", "Wbp2", "Erbb4", "Yap1", "Tp73", "Scnn1b"]
want = {g["symbol"] for g in tested} | set(CONTROL) | {r["gene"] for r in rows(HERE / "class_targets.tsv")}
CLASS = {"Astrocyte": "astro", "Neuron": "neuron", "OPC": "OPC", "NFO": "NFO", "MO": "MO", "Microglia": "microglia", "Endothelial": "endo"}
raw = files / "geo/GSE52564_raw"; expr = {}; shas = {}
for fn in sorted(os.listdir(raw)):
    if not fn.endswith(".xls.gz") or "WC" in fn: continue
    key = CLASS.get(fn.split("_")[1].split(".")[0].rstrip("12"))
    if not key: continue
    blob = open(raw / fn, "rb").read(); shas[fn] = hashlib.sha256(blob).hexdigest()
    wb = xlrd.open_workbook(file_contents=gzip.decompress(blob)); sh = wb.sheet_by_name("UCSC Genes FPKM") if "UCSC Genes FPKM" in wb.sheet_names() else wb.sheet_by_index(0)
    for r in range(1, sh.nrows):
        v = sh.row_values(r)
        if str(v[0]) in want: expr.setdefault(str(v[0]), {}).setdefault(key, []).append(float(v[1]))
mean = lambda x: sum(x) / len(x) if x else float("nan")
# P47T (mRNA of the missense knock-in), CTX and HPC
p47 = {}
for r in csv.DictReader(gzip.open(RES / "p47t_all_regions_tested_genes.tsv.gz", "rt"), delimiter="\t"):
    if r["region"] in ("CTX", "HPC") and r["symbol"] in want: p47[(r["symbol"], r["region"])] = (float(r["log2FC_centred"]), float(r["FDR_no_sex"]))
# P17 deletion descriptive rows
de = {}
for r in rows(RES / "mouse_p17_descriptive_genes_cLFC_ge0.585_separated.tsv"):
    if r["symbol"] in want: de.setdefault(r["symbol"], []).append(f"{r['contrast']}:{float(r['centred_log2_ratio']):+.2f}")
cls = {}
for r in rows(HERE / "class_targets.tsv"): cls[r["gene"]] = r["matrix_class"]
motifs = rows(scan / "ppxy_motifs.tsv")
hum_only = {g["symbol"].upper(): g for g in rows(scan / "ppxy_genes.tsv") if g["species"] == "human"}
def f(x, nd=1): return "NA" if x != x else f"{x:.{nd}f}"
table = []
for g in tested:
    s = g["symbol"]; e = expr.get(s, {}); neu = mean(e.get("neuron", [])); non = max([mean(v) for k, v in e.items() if k != "neuron"] or [float("nan")])
    mw = [x for x in motifs if x["species"] == "mouse" and x["accession"] == g["accession"]]
    table.append({"symbol": s, "accession": g["accession"], "protein": g["name"][:60], "topology": g["topology"], "n_core": int(g["n_core_PPxY"]), "motifs": g["core_positions"], "shuffle_p": float(g["shuffle_p_core"]), "BH_q": round(q[g["accession"]], 4),
                  "human_ortholog": g["human_ortholog_core"], "neuron_P7_FPKM": f(neu), "best_other_class_FPKM": f(non), "neuron_enriched": "yes" if neu == neu and non == non and neu >= 2 * max(non, 0.1) else ("NA" if neu != neu else "no"),
                  "P47T_CTX_log2FC": f(p47[(s, "CTX")][0], 2) if (s, "CTX") in p47 else "NA", "P47T_CTX_FDR": f"{p47[(s, 'CTX')][1]:.2g}" if (s, "CTX") in p47 else "NA", "P47T_HPC_log2FC": f(p47[(s, "HPC")][0], 2) if (s, "HPC") in p47 else "NA",
                  "P17_deletion_rows": ";".join(de.get(s, [])) or "none among |cLFC|>=0.585", "matrix_class": cls.get(s, "none (outside the matrix)")})
def key(t):
    neu = float(t["neuron_P7_FPKM"]) if t["neuron_P7_FPKM"] != "NA" else -1
    return (0 if neu >= 2 else 1, 0 if t["topology"] == "annotated" else 1, 0 if t["human_ortholog"] == "conserved" else 1, t["shuffle_p"], -t["n_core"], t["symbol"])
table.sort(key=key)
hdr = "# Lexicographic order: (1) neuron P7 FPKM >= 2, (2) topology annotated, (3) motif conserved in the human ortholog, (4) shuffle p ascending, (5) more motifs, (6) symbol. No weights. RNA columns are context for a protein-level hypothesis, not a test of it.\n"
(out / "candidates_ranked_ORDER.txt").write_text(hdr)    # the ordering rule lives beside the table, never inside it (TSV width test)
with open(out / "candidates_ranked.tsv", "w", newline="") as fh:
    w = csv.DictWriter(fh, list(table[0]), delimiter="\t", lineterminator="\n"); w.writeheader(); w.writerows(table)
ctl = []
for s in CONTROL:
    e = expr.get(s, {}); ctl.append({"gene": s, **{k: f(mean(e.get(k, [])), 1) for k in ("neuron", "astro", "OPC", "NFO", "MO", "microglia", "endo")}, "P47T_CTX_log2FC": f(p47[(s, "CTX")][0], 2) if (s, "CTX") in p47 else "NA", "P47T_CTX_FDR": f"{p47[(s, 'CTX')][1]:.2g}" if (s, "CTX") in p47 else "NA", "P17_deletion_rows": ";".join(de.get(s, [])) or "none among |cLFC|>=0.585"})
with open(out / "controls_ligases_ligands.tsv", "w", newline="") as fh:
    w = csv.DictWriter(fh, list(ctl[0]), delimiter="\t", lineterminator="\n"); w.writeheader(); w.writerows(ctl)
# every class-target gene against the scan: in the universe? motif? (so that a class with no motif is stated, not omitted)
allg = {g["symbol"]: g for g in rows(scan / "ppxy_genes.tsv") if g["species"] == "mouse"}
with open(out / "class_targets_scan.tsv", "w", newline="") as fh:
    w = csv.writer(fh, delimiter="\t", lineterminator="\n"); w.writerow(["gene", "matrix_class", "in_universe", "topology", "n_core_PPxY", "core_positions", "n_LPxY", "shuffle_p_core"])
    for r in rows(HERE / "class_targets.tsv"):
        x = allg.get(r["gene"]); w.writerow([r["gene"], r["matrix_class"]] + (["no", "", "", "", "", ""] if not x else ["yes", x["topology"], x["n_core_PPxY"], x["core_positions"], x["n_LPxY"], x["shuffle_p_core"]]))
(out / "join_run.json").write_text(json.dumps({"raw_inputs_sha256": shas, "p47t_table_sha256": hashlib.sha256(open(RES / "p47t_all_regions_tested_genes.tsv.gz", "rb").read()).hexdigest(), "tested_proteins": m}, indent=1, sort_keys=True) + "\n")
print(f"candidates {len(table)}; neuron >= 2 FPKM: {sum(1 for t in table if t['neuron_P7_FPKM'] != 'NA' and float(t['neuron_P7_FPKM']) >= 2)}")
