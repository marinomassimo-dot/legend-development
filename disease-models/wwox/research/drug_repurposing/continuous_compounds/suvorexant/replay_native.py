"""Reuse the previously acquired WWOX bulk RNA comparison for the orexin branch."""

from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "thiamine"))
from screen import run


if __name__ == "__main__":
    _, files, output = sys.argv
    run(Path(files), target_genes=("Hcrt", "Hcrtr1", "Hcrtr2"), output=Path(output), missing_value="NA")
