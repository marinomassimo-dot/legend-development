"""ADV-147 post hoc (labelled): per-cell number of detected genes from the same matrix; stdlib only."""
import gzip,json
nz=None
with gzip.open("cortexdev_expr.tsv.gz","rt") as f:
    hdr=f.readline().rstrip("\n").split("\t")[1:]
    nz=[0]*len(hdr)
    for line in f:
        parts=line.rstrip("\n").split("\t")[1:]
        for i,v in enumerate(parts):
            if v!="0" and v!="0.0" and float(v)>0: nz[i]+=1
json.dump(dict(zip(hdr,nz)),open("depth.json","w"))
print(len(hdr),min(nz),max(nz))
