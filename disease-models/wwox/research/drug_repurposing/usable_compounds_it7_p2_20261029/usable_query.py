#!/usr/bin/env python3
"""Bidirectional exploration of the compound catalogue by input need (IT7 P2). Read-only, offline, deterministic, standard library.

  usable_query.py need NEED-ID [--limit N] [--json]     need -> catalogue compounds on its targets, each with what M-net / M-sig can use
  usable_query.py genes SYMBOL[,SYMBOL...] [--limit N]   ad-hoc pathway (HGNC symbols) -> compounds, same columns
  usable_query.py compound NAME_OR_ID [--json]           compound -> the needs it touches AND the inputs each method would need
  usable_query.py needs                                  list the needs
  usable_query.py --help                                 this text, no work done

Flags are given per record AND rolled up per family (the census unit); M-sig state `?` = UNKNOWN, no structure key. direction = consistent/opposed only
where a role row couples the target to the need, else UNKNOWN.
Columns: signed-on-need-target = the link to THIS need's target states an up/down action; M-net(record) = the compound has a signed documented
action on a human target with a stable id ANYWHERE (not necessarily this need's target, so read the two together); M-sig-neural = a LINCS compound signature in an
iPSC-derived neural cell context; M-sig-any = a signature in any context (definitions: README.md of this directory).
It reads catalog.jsonl.gz, needs.json, target_roles.tsv and record_usability.tsv.gz and applies the catalogue's own link rules
(framework/scripts/repurposing_search.py). A usable flag is an input requirement, not a result: nothing here ranks or evaluates a
compound, a need with an uncertain direction yields an EXPLORATION list, and an empty answer means "no row in this catalogue",
never "no such compound". Access categories are US-listing evidence on a date (see counts.json), not availability or suitability.
"""
from __future__ import annotations

import argparse
import collections
import csv
import gzip
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[4]


def load_flags():
    out = {}
    with gzip.open(HERE / "record_usability.tsv.gz", "rt", encoding="utf-8") as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            out[r["record_id"]] = r
    return out


def tri(v):
    return {"1": "yes", "0": "no"}.get(v, "UNKNOWN(no structure key)")


def rollup(flags):
    """family id -> pooled flags over its records (the census unit is the family)."""
    out = {}
    for r in flags.values():
        o = out.setdefault(r["family_id"], {"records": 0, "net": 0, "sig_neural": 0, "sig_any": 0, "testable": 0})
        o["records"] += 1
        o["net"] |= r["Mnet_usable"] == "1"
        o["testable"] |= r["Msig_any_context"] != "UNKNOWN_NO_STRUCTURE_KEY"
        o["sig_neural"] |= r["Msig_neural_strict"] == "1"
        o["sig_any"] |= r["Msig_any_context"] == "1"
    return out


def roll_text(o):
    if not o:
        return "UNKNOWN"
    return (f"family roll-up ({o['records']} record(s)): M-net={'yes' if o['net'] else 'no'} "
            f"M-sig-neural={'yes' if o['sig_neural'] else ('no' if o['testable'] else 'UNKNOWN(no structure key in any member)')} "
            f"M-sig-any={'yes' if o['sig_any'] else ('no' if o['testable'] else 'UNKNOWN(no structure key in any member)')}")


def methods_text(f):
    if not f:
        return "UNKNOWN"
    return (f"record: M-net={tri(f['Mnet_usable'])}({f['Mnet_source_groups']}) "
            f"M-sig-neural={tri(f['Msig_neural_strict'])} M-sig-any={tri(f['Msig_any_context'])}")


