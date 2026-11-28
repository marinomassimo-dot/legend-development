"""Compare the prespecified calcium-handling panel in held WWOX RNA datasets."""

import argparse
from pathlib import Path
import sys

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "creatine"))
from assess import MODELS, assigned_nuclei, load_target, reference, tsv


PANEL = ("Ryr1", "Ryr2", "Ryr3", "Itpr1", "Itpr2", "Atp2a2", "Mcu", "Mcub", "Micu1", "Micu2")


def pool_decomposition(groups):
    classes = sorted(key[1] for key in groups if key[0] == "ctrl")
    rows = []
    for gene in ("Ryr2", "Ryr3", "Micu2"):
        for removed in [None, *classes]:
            retained = [name for name in classes if name != removed]
            totals = {arm: sum(groups[arm, name][0] for name in retained) for arm in ("ctrl", "ko")}
            pooled = {arm: 1e6 * sum(groups[arm, name][1][gene] for name in retained) / totals[arm]
                      for arm in totals}
            effect = pooled["ko"] - pooled["ctrl"]
            within = mixture = 0
            for name in retained:
                c_depth, ctrl = groups["ctrl", name]
                k_depth, ko = groups["ko", name]
                c_rate, k_rate = 1e6 * ctrl[gene] / c_depth, 1e6 * ko[gene] / k_depth
                c_weight, k_weight = c_depth / totals["ctrl"], k_depth / totals["ko"]
                within += (k_rate - c_rate) * (k_weight + c_weight) / 2
                mixture += (k_weight - c_weight) * (k_rate + c_rate) / 2
            assert np.isclose(effect, within + mixture)
            estimates = (pooled["ctrl"], pooled["ko"], effect, within, mixture)
            rows.append((gene.upper(), removed or "none", *(f"{x:.5f}" for x in estimates)))
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    mouse_reference, _ = reference(args.files)
    args.output.mkdir(parents=True, exist_ok=True)
    bulk = []
    for model, accession, control_tag, knockout_tag in MODELS:
        human = model == "human_organoid"
        pattern = "*count_table.txt.gz" if human else "*TPM_Table.txt.gz"
        source, = (args.files / "geo" / accession).glob(pattern)
        genes = [gene.upper() for gene in PANEL] if human else PANEL
        names, abundance = load_target(source, genes, None if human else mouse_reference)
        control = np.array([i for i, name in enumerate(names) if name.startswith(control_tag)])
        knockout = np.array([i for i, name in enumerate(names) if name.startswith(knockout_tag)])
        if min(len(control), len(knockout)) < 2:
            raise ValueError(f"Insufficient libraries for omissions in {accession}")
        for gene in genes:
            header = (model, accession, gene.upper(), len(control), len(knockout))
            if gene not in abundance:
                bulk.append((*header, "", "", "", "unmapped"))
                continue
            logged = np.log2(1 + abundance[gene])
            observed = logged[knockout].mean() - logged[control].mean()
            omissions = [
                logged[knockout[knockout != i]].mean() - logged[control[control != i]].mean()
                for i in np.r_[control, knockout]
            ]
            values = tuple(f"{value:.5f}" for value in (observed, min(omissions), max(omissions)))
            bulk.append((*header, *values, "mapped"))
    tsv(args.output / "contrasts.tsv", "model accession gene ctrl_n ko_n delta_log2 omit_min omit_max mapping".split(), bulk)

    nuclei = []
    groups = {}
    for arm, cell_class, depth, counts in assigned_nuclei(args.files, [], [], PANEL):
        total = int(depth.sum())
        gene_counts = {gene: int(counts[gene].sum()) for gene in PANEL}
        groups[arm, cell_class] = (total, gene_counts)
        for gene in PANEL:
            gene_umi = gene_counts[gene]
            nuclei.append((arm, cell_class, gene.upper(), len(depth), total, gene_umi,
                           f"{gene_umi / total * 1e6:.5f}"))
    tsv(args.output / "nuclei.tsv", "pool cell_class gene nuclei all_UMI gene_UMI CPM".split(), nuclei)
    tsv(args.output / "composition.tsv",
        "gene omitted_class ctrl_CPM ko_CPM delta_CPM within_classes_CPM class_weights_CPM".split(),
        pool_decomposition(groups))


if __name__ == "__main__":
    main()
