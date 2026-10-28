#!/usr/bin/env python3
"""Search layer of the repurposing module: need -> targets -> catalogue compounds, and
compound -> targets -> needs (works for a compound with NO card). Read-only, offline, no LLM,
standard library only. Generic: it knows the needs/catalogue shapes, not the disease.

  repurposing_search.py need NEED-ID [--limit N] [--json]       compounds whose catalogued targets are the need's targets
  repurposing_search.py compound <name|id> [--json]              its targets -> the needs they touch, with direction consistency
  repurposing_search.py target SYMBOL [--limit N]                catalogue compounds on one target (human HGNC symbol)
  repurposing_search.py needs                                    list needs with direction and exploration label

Rules enforced here (each has a regression test in framework/scripts/test_repurposing_coverage.py):
  * a link exists only through an identifier: DGIdb by HGNC id, ChEMBL by human GENE_SYMBOL of the
    target component (never by alias: PDK1 is not PDPK1; non-human ChEMBL targets are kept apart);
  * an identity_guard target is reported as a guard hit, never as a link;
  * consistency with the need is `consistent` / `opposed` only when the need's direction is up or
    down AND an explicit role row gives the coupling between target activity and the need's quantity
    (target_roles.tsv); otherwise `direction_unresolved`. A need whose direction is `uncertain`
    yields an EXPLORATION list, labelled as such, never a list of favourable treatments;
  * no potency, score or probability is invented: reference ids and source statements are carried;
  * `no link found` is only meaningful with the sources' states beside it.
"""
from __future__ import annotations

import argparse
import collections
import csv
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import compound_catalog as cc  # noqa: E402

REPO = Path(__file__).resolve().parents[2]
DR = REPO / "disease-models/wwox/research/drug_repurposing"
DEFAULT_NEEDS = DR / "needs/needs.json"
DEFAULT_ROLES = DR / "coverage/target_roles.tsv"

DOWN = {"INHIBITOR", "ANTAGONIST", "BLOCKER", "NEGATIVE ALLOSTERIC MODULATOR", "NEGATIVE MODULATOR", "ANTISENSE INHIBITOR",
        "RNAI INHIBITOR", "INVERSE AGONIST", "DEGRADER", "ALLOSTERIC ANTAGONIST", "GENE EDITING NEGATIVE MODULATOR"}
UP = {"AGONIST", "PARTIAL AGONIST", "ACTIVATOR", "POSITIVE ALLOSTERIC MODULATOR", "POSITIVE MODULATOR", "OPENER", "POTENTIATOR", "EXOGENOUS GENE"}
LINK_KINDS = {"intervention_target", "disease_gene_product", "pathway_member", "effector_constraint"}
TARGET_KINDS_EVALUABLE = {"intervention_target", "disease_gene_product"}


def action_direction(text: str | None) -> str:
    """Effect on the TARGET's activity as the source states it: down | up | unresolved (None, MODULATOR, BINDING AGENT, ...)."""
    t = (text or "").strip().upper()
    if t in DOWN:
        return "down"
    if t in UP:
        return "up"
    return "unresolved"


def load_needs(path: Path = DEFAULT_NEEDS) -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def load_roles(path: Path = DEFAULT_ROLES) -> dict[tuple[str, str], dict]:
    out = {}
    p = Path(path)
    if p.exists():
        with open(p, encoding="utf-8", newline="") as fh:
            for r in csv.DictReader(fh, delimiter="\t"):
                out[(r["need_id"], r["symbol"].upper())] = r
    return out


class Index:
    """Symbol / HGNC-id -> catalogue target rows. Built once per run."""

    def __init__(self, entries: list[dict]):
        self.entries = entries
        self.by_id = {e["id"]: e for e in entries}
        self.chembl_human = collections.defaultdict(list)   # SYMBOL -> [(entry, target)]
        self.chembl_nonhuman = collections.defaultdict(list)
        self.dgidb = collections.defaultdict(list)          # 'hgnc:1234' -> [(entry, target)]
        for e in entries:
            for t in e["targets"]:
                if t["source"] == "ChEMBL curated mechanism":
                    bucket = self.chembl_human if t.get("organism") == "Homo sapiens" else self.chembl_nonhuman
                    for g in t.get("gene_symbols") or []:
                        bucket[g.upper()].append((e, t))
                elif t["source"] == "DGIdb interaction" and t.get("gene_concept_id"):
                    self.dgidb[t["gene_concept_id"].lower()].append((e, t))
        self.family = families(entries)
        self.members = collections.defaultdict(list)
        for e in entries:
            self.members[self.family[e["id"]]].append(e)


