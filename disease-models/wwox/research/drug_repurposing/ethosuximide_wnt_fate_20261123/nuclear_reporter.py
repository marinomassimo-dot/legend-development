"""Audit the measured ethosuximide row in the deposited C2C12 nuclear beta-catenin screen."""
import argparse
import csv
import hashlib
from pathlib import Path
import numpy as np
from analyze import write

COMPOUNDS={"ethosuximide":3291,"riluzole":5070,"methotrexate":126941,"rotenone":6758}


def main(path,out):
    with path.open() as stream:
        all_rows=list(csv.DictReader(stream))
    units,=[r for r in all_rows if r["PUBCHEM_RESULT_TAG"]=="RESULT_UNIT"]
    rows=[r for r in all_rows if r["PUBCHEM_RESULT_TAG"].isdigit()]
    assert len({r["PUBCHEM_SID"] for r in rows})==len(rows)
    assert len(rows)==2509
    quantiles=[]
    examples=[]
    for c in (2,10):
        key=f"Activity at {c} uM"
        assert units[key]=="PERCENT"
        x=np.array([float(r[key]) for r in rows])
        quantiles.append([c,len(x),sum(x>=40),*np.quantile(x,[.05,.5,.95])])
        for name,cid in COMPOUNDS.items():
            r,=[r for r in rows if r["PUBCHEM_CID"]==str(cid)]
            value=float(r[key])
            examples.append([name,cid,r["PUBCHEM_SID"],c,value,r["PUBCHEM_ACTIVITY_OUTCOME"],
                             sum(x<value),sum(x==value),len(x)])
    write(out/"nuclear_screen.tsv","exposure_uM n_substances n_at_least_40pct pct05 median pct95",quantiles)
    write(out/"nuclear_controls.tsv","compound CID SID exposure_uM activity_percent author_call n_lower n_equal n_substances",examples)
    write(out/"nuclear_input.tsv","file sha256",[[path.name,hashlib.sha256(path.read_bytes()).hexdigest()]])


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("table",type=Path)
    p.add_argument("out",type=Path)
    a=p.parse_args()
    main(a.table,a.out)
