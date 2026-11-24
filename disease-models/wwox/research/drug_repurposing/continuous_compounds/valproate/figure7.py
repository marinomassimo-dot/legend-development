"""Reproduce the linear calibration of visually read coordinates in the 640x432 PMC figure."""
import csv
import sys
writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
writer.writerow(("panel", "endpoint", "axis_zero_y", "upper_tick_y", "upper_tick_value",
                 "PBS_bar_y", "VPA_bar_y", "PBS_estimate", "VPA_estimate", "difference"))
for panel, endpoint, zero, top, value, pbs, vpa in [
    ("E", "CC1_percent_all_DAPI", 135, 17, 35, 36, 71),
    ("H", "NG2_percent_all_DAPI", 283, 157, 80, 242, 180),
    ("M", "NG2_BrdU_double_positive_per_area", 420, 329, 16, 350, 356),
]:
    a = (zero-pbs)*value/(zero-top)
    b = (zero-vpa)*value/(zero-top)
    writer.writerow((panel, endpoint, zero, top, value, pbs, vpa,
                     f"{a:.2f}", f"{b:.2f}", f"{b-a:.2f}"))
