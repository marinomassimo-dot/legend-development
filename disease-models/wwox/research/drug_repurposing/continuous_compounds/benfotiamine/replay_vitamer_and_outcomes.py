"""Replay published vitamer bars, trial aggregates and rat transporter assignment."""

import argparse
from pathlib import Path
import sys

COMPOUNDS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(COMPOUNDS / "sodium_benzoate"))
sys.path.insert(0, str(COMPOUNDS / "jbpos0101"))
from coagonist_screen import bulk_panel, tsv
from replay_exposure_and_receptors import verified, verified_expression

PANEL = ("Slc19a2", "Slc19a3", "Slc25a19", "Tpk1", "Tkt", "G6pdx", "Nfe2l2", "Gclm", "Nqo1", "Hmox1", "Acpp")

REFSEQ_HASH = "ecb179ede2293bebceb52ef7226be90eaaf83b58fa87b0caea9e08d9146dfd19"
TARGETS = {
    "NM_001007674.1": "Slc25a19",
    "NM_001432577.1": "Slc19a3",
    "NM_001432579.1": "Slc19a3",
    "NM_001030024.2": "Slc19a2",
    "BC079002.1": "Slc25a19",
}
# Printed in de Moraes et al. 2020 section 2.6. Both oligos are represented 5' to 3'.
OLIGOS = {
    "mTPPTr": ("CAGCGCACTTTGTATGTGGT", "AGGTTCCCTGTTTGCTGTAG"),
    "THTR1": ("GATGCTCCTACGTACTGCCC", "TGAAGACCTGTCTCCTGGTCA"),
}
# Source figures rendered by pdftoppm at longest edge 1600 px, then resized to 850 px wide.
# Tapias left/right crops: 295x385+96+76 and 305x385+455+76, each resized to 200%.
# Volvert crop: 290x435+115+160 resized to 180%.
# Y positions at zero, top tick, bar tops. Tapias groups ordered WT/WT BFT/TG/TG BFT.
BAR_COORDINATES = (
    ("Volvert_Fig4_liver", 359, 51, 300, (346, 339), (343, 337), (181, 114)),
    ("Volvert_Fig4_brain", 739, 428, 125, (714, 722), (722, 728), (539, 551)),
    ("Tapias_Fig3A_cortex", 380, 72, 125, (356, 346, 360, 352), (312, 270, 285, 317), (90, 198, 212, 181)),
    ("Tapias_Fig3B_hippocampus", 379, 65, 70, (337, 312, 331, 319), (271, 217, 228, 240), (133, 106, 154, 159)),
    ("Tapias_Fig3C_liver", 754, 449, 800, (748, 663, 746, 641), (707, 498, 704, 489), (684, 573, 686, 635)),
    ("Tapias_Fig3D_blood", 754, 451, 6000, (738, 660, 736, 681), (746, 635, 742, 664), (713, 473, 701, 598)),
)


def image_rows():
    for panel, zero, top, maximum, *bar_sets in BAR_COORDINATES:
        cohorts = ("Sv129",) if len(bar_sets[0]) == 2 else ("WT", "P301S")
        scale = maximum / (zero - top)
        for analyte, bars in zip(("thiamine", "ThMP", "ThDP"), bar_sets):
            for index, cohort in enumerate(cohorts):
                control_y, active_y = bars[2 * index:2 * index + 2]
                control, active = zero - control_y, zero - active_y
                yield (panel, cohort, analyte, zero, top, maximum, control_y, active_y, control * scale,
                       active * scale, active / control, (active - 2) / (control + 2),
                       (active + 2) / (control - 2))


