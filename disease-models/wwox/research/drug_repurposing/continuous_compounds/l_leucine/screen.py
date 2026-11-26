"""Compare the predeclared L-leucine panel in held WWOX bulk expression."""
import argparse
import hashlib
from pathlib import Path
import sys

import numpy as np

# The held archives use Lars/LARS for the current cytosolic LARS1 symbol.
INPUT_ALIASES = {"Lars1": "Lars"}
GENES = ("Slc7a5", "Slc3a2", "Sesn2", "Lars1", "Bcat1", "Bcat2",
         "Bckdha", "Bckdhb", "Dbt", "Dld", "Bckdk", "Ppm1k")


def run(repo, files, output):
    continuous = repo / "disease-models/wwox/research/drug_repurposing/continuous_compounds"
    sys.path.insert(0, str(continuous / "creatine"))
    from assess import MODELS, assigned_nuclei, load_target, reference, tsv

    mouse_reference, _ = reference(files)
    reference_source, = (files / "reference_ensembl_r92").glob("*.fa.gz")
    sources = [reference_source]
    results = []
    for model, accession, wt_prefix, ko_prefix in MODELS:
        human = model == "human_organoid"
        pattern = "*count_table.txt.gz" if human else "*TPM_Table.txt.gz"
        source, = (files / "geo" / accession).glob(pattern)
        sources.append(source)
        input_symbols = [INPUT_ALIASES.get(gene, gene) for gene in GENES]
        if human:
            input_symbols = [gene.upper() for gene in input_symbols]
        names, values = load_target(source, input_symbols, None if human else mouse_reference)
        wt = [i for i, name in enumerate(names) if name.startswith(wt_prefix)]
        ko = [i for i, name in enumerate(names) if name.startswith(ko_prefix)]
        assert len(wt) >= 2 and len(ko) >= 2
        for gene, input_symbol in zip(GENES, input_symbols, strict=True):
            if input_symbol not in values:
                results.append([model, gene.upper(), input_symbol, len(wt), len(ko),
                                "", "", "", "", "", "unmapped"])
                continue
            abundance = values[input_symbol]
            logged = np.log2(1 + abundance)
            delta = np.mean(logged[ko]) - np.mean(logged[wt])
            omitted = [
                np.mean(logged[[i for i in ko if i != excluded]])
                - np.mean(logged[[i for i in wt if i != excluded]])
                for excluded in wt + ko
            ]
            results.append([
                model, gene.upper(), input_symbol, len(wt), len(ko),
                f"{np.mean(abundance[wt]):.5f}", f"{np.mean(abundance[ko]):.5f}",
                f"{delta:.5f}", f"{min(omitted):.5f}", f"{max(omitted):.5f}", "mapped",
            ])
    output.mkdir(parents=True, exist_ok=True)
    tsv(output / "contrasts.tsv",
        "model gene input_symbol WT_n KO_n WT_mean KO_mean delta_log2 omit_min omit_max status".split(), results)
    nuclear_genes = [INPUT_ALIASES.get(gene, gene) for gene in GENES]
    nuclear_rows = []
    for arm, cell_class, depth, values in assigned_nuclei(files, [], [], nuclear_genes):
        total_umi = int(depth.sum())
        for gene, input_symbol in zip(GENES, nuclear_genes, strict=True):
            detected = values[input_symbol]
            gene_umi = int(detected.sum())
            nuclear_rows.append([
                arm, cell_class, gene.upper(), len(depth), total_umi, gene_umi,
                int(np.count_nonzero(detected)), f"{1e6 * gene_umi / total_umi:.5f}",
            ])
    tsv(output / "nuclei.tsv",
        "pool cell_class gene nuclei all_UMI gene_UMI positive_nuclei CPM".split(), nuclear_rows)
    sources.extend(sorted((files / "geo" / "GSE158684").glob("*filtered_*gz")))
    tsv(output / "inputs.tsv", ["input", "sha256"],
        [(str(path.relative_to(files)), hashlib.sha256(path.read_bytes()).hexdigest()) for path in sources])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo", type=Path)
    parser.add_argument("files", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    run(args.repo, args.files, args.output)
