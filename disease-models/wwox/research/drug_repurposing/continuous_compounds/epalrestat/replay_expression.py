"""Replay WWOX aldose reductase, sorbitol consumption and redox contrasts."""
import argparse
import csv
from pathlib import Path
import sys

import numpy as np


PANEL = {
    "Akr1b3": "AKR1B1", "Sord": "SORD", "G6pdx": "G6PD", "Pgd": "PGD",
    "Gpi1": "GPI", "Hk2": "HK2", "Mpi": "MPI", "Pmm2": "PMM2", "Gmppb": "GMPPB",
    "Aldoa": "ALDOA", "Gsr": "GSR", "Nqo1": "NQO1",
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("drug_repurposing", type=Path)
    parser.add_argument("files", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    compounds = args.drug_repurposing / "continuous_compounds"
    sys.path.insert(0, str(compounds / "creatine"))
    from assess import MODELS, assigned_nuclei, load_target, reference, tsv
    sys.path.insert(0, str(compounds / "copper_histidinate"))
    from replay_copper_comparison import verify

    with (args.drug_repurposing / "memantine_magnesium_20261123" / "inputs.tsv").open() as stream:
        hashes = {row["input"]: row["sha256"] for row in csv.DictReader(stream, delimiter="\t")}
    genome, = (args.files / "reference_ensembl_r92").glob("*.fa.gz")
    verify(genome, hashes)
    transcripts, _ = reference(args.files)
    bulk = []
    for model, accession, wt_prefix, ko_prefix in MODELS:
        human = model == "human_organoid"
        source, = (args.files / "geo" / accession).glob(
            "*count_table.txt.gz" if human else "*TPM_Table.txt.gz")
        verify(source, hashes)
        symbols = list(PANEL.values()) if human else list(PANEL)
        names, mapped = load_target(source, symbols, None if human else transcripts)
        wt = np.array([i for i, name in enumerate(names) if name.startswith(wt_prefix)])
        ko = np.array([i for i, name in enumerate(names) if name.startswith(ko_prefix)])
        for symbol, report_gene in zip(symbols, PANEL.values(), strict=True):
            values = np.log2(1 + mapped[symbol])
            contrast = values[ko].mean() - values[wt].mean()
            omissions = [values[ko[ko != i]].mean() - values[wt[wt != i]].mean()
                         for i in np.r_[wt, ko]]
            bulk.append((model, report_gene, symbol, len(wt), len(ko), f"{contrast:.5f}",
                         f"{min(omissions):.5f}", f"{max(omissions):.5f}"))

    target_nuclei = ("Akr1b3", "Sord", "G6pdx", "Pgd", "Gmppb")
    for arm in ("ctrl", "ko"):
        for suffix in ("features.tsv.gz", "matrix.mtx.gz"):
            verify(args.files / "geo" / "GSE158684" / f"GSE158684_{arm}_filtered_{suffix}", hashes)
    nuclear = []
    for arm, cell, depth, counts in assigned_nuclei(args.files, [], [], target_nuclei):
        for gene in target_nuclei:
            umi = int(counts[gene].sum())
            total = int(depth.sum())
            nuclear.append((arm, cell, PANEL[gene], len(depth), total, umi,
                            int(np.count_nonzero(counts[gene])), f"{1e6 * umi / total:.5f}"))
    args.output.mkdir(parents=True, exist_ok=True)
    tsv(args.output / "expression.tsv",
        "model gene source_symbol wt_n ko_n log2_delta omit_min omit_max".split(), bulk)
    tsv(args.output / "nuclei.tsv",
        "pool class gene n_nuclei total_umi gene_umi positive_nuclei CPM".split(), nuclear)


if __name__ == "__main__":
    main()