def families(entries: list[dict]) -> dict[str, str]:
    """entry id -> family id. ChEMBL records join by parent link or identical InChIKey first block (connectivity layer);
    every other record is its own family (identity unresolved, never merged on name)."""
    parent: dict[str, str] = {}

    def find(x):
        while parent.setdefault(x, x) != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    first = {}
    for e in entries:
        find(e["id"])
        p = (e.get("relations") or {}).get("parent")
        if p and p != e["id"]:
            parent[find(e["id"])] = find(p)
        sk = (e.get("ids") or {}).get("skeleton_key")
        if sk:
            if sk in first:
                parent[find(e["id"])] = find(first[sk])
            else:
                first[sk] = e["id"]
    roots = collections.defaultdict(list)
    for e in entries:
        roots[find(e["id"])].append(e["id"])
    return {i: "FAM:" + min(m) for m in roots.values() for i in m}


def need_direction(need: dict) -> str:
    return need["intervention_direction"]["direction"]


def consistency(need: dict, target: dict, action_dir: str, roles: dict) -> tuple[str, str]:
    """(label, why). Labels: consistent | opposed | direction_unresolved | not_evaluable."""
    nd = need_direction(need)
    if nd in ("uncertain", "modulate"):
        return "direction_unresolved", f"the need's direction is '{nd}': exploration only"
    if target["target_kind"] not in TARGET_KINDS_EVALUABLE:
        return "not_evaluable", f"target kind '{target['target_kind']}' is not an intervention target of this need"
    if action_dir == "unresolved":
        return "direction_unresolved", "the source states no up/down action (modulator, binder, unstated or enzyme-type)"
    role = roles.get((need["id"], target["symbol"].upper()))
    if role is None:
        return "direction_unresolved", "no explicit role row couples this target's activity to the need's quantity (target_roles.tsv)"
    coupling = role["coupling"]
    want = {"up": "up", "down": "down", "restore": "up"}[nd]
    if coupling == "opposite":
        want = "down" if want == "up" else "up"
    if action_dir == want:
        return "consistent", f"{action_dir} on {target['symbol']} with coupling '{coupling}' toward need direction '{nd}'"
    return "opposed", f"{action_dir} on {target['symbol']} with coupling '{coupling}' against need direction '{nd}'"


def links_for_target(idx: Index, tgt: dict) -> tuple[list, list, list]:
    """(chembl human rows, dgidb rows, non-human chembl rows) for one need target. HGNC id for DGIdb, symbol for ChEMBL."""
    sym = tgt["symbol"].upper()
    h = tgt.get("hgnc_id", "").lower()
    return idx.chembl_human.get(sym, []), idx.dgidb.get(h, []), idx.chembl_nonhuman.get(sym, [])


