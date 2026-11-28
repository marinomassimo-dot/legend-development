"""Reproduce group contrasts and a blood-to-brain identifiability counterexample."""

import csv
from math import exp
from pathlib import Path

HERE = Path(__file__).resolve().parent


def read_tsv(name):
    with (HERE / name).open(encoding="utf-8") as stream:
        return list(csv.DictReader(stream, delimiter="\t"))


def write_tsv(name, headers, rows):
    with (HERE / name).open("w", encoding="utf-8", newline="") as stream:
        writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
        writer.writerow(headers)
        writer.writerows(rows)


def glusignal(time, tau, blood_ratio, coupling, local_drive_reduction):
    """Return extracellular glutamate versus baseline after an assumed step."""
    fall = coupling * (1 - blood_ratio) + local_drive_reduction
    return 1 - fall * (1 - exp(-time / tau))


def main():
    studies = read_tsv("study_inputs.tsv")
    ratios = {
        row["comparison"]: float(row["exposed"]) / float(row["reference"])
        for row in studies
    }
    write_tsv(
        "study_contrasts.tsv",
        ("comparison", "exposed_over_reference", "percent_fall_over_reference", "difference_pct_points"),
        [
            (r["comparison"], f"{ratios[r['comparison']]:.5f}",
             f"{100 * (1 - ratios[r['comparison']]):.3f}",
             f"{float(r['exposed']) - float(r['reference']):.1f}")
            for r in studies
        ],
    )
    p = ratios["zhang_oaa"]
    equivalent_local_reduction = (0.20 - 0.05) * (1 - p)
    cases = (
        ("weak_sink_only", 0.05, 0),
        ("moderate_sink_only", 0.20, 0),
        ("strong_sink_only", 0.40, 0),
        ("weak_sink_with_local_change", 0.05, equivalent_local_reduction),
    )
    rows = []
    for name, coupling, local in cases:
        for time in (5, 15, 60, 120):
            for tau in (5, 30, 90):
                response = glusignal(time, tau, p, coupling, local)
                clamp = glusignal(time, tau, 1, coupling, local)
                rows.append((name, coupling, f"{local:.5f}", time, tau, f"{p:.5f}",
                             f"{100 * (1 - response):.3f}", f"{100 * (1 - clamp):.3f}"))
    write_tsv(
        "transfer_sensitivity.tsv",
        ("scenario", "coupling_fraction", "local_drive_reduction", "time_min", "tau_min",
         "blood_fraction_of_reference", "modeled_ecs_fall_percent", "fall_with_blood_clamped_percent"),
        rows,
    )
    pk = read_tsv("clinical_pk.tsv")
    baseline = {r["arm_mg"]: float(r["group_mean_ng_mL"]) for r in pk if r["time_min"] == "0"}
    write_tsv(
        "pk_normalization.tsv",
        ("arm_mg", "time_min", "group_mean_over_baseline_group_mean", "reported_mean_within_person_ratio"),
        [
            (r["arm_mg"], r["time_min"],
             f"{float(r['group_mean_ng_mL']) / baseline[r['arm_mg']]:.4f}",
             r["mean_within_person_ratio"])
            for r in pk
        ],
    )


if __name__ == "__main__":
    main()
