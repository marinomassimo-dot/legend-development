"""Replay systemic 2-DG scale comparisons and selected slice summaries."""

import argparse
import csv
from hashlib import sha256
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
REGISTRY_SHA256 = "acdacc7f1fff3fc33960031b960b5fa63aab2695f04fcec0c8b4666bd39473aa"
MOLAR_MASS = 164.16  # PubChem CID 108223, g/mol.


def registry(path):
    source = path.read_bytes()
    if sha256(source).hexdigest() != REGISTRY_SHA256:
        raise ValueError("The NIH aggregate snapshot differs from the audited revision")
    return json.loads(source)["resultsSection"]


def endpoints(outcomes, title_prefix):
    outcome = next(m for m in outcomes if m["title"].startswith(title_prefix))
    assert outcome["paramType"] == "MEAN"
    groups = {g["id"]: g["title"] for g in outcome["groups"]}
    denominator, = outcome["denoms"]
    counts = {r["groupId"]: int(r["value"]) for r in denominator["counts"]}
    one_class, = outcome["classes"]
    one_category, = one_class["categories"]
    for cell in one_category["measurements"]:
        group = cell["groupId"]
        yield (groups[group], counts[group], float(cell["value"]), cell["spread"])


def exposure(data):
    outcomes = data["outcomeMeasuresModule"]["outcomeMeasures"]
    peaks = endpoints(outcomes, "Maximum Observed Blood Concentration")
    ranges = {g["id"]: g for g in data["adverseEventsModule"]["eventGroups"]}
    assert sum(g["seriousNumAtRisk"] for g in ranges.values()) == 9
    assert sum(g["seriousNumAffected"] for g in ranges.values()) == 0
    for arm, n, cmax, spread in peaks:
        as_um = cmax * 1000 / MOLAR_MASS
        yield ("adult_epilepsy_Cmax", arm, n, cmax, "ug/mL", spread)
        yield ("adult_epilepsy_Cmax", arm, n, as_um, "umol/L", "mean converted")
        for bath in (8, 10):
            yield ("nominal_bath_over_epilepsy_Cmax", arm, n, bath * 1000 / as_um, "ratio",
                   f"{bath} mM bath; separate compartments")
    for arm, n, t_half, spread in endpoints(outcomes, "Elimination Half-Life"):
        yield ("adult_epilepsy_elimination_half_life", arm, n, t_half, "h", spread)

    # Stein et al. primary abstract, separate oncology population and regimens.
    for peak in (277, 449, 744):
        group = f"reported_oncology_{peak}uM_peak"
        for bath in (8, 10):
            yield ("nominal_bath_over_oncology_Cmax", group, "NA", bath * 1000 / peak, "ratio",
                   f"{bath} mM bath; separate compartments")


def circuit():
    # Shao and Stafstrom, Fig. 3: means of fractional reductions and marginal medians.
    excit_remaining = 1 - 0.71
    inhib_remaining = 1 - 0.40
    yield ("fraction_remaining", "high_K_CA3_mean_relative_change_excitatory", "fraction",
           excit_remaining)
    yield ("fraction_remaining", "high_K_CA3_mean_relative_change_inhibitory", "fraction",
           inhib_remaining)
    yield ("ratio_of_fraction_remaining", "high_K_CA3_mean_relative_changes", "ratio",
           excit_remaining / inhib_remaining)
    yield ("ratio_of_fraction_remaining", "high_K_CA3_ratio_of_marginal_medians", "ratio",
           (2.0 / 7.3) / (29.1 / 44.7))
    yield ("ratio_of_miniature_event_frequency_medians", "TTX_after_bursting_and_2DG", "ratio",
           0.09 / 0.20)
    # Koenig et al. Figs. 3 and 4. Different preparations and intervention windows.
    yield ("change_in_fraction_of_epileptiform_sweeps", "acute_bath_after_injury", "fraction",
           0.18 - 0.90)
    yield ("change_in_fraction_of_epileptiform_sweeps", "earlier_in_vivo_after_injury", "fraction",
           0.13 - 0.95)


def write(path, header, rows):
    with path.open("w", newline="") as f:
        out = csv.writer(f, delimiter="\t", lineterminator="\n")
        out.writerow(header)
        for row in rows:
            out.writerow(f"{v:.6f}" if isinstance(v, float) else v for v in row)


def main(data, out):
    out.mkdir(parents=True, exist_ok=True)
    write(out / "exposure.tsv", ("comparison", "arm", "endpoint_n", "value", "unit", "detail"),
          exposure(registry(data)))
    write(out / "circuit.tsv", ("comparison", "preparation", "unit", "value"), circuit())


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("public_registry_snapshot", type=Path)
    p.add_argument("--out", type=Path, default=HERE)
    args = p.parse_args()
    main(args.public_registry_snapshot, args.out)
