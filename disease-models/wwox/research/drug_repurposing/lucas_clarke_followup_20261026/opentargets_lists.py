#!/usr/bin/env python3
"""Open Targets: the LIST of drug/clinical candidates per resolved target (Ensembl ids from target_resolution.tsv), with
max clinical stage and diseases. The repository's opentargets adapter returns only the COUNT of candidates
(`drug_and_clinical_candidates`), so the adapter is also called for the same targets and both numbers are written side by side.
Output opentargets_lists.tsv and opentargets_adapter_counts.tsv. Key-less; no account."""
import json, sys, time
from pathlib import Path
ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT/"framework"/"adapters")); sys.path.insert(0, str(ROOT))
import _http
from framework.adapters import opentargets
HERE = Path(__file__).resolve().parent
T = {"PDK1":"ENSG00000152256","PDK2":"ENSG00000005882","PDK3":"ENSG00000067992","PDK4":"ENSG00000004799","PDPK1_control":"ENSG00000140992",
     "LDHA":"ENSG00000134333","LDHB":"ENSG00000111716","LDHC":"ENSG00000166796","ATF4":"ENSG00000128272","EIF2AK3":"ENSG00000172071",
     "EIF2AK4":"ENSG00000128829","EIF2AK1":"ENSG00000086232","EIF2AK2":"ENSG00000055332","EIF2B1":"ENSG00000111361","EIF2B2":"ENSG00000119718",
     "EIF2B3":"ENSG00000070785","EIF2B4":"ENSG00000115211","EIF2B5":"ENSG00000145191","PPP1R15A":"ENSG00000087074","PPP1R15B":"ENSG00000158615",
     "EIF2S1":"ENSG00000134001","SLC16A1":"ENSG00000155380"}
Q = """query($id:String!){target(ensemblId:$id){approvedSymbol drugAndClinicalCandidates{count rows{maxClinicalStage drug{id name drugType}diseases{disease{name}diseaseFromSource}}}}}"""
rows = ["label\tensembl\tlist_count\tmolecule\tname\tdrugType\tmaxClinicalStage\tdiseases"]; counts = ["label\tensembl\tlist_count\tadapter_count"]
for lab, e in T.items():
    time.sleep(0.4)
    st, p = _http.get_json("https://api.platform.opentargets.org/api/v4/graphql", body={"query": Q, "variables": {"id": e}}, timeout=40)
    tg = ((p.get("data") or {}).get("target") if isinstance(p, dict) else None) or {}
    d = tg.get("drugAndClinicalCandidates") or {}
    for r in d.get("rows") or []:
        rows.append("\t".join([lab, e, str(d.get("count")), r["drug"]["id"], r["drug"]["name"], r["drug"]["drugType"], str(r["maxClinicalStage"]),
                   "; ".join(sorted({(x["disease"] or {}).get("name") or x["diseaseFromSource"] for x in r["diseases"]}))[:200]]))
    time.sleep(0.4)
    a = opentargets.query({"ensembl_id": e, "size": 1})
    ac = [h for h in a["hits"] if h.get("kind") == "target_summary"]
    counts.append("\t".join([lab, e, str(d.get("count")), str(ac[0]["drug_and_clinical_candidates"] if ac else a["status"])]))
(HERE/"opentargets_lists.tsv").write_text("\n".join(rows)+"\n"); (HERE/"opentargets_adapter_counts.tsv").write_text("\n".join(counts)+"\n")
print("\n".join(counts))
