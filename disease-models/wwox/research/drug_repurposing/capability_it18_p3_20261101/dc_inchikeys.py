#!/usr/bin/env python3
"""IT18 P3 amendment: DrugCentral struct id -> standard InChIKey, computed from structures.molV2.sdf.gz.

Why: the UniChem ChEMBL->DrugCentral map misses 530 DrugCentral structures that carry a human action
(1,019 rows; bromocriptine, cabergoline, carvedilol, mibefradil among them). The catalogue holds a full
InChIKey per record, so an exact full-key join recovers some of them without any name matching.
Needs RDKit (run it in a throwaway venv, never system-wide). --help and import do nothing else.

  derive --sdf F --out TSV      writes struct_id <TAB> inchikey (empty when RDKit cannot parse the molfile)
"""
import argparse
import gzip
import sys


def derive(sdf, out):
    from rdkit import Chem, RDLogger  # only here
    RDLogger.DisableLog("rdApp.*")
    n = bad = 0
    with gzip.open(sdf, "rb") as f, open(out, "w", encoding="utf-8") as o:
        o.write("struct_id\tinchikey\n")
        for mol in Chem.ForwardSDMolSupplier(f, sanitize=True):
            n += 1
            if mol is None:
                bad += 1
                continue
            sid = mol.GetProp("ID").strip() if mol.HasProp("ID") else ""
            key = Chem.MolToInchiKey(mol) or ""
            o.write(f"{sid}\t{key}\n")
    print({"records": n, "unparsed": bad})


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd")
    d = sub.add_parser("derive")
    d.add_argument("--sdf", required=True)
    d.add_argument("--out", required=True)
    a = ap.parse_args(argv)
    if a.cmd != "derive":
        ap.print_help()
        return 0
    derive(a.sdf, a.out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
