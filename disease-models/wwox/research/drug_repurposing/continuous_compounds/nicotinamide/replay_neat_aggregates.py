"""Compute aggregate NEAT PK observations from published Supplementary Table 2."""

import argparse
from collections import defaultdict
from decimal import Decimal
from hashlib import sha256
from pathlib import Path
from statistics import mean
from xml.etree import ElementTree as ET
from zipfile import ZipFile


DIGEST = "751e2ffdf9b2875fc352dbcb58a5d3ef42572e01736143bcf885ea517ea753af"
NS = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
NAM_LOQ = Decimal("0.4")
ELEVATED = Decimal("2.1")


def read_groups(path):
    if sha256(path.read_bytes()).hexdigest() != DIGEST:
        raise ValueError("NEAT supplement fingerprint differs")
    with ZipFile(path) as archive:
        document = ET.fromstring(archive.read("word/document.xml"))
    table, = (table for table in document.findall(".//" + NS + "tbl") if len(table.findall(NS + "tr")) > 20)
    groups = defaultdict(list)
    for row in table.findall(NS + "tr"):
        cells = ["".join(node.text or "" for node in cell.iter(NS + "t")).strip()
                 for cell in row.findall(NS + "tc")]
        if len(cells) == 18 and cells[12] in {"1500mg", "PLACEBO"}:
            label = "nicotinamide" if cells[12] == "1500mg" else "placebo"
            groups[label].append(cells)
    if {label: len(rows) for label, rows in groups.items()} != {"nicotinamide": 24, "placebo": 23}:
        raise ValueError("Unexpected supplemental table group labels or row counts")
    return groups


def values_at(rows, column):
    return [Decimal(row[column]) for row in rows if row[column]]


def report(groups):
    print("group\tendpoint\tn_available\tvalue\tunit")
    for group, rows in groups.items():
        for name, column in (("plasma NAM", 3), ("CSF NAM", 5), ("plasma MNA", 8), ("CSF MNA", 10)):
            values = values_at(rows, column)
            print(f"{group}\t12 month {name} mean as tabulated\t{len(values)}\t{mean(values):.3f}\tµM")
            print(f"{group}\t12 month {name} maximum as tabulated\t{len(values)}\t{max(values):.3f}\tµM")
        csf = values_at(rows, 5)
        elevated = [v for v in csf if v > ELEVATED]
        print(f"{group}\t12 month CSF NAM above 2.1 µM\t{len(csf)}\t{len(elevated)}\tcount")
        if elevated:
            print(f"{group}\t12 month CSF NAM elevated-only mean\t{len(elevated)}\t{mean(elevated):.3f}\tµM")
        paired = sum(bool(row[4] and row[5]) for row in rows)
        print(f"{group}\tCSF NAM with baseline and 12 month values\t{len(rows)}\t{paired}\tcount")
        for floor_substitute in (Decimal(0), NAM_LOQ / 2, NAM_LOQ):
            lower = mean(floor_substitute if value == NAM_LOQ else value for value in csf)
            print(f"{group}\t12 month CSF NAM mean with floor {floor_substitute} µM\t{len(csf)}\t{lower:.3f}\tµM")
        if group == "nicotinamide":
            print(f"{group}\tfirst tested neuronal bath / all available CSF mean\t{len(csf)}\t{Decimal(2500) / mean(csf):.2f}\tfold")
            print(f"{group}\tfirst tested neuronal bath / elevated subgroup CSF mean\t{len(elevated)}\t{Decimal(2500) / mean(elevated):.2f}\tfold")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("supplement", type=Path)
    report(read_groups(parser.parse_args().supplement))
