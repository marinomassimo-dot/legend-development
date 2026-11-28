"""Rebuild ratios, site-occupancy scenarios and aggregate trial contrasts."""
import argparse
import csv
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import re
from xml.etree import ElementTree

HERE = Path(__file__).resolve().parent


def load_tsv(path):
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write(output, name, header, rows):
    with (output / f"{name}.tsv").open("w", newline="") as handle:
        table = csv.writer(handle, delimiter="\t", lineterminator="\n")
        table.writerow(header.split())
        table.writerows(rows)


def registry_outcome(registry, fragment):
    return next(outcome for outcome in registry["outcomeMeasuresModule"]["outcomeMeasures"]
                if fragment in outcome["title"])


def groups(outcome):
    return {group["id"]: group["title"] for group in outcome["groups"]}


def denominators(outcome):
    return {row["groupId"]: int(row["value"]) for row in outcome["denoms"][0]["counts"]}


def measurements(outcome, position=0):
    return {row["groupId"]: row for row in
            outcome["classes"][position]["categories"][0]["measurements"]}


def reconstruct_counts(n, published):
    reported = Decimal(published)
    precision = Decimal(1).scaleb(reported.as_tuple().exponent)
    matches = [count for count in range(n + 1)
               if (Decimal(100 * count) / n).quantize(precision) == reported]
    if len(matches) != 1:
        raise ValueError(f"Cannot uniquely reconstruct numerator for {n} and {published}")
    return matches[0]


def replay_trials(source, output):
    photo = json.loads((source / "NCT02564029.json").read_text())["resultsSection"]
    spr = registry_outcome(photo, "Most Sensitive Eye Condition")
    complete = registry_outcome(photo, "Complete Suppression")
    photo_groups = groups(spr)
    sample = denominators(complete)
    ratings = measurements(complete)
    means = measurements(spr)
    rows = []
    for group, label in photo_groups.items():
        rows.append((label, sample[group], means[group]["value"],
                     reconstruct_counts(sample[group], ratings[group]["value"]),
                     ratings[group]["value"]))
    write(output, "photosensitivity", "single_exposure n_crossover "
          "adjusted_mean_SPR_points complete_suppression_participants complete_suppression_pct", rows)
    write(output, "photosensitivity_contrasts", "registry_group_ids difference_SPR_points ci90_low "
          "ci90_high", [("/".join(row["groupIds"]), row["paramValue"], row["ciLowerLimit"],
                         row["ciUpperLimit"]) for row in spr["analyses"]])

    focal = json.loads((source / "NCT04244175.json").read_text())["resultsSection"]
    response = registry_outcome(focal, "Response Ratio")
    responder = registry_outcome(focal, "Responder Rate")
    focal_groups = groups(response)
    primary = measurements(response)
    responder_scores = measurements(responder)
    sample = denominators(response)
    responder_sample = denominators(responder)
    participant_flow = focal["participantFlowModule"]
    flow = next(m for m in participant_flow["periods"][0]["milestones"]
                if m["type"] == "STARTED")["achievements"]
    flow_titles = {group["id"]: group["title"] for group in participant_flow["groups"]}
    started_by_arm = {flow_titles[row["groupId"]]: int(row["numSubjects"]) for row in flow}
    started_by_arm[focal_groups["OG003"]] = sum(
        count for arm, count in started_by_arm.items() if arm != "Placebo"
    )
    rows = []
    for group, arm in focal_groups.items():
        started = started_by_arm[arm]
        n_responder = responder_sample[group]
        rate = responder_scores[group]["value"]
        rows.append((arm, started, sample[group], primary[group]["value"], primary[group]["spread"],
                     n_responder, reconstruct_counts(n_responder, rate), rate))
    write(output, "focal_trial", "study_arm randomized primary_n primary_mean_RRatio_points "
          "primary_SD_points responder_n responders_derived responder_pct", rows)
    write(output, "focal_contrasts", "active_minus_placebo RRatio_point_difference ci90_low ci90_high p",
          [(row["groupDescription"], row["paramValue"], row["ciLowerLimit"], row["ciUpperLimit"],
            row["pValue"].removeprefix("=")) for row in response["analyses"]])
    adverse = focal["adverseEventsModule"]
    safety_groups = {group["id"]: group["title"] for group in adverse["eventGroups"]}
    rows = [(event["term"], safety_groups[record["groupId"]], record["numAffected"],
             record["numAtRisk"], f'{100 * record["numAffected"] / record["numAtRisk"]:.2f}')
            for event in adverse["otherEvents"] if event["term"].lower() in
            {"somnolence", "balance disorder", "dizziness", "fatigue"} for record in event["stats"]]
    write(output, "focal_safety", "event arm participants_with_event at_risk risk_pct", rows)


