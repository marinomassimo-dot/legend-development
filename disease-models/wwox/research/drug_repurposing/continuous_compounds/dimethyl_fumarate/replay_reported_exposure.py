"""Convert published MMF mass concentrations without imputing a paired PK ratio."""

from decimal import Decimal
import argparse
import csv
import json
from pathlib import Path
import sys


def exposure_rows(property_file):
    properties = json.loads(property_file.read_text())["PropertyTable"]["Properties"]
    compound, = properties
    if compound["CID"] != 5369209:
        raise ValueError("Expected monomethyl fumarate")
    molar_mass = Decimal(compound["MolecularWeight"])
    mean_plasma_peak = Decimal(1750)

    rows = (
        ("7 h CSF reported lower", Decimal(39)),
        ("7 h CSF reported upper", Decimal(79)),
        ("plasma mean Cmax", mean_plasma_peak),
    )
    for label, concentration in rows:
        yield "Edwards ACTRIMS P006", label, f"{concentration / molar_mass:.4f}", "µM", f"{concentration} ng/mL"
    for label, concentration in rows[:2]:
        yield "Edwards ACTRIMS P006", label + " / plasma mean Cmax", f"{100 * concentration / mean_plasma_peak:.2f}", "%", "different times and statistics"
        yield "Gola publisher preview and Edwards P006", "nominal proteomics bath / " + label, f"{Decimal(50) * molar_mass / concentration:.1f}", "fold", "50 µM MMF nominal bath for 48 h"
    gi_difference = 100 * (Decimal(58) / 78 - Decimal(22) / 72)
    yield "CONNECT Table 3", "GI event risk difference", f"{gi_difference:+.2f}", "pp", "58/78 DMF vs 22/72 interferon beta-1a"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pubchem_json", type=Path)
    args = parser.parse_args()
    writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    writer.writerow(("source", "measure", "value", "unit", "context"))
    writer.writerows(exposure_rows(args.pubchem_json))


if __name__ == "__main__":
    main()
