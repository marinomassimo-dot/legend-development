"""Reproduce the prespecified untreated WWOX lipoylation transcript comparison."""
from pathlib import Path
import sys

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent / 'thiamine'))
from screen import run

genes = 'Lias Lipt1 Lipt2 Gcsh Mcat Mecr Ndufab1 Dlat Dlst Dbt Pdha1 Ogdh'.split()
run(Path(sys.argv[1]), target_genes=genes, output=Path(sys.argv[2]), missing_value='NA')
