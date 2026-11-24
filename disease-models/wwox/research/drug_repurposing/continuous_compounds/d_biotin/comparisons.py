"""Reproduce the contrasts from published aggregates; no patient-level inference."""
import csv
import sys

writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
writer.writerow(("source", "measure", "reference", "exposed", "unit", "difference", "ratio"))
observations = [
    ("27264091 Table 1", "hippocampal free biotin pair-fed to deficient", 2.7, 0.5, "nmol/g protein"),
    ("27264091 Table 1", "cortical bound biotin pair-fed to deficient", 0.4, 0.9, "nmol/g protein"),
    ("12214565 Table II Roc-1", "PC replete to depleted", 5670, 252, "pmol/min/mg protein"),
    ("12214565 Table II Roc-1", "ACC replete to depleted", 1392, 602, "pmol/min/mg protein"),
    ("12214565 Table II mainly astrocytes", "PC replete to depleted", 5739, 1176, "pmol/min/mg protein"),
    ("12214565 Table II mainly astrocytes", "ACC replete to depleted", 1087, 724, "pmol/min/mg protein"),
    ("32470040 Fig2A table", "O4 cells wrapping at 1.25 ug/mL", 18.21, 26.82, "percent"),
    ("32470040 Fig2A table", "O4 cells wrapping at 250 ug/mL", 18.21, 27.58, "percent"),
    ("32470040 Results", "O4 cells wrapping at 250 ug/mL", 16.31, 27.58, "percent"),
    ("32470040 Fig2B table", "sheaths at 2.5 ug/mL", 2.796, 4.110, "per cell"),
    ("32470040 Fig2B table", "sheaths at 250 ug/mL", 2.796, 3.480, "per cell"),
    ("32470040 Fig3 Results", "ATP-linked oxygen consumption at 250 ug/mL", 2.7, 6.0, "pmol/min/ug protein"),
    ("18974016 Results", "simultaneous trough plasma to CSF", 1800, 1000, "nM total avidin binding"),
    ("33222767 author abstract", "confirmed improvement placebo to MD1003", 100*29/316, 100*39/326, "percent"),
]
for source, measure, reference, exposed, unit in observations:
    writer.writerow([source, measure, f"{reference:.6g}", f"{exposed:.6g}", unit,
                     f"{exposed-reference:.6g}", f"{exposed/reference:.6g}"])
