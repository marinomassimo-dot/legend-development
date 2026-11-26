"""Replay published prefrontal recording data and the exposure and antagonism checks."""

import argparse
import hashlib
from itertools import product
from pathlib import Path
from statistics import mean, median
import sys
from xml.etree import ElementTree
from zipfile import ZipFile

sys.path.insert(0, str(Path(__file__).resolve().parents[6] / "framework" / "scripts"))
from xlsx_to_text import sheet_names


WORKBOOK_SHA256 = "7345df531275223562b16cffd25fba2abd092190ca3177a643442c365b5bca66"
# Control and drug cell columns, range of recordings, and allowed animal counts.
COMPARISONS = (
    ("ied_10", "I", "J", 21, 25, (2, 3)),
    ("ied_100", "B", "C", 21, 26, (3,)),
    ("ied_100_idazoxan", "B", "C", 43, 46, (2,)),
    ("persistent_sodium_10", "J", "K", 61, 64, (2,)),
    ("persistent_sodium_100", "B", "C", 61, 67, (3,)),
    ("transient_sodium_10", "I", "J", 83, 86, (2,)),
    ("transient_sodium_100", "C", "D", 83, 87, (2,)),
)


def first_worksheet(path):
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    if digest != WORKBOOK_SHA256:
        raise ValueError(f"unexpected source workbook SHA-256: {digest}")
    with ZipFile(path) as workbook:
        member = dict(sheet_names(workbook))["Arkusz1"]
        sheet = ElementTree.fromstring(workbook.read(member))
    return {
        cell.attrib["r"]: cell.findtext("{*}v")
        for cell in sheet.findall(".//{*}c")
        if cell.find("{*}v") is not None
    }


def animal_mean_range(values, count):
    """Equal-animal contrast across all possible groupings with nonempty groups."""
    distinct_means = set()
    for assignment in product(range(count), repeat=len(values)):
        if len(set(assignment)) != count:
            continue
        group_means = [
            mean(value for value, label in zip(values, assignment) if label == group)
            for group in range(count)
        ]
        distinct_means.add(mean(group_means))
    return min(distinct_means), max(distinct_means)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workbook", type=Path)
    args = parser.parse_args()
    cells = first_worksheet(args.workbook)
    print("comparison\tmetric\tvalue\tunit\tlocator")

    def emit(comparison, metric, value, unit, locator):
        print(f"{comparison}\t{metric}\t{value:.7g}\t{unit}\t{locator}")

    for name, ctrl, drug, start, end, animal_counts in COMPARISONS:
        locator = f"Arkusz1!{ctrl}{start}:{drug}{end}"
        pairs = [(float(cells[f"{ctrl}{i}"]), float(cells[f"{drug}{i}"])) for i in range(start, end + 1)]
        changes = [100 * (after - before) / before for before, after in pairs]
        emit(name, "recordings", len(pairs), "recordings", locator)
        emit(name, "recordings_reduced", sum(change < 0 for change in changes), "recordings", locator)
        emit(name, "median_drug", median(after for _, after in pairs), "normalized", locator)
        emit(name, "mean_paired_change", mean(changes), "percent", locator)
        for count in animal_counts:
            low, high = animal_mean_range(changes, count)
            emit(name, f"animal_mean_min_if_n_{count}", low, "percent", locator)
            emit(name, f"animal_mean_max_if_n_{count}", high, "percent", locator)

    # PubMed 17723079 reports mean Cmax as guanfacine mass concentration, not brain exposure.
    molecular_weight = 246.09  # guanfacine free base, grams per mole
    fraction_unbound = 0.30   # EMA Intuniv, section 5.2
    ca3_ec50 = 49.0          # nM, PMID 35984443
    for age, ng_ml in (("children_6_12", 10.1), ("adolescents_13_17", 7.01)):
        total_nm = ng_ml * 1000 / molecular_weight
        plasma_free_nm = total_nm * fraction_unbound
        emit(age, "total_plasma_peak", total_nm, "nM", "Boellner 4 mg repeated, mean")
        emit(age, "estimated_free_plasma_peak", plasma_free_nm, "nM", "Boellner plus EMA binding")
        emit(age, "low_sodium_assay_over_total_peak", 10000 / total_nm, "fold", "Pasierski Fig. 4, 10 uM")
        emit(age, "low_sodium_assay_over_free_peak", 10000 / plasma_free_nm, "fold", "Pasierski Fig. 4, 10 uM")
        emit(age, "CA3_EC50_over_free_peak", ca3_ec50 / plasma_free_nm, "fold", "Biggane Fig. 4 and Results")

    # Counterexample, not a fitted prefrontal model. Apply the CA3 epinephrine Schild pKb
    # to the CA3 guanfacine EC50 and assume reversible competition with a Hill slope of one.
    kb_nm = 10 ** (9 - 7.92)
    nominal_idazoxan_nm = 20000
    dose_ratio = 1 + nominal_idazoxan_nm / kb_nm
    shifted_ec50 = ca3_ec50 * dose_ratio
    emit("antagonism_scenario", "CA3_functional_Kb", kb_nm, "nM", "Biggane Results, pKb 7.92")
    emit("antagonism_scenario", "competitive_dose_ratio", dose_ratio, "fold", "Schild equation at 20 uM")
    emit("antagonism_scenario", "shifted_CA3_EC50", shifted_ec50 / 1000, "uM", "CA3 transfer scenario")
    emit("antagonism_scenario", "relative_to_own_max_at_100_uM",
         100000 / (100000 + shifted_ec50), "fraction", "Hill coefficient one")


if __name__ == "__main__":
    main()
