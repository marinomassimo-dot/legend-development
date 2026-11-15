#!/usr/bin/env python3
"""Second read of IT49-Q02 (HE50 ISR extraction): recompute the class means and the 24 states from the raw tables, independently of
the HE50 extractor (own parsing, own grouping by sample or column names; only the join's published rule is reused: floor 1.0 FPKM, 3-fold).

Inputs: the GSE52564 raw directory (*.xls.gz, legacy Excel, needs xlrd: give the directory that holds it), the GSE73721 csv.gz, and the HE50
folder (isr_expression_mouse.tsv, isr_expression_human.tsv, isr_cell_class_states.tsv).
Prints: rows compared and discrepancies for the mouse class means (12 genes x 7 classes), the human group means (12 genes x 9 groups,
the 'mouse astrocyte' columns of that table are not used), and the 24 state rows (state, neuron value, best other value).
Run:  python3 -I recheck_isr.py <GSE52564_raw dir> <dir that holds xlrd> <GSE73721 csv.gz> <HE50 dir>      (--help prints this text)
"""
import collections
import csv
import glob
import gzip
import os
import re
import sys

GENES = ["EIF2AK1", "EIF2AK2", "EIF2AK3", "EIF2AK4", "EIF2B1", "EIF2B2", "EIF2B3", "EIF2B4", "EIF2B5", "PPP1R15A", "PPP1R15B", "EIF2S1"]
MCLASS = {"Astrocyte": "astrocytes (P7)", "Neuron": "neurons (P7)", "OPC": "OPC (P17)", "NFO": "newly formed oligodendrocytes (P17)",
          "MO": "myelinating oligodendrocytes (P17)", "Microglia": "microglia", "Endothelial": "endothelium"}


def rule(nv, others):
    ov = max(others)
    if max([nv] + others) < 1.0:
        return "NOT_DETECTED_IN_TABLE"
    if nv >= 3 * max(ov, 1e-9) and nv >= 1.0:
        return "NEURON_ENRICHED"
    if ov >= 3 * max(nv, 1e-9) and ov >= 1.0:
        return "OTHER_ENRICHED"
    return "SHARED"


def hgroup(h):
    l = h.lower()
    if l.startswith("mouse"):
        return None
    for key, name in (("tumor", "astro_tumor"), ("hippocampus", "astro_hippocampus_epilepsy_region")):
        if key in l:
            return name
    if l.startswith("fetal"):
        return "astro_fetal_ctx"
    if "ctx" in l and "astro" in l:
        return "astro_mature_ctx"
    for key, name in (("neuron", "neuron_ctx"), ("oligo", "oligo_ctx"), ("myeloid", "myeloid_ctx"), ("endo", "endo_ctx"), ("whole cortex", "whole_cortex")):
        if key in l:
            return name
    return None


def main():
    if "--help" in sys.argv or "-h" in sys.argv or len(sys.argv) < 5:
        print(__doc__)
        return 0
    raw, xdir, hcsv, he = sys.argv[1:5]
    he = he.rstrip("/") + "/"
    sys.path.insert(0, xdir)
    import xlrd
    mouse = collections.defaultdict(lambda: collections.defaultdict(list))
    for fn in sorted(glob.glob(os.path.join(raw, "*.xls.gz"))):
        cls = re.sub(r"\d+$", "", re.sub(r"^GSM\d+_", "", os.path.basename(fn)[:-7]))
        if cls not in MCLASS:
            continue
        s = xlrd.open_workbook(file_contents=gzip.open(fn).read()).sheet_by_index(0)
        names = {str(s.cell_value(r, 0)).strip().upper(): r for r in range(s.nrows)}
        for g in GENES:
            mouse[g][cls].append(float(s.cell_value(names[g], 1)))
    mm = {g: {MCLASS[c]: (sum(v) / len(v), len(v)) for c, v in d.items()} for g, d in mouse.items()}
    bad = tot = 0
    mx = 0.0
    for r in csv.DictReader(open(he + "isr_expression_mouse.tsv", encoding="utf-8"), delimiter="\t"):
        m, n = mm[r["gene"].upper()][r["cell_class"]]
        tot += 1
        mx = max(mx, abs(m - float(r["mean_fpkm"])))
        bad += (abs(m - float(r["mean_fpkm"])) > 0.006 or n != int(r["n_samples"]))
    print("mouse class means: %d rows compared, %d discrepancies, max |difference| %.4f FPKM" % (tot, bad, mx))
    rows = list(csv.reader(gzip.open(hcsv, "rt", encoding="utf-8", errors="replace")))
    hdr = [h.strip() for h in rows[0]]
    tab = {r[0].strip().upper(): r for r in rows[1:]}
    hm = {}
    for g in GENES:
        gr = collections.defaultdict(list)
        for i, h in enumerate(hdr[1:], 1):
            k = hgroup(h)
            if k:
                gr[k].append(float(tab[g][i]))
        hm[g] = {k: (sum(v) / len(v), len(v)) for k, v in gr.items()}
    bad = tot = 0
    mx = 0.0
    for r in csv.DictReader(open(he + "isr_expression_human.tsv", encoding="utf-8"), delimiter="\t"):
        if r["group"] not in hm[r["gene"].upper()]:
            continue
        m, n = hm[r["gene"].upper()][r["group"]]
        tot += 1
        mx = max(mx, abs(m - float(r["mean_fpkm"])))
        bad += (abs(m - float(r["mean_fpkm"])) > 0.006 or n != int(r["n_columns"]))
    print("human group means: %d rows compared, %d discrepancies, max |difference| %.4f FPKM" % (tot, bad, mx))
    ok = tot = 0
    for r in csv.DictReader(open(he + "isr_cell_class_states.tsv", encoding="utf-8"), delimiter="\t"):
        g = r["gene"].upper()
        if r["species"] == "mouse":
            cl = mm[g]
            nv = cl["neurons (P7)"][0]
            oth = [v[0] for k, v in cl.items() if k != "neurons (P7)"]
        else:
            cl = {k: v for k, v in hm[g].items() if k not in ("whole_cortex",)}
            nv = cl["neuron_ctx"][0]
            oth = [v[0] for k, v in cl.items() if k != "neuron_ctx"]
        mine = rule(nv, oth)
        tot += 1
        same = mine == r["state"] and abs(nv - float(r["neuron_fpkm"])) <= 0.006 and abs(max(oth) - float(r["best_other_fpkm"])) <= 0.006
        ok += same
        if not same:
            print("  DIFF", g, r["species"], mine, r["state"], round(nv, 2), round(max(oth), 2), r["neuron_fpkm"], r["best_other_fpkm"])
    print("state rows: %d of %d reproduced (state, neuron FPKM, best other FPKM)" % (ok, tot))
    return 0


if __name__ == "__main__":
    sys.exit(main())
