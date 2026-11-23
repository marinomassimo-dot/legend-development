"""Reproduce the WWOX choline transport and phosphatidylcholine synthesis contrasts."""
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent))
from thiamine.screen import run

GENES = 'Slc44a1 Slc44a2 Slc5a7 Flvcr1 Flvcr2 Chka Chkb Pcyt1a Pcyt1b Chpt1 Cept1 Pemt Slc29a1 Slc29a2 Uck2 Ctps Ctps2'.split()
if __name__ == '__main__':
    run(Path(sys.argv[1]), GENES, HERE / 'screen.tsv', {'Ctps':'CTPS1'}, missing_value='NA')
