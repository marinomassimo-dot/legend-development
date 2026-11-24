"""Recalculate group-mean changes reported in PMID 16126180's author abstract."""
import csv
import sys

writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
writer.writerow(("species", "matrix", "time_min", "unit", "control", "after_UMP", "treated_over_control"))
for species, matrix, time, unit, control, treated in (
    ("uridine", "plasma", 30, "uM", 6.6, 32.7),
    ("uridine", "whole brain", 30, "pmol/mg", 22.6, 89.1),
    ("UTP", "whole brain", 15, "pmol/mg", 254, 417),
    ("CTP", "whole brain", 15, "pmol/mg", 56.8, 71.7),
    ("CDP-choline", "whole brain", 15, "pmol/mg", 11.3, 16.4),
):
    writer.writerow((species, matrix, time, unit, control, treated, round(treated/control, 4)))