def replay_eligibility(source, output):
    studies = {}
    for search in sorted(source.glob("registry-search-*.json")):
        catalogue = json.loads(search.read_text())
        if catalogue.get("nextPageToken"):
            raise ValueError(f"Incomplete registry query: {search.name}")
        for study in catalogue["studies"]:
            protocol = study["protocolSection"]
            identifier = protocol["identificationModule"]["nctId"]
            age = protocol["eligibilityModule"]
            record = (age["minimumAge"], "/".join(age["stdAges"]))
            if studies.setdefault(identifier, record) != record:
                raise ValueError(f"Inconsistent age eligibility for {identifier}")
    write(output, "registry_ages", "NCT minimum_age age_categories",
          [(identifier, *values) for identifier, values in sorted(studies.items())])


def replay_mouse(source, output):
    article = ElementTree.parse(source / "PMC9532903.xml")
    labels = ("vehicle_PO", "darigabat_0.3_PO", "darigabat_3_PO", "darigabat_10_PO",
              "diazepam_2_IP")
    windows = {"30–50 min", "50–70 min", "70–90 min"}
    rows = []
    for table, endpoint in zip(article.findall(".//table-wrap"), ("HPD_count", "HPD_seconds"),
                               strict=True):
        per_bin = [[float(re.match(r"\s*([0-9.]+)", "".join(value.itertext()))[1]) for value in tr[1:]]
                   for tr in table.findall(".//tbody/tr") if " ".join("".join(tr[0].itertext()).split()) in windows]
        if len(per_bin) != 3:
            raise ValueError("Expected exactly three consecutive published bins")
        means = [sum(bin_values) for bin_values in zip(*per_bin, strict=True)]
        rows.extend((endpoint, label, "30-90", f"{value:.2f}", f"{value / means[0]:.4f}")
                    for label, value in zip(labels, means, strict=True))
    write(output, "mouse_hpd", "endpoint arm window_minutes sum_of_bin_means "
          "ratio_of_means_vs_vehicle", rows)


def replay_receptors(output):
    data = {row["preparation"]: row for row in load_tsv(HERE / "receptor_inputs.tsv")}
    reference = data["human_alpha1_beta3_gamma2"]
    rows = []
    for receptor, values in data.items():
        if receptor.startswith("human") and values["qpatch_max_pct"]:
            ratios = [float(values[key]) / float(reference[key]) for key in
                      ("ki_nM", "qpatch_max_pct", "manual_max_pct")]
            rows.append((receptor, *(f"{ratio:.2f}" for ratio in ratios)))
    write(output, "subtype_ratios", "receptor Ki_ratio_vs_alpha1 QPatch_max_ratio_vs_alpha1 "
          "manual_patch_max_ratio_vs_alpha1", rows)

    # Nickolls' three-component model, with deliberately varied tracer weights.
    rows = []
    maxima = 0.956
    half_values = (3.28, 53.2, 19.3)
    for alpha1_weight in (0.25, 0.5, 0.75):
        weights = (alpha1_weight, (1 - alpha1_weight) / 2, (1 - alpha1_weight) / 2)
        for aggregate in (0.50, 0.686, 0.75):
            low, high = 0.0, 1000.0
            for _ in range(60):
                concentration = (low + high) / 2
                components = [maxima * concentration / (concentration + half) for half in half_values]
                total = sum(w * component for w, component in zip(weights, components, strict=True))
                if total < aggregate:
                    low = concentration
                else:
                    high = concentration
            rows.append((alpha1_weight, aggregate, f"{concentration:.2f}",
                         *(f"{component:.4f}" for component in components)))
    write(output, "pet_sensitivity", "hypothetical_alpha1_signal_weight target_global_occupancy "
          "compatible_total_plasma_ng_mL model_alpha1_occ model_alpha2_occ model_alpha3_occ", rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("sources", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    for row in load_tsv(HERE / "source_inputs.tsv"):
        fingerprint = row["sha256"]
        if fingerprint and fingerprint != hashlib.sha256(
            (args.sources / row["file"]).read_bytes()
        ).hexdigest():
            raise ValueError(f"Source SHA-256 mismatch for {row['file']}")
    args.output.mkdir(parents=True, exist_ok=True)
    replay_receptors(args.output)
    replay_trials(args.sources, args.output)
    replay_eligibility(args.sources, args.output)
    replay_mouse(args.sources, args.output)


if __name__ == "__main__":
    main()
