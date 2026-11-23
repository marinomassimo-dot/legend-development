"""Reproduce WWOX contrasts in riboflavin uptake, cofactor synthesis and client systems."""
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from thiamine.screen import run

GENES = 'Slc52a1 Slc52a2 Slc52a3 Rfk Flad1 Slc25a32 Sdha Sdhaf2 Etfa Etfb Etfdh Acadvl Ndufv1 Aifm1 Ppox'.split()
if __name__ == '__main__':
    run(Path(sys.argv[1]), GENES, HERE / 'screen.tsv', missing_value='NA')
