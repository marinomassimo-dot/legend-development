"""Estimate transporter and nucleotide-pathway RNA within hippocampal cell classes."""
from pathlib import Path
import sys

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent / "thiamine"))
from cell_types import run

genes = "Slc29a1 Slc29a2 Uck1 Uck2 Rrm2b Pcyt1a".split()
run(Path(sys.argv[1]), genes=genes, output_dir=Path(sys.argv[2]))
