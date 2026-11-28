"""Reproduce group summaries from Saito et al. Supplemental Tables S1 and S2."""
import csv
import hashlib
from io import BytesIO
import math
from pathlib import Path
from statistics import mean, median, stdev
import sys
from zipfile import ZipFile

from openpyxl import load_workbook


SOURCE_HASH = "26685101bd3f0faf002f2a829f74faa3feec28016f7622d4bc97e23143174100"
TIMES = ("1.5 hr", "3 hr", "6 hr")
COMPOUND_NAMES = {"dimethylglycine", "n,n-dimethylglycine"}


def paired_values(sheet):
    headers = list(sheet.iter_rows(min_row=2, max_row=4, values_only=True))
    subjects, states, times = headers
    matches = [
        row for row in sheet.iter_rows(min_row=5, values_only=True)
        if any(isinstance(value, str) and value.strip().casefold() in COMPOUND_NAMES for value in row[:7])
    ]
    if len(matches) != 1:
        raise ValueError(f"Expected one named dimethylglycine row in {sheet.title}")
    pairs = {time: {} for time in TIMES}
    for subject, state, time, value in zip(subjects, states, times, matches[0], strict=True):
        if time in pairs and state in {"Pre", "Post"}:
            by_subject = pairs[time].setdefault(subject, {})
            if state in by_subject or not isinstance(value, (float, int)) or value <= 0:
                raise ValueError("Unpaired, duplicated or nonpositive DMG abundance")
            by_subject[state] = value
    for time, by_subject in pairs.items():
        if len(by_subject) != 3 or any(set(pair) != {"Pre", "Post"} for pair in by_subject.values()):
            raise ValueError(f"Expected exactly three complete paired values at {time}")
        yield time, [(pair["Pre"], pair["Post"]) for pair in by_subject.values()]


def summary(pairs):
    pre, post = zip(*pairs, strict=True)
    change = [after - before for before, after in pairs]
    omitted = [
        mean(post[:i] + post[i + 1:]) / mean(pre[:i] + pre[i + 1:]) for i in range(len(pairs))
    ]
    # For a paired t statistic with two degrees of freedom the two-sided tail is analytic.
    variation = stdev(change)
    if variation:
        statistic = abs(mean(change)) * math.sqrt(3) / variation
        nominal_p = 1 - statistic / math.sqrt(statistic ** 2 + 2)
    else:
        nominal_p = 1.0 if mean(change) == 0 else 0.0
    return (mean(post) / mean(pre), median(after / before for before, after in pairs),
            min(omitted), max(omitted), sum(delta > 0 for delta in change), nominal_p)


def main(path):
    if hashlib.sha256(path.read_bytes()).hexdigest() != SOURCE_HASH:
        raise ValueError("Saito supplement archive fingerprint differs")
    with ZipFile(path) as archive:
        book = load_workbook(BytesIO(archive.read("Supplementary Materials.xlsx")),
                             read_only=True, data_only=True)
    output = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    output.writerow(("matrix", "hours", "pairs", "ratio_of_means", "median_paired_ratio",
                     "omit_min", "omit_max", "increased", "nominal_paired_t_p"))
    for matrix, sheet in (("CSF", "table S1"), ("plasma", "table S2")):
        for time, pairs in paired_values(book[sheet]):
            ratio, paired_median, lower, upper, increased, nominal_p = summary(pairs)
            output.writerow((matrix, time.split()[0], len(pairs), f"{ratio:.6g}",
                             f"{paired_median:.6g}", f"{lower:.6g}", f"{upper:.6g}",
                             increased, f"{nominal_p:.6g}"))
    book.close()


if __name__ == "__main__":
    main(Path(sys.argv[1]))
