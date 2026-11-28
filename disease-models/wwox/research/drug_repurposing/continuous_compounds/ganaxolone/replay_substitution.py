"""Replay the ganaxolone replacement counterexamples from public aggregate sources."""

import argparse
import csv
import hashlib
import json
from math import comb
from pathlib import Path
import re

MARIGOLD_HASH = "447e0856b6f14e0769d0041c695d24450f84534f956b5f00ed2489e7be65f8c5"
ASSIGNMENT_HASH = "8bd1add7e482d049443130062c41e5386e4c474c80d45b0417165a4a8c6200b0"
TABLE_TEXT_HASH = "24859698ebb98a90b738970c91227a74b1348a9002cee003e9e1d684d9b029db"
STEROID_NAMES = re.compile(
    r"androsterone|androstane.?diol|allopregnanolone|brexanolone|pregnanolone|"
    r"5[αa][- ]?pregnan|5[αa][- ]?androstan|pregnenolone|progesterone",
    re.IGNORECASE,
)
STEROID_FORMULAS = {"C19H30O2", "C19H32O2", "C21H34O2", "C21H34O5S", "C21H32O2", "C21H30O2"}

# Carver and Reddy (2016), Table 2. Each value is relative to the 1 µM GABA response.
TONIC_CURRENT = (
    (0.1, 0.92, 0.94, 2.50, 1.61),
    (0.3, None, 1.09, 2.94, 2.76),
    (1.0, 1.47, 1.30, 4.36, 3.47),
    (3.0, 2.15, 2.95, 10.98, 8.89),
)


def verified(path, digest):
    value = path.read_bytes()
    if hashlib.sha256(value).hexdigest() != digest:
        raise ValueError(f"Unexpected input checksum: {path}")
    return value


def write_rows(path, header, rows):
    with path.open("w", newline="") as file:
        writer = csv.writer(file, delimiter="\t", lineterminator="\n")
        writer.writerow(header.split())
        writer.writerows(rows)


def fly_coverage(files):
    assignment = files / "deepening_downloads" / "n_acetylneuraminic_acid_20261126" / (
        "m_MTBLS12344_LC-MS_alternating_hilic_metabolite_profiling_v2_maf.tsv"
    )
    workbook_text = files / "fulltext" / "PMID42909904_supplement" / "Supplementary_tables_derived.txt"
    assigned = list(csv.DictReader(verified(assignment, ASSIGNMENT_HASH).decode().splitlines(), delimiter="\t"))
    yield ("MTBLS12344_MAF", len(assigned),
           sum(bool(STEROID_NAMES.search(row["metabolite_identification"])) for row in assigned),
           sum(row["chemical_formula"] in STEROID_FORMULAS for row in assigned), ASSIGNMENT_HASH)

    sheets = {4: [], 7: []}
    table = None
    for line in verified(workbook_text, TABLE_TEXT_HASH).decode().splitlines():
        if line.startswith("## sheet"):
            table = next((number for number in sheets if f"'Supplementary Table {number}'" in line), None)
        cols = line.split("\t")
        if table is not None and len(cols) >= 5 and cols[0].isdigit():
            sheets[table].append(cols[3:5])
    for table, rows in sheets.items():
        hits = sum(any(STEROID_NAMES.search(field) for field in row) for row in rows)
        yield f"Supplementary_Table_{table}", len(rows), hits, "NA", TABLE_TEXT_HASH


def current_contrasts():
    for concentration, precursor, product, allo, ganaxolone in TONIC_CURRENT:
        delta = "NA" if precursor is None else f"{product - precursor:+.2f}"
        yield concentration, "NA" if precursor is None else precursor, product, allo, ganaxolone, delta, f"{ganaxolone - 1:.2f}"


def fisher_two_sided(a, n_active, c, n_placebo):
    events = a + c
    total = n_active + n_placebo
    denominator = comb(total, events)

    def fixed_margin_count(k):
        return comb(n_active, k) * comb(n_placebo, events - k)

    observed = fixed_margin_count(a)
    feasible = range(max(0, events - n_placebo), min(events, n_active) + 1)
    return sum(fixed_margin_count(k) for k in feasible if fixed_margin_count(k) <= observed) / denominator


def trial_contrasts(files):
    snapshot = files / "deepening_downloads" / "ganaxolone_followup_20261127" / "NCT03572933.json"
    trial = json.loads(verified(snapshot, MARIGOLD_HASH))
    safety = trial["resultsSection"]["adverseEventsModule"]
    group_names = {group["id"]: group["title"].casefold() for group in safety["eventGroups"]}
    somnolence = next(event for event in safety["otherEvents"] if event["term"] == "Somnolence")
    active = next(row for row in somnolence["stats"] if "ganaxolone" in group_names[row["groupId"]])
    placebo = next(row for row in somnolence["stats"] if "placebo" in group_names[row["groupId"]])
    # Peer-reviewed Marigold manuscript Table 2 and FDA statistical review Table 7.
    data = (
        ("motor_seizure_response_at_least_50pct", 12, 49, 5, 51),
        ("motor_seizure_response_under_50pct", 37, 49, 46, 51),
        ("somnolence_registry_preferred_term", active["numAffected"], active["numAtRisk"],
         placebo["numAffected"], placebo["numAtRisk"]),
    )
    for endpoint, a, na, c, nc in data:
        risk_active, risk_placebo = a / na, c / nc
        yield (endpoint, a, na, c, nc, f"{risk_active / risk_placebo:.5f}",
               f"{100 * (risk_active - risk_placebo):+.3f}", f"{fisher_two_sided(a, na, c, nc):.5f}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    write_rows(args.output / "fly_steroid_coverage.tsv", "source rows target_name_rows target_formula_rows sha256",
               fly_coverage(args.files))
    write_rows(args.output / "tonic_current_contrasts.tsv", "nominal_steroid_uM androsterone_fold "
               "androstanediol_fold allopregnanolone_fold ganaxolone_fold product_minus_precursor "
               "ganaxolone_increment_over_gaba_alone", current_contrasts())
    write_rows(args.output / "marigold_event_coding.tsv", "event ganaxolone_n ganaxolone_denominator "
               "placebo_n placebo_denominator ganaxolone_placebo_RR risk_difference_pp two_sided_Fisher_descriptive",
               trial_contrasts(args.files))


if __name__ == "__main__":
    main()
