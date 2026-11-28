"""Replay the presynaptic endpoints from Kokotos et al. Zenodo 11122117."""

import csv
import hashlib
import io
import sys
from pathlib import Path
from random import Random
from statistics import mean


SOURCE_MD5 = {
    "Fig.2B, C, D.csv": "4f8fe39cd6ab28cfbd418c50f458f43b",
    "Fig.1E.csv": "a608be78219f14049ab75c1c1adae355",
    "Fig.S2F.csv": "440a9f22ec5f8805cbca62d5ee788ceb",
    "Fig.S2H.csv": "81ad0bc2a283cb5b446102706b47bb8d",
}


def load(directory, filename):
    data = (directory / filename).read_bytes()
    if hashlib.md5(data).hexdigest() != SOURCE_MD5[filename]:
        raise ValueError(f"Unexpected data for {filename}")
    values = {}
    for row in csv.DictReader(io.StringIO(data.decode())):
        group = values.setdefault(row["treatment"], {})
        cell = group.setdefault(row["individual_cell"], {})
        endpoint = row["timePoint"]
        if endpoint in cell:
            raise ValueError(f"Duplicate endpoint for {row['individual_cell']}")
        cell[endpoint] = float(row["dependentVariable"]) if row["dependentVariable"] else None
    return values


def endpoint(group, name):
    return [cell[name] for cell in group.values() if cell[name] is not None]


def paired_recovery(group):
    return [100 * (cell["Recovery"] - cell["Post-stim"]) for cell in group.values()]


def bootstrap_difference(treatment, comparator):
    rng = Random(201)
    estimates = sorted(
        mean(rng.choices(treatment, k=len(treatment)))
        - mean(rng.choices(comparator, k=len(comparator)))
        for _ in range(10000)
    )
    return estimates[250], estimates[9749]


def contrast(panel, measure, treated, control, unit):
    lower, upper = bootstrap_difference(treated, control)
    print(
        f"{panel}\t{measure}\t{len(treated)}\t{len(control)}\t{mean(treated):.4f}\t"
        f"{mean(control):.4f}\t{mean(treated) - mean(control):.4f}\t{lower:.4f}\t{upper:.4f}\t{unit}"
    )


def main(directory):
    print("panel\tmeasure\tn_treated\tn_comparator\tmean_treated\tmean_comparator\tdifference\tconditional_bootstrap_low95\tconditional_bootstrap_high95\tunit")
    atp = load(directory, "Fig.2B, C, D.csv")
    ctl = atp["0.1mMGlucose"]
    tz = atp["10uMTZ"]
    assert (len(ctl), len(tz), len(atp["PGK1-HALO"])) == (12, 17, 10)
    for name, group in [("10uMTZ", tz), ("PGK1-HALO", atp["PGK1-HALO"])]:
        contrast("2B", f"{name} baseline", endpoint(group, "Baseline"), endpoint(ctl, "Baseline"), "sensor ratio")
        for label, panel in [("Post-stim", "2C"), ("Recovery", "2D")]:
            contrast(panel, f"{name} {label}", [100 * x for x in endpoint(group, label)],
                     [100 * x for x in endpoint(ctl, label)], "% baseline sensor ratio")
        contrast("2D minus 2C", f"{name} paired recovery", paired_recovery(group),
                 paired_recovery(ctl), "percentage points of baseline")
    comparisons = [
        ("Fig.1E.csv", "10uMTerazosin", "0.1mMGlucose", 10, 23),
        ("Fig.S2F.csv", "10uMTZ+PGK1_KD", "10uMTZ", 13, 10),
        ("Fig.S2H.csv", "10uMTZ-md", "10uMTZ", 10, 10),
    ]
    for filename, treated, control, expected_treated, expected_control in comparisons:
        values = load(directory, filename)
        treated_values = endpoint(values[treated], "Stimulus 10")
        control_values = endpoint(values[control], "Stimulus 10")
        assert (len(treated_values), len(control_values)) == (expected_treated, expected_control)
        contrast(filename, f"{treated} minus {control}, train 10", treated_values, control_values,
                 "fraction of NH4Cl-revealed fluorescence")


if __name__ == "__main__":
    main(Path(sys.argv[1]))
