"""Compare pyruvate transporter transcripts across three untreated WWOX systems."""
from pathlib import Path
import sys

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent / "thiamine"))
from screen import run

run(Path(sys.argv[1]), target_genes="Slc16a1 Slc16a7 Slc16a3 Mpc1 Mpc2".split(),
    output=Path(sys.argv[2]), missing_value="NA")
