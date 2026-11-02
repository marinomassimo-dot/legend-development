#!/usr/bin/env python3
"""External-only versus WWOX-qualified selection over ONE usable universe (IT20 P5 reference experiment).

The question (IT20 diagnosis, question 3): does the WWOX qualification change a decision, relative to a
selection that uses the same catalogue and the same target list but no WWOX reasoning?

Both arms read the SAME usable universe U: every (compound family, module target, need) association the
existing search layer returns for the 23 qualified needs, minus the rows that layer itself excludes from
counts (placeholders, alias risk). Nothing is re-searched and no network call is made.

  arm E (external-only)    a target-list pipeline with no WWOX reasoning: keep an association with a
                           documented up/down action on a listed target, prefer an approved status, and
                           order by how many module targets and needs the family touches. This is the
                           reflex `matching_guidance_v3.md` section 5 warns against; it is the REFERENCE,
                           not a recommended method.
  arm W (WWOX-qualified)   the same U through the module's own qualification: an association counts only
                           when its documented action is direction-coherent with the need's stated
                           intervention direction (`consistency == consistent`). A need whose direction is
                           `uncertain` cannot qualify anything: its associations go to a named
                           DIRECTION-UNRESOLVED bucket, which is a visible gap, never a rejection.

Outputs (written beside this script): comparison_arms.tsv, comparison_summary.json.
Read-only, offline, standard library only, no clock in the data (the as-of date is passed in).

NOT medical advice. An association is a research lead, never a treatment. No dose, route, schedule or
preparation is carried by this tool, and an ordering here is an order of research investment - the value
of the next discriminating test - not a ranking of efficacy.
"""
from __future__ import annotations

import argparse
import collections
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / "framework/scripts"))

import repurposing_search as rs  # noqa: E402  (read-only use of the shipped search layer)
import compound_catalog as cc  # noqa: E402

AS_OF = "2026-11-02"
NEEDS = ROOT / "disease-models/wwox/research/drug_repurposing/needs/needs.json"
TOP_N = 10


def build_universe(needs: list[dict], idx: "rs.Index", roles: dict) -> list[dict]:
    """U: one row per (family, need, target, action) association the search layer returns, minus its own exclusions."""
    out = []
    for nd in needs:
        r = rs.associations_for_need(nd, idx, roles)
        for a in r["associations"]:
            if a["excluded_from_counts"] or a["target_kind"] not in rs.LINK_KINDS:
                continue
            out.append({
                "need": a["need"],
                "need_direction": a["need_direction"],
                "family": a["family"],
                "compound": a["compound"],
                "target": a["target"],
                "action_on_target": a["action_on_target"],
                "consistency": a["consistency"],
                "abstention_class": a["abstention_class"],
                "link_source": a["link_source"],
                "target_level": a["target_level"],
                "relation_kind": a["relation_kind"],
                "status_class": (a.get("pharmacology") or {}).get("status_class"),
            })
    return out


def arm_external(u: list[dict]) -> list[dict]:
    """Keep a documented up/down action on any listed target; order by targets then needs touched (the coverage reflex)."""
    kept = [a for a in u if a["action_on_target"] in ("up", "down")]
    by_fam: dict[str, list[dict]] = collections.defaultdict(list)
    for a in kept:
        by_fam[a["family"]].append(a)
    rows = []
    for fam, rs_ in sorted(by_fam.items()):
        approved = any(x["status_class"] == "approved_any_source" for x in rs_)
        rows.append({
            "family": fam,
            "compound": sorted({x["compound"] for x in rs_})[0],
            "n_targets": len({x["target"] for x in rs_}),
            "n_needs": len({x["need"] for x in rs_}),
            "approved": approved,
            "needs": sorted({x["need"] for x in rs_}),
        })
    rows.sort(key=lambda r: (-int(r["approved"]), -r["n_targets"], -r["n_needs"], r["compound"]))
    for i, r in enumerate(rows, 1):
        r["rank_external"] = i
    return rows


