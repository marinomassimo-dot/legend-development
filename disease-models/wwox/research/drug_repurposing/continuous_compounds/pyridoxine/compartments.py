"""Recompute vitamin B6 pathway abundance within pooled nuclear classes and adult hippocampus."""
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from riboflavin.holdout import adult
from thiamine.cell_types import run as pooled_nuclei

GENES = 'Pdxk Pnpo Pdxp Gad1 Gad2 Abat Slc32a1 Aldh7a1'.split()
if __name__ == '__main__':
    files = Path(sys.argv[1])
    adult(files, GENES, HERE / 'adult.tsv')
    pooled_nuclei(files, GENES, HERE)
