#!/usr/bin/env python3
"""P9: tool compounds that the P8 pull could not resolve by name. Resolution is by STANDARD InChIKey taken
from PubChem (structure checked there by IUPAC name) and looked up in ChEMBL by that key; nothing is typed
from memory. Then every activity row on NMDA/AMPA/kainate receptor targets is read with the P8 adapter
(molecule-first). Writes toolcompound_raw.json and toolcompound_summary.tsv. Run: python3 pull_toolcompounds_p9.py"""
import json, re, statistics, sys, time
from pathlib import Path
ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT))
from framework.adapters import chembl, _http  # noqa: E402
KEYS = {  # label -> (standard InChIKey as printed by PubChem on 2026-10-29, PubChem CID)
 "Ro 25-6981 (free base, GluN2B NAM)": ("WVZSEUPGUDIELE-HTAPYJJXSA-N", 6604887),
 "NVP-AAM077 / PEAQX (GluN2A-preferring competitive; first-block match only)": ("XXZGNAZRWCBSBK", 73409722),
 "TCN-201 (GluN2A NAM)": ("FYIBXBFDXNPBSF-UHFFFAOYSA-N", 4787937),
 "NAB-14 (GluN2C/2D NAM)": ("WCGIKJOMEYPSIP-UHFFFAOYSA-N", 46862257),
 "D-AP5 (D-APV)": ("VOROEQBFPPIACJ-SCSAIBSYSA-N", 135342),
 "NBQX (competitive AMPA/kainate)": ("UQNAFPHGVPVTAL-UHFFFAOYSA-N", 3272524),
 "GYKI 52466 (non-competitive AMPA)": ("LFBZZHVSGAHQPP-UHFFFAOYSA-N", 3538),
 "L-701,324 (glycine-site antagonist)": ("FLVRDMUHUXVRET-UHFFFAOYSA-N", 54682505),
 "7-chlorokynurenic acid (glycine-site antagonist)": ("UAWVRVFHMOSAPU-UHFFFAOYSA-N", 1884),
 "D-cycloserine (glycine-site partial agonist)": ("DYDCUQKUCUHJBH-UWTATZPHSA-N", 6234),
 "selfotel / CGS 19755 (competitive)": ("LPMRCCNDNGONCD-RITPCOANSA-N", 68736)}
RECEPTOR = re.compile(r"NMDA|glutamate receptor|glutamate \[NMDA\]|AMPA|kainate|GRIA|GRIN|GRIK", re.I)
log = {"retrieved_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "compounds": {}, "rows": []}
for label, (key, cid) in KEYS.items():
    url = "https://www.ebi.ac.uk/chembl/api/data/molecule.json"
    param = {"molecule_structures__standard_inchi_key" + ("__startswith" if len(key) == 14 else ""): key}
    _st, j = _http.get_json(url, params=param)
    time.sleep(1)
    mols = (j.get("molecules") or []) if isinstance(j, dict) else []
    ids = [(m["molecule_chembl_id"], m.get("pref_name"), m.get("max_phase"), (m.get("molecule_structures") or {}).get("canonical_smiles")) for m in mols]
    e = {"pubchem_cid": cid, "inchikey_used": key, "chembl_matches": ids}
    log["compounds"][label] = e
    if not ids: continue
    a = chembl.query({"molecule": ids[0][0], "types": ["IC50", "Ki", "Kd", "EC50", "Kb", "Potency"], "max_rows": 2000})
    e.update(status=a["status"], total_rows_all_targets=a.get("total_count"), truncated=a.get("truncated"), error=a["error"])
    log["rows"] += [dict(h, compound=label) for h in a["hits"] if RECEPTOR.search(h.get("target_pref_name") or "")]
Path("toolcompound_raw.json").write_text(json.dumps(log, indent=1, sort_keys=True))
L = ["compound\tchembl_id\ttarget_chembl_id\ttarget\ttarget_organism\tn_rows\tn_docs\ttypes\tmedian_nM_equal\tmin_nM\tmax_nM\tassay_organisms\tcell_or_prep"]
for comp, tid, tn, to in sorted({(r["compound"], r["target_chembl_id"], r["target_pref_name"], r["target_organism"]) for r in log["rows"]}):
    rs = [r for r in log["rows"] if (r["compound"], r["target_chembl_id"]) == (comp, tid)]
    nm = [float(r["standard_value"]) for r in rs if r["standard_units"] == "nM" and r["standard_relation"] == "=" and r["standard_value"] not in (None, "")]
    cx = [r["assay_context"] or {} for r in rs]
    L.append("\t".join(map(str, [comp, log["compounds"][comp]["chembl_matches"][0][0], tid, tn, to, len(rs), len({r["document_chembl_id"] for r in rs}), ",".join(sorted({r["standard_type"] for r in rs})),
      round(statistics.median(nm), 1) if nm else "", min(nm) if nm else "", max(nm) if nm else "", ";".join(sorted({c.get("assay_organism") or "NA" for c in cx})), ";".join(sorted({c.get("assay_cell_type") or "NA" for c in cx}))])))
Path("toolcompound_summary.tsv").write_text("\n".join(L) + "\n")
print(len(log["rows"]), "receptor rows;", {k: (v["chembl_matches"][0][0] if v["chembl_matches"] else None) for k, v in log["compounds"].items()})
