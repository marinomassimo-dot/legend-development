#!/usr/bin/env python3
"""IT40 P6: mechanism-first catalogue search. Starts from action-context-hypothesised-benefit relations (rows of RELATIONS), resolves the target group, and lists what the catalogue holds for those targets BEFORE any compound name is chosen; then resolves the tools the packages name and reports identity cautions. Read-only; no score; no ranking.
  python3 mechanism_search.py            -> writes by_action.tsv, named_tools.tsv"""
import csv, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / "framework/scripts"))
import compound_catalog as cc, repurposing_search as rs  # noqa: E402

# relation id, action, target symbols, context, hypothesised benefit (all IPOTESI), source package row
RELATIONS = [
 ("R1", "negative modulation of GluN2B-containing NMDAR", ["GRIN2B"], "burst slice, Wwox-deficient layer II/III cortex, P13-P17", "burst fall at a smaller measured fraction of total NMDAR current than d-APV needs", "ampa_nmda BH2"),
 ("R2", "negative modulation of GluN2A-containing NMDAR", ["GRIN2A"], "same", "same arm as R1 for the GluN2A share (needs a measured co-agonist level)", "ampa_nmda BH2"),
 ("R3", "AMPA/kainate receptor antagonism", ["GRIA1", "GRIA2", "GRIA3", "GRIA4", "GRIK1", "GRIK2", "GRIK3", "GRIK4", "GRIK5"], "same", "burst survives or not under a verified AMPA/kainate block", "ampa_nmda BH1"),
 ("R4", "Ih (HCN) channel blockade as a tool arm", ["HCN1", "HCN2", "HCN3", "HCN4"], "same; matched potential and deflection", "tool response only; shows contribution, not a defect", "membrane MH2"),
 ("R5", "Kv7 (KCNQ) opening, resting K+ conductance", ["KCNQ2", "KCNQ3", "KCNQ4", "KCNQ5"], "same", "none nominated; a response would not show a leak deficit", "membrane MH1"),
 ("R6", "connexin/pannexin channel block", ["GJD2", "PANX1"], "same", "carbenoxolone burst fall is not attributable to gap junctions on present data", "ampa_nmda BH3"),
]
# tools the packages name; identity cautions come from the catalogue lookup, not from memory
TOOLS = [("D-Ap5", "tool", "BH1/BH2 positive control (the package writes d-APV)"), ("perampanel", "therapeutic_class_to_study", "R3"), ("NBQX", "tool", "R3 use-only"), ("GYKI 52466", "tool", "R3 use-only"),
 ("ifenprodil", "tool", "R1"), ("Ro 25-6981", "tool", "R1"), ("radiprodil", "tool_or_candidate", "R1"), ("TCN-201", "tool", "R2"), ("memantine", "therapeutic_class_to_study", "NMDAR pore block"),
 ("ZD7288", "tool", "R4"), ("ivabradine", "therapeutic_class_to_study", "R4"), ("retigabine", "tool_or_withdrawn_drug", "R5"), ("XE991", "tool", "R5 difference current"),
 ("carbenoxolone", "tool_not_gap_junction_specific", "R6"), ("brilliant blue FCF", "tool", "R6 Panx1 arm")]

def main():
    es = cc.load(cc.DEFAULT_CATALOG); idx = rs.Index(es)
    out = []
    for rid, act, syms, ctx, ben, src in RELATIONS:
        seen = {}
        for s in syms:
            for e, t in idx.chembl_human.get(s.upper(), []):
                k = (e["id"], s)
                phase = max([r.get("max_phase") or 0 for r in e.get("status_records", [])] or [0])
                ca = t.get("action_type") or t.get("action") or ""
                ng = len(t.get("gene_symbols") or [])
                gran = "single_protein_record" if ng == 1 else ("two_gene_assembly_record" if ng == 2 else "family_record_subunit_unresolved")
                parent = (e.get("relations") or {}).get("parent") or e["id"]
                seen[k] = [rid, act, s, e["id"], e["name"], ca, rs.action_direction(ca), (t.get("target_chembl_id") or t.get("target_id") or ""), ng, gran, parent, phase, "; ".join(sorted(set(a.get("category","") for a in e.get("access",[])))) , ctx, ben, src]
        out += sorted(seen.values(), key=lambda r: (r[2], -float(r[11] or 0), r[4]))
        if not seen: out.append([rid, act, ",".join(syms), "", "NO_CATALOGUE_MECHANISM_ROW", "", "", "", "", "", "", "", "", ctx, ben, src])
    hdr = ["relation", "action", "target_symbol", "catalogue_id", "name", "catalogue_action", "direction", "catalogue_target_id", "target_n_genes", "target_record_granularity", "parent_molecule", "max_phase", "access_us", "context", "hypothesised_benefit", "source_row"]
    with open(HERE / "by_action.tsv", "w", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n"); w.writerow(hdr); w.writerows(out)
    rows = []
    for q, role, use in TOOLS:
        hits = cc.find(es, name=q)
        rows.append([q, role, use, ";".join(f"{h['id']}={h['name']}" for h in hits[:4]) or "NOT_IN_CATALOGUE", len(hits)])
    with open(HERE / "named_tools.tsv", "w", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n"); w.writerow(["package_name", "role", "used_for", "catalogue_hits_by_name", "n_hits"]); w.writerows(rows)
    print(len(out), "by-action rows;", len(rows), "named tools")
main()
