"""Measure kainate receptor transcripts in the established hippocampal nuclear classes."""
from pathlib import Path
import sys

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent / "thiamine"))
from cell_types import run

run(Path(sys.argv[1]), genes="Grik1 Grik2 Grik5".split(), output_dir=here)
