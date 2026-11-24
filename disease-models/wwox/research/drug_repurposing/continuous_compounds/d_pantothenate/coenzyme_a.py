"""Reproduce the WWOX CoA pathway contrasts, disambiguating Coasy by stable gene ID."""
import gzip
from pathlib import Path
import sys

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent / "thiamine"))
from screen import run

files, output = map(Path, sys.argv[1:])
genes = "Slc5a6 Pank1 Pank2 Pank3 Ppcs Ppcdc Coasy Slc25a42 Crat Pdha1 Acly Acss2".split()
# Release 92 calls two distinct loci Ppat. Only this stable ID encodes CoA synthase.
aliases = {}
with gzip.open(next((files/"reference_ensembl_r92").glob("*.fa.gz")), "rt") as source:
    for line in source:
        if line.startswith(">") and " gene:ENSMUSG00000001755." in line:
            aliases[line[1:].split(".")[0]] = "Coasy"
if not aliases:
    raise ValueError("Missing mouse Coasy stable gene ID in the transcript reference")
run(files, target_genes=genes, output=output, missing_value="NA", mouse_transcript_overrides=aliases)
