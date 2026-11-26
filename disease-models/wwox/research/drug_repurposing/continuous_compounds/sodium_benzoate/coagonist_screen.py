"""Compare prespecified co-agonist handling genes across held WWOX RNA datasets."""

import argparse
from pathlib import Path
import sys

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "creatine"))
from assess import MODELS, assigned_nuclei, load_target, reference, tsv


PANEL = ("Dao", "Srr", "Slc1a4", "Slc1a5", "Slc7a10", "Slc6a9", "Gldc", "Amt", "Glyat")


def bulk_panel(files):
    mouse_reference, _ = reference(files)
    for model, accession, control_tag, knockout_tag in MODELS:
        human = model == "human_organoid"
        pattern = "*count_table.txt.gz" if human else "*TPM_Table.txt.gz"
        src, = (files / "geo" / accession).glob(pattern)
        genes = [gene.upper() for gene in PANEL] if human else PANEL
        libraries, abundance = load_target(src, genes, None if human else mouse_reference)
        ctrl = np.array([i for i, name in enumerate(libraries) if name.startswith(control_tag)])
        ko = np.array([i for i, name in enumerate(libraries) if name.startswith(knockout_tag)])
        if min(len(ctrl), len(ko)) < 2:
            raise ValueError(f"Insufficient libraries for the prespecified omissions in {accession}")
        for gene in genes:
            prefix = (model, accession, gene.upper(), len(ctrl), len(ko))
            if gene not in abundance:
                yield (*prefix, "", "", "", "", "", "", "", "unmapped")
                continue
            expression = abundance[gene]
            logged = np.log2(1 + expression)
            contrast = logged[ko].mean() - logged[ctrl].mean()
            omissions = [
                logged[ko[ko != omitted]].mean() - logged[ctrl[ctrl != omitted]].mean()
                for omitted in np.r_[ctrl, ko]
            ]
            yield (*prefix, np.count_nonzero(expression[ctrl]), np.count_nonzero(expression[ko]),
                   f"{expression[ctrl].mean():.6g}", f"{expression[ko].mean():.6g}",
                   f"{contrast:.6g}", f"{min(omissions):.6g}", f"{max(omissions):.6g}", "mapped")


def nuclei_panel(files):
    for pool, cell_class, depth, counts in assigned_nuclei(files, [], [], PANEL):
        total = int(depth.sum())
        for gene in PANEL:
            gene_umi = int(counts[gene].sum())
            yield (pool, cell_class, gene.upper(), len(depth), total, gene_umi, f"{1e6 * gene_umi / total:.6g}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    tsv(args.output / "contrasts.tsv",
        "model accession gene ctrl_n ko_n ctrl_positive ko_positive ctrl_mean ko_mean log2_delta omit_min omit_max mapping".split(),
        bulk_panel(args.files))
    tsv(args.output / "nuclei.tsv", "pool cell_class gene nuclei all_UMI gene_UMI CPM".split(), nuclei_panel(args.files))


if __name__ == "__main__":
    main()
