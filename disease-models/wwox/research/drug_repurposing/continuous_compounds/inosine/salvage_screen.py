"""Reproduce the untreated WWOX expression panel for inosine disposition."""
from pathlib import Path
import sys

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent / 'thiamine'))
from cell_types import run as nuclei
from screen import run as bulk

# ENT1/2 for nucleosides, ENBT1 for bases; salvage, PRPP supply and oxidation.
genes = 'Slc29a1 Slc29a2 Slc43a3 Pnp Hprt Aprt Prps1 Prps2 Pgm2 Xdh Adsl'.split()
files, output = map(Path, sys.argv[1:])
bulk(files, target_genes=genes, output=output/'salvage_bulk.tsv',
     human_symbols={'Hprt': 'HPRT1'}, missing_value='NA')
nuclei(files, genes=genes, output_dir=output)
