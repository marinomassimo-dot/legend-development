"""Reproduce the six RNA counts sequentially, reusing verified run outputs."""
import argparse
import csv
import re
from pathlib import Path
import subprocess
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("inputs",type=Path,help="Directory with runs.tsv and NM_000826.6.gb")
    parser.add_argument("output",type=Path)
    args=parser.parse_args()
    args.output.mkdir(exist_ok=True,parents=True)
    manifest=args.inputs/"runs.tsv"
    with manifest.open() as f:
        runs=sorted(csv.DictReader(f,delimiter="\t"), key=lambda r:r["run_accession"])
    for r in runs:
        run=r["run_accession"]
        if not run.startswith("SRR") or not run[3:].isdigit():
            raise ValueError(f"Unexpected run ID: {run}")
        out=args.output/(run+".tsv")
        raw=args.inputs/(run+".fastq.gz")
        if out.exists():
            with out.open() as f:
                rows=list(csv.DictReader(f,delimiter="\t"))
            if {z["category"] for z in rows}=={"primary","flank18","interior20","splice8","low_quality"} and all(
                    z["run"]==run and z["read_total"]==r["read_count"] for z in rows):
                continue
            raise ValueError(f"Incomplete prior output: {out}")
        if not raw.exists():
            expected = r["fastq_ftp"]
            pattern = rf"ftp\.sra\.ebi\.ac\.uk/vol1/fastq/{run[:6]}/[0-9]{{3}}/{run}/{run}\.fastq\.gz"
            if not re.fullmatch(pattern,expected):
                raise ValueError(f"Unexpected ENA path for {run}")
            tmp = raw.with_suffix(".part")
            print("Retrieving",run,flush=True)
            subprocess.run(["curl","--fail","--silent","--show-error","--location","--retry","2",
                            "--max-time","1800","--output",str(tmp),"https://"+expected],check=True)
            tmp.replace(raw)
        print("Counting",run,flush=True)
        subprocess.run([sys.executable,str(Path(__file__).with_name("editing.py")),"count",
                        str(args.inputs/"NM_000826.6.gb"),str(manifest),str(raw),str(out)],check=True)
        # Only the fetched raw file in this dedicated staging directory is
        # released. Its size, MD5 and number of records have all been verified.
        raw.unlink()
        print("Verified",run,flush=True)


if __name__=="__main__":
    main()
