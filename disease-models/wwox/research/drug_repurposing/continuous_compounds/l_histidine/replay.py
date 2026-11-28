"""Reanalyse Volcko et al. Fig. 6 from the Zenodo event and session files."""
import argparse
import csv
import sys

from collections import Counter
from pathlib import Path
from statistics import mean
from xml.etree import ElementTree as ET
from zipfile import ZipFile


NS = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}


def read_session_sheet(path):
    with ZipFile(path) as archive:
        strings = ["".join(node.itertext()) for node in ET.fromstring(
            archive.read("xl/sharedStrings.xml")
        )]
        sheet = ET.fromstring(archive.read("xl/worksheets/sheet1.xml"))

    rows = []
    for row in sheet.findall(".//m:row", NS):
        values = []
        for cell in row:
            value = cell.findtext("m:v", namespaces=NS)
            values.append(strings[int(value)] if cell.get("t") == "s" else value)
        rows.append(values)
    return [dict(zip(rows[0], row, strict=True)) for row in rows[1:]]


def read_trials(path):
    starts_ms = []
    counts = []
    spouts = Counter()
    for line in path.read_text().splitlines():
        if not line.strip():
            continue
        event, time_ms = map(int, line.split())
        if event == 2:
            starts_ms.append(time_ms)
            counts.append(0)
        elif 41 <= event <= 45:
            assert starts_ms and 0 <= time_ms - starts_ms[-1] <= 3000, path
            counts[-1] += 1
            spouts[event - 40] += 1
    assert len(counts) == 100, path
    return counts, spouts


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_dir", type=Path)
    args = parser.parse_args()
    root = args.input_dir
    sessions = read_session_sheet(root / "multispout_metafile.xlsx")
    with (root / "multispout_individual_licks_per_trial_data.csv").open(newline="") as handle:
        authors = {(row["mouse"], row["injection"]): row for row in csv.DictReader(handle)}

    animals = sorted({row["mouse"] for row in sessions})
    assert len(animals) == 8 and len(sessions) == len(authors) == 16
    for cohort in (2, 3):
        with (root / f"HL_cohort{cohort}_metafile.csv").open(newline="") as handle:
            photometry_animals = {row["mouse"] for row in csv.DictReader(handle)}
        assert not photometry_animals.intersection(animals)

    outcomes = {}
    for session in sessions:
        key = session["mouse"], session["injection"]
        counts, spouts = read_trials(root / "multispout" / session["filename"])
        total = sum(counts)
        assert total == float(authors[key]["total_licks"])
        for spout in range(1, 6):
            concentration = session[f"spout{spout}"]
            assert spouts[spout] == float(authors[key][concentration])
        active = sum(value > 0 for value in counts)
        assert key not in outcomes and active > 0
        outcomes[key] = (total, active, total / active)

    writer = csv.writer(sys.stdout, dialect="excel-tab", lineterminator="\n")
    writer.writerow(("metric", "vehicle_mean", "histidine_mean", "paired_delta",
                     "animals_decreased", "leave_one_out_delta_min", "leave_one_out_delta_max"))
    metrics = ("licks per session", "trials with a lick per 100", "licks per active trial")
    for column, label in enumerate(metrics):
        vehicle = [outcomes[mouse, "veh"][column] for mouse in animals]
        histidine = [outcomes[mouse, "his"][column] for mouse in animals]
        differences = [his - veh for veh, his in zip(vehicle, histidine, strict=True)]
        leave_one_out = [mean(differences[:i] + differences[i + 1:]) for i in range(len(animals))]
        writer.writerow((label, f"{mean(vehicle):.3f}", f"{mean(histidine):.3f}",
                         f"{mean(differences):.3f}", sum(d < 0 for d in differences),
                         f"{min(leave_one_out):.3f}", f"{max(leave_one_out):.3f}"))


if __name__ == "__main__":
    main()
