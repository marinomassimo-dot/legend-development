#!/usr/bin/env python3
"""Class means of gene RNA in the two local public GEO tables the SCI44, SCI46 and IT46 questions used (no network).

Three scripts (kchan_expression.py, nrf2_expression.py, chloride_gaba_expression.py) were the same 50 lines with another gene list and another output name.
This is that extraction with the genes and the prefix as arguments. It reproduces their output files byte for byte (test_rna_class_means.py names the committed files it
is checked against), and it adds one file, `<prefix>_extraction_report.tsv`, which says for every requested gene whether it was found, found twice in one table, or not found
in a table: a gene absent from a table is *missing*, never a zero. The mean is the only number computed; no threshold, presence/absence call or biological reading is made here.

  python3 framework/scripts/rna_class_means.py --genes Keap1,Nfe2l2,Nqo1 --prefix nrf2_expression --mouse-raw <GSE52564 dir with *.xls.gz> \\
      --human-csv <GSE73721 table csv.gz> --out <output dir> [--human-extra G6PD] [--xlrd-dir <dir that holds xlrd>]

Outputs: <prefix>_mouse.tsv (gene, cell_class, n_samples, mean_fpkm, values, samples, input_sha256_first), <prefix>_human.tsv (gene, group, n_columns, mean_fpkm, input_sha256),
<prefix>_extraction_report.tsv (organism, gene, state, detail, input_sha256). Mouse: FPKM of the UCSC Genes sheet, one value per sample file, class from the file name.
Human: the table's columns grouped by the wording of their header; an empty or non-numeric cell is left out of the mean and counted in the report.
The two label maps below are the dataset's own and are the only interpretive step.
"""
from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import os
import sys
from collections import Counter

MOUSE_CLASS = {"Astrocyte": "astrocytes (P7)", "Neuron": "neurons (P7)", "OPC": "OPC (P17)", "NFO": "newly formed oligodendrocytes (P17)",
               "MO": "myelinating oligodendrocytes (P17)", "Microglia": "microglia", "Endothelial": "endothelium"}


def human_group(header: str) -> str:
    h = header.strip()
    if h.endswith("tumor periphery astro") or "tumor core astro" in h:
        return "astro_tumor"
    if "Hippocampus astro" in h:
        return "astro_hippocampus_epilepsy_region"
    if h.startswith("Fetal"):
        return "astro_fetal_ctx"
    if "ctx" in h and h.endswith("astro"):
        return "astro_mature_ctx"
    for end, name in (("neuron", "neuron_ctx"), ("oligo", "oligo_ctx"), ("myeloid", "myeloid_ctx"), ("endo", "endo_ctx")):
        if h.endswith(end):
            return name
    if "whole cortex" in h:
        return "whole_cortex"
    if h.startswith("Mouse"):
        return "mouse_astro"
    return "other"


def sha256(path: str) -> str:
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def sheet_rows(path: str) -> list[list]:
    """Rows of the UCSC Genes FPKM sheet (else the first sheet) of a gzipped .xls."""
    import xlrd
    wb = xlrd.open_workbook(file_contents=gzip.open(path).read())
    sh = wb.sheet_by_name("UCSC Genes FPKM") if "UCSC Genes FPKM" in wb.sheet_names() else wb.sheet_by_index(0)
    return [sh.row_values(r) for r in range(1, sh.nrows)]


def extract_mouse(raw: str, genes: list[str], reader=sheet_rows):
    """(rows keyed by (gene, class), report lines). A symbol found twice in one file is kept as two values and reported."""
    rows, seen, dup, files = {}, set(), [], []
    for fn in sorted(os.listdir(raw)):
        if not fn.endswith(".xls.gz") or "WC" in fn:
            continue
        key = fn.split("_")[1].split(".")[0].rstrip("12")
        path = os.path.join(raw, fn)
        sha = sha256(path)
        files.append((fn, sha))
        here = Counter()
        for v in reader(path):
            if str(v[0]) in genes:
                rows.setdefault((str(v[0]), MOUSE_CLASS.get(key, key)), []).append((float(v[1]), fn, sha))
                here[str(v[0])] += 1
        seen |= set(here)
        dup += [(g, fn, sha) for g, n in here.items() if n > 1]
    report = [("mouse", g, "FOUND", ";".join(sorted({c for (gg, c) in rows if gg == g})), "") for g in genes if g in seen]
    report += [("mouse", g, "DUPLICATE_ROWS", f"the symbol appears more than once in {fn}: each row is a separate value", sha) for g, fn, sha in dup]
    report += [("mouse", g, "NOT_FOUND", "absent from every sample table read: missing, not zero", "") for g in genes if g not in seen]
    return rows, report, files


