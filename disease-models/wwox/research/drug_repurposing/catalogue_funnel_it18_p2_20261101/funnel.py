#!/usr/bin/env python3
"""IT18 P2 catalogue funnel: source records -> identity-reconciled compounds -> compounds the matching method can use ->
compounds evaluated in a card / ranking unit -> comparable hypotheses, from the files committed today.

No new rule is written here: families are `repurposing_search.families` (the module's identity rule), the wide usability rule is
`usable_census.row_usability` (IT7 M-net), the matching-method rule is the one of `evaluation_it17_p3_20261101/direction_task.py`
and the IT18 P4 pre-registration (human ChEMBL curated mechanism with a determinate direction), exclusions are
`repurposing_search.artefact_reason`, need labels are `repurposing_search.associations_for_need`. This file only counts.

  funnel.py run [--out DIR]     writes funnel.tsv and funnel_reasons.tsv (offline, deterministic, a few seconds)
  funnel.py --help
"""
from __future__ import annotations

import argparse
import collections
import csv
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DR = HERE.parent
REPO = HERE.parents[4]
sys.path.insert(0, str(REPO / "framework/scripts"))
sys.path.insert(0, str(DR / "usable_compounds_it7_p2_20261029"))
sys.path.insert(0, str(DR / "evaluation_it17_p3_20261101"))

CHEMBL_ORIGINS = ("chembl_selected", "chembl_parent_added")


