"""Compare selenium delivery, incorporation and phospholipid peroxide handling across WWOX models."""
from pathlib import Path
import sys

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent / "thiamine"))
from screen import run

genes = "Selenop Lrp8 Sepsecs Gpx4 Txnrd1 Acsl4".split()
run(Path(sys.argv[1]), target_genes=genes, output=Path(sys.argv[2]), missing_value="NA")
