#!/usr/bin/env python3
"""IT22 P5: incremental measures of the three corrections on the SAME proposal tables, with the counting unit stated for every figure.

  measure_it22.py [--out measures_it22.json]       (reads the committed stage tables; recomputes nothing else; offline)

Stages (each a `propose` run of the same code at a different state; the engine output is shared except Q8):
  S0  IT21 as published (diagnosis_it21_v1_20261103/results_v1)                   H8 unscoped, pooled-median attribution, IT9 P1 inputs
  S1  + P1 scoped decisions (results_p1)                                           attribution still the IT21 one
  S2  + P2 typed pharmacology (results_p2b)                                        the three-effect stage 2 (results_p2 is the same code before the affinity-type fallback, kept for the record)
  S3  + P3 inputs (results_p3)                                                     Q8 seed set, seed guards consumed, hand-over order
Units: ROW = one seed-specific (compound-record, question, arm) line; FAMILY = chemical family id; COMPOUND = base name (salt/case folded); CLUSTER = (question, hypothesis, main target);
HAND-OVER = a row chosen for qualification (one per cluster, three per question and hypothesis). Rows are not hypotheses and families are not compounds.
"""
import sys
if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
    print(__doc__)
    raise SystemExit(0)
import collections, csv, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DR = HERE.parent
STAGES = [("S0_IT21", DR / "diagnosis_it21_v1_20261103" / "results_v1"), ("S1_P1", HERE / "results_p1"), ("S2_P1_P2", HERE / "results_p2b"), ("S3_P1_P2_P3", HERE / "results_p3")]


def rd(p):
    return list(csv.DictReader(open(p, encoding="utf-8", newline=""), delimiter="\t"))


def stage(d):
    P = rd(d / "proposals_it21.tsv")
    H = rd(d / "handoff_it21.tsv")
    cl = lambda r: (r["question"], r["hypothesis"], r["main_target"])
    el = [r for r in P if r["handoff_eligible"] == "yes"]
    return dict(rows=len(P), families=len({r["family_id"] for r in P}), compounds=len({r["base_name"].lower() for r in P}), clusters=len({cl(r) for r in P}),
                eligible_rows=len(el), eligible_clusters=len({cl(r) for r in el}), handover_rows=len(H), handover_compounds=len({r["compound"].lower() for r in H}),
                handover_ids=sorted(r["proposal_id"] for r in H), blockers=dict(collections.Counter(r["handoff_blocker"] or "ELIGIBLE" for r in P)),
                by_question_rows=dict(collections.Counter(r["question"] for r in P)), by_question_handover=dict(collections.Counter(r["question"] for r in H)),
                seed_support_limited_rows=sum(1 for r in P if r.get("seed_support_limited") == "yes"), work_done_rows=sum(1 for r in P if r.get("cluster_work_done") == "yes"),
                rows_with_carried_limits=sum(1 for r in P if r.get("carried_limits")), attribution_states=dict(collections.Counter(r.get("attribution_state", "") for r in P))), P, H


def main():
    out, tabs = {}, {}
    for name, d in STAGES:
        out[name], P, H = stage(d)
        tabs[name] = (P, H)
    delta = {}
    keys = lambda P: {r["proposal_id"]: r for r in P}
    for (a, _), (b, __) in zip(STAGES, STAGES[1:]):
        Pa, Ha = tabs[a]; Pb, Hb = tabs[b]
        A, B = keys(Pa), keys(Pb)
        d = dict(rows_new=len(set(B) - set(A)), rows_retired_from_the_table=len(set(A) - set(B)),
                 released=sorted(i for i in B if i in A and A[i]["handoff_eligible"] == "no" and B[i]["handoff_eligible"] == "yes"),
                 withdrawn=sorted(i for i in B if i in A and A[i]["handoff_eligible"] == "yes" and B[i]["handoff_eligible"] == "no"),
                 state_changed=sorted(i for i in B if i in A and A[i].get("attribution_state") != B[i].get("attribution_state")),
                 handover_added=sorted({r["proposal_id"] for r in Hb} - {r["proposal_id"] for r in Ha}), handover_removed=sorted({r["proposal_id"] for r in Ha} - {r["proposal_id"] for r in Hb}))
        d["released_n"], d["withdrawn_n"], d["state_changed_n"] = len(d["released"]), len(d["withdrawn"]), len(d["state_changed"])
        for k in ("released", "withdrawn", "state_changed"):
            d[k] = d[k][:0]            # the ids are in the stage tables; the counts are the figure
        delta[f"{a}->{b}"] = d
    out["deltas"] = delta
    P2 = tabs["S2_P1_P2"][0]
    sens = {}
    for T in (300.0, 1000.0, 3000.0):          # technical choice: where a comparable pair with a measured main target stops being a 'secondary activity' and becomes WEAK
        sens[f"WEAK_if_main_target_above_{T:g}nM"] = sum(1 for r in P2 if r.get("attribution_state") in ("SECONDARY_ACTIVITY_MEASURED", "WEAK_ATTRIBUTION") and r.get("attribution_main_nm") and float(r["attribution_main_nm"]) > T)
    out["sensitivity_attribution_threshold_rows_at_stage_S2"] = sens
    P3 = tabs["S3_P1_P2_P3"][0]
    out["q2_q3_dependence_on_the_failed_second_system"] = dict(
        q2_rows=sum(1 for r in P3 if r["question"] == "Q2"), q2_rows_limited=sum(1 for r in P3 if r["question"] == "Q2" and r.get("seed_support_limited") == "yes"),
        q3_rows=sum(1 for r in P3 if r["question"] == "Q3"), q3_rows_limited=sum(1 for r in P3 if r["question"] == "Q3" and r.get("seed_support_limited") == "yes"),
        q4_rows_npy_contested=sum(1 for r in P3 if r["question"] == "Q4" and "NPY_SIGN_CONTESTED" in (r.get("seed_guards") or "")),
        hnpc_excluded_arm="seed sets: Q2 has no gene seed left (all 8 placed rows are hNPC-supported), Q3 keeps 1 of 6; engine re-run of Q3 gives 0 seed-specific rows (eng_arm)")
    (HERE / "measures_it22.json").write_text(json.dumps(out, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({k: {x: v for x, v in out[k].items() if x in ("rows", "families", "compounds", "clusters", "eligible_rows", "eligible_clusters", "handover_rows", "handover_compounds")} for k, _ in STAGES}, indent=1))
    print(json.dumps(out["deltas"], indent=1))
    print(json.dumps(out["sensitivity_attribution_threshold_rows_at_stage_S2"]), json.dumps(out["q2_q3_dependence_on_the_failed_second_system"]))


if __name__ == "__main__":
    main()
