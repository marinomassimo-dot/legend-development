"""Replay the separations between HTR2C RNA, splice geometry, and function."""
import argparse
from collections import Counter
import csv
import gzip
import json
from math import log2
from pathlib import Path
import re
from statistics import mean, median

from audit_htr2c_reads import EDIT_FIRST, reference


def expression(path):
    with gzip.open(path, "rt") as stream:
        rows = csv.DictReader(stream, delimiter="\t")
        samples = tuple(key for key in rows.fieldnames if key != "gene")
        counts = {}
        for row in rows:
            if row["gene"] in counts:
                raise ValueError(f"Duplicate gene symbol {row['gene']}")
            counts[row["gene"]] = {key: float(row[key]) for key in samples}
    totals = Counter()
    for values in counts.values():
        totals.update(values)
    normalized = {
        gene: {sample: 1e6 * values[sample] / totals[sample] for sample in samples}
        for gene, values in counts.items()
    }
    return counts, normalized


def means(values):
    return (mean(value for key, value in values.items() if key.startswith("cwt")),
            mean(value for key, value in values.items() if key.startswith("cko")))


def chromosome_countercheck(path, normalized):
    # Compare broad and control-expression-matched protein-coding genes.
    # This is descriptive for one edited clone. XIST is reported separately.
    labels = ("X", "autosome", "Xq23")
    ratios = {method: {label: [] for label in labels} for method in ("all_eligible", "WT_CPM_matched")}
    threshold, _ = means(normalized["HTR2C"])
    target = None
    for row in json.loads(path.read_text())["response"]["docs"]:
        symbol = row["symbol"]
        loc = row.get("location", "")
        chr_match = re.match(r"^(X|[1-9]|1[0-9]|2[0-2])[pq]", loc)
        if (row["status"] != "Approved" or row.get("locus_group") != "protein-coding gene"
                or not chr_match or symbol not in normalized):
            continue
        ctrl, ko = means(normalized[symbol])
        values = normalized[symbol]
        if not (ctrl >= 0.5 and all(values[key] > 0 for key in values if key.startswith("cwt"))
                and sum(values[key] > 0 for key in values if key.startswith("cko")) >= 3):
            continue
        log_ratio = log2((ko + 0.1) / (ctrl + 0.1))
        if symbol == "HTR2C":
            target = log_ratio
            continue
        groups = ("X", "Xq23") if loc.startswith("Xq23") else (
            "X" if chr_match[1] == "X" else "autosome",
        )
        for group in groups:
            ratios["all_eligible"][group].append(log_ratio)
            if threshold / 2 <= ctrl <= threshold * 2:
                ratios["WT_CPM_matched"][group].append(log_ratio)
    if target is None:
        raise ValueError("HTR2C was absent from the eligible annotated set")
    yield ("X_chromosome_countercheck", "HTR2C", "log2_ratio_PC_0.1", f"{target:.5f}")
    for method, groups in ratios.items():
        for label, values in groups.items():
            group = f"{method}_{label}"
            yield ("X_chromosome_countercheck", group, "gene_n", len(values))
            if values:
                yield ("X_chromosome_countercheck", group, "median_log2_ratio_PC_0.1", f"{median(values):.5f}")
                yield ("X_chromosome_countercheck", group, "fraction_at_least_HTR2C",
                       f"{sum(value >= target for value in values) / len(values):.5f}")
    for gene in ("XIST", "XACT", "TSIX"):
        if gene in normalized:
            ctrl, ko = means(normalized[gene])
            yield ("X_chromosome_countercheck", gene, "WT_CPM", f"{ctrl:.5f}")
            yield ("X_chromosome_countercheck", gene, "KO_CPM", f"{ko:.5f}")
        else:
            yield ("X_chromosome_countercheck", gene, "in_gene_table", "no")


def emit(args):
    yield ("data", "category", "quantity", "value")
    counts, normalized = expression(args.gene_counts)
    for sample, count in counts["HTR2C"].items():
        cpm = normalized["HTR2C"][sample]
        yield ("deposited_GSE156243", sample, "Salmon_estimated_gene_reads", f"{count:.3f}")
        yield ("deposited_GSE156243", sample, "CPM", f"{cpm:.5f}")
    wt, ko = means(normalized["HTR2C"])
    ratio = ko / wt
    yield ("deposited_GSE156243", "KO_over_WT", "group_mean_CPM_ratio", f"{ratio:.4f}")
    yield ("hypothetical_fixed_agonist_response", "KO_over_WT", "break_even_productive_surface_per_RNA", f"{1 / ratio:.4f}")
    yield from chromosome_countercheck(args.hgnc, normalized)

    full, exon_ends = reference(args.references / "NM_000868.4.gb")
    donor = exon_ends[-2]
    genome = json.loads((args.references / "hg38-htr2c-cassette.json").read_text())
    offset = 114848119 - 1 - genome["start"]
    genomic_slice = genome["dna"].upper().encode()
    cassette_length = donor - EDIT_FIRST + 1
    if genomic_slice[offset:offset + cassette_length] != full[EDIT_FIRST - 1:donor]:
        raise ValueError("GRCh38 and transcript editing-to-donor sequences disagree")
    intron = genomic_slice[offset + cassette_length:]
    next_exon = full[donor:]
    first_mismatch = next(i for i, (a, b) in enumerate(zip(intron, next_exon), 1) if a != b)
    yield ("productive_splice_geometry", "first_distinguishing_base", "minimum_nt", cassette_length + first_mismatch)
    for upstream, downstream in ((0, 1), (12, 12), (18, 12)):
        bases = donor - EDIT_FIRST + 1 + upstream + downstream
        yield ("productive_splice_geometry", f"flanks_{upstream}_{downstream}", "minimum_nt", bases)

    # Gumpper et al. 2022, Fig. 1D and Results. Lorcaserin in TRUPATH.
    for isoform, log_ec50 in (("INI", -7.77), ("VSV", -7.74), ("VGV", -6.37)):
        yield ("lorcaserin_Gq_TRUPATH", isoform, "EC50_nM", f"{1e9 * 10 ** log_ec50:.3f}")
        yield ("lorcaserin_Gq_TRUPATH", isoform, "EC50_ratio_to_INI", f"{10 ** (log_ec50 + 7.77):.3f}")

    # Olaghere da Silva et al. 2010, forebrain membrane site density.
    for genotype, bmax in (("WT", 163.3), ("VGV_X", 1754), ("VGV_Y", 4266)):
        yield ("mouse_forebrain_mesulergine", genotype, "Bmax_ratio_to_WT", f"{bmax / 163.3:.3f}")

    # These adult total-CSF peaks are scale markers only. The calculation asks
    # what increase in functional midpoint could reverse a 6.33x RNA difference
    # if protein/RNA, Hill slope and maximum effect were otherwise equal.
    for label, ng_per_ml in (("adult_total_CSF_lower_group", 12.287),
                             ("adult_total_CSF_upper_group", 30.357)):
        x = (1e3 * ng_per_ml / 295.33) / 42
        threshold = ratio + (ratio - 1) * x
        yield ("hypothetical_equal_surface_and_Emax", label, "break_even_KO_EC50_over_WT", f"{threshold:.3f}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("gene_counts", type=Path)
    parser.add_argument("references", type=Path)
    parser.add_argument("hgnc", type=Path)
    args = parser.parse_args()
    for row in emit(args):
        print("\t".join(map(str, row)))


if __name__ == "__main__":
    main()
