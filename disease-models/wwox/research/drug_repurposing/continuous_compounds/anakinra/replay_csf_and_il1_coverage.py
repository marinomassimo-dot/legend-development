"""Replay anakinra exposure contrasts and WWOX IL-1 expression coverage."""

import argparse
import csv
from pathlib import Path
from statistics import mean, stdev
import sys


HERE = Path(__file__).resolve().parent
MOLAR_MASS_KDA = 17.3
GENES = (
    "Il1a", "Il1b", "Il1rn", "Il1r1", "Il1rap", "Il1r2", "Sigirr",
    "Nlrp3", "Casp1", "Pycard", "Gsdmd", "Tlr4",
)


def exposure_rows():
    # Goldbach-Mansky Table 3 and EMA assessment p. 15 use IL-1Ra standards.
    for source, baseline, month_three in (
        ("NOMID article", 211, 1136), ("NOMID EMA", 15.7, 797)
    ):
        for visit, value in (("Baseline", baseline), ("Month 3", month_three)):
            yield source, visit, "CSF measured immunoreactivity", value, "pg/mL"
            yield source, visit, "Recombinant mass equivalent", f"{value / MOLAR_MASS_KDA:.2f}", "pM equivalent"
    yield "NOMID article", "Month 3", "CSF/serum quotient of marginal medians", f"{100 * 1136 / 43237:.3f}", "%"

    # Fox Table 1 uses two repeated periods in two of the three adult rhesus macaques.
    times = (
        ("0–24 h", (59, 26, 158, 148, 164), (14900, 17400, 59900, 44700, 68300)),
        ("0–∞", (60, 27, 166, 152, 175), (14900, 17400, 59900, 44800, 69800)),
    )
    for window, csf, serum in times:
        ratios = [100 * c / s for c, s in zip(csf, serum, strict=True)]
        yield "Fox Table 1", window, "Mean CSF/serum AUC", f"{mean(ratios):.3f}", "%"
        yield "Fox Table 1", window, "SD, five periods in three animals", f"{stdev(ratios):.3f}", "%"
    yield "Fox Table 1", "Column as printed", "Mean printed AUC ratios", f"{mean((.40, .15, .26, .34, .24)):.3f}", "%"

    for assay, ligand, half_maximal in (
        ("MRC5, 20 h IL-6", 5.8, 45), ("Whole blood, 6 h IL-8", 100, 603)
    ):
        yield "Owyang Fig. 5", assay, "Nominal IL-1β challenge", ligand, "pM"
        yield "Owyang Fig. 5", assay, "Anakinra IC50", half_maximal, "pM"
        yield "Owyang Fig. 5", assay, "Anakinra IC50 mass", f"{half_maximal * MOLAR_MASS_KDA:.1f}", "pg/mL"
    yield "Owyang Fig. 5", "Blood / MRC5", "Apparent IC50 ratio", f"{603 / 45:.2f}", "fold"

    # Tomasoni Fig. 4 uses different nominal exposures for spine imaging and mEPSCs.
    for culture_ng_ml in (20, 100):
        for source, csf_ng_ml in (("NOMID article", 1.136), ("NOMID EMA", .797)):
            label = f"{culture_ng_ml} ng/mL culture vs {source}"
            yield "Tomasoni Fig. 4", label, "Culture / CSF immunoreactivity", f"{culture_ng_ml / csf_ng_ml:.2f}", "fold"

    # Helmy Table 3 reports pooled time epochs during repeat treatment.
    control_before, treated_before = 24.3, 78.8
    for label, control, treated in (
        ("6 h column", 27.6, 123.6), ("12 h column", 23.4, 138.3), ("18 h column", 23.1, 125.0)
    ):
        difference = (treated - treated_before) - (control - control_before)
        yield "Helmy Table 3", label, "Descriptive change contrast", f"{difference:.1f}", "pg/mL"


def expression_replay(files, out):
    sys.path[:0] = [str(HERE.parent / "jbpos0101"), str(HERE.parent.parent / "ganaxolone_20261123")]
    from replay_exposure_and_receptors import bulk_panel, tsv, verified_expression
    from analyze import assigned_nuclei

    verified_expression(files)
    out.mkdir(parents=True, exist_ok=True)
    tsv(out / "juvenile_bulk.tsv",
        "model accession gene ctrl_n ko_n ctrl_positive ko_positive ctrl_mean ko_mean log2_delta omit_min omit_max mapping".split(),
        bulk_panel(files, GENES))
    rows = []
    for arm, cell, depth, counts in assigned_nuclei(files, [], [], GENES):
        denominator = int(depth.sum())
        for gene in GENES:
            umi = int(counts[gene].sum())
            positive = int((counts[gene] > 0).sum())
            rows.append((arm, cell, gene, len(depth), denominator, umi, positive, 1e6 * umi / denominator))
    tsv(out / "juvenile_nuclei.tsv", "pool class gene nuclei total_UMI gene_UMI positive CPM".split(), rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--expression", type=Path, help="Root of held expression and annotation files")
    parser.add_argument("--out", type=Path, default=HERE, help="Output folder for the two RNA tables")
    args = parser.parse_args()
    if args.expression is not None:
        expression_replay(args.expression, args.out)
    else:
        writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
        writer.writerow(("source", "condition", "measure", "value", "unit"))
        writer.writerows(exposure_rows())


if __name__ == "__main__":
    main()
