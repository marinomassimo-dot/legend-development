"""Compare analytical load and oxidation error in juvenile BH4/BH2 scenarios."""

import argparse
import csv
from itertools import product
import sys


BH4_MOLAR_MASS = 241.25
KIM_HIPPOCAMPUS_PMOL_G = 21.5 * 1000 / BH4_MOLAR_MASS
ECD_LOQ_FMOL = (4490.0, 380.0)
# Arning and Bottiglieri use 30 uL diluted to 240 uL and inject 10 uL.
CSF_EQUIVALENT_UL = 30 * 10 / 240
CSF_LOWEST_CALIBRATOR_FMOL = 3 * CSF_EQUIVALENT_UL
REGIONAL_SAMPLE = (KIM_HIPPOCAMPUS_PMOL_G, KIM_HIPPOCAMPUS_PMOL_G / 10)


def image_read(value_low, value_high, y_low, y_high, data_y):
    return value_low + (value_high - value_low) * (y_low - data_y) / (y_low - y_high)


def figure_rows():
    yield ("figure", "panel", "group", "quantity", "y_low", "y_high", "data_y", "estimate", "unit")
    for source, panel, group, quantity, low, high, y_low, y_high, data_y, unit in (
        ("Herpfer", "1B", "P15_control", "MRI_volume", 8, 12, 779, 504, 688, "uL"),
        ("Hung", "4E", "NCAR", "brain_BH4", 0, 600, 1618, 1418, 1476, "pmol/g"),
        ("Hung", "4E", "R6/2", "brain_BH4", 0, 600, 1618, 1418, 1479, "pmol/g"),
        ("Hung", "4E", "NCAR", "brain_BH2", 0, 250, 1611, 1411, 1453, "pmol/g"),
        ("Hung", "4E", "R6/2", "brain_BH2", 0, 250, 1611, 1411, 1444, "pmol/g"),
    ):
        yield source, panel, group, quantity, y_low, y_high, data_y, f"{image_read(low, high, y_low, y_high, data_y):.3f}", unit


def exposure_rows():
    yield ("anchor", "wet_mg", "tissue_level_multiple", "recovery", "extra_dilution", "injection_ul",
           "undiluted_extract_ul", "total_bh4_fmol", "total_bh2_fmol", "injected_bh4_fmol", "injected_bh2_fmol",
           "bh4_vs_ecd_loq", "bh2_vs_ecd_loq", "bh4_vs_csf_lowest_calibrator", "bh2_vs_csf_lowest_calibrator")
    # The Hung values use the control-group bars from figure_rows. Kim's BH2 is a scenario.
    anchors = {"Kim_with_BH4_BH2_10": REGIONAL_SAMPLE, "Hung_NCAR_whole_brain": (426.0, 197.5)}
    for anchor, concentrations in anchors.items():
        for wet_mg, level, recovery, dilution, injection in product(
            (5, 10, 20, 30), (0.5, 1.0), (0.5, 1.0), (1, 5), (10, 20)
        ):
            # A nominal 1 mg/10 uL extraction, constrained by a 50 uL working minimum.
            extract = max(50, wet_mg * 10)
            fraction_injected = injection / (extract * dilution)
            total4, total2 = (c * wet_mg * level for c in concentrations)
            load4, load2 = (total * recovery * fraction_injected for total in (total4, total2))
            outcomes = (total4, total2, load4, load2, load4 / ECD_LOQ_FMOL[0], load2 / ECD_LOQ_FMOL[1],
                        load4 / CSF_LOWEST_CALIBRATOR_FMOL, load2 / CSF_LOWEST_CALIBRATOR_FMOL)
            yield (anchor, wet_mg, level, recovery, dilution, injection, extract, *(f"{x:.6f}" for x in outcomes))


def conversion_rows():
    yield ("true_bh4_to_bh2", "fraction_bh4_transferred", "observed_bh4_to_bh2", "apparent_ratio_loss_pct",
           "max_transfer_for_10pct_ratio_loss", "max_transfer_for_20pct_ratio_loss")
    for ratio, oxidation in product((2, 5, 10, 20), (0.0, 0.01, 0.02, 0.05)):
        observed = (1 - oxidation) * ratio / (1 + oxidation * ratio)
        yield ratio, oxidation, f"{observed:.6f}", f"{100 * (1 - observed / ratio):.6f}", \
            f"{0.10 / (1 + 0.90 * ratio):.6f}", f"{0.20 / (1 + 0.80 * ratio):.6f}"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("kind", choices=("figures", "load", "oxidation"))
    args = parser.parse_args()
    rows = {"figures": figure_rows, "load": exposure_rows, "oxidation": conversion_rows}[args.kind]()
    csv.writer(sys.stdout, delimiter="\t", lineterminator="\n").writerows(rows)


if __name__ == "__main__":
    main()
