"""Exploratory current mixtures compatible with two native probe responses, within stated assumptions."""
import csv
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).parent

def fitted_inhibition(ligand, potency, hill, maximum):
    return maximum / (1 + (potency/ligand)**hill)

def constrain(fractions, limit):
    # The third fraction is one minus the other two.
    return fractions[0]-fractions[2], fractions[1]-fractions[2], limit-fractions[2]

def vertices(inequalities):
    corners=[]
    for (a,b,c),(d,e,f) in combinations(inequalities,2):
        det=a*e-b*d
        if abs(det)<1e-12:continue
        x,y=(c*e-b*f)/det,(a*f-c*d)/det
        if all(i*x+j*y<=k+1e-10 for i,j,k in inequalities):
            corners.append((x,y,1-x-y))
    return corners

def main():
    with (ROOT/"block.tsv").open() as stream:
        measured={r["receptor"]:r for r in csv.DictReader(stream,delimiter="\t")
                  if r["mV"]=="-60" and r["Mg_mM"]=="1" and r["drug_uM"]=="0.36"}
    block=[float(measured[s]["percent_of_remaining_blocked"]) for s in ("BB","BD","DD")]
    residual=[float(measured[s]["fraction_current_after_Mg"]) for s in ("BB","BD","DD")]
    cp_b=fitted_inhibition(10,.049,1.4,.95)
    cp_bd=fitted_inhibition(10,.077,1.4,.59)
    rows=[]
    for cyclodextrin in (False,True):
        nab_bd=fitted_inhibition(10,6.8 if cyclodextrin else 3.3,1,.71 if cyclodextrin else .78)
        nab_d=fitted_inhibition(10,3.2 if cyclodextrin else 1.5,1.2 if cyclodextrin else 1,1 if cyclodextrin else 1.03)
        for tolerance in (0,.03,.06):
            # For compound/subtype pairs without a fitted IC50, make the
            # unknown 10-uM effect a range, rather than equating it to zero.
            probes=[((cp_b,cp_bd,0),(cp_b,cp_bd,.10),.70),
                    ((0,nab_bd,nab_d),(.20,nab_bd,nab_d),.43)]
            domain=[(-1,0,0),(0,-1,0),(1,1,1)]
            for low,high,observed in probes:
                domain.append(constrain(low,observed+tolerance))
                domain.append(constrain([-v for v in high],-observed+tolerance))
            corners=vertices(domain)
            if not corners:
                rows.append([cyclodextrin,tolerance,False]+["NA"]*8)
                continue
            bd=[w[1] for w in corners]
            d_bearing=[w[1]+w[2] for w in corners]
            fixed=[sum(a*b for a,b in zip(w,block)) for w in corners]
            changed=[sum(a*m*b for a,m,b in zip(w,residual,block))/sum(a*m for a,m in zip(w,residual))
                     for w in corners]
            rows.append([cyclodextrin,tolerance,True,min(bd),max(bd),min(d_bearing),max(d_bearing),
                         min(fixed),max(fixed),min(changed),max(changed)])
    with (ROOT/"mixture.tsv").open("w") as stream:
        writer=csv.writer(stream,delimiter="\t",lineterminator="\n")
        writer.writerow("NAB_with_cyclodextrin probe_absolute_tolerance feasible BD_min BD_max D_bearing_min D_bearing_max fixed_weight_block_min_pct fixed_weight_block_max_pct Mg_reweighted_block_min_pct Mg_reweighted_block_max_pct".split())
        writer.writerows(rows)

if __name__=="__main__":
    main()
