"""Compare genes for carnosine handling and methylglyoxal clearance in WWOX tissue."""
from pathlib import Path
import sys

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent / 'thiamine'))
from screen import run

run(Path(sys.argv[1]), target_genes='Carns1 Cndp1 Cndp2 Glo1 Hagh'.split(),
    output=Path(sys.argv[2]), missing_value='NA')
