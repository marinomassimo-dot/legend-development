#!/usr/bin/env python3
"""Public ChEMBL REST (key-less). For each name: molecule search (pref_name exact), mechanism,
and parent/salt info. Writes raw JSON into <outdir>/raw/ and a summary TSV. Usage: pull_chembl.py <outdir>.
Records only what the source states."""
import json, sys, urllib.request, urllib.parse, hashlib, os, time
BASE = "https://www.ebi.ac.uk/chembl/api/data/"
NAMES = ["vigabatrin","clobazam","tiagabine","retigabine","azetukalner","ganaxolone","radiprodil","gabazine","xe-991","ethosuximide","N-desmethylclobazam","norclobazam"]
def get(path, **q):
    u = BASE + path + ("?" + urllib.parse.urlencode(q) if q else "")
    with urllib.request.urlopen(u, timeout=60) as r:
        b = r.read()
    return u, b
def main():
    if len(sys.argv) != 2 or sys.argv[1] in ("-h","--help"):
        print(__doc__); return 0 if len(sys.argv) > 1 else 2
    out = sys.argv[1]; os.makedirs(out + "/raw", exist_ok=True)
    rows = []
    for n in NAMES:
        try:
            u, b = get("molecule/search.json", q=n, limit=5)
        except Exception as e:
            rows.append([n, "ERR", str(e)]); continue
        fn = f"{out}/raw/search_{n.replace(' ','_')}.json"; open(fn, "wb").write(b)
        d = json.loads(b)
        for m in d["molecules"][:3]:
            cid = m["molecule_chembl_id"]
            try:
                u2, b2 = get("mechanism.json", molecule_chembl_id=cid, limit=20)
            except Exception as e:
                b2 = b"{}"
            open(f"{out}/raw/mech_{cid}.json", "wb").write(b2)
            mech = json.loads(b2).get("mechanisms", [])
            ms = "; ".join(f"{x.get('action_type')} | {x.get('mechanism_of_action')} | {x.get('target_chembl_id')}" for x in mech)
            rows.append([n, cid, m.get("pref_name"), m.get("max_phase"), (m.get("molecule_properties") or {}).get("full_mwt"),
                         m.get("molecule_type"), m.get("chirality"), (m.get("molecule_hierarchy") or {}).get("parent_chembl_id"), ms,
                         hashlib.sha256(b).hexdigest()[:12]])
            time.sleep(0.2)
    with open(out + "/chembl_identity_mechanism.tsv", "w", encoding="utf8") as fh:
        fh.write("query\tchembl_id\tpref_name\tmax_phase\tfull_mwt\tmolecule_type\tchirality\tparent\tmechanisms\tsearch_sha12\n")
        for r in rows:
            fh.write("\t".join(str(x).replace("\t"," ") for x in r) + "\n")
    print(len(rows), "rows")
    return 0
if __name__ == "__main__": sys.exit(main())
