"""Replay matched recombinant block and registered aggregate Rett outcomes."""

import argparse
import csv
from hashlib import sha256
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
# Dravid et al. Table 2. Functional IC50s in µM, -40 mV and no added Mg²⁺.
POTENCIES = {
    7.6: {"GluN2A": (11.3, 1.3), "GluN2B": (3.74, 0.329),
          "GluN2C": (1.07, 0.146), "GluN2D": (5.4, 0.736)},
    6.9: {"GluN2A": (5.12, 0.67), "GluN2B": (1.277, 0.246),
          "GluN2C": (0.466, 0.114), "GluN2D": (2.4, 0.464)},
}
REGISTRY = {
    "NCT00593957": "25cfcc634b825834fe6f960c6e4092a96d78b129a5da5ba772dc2b8081032145",
    "NCT01520363": "34702c6ba3e71b946757b96efab7fbe4d7e3c80ec870a18143685de3b3c4e7a3",
}


def channel_comparisons():
    # Match 30% GluN2B block in an illustrative Hill-1 equilibrium model.
    drive = 0.30 / (1.0 - 0.30)
    for ph, subtypes in POTENCIES.items():
        parent_b, metabolite_b = subtypes["GluN2B"]
        parent_dose = drive * parent_b
        metabolite_dose = drive * metabolite_b
        for receptor, (parent_ic50, metabolite_ic50) in subtypes.items():
            parent_block = parent_dose / (parent_dose + parent_ic50)
            metabolite_block = metabolite_dose / (metabolite_dose + metabolite_ic50)
            equal_drive_share = metabolite_ic50 / (parent_ic50 + metabolite_ic50)
            yield (ph, receptor, parent_ic50, metabolite_ic50, parent_ic50 / metabolite_ic50,
                   parent_dose, metabolite_dose, parent_block, metabolite_block,
                   parent_block - metabolite_block, equal_drive_share)


def load_registry(raw, trial):
    byte_string = (raw / f"{trial}.json").read_bytes()
    if sha256(byte_string).hexdigest() != REGISTRY[trial]:
        raise ValueError(f"Unexpected published data snapshot for {trial}")
    return json.loads(byte_string)["resultsSection"]["outcomeMeasuresModule"]["outcomeMeasures"]


def aggregates(outcome):
    # These registered outcomes have one table and one category without strata.
    category, = outcome["classes"]
    table, = category["categories"]
    denominators, = outcome["denoms"]
    values = {item["groupId"]: float(item["value"]) for item in table["measurements"]}
    counts = {item["groupId"]: int(item["value"]) for item in denominators["counts"]}
    return [(counts[g["id"]], values[g["id"]]) for g in outcome["groups"]]


def clinical_comparisons(raw):
    older_trial, controlled = REGISTRY
    cohorts = load_registry(raw, older_trial)
    eeg = next(m for m in cohorts if m["title"].startswith("Difference in EEG Spike Counts"))
    values = aggregates(eeg)
    for i, arm in enumerate(("lower_active", "middle_active", "higher_active")):
        (n_pre, pre), (n_post, post) = values[i], values[i + 3]
        yield (older_trial, "spikes_per_min", arm, n_pre, n_post, pre, post, post - pre, "NA",
               eeg["analyses"][i]["pValue"])
    for measure in load_registry(raw, controlled):
        title = measure["title"]
        if title.startswith("Change in Seizure Frequency"):
            group = "age_0_to_4" if "0-4" in title else "age_5_to_10"
        elif title.startswith("Change in Mullen; Receptive Language"):
            group = "mullen_receptive_language"
        else:
            continue
        (n_dp, dp), (n_pp, pp), (n_df, df), (n_pf, pf) = aggregates(measure)
        marginal = (df - dp) - (pf - pp)
        shared_p = measure["analyses"][0]["pValue"] if group.startswith("age_") else "NA"
        yield controlled, group, "drug", n_dp, n_df, dp, df, df - dp, marginal, shared_p
        yield controlled, group, "placebo", n_pp, n_pf, pp, pf, pf - pp, "NA", "NA"


def write(path, header, rows):
    with path.open("w", newline="") as f:
        out = csv.writer(f, delimiter="\t", lineterminator="\n")
        out.writerow(header)
        for row in rows:
            out.writerow(f"{value:.6f}" if isinstance(value, float) else value for value in row)


def main(data_root, out):
    out.mkdir(parents=True, exist_ok=True)
    write(out / "matched_block.tsv",
          ("pH", "receptor", "parent_IC50_uM", "metabolite_IC50_uM",
           "parent_over_metabolite_IC50", "parent_at_30pct_GluN2B_uM",
           "metabolite_at_30pct_GluN2B_uM", "parent_block_fraction", "metabolite_block_fraction",
           "parent_minus_metabolite_block", "metabolite_molar_share_for_equal_drive"),
          channel_comparisons())
    write(out / "registered_rett.tsv",
          ("trial", "outcome", "arm", "n_baseline", "n_followup", "baseline_mean", "followup_mean",
           "unadjusted_marginal_change", "drug_minus_placebo_marginal_change",
           "reported_p_label_for_analysis"),
          clinical_comparisons(data_root))


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("public_registry_snapshot_dir", type=Path)
    p.add_argument("--out", type=Path, default=HERE)
    args = p.parse_args()
    main(args.public_registry_snapshot_dir, args.out)
