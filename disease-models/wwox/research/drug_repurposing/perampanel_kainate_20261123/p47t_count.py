"""Count one mate per fragment, verify ENA checksums, and apply the locked pilot gate."""
import argparse
import csv
import hashlib
import io
from pathlib import Path
import re
import subprocess
from collections import Counter


def read(path):
    with path.open() as stream:
        return list(csv.DictReader(stream,delimiter="\t"))


def manifest(source):
    rows = []
    for r in read(source):
        m = re.search(r": HPC_(WT/WT|P47T/P47T)_([MF])([0-9]+) ",r["experiment_title"])
        if not m: continue
        run = r["run_accession"]
        assert re.fullmatch("SRR[0-9]+",run) and r["library_layout"]=="PAIRED"
        files = list(zip(r["fastq_ftp"].split(";"),r["fastq_md5"].split(";"),r["fastq_bytes"].split(";"),strict=True))
        (url,md5,size), = [f for f in files if f[0].endswith("_1.fastq.gz")]
        assert re.fullmatch(r"ftp\.sra\.ebi\.ac\.uk/vol1/fastq/[a-zA-Z0-9/]+/"+run+r"_1\.fastq\.gz",url)
        rows.append(dict(run=run,arm=m[1].split("/")[0],sex=m[2],animal=m[2]+m[3],
                         fragments=int(r["read_count"]),url="https://"+url,md5=md5,bytes=int(size)))
    assert len(rows)==20 and len(set(r["run"] for r in rows))==20
    assert set(Counter(r["animal"] for r in rows).values())=={2}
    return sorted(rows,key=lambda r:r["run"])


def integrate(r,counter,probes,dest):
    probe_digest=hashlib.sha256(probes.read_bytes()).hexdigest()
    if dest.exists():
        saved=read(dest)
        if len(saved)==4 and all(s["compressed_md5"]==r["md5"] and s["probe_sha256"]==probe_digest
                                and int(s["bytes"])==r["bytes"] and int(s["reads"])==r["fragments"] for s in saved):
            return saved
        raise RuntimeError(f"Cached output mismatch for {r['run']}")
    for attempt in range(3):
        print("Counting",r["run"],r["animal"],"attempt",attempt+1,flush=True)
        amount=0
        digest=hashlib.md5()
        try:
            with subprocess.Popen(["curl","-fLsS","--connect-timeout","30","--speed-limit","1024",
                                   "--speed-time","180","--max-time","1800",r["url"]],
                                  stdout=subprocess.PIPE) as fetch, subprocess.Popen(
                [str(counter),"count",str(probes),"-"],stdin=subprocess.PIPE,stdout=subprocess.PIPE) as count:
                try:
                    for part in iter(lambda:fetch.stdout.read(1024*1024),b""):
                        digest.update(part)
                        amount+=len(part)
                        count.stdin.write(part)
                finally:
                    count.stdin.close()
                    fetch.stdout.close()
                result=count.stdout.read().decode()
                if fetch.wait() or count.wait(): raise OSError("downloader or counter failed")
            rows=list(csv.DictReader(io.StringIO(result),delimiter="\t"))
            if (amount!=r["bytes"] or digest.hexdigest()!=r["md5"] or len(rows)!=4
                    or any(int(t["reads"])!=r["fragments"] for t in rows)):
                raise ValueError(f"{r['run']}: invalid bytes, hash or record count: {amount} {digest.hexdigest()} {rows}")
        except (OSError,ValueError) as err:
            print(err,flush=True)
            if attempt==2: raise
            continue
        break
    output = [dict(run=r["run"],animal=r["animal"],sex=r["sex"],arm=r["arm"],bytes=amount,
                   compressed_md5=digest.hexdigest(),probe_sha256=probe_digest,rule=t["rule"],
                   Q=t["Q"],reads=t["reads"],insert=t["flip"],skip=t["flop"],conflict=t["conflict"]) for t in rows]
    tmp=dest.with_suffix(".partial")
    with tmp.open("w") as stream:
        w=csv.DictWriter(stream,fieldnames=output[0].keys(),delimiter="\t",lineterminator="\n")
        w.writeheader(); w.writerows(output)
    tmp.replace(dest)
    print("Verified",r["run"],output[0]["insert"],output[0]["skip"],flush=True)
    return output


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    for name in ("source","counter","probes","genome_audit","output"): p.add_argument(name,type=Path)
    a=p.parse_args()
    audit=read(a.genome_audit)
    assert len(audit)==24 and all(int(t["target_hits"])+int(t["other_hits"])==0 for t in audit)
    runs=manifest(a.source)
    a.output.mkdir(exist_ok=True,parents=True)
    pilot=[next(r for r in runs if r["animal"]==animal) for animal in ("M1","M6")]
    yields=[]
    for r in pilot:
        output=integrate(r,a.counter,a.probes,a.output/(r["run"]+".tsv"))
        (t,)=[t for t in output if t["rule"]=="centered" and int(t["Q"])==20]
        yields.append(int(t["insert"])+int(t["skip"]))
    if min(yields)<4:
        print("PILOT_LOW_YIELD",yields,flush=True)
    else:
        for r in runs:
            integrate(r,a.counter,a.probes,a.output/(r["run"]+".tsv"))
        print("COMPLETE",len(runs),flush=True)
