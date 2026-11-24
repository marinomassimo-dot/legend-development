"""Calculate untreated WWOX precursor and transmitter marker contrasts."""
from pathlib import Path
import sys

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent / "thiamine"))
from cell_types import run as score_nuclei
from screen import run as score_bulk

inputs, output = map(Path, sys.argv[1:])
genes = ("Glul Gls Gls2 Slc38a1 Slc38a2 Slc38a3 Slc38a5 Slc1a2 Slc1a3 "
         "Gad1 Gad2 Slc17a7 Slc32a1").split()
output.mkdir(parents=True, exist_ok=True)
score_bulk(inputs, target_genes=genes, output=output / "precursor_bulk.tsv", missing_value="NA")
score_nuclei(inputs, genes=genes, output_dir=output)
