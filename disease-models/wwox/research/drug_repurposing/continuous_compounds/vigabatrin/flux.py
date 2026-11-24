"""Recalculate the pool-to-synthesis scales from the published rat group estimates."""
import csv
import sys

writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
writer.writerow(("PMID", "condition", "measure", "unit", "control", "vigabatrin", "treated_over_control"))
for pmid, condition, measure, unit, control, treated in (
    (8897466, "24h", "GABA", "umol/g", 1.3, 2.7),
    (8897466, "24h", "model_synthesis", "umol/g/min", 0.14, 0.04),
    (8897466, "24h", "pool_over_synthesis", "min", 1.3/0.14, 2.7/0.04),
    (8897466, "24h", "TCA", "umol/g/min", 0.52, 0.47),
    (16517019, "5-6h", "glucose_tracer_synthesis", "umol/g/min", 0.031, 0.037),
    (16517019, "5-6h", "acetate_tracer_synthesis", "umol/g/min", 0.078, 0.084),
):
    writer.writerow((pmid, condition, measure, unit, f"{control:.5g}", f"{treated:.5g}", f"{treated/control:.5g}"))
