#!/usr/bin/env python3
"""Coverage matrix and research-priority layer of the repurposing module. Offline, deterministic,
no LLM, standard library only. One command regenerates everything:

  repurposing_coverage.py run [--out DIR]       coverage_matrix.json, priorities.json, coverage_summary.json,
                                                associations.jsonl.gz (default DIR: the WWOX coverage/ directory)
  repurposing_coverage.py check [--out DIR]     recompute and compare with the files on disk (exit 1 on drift)
  repurposing_coverage.py show NEED-ID          one need: levels, dispositions, exploration label

Inputs (read at run time, never copied): needs/needs.json, catalog/catalog.jsonl.gz (+ catalog_stats.json,
card_links.json), cards/*.card.json + *.packet.json, cards_early/*, join/measure_next.json, coverage/target_roles.tsv.

FOUR levels, never a score and never summed:
  L1 documented_link        the catalogue links a compound family to a target of the need (ChEMBL mechanism by human
                            gene symbol, DGIdb by HGNC id); readout-marker and identity-guard targets do not count
  L2 mechanistic_coherence  the stated action on an intervention target is direction-consistent with a need whose
                            direction is up/down and whose target coupling is explicit; never evaluated for an
                            `uncertain` need (that is an exploration list)
  L3 observed_effect        a card assertion (data, not inference) on the intervention reports a readout change; the
                            card is cited by the need; endpoint-level pertinence is NOT checked
  L4 observed_recovery_in_WWOX_system  a card assertion in a WWOX system whose bridge comparison is
                            OPPOSES_DISEASE_CHANGE (the module's own technical comparison: not efficacy)
Scopes stay visible: wwox_experimental | wwox_clinical_report | other_disease_precedent | unverified_hypothesis
(computational and other-WWOX-context scopes belong to the need's observations, not to a compound's assertions).

Units: a coverage statement counts compound FAMILIES (ChEMBL records joined by parent link or InChIKey connectivity block;
every source-only record is its own family, flagged as possibly duplicate when a name coincides, never merged). Each
(family, need) cell counts once however many targets, pathways or records produce it. Needs share targets (CACNA1G, ABAT),
so cell counts across needs are not independent; unions are reported next to them.
"""
from __future__ import annotations

import argparse
import collections
import csv
import gzip
import hashlib
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import compound_catalog as cc  # noqa: E402
import repurposing_search as rs  # noqa: E402

DR = rs.DR
COVERAGE = DR / "coverage"
SCHEMA = "legend.wwox.coverage/1"
EXPLORATION_NOTE = "exploration list: the need's direction is unresolved; entries are not favourable treatments"
DISPOSITIONS = {
    "consistent_mechanism_candidate": "direction-consistent action on an intervention target of a direction-evaluable need (a mechanism candidate, not a treatment)",
    "exploration_candidate": "a documented link to a need whose direction is unresolved (or an action with no stated sign): exploration only",
    "opposite_mechanism": "the stated action opposes the need's direction (and no consistent action is catalogued)",
    "not_relevant": "identity resolved and targets catalogued, none of them a target of this need",
    "insufficient_data": "a link or an intervention exists but the sign, the identity or the observation needed to decide is missing",
    "source_queried_without_result": "the sources were queried and returned no target or mechanism row for this record",
    "incomplete_or_failed_query": "a source is not in state OK (failed, truncated, stale or never fetched): this is NOT a negative",
}


# ----------------------------------------------------------------------------- cards
def _stem(ref: str) -> str:
    return re.sub(r"\s*\(.*?\)\s*$", "", ref).strip()


def assertion_scope(a: dict) -> str:
    ctx = a.get("context", {})
    dis = (ctx.get("disease_id") or "") + " " + (a.get("source") or "")
    if a.get("epistemic_status") != "DATO":
        return "unverified_hypothesis"
    if re.search(r"not WWOX|NOT WWOX", dis):
        return "other_disease_precedent"
    if not re.search(r"WWOX|Wwox|WOREE", dis):
        return "other_disease_precedent"
    blob = " ".join(str(ctx.get(k, "")) for k in ("species", "cell_type", "genotype", "disease_id")).lower()
    if any(w in blob for w in ("mouse", "murine", "organoid", "cell", "fibroblast", "fly", "drosophila")):
        return "wwox_experimental"
    return "wwox_clinical_report"


