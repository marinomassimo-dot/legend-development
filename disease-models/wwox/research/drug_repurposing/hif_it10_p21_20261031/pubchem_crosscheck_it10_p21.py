#!/usr/bin/env python3
"""IT10 P2.1: PubChem name-to-CID cross-check against the CID reached from the ChEMBL InChIKey (identity_it10_p21.tsv). Key-less PUG REST, nothing personal sent.
A name hit can be a salt, a mixture or an isomer: the table records both CIDs and the title of each; equality is not asserted when they differ."""
import csv, json, time, urllib.parse, urllib.request
from pathlib import Path
HERE = Path(__file__).resolve().parent
NAMEQ = {"PX-478": "PX-478", "echinomycin": "echinomycin", "acriflavine": "acriflavine", "KC7F2": "KC7F2", "topotecan": "topotecan", "digoxin": "digoxin", "BAY 87-2243": "BAY 87-2243",
         "belzutifan": "belzutifan", "PT2385": "PT2385", "daprodustat": "daprodustat", "vadadustat": "vadadustat", "molidustat": "molidustat", "enarodustat": "enarodustat",
         "desidustat": "desidustat", "roxadustat": "roxadustat", "IOX2": "IOX2", "DMOG": "dimethyloxalylglycine"}
def get(u):
    for i in range(3):
        try: return json.loads(urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0 research-fetch"}), timeout=40).read())
        except Exception as e: err = getattr(e, "code", str(e)[:40]); time.sleep(1.5)
    return {"error": err}
ident = {r["compound"]: r for r in csv.DictReader((HERE / "identity_it10_p21.tsv").open(), delimiter="\t")}
rows = []
for k, n in NAMEQ.items():
    d = get("https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/" + urllib.parse.quote(n) + "/property/Title,MolecularFormula,MolecularWeight,InChIKey/JSON")
    p = (d.get("PropertyTable", {}).get("Properties") or [{}])[0]
    mine = ident.get(k, {}).get("pubchem_cid", "")
    rows.append([k, n, p.get("CID", d.get("error", "")), p.get("Title", ""), p.get("MolecularFormula", ""), p.get("MolecularWeight", ""), p.get("InChIKey", ""), mine,
                 "same_CID" if str(p.get("CID")) == str(mine) else ("different_CID_or_not_reached: see title/formula" if mine or p.get("CID") else "name_not_found")])
    time.sleep(0.4)
with (HERE / "pubchem_crosscheck_it10_p21.tsv").open("w", newline="") as h:
    w = csv.writer(h, delimiter="\t"); w.writerow(["compound", "name_queried", "pubchem_cid_by_name", "title", "formula", "mwt", "inchikey_by_name", "pubchem_cid_by_chembl_inchikey", "comparison"]); w.writerows(rows)
for r in rows: print("\t".join(map(str, r)))
