"""Reanalyse nucleotide supply transcripts across assigned hippocampal nuclei."""
from pathlib import Path
import sys

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent / 'thiamine'))
from cell_types import run

genes = 'Abat Nme4 Dguok Rrm2b Tk2 Suclg1 Sucla2'.split()
run(Path(sys.argv[1]), genes=genes, output_dir=Path(sys.argv[2]))
