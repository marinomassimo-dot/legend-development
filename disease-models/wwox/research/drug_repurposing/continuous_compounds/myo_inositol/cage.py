"""One-library CAGE comparisons in human neural cultures; the target is its own QC."""
import csv
import gzip
from math import log2
from pathlib import Path
import sys

source, = (Path(sys.argv[1]) / 'geo/GSE126075').glob('*all_genes*')
with gzip.open(source, 'rt') as stream:
    rows = {r['Gene']: r for r in csv.DictReader(stream, delimiter='\t')}
with Path(sys.argv[2]).open('w') as stream:
    out = csv.writer(stream, delimiter='\t', lineterminator='\n')
    out.writerow(['symbol', 'stage', 'baseline_TPM', 'shWWOX_TPM', 'log2p1_diff', 'measured_in_table'])
    for gene in 'WWOX SLC5A3 ISYNA1 IMPA1 CDIPT KCNQ2 KCNQ3'.split():
        for stage in ['hNSC', 'Neurons']:
            if gene not in rows:
                out.writerow([gene, stage, 'NA', 'NA', 'NA', 'absent'])
                continue
            control = float(rows[gene][stage])
            knockdown = float(rows[gene][stage + '_WWOX_del'])
            out.writerow([gene, stage, control, knockdown,
                          round(log2(1 + knockdown) - log2(1 + control), 4), 'present'])
