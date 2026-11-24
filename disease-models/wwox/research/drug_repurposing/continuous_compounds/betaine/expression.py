"""Reproduce the WWOX betaine transcript screen from the held GEO input tables."""
from pathlib import Path
import sys

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent / "thiamine"))
from cell_types import run as score_nuclei
from screen import run as score_bulk

inputs, output = map(Path, sys.argv[1:])
genes = "Chdh Aldh9a1 Bhmt Slc6a12 Slc6a6 Slc6a8 Slc5a3 Nfat5 Mtr Mat2a Ahcy".split()
output.mkdir(parents=True, exist_ok=True)
score_bulk(inputs, target_genes=genes, output=output / "betaine_bulk.tsv", missing_value="NA")
score_nuclei(inputs, genes=genes, output_dir=output)
