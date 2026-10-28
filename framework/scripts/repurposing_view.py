#!/usr/bin/env python3
"""Regenerable local exploration view of the drug-repurposing module: ONE self-contained HTML file.

Reads the module's own outputs (coverage/, catalog/, needs/, cards/, join/) and writes
disease-models/wwox/research/drug_repurposing/view/index.html. Inline CSS and JS, data embedded as
JSON, no network, no server: open the file by double-click. Every displayed count is derived from
the source JSON at build time; the build reads no clock, so the output is deterministic.

Non-canonical research material. Nothing shown is a ranking of treatments, a probability of benefit
or medical advice. Public disease and reference-genotype level only.

  python3 -B framework/scripts/repurposing_view.py run      # (re)generate view/index.html
  python3 -B framework/scripts/repurposing_view.py check    # exit 1 if the file differs from a fresh build
  python3 -B framework/scripts/repurposing_view.py --help
"""
from __future__ import annotations

import argparse
import gzip
import html
import csv
import json
import re
import sys
from collections import Counter
from pathlib import Path

COUNTED_KINDS = {"intervention_target", "disease_gene_product", "pathway_member"}   # = LINK_KINDS | PATHWAY_KINDS of repurposing_search.py

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_DR = ROOT / "disease-models/wwox/research/drug_repurposing"
REGEN_CMD = "python3 -B framework/scripts/repurposing_coverage.py run && python3 -B framework/scripts/repurposing_view.py run"
SCHEMA = "legend.wwox.repurposing_view/2"
MAX_BYTES = 6_000_000
SOURCES = ("full", "shareable")
OUT_NAME = {"full": "index.html", "shareable": "index_shareable.html"}

LEVELS = ["L1_documented_link", "L2_mechanistic_coherence", "L3_observed_effect", "L4_observed_recovery_in_wwox_system"]

# Source-state vocabulary. Each class is displayed distinctly; none is ever rendered as "empty".
STATE_CLASSES = ["ok", "failed", "incomplete", "stale", "truncated", "not_fetched", "other"]


def classify_state(status) -> str:
    s = str(status or "").strip().upper()
    if s == "OK":
        return "ok"
    if "STALE" in s:  # STALE_EXPORT, STALE_AFTER_FAILED_REFRESH: tested before FAIL on purpose
        return "stale"
    if any(w in s for w in ("FAIL", "ERROR")):
        return "failed"
    if "INCOMPLETE" in s:
        return "incomplete"
    if any(w in s for w in ("TRUNC", "PARTIAL", "INTERRUPT")):
        return "truncated"
    if any(w in s for w in ("NOT_FETCHED", "NEVER", "UNTRIED", "NOT_ATTEMPTED", "ABSENT", "MISSING")):
        return "not_fetched"
    return "other"


def jload(p: Path):
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def pct(num, den):
    return round(100.0 * num / den, 1) if den else None


def card_path(dr: Path, card_id: str):
    for d in ("cards", "cards_early"):
        if (dr / d / f"{card_id}.card.json").exists():
            return f"../{d}/{card_id}.card.json"
    return None


def source_rows(manifest: dict, stats: dict, summary: dict) -> list[dict]:
    """One row per catalogue source: state class, raw status, detail, retrieval time, version, licence."""
    out = []

    def sstate(k):
        v = (summary.get("source_states") or {}).get(k)
        if isinstance(v, dict):
            return v.get("state"), v.get("detail")
        return v, None

    ver = (stats.get("source_verification") or {})
    names = sorted((set((manifest.get("sources") or {}).keys()) | set((summary.get("source_states") or {}).keys())) - {"dgidb_note"})
    for k in names:
        m = (manifest.get("sources") or {}).get(k, {})
        la = m.get("last_attempt") or {}
        data = m.get("data") or {}
        sum_status, sum_detail = sstate(k)
        status = la.get("status") or sum_status or "NOT_RECORDED"
        if sum_status and classify_state(sum_status) != "ok" and classify_state(status) == "ok":
            status = sum_status  # the module's own summary says not OK: never display OK
        out.append({
            "id": k, "name": m.get("name", k), "status": status, "state_class": classify_state(status),
            "summary_status": sum_status, "summary_detail": sum_detail,
            "detail": sum_detail if (sum_detail and classify_state(sum_status) != "ok") else la.get("detail"), "attempt_utc": la.get("utc"),
            "retrieved_utc": data.get("retrieved_utc") or (((stats.get("sources") or {}).get(k) or {}).get("retrieved_utc")),
            "version": data.get("version") or (((stats.get("sources") or {}).get(k) or {}).get("version")),
            "licence": m.get("licence") or (((stats.get("sources") or {}).get(k) or {}).get("licence")),
            "terms": m.get("terms"),
            "problems": (ver.get(k) or {}).get("problems") or data.get("problems") or [],
        })
    return out


# ------------------------------------------------------------------ data boundary (full | shareable)
def load_allowlist(dr: Path) -> dict:
    p = dr / "view/shareable_sources.json"
    return jload(p) if p.exists() else {"dgidb_claim_sources": {}, "name_sources": {}, "access_scope_prefixes": {}, "own_text": {"allowed": True}}


def assoc_tag(a: dict) -> str:
    """Provenance tag of one association row: 'ChEMBL' or 'DGIdb:<claim source>' (claim source read from the row, else from its limits text)."""
    if a.get("link_source") == "ChEMBL curated mechanism":
        return "ChEMBL"
    cs = a.get("claim_source")
    if not cs:
        for lim in a.get("limits") or []:
            m = re.search(r"claim source (\S+?)[;,]", lim)
            if m:
                cs = m.group(1)
                break
    return "DGIdb:" + (cs or "unknown")


def tag_allowed(tag: str, allow: dict) -> bool:
    return tag.startswith("DGIdb:") and tag[6:] in (allow.get("dgidb_claim_sources") or {})


def read_associations(dr: Path) -> list[dict]:
    ap = dr / "coverage/associations.jsonl.gz"
    out = []
    if ap.exists():
        with gzip.open(ap, "rt", encoding="utf-8") as fh:
            for line in fh:
                out.append(json.loads(line))
    return out


def catalog_names(dr: Path, rep_ids: set) -> dict:
    """name_source and access-evidence scopes of the representative catalogue records (shareable mode only)."""
    out = {}
    with gzip.open(dr / "catalog/catalog.jsonl.gz", "rt", encoding="utf-8") as fh:
        for line in fh:
            e = json.loads(line)
            if e["id"] in rep_ids:
                out[e["id"]] = {"name_source": e.get("name_source"), "access": [(x.get("category"), x.get("scope") or "") for x in e.get("access") or []]}
    return out


# ------------------------------------------------------------------ curated layer
SCOPES = [  # code, label, glyph. Glyph + label always travel together; colour is never the only carrier.
    ("WWOX_EXPERIMENT_IN_DEE_SYSTEM", "WWOX experiment in a DEE system", "●"),
    ("WWOX_CLINICAL_CASE", "WWOX clinical case report (uncontrolled)", "◐"),
    ("WWOX_BIOLOGY_OTHER_CONTEXT", "WWOX biology in another context", "■"),
    ("OTHER_DISEASE_PRECEDENT", "Other-disease precedent", "▲"),
    ("COMPUTATIONAL_RESULT", "Computational result", "◆"),
    ("TARGET_ENGAGEMENT", "Enzyme or cell-free assay", "□"),
    ("EXTERNAL_DATABASE_RECORD", "External database record", "▤"),
    ("SAFETY_SIGNAL", "Safety signal", "!"),
    ("UNVERIFIED_HYPOTHESIS", "Unverified hypothesis", "?"),
    ("UNCLASSIFIED", "Scope not recorded at assertion level", "–"),
]
KIND_TO_SCOPE = {"readout_in_wwox_system": "WWOX_EXPERIMENT_IN_DEE_SYSTEM", "case_report_wwox_clinical": "WWOX_CLINICAL_CASE", "readout_other_disease": "OTHER_DISEASE_PRECEDENT",
                 "target_engagement_assay": "TARGET_ENGAGEMENT", "safety_signal": "SAFETY_SIGNAL"}
GOALS = {"deep_recovery": "Broad, durable recovery (restore the lost WWOX function)", "partial_benefit": "Useful partial benefit (drugs, supplements, diets)"}
ROUTE_TO_GOAL = {"RECUPERO_PROFONDO": "deep_recovery", "BENEFICIO_PRECOCE": "partial_benefit"}
TRACKS = {"A": "Track A: variant-independent (acts whatever the WWOX allele)", "B": "Track B: variant- or lesion-specific (an allele class, a splice site, a stop codon)"}
THREAD_TEXT = {
    "WWOX restoration": "Bring WWOX itself back: add the gene, correct the transcript, read through a stop codon, rescue a misfolded protein, or raise endogenous expression.",
    "Stress signalling and metabolism": "Cell-stress and energy pathways that look disturbed when WWOX is lost: integrated stress response, pyruvate and lactate handling, mitochondrial respiration, redox balance.",
    "Network excitability": "Why neurons fire too much: excitatory gain, weak inhibition, the chloride and GABA premise, T-type calcium channels.",
    "Signalling": "Growth and survival signalling that WWOX normally restrains: GSK3beta, Wnt/beta-catenin, mTOR and autophagy.",
    "Development and glia": "Brain development and support cells: myelin, progenitor proliferation (MYC), neuroinflammation and gliosis.",
    "Symptom-level": "Symptoms treated in their own right: seizures and spasms, blood glucose and growth.",
}
GROUPS = [
    {"id": "G1", "label": "Group 1: the intervention itself was read out in a WWOX experimental system", "why": "At least one pertinent assertion of the card is a readout in a WWOX-deficient system, and the card names a next step."},
    {"id": "G2", "label": "Group 2: clinical case reports only (uncontrolled)", "why": "The only WWOX-side data for the intervention are case reports without comparator; the card names a next step."},
    {"id": "G3", "label": "Group 3: the target is seen altered in WWOX systems; this intervention is not yet tested there", "why": "The need has a WWOX-system observation, the card names a next step, but no readout of this intervention in a WWOX system is recorded."},
    {"id": "G4", "label": "Group 4: a premise or a next step is missing", "why": "The card is an abstention (a datum is missing before a test can be designed) or the need has no WWOX-system observation."},
]
GROUP_NOTE = ("Groups are ordered by how close the evidence on the intervention is to a WWOX system, not by expected benefit. Inside a group the order is alphabetical and means nothing. "
              "The reasons behind each position are printed with it. There is no score, no probability and no cure ranking.")


def clip(t, n=300):
    t = " ".join(str(t or "").split())
    if len(t) <= n:
        return t
    cut = t[:n]
    i = max(cut.rfind(". "), cut.rfind("; "))
    if i > n * 0.5:
        return cut[: i + 1]
    return cut[: cut.rfind(" ")] + " …"


PMID_RE = re.compile(r"PMID[\s:_]*(\d{6,8})")
DOI_RE = re.compile(r"\b(10\.\d{4,9}/[^\s\"'<>;,)\]]+)")


def short_need(label: str) -> str:
    t = re.split(r" \(|: ", label or "", maxsplit=1)[0]
    return clip(t, 90)


def pf(card: dict) -> dict:
    return card["input"].get("p4_card") or card["input"].get("p4_roadmap_fields") or {}


def card_status(card: dict) -> tuple[str, str]:
    """(normalised research status, raw text). The early axis cards write the status in Italian-vocabulary prose; both are kept."""
    raw = str(pf(card).get("status") or ("abstention" if card.get("abstention") else "hypothesis"))
    t = raw.lower()
    if t.startswith("astension") or "abstention" in t:
        return "abstention", raw
    if "controvers" in t:
        return "controversial", raw
    if "deferred" in t:
        return "deferred with reason", raw
    if t.startswith("ipotesi") or "hypothesis" in t:
        return "hypothesis", raw
    return "other", raw


def load_cards(dr: Path) -> dict:
    cards = {}
    for d in ("cards", "cards_early"):
        if (dr / d).exists():
            for f in sorted((dr / d).glob("*.card.json")):
                cards[f.name[: -len(".card.json")]] = (jload(f), d)
    return cards