def arm_wwox(u: list[dict]) -> tuple[list[dict], list[dict]]:
    """Direction-coherent associations only; the uncertain-direction rows are returned apart, as a named gap."""
    coherent = [a for a in u if a["consistency"] == "consistent"]
    unresolved = [a for a in u if a["consistency"] == "direction_unresolved"
                  and a["abstention_class"] == "need_direction_not_evaluable"]
    by_fam: dict[str, list[dict]] = collections.defaultdict(list)
    for a in coherent:
        by_fam[a["family"]].append(a)
    rows = []
    for fam, rs_ in sorted(by_fam.items()):
        rows.append({
            "family": fam,
            "compound": sorted({x["compound"] for x in rs_})[0],
            "needs": sorted({x["need"] for x in rs_}),
            "n_needs": len({x["need"] for x in rs_}),
            "targets": sorted({x["target"] for x in rs_}),
            "approved": any(x["status_class"] == "approved_any_source" for x in rs_),
            "opposed_elsewhere": False,
            "levels": sorted({x["target_level"] for x in rs_}),
        })
    opposed_fams = {a["family"] for a in u if a["consistency"] == "opposed"}
    for r in rows:
        r["opposed_elsewhere"] = r["family"] in opposed_fams
    rows.sort(key=lambda r: (r["compound"], r["family"]))
    return rows, unresolved


def needs_without_a_tool(u: list[dict], needs: list[dict]) -> list[dict]:
    """A need has no adequate tool when U holds no direction-coherent association for it. The reason is stated."""
    coherent_needs = {a["need"] for a in u if a["consistency"] == "consistent"}
    any_assoc = collections.Counter(a["need"] for a in u)
    out = []
    for nd in needs:
        nid = nd["id"]
        if nid in coherent_needs:
            continue
        d = nd["intervention_direction"]["direction"]
        if any_assoc.get(nid, 0) == 0:
            why = "no catalogue association at all on this need's targets"
        elif d in ("uncertain", "modulate"):
            why = "direction of the need is unresolved, so no association can be qualified as coherent"
        else:
            why = "associations exist but none carries a documented action coherent with the stated direction"
        out.append({"need": nid, "need_direction": d, "associations_in_universe": any_assoc.get(nid, 0), "why_no_tool": why})
    return out


def compare(as_of: str = AS_OF, needs_path: Path = NEEDS, catalog: Path | None = None,
            universe: list[dict] | None = None, needs: list[dict] | None = None) -> dict:
    """`universe` and `needs` may be passed in by a caller that has already built them (one pass per run)."""
    if needs is None:
        needs = rs.load_needs(needs_path)["needs"]
    if universe is None:
        entries = cc.load(catalog or cc.DEFAULT_CATALOG)
        idx = rs.Index(entries, rs.load_artefacts(), rs.module_intervention_symbols(needs))
        universe = build_universe(needs, idx, rs.load_roles())
    u = universe
    e_rows = arm_external(u)
    w_rows, unresolved = arm_wwox(u)
    e_top = e_rows[:TOP_N]
    e_fams, w_fams = {r["family"] for r in e_rows}, {r["family"] for r in w_rows}
    e_top_fams = {r["family"] for r in e_top}
    return {
        "schema": "repurposing.comparison.arms/1",
        "as_of": as_of,
        "plain_statement": "An order of research investment - the value of the next discriminating test given its cost and "
                           "what the result would change - not a ranking of efficacy. Nothing here is medical advice.",
        "universe": {
            "associations": len(u),
            "families": len({a["family"] for a in u}),
            "needs": len({a["need"] for a in u}),
            "by_consistency": dict(sorted(collections.Counter(a["consistency"] for a in u).items())),
            "definition": "every (family, target, need) association the shipped search layer returns for the 23 needs, "
                          "minus the rows it excludes from counts; identical for both arms",
        },
        "arm_external": {"families_selected": len(e_fams), "top_n": TOP_N,
                         "top": [{k: r[k] for k in ("rank_external", "compound", "family", "n_targets", "n_needs", "approved")} for r in e_top]},
        "arm_wwox": {"families_selected": len(w_fams),
                     "approved_among_them": sum(1 for r in w_rows if r["approved"]),
                     "with_an_opposed_action_elsewhere": sum(1 for r in w_rows if r["opposed_elsewhere"]),
                     "needs_covered": sorted({n for r in w_rows for n in r["needs"]})},
        "overlap": {
            "in_both": sorted(e_fams & w_fams),
            "external_only": len(e_fams - w_fams),
            "wwox_only": sorted(w_fams - e_fams),
            "external_top_n_surviving_qualification": sorted(e_top_fams & w_fams),
            "external_top_n_not_qualified": sorted(e_top_fams - w_fams),
        },
        "direction_unresolved": {
            "associations": len(unresolved),
            "families": len({a["family"] for a in unresolved}),
            "needs": sorted({a["need"] for a in unresolved}),
            "statement": "a visible gap, not a rejection: the need's own direction is unresolved, so neither arm can "
                         "qualify a lever on it and the ordering must not imply one",
        },
        "needs_without_an_adequate_tool": needs_without_a_tool(u, needs),
    }


