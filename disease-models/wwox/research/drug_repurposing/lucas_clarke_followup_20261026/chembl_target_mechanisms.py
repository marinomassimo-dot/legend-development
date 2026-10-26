#!/usr/bin/env python3
"""ChEMBL: compounds per resolved target, by UNIPROT ACCESSION (never by symbol), with the curated
mechanism action and its references, then the compound's max_phase and name.
The repository's chembl adapter answers per drug or per gene (targets, not compounds); this lists compounds
per target, which the adapter does not. Same door (_http), key-less, no account. Writes chembl_mechanisms.tsv
and the raw JSON per target under chembl_raw/. Run from the repository root."""
import json, sys, time
from pathlib import Path
ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "framework" / "adapters"))
import _http
BASE = "https://www.ebi.ac.uk/chembl/api/data"
HERE = Path(__file__).resolve().parent
RAW = HERE / "chembl_raw"; RAW.mkdir(exist_ok=True)
ACC = {"PDK1":"Q15118","PDK2":"Q15119","PDK3":"Q15120","PDK4":"Q16654","PDPK1_collision_control":"O15530",
       "LDHA":"P00338","LDHB":"P07195","LDHC":"P07864","ATF4":"P18848","PERK_EIF2AK3":"Q9NZJ5","GCN2_EIF2AK4":"Q9P2K8",
       "HRI_EIF2AK1":"Q9BQI3","PKR_EIF2AK2":"P19525","EIF2B1":"Q14232","EIF2B2":"P49770","EIF2B3":"Q9NR50","EIF2B4":"Q9UI10",
       "EIF2B5":"Q13144","PPP1R15A":"O75807","PPP1R15B":"Q5SWA1","MCT1_SLC16A1":"P53985"}
def get(url):
    time.sleep(0.4); return _http.get_json(url, timeout=40)
rows = ["label\tuniprot\ttarget_chembl_id\ttarget_name\ttarget_type\tmolecule_chembl_id\tpref_name\tmax_phase\taction_type\tmechanism\trefs"]
log = {}
for label, acc in ACC.items():
    st, t = get(f"{BASE}/target.json?target_components__accession={acc}&limit=50")
    (RAW / f"target_{acc}.json").write_text(json.dumps(t, indent=1)[:200000])
    targets = (t.get("targets") if isinstance(t, dict) else None) or []
    log[label] = {"http": st, "targets": [(x["target_chembl_id"], x["pref_name"], x["target_type"]) for x in targets]}
    for x in targets:
        tid = x["target_chembl_id"]
        st2, m = get(f"{BASE}/mechanism.json?target_chembl_id={tid}&limit=100")
        (RAW / f"mechanism_{tid}.json").write_text(json.dumps(m, indent=1)[:300000])
        for mech in (m.get("mechanisms") if isinstance(m, dict) else None) or []:
            mid = mech["molecule_chembl_id"]
            st3, mol = get(f"{BASE}/molecule/{mid}.json")
            name = (mol.get("pref_name") if isinstance(mol, dict) else None) or ""
            phase = (mol.get("max_phase") if isinstance(mol, dict) else None)
            refs = ";".join(f'{r.get("ref_type")}:{r.get("ref_id")}' for r in (mech.get("mechanism_refs") or []))
            rows.append("\t".join(str(v) for v in [label, acc, tid, x["pref_name"], x["target_type"], mid, name, phase,
                         mech.get("action_type"), (mech.get("mechanism_of_action") or "").replace("\t"," "), refs]))
(HERE / "chembl_mechanisms.tsv").write_text("\n".join(rows) + "\n")
(HERE / "chembl_target_log.json").write_text(json.dumps(log, indent=1))
print(len(rows)-1, "mechanism rows"); print(json.dumps(log)[:1500])
