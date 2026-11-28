"""Replay public tideglusib assay, figure, and registry comparisons."""

import argparse
import csv
from hashlib import sha256
from itertools import product
import json
from math import log
from pathlib import Path


SNAPSHOTS = {
    "NCT03692312.json": "6753fdff08ec53814c3a79e440db875ce1e0028773b136888b1057c203a2f5d4",
    "NCT02858908.json": "ededd5f42a369a1ef142eeb5a782168b1fd830799902b18cbec6cc6dc39c3e2e",
    "Engel_2018.pdf": "5d907b55d8b25bd87d6f0ac80364a838f9cca86d8e995b5e6e9b702a4a54df34",
}
MOLAR_MASS = 334.39


def verified(path):
    data = path.read_bytes()
    if sha256(data).hexdigest() != SNAPSHOTS[path.name]:
        raise ValueError(f"Input SHA-256 differs for {path}")
    return data


def write(path, header, rows):
    with path.open("w", newline="") as stream:
        writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
        writer.writerow(header.split())
        writer.writerows(rows)


def enzyme_rows():
    return (
        ("Dominguez_WT_beta", 1, 105, 5, 21.0, "NA"),
        ("Dominguez_C199A_beta", 1, 7000, 60, f"{7000 / 60:.2f}", f"{log(2) / (.000088 * 3600):.2f}"),
        ("Gordon_WT_beta", 3, 1780, 139, f"{1780 / 139:.2f}", "NA"),
    )


def cross_engagement():
    # Paired table values, followed by GSK3α cross-engagement conditional on a Hill slope.
    ratios = (
        ("tideglusib_beta", 908 / 502, "matched recombinant pair"),
        ("BRD3731_beta", 215 / 15, "matched recombinant pair"),
        ("BRD0705_alpha", 515 / 66, "matched recombinant pair"),
        ("cellular_sensitivity_4fold", 4, "sensitivity"),
        ("cellular_sensitivity_6fold", 6, "sensitivity"),
    )
    for (label, ratio, basis), exponent, target in product(ratios, (.7, 1.0, 1.5), (.2, .5, .8)):
        off = 1 / (1 + ratio**exponent * (1 - target) / target)
        yield label, f"{ratio:.4f}", basis, exponent, target, f"{off:.4f}"


def exposure_rows():
    # Di Deo et al., Table 3. Visit 4 model summaries, not observed patient maxima.
    plasma_samples = (("lower_trial_group", "peak", 513.5), ("lower_trial_group", "trough", 4.1),
                      ("upper_trial_group", "peak", 1170.9), ("upper_trial_group", "trough", 5.6))
    thresholds = (("WT_beta_1h", 5), ("WT_beta_0h", 105), ("WT_beta_3h_independent", 139),
                  ("WT_beta_paired", 502), ("WT_alpha_paired", 908))
    for (cohort, window, ng_ml), (assay, nM) in product(plasma_samples, thresholds):
        total = 1000 * ng_ml / MOLAR_MASS
        yield cohort, window, ng_ml, f"{total:.3f}", assay, nM, f"{100 * nM / total:.3f}", f"{.01 * total:.3f}"


def figure_rows(pdf):
    import pymupdf

    # Coordinates read from PDF page 9 at 1.8x. Sample the connected bar from baseline.
    panels = (
        ("4a_EEG", 339, 199, 20, (315, 354, 395, 434, 474)),
        ("4b_injury", 541, 400, 80, (316, 355, 395, 433, 472)),
        ("4c_injury_WT", 541, 400, 150, (573, 611)),
        ("4c_injury_Lpr", 541, 398, 200, (724, 762)),
    )
    with pymupdf.open(stream=verified(pdf), filetype="pdf") as document:
        image = document[8].get_pixmap(matrix=pymupdf.Matrix(1.8, 1.8))
        for panel, zero, top, maximum, xs in panels:
            groups = (("vehicle", "NP103_low", "NP103_high", "NP12_low", "NP12_high")
                      if len(xs) == 5 else ("vehicle", "NP12"))
            for index, (group, x) in enumerate(zip(groups, xs, strict=True)):
                y = zero - 1
                while y > top and max(image.pixel(x, y)) < 70:
                    y -= 1
                bar = y + 1
                mean = (zero - bar) * maximum / (zero - top)
                if index == 0:
                    reference = mean
                yield panel, group, x, bar, f"{mean:.2f}", f"{mean - reference:+.2f}"


def clinical_rows(sources):
    for study in ("NCT03692312", "NCT02858908"):
        data = json.loads(verified(sources / f"{study}.json"))["resultsSection"]
        flow = data["participantFlowModule"]
        start = next(m for m in flow["periods"][0]["milestones"] if m["type"] == "STARTED")
        for a in start["achievements"]:
            yield study, "study_period_started", a["groupId"], a["numSubjects"], "NA"
        for g in data["adverseEventsModule"]["eventGroups"]:
            yield study, "serious_adverse_event_people", g["id"], g["seriousNumAffected"], g["seriousNumAtRisk"]
            yield study, "nonserious_adverse_event_people", g["id"], g["otherNumAffected"], g["otherNumAtRisk"]
        primary = next(o for o in data["outcomeMeasuresModule"]["outcomeMeasures"] if o["type"] == "PRIMARY")
        for group in primary["denoms"][0]["counts"]:
            yield study, "primary_endpoint_analysis_n", group["groupId"], group["value"], "NA"
        if study == "NCT03692312":
            est = primary["analyses"][0]
            for key in ("paramValue", "ciLowerLimit", "ciUpperLimit", "pValue"):
                yield study, f"CDM1_RS_week20_{key}", "-".join(est["groupIds"]), est[key], "NA"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("sources", type=Path, help="Directory containing the pinned trial JSONs and PDF")
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    for name, header, rows in (
        ("enzyme_time_contrasts.tsv", "comparison preincubation_h IC50_before_nM IC50_after_nM ratio_before_after C199A_off_rate_half_life_h", enzyme_rows()),
        ("matched_isoform_sensitivity.tsv", "compound_target off_on_IC50_ratio basis assumed_same_slope target_block off_target_block", cross_engagement()),
        ("plasma_threshold_sensitivity.tsv", "cohort sampling plasma_total_ng_ml plasma_total_nM assay midpoint_nM required_percent_unbound_brain_to_total_plasma modeled_brain_nM_at_1pct_ratio", exposure_rows()),
        ("engel_fig4_replay.tsv", "panel group x_pixel bar_top_y_pixel approximate_mean difference_from_same_panel_vehicle", figure_rows(args.sources / "Engel_2018.pdf")),
        ("dm1_registry_replay.tsv", "trial measure group value denominator", clinical_rows(args.sources)),
        ("pparg_context_replay.tsv", "phenotype antagonist no_tideglusib with_tideglusib tideglusib_increment", (
            ("CA3_normalized_labeling_percent", "absent", 15, 95, 80),
            ("CA3_normalized_labeling_percent", "present", 20, 25, 5),
            ("CA3_normalized_labeling_percent", "difference_of_increments", "NA", "NA", -75),
        )),
    ):
        write(args.output / name, header, rows)


if __name__ == "__main__":
    main()
