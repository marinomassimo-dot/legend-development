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
  L1 documented_link        (plain wording: TARGET LISTED; a stated action is a separate field, `action_stated`) the catalogue links a compound family to an INTERVENTION target (or disease gene product) of the need
                            (ChEMBL mechanism by human gene symbol, DGIdb by HGNC id). Pathway members are counted apart; effector
                            constraints and readout markers are listed beside and never links; source-artefact rows (source_artefacts.tsv),
                            alias-risk rows and the DGIdb placeholder 'Null' are excluded and listed
  L2 mechanistic_coherence  direction-consistent action on an intervention target, only for needs whose direction is up/down/restore AND
                            an explicit role row (target_roles.tsv, with its certainty qualifier); never for an `uncertain` need
  L3 observed_effect        an assertion on THIS compound whose endpoint is listed as pertinent to THIS need in assertion_pertinence.tsv:
                            a readout in a WWOX system or a WWOX case report, with its SIGN. Other-disease precedents, target-engagement
                            assays, safety signals and label statements are separate states, never 'observed'
  L4 observed_recovery      an L3 assertion whose bridge comparison is OPPOSES_DISEASE_CHANGE, reading depth known, one dose arm at a time;
                            experimental and case-level kept apart (a technical comparison, not efficacy)
Source states: OK | STALE_EXPORT (DGIdb 2024-06-10) | STALE_AFTER_FAILED_REFRESH | PARTIAL | FAILED | INCOMPLETE | NOT_FETCHED. A hard problem
of a source does NOT blank the module. Three things are kept apart: (1) positive evidence (a target listed, a consistent/opposed action, an
observation) stays what it is, because a working source supports it; (2) the search as a whole is flagged incomplete on every record
(`search_incompleteness`); (3) only an ABSENCE conclusion (no link found, no target row) that depends on the missing source becomes
incomplete_or_failed_query. A source's role decides whether it can touch an absence conclusion (SOURCE_ROLES): an error on an accessibility
source (openFDA NDC, DSLD) only caveats the access categories. A stale source caveats every absence-type result.
Concordant and opposed actions on one need are both kept (L2 `mixed_consistent_and_opposed`, never summed into one sign).
Observations against wild type only are not effects in the disease model: see observation_levels.

Units: a coverage statement counts compound FAMILIES (ChEMBL records joined by parent link or InChIKey connectivity block;
every source-only record is its own family unless a verified identifier chain joined it, flagged as possibly duplicate when a name coincides, never merged on name;
the one joining rule is relations.family_join, set by catalog_build.py for a `merged` gtopdb_ligand_chembl_ref reconciliation). Each
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
    "exploration_candidate": "a target listed for a need whose direction is unresolved (or an action with no stated sign): exploration only",
    "opposite_mechanism": "the stated action opposes the need's direction (and no consistent action is catalogued)",
    "mixed_consistent_and_opposed_actions": "the same family has BOTH a direction-consistent and an opposed action on this need; both are listed with target, action and source and no sign is summed: not a favourable profile",
    "no_catalogue_link_found": "identity resolved and targets catalogued, none an intervention target of this need (a statement about the catalogue and its possibly stale sources, not about relevance)",
    "insufficient_data": "a link or an intervention exists but the sign, the identity or the observation needed to decide is missing",
    "source_queried_without_result": "the sources were queried and returned no target or mechanism row for this record",
    "incomplete_or_failed_query": "an ABSENCE conclusion (no link or no target row) that depends on a mechanism or identity source in a FAILED, INCOMPLETE or NOT_FETCHED state: NOT a negative. Positive evidence from a working source is not changed by it, and an accessibility-source error never produces it (a stale source adds a caveat instead)",
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
                                "genotype": a.get("context", {}).get("genotype"), "stage": a.get("context", {}).get("developmental_stage"),
                            "source": a.get("source"), "receipt": a.get("receipt"), "endpoint": a.get("endpoint")})
            out[stem] = {"card_id": stem, "dir": sub, "candidate": p.get("candidate", {}), "route": p.get("route"), "assertions": ass,
                         "endpoint_pursued": (c.get("p4_fields") or {}).get("endpoint_pursued"), "next_step": c.get("next_step"),
                         "limits": c.get("limits", []), "is_axis": str(p.get("candidate", {}).get("id", "")).startswith("AXIS:")}
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


# ----------------------------------------------------------------------------- inputs
PERT_COLS = ("card_id", "assertion_id", "need_id", "subject", "evidence_kind", "sign", "counts_L3", "counts_L4", "flags", "basis")
OPTIONAL_PERT_COLS = ("comparator",)    # read when present: what the sign is measured AGAINST (untreated_same_genotype, wild_type_only, ...)
# Evidence kinds and what each one MEANS. Only the first two are an effect in the disease model; the third and fourth are observations
# against or in wild type and are never a rescue; the fifth is a pure reference arm.
#   readout_in_wwox_system             result in the WWOX model: a WWOX-deficient system measured (treated vs untreated disease arm, or a dose arm)
#   case_report_wwox_clinical          uncontrolled clinical report in a WWOX patient
#   genotype_comparison_vs_wild_type   direct genotype comparison: the WWOX-deficient (treated) arm compared with wild type ONLY, no untreated disease arm
#   effect_in_wild_type_arm            pharmacological effect of the drug in a wild-type or carrier (heterozygous) arm of the same experiment
#   control_arm_same_experiment        reference or control arm without a drug effect of its own
READOUT_KINDS = ("readout_in_wwox_system", "case_report_wwox_clinical")
WT_COMPARISON_KIND = "genotype_comparison_vs_wild_type"
WT_EFFECT_KIND = "effect_in_wild_type_arm"
NOT_AN_OBSERVATION_KINDS = ("case_report_uninformative", "out_of_scope_endpoint", "control_arm_same_experiment")
HARD_STATES = {"FAILED", "INCOMPLETE", "NOT_FETCHED"}
# What a source can support. mechanism/identity sources decide whether a link or a target row EXISTS, so their failure can undermine an
# absence conclusion. accessibility/status_context sources only tell how a substance can be obtained or its regulatory status: their failure
# caveats access categories and never touches a mechanism or an absence of one. An unknown source is treated as mechanism (conservative).
SOURCE_ROLES = {"chembl": "mechanism", "dgidb": "mechanism", "unichem": "identity", "matrix": "status_context", "openfda_ndc": "accessibility", "dsld": "accessibility"}
MECHANISM_ROLES = ("mechanism", "identity")
LINK_SOURCE_KEY = {"ChEMBL curated mechanism": "chembl", "DGIdb interaction": "dgidb"}
STALE_STATES = {"STALE_EXPORT", "STALE_AFTER_FAILED_REFRESH"}
TOOL_SUBJECTS = {"tool_no_catalogue_identity", "genetic_precedent_not_a_compound"}


def load_pertinence(path: Path) -> list[dict]:
    p = Path(path)
    if not p.exists():
        return []
    with open(p, encoding="utf-8", newline="") as fh:
        return [r for r in csv.DictReader(fh, delimiter="\t")]


def source_roles_of(names) -> dict:
    return {k: SOURCE_ROLES.get(k, "mechanism") for k in names}


