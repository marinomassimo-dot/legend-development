"""One-substrate sensitivity at two published CSF concentrations treated as hypothetical local values."""
import csv
import math
import sys

before, after = 336.31, 433.66
peak = math.sqrt(before * after)
writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
writer.writerow(["system", "Km_uM", "baseline_fraction_Vmax", "after_fraction_Vmax",
                 "gain_pp_Vmax", "gain_pct_baseline", "required_remaining_capacity_fraction"])
for name, km in [("isolated_GlnT", 489), ("MNTB_cell_current", 940), ("analytical_max_gain", peak)]:
    baseline = before / (km + before)
    following = after / (km + after)
    writer.writerow([name, f"{km:.2f}", f"{baseline:.4f}", f"{following:.4f}",
                     f"{100 * (following - baseline):.2f}", f"{100 * (following/baseline - 1):.2f}",
                     f"{baseline / following:.4f}"])
bound = (math.sqrt(after) - math.sqrt(before)) / (math.sqrt(after) + math.sqrt(before))
assert math.isclose(after/(peak+after) - before/(peak+before), bound)