def build_curated(dr: Path, ctx: dict) -> dict:
    """Curated, physician-readable layer: threads, goals, candidates, groups. Everything is read from needs, cards, coverage and catalogue files."""
    needs_doc, summary, matrix, prios, stats, allow = ctx["needs_doc"], ctx["summary"], ctx["matrix"], ctx["prios"], ctx["stats"], ctx["allow"]
    assoc_by_family = ctx["assoc_by_family"]
    shareable = ctx["source"] == "shareable"
    needs = needs_doc["needs"]
    per_need = summary["needs"]["per_need"]

    # ---- cards
    cards = ctx["cards"]
    links = jload(dr / "catalog/card_links.json").get("cards", {}) if (dr / "catalog/card_links.json").exists() else {}
    titles = {}
    pc = dr / "join/pubmed_cache"
    if pc.exists():
        for f in sorted(pc.glob("*.json")):
            j = jload(f)
            if j.get("status") == "MATCH_FOUND" and j.get("title"):
                titles[str(j.get("pmid"))] = j["title"]
    pert = []
    pp = dr / "coverage/assertion_pertinence.tsv"
    if pp.exists():
        with open(pp, encoding="utf-8") as fh:
            pert = list(csv.DictReader(fh, delimiter="\t"))
    pert_by_id = {(r["card_id"], r["assertion_id"]): r for r in pert}

    # ---- needs
    def cid_of(x):   # needs list some cards as "EB-KD-01 (cards_early)"
        return str(x).split(" ")[0]
    need_cards: dict[str, list[str]] = {n["id"]: list(dict.fromkeys(cid_of(x) for x in (n.get("sources") or {}).get("cards") or [] if cid_of(x) in cards)) for n in needs}
    rows_by_id = {r["row_id"]: r for r in matrix["rows"]}
    for c in matrix["cells"]:
        for cd in rows_by_id[c["row_id"]].get("cards") or []:
            cid = cd["card_id"] if isinstance(cd, dict) else cd
            if cid in cards and cid not in need_cards[c["need"]]:
                need_cards[c["need"]].append(cid)
    card_needs: dict[str, list[str]] = {}
    for nid, cl in need_cards.items():
        for cid in cl:
            card_needs.setdefault(cid, []).append(nid)

    cneeds = []
    for n in needs:
        pn = per_need[n["id"]]
        obs = []
        for o in n.get("observed") or []:
            osc = o.get("evidence_scope")
            if osc == "WWOX_EXPERIMENT_IN_DEE_SYSTEM" and "clinical" in str(o.get("model_type")):
                osc = "WWOX_CLINICAL_CASE"   # the needs vocabulary files an uncontrolled case under the experiment scope; the view keeps it apart
            obs.append({"id": o.get("id"), "scope": osc, "short": clip(o.get("statement"), 260), "full": o.get("statement"), "model": o.get("model_type"), "species": o.get("species"),
                        "readout": o.get("readout"), "level": o.get("readout_level"), "limits": clip(o.get("limits"), 220), "pmid": o.get("pmid")})
        idr = n.get("intervention_direction") or {}
        tg = [t.get("symbol") for t in n.get("targets") or [] if t.get("target_kind") == "intervention_target"]
        cneeds.append({
            "id": n["id"], "label": n.get("label"), "short": short_need(n.get("label")), "thread": n.get("family"),
            "track": (n.get("track") or {}).get("value"), "goal": (n.get("goal") or {}).get("value"), "scopes": n.get("evidence_scope") or [],
            "obs": obs, "n_wwox_obs": sum(1 for o in obs if o["scope"] in ("WWOX_EXPERIMENT_IN_DEE_SYSTEM", "WWOX_CLINICAL_CASE")), "n_case_obs": sum(1 for o in obs if o["scope"] == "WWOX_CLINICAL_CASE"),
            "counter": n.get("counter_evidence") or [], "inferred": n.get("inferred") or [],
            "dir": idr.get("direction"), "dir_on": idr.get("on"), "dir_why": idr.get("rationale"), "dir_cert": idr.get("certainty"), "dir_dna": idr.get("do_not_assume"),
            "targets": tg[:8], "cards": need_cards[n["id"]], "fam_link": pn.get("families_with_documented_link"),
            "uncertain": idr.get("direction") == "uncertain", "no_l4": not pn.get("cells_L4_observed"),
        })
    nmap = {n["id"]: n for n in cneeds}

    # ---- candidates
    prio_by_row: dict[str, list[dict]] = {}
    for p in prios["priorities"]:
        prio_by_row.setdefault(p["row_id"], []).append(p)
    card_rows: dict[str, list[dict]] = {}
    for r in matrix["rows"]:
        for cd in r.get("cards") or []:
            cid = cd["card_id"] if isinstance(cd, dict) else cd
            card_rows.setdefault(cid, []).append(r)
    scope_codes = [s[0] for s in SCOPES]
    pre_count = Counter(v[0]["input"]["candidate"]["name"].split(" (")[0].strip().split(": ")[0] for v in cards.values())
    cands = []
    for cid in sorted(cards):
        card, folder = cards[cid]
        inp = card["input"]
        f = pf(card)
        md = inp.get("mission_dimensions") or {}
        route = md.get("route") or inp.get("route")
        goal = ROUTE_TO_GOAL.get(route)
        lneeds = card_needs.get(cid, [])
        tracks = sorted({nmap[x]["track"] for x in lneeds if nmap[x]["track"]})
        track = md.get("track") or (tracks[0] if len(tracks) == 1 else None)
        absn = card.get("abstention") or inp.get("abstention_card")
        absd = inp.get("abstention_card") if isinstance(inp.get("abstention_card"), dict) else (absn if isinstance(absn, dict) else {})
        efa_raw = f.get("evidence_for_and_against") or f.get("evidence_pro_contra") or {}
        efa = efa_raw if isinstance(efa_raw, dict) else {}
        against_note = efa_raw if isinstance(efa_raw, str) else None
        against = list(dict.fromkeys(list(inp.get("evidence_against") or []) + list(efa.get("against") or [])))
        for_ = list(efa.get("for") or [])
        nxt = f.get("next_measurement") or f.get("next_measure") or ""
        nk = list(inp.get("not_known") or [])
        # assertions: intervention side with scope; counts also from the pertinence table
        asserts = []
        for a in inp.get("drug_assertions") or []:
            pr = pert_by_id.get((cid, a.get("id")))
            sc = a.get("evidence_scope")
            sc = "UNVERIFIED_HYPOTHESIS" if sc == "UNQUALIFIED" else sc
            if sc not in scope_codes:
                sc = KIND_TO_SCOPE.get(pr["evidence_kind"]) if pr else None
            ctxd = a.get("context") or {}
            txt = f'{a.get("endpoint") or a.get("target_id")}: {str(a.get("direction") or "").lower()}'
            ids = sorted(set(PMID_RE.findall(f'{a.get("locator", "")} {a.get("source", "")}')))
            asserts.append({"id": a.get("id"), "scope": sc or "UNCLASSIFIED", "text": clip(txt, 200), "note": clip(a.get("measured_result_note") or a.get("note") or (pr or {}).get("basis"), 280),
                            "note_full": a.get("measured_result_note") or a.get("note") or (pr or {}).get("basis"), "species": ctxd.get("species"), "system": clip(ctxd.get("disease_id") or "", 120), "genotype": clip(ctxd.get("genotype") or "", 140),
                            "depth": a.get("reading_depth"), "sign": (pr or {}).get("sign"), "kind": (pr or {}).get("evidence_kind"), "pmids": ids})
        # per-link statistics from the module's pertinence table
        lk = {}
        for nid in lneeds:
            rs = [r for r in pert if r["card_id"] == cid and r["need_id"] == nid]
            n_w = sum(1 for r in rs if r["evidence_kind"] == "readout_in_wwox_system" and r["counts_L3"] == "yes")
            n_c = sum(1 for r in rs if r["evidence_kind"] == "case_report_wwox_clinical")
            n_o = sum(1 for r in rs if r["evidence_kind"] == "readout_other_disease")
            n_null = sum(1 for r in rs if r["sign"] == "null")
            n_harm = sum(1 for r in rs if r["sign"] == "harm")
            has_next = bool(nxt) and not absn
            if absn or not nxt:
                g = "G4"
            elif n_w:
                g = "G1"
            elif n_c:
                g = "G2"
            elif nmap[nid]["n_wwox_obs"]:
                g = "G3"
            else:
                g = "G4"
            reasons = []
            reasons.append(("WWOX relevance", f'{n_w} readout(s) of this intervention in a WWOX system; {n_c} case-report assertion(s); {nmap[nid]["n_wwox_obs"]} WWOX-system observation(s) on the need'))
            reasons.append(("Direction and context", f'need direction: {nmap[nid]["dir"]} on {nmap[nid]["dir_on"]} ({clip(nmap[nid]["dir_cert"], 90)}); {n_o} other-disease readout(s)'))
            reasons.append(("Quality of evidence", f'reading depths in the card: {", ".join(sorted({a["depth"] for a in asserts if a["depth"]})) or "none recorded"}; sources are not pooled and shared sources are not independent'))
            reasons.append(("Counter-evidence", ("pro and contra written as prose in the card (not itemised); " if against_note and not against else "") + f'{len(against)} itemised card item(s); {len(nmap[nid]["counter"])} need item(s); {n_null} measured null and {n_harm} harm signal(s) in the pertinent assertions'))
            reasons.append(("Decisive gap", clip(absd.get("missing_datum") if absn and absd.get("missing_datum") else (nk[0] if nk else "none recorded"), 200)))
            reasons.append(("Informative next step", "named in the card" if has_next else "not available (abstention or no step named)"))
            lk[nid] = {"group": g, "n_w": n_w, "n_c": n_c, "n_o": n_o, "n_null": n_null, "n_harm": n_harm, "reasons": reasons}
        # catalogue side
        rws = card_rows.get(cid, [])
        chembl = sorted({x["chembl_id"] for x in (links.get(cid) or {}).get("links", []) if x.get("chembl_id")})
        acc = sorted({a for r in rws for a in (r.get("access_categories") or [])})
        # actions on targets from associations (compare view)
        actions = {}
        for r in rws:
            for a in assoc_by_family.get(r["row_id"], []):
                if a.get("target_kind") != "intervention_target":
                    continue
                if shareable and not tag_allowed(assoc_tag(a), allow):
                    continue
                key = (a["need"], a.get("target") or a.get("gene"), a.get("action_on_target"), a.get("consistency"))
                actions[key] = actions.get(key, 0) + 1
        act = [{"need": k[0], "target": k[1], "action": k[2], "cons": k[3], "n": v} for k, v in sorted(actions.items(), key=lambda kv: (kv[0][0], str(kv[0][1]), str(kv[0][2])))][:40]
        blob = json.dumps(card, ensure_ascii=False)
        pm = {}
        for m in PMID_RE.findall(blob):
            pm.setdefault(m, "mentioned in the card")
        for nid in lneeds:
            for o in nmap[nid]["obs"]:
                if o["pmid"]:
                    pm[str(o["pmid"])] = "observation source in the need record"
        for a in asserts:
            for m in a["pmids"]:
                pm[m] = "source of an intervention assertion"
        dois = sorted(set(x.rstrip(".") for x in DOI_RE.findall(blob)))
        scope_counts = {"int": dict(Counter(a["scope"] for a in asserts)), "need": dict(Counter(o["scope"] for nid in lneeds for o in nmap[nid]["obs"]))}
        gset = sorted({v["group"] for v in lk.values()})
        name = inp["candidate"]["name"].split(" (")[0].strip()
        pre = name.split(": ")[0]
        name = pre if pre_count[pre] == 1 else name
        cands.append({
            "id": cid, "name": inp["candidate"]["name"], "short": clip(name, 80), "folder": folder, "goal": goal, "track": track, "tracks": tracks, "status": card_status(card)[0], "status_raw": clip(card_status(card)[1], 200),
            "abstention": bool(absn), "needs": lneeds, "links": lk, "group": gset[0] if gset else "G4", "assessment": card.get("assessment"), "summary": card.get("directional_summary"),
            "why": clip(f.get("indication_and_transfer") or f.get("identity"), 420), "why_full": f.get("indication_and_transfer") or f.get("identity"),
            "identity": clip(f.get("identity"), 360), "mechanism": clip(f.get("mechanism"), 360), "novelty": clip(f.get("novelty_for_woree"), 360),
            "expected": clip(f.get("expected_contribution"), 200), "access_text": clip(f.get("time_to_access"), 240), "pharm": clip(f.get("pharmacology"), 360),
            "against": against, "against_note": against_note, "for": for_, "transfer_limits": efa.get("transfer_limits"), "not_known": nk,
            "missing": absd.get("missing_datum") if absd.get("missing_datum") else (nk[0] if nk else None), "reopen": clip(absd.get("search_record"), 260) if absd.get("search_record") else None,
            "next": clip(nxt, 360), "next_full": nxt, "limits": card.get("limits") or [], "asserts": asserts, "n_disease_assertions": len(inp.get("disease_assertions") or ([inp["disease_assertion"]] if inp.get("disease_assertion") else [])),
            "access": acc, "country": ("US evidence found" if acc and acc != ["unknown/unverified"] else "no country evidence obtained"), "chembl": chembl, "actions": act,
            "pmids": [{"id": k, "role": v, "title": titles.get(k)} for k, v in sorted(pm.items())], "dois": dois, "scope_counts": scope_counts,
            "card_path": f"../{folder}/{cid}.card.json", "n_prio": sum(len(prio_by_row.get(r["row_id"], [])) for r in rws),
            "disp": dict(sorted(Counter(p["disposition"] for r in rws for p in prio_by_row.get(r["row_id"], [])).items())),
        })
    # ---- threads
    threads = []
    for fam in dict.fromkeys(n["thread"] for n in cneeds):
        ids = [n["id"] for n in cneeds if n["thread"] == fam]
        cs = sorted({c["id"] for c in cands if set(c["needs"]) & set(ids)})
        threads.append({"id": fam, "name": fam, "text": THREAD_TEXT.get(fam, ""), "needs": ids, "cards": cs,
                        "goals": dict(Counter(nmap[i]["goal"] for i in ids)), "wwox_obs": sum(nmap[i]["n_wwox_obs"] for i in ids)})
    # ---- gaps (all computed)
    n_total = len(cneeds)
    gaps = [
        {"kind": "need", "n": sum(1 for n in cneeds if n["no_l4"]), "of": n_total, "text": "needs for which no intervention has an observed recovery in a WWOX system (L4)"},
        {"kind": "need", "n": sum(1 for n in cneeds if n["n_wwox_obs"] == 0), "of": n_total, "text": "needs with no WWOX-system observation recorded in the needs file"},
        {"kind": "need", "n": sum(1 for n in cneeds if n["uncertain"]), "of": n_total, "text": "needs whose direction is uncertain, so the sign of a favourable intervention is not known"},
    ]
    dates = [x for x in (needs_doc.get("built_on"), (stats.get("generated_utc") or "")[:10]) if x]
    meta = {"data_date": max(dates) if dates else None, "needs_built_on": needs_doc.get("built_on"), "catalogue_generated": stats.get("generated_utc"), "dgidb_export": "2024-06-10", "source": ctx["source"],
            "n_cards": len(cands), "n_needs": n_total, "n_cards_by_goal": dict(Counter(c["goal"] for c in cands)), "n_abstentions": sum(1 for c in cands if c["abstention"])}
    return {"meta": meta, "scopes": [{"code": c, "label": l, "glyph": g} for c, l, g in SCOPES], "goals": GOALS, "tracks": TRACKS, "threads": threads, "needs": cneeds, "cands": cands,
            "groups": GROUPS, "group_note": GROUP_NOTE, "gaps": gaps}


def build_footer(source: str, allow: dict, emitted: Counter, srcs: list[dict]) -> dict:
    """Attribution and licence footer: what is embedded as content, and what contributed identifiers or counts only."""
    embedded, counts_only = [], []
    own = allow.get("own_text") or {}
    embedded.append({"label": "Cards, needs, priorities and dispositions (this repository)", "licence": own.get("licence"), "attribution": own.get("attribution"), "url": None, "rows": None})
    by_id = {x["id"]: x for x in srcs}
    if source == "full":
        for x in srcs:
            embedded.append({"label": x["name"], "licence": x.get("licence") or "licence not recorded", "attribution": f'{x["name"]}, version {x.get("version") or "not recorded"}, retrieved {x.get("retrieved_utc") or "not recorded"}',
                             "url": x.get("terms"), "rows": None})
        return {"source": source, "embedded": embedded, "counts_only": [], "note": "Full view for local use. It embeds third-party rows (ChEMBL, DGIdb, openFDA, MATRIX) under their own terms; DGIdb-derived rows are not cleared for public release and ChEMBL content is CC BY-SA 3.0. Use the shareable build to circulate."}
    for tag, n in sorted(emitted.items()):
        if tag.startswith("DGIdb:"):
            a = (allow.get("dgidb_claim_sources") or {}).get(tag[6:], {})
            embedded.append({"label": a.get("label", tag), "licence": a.get("licence"), "attribution": a.get("attribution"), "url": a.get("url"), "rows": n})
        elif tag.startswith("name:"):
            a = (allow.get("name_sources") or {}).get(tag[5:], {})
            embedded.append({"label": a.get("label", tag), "licence": a.get("licence"), "attribution": a.get("attribution"), "url": a.get("url"), "rows": n})
        elif tag.startswith("access:"):
            key = tag[7:]
            lab = (allow.get("access_scope_prefixes") or {}).get(key, key)
            for a in (allow.get("name_sources") or {}).values():
                if a.get("label") == lab:
                    embedded.append({"label": f"{a['label']} (access categories)", "licence": a.get("licence"), "attribution": a.get("attribution"), "url": a.get("url"), "rows": n})
                    break
    seen = set()
    for e in list(embedded):
        seen.add(e["label"].replace(" (access categories)", ""))
    for k, v in (allow.get("counts_and_identifiers_only") or {}).items():
        x = by_id.get(k.lower().replace(" ", "_").replace("nih_", ""))
        counts_only.append({"label": k, "terms": v, "version": (x or {}).get("version"), "retrieved": (x or {}).get("retrieved_utc")})
    return {"source": source, "embedded": embedded, "counts_only": counts_only,
            "note": "Shareable build: a third-party row is embedded only when its provenance is on the allowlist (view/shareable_sources.json). Everything else appears as an identifier or a count. No attribution has been removed."}