def effective_states(cstats: dict) -> dict:
    """Source states with `stale` as a state of its own. The raw catalogue state OK stays OK unless the evidence says old export / partial."""
    out = {}
    for k, v in cstats["sources"].items():
        out[k] = {"state": v.get("state"), "detail": None}
    age = cstats.get("dgidb_age") or {}
    lm = ((age.get("export_in_use") or {}).get("last_modified")) or ""
    m = re.search(r"(\d{4})", lm)
    gen = (cstats.get("generated_utc") or "")[:4]
    if "dgidb" in out and out["dgidb"]["state"] == "OK" and m and gen.isdigit() and int(gen) - int(m.group(1)) >= 1:
        out["dgidb"] = {"state": "STALE_EXPORT", "detail": f"DGIdb TSV export of {lm.strip()} (claims from ChEMBL 33); the live service reports newer source versions; current coverage not ingested"}
    d = cstats.get("dsld") or {}
    if out.get("dsld", {}).get("state") == "OK" and d.get("bulk_list_probed", 0) < d.get("bulk_list_planned_names", 0):
        out["dsld"] = {"state": "PARTIAL", "detail": f"{d.get('bulk_list_probed')} of {d.get('bulk_list_planned_names')} bulk-list names probed (name-only evidence); affects access categories only"}
    return out


# ----------------------------------------------------------------------------- build
def build(needs_path=rs.DEFAULT_NEEDS, catalog_dir: Path = cc.DEFAULT_DIR, dr: Path = DR, roles_path=rs.DEFAULT_ROLES,
          artefacts_path=rs.DEFAULT_ARTEFACTS, pertinence_path=None) -> dict:
    pertinence_path = pertinence_path or (Path(roles_path).parent / "assertion_pertinence.tsv")
    nd = rs.load_needs(needs_path)
    needs = nd["needs"]
    entries = cc.load(catalog_dir / "catalog.jsonl.gz")
    cstats = json.loads((catalog_dir / "catalog_stats.json").read_text())
    arte = rs.load_artefacts(artefacts_path)
    idx, roles = rs.Index(entries, arte), rs.load_roles(roles_path)
    cards = load_cards(dr)
    att, mods = card_attachments(catalog_dir / "card_links.json", catalog_dir / "non_molecule_modalities.tsv")
    pert = load_pertinence(pertinence_path)
    need_ids = {n["id"] for n in needs}
    stale_roles = sorted(f"{n}/{s}" for (n, s) in roles if n not in need_ids or s not in {t["symbol"].upper() for x in needs if x["id"] == n for t in x["targets"]})
    eff = effective_states(cstats)
    hard = sorted(k for k, v in eff.items() if v["state"] in HARD_STATES)
    hard_mech = [k for k in hard if SOURCE_ROLES.get(k, "mechanism") in MECHANISM_ROLES]
    hard_other = [k for k in hard if k not in hard_mech]
    stale = sorted(k for k, v in eff.items() if v["state"] in STALE_STATES)
    measure_next = json.loads((dr / "join/measure_next.json").read_text()) if (dr / "join/measure_next.json").exists() else []

    need_cards = {n["id"]: [c for c in (_stem(r) for r in n["sources"].get("cards", [])) if c in cards] for n in needs}
    missing_cards = sorted({_stem(r) for n in needs for r in n["sources"].get("cards", [])} - set(cards))
    ass_index = {(cid, a["id"]): a for cid, c in cards.items() for a in c["assertions"]}
    stale_pert = sorted(f"{r['card_id']}/{r['assertion_id']}/{r['need_id']}" for r in pert
                        if (r["card_id"], r["assertion_id"]) not in ass_index or r["need_id"] not in need_ids
                        or (r["subject"].startswith("CHEMBL") and f"CAT:{r['subject']}" not in idx.by_id))
    pert = [r for r in pert if f"{r['card_id']}/{r['assertion_id']}/{r['need_id']}" not in stale_pert]

    per_need = {n["id"]: rs.associations_for_need(n, idx, roles) for n in needs}
    assoc_all = [a for r in per_need.values() for a in r["associations"]]
    counted = lambda a: not a["excluded_from_counts"] and a["target_kind"] in rs.LINK_KINDS           # headline
    pathway = lambda a: not a["excluded_from_counts"] and a["target_kind"] in rs.PATHWAY_KINDS

    rows: dict[str, dict] = {}

    def row(fid: str) -> dict:
        if fid not in rows:
            mem = idx.members.get(fid, [])
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
        if counted(a) or pathway(a):
            cell_assoc[(a["family"], a["need"])].append(a)
            row(a["family"])

    # card rows: only DECLARED identities (identity / named_member) attach a card to a family. A mention in the card text never does.
    card_rows: dict[str, list] = {}
    for cid, c in sorted(cards.items()):
        if c["is_axis"]:
            continue
        decl = [l for l in att.get(cid, []) if l["role"] in ("identity", "named_member")]
        if decl and cid not in mods:
            card_rows[cid] = []
            for l in decl:
                fid = idx.family[l["catalogue_id"]]
                row(fid)["cards"].append({"card_id": cid, "attachment": l["role"], "rule": l["rule"]})
                card_rows[cid].append((fid, l["role"]))
        else:
            rid = "INT:" + cid
            rows[rid] = {"row_id": rid, "kind": "non_molecule_intervention" if cid in mods else "intervention_without_catalogue_identity",
                         "name": c["candidate"].get("name"), "modality": mods.get(cid, "class_level_or_no_declared_identity"),
                         "cards": [{"card_id": cid, "attachment": "own_identity", "rule": "the card is the intervention"}]}
            card_rows[cid] = [(rid, "own_identity")]

    # observations: one record per (assertion, need) listed in assertion_pertinence.tsv, attached to its SUBJECT
    obs_by_cell = collections.defaultdict(list)
    for r in pert:
        cid, aid, nid = r["card_id"], r["assertion_id"], r["need_id"]
        a = ass_index[(cid, aid)]
        subj = r["subject"]
        targets_ = []
        if subj == "card":
            targets_ = card_rows.get(cid, [])
        elif subj.startswith("CHEMBL"):
            fid = idx.family["CAT:" + subj]
            row(fid)["cards"].append({"card_id": cid, "attachment": "assertion_subject", "rule": "per-assertion subject in assertion_pertinence.tsv"}) if not any(x["card_id"] == cid and x["attachment"] == "assertion_subject" for x in rows[fid]["cards"]) else None
            targets_ = [(fid, "assertion_subject")]
        else:
            rid = f"INT:{cid}:tool"
            rows.setdefault(rid, {"row_id": rid, "kind": "tool_compound_or_genetic_precedent_not_in_catalogue", "name": f"{cards[cid]['candidate'].get('name')} [tool or genetic subject]",
                                  "modality": subj, "cards": [{"card_id": cid, "attachment": "tool_subject", "rule": "assertion subject has no catalogue identity"}]})
            targets_ = [(rid, "tool_subject")]
        for (rid, attach) in targets_:
            obs_by_cell[(rid, nid)].append(dict(a, card_id=cid, attachment=attach, kind=r["evidence_kind"], sign=r["sign"], counts_L3=r["counts_L3"] == "yes",
                                               counts_L4=r["counts_L4"] == "yes", flags=r["flags"], pert_basis=r["basis"], comparator=(r.get("comparator") or "")))
    # a card-cited need gets a cell for the card's own row even when no assertion is listed (so 'none in cards' is visible)
    cited_cells = {(rid, n) for cid, rl in card_rows.items() for (rid, _a) in rl for n, cs in need_cards.items() if cid in cs}

    cells = {}
    listed_all = {(r["card_id"], r["assertion_id"]) for r in pert}
    need_by = {n["id"]: n for n in needs}
    stale_caveat = [f"{k}: {eff[k]['detail']}" for k in stale if eff[k].get("detail")]
    partial = [f"{k}: {v['detail']}" for k, v in eff.items() if v["state"] == "PARTIAL"]
    for rr in rows.values():
        if partial and rr["kind"] == "molecule_family":
            rr["access_caveat"] = "; ".join(partial) + "; supplement status is name-only, so unknown/unverified for supplements is not a negative"
        if hard_other and rr["kind"] == "molecule_family":
            rr["access_caveat"] = (rr.get("access_caveat", "") + "; " if rr.get("access_caveat") else "") + \
                f"accessibility/status source(s) {hard_other} in a failed, truncated or never-fetched state: access categories may be incomplete (affects access only, not mechanism)"
    for rid in sorted(rows):
        r = rows[rid]
        for nid, need in need_by.items():
            assoc = cell_assoc.get((rid, nid), [])
            obs = obs_by_cell.get((rid, nid), [])
            if not assoc and not obs and (rid, nid) not in cited_cells:
                continue
            link = [a for a in assoc if counted(a)]
            pw = [a for a in assoc if pathway(a)]
            cons = [a for a in link if a["consistency"] == "consistent"]
            opp = [a for a in link if a["consistency"] == "opposed"]
            no_id = r["kind"] != "molecule_family"
            nd_dir = rs.need_direction(need)
            if no_id:
                L1 = {"state": "not_evaluable", "why": "no catalogue identity (non-molecule modality, class-level card or tool/genetic subject): not zero, not a negative"}
                L2 = {"state": "not_evaluable", "why": L1["why"]}
            else:
                if link:
                    st = "documented"
                elif hard_mech:
                    st = "source_incomplete"
                elif pw:
                    st = "pathway_member_only"
                else:
                    st = "none_found"
                L1 = {"readout_marker_only_links": 0, "state": st, "targets": sorted({a["target"] for a in link}), "target_kinds": sorted({a["target_kind"] for a in link}),
                      "link_sources": sorted({a["link_source"] for a in link}), "associations": len(link),
                      "pathway_member_targets_listed_apart": sorted({a["target"] for a in pw}) if not link else sorted({a["target"] for a in pw})}
                if st in ("none_found", "pathway_member_only"):
                    L1["why"] = "ChEMBL mechanisms and DGIdb queried; no row on this need's intervention targets"
                    if stale_caveat:
                        L1["source_caveat_stale"] = stale_caveat
                if nd_dir in ("uncertain", "modulate"):
                    L2 = {"state": "not_evaluable", "why": "need direction is 'uncertain': coherence cannot be evaluated; exploration only",
                          "actions_present": sorted({a["action_on_target"] for a in link})}
                else:
                    L2 = {"state": ("mixed_consistent_and_opposed" if cons and opp else "coherent" if cons else ("opposed" if opp else ("direction_unresolved" if link else "none"))),
                          "consistent_actions": action_contexts(cons), "opposed_actions": action_contexts(opp),
                          "signs_not_summed": True if cons and opp else None,
                          "consistent_associations": len(cons), "opposed_associations": len(opp),
                          "unresolved_associations": len([a for a in link if a["consistency"] in ("direction_unresolved", "not_evaluable")]),
                          "certainty_qualifiers": sorted({a["certainty_qualifier"] for a in cons + opp if a.get("certainty_qualifier")})}
            L3, L4 = observation_levels(obs)
            card_set = {o["card_id"] for o in obs} | {x["card_id"] for x in r["cards"]}
            L3["unassessed_assertions_on_card"] = sorted(f"{cid}/{aid}" for cid in card_set for (c2, aid), a in ass_index.items()
                                                         if c2 == cid and a["epistemic_status"] == "DATO" and (cid, aid) not in listed_all and not cards[cid]["is_axis"])
            cells[(rid, nid)] = {"row_id": rid, "need": nid, "L1_documented_link": L1, "L2_mechanistic_coherence": L2, "L3_observed_effect": L3,
                                 "L4_observed_recovery_in_wwox_system": L4, "exploration_only": nd_dir in ("uncertain", "modulate")}

    # possible duplicates and name-prefix hints
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
            r["name_is_source_artifact"] = r["name"].strip().lower() in rs.PLACEHOLDER_NAMES
    for (rid, nid), c in cells.items():
        r = rows[rid]
        if r["kind"] == "molecule_family" and c["L1_documented_link"]["state"] != "documented" and r["name"] and not r.get("name_is_source_artifact"):
            pre = cc._norm(r["name"]).split(" ")[0]
            sib = sorted(o for o, ro in rows.items() if o != rid and ro["kind"] == "molecule_family" and ro["name"] and cc._norm(ro["name"]).split(" ")[0] == pre
                         and (o, nid) in cells and cells[(o, nid)]["L1_documented_link"]["state"] == "documented")
            if sib:
                c["L1_documented_link"]["name_prefix_sibling_families_with_link_HINT_not_evidence"] = sib[:5]

    priorities = make_priorities(rows, cells, need_by, cards, card_rows, need_cards, eff, hard, stale, measure_next, idx)
    summary = make_summary(entries, idx, rows, cells, per_need, priorities, need_by, cards, need_cards, eff, hard, stale, cstats, stale_roles, stale_pert,
                           missing_cards, assoc_all, pert, ass_index, counted, pathway)
    matrix = {"schema": SCHEMA, "generated_from": inputs_digest(needs_path, catalog_dir, dr, roles_path, artefacts_path, pertinence_path),
              "levels": {"L1_documented_link": "catalogue link to an INTERVENTION target (or disease gene product) of the need; pathway members, effector constraints and readout markers are not L1",
                         "L2_mechanistic_coherence": "direction-consistent action, only for direction-evaluable needs with an explicit role row; certainty qualifiers carried",
                         "L3_observed_effect": "assertion on THIS compound, endpoint listed as pertinent to THIS need (assertion_pertinence.tsv), a readout in a WWOX system or a WWOX clinical case report; sign carried; other-disease precedents, target-engagement assays and safety signals are separate states",
                         "L4_observed_recovery_in_wwox_system": "L3 assertion with bridge comparison OPPOSES_DISEASE_CHANGE, reading depth known, high-dose arm only; experimental vs case level kept apart"},
              "never_summed": True, "unit": "rows are compound FAMILIES, card interventions, or tool/genetic subjects; a cell counts once per (row, need)",
              "need_directions": {n["id"]: rs.need_direction(n) for n in needs},
              "exploration_needs": sorted(n["id"] for n in needs if rs.need_direction(n) in ("uncertain", "modulate")),
              "source_states": {k: v for k, v in eff.items()},
              "rows": [rows[k] for k in sorted(rows)], "cells": [cells[k] for k in sorted(cells)]}
    return {"matrix": matrix, "priorities": priorities, "summary": summary, "associations": assoc_all}


