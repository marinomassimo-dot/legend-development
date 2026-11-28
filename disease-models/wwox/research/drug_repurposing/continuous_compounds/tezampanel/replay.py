"""Reproduce recombinant selectivity and rat whole-brain exposure sensitivity."""
import csv
import sys

from decimal import Decimal as D


def main():
    # Alt et al. (2006), Table 1. Kainate rows reuse Alt et al. (2004).
    ampa = {"GluA2-flip": (D("20.9"), D("0.6")), "GluA2-flop": (D("15.0"), D("0.8"))}
    kainate = {
        "GluK1": (D("0.7"), D("0.2")),
        "GluK1/GluK2": (D("1.0"), D("0.5")),
        "GluK1/GluK5": (D("3.2"), D("0.7")),
    }
    target_block, max_ampa_block = D("0.8"), D("0.2")
    target_odds = target_block / (1 - target_block)
    min_ratio = target_odds * (1 - max_ampa_block) / max_ampa_block
    rows = [("minimum Hill-1 potency ratio", f"{min_ratio:.1f}", "ratio",
             "Illustrative criterion 80% kainate and at most 20% AMPA inhibition")]

    for ampa_name, ampa_values in ampa.items():
        for kainate_name, kainate_values in kainate.items():
            for scale, ampa_value, kainate_value in zip(
                ("fixed glutamate IC50", "equal fractional challenge using apparent Kb"),
                ampa_values, kainate_values, strict=True,
            ):
                ratio = ampa_value / kainate_value
                scaled_antagonist = target_odds * kainate_value
                ampa_block = scaled_antagonist / (scaled_antagonist + ampa_value)
                label = f"{ampa_name} vs {kainate_name} ({scale})"
                rows.append((label + " potency ratio", f"{ratio:.2f}", "ratio", "Alt 2006 Table 1"))
                rows.append((label + " AMPA inhibition", f"{ampa_block * 100:.2f}", "%",
                             "Hill-1 scenario at 80% kainate inhibition"))

    # Apland et al. (2013), Table 2 and the discussion's residual plasma example.
    mass_g_per_mol = D("279.34")
    assumed_plasma_ml_per_g = D("0.0103")
    for time, brain_ng_per_g, plasma_ng_per_ml in (
        ("0.25 h", D("318.7"), D("18435.0")),
        ("0.5 h", D("125.3"), D("8453.3")),
        ("1 h", D("119.8"), D("1758.3")),
        ("1.5 h", D("36.5"), D("609.7")),
    ):
        vascular_ng_per_g = plasma_ng_per_ml * assumed_plasma_ml_per_g
        corrected_ng_per_g = brain_ng_per_g - vascular_ng_per_g
        corrected_umol_per_kg = corrected_ng_per_g / mass_g_per_mol
        rows.extend((
            (f"{time} whole-brain parent", f"{brain_ng_per_g / mass_g_per_mol:.3f}", "µmol/kg",
             "Raw homogenate mean; Apland Table 2"),
            (f"{time} illustrative vascular-subtracted parent", f"{corrected_umol_per_kg:.3f}", "µmol/kg",
             "Apland Table 2 and assumed 10.3 µL residual plasma/g tissue"),
            (f"{time} fraction of subtracted total needed to reach 0.2 µM",
             f"{100 * D('0.2') / corrected_umol_per_kg:.1f}", "%",
             "1 kg/L tissue scenario; not a measured free fraction or native potency"),
        ))

    writer = csv.writer(sys.stdout, dialect="excel-tab", lineterminator="\n")
    writer.writerow(("contrast", "value", "unit", "source_or_assumption"))
    writer.writerows(rows)


if __name__ == "__main__":
    main()
