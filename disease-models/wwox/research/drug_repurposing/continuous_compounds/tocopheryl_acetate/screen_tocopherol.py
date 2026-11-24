"""Screen vitamin E handling and susceptible lipid remodelling in untreated WWOX models."""
from pathlib import Path
import sys

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent / "thiamine"))
from screen import run

run(Path(sys.argv[1]), target_genes="Ttpa Scarb1 Abca1 Apoe Acsl4 Lpcat3".split(),
    output=Path(sys.argv[2]), missing_value="NA")
