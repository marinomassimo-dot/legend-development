"""Reproduce selected GSE255033 organoid count contrasts from the public matrix."""
import csv
import gzip
import hashlib
import math
from pathlib import Path
import statistics
import sys


COUNTS_DIGEST = "6c31f0354202c43e6304bae112d616aad0fed621a98d64dc640d8d1f584a82fd"
METADATA_DIGEST = "cd13e7e1d611da6c4763f54e97879792f329dbcc521932d8cf4be4a40c45f710"
TARGETS = ("ADCY1", "CAMK2B", "DLG4", "GRIN2B", "GPR17", "CYSLTR1", "PDGFRA", "BCAS1", "MYRF", "MBP")


def read_columns(path):
    with gzip.open(path, "rt", newline="") as source:
        for row in csv.reader(source, delimiter="\t"):
            if not row:
                continue
            if row[0] == "!Sample_title":
                titles = row[1:]
            if row[0] == "!Sample_characteristics_ch1" and row[1].startswith("treatment: "):
                return dict(zip(titles, row[1:], strict=True))
    raise ValueError("Missing treatment metadata")


def main(geo):
    matrix = geo / "GSE255033_raw_count.csv.gz"
    meta = geo / "GSE255033_series_matrix.txt.gz"
    for file, expected in ((matrix, COUNTS_DIGEST), (meta, METADATA_DIGEST)):
        if hashlib.sha256(file.read_bytes()).hexdigest() != expected:
            raise ValueError(f"{file.name} fingerprint differs")
    by_title = read_columns(meta)
    totals = [0] * 15
    targets = {gene: [0] * 15 for gene in TARGETS}
    present = set()
    with gzip.open(matrix, "rt", newline="") as source:
        data = csv.reader(source)
        titles = next(data)[2:]
        arms = {condition: [i for i, title in enumerate(titles) if by_title[title] == condition]
                for condition in sorted(set(by_title.values()))}
        if len(arms) != 3 or any(len(indices) != 5 for indices in arms.values()):
            raise ValueError("Expected five pooled libraries in each of three arms")
        for _, gene, *row in data:
            counts = tuple(map(float, row))
            totals = [a + b for a, b in zip(totals, counts, strict=True)]
            if gene in targets:
                present.add(gene)
                targets[gene] = [a + b for a, b in zip(targets[gene], counts, strict=True)]

    output = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    output.writerow(("gene", "arm", "control_detected", "treated_detected", "control_mean_CPM",
                     "treated_mean_CPM", "log2_ratio_plus_one", "omit_min", "omit_max"))
    control = arms.pop("treatment: control")
    for gene, counts in targets.items():
        if gene not in present:
            for arm in arms:
                output.writerow((gene, arm, "NA", "NA", "NA", "NA", "NA", "NA", "NA"))
            continue
        cpm = [count * 1e6 / total for count, total in zip(counts, totals, strict=True)]
        for arm, treated in arms.items():
            def mean(indices, omit=None):
                return statistics.mean(cpm[i] for i in indices if i != omit)

            baseline = mean(control)
            response = mean(treated)
            full = math.log2((response + 1) / (baseline + 1))
            omitted = [math.log2((mean(treated, i) + 1) / (mean(control, i) + 1)) for i in control + treated]
            output.writerow((gene, arm.removeprefix("treatment: "), sum(counts[i] > 0 for i in control),
                             sum(counts[i] > 0 for i in treated), f"{baseline:.8g}", f"{response:.8g}",
                             f"{full:.8g}", f"{min(omitted):.8g}", f"{max(omitted):.8g}"))


if __name__ == "__main__":
    main(Path(sys.argv[1]))