def action_contexts(assocs: list[dict]) -> list[dict]:
    """The context of each action (target, action, source, record) so that consistent and opposed actions on one need can be read side by
    side. Duplicates collapse; nothing is counted twice and no sign is combined."""
    seen, out = set(), []
    for a in sorted(assocs, key=lambda a: (a["target"], a["catalogue_id"], str(a["action_on_target"]), a["link_source"])):
        key = (a["target"], a["action_on_target"], a["action_raw"], a["link_source"], a["catalogue_id"])
        if key in seen:
            continue
        seen.add(key)
        out.append({"target": a["target"], "action": a["action_on_target"], "action_raw": a["action_raw"], "link_source": a["link_source"],
                    "record": a["catalogue_id"], "compound_record_name": a["compound"], "certainty_qualifier": a.get("certainty_qualifier")})
    return out


def observation_levels(obs: list[dict]) -> tuple[dict, dict]:
    """L3 and L4 of one cell from its listed assertions. The comparison an observation rests on decides what it means:
      result in the WWOX model          readout_in_wwox_system, case_report_wwox_clinical: a WWOX-deficient system or patient measured
                                        against its own untreated state (or a dose arm); the only kinds that reach observed_wwox_system / L4
      direct genotype comparison        genotype_comparison_vs_wild_type: the WWOX-deficient (treated) arm compared with wild type ONLY,
                                        no untreated disease arm; informative but not an effect against the disease change, never L4
      effect in a wild-type arm         effect_in_wild_type_arm: what the drug does in wild-type or carrier animals of the same experiment;
                                        not an effect in the disease model and not a rescue
      reference or control              control_arm_same_experiment: reference arm without an effect of its own
    A cell reads `observed_wwox_system` only when a result in the WWOX model is informative; otherwise the wild-type states
    (`observed_vs_wild_type_only`, `effect_in_wild_type_only`) say what was actually seen. An assertion whose reading depth is UNKNOWN never
    reaches an observed state (`observed_depth_unknown`). Uninformative case reports, out-of-scope endpoints, unquantified readouts and
    listed-but-not-counted rows stay visible under `listed_not_counted`. Each observation keeps its subject row, comparator, endpoint,
    stage, conditions, sign, reading depth and character (`observations`)."""
    counted_pool = [o for o in obs if o["kind"] in READOUT_KINDS + (WT_COMPARISON_KIND,) and o["counts_L3"]]
    deep = [o for o in counted_pool if o["reading_depth"] != "UNKNOWN"]
    shallow = [o for o in counted_pool if o["reading_depth"] == "UNKNOWN"]
    wx = [o for o in deep if o["kind"] == "readout_in_wwox_system"]
    cl = [o for o in deep if o["kind"] == "case_report_wwox_clinical"]
    gc = [o for o in deep if o["kind"] == WT_COMPARISON_KIND]
    wta_all = [o for o in obs if o["kind"] == WT_EFFECT_KIND]
    wta = [o for o in wta_all if o["reading_depth"] != "UNKNOWN"]
    oth = [o for o in obs if o["kind"] == "readout_other_disease"]
    te = [o for o in obs if o["kind"] == "target_engagement_assay"]
    saf = [o for o in obs if o["kind"] == "safety_signal"]
    lab = [o for o in obs if o["kind"] == "label_statement"]
    ctrl = [o for o in obs if o["kind"] == "control_arm_same_experiment"]
    not_counted = [o for o in obs if o not in counted_pool and o["kind"] in READOUT_KINDS + (WT_COMPARISON_KIND, "case_report_uninformative", "out_of_scope_endpoint")]
    sg = lambda L: dict(collections.Counter(o["sign"] for o in L))
    informative = lambda L: [o for o in L if o["sign"] not in ("null", "unresolved")]
    if wx and informative(wx):
        st = "observed_wwox_system"
    elif cl and informative(cl):
        st = "observed_case_level_only"
    elif shallow:
        st = "observed_depth_unknown"
    elif wx or cl:
        st = "measured_null_only"
    elif gc:
        st = "observed_vs_wild_type_only"
    elif wta:
        st = "effect_in_wild_type_only"
    elif oth:
        st = "precedent_other_disease_only"
    elif te:
        st = "target_engagement_only"
    elif saf:
        st = "safety_signal_only"
    else:
        st = "none_in_cards"
    scope_counts = dict(collections.Counter(("wwox_experimental" if o["kind"] == "readout_in_wwox_system" else "wwox_clinical_report") for o in wx + cl))
    comparison_of = {"readout_in_wwox_system": "result_in_wwox_model", "case_report_wwox_clinical": "result_in_wwox_model", WT_COMPARISON_KIND: "direct_genotype_comparison_vs_wild_type_only",
                     WT_EFFECT_KIND: "pharmacological_effect_in_wild_type_or_carrier_arm", "control_arm_same_experiment": "reference_or_control_arm"}
    recorded = [o for o in obs if o["kind"] in comparison_of]
    L3 = {"by_scope": scope_counts, "measured_null_assertions": sum(1 for o in wx + cl if o["sign"] == "null"), "inference_assertions": 0,
          "state": st, "signs_wwox_system_readouts": sg(wx), "signs_case_reports": sg(cl),
          "signs_direct_genotype_comparison_vs_wild_type_only": sg(gc), "signs_effect_in_wild_type_or_carrier_arms": sg(wta),
          "signs_depth_unknown_not_counted_as_observed": sg(shallow),
          "signs_other_disease_precedent_not_observed_here": sg(oth), "signs_control_arms_of_the_same_experiment": sg(ctrl),
          "target_engagement_assays_not_readouts": len(te), "safety_signals_kept_apart": sg(saf), "label_statements_not_observations": len(lab),
          "listed_not_counted": sorted({f"{o['id']}:{o['kind']}" for o in not_counted}),
          "assertion_ids": sorted({o["id"] for o in wx + cl + gc}), "cards": sorted({o["card_id"] for o in obs}),
          "assertion_ids_by_comparison": {"result_in_wwox_model": sorted({o["id"] for o in wx + cl}), "direct_genotype_comparison_vs_wild_type_only": sorted({o["id"] for o in gc}),
                                          "pharmacological_effect_in_wild_type_or_carrier_arm": sorted({o["id"] for o in wta_all}),
                                          "reference_or_control_arm": sorted({o["id"] for o in ctrl})},
          "wild_type_only_note": ("comparison with wild type only, or an effect in a wild-type/carrier arm: informative, but NOT an effect in the disease model and NOT a rescue"
                                  if (gc or wta_all) else None),
          "observations": sorted(({"id": o["id"], "card": o["card_id"], "attached_as": o.get("attachment"), "meaning": comparison_of[o["kind"]], "evidence_kind": o["kind"], "sign": o["sign"],
                                   "comparator": o.get("comparator") or "not_recorded", "endpoint": o.get("endpoint"), "stage_or_time": o.get("stage"), "genotype": o.get("genotype"),
                                   "reading_depth": o.get("reading_depth"),
                                   "character": ("clinical_uncontrolled_report" if o["kind"] == "case_report_wwox_clinical" else "experimental"),
                                   "counted_in_L3": bool(o["counts_L3"]), "conditions": sorted(f for f in (o.get("flags") or "").split(";") if f)} for o in recorded),
                                  key=lambda r: (r["id"], r["meaning"])),
          "flags": sorted({f for o in wx + cl + gc + shallow for f in o["flags"].split(";") if f}),
          "pertinence": "endpoint-level: each assertion is listed for this need in assertion_pertinence.tsv; unlisted assertions are not counted and are flagged per cell as unassessed_assertions_on_card",
          "harm_and_benefit_are_not_pooled": True,
          "absence_note": "none_in_cards is not a negative: cards cover a few dozen interventions" if st == "none_in_cards" and not obs else None}
    rec = [o for o in wx + cl if o["counts_L4"] and o["comparison"] == "OPPOSES_DISEASE_CHANGE"]
    exp = [o for o in rec if o["kind"] == "readout_in_wwox_system"]
    case = [o for o in rec if o["kind"] == "case_report_wwox_clinical"]
    notes = sorted({f for o in rec for f in o["flags"].split(";") if f.startswith("growth=")})
    L4 = {"by_scope": {k: v for k, v in (("wwox_experimental", len(exp)), ("wwox_clinical_report", len(case))) if v}, "via_class_card": False,
          "state": "observed_experimental" if exp else ("observed_case_level" if case else "none_in_record"),
          "assertion_ids": sorted(o["id"] for o in rec), "experimental_assertions": len(exp), "case_level_assertions": len(case),
          "endpoint_note": ("growth = body weight only (blood glucose was not changed)" if "growth=body_weight_only" in notes else None),
          "definition": "WWOX-system assertion judged by the bridge as opposing the disease change, endpoint pertinent to the need, reading depth known, high-dose arm only for dose-arm designs; a comparison with wild type only or an effect in a wild-type arm is never recovery; a technical comparison, not efficacy or safety. case_level = uncontrolled clinical report"}
    return L3, L4