def load_cards(dr: Path = DR) -> dict[str, dict]:
    out = {}
    for sub in ("cards", "cards_early"):
        for pk in sorted((dr / sub).glob("*.packet.json")):
            stem = pk.name.split(".")[0]
            cd = pk.with_name(stem + ".card.json")
            if not cd.exists():
                continue
            p, c = json.loads(pk.read_text()), json.loads(cd.read_text())
            cmp_ = {x["assertion_id"]: x["status"] for x in c.get("comparisons", [])}
            ass = []
            for a in p.get("drug_assertions", []):
                ass.append({"id": a["id"], "direction": a.get("direction"), "epistemic_status": a.get("epistemic_status"),
                            "reading_depth": a.get("reading_depth"), "scope": assertion_scope(a), "comparison": cmp_.get(a["id"], "UNRESOLVED"),
                            "species": a.get("context", {}).get("species"), "disease_context": a.get("context", {}).get("disease_id"),
                            "source": a.get("source"), "receipt": a.get("receipt"), "endpoint": a.get("endpoint")})
            out[stem] = {"card_id": stem, "dir": sub, "candidate": p.get("candidate", {}), "route": p.get("route"), "assertions": ass,
                         "endpoint_pursued": (c.get("p4_fields") or {}).get("endpoint_pursued"), "next_step": c.get("next_step"),
                         "limits": c.get("limits", []), "is_axis": str(p.get("candidate", {}).get("id", "")).startswith("AXIS:") or "-AX-" in stem}
    return out


def card_attachments(card_links: Path, modalities: Path) -> tuple[dict, dict]:
    links = json.loads(Path(card_links).read_text())["cards"]
    att = {}
    for cid, v in links.items():
        att[cid] = [{"catalogue_id": l["catalogue_id"], "role": l.get("role") or "mentioned_in_text", "rule": l["rule"]} for l in v["links"] if l.get("catalogue_id")]
    mods = {}
    if Path(modalities).exists():
        with open(modalities, encoding="utf-8", newline="") as fh:
            for r in csv.DictReader(fh, delimiter="\t"):
                mods[r["card_id"]] = r["modality"]
    return att, mods