def build_payload(dr: Path = DEFAULT_DR, source: str = "full") -> dict:
    cov = dr / "coverage"
    summary = jload(cov / "coverage_summary.json")
    matrix = jload(cov / "coverage_matrix.json")
    prios = jload(cov / "priorities.json")
    stats = jload(dr / "catalog/catalog_stats.json")
    manifest = jload(dr / "catalog/cache_manifest.json")
    needs_doc = jload(dr / "needs/needs.json")
    shareable = source == "shareable"
    if source not in SOURCES:
        raise SystemExit(f"unknown source {source!r}: use one of {SOURCES}")
    allow = load_allowlist(dr)
    assocs = read_associations(dr)
    assoc_by_family: dict[str, list[dict]] = {}
    assoc_by_pair: dict[tuple, list[dict]] = {}
    for a in assocs:
        assoc_by_family.setdefault(a.get("family"), []).append(a)
        assoc_by_pair.setdefault((a.get("family"), a["need"]), []).append(a)
    cards_all = load_cards(dr)
    card_name = {cid: v[0]["input"]["candidate"]["name"].split(" (")[0].strip() for cid, v in cards_all.items()}
    emitted: Counter = Counter()   # provenance tag -> rows embedded (drives the attribution footer)
    reps = {r["row_id"]: r.get("representative") for r in matrix["rows"]}
    cat_info = catalog_names(dr, {v for v in reps.values() if v}) if shareable else {}

    def row_label(r):
        """(name, allowed): in shareable mode a name is embedded only if our card names it or its name source is on the allowlist."""
        if not shareable:
            return r.get("name"), True
        if r.get("cards"):
            cid = r["cards"][0]["card_id"] if isinstance(r["cards"][0], dict) else r["cards"][0]
            if cid in card_name:
                return card_name[cid], True
        ns = (cat_info.get(reps.get(r["row_id"])) or {}).get("name_source")
        if ns in (allow.get("name_sources") or {}):
            emitted["name:" + ns] += 1
            return r.get("name"), True
        return str(r["row_id"]).split(":", 1)[-1].replace("CAT:", ""), False

    needs = needs_doc["needs"]
    need_ids = [n["id"] for n in needs]
    nidx = {n: i for i, n in enumerate(need_ids)}
    per_need = summary["needs"]["per_need"]
    no_link = set(summary["needs"].get("needs_without_any_intervention_target_link") or summary["needs"].get("needs_without_any_link_target") or [])

    # ---- rows referenced by cells, compact
    rows_by_id = {r["row_id"]: r for r in matrix["rows"]}
    cells = matrix["cells"]
    prio_by_key = {(p["row_id"], p["need"]): p for p in prios["priorities"]}
    cell_keys = {(c["row_id"], c["need"]) for c in cells}
    orphan = sorted(k for k in prio_by_key if k not in cell_keys)
    row_order = sorted({c["row_id"] for c in cells} | {k[0] for k in orphan})
    ridx = {r: i for i, r in enumerate(row_order)}
    rows = []
    for rid in row_order:
        r = rows_by_id[rid]
        cards = []
        for c in r.get("cards") or []:
            cid = c["card_id"] if isinstance(c, dict) else c
            cards.append({"id": cid, "att": c.get("attachment") if isinstance(c, dict) else None, "path": card_path(dr, cid)})
        nm, ok = row_label(r)
        acc = r.get("access_categories") or []
        st = r.get("status_class") or []
        mod = r.get("modality") if isinstance(r.get("modality"), list) else [r.get("modality")]
        if not ok:   # shareable: identifier and counts only; per-row attributes of a withheld record are not embedded
            pre = tuple(allow.get("access_scope_prefixes") or ())
            acc = sorted({c for c, sc in (cat_info.get(reps.get(rid)) or {}).get("access", []) if sc.startswith(pre)}) if pre else []
            for c, sc in (cat_info.get(reps.get(rid)) or {}).get("access", []):
                if pre and sc.startswith(pre):
                    emitted["access:" + sc.split(" ")[0]] += 1
            st, mod = [], []
        rows.append({"id": rid, "name": nm, "kind": r.get("kind"), "acc": acc, "st": st, "mod": mod,
                     "rec": r.get("records"), "dup": r.get("n_possible_duplicates") or 0, "cards": cards,
                     "tr": r.get("target_rows_total"), **({"w": 1} if not ok else {})})

    # ---- string table for repeated long strings
    strings: list[str] = []
    sidx: dict[str, int] = {}

    def S(s):
        if s not in sidx:
            sidx[s] = len(strings)
            strings.append(s)
        return sidx[s]

    def trim_criteria(cr: dict) -> dict:
        eq = cr.get("evidence_quality_independence") or {}
        tr = cr.get("transferability") or {}
        wr = cr.get("wwox_relevance") or {}
        dm = cr.get("direction_mechanism") or {}
        ce = cr.get("counter_evidence") or {}
        de = cr.get("discriminating_experiment") or {}
        return {
            "wwox": [wr.get("n_wwox_system_observations_in_need"), wr.get("need_evidence_scopes") or [], wr.get("intervention_assertion_scopes") or {}],
            "dir": [dm.get("L2"), dm.get("link_sources") or [], dm.get("targets") or []],
            "evq": [eq.get("card_assertions"), eq.get("distinct_source_strings"), eq.get("reading_depths") or {}],
            "ctr": [ce.get("intervention_measured_null_assertions"), ce.get("need_counter_evidence_items")],
            "tra": [tr.get("scopes") or [], tr.get("species_of_assertions") or []],
            "pha": [(cr.get("pharmacology_safety_info") or {}).get("safety_assessment"), (cr.get("pharmacology_safety_info") or {}).get("status_class") or []],
            "pot": cr.get("potency_and_assay_context"),
            "exp": [bool(de.get("exists")), de.get("card_endpoint_pursued") or []],
        }

    disp_list = sorted(prios.get("dispositions") or summary["priorities"]["all_dispositions_listed"])
    didx = {d: i for i, d in enumerate(disp_list)}

    def share_l1(l1, k):
        """Shareable: keep targets and source names only from allowlisted associations; the withheld rows are counted."""
        if not shareable:
            return l1
        al = assoc_by_pair.get(k, [])
        ok = [a for a in al if tag_allowed(assoc_tag(a), allow)]
        for a in ok:
            emitted[assoc_tag(a)] += 1
        genes = {x for a in ok for x in (a.get("target"), a.get("gene"))}
        l1 = list(l1)
        l1[2] = [t for t in l1[2] if t in genes]
        l1[3] = sorted({assoc_tag(a) for a in ok})
        l1[6] = [t for t in l1[6] if t in genes]
        if len(ok) < len(al):
            l1[5] = "withheld: at least one source row of this pair is outside the shareable allowlist; counts are kept"
        return l1 + [len(al) - len(ok)]

    pairs = []
    keys = sorted(cell_keys | set(orphan), key=lambda k: (k[1], k[0]))
    cell_by_key = {(c["row_id"], c["need"]): c for c in cells}
    for k in keys:
        c = cell_by_key.get(k)
        p = prio_by_key.get(k)
        o = {"r": ridx[k[0]], "n": nidx[k[1]]}
        if c:
            l1, l2, l3, l4 = (c[x] for x in LEVELS)
            o["l1"] = share_l1([l1.get("state"), l1.get("associations"), l1.get("targets") or [], l1.get("link_sources") or [], l1.get("readout_marker_only_links") or 0, l1.get("why"),
                                l1.get("pathway_member_targets_listed_apart") or [], bool(l1.get("source_caveat_stale"))], k)
            o["l2"] = [l2.get("state"), l2.get("consistent_associations"), l2.get("opposed_associations"), l2.get("unresolved_associations"),
                       [S(json.dumps(q, sort_keys=True) if not isinstance(q, str) else q) for q in (l2.get("certainty_qualifiers") or [])]]
            sg = {k: l3[k] for k in ("signs_wwox_system_readouts", "signs_case_reports", "signs_direct_genotype_comparison_vs_wild_type_only", "signs_effect_in_wild_type_or_carrier_arms",
                                  "signs_other_disease_precedent_not_observed_here", "safety_signals_kept_apart")
                  if l3.get(k)}
            o["l3"] = [l3.get("state"), l3.get("assertion_ids") or [], l3.get("by_scope") or {}, l3.get("cards") or [], l3.get("measured_null_assertions") or 0, l3.get("inference_assertions") or 0, sg,
                       l3.get("target_engagement_assays_not_readouts") or 0]
            o["l4"] = [l4.get("state"), l4.get("assertion_ids") or [], l4.get("by_scope") or {}, bool(l4.get("via_class_card"))]
            o["x"] = bool(c.get("exploration_only"))
        if p:
            cr = trim_criteria(p["criteria"])
            if shareable:
                al = [a for a in assoc_by_pair.get(k, []) if tag_allowed(assoc_tag(a), allow)]
                gs = {x for a in al for x in (a.get("target"), a.get("gene"))}
                cr["dir"] = [cr["dir"][0], sorted({assoc_tag(a) for a in al}), [t for t in cr["dir"][2] if t in gs]]
            o["p"] = {"d": didx[p["disposition"]], "w": S(p["disposition_reason"]), "nd": [S(x) for x in p.get("next_deepening") or []],
                      "cr": cr, "dup": p.get("possible_duplicates_not_merged") or 0}
            if "l1" not in o:
                lv = p["levels"]
                o["l1"] = [lv.get("L1_documented_link"), None, [], [], 0, None, [], False]
                o["l2"] = [lv.get("L2_mechanistic_coherence"), None, None, None, []]
                o["l3"] = [lv.get("L3_observed_effect"), [], {}, [], 0, 0, {}, 0]
                o["l4"] = [lv.get("L4_observed_recovery_in_wwox_system"), [], {}, False]
                o["x"] = bool(p.get("exploration_only"))
        pairs.append(o)

    # ---- needs panel
    lvl_counts: dict[str, dict[str, Counter]] = {nid: {lv: Counter() for lv in LEVELS} for nid in need_ids}
    for c in cells:
        for lv in LEVELS:
            lvl_counts[c["need"]][lv][c[lv]["state"]] += 1
    n_pairs = Counter(c["need"] for c in cells)
    n_prio = Counter(k[1] for k in prio_by_key)
    need_out = []
    for n in needs:
        pn = per_need[n["id"]]
        src = n.get("sources") or {}
        gaps = []
        if n["id"] in no_link:
            gaps.append("no headline (intervention-target) link in the catalogue for this need: no compound family can be linked")
        if pn.get("exploration_only"):
            gaps.append("direction uncertain: L2 mechanistic coherence is not evaluable; the family list is an exploration list")
        if pn.get("families_with_documented_link") and not pn.get("cells_L3_observed"):
            gaps.append("no observed effect (L3) for a linked family in the listed card assertions")
        if not pn.get("cells_L4_observed"):
            gaps.append("no observed recovery in a WWOX system (L4) for any intervention on this need")
        if not pn.get("wwox_system_observations"):
            gaps.append("no WWOX-system observation recorded for this need")
        if (n.get("coverage") or {}).get("status") == "NOT_ASSESSED":
            gaps.append("need's own coverage field says NOT_ASSESSED; the matrix sets it")
        need_out.append({
            "id": n["id"], "label": n.get("label"), "family": n.get("family"),
            "dir": (n.get("intervention_direction") or {}).get("direction"), "dir_on": (n.get("intervention_direction") or {}).get("on"),
            "dir_cert": (n.get("intervention_direction") or {}).get("certainty"), "dir_dna": (n.get("intervention_direction") or {}).get("do_not_assume"),
            "track": (n.get("track") or {}).get("value"), "track_basis": (n.get("track") or {}).get("basis"),
            "goal": (n.get("goal") or {}).get("value"), "goal_basis": (n.get("goal") or {}).get("basis"),
            "scopes": n.get("evidence_scope") or [], "explore": bool(pn.get("exploration_only")),
            "fam_link": pn.get("families_with_documented_link"), "rec_link": pn.get("records_with_documented_link"),
            "fam_cons": pn.get("families_consistent"), "fam_opp": pn.get("families_opposed"),
            "link_targets": pn.get("link_targets"), "wwox_obs": pn.get("wwox_system_observations"),
            "by_kind": pn.get("by_target_kind_records_families") or {}, "excluded_by_reason": pn.get("excluded_records_by_reason") or {},
            "fam_incl_pm": pn.get("families_incl_pathway_members"), "rec_incl_pm": pn.get("records_incl_pathway_members"),
            "fam_headline": pn.get("headline_families_intervention_targets", pn.get("families_with_documented_link")),
            "rec_headline": pn.get("headline_records_intervention_targets", pn.get("records_with_documented_link")),
            "levels": {lv: dict(sorted(lvl_counts[n["id"]][lv].items())) for lv in LEVELS},
            "n_pairs": n_pairs.get(n["id"], 0), "n_prio": n_prio.get(n["id"], 0),
            "gaps": gaps, "counter": n.get("counter_evidence") or [], "inferred": n.get("inferred") or [],
            "cards": [{"id": c, "path": card_path(dr, c)} for c in (src.get("cards") or [])],
            "hyps": src.get("hypotheses") or [], "map": src.get("map_records") or [], "reg": src.get("registry_ids") or [],
            "papers": [x.get("paper_registry_ids") or [] for x in (src.get("papers") or [])],
            "targets": [(t.get("symbol"), t.get("target_kind")) for t in n.get("targets") or []],
            "notes": n.get("notes"),
        })

    # ---- headline / funnel numbers (all from data)
    u, cc, ev, mx, pr, ob = summary["units"], summary["catalogue_coverage"], summary["evaluated_vs_records"], summary["matrix"], summary["priorities"], summary["observations"]
    prio_rows = {k[0] for k in prio_by_key}
    card_rows = [r for r in matrix["rows"] if r.get("cards")]
    card_prio = [k for k in prio_by_key if rows_by_id[k[0]].get("cards")]
    funnel = {
        "records": u["catalogue_records"], "families": u["families"], "chembl_families": u["chembl_families"],
        "source_only_families": u["source_only_families_unresolved_identity"],
        "records_with_target_data": cc["records_with_any_target_row"],
        "records_with_action": cc["records_with_stated_action_on_a_need_target"], "families_with_action": cc["families_with_stated_action_on_a_need_target"],
        "records_with_link": cc["records_with_documented_link_to_a_need"], "families_with_link": cc["families_with_documented_link_to_a_need"],
        "pct_records_with_link": cc["pct_records_with_link"], "pct_link_of_target_rows": cc["pct_records_with_target_row_that_link"],
        "priority_pairs": pr["records"], "priority_rows": len(prio_rows), "pairs_not_prioritised": sum(pr["pairs_not_prioritised"].values()),
        "card_rows": len(card_rows), "card_rows_by_kind": dict(sorted(Counter(r["kind"] for r in card_rows).items())),
        "card_priority_pairs": len(card_prio), "card_priority_rows": len({k[0] for k in card_prio}),
        "evaluated_records": ev["records_evaluated_against_wwox_needs_with_any_observation"],
        "evaluated_meaning": ev["meaning"], "examined": ev["records_examined_by_target_match"],
        "needs": summary["needs"]["count"], "needs_direction_evaluable": summary["needs"]["direction_evaluable"],
        "needs_exploration": summary["needs"]["exploration_only"], "cells": mx["cells_nonempty"], "rows_in_matrix": mx["rows"],
        "name_twin_families": cc["touched_families_with_a_name_twin_in_another_family_not_merged"],
        "families_if_twins_collapsed": cc["families_touching_a_need_if_name_twins_were_collapsed_SENSITIVITY_ONLY"],
        "readout_only_records": cc["records_touching_only_readout_markers"],
        "by_number_of_needs": cc["families_by_number_of_needs_touched"],
        "headline_definition": cc.get("headline_definition"),
        "union_headline_records": cc.get("union_headline_records", cc["records_with_documented_link_to_a_need"]),
        "union_headline_families": cc.get("union_headline_families", cc["families_with_documented_link_to_a_need"]),
        "union_pm_records": cc.get("union_with_pathway_members_records"), "union_pm_families": cc.get("union_with_pathway_members_families"),
        "pct_incl_pm": cc.get("pct_records_incl_pathway_members"),
        "effector_readout_only_records": cc.get("records_touching_only_effector_constraints_or_readout_markers", cc["records_touching_only_readout_markers"]),
        "excluded_rows": cc.get("excluded_rows") or {},
        "unit_records": u["records_are"], "unit_coverage": u["coverage_unit"], "unit_family_rule": u["family_rule"],
        "overlap_warning": cc["overlap_warning"],
    }
    access = {
        "total": stats["entries_total"], "overlapping": stats["access_category_overlapping_counts"],
        "signatures": stats["access_signature_sums_to_total"], "unknown": stats["access_unknown_unverified_entries"],
        "universe": stats["universe"], "not_obtained": stats.get("not_obtained") or [],
        "dsld_note": (stats.get("dsld") or {}).get("bulk_list_coverage_note"),
        "by_status": stats["by_status_class"], "by_modality": stats["by_modality"], "by_origin": stats["by_origin"],
        "rows_access_in_matrix": dict(sorted(Counter(a for r in matrix["rows"] for a in (r.get("access_categories") or ["(none)"])).items())),
    }
    excl = {}
    for a in assocs:
        if a.get("excluded_from_counts") and a.get("target_kind") in COUNTED_KINDS:   # same perimeter as the coverage summary
            e = excl.setdefault(a["catalogue_id"], {"id": a["catalogue_id"], "name": a.get("compound"), "reason": a["excluded_from_counts"], "genes": set(), "needs": set(), "src": a.get("link_source")})
            e["genes"].add(a.get("gene") or a.get("hgnc_id") or "?")
            e["needs"].add(a["need"])
    excluded_detail = sorted(({"id": e["id"], "name": (e["name"] if not shareable else e["id"].replace("CAT:", "")), "reason": (e["reason"] if not shareable else e["reason"].split(":")[0] + " (detail withheld)"), "genes": (sorted(map(str, e["genes"])) if not shareable else []),
                               "n_needs": len(e["needs"]), "src": e["src"]} for e in excl.values()), key=lambda e: (e["reason"].split(":")[0], e["id"]))
    leads_path = cov / "lead_dispositions.json"
    leads = jload(leads_path) if leads_path.exists() else {"_note": None, "dispositions": []}
    card_leads = []
    for k, p in sorted(prio_by_key.items(), key=lambda kv: (kv[0][1], kv[0][0])):
        r = rows_by_id[k[0]]
        if r.get("cards") and p["disposition"] in ("consistent_mechanism_candidate", "exploration_candidate", "opposite_mechanism", "mixed_consistent_and_opposed_actions", "source_queried_without_result", "incomplete_or_failed_query"):
            card_leads.append({"row": row_label(r)[0], "need": k[1], "disp": p["disposition"], "levels": [p["levels"].get(x) for x in LEVELS],
                               "cards": [{"id": c["card_id"], "path": card_path(dr, c["card_id"])} for c in r["cards"]]})
    srcs = source_rows(manifest, stats, summary)
    tech = {
        "schema": summary["schema"], "view_schema": SCHEMA, "matrix_schema": matrix.get("schema"),
        "generated_from": matrix.get("generated_from"), "catalog_generated_utc": stats.get("generated_utc"),
        "catalog_file": stats.get("catalog_file"), "sources": srcs,
        "inputs_status": summary["inputs_status"], "source_states_summary": summary["source_states"],
        "dgidb_age": stats.get("dgidb_age"), "units": u, "limits_summary": summary["limits"],
        "regeneration": REGEN_CMD, "never_summed": bool(matrix.get("never_summed")),
        "needs_schema": needs_doc.get("schema"), "needs_status": needs_doc.get("status"),
    }
    ctx = {"needs_doc": needs_doc, "summary": summary, "matrix": matrix, "prios": prios, "stats": stats, "allow": allow, "assoc_by_family": assoc_by_family, "cards": cards_all, "source": source}
    cur = build_curated(dr, ctx)
    cur["footer"] = build_footer(source, allow, emitted, srcs)
    return {
        "source": source, "cur": cur,
        "schema": SCHEMA, "funnel": funnel, "access": access, "matrix_summary": mx, "observations": ob,
        "dispositions": [{"id": d, "n": pr["by_disposition"].get(d, 0), "cells": (pr.get("by_disposition_cells") or {}).get(d, pr["by_disposition"].get(d, 0)),
                          "fam": (pr.get("by_disposition_distinct_families_or_rows") or {}).get(d), "def": (prios.get("dispositions") or {}).get(d)} for d in disp_list],
        "has_distinct": bool(pr.get("by_disposition_distinct_families_or_rows")),
        "exploration_flagged": pr["exploration_flagged"], "needs": need_out, "rows": rows, "pairs": pairs, "strings": strings,
        "tech": tech, "excluded_detail": excluded_detail, "leads": leads.get("dispositions") or [], "leads_note": leads.get("_note"), "card_leads": card_leads, "orphan_priorities": len(orphan), "ranking_note": prios.get("ranking"), "no_probability": prios.get("no_probability"),
        "level_defs": dict(matrix.get("levels") or {}), "pair_unit": matrix.get("unit"),
    }


