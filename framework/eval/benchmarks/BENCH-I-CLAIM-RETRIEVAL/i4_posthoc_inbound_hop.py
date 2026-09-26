"""Benchmark I · I4 post-hoc: does one INBOUND hop over CURRENT's hits reach what K1 still misses?

Harness evidence only; nothing here changes a claim or a registry.

Variant INBOUND1 = CURRENT (`registry_records.select(pmid=…, hops=1)`, K1 semantics) plus every
claim record that wikilinks to ANY record CURRENT returned — not only to the query's identity
records, which K1 already turns into `mention` hits. Frozen STRONG fixtures, registries read at
each event's parent in a detached worktree, as in I1. Run from the repository root:

    python3 framework/eval/benchmarks/BENCH-I-CLAIM-RETRIEVAL/i4_posthoc_inbound_hop.py

It writes `i4_posthoc_inbound_hop.json` beside itself and touches nothing else.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / "framework/scripts"))
import claim_retrieval_bench as crb  # noqa: E402
import registry_records  # noqa: E402

LINK = re.compile(r"\[\[([A-Za-z0-9_]+)#([^\]|]+)(?:\|[^\]]*)?\]\]")


def med(xs: list[float]) -> float:
    xs = sorted(xs)
    n = len(xs)
    return xs[n // 2] if n % 2 else round((xs[n // 2 - 1] + xs[n // 2]) / 2, 4)


def main() -> int:
    data = json.loads(crb.FIXTURES.read_text(encoding="utf-8"))
    fixtures = [f for f in data["fixtures"] if f["class"] == "STRONG"]
    by_parent: dict[str, list[dict]] = {}
    for f in fixtures:
        by_parent.setdefault(f["parent"], []).append(f)
    rows = []
    for parent, group in by_parent.items():
        with crb.tree_at(parent) as root:
            claims = [r for r in registry_records.parse_records(root, "wwox", crb.CLAIM_STEM)
                      if r.kind == "record"]
            size = {c.identity_id.upper(): len(c.text.encode("utf-8")) for c in claims}
            reg_bytes = sum(size.values())
            for f in group:
                found = registry_records.select(root, "wwox", pmid=f["pmid"], hops=1)
                hit_keys = {(r.source, r.identity_id.upper()) for r, _w in found.hits}
                cur = {r.identity_id.upper() for r, _w in found.hits
                       if r.source == crb.CLAIM_STEM and r.kind == "record"}
                inbound = {c.identity_id.upper() for c in claims
                           for stem, rid in LINK.findall(c.text)
                           if (stem, rid.strip().upper()) in hit_keys}
                union = cur | inbound
                rows.append({
                    "fixture": f["fixture_id"], "targets": f["targets"],
                    "current_hit": [t for t in f["targets"] if t in cur],
                    "inbound1_hit": [t for t in f["targets"] if t in union],
                    "current_n": len(cur), "inbound1_n": len(union),
                    "current_frac": round(sum(size.get(c, 0) for c in cur) / reg_bytes, 4),
                    "inbound1_frac": round(sum(size.get(c, 0) for c in union) / reg_bytes, 4)})
    rows.sort(key=lambda r: r["fixture"])
    tot = sum(len(r["targets"]) for r in rows)
    cur = sum(len(r["current_hit"]) for r in rows)
    inb = sum(len(r["inbound1_hit"]) for r in rows)
    out = {
        "_schema": "LEGEND Benchmark I · I4 post-hoc inbound hop v1",
        "fixtures_sha256": hashlib.sha256(crb.FIXTURES.read_bytes()).hexdigest(),
        "tool_sha256": {n: hashlib.sha256((ROOT / "framework/scripts" / n).read_bytes()).hexdigest()
                        for n in ("registry_records.py", "claim_retrieval_bench.py")},
        "strong_targets": tot, "current_retrieved": cur, "inbound1_retrieved": inb,
        "fixtures_full_current": sum(len(r["current_hit"]) == len(r["targets"]) for r in rows),
        "fixtures_full_inbound1": sum(len(r["inbound1_hit"]) == len(r["targets"]) for r in rows),
        "median_frac_current": med([r["current_frac"] for r in rows]),
        "median_frac_inbound1": med([r["inbound1_frac"] for r in rows]),
        "max_frac_inbound1": max(r["inbound1_frac"] for r in rows),
        "median_candidates_inbound1": med([r["inbound1_n"] for r in rows]),
        "rows": rows}
    dest = HERE / "i4_posthoc_inbound_hop.json"
    dest.write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
    print(f"STRONG targets {tot}: CURRENT {cur}, INBOUND1 {inb}; median claim-byte fraction "
          f"{out['median_frac_current']} -> {out['median_frac_inbound1']} -> {dest.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
