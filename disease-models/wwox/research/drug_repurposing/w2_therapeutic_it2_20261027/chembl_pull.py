#!/usr/bin/env python3
"""ChEMBL REST pulls used by the W2 package (key-less, read-only; scientist-c 2026-10-27): memantine (CHEMBL807) IC50/Ki rows on human or
unknown-origin NMDAR targets (human AND Rattus norvegicus; the organism column says which: 22 human, 15 rat in the 2026-10-27 pull), bumetanide (CHEMBL1072) rows on the NKCC1 target (CHEMBL1615383), and the curated mechanism rows of both.
NOT WWOX EVIDENCE. Usage: chembl_pull.py <out_dir>"""
import json
import sys
import urllib.request
if len(sys.argv) != 2 or sys.argv[1] in ("-h", "--help"):
    print(__doc__)
    raise SystemExit(0 if sys.argv[1:2] in (["-h"], ["--help"]) else 2)
out = sys.argv[1]
B = "https://www.ebi.ac.uk/chembl/api/data/"
def get(u):
    with urllib.request.urlopen(B + u, timeout=60) as r:
        return json.load(r)
with open(out + "/chembl_w2_rows.tsv", "w") as o:
    o.write("molecule\ttarget\ttype\trelation\tvalue\tunits\tassay\tdocument\n")
    for mol, q in (("memantine", "activity.json?molecule_chembl_id=CHEMBL807&standard_type__in=IC50,Ki&limit=200"),
                   ("bumetanide", "activity.json?molecule_chembl_id=CHEMBL1072&target_chembl_id=CHEMBL1615383&limit=50")):
        for a in get(q)["activities"]:
            if mol == "memantine" and not (a["standard_value"] and "NMDA" in (a["target_pref_name"] or "") or "N-methyl" in (a["target_pref_name"] or "")):
                continue
            o.write("\t".join(str(x) for x in (mol, a["target_pref_name"], a.get("target_organism"), a["standard_type"], a["standard_relation"], a["standard_value"], a["standard_units"], (a["assay_description"] or "")[:110], a.get("document_chembl_id"))) + "\n")
    for mol in ("CHEMBL807", "CHEMBL1072", "CHEMBL1214124"):
        m = get("mechanism.json?molecule_chembl_id=" + mol)["mechanisms"]
        o.write(f"# mechanism rows for {mol}: " + json.dumps([(x["mechanism_of_action"], x["target_chembl_id"]) for x in m]) + "\n")
