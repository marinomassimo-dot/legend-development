"""Replay public MitoQ uptake, litter-blocked counterchecks and clinical denominators."""

import argparse
import json
import math
from pathlib import Path
from statistics import mean, median, stdev
import sys

import xlrd

COMPOUNDS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(COMPOUNDS / "sodium_benzoate"))
sys.path.insert(0, str(COMPOUNDS / "jbpos0101"))
from coagonist_screen import bulk_panel, nuclei_panel, tsv
from replay_exposure_and_receptors import verified, verified_expression


FINGERPRINTS = {
    "Ross_2008_BiochemJ.pdf": "4f95bbcb9be3c478a3e2891f6032691f5065928257626a0f047149dd1fdfcfab",
    "Halliday_Oxford_VOR.pdf": "ecedced89208847afffdbca91bec0682a76acaa0f550c6f1c9ebbba2afe12630",
    "ELA_VOR.pdf": "3ff6bda795a3b3abad7485904d1445841acdd27e209b33c2e43c53e943c6c1f2",
    "ELA_DC3.xls": "63bf2b7cba6034906883a2aaf9153175fadf9f8ca427a47c9ad1c9df743ac687",
    "ELA_DC5.xls": "7d462fa47df8478ad4eb64f4452be07abf01ea835d005d9d1edcedd46a736c54",
    "ELA_DC6.xls": "d1278f26d4e1a9c7fa3adf3d93d3678a13e22dbc6e0b9f1553b854ba35da8c36",
    "Smith_NCBI.html": "51827dc0aee86e5b5a4331fb6570ece4d5de2ece94b1fb41513309e65a523a5c",
    "Porteous_NCBI.html": "8bbd6a1091f4970496a93055c6e49e7ab4ed812b7f34460b2325bb435c29578e",
    "Anxiety_NCBI.html": "ceae09df4fea8d84344d77d6dfff01910b76518ab2372475a3d5d25df8542a18",
    "Anxiety_Fig3.jpg": "a51db4a4f1823f92b6a4e3bddfd5e3474ced7a1c7f5b84062bbb9a79bb14481f",
    "NCT05410873.json": "072098720a44558a3cc66c66ab481cc42b32aeed4080dd1f56ff2cc2ce3837bd",
}
GENES = ("Abcb1a", "Abcb1b", "Abcb1", "Abcg2", "Sdha", "Sdhb", "Gpx4", "Prdx3", "Tomm20")
ARMS = ("CAU_vehicle", "ELA_vehicle", "ELA_dTPP", "ELA_MitoQ")


def voltage_rows():
    # Ross pp. 10-11 of the 29-page deposited PDF, Eq. 3 and the next section.
    as_medium, am_matrix = 0.22, 0.097
    vc, vm = 190, 10
    plasma_factor = 10 ** (40 / 61.5)
    matrix_factor = 10 ** (157 / 61.5)
    free_medium = 260 * as_medium
    free_cytosol = free_medium * plasma_factor
    free_matrix = free_cytosol * matrix_factor
    calculated_ac = vc / (921 * (vc + vm) / (as_medium * plasma_factor) - vm * matrix_factor / am_matrix)
    for mitochondria_mV in (157, 147, 137, 127):
        factor = 10 ** (mitochondria_mV / 61.5)
        for model, ac, am in (
            ("printed_coefficients", 0.002, am_matrix),
            ("cytosol_fit_to_921", calculated_ac, am_matrix),
            ("estimated_free_over_dissipation_sensitive_pools", free_cytosol * vc / (16 * 1000000),
             free_matrix * vm / (29.3 * 1000000)),
        ):
            cell_acr = as_medium * plasma_factor * (vc / ac + vm * factor / am) / (vc + vm)
            yield model, mitochondria_mV, free_medium, free_cytosol, free_cytosol * factor / 1000, ac, am, cell_acr


def xls_columns(path, columns, expected_n):
    sheet = xlrd.open_workbook(path).sheet_by_index(0)
    indexed_rows = [(int(sheet.cell_value(i, 0)), i) for i in range(4, sheet.nrows)
                    if sheet.cell_type(i, 0) == xlrd.XL_CELL_NUMBER]
    assert len(indexed_rows) == expected_n
    assert len({cohort for cohort, _ in indexed_rows}) == expected_n
    data = {arm: [float(sheet.cell_value(i, col)) for _, i in indexed_rows] for arm, col in zip(ARMS, columns)}
    return data


def hedges_g(x, y):
    df = len(x) + len(y) - 2
    pooled_sd = math.sqrt(((len(x) - 1) * stdev(x)**2 + (len(y) - 1) * stdev(y)**2) / df)
    correction = math.exp(math.lgamma(df / 2) - math.log(df / 2) / 2 - math.lgamma((df - 1) / 2))
    return correction * (mean(x) - mean(y)) / pooled_sd


