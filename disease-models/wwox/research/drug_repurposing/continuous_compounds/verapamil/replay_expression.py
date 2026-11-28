"""Replay barrier and channel transcripts and within-library marker sensitivities."""
import argparse
from pathlib import Path
import sys

import numpy as np

COMPOUNDS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(COMPOUNDS / "cannabidivarin"))
sys.path.insert(0, str(COMPOUNDS / "creatine"))

from assess import MODELS, load_target, reference, tsv
from replay_trp_expression import compare_expression


def compare_marker_scaling(files, output):
    gene_map, _ = reference(files)
    results = []
    for model, accession, ctrl_prefix, null_prefix in MODELS:
        human = model == "human_organoid"
        transporter = "ABCB1" if human else "Abcb1a"
        markers = ("CLDN5", "PECAM1", "SLC2A1") if human else ("Cldn5", "Pecam1", "Slc2a1")
        pattern = "*count_table.txt.gz" if human else "*TPM_Table.txt.gz"
        source, = (files / "geo" / accession).glob(pattern)
        libraries, expression = load_target(source, [transporter, *markers],
                                           None if human else gene_map)
        control = [i for i, name in enumerate(libraries) if name.startswith(ctrl_prefix)]
        null = [i for i, name in enumerate(libraries) if name.startswith(null_prefix)]
        numerator = np.log2(1 + expression[transporter])
        for marker in markers:
            contrast = numerator - np.log2(1 + expression[marker])
            differences = []
            for omitted in [None, *control, *null]:
                wt = [i for i in control if i != omitted]
                ko = [i for i in null if i != omitted]
                differences.append(contrast[ko].mean() - contrast[wt].mean())
            results.append([model, transporter.upper(), marker.upper(), len(control),
                            len(null), differences[0], min(differences[1:]), max(differences[1:])])
    tsv(output, "model transporter marker ctrl_n null_n delta omit_min omit_max".split(), results)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("drug_repurposing", type=Path)
    parser.add_argument("files", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    targets = tuple("Abcb1a Abcb1b Abcg2 Cldn5 Pecam1 Slc2a1 Cacna1c Cacna1d".split())
    compare_expression(args.drug_repurposing, args.files, args.output, targets, "native_bulk.tsv",
                       human_symbols={"Abcb1a": "ABCB1"})
    compare_marker_scaling(args.files, args.output / "marker_sensitivity.tsv")
