#!/usr/bin/env python3
"""IT scoring of the frozen class-level predictions under RULE_AMENDMENT_2 (+ Addendum 2a).
Reads only the sealed extraction (sha256 in it_extractor_20261116/sealed/SEAL.sha256). Deterministic; no randomness."""
import csv, itertools, math, sys
if "--help" in sys.argv or "-h" in sys.argv:
    print("usage: score_class_pairs.py [--exclude-acute-diazepam] [--a1-for-coded-four] [--reclassify-polytherapy=ROW,ROW]")
    print("Scores the frozen class-level predictions against the sealed extraction; prints to stdout; writes nothing.")
    sys.exit(0)
from pathlib import Path
HERE = Path(__file__).resolve().parent
EXT = HERE.parent / "it_extractor_20261116" / "sealed" / "extraction.tsv"
# extractor class -> matrix class; vigabatrin is in 'other' and split by agent name (declared before computing)
MAP = {"steroid_acth": "steroid/ACTH", "ketogenic_diet": "ketogenic diet", "benzodiazepine": "benzodiazepines",
       "gabaa_pam_non_benzodiazepine": "GABA-A PAM (non-benzodiazepine)", "sv2a": "SV2A",
       "carbonic_anhydrase_or_multitarget": "carbonic-anhydrase/multi-target", "valproate_type": "valproate-type",
       "sodium_channel": "sodium-channel", "cannabidiol_fenfluramine_type": "cannabidiol/fenfluramine-type"}
EXCLUDE_ACUTE = "--exclude-acute-diazepam" in sys.argv
USE_A1 = "--a1-for-coded-four" in sys.argv   # sensitivity only: public A1 table (NOT blind) replaces the extractor for four classes
rows = list(csv.DictReader(open(EXT), delimiter="\t"))
RECLASS = set()
for a in sys.argv:
    if a.startswith("--reclassify-polytherapy="):
        RECLASS = {int(x) for x in a.split("=", 1)[1].split(",") if x}   # extraction line numbers (header = line 1): sensitivity only
for i, r in enumerate(rows):
    if i + 2 in RECLASS:
        r["seizure_outcome_attributable"] = "polytherapy_unattributable"
def cls(r):
    if r["mechanism_class"] == "other":
        return "GABA-AT/GAT" if "vigabatrin" in r["agent_or_treatment_as_printed"].lower() else None
    return MAP.get(r["mechanism_class"])
child = {}
for r in rows:
    if r["seizure_outcome"] not in ("resolved", "partial", "none", "worsened") or r["seizure_outcome_attributable"] != "yes":
        continue
    c = cls(r)
    if c is None: continue
    if EXCLUDE_ACUTE and "diazep" in r["agent_or_treatment_as_printed"].lower() and "intravenous" in r["agent_or_treatment_as_printed"].lower(): continue
    key = (c, r["report_id"], r["child_label_as_printed"])
    rank = {"none": 0, "worsened": -1, "partial": 1, "resolved": 2}[r["seizure_outcome"]]
    child[key] = max(child.get(key, -9), rank)   # child-level: best attributable outcome within the class
if USE_A1:
    A1 = HERE.parent.parent.parent / "batch_sci_20261105" / "a1_wwox_reports" / "cases_a1.tsv"
    A1MAP = {"vigabatrin": "GABA-AT/GAT", "hormonal": "steroid/ACTH", "ketogenic_diet": "ketogenic diet", "cannabidiol": "cannabidiol/fenfluramine-type"}
    for k in [k for k in child if k[0] in A1MAP.values()]: del child[k]
    for r in csv.DictReader(open(A1), delimiter="\t"):
        c = A1MAP.get(r["intervention_class"]); o = r["symptomatic_outcome"]
        if c and o in ("resolved", "partial", "none"):
            key = (c, r["source_id"], r["case_label_as_printed"]); rk = {"none": 0, "partial": 1, "resolved": 2}[o]
            child[key] = max(child.get(key, -9), rk)
