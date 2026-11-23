"""Summarize measured axon morphology and bound the effect of missing mouse identifiers."""
import argparse
import csv
from itertools import product
from pathlib import Path
import xml.etree.ElementTree as ET
import zipfile
import numpy as np


def write(path,fields,rows):
    with path.open("w") as f:
        writer=csv.writer(f,delimiter="\t",lineterminator="\n")
        writer.writerow(fields.split())
        writer.writerows(rows)


def animal_bounds(values, mice):
    # Restricted growth sequences enumerate each unlabeled partition exactly once.
    def partitions(prefix, highest):
        if len(prefix)==len(values):
            if highest==mice-1: yield prefix
            return
        if highest+1+len(values)-len(prefix)<mice:return
        for label in range(min(highest+1,mice-1)+1):
            yield from partitions(prefix+[label],max(highest,label))
    means=[]
    for group in partitions([0],0):
        weight=np.bincount(group)
        means.append(np.mean(np.bincount(group,weights=values)/weight))
    return min(means),max(means),len(means)


def main(source,out):
    specs=[(1,"K","L","mean_internode_um",8,9),(1,"H","I","myelinated_branch_points_pct",7,7),
           (1,"B","C","distance_first_myelin_um",8,8),(1,"E","F","distance_first_branch_um",8,8),
           (3,"E","F","mean_node_um",7,8)]
    stats=[]
    with zipfile.ZipFile(source) as book:
        for index,col1,col2,endpoint,n1,n2 in specs:
            root=ET.fromstring(book.read(f"xl/worksheets/sheet{index}.xml"))
            groups=[]
            for column,n in [(col1,n1),(col2,n2)]:
                numbers=[]
                for c in root.findall(".//{*}c"):
                    ref=c.get("r")
                    if ref.rstrip("0123456789")!=column or c.get("t")=="s":continue
                    v=c.findtext("{*}v")
                    if v is not None and int(ref[len(column):])>=5:numbers.append(float(v))
                assert len(numbers)==n,(endpoint,column,numbers)
                groups.append(np.array(numbers))
            ctrl,mut=groups
            clo,chi,nc=animal_bounds(ctrl,5)
            mlo,mhi,nm=animal_bounds(mut,3)
            loo=[np.delete(mut,i).mean()-ctrl.mean() for i in range(len(mut))]
            loo+=[mut.mean()-np.delete(ctrl,i).mean() for i in range(len(ctrl))]
            order=np.mean([(float(b>a)+.5*float(b==a)) for a,b in product(ctrl,mut)])
            stats.append([endpoint,n1,n2,5,3,ctrl.mean(),mut.mean(),mut.mean()-ctrl.mean(),
                          min(loo),max(loo),order,mlo-chi,mhi-clo,nc,nm])
    write(out/"geometry.tsv","endpoint ctrl_cells mutant_cells ctrl_mice mutant_mice ctrl_mean mutant_mean delta omit_cell_min omit_cell_max descriptive_pair_superiority allocation_bound_min allocation_bound_max ctrl_partitions mutant_partitions",stats)


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("source",type=Path)
    p.add_argument("out",type=Path)
    a=p.parse_args()
    a.out.mkdir(exist_ok=True,parents=True)
    main(a.source,a.out)