ARM_COLS = ["arm", "rank_external", "compound", "family", "n_targets", "n_needs", "approved", "opposed_elsewhere", "needs"]


def arm_rows_for_tsv(summary: dict, e_rows: list[dict], w_rows: list[dict]) -> list[dict]:
    rows = []
    for r in e_rows[:TOP_N]:
        rows.append({"arm": "external_only", "rank_external": r["rank_external"], "compound": r["compound"], "family": r["family"],
                     "n_targets": r["n_targets"], "n_needs": r["n_needs"], "approved": "yes" if r["approved"] else "no",
                     "opposed_elsewhere": "", "needs": ";".join(r["needs"])})
    for r in w_rows:
        rows.append({"arm": "wwox_qualified", "rank_external": "", "compound": r["compound"], "family": r["family"],
                     "n_targets": len(r["targets"]), "n_needs": r["n_needs"], "approved": "yes" if r["approved"] else "no",
                     "opposed_elsewhere": "yes" if r["opposed_elsewhere"] else "no", "needs": ";".join(r["needs"])})
    return rows


def tsv_bytes(rows: list[dict], cols: list[str]) -> bytes:
    out = ["\t".join(cols)]
    for r in rows:
        out.append("\t".join(str(r.get(c, "")).replace("\t", " ").replace("\n", " ") for c in cols))
    return ("\n".join(out) + "\n").encode()


def cmd_run(args) -> int:
    needs = rs.load_needs(args.needs)["needs"]
    entries = cc.load(args.catalog or cc.DEFAULT_CATALOG)
    idx = rs.Index(entries, rs.load_artefacts(), rs.module_intervention_symbols(needs))
    roles = rs.load_roles()
    u = build_universe(needs, idx, roles)
    e_rows = arm_external(u)
    w_rows, _ = arm_wwox(u)
    summary = compare(args.as_of, args.needs, args.catalog, universe=u, needs=needs)
    (HERE / "comparison_summary.json").write_bytes((json.dumps(summary, indent=1, ensure_ascii=False) + "\n").encode())
    if args.dump_universe:
        args.dump_universe.write_bytes((json.dumps(u, ensure_ascii=False) + "\n").encode())
    (HERE / "comparison_arms.tsv").write_bytes(tsv_bytes(arm_rows_for_tsv(summary, e_rows, w_rows), ARM_COLS))
    ov = summary["overlap"]
    print(f"universe: {summary['universe']['associations']} associations, {summary['universe']['families']} families")
    print(f"arm E selected {summary['arm_external']['families_selected']} families; arm W selected {summary['arm_wwox']['families_selected']}")
    print(f"external top {TOP_N}: {len(ov['external_top_n_surviving_qualification'])} survive the WWOX qualification, "
          f"{len(ov['external_top_n_not_qualified'])} do not")
    print(f"WWOX-only families: {len(ov['wwox_only'])}; needs with no adequate tool: {len(summary['needs_without_an_adequate_tool'])}")
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0], formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--as-of", default=AS_OF)
    ap.add_argument("--needs", type=Path, default=NEEDS)
    ap.add_argument("--catalog", type=Path, default=None)
    ap.add_argument("--dump-universe", type=Path, default=None,
                    help="write the built usable universe to this path (a working file, not a package artefact)")
    sub = ap.add_subparsers(dest="cmd")
    sub.add_parser("run", help="write comparison_summary.json and comparison_arms.tsv")
    a = ap.parse_args(argv)
    if a.cmd != "run":
        ap.print_help()
        return 0
    return cmd_run(a)


if __name__ == "__main__":
    sys.exit(main())
