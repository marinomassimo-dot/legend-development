"""Replay approximate oral concentrations, vascular sensitivity and lineage contrasts."""

import argparse
from csv import writer
from hashlib import sha256
from pathlib import Path
import sys


ORAL_FIGURE_SHA256 = "c51f1df0d55316a6bebbb277dcabebbe58961d8efa198a17459f108ddf083eaa"
MOLAR_MASS = 328.4
# Hartley 2020 Fig. 2C and 2D, zero-based raster rows.
SERUM = {"zero": 358.0, "high": 85.5, "scale": 20.0, "sobetirome": 178.0, "Sob-AM2": 279.5}
BRAIN = {"zero": 356.5, "high": 83.5, "scale": 0.4, "sobetirome": 176.0, "Sob-AM2": 183.5}
# Baxi 2014 descriptions adjacent to Figs. 5 and 7–9, not pooled cell counts.
DEVELOPMENT = (
    ("P14 mouse callosal splenium", "Fig. 7E", 39, 54),
    ("P14 mouse occipital cortex", "Fig. 8B", 23, 35),
    ("P14 mouse optic nerve", "Fig. 9B", 40, 57),
    ("Human derived CNP-positive cells after PDGF withdrawal", "Fig. 5", 19, 35),
)


def ordinate(panel, row):
    return (panel["zero"] - row) * panel["scale"] / (panel["zero"] - panel["high"])


def exposure_rows():
    for treatment in ("sobetirome", "Sob-AM2"):
        serum = ordinate(SERUM, SERUM[treatment])
        brain = ordinate(BRAIN, BRAIN[treatment])
        yield treatment, "Hartley 2020 Fig. 2C", "total serum parent", "", serum, "ng/mL"
        yield treatment, "Hartley 2020 Fig. 2D", "total whole-brain parent", "", brain, "ng/g"
        yield treatment, "Hartley 2020 Fig. 2C/D", "vascular volume making residual zero", "", 1000 * brain / serum, "µL/g"
        for volume in (0.0, 5.0, 7.99, 10.3, 15.0, 20.0):
            residual = brain - volume * serum / 1000
            yield treatment, "Hartley 2020 Fig. 2C/D", "residual under assumed effective vascular volume", volume, residual, "ng/g"
            yield treatment, "Hartley 2020 Fig. 2C/D", "homogeneous total equivalent at 1 g/mL", volume, 1000 * residual / MOLAR_MASS, "nM equivalent"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("hartley_figure", type=Path)
    args = parser.parse_args()
    if sha256(args.hartley_figure.read_bytes()).hexdigest() != ORAL_FIGURE_SHA256:
        raise ValueError("Provide the original 1800 × 615 PMC Fig. 2 image.")
    rows = writer(sys.stdout, delimiter="\t", lineterminator="\n")
    rows.writerow(("comparison", "locator", "measurement", "assumed_vascular_space_µL_per_g", "value", "unit"))
    for arm, locator, measure, volume, value, unit in exposure_rows():
        rows.writerow((arm, locator, measure, volume, f"{value:.4f}", unit))
    for comparison, locator, control, treatment in DEVELOPMENT:
        rows.writerow((comparison, f"Baxi 2014 {locator}", "treated minus control reported cell fraction", "",
                       treatment - control, "percentage points"))
    rows.writerow(("HEK293 THRA / THRB", "Ferrara Table 1", "ratio of reported transactivation EC50",
                   "", f"{74.7 / 2.8:.3f}", "fold"))
    rows.writerow(("Perfused P30-start Mct8/Dio2 KO IP parent", "Hartley 2018 Fig. 1",
                   "total hemi-brain parent expressed as homogeneous equivalent at 1 g/mL",
                   "", f"{1000 * 20 / MOLAR_MASS:.3f}", "nM equivalent"))


if __name__ == "__main__":
    main()
