"""Classify Gria2 splice cassettes and test the published murine transcript TPMs."""
import argparse
from collections import defaultdict
import csv
import gzip
import hashlib
from itertools import product
from pathlib import Path
import re
import numpy as np

MOTIFS={"flip":re.compile(r"TP[A-Z]{8}S[A-Z]{3}V[A-Z]{16}AKDSG"),
        "flop":re.compile(r"NA[A-Z]{8}N[A-Z]{3}L[A-Z]{16}SGGGD")}
# Standard genetic code, codons in T/C/A/G order in each position.
CODE=dict(zip(("".join(s) for s in product("TCAG",repeat=3)),
              "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG",strict=True))


def write(path,fields,rows):
    with path.open("w") as f:
        writer=csv.writer(f,delimiter="\t",lineterminator="\n")
        writer.writerow(fields.split())
        writer.writerows(rows)


def refseq(path):
    known=defaultdict(set)
    rows=[]
    for record in path.read_text().split("//\n"):
        label=re.search(r"^VERSION\s+(\S+)",record,re.M)
        if not label:continue
        matched=re.search(r'/translation="([^"]+)',record,re.S)
        peptide="".join(matched[1].split())
        hits=[]
        for kind,pattern in MOTIFS.items():
            for m in pattern.finditer(peptide):
                hits.append(kind)
                if label[1].startswith("NM_"):known[kind].add(m[0])
        rows.append([label[1],len(peptide),",".join(hits) or "unclassified"])
    assert all(len(known[k])==1 for k in MOTIFS)
    return known,rows


def classify(seq,known):
    hits=[]
    for frame in range(3):
        protein="".join(CODE.get(seq[i:i+3],"X") for i in range(frame,len(seq)-2,3))
        for kind,pattern in MOTIFS.items():
            for m in pattern.finditer(protein):
                if m[0] not in known[kind]:raise ValueError("Non-reference cassette")
                left=protein.rfind("*",0,m.start())+1
                right=protein.find("*",m.end())
                start=protein.find("M",left,m.start())
                complete=start>=0 and right!=-1 and right-start>=800
                hits.append((kind,complete))
    if len(hits)!=1:return "unclassified",False
    return hits[0]


def catalog(path,known):
    seqs={}
    name=None
    with gzip.open(path,"rt") as source:
        for line in source:
            if line.startswith(">"):
                name=None
                if " gene_symbol:Gria2 " in line:
                    name=line[1:].split()[0]
                    seqs[name]=(re.search(r"transcript_biotype:(\S+)",line)[1],[])
            elif name:seqs[name][1].append(line.strip())
    assert seqs
    return {tx:(biotype,*classify("".join(parts),known)) for tx,(biotype,parts) in seqs.items()}


def load(path,cat):
    versionless={k.split(".")[0]:k for k in cat}
    assert len(versionless)==len(cat)
    table,versions={},{}
    with gzip.open(path,"rt") as f:
        source=csv.reader(f,delimiter="\t")
        samples=next(source)[3:]
        for row in source:
            ref=versionless.get(row[0].split(".")[0])
            if ref:
                assert ref not in table
                table[ref]=np.array(row[3:],float)
                versions[ref]=row[0]
    return samples,table,versions


def main(args):
    out=args.out
    out.mkdir(exist_ok=True,parents=True)
    known,ref=refseq(args.refseq)
    cat=catalog(args.cdna,known)
    write(out/"refseq.tsv","accession protein_length class",ref)
    labels,results,libs=[],[],[]
    for region,path,groups in [
        ("hippocampus",args.hippo,[("neuronal","S_Ctrl_","S_KO_"),("global","WT_","KO_"),("progenitor","N_Ctrl_","N_KO_")]),
        ("cortex",args.cortex,[("neuronal","CRTX_S_Ctrl_","CRTX_S_KO_")])]:
        samples,x,versions=load(path,cat)
        for tx,(biotype,cl,full) in cat.items():
            labels.append([region,tx,versions.get(tx,"missing"),biotype,cl,full,
                           np.mean(x[tx]) if tx in x else "NA"])
        all_tpm=sum(x.values())
        for mode in ("all_cassette","complete_ORF"):
            sums={}
            for kind in MOTIFS:
                sums[kind]=sum((x[tx] for tx,(_,cl,full) in cat.items() if cl==kind and tx in x and
                                (mode=="all_cassette" or full)),start=np.zeros(len(samples)))
            classified=sums["flip"]+sums["flop"]
            if np.any(classified==0):raise ValueError("No classifiable abundance")
            frac=sums["flip"]/classified
            coverage=classified/all_tpm
            lower=sums["flip"]/all_tpm
            upper=1-sums["flop"]/all_tpm
            for name,wt,ko in groups:
                controls=[i for i,t in enumerate(samples) if t.startswith(wt)]
                cases=[i for i,t in enumerate(samples) if t.startswith(ko)]
                assert min(len(controls),len(cases))>=2
                ix=controls+cases
                def diff(omit=None):
                    return frac[[i for i in cases if i!=omit]].mean()-frac[[i for i in controls if i!=omit]].mean()
                d=diff()
                loo=[diff(i) for i in ix]
                bound_min=lower[cases].mean()-upper[controls].mean()
                bound_max=upper[cases].mean()-lower[controls].mean()
                usable=min(classified[ix])>=10 and min(coverage[ix])>=.8
                results.append([region,name,mode,len(controls),len(cases),frac[controls].mean(),frac[cases].mean(),d,
                                min(loo),max(loo),min(classified[ix]),min(coverage[ix]),bound_min,bound_max,usable])
                for i in ix:libs.append([region,name,mode,samples[i],sums["flip"][i],sums["flop"][i],all_tpm[i],
                                         coverage[i],frac[i]])
    write(out/"annotations.tsv","region annotation measured_id biotype class complete_ORF mean_TPM",labels)
    write(out/"contrasts.tsv","region genotype method n_control n_KO control_flip_share KO_flip_share difference omit_min omit_max min_classified_TPM min_coverage full_attribution_min full_attribution_max eligible",results)
    write(out/"libraries.tsv","region genotype method library flip_TPM flop_TPM total_Gria2_TPM coverage flip_share",libs)
    write(out/"sources.tsv","file sha256",[(p.name,hashlib.sha256(p.read_bytes()).hexdigest()) for k,p in vars(args).items() if k!="out"])


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    for key in ("cdna","refseq","hippo","cortex","out"):p.add_argument(key,type=Path)
    main(p.parse_args())
