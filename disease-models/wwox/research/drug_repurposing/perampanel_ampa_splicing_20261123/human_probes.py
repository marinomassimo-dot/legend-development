"""Construct balanced splice probes for the 3-prime edge of the GRIA2 flip/flop cassette."""
import argparse
import csv
from collections import defaultdict
from pathlib import Path
import re
from analyze import MOTIFS, write


def construct(path, out):
    out.mkdir(exist_ok=True,parents=True)
    records,labels={},defaultdict(set)
    origins=[]
    for r in path.read_text().split("//\n"):
        if "ORIGIN" not in r: continue
        tx=re.search(r"^VERSION\s+(\S+)",r,re.M)[1]
        assert tx.startswith("NM_")
        cds=int(re.search(r"^     CDS\s+(\d+)\.\.",r,re.M)[1])
        seq=re.sub("[^acgt]","",r.split("ORIGIN")[-1]).upper()
        protein="".join(re.search(r'/translation="([^"]+)',r)[1].split())
        hits=[(c,m) for c,pattern in MOTIFS.items() for m in pattern.finditer(protein)]
        if len(hits)!=1: raise ValueError(f"{tx} has no unique reference cassette")
        kind,m=hits[0]
        start,end=cds+3*m.start(),cds+3*m.end()-1
        exon,=[(int(a),int(b)) for a,b in re.findall(r"^     exon\s+(\d+)\.\.(\d+)",r,re.M)
               if int(a)<=start<=end<=int(b)]
        assert exon[1]-exon[0]+1==115
        records[tx]=(kind,seq)
        origins.append([tx,kind,*exon])
        for offset in range(10,22):
            labels[kind,offset].add(seq[exon[1]-offset:exon[1]+31-offset])
    probes=[]
    for (kind,offset),candidates in labels.items():
        assert len(candidates)==1
        seq,=candidates
        assert len(seq)==31
        if all((seq in s)==(k==kind) for k,s in records.values()):
            probes.append([kind,offset,seq])
    write(out/"human_candidates.tsv","class offset seq",sorted(probes))
    write(out/"human_refseq.tsv","transcript class cassette_first_1based cassette_last_1based",sorted(origins))


def finalize(out):
    def read(name):
        return list(csv.DictReader((out/name).open(),delimiter="\t"))
    candidates=read("human_candidates.tsv")
    fastas=[{(r["class"],r["offset"]):r for r in read(name)} for name in
            ["human_genome_audit.tsv","human_transcript_audit.tsv"]]
    eligible={}
    for r in candidates:
        key=r["class"],r["offset"]
        genome,tx=(f[key] for f in fastas)
        if int(genome["target_hits"])+int(genome["other_hits"])==0 and int(tx["target_hits"])>0 and int(tx["other_hits"])==0:
            eligible[key]=r
    offsets={i for _,i in eligible if ("flip",i) in eligible and ("flop",i) in eligible}
    assert "15" in offsets, "Primary centered comparison unavailable"
    write(out/"human_probes.tsv","class offset seq",[[r["class"],r["offset"],r["seq"]]
          for r in candidates if r["offset"] in offsets])


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("step",choices=["construct","finalize"])
    p.add_argument("refseq",type=Path)
    p.add_argument("out",type=Path)
    a=p.parse_args()
    if a.step=="construct": construct(a.refseq,a.out)
    else: finalize(a.out)
