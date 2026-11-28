"""Replay human plasma scales, matched-control contrasts and held NAGK counts."""

from collections import defaultdict
import csv
from itertools import product
from pathlib import Path
import sys


def main():
    writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    writer.writerow(("comparison", "scope", "unit", "value"))

    def emit(comparison, scope, unit, value):
        writer.writerow((comparison, scope, unit, f"{value:.6f}"))

    # Meola et al., Table 1. Xu et al., ManNAc plasma pharmacokinetics Results.
    molecular_mass = 221.21
    for study, peak in (
        ("healthy_oral", 674),
        ("healthy_iv", 5320),
        ("gne_phase1_lowest_exposure_arm", 1502),
        ("gne_phase1_middle_exposure_arm", 1407),
        ("gne_phase1_highest_exposure_arm", 2638),
    ):
        parent_um = peak / molecular_mass
        emit("plasma_parent_peak", study, "umol/L", parent_um)
        emit("nominal_5mM_over_plasma_peak", study, "ratio", 5000 / parent_um)
    emit("ratio_of_group_mean_auc_dose_normalized", "healthy_oral_vs_iv", "percent",
         100 * (3840 / 10200) * (100 / 1000))
    emit("ratio_of_endpoint_group_peak_geometric_means", "gne_phase1", "ratio", 2638 / 1502)

    # Sabir et al., Results referring to Fig. 1D–E. WT vehicle is normalized to 1.
    for time, knockout_vehicle, knockout_treated, wildtype_treated in (
        ("20h", 0.70, 0.80, 1.13),
        ("24h", 0.79, 0.91, 1.14),
    ):
        knockout_change = knockout_treated - knockout_vehicle
        matched_change = knockout_treated / wildtype_treated - knockout_vehicle
        emit("apparent_gap_closed_vs_wildtype_vehicle", time, "percent",
             100 * knockout_change / (1 - knockout_vehicle))
        emit("treated_deficient_over_treated_wildtype", time, "ratio", knockout_treated / wildtype_treated)
        emit("change_in_matched_deficient_to_wildtype_ratio", time, "ratio", matched_change)
        emit("absolute_treatment_by_genotype_contrast", time, "normalized_ratio_units",
             knockout_change - (wildtype_treated - 1))
        rounding_range = [
            (knockout_treated + dt) / (wildtype_treated + dw) - (knockout_vehicle + db)
            for dt, dw, db in product((-0.005, 0.005), repeat=3)
        ]
        emit("rounded_matched_ratio_change_min", time, "ratio", min(rounding_range))
        emit("rounded_matched_ratio_change_max", time, "ratio", max(rounding_range))

    source = Path(__file__).resolve().parents[1] / "n_acetylglucosamine" / "nuclei.tsv"
    by_pool = defaultdict(dict)
    with source.open(newline="") as file:
        for row in csv.DictReader(file, delimiter="\t"):
            if row["gene"] == "NAGK":
                by_pool[row["pool"]][row["cell_class"]] = (int(row["gene_UMI"]), int(row["all_UMI"]))
    assert by_pool["ctrl"].keys() == by_pool["ko"].keys()
    for excluded in (None, *sorted(by_pool["ctrl"])):
        pooled_cpm = {}
        for pool, classes in by_pool.items():
            counts = [counts for cell, counts in classes.items() if cell != excluded]
            gene, total = map(sum, zip(*counts))
            pooled_cpm[pool] = 1_000_000 * gene / total
            if excluded is None:
                emit("nagk_pooled_gene_umi", pool, "count", gene)
                emit("nagk_pooled_cpm", pool, "CPM", pooled_cpm[pool])
        emit("nagk_pooled_ko_minus_control", excluded or "all_classes", "CPM",
             pooled_cpm["ko"] - pooled_cpm["ctrl"])


if __name__ == "__main__":
    main()
