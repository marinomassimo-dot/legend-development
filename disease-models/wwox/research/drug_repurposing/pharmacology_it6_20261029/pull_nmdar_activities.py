#!/usr/bin/env python3
"""P8 live use and P9 data pull: for each named glutamate-receptor compound, resolve its ChEMBL id from
an exact name or synonym (trying listed alternates), read EVERY target it was measured on, and keep the
rows whose target is an NMDA/AMPA receptor entity (single protein, heteromeric complex or group, human or
rodent). Reading the compound first matters: channel blockers are curated against complexes, so a
single-subunit query returns an empty answer that is not absence (measured 2026-10-29).
Writes raw_activities.json and activity_summary.tsv. Run: python3 pull_nmdar_activities.py [--out DIR]"""
import argparse, json, re, statistics, sys, time
from pathlib import Path
ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT))
from framework.adapters import chembl  # noqa: E402

COMPOUNDS = {  # label -> names tried in order (exact name or synonym must equal the query)
    "memantine": ["memantine"], "ketamine": ["ketamine"], "esketamine": ["esketamine"], "dizocilpine (MK-801)": ["dizocilpine", "MK-801", "dizocilpine maleate"],
    "dextromethorphan": ["dextromethorphan"], "amantadine": ["amantadine"], "ifenprodil": ["ifenprodil"], "radiprodil": ["radiprodil", "RGH-896"],
    "traxoprodil": ["traxoprodil", "CP-101,606"], "eliprodil": ["eliprodil"], "Ro 25-6981": ["Ro 25-6981", "RO-25-6981", "Ro-25-6981"],
    "NVP-AAM077 (PEAQX)": ["NVP-AAM077", "PEAQX"], "TCN-201": ["TCN-201", "TCN 201"], "NAB-14": ["NAB-14"], "perampanel": ["perampanel"],
    "felbamate": ["felbamate"], "D-AP5 (APV)": ["D-AP5", "APV", "AP5", "D-APV", "AP-5", "2-amino-5-phosphonovaleric acid"]}
RECEPTOR = re.compile(r"NMDA|glutamate receptor|glutamate \[NMDA\]|AMPA|GRIA|GRIN", re.I)


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--out", default=str(Path(__file__).parent))
    out = Path(ap.parse_args().out)
    log = {"retrieved_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "compounds": {}, "rows": []}
    for label, names in COMPOUNDS.items():
        tried, mid = [], None
        for nm in names:
            r = chembl.query({"drug": nm})
            tried.append({"name": nm, "status": r["status"], "error": r["error"], "nearest": [n.get("pref_name") for n in r.get("nearest") or []]})
            mid = next((h.get("molecule_chembl_id") for h in r["hits"] if h.get("molecule_chembl_id")), None)
            if mid:
                mechs = [(h.get("action_type"), h.get("mechanism_of_action"), h.get("target_chembl_id")) for h in r["hits"] if h.get("kind") == "mechanism"]
                break
        entry = {"molecule_chembl_id": mid, "names_tried": tried, "mechanisms": mechs if mid else []}
        log["compounds"][label] = entry
        if not mid:
            continue
        a = chembl.query({"molecule": mid, "types": ["IC50", "Ki", "Kd", "EC50", "Kb", "Potency"], "max_rows": 2000})
        entry.update({"status": a["status"], "total_rows_all_targets": a.get("total_count"), "retrieved": a.get("retrieved"), "truncated": a.get("truncated"), "error": a["error"]})
        for h in a["hits"]:
            if RECEPTOR.search(h.get("target_pref_name") or ""):
                log["rows"].append(dict(h, compound=label))
    (out / "raw_activities.json").write_text(json.dumps(log, indent=1, sort_keys=True))
    lines = ["compound\tchembl_id\ttarget_chembl_id\ttarget\ttarget_organism\tn_rows\tn_docs\ttypes\tunits\tmedian_nM_equal\tmin_nM\tmax_nM\tassay_organisms\tassay_types\tcell_or_prep\tn_non_equal_relation"]
    cells = sorted({(r["compound"], r["target_chembl_id"], r["target_pref_name"], r["target_organism"]) for r in log["rows"]})
    for comp, tid, tname, torg in cells:
        rs = [r for r in log["rows"] if (r["compound"], r["target_chembl_id"]) == (comp, tid)]
        nm = [float(r["standard_value"]) for r in rs if r["standard_units"] == "nM" and r["standard_relation"] == "=" and r["standard_value"] not in (None, "")]
        ctx = [r["assay_context"] or {} for r in rs]
        lines.append("\t".join(map(str, [comp, log["compounds"][comp]["molecule_chembl_id"], tid, tname, torg, len(rs), len({r["document_chembl_id"] for r in rs}),
            ",".join(sorted({r["standard_type"] for r in rs})), ",".join(sorted({str(r["standard_units"]) for r in rs})),
            round(statistics.median(nm), 1) if nm else "", min(nm) if nm else "", max(nm) if nm else "",
            ";".join(sorted({c.get("assay_organism") or "NA" for c in ctx})), ",".join(sorted({c.get("assay_type") or "NA" for c in ctx})),
            ";".join(sorted({c.get("assay_cell_type") or "NA" for c in ctx})), sum(1 for r in rs if r["standard_relation"] != "=")])))
    (out / "activity_summary.tsv").write_text("\n".join(lines) + "\n")
    unresolved = [k for k, v in log["compounds"].items() if not v["molecule_chembl_id"]]
    print(f"{len(log['rows'])} receptor rows; {len(cells)} compound x target cells; unresolved names: {unresolved}")
main()
