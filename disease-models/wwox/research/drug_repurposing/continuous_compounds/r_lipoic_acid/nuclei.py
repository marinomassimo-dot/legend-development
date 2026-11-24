"""Decompose marker-assigned WWOX hippocampal nuclear counts by cell class."""
from pathlib import Path
import sys

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent / 'thiamine'))
from cell_types import run

genes = 'Lias Lipt1 Lipt2 Gcsh Mcat Mecr Ndufab1 Dlat Dlst Dbt Pdha1 Ogdh'.split()
run(Path(sys.argv[1]), genes=genes, output_dir=Path(sys.argv[2]))
