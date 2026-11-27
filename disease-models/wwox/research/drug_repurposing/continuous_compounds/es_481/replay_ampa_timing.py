"""Reconcile aggregate ES-481 trial results, receptor assays and held WWOX data."""

import argparse
from io import BytesIO
from math import exp
from pathlib import Path
from statistics import mean
import sys
from xml.etree import ElementTree as ET
from zipfile import ZipFile

COMPOUNDS = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(COMPOUNDS / "sodium_benzoate"), str(COMPOUNDS / "jbpos0101")]
from coagonist_screen import bulk_panel, nuclei_panel, tsv
from replay_exposure_and_receptors import verified, verified_expression

WORKBOOK_HASH = "684c72e2a387ae3aa6a451152ba58068bb7437c6d43495024dd468ba0b451431"
CIF_HASH = "dfda2bd2655314865d3bd75fa9a32b61dcf096626c556fb655613715a2b516cf"
PANEL = ("Cacng2", "Cacng3", "Cacng4", "Cacng5", "Cacng7", "Cacng8", "Cnih2", "Cnih3",
         "Gsg1l", "Gria1", "Gria2", "Gria3", "Gria4", "Dlg4")


def worksheet_data(path):
    with ZipFile(BytesIO(verified(path, WORKBOOK_HASH))) as workbook:
        shared = ["".join(n.itertext()) for n in ET.fromstring(workbook.read("xl/sharedStrings.xml")).findall("{*}si")]
        for sheet in (1, 3, 4, 7):
            root = ET.fromstring(workbook.read(f"xl/worksheets/sheet{sheet}.xml"))
            values = {}
            for cell in root.findall(".//{*}c"):
                v = cell.findtext("{*}v")
                if v is not None:
                    values[cell.get("r")] = shared[int(v)] if cell.get("t") == "s" else float(v)
            yield sheet, values


def timing_rows(sheets):
    comparisons = (
        (4, "S6A", "GluA1i_gamma8", "peak_fraction", None, "C", 5, 11, "C21"),
        (4, "S6B", "GluA1i_gamma8", "equilibrium_percent", "N", "O", 29, 35, "O43"),
        (4, "S6A", "GluA1i_gamma8", "resensitization_percent", "I", "J", 5, 11, "J21"),
        (1, "4B", "GluA1i_gamma8", "desensitization_ms", "N", "O", 5, 11, "O18"),
        (7, "S9B", "GluA2iQ_gamma8", "peak_fraction", None, "D", 60, 68, "D74"),
        (7, "S9B", "GluA2iQ_gamma8", "equilibrium_percent", "J", "K", 60, 68, "K74"),
        (7, "S9B", "GluA2iQ_gamma8", "resensitization_percent", "R", "S", 60, 68, "S74"),
        (3, "6B", "GluA2iQ_gamma8", "desensitization_ms", "AF", "AG", 4, 12, "AG16"),
    )
    for sheet, panel, construct, endpoint, from_col, to_col, start, end, p_cell in comparisons:
        cells = sheets[sheet]
        rows = range(start, end + 1)
        pre = [cells[f"{from_col}{r}"] for r in rows] if from_col else [1.0 for r in rows]
        drug = [cells[f"{to_col}{r}"] for r in rows]
        yield ("Zhang", panel, construct, endpoint, len(drug), mean(pre), mean(drug),
               mean(drug) / mean(pre), cells[p_cell])
    for panel, endpoint, n, pre, drug, p in (
        ("7B2", "peak_fraction", 9, 1.0, 0.936, 0.0004),
        ("7C3", "equilibrium_percent", 20, 16.96, 8.35, "<0.0001"),
        ("7C2", "resensitization_percent", 20, 8.31, 0.38, "<0.0001"),
        ("7D", "desensitization_ms", 20, 26.50, 30.88, 0.0002),
    ):
        yield "Dohrke", panel, "GluA2_gamma8", endpoint, n, pre, drug, drug / pre, p


