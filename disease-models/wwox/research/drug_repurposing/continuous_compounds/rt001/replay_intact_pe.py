"""Replay developmental PE denominators and an ideal nominal isotope recapture."""

import argparse
import csv
from hashlib import sha256
from itertools import product
from pathlib import Path
from statistics import mean
import sys
import xml.etree.ElementTree as ET
from zipfile import ZipFile


WORKBOOK_HASH = "45e34a4ae94f0be63be211cb9ec0fdedeaefd010933bc4ecfb9565af4b47b1d6"
SPREADSHEET = {"a": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
TARGETS = ("PE 18:0-18:2", "PE 18:0-20:4", "PE O-18:1/18:2", "PE O-18:1/20:4", "PE O-16:1/20:4")
STAGES = ("E15.5_hemisphere", "P2_hemisphere", "P21_hemisphere", "P21_rest")

# Nominal isotope steps starting at each element's lightest stable isotope.
NOMINAL_ABUNDANCE = {
    "C": (0.9893, 0.0107, 0.0),
    "H": (0.999885, 0.000115, 0.0),
    "N": (0.99636, 0.00364, 0.0),
    "O": (0.99757, 0.00038, 0.00205),
    "P": (1.0, 0.0, 0.0),
}
IONS = {
    "intact_pe_18_0_20_4_plus_o2": {"C": 43, "H": 77, "N": 1, "O": 10, "P": 1},
    "oxidized_arachidonate_fragment_plus_o2": {"C": 20, "H": 31, "O": 4},
}
SCENARIOS = {
    "blank": (1.00, 0.00, 0.00),
    "low": (0.99, 0.002, 0.008),
    "moderate": (0.95, 0.01, 0.04),
    "equal_d1_d2": (0.85, 0.075, 0.075),
}


def sheet_cells(row, strings):
    for cell in row.findall("a:c", SPREADSHEET):
        value = cell.findtext("a:v", namespaces=SPREADSHEET)
        if value is not None:
            column = cell.attrib["r"].rstrip("0123456789")
            yield column, strings[int(value)] if cell.get("t") == "s" else value


def developmental_rows(workbook):
    if sha256(workbook.read_bytes()).hexdigest() != WORKBOOK_HASH:
        raise ValueError("Source workbook does not match its pinned SHA-256")
    with ZipFile(workbook) as source:
        strings = ["".join(item.itertext()) for item in ET.fromstring(source.read("xl/sharedStrings.xml"))]
        sheet = ET.fromstring(source.read("xl/worksheets/sheet1.xml"))
    rows = sheet.findall("a:sheetData/a:row", SPREADSHEET)
    samples = dict(sheet_cells(rows[1], strings))
    yield ("species_as_reported", "workbook_row", "stage", "observed", "expected", "mean_mol_percent",
           "min_mol_percent", "max_mol_percent", "p21_over_p2", "ratio_omit_one_min", "ratio_omit_one_max")
    for row in rows[2:]:
        cells = dict(sheet_cells(row, strings))
        if cells.get("A") not in TARGETS:
            continue
        cohorts = {stage: [float(cells[c]) for c, sample in samples.items()
                           if sample.startswith(stage + "_") and c in cells] for stage in STAGES}
        p2, p21 = cohorts["P2_hemisphere"], cohorts["P21_hemisphere"]
        leave_one = [mean(p21[:i] + p21[i + 1:]) / mean(p2) for i in range(len(p21))]
        leave_one += [mean(p21) / mean(p2[:i] + p2[i + 1:]) for i in range(len(p2))]
        for stage, observed in cohorts.items():
            expected = sum(sample.startswith(stage + "_") for sample in samples.values())
            ratios = [mean(p21) / mean(p2), min(leave_one), max(leave_one)] if stage == "P21_hemisphere" else []
            yield (cells["A"], row.attrib["r"], stage, len(observed), expected,
                   *(f"{v:.6f}" for v in (mean(observed), min(observed), max(observed))),
                   *(f"{v:.6f}" for v in ratios), *(["NA"] * (3 - len(ratios))))


def natural_envelope(formula, locked_deuteriums):
    envelope = [1.0, 0.0, 0.0]
    for element, count in formula.items():
        abundance = NOMINAL_ABUNDANCE[element]
        natural_count = count - locked_deuteriums if element == "H" else count
        for _ in range(natural_count):
            envelope = [sum(envelope[i - k] * abundance[k] for k in range(i + 1)) for i in range(3)]
    return envelope


def forward(envelopes, amounts):
    return [sum(amounts[d] * envelopes[d][i - d] for d in range(i + 1)) for i in range(3)]


def inverse(envelopes, measured):
    amounts = []
    for i, peak in enumerate(measured):
        tail = sum(value * envelopes[d][i - d] for d, value in enumerate(amounts))
        amounts.append((peak - tail) / envelopes[i][0])
    return [value / sum(amounts) for value in amounts]


def isotope_rows():
    yield ("ion", "readout", "scenario", "true_d1", "true_d2", "uncorrected_m1", "uncorrected_m2",
           "corrected_d1", "corrected_d2", "d1_min", "d1_max", "d2_min", "d2_max")
    for ion, formula in IONS.items():
        # In a matched precursor→fragment nominal transition, natural heavy atoms
        # in the neutral loss are excluded. The monoisotopic loss factor cancels.
        envelopes = [natural_envelope(formula, d) for d in range(3)]
        for scenario, truth in SCENARIOS.items():
            measured = forward(envelopes, truth)
            ideal = inverse(envelopes, measured)
            assert all(abs(real - recovered) < 1e-12 for real, recovered in zip(truth, ideal))
            errors = [inverse(envelopes, [value * multiplier for value, multiplier in zip(measured, factors)])
                      for factors in product((0.99, 1.01), repeat=3)]
            minima = [min(case[d] for case in errors) for d in (1, 2)]
            maxima = [max(case[d] for case in errors) for d in (1, 2)]
            normalized = [value / sum(measured) for value in measured]
            readout = "nominal_parent" if ion.startswith("intact") else "matched_nominal_parent_to_fragment"
            yield (ion, readout, scenario, *(f"{v:.6f}" for v in (*truth[1:], *normalized[1:],
                                                                *ideal[1:], minima[0], maxima[0], minima[1], maxima[1])))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workbook", type=Path, help="Emit developmental rows from Schmidt Supplemental Data 1")
    args = parser.parse_args()
    rows = developmental_rows(args.workbook) if args.workbook else isotope_rows()
    csv.writer(sys.stdout, delimiter="\t", lineterminator="\n").writerows(rows)


if __name__ == "__main__":
    main()
