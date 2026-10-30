#!/usr/bin/env python3
"""Explainable, provisional, updatable ranking of the interventions LEGEND has identified (IT8 P9).

A research priority for VERIFICATION, never a prediction of clinical benefit, never a therapeutic recommendation, never medical advice.
Offline, deterministic (no clock, no network, no LLM), standard library only. It extends the existing coverage/view pipeline and adds no
score, no framework, no scheduler and no gate: it reads what the module already holds and writes ordinal GROUPS with visible components.

  ranking_it8.py run        regenerate every file of this directory from the module (about 15 s)
  ranking_it8.py check      exit 1 if any file differs from a fresh regeneration (idempotence: no new information, no change)
  ranking_it8.py snapshot --reason CLASS [--note TEXT]
                            append a dated snapshot of the unit table to snapshots/ and the per-unit changes to changes.tsv (only when the
                            ordering inputs changed since the last snapshot; --reason is required when a group moved)
  ranking_it8.py diff       print what changed since the last snapshot (groups, inputs) and the suggested reason class
  ranking_it8.py show [UNIT_ID]   print the table, or one unit with its reasons
  ranking_it8.py --help

Inputs (read, never copied): coverage/ (positions through repurposing_view, cells, priorities, pertinence), cards, needs, work order,
catalog/ (records, families via usable_compounds_it7_p2 record_usability.tsv.gz), pharmacological_comparison_it7_p5, the fulltext receipt ledger
(read-only, counts per cited PMID). The method and every definition are in README.md of this directory.
"""
from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import io
import json
import os
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
DR = HERE.parent
sys.path.insert(0, str(ROOT / "framework" / "scripts"))

RULES_VERSION = "R4"            # bump when a rule of this file changes meaning (reason class: method_revision)
SCHEMA = "legend.wwox.ranking/1"
USABLE = DR / "usable_compounds_it7_p2_20261029"
COMPARISON = DR / "pharmacological_comparison_it7_p5_20261029" / "comparison.tsv"
QUALIFICATION = DR / "pharmacological_qualification_it8_p3_20261029" / "comparison.tsv"      # IT8 P3, read when present (reuse, read-only)
RECEIPTS = ROOT / "disease-models/wwox/registries/fulltext_read_receipts.jsonl"
REASON_CLASSES = ("new_evidence", "counter_evidence", "identity_correction", "better_pharmacological_qualification", "context_change", "method_revision")
NON_ASSESSMENT_CHANGES = ("new_entry", "tie_resolution")

# ---- positions: two orders, both printed in the README -------------------------------------------------------------------------------
# lead across the needs of one objective (what is the strongest reason to study this unit?)
LEAD_ORDER = ["F1", "F2", "C2", "C1", "F3", "C3", "P3", "P2", "P1"]
# merge of two cards of one unit that speak on the SAME need: a counter position is never hidden behind a weaker favourable one
MERGE_ORDER = ["F1", "F2", "C2", "C1", "C3", "F3", "P3", "P2", "P1"]

GROUPS = {   # id -> (sort key, label, plain statement)
    "G1": (1, "Strongest WWOX-specific case today (in the mouse null)", "a favourable result in a WWOX system, read against an untreated comparator of the same genotype from a full or partial text, with no position-blocking flag and no null, unfavourable or mixed WWOX-system result beside it (position F1); a reading-quality screen on the rows the position rests on (it may rest on a single row, which the item states), not a size of effect and not a result of recovery after onset"),
    "G2a": (2, "Favourable but thin WWOX-system readout, specificity not in question", "a favourable result in a WWOX system with reading or design limits only (uncontrolled, graphical, one experiment, depth-limited), no null beside it, and none of the specificity flags below (position F2)"),
    "G2b": (3, "Favourable but thin, specificity uncertain or untested", "as G2a, and the favourable readout carries a specificity flag: it also occurs in wild type, or it was obtained with a tool compound, or no drug-by-genotype test exists, or the wild-type arm is floor-limited (position F2 with a specificity flag). Not having tested specificity is an unknown, never a clean reading; G2a versus G2b is not an efficacy order"),
    "G3": (4, "Tried in a WWOX system: results mixed, null or case-level", "favourable and null or unfavourable WWOX-system results side by side, or only a null one; the study is to learn which holds (positions C2, C1). The intervention is listed because it has been tried in a WWOX system, not because its favourable part is stronger than that of untried candidates; the class label of the unit describes the pertinence of the favourable part and is not a verdict"),
    "G4a": (5, "Target-based hypothesis, direction-consistent action documented", "no test of the intervention in a WWOX system; favourable support outside WWOX; the need has WWOX-system observations; a catalogue action coherent with the need's direction is documented (position F3). The documented action does not by itself support WWOX relevance: the need's WWOX observation may rest on a different intervention"),
    "G4b": (6, "Target-based hypothesis, direction not established", "as G4a but no documented direction-consistent action: the need's direction is uncertain, the action is unresolved, or the unit has no catalogue identity (position F3)"),
    "G5": (7, "Weak pertinence or counter-evidence outside WWOX", "no signed WWOX-system result of the intervention and either a harm or null signal outside WWOX with nothing favourable beside it, or a link by mechanism only (positions C3, P3)"),
    "GU": (8, "Not yet orderable: premise missing", "an abstention (a datum is missing before any test can be designed), no step named, or no linked need of this objective carries a position; NOT a finding that the unit is unpromising"),
}
GROUP_ORDER = sorted(GROUPS, key=lambda g: GROUPS[g][0])
IN_SELECTION = ("G1", "G2a", "G2b", "G3", "G4a")      # groups a selection may list; G4b and below are listed apart, never padded in

CLASSES = {
    "ORD": "EVALUATED AND ORDERABLE",
    "WEAK": "EVALUATED WITH WEAK PERTINENCE OR COUNTER-EVIDENCE",
    "INSUFF": "STILL INSUFFICIENTLY EVALUATED",
    "EXCL": "EXCLUDED FROM A SPECIFIC COMPARISON WITH REASON",
}
SPEC_FLAGS = ("nonspecific_also_in_wild_type", "no_drug_by_genotype_test", "control_variability_comparable_to_effect", "no_treated_wt_arm", "pharmacological_effect_in_wild_type_arm", "pharmacological_effect_in_heterozygous_arm")


def is_spec_flag(f: str) -> bool:
    return f in SPEC_FLAGS or f.startswith("tool_compound")


UNIT_TYPES = {"molecule": "molecule", "class_of_molecules": "class of molecules", "diet": "diet", "gene_therapy": "gene therapy / gene-based modality", "tool_compound": "tool compound",
              "tool_compound_and_class": "tool compound + class of molecules", "mechanism_probe": "mechanism probe (a compound or genetic tool used for a mechanism experiment, not a treatment)", "not_an_intervention": "not an intervention (axis)"}
ORIGINS = {"known_track_before_it9": "known track from before IT9", "generated_in_it9": "generated in IT9", "reference_or_control": "reference or control"}
CLASS_LEVEL_TYPES = ("class_of_molecules", "tool_compound_and_class")      # a result for a member or a tool is not a result for the other members
NX_LEVELS = {"NX1": "decisive: the discriminating next experiment would change a decision (lift or stop)", "NX2": "informative: the next experiment resolves one limit, the decision moves one step at most",
             "NX3": "low or none today: no discriminating next step is named, or the outcome could not change the decision before a premise exists"}

OBJECTIVES = {"broad": "deep_recovery", "partial": "partial_benefit"}
OBJ_LABEL = {"broad": "Broad, durable functional recovery", "partial": "Partial or bridge benefit"}

WWOX_KINDS = {"readout_in_wwox_system", "case_report_wwox_clinical"}
DEPTH_RANK = {"complete_fulltext_read": 4, "partial_fulltext_read": 3, "figure_or_supplement_read": 3, "abstract_only": 1, "queried_not_full_read": 1, "UNKNOWN": 0}