def clinical_rows():
    comparisons = (
        ("overall", -1.35, -0.86, -0.49, 0.32, 1.15, 0.097),
        ("week_1", -1.15, -0.48, -0.68, 0.21, 1.24, 0.104),
        ("week_2", -1.29, -1.10, -0.19, 0.23, 3.00, 0.402),
        ("week_3", -1.34, -1.18, -0.16, 0.36, 2.01, 0.376),
        ("week_4", -1.62, -0.68, -0.94, 0.16, 0.98, 0.047),
    )
    for period, es, placebo, log_diff, low, high, p in comparisons:
        yield period, 100 * (1 - exp(es)), 100 * (1 - exp(placebo)), exp(log_diff), low, high, p, min(1, 2 * p)


def exposure_rows():
    # Total parent summaries are kept separate. Binding is a programme estimate.
    peaks = (("first_reported_peak", 362.633), ("intermediate_reported_peak", 543.355),
             ("late_reported_peak", 1190.312), ("separate_reported_high_mean_Cmax", 1317.042))
    benchmarks = (("mouse_WT_hippocampus", 27), ("rat_hippocampus", 66), ("mouse_WT_cortex", 83),
                  ("rat_cortex", 93), ("human_membranes_in_oocyte_with_CTZ", 114),
                  ("Zhang_Dohrke_nominal_test", 10000))
    for period, mass_concentration in peaks:
        total = mass_concentration * 1000 / 382.436  # OLR, 8AYN chemical component.
        for free_fraction in (0.01, 0.02, 0.03):
            free = total * free_fraction
            for assay, nominal in benchmarks:
                yield period, mass_concentration, total, free_fraction, free, assay, nominal, nominal / free


def ligand_rows(cif):
    block = cif.split("_pdbx_nonpoly_scheme.pdb_ins_code", 1)[1].split("#", 1)[0]
    for row in block.splitlines():
        fields = row.split()
        if len(fields) == 10 and fields[2] == "OLR":
            yield "8AYN", fields[0], fields[2], fields[4], fields[5], fields[8]


def formatted(rows):
    for row in rows:
        yield tuple(f"{v:.7g}" if isinstance(v, float) else "NA" if v in ("", None) else v for v in row)


def main(files, output):
    evidence = files / "deepening_downloads/es_481_20261127"
    sheets = dict(worksheet_data(evidence / "Zhang_2023_SourceData.xlsx"))
    ligands = list(ligand_rows(verified(evidence / "8AYN.cif", CIF_HASH).decode()))
    assert len(ligands) == 2
    verified_expression(files)
    output.mkdir(parents=True, exist_ok=True)
    tables = (
        ("ampa_components.tsv", "study panel construct endpoint n control drug drug_over_control published_p", timing_rows(sheets)),
        ("adult_diary_replay.tsv", "period active_improvement_pct placebo_improvement_pct ratio_of_ratios CI90_low CI90_high p_one_sided p_two_sided_if_symmetric", clinical_rows()),
        ("adult_exposure_scenarios.tsv", "adult_observation total_ng_mL total_nM assumed_plasma_fu calculated_free_plasma_nM comparison nominal_nM Kp_uu_required_to_equal_nominal", exposure_rows()),
        ("structure_ligands.tsv", "pdb label_asym component pdb_position author_position author_chain", ligands),
        ("wwox_ampa_context.tsv", "model accession gene ctrl_n ko_n ctrl_positive ko_positive ctrl_mean ko_mean log2_delta omit_min omit_max mapping", bulk_panel(files, PANEL)),
        ("wwox_ampa_nuclei.tsv", "pool cell_class gene nuclei all_UMI gene_UMI CPM", nuclei_panel(files, ("Cacng2", "Cacng4", "Cacng8", "Cnih2", "Cnih3", "Gsg1l", "Gria1", "Gria2"))),
    )
    for name, header, rows in tables:
        tsv(output / name, header.split(), formatted(rows))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", type=Path)
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parent)
    args = parser.parse_args()
    main(args.files, args.output)