def inputs_digest(needs_path, catalog_dir, dr, roles_path, artefacts_path, pertinence_path) -> dict:
    def h(p):
        p = Path(p)
        return hashlib.sha256(p.read_bytes()).hexdigest()[:16] if p.exists() else "ABSENT"
    cards = hashlib.sha256(b"".join(f.read_bytes() for sub in ("cards", "cards_early") for f in sorted((dr / sub).glob("*.json")))).hexdigest()[:16]
    return {"needs.json": h(needs_path), "catalog.jsonl.gz": h(catalog_dir / "catalog.jsonl.gz"), "catalog_stats.json": h(catalog_dir / "catalog_stats.json"),
            "card_links.json": h(catalog_dir / "card_links.json"), "target_roles.tsv": h(roles_path), "source_artefacts.tsv": h(artefacts_path),
            "assertion_pertinence.tsv": h(pertinence_path), "cards_and_packets": cards, "measure_next.json": h(dr / "join/measure_next.json")}


# ----------------------------------------------------------------------------- priorities
def make_priorities(rows, cells, need_by, cards, card_rows, need_cards, eff, hard, stale, measure_next, idx) -> dict:
    out, skipped = [], collections.Counter()
    stale_note = [f"{k}: stale ({eff[k]['detail']})" for k in stale if eff[k].get("detail")]
    for (rid, nid), c in sorted(cells.items()):
        r, need = rows[rid], need_by[nid]
        card_ids = sorted({x["card_id"] for x in r["cards"]})
        interesting = bool(card_ids) or c["L2_mechanistic_coherence"]["state"] == "coherent" or (
            r["kind"] == "molecule_family" and ("approved_any_source" in r["status_class"] or {"prescription", "OTC", "supplement"} & set(r["access_categories"])))
        if not interesting or r.get("name_is_source_artifact"):
            skipped["not_prioritised_no_card_no_coherence_no_approval_or_access" if not r.get("name_is_source_artifact") else "placeholder_record"] += 1
            continue
        L1, L2, L3, L4 = (c[k] for k in ("L1_documented_link", "L2_mechanistic_coherence", "L3_observed_effect", "L4_observed_recovery_in_wwox_system"))
        nd = rs.need_direction(need)
        qual = L2.get("certainty_qualifiers", []) if isinstance(L2, dict) else []
        if r["kind"] != "molecule_family":
            disp, why = "insufficient_data", "no catalogue identity (non-molecule modality, class-level card or tool subject): links to targets cannot be evaluated"
        elif L1["state"] == "documented":
            if L2.get("state") == "mixed_consistent_and_opposed":
                disp, why = "mixed_consistent_and_opposed_actions", ("BOTH a direction-consistent and an opposed action are catalogued on this need (" + describe_actions(L2) +
                                                                       "); the contexts differ and no sign is summed, so this profile is not favourable on the consistent action alone")
            elif L2.get("state") == "coherent":
                disp, why = "consistent_mechanism_candidate", "direction-consistent action on an intervention target with explicit coupling" + (f" [qualifier: {'; '.join(qual)}]" if qual else "")
            elif L2.get("state") == "opposed":
                disp, why = "opposite_mechanism", "the stated action opposes the need's direction; no consistent action catalogued" + (f" [qualifier: {'; '.join(qual)}]" if qual else "")
            elif nd in ("uncertain", "modulate"):
                disp, why = "exploration_candidate", EXPLORATION_NOTE
            else:
                disp, why = "insufficient_data", "link documented but no stated up/down action or the role row is unresolved (inferred, not measured)"
        elif L1["state"] == "pathway_member_only":
            disp, why = "insufficient_data", "only pathway-member links (not intervention targets): the catalogue offers no direct point of action"
        elif r["target_rows_total"] == 0:
            disp, why = "source_queried_without_result", "ChEMBL mechanism and DGIdb queried; no target row for any record of this family"
        else:
            disp, why = "no_catalogue_link_found", "by catalogued targets only: this family has target rows and none is an intervention target of this need"
            if card_ids:
                why += "; a card cites it for this need through a mechanism the catalogue does not describe as a target (the card's rationale is not overridden)"
        # source failure: positive evidence from a working source is kept; only an absence that rests on a missing mechanism/identity source is incomplete
        hard_mech = [k for k in hard if SOURCE_ROLES.get(k, "mechanism") in MECHANISM_ROLES]
        hard_other = [k for k in hard if k not in hard_mech]
        absence_depends = bool(hard_mech) and r["kind"] == "molecule_family" and L1["state"] == "source_incomplete"
        if absence_depends:
            disp, why = "incomplete_or_failed_query", (f"no link was found, but mechanism/identity source(s) {hard_mech} are in a failed, truncated or never-fetched state: "
                                                     "the absence cannot be concluded (not a negative)")
        positive_on_hard = sorted({LINK_SOURCE_KEY.get(x, x) for x in L1.get("link_sources", [])} & set(hard)) if L1["state"] == "documented" else []
        if positive_on_hard:
            why += f"; caveat: the link rests on source(s) {positive_on_hard} whose retrieval is flagged incomplete"
        if L3["state"] in ("observed_vs_wild_type_only", "effect_in_wild_type_only"):
            why += ("; the listed observation is a comparison with wild type only" if L3["state"] == "observed_vs_wild_type_only" else
                    "; the listed observation is the drug's effect in a wild-type or carrier arm") + ": not an effect in the disease model and not a rescue"
        if disp in ("no_catalogue_link_found", "source_queried_without_result") and L1.get("name_prefix_sibling_families_with_link_HINT_not_evidence"):
            why += "; other records with the same leading name word do link (salt/form families, separate identities, review hint only)"
        if disp in ("no_catalogue_link_found", "source_queried_without_result", "insufficient_data") and stale_note and r["kind"] == "molecule_family":
            why += "; absence holds for a STALE source: " + "; ".join(stale_note)
        crs = [cards[c_] for c_ in card_ids]
        sel = [a for c_ in crs for a in c_["assertions"]]
        out.append({
            "row_id": rid, "name": r["name"], "kind": r["kind"], "need": nid, "need_direction": nd,
            "exploration_only": nd in ("uncertain", "modulate"), "disposition": disp, "disposition_reason": why,
            "source_caveats": stale_note,
            "search_incompleteness": ({"overall_search_incomplete": True, "sources_in_hard_state": {k: SOURCE_ROLES.get(k, "mechanism") for k in hard},
                                       "this_conclusion_depends_on_a_missing_source": absence_depends,
                                       "effect": ("absence conclusion withheld" if absence_depends else
                                                  "positive or identity-independent conclusion unchanged" + ("; access categories may be incomplete" if hard_other else ""))} if hard else None),
            "actions": ({"consistent": c["L2_mechanistic_coherence"].get("consistent_actions", []), "opposed": c["L2_mechanistic_coherence"].get("opposed_actions", [])}
                        if c["L2_mechanistic_coherence"].get("consistent_actions") or c["L2_mechanistic_coherence"].get("opposed_actions") else None),
            "levels": {k: c[k].get("state") for k in ("L1_documented_link", "L2_mechanistic_coherence", "L3_observed_effect", "L4_observed_recovery_in_wwox_system")},
            "certainty_qualifiers": qual,
            "criteria": {
                "wwox_relevance": {"need_evidence_scopes": need["evidence_scope"], "n_wwox_system_observations_in_need": sum(1 for o in need["observed"] if o["evidence_scope"] == "WWOX_EXPERIMENT_IN_DEE_SYSTEM"),
                                   "intervention_L3_state": L3["state"]},
                "direction_mechanism": {"L2": L2.get("state"), "targets": L1.get("targets", []), "link_sources": L1.get("link_sources", [])},
                "evidence_quality_independence": {"listed_pertinent_assertions": len(L3["assertion_ids"]), "signs": {"wwox_system": L3["signs_wwox_system_readouts"], "case_reports": L3["signs_case_reports"]},
                                                  "signs_vs_wild_type_only_not_a_disease_model_effect": L3["signs_direct_genotype_comparison_vs_wild_type_only"],
                                                  "signs_effect_in_wild_type_or_carrier_arm": L3["signs_effect_in_wild_type_or_carrier_arms"],
                                                  "reading_depths_in_cards": dict(collections.Counter(a["reading_depth"] for a in sel)),
                                                  "note": "shared sources are not independent confirmations; nothing is pooled; harm and benefit stay separate"},
                "counter_evidence": {"need_counter_evidence_items": len(need["counter_evidence"]), "intervention_signs_harm": L3["safety_signals_kept_apart"],
                                     "intervention_measured_null": (L3["signs_wwox_system_readouts"].get("null", 0) + L3["signs_case_reports"].get("null", 0))},
                "potency_and_assay_context": "NOT_CARRIED: the catalogue holds no potency; target-engagement assays are counted apart (" + str(L3["target_engagement_assays_not_readouts"]) + ")",
                "transferability": {"species_of_assertions": sorted({a["species"] for a in sel if a["species"]}), "scopes": sorted({a["scope"] for a in sel}),
                                    "system_of_interest": "WWOX-DEE reference genotype class; transfer is a stated distance, not a score"},
                "pharmacology_safety_info": {"status_class": r.get("status_class"), "access_categories": r.get("access_categories"), "access_caveat": r.get("access_caveat"),
                                             "safety_assessment": "NOT_ASSESSED (catalogue); safety triage is a separate step"},
                "discriminating_experiment": {"card_endpoint_pursued": [c_["endpoint_pursued"] for c_ in crs if c_["endpoint_pursued"]][:1],
                                              "exists": any(c_["endpoint_pursued"] for c_ in crs)},
            },
            "next_deepening": deepening(disp, c, nd, crs),
            "possible_duplicates_not_merged": r.get("n_possible_duplicates", 0),
            "reversible": "a disposition is a function of the inputs; change a role row, a pertinence row, a card or the catalogue and regenerate",
        })
    return {"schema": SCHEMA, "dispositions": DISPOSITIONS, "ranking": "none: no score, no ordering by evidence volume; filter by disposition, need or criterion. Order is need id then row id.",
            "no_probability": "nothing here is a probability of benefit or cure", "priorities": out, "pairs_not_prioritised": dict(skipped)}


