"""Count all entries for Slc5a3 in the deposited matrices before cell classification."""
import csv
import gzip
from pathlib import Path
import sys

source = Path(sys.argv[1]) / 'geo/GSE158684'
with Path(sys.argv[2]).open('w') as stream:
    writer = csv.writer(stream, delimiter='\t', lineterminator='\n')
    writer.writerow(['pool', 'feature_id', 'all_matrix_barcodes', 'nonzero_entries', 'UMI'])
    for arm in ['ctrl', 'ko']:
        prefix = f'GSE158684_{arm}_filtered_'
        with gzip.open(source / (prefix + 'features.tsv.gz'), 'rt') as features:
            matches = [(index, row[0]) for index, row in enumerate(csv.reader(features, delimiter='\t'), 1)
                       if row[1] == 'Slc5a3']
        (index, feature_id), = matches
        with gzip.open(source / (prefix + 'matrix.mtx.gz'), 'rt') as matrix:
            dim = next(line for line in matrix if not line.startswith('%'))
            n_barcodes = int(dim.split()[1])
            tag = f'{index} '
            values = [int(line.split()[2]) for line in matrix if line.startswith(tag)]
        writer.writerow([arm, feature_id, n_barcodes, len(values), sum(values)])