def tsv(path: Path) -> list[dict]:
    with open(path, encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def run(out: Path) -> int:
    import compound_catalog as cc
    import repurposing_search as rs
    from usable_census import row_usability
    from direction_task import chembl_class

    cat = DR / "catalog/catalog.jsonl.gz"
    entries = cc.load(cat)
    idx = rs.Index(entries, rs.load_artefacts())
    fam = idx.family
    by_fam = collections.defaultdict(list)
    for e in entries:
        by_fam[fam[e["id"]]].append(e)
    steps, reasons = [], []

    def step(sid, name, unit, n, denom, rule, src):
        steps.append({"step": sid, "name": name, "unit": unit, "count": n, "of": denom, "rule": rule, "computed_from": src})

    def why(sid, reason, category, unit, n, note=""):
        reasons.append({"step": sid, "reason": reason, "category": category, "unit": unit, "count": n, "note": note})

    # S0 records
    step("S0", "source records", "catalogue record", len(entries), "", "one line of catalog.jsonl.gz (a salt, a stereoisomer and a source-only row each count once)", "catalog.jsonl.gz")
    for o, n in sorted(collections.Counter(e["origin"] for e in entries).items()):
        why("S0", f"origin {o}", "composition", "catalogue record", n)
    stats = json.loads((DR / "catalog/catalog_stats.json").read_text(encoding="utf-8"))
    for src, v in sorted(stats["source_verification"].items()):
        bad = v.get("last_attempt_status") != "OK" or not v.get("complete_and_coherent") or v.get("problems")
        why("S0", f"source {src} ({v.get('version')}): fetch {v.get('last_attempt_status')}, complete_and_coherent {v.get('complete_and_coherent')}",
            "error" if bad else "source_state", "source", 1)
    why("S0", "DGIdb rows come from the export of 2024-06-10 (ChEMBL 33 claims) beside ChEMBL_37: newer DGIdb content not queried",
        "incomplete_query", "source", 1, "catalog_stats.json dgidb_age")
    d = stats["dsld"]
    why("S0", "DSLD bulk supplement probe interrupted: planned names not probed (access field only, no effect on S1-S4)",
        "incomplete_query", "name string", d["bulk_list_planned_names"] - d["bulk_list_probed"], f"probe errors {d['probes_error']}")

    # S1 identity-reconciled compounds
    resolved = {f for f, ms in by_fam.items() if any(m["origin"] in CHEMBL_ORIGINS for m in ms)}
    unresolved = set(by_fam) - resolved
    step("S1", "identity-reconciled compounds", "family", len(resolved), len(by_fam),
         "family (repurposing_search.families: ChEMBL parent/child or InChIKey connectivity layer, plus source-only records merged by a GtoPdb ligand -> ChEMBL identifier chain) containing at least one ChEMBL record",
         "catalog.jsonl.gz")
    joined = sum(1 for e in entries if (e.get("relations") or {}).get("family_join"))
    why("S1", "source-only records joined to a ChEMBL family by the GtoPdb ligand chain (counted inside S1)", "reconciled", "catalogue record", joined)
    chembl_names = set()
    for e in entries:
        if e["origin"] in CHEMBL_ORIGINS:
            for nm in [e["name"]] + (e.get("synonyms") or []):
                if nm:
                    chembl_names.add(nm.strip().lower())
    by_origin = collections.Counter(by_fam[f][0]["origin"] for f in unresolved)
    for o, n in sorted(by_origin.items()):
        why("S1", f"identity unresolved: source-only {o} record, no identifier or structure tying it to a ChEMBL record", "missing_data", "family", n)
    twins = sum(1 for f in unresolved if (by_fam[f][0]["name"] or "").strip().lower() in chembl_names)
    why("S1", "of the unresolved: name equals a ChEMBL name or synonym (possible duplicate, never merged on name)", "missing_data", "family", twins,
        "the same drug can therefore sit in S1 and among these; S1 plus unresolved is an upper bound of distinct compounds")
    recon = collections.Counter((r["decision"], r["reason"]) for r in tsv(DR / "catalog/ligand_reconciliation.tsv"))
    cls = {"merged": "reconciled", "out_of_selection": "no_result", "related_not_merged": "abstention_rule",
           "rejected_conflict": "abstention_rule"}
    for (d, r), n in sorted(recon.items()):
        c = cls.get(d, "missing_data")
        if d == "unresolved" and r in ("chembl_id_unknown_to_chembl_lookup", "ligand_id_absent_from_gtopdb_release"):
            c = "no_result"
        why("S1", f"GtoPdb ligand reconciliation {d}: {r}", c, "record-ligand pair", n, "ligand_reconciliation.tsv")

    # S2 matching-method usable (P4 / direction_task rule) and the wider IT7 M-net rule, both nested in S1
    stage = {}
    stage_why = collections.Counter()
    unsigned_actions = collections.Counter()
    excluded_reasons = collections.Counter()
    p4_fams, mnet_fams, mnet_corr = set(), set(), set()
    for f in resolved:
        best, best_note = 0, None
        for e in by_fam[f]:
            for t in e["targets"]:
                u = row_usability(rs, idx, e, t)
                if u["stated"] and not u["excluded"] and u["sign"] in ("up", "down") and u["stable"]:
                    mnet_fams.add(f)
                    if u["group"] in ("ChEMBL", "GtoPdb"):
                        mnet_corr.add(f)
                if t["source"] != "ChEMBL curated mechanism":
                    best = max(best, 1)
                    continue
                if t.get("organism") != "Homo sapiens":
                    best = max(best, 2)
                    continue
                excl = rs.artefact_reason(e, t, idx.artefacts, idx.early)
                if excl:
                    if best < 3:
                        best_note = excl.split(" (")[0]
                    best = max(best, 3)
                    continue
                if chembl_class(t.get("action_type")) is None:
                    if best < 4:
                        best_note = t.get("action_type") or "UNSTATED"
                    best = max(best, 4)
                    continue
                best = 5
        stage[f] = best
        if best == 5:
            p4_fams.add(f)
        elif best == 4:
            unsigned_actions[best_note] += 1
        elif best == 3:
            excluded_reasons[best_note] += 1
    has_rows = {f for f in resolved if any(e["targets"] for e in by_fam[f])}
    step("S2", "compounds usable by the matching method", "family", len(p4_fams), len(resolved),
         "S1 family with at least one ChEMBL curated mechanism on a Homo sapiens target whose action maps to INCREASE or DECREASE (direction_task.chembl_class; partial agonist, modulator, binding agent, etc. are direction-less) and is not excluded by source_artefacts.tsv",
         "catalog.jsonl.gz, coverage/source_artefacts.tsv")
    step("S2w", "wider rule, for comparison: IT7 M-net usable (any source, signed, human stable id)", "family", len(mnet_fams), len(resolved),
         "usable_census.row_usability over every row of the S1 family (ChEMBL, GtoPdb-via-DGIdb, other DGIdb claims taken at face value); not nested in S2", "catalog.jsonl.gz")
    step("S2w-c", "wider rule, corroborated (a ChEMBL or GtoPdb row among the usable rows)", "family", len(mnet_corr), len(resolved), "as S2w restricted to ChEMBL and GtoPdb groups", "catalog.jsonl.gz")
    labels = {0: ("no target row from any source", "missing_data"), 1: ("target rows only from DGIdb (no ChEMBL curated mechanism)", "missing_data"),
              2: ("ChEMBL mechanism only on non-human targets", "out_of_scope")}
    for k, (txt, c) in labels.items():
        why("S2", txt, c, "family", sum(1 for f in resolved if stage[f] == k))
    for r, n in sorted(excluded_reasons.items()):
        why("S2", f"human ChEMBL mechanism excluded by a source rule: {r}", "abstention_rule", "family", n)
    for a, n in sorted(unsigned_actions.items(), key=lambda x: (-x[1], x[0])):
        why("S2", f"human ChEMBL mechanism without a determinate direction: {a}", "abstention_rule", "family", n)
    prov = collections.Counter()
    for f in p4_fams:
        srcs = {t.get("claim_source") for e in by_fam[f] for t in e["targets"] if t["source"] == "DGIdb interaction"}
        gt = any(row_usability(rs, idx, e, t)["group"] == "GtoPdb" and rs.action_direction(t.get("interaction_type")) != "unresolved"
                 for e in by_fam[f] for t in e["targets"] if t["source"] == "DGIdb interaction")
        prov["gtopdb_signed"] += gt
        prov["chembl_copy"] += "ChEMBL" in srcs
        prov["chembl_only"] += not gt
    why("S2", "provenance: S2 families that also carry a signed GtoPdb row (a second curator; shares literature with ChEMBL)", "provenance", "family", prov["gtopdb_signed"])
    why("S2", "provenance: S2 families whose direction rests on ChEMBL alone (no signed GtoPdb row)", "provenance", "family", prov["chembl_only"])
    why("S2", "provenance: S2 families that also carry DGIdb rows whose claim source is ChEMBL (v33): a copy of the same curation, not a second vote", "provenance", "family", prov["chembl_copy"])
    assert len(resolved - has_rows) == sum(1 for f in resolved if stage[f] == 0)
    why("S2", "families outside S1 (identity unresolved) that the wider M-net rule would use: not counted, identity first",
        "abstention_rule", "family", sum(1 for f in unresolved if any(
            (lambda u: u["stated"] and not u["excluded"] and u["sign"] in ("up", "down") and u["stable"])(row_usability(rs, idx, e, t))
            for e in by_fam[f] for t in e["targets"])))

    # S3 evaluated in a card / ranking unit
    members = tsv(DR / "ranking_it8_p9_20261029/unit_members.tsv")
    unit_fams = {r["family_id"] for r in members if r["family_id"]}
    links = json.loads((DR / "catalog/card_links.json").read_text(encoding="utf-8"))
    card_fams = {fam[l["catalogue_id"]] for c in links["cards"].values() for l in c["links"] if l["catalogue_id"] in fam}
    missing_link_ids = sorted({l["catalogue_id"] for c in links["cards"].values() for l in c["links"] if l["catalogue_id"] not in fam})
    ev = unit_fams | card_fams
    internal = sorted(f for f in ev if f not in by_fam and f.startswith("INT:"))
    stale_ids = sorted(f for f in ev if f not in by_fam and not f.startswith("INT:"))
    ev_ok = ev & set(by_fam)
    step("S3", "compounds evaluated in a card or ranking unit", "family", len(ev_ok & p4_fams), len(p4_fams),
         "S2 family that is a member of a ranking unit (unit_members.tsv family_id) or linked to a curated card (card_links.json)",
         "ranking_it8_p9_20261029/unit_members.tsv, catalog/card_links.json")
    why("S3", "evaluated families in total (any stage), the union of the two consumers", "composition", "family", len(ev_ok))
    why("S3", "evaluated families that are ranking-unit members", "composition", "family", len(unit_fams & ev_ok))
    why("S3", "evaluated families that are card-linked", "composition", "family", len(card_fams & ev_ok))
    why("S3", "evaluated but identity unresolved (source-only family)", "missing_data", "family", len(ev_ok & unresolved))
    why("S3", "evaluated, identity resolved, but not usable by the matching method", "abstention_rule", "family", len((ev_ok & resolved) - p4_fams),
        "; ".join(sorted(f"{by_fam[f][0]['name'] or f}:{labels.get(stage[f], ('excluded or no direction',))[0] if stage[f] < 3 else ('excluded by a source rule' if stage[f] == 3 else 'no determinate direction')}" for f in (ev_ok & resolved) - p4_fams)))
    why("S3", "unit member that is a tool compound or precedent kept outside the catalogue by design (INT: id)", "out_of_scope", "unit member id", len(internal), "; ".join(internal))
    why("S3", "family id cited by a consumer but absent from the current catalogue", "error", "family", len(stale_ids) + len(missing_link_ids), "; ".join(stale_ids + missing_link_ids))
    no_identity_units = sorted({r["unit_id"] for r in members if not r["family_id"]} - {r["unit_id"] for r in members if r["family_id"]})
    kinds = collections.Counter(r["kind"] for r in members if r["unit_id"] in no_identity_units and not r["family_id"])
    for k, n in sorted(kinds.items()):
        why("S3", f"ranking unit with no catalogue identity, kind {k}", "out_of_scope", "ranking unit", n, "class, axis, modality, diet or tool not in the catalogue: no compound to count")
    step("S3u", "ranking units with at least one catalogue family", "ranking unit", len({r["unit_id"] for r in members if r["family_id"]}),
         len({r["unit_id"] for r in members}), "unit_members.tsv", "ranking_it8_p9_20261029/unit_members.tsv")

    # S4 comparable hypotheses
    un = tsv(DR / "ranking_it8_p9_20261029/unit_needs.tsv")
    det = [r for r in un if r["need_direction"] not in ("uncertain", "modulate")]
    comp = [r for r in det if any(k in json.loads(r["l2_states"] or "{}") for k in ("coherent", "opposed"))]
    step("S4", "comparable hypotheses (ranking)", "unit-need pair", len(comp), len(un),
         "unit_needs.tsv row whose need direction is determinate (down/up/restore) and where at least one member family has an L2 state coherent or opposed, i.e. a compatible/opposite comparison is possible",
         "ranking_it8_p9_20261029/unit_needs.tsv")
    why("S4", "unit-need pairs whose need direction is uncertain", "abstention_rule", "unit-need pair", len(un) - len(det))
    l2c = collections.Counter()
    for r in det:
        if r not in comp:
            st = json.loads(r["l2_states"] or "{}")
            l2c[",".join(sorted(st)) or "no catalogue family in the cell"] += 1
    for k, n in sorted(l2c.items()):
        why("S4", f"direction determinate, L2 never coherent/opposed: {k}", "abstention_rule" if k != "no catalogue family in the cell" else "missing_data", "unit-need pair", n)
    roles = rs.load_roles()
    pairs, pairs_any, need_dir = set(), set(), {}
    data = rs.load_needs()
    for n in data["needs"]:
        need_dir[n["id"]] = rs.need_direction(n)
        res = rs.associations_for_need(n, idx, roles)
        for a in res["associations"] if isinstance(res, dict) else res:
            if a["excluded_from_counts"] or a["target_kind"] not in rs.LINK_KINDS:
                continue
            f = fam[a["catalogue_id"]]
            if f not in resolved:
                continue
            pairs_any.add((f, n["id"]))
            if a["consistency"] in ("consistent", "opposed"):
                pairs.add((f, n["id"]))
    step("S4m", "comparable hypotheses (module need matching)", "family-need pair", len(pairs), len(pairs_any),
         "S1 family linked by identifier to an intervention target of a need (not excluded) whose module label is consistent or opposed (need direction determinate and a role row couples the target to the need)",
         "needs/needs.json, coverage/target_roles.tsv, catalog.jsonl.gz")
    why("S4m", "needs with a determinate direction", "composition", "need", sum(1 for v in need_dir.values() if v not in ("uncertain", "modulate")), f"of {len(need_dir)}")
    why("S4m", "family-need pairs on a determinate-direction need", "composition", "family-need pair", sum(1 for f, n in pairs_any if need_dir[n] not in ("uncertain", "modulate")))
    why("S4m", "of the comparable pairs, family also in S2", "composition", "family-need pair", sum(1 for f, n in pairs if f in p4_fams))

    out.mkdir(parents=True, exist_ok=True)
    for name, rows, cols in (("funnel.tsv", steps, ["step", "name", "unit", "count", "of", "rule", "computed_from"]),
                             ("funnel_reasons.tsv", reasons, ["step", "reason", "category", "unit", "count", "note"])):
        with open(out / name, "w", encoding="utf-8", newline="") as fh:
            w = csv.DictWriter(fh, cols, delimiter="\t", lineterminator="\n")
            w.writeheader()
            w.writerows(rows)
    for s in steps:
        print(f"{s['step']}\t{s['count']}\tof {s['of']}\t{s['unit']}\t{s['name']}")
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd")
    r = sub.add_parser("run")
    r.add_argument("--out", default=str(HERE))
    a = ap.parse_args(argv)
    if a.cmd != "run":
        ap.print_help()
        return 0
    return run(Path(a.out))


if __name__ == "__main__":
    sys.exit(main())