def describe_actions(l2: dict) -> str:
    f = lambda L: "; ".join(f"{x['target']} {x['action']} [{x['link_source']}, {x['record']}]" for x in L)
    return f"consistent: {f(l2.get('consistent_actions', []))} | opposed: {f(l2.get('opposed_actions', []))}"


def deepening(disp, c, nd, crs) -> list[str]:
    d = []
    if disp == "mixed_consistent_and_opposed_actions":
        d.append("resolve which target and action governs the quantity in the disease system before reading either action as supportive; no net sign is computed")
    if c["L3_observed_effect"]["state"] in ("observed_vs_wild_type_only", "effect_in_wild_type_only"):
        d.append("the only observation is against wild type or in a wild-type arm: a treated-versus-untreated arm of the WWOX-deficient system is the missing comparison")
    if nd in ("uncertain", "modulate"):
        d.append("resolve the sign of the need before reading any mechanism as supportive")
    if c["L4_observed_recovery_in_wwox_system"]["state"] == "none_in_record":
        d.append("no WWOX-system recovery observation recorded: a discriminating measurement in a WWOX-deficient system is the missing step")
    if disp in ("consistent_mechanism_candidate", "exploration_candidate"):
        d.append("fitted potency and selectivity on the linked target (not carried by the catalogue)")
    if disp == "no_catalogue_link_found":
        d.append("none for this need by catalogued targets; the compound may belong to other needs")
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


