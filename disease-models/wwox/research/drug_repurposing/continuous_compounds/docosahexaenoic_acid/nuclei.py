"""Resolve the bulk lipid and conductance contrasts across pooled hippocampal cell classes."""
from pathlib import Path
import sys

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent / "thiamine"))
from cell_types import run

genes = "Mfsd2a Cldn5 Pecam1 Slc2a1 Acsl6 Lpcat3 Kcnk2 Kcnk10 Kcnk4".split()
run(Path(sys.argv[1]), genes=genes, output_dir=Path(sys.argv[2]))
