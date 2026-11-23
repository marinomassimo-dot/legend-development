"""Summarize six libraries without using sequencing reads as biological replicates."""
import argparse
import csv
from math import sqrt
from pathlib import Path
from statistics import mean


def wilson(successes, trials):
    if not trials:
        return None,None
    z=1.959963984540054
    p=successes/trials
    mid=p+z*z/(2*trials)
    radius=z*sqrt(p*(1-p)/trials + z*z/(4*trials**2))
    denom=1+z*z/trials
    return max(0,(mid-radius)/denom),min(1,(mid+radius)/denom)


def fmt(v):
    return "NA" if v is None else f"{100*v:.5f}"


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("runs",type=Path)
    parser.add_argument("out",type=Path)
    args=parser.parse_args()
    args.out.mkdir(exist_ok=True,parents=True)
    by={}
    with (args.out/"per_library.tsv").open("w") as out:
        print("run\tgroup\tcategory\tA\tG\tother\tA_percent\tcounting_only_lo95\tcounting_only_hi95\tA_distinct_offset\tG_distinct_offset",file=out)
        for f in sorted(args.runs.glob("SRR*.tsv")):
            with f.open() as src:
                for r in csv.DictReader(src,delimiter="\t"):
                    if r["category"]=="low_quality":
                        continue
                    a,g=int(r["A"]),int(r["G"])
                    other=sum(int(r[b]) for b in "CTN")
                    prop=a/(a+g) if a+g else None
                    print(r["run"],r["group"],r["category"],a,g,other,fmt(prop),*map(fmt,wilson(a,a+g)),
                          r["A_distinct_offset"],r["G_distinct_offset"],sep="\t",file=out)
                    by.setdefault(r["category"],[]).append((r["run"],r["group"],a+g,prop))
    with (args.out/"group_difference.tsv").open("w") as out:
        print("category\tKO_libraries\tWT_libraries\tmin_informative_reads\tKO_mean_pct\tWT_mean_pct\tKO_minus_WT_pp\tloo_min_pp\tloo_max_pp",file=out)
        for mode,rows in by.items():
            assert len({r[0] for r in rows})==6 and sum(r[1]=="KO" for r in rows)==4
            def means(data):
                groups=[[p for _,group,_,p in data if group==key] for key in ["KO","WT"]]
                if any(None in values for values in groups):
                    return None,None
                return [mean(v) for v in groups]
            ko,wt=means(rows)
            contrasts=[]
            for omit in range(len(rows)):
                k,w=means([v for i,v in enumerate(rows) if i!=omit])
                if k is not None:
                    contrasts.append(k-w)
            print(mode,4,2,min(r[2] for r in rows),fmt(ko),fmt(wt),fmt(None if ko is None else ko-wt),
                  fmt(min(contrasts) if len(contrasts)==6 else None),fmt(max(contrasts) if len(contrasts)==6 else None),sep="\t",file=out)


if __name__=="__main__":
    main()
