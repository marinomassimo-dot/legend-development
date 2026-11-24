"""Invert the published pediatric binding model at illustrative total concentrations."""
from math import sqrt, isclose
import csv
import sys
kd, capacity = 7.8, 130.0
writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
writer.writerow(("illustrative_total_ug_ml","model_free_ug_ml","model_free_percent"))
for total in (50.,75.,100.):
    b = kd + capacity - total
    free = 2*kd*total / (b+sqrt(b*b + 4*kd*total))
    assert isclose(total, free+capacity*free/(kd+free))
    writer.writerow((total, f"{free:.3f}", f"{100*free/total:.2f}"))
