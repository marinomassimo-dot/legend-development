"""Convert published pantothenate group summaries to acid-equivalent micromolar units."""
import csv
import sys

mw = 219.23  # g/mol for pantothenic acid; LC-MS assayed the circulating analyte
rows = [
    ("Rao Table 3", "adult plasma single fasted 500 mg", 8, 672, "ng/mL"),
    ("Rao Table 3", "adult plasma single fasted 1000 mg", 8, 1749, "ng/mL"),
    ("Rao Table 3", "adult plasma single fasted 2000 mg", 8, 5087, "ng/mL"),
    ("Rao Table 3", "adult plasma single fasted 5000 mg", 8, 3556, "ng/mL"),
    ("Rao Table 3", "adult plasma single fed 5000 mg", 8, 4464, "ng/mL"),
    ("Rao Table 5", "adult plasma day 1 peak", 8, 2423, "ng/mL"),
    ("Rao Table 5", "adult plasma day 14 peak", 8, 5971, "ng/mL"),
    ("Rao Table 5", "adult plasma day 1 AUC0-24", 8, 9185, "ng*h/mL"),
    ("Rao Table 5", "adult plasma day 14 AUC0-24", 8, 27130, "ng*h/mL"),
    ("Dastur Table 1", "adult control CSF mean", 5, 228, "ng/mL"),
    ("Dastur Table 1", "adult control CSF standard error", 5, 15, "ng/mL"),
    ("Dastur Table 1", "adult control blood mean", 64, 277, "ng/mL"),
    ("SLC5A6 Table 3", "untreated serum case 2-1", 1, 44.79, "ug/L"),
]
writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
writer.writerow(("source", "population_and_measure", "n", "reported_value", "reported_unit", "uM_or_24h_mean_uM"))
for source, measure, n, value, unit in rows:
    duration = 24 if unit == "ng*h/mL" else 1
    writer.writerow((source, measure, n, value, unit, round(value / mw / duration, 4)))
