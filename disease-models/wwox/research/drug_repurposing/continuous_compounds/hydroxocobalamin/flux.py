"""Reanalyse paired fibroblast propionate incorporation in public Forny source data."""
import csv
from pathlib import Path
from statistics import median
import sys
from openpyxl import load_workbook

folder = Path(sys.argv[1]) / "deepening_downloads/hydroxocobalamin_loop_20261124"
book = load_workbook(folder / "forny_s4.xlsx", read_only=True, data_only=True)
header, *values = book.active.values
rows = [dict(zip(header, row)) for row in values]
assert len(rows) == len({row[None] for row in rows}) == 230
def paired(row):
    return all(isinstance(row[k], (int, float)) and row[k] > 0 for k in ("OHCblMinus", "OHCblPlus"))

controls = [r for r in rows if r["case"] == 0 and paired(r)]
control_treated = median(r["OHCblPlus"] for r in controls)
group = {
    "unaffected": [r for r in rows if r["case"] == 0],
    "MMUT_category_0": [r for r in rows if r["mut_category"] == 0],
    "MMUT_category_1": [r for r in rows if r["mut_category"] == 1],
    "all_other_MMA": [r for r in rows if r["case"] == 1 and r["mut_category"] == "NA"],
}
for sample in ("MMA206", "MMA209"):
    group[sample] = [r for r in rows if r[None] == sample]
writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
writer.writerow(("group", "total", "paired", "median_baseline", "median_treated", "median_paired_gain",
                 "median_fold", "median_treated_pct_of_unaffected_treated_median", "positive_gains"))
for label, members in group.items():
    pairs = [(r["OHCblMinus"], r["OHCblPlus"]) for r in members if paired(r)]
    a, b = zip(*pairs)
    gains = [y-x for x,y in pairs]
    writer.writerow((label, len(members), len(pairs),median(a),median(b),median(gains),
                     round(median(y/x for x,y in pairs),3),round(100*median(b)/control_treated,1),
                     sum(g>0 for g in gains)))
