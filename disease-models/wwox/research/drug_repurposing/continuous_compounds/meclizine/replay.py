"""Reproduce the exposure arithmetic and the two-sink sensitivity analysis."""

import argparse
import csv
from pathlib import Path


def records(path):
    with path.open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream, delimiter="\t"))


def write_rows(path, header, rows):
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
        writer.writerow(header)
        writer.writerows(rows)


def exposure_table(folder, output):
    parent_mw = 390.95
    cell_bath_um = 25
    neuronal_bath_um = 5
    rows = []
    for source in records(folder / "exposure_inputs.tsv"):
        mean_um = float(source["mean_plasma_parent_ng_ml"]) / parent_mw
        low_um = float(source["lower_ci_ng_ml"]) / parent_mw
        high_um = float(source["upper_ci_ng_ml"]) / parent_mw
        rows.append((source["comparison"], f"{mean_um:.3f}", f"{low_um:.3f}",
                     f"{high_um:.3f}", f"{cell_bath_um / mean_um:.1f}",
                     f"{neuronal_bath_um / mean_um:.1f}", source["locator"]))
    write_rows(output / "exposure_replay.tsv",
               ("comparison", "total_plasma_mean_uM", "total_plasma_lower_ci_uM",
                "total_plasma_upper_ci_uM", "HEK_nominal_25uM_over_total_plasma_mean",
                "embryonic_neuron_nominal_5uM_over_total_plasma_mean", "locator"),
               rows)


def sink_table(folder, output):
    # Transcript ratios parameterize a hypothetical sensitivity analysis.
    # The input is fixed. The only sinks are the first-order PCYT2 and
    # ETNPPL branches. All outputs use untreated WT as a common reference.
    biological_rows = records(folder / "native_bulk.tsv")
    models = ("mouse_cortex", "mouse_hippocampus")
    rows = []
    for model in models:
        relevant = {row["gene"]: row for row in biological_rows if row["model"] == model}
        catalytic = relevant["PCYT2"]
        disposal = relevant["ETNPPL"]
        a = float(catalytic["ko_mean"]) / float(catalytic["wt_mean"])
        b = float(disposal["ko_mean"]) / float(disposal["wt_mean"])
        crossover = (1 - a) / (b - a)
        threshold = f"{crossover:.3f}" if 0 <= crossover <= 1 else "no crossover in [0,1]"
        for disposal_fraction in (0.05, 0.15, 0.40):
            total_sink = a * (1 - disposal_fraction) + b * disposal_fraction
            # A 50% loss of remaining catalytic capacity is an illustrative
            # perturbation. The model infers no meclizine concentration.
            inhibited_sink = 0.5 * a * (1 - disposal_fraction) + b * disposal_fraction
            rows.append((model, f"{a:.3f}", f"{b:.3f}", threshold, f"{disposal_fraction:.2f}",
                         f"{1 / total_sink:.3f}", f"{a / total_sink:.3f}",
                         f"{1 / inhibited_sink:.3f}", f"{0.5 * a / inhibited_sink:.3f}"))
    write_rows(output / "sink_sensitivity.tsv",
               ("model", "pcyt2_RNA_ratio_scenario", "etnppl_RNA_ratio_scenario", "baseline_disposal_crossover",
                "WT_disposal_fraction_assumed", "KO_PEtn_pool_relative", "KO_Kennedy_flux_relative",
                "KO_PEtn_with_half_remaining_PCYT2", "KO_Kennedy_flux_with_half_remaining_PCYT2"),
               rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    folder = Path(__file__).resolve().parent
    exposure_table(folder, args.output)
    sink_table(folder, args.output)


if __name__ == "__main__":
    main()
