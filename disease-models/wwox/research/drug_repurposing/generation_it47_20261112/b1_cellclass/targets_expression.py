"""IT47 queue B1: the same extraction as SCI44 kchan_expression.py (copied; only the gene list and the output names differ): class means of RNA for the 30 target genes that had no row in the local GEO tables already used for the PDK question (no network).
  python3 -I kchan_expression.py <GSE52564 raw dir with *.xls.gz> <dir that holds xlrd> <GSE73721 csv.gz> <out dir>
Writes targets_expression_mouse.tsv and targets_expression_human.tsv (class means, replicate counts, input hashes) and prints nothing else. Predictions are in PREREGISTRATION.md and are scored by score_predictions.py.

HE50 (2026-11-13): the same script, made parametric so a fifth copy is not needed: `--genes EIF2AK1,EIF2B1,...` (human symbols; the mouse symbol is the same in title case, a naming convention) and `--prefix NAME`
(output file prefix) replace the built-in list and names. Without them the behaviour and the bytes of the outputs are unchanged (checked against the committed tables). With `--genes` it also prints to stderr, per gene,
what a join must not lose: a symbol absent from a table, and any class whose row count differs from its replicate files or any human symbol that appears on more than one row (an ambiguity, never averaged away silently)."""
import sys, os, gzip, csv, hashlib
if "--help" in sys.argv or "-h" in sys.argv or len(sys.argv) < 5:
    print(__doc__); sys.exit(0)
raw, xdir, hcsv, out = sys.argv[1:5]
_opt = lambda k: sys.argv[sys.argv.index(k) + 1] if k in sys.argv else None
PREFIX = _opt("--prefix") or "targets_expression"
sys.path.insert(0, xdir)
import xlrd
GENES = ['Gjd2', 'Gria1', 'Gria2', 'Gria3', 'Gria4', 'Grik1', 'Grik2', 'Grik3', 'Grik4', 'Grik5', 'Grin1', 'Grin2a', 'Grin2b', 'Grin2c', 'Grin2d', 'Hcn3', 'Hcn4', 'Kcnj12', 'Kcnj16', 'Kcnj4', 'Kcnk10', 'Kcnk13', 'Kcnk4', 'Kcnq4', 'Kcnq5', 'Panx1', 'Pdk1', 'Pdk2', 'Pdk3', 'Pdk4', 'Rbfox3', 'Gfap', 'Cldn5']
_given = _opt("--genes")
CUSTOM = bool(_given)
if CUSTOM:
    GENES = [g.strip().upper().capitalize() for g in _given.split(",") if g.strip()]   # mouse form of a human symbol: title case (EIF2AK1 -> Eif2ak1)
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
with open(os.path.join(out, PREFIX + "_mouse.tsv"), "w", newline="") as f:
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
with open(os.path.join(out, PREFIX + "_human.tsv"), "w", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n"); w.writerow(["gene", "group", "n_columns", "mean_fpkm", "input_sha256"])
    for r in rd:
        if r[0].upper() in up:
            for g, cols in groups.items():
                vals = [float(r[i]) for i in cols]
                w.writerow([r[0].upper(), g, len(vals), "%.2f" % (sum(vals) / len(vals)), sha])
if CUSTOM:
    nfiles = {}
    for fn in sorted(os.listdir(raw)):
        if fn.endswith(".xls.gz") and "WC" not in fn:
            k = CLASS.get(fn.split("_")[1].split(".")[0].rstrip("12"), fn.split("_")[1].split(".")[0].rstrip("12"))
            nfiles[k] = nfiles.get(k, 0) + 1
    for g in GENES:
        have = {c: len(v) for (gg, c), v in rows.items() if gg == g}
        if not have:
            print(f"MOUSE_ABSENT {g}: no row in any class (not queried or named differently; unknown, not low)", file=sys.stderr)
        for c, n in have.items():
            if n != nfiles.get(c):
                print(f"MOUSE_AMBIGUOUS {g} {c}: {n} rows for {nfiles.get(c)} replicate files", file=sys.stderr)
    seen = {}
    rd2 = csv.reader(gzip.open(hcsv, "rt", encoding="latin1")); next(rd2)
    for r in rd2:
        if r[0].upper() in up:
            seen[r[0].upper()] = seen.get(r[0].upper(), 0) + 1
    for g in GENES:
        if seen.get(g.upper(), 0) == 0:
            print(f"HUMAN_ABSENT {g.upper()}: no row in the table (unknown, not low)", file=sys.stderr)
        elif seen[g.upper()] > 1:
            print(f"HUMAN_AMBIGUOUS {g.upper()}: {seen[g.upper()]} rows for one symbol", file=sys.stderr)
