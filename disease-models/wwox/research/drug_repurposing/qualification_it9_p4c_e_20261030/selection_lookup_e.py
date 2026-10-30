#!/usr/bin/env python3
"""IT9 P4c-e step 1: feasibility lookup (ChEMBL name search) for the mechanism-cluster representatives named in selection_note_E.md.
Only compound names are sent. Usage: selection_lookup_e.py run --out selection_feasibility.tsv   (live; --help prints this text, no network)"""
import argparse, csv, json, sys, time, urllib.parse
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(HERE.parent / "pharmacological_qualification_it8_p3_20261029"))
NAMES = ["PX-478", "roxadustat", "daprodustat", "vadadustat", "desidustat", "molidustat", "STC-15", "STM2457", "sulfopin", "AG-17724", "BJP-06-005-3", "GNF4877", "GNF2133",
         "D4476", "IC261", "CR8", "nirogacestat", "MK-0752", "osugacestat", "XCT790", "fedratinib", "pacritinib", "belzutifan", "onapristone", "asoprisnil", "AZD1080"]
def main():
    ap = argparse.ArgumentParser(description=__doc__); ap.add_argument("cmd", nargs="?", choices=["run"]); ap.add_argument("--out", default=str(HERE / "selection_feasibility.tsv"))
    a = ap.parse_args()
    if not a.cmd: ap.print_help(); return
    import pharm_qualify as pq
    net = pq.Net(); rows = []; logrows = []
    for n in NAMES:
        net.case = "sel:" + n
        s, p = net.get("https://www.ebi.ac.uk/chembl/api/data/molecule/search.json", params={"q": n, "limit": "5"})
        if s != 200 or not isinstance(p, dict): rows.append([n, "SERVICE_ERROR" if s != 200 else "NO_RECORD", s, "", "", "", "", "", "", "", ""]); continue
        ms = p.get("molecules") or []
        if not ms: rows.append([n, "NO_RECORD", s, "", "", "", "", "", "", "", ""]); continue
        for m in ms[:3]:
            syn = "|".join(sorted({x.get("molecule_synonym") for x in (m.get("molecule_synonyms") or []) if x.get("molecule_synonym")}))[:160]
            rows.append([n, "ROWS_RETRIEVED", s, m.get("molecule_chembl_id"), m.get("pref_name") or "", m.get("max_phase") or "", m.get("molecule_type") or "", m.get("oral"), m.get("parenteral"), m.get("first_approval") or "", syn])
    with open(a.out, "w", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n"); w.writerow(["query_name", "state", "http", "chembl_id", "pref_name", "max_phase", "molecule_type", "oral", "parenteral", "first_approval", "synonyms"]); w.writerows(rows)
    with open(HERE / "selection_service_log.tsv", "w", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n"); w.writerow(["case", "attempt", "status", "seconds", "url", "error"])
        for l in net.log: w.writerow([l["case"], l["attempt"], l["status"], l["seconds"], l["url"], l["error"]])
    print(len(rows), "rows;", len(net.log), "attempts")
if __name__ == "__main__": main()
