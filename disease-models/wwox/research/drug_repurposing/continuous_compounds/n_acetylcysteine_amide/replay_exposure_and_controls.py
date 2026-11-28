"""Recompute descriptive NACA exposure and control contrasts from public sources."""

import argparse
import csv
from decimal import Decimal as D
from hashlib import sha256
from pathlib import Path
import sys
from xml.etree import ElementTree as ET


def penugonda_tables(path):
    data = path.read_bytes()
    if sha256(data).hexdigest() != "377a6091561f08b12cbf1668769274bc3b6357bed743886cf4108ad4c5c60756":
        raise ValueError("Unexpected Penugonda manuscript fingerprint")
    root = ET.fromstring(data)
    for table_id in ("T1", "T2"):
        table = {}
        for tr in root.findall(f".//table-wrap[@id='{table_id}']//tbody/tr"):
            values = ["".join(td.itertext()).strip() for td in tr]
            table[values[0]] = [D(value.split("±")[0].strip()) for value in values[1:]]
        yield table


def rows(source):
    # Wu et al. Table 3, p. 419. Three adult rats per condition. Brain and
    # liver are nmol/mg homogenate protein, whereas plasma is in µM.
    plasma_ratio = D("15.07") / D("84.55")
    brain_ratio = D("0.05") / D("0.07")
    yield "Wu 2006 Table 3", "plasma NACA/NAC ratio of means", plasma_ratio, "ratio"
    yield "Wu 2006 Table 3", "brain NACA/NAC ratio of means", brain_ratio, "ratio"
    yield "Wu 2006 Table 3", "brain/plasma within-matrix ratios", brain_ratio / plasma_ratio, "fold"
    for matrix, vehicle, treated in (("brain", "10.18", "10.97"), ("liver", "13.55", "31.57"),
                                     ("plasma", "6.96", "22.59")):
        yield "Wu 2006 Table 3", f"{matrix} GSH treated/vehicle means", D(treated) / D(vehicle), "fold"

    lead, redox = penugonda_tables(source)
    for endpoint, table, column, unit in (
        ("brain lead", lead, 1, "ppb"),
        ("brain GSH", redox, 0, "nmol/mg protein"),
        ("brain GSH/GSSG", redox, 1, "ratio"),
        ("brain Glu/Gln", redox, 3, "ratio"),
        ("brain glutamine synthetase", redox, 4, "U/mg protein"),
    ):
        locator = "Penugonda 2011 Table 1" if table is lead else "Penugonda 2011 Table 2"
        for label in ("Control", "Lead only", "Lead + NAC", "Lead + NACA"):
            yield locator, f"{label}, {endpoint}", table[label][column], unit
        contrast = table["Lead + NACA"][column] - table["Lead + NAC"][column]
        yield locator, f"NACA minus NAC after lead, {endpoint}", contrast, unit

    # Sponsor's approximate aggregate plasma values. Molecular mass of
    # nominal parent from PubChem CID 10176265. No free fraction is assigned.
    molecular_mass = D("162.21")
    for label, value in (("solution Cmax day 14", 900), ("tablet range low", 600), ("tablet range high", 800)):
        yield "US20260240778A1 [0160]", label, D(value) / molecular_mass, "µM"

    # Glutamate plus BSO plus NACA arm divided by untreated mean.
    yield "Penugonda 2005 Table 1", "triple-arm GSH/untreated mean", D(30) / D(54), "fold"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("penugonda_xml", type=Path)
    writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    writer.writerow(("locator", "endpoint", "value", "unit"))
    writer.writerows((locator, endpoint, f"{value:.4f}", unit)
                     for locator, endpoint, value, unit in rows(parser.parse_args().penugonda_xml))
