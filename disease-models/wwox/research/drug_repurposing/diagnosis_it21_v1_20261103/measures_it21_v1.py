#!/usr/bin/env python3
"""IT21 V1 measures: committed IT21 P2 tables (forward path) against the v1 tables (identity bridge + attribution screen + P4a decisions), plus the catalogue-level
size of the claim-name bridge. Reads existing tables only; writes measures_it21_v1.json next to this file. Needs LEGEND_CATALOG_CACHE for the bridge counts.
"""
import sys
if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
    print(__doc__)
    raise SystemExit(0)
import collections, csv, importlib.util, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DR = HERE.parent
REPO = HERE.parents[4]
sys.path.insert(0, str(REPO / "framework/scripts"))


def rd(p):
    with open(p, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    sys.modules[name] = m
    spec.loader.exec_module(m)
    return m


def main():
    import compound_catalog as cc
    import repurposing_search as rs
    AS = load("attribution_screen_it21", DR / "generation_it21_p2_20261103" / "attribution_screen_it21.py")
    old = {r["proposal_id"]: r for r in rd(DR / "generation_it21_p2_20261103/results/proposals_it21.tsv")}
    new = {r["proposal_id"]: r for r in rd(HERE / "results_v1/proposals_it21.tsv")}
    ho = [r["proposal_id"] for r in rd(DR / "generation_it21_p2_20261103/results/handoff_it21.tsv")]
    hn = [r["proposal_id"] for r in rd(HERE / "results_v1/handoff_it21.tsv")]
    out = {}
    out["rows"] = len(new)
    out["eligible_before_after"] = [sum(1 for r in old.values() if r["handoff_eligible"] == "yes"), sum(1 for r in new.values() if r["handoff_eligible"] == "yes")]
    out["handed_before_after"] = [len(ho), len(hn)]
    out["handed_dropped"] = {i: (old[i]["compound"], new[i]["handoff_blocker"] or "not selected (cap)") for i in ho if i not in hn}
    out["handed_added"] = {i: (new[i]["compound"], new[i]["question"] + " " + new[i]["hypothesis"] + " " + new[i]["main_target"], new[i]["attribution_state"]) for i in hn if i not in ho}
    out["blockers_before"] = dict(collections.Counter(r["handoff_blocker"] or "ELIGIBLE" for r in old.values()))
    out["blockers_after"] = dict(collections.Counter(r["handoff_blocker"] or "ELIGIBLE" for r in new.values()))
    out["identity_bridged_rows"] = sum(1 for r in new.values() if r["identity_via"])
    out["identity_not_resolved_before_after"] = [out["blockers_before"].get("identity_not_resolved", 0), out["blockers_after"].get("identity_not_resolved", 0)]
    out["attribution_states"] = dict(collections.Counter(r["attribution_state"] for r in new.values()))
    folds = [float(r["attribution_fold"]) for r in new.values() if r["attribution_fold"] != ""]
    out["attribution_sensitivity_assessed_rows_at_or_above_fold"] = dict(AS.sensitivity(folds), assessed=len(folds))
    elig_old = [r for r in old.values() if r["handoff_blocker"] == "" or r["handoff_eligible"] == "yes"]
    out["previously_eligible_now_weak"] = sorted((r["compound"], r["main_target"], new[r["proposal_id"]]["attribution_fold"]) for r in elig_old if new[r["proposal_id"]]["attribution_state"] == "WEAK_ATTRIBUTION")
    out["generated_rows_changed"] = sum(1 for i, n in new.items() for c in ("status", "qualified", "z_total", "z_reach", "main_target") if n[c] != old[i][c])
    out["any_qualified"] = sum(1 for r in new.values() if r["qualified"] != "no")
    # the declared universe: Q2 H_HARM rows (the arm vorinostat was generated in)
    uni = [r for r in new.values() if r["question"] == "Q2" and r["hypothesis"] == "H_HARM"]
    out["universe_Q2_H_HARM"] = dict(rows=len(uni), eligible_before=sum(1 for r in uni if old[r["proposal_id"]]["handoff_eligible"] == "yes"),
                                    eligible_after=sum(1 for r in uni if r["handoff_eligible"] == "yes"), by_blocker_after=dict(collections.Counter(r["handoff_blocker"] or "ELIGIBLE" for r in uni)),
                                    hdac5_cluster_members=sorted((r["compound"], r["attribution_state"], r["attribution_fold"]) for r in uni if r["main_target"] == "HDAC5"))
    v = new["IT21P2-0031"]
    out["vorinostat"] = {k: v[k] for k in ("proposal_id", "status", "qualified", "z_total", "z_reach", "main_target", "identity_via", "attribution_state", "attribution_fold",
                                           "attribution_main_nm", "attribution_best_target", "attribution_best_nm", "sibling_family", "sibling_z_reach", "sibling_compatible_action",
                                           "handoff_eligible", "handoff_blocker")}
    out["vorinostat_before"] = {k: old["IT21P2-0031"][k] for k in ("handoff_eligible", "handoff_blocker")}
    out["contrast"] = {}
    for pid, nm in (("IT21P2-0195", "C1 GSK343"), ("IT21P2-0374", "C2 tizaterkib"), ("IT21P2-0006", "C3a nanatinostat")):
        n = new[pid]
        out["contrast"][nm] = dict(status=n["status"], qualified=n["qualified"], attribution=n["attribution_state"], fold=n["attribution_fold"], handoff_before=old[pid]["handoff_eligible"] + "/" + (pid in ho and "handed" or "not handed"),
                                   handoff_after=n["handoff_eligible"] + "/" + (pid in hn and "handed" or "not handed"), blocker_after=n["handoff_blocker"])
    out["glue_rows_with_main_target_CRBN"] = sorted({r["compound"] for r in new.values() if r["main_target"].upper() == "CRBN"})
    # catalogue-level size of the claim-name bridge (stored catalogue unchanged)
    entries = cc.load(DR / "catalog/catalog.jsonl.gz")
    fam = rs.families(entries)
    br = AS.bridge_claim_name_ligands(entries)
    dec = collections.Counter(r["decision"] for v_ in br.values() for r in v_)
    out["claim_name_bridge"] = dict(dgidb_only_entries_with_a_claim_name_ligand_and_no_concept_id_ligand=len(br), decisions=dict(dec), twin_families_joinable=len(AS.family_bridge(br, fam)))
    (HERE / "measures_it21_v1.json").write_text(json.dumps(out, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=1, sort_keys=True))


if __name__ == "__main__":
    main()