def extract_human(csv_path: str, genes: list[str], extra: list[str] = ()):
    """(output rows, report lines). Group columns by header wording; an empty or non-numeric cell is missing and left out of that mean."""
    sha = sha256(csv_path)
    rd = csv.reader(gzip.open(csv_path, "rt", encoding="latin1"))
    hdr = next(rd)
    groups: dict[str, list[int]] = {}
    for i, h in enumerate(hdr[1:], start=1):
        groups.setdefault(human_group(h), []).append(i)
    up = {x.upper() for x in genes} | {x.upper() for x in extra}
    out, count, missing = [], Counter(), Counter()
    for r in rd:
        if r[0].upper() not in up:
            continue
        count[r[0].upper()] += 1
        for g, cols in groups.items():
            vals = []
            for i in cols:
                try:
                    vals.append(float(r[i]))
                except (ValueError, IndexError):
                    missing[r[0].upper()] += 1
            if vals:
                out.append([r[0].upper(), g, len(vals), "%.2f" % (sum(vals) / len(vals)), sha])
    report = [("human", g, "FOUND", f"{count[g.upper()]} row(s)" + (f"; {missing[g.upper()]} empty or non-numeric cell(s) left out" if missing[g.upper()] else ""), sha)
              for g in genes if count[g.upper()] == 1]
    report += [("human", g, "DUPLICATE_ROWS", f"{count[g.upper()]} rows carry this symbol: each is written as its own line", sha) for g in genes if count[g.upper()] > 1]
    report += [("human", g, "NOT_FOUND", "absent from the table: missing, not zero", sha) for g in genes if count[g.upper()] == 0]
    return out, report


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--genes", required=True, help="comma-separated mouse symbols, as written in the sheet (human rows are matched upper-case)")
    ap.add_argument("--prefix", required=True)
    ap.add_argument("--mouse-raw", required=True)
    ap.add_argument("--human-csv", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--human-extra", default="", help="comma-separated additional human symbols to read (an alias the mouse name does not give)")
    ap.add_argument("--xlrd-dir", default="")
    a = ap.parse_args(argv)
    if a.xlrd_dir:
        sys.path.insert(0, a.xlrd_dir)
    genes = [g for g in a.genes.split(",") if g]
    mouse, rep_m, files = extract_mouse(a.mouse_raw, genes)
    human, rep_h = extract_human(a.human_csv, genes, [g for g in a.human_extra.split(",") if g])
    os.makedirs(a.out, exist_ok=True)

    def table(name, header, lines):
        with open(os.path.join(a.out, f"{a.prefix}_{name}.tsv"), "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f, delimiter="\t", lineterminator="\n")
            w.writerow(header)
            w.writerows(lines)

    table("mouse", ["gene", "cell_class", "n_samples", "mean_fpkm", "values", "samples", "input_sha256_first"],
          [[g, c, len(vs), "%.2f" % (sum(x[0] for x in vs) / len(vs)), ";".join("%.2f" % x[0] for x in vs), ";".join(x[1] for x in vs), vs[0][2]] for (g, c), vs in sorted(mouse.items())])
    table("human", ["gene", "group", "n_columns", "mean_fpkm", "input_sha256"], human)
    table("extraction_report", ["organism", "gene", "state", "detail", "input_sha256"], rep_m + rep_h)
    return 0


if __name__ == "__main__":
    sys.exit(main())
