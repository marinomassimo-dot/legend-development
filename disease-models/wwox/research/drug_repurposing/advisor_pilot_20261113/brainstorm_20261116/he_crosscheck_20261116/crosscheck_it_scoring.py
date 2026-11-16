"""HE read-only cross-check of IT's scoring (score_class_pairs.py) with the generator's concordance arithmetic.

    python3 crosscheck_it_scoring.py            (run from the repository root)

Three things are re-derived independently of IT's script and compared with what IT printed (it_scoring_20261116/result_main.txt):
  1. the per-class counts (children n, improved k) from the SEALED extraction, written here from the README's definitions;
  2. the frozen predictions, READ from the files at SCI's freeze commit and from baseline (ii) (not typed in);
  3. the concordance, with framework/scripts/aed_matrix.py `concordance` (ties 0.5, observed tie below one child on the smaller n).
Reads only committed files; writes nothing; the verdict is printed.
"""
import csv
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, "framework/scripts")
import aed_matrix as am  # noqa: E402

B = Path("disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/brainstorm_20261116")
SCI = Path("disease-models/wwox/research/drug_repurposing/aed_matrix_sci_20261116")
FREEZE = "f5b71a3f4"


def show(commit, path):
    return subprocess.run(["git", "show", f"{commit}:{path}"], capture_output=True, text=True, check=True).stdout


# 1. counts from the sealed extraction ------------------------------------------------------------------------
CLASS = {"steroid_acth": "steroid_acth", "ketogenic_diet": "ketogenic_diet", "benzodiazepine": "benzodiazepine",
         "gabaa_pam_non_benzodiazepine": "gabaa_pam_nonbzd", "sv2a": "sv2a", "valproate_type": "valproate_type",
         "carbonic_anhydrase_or_multitarget": "carbonic_anhydrase_multitarget", "sodium_channel": "sodium_channel",
         "cannabidiol_fenfluramine_type": "cbd_fenfluramine", "ampa_antagonist": "ampa_antagonist", "t_type_calcium": "t_type_calcium"}
RANK = {"none": 0, "worsened": -1, "partial": 1, "resolved": 2}
best = {}
for r in csv.DictReader(open(B / "it_extractor_20261116/sealed/extraction.tsv", newline=""), delimiter="\t"):
    if r["seizure_outcome_attributable"] != "yes" or r["seizure_outcome"] not in RANK:
        continue
    cls = CLASS.get(r["mechanism_class"])
    if r["mechanism_class"] == "other" and "vigabatrin" in r["agent_or_treatment_as_printed"].lower():
        cls = "gaba_at_gat"
    if cls is None:
        continue
    key = (cls, r["report_id"], r["child_label_as_printed"])
    best[key] = max(best.get(key, -9), RANK[r["seizure_outcome"]])
n, k_partial, k_resolved = {}, {}, {}
for (cls, _, _), v in best.items():
    n[cls] = n.get(cls, 0) + 1
    k_partial[cls] = k_partial.get(cls, 0) + (v >= 1)
    k_resolved[cls] = k_resolved.get(cls, 0) + (v >= 2)

# what IT printed -------------------------------------------------------------------------------------------------
IT_LABEL = {"GABA-A PAM (non-benzodiazepine)": "gabaa_pam_nonbzd", "GABA-AT/GAT": "gaba_at_gat", "SV2A": "sv2a", "benzodiazepines": "benzodiazepine",
            "cannabidiol/fenfluramine-type": "cbd_fenfluramine", "carbonic-anhydrase/multi-target": "carbonic_anhydrase_multitarget",
            "ketogenic diet": "ketogenic_diet", "sodium-channel": "sodium_channel", "steroid/ACTH": "steroid_acth", "valproate-type": "valproate_type"}
it_text = open(B / "it_scoring_20261116/result_main.txt").read()
it_counts = {}
for m in re.finditer(r"^  (.+?): n=(\d+) k_partial_counts=(\d+) k_resolved=(\d+)", it_text, re.M):
    it_counts[IT_LABEL[m.group(1)]] = (int(m.group(2)), int(m.group(3)), int(m.group(4)))
mine_counts = {c: (n[c], k_partial[c], k_resolved[c]) for c in n if c in it_counts or n[c] >= 3}
same_counts = all(mine_counts.get(c) == v for c, v in it_counts.items())

# 2. frozen predictions read from the freeze commit ----------------------------------------------------------------
LABEL = {"sodium-channel": "sodium_channel", "T-type calcium": "t_type_calcium", "SV2A": "sv2a", "AMPA antagonists": "ampa_antagonist",
         "NMDAR pore blockers": "nmdar_pore_blocker", "GluN2B NAMs": "glun2b_nam", "GABA-A PAM (non-benzodiazepine)": "gabaa_pam_nonbzd",
         "benzodiazepines": "benzodiazepine", "GABA-AT/GAT": "gaba_at_gat", "Kv7 openers": "kv7_opener",
         "carbonic-anhydrase/multi-target": "carbonic_anhydrase_multitarget", "valproate-type": "valproate_type", "steroid/ACTH": "steroid_acth",
         "ketogenic diet": "ketogenic_diet", "cannabidiol/fenfluramine-type": "cbd_fenfluramine"}


