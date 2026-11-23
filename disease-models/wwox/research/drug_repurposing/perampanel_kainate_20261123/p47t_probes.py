"""Generate class-balanced exact nucleotide probes for the downstream Grik1 cassette boundary."""
import csv
import gzip
import itertools
from pathlib import Path
import sys
from kainate_transfer import CODE, LEFT, RIGHT, CASSETTE, tsv

root=Path(__file__).parent
files=Path(sys.argv[1])
ref=next((files/"reference_ensembl_r92").glob("*.fa.gz"))
out=root/"results"
probe_sets={}
def records(fasta):
    with gzip.open(fasta, "rt") as source:
        for is_header, lines in itertools.groupby(source,lambda s:s.startswith(">")):
            if is_header:
                header=next(lines).strip()
            else:
                yield header,"".join(s.strip() for s in lines)

for header,seq in records(ref):
    if "gene_symbol:Grik1 " not in header: continue
    for frame in range(3):
        protein="".join(CODE.get(tuple(seq[i:i+3]),"X") for i in range(frame,len(seq)-2,3))
        for kind,mid in (("insert",CASSETTE),("skip","")):
            start=protein.find(LEFT+mid+RIGHT)
            if start<0: continue
            cut=frame+3*(start+len(LEFT+mid))
            for offset in range(10,22):
                probe_sets.setdefault((kind,offset),set()).add(seq[cut-offset:cut-offset+31])
assert len(probe_sets)==24 and all(len(s)==1 for s in probe_sets.values())
# The existing standalone binary accepts flip/flop as its two input labels.
to_binary={"insert":"flip","skip":"flop"}
rc=str.maketrans("ACGT","TGCA")
probes=[(k,o,next(iter(s))) for (k,o),s in sorted(probe_sets.items())]
matches={(k,o):[0,0] for k,o,_ in probes}
for head,seq in records(ref):
    for k,o,q in probes:
        if q in seq or q.translate(rc)[::-1] in seq:
            matches[k,o][int("gene_symbol:Grik1 " not in head)]+=1
assert all(t>0 and x==0 for t,x in matches.values())
tsv(out/"junction_probe_audit.tsv",["class","offset","Grik1_transcripts","other_transcripts"],
    [(k,o,*matches[k,o]) for k,o,_ in probes])
tsv(out/"junction_probes.tsv",["class","offset","sequence"],
    [(to_binary[k],o,q) for k,o,q in probes])
