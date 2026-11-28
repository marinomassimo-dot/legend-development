"""Reproduce exposure sensitivities, enzyme contrasts and aggregate trial contrasts."""

import argparse
import csv
from hashlib import sha256
import json
from math import comb, sqrt
from pathlib import Path

HERE = Path(__file__).resolve().parent


def read_rows(path):
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write(out, name, fields, rows):
    with (out / f"{name}.tsv").open("w", newline="") as handle:
        table = csv.writer(handle, delimiter="\t", lineterminator="\n")
        table.writerow(fields.split())
        table.writerows(rows)


def load_inputs():
    return {(row["group"], row["key"]): float(row["value"])
            for row in read_rows(HERE / "inputs.tsv")}


def replay_exposure(out, data):
    molar_mass = data["adult_pk", "free_base_mass"]
    interval = data["adult_pk", "interval"]
    free_plasma = data["adult_pk", "free_fraction"]
    targets = (data["benchmarks", "pkm2_ac50"], data["benchmarks", "h3_ec50"])
    rows = []
    for study in ("rat_single", "rat_repeat"):
        # Assume 1 g/mL to make the published tissue-to-plasma AUC ratio dimensionless.
        kp = data[study, "brain_auc"] / data[study, "plasma_auc"]
        for arm in ("plasma_arm_A", "plasma_arm_B", "plasma_arm_C"):
            coordinates = (("peak", data[arm, "cmax"]),
                           ("mean", data[arm, "auc"] / interval),
                           ("trough", data[arm, "ctrough"]))
            for label, ng_ml in coordinates:
                plasma_total = 1000 * ng_ml / molar_mass
                brain_total = plasma_total * kp
                required = [benchmark / brain_total for benchmark in targets]
                rows.append((study, arm, label, f"{kp:.5f}", f"{plasma_total * free_plasma:.3f}",
                             f"{brain_total:.3f}", *(f"{x:.3f}" for x in required),
                             *(f"{brain_total * f:.3f}" for f in (0.03, 0.10, 0.30))))
    write(out, "exposure_sensitivity", "rat_AUC_context historical_adult_arm coordinate "
          "Kp_assumed free_plasma_nM brain_total_scenario_nM required_fu_brain_PKM2 "
          "required_fu_brain_H3_inverse_agonism brain_free_at_fu_003_nM "
          "brain_free_at_fu_010_nM brain_free_at_fu_030_nM", rows)


def replay_pkr(out, data):
    sample = (0.065, 0.1, 0.3, 1.0, 3.0, 10.0)
    rows = []
    for pep in sample:
        baseline, activated = [data["pkr_assay", f"{state}_vmax"] * pep /
                               (data["pkr_assay", f"{state}_km"] + pep)
                               for state in ("vehicle", "bound")]
        rows.append((pep, f"{baseline:.5f}", f"{activated:.5f}", f"{activated / baseline:.3f}"))
    write(out, "pkr_substrate", "PEP_mM vehicle_umol_per_s_mg activated_umol_per_s_mg fold", rows)


def wilson(x, n):
    z = 1.959963984540054
    fraction = x / n
    base = 1 + z**2 / n
    center = (fraction + z**2 / (2 * n)) / base
    width = z / base * sqrt(fraction * (1 - fraction) / n + z**2 / (4 * n**2))
    return center - width, center + width


def trial_row(name, treated_success, treated, control_success, control):
    x, n = treated_success, treated
    y, m = control_success, control
    active, placebo = x / n, y / m
    active_lo, active_hi = wilson(x, n)
    control_lo, control_hi = wilson(y, m)
    risk_difference = active - placebo
    lower = risk_difference - sqrt((active - active_lo)**2 + (control_hi - placebo)**2)
    upper = risk_difference + sqrt((active_hi - active)**2 + (placebo - control_lo)**2)
    success = x + y
    support = range(max(0, success - m), min(n, success) + 1)
    observed_mass = comb(n, x) * comb(m, y)
    masses = [comb(n, k) * comb(m, success - k) for k in support]
    fisher = sum(mass for mass in masses if mass <= observed_mass) / comb(n + m, success)
    return (name, x, n, y, m, f"{100 * risk_difference:.2f}", f"{100 * lower:.2f}",
            f"{100 * upper:.2f}", f"{fisher:.5f}")


def replay_trials(source, out, data):
    raw = json.loads((source / "NCT03548220.json").read_text())
    outcomes = raw["resultsSection"]["outcomeMeasuresModule"]["outcomeMeasures"]
    primary = next(item for item in outcomes if item["type"] == "PRIMARY")
    sample = {row["groupId"]: int(row["value"]) for row in primary["denoms"][0]["counts"]}
    measures = primary["classes"][0]["categories"][0]["measurements"]
    counts = {row["groupId"]: round(sample[row["groupId"]] * float(row["value"]) / 100)
              for row in measures}
    rows = [trial_row("adult_ACTIVATE_Hb", counts["OG001"], sample["OG001"],
                      counts["OG000"], sample["OG000"])]
    for group, record in (("peds_NT", "NCT05175105"), ("peds_T", "NCT05144256")):
        raw = json.loads((source / f"{record}.json").read_text())
        expected = raw["protocolSection"]["designModule"]["enrollmentInfo"]["count"]
        args = [int(data[group, field]) for field in
                ("active_success", "active_n", "control_success", "control_n")]
        if args[1] + args[3] != expected:
            raise ValueError(f"Poster or sponsor denominator differs from registry: {record}")
        rows.append(trial_row(group, *args))
    write(out, "controlled_trials", "cohort treated_success treated_n control_success control_n "
          "risk_difference_pp Newcombe95_lo_pp Newcombe95_hi_pp Fisher_two_sided_descriptive", rows)


def replay_flux(out):
    # Unitless, steady substrate supply and fixed oxidative cap, illustrative rather than fitted.
    scenarios = (("PK_limited", 1.4, 0.6, 0.9),
                 ("upstream_limited", 0.5, 0.6, 0.9),
                 ("oxidative_limited", 1.4, 0.6, 0.3))
    rows = []
    for scenario, supply, pk, oxidative_cap in scenarios:
        for perturbation in (1, 2):
            glycolysis = min(supply, pk * perturbation)
            oxidation = min(glycolysis, oxidative_cap)
            rows.append((scenario, supply, pk, oxidative_cap, perturbation, f"{glycolysis:.2f}",
                         f"{oxidation:.2f}", f"{glycolysis - oxidation:.2f}"))
    write(out, "flux_examples", "scenario upstream_capacity baseline_PK_capacity oxidative_capacity "
          "PK_multiplier terminal_glycolytic_ATP_proxy oxidation_flux_proxy lactate_export_proxy", rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("sources", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    for item in read_rows(HERE / "sources.tsv"):
        if item["file"] and sha256((args.sources / item["file"]).read_bytes()).hexdigest() != item["sha256"]:
            raise ValueError(f"Source SHA-256 mismatch for {item['file']}")
    args.output.mkdir(parents=True, exist_ok=True)
    inputs = load_inputs()
    replay_exposure(args.output, inputs)
    replay_pkr(args.output, inputs)
    replay_trials(args.sources, args.output, inputs)
    replay_flux(args.output)


if __name__ == "__main__":
    main()
