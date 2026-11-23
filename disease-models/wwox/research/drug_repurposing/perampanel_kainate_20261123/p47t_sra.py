"""Recover first mates from public NCBI normalized archives, with a cross-archive control."""
import argparse
import csv
import hashlib
import io
from pathlib import Path
import re
import shutil
import subprocess
import tempfile


def read(path):
    with path.open() as f:
        return list(csv.DictReader(f,delimiter="\t"))


def raw_hashes(path):
    # The NCBI public S3 objects for these accessions use 8 MiB multipart checksums.
    multipart,sha,n=hashlib.md5(),hashlib.sha256(),0
    with path.open("rb") as f:
        for block in iter(lambda:f.read(8*1024*1024),b""):
            multipart.update(hashlib.md5(block).digest())
            sha.update(block)
            n+=1
    return f"{multipart.hexdigest()}-{n}",sha.hexdigest()


def verify_anchor(path,match):
    source=read(path)
    other=read(match)
    keys=lambda t:(t["rule"],t["Q"],int(t["reads"]),int(t["insert"]),int(t["skip"]),int(t["conflict"]))
    assert len(source)==len(other)==4 and sorted(map(keys,source))==sorted(map(keys,other))


def process(r,args,source_file=None,source_header=None):
    run=r["run"]
    assert re.fullmatch("SRR[0-9]+",run)
    dest=args.out/(run+".tsv")
    if dest.exists():
        rows=read(dest)
        assert len(rows)==4 and all(t["source"]=="NCBI_full_quality" and int(t["reads"])==int(r["fragments"])
                                    and t["probe_sha256"]==args.probe_sha for t in rows)
        return dest
    url=f"https://sra-pub-run-odp.s3.amazonaws.com/sra/{run}/{run}"
    with tempfile.TemporaryDirectory(prefix="legend-p47t-sra-") as work:
        raw=Path(work)/(run+".sra") if source_file is None else source_file
        head=Path(work)/"headers" if source_header is None else source_header
        if source_file is None:
            hdr=subprocess.check_output(["curl","-fsSI","--max-time","25",url],text=True)
            size=int(re.search(r"(?im)^Content-Length:\s*(\d+)",hdr)[1])
            if shutil.disk_usage(work).free < size+450_000_000: raise RuntimeError("Insufficient temporary disk space")
            print("Download",run,size,flush=True)
            subprocess.run(["curl","-fsSL","--retry","2","--connect-timeout","20","--max-time","640",
                            "--max-filesize",str(size),"-D",str(head),"-o",str(raw),url],check=True)
        headers=head.read_text()
        assert raw.stat().st_size==int(re.findall(r"(?im)^Content-Length:\s*(\d+)",headers)[-1])
        etag,sha=raw_hashes(raw)
        assert etag==re.findall(r'(?im)^ETag:\s*"([^"]+)"',headers)[-1]
        print("Verified archive; counting",run,flush=True)
        cmd=[str(args.reader),"--split-spot","-Z","--defline-seq","@$si/$ri","--defline-qual","+",str(raw)]
        with subprocess.Popen(cmd,stdout=subprocess.PIPE) as export:
            stats=subprocess.check_output([str(args.counter),"count",str(args.probes),"-"],stdin=export.stdout,text=True)
            export.stdout.close()
            if export.wait(): raise RuntimeError("SRA reader failed")
        rows=list(csv.DictReader(io.StringIO(stats),delimiter="\t"))
        paired=getattr(args,"paired",False)
        count_field="fragments" if paired else "reads"
        assert len(rows)==4 and all(int(t[count_field])==int(r["fragments"]) for t in rows)
        assert {(t["rule"],t["Q"]) for t in rows}=={(s,q) for s in ("centered","any") for q in ("20","30")}
        data=[]
        for t in rows:
            item=dict(run=run,animal=r["animal"],sex=r["sex"],arm=r["arm"],source="NCBI_full_quality",
                      bytes=raw.stat().st_size,archive_etag=etag,archive_sha256=sha,probe_sha256=args.probe_sha,
                      rule=t["rule"],Q=t["Q"],reads=t[count_field])
            if paired:
                item.update({k:v for k,v in t.items() if k.startswith(("R1_","R2_","either_"))})
            else:
                item.update(insert=t["flip"],skip=t["flop"],conflict=t["conflict"])
            data.append(item)
    tmp=dest.with_suffix(".partial")
    with tmp.open("w") as f:
        w=csv.DictWriter(f,fieldnames=data[0].keys(),delimiter="\t",lineterminator="\n")
        w.writeheader();w.writerows(data)
    tmp.replace(dest)
    print("Verified first mates",run,flush=True)
    return dest


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    for n in ("manifest","probes","reader","counter","ena_counts","out"):
        p.add_argument(n,type=Path)
    p.add_argument("--anchor-archive",type=Path)
    p.add_argument("--anchor-headers",type=Path)
    p.add_argument("--anchor-only",action="store_true")
    args=p.parse_args()
    args.probe_sha=hashlib.sha256(args.probes.read_bytes()).hexdigest()
    args.out.mkdir(exist_ok=True,parents=True)
    runs={r["run"]:r for r in read(args.manifest)}
    anchor="SRR21892149"
    entry=process(runs[anchor],args,args.anchor_archive,args.anchor_headers)
    verify_anchor(entry,args.ena_counts/(anchor+".tsv"))
    print("Full cross-archive anchor matched",anchor,flush=True)
    if not args.anchor_only:
        for suffix in ("152","160","161","162","163","164","157","158","153","154","155","156","145","146","147","148","149","150","151","159"):
            run="SRR21892"+suffix
            ena=args.ena_counts/(run+".tsv")
            if ena.exists():
                if (args.out/(run+".tsv")).exists(): verify_anchor(args.out/(run+".tsv"),ena)
                continue
            process(runs[run],args)
        print("COMPLETE",len(runs),flush=True)