# ------------------------------------------------------------------ static (server-rendered) parts
E = html.escape


def fmt(n) -> str:
    return f"{n:,}" if isinstance(n, int) else str(n)


def num(key: str, value) -> str:
    """A headline number: the value is also written in data-k so a test can compare it with the source JSON."""
    return f'<b class="num" data-k="{E(key)}" data-v="{E(str(value))}">{E(fmt(value))}</b>'


def render_sources(srcs: list[dict]) -> str:
    if not srcs:
        return '<p class="state-none">No source states recorded in the cache manifest (this is a missing record, not a successful query).</p>'
    out = ['<table class="tbl"><thead><tr><th>Source</th><th>State</th><th>Detail</th><th>Retrieved (UTC)</th><th>Version</th><th>Licence</th></tr></thead><tbody>']
    for s in srcs:
        c = s["state_class"]
        label = {"ok": "OK", "failed": "FAILED", "incomplete": "INCOMPLETE", "stale": "STALE", "truncated": "TRUNCATED/PARTIAL", "not_fetched": "NOT FETCHED", "other": "UNRECOGNISED"}[c]
        if c == "other":
            label += f" ({s['status']})"
        elif c != "ok":
            label += f" ({s['status']})"
        prob = f'<div class="prob">problems: {E("; ".join(map(str, s["problems"])))}</div>' if s["problems"] else ""
        lic = E(s.get("licence") or "licence not recorded")
        cls = "lic-warn" if "NOT CLEARED" in (s.get("licence") or "").upper() else ""
        out.append(f'<tr data-source="{E(s["id"])}" data-state="{c}"><td>{E(s["name"])}<div class="mut">{E(s["id"])}</div></td>'
                   f'<td><span class="st st-{c}">{E(label)}</span></td><td>{E(str(s["detail"] or "no detail recorded"))}{prob}</td>'
                   f'<td>{E(str(s["retrieved_utc"] or "not recorded"))}</td><td>{E(str(s["version"] or "not recorded"))}</td>'
                   f'<td class="{cls}">{lic}</td></tr>')
    out.append("</tbody></table>")
    return "".join(out)


def bar(p) -> str:
    return f'<span class="bar"><i style="width:{max(0.4, min(100, p or 0))}%"></i></span>'


