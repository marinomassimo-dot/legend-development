"""Benchmark I · CLI Retrieval v2 post-hoc: can deterministic selection TIERS, or a whole-record
byte budget in tier order, keep PROGRESSIVE's recall at a material context reduction?

Harness evidence only; nothing here changes a claim, a registry or a retrieval rule. Post-hoc:
the fixtures, labels and candidate sets are Benchmark I's, frozen; only the ordering is new.

Tiers (retrieval distance, never a score): 1 = CURRENT's hit (identity, PMID citation, K1 link or
hop); 2 = a PROGRESSIVE literal hit on >= 2 kept terms; 3 = a hit on one term. Whole records are
admitted in tier order, claim-ID order inside a tier; claim bytes are measured at each fixture's
`commit_read` from git objects. A term-count order inside the literal tiers is also reported,
labelled exploratory, because it is a weight the v2 brief did not ask for. Run from the root:

    python3 framework/eval/benchmarks/BENCH-I-CLAIM-RETRIEVAL/r2_posthoc_tiers.py [CAP20.json]

where CAP20.json is `claim_retrieval_bench.py i1 --df-cap-fraction 0.2 --no-sensitivity --out …`
(the 0.20 sensitivity arm keeps no selection paths). It writes `r2_posthoc_tiers.json` beside
itself and touches nothing else.
"""
import json, statistics as st, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
sys.path.insert(0, str(REPO / "framework/scripts"))
import registry_records as rr  # noqa: E402

CLAIMS = "disease-models/wwox/registries/claim_registry_current.md"


def claim_bytes(commit):
    text = subprocess.run(["git", "-C", str(REPO), "show", f"{commit}:{CLAIMS}"],
                          capture_output=True, text=True, check=True).stdout
    out = {}
    for b in rr.partition(text, (2,)):
        if b.kind == "record":
            out[b.key] = len(text[b.start:b.end].encode())
    return out


def nterms(path):
    if not path.startswith("term route"):
        return 0
    return len(path.split(":", 1)[1].split(","))


def analyse(results_path, label):
    d = json.load(open(results_path))
    rows = [r for r in d["rows"] if r["class"] == "STRONG"]
    cache = {}
    per = []
    for r in rows:
        sizes = cache.setdefault(r["commit_read"], claim_bytes(r["commit_read"]))
        total = sum(sizes.values())
        cur = set(r["strategies"]["CURRENT"]["candidates"])
        p = r["strategies"]["PROGRESSIVE"]
        sp = p["selection_path"]
        tier = {}
        for c in p["candidates"]:
            tier[c] = 1 if c in cur else (2 if nterms(sp.get(c, "")) >= 2 else 3)
        ids = sorted(tier, key=lambda c: (tier[c], c))                     # tiers, id order
        ids_tc = sorted(tier, key=lambda c: (tier[c] if tier[c] == 1 else 2,
                                             -nterms(sp.get(c, "")), c))   # exploratory
        def cum(order):
            acc, out = 0, {}
            for c in order:
                acc += sizes.get(c, 0)
                out[c] = acc / total
            return out
        c_tier, c_tc = cum(ids), cum(ids_tc)
        t2 = sum(sizes.get(c, 0) for c in tier if tier[c] <= 2) / total
        found = [t for t in r["targets"] if t in tier]
        per.append({
            "fx": r["fixture_id"], "targets": len(r["targets"]), "found": len(found),
            "tier_of": {t: tier.get(t, "MISS") for t in r["targets"]},
            "le2_hits": sum(1 for t in r["targets"] if tier.get(t, 9) <= 2), "le2_frac": t2,
            "all_frac": sum(sizes.get(c, 0) for c in tier) / total,
            "need_tier": max((c_tier[t] for t in found), default=0),
            "need_tc": max((c_tc[t] for t in found), default=0)})
    tot = sum(x["targets"] for x in per)
    q = lambda a, f: sorted(a)[min(len(a) - 1, int(f * len(a)))]
    print(f"== {label}: STRONG fixtures {len(per)}, targets {tot}")
    print(f"  PROGRESSIVE all candidates: {sum(x['found'] for x in per)}/{tot}, median frac "
          f"{st.median(x['all_frac'] for x in per):.3f} p90 {q([x['all_frac'] for x in per], .9):.3f}")
    print(f"  TIER<=2 cut: {sum(x['le2_hits'] for x in per)}/{tot}, median frac "
          f"{st.median(x['le2_frac'] for x in per):.3f} p90 {q([x['le2_frac'] for x in per], .9):.3f}")
    for name, key in (("tier then id", "need_tier"), ("tier then term-count (exploratory)", "need_tc")):
        need = [x[key] for x in per if x["found"]]
        print(f"  budget to reach every found target, {name}: median {st.median(need):.3f} "
              f"p90 {q(need, .9):.3f} max {max(need):.3f}")
        for budget in (0.3, 0.4, 0.5):
            hit = 0
            for x in per:
                hit += x["found"] if x[key] <= budget else 0   # conservative: all-or-nothing
            print(f"    fixed budget {budget:.0%}: fixtures fully within budget "
                  f"{sum(1 for x in per if x['found'] == x['targets'] and x[key] <= budget)}/{len(per)}")
    return per


if __name__ == "__main__":
    runs = [(HERE / "i1_results_after_K1.json", "df_cap 0.10 (primary, frozen)")]
    if len(sys.argv) > 1:
        runs.append((Path(sys.argv[1]), "df_cap 0.20 (sensitivity, regenerated)"))
    out = {label: analyse(path, label) for path, label in runs}
    (HERE / "r2_posthoc_tiers.json").write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
