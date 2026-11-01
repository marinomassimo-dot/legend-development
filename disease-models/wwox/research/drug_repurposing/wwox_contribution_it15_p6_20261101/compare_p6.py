#!/usr/bin/env python3
"""IT15 P6: what the three paths produced on the two IT15 questions, counted from the package tables (no network, standard library).
Paths: (1) simple target-action retrieval (the target-first tables), (2) the same retrieval read through WWOX context (the selection criteria, the cases),
(3) the earlier network/signature generator output where it addressed the question (IT10 Q7 dispositions for GSK3B; the NMDAR queue for Q-A).
Counts only; it measures coverage and what each path let through, never predictive accuracy or benefit. Writes comparison_p6.tsv next to this file."""
import argparse, csv, collections, os
H = os.path.dirname(os.path.abspath(__file__)); DR = os.path.dirname(H)
def rd(p): return list(csv.DictReader(open(os.path.join(DR, p), encoding="utf-8"), delimiter="\t"))
def main():
    argparse.ArgumentParser(description=__doc__).parse_args()
    out = []
    def add(q, path, measure, value, note=""): out.append((q, path, measure, str(value), note))
    # Q-A
    ra = rd("target_first_it15_qa_nmdar_20261101/relations_qa.tsv"); ga = rd("target_first_it15_qa_nmdar_20261101/graded_comparisons_qa.tsv"); ca = rd("target_first_it15_qa_nmdar_20261101/cases_qa.tsv")
    q = rd("ranking_it8_p9_20261029/deepening_queue.tsv"); nm = [r for r in ra if r.get("molecule_pref_name")]
    add("Q-A", "1 simple target-action", "activity rows retrieved", len(ra))
    add("Q-A", "1 simple target-action", "parent compounds with a row", len({r["molecule_chembl_id"] for r in ra}))
    add("Q-A", "1 simple target-action", "named compounds", len({r["molecule_chembl_id"] for r in nm}))
    add("Q-A", "1 simple target-action", "censored rows kept apart", sum(1 for r in ra if r["relation"] in ("<", ">")))
    gc = collections.Counter(r["grade"] for r in ga)
    for k in ("INTERPRETABLE", "LIMITED", "NOT_DETERMINABLE", "PANEL_NOT_SELECTIVITY"): add("Q-A", "1 simple target-action", f"same-document groups graded {k}", gc.get(k, 0), "grade assigned by selectivity_p6.py; counts are derived")
    add("Q-A", "3 earlier queue", "NMDAR entries in the deepening queue (rule: documented direction-consistent action on a need with WWOX observations)", sum(1 for r in q if "EXCITATORY" in r["needs"]))
    rc = collections.Counter(r["reconciliation"] for r in q); rn = collections.Counter(r["reconciliation"] for r in q if "EXCITATORY" in r["needs"])
    for k in sorted(rc): add("Q-A", "3 earlier queue", f"reconciliation {k}: whole queue / NMDAR entries", f"{rc[k]} / {rn.get(k, 0)}", "derived at run time from cards, qualification records and uncarded items (READMEs not searched)")
    add("Q-A", "2 WWOX-informed", "cases deepened", len(ca), "known reference, hypothesis, different mechanism, discriminating control")
    # Q-B
    rb = rd("target_first_it15_qb_gsk3_20261101/relations_qb.tsv"); gb = rd("target_first_it15_qb_gsk3_20261101/graded_comparisons_qb.tsv"); cb = rd("target_first_it15_qb_gsk3_20261101/cases_qb.tsv")
    add("Q-B", "1 simple target-action", "activity rows retrieved (census table)", len(rb))
    gcb = collections.Counter(r["grade"] for r in gb)
    for k in ("INTERPRETABLE", "LIMITED", "NOT_DETERMINABLE", "PANEL_NOT_SELECTIVITY"): add("Q-B", "1 simple target-action", f"same-document groups graded {k}", gcb.get(k, 0))
    try:
        q7 = [r for r in rd("generation_it10_p1_20261031/results/dispositions_Q7.tsv") if r.get("disposition", r.get("verdict", "")) != ""]
        col = [c for c in (q7[0].keys() if q7 else []) if "dispos" in c.lower() or "verdict" in c.lower()]
        add("Q-B", "3 earlier generator", "Q7 rows (direct search on GSK3B)", len(q7), "dispositions: " + str(dict(collections.Counter(r[col[0]] for r in q7)) if col else "n/a"))
    except Exception as e:
        add("Q-B", "3 earlier generator", "Q7 rows", "unreadable", str(e)[:80])
    add("Q-B", "2 WWOX-informed", "cases deepened", len(cb), "reference, tool hypothesis, different mechanism, control")
    with open(os.path.join(H, "comparison_p6.tsv"), "w") as f:
        f.write("question\tpath\tmeasure\tvalue\tnote\n")
        for r in out: f.write("\t".join(r) + "\n")
    for r in out: print("\t".join(r))
if __name__ == "__main__": main()
