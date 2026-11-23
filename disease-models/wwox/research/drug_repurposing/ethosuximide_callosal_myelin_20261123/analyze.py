"""Recalculate animal-level contrasts from four Knowles source-data workbooks."""
import argparse
import csv
import itertools
from collections import defaultdict
from pathlib import Path
from statistics import mean

import openpyxl


def sheet(root, number):
    book = openpyxl.load_workbook(root / f"legend-knowles-{number}.xlsx",
                                  read_only=True, data_only=True)
    try:
        return list(book.active.values)
    finally:
        book.close()


def analyze(root):
    rates, ratios, matched = {}, {}, []
    groups = defaultdict(list)
    for row in sheet(root, 4)[2:33]:
        animal, strain, sex, _, arm, rate = row[:6]
        if isinstance(rate, (int, float)) and arm in {"H20", "ETX"}:
            key = (strain.strip(), arm, animal, sex.strip())
            assert key not in rates
            rates[key] = rate
            groups["seizures/h", *key[:2]].append(rate)
        animal, strain, arm, sex, _, ratio = row[8:14]
        if isinstance(ratio, (int, float)):
            key = (strain, arm, animal, sex)
            assert key not in ratios
            ratios[key] = ratio
            groups["g-ratio", *key[:2]].append(ratio)
    assert len(rates) == 31 and len(ratios) == 13
    for key in ratios:
        if key in rates:
            matched.append((*key, rates[key], ratios[key]))
    out = []
    for metric in ("seizures/h", "g-ratio"):
        arms = [groups[metric, strain, arm]
                for strain, arm in itertools.product(("WAG", "WIS"), ("ETX", "H20"))]
        for (strain, arm), vals in zip(itertools.product(("WAG", "WIS"), ("ETX", "H20")), arms):
            out.append((metric, strain + " " + arm, len(vals), mean(vals)))
        def interaction(means):
            a, b, c, d = means
            return (a - b) - (c - d)
        out.append((metric, "treatment x strain", "", interaction(list(map(mean, arms)))))
        deletions = [[mean(vals[:i] + vals[i + 1:]) for i in range(len(vals))] for vals in arms]
        sensitivity = [interaction(v) for v in itertools.product(*deletions)]
        out.extend([(metric, "omit one per arm: min", "", min(sensitivity)),
                    (metric, "omit one per arm: max", "", max(sensitivity))])
    anatomy = defaultdict(dict)
    for row in sheet(root, 3)[:20]:
        rat, strain, age, _, ratio = row[9:14]
        if isinstance(ratio, (int, float)):
            anatomy["body",age,strain][rat] = ratio
    for row in sheet(root, 12)[:11]:
        rat, strain, age, _, ratio = row[11:16]
        if isinstance(ratio, (int, float)):
            anatomy["splenium",age,strain][rat] = ratio
    delta = {}
    for region, age in (("body",1.5),("body",6),("splenium",6)):
        wag, wis = (anatomy[region,age,g] for g in ("WAG","WIS"))
        delta[region,age] = mean(wag.values()) - mean(wis.values())
        out.append(("untreated g-ratio", f"{region} {age}m: WAG - WIS",
                    f"{len(wag)}/{len(wis)}", delta[region,age]))
    paired = []
    for strain in ("WAG","WIS"):
        body, splenium = (anatomy[r,6,strain] for r in ("body","splenium"))
        shared = sorted(body.keys() & splenium.keys())
        paired.append(mean(body[i] - splenium[i] for i in shared))
        out.append(("matched g-ratio", strain + " body - splenium",len(shared),paired[-1]))
    out.append(("matched g-ratio","region x strain","","%f"%(paired[0] - paired[1])))
    coverage = defaultdict(list)
    for row in sheet(root,10):
        if row[0] in ("WAG","WIS"):
            coverage[row[1],row[0]].append(row[7])
    for age in (1.5,6):
        w,c = (coverage[age,g] for g in ("WAG","WIS"))
        out.append(("myelinated fraction (points)", f"{age}m: WAG - WIS",
                    f"{len(w)}/{len(c)}",mean(w) - mean(c)))
    for title,y0,yt,tick,tops in [
        ("corpus callosum",567,67,160,[159,422,238]),
        ("optic nerve",475,23,180,[123,303,161])]:
        estimates = [(y0-y)*tick/(y0-yt) for y in tops]
        for name,value in zip(("WT","KO","KO + neuronal Wwox"),estimates):
            out.append(("WWOX myelinated axons/field",title+" "+name,3,value))
        wt,ko,add = estimates
        out.append(("fraction of WT-KO gap recovered",title,"",(add-ko)/(wt-ko)))
    return out,matched


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_dir",type=Path)
    args = parser.parse_args()
    outcomes,matched = analyze(args.input_dir)
    for filename,columns,data in [
        ("results.tsv",("measure","contrast","animals","value"),outcomes),
        ("matched_animals.tsv",("strain","arm","animal","sex","seizures_per_hour","g_ratio"),matched)]:
        with open(Path(__file__).parent/filename,"w") as f:
            writer = csv.writer(f,delimiter="\t",lineterminator="\n")
            writer.writerow(columns)
            writer.writerows(data)
