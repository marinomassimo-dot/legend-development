"""Identity lookup: ChEMBL molecule endpoint (batches of 40, <=2 retries) for the compound ids that appear in a GluN2B/GluN2A graded comparison, plus the anchor ids. Writes raw/molecules_names.json. --help safe."""
import argparse, csv, json, os, re, sys, time
argparse.ArgumentParser(description=__doc__).parse_args()
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pull_it15_qa as P
H = P.HERE
ids = set()
for x in csv.DictReader(open(os.path.join(H, "graded_comparisons_qa.tsv")), delimiter="\t"):
    t = x["targets_median_nM [n; min-max; censored]"]
    if x["grade"] in ("INTERPRETABLE", "LIMITED") and re.search(r"GRIN2B \[", t) and re.search(r"GRIN2A \[", t): ids.add(x["compound"])
ids |= {"CHEMBL807", "CHEMBL742", "CHEMBL305187", "CHEMBL84612", "CHEMBL182066", "CHEMBL305195"}
ids = sorted(i for i in ids if i.startswith("CHEMBL")); out = {}; log = []
for i in range(0, len(ids), 40):
    url = f"{P.chembl.BASE}/molecule.json?molecule_chembl_id__in={','.join(ids[i:i+40])}&limit=100"
    st, p = P.fetch(url)
    log.append([url[:120], st])
    if st == 200:
        for m in p["molecules"]:
            out[m["molecule_chembl_id"]] = {"pref_name": m.get("pref_name"), "max_phase": m.get("max_phase"), "molecule_type": m.get("molecule_type"),
              "parent": (m.get("molecule_hierarchy") or {}).get("parent_chembl_id"), "inchikey": (m.get("molecule_structures") or {}).get("standard_inchi_key"),
              "synonyms": sorted({s["molecule_synonym"] for s in (m.get("molecule_synonyms") or [])})[:12], "chirality": m.get("chirality")}
json.dump({"log": log, "failures": P.FAILS, "molecules": out, "requested": ids}, open(os.path.join(H, "raw", "molecules_names.json"), "w"))
print(len(ids), "requested", len(out), "found", "failures", len(P.FAILS))
