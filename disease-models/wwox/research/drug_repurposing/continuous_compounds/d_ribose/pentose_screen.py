"""Reproduce the WWOX ribose phosphorylation and purine salvage contrasts."""
from pathlib import Path
import sys

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent / 'thiamine'))
from cell_types import run as nuclei
from screen import run as bulk

genes = 'Rbks Rpia Rpe Tkt Taldo1 Prps1 Prps2 Aprt Hprt Adsl'.split()
files, output = map(Path, sys.argv[1:])
bulk(files, target_genes=genes, output=output/'pentose_bulk.tsv',
     human_symbols={'Hprt': 'HPRT1'}, missing_value='NA')
nuclei(files, genes=genes, output_dir=output)
