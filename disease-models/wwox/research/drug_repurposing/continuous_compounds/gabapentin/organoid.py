"""Week-15 THBS4 expression relative to individual lineage-associated transcripts."""
from pathlib import Path
import sys
import csv
import numpy as np

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here.parents[1] / 'ganaxolone_20261123'))
from analyze import load_target

files = Path(sys.argv[1])
source, = (files/'geo'/'GSE156243').glob('*count_table.txt.gz')
markers = 'GFAP AQP4 ALDH1L1 SLC1A3 FABP7 HOPX SNAP25'.split()
samples, counts = load_target(source, ['THBS4', *markers])
wt = [i for i,s in enumerate(samples) if s.startswith('cwt')]
ko = [i for i,s in enumerate(samples) if s.startswith('cko')]
assert len(wt)==2 and len(ko)==4
writer = csv.writer(sys.stdout, delimiter='\t', lineterminator='\n')
writer.writerow(['marker','wt_mean_CPM','ko_mean_CPM','marker_delta','ligand_minus_marker_delta',
                 'omit_one_low','omit_one_high','relative_delta_pseudocount_0.1','relative_delta_pseudocount_0.01'])
for marker in markers:
    reference = counts[marker]
    ligand = np.log2(1+counts['THBS4'])
    marker_log = np.log2(1+reference)
    relative = ligand - marker_log
    def difference(values, dropped=None):
        return np.mean([values[i] for i in ko if i!=dropped]) - np.mean([values[i] for i in wt if i!=dropped])
    omitted = [difference(relative,i) for i in wt+ko]
    row = [np.mean(reference[wt]),np.mean(reference[ko]),difference(marker_log),
           difference(relative),min(omitted),max(omitted)]
    for offset in (0.1, 0.01):
        row.append(difference(np.log2(offset+counts['THBS4'])-np.log2(offset+reference)))
    writer.writerow([marker,*[f'{v:.4f}' for v in row]])
