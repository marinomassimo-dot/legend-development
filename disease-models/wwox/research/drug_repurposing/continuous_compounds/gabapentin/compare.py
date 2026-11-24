"""Reproduce the bulk and hippocampal nuclear comparisons from the GEO input directory."""
from pathlib import Path
import sys

shared = Path(__file__).resolve().parents[1] / 'thiamine'
sys.path.insert(0, str(shared))
from screen import run as bulk
from cell_types import run as nuclei

files, out = map(Path, sys.argv[1:])
genes = 'Cacna2d1 Cacna2d2 Thbs1 Thbs2 Thbs4'.split()
bulk(files, target_genes=genes, output=out/'bulk.tsv', missing_value='NA')
nuclei(files, genes=genes, output_dir=out)
