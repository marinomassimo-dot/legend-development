"""Replay descriptive bar digitization and the preclinical exposure comparisons."""

import csv
from pathlib import Path


def estimate(row, group):
    low = float(row["low_tick"])
    high = float(row["high_tick"])
    low_y = int(row["low_y"])
    high_y = int(row["high_y"])
    pixel_y = int(row[f"{group}_y"])
    return low + (low_y - pixel_y) * (high - low) / (low_y - high_y)


def main():
    with Path(__file__).with_name("pk_lineage_pixels.tsv").open() as source:
        rows = list(csv.DictReader(source, delimiter="\t"))

    by_endpoint = {}
    print("study\tpanel\tendpoint\ttime\tunit\tcontrol\tintermediate\ttreated")
    for row in rows:
        values = [estimate(row, group) for group in ("control", "intermediate", "treated")]
        by_endpoint[row["endpoint"], int(row["time"])] = values
        values_text = [f"{value:.3f}" for value in values]
        print("\t".join([row[key] for key in ("study", "panel", "endpoint", "time", "unit")] + values_text))

    control_day8, _, treated_day8 = by_endpoint["whole_blood_change", 8]
    day8_blood_difference = treated_day8 - control_day8
    peak_sampled_plasma = max(values[2] for (endpoint, _), values in by_endpoint.items() if endpoint == "plasma")
    print(f"day8_whole_blood_contrast_µM\t{day8_blood_difference:.2f}")
    print(f"day8_whole_blood_text_to_plot_ratio\t{125 / day8_blood_difference:.2f}")
    print(f"5µM_progenitor_bath_to_peak_sampled_adult_plasma\t{5 / peak_sampled_plasma:.2f}")
    print(f"500µM_progenitor_bath_to_peak_sampled_adult_plasma\t{500 / peak_sampled_plasma:.2f}")
    print(f"CSF_clearance_WT_to_KO_tracer\t{3.62 / 1.42:.2f}")
    print(f"CSF_clearance_WT_to_KO_mannitol\t{1.59 / 1.25:.2f}")
    print(f"CSF_clearance_descriptive_interaction_µL/min\t{(3.62 - 1.59) - (1.42 - 1.25):.2f}")


if __name__ == "__main__":
    main()
