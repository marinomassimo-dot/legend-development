"""Validate each original ENA FASTQ and retain aggregate counts, one library at a time."""
import argparse
import csv
from contextlib import nullcontext
import hashlib
from io import StringIO
from pathlib import Path
import re
import subprocess
from tempfile import TemporaryDirectory


def main(args):
    with args.manifest.open() as f:
        runs=list(csv.DictReader(f,delimiter="\t"))
    assert len(runs)==6 and len({r["run_accession"] for r in runs})==6
    probe_hash=hashlib.sha256(args.probes.read_bytes()).hexdigest()
    args.out.mkdir(exist_ok=True,parents=True)
    for r in sorted(runs,key=lambda r:r["run_accession"]):
        run=r["run_accession"]
        assert re.fullmatch("SRR[0-9]+",run) and r["library_layout"]=="SINGLE"
        url=r["fastq_ftp"]
        assert re.fullmatch(r"ftp\.sra\.ebi\.ac\.uk/vol1/fastq/[a-zA-Z0-9/]+/"+run+r"\.fastq\.gz",url)
        dest=args.out/(run+".tsv")
        if dest.exists():
            with dest.open() as stream: loaded=list(csv.DictReader(stream,delimiter="\t"))
            if len(loaded)==4 and all(z["compressed_md5"]==r["fastq_md5"] and z["probe_sha256"]==probe_hash
                                     and z["reads"]==r["read_count"] and z["bytes"]==r["fastq_bytes"]
                                     for z in loaded):
                continue
        print("Counting",run,flush=True)
        # One temporary file permits resuming interruptions and separates network
        # truncation from a decoder or record-format failure. Old verified runs are reused.
        if args.resume_dir:
            args.resume_dir.mkdir(parents=True,exist_ok=True)
        workspace=nullcontext(args.resume_dir) if args.resume_dir else TemporaryDirectory(prefix="legend-gria2-junction-")
        with workspace as work:
            raw=Path(work)/(run+".fastq.gz")
            for attempt in range(3):
                get=subprocess.run(["curl","--fail","--silent","--show-error","--location",
                                    "--connect-timeout","30","--speed-limit","1024","--speed-time","120",
                                    "--max-time","1800","--continue-at","-","--output",str(raw),"https://"+url])
                if get.returncode:
                    print("Transfer retry",run,get.returncode,flush=True)
                    continue
                size=raw.stat().st_size
                with raw.open("rb") as stream:
                    digest=hashlib.file_digest(stream,"md5")
                if size==int(r["fastq_bytes"]) and digest.hexdigest()==r["fastq_md5"]:
                    break
                print("Integrity retry",run,size,flush=True)
                raw.unlink()
            else:
                raise RuntimeError(f"No verified FASTQ for {run}")
            result=subprocess.check_output([str(args.counter),"count",str(args.probes),str(raw)],text=True)
            rows=list(csv.DictReader(StringIO(result),delimiter="\t"))
        if {(x["rule"],x["Q"]) for x in rows}!={(m,q) for m in ("centered","any") for q in ("20","30")}:
            raise ValueError(f"{run}: missing output strata")
        if not all(x["reads"]==r["read_count"] for x in rows):
            raise ValueError(f"{run}: read-count mismatch")
        partial=dest.with_suffix(".partial")
        with partial.open("w") as stream:
            fields=["run","sample","bytes","compressed_md5","probe_sha256",*rows[0]]
            w=csv.DictWriter(stream,fieldnames=fields,delimiter="\t",lineterminator="\n")
            w.writeheader()
            for row in rows:
                w.writerow(dict(run=run,sample=r["sample_title"],bytes=size,compressed_md5=digest.hexdigest(),
                                probe_sha256=probe_hash,**row))
        partial.replace(dest)
        print("Verified",run,size,flush=True)


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    for key in ("manifest","counter","probes","out"):p.add_argument(key,type=Path)
    p.add_argument("--resume-dir",type=Path,help="Reuse partial files from an interrupted run in this directory.")
    main(p.parse_args())
