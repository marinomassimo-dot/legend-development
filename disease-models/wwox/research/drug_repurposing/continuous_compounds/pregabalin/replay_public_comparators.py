"""Extract registered pregabalin outcomes and compare measured CSF with bath concentrations."""

import argparse
import csv
import hashlib
import json
from pathlib import Path
import sys

TRIAL_SHA256 = "0e8aac6112eea8dd94e67f008b84598a70f433de5a582c8a6b41e20cbf578c8a"
PREGABALIN_GRAMS_PER_MOLE = 159.23


def first_measurements(outcome):
    return outcome["classes"][0]["categories"][0]["measurements"]


def trial_rows(result):
    flow = result["participantFlowModule"]["periods"][0]["milestones"]
    started, completed = ([int(row["numSubjects"]) for row in item["achievements"]] for item in flow[:2])
    primary, response = result["outcomeMeasuresModule"]["outcomeMeasures"][:2]
    somnolence = next(event["stats"] for event in result["adverseEventsModule"]["otherEvents"]
                      if event["term"] == "Somnolence")
    for index, (group, primary_n, adjusted, responders, drowsy) in enumerate(zip(
        primary["groups"], primary["denoms"][0]["counts"], first_measurements(primary),
        first_measurements(response), somnolence, strict=True,
    )):
        n = int(primary_n["value"])
        response_count = round(n * float(responders["value"]) / 100)
        label = group["title"]
        yield label, "randomized", started[index], "people"
        yield label, "completed blinded period", completed[index], "people"
        yield label, "primary modified ITT", n, "people"
        yield label, "outside primary modified ITT", started[index] - n, "people"
        yield label, "adjusted log(24-hour seizure count + 1)", adjusted["value"], "log scale"
        yield label, "≥50% EEG responders", f"{response_count}/{n}", "people / mITT"
        yield label, "reported somnolence", f'{drowsy["numAffected"]}/{drowsy["numAtRisk"]}', "people / safety denominator"
    for i, contrast in enumerate(primary["analyses"]):
        label = primary["groups"][i]["title"] + " versus placebo"
        yield label, "adjusted log difference (95% CI)", (
            f'{contrast["paramValue"]} ({contrast["ciLowerLimit"]}, {contrast["ciUpperLimit"]})'
        ), "log scale"
        yield label, "primary p-value", contrast["pValue"], "probability"


def cerebrospinal_rows():
    for hour, micrograms_per_ml in ((2, 0.115), (6, 0.359)):
        micromolar = micrograms_per_ml * 1000 / PREGABALIN_GRAMS_PER_MOLE
        label = f"Adult lumbar CSF at {hour}h, PMID 20975469"
        yield label, "reported concentration", micrograms_per_ml, "µg/mL"
        yield label, "molar conversion", f"{micromolar:.4f}", "µM"
        for bath in (20, 100, 500):
            yield label, f"nominal {bath} µM bath / reported CSF", f"{bath / micromolar:.2f}", "ratio"


def rat_extracellular_rows():
    # FDA nonclinical review, printed p. 42 (PDF p. 78), pdftoppm at 140 dpi.
    time_zero_x, time_100_x, sample_x = 304, 417, 421
    ng_per_ml_100_y, ng_per_ml_1000_y = 497, 406
    minutes = 100 * (sample_x - time_zero_x) / (time_100_x - time_zero_x)
    for compartment, sample_y in (("brain extracellular fluid", 445), ("plasma", 352)):
        order = 2 + (ng_per_ml_100_y - sample_y) / (ng_per_ml_100_y - ng_per_ml_1000_y)
        ng_per_ml = 10**order
        label = f"FDA rat {compartment}, scan page 78"
        yield label, "estimated time at plotted mean", f"{minutes:.1f}", "min"
        yield label, "digitized plotted mean", f"{ng_per_ml:.1f}", "ng/mL"
        yield label, "molar conversion", f"{ng_per_ml / PREGABALIN_GRAMS_PER_MOLE:.4f}", "µM"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("trial_snapshot", type=Path)
    args = parser.parse_args()
    contents = args.trial_snapshot.read_bytes()
    if hashlib.sha256(contents).hexdigest() != TRIAL_SHA256:
        raise ValueError("The registry snapshot differs from the input used for this comparison.")
    result = json.loads(contents)["resultsSection"]
    writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    writer.writerow(("source_group", "measure", "value", "unit"))
    writer.writerows(trial_rows(result))
    writer.writerows(cerebrospinal_rows())
    writer.writerows(rat_extracellular_rows())


if __name__ == "__main__":
    main()
