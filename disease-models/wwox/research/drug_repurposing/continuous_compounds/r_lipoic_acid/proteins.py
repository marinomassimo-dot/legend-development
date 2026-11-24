"""Look up the prespecified WWOX pathway in the held Zeng S1 extraction."""
import csv
import hashlib
from pathlib import Path
import sys

source, output = map(Path, sys.argv[1:])
assert hashlib.sha256(source.read_bytes()).hexdigest() == 'cae297dce11b3b61cb20ab46ec05799fa30c28dae1099b761cb57ce5be980090'
with source.open() as stream:
    proteins = list(csv.DictReader(stream, delimiter='\t'))
genes = 'LIAS LIPT1 LIPT2 GCSH MCAT MECR NDUFAB1 DLAT DLST DBT PDHA1 OGDH'.split()
with output.open('w') as stream:
    table = csv.writer(stream, delimiter='\t', lineterminator='\n')
    table.writerow(['gene', 'S1_row', 'silenced_minus_control_log2', 'BH_adjusted_P'])
    for gene in genes:
        matches = [row for row in proteins if row['symbol'] == gene]
        if not matches:
            table.writerow([gene, 'not_in_parsed_table', 'NA', 'NA'])
        for row in matches:
            table.writerow([gene, row['row'], row['log2fc'], row['bh_adj_p']])
