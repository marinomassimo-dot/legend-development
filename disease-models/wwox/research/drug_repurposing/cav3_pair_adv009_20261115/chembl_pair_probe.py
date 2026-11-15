#!/usr/bin/env python3
"""ADV-009: ChEMBL activities of efonidipine and flunarizine on Cav3.1/3.2/3.3, Cav1.2 and hERG, by molecule and by target.

Plain urllib, a generic client name, public REST, no key, no contact identifier in any request. At most two attempts per
request (a failing endpoint is a result, no retry against protection). Writes molecule_lookup.tsv, target_map.tsv,
activity_rows.tsv, service_state.tsv into the output folder. No WWOX evidence; a ChEMBL row is a curated transcription.
Run: python3 -I chembl_pair_probe.py <out_dir> [--help]
"""
import csv
import json
import os
import sys
import time
import urllib.parse
import urllib.request

BASE = "https://www.ebi.ac.uk/chembl/api/data"
UA = {"User-Agent": "legend-public-probe"}
MOLS = ["efonidipine", "flunarizine"]
GENES = {"CACNA1G": "O43497", "CACNA1H": "O95180", "CACNA1I": "Q9P0X4", "CACNA1C": "Q13936", "KCNH2": "Q12809"}
STATE = []


def get(path, tries=2):
    url = path if path.startswith("http") else f"{BASE}/{path}"
    t0 = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    last = None
    for _ in range(tries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=60) as r:
                body = r.read()
                STATE.append((t0, url[:140], r.status, len(body)))
                return json.loads(body)
        except Exception as e:  # noqa
            last = e
            STATE.append((t0, url[:140], getattr(e, "code", "ERR"), 0))
            time.sleep(3)
    return {"_error": str(last)}


def tsv(out, name, header, rows):
    with open(os.path.join(out, name), "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(header)
        w.writerows(rows)


def main():
    if "--help" in sys.argv or "-h" in sys.argv or len(sys.argv) < 2:
        print(__doc__)
        return
    out = sys.argv[1]
    os.makedirs(out, exist_ok=True)
    st = get("status.json")
    mols, tmap, acts = [], [], []
    for name in MOLS:
        d = get("molecule/search.json?" + urllib.parse.urlencode({"q": name, "limit": 20}))
        for m in d.get("molecules", []):
            mols.append((name, m.get("molecule_chembl_id"), m.get("pref_name"), m.get("max_phase"),
                         (m.get("molecule_structures") or {}).get("canonical_smiles", "")[:80]))
    mol_ids = {}
    for q, cid, pref, ph, smi in mols:
        if pref and pref.lower().startswith(q[:6]):
            mol_ids.setdefault(q, []).append(cid)
    targets = {}
    for g, acc in GENES.items():
        d = get("target.json?" + urllib.parse.urlencode({"target_components__accession": acc, "limit": 20}))
        for t in d.get("targets", []):
            tmap.append((g, acc, t.get("target_chembl_id"), t.get("target_type"), t.get("pref_name")))
            if t.get("target_type") == "SINGLE PROTEIN":
                targets.setdefault(g, t.get("target_chembl_id"))
    for q, ids in mol_ids.items():
        for cid in ids:
            for g, tid in targets.items():
                d = get("activity.json?" + urllib.parse.urlencode({"molecule_chembl_id": cid, "target_chembl_id": tid, "limit": 200}))
                rows = d.get("activities", [])
                if "_error" in d:
                    acts.append((q, cid, g, tid, "READ_ERROR", d["_error"][:80], "", "", "", "", "", ""))
                elif not rows:
                    acts.append((q, cid, g, tid, "NO_ACTIVITY_ROWS", "", "", "", "", "", "", ""))
                for a in rows:
                    acts.append((q, cid, g, tid, a.get("standard_type"), a.get("standard_relation"), a.get("standard_value"),
                                 a.get("standard_units"), a.get("assay_description", "")[:160], a.get("assay_type"),
                                 a.get("document_chembl_id"), a.get("assay_organism")))
    tsv(out, "molecule_lookup.tsv", ["query", "molecule_chembl_id", "pref_name", "max_phase", "smiles_head"], mols)
    tsv(out, "target_map.tsv", ["gene", "uniprot", "target_chembl_id", "target_type", "pref_name"], tmap)
    tsv(out, "activity_rows.tsv", ["query", "molecule", "gene", "target", "standard_type", "relation", "value", "units",
                                   "assay_description", "assay_type", "document", "organism"], acts)
    tsv(out, "service_state.tsv", ["utc", "url", "status", "bytes"],
        STATE + [("release", str(st.get("chembl_db_version")), str(st.get("status")), st.get("_error", ""))])
    print(f"molecules {len(mols)}; target rows {len(tmap)}; activity rows {len(acts)}; requests {len(STATE)}")


if __name__ == "__main__":
    main()