def render_static(P: dict) -> dict[str, str]:
    f, a, t = P["funnel"], P["access"], P["tech"]
    rec, fam = f["records"], f["families"]
    steps = [
        ("records", "1", "Catalogue records enumerated", num("funnel.records", rec), "records",
         f'{E(f["unit_records"])}. Bar: share of the {fmt(rec)} records.', 100),
        ("families", "2", "Families (grouping of those records)", num("funnel.families", fam), "families",
         f'{E(f["unit_family_rule"])}. {fmt(f["chembl_families"])} ChEMBL families and {fmt(f["source_only_families"])} source-only families whose identity is unresolved. A family is not a distinct drug.', 100),
        ("records_with_target_data", "3", "Records with target data", num("funnel.records_with_target_data", f["records_with_target_data"]), "records",
         f'{pct(f["records_with_target_data"], rec)}% of {fmt(rec)} records carry any target row (ChEMBL mechanism or DGIdb).', pct(f["records_with_target_data"], rec)),
        ("records_with_action", "4", "Records with a STATED ACTION on an intervention target of a need", num("funnel.records_with_action", f["records_with_action"]), "records",
         f'Headline, first: the source states what the compound does to the target (inhibitor, agonist, ...). In families: {num("funnel.families_with_action", f["families_with_action"])} of {fmt(fam)}. '
         f'Still a source statement about a target: not evidence of effect in WWOX and not rescue.', pct(f["records_with_action"], rec)),
        ("records_with_link", "5", "Records with a TARGET LISTED (intervention target of a need; action stated or not)", num("funnel.records_with_link", f["records_with_link"]), "records",
         f'{f["pct_records_with_link"]["percent"]}% of {fmt(f["pct_records_with_link"]["denominator"])} records; {f["pct_link_of_target_rows"]["percent"]}% of the {fmt(f["pct_link_of_target_rows"]["denominator"])} records with target data. '
         f'In families: {num("funnel.families_with_link", f["families_with_link"])} of {fmt(fam)}. {fmt(f["records_with_link"] - f["records_with_action"])} of these records state no action (a listing, a bioactivity compilation or an association): they are listed, not documented interactions. '
         f'Intervention targets only (pathway members, effector constraints and readout markers are not counted; see the split below).', pct(f["records_with_link"], rec)),
        ("priority_pairs", "6", "Priorities", num("funnel.priority_pairs", f["priority_pairs"]), "(family, need) pairs",
         f'On {num("funnel.priority_rows", f["priority_rows"])} distinct families or interventions; a disposition, not a ranking. A further {num("funnel.pairs_not_prioritised", f["pairs_not_prioritised"])} pairs stay in the matrix only. Out of {fmt(f["cells"])} non-empty pairs.', pct(f["priority_pairs"], f["cells"])),
        ("card_rows", "7", "Card-attached", num("funnel.card_rows", f["card_rows"]), "families or interventions with a card",
         f'{", ".join(f"{fmt(v)} {E(k.replace("_", " "))}" for k, v in f["card_rows_by_kind"].items())}. {num("funnel.card_priority_pairs", f["card_priority_pairs"])} priority pairs on {num("funnel.card_priority_rows", f["card_priority_rows"])} of them.', pct(f["card_rows"], f["rows_in_matrix"])),
        ("evaluated_records", "8", "Evaluated against WWOX (own definition)", num("funnel.evaluated_records", f["evaluated_records"]), "records",
         f'Definition: {E(f["evaluated_meaning"])}. This is NOT the number examined by target match ({num("funnel.examined", f["examined"])} records, which is step 1) and NOT a count of tested drugs.', pct(f["evaluated_records"], rec)),
    ]
    fun = ['<ol class="funnel">']
    for key, n, title, val, unit, note, p in steps:
        fun.append(f'<li data-step="{key}"><div class="fh"><span class="fn">{n}</span><span class="ft">{E(title)}</span>{val}<span class="unit">{E(unit)}</span></div>{bar(p)}<p class="mut">{note}</p></li>')
    fun.append("</ol>")
    fun.append(f'<p class="mut">Units differ between steps (records, families, pairs, interventions): compare a bar only with its own unit. Needs share targets, so per-need family counts must not be added: {E(f["overlap_warning"])}. '
               f'{num("funnel.name_twin_families", f["name_twin_families"])} touched families have a name twin in another family (not merged; {num("funnel.families_if_twins_collapsed", f["families_if_twins_collapsed"])} families would touch a need if twins were collapsed: sensitivity only). '
               f'{num("funnel.readout_only_records", f["readout_only_records"])} records touch only readout markers or effector constraints and are not links.</p>')
    fun.append('<h3>Link counts by target kind (unions, each counted once)</h3><table class="tbl" data-table="link-split"><thead><tr><th>Counted</th><th>Records</th><th>Families</th><th>Share of records</th></tr></thead><tbody>'
               f'<tr><td><b>Headline, first</b>: stated action on an intervention target or disease gene product</td><td>{num("funnel.records_with_action", f["records_with_action"])}</td><td>{num("funnel.families_with_action", f["families_with_action"])}</td><td>{pct(f["records_with_action"], rec)}%</td></tr>'
               f'<tr><td><b>Target listed</b> (headline definition: intervention targets and disease gene products, action stated or not)</td><td>{num("funnel.union_headline_records", f["union_headline_records"])}</td><td>{num("funnel.union_headline_families", f["union_headline_families"])}</td><td>{pct(f["union_headline_records"], rec)}%</td></tr>'
               + (f'<tr><td>Headline plus pathway members (not headline; shown apart)</td><td>{num("funnel.union_pm_records", f["union_pm_records"])}</td><td>{num("funnel.union_pm_families", f["union_pm_families"])}</td><td>{pct(f["union_pm_records"], rec)}%</td></tr>' if f.get("union_pm_records") is not None else "")
               + f'<tr><td>Kept out of links: touch only effector constraints (e.g. MAPT) or readout markers</td><td>{num("funnel.effector_readout_only_records", f["effector_readout_only_records"])}</td><td></td><td>{pct(f["effector_readout_only_records"], rec)}%</td></tr>'
               '</tbody></table>' + (f'<p class="mut">{E(f["headline_definition"])}</p>' if f.get("headline_definition") else ""))
    ex = f.get("excluded_rows") or {}
    if ex:
        det = P["excluded_detail"]
        fun.append(f'<h3>Excluded from counts, with reasons</h3><p>{num("funnel.excluded_records", ex.get("records", 0))} catalogue records carry a row kept out of every count: '
                   + ", ".join(f'{E(k.replace("_", " "))} {num("funnel.excluded." + k, v)}' for k, v in sorted((ex.get("by_reason") or {}).items()))
                   + '. Rules: a <b>source artefact</b> is a lone Guide-to-Pharmacology row from a gene list that also holds unrelated targets (rule: a second source is required); '
                   'a <b>placeholder</b> is a drug literally named NULL; an <b>alias risk</b> is a PDK1 row on a record that also carries PDPK1 with no ChEMBL PDK1 mechanism (unresolved, listed, not counted).</p>'
                   '<details><summary>list the excluded records (' + str(len(det)) + ')</summary><table class="tbl" data-table="excluded"><thead><tr><th>Record</th><th>Reason</th><th>Genes</th><th>Needs</th></tr></thead><tbody>'
                   + "".join(f'<tr><td>{E(str(e["name"]))}<div class="mut">{E(e["id"])}</div></td><td>{E(e["reason"])}</td><td>{E(", ".join(e["genes"]))}</td><td>{e["n_needs"]}</td></tr>' for e in det)
                   + '</tbody></table></details>')

    tk = f.get("target_kind_split") or {}
    if tk:
        fun.append('<h3>Target-kind split reported by the module</h3><table class="tbl"><tbody>' + "".join(
            f'<tr data-tk="{E(k)}"><td><code>{E(k)}</code></td><td>' + (
                ", ".join(f"{E(str(a))}: {num('tk.' + k + '.' + str(a), b)}" for a, b in v.items()) if isinstance(v, dict) else E(json.dumps(v))) + "</td></tr>"
            for k, v in sorted(tk.items())) + "</tbody></table>")
    # access
    tot = a["total"]
    order = ["supplement", "OTC", "prescription", "experimental", "unknown/unverified"]
    ac = ['<table class="tbl"><thead><tr><th>Access category</th><th>Records</th><th>Share of ' + fmt(tot) + '</th><th></th></tr></thead><tbody>']
    for k in order + sorted(set(a["overlapping"]) - set(order)):
        if k in a["overlapping"]:
            v = a["overlapping"][k]
            ac.append(f'<tr data-access="{E(k)}"><td>{E(k)}</td><td>{num("access." + k, v)}</td><td>{pct(v, tot)}%</td><td>{bar(pct(v, tot))}</td></tr>')
    ac.append("</tbody></table>")
    ac.append(f'<p><b>Unknown share:</b> {num("access.unknown", a["unknown"])} of {fmt(tot)} records ({pct(a["unknown"], tot)}%) have no access evidence in any source queried. '
              'Unknown means not obtained, not "not available".</p>')
    ac.append('<p class="mut">Categories overlap (a record can have OTC and prescription evidence), so the rows above do not sum to the total. '
              'Mutually exclusive signatures, which do sum to the total:</p><p class="chips">' +
              " ".join(f'<span class="chip">{E(k)}: {fmt(v)}</span>' for k, v in sorted(a["signatures"].items(), key=lambda kv: -kv[1])) + "</p>")
    ac.append('<div class="note"><b>Scope.</b> An access category is US evidence found in the sources on the retrieval dates shown under technical details '
              '(openFDA NDC listings, NIH DSLD labels matched by normalised name, ChEMBL and MATRIX status flags). '
              'It is not an approval, not appropriateness for any person, and not a safety statement. Non-US access was not obtained. ' +
              'Catalogue note: ' + E(a["universe"].get("meaning_of_the_previous", "")) + '. DSLD: ' + E(a.get("dsld_note") or "no note") + '.</div>')
    ac.append('<p class="mut">Not obtained: ' + E("; ".join(a["not_obtained"])) + "</p>")

    # dispositions
    hd = P.get("has_distinct")
    dp = ['<table class="tbl"><thead><tr><th>Disposition</th><th>Pairs (cells)</th>' + ('<th>Distinct families or rows</th>' if hd else "") + '<th>Meaning</th></tr></thead><tbody>']
    for d in P["dispositions"]:
        dp.append(f'<tr data-disp="{E(d["id"])}"><td><span class="dp dp-{E(d["id"])}">{E(d["id"].replace("_", " "))}</span></td><td>{num("disp." + d["id"], d["n"])}</td>'
                  + (f'<td>{num("dispfam." + d["id"], d["fam"])}</td>' if hd and d["fam"] is not None else ("<td>0</td>" if hd else "")) + f'<td>{E(d["def"] or "")}</td></tr>')
    dp.append("</tbody></table>")
    if hd:
        dp.append('<p class="mut">Cells and distinct families are different units: one family can hold several cells (one per need). A count of cells is not a count of compounds.</p>')
    dp.append(f'<p class="mut">{E(str(P["ranking_note"]))}. {num("disp.exploration_flagged", P["exploration_flagged"])} priority pairs are flagged exploration (need direction uncertain).</p>')

    # levels summary
    ms = P["matrix_summary"]
    lv = ['<table class="tbl"><thead><tr><th>Level</th><th>State</th><th>Cells</th></tr></thead><tbody>']
    for lvl in ("L1", "L2", "L3", "L4"):
        if isinstance(ms.get(lvl + "_states"), dict):
            items = [(k, v) for k, v in sorted(ms[lvl + "_states"].items())]
        else:
            items = [(k[3:], ms[k]) for k in sorted(ms) if k.startswith(lvl + "_") and isinstance(ms[k], int)]
        for k, v in items:
            lv.append(f'<tr><td>{lvl}</td><td>{E(k.replace("_", " "))}</td><td>{num("matrix." + lvl + "." + k, v)}</td></tr>')
    lv.append("</tbody></table><p class='mut'>Each level is a separate partition of the same cells; the rows are never added across levels.</p>")

    # leads
    ld = [f'<p class="mut">{E(str(P.get("leads_note") or ""))}</p>' if P.get("leads_note") else ""]
    ld.append('<p>A catalogue target listing (a stated action, or none) is a source statement, not a recommendation. Reasoned endings of searches, including abstentions and opposite mechanisms, each with what would reopen it. Same content as the section "Catalogue-derived leads" of <a href="../../repurposing_batch_selection_20261028_module.md">the handoff</a> (<code>../../repurposing_batch_selection_20261028_module.md</code>). Sources: <code>coverage/lead_dispositions.json</code>.</p>')
    ld.append(f'<h3>Lead dispositions ({num("leads.n", len(P["leads"]))})</h3>')
    for d in P["leads"]:
        card = f'<a href="../{E(d["card"])}">{E(d["card"])}</a>' if d.get("card") else "no card"
        rec = d.get("record")
        reca = f'<a href="../{E(rec)}">{E(rec)}</a>' if rec else "none"
        ld.append(f'<div class="item" data-lead="{E(d["id"])}"><div class="top"><span class="nm">{E(d["id"])}</span><span class="chip">decision: {E(d["decision"])}</span><span class="mut">{E(d["need"])}</span></div>'
                  f'<div>{E(d["subject"])}</div><dl class="crit"><dt>Why</dt><dd>{E(d["why"])}</dd><dt>Reopening condition</dt><dd>{E(d["reopening_condition"])}</dd>'
                  f'<dt>Next experiment</dt><dd>{E(d["next_experiment"])}</dd><dt>Owner</dt><dd>{E(d["owner"])}</dd><dt>Card</dt><dd>{card}</dd><dt>Record</dt><dd>{reca}</dd>'
                  f'<dt>Catalogue ids</dt><dd>{E(", ".join(d.get("catalogue_ids") or []) or "none")}</dd></dl></div>')
    ld.append(f'<h3>Card-attached catalogue pairs ({num("leads.card_pairs", len(P["card_leads"]))})</h3><table class="tbl" data-table="card-leads"><thead><tr><th>Compound or intervention</th><th>Need</th><th>Disposition</th><th>L1</th><th>L2</th><th>L3</th><th>L4</th><th>Card</th></tr></thead><tbody>')
    for c in P["card_leads"]:
        cl = ", ".join(f'<a href="{E(x["path"])}">{E(x["id"])}</a>' if x["path"] else E(x["id"]) for x in c["cards"])
        ld.append(f'<tr><td>{E(c["row"])}</td><td>{E(c["need"])}</td><td><span class="dp dp-{E(c["disp"])}">{E(c["disp"].replace("_", " "))}</span></td>' + "".join(f"<td>{E(str(x).replace('_', ' '))}</td>" for x in c["levels"]) + f"<td>{cl}</td></tr>")
    ld.append("</tbody></table>")

    # technical
    bad = [x for x in t["sources"] if x["state_class"] != "ok"]
    banner = ""
    if bad:
        banner = ('<div class="warnbar" id="source-banner" role="alert"><b>Source states are not all OK:</b> ' + "; ".join(
            f'<span class="st st-{x["state_class"]}" data-banner="{E(x["id"])}">{E(x["name"])}: {E(str(x["status"]))}</span> {E(str(x["detail"] or ""))}' for x in bad)
            + ' Every absence-type result below ("no catalogue link found", "source queried without result") carries this caveat, and none is a negative finding about biology.</div>')
    tc = [f'<p>Data generated (catalogue): {E(str(t["catalog_generated_utc"]))}. This view reads no clock; the build is deterministic from the inputs below.</p>',
          f'<p>Regenerate: <code>{E(t["regeneration"])}</code></p>']
    tc.append("<h3>Sources, versions, licences, states</h3>" + render_sources(t["sources"]))
    tc.append(f'<p data-k="sources.not_ok" data-v="{len(bad)}">Sources not in state OK: {len(bad)}. ' +
              ("A source not in state OK turns every disposition into <i>incomplete or failed query</i>; that is not a negative." if bad else "None: no disposition is currently demoted to incomplete or failed query.") + "</p>")
    ins = t["inputs_status"]
    tc.append("<h3>Input checks</h3><ul>" + "".join(
        f'<li>{E(k.replace("_", " "))}: ' + (f'<span class="st st-{"stale" if k.startswith("stale") else "failed"}">{len(v)} listed</span> {E(", ".join(map(str, v)))}' if v else '<span class="st st-ok">none</span>') + "</li>"
        for k, v in sorted(ins.items())) + "</ul>")
    d = t.get("dgidb_age") or {}
    if d:
        tc.append(f'<p class="note"><b>DGIdb.</b> {E(d.get("reading", ""))} Licence not cleared for public release: DGIdb-derived rows stay in the development repository. '
                  f'Live service checked {E(str(d.get("live_service_checked_utc")))}; {num("dgidb.differs", d.get("sources_where_live_service_differs_from_export"))} sources differ from the export. {E(d.get("current_service_coverage", ""))}</p>')
    tc.append("<h3>Input digests</h3><ul>" + "".join(f"<li><code>{E(str(k))}</code> {E(str(v))}</li>" for k, v in (t.get("generated_from") or {}).items()) + "</ul>")
    tc.append(f'<p class="mut">Schemas: {E(str(t["schema"]))}, matrix {E(str(t["matrix_schema"]))}, needs {E(str(t["needs_schema"]))}, view {E(t["view_schema"])}. Catalogue file: {E(json.dumps(t.get("catalog_file")))}</p>')

    limits = ("<ul>"
              "<li><b>Association is not modulation, and modulation is not rescue.</b> A headline link (L1) is a source statement about a target; it says nothing about a change in a WWOX-deficient system.</li>"
              "<li><b>No efficacy is shown or implied.</b> L3 is an assertion listed as pertinent to the need, with its sign and scope (other-disease precedent, enzyme or cell-free engagement and safety signals are separate states); L4 is a technical comparison against the disease change in a WWOX system, not efficacy and not safety.</li>"
              "<li><b>Scores are not probabilities.</b> There is no score or probability in this view. Dispositions are reasoned categories; the order is need id then row id, not evidence volume. Any model score elsewhere in the module is not a probability.</li>"
              "<li><b>Combinations are not inferred.</b> No synergy, complementarity or joint effect is computed; sets of compounds are not scored.</li>"
              "<li><b>Exploration lists.</b> For the " + num("funnel.needs_exploration", f["needs_exploration"]) + " needs whose direction is uncertain, L2 is not evaluable and the compound list is for exploration, not a list of favourable treatments.</li>"
              "<li><b>Access is US evidence, dated;</b> not approval, appropriateness or safety. Unknown is not negative. Safety is NOT_ASSESSED for every family; potency is not carried.</li>"
              "<li><b>A family is not a drug.</b> Records are source-level substance records (salts, stereoisomers and source-only rows count once each); name twins are not merged.</li>"
              "<li><b>Pertinence is listed by hand per assertion;</b> an assertion not in the pertinence table is not counted. Absence in cards (none in cards) is not a negative finding. Seizure-need cells are symptom-level inferences. Role rows carry certainty qualifiers.</li>"
              "<li>Public disease and reference-genotype level only. Nothing here is medical advice.</li>"
              "</ul>" + "<p class='mut'>Source limits recorded by the module: " + E("; ".join(t["limits_summary"])) + "</p>")
    return {"LEADS": "".join(ld), "BANNER": banner, "FUNNEL": "".join(fun), "ACCESS": "".join(ac), "DISPOSITIONS": "".join(dp), "LEVELS": "".join(lv), "TECH": "".join(tc), "LIMITS": limits,
            "NNEEDS": fmt(f["needs"]), "NPAIRS": fmt(f["cells"]), "NPRIO": fmt(f["priority_pairs"])}