# ----------------------------------------------------------------------------- build
def build(needs_path=rs.DEFAULT_NEEDS, catalog_dir: Path = cc.DEFAULT_DIR, dr: Path = DR, roles_path=rs.DEFAULT_ROLES) -> dict:
    nd = rs.load_needs(needs_path)
    needs = nd["needs"]
    entries = cc.load(catalog_dir / "catalog.jsonl.gz")
    cstats = json.loads((catalog_dir / "catalog_stats.json").read_text())
    idx, roles = rs.Index(entries), rs.load_roles(roles_path)
    cards = load_cards(dr)
    att, mods = card_attachments(catalog_dir / "card_links.json", catalog_dir / "non_molecule_modalities.tsv")
    need_ids = {n["id"] for n in needs}
    stale_roles = sorted(f"{n}/{s}" for (n, s) in roles if n not in need_ids or s not in {t["symbol"].upper() for x in needs if x["id"] == n for t in x["targets"]})
    src = {k: v for k, v in cstats["sources"].items()}
    src_problem = sorted(k for k in ("chembl", "dgidb") if src.get(k, {}).get("state") != "OK")
    measure_next = json.loads((dr / "join/measure_next.json").read_text()) if (dr / "join/measure_next.json").exists() else []

    # need -> cards
    need_cards = {n["id"]: [c for c in (_stem(r) for r in n["sources"].get("cards", [])) if c in cards] for n in needs}
    missing_cards = sorted({_stem(r) for n in needs for r in n["sources"].get("cards", [])} - set(cards))

    # associations
    per_need = {n["id"]: rs.associations_for_need(n, idx, roles) for n in needs}
    assoc_all = [a for r in per_need.values() for a in r["associations"]]

    # rows: families touched by an association or a card attachment; card interventions without identity
    rows: dict[str, dict] = {}

    def row(fid: str) -> dict:
        if fid not in rows:
            mem = idx.members.get(fid.replace("FAM:", "FAM:"), [])
            rep = sorted(mem, key=lambda e: (not (e["relations"] or {}).get("is_parent", False), e["id"]))[0] if mem else None
            rows[fid] = {"row_id": fid, "kind": "molecule_family", "name": rep["name"] if rep else None, "representative": rep["id"] if rep else None,
                         "records": len(mem), "origin": sorted({e["origin"] for e in mem}), "cards": [], "modality": sorted({e["modality"] for e in mem}),
                         "status_class": sorted({e["status_class"] for e in mem}), "access_categories": sorted({c for e in mem for c in e["access_categories"]}),
                         "target_rows_total": sum(len(e["targets"]) for e in mem),
                         "chembl_mechanism_rows": sum(1 for e in mem for t in e["targets"] if t["source"] == "ChEMBL curated mechanism"),
                         "dgidb_rows": sum(1 for e in mem for t in e["targets"] if t["source"] == "DGIdb interaction")}
        return rows[fid]

    cell_assoc = collections.defaultdict(list)
    for a in assoc_all:
        cell_assoc[(a["family"], a["need"])].append(a)
        row(a["family"])
    card_rows = {}
    for cid, c in sorted(cards.items()):
        if c["is_axis"]:
            continue
        links = [l for l in att.get(cid, []) if l["role"] in ("identity", "named_member", "mentioned_in_text")]
        decl = [l for l in links if l["role"] in ("identity", "named_member")]
        use = decl or [l for l in links]  # declarations win; mentions only when nothing is declared
        if use and cid not in mods:
            card_rows[cid] = []
            for l in use:
                fid = idx.family[l["catalogue_id"]]
                row(fid)["cards"].append({"card_id": cid, "attachment": l["role"], "rule": l["rule"]})
                card_rows[cid].append((fid, l["role"]))
        else:
            rid = "INT:" + cid
            rows[rid] = {"row_id": rid, "kind": "non_molecule_intervention" if cid in mods else "intervention_without_catalogue_identity",
                         "name": c["candidate"].get("name"), "modality": mods.get(cid, "class_level_or_unmatched"),
                         "cards": [{"card_id": cid, "attachment": "own_identity", "rule": "the card is the intervention"}]}
            card_rows[cid] = [(rid, "own_identity")]

    # cells
    cells = {}
    need_by = {n["id"]: n for n in needs}

    def obs_for(rid, nid):
        out = []
        for cid, rl in card_rows.items():
            if nid not in [n for n, cs in need_cards.items() if cid in cs]:
                continue
            for (r, attach) in rl:
                if r == rid:
                    for a in cards[cid]["assertions"]:
                        out.append(dict(a, card_id=cid, attachment=attach))
        return out

    for rid, r in rows.items():
        for nid, need in need_by.items():
            assoc = cell_assoc.get((rid, nid), [])
            obs = obs_for(rid, nid)
            if not assoc and not obs and not (r["kind"] != "molecule_family" and any(rid == x[0] for cid in card_rows for x in card_rows[cid] if nid in [n for n, cs in need_cards.items() if cid in cs])):
                continue
            link = [a for a in assoc if a["target_kind"] in rs.LINK_KINDS]
            marker = [a for a in assoc if a["target_kind"] not in rs.LINK_KINDS]
            cons = [a for a in link if a["consistency"] == "consistent"]
            opp = [a for a in link if a["consistency"] == "opposed"]
            no_id = r["kind"] != "molecule_family"
            if no_id:
                L1 = {"state": "not_evaluable", "why": "no catalogue identity (non-molecule modality or class-level card): not zero, not a negative"}
                L2 = {"state": "not_evaluable", "why": L1["why"]}
            else:
                L1 = {"state": "documented" if link else ("source_incomplete" if src_problem else "none_found"),
                      "targets": sorted({a["target"] for a in link}), "link_sources": sorted({a["link_source"] for a in link}),
                      "associations": len(link), "readout_marker_only_links": len(marker) if not link else 0}
                if L1["state"] == "none_found":
                    L1["why"] = "ChEMBL mechanisms and DGIdb queried (both state OK); no row on this need's link targets"
                if nd_dir := rs.need_direction(need_by[nid]):
                    if nd_dir in ("uncertain", "modulate"):
                        L2 = {"state": "not_evaluable", "why": "need direction is 'uncertain': coherence cannot be evaluated; exploration only",
                              "actions_present": sorted({a["action_on_target"] for a in link})}
                    else:
                        L2 = {"state": "coherent" if cons else ("opposed" if opp else ("direction_unresolved" if link else "none")),
                              "consistent_associations": len(cons), "opposed_associations": len(opp),
                              "unresolved_associations": len([a for a in link if a["consistency"] in ("direction_unresolved", "not_evaluable")])}
            decl_obs = [o for o in obs if o["epistemic_status"] == "DATO"]
            changed = [o for o in decl_obs if o["direction"] in ("INCREASE", "DECREASE")]
            nulls = [o for o in decl_obs if o["direction"] == "NO_CHANGE"]
            L3 = {"state": "observed" if changed else ("measured_null_only" if nulls else ("inference_only" if obs else "none_in_cards")),
                  "assertions": len(changed), "measured_null_assertions": len(nulls), "inference_assertions": len([o for o in obs if o["epistemic_status"] != "DATO"]),
                  "by_scope": dict(collections.Counter(o["scope"] for o in changed)), "cards": sorted({o["card_id"] for o in obs}),
                  "assertion_ids": sorted(o["id"] for o in changed),
                  "pertinence": "card-level: the card is cited by the need; endpoint-level pertinence not checked",
                  "absence_note": "none_in_cards is not a negative: cards cover a few dozen interventions" if not obs else None}
            rec = [o for o in changed if o["scope"] in ("wwox_experimental", "wwox_clinical_report") and o["comparison"] == "OPPOSES_DISEASE_CHANGE"]
            L4 = {"state": "observed" if rec else "none_in_record", "assertions": len(rec), "by_scope": dict(collections.Counter(o["scope"] for o in rec)),
                  "assertion_ids": sorted(o["id"] for o in rec), "via_class_card": any(o["attachment"] != "identity" and o["attachment"] != "own_identity" for o in rec),
                  "definition": "WWOX-system assertion whose bridge comparison is OPPOSES_DISEASE_CHANGE on target, endpoint and context: a technical comparison, not efficacy or safety"}
            cells[(rid, nid)] = {"row_id": rid, "need": nid, "L1_documented_link": L1, "L2_mechanistic_coherence": L2, "L3_observed_effect": L3,
                                 "L4_observed_recovery_in_wwox_system": L4, "exploration_only": rs.need_direction(need_by[nid]) in ("uncertain", "modulate")}

    # possible duplicates: source-only rows whose normalised name equals a record of another family
    byname = collections.defaultdict(set)
    for e in entries:
        for nm in [e["name"]] + e["synonyms"][:5]:
            if nm:
                byname[cc._norm(nm)].add(idx.family[e["id"]])
    for rid, r in rows.items():
        if r["kind"] == "molecule_family" and r["name"]:
            others = sorted(byname.get(cc._norm(r["name"]), set()) - {rid})
            r["possible_duplicate_families_by_name_not_merged"] = others[:6]
            r["n_possible_duplicates"] = len(others)
            r["name_is_source_artifact"] = r["name"].strip().lower() in ("null", "none", "unknown", "")

    # name-prefix siblings (salt/form records of "the same substance" that are separate families): a HINT for review, never evidence, never merged
    for (rid, nid), c in cells.items():
        r = rows[rid]
        if r["kind"] == "molecule_family" and c["L1_documented_link"]["state"] != "documented" and r["name"] and not r.get("name_is_source_artifact"):
            pre = cc._norm(r["name"]).split(" ")[0]
            sib = sorted(o for o, ro in rows.items() if o != rid and ro["kind"] == "molecule_family" and ro["name"] and cc._norm(ro["name"]).split(" ")[0] == pre
                         and (o, nid) in cells and cells[(o, nid)]["L1_documented_link"]["state"] == "documented")
            if sib:
                c["L1_documented_link"]["name_prefix_sibling_families_with_link_HINT_not_evidence"] = sib[:5]
    priorities = make_priorities(rows, cells, need_by, cards, card_rows, need_cards, src, src_problem, measure_next, idx)
    summary = make_summary(entries, idx, rows, cells, per_need, priorities, need_by, cards, card_rows, need_cards, src, cstats, stale_roles, missing_cards, assoc_all)
    matrix = {"schema": SCHEMA, "generated_from": inputs_digest(needs_path, catalog_dir, dr, roles_path),
              "levels": {"L1_documented_link": "catalogue link to a target of the need", "L2_mechanistic_coherence": "direction-consistent action, only for direction-evaluable needs with an explicit role row",
                         "L3_observed_effect": "card assertion reports a readout change (card-level pertinence)", "L4_observed_recovery_in_wwox_system": "WWOX-system assertion with bridge comparison OPPOSES_DISEASE_CHANGE"},
              "never_summed": True, "unit": "rows are compound FAMILIES or card interventions; a cell counts once per (row, need)",
              "need_directions": {n["id"]: rs.need_direction(n) for n in needs},
              "exploration_needs": sorted(n["id"] for n in needs if rs.need_direction(n) in ("uncertain", "modulate")),
              "rows": [rows[k] for k in sorted(rows)], "cells": [cells[k] for k in sorted(cells)]}
    return {"matrix": matrix, "priorities": priorities, "summary": summary, "associations": assoc_all}


