"""Reproduce the prespecified untreated WWOX pyrimidine pathway contrasts."""
from pathlib import Path
import sys

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent / "thiamine"))
from screen import run

genes = "Cad Dhodh Umps Slc29a1 Slc29a2 Uck1 Uck2 Upp1 Cmpk1 Ctps Ctps2 Rrm1 Rrm2b Pcyt1a".split()
run(Path(sys.argv[1]), target_genes=genes, human_symbols={"Ctps": "CTPS1"},
    output=Path(sys.argv[2]), missing_value="NA")
