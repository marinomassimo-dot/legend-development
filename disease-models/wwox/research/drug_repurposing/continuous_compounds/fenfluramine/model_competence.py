"""Audit coverage of neuronal serotonin release and sigma-1 pathway markers by library."""
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent / 'ganaxolone_20261123'))
from analyze import load_target, tsv

files, output = map(Path, sys.argv[1:])
source, = (files / 'geo/GSE156243').glob('*count_table.txt.gz')
symbols = 'TPH2 SLC6A4 FEV DDC SIGMAR1 HSPA5 GRIN1'.split()
names, counts = load_target(source, symbols)
samples = [i for i, name in enumerate(names) if name.startswith(('cko', 'cwt'))]
assert len(samples) == 6
tsv(output, ['gene', 'mapping', *[names[i] for i in samples]],
    [[gene, 'measured' if gene in counts else 'absent',
      *[round(counts[gene][i], 5) if gene in counts else 'NA' for i in samples]]
     for gene in symbols])
