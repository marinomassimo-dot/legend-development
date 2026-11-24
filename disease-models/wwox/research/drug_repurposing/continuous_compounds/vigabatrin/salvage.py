"""Contrast untreated WWOX mitochondrial nucleotide and GABA-handling genes."""
from pathlib import Path
import sys

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent / 'thiamine'))
from screen import run

genes = 'Abat Gad1 Gad2 Aldh5a1 Suclg1 Sucla2 Nme4 Tk2 Dguok Rrm2b Polg Tfam'.split()
run(Path(sys.argv[1]), target_genes=genes, output=Path(sys.argv[2]), missing_value='NA')
