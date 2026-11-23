"""Apply the locked secondary paired-fragment feasibility rule to validated archives."""
import argparse
from collections import defaultdict
import csv
from datetime import datetime, timezone
import hashlib
from pathlib import Path
import time

from p47t_sra import process, read


def write(path,rows):
    with path.open("w") as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys(),delimiter="\t",lineterminator="\n")
        w.writeheader();w.writerows(rows)


def main(args):
    runs=read(args.manifest)
    def primary_file(r):
        for folder in (args.ena_counts,args.ncbi_counts):
            p=folder/(r["run"]+".tsv")
            if p.exists():return p
        return None
    while any(primary_file(r) is None for r in runs):
        if time.time()>args.deadline:raise SystemExit("Secondary analysis time limit")
        time.sleep(20)
    totals=defaultdict(int)
    for r in runs:
        (t,)=[t for t in read(primary_file(r)) if t["rule"]=="centered" and t["Q"]=="20"]
        totals[r["animal"]]+=int(t["insert"])+int(t["skip"])
    assert totals["M2"]==6
    remaining=[a for a,n in sorted(totals.items(),key=lambda x:(x[1],x[0])) if n<12 and a!="M2"]
    order=["M2",*remaining,*sorted(set(totals)-{"M2",*remaining})]
    rows=[]
    for animal in order:
        animal_rows=[]
        for r in sorted((r for r in runs if r["animal"]==animal),key=lambda r:r["run"]):
            if time.time()+150>args.deadline:
                print("TIME_LIMIT",animal,flush=True)
                return
            path=process(r,args)
            lookup={(t["rule"],t["Q"]):t for t in read(primary_file(r))}
            for t in read(path):
                old=lookup[t["rule"],t["Q"]]
                assert all(t["R1_"+v]==old[v] for v in ("insert","skip","conflict"))
                if t["rule"]=="centered" and t["Q"]=="20":
                    animal_rows.append(t)
        assert len(animal_rows)==2
        n=sum(int(t["either_insert"])+int(t["either_skip"]) for t in animal_rows)
        rows.append(dict(animal=animal,arm=animal_rows[0]["arm"],primary_R1=totals[animal],
                         primary_R2=sum(int(t["R2_insert"])+int(t["R2_skip"]) for t in animal_rows),
                         paired_unique=n,conflicts=sum(int(t["either_conflict"]) for t in animal_rows)))
        write(args.out/"paired_coverage.tsv",rows)
        print("Paired coverage",animal,n,flush=True)
        if n<12:
            print("STOP_INSUFFICIENT_PAIRED_COVERAGE",animal,n,flush=True)
            return
    print("ALL_ANIMALS_REACHED_INDIVIDUAL_MINIMUM",flush=True)


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    for n in ("manifest","probes","reader","counter","ena_counts","ncbi_counts","out"):
        p.add_argument(n,type=Path)
    p.add_argument("utc_deadline",help="ISO UTC datetime")
    args=p.parse_args()
    args.deadline=datetime.fromisoformat(args.utc_deadline).replace(tzinfo=timezone.utc).timestamp()
    args.probe_sha=hashlib.sha256(args.probes.read_bytes()).hexdigest()
    args.paired=True
    args.out.mkdir(exist_ok=True,parents=True)
    main(args)
