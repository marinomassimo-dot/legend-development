"""Recompute descriptive, study-specific clinical and assay contrasts."""

import argparse
import csv
from decimal import Decimal as D
from hashlib import sha256
import json
from pathlib import Path
import sys
from xml.etree import ElementTree as ET


def checked(path, expected):
    data = path.read_bytes()
    if sha256(data).hexdigest() != expected:
        raise ValueError(f"Unexpected source fingerprint for {path.name}")
    return data


def registry_measure(outcomes, title):
    row, = (result for result in outcomes if result["title"] == title)
    groups = {group["id"]: group["title"] for group in row["groups"]}
    values = row["classes"][0]["categories"][0]["measurements"]
    return {groups[value["groupId"]]: D(value["value"]) for value in values}


def norm_text(node):
    return " ".join("".join(node.itertext()).split())


def rows(sources):
    registry = json.loads(checked(
        sources / "NCT01053156.json",
        "f57bc2ab0e6cb243594e502761b99e5b7ca5473de4f07418806ade00f70373d2",
    ))
    outcomes = registry["resultsSection"]["outcomeMeasuresModule"]["outcomeMeasures"]
    for title, unit in (("Clinical Global Impression Scale (CGI)", "rating units"),
                        ("Visual Analogue Scale- Behavior 1", "cm")):
        values = registry_measure(outcomes, title)
        yield "NCT01053156", title, values["Minocycline"] - values["Placebo"], unit

    angelman = ET.fromstring(checked(
        sources / "aas-manece.nxml",
        "3b0d79e2b3d9fc35785943166f5b14a7a0c5447e982c4c77d1ecbb1255e2a4f1",
    ))
    table = angelman.find(".//table-wrap[@id='Tab2']")
    change = next(row for row in table.findall(".//tr") if norm_text(row[0]) == "Absolute mean change")
    placebo, treated = (D(norm_text(td).split()[0].replace("·", ".")) for td in change[1:3])
    yield "A-MANECE Table 2", "minocycline minus placebo change at 8 weeks", treated - placebo, "age-equivalent months"

    # Acute spinal-injury high-IV CSF (Casha 2012 abstract).
    # Convert concentrations of the measured parent using its molar mass,
    # distinct from the molecular mass of the dispensed hydrochloride salt.
    parent_mass = D("457.5")
    for value, label in (("2.1", "CI low"), ("2.3", "mean"), ("2.5", "CI high")):
        yield "Casha 2012 abstract", f"acute spinal-injury CSF {label}", D(value) * 1000 / parent_mass, "µM"
    csf = D("2.3") * 1000 / parent_mass
    yield "Casha and Romero-Perez", "direct active MMP9 IC50 / mean CSF", D(180) / csf, "fold"

    # Dziembowska Results and Fig. 1 report the model ratio to baseline
    # from paired plasma samples, including latent and active bands.
    for value, label in (("0.58", "CI low"), ("0.75", "geometric"), ("0.97", "CI high")):
        yield "Dziembowska 2013", f"change in normalized plasma signal, {label}", (D(value) - 1) * 100, "%"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("sources", type=Path)
    writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    writer.writerow(("source", "contrast", "value", "unit"))
    writer.writerows((source, label, f"{value:.4f}", unit)
                     for source, label, value, unit in rows(parser.parse_args().sources))
