"""Replay published MPS exposure arithmetic and a native Fig. 4a interpolation."""

import csv
import math
from pathlib import Path


def report(metric, lower, upper, unit, locator):
    print(f"{metric}\t{lower:.3f}\t{upper:.3f}\t{unit}\t{locator}")


def digitized_points():
    # Coulter p. 803, page 4 of the Stanford PDF, pdftoppm -r 175.
    # Use the local 100 and 1,000 µM ticks for the low-exposure interpolation.
    # y = 459 at zero, with 90 percentage points over 301 pixels.
    with Path(__file__).with_name("figure_points.tsv").open(newline="") as handle:
        return [(100 * 10 ** ((int(row["x_px"]) - 328) / 119),
                 (459 - int(row["y_px"])) * 90 / 301)
                for row in csv.DictReader(handle, delimiter="\t")]


def interpolate(points, exposure):
    for (left, bottom), (right, top) in zip(points, points[1:]):
        if left <= exposure <= right:
            weight = math.log(exposure / left) / math.log(right / left)
            return bottom + weight * (top - bottom)
    raise ValueError(f"Figure interpolation would extrapolate at {exposure:g} µM")


def main():
    molecular_weight = 189.21  # N-desmethylmethsuximide, PubChem 92154
    plasma_mg_l = 25.3, 44.7  # Sigler et al., fasting total in responders
    total = tuple(value * 1000 / molecular_weight for value in plasma_mg_l)
    free = total[0] * 0.40, total[1] * 0.55  # Wad et al., unrelated serum samples
    print("quantity\tlow\thigh\tunit\tlocator")
    report("MPS total plasma benchmark", *total, "µM", "Sigler abstract; PubChem 92154")
    report("MPS free plasma scenario", *free, "µM", "Sigler and Wad abstracts; crossed extrema")
    report("Coulter Fig. 4a nearby observed x range", *(point[0] for point in digitized_points()[1:3]),
           "µM", "about 54 and 134 µM; local horizontal calibration")
    for exposure in free:
        y = interpolate(digitized_points(), exposure)
        report(f"Native Fig. 4a readout at {exposure:.1f} µM", y - 1.5, y + 1.5,
               "% peak reduction", "Coulter Fig. 4a; reading tolerance only")
    fit = [100 * exposure / (1100 + exposure) for exposure in free]
    report("Native published by-eye fit", *fit, "% peak reduction", "Coulter Fig. 4a legend")
    for isoform, rested, conditioned in (
            ("CaV3.1", 2600, 1000), ("CaV3.2", 3100, 1400), ("CaV3.3", 1700, 800)):
        for state, midpoint in (("-110 mV", rested), ("-75 mV", conditioned)):
            margins = midpoint / free[1], midpoint / free[0]
            report(f"{isoform} {state} peak IC50 / free scenario", *margins, "fold", "Gomora Table 2")
    report("Within-cell command sensitivity at 250 µM", 7.4, 22.2, "% peak reduction",
           "Coulter p. 802, -30 vs -60 mV, same 5 cells")
    report("Pediatric short-term reduction ≥ 50%", 100 * 40 / 112, 100 * 40 / 112, "%",
           "Sigler abstract; uncontrolled cohort")
    report("Pediatric adverse event arithmetic", 100 * 41 / 112, 100 * 41 / 112, "%",
           "Sigler abstract; printed 28.9% disagrees")
    report("Younger cohort valproate mean change", 100 * (55.7 / 81.9 - 1),
           100 * (55.7 / 81.9 - 1), "%", "Besag et al. 2001; n=17")
    report("Younger cohort lamotrigine mean change", 100 * (6.3 / 13.4 - 1),
           100 * (6.3 / 13.4 - 1), "%", "Besag et al. 2000; n=16")


if __name__ == "__main__":
    main()
