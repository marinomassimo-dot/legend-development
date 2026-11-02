#!/usr/bin/env python3
"""IT19 P5 step 5: join the reference to the module's answers and report what changed.

  join_it19_p5.py --selection F --reference F --prefix F --guarded F --out F

Reports, for the 32 selected pairs: how many now carry a usable reference and of which kind; the
agreement of each module answer with the reference before and after the group-transfer fix, with
Wilson intervals; and, per pair, whether the fix removed an unsupported attribution, kept a
supported one, or abstained where the reference does hold a direction. Offline.
"""
import argparse
import collections
import csv
import json
import math
import sys
from pathlib import Path

DETERMINATE = ("compatible", "opposite")


def read_tsv(path):
    with open(path, encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def wilson(k, n, z=1.96):
    if n == 0:
        return [None, None]
    p = k / n
    d = 1 + z * z / n
    c = p + z * z / (2 * n)
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return [round((c - h) / d, 4), round((c + h) / d, 4)]


def module_direction(consistency):
    """The direction the module's answer asserts, or None when it asserts none."""
    if consistency == "consistent":
        return "compatible"
    if consistency == "opposed":
        return "opposite"
    if consistency.startswith("mixed:"):
        parts = set(consistency.split(":", 1)[1].split("|"))
        if parts == {"consistent", "direction_unresolved"}:
            return "compatible"
        if parts == {"direction_unresolved", "opposed"}:
            return "opposite"
    return None


def classify(ref_label, asserted):
    if asserted is None:
        return "abstained_reference_determinate" if ref_label in DETERMINATE else "abstained_reference_not_determinate"
    if ref_label not in DETERMINATE:
        return "asserted_reference_not_determinate"
    return "asserted_and_agrees" if asserted == ref_label else "asserted_and_disagrees"


def join(reference, prefix, guarded):
    ref = {r["pair_id"]: r for r in reference}
    pre = {r["pair_id"]: r for r in prefix}
    post = {r["pair_id"]: r for r in guarded}
    rows = []
    for pid in sorted(ref):
        r, a, b = ref[pid], pre[pid], post[pid]
        pa, pb = module_direction(a["active_consistency"]), module_direction(b["active_consistency"])
        rows.append({"pair_id": pid, "need": r["need_id"], "compound": r["compound"], "reference_label": r["reference_label"],
                     "reference_status": r["status"], "dependency": r["dependency_on_module_sources"].split(" ")[0],
                     "error_attribution": r["error_attribution"].split(":")[0],
                     "before": a["active_consistency"], "after": b["active_consistency"],
                     "before_class": classify(r["reference_label"], pa), "after_class": classify(r["reference_label"], pb),
                     "it18_L_v1": a["it18_L_v1"], "it18_L_v2": a["it18_L_v2"]})

    def score(key, labels):
        asserted = [x for x in rows if x[key].startswith("asserted") and x["reference_label"] in DETERMINATE]
        ok = [x for x in asserted if x[key] == "asserted_and_agrees"]
        return {"asserted_on_determinate": len(asserted), "agrees": len(ok),
                "accuracy": round(len(ok) / len(asserted), 4) if asserted else None,
                "ci95": wilson(len(ok), len(asserted)), "classes": dict(collections.Counter(x[key] for x in rows)),
                "pairs_asserted": sorted(x["pair_id"] for x in asserted)}

    l_v1 = [{"pair_id": x["pair_id"], "reference_label": x["reference_label"],
             "asserted": {"compatible": "compatible", "opposite": "opposite"}.get(x["it18_L_v1"])} for x in rows]
    l_v2 = [{"pair_id": x["pair_id"], "reference_label": x["reference_label"],
             "asserted": {"compatible": "compatible", "opposite": "opposite"}.get(x["it18_L_v2"])} for x in rows]

    def score_l(items):
        asserted = [x for x in items if x["asserted"] and x["reference_label"] in DETERMINATE]
        ok = [x for x in asserted if x["asserted"] == x["reference_label"]]
        return {"asserted_on_determinate": len(asserted), "agrees": len(ok),
                "accuracy": round(len(ok) / len(asserted), 4) if asserted else None, "ci95": wilson(len(ok), len(asserted))}

    changed = [x for x in rows if x["before"] != x["after"]]
    return rows, {
        "pairs": len(rows),
        "reference_labels": dict(collections.Counter(x["reference_label"] for x in rows)),
        "usable_reference_rows": sum(1 for x in rows if x["reference_label"] in DETERMINATE),
        "usable_functional": sum(1 for x in rows if x["reference_status"] == "determinate_functional"),
        "usable_class_level": sum(1 for x in rows if x["reference_status"].startswith("determinate_class_level")),
        "independent_of_module_input_on_determinate": sum(1 for x in rows if x["reference_label"] in DETERMINATE and x["dependency"] == "independent_of_module_input"),
        "active_path_before_fix": score("before_class", None),
        "active_path_after_fix": score("after_class", None),
        "it18_L_v1": score_l(l_v1), "it18_L_v2": score_l(l_v2),
        "rows_changed_by_fix": [{"pair_id": x["pair_id"], "compound": x["compound"], "need": x["need"],
                                 "before": x["before"], "after": x["after"], "reference_label": x["reference_label"],
                                 "verdict": ("removed_unsupported_attribution" if x["reference_label"] not in DETERMINATE
                                             else "abstained_although_the_reference_holds_a_direction")} for x in changed],
        "error_attribution": dict(collections.Counter(x["error_attribution"] for x in rows)),
    }


HEADER = ["pair_id", "need", "compound", "reference_label", "reference_status", "dependency", "error_attribution",
          "before", "after", "before_class", "after_class", "it18_L_v1", "it18_L_v2"]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--selection", required=True)
    ap.add_argument("--reference", required=True)
    ap.add_argument("--prefix", required=True)
    ap.add_argument("--guarded", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--out-tsv")
    a = ap.parse_args(argv)
    rows, summary = join(read_tsv(a.reference), read_tsv(a.prefix), read_tsv(a.guarded))
    Path(a.out).write_text(json.dumps(summary, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    if a.out_tsv:
        with open(a.out_tsv, "w", encoding="utf-8", newline="") as f:
            w = csv.writer(f, delimiter="\t", lineterminator="\n")
            w.writerow(HEADER)
            w.writerows([[r[k] for k in HEADER] for r in rows])
    print(json.dumps(summary, indent=1, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
