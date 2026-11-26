"""Compare the predeclared D-mannose and Golgi panel in held WWOX bulk datasets."""
import argparse
import hashlib
from pathlib import Path
import sys

import numpy as np


MOUSE_ALIASES = {"Man1a1": "Man1a"}
PANEL = ("Hk1", "Hk2", "Mpi", "Pmm2", "Gmppa", "Gmppb", "Dpagt1", "Dpm1",
         "Man1a1", "Man2a1", "Cog4", "Cog6", "Copb2", "C1galt1", "C1galt1c1")


def run(repository, files, output):
    shared = repository / "disease-models/wwox/research/drug_repurposing/continuous_compounds/creatine"
    sys.path.insert(0, str(shared))
    from assess import MODELS, assigned_nuclei, load_target, reference, tsv

    reference_map, _ = reference(files)
    reference_path, = (files / "reference_ensembl_r92").glob("*.fa.gz")
    sources = [reference_path]
    contrasts = []
    for model, accession, ctrl_prefix, ko_prefix in MODELS:
        human = model == "human_organoid"
        pattern = "*count_table.txt.gz" if human else "*TPM_Table.txt.gz"
        data, = (files / "geo" / accession).glob(pattern)
        sources.append(data)
        genes = [gene.upper() if human else MOUSE_ALIASES.get(gene, gene) for gene in PANEL]
        libraries, measured = load_target(data, genes, None if human else reference_map)
        ctrl = np.array([i for i, name in enumerate(libraries) if name.startswith(ctrl_prefix)])
        ko = np.array([i for i, name in enumerate(libraries) if name.startswith(ko_prefix)])
        assert len(ctrl) >= 2 and len(ko) >= 2
        for target, gene in zip(PANEL, genes, strict=True):
            row = (model, target.upper(), gene, len(ctrl), len(ko))
            if gene not in measured:
                contrasts.append((*row, "", "", "", "unmapped"))
                continue
            counts = np.log2(1 + measured[gene])
            delta = counts[ko].mean() - counts[ctrl].mean()
            omit = [
                counts[ko[ko != i]].mean() - counts[ctrl[ctrl != i]].mean()
                for i in np.r_[ctrl, ko]
            ]
            contrasts.append((*row, f"{delta:.5f}", f"{min(omit):.5f}", f"{max(omit):.5f}", "mapped"))
    output.mkdir(exist_ok=True, parents=True)
    tsv(output / "contrasts.tsv", "model target input_symbol ctrl_n ko_n delta_log2 omit_min omit_max status".split(), contrasts)
    stable_targets = ("Gmppb", "Dpm1", "Cog4", "Cog6")
    nuclear = []
    for arm, cell, depth, values in assigned_nuclei(files, [], [], stable_targets):
        library_depth = int(depth.sum())
        for gene in stable_targets:
            gene_umi = int(values[gene].sum())
            nuclear.append((arm, cell, gene.upper(), len(depth), library_depth,
                            gene_umi, int(np.count_nonzero(values[gene])),
                            f"{1e6 * gene_umi / library_depth:.5f}"))
    tsv(output / "nuclei.tsv", "pool cell_class gene nuclei all_UMI gene_UMI positive_nuclei CPM".split(), nuclear)
    sources.extend(sorted((files / "geo" / "GSE158684").glob("*filtered_*gz")))
    tsv(output / "inputs.tsv", ("filename", "sha256"),
        [(path.relative_to(files), hashlib.sha256(path.read_bytes()).hexdigest()) for path in sources])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repository", type=Path)
    parser.add_argument("files", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    run(args.repository, args.files, args.output)
