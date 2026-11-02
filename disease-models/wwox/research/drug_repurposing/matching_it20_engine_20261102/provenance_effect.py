#!/usr/bin/env python3
"""IT20 P2 - what the republication datum changes in the ACTIVE path, measured on the real catalogue.

The A/B is on DATA, not on a code flag: `source_artefacts.tsv` either holds the
`republication:ChEMBL` row or it does not. "before" runs the active path with that row removed
(the IT19 behaviour, group guard on), "after" runs it with the row present. Nothing else differs.

Writes a per-row table (`provenance_rows.tsv`), the counts (`provenance_effect.json`) and the
compounds whose only directed row in a need was a republished copy, so the price of the abstention
is visible and not smoothed.

  python3 matching_it20_engine_20261102/provenance_effect.py --out-dir matching_it20_engine_20261102

Offline, standard library only. Non-canonical research material; not medical advice; pharmacological
compatibility only, no benefit claim; no compound is proposed for use.
"""
from __future__ import annotations

import argparse
import collections
import csv
import json
import sys
from pathlib import Path

DR = Path(__file__).resolve().parents[1]
REPO = DR.parents[3]
sys.path.insert(0, str(REPO / "framework/scripts"))
import compound_catalog as cc  # noqa: E402
import repurposing_search as rs  # noqa: E402

DIRECTED = ("consistent", "opposed")


def run(artefacts: list[dict]) -> list[dict]:
    needs = rs.load_needs()["needs"]
    entries = cc.load(cc.DEFAULT_CATALOG)
    idx = rs.Index(entries, artefacts, rs.module_intervention_symbols(needs))
    roles = rs.load_roles()
    out = []
    for n in needs:
        out += rs.associations_for_need(n, idx, roles)["associations"]
    return out


def key(a: dict) -> tuple:
    """The business identity of a row. It is NOT unique: one record can carry two rows on the same gene and
    action from two claim sources (Verapamil TTD and TEND, Esketamine twice). Keying a dict on it silently
    collapsed 631 of 5240 rows in the first draft of this script, so the two runs are paired POSITIONALLY and
    this key is only asserted to agree pair by pair."""
    return (a["need"], a["target"], a["catalogue_id"], a["link_source"], str(a["action_raw"]))


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--out-dir", type=Path, default=Path(__file__).resolve().parent)
    a = ap.parse_args(argv)
    full = rs.load_artefacts()
    without = [r for r in full if not r["rule"].startswith("republication:")]
    assert len(without) == len(full) - 1, "the republication row is not in source_artefacts.tsv"
    # three arms, so the two data rows added in IT20 are not reported as one effect:
    #   it19   = neither row            (the state IT19 left)
    #   p2only = republication only     (the fix, before the recovered evidence)
    #   full   = both rows              (what the branch ships)
    it19 = [r for r in without if not r["rule"].startswith(rs.DOCUMENTED_LEVEL_RULE)]
    assert len(it19) == len(without) - 1, "the documented-level row is not in source_artefacts.tsv"
    arms = {"it19_neither_row": it19, "p2_republication_only": without, "shipped_both_rows": full}
    res_arms = {}
    for name, arte in arms.items():
        rws = run(arte)
        res_arms[name] = {
            "rows": len(rws),
            "directed": sum(1 for x in rws if x["consistency"] in DIRECTED),
            "documented_level_waivers": sum(1 for x in rws if x.get("documented_level_waiver")),
            "abstained_republished_claim_level_not_carried":
                sum(1 for x in rws if x["abstention_class"] == "republished_claim_level_not_carried"),
            "abstained_group_record_mostly_outside_module_targets":
                sum(1 for x in rws if x["abstention_class"] == "group_record_mostly_outside_module_targets"),
        }

    before, after = run(without), run(full)
    assert len(before) == len(after), "the datum must not add or remove a row from the listing"
    pairs = list(zip(before, after))
    assert all(key(b) == key(af) for b, af in pairs), "the two runs do not list the same rows in the same order"

    changed = [(b, af) for b, af in pairs if b["consistency"] != af["consistency"]]
    rep = [x for x in after if x.get("claim_provenance")]
    res = {
        "what_this_is": "effect of the republication datum on the active path; one row per association, real catalogue",
        "arms": res_arms,
        "arms_note": ("`before`/`after` below isolate the P2 republication datum (both arms carry the P3 "
                      "documented-level row). `arms` separates the two: it19_neither_row is the state IT19 left."),
        "association_rows_total": len(after),
        "rows_unchanged_by_the_datum": len(after) - len(changed),
        "directed_rows_before": sum(1 for x in before if x["consistency"] in DIRECTED),
        "directed_rows_after": sum(1 for x in after if x["consistency"] in DIRECTED),
        "republished_rows": {
            "rows": len(rep),
            "original_record_resolved_through_an_identifier": sum(1 for x in rep if x["claim_provenance"]["original_record"]),
            "original_record_level_not_carried": sum(1 for x in rep if not x["claim_provenance"]["original_record"]),
            "resolved_and_still_directed": sum(1 for x in rep if x["claim_provenance"]["original_record"] and x["consistency"] in DIRECTED),
            "resolved_and_abstained_because_the_original_record_is_held_back":
                sum(1 for x in rep if x["claim_provenance"]["original_record"] and x["consistency"] not in DIRECTED
                    and x["abstention_class"] == "group_record_mostly_outside_module_targets"),
        },
        "rows_that_lost_a_direction": len(changed),
        "rows_that_gained_a_direction": sum(1 for b, af in changed if af["consistency"] in DIRECTED),
        "lost_by_abstention_class": dict(sorted(collections.Counter(af["abstention_class"] for b, af in changed).items())),
        "copies_no_longer_counted_as_distinct_support": sum(
            1 for x in rep if x["claim_provenance"]["original_record"] and x["consistency"] in DIRECTED),
        "note": ("a row never leaves the listing: it keeps its compound, its claim source, its action and its reason. "
                 "`lost a direction` means the row no longer asserts one, not that it was removed."),
    }

    # the price: for each (need, substance name) that had a directed row only through a republished copy
    directed_names = collections.defaultdict(set)
    for x in after:
        if x["consistency"] in DIRECTED:
            directed_names[x["need"]].add(cc._norm(x["compound"] or ""))
    orphan = sorted({(af["need"], af["target"], af["compound"]) for b, af in changed
                     if cc._norm(af["compound"] or "") not in directed_names[af["need"]]})
    res["lost_rows_whose_substance_name_keeps_no_directed_row_in_that_need"] = len(orphan)

    out = Path(a.out_dir)
    with open(out / "provenance_rows.tsv", "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(["need", "target", "catalogue_id", "compound", "link_source", "claim_source", "action_raw",
                    "target_level", "effective_target_level", "original_record", "consistency_before",
                    "consistency_after", "abstention_class_after"])
        for b, af in changed:
            p = af.get("claim_provenance") or {}
            w.writerow([af["need"], af["target"], af["catalogue_id"], af["compound"], af["link_source"].split()[0],
                        af.get("claim_source") or "", af["action_raw"] or "", af["target_level"],
                        af.get("effective_target_level") or "", p.get("original_record") or "",
                        b["consistency"], af["consistency"], af["abstention_class"] or ""])
    with open(out / "provenance_orphans.tsv", "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(["need", "target", "compound"])
        w.writerows(orphan)
    (out / "provenance_effect.json").write_text(json.dumps(res, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(res, indent=1, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
