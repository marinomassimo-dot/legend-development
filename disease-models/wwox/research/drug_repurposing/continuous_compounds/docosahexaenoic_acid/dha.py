"""Reproduce the prespecified WWOX lipid, vascular and potassium-channel contrasts."""
from pathlib import Path
import sys

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent / "thiamine"))
from screen import run

genes = "Mfsd2a Cldn5 Pecam1 Slc2a1 Acsl6 Lpcat3 Kcnk2 Kcnk10 Kcnk4".split()
run(Path(sys.argv[1]), target_genes=genes, output=Path(sys.argv[2]), missing_value="NA")