# ------------------------------------------------------------------ page template
CSS = r"""
:root{--bg:#fbfaf7;--fg:#1d2127;--mut:#5d6672;--card:#fff;--line:#d9dde3;--acc:#1f5f8b;--accbg:#e6f0f7;--warn:#8a4b00;--warnbg:#fff1dc;--bad:#9b1c1c;--badbg:#fde8e8;--ok:#1d6b3a;--okbg:#e4f4ea;--bar:#2f7cab}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){--bg:#14171b;--fg:#e6e8eb;--mut:#a0a8b3;--card:#1c2026;--line:#333a43;--acc:#7fb8e0;--accbg:#1f3342;--warn:#f0b36a;--warnbg:#3b2a12;--bad:#f09a9a;--badbg:#3d1a1a;--ok:#7fd29b;--okbg:#17321f;--bar:#5a9fcc}}
:root[data-theme=dark]{--bg:#14171b;--fg:#e6e8eb;--mut:#a0a8b3;--card:#1c2026;--line:#333a43;--acc:#7fb8e0;--accbg:#1f3342;--warn:#f0b36a;--warnbg:#3b2a12;--bad:#f09a9a;--badbg:#3d1a1a;--ok:#7fd29b;--okbg:#17321f;--bar:#5a9fcc}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--fg);font:15px/1.5 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
main,header .in,nav .in{max-width:1180px;margin:0 auto;padding:0 16px}
header{padding:18px 0 6px}h1{font-size:1.45rem;margin:0 0 4px}h2{font-size:1.2rem;margin:0 0 8px}h3{font-size:1rem;margin:16px 0 6px}
section{margin:22px 0;padding:14px 16px;background:var(--card);border:1px solid var(--line);border-radius:10px}
nav{position:sticky;top:0;background:var(--bg);border-bottom:1px solid var(--line);z-index:5}
nav .in{display:flex;gap:4px 12px;flex-wrap:wrap;padding-top:6px;padding-bottom:6px;font-size:.88rem}
a{color:var(--acc)}code{font-size:.85em;background:var(--accbg);padding:1px 4px;border-radius:4px;word-break:break-all}
.mut{color:var(--mut);font-size:.88em}.note{background:var(--warnbg);color:var(--fg);border-left:4px solid var(--warn);padding:8px 12px;border-radius:6px;margin:10px 0}
.tbl{width:100%;border-collapse:collapse;font-size:.9rem;display:block;overflow-x:auto}.tbl th,.tbl td{border-bottom:1px solid var(--line);padding:5px 8px;text-align:left;vertical-align:top}
.num{font-variant-numeric:tabular-nums}.funnel{list-style:none;margin:0;padding:0}.funnel li{padding:8px 0;border-bottom:1px solid var(--line)}
.fh{display:flex;flex-wrap:wrap;align-items:baseline;gap:6px 10px}.fn{background:var(--accbg);color:var(--acc);border-radius:50%;width:1.6em;height:1.6em;display:inline-flex;align-items:center;justify-content:center;font-weight:600}
.ft{font-weight:600}.funnel .num{font-size:1.2rem}.unit{font-size:.8rem;background:var(--accbg);color:var(--acc);padding:1px 8px;border-radius:99px}
.bar{display:block;height:7px;background:var(--line);border-radius:4px;margin:4px 0;overflow:hidden}.bar i{display:block;height:100%;background:var(--bar)}
.chip,.st,.dp,.lv{display:inline-block;padding:1px 8px;border-radius:99px;font-size:.78rem;border:1px solid var(--line);margin:1px 2px;white-space:nowrap}
.chips{line-height:2}#lvl-now .chip,#disp-now .chip{white-space:normal}
.st-ok{background:var(--okbg);color:var(--ok)}.st-failed{background:var(--badbg);color:var(--bad);font-weight:700}.st-stale{background:var(--warnbg);color:var(--warn);font-weight:700}
.st-truncated{background:var(--warnbg);color:var(--warn);border-style:dashed;font-weight:700}.st-not_fetched{background:transparent;color:var(--mut);border-style:dotted;font-weight:700}.st-other{background:var(--badbg);color:var(--bad);border-style:dashed}
.warnbar{background:var(--warnbg);border-bottom:3px solid var(--warn);padding:8px 16px;font-size:.9rem}.st-incomplete{background:var(--badbg);color:var(--bad);border-style:dashed;font-weight:700}.lic-warn{color:var(--bad);font-weight:600}.state-none{background:var(--warnbg);padding:6px 10px;border-radius:6px}
.dp-consistent_mechanism_candidate{background:var(--okbg);color:var(--ok)}.dp-exploration_candidate{background:var(--accbg);color:var(--acc);border-style:dashed}
.dp-opposite_mechanism,.dp-mixed_consistent_and_opposed_actions{background:var(--badbg);color:var(--bad)}.dp-mixed_consistent_and_opposed_actions{border-style:dashed}.dp-not_relevant,.dp-no_catalogue_link_found{color:var(--mut)}.dp-insufficient_data{color:var(--mut);border-style:dashed}
.dp-source_queried_without_result{background:var(--warnbg);color:var(--warn);border-style:dotted}.dp-incomplete_or_failed_query{background:var(--badbg);color:var(--bad);border-style:double;border-width:3px;font-weight:700}
.filters{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:8px}.filters label{font-size:.78rem;color:var(--mut);display:flex;flex-direction:column;gap:2px}
select,input[type=search],button{font:inherit;padding:5px 7px;border:1px solid var(--line);border-radius:6px;background:var(--card);color:var(--fg);min-width:0;width:100%}
button{width:auto;cursor:pointer}.bar-actions{display:flex;gap:8px;align-items:center;flex-wrap:wrap;margin-top:8px}
#filters{position:sticky;top:34px;z-index:4}
.item{border:1px solid var(--line);border-radius:8px;padding:8px 10px;margin:8px 0;background:var(--card)}
.item .top{display:flex;flex-wrap:wrap;gap:4px 10px;align-items:baseline}.item .nm{font-weight:600}.lvls{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:4px 10px;margin-top:6px;font-size:.84rem}
.lvls div{border-left:3px solid var(--line);padding-left:6px}.lvls .k{color:var(--mut);font-size:.74rem;display:block}
.v-documented,.v-coherent,.v-observed,.v-observed_wwox_system,.v-observed_experimental{color:var(--ok);font-weight:600}.v-observed_case_level,.v-observed_case_level_only,.v-pathway_member_only,.v-measured_null_only,.v-precedent_other_disease_only,.v-target_engagement_only,.v-safety_signal_only,.v-source_incomplete{color:var(--warn);font-weight:600}.v-opposed,.v-mixed_consistent_and_opposed{color:var(--bad);font-weight:600}.v-observed_vs_wild_type_only,.v-effect_in_wild_type_only,.v-observed_depth_unknown{color:var(--warn);font-weight:600}.v-none_found,.v-none,.v-none_in_cards,.v-none_in_record{color:var(--mut)}.v-not_evaluable,.v-direction_unresolved{color:var(--warn)}
details{margin-top:6px}summary{cursor:pointer;color:var(--acc)}.crit{display:grid;grid-template-columns:minmax(120px,max-content) 1fr;gap:3px 12px;font-size:.84rem;margin-top:6px}.crit dt{color:var(--mut)}.crit dd{margin:0;word-break:break-word}
.pager{display:flex;gap:8px;align-items:center;flex-wrap:wrap;margin:8px 0}.needs{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,420px),1fr));gap:10px}
.ncard{border:1px solid var(--line);border-radius:8px;padding:10px;background:var(--card)}.ncard.explore{border-style:dashed}.ncard h3{margin-top:0;font-size:.95rem}
.kv{font-size:.84rem;margin:2px 0}.kv b{font-weight:600}ul{padding-left:20px;margin:4px 0}.sr{position:absolute;left:-9999px}
.cnt{font-weight:600}
@media (max-width:560px){body{font-size:14px}section{padding:10px 10px;margin:14px 0}#filters{position:static}.tbl{font-size:.82rem}}
"""