def associations_for_need(need: dict, idx: Index, roles: dict) -> dict:
    nd = need_direction(need)
    assoc, guards, nonhuman = [], [], 0
    for tgt in need["targets"]:
        ch, dg, nh = links_for_target(idx, tgt)
        nonhuman += len(nh)
        rows = [("ChEMBL curated mechanism", e, t) for e, t in ch] + [("DGIdb interaction", e, t) for e, t in dg]
        if tgt["target_kind"] == "identity_guard":
            guards += [{"target": tgt["symbol"], "catalogue_id": e["id"], "name": e["name"], "source": s} for s, e, _ in rows]
            continue
        for src, e, t in rows:
            raw = t.get("action_type") if src.startswith("ChEMBL") else t.get("interaction_type")
            ad = action_direction(raw)
            label, why = consistency(need, tgt, ad, roles)
            limits = []
            if src.startswith("ChEMBL") and t.get("target_type") not in (None, "SINGLE PROTEIN"):
                limits.append(f"ChEMBL target is a {t['target_type'].lower()}: the link to this gene is not subunit-specific")
            if src.startswith("DGIdb"):
                limits.append(f"DGIdb claim source {t.get('claim_source')}; export of 2024-06-10; interaction type {'stated' if raw else 'UNKNOWN'}")
                if not raw:
                    limits.append("interaction type unstated: the claim may be an expression, association or biomarker statement rather than a modulation")
                if t.get("multiplicity", 1) > 1:
                    limits.append(f"DGIdb group matched {t['multiplicity']} catalogue records")
            if tgt["target_kind"] == "readout_marker":
                limits.append("the gene is a readout marker of the need, not an intervention target")
            assoc.append({
                "need": need["id"], "target": tgt["symbol"], "hgnc_id": tgt.get("hgnc_id"), "target_kind": tgt["target_kind"],
                "catalogue_id": e["id"], "compound": e["name"], "family": idx.family[e["id"]],
                "link_source": src, "action_raw": raw, "action_on_target": ad,
                "need_direction": nd, "consistency": label, "consistency_why": why,
                "list_label": "exploration list: the need's direction is unresolved; this is not a list of favourable treatments" if nd in ("uncertain", "modulate") else "direction-evaluable need",
                "reference_ids": t.get("reference_ids", []), "mechanism_of_action": t.get("mechanism_of_action"),
                "limits": limits,
                "pharmacology": {"status_class": e["status_class"], "potency": "NOT_CARRIED (catalogue holds ids and direction only)",
                                 "chembl_max_phase": next((s.get("max_phase") for s in e["status_records"] if s["source"] == "ChEMBL"), None)},
            })
    assoc.sort(key=lambda a: (a["target"], a["catalogue_id"], a["link_source"], a["action_raw"] or ""))
    return {"need": need["id"], "label": need["label"], "need_direction": nd,
            "exploration_only": nd in ("uncertain", "modulate"), "associations": assoc,
            "identity_guard_hits": guards, "nonhuman_chembl_rows_set_aside": nonhuman}


def resolve_compound(idx: Index, query: str) -> list[dict]:
    """Candidates for a name or id. Several records may match: all are returned, none is chosen."""
    q = query.strip()
    hits = cc.find(idx.entries, id=q) if (q.upper().startswith(("CHEMBL", "CAT:")) or q.upper().startswith("DB")) else []
    if not hits:
        hits = cc.find(idx.entries, name=q)
    exact = [e for e in hits if cc._norm(e["name"] or "") == cc._norm(q)]
    return exact or hits


def compound_to_needs(entry: dict, needs: list[dict], idx: Index, roles: dict, family: bool = True) -> list[dict]:
    """Needs touched by the entry's targets. With family=True the targets of the other records of its chemical family
    (salt/parent/stereo records) are included and marked `via` - mechanisms are often curated on one salt form only."""
    out = []
    pool = [(entry, t, None) for t in entry["targets"]]
    if family:
        pool += [(m, t, m["id"]) for m in idx.members[idx.family[entry["id"]]] if m["id"] != entry["id"] for t in m["targets"]]
    for need in needs:
        syms = {t["symbol"].upper(): t for t in need["targets"]}
        nd = need_direction(need)
        for _own, t, via in pool:
            if t["source"] == "ChEMBL curated mechanism":
                if t.get("organism") != "Homo sapiens":
                    continue
                keys = [g.upper() for g in t.get("gene_symbols") or []]
                raw = t.get("action_type")
            else:
                keys = []
                raw = t.get("interaction_type")
                for s, tg in syms.items():
                    if tg.get("hgnc_id", "").lower() == (t.get("gene_concept_id") or "").lower():
                        keys.append(s)
            for k in keys:
                tgt = syms.get(k)
                if not tgt or tgt["target_kind"] == "identity_guard":
                    continue
                ad = action_direction(raw)
                label, why = consistency(need, tgt, ad, roles)
                out.append({"need": need["id"], "target": tgt["symbol"], "target_kind": tgt["target_kind"], "link_source": t["source"],
                            "action_raw": raw, "action_on_target": ad, "need_direction": nd, "consistency": label, "consistency_why": why,
                            "exploration_only": nd in ("uncertain", "modulate"), "via_family_member": via})
    seen, uniq = set(), []
    for a in sorted(out, key=lambda a: (a["need"], a["target"], a["link_source"], a["action_raw"] or "", a["via_family_member"] or "")):
        k = (a["need"], a["target"], a["link_source"], a["action_raw"])
        if k not in seen:
            seen.add(k)
            uniq.append(a)
    return uniq