def inputs_digest(needs_path, catalog_dir, dr, roles_path) -> dict:
    def h(p):
        p = Path(p)
        return hashlib.sha256(p.read_bytes()).hexdigest()[:16] if p.exists() else "ABSENT"
    cards = hashlib.sha256(b"".join(f.read_bytes() for sub in ("cards", "cards_early") for f in sorted((dr / sub).glob("*.json")))).hexdigest()[:16]
    return {"needs.json": h(needs_path), "catalog.jsonl.gz": h(catalog_dir / "catalog.jsonl.gz"), "catalog_stats.json": h(catalog_dir / "catalog_stats.json"),
            "card_links.json": h(catalog_dir / "card_links.json"), "target_roles.tsv": h(roles_path), "cards_and_packets": cards, "measure_next.json": h(dr / "join/measure_next.json")}


# ----------------------------------------------------------------------------- priorities
def make_priorities(rows, cells, need_by, cards, card_rows, need_cards, src, src_problem, measure_next, idx) -> dict:
    out, skipped = [], collections.Counter()
    for (rid, nid), c in sorted(cells.items()):
        r, need = rows[rid], need_by[nid]
        card_ids = sorted({x["card_id"] for x in r["cards"]})
        interesting = bool(card_ids) or c["L2_mechanistic_coherence"]["state"] == "coherent" or (r["kind"] == "molecule_family" and
                                                                                                     ("approved_any_source" in r["status_class"] or {"prescription", "OTC", "supplement"} & set(r["access_categories"])))
        if not interesting:
            skipped["not_prioritised_no_card_no_coherence_no_approval_or_access"] += 1
            continue
        L1, L2, L3, L4 = (c[k] for k in ("L1_documented_link", "L2_mechanistic_coherence", "L3_observed_effect", "L4_observed_recovery_in_wwox_system"))
        nd = rs.need_direction(need)
        if src_problem:
            disp, why = "incomplete_or_failed_query", f"catalogue source(s) {src_problem} not in state OK"
        elif r["kind"] != "molecule_family":
            disp, why = "insufficient_data", "no catalogue identity (non-molecule modality or class-level card): links to targets cannot be evaluated"
        elif L1["state"] == "documented":
            if L2.get("state") == "coherent":
                disp, why = "consistent_mechanism_candidate", "direction-consistent action on an intervention target with explicit coupling"
            elif L2.get("state") == "opposed":
                disp, why = "opposite_mechanism", "the stated action opposes the need's direction; no consistent action catalogued"
            elif nd in ("uncertain", "modulate"):
                disp, why = "exploration_candidate", EXPLORATION_NOTE
            else:
                disp, why = "insufficient_data", "link documented but no stated up/down action or no coupling row"
        elif r["target_rows_total"] == 0:
            disp, why = "source_queried_without_result", "ChEMBL mechanism and DGIdb queried; no target row for any record of this family"
            if L1.get("name_prefix_sibling_families_with_link_HINT_not_evidence"):
                why += "; other records with the same leading name word do link (salt/form families, separate identities, review hint only)"
        else:
            disp, why = "not_relevant", "by catalogued targets only: this family has target rows and none is a link target of this need"
            if card_ids:
                why += "; a card cites it for this need through a mechanism the catalogue does not describe as a target (the card's rationale is not overridden)"
            if L1.get("name_prefix_sibling_families_with_link_HINT_not_evidence"):
                why += "; other records with the same leading name word do link (salt/form families, separate identities, review hint only)"
        crs = [cards[c_] for c_ in card_ids]
        assertions = [a for c_ in crs for a in c_["assertions"]]
        independent = len({a["source"] for a in assertions if a["source"]})
        mn = [m for m in measure_next]  # pointer only; per-card query ids are not recorded in measure_next
        out.append({
            "row_id": rid, "name": r["name"], "kind": r["kind"], "need": nid, "need_direction": nd,
            "exploration_only": nd in ("uncertain", "modulate"), "disposition": disp, "disposition_reason": why,
            "levels": {k: c[k].get("state") for k in ("L1_documented_link", "L2_mechanistic_coherence", "L3_observed_effect", "L4_observed_recovery_in_wwox_system")},
            "criteria": {
                "wwox_relevance": {"need_evidence_scopes": need["evidence_scope"], "n_wwox_system_observations_in_need": sum(1 for o in need["observed"] if o["evidence_scope"] == "WWOX_EXPERIMENT_IN_DEE_SYSTEM"),
                                   "intervention_assertion_scopes": L3["by_scope"] or {}},
                "direction_mechanism": {"L2": L2.get("state"), "targets": L1.get("targets", []), "link_sources": L1.get("link_sources", [])},
                "evidence_quality_independence": {"card_assertions": len(assertions), "reading_depths": dict(collections.Counter(a["reading_depth"] for a in assertions)),
                                                  "distinct_source_strings": independent, "note": "shared sources are not independent confirmations; nothing is pooled"},
                "counter_evidence": {"need_counter_evidence_items": len(need["counter_evidence"]), "intervention_measured_null_assertions": L3["measured_null_assertions"]},
                "potency_and_assay_context": "NOT_CARRIED: the catalogue holds no potency; card measured-result notes are free text in the cards",
                "transferability": {"species_of_assertions": sorted({a["species"] for a in assertions if a["species"]}), "scopes": sorted({a["scope"] for a in assertions}),
                                    "system_of_interest": "WWOX-DEE reference genotype class; transfer is a stated distance, not a score"},
                "pharmacology_safety_info": {"status_class": r.get("status_class"), "access_categories": r.get("access_categories"),
                                             "safety_assessment": "NOT_ASSESSED (catalogue); safety triage is a separate step"},
                "discriminating_experiment": {"card_endpoint_pursued": [c_["endpoint_pursued"] for c_ in crs if c_["endpoint_pursued"]][:1],
                                              "exists": any(c_["endpoint_pursued"] for c_ in crs)},
            },
            "next_deepening": deepening(disp, c, nd, crs),
            "possible_duplicates_not_merged": r.get("n_possible_duplicates", 0),
            "reversible": "a disposition is a function of the inputs; change a role row, a card or the catalogue and regenerate",
        })
    return {"schema": SCHEMA, "dispositions": DISPOSITIONS, "ranking": "none: no score, no ordering by evidence volume; filter by disposition, need or criterion. Order is need id then row id.",
            "no_probability": "nothing here is a probability of benefit or cure", "priorities": out, "pairs_not_prioritised": dict(skipped)}


