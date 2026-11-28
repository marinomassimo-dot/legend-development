"""Reproduce the RT001 conversion and allocation contrast in hippocampal nuclei."""

import argparse
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "thiamine"))
from cell_types import run


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("shared_files", type=Path)
    parser.add_argument("--out", type=Path, default=HERE / "nuclei")
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    genes = ["Fads2", "Fads1", "Elovl5", "Pla2g6", "Acsl4", "Lpcat3", "Tmem189", "Gnpat", "Agps", "Gpx4"]
    run(args.shared_files, genes=genes, output_dir=args.out)


if __name__ == "__main__":
    main()
