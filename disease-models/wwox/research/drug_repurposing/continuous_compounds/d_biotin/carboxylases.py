"""Summarize biotin-related transcripts in untreated WWOX datasets from local GEO inputs."""
from pathlib import Path
import sys

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent / "thiamine"))
from screen import run as bulk
from cell_types import run as nuclei

genes = "Slc5a6 Btd Hlcs Pcx Acaca Acacb Pcca Pccb Mccc1 Mccc2 Fasn Mbp".split()
files, output = map(Path, sys.argv[1:])
bulk(files, target_genes=genes, human_symbols={"Pcx": "PC"}, output=output/"screen.tsv", missing_value="NA")
nuclei(files, genes=genes, output_dir=output)