# ------------------------------------------------------------------------------------------------------------------------ small helpers
def jload(p: Path):
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def read_tsv(p: Path) -> list[dict]:
    with open(p, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def sha16(*parts) -> str:
    h = hashlib.sha256()
    for p in parts:
        h.update(json.dumps(p, sort_keys=True, ensure_ascii=False, default=str).encode("utf-8"))
        h.update(b"\x1f")
    return h.hexdigest()[:16]


def clip(t, n=240):
    t = re.sub(r"\s+", " ", str(t or "")).strip()
    return t if len(t) <= n else t[: n - 1].rstrip() + "…"


def cell(v) -> str:
    if v is None:
        return ""
    if isinstance(v, bool):
        return "yes" if v else "no"
    if isinstance(v, (list, tuple, set)):
        return "; ".join(str(x) for x in v)
    return re.sub(r"[\t\r\n]+", " ", str(v))


def tsv_bytes(rows: list[dict], cols: list[str]) -> bytes:
    out = io.StringIO()
    out.write("\t".join(cols) + "\n")
    for r in rows:
        out.write("\t".join(cell(r.get(c)) for c in cols) + "\n")
    return out.getvalue().encode("utf-8")


def gz_bytes(data: bytes) -> bytes:
    buf = io.BytesIO()
    with gzip.GzipFile(fileobj=buf, mode="wb", mtime=0, compresslevel=9) as g:
        g.write(data)
    return buf.getvalue()


def json_bytes(o) -> bytes:
    return (json.dumps(o, ensure_ascii=False, sort_keys=True, indent=1) + "\n").encode("utf-8")


SALT_WORDS = {"hydrochloride", "dihydrochloride", "hcl", "sodium", "calcium", "potassium", "magnesium", "mesylate", "citrate", "sulfate", "sulphate", "phosphate",
              "acetate", "tartrate", "maleate", "fumarate", "succinate", "bromide", "chloride", "free", "base", "polistirex", "hydrobromide", "besylate", "dimesylate",
              "disodium", "monohydrate", "hydrate", "anhydrous", "lysine", "tosylate"}


def display_group_key(name: str) -> str:
    """Display grouping of name twins and salts: lower-case, punctuation out, salt words out. NOT identity: the family key stays the identity, members are all listed."""
    toks = [t for t in re.sub(r"[^a-z0-9]+", " ", (name or "").lower()).split() if t not in SALT_WORDS]
    return " ".join(toks) or re.sub(r"[^a-z0-9]+", " ", (name or "").lower()).strip()


# ------------------------------------------------------------------------------------------------------------------------ load
def load_all() -> dict:
    import repurposing_view as v
    P = v.build_payload(DR, "full", with_ranking=False)
    cur = P["cur"]
    ctx = {
        "cur": cur,
        "cands": {c["id"]: c for c in cur["cands"]},
        "needs": {n["id"]: n for n in cur["needs"]},
        "wo": {e["need"]: e for e in cur["work_order"]["entries"]},
        "matrix": jload(DR / "coverage/coverage_matrix.json"),
        "prios": jload(DR / "coverage/priorities.json"),
        "pert": read_tsv(DR / "coverage/assertion_pertinence.tsv"),
        "comparison": read_tsv(COMPARISON),
        "unit_map": read_tsv(HERE / "unit_map.tsv"),
        "summary": jload(DR / "coverage/coverage_summary.json"),
        "gen_from": jload(DR / "coverage/coverage_matrix.json").get("generated_from", {}),
        "hyp": {h["id"]: h for h in cur["hypotheses"]},
    }
    ctx["uncarded"] = read_tsv(HERE / "uncarded_items.tsv")
    ctx["caveats"] = read_tsv(HERE / "unit_caveats.tsv")
    ctx["qualification_all"] = load_qualification()
    ctx["qualification"] = read_tsv(QUALIFICATION) if QUALIFICATION.exists() else []
    return ctx


def load_catalog() -> dict:
    p = DR / "catalog/catalog.jsonl.gz"
    ents = {}
    with gzip.open(p, "rt", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                e = json.loads(line)
                ents[e["id"]] = e
    return ents


def load_usability() -> dict:
    fam: dict[str, dict] = {}
    with gzip.open(USABLE / "record_usability.tsv.gz", "rt", encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            d = fam.setdefault(r["family_id"], {"records": [], "target": 0, "action": 0, "mnet": 0, "msn": "0", "msa": "0"})
            d["records"].append(r["record_id"])
            d["target"] |= int(r["any_target_row"] == "1")
            d["action"] |= int(r["stated_action"] == "1")
            d["mnet"] |= int(r["Mnet_usable"] == "1")
            for k, col in (("msn", "Msig_neural_strict"), ("msa", "Msig_any_context")):
                v_ = r[col]
                if v_ == "1" or (v_ not in ("0", "1") and d[k] == "0"):
                    d[k] = "1" if v_ == "1" else "?"
    return fam


def ledger_lines() -> int:
    if not RECEIPTS.exists():
        return 0
    with open(RECEIPTS, encoding="utf-8") as f:
        return sum(1 for line in f if line.strip())


def receipts_by_pmid() -> dict:
    out: dict[str, list[str]] = defaultdict(list)
    if RECEIPTS.exists():
        with open(RECEIPTS, encoding="utf-8") as f:
            for line in f:
                if not line.strip():
                    continue
                try:
                    r = json.loads(line)
                except ValueError:
                    continue
                pm = str((r.get("study_id") or {}).get("pmid") or "")
                if pm:
                    out[pm].append(str(r.get("event_id")))
    return out


# ------------------------------------------------------------------------------------------------------------------------ units
def build_units(ctx: dict, cat: dict) -> list[dict]:
    cands, needs, wo, pert = ctx["cands"], ctx["needs"], ctx["wo"], ctx["pert"]
    mapped = [c for r in ctx["unit_map"] for c in r["cards"].split(";") if c]
    missing = sorted(set(cands) - set(mapped))
    dup = sorted(c for c, n in Counter(mapped).items() if n > 1)
    unknown = sorted(set(mapped) - set(cands))
    if missing or dup or unknown:
        raise SystemExit(f"unit_map.tsv does not cover the cards exactly once: missing {missing} duplicated {dup} unknown {unknown}")
    cells_by_card: dict[str, list[dict]] = defaultdict(list)
    rows_by_id = {r["row_id"]: r for r in ctx["matrix"]["rows"]}
    for c in ctx["matrix"]["cells"]:
        for cd in rows_by_id[c["row_id"]].get("cards") or []:
            cells_by_card[cd["card_id"] if isinstance(cd, dict) else cd].append(c)
    receipts = receipts_by_pmid()
    comp_by_card: dict[str, dict] = {}
    for r in ctx["comparison"]:
        for c in r["hypothesis_cards"].split(";"):
            comp_by_card[c.strip()] = r
    qual_by_card: dict[str, list[dict]] = defaultdict(list)
    for q in ctx.get("qualification") or []:
        toks = set(re.findall(r"[A-Za-z0-9-]+", q["cards_and_needs"].split("->")[0] + " " + q["cards_and_needs"]))
        for cid in cands:
            if cid in q["cards_and_needs"] or cid.split("_")[0] in toks:
                qual_by_card[cid].append(q)
    prios_by_row_need = defaultdict(list)
    for p in ctx["prios"]["priorities"]:
        prios_by_row_need[(p["row_id"], p["need"])].append(p)
    units = []
    for m in ctx["unit_map"]:
        cards = [c for c in m["cards"].split(";") if c]
        if m.get("unit_type") not in UNIT_TYPES or m.get("origin") not in ORIGINS:
            raise SystemExit(f"unit_map.tsv: {m['unit_id']} needs a valid unit_type ({', '.join(UNIT_TYPES)}) and origin ({', '.join(ORIGINS)}); got {m.get('unit_type')!r} / {m.get('origin')!r}")
        u = {"unit_id": m["unit_id"], "label": m["label"], "kind": m["kind"], "unit_type": m["unit_type"], "origin": m["origin"], "cards": cards, "merge_reason": m["merge_reason"],
             "excluded": m["excluded"] == "yes", "excluded_reason": m["excluded_reason"]}
        # ---- positions per need (merge of the unit's cards on the same need) --------------------------------------------------------
        per_need: dict[str, dict] = {}
        for cid in cards:
            for nid, lk in (cands[cid].get("links") or {}).items():
                e = per_need.setdefault(nid, {"by_card": {}, "links": {}})
                e["by_card"][cid] = lk["group"]
                e["links"][cid] = lk
        for nid, e in per_need.items():
            e["position"] = min(e["by_card"].values(), key=MERGE_ORDER.index)
            e["conflict"] = len(set(e["by_card"].values())) > 1
            e["lead_card"] = sorted(e["by_card"], key=lambda cc: (MERGE_ORDER.index(e["by_card"][cc]), cc))[0]
        u["per_need"] = per_need
        u["declared_goals"] = sorted({cands[c]["goal"] for c in cards})
        u["tracks"] = sorted({cands[c]["track"] for c in cards if cands[c].get("track")})
        u["abstention_cards"] = [c for c in cards if cands[c]["abstention"]]
        u["cells"] = [c for cid in cards for c in cells_by_card.get(cid, [])]
        # ---- members (catalogue families tied to the unit's cards) ----------------------------------------------------------------
        members = []
        for r in ctx["matrix"]["rows"]:
            att = [(cd["card_id"], cd["attachment"]) for cd in (r.get("cards") or []) if isinstance(cd, dict) and cd["card_id"] in cards]
            if att and (r["kind"] == "molecule_family" or r["kind"].startswith("tool_compound")):
                members.append((r, att))
        u["members"] = members
        # ---- pertinence rows --------------------------------------------------------------------------------------------------------
        u["pert"] = [r for r in pert if r["card_id"] in cards]
        u["asserts"] = [a for cid in cards for a in cands[cid].get("asserts") or []]
        pm = []
        for cid in cards:
            for p in cands[cid].get("pmids") or []:
                pm.append(str(p["id"]))
            for a in cands[cid].get("asserts") or []:
                pm.extend(str(x) for x in a.get("pmids") or [])
        u["pmids"] = sorted(set(pm))
        u["receipts"] = {p: len(receipts.get(p, [])) for p in u["pmids"]}
        u["comparison"] = [comp_by_card[c] for c in cards if c in comp_by_card]
        u["qualification"] = sorted({q["case_id"]: q for c in cards for q in qual_by_card.get(c, [])}.values(), key=lambda q: q["case_id"])
        units.append(u)
    return units


def card_goal_needs(ctx: dict, objective: str) -> set[str]:
    return {n for n, nd in ctx["needs"].items() if nd["goal"] == OBJECTIVES[objective]}


def wwox_favourable_flags(u: dict, need: str) -> set[str]:
    out: set[str] = set()
    for r in u["pert"]:
        if r["need_id"] == need and r["evidence_kind"] in WWOX_KINDS and r["sign"] in ("benefit", "partial_benefit"):
            out |= {f for f in (r["flags"] or "").split(";") if f}
    return out


def coherent_on(u: dict, need: str) -> bool:
    return any(c["need"] == need and c["L2_mechanistic_coherence"]["state"] == "coherent" for c in u["cells"])


def view_assessment(u: dict, ctx: dict, obj: str) -> dict:
    needs_obj = card_goal_needs(ctx, obj)
    declared = OBJECTIVES[obj] in u["declared_goals"]
    pos = {n: e["position"] for n, e in u["per_need"].items() if n in needs_obj}
    out = {"objective": obj, "declared": declared, "positions": dict(sorted(pos.items())), "member": declared or bool(pos)}
    if not out["member"]:
        return out
    real = {n: p for n, p in pos.items() if p not in ("P1", "P2")}
    if not real:
        lead_need, lead = None, None
        reason = ("declared objective of the card, no linked need of this objective carries a position" if not pos else "every position on this objective is a premise-missing abstention (P1/P2)")
        out.update({"lead": lead, "lead_need": lead_need, "group": "GU", "evidence_quality": "premise_missing", "group_reason": reason, "contested": False, "counter_needs": []})
        return out
    lead_need = sorted(real, key=lambda n: (LEAD_ORDER.index(real[n]), 0 if coherent_on(u, n) else 1, n))[0]
    lead = real[lead_need]
    counter_needs = sorted(n for n, p in real.items() if p in ("C1", "C2", "C3") and n != lead_need)
    if lead == "F1":
        g = "G1"
    elif lead == "F2":
        flags = wwox_favourable_flags(u, lead_need)
        g = "G2b" if any(is_spec_flag(f) for f in flags) else "G2a"
    elif lead in ("C1", "C2"):
        g = "G3"
    elif lead == "F3":
        g = "G4a" if coherent_on(u, lead_need) else "G4b"
    else:
        g = "G5"
    evq = {"G1": "favourable_with_comparator_may_rest_on_one_row", "G2a": "favourable_thin", "G2b": "favourable_thin_specificity_uncertain", "G3": "contested", "G4a": "no_wwox_test_target_supported", "G4b": "no_wwox_test_target_hypothesis", "G5": "weak_pertinence_or_outside_counter"}[g]
    out.update({"lead": lead, "lead_need": lead_need, "group": g, "evidence_quality": evq, "contested": lead in ("F1", "F2", "F3") and bool(counter_needs), "counter_needs": counter_needs,
                "group_reason": GROUPS[g][2]})
    return out


def lead_need_summary(u: dict, need: str | None) -> dict:
    if not need:
        return {}
    seen, signs = set(), Counter()
    for r in u["pert"]:
        if r["need_id"] == need and r["evidence_kind"] in WWOX_KINDS and (r["card_id"], r["assertion_id"]) not in seen:
            seen.add((r["card_id"], r["assertion_id"]))
            signs[r["sign"]] += 1
    outside = Counter()
    for r in u["pert"]:
        if r["need_id"] == need and r["evidence_kind"] in ("readout_other_disease", "safety_signal", "label_statement", "target_engagement_assay"):
            outside[(r["evidence_kind"], r["sign"])] += 1
    nobs = sum(v for (k, sg), v in outside.items() if sg in ("null", "harm"))
    nfav = sum(v for (k, sg), v in outside.items() if sg in ("benefit", "partial_benefit"))
    return {"wwox_signs": dict(sorted(signs.items())), "wwox_null_harm_mixed": sum(v for k, v in signs.items() if k in ("null", "harm", "mixed")), "outside_favourable": nfav, "outside_null_or_harm": nobs}


def unit_class(u: dict) -> tuple[str, str]:
    if u["excluded"]:
        return "EXCL", u["excluded_reason"]
    leads = {n: e["position"] for n, e in u["per_need"].items()}
    real = {n: p for n, p in leads.items() if p not in ("P1", "P2")}
    if any(p in ("F1", "F2", "F3") for p in real.values()):
        return "ORD", "at least one linked need has a favourable position (F1, F2 or F3) after the merge of the unit's cards; the group says how strong"
    if real:
        return "WEAK", "evaluated at card level; every position is counter-evidence (C1-C3) or a mechanism-only link (P3), none favourable"
    return "INSUFF", "every card of the unit is an abstention or names no step: a datum is missing before a test can be designed; not placed at the bottom"


# ------------------------------------------------------------------------------------------------------------------------ components
def counts_of(rows: list[dict], key: str) -> dict:
    return dict(sorted(Counter(r[key] for r in rows).items()))


def component_wwox(u: dict) -> dict:
    seen = set()
    wr = []
    for r in u["pert"]:
        k = (r["card_id"], r["assertion_id"])
        if r["evidence_kind"] in WWOX_KINDS and k not in seen:
            seen.add(k)
            wr.append(r)
    signs = Counter(r["sign"] for r in wr)
    wt_only = len({(r["card_id"], r["assertion_id"]) for r in u["pert"] if r["evidence_kind"] in ("genotype_comparison_vs_wild_type", "effect_in_wild_type_arm")})
    asserts = {(a["id"]): a for a in u["asserts"]}
    fav_pm = sorted({str(p) for r in wr if r["sign"] in ("benefit", "partial_benefit") for p in (asserts.get(r["assertion_id"], {}).get("pmids") or [])})
    depth_known = sum(1 for r in wr if (asserts.get(r["assertion_id"], {}).get("depth") or "UNKNOWN") not in ("UNKNOWN", "abstract_only", "queried_not_full_read"))
    l4 = Counter(c["L4_observed_recovery_in_wwox_system"]["state"] for c in u["cells"])
    state = "none: no result of the intervention in a WWOX system recorded"
    if wr:
        state = f"{len(wr)} WWOX-system or WWOX case-report assertion(s): " + ", ".join(f"{n} {s}" for s, n in sorted(signs.items()))
        l4n = {k: v for k, v in l4.items() if k not in ("none_in_record",)}
        if l4n:
            state += "; L4 technical comparison (opposes the disease change, not efficacy): " + ", ".join(f"{k} in {v} cell(s)" for k, v in sorted(l4n.items()))
    return {"wwox_assertions": len(wr), "signs": dict(sorted(signs.items())), "wild_type_only_assertions": wt_only, "favourable_distinct_pmids": fav_pm,
            "read_beyond_abstract": depth_known, "l4_states": dict(sorted(l4.items())), "text": state,
            "replication": ("none recorded: one source paper" if len(fav_pm) <= 1 else f"{len(fav_pm)} papers; independence of the groups is not established by this table (shared authors are not excluded)") if wr else "not applicable (no result)"}


def component_mechanism(u: dict) -> dict:
    fam_rows = {r["row_id"]: r for r, _ in u["members"] if r["kind"] == "molecule_family"}
    cells = [c for c in u["cells"] if c["row_id"] in fam_rows]
    l2 = Counter(c["L2_mechanistic_coherence"]["state"] for c in cells)
    l1 = Counter(c["L1_documented_link"]["state"] for c in cells)
    fams = sorted(fam_rows)
    opposed = sorted({c["need"] for c in cells if c["L2_mechanistic_coherence"]["state"] == "opposed"})
    if not fams and u["kind"].startswith("modality"):
        txt = "modality acting on WWOX dosage or transcript itself: no drug-target identity applies (not a compound question); coherence with the need is by design, not by a catalogue action"
    elif not fams:
        txt = "no catalogue identity: target identity, direction of action and link to the need are NOT EVALUABLE here (UNKNOWN, not zero)"
    else:
        txt = f"{len(fams)} catalogue family(ies); L2 over {len(cells)} (family, need) cell(s): " + (", ".join(f"{n} {s}" for s, n in sorted(l2.items())) or "no cell")
    return {"families": fams, "l1": dict(sorted(l1.items())), "l2": dict(sorted(l2.items())), "opposed_needs": opposed, "text": txt}


def component_transfer(u: dict, ctx: dict) -> dict:
    cands = ctx["cands"]
    wr = [a for a in u["asserts"] if a.get("scope", "").startswith("WWOX_EXPERIMENT") or a.get("scope") == "WWOX_CLINICAL_CASE"]
    species = sorted({a.get("species") or "UNKNOWN" for a in wr})
    genos = sorted({clip(a.get("genotype") or "UNKNOWN", 60) for a in wr})
    win = []
    for cid in u["cards"]:
        for w in (ctx["cur"]["work_order"].get("card_windows") or {}).get(cid, []) if isinstance(ctx["cur"]["work_order"].get("card_windows"), dict) else []:
            win.append(w)
    tl = [clip(cands[c].get("transfer_limits"), 260) for c in u["cards"] if cands[c].get("transfer_limits")]
    return {"track": u["tracks"], "species_of_wwox_assertions": species or ["none (no result in a WWOX system)"], "genotypes": genos, "transfer_limits": tl,
            "window_note": win}


def component_pharm(u: dict, ctx: dict) -> dict:
    comp = u["comparison"]
    if comp:
        c = comp[0]
        d = {"state": "class-level table (IT7 P5); potency in a WWOX system UNKNOWN", "potency_with_assay_context": clip(c["potency_with_assay_context"], 420),
             "human_exposure": clip(c["human_exposure"], 300), "brain_penetration": clip(c["brain_penetration"], 300), "record": c["record_id"]}
    else:
        ph = [clip(ctx["cands"][c].get("pharm"), 300) for c in u["cards"] if ctx["cands"][c].get("pharm")]
        d = {"state": "not in the pharmacological comparison table; card text only (potency, exposure and nervous-system data UNKNOWN unless the card says otherwise)",
             "potency_with_assay_context": ph[0] if ph else "UNKNOWN", "human_exposure": "UNKNOWN", "brain_penetration": "UNKNOWN", "record": ""}
    qs = u.get("qualification") or []
    if qs:
        d["qualification"] = [{"case": q["case_id"], "status": q["decision_status"], "new_decision": clip(q["new_decision"], 200), "quantitative": clip(q["quantitative_measures_by_assay_type_not_aggregated"], 500),
                               "human_exposure": clip(q["human_exposure"], 300), "nervous_system_data": clip(q["nervous_system_data"], 300), "contrary": clip(q["contrary_signals"], 300), "unknown": clip(q["unknown_signals"], 300)} for q in qs]
        d["state"] += "; qualified in IT8 P3 (" + ", ".join(q["case_id"] for q in qs) + "): measures by assay type, never aggregated; a binding or enzyme measure is not functional benefit"
    return d


def component_counter(u: dict, ctx: dict) -> dict:
    nul = sorted({(r["card_id"], r["assertion_id"]) for r in u["pert"] if r["evidence_kind"] in WWOX_KINDS and r["sign"] in ("null", "harm", "mixed")})
    outside = sorted({(r["card_id"], r["assertion_id"]) for r in u["pert"] if r["evidence_kind"] in ("readout_other_disease", "safety_signal", "label_statement") and r["sign"] in ("null", "harm")})
    need_ctr = 0
    for nid in u["per_need"]:
        need_ctr += len(ctx["needs"][nid].get("counter") or [])
    tags = sorted({t for e in u["per_need"].values() for lk in e["links"].values() for t in lk.get("tags") or []})
    cm = component_mechanism(u)
    return {"wwox_null_harm_mixed": len(nul), "outside_wwox_null_or_harm": len(outside), "need_level_counter_items": need_ctr, "need_level_counter_items_note": f"over {len(u['per_need'])} linked need(s); items of the need record, not of the intervention",
            "opposed_action_needs": cm["opposed_needs"], "tags": tags}


def component_uncertainty(u: dict) -> dict:
    pn = u["per_need"]
    n = len(pn)
    meas = sum(1 for e in pn.values() if e["position"] in ("F1", "F2", "C1", "C2"))
    hyp = sum(1 for e in pn.values() if e["position"] == "F3")
    mech_only = sum(1 for e in pn.values() if e["position"] in ("P3", "C3"))
    prem = sum(1 for e in pn.values() if e["position"] in ("P1", "P2"))
    unknown = ["potency in a WWOX system", "exposure in a WWOX-deficient nervous system", "dose-response in a WWOX system"]
    return {"linked_needs": n, "measured_in_wwox_system": meas, "hypothesised_from_target": hyp, "mechanism_only_or_outside_counter": mech_only, "premise_missing": prem,
            "unknown": unknown, "text": f"of {n} linked need(s): {meas} with a measured WWOX-system result, {hyp} hypothesised from the target, {mech_only} mechanism-only or counter-signal, {prem} premise missing"}


# ------------------------------------------------------------------------------------------------------------------------ access, evidence, next, change
def access_class(scope: str) -> str:
    """Licence class of the source that states an access category (view/shareable_sources.json: access_scope_sources)."""
    if "openFDA NDC" in scope or "Every Cure MATRIX" in scope:
        return "A"
    if "ChEMBL" in scope:
        return "B"
    if "DSLD" in scope:
        return "C"
    return "unclassified"


def access_text(u: dict, cat: dict, ctx: dict) -> tuple[str, list[str], list[dict]]:
    if u["kind"] in ("diet",):
        return "dietary regimen; no product register applies; access not assessed", [], []
    if u["kind"].startswith("modality"):
        return "not a product listing (gene-based modality); access UNKNOWN", [], []
    items, cats = [], set()
    for r, att in u["members"]:
        rep = cat.get(r.get("representative") or "")
        if not rep:
            continue
        for a in rep.get("access") or []:
            cats.add(a["category"])
            sc = a.get("scope", "")
            m = re.search(r"(\d{4}-\d\d-\d\d)", sc)
            items.append({"member": r["name"].title(), "category": a["category"], "jurisdiction": "US" if sc.startswith("US") else "jurisdiction not stated",
                          "source": clip(re.sub(r"^US,\s*", "", sc).split(":")[0], 60), "strength": a.get("strength", "strength n/a"),
                          "date": m.group(1) if m else (str(a.get("retrieved_utc") or "")[:10] or "date not stated"), "licence_class": access_class(sc)})
    items = sorted({json.dumps(i, sort_keys=True) for i in items})
    items = [json.loads(i) for i in items]
    parts = [f"{i['member']}: {i['category']} ({i['jurisdiction']}; {i['source']}; {i['strength']}; {i['date']})" for i in items]
    if not parts:
        card_acc = sorted({x for c in u["cards"] for x in ctx["cands"][c].get("access") or []})
        return ("class level, no named catalogue identity; access categories from the cards: " + (", ".join(card_acc) if card_acc else "UNKNOWN")), card_acc, []
    return " | ".join(parts[:6]) + (f" | (+{len(parts) - 6} more)" if len(parts) > 6 else "") + " -- descriptive listing evidence, not efficacy or safety", sorted(cats), items


def best_evidence(u: dict, need: str | None) -> dict:
    rank = lambda a: (DEPTH_RANK.get(a.get("depth") or "UNKNOWN", 0), a["id"])
    by_id = {a["id"]: a for a in u["asserts"]}
    fav_ids = {r["assertion_id"] for r in u["pert"] if r["evidence_kind"] in WWOX_KINDS and r["sign"] in ("benefit", "partial_benefit") and (not need or r["need_id"] == need)}
    fav_all = {r["assertion_id"] for r in u["pert"] if r["evidence_kind"] in WWOX_KINDS and r["sign"] in ("benefit", "partial_benefit")}
    wr = [by_id[i] for i in sorted(fav_all) if i in by_id]
    pick, carrier = None, False
    if need and need in u["per_need"]:
        carr = [str(c).split(":")[0].strip() for lk in u["per_need"][need]["links"].values() for c in lk.get("carrier") or []]
        c0 = [by_id[i] for i in carr if i in by_id]
        if c0:
            pick, carrier = c0[0], True
    if not pick:
        c1 = [by_id[i] for i in sorted(fav_ids) if i in by_id]
        if c1:
            pick = sorted(c1, key=rank, reverse=True)[0]
    if not pick and wr:
        pick = sorted(wr, key=rank, reverse=True)[0]
    others = len([a for a in wr if pick and a["id"] != pick["id"]])
    if pick:
        flags = sorted({f for r in u["pert"] if r["assertion_id"] == pick["id"] for f in (r["flags"] or "").split(";") if f})
        inw = pick.get("scope") in ("WWOX_EXPERIMENT_IN_DEE_SYSTEM", "WWOX_CLINICAL_CASE")
        return {"in_wwox": inw, "carrier_of_position": carrier, "id": pick["id"], "text": clip(pick.get("text"), 220), "scope": pick.get("scope"), "species": pick.get("species"), "genotype": clip(pick.get("genotype"), 60),
                "depth": pick.get("depth"), "pmids": pick.get("pmids") or [], "flags": flags, "other_favourable_wwox_assertions": others}
    oth = [a for a in u["asserts"] if a.get("sign") in ("benefit", "partial_benefit")]
    if oth:
        a = sorted(oth, key=rank, reverse=True)[0]
        return {"in_wwox": False, "carrier_of_position": False, "id": a["id"], "text": clip(a.get("text"), 220), "scope": a.get("scope"), "species": a.get("species"), "genotype": clip(a.get("genotype"), 60), "depth": a.get("depth"),
                "pmids": a.get("pmids") or [], "flags": sorted({f for r in u["pert"] if r["assertion_id"] == a["id"] for f in (r["flags"] or "").split(";") if f}), "other_favourable_wwox_assertions": 0}
    return {"in_wwox": False, "carrier_of_position": False, "id": "", "text": "none recorded", "scope": "", "species": "", "genotype": "", "depth": "", "pmids": [], "flags": [], "other_favourable_wwox_assertions": 0}


def next_step(u: dict, ctx: dict, need: str | None) -> dict:
    wo = ctx["wo"].get(need) if need else None
    if wo:
        return {"kind": wo.get("kind"), "question": clip(wo.get("question"), 360), "would_change": clip(wo.get("would_change"), 360), "feasibility": clip(wo.get("feasibility"), 240), "need": need,
                "date": wo.get("date")}
    c = ctx["cands"][u["cards"][0]]
    return {"kind": "", "question": clip(c.get("next"), 360), "would_change": "", "feasibility": "not stated", "need": need or "", "date": ""}


def criteria_not_met(u: dict, need: str | None) -> list[str]:
    if not need:
        return []
    e = u["per_need"].get(need)
    if not e:
        return []
    lk = e["links"][e["lead_card"]]
    return [c["text"] for c in lk.get("criteria") or [] if not c.get("met")]


def change_triggers(u: dict, va: dict | None, need: str | None) -> dict:
    lead = va.get("lead") if va else None
    nm = criteria_not_met(u, need)
    rise = {
        "F1": "already at the top group; it holds while no null, unfavourable or mixed WWOX-system result appears beside it",
        "F2": "would rise to G1 if one and the same readout met the criteria not met now: " + ("; ".join(nm) if nm else "none listed"),
        "C2": "would rise if the null or mixed rows were shown to be an artefact of dose, timing, genotype or reading depth and a controlled, unflagged favourable readout stood alone",
        "C1": "would rise only if the null result were shown to be an artefact (dose, timing, genotype, reading depth) and a favourable result obtained",
        "F3": "would rise to F2/F1 with a first signed result of the intervention in a WWOX system against an untreated same-genotype comparator; criteria not met now: " + ("; ".join(nm) if nm else "none listed"),
        "C3": "would rise if the harm or null signal were shown not to apply to a WWOX system and a favourable signal were recorded",
        "P3": "would rise if the card recorded a favourable signal for the intervention on this need, or the need acquired a WWOX-system observation",
    }.get(lead or "", "would leave the premise-missing group when the card names the missing datum as obtained or a first test")
    fall = ("a signed null, unfavourable or mixed result beside the favourable rows lowers the group by one step; a counter-evidence group (C1/C2) is reached only when the null stands as the lead; "
            "for a thin readout, a failed replication or a drug-by-genotype test showing the effect in wild type too moves it down within the group")
    leave = "the decisive premise is falsified (see the card's 'premise missing' / 'not known' fields), or the identity is corrected so that the evidence attaches to a different compound"
    return {"rise": rise, "fall": fall, "leave": leave}


def needs_overview(u: dict, ctx: dict) -> list[dict]:
    out = []
    for nid in sorted(u["per_need"]):
        e = u["per_need"][nid]
        nd = ctx["needs"][nid]
        cells = [c for c in u["cells"] if c["need"] == nid]
        l1 = Counter(c["L1_documented_link"]["state"] for c in cells)
        l2 = Counter(c["L2_mechanistic_coherence"]["state"] for c in cells)
        l3 = Counter(c["L3_observed_effect"]["state"] for c in cells)
        l4 = Counter(c["L4_observed_recovery_in_wwox_system"]["state"] for c in cells)
        if any(s in ("observed_wwox_system", "observed_case_level_only", "observed_depth_unknown") for s in l3):
            ev = "effect_observed_in_wwox_system"
        elif l2.get("coherent"):
            ev = "directionally_compatible_documented_action"
        elif l1.get("documented"):
            ev = "documented_association_target_listed"
        elif any(s.startswith("precedent_other_disease") for s in l3):
            ev = "other_disease_precedent_only"
            if any(r["need_id"] == nid and "WWOX_patients" in (r["flags"] or "") for r in u["pert"]):
                ev = "other_disease_precedent_plus_wwox_case_level_signal"
        else:
            ev = "card_inference_by_mechanism_no_catalogue_row"
        out.append({"need": nid, "need_short": nd["short"], "thread": nd["thread"], "objective": "broad" if nd["goal"] == "deep_recovery" else "partial", "need_direction": nd["dir"],
                    "position": e["position"], "position_by_card": e["by_card"], "same_need_conflict": e["conflict"], "link_evidence": ev,
                    "l1": dict(l1), "l2": dict(l2), "l3": dict(l3), "l4": dict(l4), "opposed_action": bool(l2.get("opposed")),
                    "computational_prediction": "none: card-linked families were firewalled out of the IT7 P3 comparison (exploratory, minimum detectable effect about 0.157)",
                    "wwox_observations_on_need": nd["n_wwox_obs"]})
    return out


def depth_label(u: dict, comp: dict) -> tuple[str, str]:
    if u["excluded"]:
        return "n/a", "not an intervention"
    if all(c in u["abstention_cards"] for c in u["cards"]):
        d, t = "E2", "card reviewed, abstention (premise named, no test designed)"
    elif comp["read_beyond_abstract"]:
        d, t = "E4", f"card reviewed, {comp['read_beyond_abstract']} WWOX-side assertion(s) read beyond abstract"
    else:
        d, t = "E3", "card reviewed with assertions; no WWOX-side result read beyond abstract"
    if u["comparison"]:
        t += "; class pharmacology table (IT7 P5)"
    return d, t


_FAMREC: dict = {}


def family_records() -> dict:
    if not _FAMREC:
        _FAMREC.update({k: set(v["records"]) for k, v in load_usability().items()})
    return _FAMREC


def attribute_rows(u: dict) -> list[dict]:
    """Member-level attribution of the pertinence rows of one intervention. A row is attributed ONLY to the member its subject names (a catalogue record of the member's
    family; a tool compound for the tool subjects of its card). A card-level row ('card') belongs to the molecule/diet/vector for single interventions, to the named
    identity of the card when the card has one, and otherwise to the CLASS/MECHANISM level, never to a member. A result for a tool compound or for one member is
    therefore never a result for another member."""
    fr = family_records()
    members = []
    for r, att in u["members"]:
        if r["kind"] == "molecule_family":
            members.append({"key": r["row_id"], "name": r["name"].title(), "type": "molecule", "records": fr.get(r["row_id"], set()) | {"CAT:" + r["row_id"].split(":")[-1]},
                            "identity_cards": sorted({c for c, a in att if a == "identity"}), "cards": sorted({c for c, _ in att}), "rows": []})
        else:
            members.append({"key": r["row_id"], "name": u.get("tool_names", {}).get(sorted({c for c, _ in att})[0]) or f"tool compound(s) or precedent named in card {sorted({c for c, _ in att})[0]}", "type": "tool_compound", "records": set(), "identity_cards": [],
                            "cards": sorted({c for c, _ in att}), "rows": []})
    single = u["unit_type"] in ("molecule", "diet", "gene_therapy")
    self_m = {"key": "UNIT", "name": u["label"], "type": u["unit_type"], "records": set(), "identity_cards": [], "cards": u["cards"], "rows": []}
    class_m = {"key": "CLASS", "name": "class or mechanism level (card-level assertions and unnamed members)", "type": "class_level", "records": set(), "identity_cards": [], "cards": u["cards"], "rows": []}
    for r in u["pert"]:
        subj = r["subject"]
        target = None
        if subj.startswith("CHEMBL"):
            target = next((m for m in members if "CAT:" + subj in m["records"]), None)
        elif subj in ("tool_no_catalogue_identity", "genetic_precedent_not_a_compound"):
            target = next((m for m in members if m["type"] == "tool_compound" and r["card_id"] in m["cards"]), None)
        elif subj == "card":
            if single:
                target = next((m for m in members if m["type"] == "molecule" and r["card_id"] in m["identity_cards"]), self_m)
            else:
                target = next((m for m in members if r["card_id"] in m["identity_cards"]), class_m)
        if target is None:
            target = class_m if not single else self_m      # named but not a member of the family set: kept at class level, flagged by the evidence text
        target["rows"].append(r)
    keep_self = single and (self_m["rows"] or not members)
    keep_class = (not single) or class_m["rows"]
    return members + ([self_m] if keep_self else []) + ([class_m] if keep_class else [])


def member_evidence(u: dict) -> list[dict]:
    asserts = {a["id"]: a for a in u["asserts"]}
    rank = lambda a: (DEPTH_RANK.get(a.get("depth") or "UNKNOWN", 0), a["id"])
    res = []
    for m in attribute_rows(u):
        seen, signs, best = set(), Counter(), None
        for r in m["rows"]:
            if r["evidence_kind"] in WWOX_KINDS and (r["card_id"], r["assertion_id"]) not in seen:
                seen.add((r["card_id"], r["assertion_id"]))
                signs[r["sign"]] += 1
                a = asserts.get(r["assertion_id"])
                if a and (best is None or rank(a) > rank(best)):
                    best = a
        outside = len({(r["card_id"], r["assertion_id"]) for r in m["rows"] if r["evidence_kind"] not in WWOX_KINDS})
        pm = sorted({str(x) for r in m["rows"] if r["evidence_kind"] in WWOX_KINDS for x in (asserts.get(r["assertion_id"], {}).get("pmids") or [])})
        tested = bool(seen)
        res.append({"member": m["name"], "member_type": m["type"], "member_key": m["key"], "tested_in_wwox_system": "yes" if tested else "no", "wwox_assertions": len(seen), "signs": dict(sorted(signs.items())),
                    "what": clip(best.get("text"), 200) if best else ("no WWOX-system assertion attributed to this member" + (f"; {outside} outside-WWOX assertion(s) attributed" if outside else "")),
                    "source_pmids": pm, "depth": (best.get("depth") if best else "") or "", "assertion_ids": sorted(a for _, a in seen), "outside_wwox_assertions": outside})
    return res


def matching_pilot(units: list[dict], cases: list[dict] | None = None) -> list[dict]:
    """Small v3 pilot, projected by this ranking's existing generator. No score or
    compound promotion: statements remain attributed to the actual member; development
    requirements do not change the biological group or the research question.
    Case notes are research interpretations of the linked cards, not new evidence.
    """
    if cases is None:
        cases = jload(HERE / "matching_pilot_cases.json")
    by_id = {u["unit_id"]: u for u in units}
    out = []
    for case in cases:
        u = by_id[case["unit_id"]]
        member = next(m for m in u["member_evidence"] if m["member_key"] == case["member_key"])
        requirements = case["development_requirements"]
        if any(r["state"] not in ("favorable", "unfavorable", "unknown") for r in requirements):
            raise ValueError(f"unknown requirement state in {case['case_id']}")
        out.append({**case, "evidence_of_this_member": {
            k: member[k] for k in ("tested_in_wwox_system", "assertion_ids", "signs", "source_pmids", "depth", "outside_wwox_assertions")
        }, "mechanism_context": u["evidence_level_note"]["of_mechanism_or_class"],
            # These are scoped obstacles/questions, never a compound inactivity verdict.
            "development_status": {state: [r["question"] for r in requirements if r["state"] == state]
                                   for state in ("favorable", "unfavorable", "unknown")}})
    return out


def evidence_level_note(u: dict, mev: list[dict]) -> dict:
    """The two readable fields: evidence of the molecule(s) tested, and evidence of the mechanism or class, kept apart."""
    t = u["unit_type"]
    if t in CLASS_LEVEL_TYPES:
        named = [m for m in mev if m["member_type"] in ("molecule", "tool_compound")]
        tested = [m for m in named if m["tested_in_wwox_system"] == "yes"]
        mol = ("; ".join(f"{m['member']}: tested in a WWOX system ({m['wwox_assertions']} assertion(s): " + ", ".join(f"{n} {k}" for k, n in m["signs"].items()) + ")" for m in tested) or "no named member has a WWOX-system result")
        untested = [m["member"] for m in named if m["tested_in_wwox_system"] == "no"]
        cls = next((m for m in mev if m["member_type"] == "class_level"), None)
        mech = (f"{cls['wwox_assertions']} class- or mechanism-level WWOX-system assertion(s)" if cls and cls["wwox_assertions"] else "no class- or mechanism-level WWOX-system assertion at card level")
        tool = [m for m in tested if m["member_type"] == "tool_compound"]
        if tool:
            mech += "; a tool-compound result supports the evaluation of the MECHANISM only, not of any clinical agent"
        return {"of_molecule": mol, "of_mechanism_or_class": mech, "untested_members": untested,
                "attribution_rule": "a result for a tool compound or one member is not a result for the other members; the unit group describes the mechanism/class evaluation"}
    return {"of_molecule": "the intervention's own WWOX-system results (all card-level assertions belong to it)", "of_mechanism_or_class": "not applicable: a single intervention, not a class", "untested_members": [],
            "attribution_rule": "single intervention: its group is its own"}


def validate_attribution(u: dict, table: list[dict]) -> list[str]:
    """Recompute the attribution from the pertinence rows and compare: a member marked tested must own a WWOX row whose subject names it (or whose card-level rows belong to it by the rules)."""
    errs = []
    fresh = {m["member_key"]: m for m in member_evidence(u)}
    for t in table:
        f = fresh.get(t["member_key"])
        if f is None:
            errs.append(f"{u['unit_id']}: member {t['member_key']} is not a member of the intervention")
        elif (f["tested_in_wwox_system"], f["assertion_ids"]) != (t["tested_in_wwox_system"], t["assertion_ids"]):
            errs.append(f"{u['unit_id']}: member {t['member']} is attributed {t['assertion_ids']} but its own rows are {f['assertion_ids']}")
    ids = [i for t in table for i in t["assertion_ids"]]
    if len(ids) != len(set(ids)):
        errs.append(f"{u['unit_id']}: one assertion is attributed to more than one member")
    return errs


NX_STAKE = {
    "F1": ("whether the strongest case holds beyond its single row and its window", "NX2"),
    "F2": ("whether a thin WWOX-system signal is real and specific: the outcomes lead to opposite decisions (lift or stop)", "NX1"),
    "C2": ("which of the favourable and null WWOX-system results holds: the outcomes lead to opposite decisions (lift or stop)", "NX1"),
    "C1": ("whether the only (null) WWOX-system result is real: the outcomes lead to opposite decisions (continue or stop)", "NX1"),
    "F3": ("first WWOX-system test of a target hypothesis", "NX2"),
    "C3": ("whether an outside-WWOX harm or null signal applies; no favourable signal exists to lift", "NX3"),
    "P3": ("a mechanism-only link: the outcome could not change the decision before a premise exists", "NX3"),
}


def next_priority(va: dict) -> dict:
    """Priority of the NEXT EXPERIMENT (ordinal; information value = how much the discriminating next experiment would change a decision). A rule on the lead position and on
    what the work order names, NOT on how often a candidate has been studied, NOT on cost. Cost and feasibility are a separate flag."""
    lead = va.get("lead")
    nx = va["next"]
    named = bool((nx.get("question") or "").strip()) and nx.get("question") != "not stated"
    if lead is None:
        stake = "no position on this objective: a first datum would decide whether any test can be designed" if (nx.get("kind") == "risolvere una premessa") else "no discriminating next step named"
        level = "NX2" if (nx.get("kind") == "risolvere una premessa" and named) else "NX3"
    else:
        stake, level = NX_STAKE[lead]
        if lead == "F3" and va.get("group") == "G4a":
            level, stake = "NX1", "first WWOX-system test of a coherent, selected target hypothesis: the outcomes lead to opposite decisions (continue or stop)"
        if not named:
            level, stake = "NX3", "no discriminating next step is named"
    txt = (nx.get("feasibility") or "")
    flags = []
    if re.search(r"not known|none known|no access|not held|unknown", txt, re.I):
        flags.append("access_or_material_not_known")
    if re.search(r"wet-lab|animal|organoid|slice|cell line|patch|mouse|mice|culture", txt, re.I):
        flags.append("new_wet_lab_work_needed")
    return {"level": level, "level_text": NX_LEVELS[level], "stake": stake, "feasibility_flags": flags or ["unclear"], "feasibility_text": clip(txt, 200)}


QUAL_SOURCES = [
    ("P4b-a", "qualification_it9_p4b_a_20261030/qualification_q2_metabolism.tsv", {"promise": "biological_promise_given_seed_link_and_target_action", "depth": "depth_of_evidence", "feas": "feasibility", "prio": "priority_of_next_experiment", "nxt": "next_experiment", "fals": "falsifier", "datum": "decisive_datum", "unv": "unverified"}),
    ("P4b-b", "qualification_it9_p4b_b_20261030/qualification_b.tsv", {"promise": "biological_promise", "depth": "depth_of_evidence", "feas": "feasibility", "prio": "priority_next_experiment", "nxt": "next_experiment", "fals": "falsifier", "datum": "decisive_datum", "unv": "unverified"}),
    ("P4b-c", "qualification_it9_p4b_c_20261030/qualification_Q6_group.tsv", {"promise": "biological_promise", "depth": "evidence_depth", "feas": "feasibility", "prio": "next_experiment_priority", "nxt": "decisive_datum_or_next_experiment", "fals": "verification_readout", "datum": "decisive_datum_or_next_experiment", "unv": "unverified"}),
    ("P4c-d", "qualification_it9_p4c_d_20261030/qualification_D.tsv", {"promise": "biological_promise", "depth": "depth_of_evidence", "feas": "feasibility", "prio": "priority_of_next_experiment", "nxt": "next_experiment", "fals": "falsifier", "datum": "decisive_datum", "unv": "unverified"}),
    ("P4c-e", "qualification_it9_p4c_e_20261030/qualification_E.tsv", {"promise": "biological_promise", "depth": "depth_of_evidence", "feas": "feasibility", "prio": "priority_next_experiment", "nxt": "next_experiment", "fals": "falsifier", "datum": "decisive_datum", "unv": "unverified"}),
]
STATE_CLASS = {"KEEP": "ORD", "INCONCLUSIVE": "INSUFF", "DROP": "EXCL", "REFERENCE": "EXCL"}


def load_qualification() -> dict:
    """The five IT9 P4 qualification tables, read as stored: one record per candidate id (32 records)."""
    out: dict[str, dict] = {}
    for pk, rel, m in QUAL_SOURCES:
        p = DR / rel
        if not p.exists():
            continue
        for r in read_tsv(p):
            d = r["decision"].upper()
            state = "KEEP" if d.startswith("KEEP") else "INCONCLUSIVE" if d.startswith("INCONCLUSIVE") else "DROP" if d.startswith("DROP") else "REFERENCE" if d.startswith("REFERENCE") else "UNKNOWN"
            out[r["cand_id"]] = {"cand_id": r["cand_id"], "package": pk, "name": r["name"], "decision": r["decision"], "state": state, **{k: r.get(v, "") for k, v in m.items()}}
    return out


def proposal_units(ctx: dict) -> tuple[list[dict], list[dict]]:
    """Units for the IT9-qualified candidates that have no card (KEEP -> ordered as a proposal, INCONCLUSIVE -> still insufficiently evaluated, DROP and REFERENCE -> excluded from
    this comparison with the reason). No WWOX-system result of any compound exists, so the documented PROPOSAL RULE gives a KEEP proposal the position F3 (target-based hypothesis,
    nothing tested in WWOX) and the group G4b, and an INCONCLUSIVE one no position (GU, premise missing). Promise, depth and next-experiment priority stay separate."""
    qual = load_qualification()
    pm = read_tsv(HERE / "proposals_map.tsv")
    for r in pm:
        if r["cand_id"] not in qual:
            raise SystemExit(f"proposals_map.tsv: {r['cand_id']} is not in a qualification table")
        if r["unit_type"] not in UNIT_TYPES or r["origin"] not in ORIGINS:
            raise SystemExit(f"proposals_map.tsv: {r['cand_id']} has an invalid type or origin")
    by_unit: dict[str, list[dict]] = defaultdict(list)
    for r in pm:
        by_unit[r["unit_id"]].append(r)
    needs = ctx["needs"]
    units, records = [], []
    for uid in sorted(by_unit):
        rs = by_unit[uid]
        qs = [qual[r["cand_id"]] for r in rs]
        m0 = rs[0]
        state = qs[0]["state"]
        cls = STATE_CLASS[state]
        nd = needs[m0["need"]]
        obj = "broad" if nd["goal"] == "deep_recovery" else "partial"
        join = lambda k, n=400: clip(" || ".join(dict.fromkeys(q[k] for q in qs if q[k])), n)
        member = cls in ("ORD", "INSUFF")
        lead = "F3" if cls == "ORD" else None
        group = "G4b" if cls == "ORD" else "GU"
        kind = "verificare un'ipotesi" if cls == "ORD" else "risolvere una premessa"
        stake_nx = None
        cand_ids = [q["cand_id"] for q in qs]
        reason_cls = {"ORD": "KEEP-AS-PROPOSAL: the qualification keeps it as a proposal; no WWOX-system result of any compound exists, so the proposal rule gives the position F3 and the group G4b (target-based hypothesis, proposed, not performed)",
                      "INSUFF": "INCONCLUSIVE: insufficient support, not no activity; the missing datum is named in the next experiment; not placed at the bottom and never ranked below an item shown unpromising",
                      "EXCL": ("DROP: excluded from this comparison with the reason in the decisive datum (insufficient support for the proposal chain or the compound-to-target step; none is a finding that the compound is inactive)" if state == "DROP"
                               else "REFERENCE-ONLY: a reference or control record, not a candidate; excluded from this comparison")}[cls]
        va_next = {"kind": kind, "question": join("nxt"), "would_change": join("fals", 300), "feasibility": join("feas", 240), "need": m0["need"]}
        lead_va = {"lead": lead, "group": group, "next": va_next}
        npri = next_priority(lead_va) if member else None
        trig = {"rise": "would rise if the next experiment returns what the proposal needs: " + join("nxt", 300), "fall": "falsifier: " + join("fals", 300),
                "leave": "the gate or premise named in the next experiment fails, or the identity is corrected so that the evidence attaches to a different compound"}
        view = {"member": False}
        if member:
            view = {"member": True, "declared": True, "group": group, "lead": lead, "lead_need": m0["need"], "positions": {m0["need"]: lead or "P1"}, "contested": False, "counter_needs": [],
                    "evidence_quality": "no_wwox_test_target_hypothesis" if lead else "premise_missing", "group_reason": GROUPS[group][2],
                    "evidence": {"in_wwox": False, "carrier_of_position": False, "id": "", "text": "none recorded for the compound in a WWOX system; the proposal rests on a WWOX-side seed observation and a compound-to-target action from other systems",
                                 "scope": "", "species": "", "genotype": "", "depth": "", "pmids": [], "flags": [], "other_favourable_wwox_assertions": 0},
                    "next": va_next, "triggers": trig, "criteria_not_met": ["a signed result of the intervention in a WWOX system exists"], "lead_summary": {"wwox_signs": {}, "wwox_null_harm_mixed": 0, "outside_favourable": 0, "outside_null_or_harm": 0},
                    "next_priority": npri, "counter_statements": [join("datum", 400)] if cls == "ORD" else [], "objective_note": "", "view_note": "", "notes": [], "caveat_limits": [],
                    "main_limit": clip(join("unv", 300) + " | decisive datum: " + join("datum", 300), 700)}
        views = {"broad": view if obj == "broad" else {"member": False}, "partial": view if obj == "partial" else {"member": False}}
        tx = f"decisive datum: {join('datum', 300)}"
        comp = {"W_wwox_evidence": {"wwox_assertions": 0, "signs": {}, "wild_type_only_assertions": 0, "favourable_distinct_pmids": [], "read_beyond_abstract": 0, "l4_states": {},
                                    "text": "none: no result of the compound in a WWOX system; the link to WWOX is a seed observation and a context-free network edge", "replication": "not applicable (no result)"},
                "M_mechanism": {"families": [], "l1": {}, "l2": {}, "opposed_needs": [], "text": "generated proposal (IT9 seed-based engine): " + tx},
                "T_transferability": {"track": ["A"], "species_of_wwox_assertions": ["none (no result in a WWOX system)"], "genotypes": [], "transfer_limits": [join("unv", 300)], "window_note": []},
                "P_pharmacology": {"state": f"qualified in IT9 {qs[0]['package']} ({', '.join(cand_ids)}); promise {join('promise', 60)}; depth {join('depth', 80)}; potency in a WWOX system UNKNOWN",
                                   "potency_with_assay_context": join("feas", 300), "human_exposure": "see the qualification record", "brain_penetration": "see the qualification record", "record": ", ".join(cand_ids)},
                "X_counter_evidence": {"wwox_null_harm_mixed": 0, "outside_wwox_null_or_harm": 0, "need_level_counter_items": 0, "need_level_counter_items_note": "proposal without a card: counter-evidence is in the decisive datum",
                                       "opposed_action_needs": [], "tags": [join("datum", 200)] if cls != "ORD" else []},
                "U_uncertainty": {"linked_needs": 1 if member else 0, "measured_in_wwox_system": 0, "hypothesised_from_target": 1 if cls == "ORD" else 0, "mechanism_only_or_outside_counter": 0, "premise_missing": 1 if cls == "INSUFF" else 0,
                                  "unknown": [join("unv", 300)], "text": "no WWOX-system result of the compound; what is unknown: " + join("unv", 200)}}
        pathways = []
        if member:
            pathways = [{"need": m0["need"], "need_short": nd["short"], "thread": nd["thread"], "objective": obj, "need_direction": nd["dir"], "position": lead or "P1", "position_by_card": {}, "same_need_conflict": False,
                         "link_evidence": "computational_prediction_generated_in_it9", "l1": {}, "l2": {}, "l3": {}, "l4": {}, "opposed_action": False,
                         "computational_prediction": "seed-based engine (IT9 P2 v2/v3): a compatible-action prediction on a context-free network, not an effect", "wwox_observations_on_need": nd["n_wwox_obs"]}]
        mt = "tool_compound" if m0["unit_type"] == "mechanism_probe" else "molecule"
        mev = [{"member": m0["label"], "member_type": mt, "member_key": uid, "tested_in_wwox_system": "no", "wwox_assertions": 0, "signs": {}, "what": "no WWOX-system assertion: the compound has not been tested in any WWOX system; the entry is a generated, qualified hypothesis",
                "source_pmids": [], "depth": "", "assertion_ids": [], "outside_wwox_assertions": 0}]
        units.append({"unit_id": uid, "label": m0["label"], "kind": "it9_proposal", "unit_type": m0["unit_type"], "unit_type_label": UNIT_TYPES[m0["unit_type"]], "origin": m0["origin"], "origin_label": ORIGINS[m0["origin"]],
                      "member_evidence": mev, "evidence_level_note": {"of_molecule": "no WWOX-system result of the compound (proposed, not performed)", "of_mechanism_or_class": "the WWOX-side link is a seed observation on " + nd["short"] + "; no mechanism-level WWOX result for the compound",
                                                                       "untested_members": [m0["label"]], "attribution_rule": "single qualified candidate: no result is attributed to it from another compound or class"},
                      "cards": [], "merge_reason": ("two qualification records of the same compound (" + ", ".join(cand_ids) + ") are one entry" if len(qs) > 1 else ""), "class": cls, "class_label": CLASSES[cls], "class_reason": reason_cls,
                      "declared_goals": [nd["goal"]], "tracks": ["A"], "views": views, "components": comp, "evaluation_depth": "E3q", "evaluation_depth_text": f"IT9 {qs[0]['package']} qualification record ({', '.join(cand_ids)}), no card; depth as stated there: {join('depth', 160)}",
                      "access": "not assessed here; the qualification record's feasibility field says: " + join("feas", 200), "access_categories": [], "access_items": [],
                      "exploratory_it7": "generated in IT9 (seed-based engine); the IT7 P3 comparison is not used", "pathways": pathways, "members": [], "pmids": [], "receipts_on_cited_pmids": 0, "model_exclusions": [], "comparison_record": "",
                      "depth_of_benefit_sought": "", "research_objective": "", "excluded_from_comparisons": [],
                      "inputs": {"T1_cards": sha16([(q["cand_id"], q["decision"], q["datum"]) for q in qs]), "T2_pertinence": sha16([]), "T3_receipts": sha16([]), "T4_needs": sha16(nd["n_wwox_obs"], nd["dir"]),
                                 "T5_pharmacology": sha16([(q["promise"], q["depth"], q["feas"], q["prio"]) for q in qs]), "T6_identity": sha16(cand_ids)},
                      "caveats": {}, "abstention_cards": []})
        for r, q in zip(rs, qs):
            records.append({"cand_id": q["cand_id"], "package": q["package"], "compound": q["name"], "state": state, "decision": q["decision"], "unit_id": uid, "class": cls, "origin": m0["origin"], "need": m0["need"]})
    return units, records


def assemble(ctx: dict, cat: dict) -> dict:
    units = build_units(ctx, cat)
    known = {u["unit_id"] for u in units}
    cav: dict[str, dict[str, list]] = defaultdict(lambda: defaultdict(list))
    for r in ctx["caveats"]:
        if r["unit_id"] not in known or r["kind"] not in ("limit", "counter", "question", "note", "objective_note", "view_note", "tool_name", "next_question", "next_kind", "next_feasibility"):
            raise SystemExit(f"unit_caveats.tsv: invalid row {r['unit_id']} {r['kind']}")
        cav[r["unit_id"]][r["kind"]].append(r["text"])
    for u_ in units:
        u_["tool_names"] = dict(t.split("=", 1) for t in cav.get(u_["unit_id"], {}).get("tool_name", []))
    out_units = []
    for u in units:
        cls, cls_reason = unit_class(u)
        w, mch, tr, ph, ct, un = component_wwox(u), component_mechanism(u), component_transfer(u, ctx), component_pharm(u, ctx), component_counter(u, ctx), component_uncertainty(u)
        d, dtxt = depth_label(u, w)
        acc_txt, acc_cats, acc_items = access_text(u, cat, ctx)
        mev = member_evidence(u)
        errs = validate_attribution(u, mev)
        if errs:
            raise SystemExit("member attribution is inconsistent:\n  " + "\n  ".join(errs))
        views = {}
        for obj in OBJECTIVES:
            va = view_assessment(u, ctx, obj) if not u["excluded"] else {"objective": obj, "member": False}
            if va.get("member"):
                need = va.get("lead_need")
                va["evidence"] = best_evidence(u, need)
                va["next"] = next_step(u, ctx, need)
                va["triggers"] = change_triggers(u, va, need)
                va["criteria_not_met"] = criteria_not_met(u, need)
                va["lead_summary"] = lead_need_summary(u, need)
                cvx = cav.get(u["unit_id"], {})
                if cvx.get("next_question"):
                    va["next"] = dict(va["next"], question=cvx["next_question"][0], kind=(cvx.get("next_kind") or [va["next"].get("kind")])[0],
                                      feasibility=(cvx.get("next_feasibility") or [va["next"].get("feasibility")])[0], would_change="")
                va["next_priority"] = next_priority(va)
                cv = cav.get(u["unit_id"], {})
                if cv.get("question"):
                    va["triggers"]["rise"] += " | further questions: " + "; ".join(cv["question"])
                va["counter_statements"] = list(cv.get("counter", []))
                va["objective_note"] = " ".join(cv.get("objective_note", []))
                va["view_note"] = " ".join(cv.get("view_note", [])) if obj == "broad" else ""
                va["notes"] = list(cv.get("note", []))
                va["caveat_limits"] = list(cv.get("limit", []))
                va["main_limit"] = " | ".join([clip("; ".join(va["evidence"]["flags"][:6]) or (va["criteria_not_met"][0] if va["criteria_not_met"] else "none stated"), 260)] + va["caveat_limits"])
            views[obj] = va
        hyp_models = [ctx["hyp"][h] for h in ctx["hyp"] if set(ctx["hyp"][h]["cards"]) & set(u["cards"])]
        exclusions = sorted({r for h in hyp_models for r in h.get("model_reasons") or []})
        pathways = needs_overview(u, ctx)
        comp_row = u["comparison"][0] if u["comparison"] else None
        inputs = {
            "T1_cards": sha16([ctx["gen_from"].get("cards_and_packets")], u["cards"], [(c, ctx["cands"][c].get("assessment"), ctx["cands"][c].get("summary")) for c in u["cards"]], [(a["id"], a.get("sign"), a.get("scope"), a.get("depth")) for a in u["asserts"]], {k: v for k, v in sorted(cav.get(u["unit_id"], {}).items())}),
            "T2_pertinence": sha16([[r[k] for k in ("card_id", "assertion_id", "need_id", "evidence_kind", "sign", "flags", "comparator")] for r in u["pert"]]),
            "T3_receipts": sha16(sorted(u["receipts"].items())),
            "T4_needs": sha16([(n, ctx["needs"][n].get("n_wwox_obs"), len(ctx["needs"][n].get("obs") or []), len(ctx["needs"][n].get("counter") or []), ctx["needs"][n].get("dir")) for n in sorted(u["per_need"])], [ctx["wo"].get(n, {}).get("would_change") for n in sorted(u["per_need"])]),
            "T5_pharmacology": sha16(comp_row, u["qualification"]) if u["qualification"] else sha16(comp_row),
            "T6_identity": sha16(sorted(r["row_id"] for r, _ in u["members"]), sorted({c["row_id"] for c in u["cells"]}), sorted((c["row_id"], c["need"], c["L2_mechanistic_coherence"]["state"], c["L3_observed_effect"]["state"]) for c in u["cells"])),
        }
        out_units.append({
            "unit_id": u["unit_id"], "label": u["label"], "kind": u["kind"], "unit_type": u["unit_type"], "unit_type_label": UNIT_TYPES[u["unit_type"]], "origin": u["origin"], "origin_label": ORIGINS[u["origin"]],
            "member_evidence": mev, "evidence_level_note": evidence_level_note(u, mev), "cards": u["cards"], "merge_reason": u["merge_reason"], "class": cls, "class_label": CLASSES[cls], "class_reason": cls_reason,
            "declared_goals": u["declared_goals"], "tracks": u["tracks"], "views": views, "components": {"W_wwox_evidence": w, "M_mechanism": mch, "T_transferability": tr, "P_pharmacology": ph, "X_counter_evidence": ct, "U_uncertainty": un},
            "evaluation_depth": d, "evaluation_depth_text": dtxt, "access": acc_txt, "access_categories": acc_cats, "access_items": acc_items,
            "exploratory_it7": clip(comp_row["MODEL_position_P3_P2"], 360) if comp_row else "no pharmacological-comparison record for this unit; no IT7 P3/P2 information", "pathways": pathways,
            "members": [{"family_id": r["row_id"], "name": r["name"], "cards": sorted({c for c, _ in att}), "roles": sorted({a for _, a in att}), "records": r.get("records"), "status_class": r.get("status_class"),
                         "access_categories": r.get("access_categories"), "name_twins_not_merged": r.get("possible_duplicate_families_by_name_not_merged") or [], "kind": r.get("kind")} for r, att in u["members"]],
            "pmids": u["pmids"], "receipts_on_cited_pmids": sum(u["receipts"].values()), "model_exclusions": exclusions, "comparison_record": comp_row["record_id"] if comp_row else "",
            "depth_of_benefit_sought": clip(comp_row["depth_of_benefit_sought"], 260) if comp_row else "", "research_objective": clip(comp_row["research_objective"], 200) if comp_row else "",
            "inputs": inputs, "caveats": {k: v for k, v in sorted(cav.get(u["unit_id"], {}).items())}, "excluded_from_comparisons": exclusions, "abstention_cards": u["abstention_cards"],
        })
    pu, precs = proposal_units(ctx)
    keep_card = [{"cand_id": "E-01", "package": "P4c-e", "compound": "PX-478", "state": "KEEP", "decision": ctx["qualification_all"].get("E-01", {}).get("decision", ""), "unit_id": "U28", "class": "ORD", "origin": "generated_in_it9", "need": "NEED-PDH-PYRUVATE-AXIS"}]
    return {"units": out_units + pu, "it9_records": sorted(precs + keep_card, key=lambda r: r["cand_id"])}


# ------------------------------------------------------------------------------------------------------------------------ catalogue inventory
def inventory(ctx: dict, cat: dict, uni: dict) -> tuple[list[dict], dict]:
    fam = load_usability()
    rows_by_id = {r["row_id"]: r for r in ctx["matrix"]["rows"]}
    cells_by_row: dict[str, list[dict]] = defaultdict(list)
    for c in ctx["matrix"]["cells"]:
        cells_by_row[c["row_id"]].append(c)
    unit_of_row: dict[str, list[str]] = defaultdict(list)
    cls_of_unit = {u["unit_id"]: u["class"] for u in uni["units"]}
    for u in uni["units"]:
        for m in u["members"]:
            unit_of_row[m["family_id"]].append(u["unit_id"])
    out = []
    for fid in sorted(fam):
        d = fam[fid]
        recs = [cat[r] for r in d["records"] if r in cat]
        lead = cat.get(fid[4:]) or (recs[0] if recs else {})
        status = sorted({e.get("status_class") for e in recs if e.get("status_class")})
        acc = sorted({a for e in recs for a in e.get("access_categories") or []})
        mod = sorted({e.get("modality") for e in recs if e.get("modality")})
        mr = rows_by_id.get(fid)
        cells = cells_by_row.get(fid, [])
        l2 = Counter(c["L2_mechanistic_coherence"]["state"] for c in cells)
        needs_l1 = sorted({c["need"] for c in cells if c["L1_documented_link"]["state"] == "documented"})
        needs_pm = sorted({c["need"] for c in cells if c["L1_documented_link"]["state"] == "pathway_member_only"})
        coh = sorted({c["need"] for c in cells if c["L2_mechanistic_coherence"]["state"] == "coherent"})
        opp = sorted({c["need"] for c in cells if c["L2_mechanistic_coherence"]["state"] == "opposed"})
        units = sorted(unit_of_row.get(fid, []))
        if mr and mr.get("name_is_source_artifact"):
            cls, reason = "EXCL", "the family name is a source artefact: identity unresolved, no comparison is made on a name that is not an identity"
            depth, order = "E0", "X"
        elif units:
            cls = "UNIT:" + "+".join(sorted({cls_of_unit[x] for x in units}))
            reason = "member of a ranked intervention unit; the unit carries the evaluation, not the family"
            depth, order = "E3", "UNIT"
        elif coh:
            cls, reason, depth, order = "INSUFF", "target listed with a direction-consistent documented action on a direction-evaluable need; no WWOX data, no card: no WWOX rationale beyond the target", "E1c", "Q1"
        elif needs_l1:
            cls, reason, depth, order = "INSUFF", "target listed on an intervention target of a need whose direction is uncertain or whose action is unresolved; exploration list only", "E1", "Q2"
        elif needs_pm:
            cls, reason, depth, order = "INSUFF", "linked only through a pathway-member target (counted apart, not a headline link)", "E1p", "Q3"
        elif d["action"]:
            cls, reason, depth, order = "INSUFF", "documented target action but no link to any need of the module: no WWOX rationale by default", "E0a", "Q4"
        else:
            cls, reason, depth, order = "INSUFF", "database record only (no stated action or no target row): no WWOX rationale by default", "E0", "Q5"
        out.append({"family_id": fid, "name": (lead.get("name") or fid), "records": len(d["records"]), "origin": lead.get("origin", ""), "modality": mod, "status_class": status, "access_categories": acc,
                    "class": cls, "evaluation_depth": depth, "first_order": order, "needs_documented_target_link": needs_l1, "needs_pathway_member_only": needs_pm,
                    "needs_direction_consistent": coh, "needs_opposed": opp, "mnet_usable": "yes" if d["mnet"] else "no", "msig_neural_strict": {"1": "yes", "0": "no", "?": "UNKNOWN_NO_STRUCTURE_KEY"}[d["msn"]],
                    "msig_any_context": {"1": "yes", "0": "no", "?": "UNKNOWN_NO_STRUCTURE_KEY"}[d["msa"]], "units": units,
                    "name_twins_not_merged": (mr or {}).get("possible_duplicate_families_by_name_not_merged") or [], "reason": reason})
    # name twins and salts: display group key (counted once in the distinct-name figure; identity stays the family)
    keys = Counter(display_group_key(r["name"]) for r in out)
    for r in out:
        r["display_group"] = display_group_key(r["name"])
        r["display_group_size"] = keys[r["display_group"]]
    n_f = len(out)
    by_cls = Counter(r["class"] if not r["class"].startswith("UNIT") else "UNIT" for r in out)
    by_order = Counter(r["first_order"] for r in out)
    nl = [r for r in out if r["first_order"] in ("Q1", "Q2", "Q3")]
    summary = {
        "families": n_f, "records": sum(r["records"] for r in out), "by_class": dict(sorted(by_cls.items())), "by_first_order": dict(sorted(by_order.items())),
        "need_linked_families_q1_q2_q3": len(nl), "need_linked_families_plus_units": len([r for r in out if r["first_order"] in ("Q1", "Q2", "Q3", "UNIT")]),
        "distinct_display_names_total": len({r["display_group"] for r in out}), "distinct_display_names_in_q1": len({r["display_group"] for r in out if r["first_order"] == "Q1"}),
        "q1_with_opposed_action_elsewhere": sum(1 for r in out if r["first_order"] == "Q1" and r["needs_opposed"]),
        "mnet_usable_families": sum(1 for r in out if r["mnet_usable"] == "yes"),
        "msig_neural_families": sum(1 for r in out if r["msig_neural_strict"] == "yes"),
        "need_linked_by_access_category": dict(sorted(Counter(a for r in out if r["first_order"] in ("Q1", "Q2", "Q3", "UNIT") for a in (r["access_categories"] or ["none"])).items())),
        "all_families_by_access_category": dict(sorted(Counter(a for r in out for a in (r["access_categories"] or ["none"])).items())),
        "q1_by_status": dict(sorted(Counter(",".join(r["status_class"]) or "none" for r in out if r["first_order"] == "Q1").items())),
    }
    return out, summary


def deepening_queue(inv: list[dict], ctx: dict, uni: dict | None = None) -> list[dict]:
    """Where to deepen first: Q1 families (target listed, direction-consistent action, no opposed action anywhere) that a person could in principle obtain
    (an approved or marketed status, or an access category that is not 'unknown/unverified'), on a need that has WWOX-system observations.
    Order: needs with a WWOX-system observation, then access evidence, then name. It is a work queue, not a promise ranking."""
    nobs = {n["id"]: n["n_wwox_obs"] for n in ctx["cur"]["needs"]}
    q = []
    groups: dict[str, list[dict]] = defaultdict(list)
    for r in inv:
        if r["first_order"] != "Q1" or r["needs_opposed"]:
            continue
        groups[r["display_group"]].append(r)
    for g, rs in sorted(groups.items()):
        needs = sorted({n for r in rs for n in r["needs_direction_consistent"]})
        wobs = max(nobs.get(n, 0) for n in needs)
        acc = sorted({a for r in rs for a in r["access_categories"] if a != "unknown/unverified"})
        st = sorted({s for r in rs for s in r["status_class"]})
        approved = "approved_any_source" in st
        if wobs == 0 or not (approved or acc):
            continue
        q.append({"display_group": g, "names": sorted({r["name"] for r in rs}), "family_ids": sorted(r["family_id"] for r in rs), "needs": needs, "wwox_observations_on_best_need": wobs,
                  "status_class": st, "access_categories": acc or ["unknown/unverified"], "mnet_usable": any(r["mnet_usable"] == "yes" for r in rs),
                  "msig_neural": any(r["msig_neural_strict"] == "yes" for r in rs), "units": sorted({u for r in rs for u in r["units"]}),
                  "shares_need_with_units": sorted({u["unit_id"] for u in (uni or {"units": []})["units"] if u["class"] != "EXCL" for p in u["pathways"] if p["need"] in needs}),
                  "why": "target listed with a direction-consistent documented action on a need with WWOX-system observations; nothing else is known about this compound in WWOX"})
    q.sort(key=lambda r: (-r["wwox_observations_on_best_need"], 0 if r["access_categories"] != ["unknown/unverified"] else 1, r["display_group"]))
    return q


# ------------------------------------------------------------------------------------------------------------------------ selections
def view_rows(uni: dict, obj: str) -> list[dict]:
    rows = []
    for u in uni["units"]:
        va = u["views"].get(obj) or {}
        if va.get("member"):
            rows.append((u, va))
    return rows


def group_sort_key(g):
    return GROUPS[g][0]


def selection_rows(uni: dict, view: str) -> list[dict]:
    """view: 'general' | 'broad' | 'partial'. General: the better of the two objective groups of a unit (the objective shown beside it)."""
    out = []
    for u in uni["units"]:
        if u["class"] == "EXCL":
            continue
        cand = []
        for obj in (("broad", "partial") if view == "general" else (view,)):
            va = u["views"].get(obj) or {}
            if va.get("member"):
                cand.append((group_sort_key(va["group"]), obj, va))
        if not cand:
            continue
        cand.sort(key=lambda x: (x[0], x[1]))
        k, obj, va = cand[0]
        out.append({"unit": u, "va": va, "objective": obj, "group": va["group"], "other": [(o, va2["group"]) for _, o, va2 in cand[1:]]})
    out.sort(key=lambda r: (group_sort_key(r["group"]), r["unit"]["label"]))
    return out


def build_selections(uni: dict) -> dict:
    sel = {}
    for view in ("general", "broad", "partial"):
        rows = selection_rows(uni, view)
        top = [r for r in rows if r["group"] in IN_SELECTION][:10]
        rest = [r for r in rows if r not in top]
        sel[view] = {"top": [x["unit"]["unit_id"] for x in top], "top_groups": {x["unit"]["unit_id"]: x["group"] for x in top}, "top_objective": {x["unit"]["unit_id"]: x["objective"] for x in top},
                     "not_in_top_listed_apart": [{"unit_id": x["unit"]["unit_id"], "group": x["group"], "objective": x["objective"]} for x in rest],
                     "n_listed": len(rows), "cut_rule": "groups " + ", ".join(IN_SELECTION) + " are listed (at most ten); lower groups are listed apart, not padded in; ties are kept whole"}
        if len(top) == 10 and len([r for r in rows if r["group"] in IN_SELECTION]) > 10:
            sel[view]["cut_warning"] = "more than ten units stand in the listable groups; the cut falls inside a tie group and the remainder are in 'not_in_top_listed_apart'"
    return sel


# ------------------------------------------------------------------------------------------------------------------------ outputs
UNIT_COLS = ["unit_id", "label", "unit_type", "origin", "kind", "cards", "class", "evaluation_depth", "declared_goals", "tracks", "general_group", "broad_group", "broad_lead", "broad_lead_need", "broad_positions", "broad_contested",
             "partial_group", "partial_lead", "partial_lead_need", "partial_positions", "partial_contested", "W_wwox_evidence", "M_mechanism", "T_transferability", "P_pharmacology", "X_counter_evidence",
             "U_uncertainty", "access", "members", "needs_linked", "needs_linked_denominator", "model_exclusions", "comparison_record", "merge_reason", "class_reason", "caveats", "evidence_of_molecule", "evidence_of_mechanism_or_class", "untested_members",
             "next_priority_broad", "next_priority_partial", "feasibility_flags"]


def unit_row(u: dict, need_total: int) -> dict:
    b, p = u["views"]["broad"], u["views"]["partial"]
    gens = [x["group"] for x in (b, p) if x.get("member") and x.get("group")]
    gen = min(gens, key=group_sort_key) if gens else ("n/a" if u["class"] == "EXCL" else "GU")
    c = u["components"]
    fmt_pos = lambda va: "; ".join(f"{n}={p_}" for n, p_ in (va.get("positions") or {}).items())
    npr = lambda va: va["next_priority"]["level"] if va.get("member") and va.get("next_priority") else ""
    fl = sorted({f for v in (b, p) if v.get("member") and v.get("next_priority") for f in v["next_priority"]["feasibility_flags"]})
    return {"unit_id": u["unit_id"], "label": u["label"], "unit_type": u["unit_type_label"], "origin": u["origin_label"], "kind": u["kind"], "cards": u["cards"], "class": u["class_label"], "evaluation_depth": u["evaluation_depth"] + " " + u["evaluation_depth_text"],
            "declared_goals": u["declared_goals"], "tracks": u["tracks"] or "UNKNOWN", "general_group": gen,
            "broad_group": b.get("group", "not a member" if not b.get("member") else "GU"), "broad_lead": b.get("lead"), "broad_lead_need": b.get("lead_need"), "broad_positions": fmt_pos(b),
            "broad_contested": b.get("contested"), "partial_group": p.get("group", "not a member" if not p.get("member") else "GU"), "partial_lead": p.get("lead"), "partial_lead_need": p.get("lead_need"),
            "partial_positions": fmt_pos(p), "partial_contested": p.get("contested"), "W_wwox_evidence": c["W_wwox_evidence"]["text"] + " | replication: " + c["W_wwox_evidence"]["replication"],
            "M_mechanism": c["M_mechanism"]["text"], "T_transferability": f"track {','.join(u['tracks']) or 'UNKNOWN'}; species {', '.join(c['T_transferability']['species_of_wwox_assertions'])}",
            "P_pharmacology": c["P_pharmacology"]["state"], "X_counter_evidence": f"WWOX-system null/harm/mixed assertions {c['X_counter_evidence']['wwox_null_harm_mixed']}; outside-WWOX null/harm {c['X_counter_evidence']['outside_wwox_null_or_harm']}; "
            f"need-level counter items {c['X_counter_evidence']['need_level_counter_items']} ({c['X_counter_evidence']['need_level_counter_items_note']}); opposed-action needs {len(c['X_counter_evidence']['opposed_action_needs'])}",
            "U_uncertainty": c["U_uncertainty"]["text"], "access": u["access"], "members": [m["name"] for m in u["members"]], "needs_linked": len(u["pathways"]), "needs_linked_denominator": need_total,
            "model_exclusions": u["model_exclusions"], "comparison_record": u["comparison_record"], "merge_reason": u["merge_reason"], "class_reason": u["class_reason"],
            "caveats": " || ".join(f"{k}: {t}" for k, v in u["caveats"].items() for t in v),
            "evidence_of_molecule": u["evidence_level_note"]["of_molecule"], "evidence_of_mechanism_or_class": u["evidence_level_note"]["of_mechanism_or_class"], "untested_members": u["evidence_level_note"]["untested_members"],
            "next_priority_broad": npr(b), "next_priority_partial": npr(p), "feasibility_flags": fl}


NEED_COLS = ["unit_id", "need", "need_short", "thread", "objective", "need_direction", "position", "position_by_card", "same_need_conflict", "link_evidence", "opposed_action", "l1_states", "l2_states",
             "l3_states", "l4_states", "wwox_observations_on_need", "computational_prediction"]


def need_rows(uni: dict) -> list[dict]:
    rows = []
    for u in uni["units"]:
        for p in u["pathways"]:
            rows.append({"unit_id": u["unit_id"], "need": p["need"], "need_short": p["need_short"], "thread": p["thread"], "objective": p["objective"], "need_direction": p["need_direction"],
                         "position": p["position"], "position_by_card": "; ".join(f"{k}={v}" for k, v in sorted(p["position_by_card"].items())), "same_need_conflict": p["same_need_conflict"],
                         "link_evidence": p["link_evidence"], "opposed_action": p["opposed_action"], "l1_states": json.dumps(p["l1"], sort_keys=True), "l2_states": json.dumps(p["l2"], sort_keys=True),
                         "l3_states": json.dumps(p["l3"], sort_keys=True), "l4_states": json.dumps(p["l4"], sort_keys=True), "wwox_observations_on_need": p["wwox_observations_on_need"],
                         "computational_prediction": p["computational_prediction"]})
    return rows


MEMBER_COLS = ["unit_id", "family_id", "name", "cards", "roles", "records_in_family", "status_class", "access_categories", "name_twins_not_merged", "kind"]


def member_rows(uni: dict) -> list[dict]:
    rows = []
    for u in uni["units"]:
        if not u["members"]:
            rows.append({"unit_id": u["unit_id"], "family_id": "", "name": "(no catalogue identity: class, modality or axis named in the card text; a name in prose attaches nothing)", "cards": u["cards"],
                         "roles": "", "records_in_family": "", "status_class": "", "access_categories": "", "name_twins_not_merged": "", "kind": u["kind"]})
        for m in u["members"]:
            rows.append({"unit_id": u["unit_id"], "family_id": m["family_id"], "name": m["name"], "cards": m["cards"], "roles": m["roles"], "records_in_family": m["records"], "status_class": m["status_class"],
                         "access_categories": m["access_categories"], "name_twins_not_merged": m["name_twins_not_merged"], "kind": m["kind"]})
    return rows


SEL_COLS = ["view", "position_in_list", "unit_type", "origin", "biological_promise_group", "depth_of_evidence", "next_experiment_priority", "next_experiment_stake", "feasibility_flags", "evidence_of_molecule", "evidence_of_mechanism_or_class", "group", "unit_id", "intervention", "objective", "access", "context", "applicability_track", "main_reason", "best_relevant_evidence", "main_limit", "pathways_needs",
            "next_experiment_or_control", "could_rise", "could_fall", "could_leave", "sources_pmids", "evaluated_on", "evaluation_depth", "contested_elsewhere", "counter_evidence_statements", "notes"]


def selection_table(uni: dict, sel: dict, as_of: str, units_by_id: dict) -> list[dict]:
    rows = []
    for view in ("general", "broad", "partial"):
        for i, uid in enumerate(sel[view]["top"], 1):
            u = units_by_id[uid]
            obj = sel[view]["top_objective"][uid]
            va = u["views"][obj]
            ev = va["evidence"]
            comp = u["components"]
            ctx_txt = (f"{ev['species'] or 'no WWOX-system species'}; {ev['genotype'] or 'genotype n/a'}; depth {ev['depth'] or 'n/a'}" if ev["in_wwox"] else
                       f"no WWOX-system result of the intervention; best signal is outside WWOX ({ev['scope'] or 'none'}; {ev['species'] or 'species n/a'})")
            ls = va.get("lead_summary") or {}
            lead_short = next((p["need_short"] for p in u["pathways"] if p["need"] == va["lead_need"]), va["lead_need"])
            sg = ", ".join(f"{n} {k}" for k, n in (ls.get("wwox_signs") or {}).items()) or "no signed WWOX-system assertion"
            dq = " Reading depth of the evidence row: queried or abstract only, not a full read." if (ev["depth"] or "") in ("queried_not_full_read", "abstract_only") else ""
            reason = (f"{GROUPS[va['group']][1]}: lead position {va['lead']} on '{lead_short}' ({va['lead_need']}). On that need: {sg}; outside WWOX {ls.get('outside_favourable', 0)} favourable and "
                      f"{ls.get('outside_null_or_harm', 0)} null or harm row(s) (some may be class-level rows from other compounds, see the limits). Mechanism: {comp['M_mechanism']['text']}.{dq} "
                      + (f"Counter-evidence on other needs of this objective: {', '.join(va['counter_needs'])}. " if va.get("counter_needs") else ""))
            npv = va["next_priority"]
            rows.append({"view": view, "position_in_list": i, "unit_type": u["unit_type_label"], "origin": u["origin_label"], "biological_promise_group": va["group"],
                         "depth_of_evidence": u["evaluation_depth"] + " " + u["evaluation_depth_text"], "next_experiment_priority": npv["level"] + ": " + npv["level_text"], "next_experiment_stake": npv["stake"],
                         "feasibility_flags": npv["feasibility_flags"], "evidence_of_molecule": u["evidence_level_note"]["of_molecule"], "evidence_of_mechanism_or_class": u["evidence_level_note"]["of_mechanism_or_class"],
                         "group": va["group"], "unit_id": uid, "intervention": u["label"], "objective": OBJ_LABEL[obj] + (f" ({va.get('objective_note')})" if va.get("objective_note") else ""), "access": u["access"], "context": ctx_txt,
                         "applicability_track": ", ".join(u["tracks"]) or "UNKNOWN", "main_reason": reason,
                         "best_relevant_evidence": ((("carrier of the position, " if ev.get("carrier_of_position") else "") + f"{ev['id']}: {ev['text']}") + (f" [PMID {', '.join(map(str, ev['pmids']))}]" if ev["pmids"] else "") + (f" (+{ev['other_favourable_wwox_assertions']} other favourable WWOX-system assertion(s) on the unit)" if ev.get("other_favourable_wwox_assertions") else "")), "main_limit": va["main_limit"],
                         "pathways_needs": "",
                         "next_experiment_or_control": va["next"]["question"], "could_rise": va["triggers"]["rise"] + (f" | stored work-order statement: {va['next']['would_change']}" if va["next"].get("would_change") else ""), "could_fall": va["triggers"]["fall"], "could_leave": va["triggers"]["leave"],
                         "sources_pmids": u["pmids"], "evaluated_on": as_of, "evaluation_depth": u["evaluation_depth"] + " " + u["evaluation_depth_text"],
                         "contested_elsewhere": ", ".join(va.get("counter_needs") or []) or "no",
                         "counter_evidence_statements": " | ".join(va.get("counter_statements") or []) or "none stated beyond the counts", "notes": " | ".join(([va["view_note"]] if va.get("view_note") else []) + (va.get("notes") or [])) or "none"})
    return rows


def as_of_date(ctx: dict) -> str:
    dates = []
    for p in DR.iterdir():
        m = re.search(r"_(20\d\d)(\d\d)(\d\d)(?:\.\w+)?$", p.name)
        if m:
            dates.append("-".join(m.groups()))
    return max(dates) if dates else "UNKNOWN"


def triggers_rows() -> list[dict]:
    return [
        {"trigger": "T1_cards", "what": "a card or packet of a ranked unit changes (assertion added, sign or depth corrected, abstention lifted, next step named)", "detected_by": "digest of the unit's cards, assertions, signs, scopes, depths",
         "re_evaluates": "positions of the unit (coverage + view regenerate first), then group, class, reasons", "reason_class_when_order_moves": "new_evidence, counter_evidence or identity_correction (declare with snapshot --reason)"},
        {"trigger": "T2_pertinence", "what": "a pertinence row is added or changed (assertion judged pertinent to a need, sign, comparator, flags)", "detected_by": "digest of the unit's rows of coverage/assertion_pertinence.tsv",
         "re_evaluates": "the F/C/P position of the card on that need and the specificity flags (G2a/G2b)", "reason_class_when_order_moves": "new_evidence or counter_evidence"},
        {"trigger": "T3_receipts", "what": "a new fulltext read receipt on a PMID that a ranked unit cites (a new reading of a source it rests on)", "detected_by": "count of receipts per cited PMID, read-only from the ledger",
         "re_evaluates": "a human re-reads the unit's cards against the new receipt; the digest only raises the flag, it never changes a group by itself", "reason_class_when_order_moves": "new_evidence or counter_evidence"},
        {"trigger": "T4_needs", "what": "a need observation, counter-evidence item, direction or work-order text changes for a need the unit is linked to", "detected_by": "digest of the linked needs' observation counts, direction and work-order change statements",
         "re_evaluates": "context of the unit (F3 needs a WWOX observation on the need; a direction change reverses what is consistent)", "reason_class_when_order_moves": "context_change"},
        {"trigger": "T5_pharmacology", "what": "the pharmacological comparison row of the unit changes (P3 qualification of potency, selectivity, exposure, nervous-system data)", "detected_by": "digest of the unit's comparison record",
         "re_evaluates": "the pharmacology component and, by judgement, the order", "reason_class_when_order_moves": "better_pharmacological_qualification"},
        {"trigger": "T6_identity", "what": "the catalogue families tied to the unit, their coverage cells or their L2/L3 states change (new catalogue build, identity corrected, name twin resolved)", "detected_by": "digest of member family ids and the unit's coverage cells",
         "re_evaluates": "mechanism component, G4a/G4b split, member table", "reason_class_when_order_moves": "identity_correction or context_change"},
        {"trigger": "T7_method", "what": "a rule of ranking_it8.py changes meaning (RULES_VERSION)", "detected_by": "RULES_VERSION constant stored in ranking.json", "re_evaluates": "every group", "reason_class_when_order_moves": "method_revision"},
        {"trigger": "T8_radar", "what": "the daily scout reports a changed source (ChEMBL, DGIdb, openFDA NDC, Open Targets, WWOX PubMed count)", "detected_by": "existing radar (framework/scripts/scout_daily.py report); no new scheduler",
         "re_evaluates": "run repurposing_coverage.py run, then ranking_it8.py run; if the check shows no input digest changed, nothing is re-evaluated and the order is identical", "reason_class_when_order_moves": "per the input that changed"},
    ]


def build_all() -> dict[str, bytes]:
    ctx = load_all()
    cat = load_catalog()
    uni = assemble(ctx, cat)
    inv, inv_sum = inventory(ctx, cat, uni)
    queue = deepening_queue(inv, ctx, uni)
    sel = build_selections(uni)
    units_by_id = {u["unit_id"]: u for u in uni["units"]}
    unc = ctx["uncarded"]
    for r in unc:
        if r["class"] not in CLASSES or (r["related_unit"] and r["related_unit"] not in units_by_id) or r["provenance"] not in ("own_search", "catalogue_only"):
            raise SystemExit(f"uncarded_items.tsv: invalid row {r['item_id']}")
    if len({r["item_id"] for r in unc}) != len(unc):
        raise SystemExit("uncarded_items.tsv: duplicate item ids")
    need_total = len(ctx["needs"])
    as_of = as_of_date(ctx)
    urows = [unit_row(u, need_total) for u in uni["units"]]
    # selection table with explicit denominator
    srows = []
    for r in selection_table(uni, sel, as_of, units_by_id):
        u = units_by_id[r["unit_id"]]
        r["pathways_needs"] = "; ".join(f"{p['need_short']} [{p['position']}; {p['link_evidence']}" + ("; OPPOSED action documented" if p["opposed_action"] else "") + "]" for p in u["pathways"]) + \
            f" -- {len(u['pathways'])} of {need_total} needs linked (a count of links, not a share of the disease treated, and it does not raise the group)"
        srows.append(r)
    # counts
    non_excl = [u for u in uni["units"] if u["class"] != "EXCL"]
    cls_cnt = Counter(u["class"] for u in uni["units"])
    grp = {obj: dict(sorted(Counter(u["views"][obj]["group"] for u in uni["units"] if u["views"][obj].get("member")).items(), key=lambda kv: group_sort_key(kv[0]))) for obj in OBJECTIVES}
    summary = {
        "schema": SCHEMA, "rules_version": RULES_VERSION, "as_of": as_of,
        "plain_statement": "A provisional research priority for verification. It is not a validated prediction of clinical benefit, not a probability and not a therapeutic recommendation; nothing here is medical advice. "
                           "An ordinal group is the strength of the case for the NEXT STUDY, with visible components; it is not a score.",
        "units": {"total_in_map": len(uni["units"]), "ranked_interventions": len(non_excl), "excluded_axes": cls_cnt.get("EXCL", 0), "by_class": {CLASSES[k]: cls_cnt.get(k, 0) for k in CLASSES},
                  "cards_covered": sum(len(u["cards"]) for u in uni["units"]), "cards_total": len(ctx["cands"]),
                  "orderable_in_a_group_of_the_selection": len({uid for v in sel.values() for uid in v["top"]}), "groups_by_objective": grp},
        "it9": {"records_qualified": len(uni["it9_records"]), "distinct_compounds": len({r["unit_id"] for r in uni["it9_records"]}),
                "by_state": dict(sorted(Counter(r["state"] for r in uni["it9_records"]).items())), "by_class": {CLASSES[k]: sum(1 for r in uni["it9_records"] if r["class"] == k) for k in CLASSES if any(r["class"] == k for r in uni["it9_records"])},
                "units_by_origin": dict(sorted(Counter(u["origin"] for u in uni["units"] if u["class"] != "EXCL" or u["origin"] != "known_track_before_it9").items())),
                "all_units_by_origin": dict(sorted(Counter(u["origin"] for u in uni["units"]).items())),
                "ranked_by_origin": dict(sorted(Counter(u["origin"] for u in non_excl).items()))},
        "inventory": inv_sum, "deepening_queue_compounds": len(queue),
        "uncarded": {"items": len(unc), "by_class": {CLASSES[k]: sum(1 for r in unc if r["class"] == k) for k in CLASSES}, "by_provenance": dict(sorted(Counter(r["provenance"] for r in unc).items()))}, "selections": sel,
        "needs_total": need_total, "p3_note": "IT7 P3 results (network and signature comparison on 256 families) are exploratory, may not drive the ranking, and card-linked families were firewalled out of that comparison: no unit is ranked or re-ranked by them.",
        "inputs": {"coverage_generated_from": ctx["gen_from"], "comparison_rows": len(ctx["comparison"]), "receipt_ledger_lines": ledger_lines()},
        "groups": {g: {"label": GROUPS[g][1], "statement": GROUPS[g][2]} for g in GROUP_ORDER}, "classes": CLASSES,
        "reason_classes": list(REASON_CLASSES), "non_assessment_changes": list(NON_ASSESSMENT_CHANGES),
        "order_digest": sha16([(u["unit_id"], u["views"]["broad"].get("group"), u["views"]["partial"].get("group"), u["class"]) for u in uni["units"]]),
    }
    files: dict[str, bytes] = {}
    files["units.tsv"] = tsv_bytes(urows, UNIT_COLS)
    files["unit_needs.tsv"] = tsv_bytes(need_rows(uni), NEED_COLS)
    files["unit_members.tsv"] = tsv_bytes(member_rows(uni), MEMBER_COLS)
    files["selections.tsv"] = tsv_bytes(srows, SEL_COLS)
    mrows = [{"unit_id": u["unit_id"], "unit_type": u["unit_type_label"], "member": m["member"], "member_type": m["member_type"], "tested_in_wwox_system": m["tested_in_wwox_system"], "wwox_assertions": m["wwox_assertions"],
              "signs": ", ".join(f"{n} {k}" for k, n in m["signs"].items()), "what": m["what"], "source_pmids": m["source_pmids"], "depth": m["depth"], "assertion_ids": m["assertion_ids"],
              "outside_wwox_assertions": m["outside_wwox_assertions"]} for u in uni["units"] if u["class"] != "EXCL" for m in u["member_evidence"]]
    files["member_evidence.tsv"] = tsv_bytes(mrows, ["unit_id", "unit_type", "member", "member_type", "tested_in_wwox_system", "wwox_assertions", "signs", "what", "source_pmids", "depth", "assertion_ids", "outside_wwox_assertions"])
    files["it9_records.tsv"] = tsv_bytes(uni["it9_records"], ["cand_id", "package", "compound", "state", "decision", "unit_id", "class", "origin", "need"])
    files["triggers.tsv"] = tsv_bytes(triggers_rows(), ["trigger", "what", "detected_by", "re_evaluates", "reason_class_when_order_moves"])
    inv_cols = ["family_id", "name", "records", "origin", "modality", "status_class", "access_categories", "class", "evaluation_depth", "first_order", "needs_documented_target_link", "needs_pathway_member_only",
                "needs_direction_consistent", "needs_opposed", "mnet_usable", "msig_neural_strict", "msig_any_context", "units", "name_twins_not_merged", "display_group", "display_group_size", "reason"]
    files["inventory_families.tsv.gz"] = gz_bytes(tsv_bytes(inv, inv_cols))
    qrows = [{"display_group": q["display_group"], "names": q["names"], "family_ids": q["family_ids"], "needs": q["needs"], "wwox_observations_on_best_need": q["wwox_observations_on_best_need"],
              "status_class": q["status_class"], "access_categories": q["access_categories"], "mnet_usable": q["mnet_usable"], "msig_neural": q["msig_neural"], "units": q["units"], "shares_need_with_units": q["shares_need_with_units"], "why": q["why"]} for q in queue]
    files["deepening_queue.tsv"] = tsv_bytes(qrows, ["display_group", "names", "family_ids", "needs", "wwox_observations_on_best_need", "status_class", "access_categories", "mnet_usable", "msig_neural", "units", "shares_need_with_units", "why"])
    ing = {"summary": summary, "units": uni["units"], "selection_table": srows, "deepening_queue_head": queue[:40], "uncarded": unc, "it9_records": uni["it9_records"],
           "matching_pilot": matching_pilot(uni["units"])}
    files["ranking.json"] = json_bytes(ing)
    # per-unit input digests (for the snapshot / diff mechanism)
    drows = [{"unit_id": u["unit_id"], **u["inputs"]} for u in uni["units"]]
    files["unit_inputs.tsv"] = tsv_bytes(drows, ["unit_id", "T1_cards", "T2_pertinence", "T3_receipts", "T4_needs", "T5_pharmacology", "T6_identity"])
    return files


def write_files(files: dict[str, bytes]):
    for name, data in sorted(files.items()):
        (HERE / name).write_bytes(data)


# ------------------------------------------------------------------------------------------------------------------------ snapshots
def snapshot_dir() -> Path:
    d = HERE / "snapshots"
    d.mkdir(exist_ok=True)
    return d


def current_state(files: dict[str, bytes]) -> dict:
    j = json.loads(files["ranking.json"])
    st = {}
    for u in j["units"]:
        st[u["unit_id"]] = {"label": u["label"], "class": u["class"], "broad": u["views"]["broad"].get("group", "-"), "partial": u["views"]["partial"].get("group", "-"), "inputs": u["inputs"]}
    return {"rules_version": j["summary"]["rules_version"], "as_of": j["summary"]["as_of"], "units": st}


def latest_snapshot() -> tuple[Path | None, dict | None]:
    d = snapshot_dir()
    cands = sorted(d.glob("units_*.json"))
    if not cands:
        return None, None
    # Several snapshots can share a date and the hash in the name has no order: the append order of changes.tsv is the record of which came last.
    order = {}
    ch = HERE / "changes.tsv"
    if ch.exists():
        for line in ch.read_text(encoding="utf-8").splitlines()[1:]:
            sid = line.split("\t", 1)[0]
            order.setdefault(sid, len(order))
    cands.sort(key=lambda p: (order.get(p.stem, -1), p.name))
    return cands[-1], jload(cands[-1])


def compare(prev: dict | None, cur: dict) -> list[dict]:
    rows = []
    if prev is None:
        return [{"unit_id": k, "change": "new_entry", "from": "", "to": f"{v['broad']}/{v['partial']}", "inputs_changed": ""} for k, v in cur["units"].items()]
    for k, v in cur["units"].items():
        o = prev["units"].get(k)
        if o is None:
            rows.append({"unit_id": k, "change": "new_entry", "from": "", "to": f"{v['broad']}/{v['partial']}", "inputs_changed": ""})
            continue
        ic = sorted(t for t in v["inputs"] if v["inputs"][t] != o["inputs"].get(t))
        if prev["rules_version"] != cur["rules_version"]:
            ic.append("T7_method")
        if (o["broad"], o["partial"], o["class"]) != (v["broad"], v["partial"], v["class"]):
            rows.append({"unit_id": k, "change": "group_moved", "from": f"{o['broad']}/{o['partial']} ({o['class']})", "to": f"{v['broad']}/{v['partial']} ({v['class']})", "inputs_changed": "; ".join(ic) or "none detected"})
        elif ic:
            rows.append({"unit_id": k, "change": "inputs_changed_group_unchanged", "from": f"{o['broad']}/{o['partial']}", "to": f"{v['broad']}/{v['partial']}", "inputs_changed": "; ".join(ic)})
    for k in prev["units"]:
        if k not in cur["units"]:
            rows.append({"unit_id": k, "change": "removed", "from": "", "to": "", "inputs_changed": ""})
    return rows


SUGGEST = {"T1_cards": "new_evidence or counter_evidence", "T2_pertinence": "new_evidence or counter_evidence", "T3_receipts": "new_evidence or counter_evidence (a human reads the receipt)",
           "T4_needs": "context_change", "T5_pharmacology": "better_pharmacological_qualification", "T6_identity": "identity_correction or context_change", "T7_method": "method_revision"}


def cmd_snapshot(args) -> int:
    files = build_all()
    cur = current_state(files)
    p, prev = latest_snapshot()
    changes = compare(prev, cur)
    if prev is not None and not changes:
        print("snapshot: nothing changed since", p.name, "- no new snapshot (idempotent)")
        return 0
    moved = [c for c in changes if c["change"] == "group_moved"]
    if moved and args.reason not in REASON_CLASSES:
        print("snapshot: a group moved; --reason must be one of " + ", ".join(REASON_CLASSES), file=sys.stderr)
        for c in moved:
            print("  ", c["unit_id"], c["from"], "->", c["to"], "| inputs changed:", c["inputs_changed"], "| suggested:", "; ".join(sorted({SUGGEST[t] for t in c["inputs_changed"].split("; ") if t in SUGGEST})), file=sys.stderr)
        return 2
    only_new = all(c["change"] == "new_entry" for c in changes)
    name = f"units_{cur['as_of']}_{sha16(cur)}"
    (snapshot_dir() / (name + ".json")).write_bytes(json_bytes(cur))
    tsv = [{"unit_id": k, "label": v["label"], "class": v["class"], "broad_group": v["broad"], "partial_group": v["partial"]} for k, v in sorted(cur["units"].items())]
    (snapshot_dir() / (name + ".tsv")).write_bytes(tsv_bytes(tsv, ["unit_id", "label", "class", "broad_group", "partial_group"]))
    ch = HERE / "changes.tsv"
    old = ch.read_text(encoding="utf-8") if ch.exists() else ""
    cols = ["snapshot", "unit_id", "change", "kind_of_change", "reason_class", "from", "to", "inputs_changed", "note"]
    out = io.StringIO()
    out.write(old if old else "\t".join(cols) + "\n")
    for c in changes:
        kind = "entry_of_new_compound" if c["change"] == "new_entry" else ("assessment_change" if c["change"] == "group_moved" else ("input_change_without_order_change" if c["change"] == "inputs_changed_group_unchanged" else c["change"]))
        reason = "new_entry" if c["change"] == "new_entry" else (args.reason if c["change"] == "group_moved" else (args.reason or "unspecified"))
        out.write("\t".join(cell(x) for x in [name, c["unit_id"], c["change"], kind, reason, c["from"], c["to"], c["inputs_changed"], args.note or ""]) + "\n")
    ch.write_text(out.getvalue(), encoding="utf-8")
    print(f"snapshot: wrote {name} ({len(changes)} change row(s)" + (", entry of new units only" if only_new else "") + ")")
    return 0


def cmd_diff(args) -> int:
    files = build_all()
    cur = current_state(files)
    p, prev = latest_snapshot()
    ch = compare(prev, cur)
    if not ch:
        print("no change since", p.name if p else "(no snapshot)")
        return 0
    for c in ch:
        sug = "; ".join(sorted({SUGGEST[t] for t in c["inputs_changed"].split("; ") if t in SUGGEST}))
        print(f"{c['unit_id']}\t{c['change']}\t{c['from']} -> {c['to']}\tinputs: {c['inputs_changed'] or '-'}\tsuggested reason: {sug or '-'}")
    return 0


def cmd_run(args) -> int:
    files = build_all()
    write_files(files)
    j = json.loads(files["ranking.json"])["summary"]
    print("ranking: wrote", len(files), "files;", j["units"]["ranked_interventions"], "ranked interventions, order digest", j["order_digest"])
    return 0


def cmd_check(args) -> int:
    files = build_all()
    bad = [n for n, d in sorted(files.items()) if not (HERE / n).exists() or (HERE / n).read_bytes() != d]
    if bad:
        print("ranking: STALE:", ", ".join(bad), "- regenerate with: python3 -B " + str((HERE / "ranking_it8.py").relative_to(ROOT)) + " run", file=sys.stderr)
        return 1
    # the latest snapshot must describe the current order unless it is stale on purpose and reported
    cur = current_state(files)
    p, prev = latest_snapshot()
    ch = compare(prev, cur)
    if ch:
        print("ranking: files are current; note: the latest snapshot differs from the current state in", len(ch), "unit(s) (run 'diff', then 'snapshot --reason ...' when the change is a real change of assessment)")
    else:
        print("ranking: current (files byte-identical to a fresh regeneration; snapshot agrees)")
    return 0


def cmd_show(args) -> int:
    j = json.loads(build_all()["ranking.json"])
    if args.unit:
        for u in j["units"]:
            if u["unit_id"] == args.unit:
                print(json.dumps(u, indent=1, ensure_ascii=False))
                return 0
        print("unknown unit", args.unit, file=sys.stderr)
        return 1
    print((HERE / "units.tsv").read_text(encoding="utf-8") if (HERE / "units.tsv").exists() else "")
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0], formatter_class=argparse.RawDescriptionHelpFormatter, epilog=__doc__)
    sub = ap.add_subparsers(dest="cmd")
    sub.add_parser("run")
    sub.add_parser("check")
    s = sub.add_parser("snapshot")
    s.add_argument("--reason", default="")
    s.add_argument("--note", default="")
    sub.add_parser("diff")
    sh = sub.add_parser("show")
    sh.add_argument("unit", nargs="?")
    a = ap.parse_args(argv)
    if not a.cmd:
        ap.print_help()
        return 0
    return {"run": cmd_run, "check": cmd_check, "snapshot": cmd_snapshot, "diff": cmd_diff, "show": cmd_show}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
