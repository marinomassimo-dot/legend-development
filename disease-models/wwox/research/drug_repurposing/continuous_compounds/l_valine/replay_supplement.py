"""Recompute exposure, comparisons and denominator effects from Eller DataSheet1."""
import argparse
import csv
import hashlib
from math import log, sqrt
from pathlib import Path
import re
import sys
from xml.etree import ElementTree as ET
from zipfile import ZipFile


EXPECTED_DIGEST = "495a67513191a6e043273ec3e405db7e7640e9b1450bcf29853f7455e94f9b83"
WORD = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
ARM_LABELS = ("WT_control", "ECHS1D_control", "WT_intervention", "ECHS1D_intervention")


def cell_text(cell):
    return " ".join(" ".join(node.text or "" for node in cell.findall(".//w:t", WORD)).split())


def read_tables(source):
    if hashlib.sha256(source.read_bytes()).hexdigest() != EXPECTED_DIGEST:
        raise ValueError("The supplement digest does not match the archived study file.")
    with ZipFile(source) as archive:
        document = ET.fromstring(archive.read("word/document.xml"))
    return [
        [[cell_text(c) for c in row.findall("w:tc", WORD)] for row in table.findall("w:tr", WORD)]
        for table in document.findall("./w:body/w:tbl", WORD)
    ]


def measured_brain(out, section, rows):
    data = {}
    for row in rows[1:]:
        name, *columns = row
        if name not in ("Val", "Leu", "Ile", "Ala", "Lys", "Pro"):
            continue
        values = [tuple(map(float, re.findall(r"\d+(?:\.\d+)?", cell))) for cell in columns[:4]]
        data[name] = values
        for arm, (mean, sem) in zip(ARM_LABELS, values):
            out.writerow((section, name, arm, f"{mean:.1f}", "nmol/g", f"SEM={sem:.1f}"))
        control_wt, control_mutant, changed_wt, changed_mutant = [mean for mean, _ in values]
        wt_delta = changed_wt - control_wt
        mutant_delta = changed_mutant - control_mutant
        for arm, delta, control in (("WT", wt_delta, control_wt), ("ECHS1D", mutant_delta, control_mutant)):
            out.writerow((section, name, f"{arm}_change", f"{delta:.1f}", "nmol/g",
                          f"{100 * delta / control:+.1f}% of control"))
        uncertainty = sqrt(sum(sem**2 for _, sem in values))
        out.writerow((section, name, "interaction", f"{mutant_delta - wt_delta:.1f}", "nmol/g",
                     f"illustrative independent-arm SEM={uncertainty:.1f}"))

    for arm, control, changed in (("WT", 0, 2), ("ECHS1D", 1, 3)):
        ala_control, ala_changed = (data["Ala"][position][0] for position in (control, changed))
        lys_control, lys_changed = (data["Lys"][position][0] for position in (control, changed))
        ala_fold, lys_fold = ala_changed / ala_control, lys_changed / lys_control
        out.writerow((section, "Ala/Lys", f"{arm}_diet_ratio_of_arm_means", f"{ala_fold / lys_fold:.3f}",
                      "fold", f"Ala multiplier={ala_fold:.3f}; Lys multiplier={lys_fold:.3f}"))
        for name, term in (("Ala", log(ala_fold)), ("Lys", -log(lys_fold))):
            out.writerow((section, "Ala/Lys", f"{arm}_{name}_log_component", f"{term:+.4f}",
                          "natural_log_units", "signed log-ratio decomposition from arm means"))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("supplement", type=Path)
    args = parser.parse_args()
    tables = read_tables(args.supplement)
    out = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    out.writerow(("source", "measure", "contrast", "value", "unit", "basis"))
    diet = next(row for row in tables[0] if "Aspartic Acid Glutamic Acid" in row[0])
    for name, index in (("Leu", 7), ("Ile", 8), ("Val", 9), ("Lys", 14)):
        for label, column in zip(("standard", "supplemented", "AA_control", "restricted"), diet[1:]):
            out.writerow(("Table S1", name, label, column.split()[index], "g/kg_diet",
                          "aligned ordered amino acid row"))

    measured_brain(out, "Table S2", tables[1])
    measured_brain(out, "Table S3", tables[2])
    for table_number, names in ((5, ("SCPC", "SCEC")), (7, ("Alanine:Lysine", "NAD:NADH", "Energy charge")),
                                (9, ("SCPC", "SCEC")), (11, ("Energy charge",))):
        for row in tables[table_number - 1][1:]:
            if row[0] in names and row[1] == "Interaction":
                out.writerow((f"Table S{table_number}", row[0], "model_genotype_by_diet", row[3],
                              "p_reported", "published omnibus interaction term"))


if __name__ == "__main__":
    main()
