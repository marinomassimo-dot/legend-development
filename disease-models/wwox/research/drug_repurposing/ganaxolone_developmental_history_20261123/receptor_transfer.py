"""Explore which in-vitro receptor-mixture predictions survive uncertain Hill slopes."""
import csv
from itertools import product
from math import hypot
from pathlib import Path

OUT = Path(__file__).parent / "results"

# Modgil et al. 2017, Table 1: EC50 nM, maximum total response as % GABA-alone,
# SEM of pEC50, SEM of the maximum. Receptors are in the order shown below.
PAIRS = {
    "ganaxolone": ((256,400,.2,27),(94,225,.1,8)),
    "allopregnanolone": ((115,229,.2,19),(57,426,.3,42)),
}
CONCENTRATIONS = (10,30,100,300,1000,3000)
SLOPES = (.7,1,1.5)


def write(name, columns, rows):
    with (OUT/name).open("w") as stream:
        writer=csv.writer(stream,delimiter="\t",lineterminator="\n")
        writer.writerow(columns.split())
        writer.writerows(rows)


def gain(concentration, parameters, slope):
    ec50, maximum = parameters[:2]
    return (maximum-100)/(1+(ec50/concentration)**slope)


def corners(parameters):
    ec50,maximum,log_se,max_se=parameters
    return [(ec50*10**(scale*log_se),maximum+sign*max_se)
            for scale,sign in product((-1,1),repeat=2)]


def main():
    rows,anchors=[],[]
    for compound,(syn,extra) in PAIRS.items():
        anchors.append([compound,extra[0]/syn[0],(extra[1]-100)-(syn[1]-100),
                        min(a[1]-b[1] for a,b in product(corners(extra),corners(syn))),
                        max(a[1]-b[1] for a,b in product(corners(extra),corners(syn)))])
        for c in CONCENTRATIONS:
            syn_gain=gain(c,syn,1)
            extra_gain=gain(c,extra,1)
            reasonable=[gain(c,extra,he)-gain(c,syn,hs) for hs,he in product(SLOPES,repeat=2)]
            wide=[gain(c,e,he)-gain(c,s,hs) for s,e,hs,he in
                  product(corners(syn),corners(extra),SLOPES,SLOPES)]
            rows.append([compound,c,syn_gain,extra_gain,extra_gain-syn_gain,
                         min(reasonable),max(reasonable),min(wide),max(wide)])
    write("receptor_mixture.tsv","compound concentration_nM syn_gain extra_gain extra_minus_syn slope_min slope_max corner_min corner_max",rows)
    write("receptor_anchors.tsv","compound extra_over_syn_EC50 extra_minus_syn_max_gain lower_corner_max_gain upper_corner_max_gain",anchors)
    # Independent-arm descriptive SE. No animal-level variance or covariance is available.
    groups={"vehicle":(43.9,5.7),"ganaxolone":(57.4,6.3),
            "allopregnanolone":(95.8,10.8),"SGE516":(123.0,22.2)}
    comparisons=[]
    for a,b in [("ganaxolone","vehicle"),("allopregnanolone","vehicle"),
                ("SGE516","vehicle"),("ganaxolone","allopregnanolone")]:
        delta=groups[a][0]-groups[b][0]
        se=hypot(groups[a][1],groups[b][1])
        comparisons.append([a,b,delta,se,delta-2*se,delta+2*se])
    write("washout_comparisons.tsv","group reference delta_pA descriptive_SE minus_2SE plus_2SE",comparisons)


if __name__=="__main__":
    main()