def source_states(catalog_dir: Path | None = None) -> dict:
    p = (catalog_dir or cc.DEFAULT_DIR) / "catalog_stats.json"
    s = json.loads(p.read_text())
    return {k: v.get("state") for k, v in s["sources"].items()} | {"_catalog_generated_utc": s.get("generated_utc")}


def _print_assoc(a: dict) -> str:
    return "\t".join([a["target"], a["catalogue_id"], a["compound"] or "-", a["link_source"].split()[0], a["action_raw"] or "UNSTATED", a["consistency"]])


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0], formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--catalog", type=Path, default=cc.DEFAULT_CATALOG)
    ap.add_argument("--needs", type=Path, default=DEFAULT_NEEDS)
    ap.add_argument("--roles", type=Path, default=DEFAULT_ROLES)
    sub = ap.add_subparsers(dest="cmd")
    n = sub.add_parser("need")
    n.add_argument("need_id")
    n.add_argument("--limit", type=int, default=30)
    n.add_argument("--json", action="store_true")
    c = sub.add_parser("compound")
    c.add_argument("query")
    c.add_argument("--json", action="store_true")
    t = sub.add_parser("target")
    t.add_argument("symbol")
    t.add_argument("--limit", type=int, default=30)
    sub.add_parser("needs")
    a = ap.parse_args(argv)
    if not a.cmd:
        ap.print_help()
        return 0
    needs = load_needs(a.needs)["needs"]
    if a.cmd == "needs":
        for x in needs:
            d = x["intervention_direction"]["direction"]
            print(f"{x['id']}\t{d}\t{'EXPLORATION' if d in ('uncertain', 'modulate') else 'direction-evaluable'}\t{len(x['targets'])} targets")
        return 0
    entries = cc.load(a.catalog)
    idx, roles = Index(entries), load_roles(a.roles)
    if a.cmd == "need":
        nd = next((x for x in needs if x["id"] == a.need_id), None)
        if nd is None:
            print(f"unknown need {a.need_id}", file=sys.stderr)
            return 2
        r = associations_for_need(nd, idx, roles)
        if a.json:
            print(json.dumps(r, indent=1, ensure_ascii=False))
            return 0
        print(f"# {r['need']} direction={r['need_direction']} {'EXPLORATION LIST (not favourable treatments)' if r['exploration_only'] else ''}")
        print(f"# associations={len(r['associations'])} compounds={len({x['catalogue_id'] for x in r['associations']})} families={len({x['family'] for x in r['associations']})} "
              f"identity_guard_hits={len(r['identity_guard_hits'])} nonhuman_chembl_set_aside={r['nonhuman_chembl_rows_set_aside']}")
        for x in r["associations"][: a.limit]:
            print(_print_assoc(x))
        return 0
    if a.cmd == "compound":
        cands = resolve_compound(idx, a.query)
        res = [{"catalogue_id": e["id"], "name": e["name"], "family": idx.family[e["id"]], "origin": e["origin"], "status_class": e["status_class"],
                "access": e["access_categories"], "n_target_rows": len(e["targets"]),
                "family_size": len(idx.members[idx.family[e["id"]]]),
                "needs_touched": compound_to_needs(e, needs, idx, roles)} for e in cands]
        if a.json:
            print(json.dumps(res, indent=1, ensure_ascii=False))
        else:
            print(f"{len(res)} catalogue record(s) match '{a.query}' (none is chosen for you)", file=sys.stderr)
            for r in res:
                print(f"## {r['catalogue_id']}\t{r['name']}\t{r['status_class']}\t{','.join(r['access'])}\ttarget rows={r['n_target_rows']}\t{r['family']}")
                for x in r["needs_touched"]:
                    print(f"   {x['need']}\t{x['target']}\t{x['action_raw'] or 'UNSTATED'}\t{x['consistency']}{' [exploration]' if x['exploration_only'] else ''}{' via ' + x['via_family_member'] if x['via_family_member'] else ''}")
        return 0 if res else 1
    if a.cmd == "target":
        rows = idx.chembl_human.get(a.symbol.upper(), [])
        print(f"{len(rows)} ChEMBL human mechanism rows; {len(idx.chembl_nonhuman.get(a.symbol.upper(), []))} non-human rows set aside (DGIdb needs the HGNC id: use a need)")
        for e, t in rows[: a.limit]:
            print(f"{e['id']}\t{e['name']}\t{t['action_type']}\t{t['target_id']}")
        return 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
