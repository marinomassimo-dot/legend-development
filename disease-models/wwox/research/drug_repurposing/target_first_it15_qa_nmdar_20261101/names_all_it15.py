"""Identity lookup for every parent compound id in relations_qa.tsv (ChEMBL molecule endpoint, batches of 100, <=2 retries per request via pull_it15_qa.fetch). Writes raw/molecules_all.json. --help safe."""
import argparse, csv, json, os, sys
argparse.ArgumentParser(description=__doc__).parse_args()
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pull_it15_qa as P
H = P.HERE
ids = sorted({r["compound"] for r in csv.DictReader(open(os.path.join(H, "relations_qa.tsv")), delimiter="\t") if r["source"] == "chembl_activity"})
out, fails = {}, []
for i in range(0, len(ids), 100):
    b = ids[i:i+100]
    st, p = P.fetch(f"{P.chembl.BASE}/molecule.json?molecule_chembl_id__in={','.join(b)}&limit=100")
    if st != 200: fails.append(b); continue
    for m in p["molecules"]:
        out[m["molecule_chembl_id"]] = {"pref_name": m.get("pref_name"), "max_phase": m.get("max_phase"), "molecule_type": m.get("molecule_type"), "parent": (m.get("molecule_hierarchy") or {}).get("parent_chembl_id"),
          "synonyms": sorted({s["molecule_synonym"] for s in (m.get("molecule_synonyms") or [])})[:10], "chirality": m.get("chirality")}
    print(i, len(out), flush=True)
json.dump({"requested": len(ids), "found": len(out), "failed_batches": fails, "http_failures": P.FAILS, "molecules": out}, open(os.path.join(H, "raw", "molecules_all.json"), "w"))
print("requested", len(ids), "found", len(out), "failed batches", len(fails))
