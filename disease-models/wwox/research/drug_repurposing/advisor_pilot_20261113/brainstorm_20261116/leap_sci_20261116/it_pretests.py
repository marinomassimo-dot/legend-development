#!/usr/bin/env python3
"""PRESIDIO (SCI): held-data lookups for the five IT leap hypotheses (HIT-1 to HIT-5). Reads only held tables: the A1 cases table and the
sealed extractor output. No network. Standard library only.

    python3 it_pretests.py run <cases_a1.tsv> <sealed extraction.tsv> <out_dir>

Writes a1_both_endpoint_children.tsv, status_by_outcome.tsv, vigabatrin_rows.tsv. Descriptive only; not WWOX evidence about a patient.
"""
import sys

if len(sys.argv) != 5 or sys.argv[1] != "run":
    print(__doc__)
    raise SystemExit(0)

import collections, csv, math, os, re

cases, ext, out = sys.argv[2], sys.argv[3], sys.argv[4]
os.makedirs(out, exist_ok=True)


def wilson(k, n, z=1.96):
    if n == 0:
        return ("", "")
    p = k / n; d = 1 + z * z / n; ce = (p + z * z / (2 * n)) / d; hw = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (round(ce - hw, 2), round(ce + hw, 2))


A1 = list(csv.DictReader(open(cases, encoding="utf-8"), delimiter="\t"))
rows = [r for r in A1 if r["concordance"] in ("discordant", "concordant")]
kids = collections.OrderedDict()
for r in rows:
    key = (r["source_id"], r["case_label_as_printed"][:30])
    kids.setdefault(key, []).append(r)
with open(os.path.join(out, "a1_both_endpoint_children.tsv"), "w", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n")
    w.writerow(["source", "child", "rows", "seizure_outcomes_by_row", "developmental_outcome", "concordance", "first_imaging_stated"])
    for (s, c), rr in kids.items():
        w.writerow([s, c, len(rr), "; ".join(f"{x['intervention_class']}={x['symptomatic_outcome']}" for x in rr), "; ".join(sorted({x["developmental_outcome"] for x in rr})),
                    "; ".join(sorted({x["concordance"] for x in rr})), rr[0]["imaging_finding"][:110]])
E_ = list(csv.DictReader(open(ext, encoding="utf-8"), delimiter="\t"))
A = [r for r in E_ if r["seizure_outcome_attributable"] == "yes"]
with open(os.path.join(out, "status_by_outcome.tsv"), "w", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n")
    w.writerow(["status", "n", "resolved", "partial", "none", "improved(resolved+partial)", "improved_wilson95", "resolved_wilson95"])
    for st in ("tried", "added_on", "continued", "stopped"):
        rr = [r for r in A if r["status"] == st]
        c = collections.Counter(r["seizure_outcome"] for r in rr); imp = c["resolved"] + c["partial"]
        w.writerow([st, len(rr), c["resolved"], c["partial"], c["none"], imp, wilson(imp, len(rr)), wilson(c["resolved"], len(rr))])
vg = [r for r in A if re.search(r"vigabatrin|VGB", r["agent_or_treatment_as_printed"], re.I)]
with open(os.path.join(out, "vigabatrin_rows.tsv"), "w", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n")
    w.writerow(["report", "child", "status", "seizure_outcome"])
    for r in vg:
        w.writerow([r["report_id"], r["child_label_as_printed"][:30], r["status"], r["seizure_outcome"]])
    k = sum(r["seizure_outcome"] == "resolved" for r in vg); k2 = sum(r["seizure_outcome"] in ("resolved", "partial") for r in vg)
    w.writerow(["TOTAL", f"distinct children {len({(r['report_id'], r['child_label_as_printed'][:30]) for r in vg})}", f"resolved {k}/{len(vg)} {wilson(k, len(vg))}", f"improved {k2}/{len(vg)} {wilson(k2, len(vg))}"])
print("done")
