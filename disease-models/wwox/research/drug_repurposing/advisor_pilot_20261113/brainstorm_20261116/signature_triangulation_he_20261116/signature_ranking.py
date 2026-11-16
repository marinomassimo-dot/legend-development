"""Step A of the signature triangulation (HE): the class-level signature ranking from the held LINCS-type table.

    python3 signature_ranking.py        (run from the repository root; reads held tables only, writes the two TSVs beside itself)

Reads  network_comparison_it7_p3_20261029/results/{signature_scores,family_scores}.tsv and inputs/pilot_lincs_contexts.tsv.
Writes signature_rows.tsv (one row per signature of an antiseizure-class agent, with its context) and signature_ranking.tsv
(one row per rule class that has at least one agent: n signatures, k with opposition > 0, the share, the base rate of the SAME
context, the effect = share minus base rate, the two exact one-sided binomial tails against the base rate (opposing or more; aligned with WWOX loss or more), and the rank by effect).
No query, no network. `opposition_score` > 0 means the signature opposes the WWOX-loss module; < 0 means it moves it further.
"""
import csv
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
D = Path("disease-models/wwox/research/drug_repurposing/network_comparison_it7_p3_20261029")
# agent (family name in the held table) -> (rule v1 class id, confidence of the mapping)
AGENT_CLASS = {
    "CARBAMAZEPINE": ("sodium_channel", "high"),
    "LAMOTRIGINE": ("sodium_channel", "high"),
    "VALPROIC ACID": ("valproate_type", "high"),
    "ZONISAMIDE": ("carbonic_anhydrase_multitarget", "medium: multi-target, carbonic-anhydrase inhibitor"),
    "DEXAMETHASONE": ("steroid_acth", "low: a glucocorticoid, not the corticotropin or prednisolone the class means"),
}
NOT_MAPPED = {"RILUZOLE": "glutamate-release modulator, no rule class", "NIMODIPINE": "L-type calcium blocker, no rule class"}
CONTEXT_NAME = {"E": "neuron-like (NEU, evaluation contexts)", "B": "progenitor-like (NPC, build contexts)"}


def tail(k, n, p):
    """P(X >= k) for X ~ Binomial(n, p)."""
    return sum(math.comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(k, n + 1))


def tail_low(k, n, p):
    """P(X <= k) for X ~ Binomial(n, p): the other tail (signatures that move the module the way WWOX loss does)."""
    return sum(math.comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(0, k + 1))


fam = {r["family_id"]: r["name"] for r in csv.DictReader(open(D / "results/family_scores.tsv"), delimiter="\t")}
pert2fam = {}
for r in csv.DictReader(open(D / "inputs/pilot_lincs_contexts.tsv"), delimiter="\t"):
    pert2fam.setdefault(r["pert_id"], set()).add(r["family_id"])
sigs = list(csv.DictReader(open(D / "results/signature_scores.tsv"), delimiter="\t"))
base = {}
for ctx in ("E", "B"):
    v = [float(s["opposition_score"]) for s in sigs if s["context_class"] == ctx]
    base[ctx] = (len(v), sum(x > 0 for x in v) / len(v))

rows = []
for s in sigs:
    for f in sorted(pert2fam.get(s["pert_id"], ())):
        name = fam.get(f)
        if name in AGENT_CLASS or name in NOT_MAPPED:
            rows.append({"agent": name, "class_id": AGENT_CLASS.get(name, ("", ""))[0] or "not_mapped", "cell_id": s["cell_id"],
                         "context_class": s["context_class"], "dose": s["dose"], "time": s["time"], "opposition_score": s["opposition_score"]})
rows.sort(key=lambda r: (r["agent"], r["context_class"], r["time"], r["opposition_score"]))
with open(HERE / "signature_rows.tsv", "w", newline="") as h:
    w = csv.DictWriter(h, fieldnames=list(rows[0]), delimiter="\t", lineterminator="\n")
    w.writeheader()
    w.writerows(rows)

out = []
for ctx in ("E", "B"):
    classes = sorted({r["class_id"] for r in rows if r["class_id"] != "not_mapped"})
    part = []
    for c in classes:
        mine = [float(r["opposition_score"]) for r in rows if r["class_id"] == c and r["context_class"] == ctx]
        if not mine:
            continue
        n, k = len(mine), sum(x > 0 for x in mine)
        p0 = base[ctx][1]
        part.append({"context": ctx, "class_id": c, "agents": ",".join(sorted({r["agent"] for r in rows if r["class_id"] == c})),
                     "n_signatures": n, "k_opposing": k, "share_opposing": f"{k / n:.3f}", "base_rate_same_context": f"{p0:.3f}",
                     "effect_vs_base": f"{k / n - p0:+.3f}", "p_tail_opposing_or_more": f"{tail(k, n, p0):.3f}", "p_tail_aligned_or_more": f"{tail_low(k, n, p0):.3f}",
                     "mapping_confidence": min((AGENT_CLASS[a][1] for a in AGENT_CLASS if AGENT_CLASS[a][0] == c), key=lambda t: ("high", "medium", "low").index(t.split(":")[0]))})
    part.sort(key=lambda r: (-float(r["effect_vs_base"]), r["class_id"]))
    for i, r in enumerate(part, 1):
        r["rank_by_effect"] = 1 + sum(float(o["effect_vs_base"]) > float(r["effect_vs_base"]) for o in part)
        out.append(r)
with open(HERE / "signature_ranking.tsv", "w", newline="") as h:
    w = csv.DictWriter(h, fieldnames=list(out[0]), delimiter="\t", lineterminator="\n")
    w.writeheader()
    w.writerows(out)
print(f"base rate of opposition > 0: " + ", ".join(f"{CONTEXT_NAME[c]} {base[c][1]:.3f} over {base[c][0]} signatures" for c in base))
for r in out:
    print(r["context"], r["class_id"], r["agents"], f"{r['k_opposing']}/{r['n_signatures']}", r["effect_vs_base"], "p(opposing tail)", r["p_tail_opposing_or_more"], "p(aligned tail)", r["p_tail_aligned_or_more"], "rank", r["rank_by_effect"])
