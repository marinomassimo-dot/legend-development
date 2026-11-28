"""Extract matched Barski Table 1 constants and an HNE buffer sensitivity bound."""
import argparse
import re
from pathlib import Path
from xml.etree import ElementTree


def text(node):
    return " ".join("".join(node.itertext()).split())


def table_constants(path):
    root = ElementTree.parse(path).getroot()
    table = root.find(".//table-wrap[@id='T1']")
    if table is None or "Bimolecular rate constants" not in text(table.find("caption")):
        raise ValueError("Expected Barski et al. Table 1")
    rows = {}
    for row in table.findall(".//tbody/tr"):
        cells = [text(cell) for cell in row.findall("td")]
        if cells and cells[0] in {"4-HNE", "Acrolein"}:
            rows[cells[0]] = [float(cell.split("±")[0]) for cell in cells[1:3]]
    note = text(table.find("table-wrap-foot"))
    reverse = re.search(r"reverse rate constant of ([0-9.]+)×10−([0-9]+)", note)
    if set(rows) != {"4-HNE", "Acrolein"} or reverse is None:
        raise ValueError("Expected two analytes and the reverse-rate annotation")
    return rows, float(reverse[1]) * 10 ** -int(reverse[2])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("article_xml", type=Path)
    args = parser.parse_args()
    rows, reverse = table_constants(args.article_xml)
    print("observable\tcondition\tvalue\tunit")
    for analyte, (carnosine, anserine) in rows.items():
        print(f"forward_rate_ratio\t{analyte} anserine/carnosine\t{anserine / carnosine:.4f}\tratio")
    kd = reverse / rows["4-HNE"][1]
    print(f"dissociation_constant\t4-HNE anserine\t{kd * 1000:.4f}\tmM")
    for parent in (1, 10, 100, 1000):
        parent_molar = parent * 1e-6
        fraction = parent_molar / (parent_molar + kd)
        print(f"equilibrium_fraction\t4-HNE fixed anserine {parent} uM\t{fraction:.6f}\tfraction")


if __name__ == "__main__":
    main()
