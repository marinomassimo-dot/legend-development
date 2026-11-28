"""Replay exposure ratios and within-study mouse contrasts from published summary data."""

import csv
from pathlib import Path
import sys

MOLECULAR_WEIGHT_G_MOL = 174.20


def main():
    with Path(__file__).with_name("external_inputs.tsv").open(newline="") as stream:
        inputs = {row["id"]: row for row in csv.DictReader(stream, delimiter="\t")}

    def value(name, unit, field="value"):
        row = inputs[name]
        if row["unit"] != unit:
            raise ValueError(f"Unexpected unit for {name}: {row['unit']}")
        return float(row[field])

    granule = "adult_granule_peak"
    peaks = {
        "capsule": value("adult_capsule_peak", "umol/L"),
        "tea": value("adult_tea_peak", "umol/L"),
        "granule": value(granule, "ug/mL") * 1000 / MOLECULAR_WEIGHT_G_MOL,
    }
    results = [
        ("adult_granule_peak", peaks["granule"], "umol/L"),
        ("adult_granule_peak_sd", value(granule, "ug/mL", "dispersion") * 1000 / MOLECULAR_WEIGHT_G_MOL, "umol/L"),
        ("adult_granule_120_after_glucose", value("adult_granule_120", "ug/mL") * 1000 / MOLECULAR_WEIGHT_G_MOL, "umol/L"),
    ]
    targets = {
        "rat_synaptosome_IC50": value("rat_glutamine_ic50", "umol/L"),
        "P19_four_day_nominal": value("p19_prolonged", "umol/L"),
    }
    for endpoint, concentration in targets.items():
        for formulation, peak in peaks.items():
            results.append((f"{endpoint}_over_{formulation}_peak", concentration / peak, "ratio"))
    for endpoint, unit in (
        ("pilocarpine_twitch", "mg/kg"),
        ("ptz_tonus", "mg/kg"),
        ("cortical_gaba", "umol/L"),
        ("hippocampal_gaba", "umol/L"),
    ):
        vehicle = value(f"{endpoint}_water", unit)
        treated = value(f"{endpoint}_theanine", unit)
        results.append((f"{endpoint}_relative_difference", 100 * (treated / vehicle - 1), "%"))

    writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    writer.writerow(["comparison", "value", "unit"])
    writer.writerows((name, f"{number:.3f}", unit) for name, number, unit in results)


if __name__ == "__main__":
    main()
