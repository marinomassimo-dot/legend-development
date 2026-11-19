#!/usr/bin/env python3
"""Human neocortex marker time course from the BrainSpan gene-level RPKM zip, per the frozen ADV-088 pre-registration.

Read-only. Usage: python3 -I human_timecourse.py EXTRACTED_DIR OUT_TSV
EXTRACTED_DIR holds expression_matrix.csv, rows_metadata.csv and columns_metadata.csv (the unzipped
"RNA-Seq Gencode v10 summarized to genes" download). Neocortical regions only (A1C, DFC, IPC, ITC, M1C,
MFC, OFC, S1C, STC, V1C, VFC); one value per donor = mean RPKM over the donor's neocortical samples;
plateau = mean over donors aged 10 years or more; fraction of plateau computed on the linear RPKM scale.
"""
import csv
import re
import sys
from pathlib import Path

MARKERS = [
    "WWOX", "PVALB", "GAD1", "GAD2", "SST", "VIP", "LHX6", "NKX2-1", "SLC12A5", "SLC12A2",
    "KCNC1", "SYT2", "ACAN", "GABRA1", "GABRA2", "MBP", "PLP1", "MOG", "MOBP", "MAG", "CNP",
]
NEOCORTEX = {"A1C", "DFC", "IPC", "ITC", "M1C", "MFC", "OFC", "S1C", "STC", "V1C", "VFC"}


def age_years(label):
    """Years since birth (negative before birth: pcw counted from conception, birth at 40 pcw)."""
    n, unit = label.split()
    n = float(n)
    if unit == "pcw":
        return (n - 40.0) / 52.18
    if unit == "mos":
        return n / 12.0
    return n


def main(argv):
    if len(argv) != 3 or argv[1] in ("-h", "--help"):
        print(__doc__)
        return 0 if len(argv) > 1 and argv[1] in ("-h", "--help") else 2
    d, out = Path(argv[1]), argv[2]
    rows = {r["gene_symbol"]: int(r["row_num"]) for r in csv.DictReader(open(d / "rows_metadata.csv", encoding="utf-8"))}
    cols = list(csv.DictReader(open(d / "columns_metadata.csv", encoding="utf-8")))
    use = [int(c["column_num"]) for c in cols if c["structure_acronym"] in NEOCORTEX]
    donor = {int(c["column_num"]): (c["donor_name"], c["age"]) for c in cols}
    want = {rows[s]: s for s in MARKERS if s in rows}
    values = {}
    with open(d / "expression_matrix.csv", encoding="utf-8") as fh:
        for line in fh:
            parts = line.rstrip("\n").split(",")
            rn = int(parts[0])
            if rn in want:
                values[want[rn]] = parts
    donors = {}
    for cn in use:
        donors.setdefault(donor[cn], []).append(cn)
    table = []
    for (name, age), cns in donors.items():
        rec = {"donor": name, "age": age, "age_years": round(age_years(age), 3), "neocortical_samples": len(cns)}
        for s in MARKERS:
            if s in values:
                rec[s] = round(sum(float(values[s][c]) for c in cns) / len(cns), 3)
        table.append(rec)
    table.sort(key=lambda r: r["age_years"])
    plateau_donors = [r for r in table if r["age_years"] >= 10]
    plateau = {s: sum(r[s] for r in plateau_donors) / len(plateau_donors) for s in MARKERS if s in values}
    for r in table:
        for s in plateau:
            r["frac_" + s] = round(r[s] / plateau[s], 3) if plateau[s] > 0 else ""
    keys = list(table[0].keys())
    with open(out, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=keys, delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(table)
    print("donors", len(table), "plateau donors", len(plateau_donors), "markers found", sorted(plateau))
    print("absent:", [s for s in MARKERS if s not in values])
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
