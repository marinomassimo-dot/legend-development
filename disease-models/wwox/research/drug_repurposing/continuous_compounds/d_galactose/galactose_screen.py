"""Replay the prespecified galactose panel in the held WWOX bulk datasets."""

import argparse
from pathlib import Path
import sys

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "creatine"))
from assess import MODELS, assigned_nuclei, load_target, reference, tsv


PANEL = (
    "Galk1", "Galt", "Gale", "Ugp2", "Pgm1", "Slc35a2", "Slc35a3",
    "B4galt1", "B4galt2", "C1galt1", "C1galt1c1", "Cog4", "Cog6", "Copb2",
    "Tmem165",
)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("nuclei_output", type=Path)
    args = parser.parse_args()
    mouse_reference, _ = reference(args.files)
    contrasts = []
    for model, accession, control_prefix, knockout_prefix in MODELS:
        human = model == "human_organoid"
        pattern = "*count_table.txt.gz" if human else "*TPM_Table.txt.gz"
        source, = (args.files / "geo" / accession).glob(pattern)
        targets = [gene.upper() for gene in PANEL] if human else PANEL
        libraries, expression = load_target(source, targets, None if human else mouse_reference)
        control = np.array([i for i, name in enumerate(libraries) if name.startswith(control_prefix)])
        knockout = np.array([i for i, name in enumerate(libraries) if name.startswith(knockout_prefix)])
        if len(control) < 2 or len(knockout) < 2:
            raise ValueError(f"{accession}: at least two libraries per group are needed")

        for gene in targets:
            row = (model, accession, gene.upper(), len(control), len(knockout))
            if gene not in expression:
                contrasts.append((*row, "", "", "", "unmapped"))
                continue
            values = np.log2(1 + expression[gene])
            delta = values[knockout].mean() - values[control].mean()
            omissions = [
                values[knockout[knockout != i]].mean() - values[control[control != i]].mean()
                for i in np.r_[control, knockout]
            ]
            contrasts.append((*row, f"{delta:.5f}", f"{min(omissions):.5f}", f"{max(omissions):.5f}", "mapped"))

    columns = "model accession target control_n knockout_n delta_log2 omit_min omit_max status".split()
    tsv(args.output, columns, contrasts)

    nuclear_targets = ("Galk1", "Slc35a2", "B4galt2", "C1galt1", "Cog6")
    nuclei = []
    for arm, cell_class, depth, counts in assigned_nuclei(args.files, [], [], nuclear_targets):
        for gene in nuclear_targets:
            if gene not in counts:
                continue
            total = int(depth.sum())
            gene_umi = int(counts[gene].sum())
            nuclei.append((arm, cell_class, gene.upper(), len(depth), total,
                           gene_umi, f"{gene_umi / total * 1e6:.5f}"))
    tsv(args.nuclei_output, "pool cell_class gene nuclei total_UMI gene_UMI CPM".split(), nuclei)


if __name__ == "__main__":
    main()
