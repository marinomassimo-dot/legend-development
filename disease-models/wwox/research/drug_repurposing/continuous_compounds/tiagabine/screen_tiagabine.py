"""Run the existing WWOX bulk and nuclear analyses for GABA uptake and circuit context."""
import argparse
from pathlib import Path
import sys

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent / "thiamine"))
from screen import run as bulk
from cell_types import run as nuclei

parser = argparse.ArgumentParser()
parser.add_argument('files', type=Path)
parser.add_argument('output_dir', type=Path)
args = parser.parse_args()
genes = 'Slc6a1 Slc6a11 Slc32a1 Gad1 Gabrd Gabra4'.split()
bulk(args.files, target_genes=genes, output=args.output_dir / 'bulk.tsv', missing_value='NA')
nuclei(args.files, genes=genes, output_dir=args.output_dir)
