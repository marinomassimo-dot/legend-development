"""Replay edaravone exposure, primary study contrasts and held WWOX RNA."""

import csv
from pathlib import Path

PARENT_MASS = 174.20
ESTIMATED_FREE_FRACTION = 0.08
ROOT = Path(__file__).resolve().parent


def centred_recovery(reference, injured, treated):
    """Fraction of the injury contrast reversed, using published group values."""
    return (treated - injured) / (reference - injured)


def main():
    plot_crossing = 10 ** (1 + (637 - 632) / (669.5 - 632))
    rows = [("iNIL_fig5d_nominal_50pct", "uM", plot_crossing)]
    # FDA Clinical Pharmacology Review, Table 9. Total plasma, arithmetic means.
    for group, total_ng_ml in (("J03", 1656), ("J04", 1903), ("J05", 2163)):
        total = total_ng_ml / PARENT_MASS
        free = total * ESTIMATED_FREE_FRACTION
        rows.extend([
            (f"{group}_total_parent_mean_peak", "uM", total),
            (f"{group}_estimated_free_parent_mean_peak", "uM", free),
            (f"iNIL_fig5d_over_{group}_estimated_free_peak", "ratio", plot_crossing / free),
        ])

    # Song Results, Fig. 4D (well means), and Li Results, Fig. 5B and 5F (rounded losses).
    rows.extend([
        ("pc12_apoptosis_treatment_minus_injury", "percentage_points", 20 - 46),
        ("pc12_share_of_excess_apoptosis_reversed", "ratio", centred_recovery(1.5, 46, 20)),
        ("human_motor_neurite_peroxide_share_of_loss_reversed", "ratio", centred_recovery(0, 93, 26)),
        ("human_motor_neurite_glutamate_share_of_loss_reversed", "ratio", centred_recovery(0, 57, 15)),
        ("pediatric_17_zero_events_one_sided_95pct_upper", "percent", 100 * (1 - 0.05 ** (1 / 17))),
    ])

    # Minnelli Fig. 2B–C, original 756 × 565 raster. Percent axis from two ticks.
    for panel, zero, hundred, parent, derivative in (
        ("aqueous", 258, 22, 65, 124),
        ("lipid", 536, 300, 475, 435),
    ):
        rows.extend([
            (f"liposome_{panel}_parent_tbars_inhibition", "percent", 100 * (zero - parent) / (zero - hundred)),
            (f"liposome_{panel}_C18_tbars_inhibition", "percent", 100 * (zero - derivative) / (zero - hundred)),
        ])

    held_nuclei = ROOT.parent / "sodium_selenite" / "cell_types.tsv"
    with held_nuclei.open(newline="") as source:
        pool_cpm = {
            (record["pool"], record["class"], record["gene"]): float(record["CPM"])
            for record in csv.DictReader(source, delimiter="\t")
        }
    for cell_class in ("exc", "inh", "OPC", "NFOL"):
        for gene in ("Gpx4", "Acsl4"):
            control = pool_cpm["ctrl", cell_class, gene]
            knockout = pool_cpm["ko", cell_class, gene]
            rows.extend([
                (f"P17_hippocampus_{cell_class}_{gene}_control", "UMI_CPM", control),
                (f"P17_hippocampus_{cell_class}_{gene}_knockout", "UMI_CPM", knockout),
            ])

    print("comparison\tunit\tvalue")
    for name, unit, value in rows:
        print(f"{name}\t{unit}\t{value:.4f}")


if __name__ == "__main__":
    main()
