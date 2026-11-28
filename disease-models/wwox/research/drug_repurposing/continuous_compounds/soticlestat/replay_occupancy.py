"""Compare CYP46A1 occupancy and 24S-HC from Miyamoto Table S2."""

import argparse
import csv
import hashlib
from math import log
from pathlib import Path
from xml.etree import ElementTree as ET
from zipfile import ZipFile

SUPPLEMENT_SHA256 = "a07385426099afdb68d1b6720734d76201e3c30eabc8efda8af407a2a3e57f4f"
ARMS = ("single_low", "single_middle", "single_high", "fifth_middle")
TIMES = (1, 8, 24)


def read_table(rows):
    values = {}
    for row in rows[3:]:
        time = int(row[0])
        by_arm = [tuple(map(float, cell.split("±"))) for cell in row[1:]]
        values.update(zip(((time, arm) for arm in ARMS), by_arm, strict=True))
    if tuple(dict.fromkeys(time for time, _ in values)) != TIMES:
        raise ValueError("Unexpected timing in Supplemental Table 2")
    return values


def supplement_tables(path):
    if hashlib.sha256(path.read_bytes()).hexdigest() != SUPPLEMENT_SHA256:
        raise ValueError("Unexpected Miyamoto supplement; verify the edition before extracting")
    with ZipFile(path) as archive:
        root = ET.fromstring(archive.read("word/document.xml"))
    tables = {}
    for table in root.findall(".//{*}body/{*}tbl"):
        rows = [
            ["".join(item.text or "" for item in cell.iterfind(".//{*}t")).strip()
             for cell in row.findall("{*}tc")]
            for row in table.findall("{*}tr")
        ]
        metric = rows[0][-1]
        if metric in ("EO, %", "Brain 24HC, % of control"):
            tables[metric] = read_table(rows)
    return tables["EO, %"], tables["Brain 24HC, % of control"]


def source_contrasts(path):
    occupancy, remaining = supplement_tables(path)
    reference = "single_middle"
    for time in TIMES:
        for arm in ARMS:
            eo, eo_sd = occupancy[time, arm]
            ratio, ratio_sd = remaining[time, arm]
            yield (time, arm, eo, eo_sd, 100 - ratio, ratio_sd,
                   eo - occupancy[time, reference][0],
                   remaining[time, reference][0] - ratio)


def turnover():
    # Recalculate the two-animal pulse-chase as a nominal first-order rate.
    inferred_half_life = 15 * log(2) / log(21 / 9)
    # Instantaneous 100% synthesis inhibition and unchanged first-order clearance.
    # The 6, 18 and 36-hour half-lives are illustrative sensitivity cases.
    for half_life in (6, inferred_half_life, 18, 36):
        for time in (1, 2, 4, 6, 8, 24):
            yield (half_life, time, 100 * (1 - 2 ** (-time / half_life)))


def write_table(path, header, rows):
    with path.open("w", newline="") as stream:
        writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
        writer.writerow(header)
        for row in rows:
            writer.writerow(f"{value:.3f}" if isinstance(value, float) else value for value in row)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("supplement", type=Path, help="Pinned publisher DOCX supplement")
    parser.add_argument("--out", type=Path, default=Path(__file__).resolve().parent)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    write_table(args.out / "occupancy_vs_depletion.tsv",
                ("hour", "mouse_arm", "occupancy_percent", "occupancy_sd",
                 "depletion_percent", "depletion_sd", "occupancy_delta_vs_single_middle_pp",
                 "depletion_delta_vs_single_middle_pp"),
                source_contrasts(args.supplement))
    write_table(args.out / "turnover_sensitivity.tsv",
                ("assumed_half_life_h", "time_after_perfect_synthesis_stop_h", "modeled_depletion_percent"),
                turnover())
