"""Reconstruct published summary contrasts and an explicit ion-binding sensitivity."""
import argparse
import csv
from math import sqrt
from pathlib import Path


def wilson(successes, count):
    proportion = successes / count
    z = 1.959963984540054
    denominator = 1 + z**2 / count
    center = (proportion + z**2 / (2 * count)) / denominator
    half_width = z * sqrt(proportion * (1 - proportion) / count + z**2 / (4 * count**2)) / denominator
    return center - half_width, center + half_width


def main(inputs, output):
    with inputs.open() as handle:
        rows = {row["key"]: row for row in csv.DictReader(handle, delimiter="\t")}
    values = {name: float(row["value"]) for name, row in rows.items()}

    stop = values["juvenile_stop"]
    count = int(rows["juvenile_stop"]["n"])
    low, high = wilson(stop, count)
    retained = values["hva_fbp"] / values["hva_baseline"]
    blood_uM = 1000 * values["adult_oral_blood"] / values["free_acid_mass"]
    brain_difference = (values["adult_oral_brain"] - values["adult_naive_brain"])
    pixel_span = values["mef_axis_bottom"] - values["mef_axis_top"]

    results = [
        ("slice_burst_responder_fraction", values["slice_burst_responders"] / int(rows["slice_burst_responders"]["n"]), "fraction"),
        ("2DG_to_FBP_time_different_studies", values["older_2dg_time"] / values["slice_time"], "ratio"),
        ("juvenile_status_stopped", stop / count, "fraction"),
        ("juvenile_status_stopped_wilson_lower", low, "fraction"),
        ("juvenile_status_stopped_wilson_upper", high, "fraction"),
        ("HVA_reduction_from_means", 100 * (1 - retained), "percent"),
        ("GABA_reduction_from_means", 100 * (1 - values["gaba_fbp"] / values["gaba_baseline"]), "percent"),
        ("oral_adult_rat_total_whole_blood_acid_equivalent", blood_uM, "µM"),
        ("bath_low_vs_adult_total_whole_blood", 1000 * values["slice_bath_low"] / blood_uM, "ratio"),
        ("bath_high_vs_adult_total_whole_blood", 1000 * values["slice_bath_high"] / blood_uM, "ratio"),
        ("oral_adult_rat_brain_difference", brain_difference, "mg/g"),
        ("oral_adult_rat_brain_difference_acid_equivalent", 1000 * brain_difference / values["free_acid_mass"], "µmol/g"),
        ("fibroblast_wt_median_approx", 3.5 * (values["mef_axis_bottom"] - values["mef_wt_median"]) / pixel_span, "plotted fold units"),
        ("fibroblast_ko_median_approx", 3.5 * (values["mef_axis_bottom"] - values["mef_ko_median"]) / pixel_span, "plotted fold units"),
        ("fibroblast_ko_wt_median_ratio", (values["mef_axis_bottom"] - values["mef_ko_median"]) / (values["mef_axis_bottom"] - values["mef_wt_median"]), "ratio"),
        ("fibroblast_ko_wt_median_ratio_with_2px_lower", (values["mef_axis_bottom"] - values["mef_ko_median"] - 2) / (values["mef_axis_bottom"] - values["mef_wt_median"] + 2), "ratio"),
        ("fibroblast_ko_wt_median_ratio_with_2px_upper", (values["mef_axis_bottom"] - values["mef_ko_median"] + 2) / (values["mef_axis_bottom"] - values["mef_wt_median"] - 2), "ratio"),
    ]
    total_ca = values["hva_calcium"]
    total_fbp = values["slice_bath_high"]
    for exponent in (0.5, 1, 2):
        # Invert the assumed current/free-calcium relation, then 1:1 mass action.
        free_ca = total_ca * retained ** (1 / exponent)
        bound = total_ca - free_ca
        apparent_kd = free_ca * (total_fbp - bound) / bound
        results.append((f"free_calcium_if_current_exponent_{exponent}", free_ca, "mM scenario"))
        results.append((f"apparent_Kd_if_current_exponent_{exponent}", apparent_kd, "mM scenario"))

    with output.open("w") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(["comparison", "value", "units"])
        writer.writerows((name, f"{value:.7g}", units) for name, value, units in results)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("inputs", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    main(args.inputs, args.output)
