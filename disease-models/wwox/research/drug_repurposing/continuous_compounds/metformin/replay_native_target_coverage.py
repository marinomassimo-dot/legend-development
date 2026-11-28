"""Replay stage-specific protein coverage without equating missing signal with absence."""

import argparse
import csv
from hashlib import sha256
from io import BytesIO
from pathlib import Path
import sys
from xml.etree import ElementTree as ET
from zipfile import ZipFile

P14_ZIP_DIGEST = "01078a3341d31250f99b89952ff80c210b20d4dc6855a7a3809a06b57a016abe"
PHOSPHO_DIGEST = "b1238e90321da779f7abd48157a8b9da2e1e5ec0c5ca9dc184c709efd720d24f"
NS = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
REL_ID = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id"
PROTEINS = ("PRKAA1", "PRKAA2", "PRKAB1", "PRKAB2", "PSENEN", "ATP6AP1", "ACACA", "ACACB")

# Canonical mouse accession coordinates. The literature also uses ACC2 Ser212
# numbering, so the exact-accession screen cannot exclude every isoform match.
SITES = (
    ("ACACA", "Q5SWU9", "S", "79"),
    ("ACACB", "E9Q4Z2", "S", "222"),
    ("PRKAA1", "Q5EG47", "T", "183"),
    ("PRKAA2", "Q8BRK8", "T", "172"),
)


def checked_bytes(path, digest):
    value = path.read_bytes()
    if sha256(value).hexdigest() != digest:
        raise ValueError(f"Unexpected source fingerprint for {path.name}")
    return value


def worksheet_rows(archive, name):
    book = ET.fromstring(archive.read("xl/workbook.xml"))
    sheet = next(s for s in book.iter(NS + "sheet") if s.get("name") == name)
    relationships = ET.fromstring(archive.read("xl/_rels/workbook.xml.rels"))
    entry = next(r.get("Target") for r in relationships if r.get("Id") == sheet.get(REL_ID))
    strings = ["".join(node.itertext()) for node in ET.fromstring(archive.read("xl/sharedStrings.xml"))]
    with archive.open("xl/" + entry) as stream:
        for event, element in ET.iterparse(stream, events=("start", "end")):
            if event == "start" and element.tag == NS + "sheetData":
                sheet_data = element
            if event != "end" or element.tag != NS + "row":
                continue
            values = {}
            for cell in element:
                value = cell.findtext(NS + "v")
                if value is not None:
                    column = cell.get("r").rstrip("0123456789")
                    values[column] = strings[int(value)] if cell.get("t") == "s" else value
            yield int(element.get("r")), values
            sheet_data.remove(element)


def p14_coverage(path):
    with ZipFile(BytesIO(checked_bytes(path, P14_ZIP_DIGEST))) as archive:
        with ZipFile(BytesIO(archive.read("sciadv.abo7639_table_s1.xlsx"))) as workbook:
            rows = worksheet_rows(workbook, "02_ANOME_P14")
            _, header = next(rows)
            columns = [col for col, label in header.items() if label.startswith("O_P14.")]
            if len(columns) != 8:
                raise ValueError("Unexpected number of O4+ acquisition columns")
            targets = {}
            for index, row in rows:
                symbol = row.get("A", "").upper()
                if symbol in PROTEINS:
                    if symbol in targets:
                        raise ValueError(f"Ambiguous protein row for {symbol}")
                    targets[symbol] = index, row
    for symbol in PROTEINS:
        index, row = targets.get(symbol, ("NA", {}))
        covered = sum(row.get(col) not in {None, "NA", "NaN", "0"} for col in columns)
        yield "Düking P14 O4+", symbol, row.get("B", "NA"), index, "quantified injections", covered, "of 8"


def phosphosite_coverage(path):
    stages = {
        "K": "day 7 / 0 raw Rep01", "N": "day 7 / 0 raw Rep02",
        "L": "day 14 / 0 raw Rep01", "O": "day 14 / 0 raw Rep02",
        "W": "day 7 / 0 protein corrected Rep01", "X": "day 7 / 0 protein corrected Rep02",
        "Y": "day 14 / 0 protein corrected Rep01", "Z": "day 14 / 0 protein corrected Rep02",
    }
    sites = {site: [] for site in SITES}
    with ZipFile(BytesIO(checked_bytes(path, PHOSPHO_DIGEST))) as archive:
        rows = worksheet_rows(archive, "01_ClassI-sites_exp_quantified")
        next(rows)
        for index, row in rows:
            if row.get("F", "").upper() not in PROTEINS:
                continue
            # Check accession and position pairs as published for all matching isoforms.
            mapped = set(zip(row["A"].split(";"), row["B"].split(";"), strict=True))
            for site in sites:
                symbol, protein, residue, position = site
                if row["F"].upper() == symbol and row["G"] == residue and (protein, position) in mapped:
                    sites[site].append((index, row))
    for (symbol, protein, residue, position), results in sites.items():
        label = f"{symbol} {residue}{position}"
        if not results:
            yield "Oligosphere phosphoproteome", label, protein, "NA", "exact mapped row", 0, "rows"
        for index, row in results:
            yield "Oligosphere phosphoproteome", label, protein, index, "localization probability", row["J"], "fraction"
            for col, stage in stages.items():
                yield "Oligosphere phosphoproteome", label, protein, index, stage, row[col], "log2 ratio"


def reference_contrasts():
    # Dimas Fig. 3—figure supplement 2b/g; both groups relative to all counted axons.
    for day, control, mutant in (("P14", 75.68, 84.08), ("P180", 4.29, 21.16)):
        yield "Dimas optic nerve", "FASN conditional loss", "NA", day, "unwrapped mutant minus control", f"{mutant - control:.2f}", "percentage points"
    # Hale, pp. 1511–1512, assay detection limit and two detected infant plasma values.
    for measure, mg_per_liter in (("detection limit", 0.01), ("low detected", 0.05), ("high detected", 0.08)):
        yield "Hale infant plasma", "metformin", "NA", "pp. 1511–1512", measure, f"{mg_per_liter * 1000 / 129.16:.4f}", "µM parent equivalent"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("p14_archive", type=Path)
    parser.add_argument("phosphoproteome", type=Path)
    args = parser.parse_args()
    writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    writer.writerow(("source", "target", "accession", "row", "measure", "value", "unit"))
    writer.writerows(p14_coverage(args.p14_archive))
    writer.writerows(phosphosite_coverage(args.phosphoproteome))
    writer.writerows(reference_contrasts())


if __name__ == "__main__":
    main()