JS = r"""
(function(){
'use strict';
var D=JSON.parse(document.getElementById('data').textContent);
var NEEDS=D.needs,ROWS=D.rows,PAIRS=D.pairs,STR=D.strings,DISP=D.dispositions;
var LBL={documented:'headline link (intervention target)',pathway_member_only:'pathway member only (not headline)',source_incomplete:'source incomplete (not a negative)',observed_wwox_system:'result in the WWOX model',observed_vs_wild_type_only:'compared with wild type only (not a disease-model effect, not a rescue)',effect_in_wild_type_only:'effect in a wild-type or carrier arm only (not a disease-model effect)',observed_depth_unknown:'observed, reading depth unknown (not counted)',mixed_consistent_and_opposed:'consistent AND opposed actions (both listed, never summed)',observed_case_level_only:'observed in a clinical case report only',measured_null_only:'measured null only',precedent_other_disease_only:'precedent in another disease only',target_engagement_only:'enzyme or cell-free engagement only',safety_signal_only:'safety signal only',observed_experimental:'recovery, experimental WWOX system',observed_case_level:'recovery, case-level (uncontrolled report)',none_found:'queried, none found',not_evaluable:'not evaluable',coherent:'coherent',opposed:'opposed',direction_unresolved:'direction unresolved',none:'none',none_in_cards:'none in cards (not a negative)',observed:'observed',none_in_record:'none in record (not a negative)'};
function lbl(s){return LBL[s]||String(s).replace(/_/g,' ');}
function esc(s){return String(s==null?'':s).replace(/[&<>"']/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c];});}
function $(id){return document.getElementById(id);}
var F={access:'',need:'',scope:'',oscope:'',track:'',goal:'',disp:'',q:''};
var page={m:0,p:0};var PS=30;
// ---- derived indexes
var needScopes=[],tracks=[],goals=[],oscopes=[],accs=[];
function uniq(a){var o={},r=[];a.forEach(function(x){if(x!=null&&!o[x]){o[x]=1;r.push(x);}});return r.sort();}
needScopes=uniq([].concat.apply([],NEEDS.map(function(n){return n.scopes;})));
tracks=uniq(NEEDS.map(function(n){return n.track;}));goals=uniq(NEEDS.map(function(n){return n.goal;}));
accs=uniq([].concat.apply([],ROWS.map(function(r){return r.acc;})));
PAIRS.forEach(function(p){var s={};if(p.l3)Object.keys(p.l3[2]).forEach(function(k){s[k]=1;});if(p.l4)Object.keys(p.l4[2]).forEach(function(k){s[k]=1;});p._os=Object.keys(s);
 var r=ROWS[p.r],n=NEEDS[p.n];
 p._q=(r.name+' '+r.id+' '+n.id+' '+n.label+' '+r.cards.map(function(c){return c.id;}).join(' ')+' '+(p.l1?p.l1[2].join(' '):'')+' '+n.hyps.join(' ')+' '+r.acc.join(' ')).toLowerCase();});
oscopes=uniq([].concat.apply([],PAIRS.map(function(p){return p._os;})));
function opt(sel,vals,all){sel.innerHTML='<option value="">'+all+'</option>'+vals.map(function(v){return '<option value="'+esc(v)+'">'+esc(v)+'</option>';}).join('');}
opt($('f-access'),accs,'any access category');
opt($('f-need'),NEEDS.map(function(n){return n.id;}),'any need');
opt($('f-scope'),needScopes,'any need evidence scope');
opt($('f-oscope'),oscopes,'any observation scope (L3/L4)');
opt($('f-track'),tracks,'any Track');opt($('f-goal'),goals,'any recovery goal');
opt($('f-disp'),DISP.map(function(d){return d.id;}),'any disposition');
// ---- predicates
function needOk(n){return (!F.need||n.id===F.need)&&(!F.scope||n.scopes.indexOf(F.scope)>=0)&&(!F.track||n.track===F.track)&&(!F.goal||n.goal===F.goal);}
function pairOk(p){var n=NEEDS[p.n],r=ROWS[p.r];if(!needOk(n))return false;
 if(F.access&&r.acc.indexOf(F.access)<0)return false;
 if(F.oscope&&p._os.indexOf(F.oscope)<0)return false;
 if(F.disp&&!(p.p&&DISP[p.p.d].id===F.disp))return false;
 if(F.q){var t=F.q.toLowerCase().split(/\s+/);for(var i=0;i<t.length;i++)if(t[i]&&p._q.indexOf(t[i])<0)return false;}
 return true;}
// ---- rendering helpers
function lv(k,v,extra){return '<div><span class="k">'+k+'</span><span class="v-'+esc(v)+'">'+esc(lbl(v))+'</span>'+(extra?' <span class="mut">'+extra+'</span>':'')+'</div>';}
function signs(o){var k=Object.keys(o||{});return k.length?' signs: '+k.map(function(a){return esc(a.replace(/^signs_/,'').replace(/_/g,' '))+' '+esc(JSON.stringify(o[a]));}).join('; '):'';}
function scopes(o){var k=Object.keys(o||{});return k.length?k.map(function(s){return esc(s)+' x'+o[s];}).join(', '):'';}
function cardLinks(cs){return cs.map(function(c){return c.path?'<a href="'+esc(c.path)+'">'+esc(c.id)+'</a>':esc(c.id)+' (file not found)';}).join(', ');}
function pairHtml(p,withCrit){
 var r=ROWS[p.r],n=NEEDS[p.n],h='';
 h+='<div class="item" data-row="'+esc(r.id)+'" data-need="'+esc(n.id)+'"><div class="top"><span class="nm">'+esc(r.name)+'</span>';
 h+='<span class="mut">'+esc(r.kind.replace(/_/g,' '))+(r.rec?' - '+r.rec+' record'+(r.rec>1?'s':''):'')+'</span>';
 if(r.acc.length)h+=r.acc.map(function(a){return '<span class="chip">'+esc(a)+'</span>';}).join('');
 h+='<span class="mut">-> '+esc(n.id)+' ('+esc(n.dir)+(n.explore?', exploration':'')+')</span>';
 if(p.p){var d=DISP[p.p.d].id;h+='<span class="dp dp-'+esc(d)+'">'+esc(d.replace(/_/g,' '))+'</span>';}else h+='<span class="chip">matrix only (not prioritised)</span>';
 h+='</div>';
 var l1=p.l1,l2=p.l2,l3=p.l3,l4=p.l4;
 h+='<div class="lvls">'+lv('L1 headline link',l1[0],(l1[1]!=null?l1[1]+' assoc.; '+esc((l1[2]||[]).join(', ')):'')+((l1[6]&&l1[6].length)?' pathway members listed apart: '+esc(l1[6].join(', ')):'')+(l1[7]?' [DGIdb export is stale: absence is not a negative]':''))+lv('L2 mechanistic coherence',l2[0],l2[1]!=null?(l2[1]+' consistent, '+l2[2]+' opposed, '+l2[3]+' unresolved'):'')+lv('L3 observed effect',l3[0],scopes(l3[2])+signs(l3[6]))+lv('L4 recovery in a WWOX system',l4[0],scopes(l4[2]))+'</div>';
 if(p.x)h+='<div class="mut">exploration: this need\'s direction is uncertain; L2 not evaluable.</div>';
 if(withCrit&&p.p)h+='<details data-crit="1"><summary>reasons, criteria, links</summary><div class="dd"></div></details>';
 h+='</div>';return h;}
function critHtml(p){
 var r=ROWS[p.r],n=NEEDS[p.n],c=p.p.cr,h='<p>'+esc(STR[p.p.w])+'</p><dl class="crit">';
 function row(k,v){h+='<dt>'+k+'</dt><dd>'+v+'</dd>';}
 row('WWOX relevance',esc(c.wwox[0])+' WWOX-system observation(s) in the need; need scopes: '+esc(c.wwox[1].join(', ')||'none')+'; intervention assertion scopes: '+(scopes(c.wwox[2])||'none'));
 row('Direction / mechanism','L2 '+esc(lbl(c.dir[0]))+'; sources: '+esc(c.dir[1].join(', ')||'none')+'; targets: '+esc(c.dir[2].join(', ')||'none'));
 row('Evidence quality and independence',esc(c.evq[0])+' card assertion(s), '+esc(c.evq[1])+' distinct source string(s); reading depth: '+(scopes(c.evq[2])||'none')+'. Shared sources are not independent confirmations.');
 row('Counter-evidence',esc(c.ctr[0])+' measured-null assertion(s) for this intervention; '+esc(c.ctr[1])+' counter-evidence item(s) on the need (text in the need panel)');
 if(p.l2&&p.l2[4]&&p.l2[4].length)row('Certainty qualifiers of the role rows',esc(p.l2[4].map(function(i){return STR[i];}).join(' | ')));
 if(p.l3&&p.l3[7])row('Enzyme or cell-free assays (not readouts)',esc(p.l3[7]));
 row('Potency and assay context',esc(c.pot));
 row('Transferability (a stated distance, not a score)','scopes: '+esc(c.tra[0].join(', ')||'none')+'; species: '+esc(c.tra[1].join(', ')||'none')+'; target system: WWOX-DEE reference genotype class');
 row('Pharmacology / safety info',esc(c.pha[0])+'; status: '+esc(c.pha[1].join(', ')||'none'));
 row('Discriminating experiment named',c.exp[0]?'yes: '+esc(c.exp[1].join(' | ')):'no');
 row('Next deepening',p.p.nd.length?'<ul>'+p.p.nd.map(function(i){return '<li>'+esc(STR[i])+'</li>';}).join('')+'</ul>':'none listed');
 row('Cards',r.cards.length?cardLinks(r.cards)+' ('+esc(r.cards.map(function(c){return c.att;}).join(', '))+')':'no card attached');
 row('Hypothesis ids (of the need)',esc(n.hyps.join(', ')||'none'));
 row('Need record',esc(n.id)+' in <code>needs/needs.json</code>; map: '+esc(n.map.join(', ')||'none')+'; registry: '+esc(n.reg.join(', ')||'none'));
 if(p.l3&&p.l3[1].length)row('L3 assertion ids',esc(p.l3[1].join(', '))+(p.l3[4]?' ('+p.l3[4]+' measured null)':''));
 if(p.l4&&p.l4[1].length)row('L4 assertion ids',esc(p.l4[1].join(', ')));
 if(p.p.dup)row('Possible duplicates',esc(p.p.dup)+' name twin family/families, not merged');
 return h+'</dl>';}
function pager(id,total,key,cb){var pages=Math.max(1,Math.ceil(total/PS));if(page[key]>=pages)page[key]=pages-1;
 var el=$(id);el.innerHTML='<button data-d="-1"'+(page[key]<=0?' disabled':'')+'>previous</button><span>page '+(page[key]+1)+' of '+pages+'</span><button data-d="1"'+(page[key]>=pages-1?' disabled':'')+'>next</button>';
 Array.prototype.forEach.call(el.querySelectorAll('button'),function(b){b.onclick=function(){page[key]+=+b.dataset.d;cb();};});}
// ---- views
var cur=[];var OPENALL=false;
function renderPairs(){
 cur=PAIRS.filter(pairOk);var pr=cur.filter(function(p){return p.p;});
 $('cnt-pairs').textContent=cur.length;$('cnt-prio').textContent=pr.length;$('cnt-pairs-of').textContent=PAIRS.length;$('cnt-prio-of').textContent=PAIRS.filter(function(p){return p.p;}).length;
 var lc={};['l1','l2','l3','l4'].forEach(function(k){lc[k]={};});cur.forEach(function(p){['l1','l2','l3','l4'].forEach(function(k){var s=p[k][0];lc[k][s]=(lc[k][s]||0)+1;});});
 $('lvl-now').innerHTML=['l1','l2','l3','l4'].map(function(k){return '<span class="chip"><b>'+k.toUpperCase()+'</b> '+Object.keys(lc[k]).sort().map(function(s){return esc(lbl(s))+': '+lc[k][s];}).join('; ')+'</span>';}).join(' ');
 var dc={};cur.forEach(function(p){var d=p.p?DISP[p.p.d].id:'(matrix only)';dc[d]=(dc[d]||0)+1;});
 $('disp-now').innerHTML=DISP.map(function(d){return '<span class="dp dp-'+esc(d.id)+'" data-dn="'+esc(d.id)+'">'+esc(d.id.replace(/_/g,' '))+': '+(dc[d.id]||0)+'</span>';}).join(' ')+' <span class="chip">matrix only: '+(dc['(matrix only)']||0)+'</span>';
 drawMatrix();drawPrio(pr);drawNeeds();}
function drawMatrix(){var tot=cur.length;pager('pg-m',tot,'m',drawMatrix);var s=page.m*PS,sl=cur.slice(s,s+PS);
 $('matrix-list').innerHTML=sl.length?sl.map(function(p){return pairHtml(p,false);}).join(''):'<p class="state-none">No pair matches these filters (a filter result, not a finding about the compounds).</p>';}
var prCur=[];
function drawPrio(pr){prCur=pr;pager('pg-p',pr.length,'p',function(){drawPrio(prCur);});var s=page.p*PS,sl=pr.slice(s,s+PS);var box=$('prio-list');
 box.innerHTML=sl.length?sl.map(function(p){return pairHtml(p,true);}).join(''):'<p class="state-none">No prioritised pair matches these filters.</p>';
 var ds=box.querySelectorAll('details[data-crit]');Array.prototype.forEach.call(ds,function(d,i){d.addEventListener('toggle',function(){var t=d.querySelector('.dd');if(d.open&&!t.innerHTML)t.innerHTML=critHtml(sl[i]);});});}
function lvlChips(n){var h='';['L1_documented_link','L2_mechanistic_coherence','L3_observed_effect','L4_observed_recovery_in_wwox_system'].forEach(function(L){var o=n.levels[L];h+='<div class="kv"><b>'+L.slice(0,2)+'</b> '+(Object.keys(o).length?Object.keys(o).map(function(s){return '<span class="chip v-'+esc(s)+'">'+esc(lbl(s))+': '+o[s]+'</span>';}).join(''):'<span class="chip">no cells</span>')+'</div>';});return h;}
function drawNeeds(){var ns=NEEDS.filter(needOk);$('cnt-needs').textContent=ns.length;
 $('needs-list').innerHTML=ns.map(function(n){var ni=NEEDS.indexOf(n),np=cur.filter(function(p){return p.n===ni;}).length;
  return '<div class="ncard'+(n.explore?' explore':'')+'" data-need="'+esc(n.id)+'"><h3>'+esc(n.id)+'</h3><div>'+esc(n.label)+'</div>'
  +'<div class="kv"><b>Desired direction:</b> '+esc(n.dir)+(n.explore?' <span class="dp dp-exploration_candidate">uncertain: exploration</span>':'')+' on '+esc(n.dir_on)+' <span class="mut">('+esc(n.dir_cert)+')</span></div>'
  +'<div class="kv"><b>Track</b> '+esc(n.track)+' - <b>goal</b> '+esc(n.goal)+'</div>'
  +'<div class="kv"><b>Evidence scopes:</b> '+n.scopes.map(function(s){return '<span class="chip">'+esc(s)+'</span>';}).join('')+'</div>'
  +'<div class="kv"><b>Headline link (intervention targets):</b> '+n.fam_headline+' families ('+n.rec_headline+' records), '+n.link_targets+' link target(s); not additive across needs</div>'
  +(n.fam_incl_pm!=null?'<div class="kv"><b>Incl. pathway members:</b> '+n.fam_incl_pm+' families ('+n.rec_incl_pm+' records)</div>':'')
  +'<div class="kv"><b>By target kind (records / families):</b> '+(Object.keys(n.by_kind).map(function(k){return '<span class="chip">'+esc(k.replace(/_/g,' '))+': '+n.by_kind[k].records+' / '+n.by_kind[k].families+'</span>';}).join('')||'none')+'</div>'
  +(Object.keys(n.excluded_by_reason).length?'<div class="kv"><b>Excluded from counts:</b> '+esc(JSON.stringify(n.excluded_by_reason))+'</div>':'')
  +'<div class="kv"><b>Levels (cells, never summed):</b></div>'+lvlChips(n)
  +'<div class="kv"><b>Pairs here:</b> '+n.n_pairs+' in the matrix, '+n.n_prio+' prioritised; '+np+' match the current filters</div>'
  +'<div class="kv"><b>Gaps:</b></div><ul>'+n.gaps.map(function(g){return '<li>'+esc(g)+'</li>';}).join('')+'</ul>'
  +'<details><summary>sources, counter-evidence ('+n.counter.length+'), not measured ('+n.inferred.length+')</summary>'
  +'<div class="kv"><b>Cards:</b> '+(n.cards.length?cardLinks(n.cards):'none')+'</div><div class="kv"><b>Hypothesis ids:</b> '+esc(n.hyps.join(', ')||'none')+'</div>'
  +'<div class="kv"><b>Map records:</b> '+esc(n.map.join(', ')||'none')+' <b>Registry:</b> '+esc(n.reg.join(', ')||'none')+' <b>Papers (registry ids):</b> '+esc([].concat.apply([],n.papers).join(', ')||'none')+'</div>'
  +'<div class="kv"><b>Targets:</b> '+esc(n.targets.map(function(t){return t[0]+' ('+t[1]+')';}).join(', ')||'none')+'</div>'
  +'<div class="kv"><b>Counter-evidence:</b></div>'+(n.counter.length?'<ul>'+n.counter.map(function(c){return '<li>'+esc(c)+'</li>';}).join('')+'</ul>':'<p class="mut">none recorded</p>')
  +'<div class="kv"><b>Not measured (inferred, do not assume):</b></div>'+(n.inferred.length?'<ul>'+n.inferred.map(function(c){return '<li>'+esc(c)+'</li>';}).join('')+'</ul>':'<p class="mut">none recorded</p>')
  +'<div class="kv"><b>Do not assume:</b> '+esc(n.dir_dna)+'</div></details>'
  +'<div class="bar-actions"><button data-pick="'+esc(n.id)+'">show this need\'s pairs</button></div></div>';}).join('')||'<p class="state-none">No need matches these filters.</p>';
 Array.prototype.forEach.call(document.querySelectorAll('[data-pick]'),function(b){b.onclick=function(){F.need=b.dataset.pick;sync();apply();location.hash='#matrix';};});}
// ---- filter state <-> controls <-> URL hash
var IDS={access:'f-access',need:'f-need',scope:'f-scope',oscope:'f-oscope',track:'f-track',goal:'f-goal',disp:'f-disp',q:'f-q'};
function sync(){Object.keys(IDS).forEach(function(k){$(IDS[k]).value=F[k];});}
function apply(){page.m=0;page.p=0;renderPairs();}
function fromHash(){var h=decodeURIComponent(location.hash||'');var m=h.match(/^#f=(.*)$/);if(!m)return;m[1].split('&').forEach(function(kv){var i=kv.indexOf(':');if(i>0){var k=kv.slice(0,i);if(k in F)F[k]=kv.slice(i+1);else if(k==='openall')OPENALL=true;}});}
Object.keys(IDS).forEach(function(k){$(IDS[k]).addEventListener(k==='q'?'input':'change',function(){F[k]=this.value;apply();});});
$('f-reset').onclick=function(){Object.keys(F).forEach(function(k){F[k]='';});sync();apply();};
window.addEventListener('hashchange',function(){fromHash();sync();apply();});
fromHash();sync();renderPairs();
if(OPENALL)Array.prototype.forEach.call(document.querySelectorAll('#prio-list details'),function(d){d.open=true;});
document.body.setAttribute('data-ready','1');
})();
"""

