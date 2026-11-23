"""Recompute mixed-receptor block from Yi et al. Table 3; preserve the current denominator."""
import argparse
import csv
import hashlib
from pathlib import Path
import re
from xml.etree import ElementTree

ROOT=Path(__file__).parent
EXPECTED="87ee420f6086fb5a93fe88a7fadb5a5462de32bcf213494f9986d422ee5be011"

def fractional_block(c, potency, slope):
    return 1/(1+(potency/c)**slope)

def main(path):
    assert hashlib.sha256(path.read_bytes()).hexdigest()==EXPECTED
    tree=ElementTree.parse(path)
    panel,=[t for t in tree.findall(".//table-wrap") if t.findtext("label","").rstrip(".")=="Table 3"]
    fits={}
    for row in panel.findall(".//tbody/tr"):
        cells=["".join(c.itertext()).strip() for c in row]
        agent=cells[0]
        if agent not in ("Mg2+","memantine (control)","memantine (+ Mg2+)"):continue
        voltage=int(cells[1].replace("−","-"))
        for j,subtype in enumerate(("BB","BD","DD")):
            ic,sem=map(float,re.findall(r"[0-9]+(?:\.[0-9]+)?",cells[2+j*3])[:2])
            fits[agent,voltage,subtype]=(ic,sem,float(cells[3+j*3]),int(cells[4+j*3]))
    out=[]
    for voltage in (-60,-40,-20):
        for c in (0.18,0.36,0.72,1.0):
            for mg,drug in ((0,"memantine (control)"),(1,"memantine (+ Mg2+)")):
                for subtype in ("BB","BD","DD"):
                    ic,sem,h,n=fits[drug,voltage,subtype]
                    block=fractional_block(c,ic,h)
                    # Mg-only IC50 is measured at -60 and -40 but not -20 mV.
                    residual=1.0 if not mg else None
                    if mg and ("Mg2+",voltage,subtype) in fits:
                        icmg,_,hmg,_=fits["Mg2+",voltage,subtype]
                        residual=1-fractional_block(1000,icmg,hmg)
                    absolute=100*block*residual if residual is not None else None
                    out.append([voltage,c,mg,subtype,ic,sem,h,n,100*block,
                        100*fractional_block(c,ic+sem,h),100*fractional_block(c,ic-sem,h),
                        residual,absolute])
    with (ROOT/"block.tsv").open("w") as stream:
        writer=csv.writer(stream,delimiter="\t",lineterminator="\n")
        writer.writerow("mV drug_uM Mg_mM receptor IC50_uM IC50_SEM hill oocytes percent_of_remaining_blocked lower_at_IC50_plus_SEM upper_at_IC50_minus_SEM fraction_current_after_Mg extra_loss_points_of_Mg_free_current".split())
        writer.writerows(["NA" if value is None else value for value in row] for row in out)

if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("source_xml",type=Path)
    main(p.parse_args().source_xml)
