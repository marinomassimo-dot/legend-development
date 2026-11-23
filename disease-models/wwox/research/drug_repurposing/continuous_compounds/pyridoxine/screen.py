"""Reproduce the WWOX vitamin B6 handling and GABA contrasts."""
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent))
from thiamine.screen import run

GENES = 'Pdxk Pnpo Plpbp Pdxp Alpl Gad1 Gad2 Abat Aldh5a1 Slc32a1 Aldh7a1'.split()
if __name__ == '__main__':
    run(Path(sys.argv[1]), GENES, HERE / 'screen.tsv', {}, missing_value='NA')