TEMPLATE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>WWOX repurposing: curated research view</title>
<style>__CSS__</style></head><body>
<a class="skip" href="#main">Skip to the content</a>
<header><div class="in"><h1>WWOX drug repurposing: what to study next, and on what evidence</h1>
<div class="mut">Local, regenerable, non-canonical research material (__SOURCELABEL__). Public disease and reference-genotype level only. Not a ranking of treatments, not a probability of benefit, not medical advice.</div></div></header>
__BANNER__<nav aria-label="Sections"><div class="in"><a href="#overview">Overview</a><a href="#navigate">Navigate</a><a href="#candidates">Candidates</a><a href="#priorities-cur">Priorities</a><a href="#compare">Compare</a><a href="#funnel">Full data</a><a href="#limits">Limits</a><a href="#technical">Technical</a><a href="#attribution">Sources</a></div></nav>
<main id="main">
__CURATED__
<section id="funnel"><h2>6. From catalogue to evaluated: what is counted, in which unit</h2>__FUNNEL__</section>
<section id="access"><h2>7. Distribution by access category</h2>__ACCESS__</section>
<section id="filters"><h2>Filters for the full matrix <span class="mut">(sections 8 to 10; shareable through the URL hash, for example <code>#f=disp:exploration_candidate&amp;need:NEED-ISR-ATTENUATION</code>)</span></h2>
<div class="filters">
<label>Access category<select id="f-access"></select></label><label>Need<select id="f-need"></select></label>
<label>Need evidence scope<select id="f-scope"></select></label><label>Observation scope (L3/L4)<select id="f-oscope"></select></label>
<label>Track<select id="f-track"></select></label><label>Recovery goal<select id="f-goal"></select></label>
<label>Disposition<select id="f-disp"></select></label><label>Text search<input type="search" id="f-q" placeholder="name, id, target, card, hypothesis"></label></div>
<div class="bar-actions"><button id="f-reset">reset filters</button><span><span class="cnt" id="cnt-pairs">0</span> of <span id="cnt-pairs-of">0</span> pairs match; <span class="cnt" id="cnt-prio">0</span> of <span id="cnt-prio-of">0</span> prioritised; <span class="cnt" id="cnt-needs">0</span> needs shown</span></div>
<div class="chips" id="lvl-now" aria-live="polite"></div><div class="chips" id="disp-now"></div></section>
<section id="needs"><h2>8. Needs: direction, Track, goal, evidence, levels, gaps</h2>
<p class="mut">A need is a place where the record observed something and an intervention could be aimed. Needs whose direction is <i>uncertain</i> are exploration only: L2 is not evaluable there. Level counts are cells (family, need) and are never summed across levels or needs.</p>
<div class="needs" id="needs-list"></div></section>
<section id="matrix"><h2>9. Matrix: interventions and compound families x needs</h2>
<p class="mut">Pair unit: __PAIRUNIT__. Four levels are shown side by side and never summed or scored. Scope is shown on L3 and L4.</p>
__LEVELS__
<div class="pager" id="pg-m"></div><div id="matrix-list"></div></section>
<section id="priorities"><h2>10. Dispositions: one per pair, with reasons per criterion</h2>
__DISPOSITIONS__
<div class="note">Dispositions are distinct: <b>source queried without result</b> (the sources were asked and returned no row for the record), <b>incomplete or failed query</b> (a source was not in state OK; this is never a negative) and <b>not relevant / no catalogue link found</b> and <b>insufficient data</b> (a decision from the data that exist) are different statements and are not merged.</div>
<div class="pager" id="pg-p"></div><div id="prio-list"></div></section>
<section id="leads"><h2>11. Catalogue-derived leads and lead dispositions</h2>__LEADS__</section>
<section id="limits"><h2>12. Honest limits</h2>__LIMITS__</section>
<section id="technical"><h2>13. Technical details (separate from the exploration above)</h2>__TECH__</section>
</main>
<footer id="attribution" aria-label="Sources and licences">__FOOTER__</footer>
<div id="export-area" aria-live="polite"></div>
<script id="data" type="application/json">__DATA__</script>
<script>__JS__</script>
<script>__CJS__</script>
</body></html>
"""


def read_asset(dr: Path, name: str) -> str:
    p = dr / "view/assets" / name
    if not p.exists():
        raise SystemExit(f"missing view asset {p}")
    return p.read_text(encoding="utf-8")


def render_overview(P: dict) -> str:
    """First screen, server-rendered from the payload so that it reads without JavaScript."""
    cur, f = P["cur"], P["funnel"]
    meta, cands, needs = cur["meta"], cur["cands"], cur["needs"]
    from urllib.parse import quote
    n_g = Counter(c["group"] for c in cands)

    def tile(key, val, unit, desc):
        return f'<div class="tile"><span class="big">{num(key, val)}</span><span class="u">{E(unit)}</span><span class="d">{E(desc)}</span></div>'
    t1 = "".join([
        tile("cur.needs", len(needs), "needs", "places where a WWOX-deficient system was observed and an intervention could be aimed"),
        tile("cur.threads", len(cur["threads"]), "biological threads", "groups of needs that share a biology"),
        tile("cur.cards", len(cands), "candidate cards", "an intervention, a class or an axis that has been read and written up"),
        tile("cur.abstentions", meta["n_abstentions"], "abstentions", "cards that name the missing datum instead of a test"),
        tile("cur.group1", n_g.get("G1", 0), "cards in Group 1", "the intervention itself was read out in a WWOX experimental system"),
    ])
    t2 = "".join([
        tile("funnel.records", f["records"], "catalogue records", "source-level substance records screened (salts and duplicates count once each)"),
        tile("funnel.families", f["families"], "catalogue families", "groupings of records; a family is not a distinct drug and not a candidate"),
        tile("funnel.records_with_action", f["records_with_action"], "records with a stated action on a need target", "headline: the source states an action; still a source statement, not evidence of effect or rescue"),
        tile("funnel.records_with_link", f["records_with_link"], "records with a target listed", "the larger count: includes records whose source states no action (listings, compilations, associations)"),
        tile("funnel.families_with_link", f["families_with_link"], "families with a target listed", "a listing is a source statement about a target, not modulation and not rescue"),
        tile("funnel.evaluated_records", f["evaluated_records"], "records evaluated against WWOX", "records with any observation against a WWOX need; not a count of tested drugs"),
    ])
    gtxt = {"deep_recovery": ("deep", "Broad, durable recovery"), "partial_benefit": ("partial", "Useful partial benefit")}
    panels = []
    for g, (cls, title) in gtxt.items():
        cs = [c for c in cands if c["goal"] == g]
        ns = [n for n in needs if n["goal"] == g]
        tr = Counter(c["track"] or "not stated" for c in cs)
        nxt = []
        for gid in ("G1", "G2", "G3"):
            names = [c for c in cs if c["group"] == gid]
            if names:
                nxt.append(f'<div class="kv"><span class="grp {gid.lower()}">{E(GROUPS[int(gid[1]) - 1]["label"].split(":")[0])}</span> ' + ", ".join(f'<a href="#cand-{E(c["id"])}" data-open="{E(c["id"])}">{E(c["short"])}</a>' for c in names) + "</div>")
        gaps, seen = [], set()
        for gid in ("G1", "G3", "G4"):
            for c in [c for c in cs if c["group"] == gid and c.get("missing") and c["missing"] not in seen][:2]:
                seen.add(c["missing"])
                gaps.append(f'<li><b>{E(c["short"])}:</b> {E(clip(c["missing"], 190))}</li>')
        panels.append(
            f'<div class="goal {cls}" data-goal="{g}"><h3>{E(title)}</h3><p class="mini">{E(GOALS[g])}. Kept apart from the other possibility: nothing below is added to it.</p>'
            f'<div class="kv"><b>Needs with this aim:</b> {num("cur.goal." + g + ".needs", len(ns))} needs (in: {E(", ".join(sorted({n["thread"] for n in ns})))})</div>'
            f'<div class="kv"><b>Candidate cards with this aim:</b> {num("cur.goal." + g + ".cards", len(cs))} cards, {sum(1 for c in cs if c["abstention"])} of them abstentions</div>'
            f'<div class="kv"><b>Track (a separate field):</b> ' + "; ".join(f"Track {E(k)}: {v}" for k, v in sorted(tr.items())) + '</div>'
            f'<div class="kv"><b>To study next (cards that name a next step), by evidence group:</b></div>' + ("".join(nxt) or '<p class="mini">None.</p>') +
            f'<div class="kv"><b>Decisive gaps (missing datum stated in the cards):</b></div><ul class="mini">' + "".join(gaps) + '</ul></div>')
    th = "".join(
        f'<div class="thread" data-thread="{E(t["id"])}"><h3>{E(t["name"])}</h3><p>{E(t["text"])}</p>'
        f'<p class="mini">{len(t["needs"])} needs ({t["goals"].get("deep_recovery", 0)} deep recovery, {t["goals"].get("partial_benefit", 0)} partial benefit); {t["wwox_obs"]} observations in WWOX systems (entries in the need records); {len(t["cards"])} candidate cards linked.</p>'
        f'<a href="#c=thread:{quote(t["id"])}">show this thread</a></div>' for t in cur["threads"])
    gaps = "".join(f'<li><b>{g["n"]} of {g["of"]}</b> {E(g["text"])}</li>' for g in cur["gaps"])
    dd = meta["data_date"]
    return (
        '<section id="overview" aria-labelledby="h-over"><h2 id="h-over">1. Overview</h2>'
        '<p class="lead"><b>Research goal.</b> Find out which existing drugs, supplements, diets and other interventions are worth testing for WWOX-related developmental and epileptic encephalopathy (WWOX-DEE), and say plainly what has been observed in WWOX, what is borrowed from other diseases or from predictions, what argues against it and what proof is missing.</p>'
        '<dl class="facts"><dt>Perimeter</dt><dd>WWOX-DEE, reference genotype class; public literature and public databases; no individual-level data. Research material for discussion, not medical advice.</dd>'
        f'<dt>Data date</dt><dd data-k="meta.data_date" data-v="{E(str(dd))}">{E(str(dd))} (catalogue and coverage build {E(str(meta["catalogue_generated"]))}; needs record {E(str(meta["needs_built_on"]))}). DGIdb export dated {E(meta["dgidb_export"])} (stale); this page reads no clock.</dd>'
        '<dt>Two open possibilities</dt><dd>Broad, durable recovery and useful partial benefit are two separate dimensions, shown side by side below and never combined. <b>Track A</b> (variant-independent) and <b>Track B</b> (variant- or lesion-specific) are a third, independent field.</dd></dl>'
        '<div class="goals">' + "".join(panels) + '</div>'
        '<div class="tilegroup">Curated work (read and written up)</div><div class="tiles">' + t1 + '</div>'
        '<div class="tilegroup">Catalogue screening (large numbers; not candidates)</div><div class="tiles">' + t2 + '</div>'
        '<p class="mini mut">Different units: a <b>need</b> is a biological question, a <b>card</b> is a written-up candidate, a <b>record</b> is one source entry, a <b>family</b> is a grouping of records. They are never added or compared as one number.</p>'
        '<h3>Main biological threads (the ' + str(len(needs)) + ' needs grouped)</h3><div class="threads">' + th + '</div>'
        '<h3>Decisive gaps, counted over the needs</h3><ul>' + gaps + '</ul></section>')


def render_footer(P: dict) -> str:
    ft = P["cur"]["footer"]
    h = [f'<h2>Sources, licences and attribution ({E(ft["source"])} build)</h2><p>{E(ft["note"])}</p><h3>Embedded as content</h3><ul>']
    for e in ft["embedded"]:
        u = f' <a href="{E(e["url"])}" rel="noopener noreferrer">{E(e["url"])}</a>' if e.get("url") else ""
        n = f' ({e["rows"]} association row(s) embedded)' if e.get("rows") else ""
        h.append(f'<li><b>{E(e["label"])}</b>{n}: {E(str(e.get("licence") or ""))}. {E(str(e.get("attribution") or ""))}{u}</li>')
    h.append("</ul>")
    if ft["counts_only"]:
        h.append("<h3>Contributed identifiers or counts only (content withheld)</h3><ul>")
        for e in ft["counts_only"]:
            h.append(f'<li><b>{E(e["label"])}</b>: {E(e["terms"])}' + (f'; version {E(str(e["version"]))}' if e.get("version") else "") + "</li>")
        h.append("</ul>")
    h.append('<p class="mini">Bibliographic identifiers (PubMed, DOI, ChEMBL) are public identifiers of cited works; titles shown come from PubMed records fetched into the module. Nothing here is medical advice.</p>')
    return "".join(h)


def render(P: dict, dr: Path = DEFAULT_DR) -> str:
    st = render_static(P)
    data = json.dumps(P, ensure_ascii=False, sort_keys=True, separators=(",", ":")).replace("</", "<\\/").replace("<!--", "<\\!--")
    page = TEMPLATE
    cur_html = read_asset(dr, "curated.html")
    cur_html = cur_html.replace("__OVERVIEW__", render_overview(P)).replace("__GROUPNOTE__", E(GROUP_NOTE))
    page = page.replace("__CSS__", CSS + read_asset(dr, "curated.css")).replace("__JS__", JS).replace("__CJS__", read_asset(dr, "curated.js"))
    page = page.replace("__CURATED__", cur_html).replace("__FOOTER__", render_footer(P))
    page = page.replace("__SOURCELABEL__", "shareable build: third-party rows limited to the allowlist" if P["source"] == "shareable" else "full local build: includes third-party rows, not for redistribution")
    for k, v in st.items():
        page = page.replace(f"__{k}__", v)
    page = page.replace("__PAIRUNIT__", E(str(P["pair_unit"])))
    page = page.replace("__DATA__", data)  # last: the data may contain placeholder-like text
    return page


def build(dr: Path = DEFAULT_DR, source: str = "full") -> str:
    out = render(build_payload(dr, source), dr)
    n = len(out.encode("utf-8"))
    if n > MAX_BYTES:
        raise SystemExit(f"view is {n} bytes, above the {MAX_BYTES} budget: trim the projection")
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0], formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", nargs="?", choices=["run", "check"], help="run: write the view; check: exit 1 if a file is stale")
    ap.add_argument("--dr", type=Path, default=DEFAULT_DR, help="drug_repurposing directory (default: the module)")
    ap.add_argument("--source", choices=list(SOURCES), default=None,
                    help="run: full (default) embeds every row, written to view/index.html; shareable embeds only allowlisted rows (view/shareable_sources.json), written to view/index_shareable.html. check: both unless given")
    ap.add_argument("--out", type=Path, default=None, help="output file (default: <dr>/view/index.html or index_shareable.html); with check and no --source, only valid for one source")
    a = ap.parse_args(argv)
    if not a.command:
        ap.print_help()
        return 0
    if a.command == "run":
        src = a.source or "full"
        out = a.out or (a.dr / "view" / OUT_NAME[src])
        text = build(a.dr, src)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text, encoding="utf-8")
        print(f"wrote {out} ({len(text.encode('utf-8')):,} bytes, source {src})")
        return 0
    rc = 0
    for src in ([a.source] if a.source else list(SOURCES)):
        out = a.out if (a.out and a.source) else (a.dr / "view" / OUT_NAME[src])
        text = build(a.dr, src)
        if not out.exists() or out.read_text(encoding="utf-8") != text:
            print(f"STALE: {out} differs from a fresh {src} build; run: python3 -B framework/scripts/repurposing_view.py run" + (" --source shareable" if src == "shareable" else ""))
            rc = 1
        else:
            print(f"view is current ({src})")
    return rc


if __name__ == "__main__":
    sys.exit(main())
