"""Step B of the signature triangulation (HE), run only after FREEZE_BEFORE_COMPARISON.md was committed.

    python3 triangulate.py        (run from the repository root; reads committed files, writes triangulation.tsv beside itself)

Compares the frozen class-level signature ranking (signature_ranking.tsv, neuron-like context primary, progenitor-like beside it) with
(1) the frozen matrix F1 scores read from SCI's freeze commit (per-thread sum and origin-collapsed), and
(2) IT's observed class ordering re-derived from the sealed extraction (counts as in he_crosscheck_20261116, `aed_matrix.concordance`).
Tied predictions score 0.5; an observed tie is not classifiable; a class the signature does not cover drops its pairs.
For (1) the matrix plays the reference role: two orderings of the shared classes are compared pair by pair, a tie in the reference is not classifiable.
"""
import csv
import itertools
import re
import runpy
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, "framework/scripts")
import aed_matrix as am  # noqa: E402

HERE = Path(__file__).resolve().parent
B = HERE.parent
FREEZE = "f5b71a3f4"
ranking = {}
for r in csv.DictReader(open(HERE / "signature_ranking.tsv"), delimiter="\t"):
    ranking.setdefault(r["context"], {})[r["class_id"]] = float(r["effect_vs_base"])


def two_orderings(pred, ref):
    """pair concordance of `pred` with the reference ordering `ref` on the classes both hold; ties in pred score 0.5, ties in ref are not classifiable"""
    shared = sorted(set(pred) & set(ref))
    pairs = list(itertools.combinations(shared, 2))
    cl = [(a, b) for a, b in pairs if ref[a] != ref[b]]
    total = 0.0
    for a, b in cl:
        d = (pred[a] > pred[b]) - (pred[a] < pred[b])
        o = 1 if ref[a] > ref[b] else -1
        total += 0.5 if d == 0 else (1.0 if d == o else 0.0)
    return {"shared_classes": len(shared), "pairs": len(pairs), "classifiable": len(cl), "concordance": (total / len(cl)) if cl else None}


def show(commit, path):
    return subprocess.run(["git", "show", f"{commit}:{path}"], capture_output=True, text=True, check=True).stdout


LABEL = {"sodium-channel": "sodium_channel", "valproate-type": "valproate_type", "carbonic-anhydrase/multi-target": "carbonic_anhydrase_multitarget",
         "steroid/ACTH": "steroid_acth", "ketogenic diet": "ketogenic_diet", "GABA-AT/GAT": "gaba_at_gat", "SV2A": "sv2a",
         "benzodiazepines": "benzodiazepine", "GABA-A PAM (non-benzodiazepine)": "gabaa_pam_nonbzd"}
matrix = {}
for kind in ("per_thread_sum", "origin_collapsed"):
    d = {}
    for r in csv.DictReader(show(FREEZE, "disease-models/wwox/research/drug_repurposing/aed_matrix_sci_20261116/output/rankings.tsv").splitlines(), delimiter="\t"):
        if (r["endpoint"], r["window"], r["ranking"]) == ("seizure", "P13-P15", kind):
            score = int(re.search(r"\(score (\d+)\)\s*$", r["classes"]).group(1))
            for name in re.sub(r"\s*\(score \d+\)\s*$", "", r["classes"]).split("; "):
                if name.strip() in LABEL:
                    d[LABEL[name.strip()]] = float(score)
    matrix[kind] = d

import contextlib
import io
with contextlib.redirect_stdout(io.StringIO()):   # the cross-check prints its own report when run; only its counts are used here
    ns = runpy.run_path(str(B / "he_crosscheck_20261116/crosscheck_it_scoring.py"), run_name="not_main")
counts = ns["mine_counts"]

rows = []
for ctx, name in (("E", "neuron-like"), ("B", "progenitor-like")):
    sig = ranking[ctx]
    for kind in ("per_thread_sum", "origin_collapsed"):
        r = two_orderings(sig, matrix[kind])
        rows.append({"signature_context": name, "reference": f"matrix F1 {kind} (seizure P13-P15, frozen)", **r})
    for version, col in (("partial_counts", 1), ("resolved_only", 2)):
        r = am.concordance(sig, {c: (v[0], v[col]) for c, v in counts.items()})
        shared = sorted(set(sig) & {c for c, v in counts.items() if v[0] >= 3})
        rows.append({"signature_context": name, "reference": f"IT observed ordering, {version} (sealed extraction)", "shared_classes": len(shared),
                     "pairs": r["pairs"] if False else len(list(itertools.combinations(shared, 2))), "classifiable": None, "concordance": r["concordance"], "_scored": r["scored"]})
for r in rows:
    if "_scored" in r:
        r["classifiable"] = r.pop("_scored")
cols = ["signature_context", "reference", "shared_classes", "pairs", "classifiable", "concordance"]
with open(HERE / "triangulation.tsv", "w", newline="") as h:
    w = csv.DictWriter(h, fieldnames=cols, delimiter="\t", lineterminator="\n")
    w.writeheader()
    for r in rows:
        w.writerow({**r, "concordance": "not scorable" if r["concordance"] is None else f"{r['concordance']:.2f}"})
for r in rows:
    print(f"{r['signature_context']:15s} vs {r['reference']:62s} shared {r['shared_classes']} pairs {r['pairs']} classifiable-and-scored {r['classifiable']} concordance " + ("not scorable" if r["concordance"] is None else f"{r['concordance']:.2f}"))