def clinical_rows():
    # Ratios of group means, with different baseline, timepoints and available cases.
    rows = (
        ("Gibson_3C", "thiamine", 34, 36, 6.20, 999.51, 5.48, 13.64, None, None),
        ("Gibson_3C", "ThMP", 34, 36, 2.97, 20.73, 3.38, 4.05, None, None),
        ("Gibson_3C", "ThDP", 34, 36, 64.82, 197.39, 74.46, 91.70, None, None),
        ("BOND_5", "thiamine", 24, 27, 9.208, 336.273, 5.519, 22.208, 326.727, 16.875),
        ("BOND_5", "ThMP", 24, 27, 3.792, 12.091, 3.630, 4.000, 8.182, 0.292),
        ("BOND_5", "ThDP", 24, 27, 182, 374.636, 173.148, 211.208, 191.091, 40),
    )
    for study, analyte, n_active, n_placebo, ba, fa, bp, fp, da, dp in rows:
        active, placebo = fa / ba, fp / bp
        paired_active = "NA" if da is None else da / ba
        paired_placebo = "NA" if dp is None else dp / bp
        yield (study, analyte, n_active, n_placebo, ba, fa, bp, fp, active, placebo,
               active / placebo, paired_active, paired_placebo)


def assignment_rows(fasta):
    translation = str.maketrans("ACGT", "TGCA")
    for entry in fasta.strip().split(">")[1:]:
        header, *lines = entry.splitlines()
        accession = header.split()[0]
        sequence = "".join(lines).upper()
        for assay, (forward, reverse) in OLIGOS.items():
            reverse_target = reverse.translate(translation)[::-1]
            start = sequence.find(forward)
            candidates = []
            if start >= 0:
                # Search at most 500 nt downstream of the first exact forward hit.
                stop = min(len(sequence) - len(reverse_target) + 1, start + 500)
                for end in range(start + len(forward), stop):
                    window = sequence[end:end + len(reverse_target)]
                    differences = sum(left != right for left, right in zip(reverse_target, window))
                    candidates.append((differences, end, window[0] == reverse_target[0]))
            best = min(candidates, default=None)
            mismatch, final_base, size, terminal_match = ("NA", "NA", "NA", "NA")
            if best is not None:
                mismatch, end, terminal_match = best
                final_base = end + len(reverse_target)
                size = final_base - start
            yield (assay, accession, TARGETS[accession], sequence.count(forward),
                   sequence.count(reverse_target), start + 1 if start >= 0 else "NA",
                   mismatch, final_base, size, terminal_match)


def main(files, out):
    evidence = files / "deepening_downloads/benfotiamine_20261127"
    fasta = verified(evidence / "rat_thiamine_refseq.fasta", REFSEQ_HASH).decode()
    out.mkdir(parents=True, exist_ok=True)
    tables = (
        ("vitamer_figures.tsv", "panel genotype analyte zero_y top_y top_pmol_per_mg control_y bft_y control_pmol_per_mg bft_pmol_per_mg ratio min_ratio_2px max_ratio_2px", image_rows()),
        ("adult_blood_ratios.tsv", "table analyte n_active_label n_placebo_label active_baseline_nM active_month12_nM placebo_baseline_nM placebo_month12_nM active_ratio placebo_ratio ratio_of_ratios paired_delta_over_baseline_active paired_delta_over_baseline_placebo", clinical_rows()),
        ("rat_qpcr_assignment.tsv", "assay accession gene forward_exact reverse_complement_exact forward_start_1based best_reverse_mismatches candidate_end_1based candidate_span_nt reverse_3prime_base_match", assignment_rows(fasta)),
    )
    for name, header, rows in tables:
        tsv(out / name, header.split(), ([f"{v:.6g}" if isinstance(v, float) else v for v in row] for row in rows))
    verified_expression(files)
    tsv(out / "wwox_cofactor_and_redox.tsv",
        "model accession gene ctrl_n ko_n ctrl_positive ko_positive ctrl_mean ko_mean log2_delta omit_min omit_max mapping".split(),
        bulk_panel(files, PANEL, human_panel=("SLC19A2", "SLC19A3", "SLC25A19", "TPK1", "TKT",
                                             "G6PD", "NFE2L2", "GCLM", "NQO1", "HMOX1", "ACPP")))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", type=Path)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    main(args.files, args.out)
