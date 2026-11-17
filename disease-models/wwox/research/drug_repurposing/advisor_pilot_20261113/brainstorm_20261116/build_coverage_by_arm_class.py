"""Coverage by arm class: joins the v8 arm table (cell_id, arm) with the row-level best-tier table.
A count of cells, not of evidence. Writes COVERAGE_BY_ARM_CLASS_V8_IT_20261117.tsv beside this script."""
import csv, collections
from pathlib import Path
H = Path(__file__).resolve().parent
v8 = list(csv.DictReader(open(H / "ideas_arm_table_v8_20261117.tsv"), delimiter="\t"))
rl = {r["cell_id"]: r for r in csv.DictReader(open(H / "ROW_LEVEL_TIER_V8_IT_20261117.tsv"), delimiter="\t")}
t = collections.defaultdict(lambda: [0, 0, 0, 0])
for r in v8:
    x = t[r["arm"]]; x[0] += 1
    b = rl.get(r["cell_id"])
    if b:
        x[1] += 1
        if b["best_tier_row_level"] in ("1", "2"): x[2] += 1
        elif b["best_tier_row_level"] == "3": x[3] += 1
rows = sorted(t.items(), key=lambda z: (-z[1][0], z[0]))
with open(H / "COVERAGE_BY_ARM_CLASS_V8_IT_20261117.tsv", "w", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n")
    w.writerow(["arm_class", "cells", "cells_with_origin_row", "best_tier_1_or_2", "tier_3_only"])
    for a, x in rows: w.writerow([a] + x)
    w.writerow(["TOTAL (denominator: 75 cells of arm table v8; a count of cells, not of evidence)"] + [sum(x[i] for _, x in rows) for i in range(4)])
print(len(rows), "classes;", sum(1 for _, x in rows if x[1] == 0), "with no origin row")
