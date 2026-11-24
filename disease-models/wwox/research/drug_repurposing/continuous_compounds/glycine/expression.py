"""Recompute the untreated WWOX glycine transport, clearance and receptor panel."""
import sys
from pathlib import Path

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent / "thiamine"))
from screen import run

genes = "Grin1 Grin2a Grin2b Slc6a9 Slc6a5 Glra1 Glra2 Glrb Gldc Amt Srr Shmt2".split()
run(Path(sys.argv[1]), target_genes=genes, output=Path(sys.argv[2]), missing_value="NA")