def deepening(disp, c, nd, crs) -> list[str]:
    d = []
    if nd in ("uncertain", "modulate"):
        d.append("resolve the sign of the need before reading any mechanism as supportive")
    if c["L4_observed_recovery_in_wwox_system"]["state"] != "observed":
        d.append("no WWOX-system observation recorded: a discriminating measurement in a WWOX-deficient system is the missing step")
    if disp in ("consistent_mechanism_candidate", "exploration_candidate"):
        d.append("fitted potency and selectivity on the linked target (not carried by the catalogue)")
    if disp == "not_relevant":
        d.append("none for this need; the compound may belong to other needs")
    if disp == "source_queried_without_result":
        d.append("identify the targets by another source before deciding")
    for c_ in crs:
        if c_["endpoint_pursued"]:
            d.append("card endpoint: " + c_["endpoint_pursued"][:200])
            break
    return d


# ----------------------------------------------------------------------------- summary
def collapsed_count(fams, rows) -> int:
    """Lower bound if families sharing a normalised name were one substance. A sensitivity figure, never used for coverage."""
    seen = set()
    for f in sorted(fams):
        r = rows.get(f)
        seen.add(cc._norm(r["name"]) if r and r.get("name") else f)
    return len(seen)


def pct(num, den, what) -> dict:
    return {"numerator": num, "denominator": den, "percent": round(100.0 * num / den, 1) if den else None, "what": what}


