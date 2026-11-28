"""Replay analytical exposure conversions and pooled nuclear sensitivity comparisons."""

import csv
from math import isclose
from pathlib import Path


HERE = Path(__file__).resolve().parent


def print_exposure():
    molecular_mass = 444.65  # MK-4, g/mol
    print("endpoint\tstratum\tvalue\tunit")
    for stratum, concentration in (
        ("Sato single-dose serum detection limit", 0.016),
        ("Glakay adult fed mean peak", 253.2),
        ("Glakay paired adult fasted mean peak", 32.3),
        ("Glakay paired adult fed mean peak", 354.0),
        ("Kaytwo adult syrup mean peak", 325.0),
    ):
        print(f"analytical_concentration\t{stratum}\t{1000 * concentration / molecular_mass:.3f}\tnmol/L")
    print(f"fed_to_fasted_mean_Cmax\tGlakay n=3\t{354.0 / 32.3:.3f}\tratio")
    print(f"fed_to_fasted_mean_AUC\tGlakay n=3\t{1114.50 / 165.00:.3f}\tratio")


def print_nuclear_comparisons():
    with (HERE / "nuclei.tsv").open() as source:
        counts = {
            (r["pool"], r["cell_class"], r["gene"]): (int(r["all_UMI"]), int(r["gene_UMI"]))
            for r in csv.DictReader(source, delimiter="\t")
        }
    groups = sorted({cell_class for _, cell_class, _ in counts})
    for gene in ("AIFM2", "UBIAD1", "GGCX", "GAS6", "TYRO3", "AXL"):
        ctrl_depths, ctrl_counts = zip(*(counts["ctrl", group, gene] for group in groups))
        ko_depths, ko_counts = zip(*(counts["ko", group, gene] for group in groups))
        ctrl_total_depth, ko_total_depth = sum(ctrl_depths), sum(ko_depths)
        ctrl_cpm = 1e6 * sum(ctrl_counts) / ctrl_total_depth
        ko_cpm = 1e6 * sum(ko_counts) / ko_total_depth
        within_class = class_weight = 0
        for dc, cc, dk, ck in zip(ctrl_depths, ctrl_counts, ko_depths, ko_counts):
            ctrl_rate, ko_rate = 1e6 * cc / dc, 1e6 * ck / dk
            ctrl_weight, ko_weight = dc / ctrl_total_depth, dk / ko_total_depth
            within_class += (ko_rate - ctrl_rate) * (ctrl_weight + ko_weight) / 2
            class_weight += (ko_weight - ctrl_weight) * (ctrl_rate + ko_rate) / 2
        assert isclose(ko_cpm - ctrl_cpm, within_class + class_weight, abs_tol=1e-9)
        for endpoint, value in (("pooled_ctrl", ctrl_cpm), ("pooled_ko", ko_cpm),
                                ("pooled_delta", ko_cpm - ctrl_cpm),
                                ("within_class_part", within_class), ("class_weight_part", class_weight)):
            print(f"{endpoint}\t{gene}\t{value:.4f}\tUMI CPM")


def print_gas6_comparison():
    wild_type_change = 87.52 - 57.29  # Akkermann et al., Fig. 4D Results means
    tyro3_null_change = 39.50 - 35.13
    print(f"gas6_change\tWT OPCs\t{wild_type_change:.2f}\tMBP+ segments per field")
    print(f"gas6_change\tTyro3-null OPCs\t{tyro3_null_change:.2f}\tMBP+ segments per field")
    print(f"gas6_difference_of_changes\tWT minus Tyro3 null\t{wild_type_change - tyro3_null_change:.2f}\tMBP+ segments per field")


if __name__ == "__main__":
    print_exposure()
    print_nuclear_comparisons()
    print_gas6_comparison()
