"""Descriptive transporter and GABA-synthesis contrasts in archived WWOX datasets."""
from pathlib import Path
import sys
import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'creatine'))
from assess import MODELS, load_target, reference, tsv

GENES = 'Gad1 Gad2 Slc6a6 Slc12a5 Slc12a2 Wnk1 Stk39 Oxsr1'.split()

def run(files):
    mouse_map, _ = reference(files)
    rows, libraries = [], []
    for model, accession, wt_prefix, ko_prefix in MODELS:
        human = model == 'human_organoid'
        pattern = '*count_table.txt.gz' if human else '*TPM_Table.txt.gz'
        source, = (files / 'geo' / accession).glob(pattern)
        genes = [gene.upper() if human else gene for gene in GENES]
        names, measured = load_target(source, genes, None if human else mouse_map)
        assert set(genes) == set(measured)
        wt = [i for i, name in enumerate(names) if name.startswith(wt_prefix)]
        ko = [i for i, name in enumerate(names) if name.startswith(ko_prefix)]
        assert len(wt) > 1 and len(ko) > 1
        values = {symbol.upper(): np.log2(1 + expr) for symbol, expr in measured.items()}
        values['KCC2_minus_NKCC1'] = values['SLC12A5'] - values['SLC12A2']
        for target, x in values.items():
            def delta(omit):
                return np.mean([x[i] for i in ko if i != omit]) - np.mean([x[i] for i in wt if i != omit])
            omitted = [delta(i) for i in wt + ko]
            rows.append([model, target, len(wt), len(ko), delta(None), min(omitted), max(omitted)])
            libraries.extend([model, target, names[i], 'WT' if i in wt else 'KO', x[i]] for i in wt + ko)
    tsv(HERE/'transcripts.tsv', 'model target wt_n ko_n delta_log2 omit_min omit_max'.split(), rows)
    tsv(HERE/'transcript_libraries.tsv', 'model target library arm log2_measure'.split(), libraries)

if __name__ == '__main__':
    run(Path(sys.argv[1]))
