"""Recompute descriptive contrasts and explicit, non-fitted counterexamples."""

import argparse
import csv
from pathlib import Path


def write_table(out, columns, rows):
    with out.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
        writer.writerow(columns)
        writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path)
    out = parser.parse_args().output
    out.mkdir(parents=True, exist_ok=True)

    with Path(__file__).with_name("inputs.tsv").open(encoding="utf-8", newline="") as stream:
        data = list(csv.DictReader(stream, delimiter="\t"))
    write_table(
        out / "acute_replay.tsv",
        ("preparation", "site", "spikes_suppressed_pct", "duration_delta_ms",
         "period_delta_ms", "locator"),
        ((row["preparation"], row["site"], 100 - int(row["spikes_pct_control"]),
          row["duration_delta_ms"], int(row["period_clonazepam_ms"]) - int(row["period_control_ms"]),
          row["locator"]) for row in data),
    )

    # Two stylized patterns with the published WT whole-oscillation retention.
    # Control contributes 20 spikes to each fixed window. These are not estimates
    # of Fig. 4 values and carry no fitted biological parameters.
    temporal = (
        ("uniform suppression", (0.87, 0.87, 0.87, 0.87, 0.87)),
        ("predominantly late suppression", (0.98, 0.96, 0.91, 0.82, 0.68)),
    )
    write_table(
        out / "temporal_counterexample.tsv",
        ("scenario", "spikes_q1", "spikes_q2", "spikes_q3", "spikes_q4", "spikes_q5",
         "total_spikes_from_100", "first_two_retained_pct", "last_two_retained_pct"),
        ((name, *(f"{20 * fraction:.1f}" for fraction in fractions),
          f"{20 * sum(fractions):.1f}",
          f"{50 * sum(fractions[:2]):.1f}", f"{50 * sum(fractions[-2:]):.1f}")
         for name, fractions in temporal),
    )

    # A local charge proxy is the product of three normalized factors at fixed
    # duration. The factors illustrate identifiability; they are not fit to tissue.
    adaptation = (
        ("acute calibration", 1.0, 1.0, 1.0),
        ("lower local engagement", 0.5, 1.0, 1.0),
        ("lower conductance per engagement", 1.0, 0.5, 1.0),
        ("lower driving force during a train", 1.0, 1.0, 0.5),
    )
    write_table(
        out / "charge_counterexample.tsv",
        ("scenario", "local_engagement_relative", "conductance_per_engagement_relative",
         "effective_driving_force_relative", "added_charge_relative"),
        ((name, engagement, conductance, force, f"{engagement * conductance * force:.2f}")
         for name, engagement, conductance, force in adaptation),
    )

    # Reported total serum range at eight weeks. Applying adult label binding
    # is an explicitly illustrative scenario, not a measured pediatric fraction.
    molecular_mass = 315.71
    unbound_scenario = 0.15
    bath_nm = 100
    write_table(
        out / "exposure_replay.tsv",
        ("range_endpoint", "total_serum_ng_ml", "total_serum_nM",
         "illustrative_serum_unbound_fraction", "illustrative_serum_unbound_nM",
         "fraction_of_nominal_slice_bath"),
        ((name, ng_ml, f"{nM:.2f}", unbound_scenario, f"{nM * unbound_scenario:.2f}",
          f"{nM * unbound_scenario / bath_nm:.3f}")
         for name, ng_ml in (("low", 13), ("high", 72))
         for nM in (1000 * ng_ml / molecular_mass,)),
    )


if __name__ == "__main__":
    main()
