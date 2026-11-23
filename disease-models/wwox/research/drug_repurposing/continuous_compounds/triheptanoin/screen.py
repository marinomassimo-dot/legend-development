"""Recompute WWOX contrasts in odd-chain entry, B12 cofactor handling and ketolysis."""
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from thiamine.screen import run

GENES = 'Pcca Pccb Mcee Mut Mmaa Mmab Bdh1 Oxct1 Acat1 Slc16a1 Slc16a7 Sdha Suclg1 Sucla2'.split()

if __name__ == '__main__':
    run(Path(sys.argv[1]), GENES, HERE / 'screen.tsv')
