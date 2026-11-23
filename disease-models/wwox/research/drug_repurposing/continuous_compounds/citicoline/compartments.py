"""Recompute choline-pathway abundance within pooled nuclear classes and adult hippocampus."""
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from riboflavin.holdout import adult
from thiamine.cell_types import run as pooled_nuclei

GENES = 'Slc44a1 Flvcr1 Chka Pcyt1a Pcyt1b Chpt1 Cept1'.split()
if __name__ == '__main__':
    files = Path(sys.argv[1])
    adult(files, GENES, HERE / 'adult.tsv')
    pooled_nuclei(files, GENES, HERE)
