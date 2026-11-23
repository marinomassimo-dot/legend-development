"""Recompute WWOX contrasts for carnitine supply, the shuttle and oxidation."""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from thiamine.screen import run

GENES = 'Slc22a5 Slc16a9 Bbox1 Tmlhe Cpt1a Cpt1b Cpt1c Slc25a20 Cpt2 Crat Acadvl Hadha Hadhb'.split()

if __name__ == '__main__':
    run(Path(sys.argv[1]), GENES, HERE / 'screen.tsv')