def frozen_ranking(kind):
    out = {}
    for r in csv.DictReader(show(FREEZE, str(SCI / "output/rankings.tsv")).splitlines(), delimiter="\t"):
        if (r["endpoint"], r["window"], r["ranking"]) == ("seizure", "P13-P15", kind):
            score = int(re.search(r"\(score (\d+)\)\s*$", r["classes"]).group(1))
            for name in re.sub(r"\s*\(score \d+\)\s*$", "", r["classes"]).split("; "):
                out[LABEL[name.strip()]] = score
    return out


PRED = {"F1_per_thread_sum": frozen_ranking("per_thread_sum"), "F1_origin_collapsed": frozen_ranking("origin_collapsed")}
PRED["F2"] = {"gaba_at_gat": 6, "cbd_fenfluramine": 3, "steroid_acth": 0, "ketogenic_diet": 0}   # SCI's F2 sentence: GABA-AT above CBD above steroid and diet tied
ptz = {LABEL[r["class"]]: int(r["ptz_profile_level"]) for r in csv.DictReader(show(FREEZE, str(SCI / "baselines.tsv")).splitlines(), delimiter="\t")
       if r["ptz_profile_level"].isdigit()}
PRED["baseline_i_PTZ"] = ptz
freq = {r["class_id"]: int(r["children_with_a_row"]) for r in csv.DictReader(open(B / "baseline_ii_he_20261116/baseline_ii.tsv"), delimiter="\t")}
PRED["baseline_ii_frequency"] = freq
PRED["baseline_iii_uniform"] = {c: 1 for c in LABEL.values()}

# 3. concordance ------------------------------------------------------------------------------------------------------
print(f"counts re-derived from the sealed extraction equal IT's printed counts for all {len(it_counts)} classes IT printed: {same_counts}")
if not same_counts:
    for c, v in sorted(it_counts.items()):
        print(f"  {c}: IT {v}  here {mine_counts.get(c)}")
it_conc = {}
section = None
for line in it_text.splitlines():
    m = re.match(r"== observed ordering version '(\w+)'", line)
    if m:
        section = m.group(1)
    m = re.match(r"  (\S+).*: classifiable pairs scored (\d+), concordance ([\d.]+)", line)
    if m and section:
        it_conc[(section, m.group(1))] = (int(m.group(2)), float(m.group(3)))
IT_NAME = {"F1_per_thread_sum": "F1_per_thread_sum", "F1_origin_collapsed": "F1_origin_collapsed", "F2": "F2_",
           "baseline_i_PTZ": "baseline_i_PTZ_profile", "baseline_ii_frequency": "baseline_ii_frequency_of_use", "baseline_iii_uniform": "baseline_iii_uniform"}
agree = True
for version, col in (("partial_counts", 1), ("resolved_only", 2)):
    counts = {c: (v[0], v[col]) for c, v in mine_counts.items()}
    print(f"\nobserved ordering '{version}'")
    for name, pred in PRED.items():
        r = am.concordance(pred, counts)
        mine = f"{r['concordance']:.2f}" if r["concordance"] is not None else "not scorable"
        key = next((kk for kk in it_conc if kk[0] == version and kk[1].startswith(IT_NAME[name])), None)
        it = it_conc.get(key)
        theirs = f"{it[1]:.2f} on {it[0]} pairs" if it else "n/a"
        ok = (it is None and r["concordance"] is None) or (it is not None and r["concordance"] is not None and it[0] == r["scored"] and abs(it[1] - round(r["concordance"], 2)) < 0.005)
        agree &= ok
        print(f"  {name}: here {mine} on {r['scored']} pairs ({r['classifiable']} classifiable of {r['pairs']}); IT {theirs}; {'AGREE' if ok else 'CHECK'}")
print("\nVERDICT:", "the two computations agree" if agree and same_counts else "the two computations differ somewhere; see the lines marked CHECK")

# 4. like for like: IT compares F1 (15 pairs) with baseline (i) (7 pairs, only the classes with a PTZ level). On the SAME classes: ----------------
print("\nlike for like: every prediction scored on the classes baseline (i) has a level for (resolved_only; partial_counts has no classifiable pair there)")
shared = set(PRED["baseline_i_PTZ"])
for version, col in (("resolved_only", 2), ("partial_counts", 1)):
    counts = {c: (v[0], v[col]) for c, v in mine_counts.items() if c in shared and v[0] >= 3}
    for name in ("F1_per_thread_sum", "F1_origin_collapsed", "baseline_i_PTZ", "baseline_ii_frequency"):
        r = am.concordance(PRED[name], counts)
        print(f"  {version} {name}: {r['scored']} pairs, " + (f"{r['concordance']:.3f}" if r["concordance"] is not None else "not scorable"))
