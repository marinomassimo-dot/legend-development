"""Reproduce the WWOX tissue contrasts and cell-class counts for the sulforaphane dossier."""
from pathlib import Path
import sys

shared = Path(__file__).resolve().parents[1] / 'thiamine'
sys.path.insert(0, str(shared))
from screen import run as bulk
from cell_types import run as nuclei

files, out = map(Path, sys.argv[1:])
genes = 'Nfe2l2 Keap1 Gclc Gclm Gss Nqo1 Slc7a11'.split()
bulk(files, target_genes=genes, output=out/'bulk.tsv', missing_value='NA')
nuclei(files, genes=genes, output_dir=out)
