"""Reproduce the bulk WWOX comparison for carbonic anhydrases and ion transport."""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from thiamine.screen import run

if __name__ == '__main__':
    genes = 'Car7 Car2 Car4 Car14 Slc12a2 Slc12a5 Slc4a3 Slc4a7 Slc4a10'.split()
    human_symbols = {'Car7': 'CA7', 'Car2': 'CA2', 'Car4': 'CA4', 'Car14': 'CA14'}
    run(Path(sys.argv[1]), genes, HERE / 'screen.tsv', human_symbols)