def ela_rows(source):
    for endpoint, sex, spec, columns, n, unit in (
        ("complex_I", "female", 3, (1, 4, 7, 10), 12, "printed_fig4_mOD/min/ug"),
        ("complex_I", "male", 3, (2, 5, 8, 11), 12, "printed_fig4_mOD/min/ug"),
        ("sucrose", "female", 6, (1, 3, 5, 7), 15, "percentage_points"),
        ("sucrose", "male", 5, (1, 3, 5, 7), 15, "percentage_points"),
    ):
        groups = xls_columns(source / f"ELA_DC{spec}.xls", columns, n)
        for a, b in (("ELA_MitoQ", "ELA_dTPP"), ("ELA_MitoQ", "ELA_vehicle"), ("ELA_dTPP", "ELA_vehicle")):
            x, y = groups[a], groups[b]
            d = [left - right for left, right in zip(x, y)]
            omit = [mean(d[:i] + d[i + 1:]) for i in range(n)]
            yield (endpoint, sex, a, b, n, unit, mean(x), mean(y), mean(d), median(d),
                   min(omit), max(omit), hedges_g(x, y), sum(delta > 0 for delta in d))


def radiolabel_rows():
    # Keep the radiolabel source unit. Do not apply an intact fraction from Jurkat.
    wt, transporter_null = 0.6, 2.3
    hours = 20 - 1
    yield "Porteous_2013_III_Fig2B", "whole_brain_wet", "WT", 1, 20, wt, wt / hours, 1
    yield ("Porteous_2013_III_Fig2B", "whole_brain_wet", "Mdr1a_Mdr1b_Bcrp_KO", 1, 20,
           transporter_null, transporter_null / hours, transporter_null / wt)


def brain_mass_rows():
    # Filiou Fig. 3B on the source 715 x 466 px image. Read bar tops, not SEM bars.
    for group, bar_y in (("DL_responder", 132), ("DL_nonresponder", 68)):
        pmol_per_mg = (175 - bar_y) * 0.04 / (175 - 22)
        yield (group, bar_y, pmol_per_mg, pmol_per_mg * 1000)


def clinical_rows(data):
    protocol = data["protocolSection"]
    enrollment = protocol["designModule"]["enrollmentInfo"]
    drug = protocol["armsInterventionsModule"]["interventions"][0]
    assert (enrollment["type"], data["hasResults"], drug["description"]) == ("ACTUAL", False, "Mitoquinol mesylate")
    outcomes = [row["measure"] for row in protocol["outcomesModule"]["primaryOutcomes"]]
    assert outcomes == ["Vanguard phase - change in myocardial PCr:ATP",
                        "Vanguard phase - change in circulating markers of oxidative stress",
                        "Primary outcome - change in LVESVi"]
    yield "Halliday_Fig1B_D", enrollment["count"], 34, 16, 18, 14, 18, 3, "myocardial_PCr/ATP", -0.09, -0.24, 0.07, 0.27, 0.25
    yield "Halliday_Fig1C_D", enrollment["count"], 34, 16, 18, 14, 17, 3, "muscle_PCr_recovery_s", -1.3, -7.6, 4.9, 0.67, 0.67


def rounded(rows):
    for row in rows:
        yield (f"{v:.6g}" if isinstance(v, float) else v for v in row)


def main(files, out):
    source = files / "deepening_downloads/mitoquinone_20261127"
    inputs = {name: verified(source / name, digest) for name, digest in FINGERPRINTS.items()}
    out.mkdir(parents=True, exist_ok=True)
    tables = (
        ("ross_voltage.tsv", "model matrix_negative_mV media_free_nM cyto_free_nM matrix_free_uM cyto_fraction_free matrix_fraction_free predicted_cell_to_medium_total_ACR", voltage_rows()),
        ("ela_blocked.tsv", "endpoint sex arm_a arm_b cohort_n unit mean_a mean_b delta median_pair_delta omit_min omit_max unpaired_Hedges_g positive_pairs", ela_rows(source)),
        ("brain_radiolabel.tsv", "source compartment genotype start_hr end_hr radiolabel_AUC_parent_eq_nmol_h_g time_avg_parent_eq_nmol_g ratio_to_WT", radiolabel_rows()),
        ("brain_lcms.tsv", "Filiou_Fig3B_group bar_top_y_px approx_pmol_mg_wet approx_pmol_g_wet", brain_mass_rows()),
        ("heart_trial.tsv", "publication registered_total randomized_substudy active_randomized placebo_randomized active_analyzed placebo_analyzed month endpoint adjusted_delta CI95_lo CI95_hi p_text p_figure_table", clinical_rows(json.loads(inputs["NCT05410873.json"]))),
    )
    for filename, header, rows in tables:
        tsv(out / filename, header.split(), rounded(rows))
    verified_expression(files)
    rows = (row for row in bulk_panel(files, GENES)
            if row[2] not in ({"ABCB1A", "ABCB1B"} if row[0] == "human_organoid" else {"ABCB1"}))
    tsv(out / "wwox_bulk.tsv", "model accession gene ctrl_n ko_n ctrl_positive ko_positive ctrl_mean ko_mean log2_delta omit_min omit_max mapping".split(), rows)
    tsv(out / "wwox_nuclei.tsv", "pool cell_class gene nuclei all_UMI gene_UMI CPM".split(),
        nuclei_panel(files, tuple(g for g in GENES if g != "Abcb1")))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", type=Path)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    main(args.files, args.out)
