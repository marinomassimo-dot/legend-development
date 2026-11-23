"""Count exact read-length windows common to the two annotated α7 receptor genes."""
import argparse
import csv
import gzip
import hashlib
from pathlib import Path
import re


def compare(path, out):
    transcripts={}
    gene=None
    with gzip.open(path,"rt") as source:
        for line in source:
            if line.startswith(">"):
                match=re.search(r" gene_symbol:(CHRNA7|CHRFAM7A)(?: |$)",line)
                gene=match[1] if match else None
                if gene:
                    tx=line[1:].split()[0]
                    transcripts.setdefault(gene,{})[tx]=""
            elif gene:
                transcripts[gene][tx]+=line.strip().upper()
    assert set(transcripts)=={"CHRNA7","CHRFAM7A"}
    rows=[]
    for k in (50,75,100):
        def words(seq):
            return [seq[i:i+k] for i in range(len(seq)-k+1)]
        reverse=str.maketrans("ACGT","TGCA")
        pool={}
        for gene,records in transcripts.items():
            direct={w for seq in records.values() for w in words(seq) if "N" not in w}
            pool[gene]=direct|{w.translate(reverse)[::-1] for w in direct}
        for gene,records in transcripts.items():
            other, = set(pool)-{gene}
            for tx,seq in sorted(records.items()):
                w=[v for v in words(seq) if "N" not in v]
                shared=sum(v in pool[other] for v in w)
                rows.append([gene,tx,len(seq),k,len(w),shared,shared/len(w) if w else "NA"])
    with (out/"paralog_windows.tsv").open("w") as stream:
        writer=csv.writer(stream,delimiter="\t",lineterminator="\n")
        writer.writerow("gene transcript length nt_window eligible_positions also_in_other_gene shared_fraction".split())
        writer.writerows(rows)
    with path.open("rb") as stream:
        print(hashlib.file_digest(stream,"sha256").hexdigest())


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("reference",type=Path)
    p.add_argument("out",type=Path)
    a=p.parse_args()
    compare(a.reference,a.out)
