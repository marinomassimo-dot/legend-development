"""Reproduce the published-source comparisons for clemizole and the held WWOX panel."""

import argparse
from io import BytesIO
from math import exp, log, sqrt
from pathlib import Path
from statistics import mean, stdev
import sys
from xml.etree import ElementTree as ET
from zipfile import ZipFile

COMPOUNDS = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(COMPOUNDS / "sodium_benzoate"), str(COMPOUNDS / "jbpos0101")]
from coagonist_screen import bulk_panel, tsv
from replay_exposure_and_receptors import verified, verified_expression

FIGURE_HASH = "a59f98cbb43e9f0ae2879edc074a15771cbf234f9050add75dbc1dc0b8d34773"
PANEL = ("Htr2a", "Htr2b", "Htr2c", "Hrh1", "Trpc1", "Trpc4", "Trpc5", "Kcnh2", "Tph2", "Slc6a4", "Slc18a2")
ADULT_UNBOUND_PEAK_UM = 0.01  # Approximate, from the EPX-100 EILAT XVIII section.


def trpc5_rows(source):
    with ZipFile(BytesIO(verified(source, FIGURE_HASH))) as workbook:
        worksheet = ET.fromstring(workbook.read("xl/worksheets/sheet1.xml"))
    cells = {cell.attrib["r"]: cell.find("{*}v").text for cell in worksheet.findall(".//{*}c")
             if cell.find("{*}v") is not None}
    for row in range(3, 13):
        concentration, *results = (float(cells[f"{column}{row}"]) for column in "ABCD")
        yield concentration, len(results), mean(results), stdev(results) / sqrt(len(results))


def midpoint_rows(assay_rows):
    # Observable is a 50% normalized response, which need not equal a 4PL midpoint.
    left, right = next((a, b) for a, b in zip(assay_rows, assay_rows[1:]) if a[2] >= 50 > b[2])
    weight = (left[2] - 50) / (left[2] - right[2])
    yield "Song_Fig1_log_interpolation", left[0], left[2], right[0], right[2], exp(log(left[0]) + weight * log(right[0] / left[0]))


def exposure_rows():
    references = (
        ("hERG_WT_Jie_2017", 0.07, "functional_IC50", "cardiac"),
        ("TRPC5_Richter_low", 1.0, "functional_IC50", "neural"),
        ("TRPC5_Richter_high", 1.3, "functional_IC50", "neural"),
        ("hTRPC5_Song_WT", 3.07, "functional_IC50", "neural"),
        ("hTRPC5_Song_N443L", 10.43, "functional_IC50", "construct_control"),
        ("HTR2A_B_C_Griffin_parent", None, "functional_EC50_unavailable", "neural"),
    )
    for assay, midpoint, endpoint, compartment in references:
        for factor in ((0.1, 1.0, 10.0) if compartment == "neural" else (1.0,)):
            local = ADULT_UNBOUND_PEAK_UM * factor
            yield assay, endpoint, compartment, local, factor, midpoint, midpoint / local if midpoint else None


def formatted(rows):
    for row in rows:
        yield tuple(f"{value:.7g}" if isinstance(value, float) else "NA" if value in ("", None) else value
                    for value in row)


def main(files, out):
    source = files / "deepening_downloads/clemizole_20261127/Song_2021_Fig1.xlsx"
    assay_rows = list(trpc5_rows(source))
    out.mkdir(parents=True, exist_ok=True)
    tsv(out / "trpc5_source_curve.tsv", "nominal_uM n normalized_response_mean normalized_response_SEM".split(),
        formatted(assay_rows))
    tsv(out / "trpc5_midpoint_check.tsv", "calculation lower_uM lower_response upper_uM upper_response interpolated_uM".split(),
        formatted(midpoint_rows(assay_rows)))
    tsv(out / "exposure_comparison.tsv", "assay endpoint compartment assumed_local_unbound_uM multiple_of_adult_unbound_peak assay_midpoint_uM midpoint_over_local".split(),
        formatted(exposure_rows()))
    verified_expression(files)
    tsv(out / "wwox_receptor_context.tsv",
        "model accession gene ctrl_n ko_n ctrl_positive ko_positive ctrl_mean ko_mean log2_delta omit_min omit_max mapping".split(),
        formatted(bulk_panel(files, PANEL)))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", type=Path)
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parent)
    options = parser.parse_args()
    main(options.files, options.output)
