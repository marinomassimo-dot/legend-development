"""Exploratory comparison to three compartment markers, using the same six organoid libraries."""
from pathlib import Path
import sys
import numpy as np
from transport import HERE
sys.path.insert(0, str(HERE.parent.parent / 'ganaxolone_20261123'))
from analyze import load_target, tsv

files, out = map(Path, sys.argv[1:])
source, = (files / 'geo/GSE156243').glob('*count_table.txt.gz')
targets = ['FOLR1', 'SLC46A1', 'SLC19A1', 'MTHFS']
markers = ['TTR', 'AQP1', 'OTX2']
names, counts = load_target(source, targets + markers)
samples = [i for i, name in enumerate(names) if name.startswith(('cwt', 'cko'))]
rows = []
for marker in markers:
    for target in targets:
        scores = np.log2(1 + counts[target]) - np.log2(1 + counts[marker])
        def effect(skip=None):
            def mean(prefix):
                return np.mean([scores[i] for i in samples if i != skip and names[i].startswith(prefix)])
            return mean('cko') - mean('cwt')
        omissions = [effect(i) for i in samples]
        rows.append([target, marker, effect(), min(omissions), max(omissions)])
tsv(out, 'target context_marker delta_relative omit_min omit_max'.split(), rows)
