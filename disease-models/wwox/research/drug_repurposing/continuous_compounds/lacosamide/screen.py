"""Recompute WWOX contrasts for sodium-channel subunits, axonal organization and CRMP2."""
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from thiamine.screen import run

GENES = 'Scn1a Scn2a Scn3a Scn8a Scn1b Scn2b Scn3b Scn4b Dpysl2 Ank3 Sptbn4 Nfasc Cntnap1'.split()

if __name__ == '__main__':
    run(Path(sys.argv[1]), GENES, HERE / 'screen.tsv')
