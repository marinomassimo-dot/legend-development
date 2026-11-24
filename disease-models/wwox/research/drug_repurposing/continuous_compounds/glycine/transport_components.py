"""Decompose the difference in CPM among assigned nuclei at symmetric arm weights."""
import csv
import sys
from pathlib import Path
rows=list(csv.DictReader(Path(sys.argv[1]).open(),delimiter="\t"))
writer=csv.writer(sys.stdout,delimiter="\t",lineterminator="\n")
writer.writerow(("gene","ctrl_CPM","KO_CPM","within_class_delta_CPM","composition_delta_CPM"))
for gene in sorted({r["gene"] for r in rows}):
    by_arm={arm:{r["class"]:r for r in rows if r["gene"]==gene and r["pool"]==arm} for arm in ("ctrl","ko")}
    totals={arm:sum(int(r["UMI"]) for r in cells.values()) for arm,cells in by_arm.items()}
    bulk={arm:1e6*sum(int(r["gene_UMI"]) for r in cells.values())/totals[arm] for arm,cells in by_arm.items()}
    within=mix=0
    for cell in by_arm["ctrl"]:
        weights=[]; rates=[]
        for arm,cells in by_arm.items():
            r=cells[cell]; depth=int(r["UMI"])
            weights.append(depth/totals[arm]); rates.append(1e6*int(r["gene_UMI"])/depth)
        within+=sum(weights)/2*(rates[1]-rates[0])
        mix+=sum(rates)/2*(weights[1]-weights[0])
    assert abs(within+mix-(bulk['ko']-bulk['ctrl']))<1e-8
    writer.writerow([gene,*[f"{v:.4f}" for v in (bulk['ctrl'],bulk['ko'],within,mix)]])
