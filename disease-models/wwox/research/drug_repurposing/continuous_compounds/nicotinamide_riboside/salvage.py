"""Reproduce the prespecified untreated WWOX NAD metabolism contrasts."""
from pathlib import Path
import sys

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent / "thiamine"))
from screen import run

genes = "Nmrk1 Nmrk2 Nampt Nmnat1 Nmnat2 Nmnat3 Sarm1 Cd38 Parp1 Slc25a51 Slc29a1".split()
run(Path(sys.argv[1]), target_genes=genes, output=Path(sys.argv[2]), missing_value="NA")