def headline_by_relation(head: list) -> dict:
    """Headline records by the strongest kind of statement behind them (never a quality score): a stated action from a curated source,
    a stated action from another source, or a link whose source states no action (listing / association)."""
    best = {}
    for a in head:
        r = 0 if (a["action_stated"] and a["relation_kind"] in rs.CURATED_KINDS) else 1 if a["action_stated"] else 2
        best[a["catalogue_id"]] = min(best.get(a["catalogue_id"], 2), r)
    names = {0: "action_stated_by_curated_source", 1: "action_stated_by_other_source_only", 2: "link_without_stated_action_only"}
    return {names[k]: sum(1 for v in best.values() if v == k) for k in (0, 1, 2)}


def make_summary(entries, idx, rows, cells, per_need, priorities, need_by, cards, need_cards, eff, hard, stale, cstats, stale_roles, stale_pert, missing_cards, assoc_all, pert, ass_index, counted, pathway) -> dict:
    fam_all = set(idx.family.values())
    chembl_fams = {idx.family[e["id"]] for e in entries if e["origin"].startswith("chembl")}
    head = [a for a in assoc_all if counted(a)]
    pw = [a for a in assoc_all if pathway(a)]
    excl = [a for a in assoc_all if a["excluded_from_counts"] and a["target_kind"] in (rs.LINK_KINDS | rs.PATHWAY_KINDS)]
    head_rec, head_fam = {a["catalogue_id"] for a in head}, {a["family"] for a in head}
    act_rec, act_fam = {a["catalogue_id"] for a in head if a["action_stated"]}, {a["family"] for a in head if a["action_stated"]}
    wide_rec, wide_fam = head_rec | {a["catalogue_id"] for a in pw}, head_fam | {a["family"] for a in pw}
    beside_rec = {a["catalogue_id"] for a in assoc_all if a["target_kind"] in rs.BESIDE_KINDS and not a["excluded_from_counts"]}
    recs_with_targets = sum(1 for e in entries if e["targets"])
    lv = lambda key, st: sum(1 for c in cells.values() if c[key]["state"] == st)
    reason_class = lambda a: a["excluded_reason"]
    per = {}
    kinds = ("intervention_target", "disease_gene_product", "pathway_member", "effector_constraint", "readout_marker")
    for nid, n in need_by.items():
        a_all = per_need[nid]["associations"]
        ok = lambda a: not a["excluded_from_counts"]
        by_kind = {k: {"records": len({a["catalogue_id"] for a in a_all if a["target_kind"] == k and ok(a)}), "families": len({a["family"] for a in a_all if a["target_kind"] == k and ok(a)})} for k in kinds}
        h = [a for a in a_all if counted(a)]
        wd = h + [a for a in a_all if pathway(a)]
        cs = [c for (r, k), c in cells.items() if k == nid]
        per[nid] = {"direction": rs.need_direction(n), "exploration_only": rs.need_direction(n) in ("uncertain", "modulate"),
                    "targets": len(n["targets"]), "target_kinds": dict(collections.Counter(t["target_kind"] for t in n["targets"])),
                    "headline_records_intervention_targets": len({x["catalogue_id"] for x in h}), "headline_families_intervention_targets": len({x["family"] for x in h}),
                    "records_incl_pathway_members": len({x["catalogue_id"] for x in wd}), "families_incl_pathway_members": len({x["family"] for x in wd}),
                    "by_target_kind_records_families": by_kind,
                    "families_consistent": len({x["family"] for x in h if x["consistency"] == "consistent"}),
                    "families_opposed": len({x["family"] for x in h if x["consistency"] == "opposed"}),
                    "families_with_both_consistent_and_opposed": len({x["family"] for x in h if x["consistency"] == "consistent"} & {x["family"] for x in h if x["consistency"] == "opposed"}),
                    "excluded_records_by_reason": dict(collections.Counter(reason_class(a) for a in {x["catalogue_id"]: x for x in a_all if x["excluded_from_counts"] and x["target_kind"] in (rs.LINK_KINDS | rs.PATHWAY_KINDS)}.values())),
                    "identity_guard_hits": len(per_need[nid]["identity_guard_hits"]), "nonhuman_chembl_rows_set_aside": per_need[nid]["nonhuman_chembl_rows_set_aside"],
                    "cells_L3_observed_wwox_system": sum(1 for c in cs if c["L3_observed_effect"]["state"] == "observed_wwox_system"),
                    "cells_L3_observed_vs_wild_type_only": sum(1 for c in cs if c["L3_observed_effect"]["state"] == "observed_vs_wild_type_only"),
                    "cells_L3_effect_in_wild_type_only": sum(1 for c in cs if c["L3_observed_effect"]["state"] == "effect_in_wild_type_only"),
                    "cells_L3_observed_case_level_only": sum(1 for c in cs if c["L3_observed_effect"]["state"] == "observed_case_level_only"),
                    "cells_L4_observed": sum(1 for c in cs if c["L4_observed_recovery_in_wwox_system"]["state"] != "none_in_record"),
                    "cards_citing_need": need_cards[nid], "wwox_system_observations": sum(1 for o in n["observed"] if o["evidence_scope"] == "WWOX_EXPERIMENT_IN_DEE_SYSTEM")}
    fam_needs = collections.defaultdict(set)
    for a in head:
        fam_needs[a["family"]].add(a["need"])
    dist = collections.Counter(len(v) for v in fam_needs.values())
    disp = collections.Counter(p["disposition"] for p in priorities["priorities"])
    disp_fam = {d: len({p["row_id"] for p in priorities["priorities"] if p["disposition"] == d}) for d in disp}
    listed = {(r["card_id"], r["assertion_id"]) for r in pert}
    all_a = {k for k, a in ass_index.items() if not cards[k[0]]["is_axis"] and a["epistemic_status"] == "DATO"}
    alias_rows = sorted({(a["catalogue_id"], a["compound"], a["target"]) for a in assoc_all if a["excluded_from_counts"] and a["excluded_from_counts"].startswith("alias_risk")})
    cell_states = lambda key: dict(sorted(collections.Counter(c[key]["state"] for c in cells.values()).items()))
    pend = sum(1 for _ in cells)
    out = {
        "schema": SCHEMA,
        "units": {"catalogue_records": len(entries), "records_are": "source-level substance records, not distinct drugs",
                  "families": len(fam_all), "chembl_families": len(chembl_fams), "source_only_families_unresolved_identity": len(fam_all - chembl_fams),
                  "family_rule": "ChEMBL parent link or identical InChIKey connectivity block; a source-only record joins a family only through relations.family_join (a merged gtopdb_ligand_chembl_ref reconciliation: GtoPdb ligand -> ChEMBL id, equal InChIKey, active id); otherwise it stays a singleton; nothing merged on name",
                  "coverage_unit": "compound families (each counted once per need); card interventions and tool subjects are separate rows"},
        "plain_statement": ("None of the interventions in this matrix is a catalogued repurposing candidate with a controlled recovery in a WWOX system. The only "
                            "experimental L4 cells are an AAV9 gene therapy (high dose, n 5 for spike-wave discharges; for growth, body weight only, blood glucose unchanged); "
                            "the other L4 cell is an uncontrolled case-level clinical report (vigabatrin); the ketogenic-diet record is retrospective, has no denominator and is not counted as L4. Ethosuximide, lithium and a tool compound (d-APV) have "
                            "single WWOX-system readouts without recovery status. Compound-target links are source statements, not evidence of effect."),
        "access_caveats": [f"{k}: {v['detail']}" for k, v in eff.items() if v["state"] == "PARTIAL"],
        "source_states": {k: {"state": v["state"], "detail": v["detail"]} for k, v in eff.items()},
        "source_state_vocabulary": "OK | STALE_EXPORT | STALE_AFTER_FAILED_REFRESH | PARTIAL | FAILED | INCOMPLETE | NOT_FETCHED; a hard problem (FAILED, INCOMPLETE, NOT_FETCHED) of a mechanism or identity source turns only the ABSENCE conclusions into incomplete_or_failed_query and flags every record (search_incompleteness); positive evidence from a working source is unchanged; a hard problem of an accessibility/status source only caveats access categories; stale states add a caveat to every absence-type result",
        "search_completeness": {"overall": "incomplete" if hard else "complete", "hard_problem_sources_by_role": source_roles_of(hard),
                                "mechanism_or_identity_sources_in_hard_state": [k for k in hard if SOURCE_ROLES.get(k, "mechanism") in MECHANISM_ROLES],
                                "accessibility_or_status_sources_in_hard_state": [k for k in hard if SOURCE_ROLES.get(k, "mechanism") not in MECHANISM_ROLES],
                                "records_whose_absence_conclusion_is_withheld": disp.get("incomplete_or_failed_query", 0),
                                "rule": "incompleteness of the search is visible on every record; only an absence that depends on a missing mechanism/identity source is withheld; positive evidence from a working source and accessibility errors do not blank the module"},
        "inputs_status": {"hard_problem_sources": hard, "stale_sources": stale, "stale_role_rows": stale_roles, "stale_pertinence_rows": stale_pert,
                          "cards_cited_by_needs_but_missing": missing_cards},
        "needs": {"count": len(need_by), "direction_evaluable": sum(1 for n in need_by.values() if rs.need_direction(n) not in ("uncertain", "modulate")),
                  "exploration_only": sum(1 for n in need_by.values() if rs.need_direction(n) in ("uncertain", "modulate")),
                  "needs_without_any_intervention_target_link": sorted(k for k, v in per.items() if v["headline_records_intervention_targets"] == 0),
                  "needs_with_headline_link_families": sum(1 for v in per.values() if v["headline_families_intervention_targets"] > 0),
                  "per_need": per},
        "catalogue_coverage": {
            "headline_definition": "TARGET LISTED (record count, not an action count) = a catalogue row on an INTERVENTION target (or disease gene product) of a need, excluding source-artefact rows, alias-risk rows and the DGIdb placeholder; pathway members counted apart; effector constraints and readout markers are never links",
            "records_examined": len(entries), "records_with_any_target_row": recs_with_targets,
            "headline_order": "action-stated records first (records_with_stated_action_on_a_need_target), then target-listed records (union_headline_records = all headline records, with or without a stated action); both are record/family counts and neither is an evidence-of-effect count",
            "records_with_stated_action_on_a_need_target": len(act_rec), "families_with_stated_action_on_a_need_target": len(act_fam),
            "union_headline_records": len(head_rec), "union_headline_families": len(head_fam),
            "records_target_listed": len(head_rec), "families_target_listed": len(head_fam),
            "records_target_listed_without_stated_action": len(head_rec - act_rec),
            "union_with_pathway_members_records": len(wide_rec), "union_with_pathway_members_families": len(wide_fam),
            "records_touching_only_effector_constraints_or_readout_markers": len(beside_rec - wide_rec),
            "pct_records_with_headline_link": pct(len(head_rec), len(entries), "catalogue records with at least one headline link to any of the needs / all catalogue records; links are source statements, not relevance"),
            "pct_records_with_target_row_that_link": pct(len(head_rec), recs_with_targets, "records with a headline link / records carrying any target row"),
            "pct_records_incl_pathway_members": pct(len(wide_rec), len(entries), "records with a headline OR pathway-member link / all catalogue records"),
            "excluded_rows": {"records": len({a["catalogue_id"] for a in excl}), "by_reason": dict(collections.Counter(reason_class(a) for a in {(a["catalogue_id"], a["need"], a["target"]): a for a in excl}.values())),
                              "alias_risk_rows_unresolved": [{"catalogue_id": c, "compound": n, "gene": g} for c, n, g in alias_rows]},
            "headline_records_by_strongest_relation": headline_by_relation(head),
            "touched_headline_families_with_a_name_twin_not_merged": sum(1 for f in head_fam if rows.get(f, {}).get("n_possible_duplicates", 0) > 0),
            "headline_families_if_name_twins_collapsed_SENSITIVITY_ONLY": collapsed_count(head_fam, rows),
            "families_by_number_of_needs_touched": {str(k): v for k, v in sorted(dist.items())},
            "overlap_warning": "needs share targets (e.g. CACNA1G, ABAT); per-need counts must not be added: use the unions above"},
        "evaluated_vs_records": {"records_in_catalogue": len(entries), "records_examined_by_target_match": len(entries),
                                 "records_with_target_data_at_all": recs_with_targets, "records_with_a_headline_link": len(head_rec),
                                 "interventions_with_a_listed_pertinent_readout_assertion": len({rid for (rid, _n), c in cells.items() if c["L3_observed_effect"]["state"] in ("observed_wwox_system", "observed_case_level_only", "measured_null_only")}),
                                 "meaning": "'examined' = target-matched against the needs; the last figure counts matrix rows (families or card interventions) with a pertinent WWOX-system readout or case report"},
        "matrix": {"rows": len(rows), "row_kinds": dict(collections.Counter(r["kind"] for r in rows.values())), "cells_nonempty": len(cells),
                   "cells_possible_rows_x_needs": len(rows) * len(need_by),
                   "L1_states": cell_states("L1_documented_link"), "L2_states": cell_states("L2_mechanistic_coherence"),
                   "L3_states": cell_states("L3_observed_effect"), "L4_states": cell_states("L4_observed_recovery_in_wwox_system"),
                   "levels_are_never_summed": True},
        "observations": {"card_interventions": len([c for c in cards.values() if not c["is_axis"]]), "axis_cards_not_interventions": len([c for c in cards.values() if c["is_axis"]]),
                         "data_assertions_in_intervention_cards": len(all_a), "assertions_listed_in_pertinence_table": len(listed & all_a),
                         "assertions_not_assessed_for_pertinence_not_counted": len(all_a - listed),
                         "listed_by_evidence_kind": dict(collections.Counter(r["evidence_kind"] for r in pert)),
                         "listed_by_sign": dict(collections.Counter(r["sign"] for r in pert)),
                         "note": "an assertion is counted per (assertion, need) row of the pertinence table; L3/L4 cells count (row, need) pairs"},
        "priorities": {"records": len(priorities["priorities"]), "by_disposition_cells": dict(sorted(disp.items())), "by_disposition_distinct_families_or_rows": dict(sorted(disp_fam.items())),
                       "all_dispositions_listed": sorted(DISPOSITIONS), "pairs_not_prioritised": priorities["pairs_not_prioritised"],
                       "exploration_flagged": sum(1 for p in priorities["priorities"] if p["exploration_only"])},
        "limits": ["catalogue links are source statements; no potency is carried", "DGIdb is a STALE export (2024-06-10); current service coverage not ingested", "ChEMBL non-human target rows are set aside, not matched",
                   "pertinence of an assertion to a need is judged in assertion_pertinence.tsv (a curated input, reviewable); unlisted assertions are not counted",
                   "L4 is a technical bridge comparison, not efficacy; case_level = uncontrolled clinical report", "needs' own WWOX observations are not interventions and fill no compound cell",
                   "seizure-need cells are symptom-level inferences, not mechanism-linked to WWOX; GRIN and T-type couplings rest on one experiment each"],
    }
    legacy_aliases(out)
    return out


