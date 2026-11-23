"""Reproduce the WWOX thiamine and PDH contrasts with leave-one-library-out bounds."""
from pathlib import Path
import sys
import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'creatine'))
from assess import MODELS, load_target, reference, tsv

GENES = 'Slc19a2 Slc19a3 Tpk1 Slc25a19 Pdha1 Pdhb Dlat Dld Pdk1 Pdk2 Pdk3 Pdk4 Ogdh Tkt'.split()

def run(files, target_genes=GENES, output=HERE / 'screen.tsv', human_symbols=None):
    gene_map, _ = reference(files)
    rows = []
    for model, accession, wt_prefix, ko_prefix in MODELS:
        human = model == 'human_organoid'
        genes = [(human_symbols or {}).get(g, g.upper()) if human else g for g in target_genes]
        source, = (files / 'geo' / accession).glob('*count_table.txt.gz' if human else '*TPM_Table.txt.gz')
        names, measured = load_target(source, genes, None if human else gene_map)
        wt = [i for i, name in enumerate(names) if name.startswith(wt_prefix)]
        ko = [i for i, name in enumerate(names) if name.startswith(ko_prefix)]
        assert len(wt) > 1 and len(ko) > 1
        for g in genes:
            if g not in measured:
                rows.append([model, accession, g.upper(), len(wt), len(ko), 'unmapped', '', '', '', '', ''])
                continue
            expr = measured[g]
            log_values = np.log2(1 + expr)
            def delta(omitted=None):
                a = [i for i in wt if i != omitted]
                b = [i for i in ko if i != omitted]
                return log_values[b].mean() - log_values[a].mean()
            omissions = [delta(i) for i in wt + ko]
            rows.append([model, accession, g.upper(), len(wt), len(ko), 'mapped', expr[wt].mean(),
                         expr[ko].mean(), delta(), min(omissions), max(omissions)])
    tsv(output, 'model accession gene wt_n ko_n mapping wt_mean ko_mean delta omit_min omit_max'.split(), rows)

if __name__ == '__main__':
    run(Path(sys.argv[1]))
