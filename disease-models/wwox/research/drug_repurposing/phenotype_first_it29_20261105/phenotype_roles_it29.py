#!/usr/bin/env python3
"""IT29: turn signed perturbation evidence into target-to-need coupling rows the existing search layer consumes.

Input  : one or more evidence_it29_<letter>.tsv files (columns in BRIEF_COMMON.md) and a need id per endpoint.
Output : a roles TSV with the columns of coverage/target_roles.tsv (need_id, symbol, coupling, basis, qualifier),
         to be passed to `repurposing_search.py --roles` (the committed roles file is never edited).

Rules (each protects against a named mistake):
  * Only rows that name a target AND are target_controlled or genetic sign a target. A compound-only effect is not
    attributed to its nominal target.
  * Viability and transcript-level rows never sign; unknown / null / undetermined / context_dependent rows never
    sign either (unknown is not negative), but a context_dependent row, attributed or not, makes the target `unresolved`
    because a discordance on the same question must stay visible (attribution limits positive claims, not caution).
  * Direction is converted through the action on the TARGET: lowering target activity with a favourable result
    means more target activity lowers the endpoint, so coupling `opposite`.
  * Rows from different sources that disagree give `unresolved` with the count in the qualifier; they are not averaged.
  * Every emitted row carries EXTERNAL_TRANSFER in the qualifier, so a qualified lever is never read as a WWOX measurement.
"""
from __future__ import annotations

import argparse
import csv
import sys
from collections import defaultdict
from pathlib import Path

LOWER = {"inhibit", "antagonize", "loss", "knockout", "knockdown", "block", "degrade", "lower"}
RAISE = {"activate", "agonize", "gain", "overexpress", "raise", "potentiate"}
SIGNING_LEVELS = {"function", "marker"}


def activity_change(action: str) -> str | None:
    a = (action or "").strip().lower()
    if a in LOWER:
        return "down"
    if a in RAISE:
        return "up"
    return None


def signs(row: dict) -> str | None:
    """'same' / 'opposite' for one row, or None when the row cannot sign."""
    if not row.get("target_symbol", "").strip():
        return None
    if row.get("attribution") != "target_controlled" and not row.get("intervention_type", "").startswith("genetic"):
        return None
    if row.get("measure_level") not in SIGNING_LEVELS:
        return None
    ch = activity_change(row.get("action_on_target", ""))
    d = row.get("direction_on_endpoint")
    if ch is None or d not in ("favourable", "adverse"):
        return None
    helps = d == "favourable"
    # activity down + favourable  => more activity lowers the endpoint => opposite
    # activity up   + favourable  => same
    return "same" if (ch == "up") == helps else "opposite"


def build(rows: list[dict], need_id: str) -> list[dict]:
    by_target = defaultdict(list)
    for r in rows:
        sym = r.get("target_symbol", "").strip().upper()
        if sym:
            by_target[sym].append(r)
    out = []
    for sym, rs in sorted(by_target.items()):
        votes = defaultdict(set)
        ctx = 0
        for r in rs:
            if r.get("direction_on_endpoint") == "context_dependent":
                ctx += 1                          # a compound-only row cannot SIGN a target, but it may keep a discordance visible
            s = signs(r)
            if s:
                votes[s].add(r["source_id"])
        n = {k: len(v) for k, v in votes.items()}
        if not n and not ctx:
            continue                               # nothing signs: no row, so the abstention class stays no_coupling_row
        if len(n) == 2 or ctx:
            coupling, why = "unresolved", f"discordant or context-dependent: same={n.get('same', 0)} opposite={n.get('opposite', 0)} sources, context_dependent rows={ctx}"
        else:
            coupling = next(iter(n))
            auto = any(r.get("composition_or_autonomous") == "cell_autonomous" and signs(r) for r in rs)
            fn = any(r.get("measure_level") == "function" and signs(r) for r in rs)
            why = f"{n[coupling]} source(s); " + ("cell-autonomous shown" if auto else "autonomy not separated") + "; " + ("functional readout" if fn else "marker-level readout only")
        out.append({
            "need_id": need_id, "symbol": sym, "coupling": coupling,
            "basis": f"perturbation evidence for the endpoint (IT29 phenotype-first table): {why}",
            "qualifier": "EXTERNAL_TRANSFER: sign comes from non-WWOX systems; not measured in a WWOX-deficient cell; " + why
                         + "".join("; " + n for n in dict.fromkeys(r.get("curation_note", "").strip() for r in rs) if n),
        })
    return out


def extend_needs(needs_path: Path, need_id: str, symbols: list[str], hgnc: dict, out: Path) -> int:
    """Write a copy of needs.json in which `need_id` also lists `symbols` as intervention targets (the search layer
    walks need -> targets, so a signed target that the need does not list is never reached). Returns how many were added."""
    import json
    doc = json.loads(needs_path.read_text(encoding="utf-8"))
    needs = doc["needs"] if isinstance(doc, dict) and "needs" in doc else doc
    need = next(n for n in needs if n["id"] == need_id)
    have = {t["symbol"].upper() for t in need["targets"]}
    added = 0
    for sym in symbols:
        if sym.upper() in have or sym.upper() not in hgnc:
            continue
        need["targets"].append({"symbol": sym.upper(), "role": "target with perturbation evidence for this endpoint (IT29 phenotype-first table)",
                                "hgnc_id": hgnc[sym.upper()][0], "hgnc_name": hgnc[sym.upper()][1], "target_kind": "intervention_target"})
        added += 1
    out.write_text(json.dumps(doc, indent=1, ensure_ascii=False), encoding="utf-8")
    return added


def read_tsv(path: Path) -> list[dict]:
    with open(path, encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--need", required=True)
    ap.add_argument("--evidence", nargs="+", type=Path, required=True)
    ap.add_argument("--base-roles", type=Path, help="existing roles file to append to (not modified)")
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--needs-in", type=Path, help="needs.json to extend with the signed targets (needs --hgnc and --needs-out)")
    ap.add_argument("--hgnc", type=Path, help="TSV symbol, hgnc_id, hgnc_name")
    ap.add_argument("--needs-out", type=Path)
    a = ap.parse_args(argv)
    rows = [r for p in a.evidence for r in read_tsv(p)]
    new = build(rows, a.need)
    cols = ["need_id", "symbol", "coupling", "basis", "qualifier"]
    base = read_tsv(a.base_roles) if a.base_roles else []
    keep = {(r["need_id"], r["symbol"].upper()) for r in new}
    base = [r for r in base if (r["need_id"], r["symbol"].upper()) not in keep]
    with open(a.out, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(base + new)
    if a.needs_in:
        hg = {r["symbol"].upper(): (r["hgnc_id"], r["hgnc_name"]) for r in read_tsv(a.hgnc)}
        n_add = extend_needs(a.needs_in, a.need, [r["symbol"] for r in new], hg, a.needs_out)
        print(f"{n_add} target(s) added to {a.need} in {a.needs_out}", file=sys.stderr)
    print(f"{len(new)} coupling row(s) for {a.need} -> {a.out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