def make_summary(entries, idx, rows, cells, per_need, priorities, need_by, cards, card_rows, need_cards, src, cstats, stale_roles, missing_cards, assoc_all) -> dict:
    fam_all = set(idx.family.values())
    chembl_fams = {idx.family[e["id"]] for e in entries if e["origin"].startswith("chembl")}
    source_only = len(fam_all - chembl_fams)
    link_assoc = [a for a in assoc_all if a["target_kind"] in rs.LINK_KINDS]
    touched_rec = {a["catalogue_id"] for a in link_assoc}
    touched_fam = {a["family"] for a in link_assoc}
    marker_rec = {a["catalogue_id"] for a in assoc_all if a["target_kind"] not in rs.LINK_KINDS}
    recs_with_targets = sum(1 for e in entries if e["targets"])
    lv = lambda key, st: sum(1 for c in cells.values() if c[key]["state"] == st)
    per = {}
    for nid, n in need_by.items():
        a = [x for x in per_need[nid]["associations"] if x["target_kind"] in rs.LINK_KINDS]
        cs = [c for (r, k), c in cells.items() if k == nid]
        per[nid] = {"direction": rs.need_direction(n), "exploration_only": rs.need_direction(n) in ("uncertain", "modulate"),
                    "targets": len(n["targets"]), "link_targets": sum(1 for t in n["targets"] if t["target_kind"] in rs.LINK_KINDS),
                    "records_with_documented_link": len({x["catalogue_id"] for x in a}), "families_with_documented_link": len({x["family"] for x in a}),
                    "families_consistent": len({x["family"] for x in a if x["consistency"] == "consistent"}),
                    "families_opposed": len({x["family"] for x in a if x["consistency"] == "opposed"}),
                    "readout_marker_only_records": len({x["catalogue_id"] for x in per_need[nid]["associations"] if x["target_kind"] not in rs.LINK_KINDS} - {x["catalogue_id"] for x in a}),
                    "identity_guard_hits": len(per_need[nid]["identity_guard_hits"]), "nonhuman_chembl_rows_set_aside": per_need[nid]["nonhuman_chembl_rows_set_aside"],
                    "cells_L3_observed": sum(1 for c in cs if c["L3_observed_effect"]["state"] == "observed"),
                    "cells_L4_observed": sum(1 for c in cs if c["L4_observed_recovery_in_wwox_system"]["state"] == "observed"),
                    "cards_citing_need": need_cards[nid], "wwox_system_observations": sum(1 for o in n["observed"] if o["evidence_scope"] == "WWOX_EXPERIMENT_IN_DEE_SYSTEM")}
    fam_needs = collections.defaultdict(set)
    for a in link_assoc:
        fam_needs[a["family"]].add(a["need"])
    dist = collections.Counter(len(v) for v in fam_needs.values())
    all_assertions = {(cid, a["id"]): a for cid, c in cards.items() for a in c["assertions"]}
    obs_assertions = {(cid, a["id"]) for cid, c in cards.items() if not c["is_axis"] for a in c["assertions"]
                      if a["epistemic_status"] == "DATO" and a["direction"] in ("INCREASE", "DECREASE") and any(cid in v for v in need_cards.values())}
    rec_assertions = {k for k in obs_assertions if all_assertions[k]["scope"] in ("wwox_experimental", "wwox_clinical_report") and all_assertions[k]["comparison"] == "OPPOSES_DISEASE_CHANGE"}
    disp = collections.Counter(p["disposition"] for p in priorities["priorities"])
    n_cells_possible = len([r for r in rows.values()]) * len(need_by)
    return {
        "schema": SCHEMA,
        "units": {"catalogue_records": len(entries), "records_are": "source-level substance records, not distinct drugs",
                  "families": len(fam_all), "chembl_families": len(chembl_fams), "source_only_families_unresolved_identity": source_only,
                  "family_rule": "ChEMBL parent link or identical InChIKey connectivity block; source-only records stay singletons; nothing merged on name",
                  "coverage_unit": "compound families (each counted once per need); card interventions are separate rows"},
        "source_states": {k: v.get("state") for k, v in src.items()} | {"dgidb_note": "export of 2024-06-10; current service coverage not ingested"},
        "inputs_status": {"catalogue_sources_not_ok": sorted(k for k, v in src.items() if v.get("state") not in ("OK",)),
                          "stale_role_rows": stale_roles, "cards_cited_by_needs_but_missing": missing_cards},
        "needs": {"count": len(need_by), "direction_evaluable": sum(1 for n in need_by.values() if rs.need_direction(n) not in ("uncertain", "modulate")),
                  "exploration_only": sum(1 for n in need_by.values() if rs.need_direction(n) in ("uncertain", "modulate")),
                  "needs_without_any_link_target": sorted(k for k, v in per.items() if v["link_targets"] == 0),
                  "needs_with_documented_link_families": sum(1 for v in per.values() if v["families_with_documented_link"] > 0),
                  "per_need": per},
        "catalogue_coverage": {
            "records_examined": len(entries), "records_with_any_target_row": recs_with_targets,
            "records_with_documented_link_to_a_need": len(touched_rec), "families_with_documented_link_to_a_need": len(touched_fam),
            "records_touching_only_readout_markers": len(marker_rec - touched_rec),
            "pct_records_with_link": pct(len(touched_rec), len(entries), "catalogue records with at least one documented link to a link-type target of any of the needs / all catalogue records; links are source statements, not relevance"),
            "pct_records_with_target_row_that_link": pct(len(touched_rec), recs_with_targets, "records linked to some need / records carrying any target row"),
            "touched_families_with_a_name_twin_in_another_family_not_merged": sum(1 for f in touched_fam if rows.get(f, {}).get("n_possible_duplicates", 0) > 0),
            "families_touching_a_need_if_name_twins_were_collapsed_SENSITIVITY_ONLY": collapsed_count(touched_fam, rows),
            "families_by_number_of_needs_touched": {str(k): v for k, v in sorted(dist.items())},
            "families_touching_at_least_one_need_counted_once": len(touched_fam),
            "overlap_warning": "needs share targets (e.g. CACNA1G, ABAT); per-need family counts must not be added: use the union above"},
        "evaluated_vs_records": {"records_in_catalogue": len(entries), "records_examined_by_target_match": len(entries),
                                 "records_with_target_data_at_all": recs_with_targets, "records_with_a_link_to_a_need_target": len(touched_rec),
                                 "records_evaluated_against_wwox_needs_with_any_observation": len({a for a in {cid for cid, _ in obs_assertions}}),
                                 "meaning": "'examined' = target-matched against the 22 needs; 'evaluated with observation' = card interventions with at least one data assertion on a need citing the card"},
        "matrix": {"rows": len(rows), "row_kinds": dict(collections.Counter(r["kind"] for r in rows.values())), "cells_nonempty": len(cells),
                   "cells_possible_rows_x_needs": n_cells_possible,
                   "L1_documented": lv("L1_documented_link", "documented"), "L1_none_found": lv("L1_documented_link", "none_found"), "L1_not_evaluable": lv("L1_documented_link", "not_evaluable"),
                   "L2_coherent": lv("L2_mechanistic_coherence", "coherent"), "L2_opposed": lv("L2_mechanistic_coherence", "opposed"),
                   "L2_direction_unresolved": lv("L2_mechanistic_coherence", "direction_unresolved"), "L2_not_evaluable": lv("L2_mechanistic_coherence", "not_evaluable"),
                   "L3_observed": lv("L3_observed_effect", "observed"), "L3_measured_null_only": lv("L3_observed_effect", "measured_null_only"),
                   "L3_inference_only": lv("L3_observed_effect", "inference_only"), "L3_none_in_cards": lv("L3_observed_effect", "none_in_cards"),
                   "L4_observed": lv("L4_observed_recovery_in_wwox_system", "observed"),
                   "levels_are_never_summed": True},
        "observations": {"card_interventions": len([c for c in cards.values() if not c["is_axis"]]), "axis_cards_not_interventions": len([c for c in cards.values() if c["is_axis"]]),
                         "data_assertions_with_readout_change_on_cited_needs": len(obs_assertions), "of_which_wwox_system_opposing_disease_change": len(rec_assertions),
                         "by_scope": dict(collections.Counter(all_assertions[k]["scope"] for k in obs_assertions)),
                         "note": "an assertion counts once however many needs cite its card; L3/L4 cells count (row, need) pairs"},
        "priorities": {"records": len(priorities["priorities"]), "by_disposition": dict(sorted(disp.items())),
                       "all_dispositions_listed": sorted(DISPOSITIONS), "pairs_not_prioritised": priorities["pairs_not_prioritised"],
                       "exploration_flagged": sum(1 for p in priorities["priorities"] if p["exploration_only"])},
        "limits": ["catalogue links are source statements; no potency is carried", "DGIdb is the 2024-06-10 export", "ChEMBL non-human target rows are set aside, not matched",
                   "card pertinence to a need is card-level", "L4 is a technical bridge comparison, not efficacy", "needs' own WWOX observations are not interventions and fill no compound cell"],
    }


