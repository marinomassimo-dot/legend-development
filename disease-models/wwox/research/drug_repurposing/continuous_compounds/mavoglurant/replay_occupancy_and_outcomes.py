"""Replay the adult PET model, pediatric PK summaries and FXLEARN aggregate outcomes."""

import argparse
from hashlib import sha256
import json
from math import sqrt
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "sodium_benzoate"))
sys.path.insert(0, str(HERE.parent / "jbpos0101"))
from coagonist_screen import bulk_panel, nuclei_panel, tsv
from replay_exposure_and_receptors import verified_expression

FINGERPRINTS = {
    "NCT02920892.json": "c636b088aee9fa14f0a31340745ce44599e77f33053064b332025597d6911540",
    "NCT02920892_Prot_SAP.pdf": "eb29b67479b1e6aa1a324e12c1b783498203d42592f952cbf6fb17a8544c397f",
    "PET_Streffer_2021.pdf": "fc129401fedaa2ed2d5ef3468844ecb99e6a27967820608158389642642b1d25",
    "FXLEARN_JCI_2024.pdf": "e4a0573a9ee29a44e5b24a149f3ea65355bd04cd668578db062d156a39569339",
}
GENES = ("Grm5", "Grm1", "Homer1", "Plcb1", "Itpr1", "Eef2k", "Eif4e", "Arc", "Dlg4")
EC50 = 43  # adult target-region pooled ng/mL. Regional sensitivity uses 35 and 58.
ED50 = 69  # adult acute dose fit, mg, 3–4 hours after administration
EMAX_DISPLACEMENT = 65  # approximate percent loss of tracer BPP at asymptote


def verified(path, expected):
    raw = path.read_bytes()
    if sha256(raw).hexdigest() != expected:
        raise ValueError(f"Unexpected source fingerprint: {path}")
    return raw


def occupancy(level, midpoint):
    return 100 * level / (midpoint + level)


def adult_pet():
    # Streffer Table 1 PK denominator may differ from PET cohort size. Scan window is one hour.
    for dose, n, peak, scan_auc, reported in (
        (25, 5, 54.23, 31.42, 27),
        (100, 3, 191.6, 156.3, 59),
        (200, 4, 337.6, 202.8, 74),
        (400, 3, 1004.0, 715.0, 85),
    ):
        dose_implied = occupancy(dose, ED50)
        from_mean_c = occupancy(scan_auc, EC50)
        yield dose, n, peak, scan_auc, reported, dose_implied, dose_implied * EMAX_DISPLACEMENT / 100, from_mean_c



def figure3_points():
    # Fig. 3A on page 6, rendered with pdftoppm -scale-to 1550.
    centers = (
        (25, 160.92, 397.37), (25, 172.72, 395.90), (25, 166.13, 342.87),
        (100, 179.54, 322.81), (100, 235.05, 311.84), (100, 218.09, 306.03),
        (200, 242.00, 308.00), (200, 251.50, 261.50), (200, 180.00, 278.00),
        (400, 235.50, 292.00), (400, 489.00, 242.25), (400, 428.00, 237.50),
    )
    for dose, x, y in centers:
        yield dose, x, y, (x - 159) * 1250 / (565 - 159), (437 - y) * 100 / (437 - 155)


def fit_displacement(points):
    """Weighted equally by plotted point, solve the scale at each midpoint."""
    def candidate(k):
        weights = [c / (k + c) for _, _, _, c, _ in points]
        max_displacement = sum(weight * row[-1] for weight, row in zip(weights, points)) / sum(w * w for w in weights)
        squared_error = sum((weight * max_displacement - row[-1]) ** 2 for weight, row in zip(weights, points))
        return squared_error, k, max_displacement

    error, midpoint, maximum = min(candidate(step / 10) for step in range(10, 2001))
    return midpoint, maximum, sqrt(error / len(points))


def fit_checks(points):
    yield "all_points", len(points), *fit_displacement(points)
    for dose in (25, 100, 200, 400):
        sub = [row for row in points if row[0] != dose]
        yield f"omit_dose_{dose}_mg", len(sub), *fit_displacement(sub)


def pediatric_pk():
    # CAFQ056B2154 as transcribed in FXLEARN protocol Tables 2 and 3. AUC_last is not AUC0–12.
    rows = (
        ("3–4", 8, 15, 1, 177.0, 0, None),
        ("3–4", 8, 20, 1, 75.4, 0, None),
        ("3–4", 8, 25, 2, 149.0, 2, 689.0),
        ("3–4", 8, 50, 4, 179.0, 2, 768.0),
        ("3–4", 8, 100, 1, 96.0, 0, None),
        ("5–11", 7, 20, 1, 196.0, 0, None),
        ("5–11", 7, 25, 1, 113.0, 1, 461.0),
        ("5–11", 7, 50, 3, 229.0, 1, 585.0),
        ("5–11", 7, 60, 1, 234.0, 0, None),
        ("5–11", 7, 100, 6, 286.0, 3, 1210.0),
    )
    for age, day, dose, n_peak, cmax, n_auc, auc in rows:
        avg = auc / 12 if auc is not None else None
        models = (occupancy(avg, k) for k in (58, EC50, 35)) if avg is not None else ("NA",) * 3
        yield age, day, dose, n_peak, cmax, n_auc, auc, avg, occupancy(cmax, EC50), *models


