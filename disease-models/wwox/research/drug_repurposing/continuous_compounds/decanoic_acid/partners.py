"""AMPA partner transcript balance in juvenile WWOX mouse hippocampal nuclei."""
from pathlib import Path
import sys
import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent / 'ganaxolone_20261123'))
from analyze import assigned_nuclei, tsv


def run(files, output):
    genes = ['Gria1', 'Gria2', 'Gria3']
    rows = []
    for arm, cell, depth, counts in assigned_nuclei(files, [], [], genes):
        if cell in {'exc', 'inh'}:
            for label, mask in [('all_assigned', np.ones(len(depth), dtype=bool)),
                                ('Gria2_detected', counts['Gria2'] > 0)]:
                a1, a2, a3 = [int(counts[g][mask].sum()) for g in genes]
                rows.append([arm, cell, label, int(mask.sum()), a1, a2, a3, a3 / (a1 + a3)])
    tsv(output, 'pool cell subset nuclei Gria1 Gria2 Gria3 Gria3_partner_fraction'.split(), rows)


if __name__ == '__main__':
    run(Path(sys.argv[1]), Path(sys.argv[2]))