# ----------------------------------------------------------------------------- IO
def dump(obj, compact: bool = False) -> str:
    if compact:
        return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n"
    return json.dumps(obj, indent=1, ensure_ascii=False, sort_keys=True) + "\n"


def write_all(res: dict, out: Path) -> dict[str, str]:
    out.mkdir(parents=True, exist_ok=True)
    files = {"coverage_matrix.json": dump(res["matrix"], True), "priorities.json": dump(res["priorities"], True), "coverage_summary.json": dump(res["summary"])}
    for k, v in files.items():
        (out / k).write_text(v, encoding="utf-8")
    with gzip.GzipFile(out / "associations.jsonl.gz", "wb", mtime=0) as fh:
        for a in res["associations"]:
            fh.write((json.dumps(a, sort_keys=True, ensure_ascii=False) + "\n").encode())
    return {k: hashlib.sha256(v.encode()).hexdigest()[:16] for k, v in files.items()}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0], formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd")
    for name in ("run", "check"):
        p = sub.add_parser(name)
        p.add_argument("--out", type=Path, default=COVERAGE)
    s = sub.add_parser("show")
    s.add_argument("need_id")
    a = ap.parse_args(argv)
    if not a.cmd:
        ap.print_help()
        return 0
    res = build()
    if a.cmd == "run":
        h = write_all(res, a.out)
        sm = res["summary"]
        print(json.dumps({"files": h, "matrix": sm["matrix"], "priorities": sm["priorities"]["by_disposition"]}, indent=1))
        return 0
    if a.cmd == "check":
        want = {"coverage_matrix.json": dump(res["matrix"], True), "priorities.json": dump(res["priorities"], True), "coverage_summary.json": dump(res["summary"])}
        drift = [k for k, v in want.items() if not (a.out / k).exists() or (a.out / k).read_text(encoding="utf-8") != v]
        print("OK: files match a fresh regeneration" if not drift else "DRIFT: " + ", ".join(drift))
        return 1 if drift else 0
    if a.cmd == "show":
        pn = res["summary"]["needs"]["per_need"].get(a.need_id)
        if pn is None:
            print("unknown need", file=sys.stderr)
            return 2
        print(json.dumps(pn, indent=1))
        for p in res["priorities"]["priorities"]:
            if p["need"] == a.need_id:
                print(f"{p['disposition']}\t{p['row_id']}\t{p['name']}\t{p['levels']}{'  [EXPLORATION]' if p['exploration_only'] else ''}")
        return 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
