"""Recompute paired adult plasma AUC contrasts from supplementary Tables S5 and S6."""

import argparse
from itertools import product
from math import sqrt
import re
from statistics import mean, stdev
import subprocess


PAGES = {"spermidine": 7, "spermine": 12}
T_975_DF_11 = 2.200985


def auc_pairs(path, page):
    text = subprocess.check_output(
        ["pdftotext", "-f", str(page), "-l", str(page), "-layout", path, "-"], text=True
    )
    auc_section = text.split("AUC 0-tlast", 2)[-1].split("cmax", 1)[0]
    pattern = r"^\s*(?:\(h\S*\s*ng/mL\)\s*)?(\d{1,2}) {2,}(\d+(?:\.\d+)?) {2,}(\d+(?:\.\d+)?)"
    pairs = [(int(index), float(placebo), float(verum))
             for index, placebo, verum in re.findall(pattern, auc_section, flags=re.MULTILINE)]
    if [row[0] for row in pairs] != list(range(1, 13)):
        raise ValueError(f"Expected all 12 pairs on page {page}, found {len(pairs)}")
    return [(placebo, verum) for _, placebo, verum in pairs]


def contrast(pairs):
    placebo, verum = map(mean, zip(*pairs))
    deltas = [during - before for before, during in pairs]
    delta_mean = mean(deltas)
    half_interval = T_975_DF_11 * stdev(deltas) / sqrt(len(deltas))
    abs_total = abs(sum(deltas))
    at_least_as_extreme = sum(
        abs(sum(sign * delta for sign, delta in zip(signs, deltas))) >= abs_total - 1e-9
        for signs in product((-1, 1), repeat=len(deltas))
    )
    omissions = [mean(deltas[:i] + deltas[i + 1:]) for i in range(len(deltas))]
    return (len(deltas), sum(d > 0 for d in deltas), f"{placebo:.3f}", f"{verum:.3f}",
            f"{delta_mean:.3f}", f"{100 * delta_mean / placebo:.2f}",
            f"{delta_mean - half_interval:.3f}", f"{delta_mean + half_interval:.3f}",
            f"{at_least_as_extreme / (2 ** len(deltas)):.5f}",
            f"{min(omissions):.3f}", f"{max(omissions):.3f}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("supplement_pdf")
    args = parser.parse_args()
    print("plasma_analyte\tunit\tpairs\tpositive_pairs\tplacebo_mean\tverum_mean\tpaired_mean"
          "\tpercent_of_placebo\tpaired_t_ci95_low\tpaired_t_ci95_high"
          "\tsign_flip_p_two_sided\tomit_min\tomit_max")
    for analyte, page in PAGES.items():
        result = contrast(auc_pairs(args.supplement_pdf, page))
        print("\t".join(map(str, (analyte, "h ng/mL", *result))))


if __name__ == "__main__":
    main()