byc = {}
for (c, _, _), v in child.items(): byc.setdefault(c, []).append(v)
def wilson(k, n, z=1.96):
    if n == 0: return (0, 1)
    p = k / n; d = 1 + z*z/n; m = p + z*z/(2*n); h = z*math.sqrt(p*(1-p)/n + z*z/(4*n*n))
    return ((m-h)/d, (m+h)/d)
shares = {}
for c, vs in sorted(byc.items()):
    n = len(vs); a = sum(v >= 1 for v in vs); b = sum(v >= 2 for v in vs)
    shares[c] = (n, a, b)
print("children with an attributable stated seizure outcome (class: n, partial-counts k, resolved-only k, Wilson 95% partial-counts)")
for c, (n, a, b) in shares.items():
    lo, hi = wilson(a, n); print(f"  {c}: n={n} k_partial_counts={a} k_resolved={b} share={a/n:.2f} [{lo:.2f},{hi:.2f}] {'SCORABLE' if n>=3 else 'not scorable (<3)'}")
S = [c for c, (n, _, _) in shares.items() if n >= 3]
PRED = {
 "F1_per_thread_sum": {"GABA-A PAM (non-benzodiazepine)": 9, "benzodiazepines": 9, "GABA-AT/GAT": 6, "carbonic-anhydrase/multi-target": 6, "SV2A": 3, "steroid/ACTH": 0, "ketogenic diet": 0},
 "F1_origin_collapsed": {"GABA-A PAM (non-benzodiazepine)": 9, "benzodiazepines": 9, "GABA-AT/GAT": 6, "carbonic-anhydrase/multi-target": 3, "SV2A": 3, "steroid/ACTH": 0, "ketogenic diet": 0},
 "F2_GABA-AT>CBD>steroid=KD (CBD pairs only when CBD is scorable)": {"GABA-AT/GAT": 6, "cannabidiol/fenfluramine-type": 3, "steroid/ACTH": 0, "ketogenic diet": 0},
 "baseline_i_PTZ_profile": {"GABA-A PAM (non-benzodiazepine)": 2, "benzodiazepines": 2, "GABA-AT/GAT": 1, "carbonic-anhydrase/multi-target": 1, "SV2A": 0},
 "baseline_ii_frequency_of_use": {"GABA-AT/GAT": 22, "ketogenic diet": 12, "steroid/ACTH": 11, "benzodiazepines": 9, "GABA-A PAM (non-benzodiazepine)": 9, "carbonic-anhydrase/multi-target": 7, "SV2A": 7},
 "baseline_iii_uniform": {c: 1 for c in S},
 "baseline_arm_memory_free (score_match; unknown excluded)": {"GABA-A PAM (non-benzodiazepine)": 6},
}
def observed(a, b, ver):
    (na, ka, ra), (nb, kb, rb) = shares[a], shares[b]
    pa, pb = (ka/na, kb/nb) if ver == "partial_counts" else (ra/na, rb/nb)
    if abs(pa - pb) < 1/min(na, nb): return 0
    return 1 if pa > pb else -1
pairs = list(itertools.combinations(sorted(S), 2))
print(f"\nscorable classes ({len(S)}): {S}; class pairs: {len(pairs)}")
for ver in ("partial_counts", "resolved_only"):
    obs = {p: observed(p[0], p[1], ver) for p in pairs}
    cl = [p for p in pairs if obs[p] != 0]
    print(f"\n== observed ordering version '{ver}': classifiable (not tied) pairs {len(cl)} of {len(pairs)}")
    for name, pr in PRED.items():
        sc = 0; n = 0
        for p in cl:
            a, b = p
            if a not in pr or b not in pr: continue
            n += 1
            d = (pr[a] > pr[b]) - (pr[a] < pr[b])
            sc += 0.5 if d == 0 else (1.0 if d == obs[p] else 0.0)
        print(f"  {name}: classifiable pairs scored {n}, concordance {sc/n:.2f}" if n else f"  {name}: 0 classifiable pairs scored (not scorable)")
