"""Check the flavin transport and synthesis steps in two further WWOX datasets."""
import csv
import gzip
import hashlib
from pathlib import Path
import sys
import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent.parent / 'perampanel_kainate_20261123'))
from p47t_analysis import contrast
from thiamine.cell_types import run as pooled_nuclei, tsv

GENES = ['Slc52a2', 'Rfk', 'Flad1', 'Slc25a32']

def adult(files):
    source = files / 'deepening_downloads/gse215425/GSE215425_processed_data.csv.gz'
    assert hashlib.sha256(source.read_bytes()).hexdigest() == 'd654f6bdd2a4ac5b3e24741f16962503a711575c72aa92a2c729a7a0cf04c18c'
    with gzip.open(source, 'rt') as stream:
        reader = csv.reader(stream, delimiter='\t')
        labels = next(reader)[2:]
        cols = [i for i, label in enumerate(labels) if label.startswith('HPC_')]
        names = [labels[i] for i in cols]
        assert len(set(names)) == len(names) == 10
        totals = np.zeros(len(names))
        counts = {}
        for _, gene, *row in reader:
            values = np.array([int(row[i]) for i in cols])
            totals += values
            if gene in GENES:
                counts[gene] = counts.get(gene, 0) + values
    assert set(counts) == set(GENES)
    groups = [(label.split('_')[1].split('/')[0], label.split('_')[2][0]) for label in names]
    rows = []
    for gene in GENES:
        logged = np.log2(1 + 1e6 * counts[gene] / totals)
        rows.append([gene, *contrast(logged, groups)])
    tsv(HERE / 'adult.tsv', 'gene sex_balanced_delta female_delta male_delta omit_min omit_max'.split(), rows)

if __name__ == '__main__':
    files = Path(sys.argv[1])
    adult(files)
    pooled_nuclei(files, GENES, HERE)
