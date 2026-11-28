"""Recompute cohort aggregates and a cross-system arginine transport sensitivity."""

import argparse
import csv
from decimal import Decimal as D
from hashlib import sha256
from pathlib import Path
from statistics import mean, median
import sys
from xml.etree import ElementTree as ET


def checked(path, expected):
    data = path.read_bytes()
    if sha256(data).hexdigest() != expected:
        raise ValueError(f"Unexpected source fingerprint for {path.name}")
    return data


def cells(row):
    return [" ".join("".join(cell.itertext()).split()) for cell in row]


def spectroscopy(sources):
    # Fons article pp. 725–727. Aggregate only, from the visually read
    # before/after urinary GAA row in Table 1, not its diagnostic row.
    checked(sources / "fons-thesis.pdf",
            "738489816db3f441602aee3b7762882c65c711f3fb86d6da093802ecb509411f")
    pre = tuple(map(D, (34, 22, 117, 50)))
    post = tuple(map(D, (66, 108, 149, 105)))
    paired = [b - a for a, b in zip(pre, post, strict=True)]
    for name, values in (("before", pre), ("after", post), ("paired change", paired)):
        yield "Fons Table 1", f"mean urinary GAA {name}", len(values), mean(values), "mmol/mol creatinine"
    yield "Fons Table 1", "participants with urinary GAA increase", len(paired), sum(x > 0 for x in paired), "count"

    root = ET.fromstring(checked(sources / "chilosi.nxml",
                                 "5f22abb1b6e71c07876fed9bb46a8b9849a59c8ab93011f060d18756b4dbb2d3"))
    table = root.find(".//table-wrap")
    visits = {}
    for row in table.findall(".//tr"):
        entry = cells(row)
        if entry[0] in {"T0", "T1"}:
            visits[entry[0]] = entry[1:]
    for analyte, column, unit in (("PCr/PDE", 0, "ratio"), ("tCr", 1, "mmol/L voxel")):
        pre = visits["T0"][column::2]
        post = visits["T1"][column::2]
        paired = [D(b) - D(a) for a, b in zip(pre, post, strict=True)
                  if a not in {"", "-", "#"} and b not in {"", "-", "#"}]
        if len(paired) != 3:
            raise ValueError("Expected three paired participants at 12 months")
        yield "Chilosi Table 1", f"{analyte} mean paired change", len(paired), mean(paired), unit
        yield "Chilosi Table 1", f"{analyte} median paired change", len(paired), median(paired), unit
        yield "Chilosi Table 1", f"{analyte} participants increasing", len(paired), sum(x > 0 for x in paired), "count"
        omitted_means = [mean(paired[:i] + paired[i + 1:]) for i in range(len(paired))]
        yield "Chilosi Table 1", f"{analyte} min leave-one-out mean", len(paired), min(omitted_means), unit
        yield "Chilosi Table 1", f"{analyte} max leave-one-out mean", len(paired), max(omitted_means), unit


def uptake_sensitivity():
    # Female mouse perfusion nonlinear fit (Fig. 2–3) and single-competitor
    # measurements (Fig. 6). Competition below is a hypothetical joint model.
    km, vmax = D("55"), D("5.9")
    kd_per_min = D("0.00027") * 60

    def flux(arg, orn=0, lys=0):
        apparent_km = km * (1 + D(orn) / 44 + D(lys) / 37)
        saturable = vmax * arg / (apparent_km + arg)
        return saturable, saturable + kd_per_min * arg

    for arm, count, a0, a1, o0, o1 in (("arginine", 22, 81, 168, 198, 283),
                                        ("placebo", 25, 93, 125, 208, 240)):
        yield "Onalo Table 2", f"{arm} post/pre plasma arginine medians", count, D(a1) / D(a0), "fold"
        for scenario, pre_o, post_o, lys in (("arginine only", 0, 0, 0),
                                             ("with ornithine", o0, o1, 0),
                                             ("ornithine and fixed lysine 150 µM", o0, o1, 150),
                                             ("ornithine and fixed lysine 250 µM", o0, o1, 250)):
            basal, higher = flux(a0, pre_o, lys), flux(a1, post_o, lys)
            yield "Cross-system sensitivity", f"{arm}, {scenario}, total at lower composition", "", basal[1], "nmol/min/g"
            yield "Cross-system sensitivity", f"{arm}, {scenario}, total at higher composition", "", higher[1], "nmol/min/g"
            for component, j0, j1 in zip(("saturable", "saturable plus linear"), basal, higher, strict=True):
                yield "Cross-system sensitivity", f"{arm}, {scenario}, {component}", "", j1 / j0, "fold"


def transfer_sensitivity():
    for description, decrease in (("raw 37 C", D("30.6")), ("37 C minus 4 C", D("53.2"))):
        yield "Jomura Fig. 4", f"{description} proportional transport share", 3, decrease / D("57.8") * 100, "%"
    yield "Jomura Fig. 5", "apparent brain clearance creatine/mannitol", "", D("4.65") / D("5.18"), "fold"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("sources", type=Path)
    sources = parser.parse_args().sources
    writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    writer.writerow(("source", "contrast", "n_values_when_given", "value", "unit"))
    for comparison in (spectroscopy(sources), uptake_sensitivity(), transfer_sensitivity()):
        writer.writerows((source, name, n, f"{value:.4f}", unit) for source, name, n, value, unit in comparison)
