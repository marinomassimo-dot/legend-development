"""Recompute the nine hippocampal class contrasts for bicarbonate and chloride handling."""
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from thiamine.cell_types import run

if __name__ == '__main__':
    genes = 'Car7 Car2 Car4 Car14 Slc12a2 Slc12a5 Slc4a3 Slc4a7 Slc4a10'.split()
    run(Path(sys.argv[1]), genes, HERE)
