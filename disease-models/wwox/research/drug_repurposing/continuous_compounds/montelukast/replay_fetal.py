"""Reproduce target detection in independent descriptive GSE155488 stage gates."""
import csv
import gzip
import hashlib
from pathlib import Path
import sys


def main(source):
    recorded_hash = "c3e3e6fa4190fa50b0101e3017ed022fb7457afe7dee0cb73bff04fe04e3b5eb"
    if hashlib.sha256(source.read_bytes()).hexdigest() != recorded_hash:
        raise ValueError("GSE155488 matrix fingerprint differs")
    markers = ("PDGFRA", "TCF7L2", "MBP")
    targets = ("GPR17", "CYSLTR1", "ALOX5", "ALOX5AP", "LTC4S")
    detected = {}
    depth = [0] * 359
    with gzip.open(source, "rt", newline="") as matrix:
        for gene, *values in csv.reader(matrix):
            positive = [float(value) > 0 for value in values]
            depth = [count + present for count, present in zip(depth, positive, strict=True)]
            if gene in markers or gene in targets:
                if gene in detected:
                    raise ValueError(f"Duplicate marker: {gene}")
                detected[gene] = positive

    columns = range(len(depth))
    mbp = detected["MBP"]
    transition = detected["TCF7L2"]
    precursor = detected["PDGFRA"]
    groups = {
        "all_columns": columns,
        "PDGFRA_positive_no_TCF7L2_or_MBP": [
            i for i in columns if precursor[i] and not transition[i] and not mbp[i]
        ],
        "TCF7L2_positive_MBP_negative": [i for i in columns if transition[i] and not mbp[i]],
        "MBP_positive": [i for i in columns if mbp[i]],
    }
    median = sorted(depth)[len(depth) // 2]
    output = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    output.writerow(("marker_gate", "depth_stratum", "columns", "gene", "positive"))
    for gate, members in groups.items():
        for stratum, subset in (
            ("all", members), (f"ge_median_{median}", [i for i in members if depth[i] >= median])
        ):
            for gene in targets:
                positives = sum(detected[gene][i] for i in subset) if gene in detected else "NA"
                output.writerow((gate, stratum, len(subset), gene, positives))


if __name__ == "__main__":
    main(Path(sys.argv[1]))