def legacy_aliases(sm: dict) -> None:
    """Keys of the first schema revision, kept so existing consumers (the view) keep reading. They carry the NEW definitions
    (the legacy names say 'documented link'; the plain wording everywhere is 'target listed', and the action-stated subset is reported first):
    'documented link' = headline intervention-target listing, with or without a stated action; 'observed' = a pertinent WWOX-system readout or case report."""
    cc_ = sm["catalogue_coverage"]
    cc_["records_with_documented_link_to_a_need"] = cc_["union_headline_records"]
    cc_["families_with_documented_link_to_a_need"] = cc_["union_headline_families"]
    cc_["families_touching_at_least_one_need_counted_once"] = cc_["union_headline_families"]
    cc_["pct_records_with_link"] = cc_["pct_records_with_headline_link"]
    cc_["records_touching_only_readout_markers"] = cc_["records_touching_only_effector_constraints_or_readout_markers"]
    cc_["touched_families_with_a_name_twin_in_another_family_not_merged"] = cc_["touched_headline_families_with_a_name_twin_not_merged"]
    cc_["families_touching_a_need_if_name_twins_were_collapsed_SENSITIVITY_ONLY"] = cc_["headline_families_if_name_twins_collapsed_SENSITIVITY_ONLY"]
    sm["evaluated_vs_records"]["records_evaluated_against_wwox_needs_with_any_observation"] = sm["evaluated_vs_records"]["interventions_with_a_listed_pertinent_readout_assertion"]
    sm["priorities"]["by_disposition"] = sm["priorities"]["by_disposition_cells"]
    for v in sm["needs"]["per_need"].values():
        v["families_with_documented_link"] = v["headline_families_intervention_targets"]
        v["records_with_documented_link"] = v["headline_records_intervention_targets"]
        v["link_targets"] = sum(v["target_kinds"].get(k, 0) for k in ("intervention_target", "disease_gene_product"))
        v["cells_L3_observed"] = v["cells_L3_observed_wwox_system"] + v["cells_L3_observed_case_level_only"]
    m = sm["matrix"]
    m["L1_documented"] = m["L1_states"].get("documented", 0)
    m["L1_none_found"] = m["L1_states"].get("none_found", 0)
    m["L1_not_evaluable"] = m["L1_states"].get("not_evaluable", 0)
    m["L2_coherent"] = m["L2_states"].get("coherent", 0)
    m["L3_observed"] = m["L3_states"].get("observed_wwox_system", 0) + m["L3_states"].get("observed_case_level_only", 0)
    m["L4_observed"] = m["L4_states"].get("observed_experimental", 0) + m["L4_states"].get("observed_case_level", 0)


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
        print(json.dumps({"files": h, "matrix": sm["matrix"], "priorities": sm["priorities"]["by_disposition_cells"]}, indent=1))
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
