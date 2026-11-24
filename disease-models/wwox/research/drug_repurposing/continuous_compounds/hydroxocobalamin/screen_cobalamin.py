"""Untreated WWOX contrasts in cobalamin delivery and its two cofactor branches."""
from pathlib import Path
import sys

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent / "thiamine"))
from screen import run

genes = "Tcn2 Cd320 Lmbrd1 Abcd4 Mmachc Mmadhc Mtr Mtrr Mmaa Mmab Mut".split()
run(Path(sys.argv[1]), target_genes=genes, output=Path(sys.argv[2]),
    missing_value="NA")
