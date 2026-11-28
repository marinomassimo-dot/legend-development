"""Verify the public trial status and compare measured plasma exposure by unit."""
import argparse
import csv
from hashlib import sha256
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("snapshot", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    content = args.snapshot.read_bytes()
    if sha256(content).hexdigest() != "136f0c8c8c5120f6efd4ea22ea1c27ac4c0c9c5d98652bc1f4d0d42f936c6717":
        raise ValueError("Expected the documented registry snapshot from 2026-11-27")
    study = json.loads(content)
    protocol = study["protocolSection"]
    nct = protocol["identificationModule"]["nctId"]
    status = protocol["statusModule"]
    eligibility = protocol["eligibilityModule"]
    design = protocol["designModule"]
    rows = [
        ("NCT04925960 status", status["overallStatus"], "registry label", nct),
        ("NCT04925960 reason", status["whyStopped"], "registry text", nct),
        ("NCT04925960 randomized", design["designInfo"]["allocation"], "registry label", nct),
        ("NCT04925960 actual enrollment", design["enrollmentInfo"]["count"], "participants", nct),
        ("NCT04925960 age eligibility",
         f'{eligibility["minimumAge"]} to {eligibility["maximumAge"]}', "registry bounds", nct),
        ("NCT04925960 resultsSection present", str("resultsSection" in study).lower(), "boolean", nct),
        ("NCT04925960 hasResults", str(study["hasResults"]).lower(), "boolean", nct),
    ]
    rows.extend(("NCT04925960 primary measure", outcome["measure"], outcome["timeFrame"], nct)
                for outcome in protocol["outcomesModule"]["primaryOutcomes"])

    label = "Sawai PMDA sections 16.1.1 and 16.3"
    pediatric = "Ligezka 2021, pharmacokinetics Results and Fig. 7B"
    mw = 319.40
    free_fraction = 1 - 0.901
    rows.extend([
        ("Molecular mass", mw, "g/mol", "Sawai PMDA section 19"),
        ("Protein binding", 90.1, "% in vitro in human serum", label),
    ])
    for population, measured, source in (
        ("Adult single administration peak", 3896, label),
        ("Adult single administration 4 h", 370, label),
        ("Pediatric case observed peak", 1125, pediatric),
        ("Pediatric case late time point", 23.4, pediatric),
    ):
        total = measured / mw
        free = total * free_fraction
        rows.extend([
            (population, measured, "ng/mL plasma, measured total", source),
            (population, f"{total:.5f}", "µM plasma, converted total", source),
            (population, f"{free:.5f}", "µM plasma, binding-fraction scenario", source),
        ])
    rows.extend([
        ("PMM2 fibroblast nominal / adult free peak scenario", f"{10 / (3896 / mw * free_fraction):.2f}",
         "ratio, different matrices", "Radenkovic 2023 Fig. 2A–C; PMDA 16.1.1/16.3"),
        ("PMM2 fibroblast nominal / pediatric total observed peak", f"{10 / (1125 / mw):.2f}",
         "ratio, different matrices", "Radenkovic 2023 Fig. 2A–C; Ligezka 2021 Fig. 7B"),
    ])
    with args.output.open("w", newline="") as stream:
        writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
        writer.writerow(("comparison", "value", "unit_or_scope", "source"))
        writer.writerows(rows)


if __name__ == "__main__":
    main()
