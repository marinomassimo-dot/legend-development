"""SCI44 coda: class means of K-channel gene RNA in the local GEO tables already used for the PDK question (no network).
  python3 -I kchan_expression.py <GSE52564 raw dir with *.xls.gz> <dir that holds xlrd> <GSE73721 csv.gz> <out dir>
Writes kchan_expression_mouse.tsv and kchan_expression_human.tsv (class means, replicate counts, input hashes) and prints nothing else. Predictions are in PREREGISTRATION.md and are scored by score_predictions.py."""
import sys, os, gzip, csv, hashlib
if "--help" in sys.argv or "-h" in sys.argv or len(sys.argv) < 5:
    print(__doc__); sys.exit(0)
raw, xdir, hcsv, out = sys.argv[1:5]
sys.path.insert(0, xdir)
import xlrd
GENES = ["Kcnj11", "Abcc8", "Kcnj8", "Abcc9", "Kcnj10", "Kcnj2", "Kcnj3", "Kcnj6", "Kcnk1", "Kcnk2", "Kcnk3", "Kcnk9", "Kcnq2", "Kcnq3", "Hcn1", "Hcn2", "Kcnc1", "Kcna1", "Rbfox3", "Gfap", "Cldn5"]
CLASS = {"Astrocyte": "astrocytes (P7)", "Neuron": "neurons (P7)", "OPC": "OPC (P17)", "NFO": "newly formed oligodendrocytes (P17)", "MO": "myelinating oligodendrocytes (P17)", "Microglia": "microglia", "Endothelial": "endothelium"}
rows = {}
for fn in sorted(os.listdir(raw)):
    if not fn.endswith(".xls.gz") or "WC" in fn: continue
    key = fn.split("_")[1].split(".")[0].rstrip("12")
    sha = hashlib.sha256(open(os.path.join(raw, fn), "rb").read()).hexdigest()
    wb = xlrd.open_workbook(file_contents=gzip.open(os.path.join(raw, fn)).read())
    sh = wb.sheet_by_name("UCSC Genes FPKM") if "UCSC Genes FPKM" in wb.sheet_names() else wb.sheet_by_index(0)
    for r in range(1, sh.nrows):
        v = sh.row_values(r)
        if str(v[0]) in GENES:
            rows.setdefault((str(v[0]), CLASS.get(key, key)), []).append((float(v[1]), fn, sha))
with open(os.path.join(out, "kchan_expression_mouse.tsv"), "w", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n"); w.writerow(["gene", "cell_class", "n_samples", "mean_fpkm", "values", "samples", "input_sha256_first"])
    for (g, c), vs in sorted(rows.items()):
        w.writerow([g, c, len(vs), "%.2f" % (sum(x[0] for x in vs) / len(vs)), ";".join("%.2f" % x[0] for x in vs), ";".join(x[1] for x in vs), vs[0][2]])
sha = hashlib.sha256(open(hcsv, "rb").read()).hexdigest()
rd = csv.reader(gzip.open(hcsv, "rt", encoding="latin1")); hdr = next(rd); groups = {}
for i, h in enumerate(hdr[1:], start=1):
    h2 = h.strip()
    if h2.endswith("tumor periphery astro") or "tumor core astro" in h2: g = "astro_tumor"
    elif "Hippocampus astro" in h2: g = "astro_hippocampus_epilepsy_region"
    elif h2.startswith("Fetal"): g = "astro_fetal_ctx"
    elif "ctx" in h2 and h2.endswith("astro"): g = "astro_mature_ctx"
    elif h2.endswith("neuron"): g = "neuron_ctx"
    elif h2.endswith("oligo"): g = "oligo_ctx"
    elif h2.endswith("myeloid"): g = "myeloid_ctx"
    elif h2.endswith("endo"): g = "endo_ctx"
    elif "whole cortex" in h2: g = "whole_cortex"
    elif h2.startswith("Mouse"): g = "mouse_astro"
    else: g = "other"
    groups.setdefault(g, []).append(i)
up = {x.upper() for x in GENES}
with open(os.path.join(out, "kchan_expression_human.tsv"), "w", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n"); w.writerow(["gene", "group", "n_columns", "mean_fpkm", "input_sha256"])
    for r in rd:
        if r[0].upper() in up:
            for g, cols in groups.items():
                vals = [float(r[i]) for i in cols]
                w.writerow([r[0].upper(), g, len(vals), "%.2f" % (sum(vals) / len(vals)), sha])