def fxlearn_flow(data):
    periods = data["participantFlowModule"]["periods"]
    outcomes = {row["type"]: row["achievements"] for row in periods[1]["milestones"]}
    group_counts = {row["groupId"]: int(row["numSubjects"]) for row in outcomes["STARTED"]}
    for group, arm, paper_completed in (("FG001", "placebo", 46), ("FG002", "mavoglurant", 45)):
        posted, = [int(row["numSubjects"]) for row in outcomes["COMPLETED"] if row["groupId"] == group]
        yield arm, group_counts[group], paper_completed, posted, paper_completed - posted


def fxlearn_effect(data):
    outcome = data["outcomeMeasuresModule"]["outcomeMeasures"][0]
    assert outcome["type"] == "PRIMARY" and outcome["paramType"] == "LEAST_SQUARES_MEAN"
    contrast, = outcome["analyses"]
    assert contrast["ciPctValue"] == "90"
    effect, low, high = (float(contrast[key]) for key in ("paramValue", "ciLowerLimit", "ciUpperLimit"))
    yield effect, low, high, float(contrast["pValue"]), 10**effect, 10**low, 10**high


def fxlearn_safety(data):
    for group, arm in (("EG001", "placebo"), ("EG002", "mavoglurant")):
        summary, = [row for row in data["adverseEventsModule"]["eventGroups"] if row["id"] == group]
        for prefix, label in (("other", "other_AE"), ("serious", "serious_AE")):
            affected, risk = (summary[f"{prefix}Num{s}"] for s in ("Affected", "AtRisk"))
            yield arm, label, affected, risk, affected / risk
        for term in ("Insomnia", "irritability", "Psychomotor Hyperactivity"):
            event, = [e for e in data["adverseEventsModule"]["otherEvents"] if e["term"] == term]
            stat, = [s for s in event["stats"] if s["groupId"] == group]
            yield arm, term, stat["numAffected"], stat["numAtRisk"], stat["numAffected"] / stat["numAtRisk"]


def rounded(rows):
    for row in rows:
        yield (f"{v:.5g}" if isinstance(v, float) else v if v is not None else "NA" for v in row)


def main(files, out):
    source = files / "deepening_downloads/mavoglurant_20261127"
    inputs = {name: verified(source / name, digest) for name, digest in FINGERPRINTS.items()}
    results = json.loads(inputs["NCT02920892.json"])["resultsSection"]
    out.mkdir(parents=True, exist_ok=True)
    points = list(figure3_points())
    tables = (
        ("adult_pet.tsv", "single_dose_mg PK_n mean_Cmax_ng_mL mean_AUC3to4_ng_h_mL reported_RO_pct dose_model_RO_pct implied_dose_model_displacement_pct mean_scan_C_inserted_into_C_model_pct", adult_pet()),
        ("adult_PET_figure3_points.tsv", "adult_dose_mg plot_center_x_px plot_center_y_px mean_C3to4_ng_mL_approx displacement_pct_approx", points),
        ("adult_PET_figure3_fit.tsv", "fit_subset plot_point_n apparent_EC50_ng_mL apparent_Emax_displacement_pct fit_RMSE_pct_points", fit_checks(points)),
        ("pediatric_PK_sensitivity.tsv", "age_years PK_day study_regimen_mg_per_administration PK_n_Cmax mean_Cmax_ng_mL PK_n_AUC0to12 mean_AUC0to12_ng_h_mL arithmetic_mean_Cavg_ng_mL adult_model_at_pediatric_mean_Cmax_pct adult_model_at_Cavg_K58_pct adult_model_at_Cavg_K43_pct adult_model_at_Cavg_K35_pct", pediatric_pk()),
        ("fxlearn_flow.tsv", "arm randomized paper_completed_blinded registry_completed_blinded count_difference", fxlearn_flow(results)),
        ("fxlearn_primary.tsv", "AFQ056_minus_placebo_log10_WCS_change lo_90CI hi_90CI p_value ratio_of_modeled_fold_changes lo_ratio_90CI hi_ratio_90CI", fxlearn_effect(results)),
        ("fxlearn_safety.tsv", "arm item affected_n at_risk_n fraction", fxlearn_safety(results)),
    )
    for filename, fields, rows in tables:
        tsv(out / filename, fields.split(), rounded(rows))
    verified_expression(files)
    tsv(out / "bulk_mglur5_panel.tsv",
        "model accession gene ctrl_n ko_n ctrl_positive ko_positive ctrl_mean ko_mean log2_delta omit_min omit_max mapping".split(),
        bulk_panel(files, GENES))
    tsv(out / "hippocampal_nuclei_panel.tsv", "pool cell_class gene nuclei all_UMI gene_UMI CPM".split(),
        nuclei_panel(files, GENES))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", type=Path)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    main(args.files, args.out)
