"""Resolve CoA synthesis, buffering and transporter RNA in pooled WWOX hippocampal nuclei."""
from pathlib import Path
import sys

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent / "thiamine"))
from cell_types import run

genes = "Pank3 Coasy Crat Slc25a42 Slc25a16".split()
run(Path(sys.argv[1]), genes=genes, output_dir=Path(sys.argv[2]))
