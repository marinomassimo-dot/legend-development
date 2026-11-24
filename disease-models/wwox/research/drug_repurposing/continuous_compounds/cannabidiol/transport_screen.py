"""Reproduce the WWOX cell-class and bulk contrasts for adenosine handling."""
import sys
from pathlib import Path

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent / 'thiamine'))
from cell_types import run as nuclei
from screen import run as bulk

files, out = map(Path, sys.argv[1:])
# ENT1/2 transport, extracellular ATP hydrolysis, intracellular removal, and receptor response.
genes = 'Slc29a1 Slc29a2 Entpd1 Nt5e Adk Ada Adora1 Adora2a'.split()
bulk(files, target_genes=genes, output=out/'transport_bulk.tsv', missing_value='NA')
nuclei(files, genes=genes, output_dir=out)
