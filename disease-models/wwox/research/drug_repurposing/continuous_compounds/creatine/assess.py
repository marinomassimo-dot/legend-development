"""Recompute substrate, transporter and kinase contrasts from archived WWOX datasets."""
import argparse
import hashlib
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parent.parent
sys.path.insert(0, str(PROJECT / "ganaxolone_20261123"))
from analyze import assigned_nuclei, load_target, reference, tsv

MODELS = [
    ("mouse_cortex", "GSE158682", "CRTX_S_Ctrl_", "CRTX_S_KO_"),
    ("human_organoid", "GSE156243", "cwt", "cko"),
    ("mouse_hippocampus", "GSE158681", "S_Ctrl_", "S_KO_"),
]
GENES = ["Gatm", "Gamt", "Slc6a8", "Ckb"]


def composition(files):
    """Split the pooled difference in CPM using symmetric class weights and rates."""
    groups = {}
    rows = []
    for arm, cell, depth, values in assigned_nuclei(files, [], [], GENES):
        groups[arm, cell] = (depth.sum(), {g: values[g].sum() for g in GENES})
        for gene in GENES:
            rows.append([arm, cell, len(depth), int(depth.sum()), gene, int(values[gene].sum()),
                         int(np.count_nonzero(values[gene]))])
    tsv(HERE / "nuclei.tsv", "pool class nuclei all_UMI gene gene_UMI positive_nuclei".split(), rows)
    classes = sorted({cell for _, cell in groups})
    totals = {arm: sum(groups[arm, c][0] for c in classes) for arm in ("ctrl", "ko")}
    effects = []
    for gene in GENES:
        within = mixture = 0.0
        observed = {}
        for arm in totals:
            observed[arm] = 1e6 * sum(groups[arm, c][1][gene] for c in classes) / totals[arm]
        for c in classes:
            rate, weight = {}, {}
            for arm in totals:
                depth, counts = groups[arm, c]
                rate[arm] = 1e6 * counts[gene] / depth
                weight[arm] = depth / totals[arm]
            within += (rate["ko"] - rate["ctrl"]) * (weight["ko"] + weight["ctrl"]) / 2
            mixture += (weight["ko"] - weight["ctrl"]) * (rate["ko"] + rate["ctrl"]) / 2
        difference = observed["ko"] - observed["ctrl"]
        assert np.isclose(within + mixture, difference)
        effects.append([gene, observed["ctrl"], observed["ko"], difference, within, mixture])
    tsv(HERE / "composition.tsv", "gene ctrl_CPM ko_CPM difference within_class class_weights".split(), effects)


def run(files):
    gene_map, _ = reference(files)
    sources = [next((files / "reference_ensembl_r92").glob("*.fa.gz"))]
    contrasts, libraries = [], []
    for model, accession, wt_prefix, ko_prefix in MODELS:
        human = model == "human_organoid"
        pattern = "*count_table.txt.gz" if human else "*TPM_Table.txt.gz"
        source, = (files / "geo" / accession).glob(pattern)
        sources.append(source)
        symbols = [g.upper() if human else g for g in GENES]
        names, values = load_target(source, symbols, None if human else gene_map)
        wt = [i for i, n in enumerate(names) if n.startswith(wt_prefix)]
        ko = [i for i, n in enumerate(names) if n.startswith(ko_prefix)]
        assert len(wt) >= 2 and len(ko) >= 2 and set(symbols) == set(values)
        for symbol, expr in values.items():
            logged = np.log2(1 + expr)
            def change(omit):
                return np.mean([logged[i] for i in ko if i != omit]) - np.mean([logged[i] for i in wt if i != omit])
            omissions = [change(i) for i in wt + ko]
            contrasts.append([model, symbol.upper(), len(wt), len(ko), np.mean(expr[wt]), np.mean(expr[ko]),
                              change(None), min(omissions), max(omissions)])
            for i in wt + ko:
                libraries.append([model, names[i], "WT" if i in wt else "KO", symbol.upper(), expr[i]])
    tsv(HERE / "contrasts.tsv", "model gene WT_n KO_n WT_mean KO_mean delta_log2 omit_min omit_max".split(), contrasts)
    tsv(HERE / "libraries.tsv", "model library group gene expression".split(), libraries)
    composition(files)
    sources.extend(sorted((files / "geo" / "GSE158684").glob("*filtered_*gz")))
    tsv(HERE / "inputs.tsv", ["filename", "sha256"], [(f.name, hashlib.sha256(f.read_bytes()).hexdigest()) for f in sources])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", type=Path)
    run(parser.parse_args().files)
