#!/usr/bin/env python3
"""IT10 P2.1 task 2: ClinicalTrials.gov v2 (key-less, no contact string) per alternative, as counts for three slices: all studies naming the intervention; with a
child age group (AREA[StdAge]CHILD); matching a neurological/seizure/stroke term. A zero is 'no hit for that query string on that date', not a negative.
Usage: python3 -I trials_it10_p21.py"""
import csv, json, time, urllib.parse, urllib.request
from pathlib import Path
HERE = Path(__file__).resolve().parent
NAMES = ["PX-478", "echinomycin", "acriflavine", "KC7F2", "topotecan", "digoxin", "BAY 87-2243", "belzutifan", "PT2385", "daprodustat", "vadadustat", "molidustat", "enarodustat", "desidustat", "roxadustat", "IOX2", "dimethyloxalylglycine"]
NEURO = "AREA[ConditionSearch](seizure OR epilepsy OR encephalopathy OR neurodevelopmental OR stroke OR cerebral OR brain)"
def q(name, term=None, size=3):
    p = {"query.intr": name, "pageSize": size, "countTotal": "true", "fields": "NCTId,BriefTitle"}
    if term: p["query.term"] = term
    url = "https://clinicaltrials.gov/api/v2/studies?" + urllib.parse.urlencode(p)
    err = ""
    for i in range(3):
        try:
            return json.loads(urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 research-fetch"}), timeout=60).read())
        except Exception as e: err = str(e)[:60]; time.sleep(2)
    return {"error": err, "studies": [], "totalCount": -1}
rows = []
for n in NAMES:
    a, c, z = q(n), q(n, "AREA[StdAge]CHILD"), q(n, NEURO, 5)
    hits = ";".join(s["protocolSection"]["identificationModule"]["nctId"] + ":" + s["protocolSection"]["identificationModule"].get("briefTitle", "")[:70] for s in z.get("studies", []))
    rows.append([n, a["totalCount"], c["totalCount"], z["totalCount"], hits]); time.sleep(0.3)
with (HERE / "trials_it10_p21.tsv").open("w", newline="") as h:
    w = csv.writer(h, delimiter="\t"); w.writerow(["intervention_query", "studies_all", "studies_with_child_age_group", "studies_neuro_terms_in_condition", "first_neuro_matches(NCT:title)"]); w.writerows(rows)
for r in rows: print("\t".join(map(str, r))[:380])
