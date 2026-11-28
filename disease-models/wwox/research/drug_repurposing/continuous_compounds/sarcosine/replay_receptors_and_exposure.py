"""Replay sarcosine assay scales, adult plasma figure envelope and WWOX bulk data."""

import argparse
from pathlib import Path
import sys

COMPOUNDS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(COMPOUNDS / "sodium_benzoate"))
sys.path.insert(0, str(COMPOUNDS / "jbpos0101"))
from coagonist_screen import bulk_panel, tsv
from replay_exposure_and_receptors import verified_expression

PANEL = ("Slc6a9", "Slc6a5", "Sardh", "Dmgdh", "Gnmt", "Gldc", "Amt", "Glra2", "Glrb", "Slc12a5")
# Midpoint (micromolar), SEM and measured or scenario Hill slopes for three distinct assays.
ASSAYS = (
    ("mouse_culture_NMDAR_peak_coagonism", 26, 3, (1.8,)),
    ("human_GlyT1_glycine_uptake_inhibition", 96.81, 13.67, (0.75, 1.0, 1.5)),
    ("mouse_culture_GlyR_peak_current", 3200, 700, (1.5,)),
)
CONCENTRATIONS = (7, 20, 26, 96.81, 100, 500, 3200)


def response(concentration, midpoint, slope):
    return 100 / (1 + (midpoint / concentration) ** slope)


def assay_rows():
    for name, midpoint, sem, slopes in ASSAYS:
        for concentration in CONCENTRATIONS:
            for slope in slopes:
                yield (name, concentration, midpoint, sem, slope,
                       response(concentration, midpoint, slope),
                       response(concentration, midpoint + sem, slope),
                       response(concentration, midpoint - sem, slope))


def plasma_rows():
    # Glorieux Fig. 2, p. 2315, full page raster from Poppler at longest edge 1550 px.
    # Log axis tick centers and one-hour adult group envelope only. The raw graph is not exported.
    y_one, y_point_two = 784, 908
    for label, center in (("lower_group_envelope", 872), ("upper_group_envelope", 762)):
        for delta in (-3, 0, 3):
            position = center + delta
            value = 1000 * 0.2 ** ((position - y_one) / (y_point_two - y_one))
            yield (4, 1, label, delta, position, value)


def rodent_outcome_rows():
    for exposure, point, lower, upper in ((0, 9.92, 9.19, 10.71), (100, 11.05, 10.33, 11.82),
                                           (200, 11.02, 10.39, 11.68), (400, 11.93, 11.50, 12.38),
                                           (800, 11.93, 11.15, 12.77)):
        yield ("Socala_MEST", exposure, "CC50_mA", point, lower, upper, "", "",
               point / 9.92)
    for exposure, point, sem, n in ((0, 17.29, 0.17, 15), (200, 23.07, 0.42, 5), (800, 28.90, 2.30, 5)):
        yield ("Fone_PFC", exposure, "glycine_AUC_pct_min_per_1000", point, "", "", sem, n,
               point / 17.29)


def main(files, out):
    out.mkdir(parents=True, exist_ok=True)
    for name, header, rows in (
        ("assay_scales.tsv", "assay scenario_uM midpoint_uM midpoint_SEM_uM slope response_pct response_at_midpoint_plus_SEM_pct response_at_midpoint_minus_SEM_pct", assay_rows()),
        ("adult_plasma_figure.tsv", "n hour boundary shift_px y_px nominal_plasma_uM", plasma_rows()),
        ("rodent_outcomes.tsv", "source study_exposure_mg_kg_ip endpoint point lower_95CL upper_95CL SEM n ratio_to_vehicle", rodent_outcome_rows()),
    ):
        tsv(out / name, header.split(), ([f"{v:.6g}" if isinstance(v, float) else v for v in row] for row in rows))
    verified_expression(files)
    tsv(out / "wwox_bulk_sarcosine.tsv",
        "model accession gene ctrl_n ko_n ctrl_positive ko_positive ctrl_mean ko_mean log2_delta omit_min omit_max mapping".split(),
        bulk_panel(files, PANEL))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", type=Path)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    main(args.files, args.out)
