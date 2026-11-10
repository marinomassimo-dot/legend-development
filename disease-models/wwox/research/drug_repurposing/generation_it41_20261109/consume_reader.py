"""IT41 P3/P5: the generation path calls Harness's reader and identity table (not only availability).
  1. hypothesis_package.comparison_for(load_all(), 'INV-05') -> comparison_rows_it41.tsv (one line per comparison row of every package registered for INV-05: key, package, kind, the action cell and the qualification cell, verbatim, cut nowhere).
  2. identity_it41_20261109/identity_table.tsv joined to the names of compound_view.tsv -> compound_identity_join.tsv (per item and name: identity state, label conflict, evidence level per expected gene, selectivity state).
No score, no ranking; a name with no row in the identity table is written as NO_IDENTITY_ROW, never as absent."""
import csv, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent; DR = HERE.parent
sys.path.insert(0, str(HERE.parents[4] / "framework/scripts"))
import hypothesis_package as hp  # noqa: E402

def main():
    rec = hp.comparison_for(hp.load_all(), "INV-05")
    with open(HERE / "comparison_rows_it41.tsv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n"); w.writerow(["inv_id", "state", "key", "package", "action_cell", "compound_or_probe_cell", "outcome_unresolved_cell"])
        for r in rec["rows"]:
            row = r["row"]; ks = list(row.keys())
            pick = lambda *cands: next((row[k] for k in ks for c in cands if k == c or k.startswith(c)), "")
            w.writerow([rec["inv_id"], rec["state"], r["key"], r["package"], pick("pharmacological_action_required", "action_context_hypothesised_benefit"), pick("compound_or_probe_qualified_or_identity_unresolved", "compound_or_probe"), pick("outcome_unresolved")])
    ident = {}
    for r in csv.DictReader(open(DR / "identity_it41_20261109/identity_table.tsv", encoding="utf-8"), delimiter="\t"): ident.setdefault(r["query_name"].lower(), []).append(r)
    out = []
    for c in csv.DictReader(open(HERE / "compound_view.tsv", encoding="utf-8"), delimiter="\t"):
        for nm in [re.sub(r"\s*\(.*?\)", "", x).strip() for x in c["name_full"].split(";") if x.strip()]:
            hits = ident.get(nm.lower()) or next((v for k, v in ident.items() if k and (k in nm.lower() or nm.lower() in k)), None)
            if not hits: out.append([c["item_id"], nm, "NO_IDENTITY_ROW", "", "", "", ""]); continue
            for h in hits: out.append([c["item_id"], nm, h["identity_state"], h["label_conflict"], h["expected_gene"], h["evidence_level"], h["selectivity"]])
    with open(HERE / "compound_identity_join.tsv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n"); w.writerow(["item_id", "name", "identity_state", "label_conflict", "expected_gene", "evidence_level", "selectivity"]); w.writerows(out)
    print(len(rec["rows"]), "comparison rows;", len(out), "identity join rows")

if __name__ == "__main__":
    main()
