"""Map author-reported fetal deglycopeptides to nominated canonical N-sites."""

import argparse
from collections import defaultdict
import csv
from pathlib import Path
import re
import sys
from xml.etree import ElementTree as ET
from zipfile import ZipFile


SITES = {
    "L1CAM": ("P32004", (288, 668, 723, 977)),
    "PLXNB2": ("O15031", (124, 844, 1084)),
    "SV2A": ("Q7L0J3", (498, 573)),
}


def exact_peptides(workbook):
    """Read the author-annotated peptide sequences from Supplementary Table S1f."""
    peptides = defaultdict(set)
    with ZipFile(workbook) as archive:
        strings = [
            "".join(node.text or "" for node in entry.iterfind(".//{*}t"))
            for entry in ET.fromstring(archive.read("xl/sharedStrings.xml"))
        ]
        with archive.open("xl/worksheets/sheet6.xml") as sheet:
            for _, row in ET.iterparse(sheet, events=("end",)):
                if not row.tag.endswith("}row"):
                    continue
                cells = {}
                for cell in row:
                    column = cell.attrib["r"].rstrip("0123456789")
                    if column in {"A", "C"} and cell.get("t") == "s":
                        cells[column] = strings[int(cell.findtext("{*}v"))]
                accession = cells.get("A")
                if accession in {value[0] for value in SITES.values()}:
                    match = re.fullmatch(r"\[[^\]]+\]\.([A-Z]+)\.\[[^\]]+\]", cells.get("C", ""))
                    if match:
                        sequence = match[1]
                        peptides[accession, f"{sequence[:4]}_{len(sequence)}"].add(sequence)
                row.clear()
    return peptides


def canonical_sites(row, sequence, peptides):
    peptide_id = row["Peptide_ID"]
    glyco_id = row["Glyco_unique_ID"]
    marker = row["Gene_symbol"] + "_" + peptide_id + "_"
    if not glyco_id.startswith(marker):
        return ()
    suffix = glyco_id[len(marker):]
    if not re.fullmatch(r"N\d+(?:_N\d+)*", suffix):
        return ()
    matches = peptides[row["Accession"], peptide_id]
    if len(matches) != 1:
        return ()
    peptide, = matches
    starts = [match.start() for match in re.finditer(f"(?={peptide})", sequence)]
    if len(starts) != 1:
        return ()
    offsets = [int(part[1:]) for part in suffix.split("_")]
    if any(offset < 1 or offset > len(peptide) for offset in offsets):
        return ()
    positions = [starts[0] + offset for offset in offsets]
    if any(not re.fullmatch(r"N[^P][ST]", sequence[pos - 1:pos + 2]) for pos in positions):
        return ()
    return positions


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source_dir", type=Path)
    args = parser.parse_args()
    sequences = {}
    for gene, (accession, _) in SITES.items():
        fasta = (args.source_dir / (accession + ".fasta")).read_text().splitlines()
        assert fasta[0].split("|")[1] == accession
        sequences[gene] = "".join(fasta[1:])

    peptides = exact_peptides(args.source_dir / "PXD065788_S1.xlsx")
    regions = defaultdict(lambda: defaultdict(set))
    with (args.source_dir / "PXD065788_S2.csv").open(newline="", encoding="utf-8") as source:
        for row in csv.DictReader(source):
            gene = row["Gene_symbol"]
            if gene not in SITES or row["Accession"] != SITES[gene][0]:
                continue
            if row["Glycosylated"] != "Yes" or row["Glyco_abundance"] in {"", "NA"}:
                continue
            if float(row["Glyco_abundance"]) <= 0:
                continue
            for position in canonical_sites(row, sequences[gene], peptides):
                if position in SITES[gene][1]:
                    regions[gene, position][row["Glyco_unique_ID"]].add(row["Region"])

    writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    writer.writerow(("gene", "canonical_accession", "reported_position", "canonical_triplet",
                     "Glyco_unique_ID", "full_author_peptide", "regions_detected"))
    for gene, (accession, positions) in SITES.items():
        for position in positions:
            hits = regions[gene, position]
            triplet = sequences[gene][position - 1:position + 2]
            if hits:
                for glyco_id, region_set in sorted(hits.items()):
                    cluster = "_".join(glyco_id.split("_")[1:3])
                    peptide, = peptides[accession, cluster]
                    writer.writerow((gene, accession, position, triplet, glyco_id, peptide, len(region_set)))
            else:
                writer.writerow((gene, accession, position, triplet, "", "", 0))


if __name__ == "__main__":
    main()
