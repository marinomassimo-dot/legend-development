"""Measure sensitivity of the SLC16A7 RNA result to three neuronal reference genes."""
from pathlib import Path
import sys

import numpy as np

# Execute from the root of the SCI_CODEX checkout.
sys.path.insert(0, str(Path.cwd() / 'disease-models/wwox/research/drug_repurposing/continuous_compounds/creatine'))
from assess import MODELS, load_target, reference, tsv


def run(files, output):
    genes = ['Slc16a7', 'Snap25', 'Rbfox3', 'Map2']
    mapping, _ = reference(files)
    rows = []
    for model, accession, wt_prefix, ko_prefix in MODELS:
        human = model == 'human_organoid'
        symbols = [gene.upper() if human else gene for gene in genes]
        pattern = '*count_table.txt.gz' if human else '*TPM_Table.txt.gz'
        source, = (files / 'geo' / accession).glob(pattern)
        names, values = load_target(source, symbols, None if human else mapping)
        wt = [i for i, name in enumerate(names) if name.startswith(wt_prefix)]
        ko = [i for i, name in enumerate(names) if name.startswith(ko_prefix)]
        logged = np.array([np.log2(1 + values[gene]) for gene in symbols])
        references = dict(zip(symbols[1:], logged[1:]))
        references['reference_geomean'] = logged[1:].mean(axis=0)
        for label, background in references.items():
            ratio = logged[0] - background

            def delta(omitted=None):
                control = [i for i in wt if i != omitted]
                knockout = [i for i in ko if i != omitted]
                return ratio[knockout].mean() - ratio[control].mean()

            omissions = [delta(i) for i in wt + ko]
            rows.append([model, label, delta(), min(omissions), max(omissions)])
    tsv(output, ['model', 'reference', 'delta_log_ratio', 'omit_min', 'omit_max'], rows)


if __name__ == '__main__':
    run(Path(sys.argv[1]), Path(__file__).with_suffix('.tsv'))
