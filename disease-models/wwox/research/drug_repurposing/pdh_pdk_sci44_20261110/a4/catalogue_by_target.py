"""SCI44 A4: every catalogue record that carries a target row for the given gene symbols, with its source and action. Read-only; writes catalogue_by_target.tsv beside itself.
  python3 catalogue_by_target.py LDHA LDHB PDP1 PDP2 PDK1 PDK2 PDK3 PDK4 PDHA1"""
import csv, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[5] / "framework/scripts"))
import compound_catalog as cc
def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__); return 0
    syms = {s.upper() for s in argv}
    es = cc.load(cc.DEFAULT_CATALOG); rows = []
    for e in es:
        for t in e.get("targets") or []:
            hit = ({g.upper() for g in (t.get("gene_symbols") or [])} | ({t["gene"].upper()} if t.get("gene") else set())) & syms
            if hit:
                rows.append([e["id"], e.get("name", ""), e.get("origin", ""), ";".join(sorted(hit)), (t.get("source", "") + (" / " + t["claim_source"] if t.get("claim_source") else "")), t.get("action_type") or t.get("interaction_type") or "", t.get("mechanism_of_action") or t.get("target_name") or "", ";".join(str(x) for x in (t.get("reference_ids") or [])[:3])])
    with open(HERE / "catalogue_by_target.tsv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter="\t"); w.writerow(["catalogue_id", "name", "origin", "symbols", "source", "action", "mechanism_or_target_name", "reference_ids"]); w.writerows(rows)
    print(len(rows), "rows"); return 0
if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
