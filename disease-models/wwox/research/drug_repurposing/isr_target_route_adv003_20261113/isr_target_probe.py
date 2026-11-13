#!/usr/bin/env python3
"""ADV-003: by-target ChEMBL queries for the ISR / eIF2B subunit targets, with the service state recorded at run time.

Plain urllib, a generic client name, public REST, no key, no contact identifier in any request. At most two attempts
per request (a failing endpoint is a result, no retry against protection). Writes target_map.tsv, activity_counts.tsv,
mechanism_rows.tsv, activity_rows.tsv, molecule_lookup.tsv, service_state.tsv next to this file.
Run: python3 isr_target_probe.py [--help]
"""
import csv
import json
import os
import sys
import time
import urllib.parse
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = "https://www.ebi.ac.uk/chembl/api/data"
UA = {"User-Agent": "legend-public-probe"}
GENES = {"EIF2B1": "Q14232", "EIF2B2": "P49770", "EIF2B3": "Q9NR50", "EIF2B4": "Q9UI10", "EIF2B5": "Q13144",
         "EIF2AK1": "Q9BQI3", "EIF2AK2": "P19525", "EIF2AK3": "Q9NZJ5", "EIF2AK4": "Q9P2K8",
         "EIF2S1": "P05198", "PPP1R15A": "O75807", "PPP1R15B": "Q5SWA1"}
MOLS = ["ISRIB", "trans-ISRIB", "2BAct", "salubrinal", "guanabenz", "sephin1", "GSK2606414", "GSK2656157", "ABBV-CLS-7262", "fosigotifator"]
STATE = []


def get(path, tries=2):
    url = path if path.startswith("http") else f"{BASE}/{path}"
    t0 = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=60) as r:
                body = r.read()
                STATE.append((t0, url[:110], r.status, len(body)))
                return json.loads(body)
        except Exception as e:  # noqa
            last = e
            code = getattr(e, "code", "ERR")
            STATE.append((t0, url[:110], code, 0))
            time.sleep(3)
    return {"_error": str(last)}


def tsv(name, header, rows):
    with open(os.path.join(HERE, name), "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(header)
        w.writerows(rows)


def main():
    if "--help" in sys.argv or "-h" in sys.argv:
        print(__doc__)
        return
    d = get("status.json")
    before = (time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), d.get("status"), d.get("chembl_db_version"), d.get("_error", ""))
    tmap, counts, mech, acts = [], [], [], []
    for gene, acc in GENES.items():
        d = get(f"target.json?target_components__accession={acc}&limit=20")
        if "_error" in d:
            tmap.append([gene, acc, "ERROR", d["_error"][:80]]); continue
        ts = d.get("targets", [])
        if not ts:
            tmap.append([gene, acc, "NO_TARGET_RECORD", ""]); continue
        for t in ts:
            tid = t["target_chembl_id"]
            tmap.append([gene, acc, tid, f"{t.get('target_type')}; {t.get('pref_name')}; {t.get('organism')}"])
            a = get(f"activity.json?target_chembl_id={tid}&limit=1")
            total = a.get("page_meta", {}).get("total_count", "ERROR") if "_error" not in a else "ERROR"
            m = get(f"mechanism.json?target_chembl_id={tid}&limit=100")
            mrows = m.get("mechanisms", []) if "_error" not in m else []
            counts.append([gene, tid, total, len(mrows) if "_error" not in m else "ERROR"])
            for r in mrows:
                mech.append([gene, tid, r.get("molecule_chembl_id"), r.get("mechanism_of_action"), r.get("action_type"), r.get("max_phase") or ""])
            if isinstance(total, int) and total:
                url = f"activity.json?target_chembl_id={tid}&limit=1000"
                n = 0
                while url and n < 3000:
                    ad = get(url)
                    if "_error" in ad:
                        break
                    for r in ad["activities"]:
                        acts.append([gene, tid, r.get("molecule_chembl_id"), r.get("parent_molecule_chembl_id"), r.get("molecule_pref_name") or "",
                                     r.get("standard_type") or "", r.get("standard_relation") or "", r.get("standard_value") or "", r.get("standard_units") or "",
                                     r.get("assay_chembl_id"), (r.get("assay_description") or "")[:160].replace("\t", " "), r.get("assay_type"), r.get("document_chembl_id")])
                        n += 1
                    nx = ad["page_meta"].get("next")
                    url = ("https://www.ebi.ac.uk" + nx) if nx else None
    mol = []
    for name in MOLS:
        d = get(f"molecule/search.json?q={urllib.parse.quote(name)}&limit=5")
        ms = d.get("molecules", []) if "_error" not in d else []
        if not ms:
            mol.append([name, "", "", "NO_RESULT" if "_error" not in d else "ERROR"])
        for m in ms:
            mol.append([name, m["molecule_chembl_id"], m.get("pref_name") or "", m.get("max_phase")])
    d = get("status.json")
    after = (time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), d.get("status"), d.get("chembl_db_version"), d.get("_error", ""))
    tsv("target_map.tsv", ["gene", "uniprot", "target_chembl_id_or_state", "type_name_organism"], tmap)
    tsv("activity_counts.tsv", ["gene", "target_chembl_id", "activity_total_count", "mechanism_rows"], counts)
    tsv("mechanism_rows.tsv", ["gene", "target", "molecule", "mechanism_of_action", "action_type", "max_phase"], mech)
    tsv("activity_rows.tsv", ["gene", "target", "molecule", "parent_molecule", "pref_name", "type", "relation", "value", "units", "assay", "assay_description", "assay_type", "document"], acts)
    tsv("molecule_lookup.tsv", ["query_name", "molecule", "pref_name", "max_phase"], mol)
    tsv("service_state.tsv", ["utc", "request_or_phase", "http_status_or_state", "bytes_or_version"],
        [(before[0], "status.json BEFORE", before[1], before[2])] + [(a, b, c, str(d_)) for a, b, c, d_ in STATE] + [(after[0], "status.json AFTER", after[1], after[2])])
    print("before:", before, "after:", after, "targets:", len(tmap), "activity rows:", len(acts))


if __name__ == "__main__":
    main()
