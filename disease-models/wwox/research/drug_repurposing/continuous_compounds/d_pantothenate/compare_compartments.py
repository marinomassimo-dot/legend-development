"""Recompute within-panel ratios of mean LC-MS signals without comparing absolute intensities across panels."""
from pathlib import Path
from statistics import mean
import csv
import sys
import openpyxl

root = Path(sys.argv[1])
writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
writer.writerow(("perturbation", "panel", "compartment", "species", "ctrl_n", "ko_n", "KO_over_control"))
for file, sheet, perturbation, compartment in [
    ("source6.xlsx", "3f", "COASY_KO", "whole_cell"),
    ("source8.xlsx", "5a", "A16_A42_DKO", "mitochondria"),
    ("source8.xlsx", "5c", "A16_A42_DKO", "whole_cell"),
]:
    wb = openpyxl.load_workbook(root/file, read_only=True, data_only=True)
    for row in wb[sheet].values:
        if not isinstance(row[1], str):
            continue
        name = " ".join(row[1].split())
        if name not in ("CoASH", "C2:0 acetyl-CoA", "C3:0 propionyl-CoA"):
            continue
        ctrl, ko = row[2:5], row[5:8]
        writer.writerow((perturbation, sheet, compartment, name, len(ctrl), len(ko), round(mean(ko)/mean(ctrl), 4)))
