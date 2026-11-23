"""Reanalyse individual adult SV2A PET rows and bound a co-occupancy counterfactual."""
import argparse
import csv
import hashlib
from collections import Counter
from math import sqrt
from pathlib import Path
import re
from statistics import mean
from xml.etree import ElementTree

HERE = Path(__file__).resolve().parent
PET_SHA = "30b8ede5307587db509d1d9ff4dcfe524a1ddd7ca8affb69ab084e34f531b09c"
COHORT_SHA = "780f42de9b3982fa5bf9bf1e6bb76f71384c943aa197fb2d4de80be7ac7e7a34"


def source(files, relative, expected):
    data = (files / relative).read_bytes()
    assert hashlib.sha256(data).hexdigest() == expected
    return ElementTree.fromstring(data)


def table_two(article):
    return next(t for t in article.findall(".//table-wrap") if t.findtext("label", "").upper().split() == ["TABLE", "2"])


def write(name, columns, rows):
    with (HERE / name).open("w") as stream:
        writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
        writer.writerow(columns.split())
        writer.writerows(rows)


def individual_pet(table):
    # Table 2 uses HTML row spans for repeated conditions and subject identifiers.
    active = {}
    observations = []
    for row in table.findall(".//tbody/tr"):
        filled = {col: value for col, (remaining, value) in active.items()}
        active = {col: (remaining-1, value) for col, (remaining, value) in active.items() if remaining > 1}
        col = 0
        for cell in row:
            while col in filled:
                col += 1
            width = int(cell.get("colspan", 1))
            length = int(cell.get("rowspan", 1))
            value = " ".join("".join(cell.itertext()).split())
            for pos in range(col, col + width):
                filled[pos] = value
                if length > 1:
                    active[pos] = length-1, value
            col += width
        if filled[0] in ("2", "3"):
            observations.append((filled[2], int(filled[1]), filled[3], float(filled[5]), float(filled[6])/100))
    assert Counter(row[0] for row in observations) == {"BRV":17,"LEV":7}
    return observations


def fit(rows, equal_people):
    multiplicity = Counter(person for _, person, *_ in rows)
    def loss(k):
        return sum((obs-c/(c+k))**2 / (multiplicity[person] if equal_people else 1)
                   for _, person, _, c, obs in rows)
    low, high = .01, 30.
    for _ in range(110):
        left = low+(high-low)/3
        right = high-(high-low)/3
        if loss(left) <= loss(right):
            high = right
        else:
            low = left
    return (low+high)/2


def run(files):
    pet = source(files, "deepening_downloads/brivaracetam_loop_20261123/PMC6532410.1.xml", PET_SHA)
    wwox = source(files, "fulltext/PMID36779245_Oliver2023_PMC_r2.xml", COHORT_SHA)
    observations = individual_pet(table_two(pet))
    write("pet_rows.tsv", "drug subject condition plasma_mg_L observed_occupancy", observations)
    fits = []
    for drug in ("BRV", "LEV"):
        rows = [r for r in observations if r[0] == drug]
        people = {r[1] for r in rows}
        individual_weight = fit(rows, True)
        omit = [fit([r for r in rows if r[1]!=removed], True) for removed in sorted(people)]
        error = [abs(r[4]-r[3]/(r[3]+fit([v for v in rows if v[1]!=r[1]], True))) for r in rows]
        fits.append((drug,len(rows),len(people),fit(rows,False),individual_weight,min(omit),max(omit),100*mean(error)))
    write("pet_fits.tsv","drug rows persons row_weighted_IC50 person_weighted_IC50 omit_person_min omit_person_max left_out_MAE_pp",fits)

    asm_row = next(r for r in table_two(wwox).findall(".//tr") if "ASMs trialed" in "".join(r[0].itertext()))
    histories = []
    for i,cell in enumerate(list(asm_row)[1:],1):
        history = set(re.findall(r"[A-Z]{2,}", "".join(cell.itertext())))
        current = set(re.findall(r"[A-Z]{2,}", " ".join("".join(u.itertext()) for u in cell.findall(".//underline"))))
        assert current <= history
        histories.append([i,*[int(d in a) for d in ("BRV","LEV","PHB","CBZ","VPA") for a in (history,current)]])
    assert len(histories)==13
    write("cohort_exposure.tsv","published_number BRV_ever BRV_current LEV_ever LEV_current PHB_ever PHB_current CBZ_ever CBZ_current VPA_ever VPA_current",histories)

    # These are plasma concentration scenarios, not simulated patients or treatment regimens.
    results=[]
    for fit_name,kb,kl in [("paper",.46,4.02),("person_weighted",fits[0][4],fits[1][4])]:
        for name,clearance in [("reference",1),("PB",1.408),("CBZ",1.479),("VPA",.899)]:
            cb=2.10/clearance
            x=cb/kb
            for cl in sorted({0.,*[r[3] for r in observations if r[0]=="LEV"]}):
                y=cl/kl
                b,l=x/(1+x+y),y/(1+x+y)
                added=b+l-y/(1+y)
                results.append((fit_name,name,cb,cl,b,l,b+l,added))
    write("occupancy_scenarios.tsv","fit BRV_context BRV_mg_L LEV_mg_L BRV_fraction LEV_fraction total_fraction increment_over_LEV",results)
    x=2.10/.46
    cutoff=4.02*((sqrt(x*x+4*x/.10)-x)/2-1)
    print(f"10-point sensitivity threshold at reference exposure: {cutoff:.3f} mg/L LEV")
    print("Cohort counts:", list(map(sum,zip(*(r[1:] for r in histories)))))
    print(fits)


if __name__ == "__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files",type=Path)
    run(parser.parse_args().files)
