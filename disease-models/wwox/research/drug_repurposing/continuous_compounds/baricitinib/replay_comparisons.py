"""Replay the aggregate baricitinib exposure and published Laitman Fig. 5 contrasts."""
import argparse
import csv
import hashlib
from pathlib import Path, PurePosixPath
from statistics import mean
import sys
from xml.etree import ElementTree
from zipfile import ZipFile


HERE = Path(__file__).resolve().parent
WORKBOOK_SHA256 = "39299d5bac8812585d3d0a60117d0d07b0d525d2f6618edaecd3b02a2f5a11de"
PANELS = {
    "Figure 5I": {"olig1_p0_APC": ("A", "C", "cells per lumbar section")},
    "Figure 5J": {"olig1_p0_MBP": ("A", "C", "um2 per lumbar section")},
    "Figure 5M": {
        "pdgfra_E18_OLP": ("C", "D", "source cell count"),
        "pdgfra_E18_APC": ("E", "F", "source cell count"),
    },
}
EXPECTED_COLUMNS = {
    "Figure 5I": ("A5", "C5", "Stat3fl/fl", "Olig1Cre:Stat3fl/fl"),
    "Figure 5J": ("A3", "C3", "Stat3fl/fl", "Olig1Cre:Stat3fl/fl"),
    "Figure 5M": ("C5", "D5", "Stat3 f/f", "Stat3 f/f:PdgfraCre"),
}


def numeric_sheet(archive, name):
    rels = ElementTree.fromstring(archive.read("xl/_rels/workbook.xml.rels"))
    targets = {entry.get("Id"): entry.get("Target") for entry in rels}
    workbook = ElementTree.fromstring(archive.read("xl/workbook.xml"))
    sheet, = [node for node in workbook.findall(".//{*}sheet") if node.get("name") == name]
    rid = next(value for key, value in sheet.attrib.items() if key.endswith("}id"))
    path = PurePosixPath("xl", targets[rid])
    root = ElementTree.fromstring(archive.read(str(path).lstrip("/")))
    shared = ElementTree.fromstring(archive.read("xl/sharedStrings.xml"))
    strings = ["".join(node.itertext()) for node in shared.findall("{*}si")]
    cells = {}
    for cell in root.findall(".//{*}c"):
        value = cell.findtext("{*}v")
        if value is not None:
            cells[cell.get("r")] = strings[int(value)] if cell.get("t") == "s" else float(value)
    return cells


def replay_tissue(workbook, output):
    if hashlib.sha256(workbook.read_bytes()).hexdigest() != WORKBOOK_SHA256:
        raise ValueError("The workbook differs from the verified publisher S1 Data")
    with ZipFile(workbook) as archive:
        for panel, comparisons in PANELS.items():
            cells = numeric_sheet(archive, panel)
            first, second, reference, perturbed = EXPECTED_COLUMNS[panel]
            if (cells[first], cells[second]) != (reference, perturbed):
                raise ValueError(f"Unresolved genotype columns in {panel}")
            for name, (control_col, loss_col, unit) in comparisons.items():
                groups = [[value for key, value in cells.items()
                           if key.rstrip("0123456789") == column and isinstance(value, float)]
                          for column in (control_col, loss_col)]
                means = [mean(group) for group in groups]
                for arm, values, average in zip(("control", "Stat3-loss"), groups, means):
                    output.writerow([name, panel, f"{arm} mean from {len(values)} entries",
                                     f"{average:.4f}", unit])
                output.writerow([name, panel, "relative change of means",
                                 f"{100 * (means[1] / means[0] - 1):.2f}", "percent"])


def replay_exposure(output):
    with (HERE / "source_inputs.tsv").open(encoding="utf-8") as handle:
        entries = {row["id"]: row for row in csv.DictReader(handle, delimiter="\t")}
    mass = float(entries["molecular_weight"]["value"])
    csf = {key: 1000 * float(row["value"]) / mass
           for key, row in entries.items() if row["kind"] == "csf"}
    for name, value in csf.items():
        output.writerow([name, "molecular_weight", "CSF total", f"{value:.4f}", "nM"])
    for name, row in entries.items():
        if row["kind"] not in {"assay", "bath"}:
            continue
        value = float(row["value"])
        comparator = "nominal blood IC50" if row["kind"] == "assay" else "tested nominal bath"
        for sample in ("ags_median", "ags_max"):
            output.writerow([name, sample, f"{comparator} / total CSF",
                             f"{value / csf[sample]:.4f}", "fold"])
        if row["reference"]:
            reference = float(entries[row["reference"]]["value"])
            output.writerow([name, row["reference"], "nominal IC50 ratio within stimulus",
                             f"{value / reference:.4f}", "fold"])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("publisher_s1_data", type=Path)
    output = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    output.writerow(["comparison", "reference", "statistic", "value", "unit"])
    replay_exposure(output)
    replay_tissue(parser.parse_args().publisher_s1_data, output)
