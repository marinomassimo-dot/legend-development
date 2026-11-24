"""Sharp composition-only bound for nuclear Grin1 molecules in GSE158684."""
import csv
import gzip
from pathlib import Path
import sys
from collections import defaultdict

repo, files = map(Path, sys.argv[1:3])
sys.path.insert(0,str(repo/"disease-models/wwox/research/drug_repurposing/ganaxolone_20261123"))
from analyze import assigned_nuclei

counts=defaultdict(dict)
for arm, cell, depth, values in assigned_nuclei(files, [], [], ["Grin1"]):
    counts[arm][cell]=int(values["Grin1"].sum())
weights={}
with open("cell_weights.tsv","w") as f:
    writer=csv.writer(f, delimiter="\t",lineterminator="\n")
    writer.writerow(("pool","cell_class","Grin1_UMI","pool_Grin1_UMI","weight"))
    for arm, assigned in counts.items():
        prefix=files/"geo/GSE158684"/f"GSE158684_{arm}_filtered_"
        with gzip.open(str(prefix)+"features.tsv.gz","rt") as source:
            ids={str(i) for i,line in enumerate(source,1) if line.split("\t")[1]=="Grin1"}
        assert ids
        with gzip.open(str(prefix)+"matrix.mtx.gz","rt") as source:
            next(line for line in source if not line.startswith("%"))
            total=sum(int(parts[2]) for line in source if (parts:=line.split())[0] in ids)
        assigned["unassigned_or_low_depth"]=total-sum(assigned.values())
        assert assigned["unassigned_or_low_depth"]>=0
        weights[arm]={cell:n/total for cell,n in assigned.items()}
        for cell, n in assigned.items():
            writer.writerow((arm,cell,n,total,f"{n/total:.6f}"))
assert weights["ctrl"].keys()==weights["ko"].keys()
bound=sum(abs(weights["ko"][cell]-p) for cell,p in weights["ctrl"].items())/2
print(f"Maximum absolute change among these class weights: {bound*100:.3f} percentage points")