def missing_inputs(f, entry):
    miss = {}
    if f["Mnet_usable"] != "1":
        if f["any_target_row"] != "1":
            miss["M-net"] = "no target row in any source used"
        elif f["stated_action"] != "1":
            miss["M-net"] = "target rows exist but none states an action that passes the catalogue artefact rules"
        else:
            miss["M-net"] = "a stated action exists but none is signed (up/down) on a human target with a stable id"
    if f["Msig_any_context"] == "UNKNOWN_NO_STRUCTURE_KEY":
        miss["M-sig"] = "UNKNOWN: no structure key in this record, cannot be matched to LINCS (not a negative)"
    elif f["Msig_any_context"] != "1":
        miss["M-sig"] = "no LINCS compound signature for this connectivity layer in GSE92742 or GSE70138"
    elif f["Msig_neural_strict"] != "1":
        miss["M-sig-neural"] = "signatures exist only outside the neural-lineage cell ids (NPC*, NEU*, MNEU.E)"
    return miss


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0], epilog=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd")
    n = sub.add_parser("need")
    n.add_argument("need_id")
    n.add_argument("--limit", type=int, default=40)
    n.add_argument("--json", action="store_true")
    g = sub.add_parser("genes")
    g.add_argument("symbols")
    g.add_argument("--limit", type=int, default=40)
    c = sub.add_parser("compound")
    c.add_argument("query")
    c.add_argument("--json", action="store_true")
    sub.add_parser("needs")
    a = ap.parse_args(argv)
    if not a.cmd:
        ap.print_help()
        return 0
    sys.path.insert(0, str(REPO / "framework/scripts"))
    import compound_catalog as cc
    import repurposing_search as rs
    needs = rs.load_needs()["needs"]
    if a.cmd == "needs":
        for x in needs:
            d = x["intervention_direction"]["direction"]
            print(f"{x['id']}\t{d}\t{'EXPLORATION' if d in ('uncertain', 'modulate') else 'direction-evaluable'}\t{len(x['targets'])} targets")
        return 0
    entries = cc.load()
    idx, roles = rs.Index(entries, rs.load_artefacts()), rs.load_roles()
    flags = load_flags()
    roll = rollup(flags)
    if a.cmd in ("need", "genes"):
        if a.cmd == "need":
            need = next((x for x in needs if x["id"] == a.need_id), None)
            if need is None:
                print(f"unknown need {a.need_id}", file=sys.stderr)
                return 2
        else:
            syms = [s.strip().upper() for s in a.symbols.split(",") if s.strip()]
            hg = {}
            for e in entries:
                for t in e["targets"]:
                    if t["source"] == "DGIdb interaction" and (t.get("gene") or "").upper() in syms and t.get("gene_concept_id"):
                        hg[t["gene"].upper()] = t["gene_concept_id"]
            need = {"id": "AD-HOC-GENES", "label": "ad-hoc gene list " + ",".join(syms), "intervention_direction": {"direction": "uncertain"},
                    "targets": [{"symbol": s, "hgnc_id": hg.get(s, ""), "target_kind": "intervention_target"} for s in syms]}
        r = rs.associations_for_need(need, idx, roles)
        kept = [x for x in r["associations"] if not x["excluded_from_counts"] and x["target_kind"] in rs.LINK_KINDS]
        recs = collections.OrderedDict()
        for x in kept:
            recs.setdefault(x["catalogue_id"], []).append(x)
        rows = []
        for cid in sorted(recs):
            f = flags.get(cid)
            xs = recs[cid]
            labs = {x["consistency"] for x in xs}
            direction = "/".join(sorted(l for l in labs if l in ("consistent", "opposed"))) or "UNKNOWN"
            fr = roll.get(xs[0]["family"])
            rows.append({"direction_vs_need": direction, "family_Mnet_usable": bool(fr and fr["net"]), "family_Msig_neural": bool(fr and fr["sig_neural"]),
                         "family_Msig_unknown_no_key": bool(fr and not fr["testable"]), "catalogue_id": cid, "name": xs[0]["compound"], "family": xs[0]["family"],
                         "targets": sorted({f"{x['target']}:{x['action_raw'] or 'UNSTATED'}" for x in xs}),
                         "signed_on_this_need_target": any(x["action_on_target"] in ("up", "down") for x in xs),
                         "Mnet_usable": bool(f and f["Mnet_usable"] == "1"), "Msig_neural": bool(f and f["Msig_neural_strict"] == "1"),
                         "Msig_any": bool(f and f["Msig_any_context"] == "1"), "Msig_state": tri(f["Msig_any_context"]) if f else "UNKNOWN"})
        head = {"need": r["need"], "label": r["label"], "need_direction": r["need_direction"], "exploration_only": r["exploration_only"],
                "records": len(rows), "families": len({x["family"] for x in rows}),
                "records_signed_on_this_need_target": sum(1 for x in rows if x["signed_on_this_need_target"]),
                "records_Mnet_usable": sum(1 for x in rows if x["Mnet_usable"]), "records_Msig_neural": sum(1 for x in rows if x["Msig_neural"]),
                "records_Msig_any": sum(1 for x in rows if x["Msig_any"]),
                "records_both_Mnet_and_Msig_neural": sum(1 for x in rows if x["Mnet_usable"] and x["Msig_neural"]),
                "records_Msig_UNKNOWN_no_structure_key": sum(1 for x in rows if x["Msig_state"].startswith("UNKNOWN")),
                "families_Mnet_usable_family_rollup": len({x["family"] for x in rows if x["family_Mnet_usable"]}),
                "families_Msig_neural_family_rollup": len({x["family"] for x in rows if x["family_Msig_neural"]}),
                "families_Msig_UNKNOWN_no_structure_key": len({x["family"] for x in rows if x["family_Msig_unknown_no_key"]}),
                "reading": "target association only (a documented link), not a directional prediction, not an observed effect, not a share of disease treated"}
        if getattr(a, "json", False):
            print(json.dumps({"summary": head, "rows": rows}, indent=1, ensure_ascii=False))
            return 0
        print("# " + json.dumps(head, ensure_ascii=False))
        if head["exploration_only"]:
            print("# EXPLORATION LIST: direction unresolved; this is not a list of favourable treatments")
        print(f"# showing {min(a.limit, len(rows))} of {len(rows)} linked records (sorted by catalogue id; raise --limit or use --json for all)")
        for x in rows[: a.limit]:
            print("\t".join([x["catalogue_id"], x["name"] or "-", ",".join(x["targets"][:4]), f"direction={x['direction_vs_need']}", f"signed-on-need-target={'Y' if x['signed_on_this_need_target'] else 'n'}", f"M-net(record)={'Y' if x['Mnet_usable'] else 'n'}",
                             f"M-sig-neural={'Y' if x['Msig_neural'] else 'n'}", f"M-sig-any={'Y' if x['Msig_any'] else ('?' if x['Msig_state'].startswith('UNKNOWN') else 'n')}",
                             f"family: M-net={'Y' if x['family_Mnet_usable'] else 'n'} M-sig-neural={'Y' if x['family_Msig_neural'] else ('?' if x['family_Msig_unknown_no_key'] else 'n')}"]))
        return 0
    if a.cmd == "compound":
        cands = rs.resolve_compound(idx, a.query)
        res = []
        for e in cands:
            f = flags.get(e["id"])
            res.append({"catalogue_id": e["id"], "name": e["name"], "family": idx.family[e["id"]], "status_class": e["status_class"], "access": e["access_categories"],
                        "usable_by": methods_text(f), "family_rollup": roll_text(roll.get(idx.family[e["id"]])), "missing_inputs": missing_inputs(f, e) if f else {"all": "UNKNOWN"},
                        "needs_touched": [x for x in rs.compound_to_needs(e, needs, idx, roles) if not x["excluded_from_counts"]]})
        if a.json:
            print(json.dumps(res, indent=1, ensure_ascii=False))
        else:
            print(f"{len(res)} catalogue record(s) match '{a.query}' (none is chosen for you)", file=sys.stderr)
            fams = sorted({r["family"] for r in res})
            for fid in fams:
                print(f"# {fid}: {roll_text(roll.get(fid))}")
            for r in res:
                print(f"## {r['catalogue_id']}\t{r['name']}\t{r['status_class']}\t{','.join(r['access'])}\t{r['family']}\t{r['usable_by']}")
                for k, v in sorted(r["missing_inputs"].items()):
                    print(f"   missing for {k}: {v}")
                for x in r["needs_touched"]:
                    print(f"   {x['need']}\t{x['target']}\t{x['action_raw'] or 'UNSTATED'}\t{x['consistency']}{' [exploration]' if x['exploration_only'] else ''}{' via ' + x['via_family_member'] if x['via_family_member'] else ''}")
        return 0 if res else 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
