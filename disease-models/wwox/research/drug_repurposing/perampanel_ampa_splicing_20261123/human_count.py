"""Stream the original ENA FASTQs, validate their checksums and retain only aggregate counts."""
import argparse
import csv
import hashlib
from io import StringIO
from pathlib import Path
import re
import subprocess
from tempfile import TemporaryFile
import urllib.request


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
        digest=hashlib.md5()
        size=0
        with TemporaryFile() as result:
            with subprocess.Popen([str(args.counter),"count",str(args.probes),"-"],stdin=subprocess.PIPE,stdout=result) as process:
                try:
                    with urllib.request.urlopen("https://"+url,timeout=90) as raw:
                        while block:=raw.read(1<<20):
                            digest.update(block)
                            size+=len(block)
                            process.stdin.write(block)
                finally:
                    process.stdin.close()
                if process.wait()!=0:
                    raise RuntimeError(f"Counter failed for {run}")
            result.seek(0)
            rows=list(csv.DictReader(StringIO(result.read().decode()),delimiter="\t"))
        if size!=int(r["fastq_bytes"]) or digest.hexdigest()!=r["fastq_md5"]:
            raise ValueError(f"{run}: compressed file integrity")
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
    main(p.parse_args())
