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
  python3 -B framework/scripts/repurposing_view.py run --source shareable   # the shareable view (allowlisted rows only)
  python3 -B framework/scripts/repurposing_view.py audit-shareable          # proof: no non-allowlisted value is in the shareable bytes
  python3 -B framework/scripts/repurposing_view.py package [--zip PATH]     # view/shareable_package/ (local preview, not published)
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
import textwrap
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


TITLES_NAME = "view/source_titles.json"
ESUMMARY = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
ESUMMARY_BATCH = 100      # ids per call
ESUMMARY_SLEEP = 0.5      # seconds between calls (>= 0.4: keyless E-utilities allow three requests per second)


def load_titles(dr: Path) -> dict:
    """PMID -> {"title","journal","year"}. Reads ONLY files (offline, deterministic): the tracked cache view/source_titles.json first,
    then the titles already fetched into join/pubmed_cache. Refresh the first with: repurposing_view.py titles --refresh"""
    out: dict = {}
    pc = dr / "join/pubmed_cache"
    if pc.exists():
        for f in sorted(pc.glob("*.json")):
            j = jload(f)
            if j.get("status") == "MATCH_FOUND" and j.get("title"):
                out[str(j.get("pmid"))] = {"title": j["title"], "journal": None, "year": None}
    p = dr / TITLES_NAME
    if p.exists():
        for k, v in (jload(p).get("titles") or {}).items():
            if v.get("title"):
                out[str(k)] = {"title": v["title"], "journal": v.get("journal"), "year": v.get("year")}
    return out


def cite_of(titles: dict, pmid) -> str | None:
    t = titles.get(str(pmid)) if pmid else None
    if not t:
        return None
    return f'{t["title"]}' + (f' ({", ".join(x for x in (t.get("journal"), t.get("year")) if x)})' if (t.get("journal") or t.get("year")) else "")


def referenced_pmids(dr: Path = None) -> list[str]:
    """Every PMID the cards and the needs point to (what the page prints a source line for)."""
    cur = build_payload(dr or DEFAULT_DR, "full")["cur"]
    ids = {p["id"] for c in cur["cands"] for p in c["pmids"]} | {str(o["pmid"]) for n in cur["needs"] for o in n["obs"] if o.get("pmid")}
    return sorted(ids)


def esummary_batch(ids: list[str], opener=None) -> dict:
    """ONE keyless NCBI esummary call for up to 100 ids. No e-mail, no tool parameter, no contact string of any kind."""
    import urllib.request
    from urllib.parse import urlencode
    url = ESUMMARY + "?" + urlencode({"db": "pubmed", "retmode": "json", "id": ",".join(ids)})
    req = urllib.request.Request(url, headers={"User-Agent": "legend-repurposing-view"})
    with (opener or urllib.request.urlopen)(req, timeout=60) as r:
        res = json.loads(r.read().decode("utf-8")).get("result") or {}
    out = {}
    for i in ids:
        e = res.get(i)
        if isinstance(e, dict) and e.get("title"):
            y = re.match(r"(\d{4})", str(e.get("pubdate") or ""))
            out[i] = {"title": " ".join(str(e["title"]).split()), "journal": e.get("source") or None, "year": y.group(1) if y else None}
    return out


def refresh_titles(dr: Path = None, ids: list[str] | None = None, fetch=None, sleep=None, refetch: bool = False) -> dict:
    """Fill view/source_titles.json for the referenced PMIDs that it does not hold (all of them with refetch=True)."""
    import time
    dr = dr or DEFAULT_DR
    path = dr / TITLES_NAME
    cache = jload(path) if path.exists() else {}
    have = cache.get("titles") or {}
    want = [i for i in (ids if ids is not None else referenced_pmids(dr)) if refetch or i not in have]
    fetch = fetch or esummary_batch
    nsleep = ESUMMARY_SLEEP if sleep is None else sleep
    for k in range(0, len(want), ESUMMARY_BATCH):
        if k:
            time.sleep(nsleep)
        have.update(fetch(want[k:k + ESUMMARY_BATCH]))
    doc = {"schema": "legend.wwox.source_titles/1", "source": "NCBI E-utilities esummary (db=pubmed), keyless, one call per 100 ids",
           "refresh": "python3 -B framework/scripts/repurposing_view.py titles --refresh", "titles": dict(sorted(have.items()))}
    path.write_text(json.dumps(doc, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    return doc


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


def access_category_allowed(cat: str, allow: dict) -> tuple[bool, str | None]:
    """(embeddable, source label) for one per-compound access category in the shareable build (IT5 P13).
    A category is kept only when the catalogue states it from a class-A scope (openFDA NDC, MATRIX); 'experimental' (ChEMBL)
    and 'supplement' (DSLD) are withheld from individual compounds; 'unknown/unverified' is an absence statement, not source content."""
    if cat == "unknown/unverified":
        return True, None
    for label, spec in (allow.get("access_scope_sources") or {}).items():
        if cat in (spec.get("categories") or []):
            return spec.get("class") == "A", label
    return False, None   # a category no source claims is not embedded (fail closed)


def share_excluded_rows(ex: dict) -> dict:
    """Shareable: an excluded row is a DGIdb row (compound name + gene); only its catalogue identifier and the counts are kept (IT5 P13: the string audit found the names here)."""
    out = dict(ex)
    if "alias_risk_rows_unresolved" in out:
        out["alias_risk_rows_unresolved"] = [{"catalogue_id": x.get("catalogue_id")} for x in out["alias_risk_rows_unresolved"]]
    return out


FILE_TOKEN_RE = re.compile(r"(?<![\w/.-])(?:[\w.-]+/)*[\w.-]+\.(?:md|tsv|py|jsonl|json|csv|gz)(?:#[\w-]+)?")
PACKAGE_FILE_NAMES = {"README.md", "NOTICE.md", "COMPARISON.md", "manifest.json", "TEXT_PROVENANCE.json", "index.html"}


def scrub_file_tokens(text: str, allow: dict) -> str:
    """Shareable: a repository file name cannot be used outside the repository; it is replaced by a plain description."""
    rep = (allow.get("prose_policy") or {}).get("file_token_replacement") or "a repository record"
    return FILE_TOKEN_RE.sub(lambda m: m.group(0) if m.group(0) in PACKAGE_FILE_NAMES or m.group(0).startswith("class_b/") else rep, text)


def _map_strings(o, fn):
    if isinstance(o, dict):
        return {k: _map_strings(v, fn) for k, v in o.items()}
    if isinstance(o, list):
        return [_map_strings(v, fn) for v in o]
    return fn(o) if isinstance(o, str) else o


def apply_prose_policy(P: dict, allow: dict) -> dict:
    """Shareable data boundary for prose (IT5 P13 fix): explicit, exact redactions of sentences that state a class-B/C compound-target pair, a catalogue-only compound or a
    per-compound status from a class-B/C source (rule: shareable_sources.json prose_policy), then repository file names. A redaction that matches nothing is a build error."""
    pol = allow.get("prose_policy") or {}
    # cards: substring replacements over every string of the cards' subtree
    hits = Counter()

    def cards_fn(t):
        for i, r in enumerate(pol.get("card_substrings") or []):
            if r["find"] in t:
                hits[("card", i)] += 1
                t = t.replace(r["find"], r["replace"])
        return t
    P["cur"]["cands"] = _map_strings(P["cur"]["cands"], cards_fn)
    for i, r in enumerate(pol.get("card_substrings") or []):
        if not hits[("card", i)]:
            raise SystemExit(f"stale prose redaction (no card text contains it): {r['find'][:80]}")
    leads = [dict(d) for d in P["leads"]]
    for j, r in enumerate(pol.get("lead_fields") or []):
        d = next((x for x in leads if x["id"] == r["id"]), None)
        if d is None or not str(d.get(r["field"]) or "").startswith(r["expect_startswith"]):
            raise SystemExit(f"stale lead redaction: {r['id']}.{r['field']}")
        d[r["field"]] = r["replace"]
    for r in pol.get("lead_substrings") or []:
        d = next((x for x in leads if x["id"] == r["id"]), None)
        if d is None or r["find"] not in str(d.get(r["field"]) or ""):
            raise SystemExit(f"stale lead redaction: {r['id']}.{r['field']}")
        d[r["field"]] = d[r["field"]].replace(r["find"], r["replace"])
    for d in leads:   # record and card files are repository paths: described, not printed
        if d.get("card"):
            d["card"] = "scheda " + Path(d["card"]).name.split(".")[0]
        if d.get("record"):
            d["record"] = "registro di ricerca del repository (non incluso in questo pacchetto)"
    P["leads"] = leads
    t = P["tech"]
    t["regeneration"] = pol.get("regeneration_text") or "see the package README"
    labels = pol.get("input_labels") or {}
    t["generated_from"] = {labels.get(k, k): v for k, v in (t.get("generated_from") or {}).items()}
    t["catalog_file"] = dict(t.get("catalog_file") or {}, path="catalogo dei composti")
    for k in ("leads", "tech", "cur", "needs", "funnel", "strings", "access", "observations", "dispositions", "level_defs", "excluded_detail", "card_leads"):
        P[k] = _map_strings(P[k], lambda x: scrub_file_tokens(x, allow))
    for k in ("leads_note", "pair_unit", "ranking_note", "no_probability"):
        if isinstance(P.get(k), str):
            P[k] = scrub_file_tokens(P[k], allow)
    return P


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
CARD_FILE_NOTE_IT = "scheda {id} (file del repository, non incluso in questo pacchetto)"
# ---------------------------------------------------------------------------------------------
# Research-priority positions (IT5 P11). One position per card AND per need. There is no global
# position of a card: the profile lists one position per need and the overview shows the SET of
# need-level positions. A position names the REASON a next study is interesting; it is not a rank,
# a score or a probability. All rules live in assign_need_position() so that they have one home.
# ---------------------------------------------------------------------------------------------
KIND_FAV, KIND_COUNTER, KIND_PREMISE = "favourable_hypothesis", "counter_evidence_clarification", "premise_missing"
GROUPS = [
    {"id": "F1", "kind": KIND_FAV, "label": "F1: Favourable hypothesis, controlled WWOX readout", "why": "Reason to study: a favourable result in a WWOX system, read against an untreated comparator of the same genotype from a full or partial text, with no null, unfavourable or mixed WWOX-system result beside it (rows outside WWOX are not part of this test and are shown as a tag), and a next step named. The page names the row that carries it; it is a reading-quality screen, not a size of effect."},
    {"id": "F2", "kind": KIND_FAV, "label": "F2: Favourable hypothesis, thin WWOX readout", "why": "Reason to study: a favourable result in a WWOX system, but uncontrolled (case reports, wild-type-only comparison) or of limited depth or specificity, with no null, unfavourable or mixed WWOX result beside it, and a next step named. The next study is to learn whether the signal is real."},
    {"id": "F3", "kind": KIND_FAV, "label": "F3: Favourable hypothesis from the target, intervention not tested in WWOX", "why": "Reason to study: the need has WWOX-system observations and the intervention has no readout in a WWOX system; what exists comes from other diseases or from target-engagement assays, with no counter-signal alone. A next step is named."},
    {"id": "C1", "kind": KIND_COUNTER, "label": "C1: Counter-evidence to clarify, null or unfavourable WWOX result", "why": "Reason to study: the only signed WWOX-system result is null or unfavourable. The next study is to learn whether that result is real (dose, timing, genotype, depth of reading), not to confirm a hope."},
    {"id": "C2", "kind": KIND_COUNTER, "label": "C2: Counter-evidence to clarify, mixed WWOX result", "why": "Reason to study: favourable and null or unfavourable WWOX results stand side by side for this need. The next study is to learn which one holds."},
    {"id": "C3", "kind": KIND_COUNTER, "label": "C3: Counter-evidence to clarify, harm or null signal from outside WWOX", "why": "Reason to study: no signed WWOX-system result, and what exists outside WWOX (other disease, safety, label) is harm or null with no favourable signal beside it. The next study is to learn whether that signal applies to WWOX."},
    {"id": "P1", "kind": KIND_PREMISE, "label": "P1: Premise missing, abstention", "why": "The card is an abstention: a datum is missing before any test can be designed. The missing datum is the first thing to obtain."},
    {"id": "P2", "kind": KIND_PREMISE, "label": "P2: Premise missing, no next step named", "why": "The card names no next step for this need, so no study can be put forward from it."},
    {"id": "P3", "kind": KIND_PREMISE, "label": "P3: Premise missing, nothing favourable recorded for this intervention on this need, or no WWOX-system observation on the need", "why": "No signed WWOX-system result of the intervention, no outside-WWOX counter-signal to clarify, and either no favourable support for the intervention recorded on this need or no WWOX-system observation on the need. The card links the need by mechanism only; what is missing is stated in the criteria."},
]
POS_BY_ID = {g["id"]: g for g in GROUPS}
GROUP_NOTE = ("Each candidate-need link has its own position, and the position states the REASON a study is interesting: a favourable hypothesis (F), a counter-evidence to clarify (C) or a missing premise (P). "
              "A card has no single position: its profile lists one per need, and the overview shows the set of need-level positions, never the best of them. "
              "The order in which positions are listed is a grouping by kind of reason, not a ranking; inside a position the order is alphabetical and means nothing. "
              "The criteria met and not met are printed with each position. There is no score, no probability and no cure ranking.")
# ---------------------------------------------------------------------------------------------
# Italian orientation texts (physician mode). DATA, not logic: the page reads them from the payload
# (D.ui) and from the server-side renderers; assets use {{key}} tokens. Scientific citations
# (titles, quotes, identifiers, source passages, compound names) are never translated.
# P13 (shareable package) reuses these dicts as they are.
# ---------------------------------------------------------------------------------------------
UI_IT = {
    # page frame
    "page_title": "WWOX: farmaci e interventi da studiare",
    "h1": "WWOX: che cosa studiare, e su quale evidenza",
    "sub": "Materiale di ricerca, non consiglio medico né graduatoria di trattamenti. Livello della malattia e del genotipo di riferimento, nessun dato individuale.",
    "skip": "Vai al contenuto",
    "src_share": "Versione condivisibile: le righe di terze parti sono limitate alla lista consentita.",
    "src_full": "Versione locale completa: include righe di terze parti, non per la ridistribuzione.",
    "nav_label": "Sezioni",
    "nav_overview": "Panoramica", "nav_threads": "Filoni", "nav_charts": "Grafici", "nav_navigate": "Esplora", "nav_cards": "Schede",
    "nav_priority": "Priorità", "nav_compare": "Confronto", "nav_tech": "Dettagli tecnici",
    "source_limited": "Alcune fonti hanno uno stato limitato",
    "source_limited_tail": "Un dato assente non è una conclusione sulla biologia.",
    "see_tech": "vedi i dettagli tecnici",
    # overview
    "ov_h": "Panoramica",
    "need_gloss": "Un «bisogno» è un obiettivo biologico: un'alterazione osservata in un sistema WWOX su cui un intervento potrebbe agire.",
    "ov_lead": "Quali farmaci, integratori, diete e altri interventi esistenti vale la pena studiare per l'encefalopatia epilettica e dello sviluppo legata a WWOX (WWOX-DEE)? Qui si vede che cosa è osservato in WWOX, che cosa viene da altre malattie o da previsioni, che cosa va contro e quale evidenza manca.",
    "warn_h": "Da tenere presente",
    "warn_1": "Materiale di ricerca per la discussione con il team clinico curante: non è un consiglio medico né un'indicazione di trattamento.",
    "warn_2": "Una lettera di priorità dice perché vale la pena studiare un intervento, non quanto funzioni: non è un punteggio né una probabilità.",
    "warn_3": "Che un'informazione manchi (accesso, esito, evidenza contraria) non significa che sia negativa: significa che non è stata ottenuta.",
    "how_h": "Come leggere in quattro passi", "how_sum": "Come leggere la pagina",
    "how_1": "Scegli un filone biologico qui sotto.",
    "how_2": "Guarda il motivo della priorità: la lettera F, C o P.",
    "how_3": "Apri la scheda del candidato per le sei risposte brevi.",
    "how_4": "Leggi l'evidenza che manca e il passo successivo informativo.",
    "legend_h": "Che cosa significano le lettere",
    "legend_note": "Le lettere sono motivi, non voti. Ogni legame tra candidato e bisogno ha la propria lettera; una scheda può averne più d'una e non ne esiste una «migliore».",
    "fam_F": "Ipotesi favorevole da verificare",
    "fam_C": "Evidenza contraria da chiarire",
    "fam_P": "Premessa mancante",
    "fam_F_txt": "un risultato favorevole, in WWOX o dal bersaglio, giustifica lo studio",
    "fam_C_txt": "un risultato nullo, misto o sfavorevole va chiarito prima di considerare l'ipotesi",
    "fam_P_txt": "manca un dato: è la prima cosa da ottenere",
    "facts_h": "In cifre (ogni numero ha la sua unità)",
    "unit_needs": "bisogni", "unit_threads": "filoni biologici", "unit_cards": "schede candidato", "unit_abst": "astensioni",
    "d_needs": "punti in cui in un sistema WWOX si è osservata un'alterazione su cui un intervento potrebbe agire",
    "d_threads": "gruppi di bisogni che condividono la stessa biologia",
    "d_cards": "interventi, classi o assi già letti e scritti in una scheda",
    "d_abst": "schede che indicano il dato mancante invece di un test",
    "unit_note": "Un bisogno è una domanda biologica, una scheda è un candidato scritto, un record è una voce di fonte, una famiglia è un raggruppamento di record: non si sommano né si confrontano come un solo numero.",
    "data_date": "Dati aggiornati al",
    "perimeter": "Perimetro",
    "perimeter_txt": "WWOX-DEE, classe del genotipo di riferimento; letteratura e basi dati pubbliche; nessun dato individuale.",
    "goals_h": "Due possibilità aperte, due dimensioni separate",
    "goal_links": "Legami candidato-bisogno per lettera (secondo l'obiettivo del bisogno)",
    "goal_cross": "I {total} legami candidato-bisogno sono contati tutti, ciascuno una volta, sotto l'obiettivo del bisogno; {cross} di essi collegano una scheda e un bisogno con obiettivi diversi, e per questo il numero di schede di un obiettivo e quello dei suoi legami non coincidono.",
    "goals_note": "Recupero ampio e beneficio parziale non si sommano e non si confrontano. Il Track (A: indipendente dalla variante; B: specifico della variante o della lesione) è un terzo campo indipendente.",
    "goal_deep": "Recupero ampio e duraturo",
    "goal_partial": "Beneficio parziale utile",
    "goal_deep_long": "Recupero ampio e duraturo (ripristinare la funzione WWOX perduta)",
    "goal_partial_long": "Beneficio parziale utile (farmaci, integratori, diete)",
    "needs_with_aim": "Bisogni con questo obiettivo",
    "cards_with_aim": "Schede con questo obiettivo",
    "of_which_abst": "di cui {n} astensioni",
    "track_field": "Track (campo separato)",
    "track_none": "non indicato",
    "track_A": "Track A: indipendente dalla variante (agisce qualunque sia l'allele WWOX)",
    "track_B": "Track B: specifico della variante o della lesione (una classe di alleli, un sito di splicing, un codone di stop)",
    "track_A_s": "Track A (indipendente dalla variante)", "track_B_s": "Track B (specifico di variante o lesione)", "track_none_s": "Track: non indicato nella scheda",
    # threads
    "th_h": "Filoni biologici: da dove partire",
    "th_note": "Ogni riquadro riassume un gruppo di bisogni che condividono la biologia: l'obiettivo, i candidati, il motivo della priorità, il tipo di evidenza e la lacuna decisiva.",
    "th_aim": "Obiettivo",
    "th_needs_n": "bisogni",
    "th_deep": "di recupero ampio", "th_partial": "di beneficio parziale",
    "th_cands": "Composti e interventi da studiare",
    "th_cands_none": "nessuna scheda candidato",
    "th_more": "altri",
    "th_why": "Motivo della priorità (un legame candidato-bisogno ciascuno)",
    "th_evid": "Tipo di evidenza osservata nei bisogni",
    "th_evid_none": "nessuna osservazione registrata",
    "th_gap": "Lacuna decisiva",
    "th_gap_wwox": "bisogni senza alcuna osservazione in un sistema WWOX",
    "th_gap_l4": "bisogni per cui nessun intervento ha un recupero osservato in WWOX",
    "th_gap_card": "Dato mancante dichiarato nella scheda",
    "th_explore": "Esplora questo filone",
    "th_obs_note": "(volume di osservazioni, non forza dell'evidenza)",
    # charts
    "ch_h": "Grafici: uno sguardo d'insieme",
    "ch_note": "Cinque grafici solo dove chiariscono. Nessun grafico misura l'efficacia: il numero di vie biologiche toccate, di pubblicazioni o di record non entra in alcuna priorità.",
    "g1_h": "1. Dal catalogo alle schede: che cosa viene contato, in quale unità",
    "g1_how": "Come leggere: ogni riga ha la sua unità. Le barre sono in scala solo entro la stessa unità (record con record, famiglie con famiglie); le schede non sono una frazione delle famiglie.",
    "g1_records": "Record di catalogo", "g1_families": "Famiglie (raggruppamenti di quei record)",
    "g1_fam_link": "Famiglie con un bersaglio elencato", "g1_fam_act": "Famiglie con un'azione dichiarata su un bersaglio di un bisogno", "g1_cards": "Schede candidato",
    "g1_u_records": "record", "g1_u_families": "famiglie", "g1_u_cards": "schede",
    "g1_rec_sub": "Stessa grandezza in record: {link} record con bersaglio elencato; {act} record con azione dichiarata su un bersaglio di un bisogno.",
    "g1_share": "delle {den} famiglie",
    "g1_note": "«Bersaglio elencato» è una dichiarazione di una fonte su un bersaglio, non modulazione e non recupero. «Azione dichiarata» dice che cosa fa il composto sul bersaglio (inibitore, agonista…): ancora una dichiarazione di fonte, non un'evidenza di effetto in WWOX. Una famiglia non è un farmaco distinto.",
    "g1_cards_note": "Unità diversa: composti o interventi che hanno una scheda scritta e letta.",
    "g2_h": "2. Categorie di accesso (evidenza prevalentemente USA)",
    "g2_how": "Come leggere: ogni barra è la quota dei {den} record di catalogo con quella categoria di accesso. Le categorie si sovrappongono (un record può avere evidenza sia OTC sia con prescrizione), quindi le barre non si sommano al totale.",
    "g2_unit": "record", "g2_of": "di", "g2_unknown": "senza alcuna evidenza di accesso",
    "g2_note": "Evidenza di accesso proveniente da openFDA e NIH DSLD (specifiche degli Stati Uniti) e da ChEMBL e MATRIX (non specifiche di un paese: per esempio lo stato «in sperimentazione» di ChEMBL non indica un paese), alle date di recupero riportate nei dettagli tecnici. Nessun paese è stato interrogato direttamente oltre agli Stati Uniti. «Sconosciuto» significa non ottenuto, non «non disponibile». Non è un'approvazione, né idoneità per una persona, né un'affermazione di sicurezza.",
    "acc_supplement": "integratore", "acc_OTC": "da banco (OTC)", "acc_prescription": "con prescrizione", "acc_experimental": "in sperimentazione", "acc_unknown/unverified": "sconosciuto o non verificato",
    "g3_h": "3. Bisogni per interventi: la lettera di ciascun legame",
    "g3_how": "Come leggere: una tabella per filone. Righe: schede candidato; colonne: bisogni. Ogni cella riporta la lettera e il suo significato in parole; la cella vuota (·) significa nessun legame. Il colore non è mai l'unico segnale: contano la lettera, il bordo e il testo.",
    "g3_cand": "Candidato", "g3_empty": "nessun legame",
    "g3_cell_F1": "ipotesi, esito WWOX controllato", "g3_cell_F2": "ipotesi, esito WWOX debole", "g3_cell_F3": "ipotesi dal bersaglio, nessun test in WWOX",
    "g3_cell_C1": "evidenza contraria: esito WWOX nullo o sfavorevole", "g3_cell_C2": "evidenza contraria: esito WWOX misto", "g3_cell_C3": "evidenza contraria da fuori WWOX",
    "g3_cell_P1": "astensione: manca un dato", "g3_cell_P2": "nessun passo successivo", "g3_cell_P3": "manca la premessa",
    "g4_h": "4. Meccanismo e candidati: quali bersagli sono toccati da quali composti",
    "g4_how": "Come leggere: a sinistra il bersaglio, a destra i candidati per cui una fonte dichiara un'azione su quel bersaglio. È una dichiarazione di fonte sul bersaglio, non un effetto in WWOX. «Opposta» significa contraria alla direzione voluta per il bisogno; «direzione non risolta» significa che il segno voluto non è noto.",
    "g4_target": "Bersaglio", "g4_cands": "Candidati e azione dichiarata", "g4_needs": "Bisogni su cui il bersaglio è elencato",
    "g4_none": "Nessuna azione dichiarata su un bersaglio è registrata nelle schede.",
    "g4_none_share": "In questa versione condivisibile le azioni dichiarate da fonti non incluse nella lista consentita non sono riportate: non significa che non esistano. La versione locale completa le contiene.",
    "g4_note": "Si tratta delle righe di catalogo collegate alle schede; il numero di vie biologiche non è mostrato perché non misura l'efficacia.",
    "act_down": "riduce", "act_up": "aumenta", "act_unresolved": "azione non risolta",
    "cons_consistent": "coerente con la direzione voluta", "cons_opposed": "opposta alla direzione voluta", "cons_direction_unresolved": "direzione non risolta",
    "g5_h": "5. Che cosa è stato misurato in un sistema WWOX e che cosa no",
    "g5_how": "Come leggere: per ogni bisogno, quattro domande con risposta in testo. «Sì» e «no» non sono giudizi di valore: dicono solo se il dato esiste nei registri.",
    "g5_need": "Bisogno",
    "g5_c1": "Osservazioni del bisogno in un sistema WWOX", "g5_c2": "Schede collegate", "g5_c3": "Schede con un esito dell'intervento in un sistema WWOX", "g5_c4": "Recupero osservato in WWOX (livello L4)",
    "g5_yes": "sì", "g5_no": "no", "g5_obs": "osservazioni", "g5_obs1": "osservazione", "g5_cards": "schede", "g5_cards1": "scheda",
    "g5_note": "Il conteggio delle osservazioni è un volume, non una forza dell'evidenza; «no» alla colonna L4 non è un risultato negativo: nessun intervento è stato ancora osservato recuperare quel bisogno in WWOX.",
    # navigate
    "nv_h": "Esplora: bisogno, meccanismo, composti e interventi, evidenza, prossima domanda",
    "nv_note": "Ogni riga segue un bisogno biologico: che cosa è stato osservato, quale meccanismo si potrebbe muovere, quali schede candidato lo mirano, quale evidenza c'è e quale domanda viene dopo. I filtri valgono per questa sezione, per le schede, per le priorità e per il confronto.",
    "f_label": "Filtri per le viste curate",
    "f_thread": "Filone biologico", "f_need": "Bisogno", "f_access": "Categoria di accesso (evidenza prevalentemente USA)", "f_country": "Evidenza per paese", "f_scope": "Tipo di evidenza",
    "f_track": "Track", "f_goal": "Obiettivo di recupero", "f_status": "Stato della ricerca", "f_q": "Cerca testo",
    "f_q_ph": "nome, id, id ChEMBL, bisogno",
    "f_any_thread": "tutti i filoni", "f_any_need": "tutti i bisogni", "f_any_access": "tutte le categorie", "f_any_country": "tutti", "f_any_scope": "tutti i tipi", "f_any_track": "tutti i Track", "f_any_goal": "tutti gli obiettivi", "f_any_status": "tutti gli stati",
    "f_reset": "azzera i filtri",
    "f_note": "Paese: l'evidenza di accesso proviene in parte da fonti statunitensi (openFDA, DSLD) e in parte da fonti non specifiche di un paese (ChEMBL, MATRIX); nessun altro paese è stato interrogato direttamente, quindi il filtro separa soltanto «evidenza di accesso trovata» da «nessuna ottenuta». Obiettivo: quello di un bisogno è proprio del bisogno; quello di una scheda è lo scopo scritto nella scheda, e i due possono differire.",
    "nv_c_need": "Bisogno", "nv_c_mech": "Meccanismo", "nv_c_comp": "Composti e interventi", "nv_c_evid": "Evidenza", "nv_c_next": "Prossima domanda",
    "nv_mech_lab": "Meccanismo (che cosa si muoverebbe)",
    "nv_dir": "Direzione voluta", "nv_on": "oggetto", "nv_targets": "Bersagli", "nv_none": "nessuno elencato",
    "nv_uncertain": "segno incerto: solo esplorazione",
    "nv_comp_none": "nessuna scheda ({n} famiglie di catalogo hanno un bersaglio elencato; un elenco non è un candidato)",
    "nv_evid_none": "nessuna osservazione registrata",
    "nv_evid_line": "{w} in un sistema WWOX (di cui {c} casi clinici non controllati); voci di evidenza contraria sul bisogno: {k}",
    "nv_next_none": "Nessuna scheda candidato indica un passo successivo per questo bisogno.",
    "nv_missing": "dato mancante",
    "nv_shown": "{a} di {b} bisogni mostrati",
    "nv_nomatch": "Nessun bisogno corrisponde a questi filtri (è un risultato del filtro, non una conclusione).",
    "count_line": "{n1} di {n2} bisogni e {c1} di {c2} schede corrispondono ai filtri",
    "dir_restore": "ripristinare", "dir_down": "ridurre", "dir_up": "aumentare", "dir_uncertain": "incerta",
    # cards
    "cd_h": "Schede candidato",
    "cd_shown": "mostrate",
    "cd_note": "Ogni scheda risponde brevemente a sei domande; i dettagli tecnici e le tabelle complete sono un clic più in basso. I tipi di evidenza non si fondono mai: un esperimento WWOX in un sistema DEE, la biologia WWOX in un altro contesto, un precedente di un'altra malattia, un risultato computazionale e un'ipotesi non verificata hanno etichette proprie.",
    "cd_order": "Ordine", "cd_o_group": "per insieme di lettere dei legami, poi A-Z", "cd_o_name": "A-Z",
    "cd_sel": "Selezione",
    "cd_sel_none": "Nessuna scheda selezionata. Spunta «seleziona per confronto o esportazione» su due-quattro schede.",
    "cd_sel_clear": "azzera la selezione", "cd_sel_export": "Esporta la selezione (stampa / PDF)",
    "cd_none": "Nessuna scheda corrisponde a questi filtri.",
    "cd_pick": "seleziona per confronto o esportazione",
    "cd_export": "Esporta questa scheda (stampa / PDF)",
    "cd_status": "Stato", "cd_access": "Accesso (evidenza prevalentemente USA)", "cd_access_none": "Accesso: nessuna identità di catalogo o nessuna evidenza ottenuta",
    "cd_no_need": "nessun bisogno collegato",
    "cd_noscope": "Nessuna affermazione sull'intervento ha un tipo di evidenza in questa scheda.",
    "q1": "1. Perché è in elenco", "q2": "2. Risultato in WWOX", "q3": "3. Precedente esterno o previsione", "q4": "4. Evidenza contraria", "q5": "5. Evidenza mancante", "q6": "6. Prossimo passo",
    "q1_needs": "Bisogni che affronterebbe", "q1_noneed": "Nessun bisogno è collegato a questa scheda.",
    "q2_own": "Questo intervento, provato in un sistema WWOX", "q2_none": "Nella scheda non è registrato alcun esito di questo intervento in un sistema WWOX.",
    "q2_ctx": "Osservazioni sui bisogni collegati in sistemi WWOX (contesto: possono riguardare altri interventi)", "q2_noctx": "I bisogni collegati non hanno osservazioni in sistemi WWOX.",
    "more_in_tech": "{n} altre nei dettagli tecnici.", "more_in_tech1": "{n} altra nei dettagli tecnici.",
    "q3_none": "Nessuno registrato.",
    "q4_note": "Come scritto nella scheda (pro e contro insieme, non elencati)",
    "q4_need": "Bisogno", "q4_none": "In questa scheda non è elencata alcuna evidenza contraria (l'assenza nella scheda non è un risultato negativo).",
    "q5_miss": "Dato mancante", "q5_nomiss": "Non è indicato alcun dato mancante.", "q5_reopen": "Condizione di riapertura",
    "q6_next": "Passo successivo informativo", "q6_none": "Non è indicato un passo successivo (scheda di astensione o di asse).",
    "full_text": "testo completo",
    "pos_why_h": "Perché ha questa lettera, bisogno per bisogno",
    "pos_for": "per",
    "tech_sum": "Dettagli tecnici e tabelle complete",
    "tc_identity": "Identità e meccanismo (come scritti nella scheda)", "tc_mech": "Meccanismo", "tc_novelty": "Novità e strade già note", "tc_pharm": "Farmacologia", "tc_access": "Accesso",
    "tc_links_h": "Tutti i bisogni collegati e perché la lettera è questa", "tc_need": "Bisogno", "tc_pos": "Lettera", "tc_crit": "Criteri",
    "tc_asserts": "Affermazioni sull'intervento nella scheda", "tc_scope": "Tipo di evidenza", "tc_stmt": "Affermazione", "tc_sys": "Sistema", "tc_depth": "Profondità di lettura", "tc_src": "Fonti",
    "tc_obs": "Osservazioni nei registri dei bisogni collegati", "tc_against": "Tutta l'evidenza contraria della scheda", "tc_for": "Evidenza a favore, come scritte nella scheda", "tc_notknown": "Non noto",
    "tc_actions": "Azioni di catalogo sui bersagli dei bisogni (dichiarazioni di fonte, non modulazione in un sistema WWOX)", "tc_target": "Bersaglio", "tc_action": "Azione", "tc_rel": "Relazione con la direzione voluta",
    "tc_sources": "Fonti per identificativo pubblico", "tc_nosrc": "Nessun identificativo pubblico è collegato a questa scheda.", "tc_compound_id": "identità del composto",
    "tc_cardfile": "File della scheda (percorso nel repository, solo uso locale)", "tc_assess": "Valutazione", "tc_bridge": "sintesi della direzione",
    "q2_other": "Altro materiale su WWOX (calcolo sui dati WWOX, o tipo di evidenza non registrato nella scheda)",
    "ex_lim_card": "Limiti scritti nella scheda (testo originale in inglese):",
    "tc_text_en": "Testo tecnico tratto dalla scheda, in inglese; può citare riferimenti interni (CLAIM n, A-xxx-n, T1, DL-…) non necessari alla lettura e non consultabili fuori dal repository.",
    "opposed": "OPPOSTA alla direzione voluta",
    "limits_note": "limiti",
    # priority
    "pr_h": "Priorità di ricerca: che cosa studiare ancora, e perché",
    "pr_note": "Si tratta di un raggruppamento per il motivo per cui uno studio è interessante, non di un ordine di schede e non di una graduatoria di efficacia: il numero di pubblicazioni, di vie biologiche toccate o una cella L4 non vi entrano. Ogni legame candidato-bisogno ha la propria posizione: ipotesi favorevole (F), evidenza contraria da chiarire (C) o premessa mancante (P). L'ordine delle posizioni è un raggruppamento per tipo di motivo; dentro una posizione l'ordine è alfabetico e non significa nulla. I criteri soddisfatti e non soddisfatti sono stampati con ogni posizione.",
    "pr_view": "Vista", "pr_by_need": "per bisogno", "pr_by_goal": "per obiettivo di recupero",
    "pr_sort": "Ordine dentro un gruppo", "pr_s_az": "A-Z (nessun ordine implicito)", "pr_s_wwox": "più esiti in sistemi WWOX (un volume, non una forza)", "pr_s_counter": "più voci di evidenza contraria (un volume, non un verdetto)",
    "pr_links": "legami", "pr_link": "legame",
    "pr_nolink": "Nessun legame candidato.",
    "pr_need_nocard": "Nessuna scheda candidato è collegata a questo bisogno. Per {n} famiglie di catalogo esiste un bersaglio elencato, ma è una dichiarazione di fonte e non un candidato.",
    "pr_axis_h": "Schede di asse senza bisogno collegato", "pr_axis_note": "Assi di endpoint o di ancoraggio: nessuna lettera si applica; sono elencate perché l'elenco completo resti raggiungibile.",
    "pr_open": "apri il profilo", "pr_open_card": "apri il profilo del candidato",
    "pr_goal_aim_diff": "lo scopo della scheda differisce da quello del bisogno",
    "pr_reasons": "motivi di questa posizione (criteri soddisfatti e non soddisfatti, e i fatti che li sostengono)",
    "pr_sum_wwox": "Esito in WWOX", "pr_sum_counter": "Evidenza contraria", "pr_sum_item": "voci", "pr_sum_item1": "voce", "pr_sum_prose": "in prosa", "pr_sum_next": "Passo successivo", "pr_next_yes": "indicato nella scheda", "pr_next_no": "non indicato",
    "pr_goal_needs": "bisogni con questo obiettivo", "pr_goal_links": "legami candidato-bisogno",
    "res_favourable": "favorevole", "res_mixed": "misto", "res_null": "nullo", "res_unfavourable": "sfavorevole", "res_unresolved": "non risolto", "res_none": "nessun esito in sistemi WWOX",
    "pr_w_counts": "esiti in sistemi WWOX: {w}; nulli: {nul}; sfavorevoli: {unf}",
    "crit_met": "soddisfatto", "crit_not": "non soddisfatto",
    "tag_tool": "composto-strumento, non un farmaco candidato", "tag_outside": "evidenza contraria fuori da WWOX in {n} righe", "tag_wt": "{n} confronto/i solo con wild type, contati in nessuna direzione",
    "tag_qual": "accanto a un braccio «non normalizzato rispetto al wild type»",
    # compare
    "cp_h": "Confronto tra pochi candidati",
    "cp_note": "Seleziona da due a quattro schede nelle schede candidato. Sono mostrati sovrapposizioni, copertura complementare e azioni opposte. Condividere un bisogno, o coprire bisogni diversi, non implica mai sinergia.",
    "cp_pick": "Seleziona da due a quattro schede per confrontarle.",
    "cp_caption": "Confronto di {n} schede candidato",
    "cp_dim": "Dimensione", "cp_aim": "Obiettivo di recupero", "cp_track": "Track", "cp_status": "Stato e lettere", "cp_needs": "Bisogni mirati (direzione voluta)",
    "cp_actions": "Azioni di catalogo sui bersagli dei bisogni", "cp_scopes": "Tipi di evidenza (affermazioni nella scheda)", "cp_against": "Voci di evidenza contraria nella scheda", "cp_missing": "Dato mancante",
    "cp_noact": "nessuna riga di azione di catalogo (scheda di classe, basata su gene o di asse: la direzione viene dal registro del bisogno)",
    "cp_noscope": "nessuna con tipo di evidenza", "cp_prose": "solo prosa", "cp_none": "nessuno", "cp_nostated": "non dichiarato",
    "cp_overlap": "Sovrapposizione", "cp_all": "Bisogni condivisi da tutte le schede selezionate", "cp_two": "Bisogni condivisi da almeno due", "cp_tg": "Bersagli in comune tra i bisogni di due o più schede",
    "cp_comp": "Complementarità (bisogni diversi, non un effetto congiunto)", "cp_alone": "— bisogni coperti solo da questa scheda", "cp_nothing": "nessuno: gli altri candidati coprono già gli stessi bisogni",
    "cp_opp_h": "Azioni opposte", "cp_opp_none": "Tra queste schede non è registrata alcuna azione opposta, né nelle righe di catalogo né nelle direzioni volute dei loro bisogni. È un'affermazione sui dati disponibili, non la dimostrazione che non esista.",
    "cp_opp_acts": "agisce su", "cp_opp_dir": "in senso opposto alla direzione voluta per", "cp_raises": "aumenta mentre", "cp_lowers": "riduce", "cp_on": "Su", "cp_wanted_diff": "La direzione voluta su {t} differisce tra bisogni",
    "cp_nosyn": "Non si inferisce alcuna sinergia.", "cp_nosyn_txt": "Condividere un bisogno, o coprirne di diversi, non dice nulla sul fatto che gli interventi funzionino insieme: interazioni, dosi e sicurezza combinata non sono valutate qui.",
    "cp_max": "Si possono confrontare al massimo quattro schede. Toglierne prima una.",
    "cp_opp_word": "OPPOSTA",
    # export
    "ex_back": "Torna alla vista", "ex_print": "Stampa o salva come PDF", "ex_dl": "Scarica come HTML autonomo", "ex_n": "Schede esportate: {n}. I collegamenti sono identificativi pubblici e restano validi fuori da questa cartella.",
    "ex_unknown": "Identificativo di scheda sconosciuto.", "ex_title": "Esportazione",
    "ex_card": "Scheda", "ex_data_date": "Dati aggiornati al", "ex_needs_rec": "registro dei bisogni", "ex_cat_build": "versione del catalogo",
    "ex_perim": "Perimetro", "ex_perim_txt": "encefalopatia epilettica e dello sviluppo legata a WWOX (WWOX-DEE), classe del genotipo di riferimento; solo letteratura e basi dati pubbliche; nessun dato individuale. Materiale di ricerca per la discussione con il team clinico curante: non è consiglio medico, non è una raccomandazione di trattamento, non è una probabilità di beneficio.",
    "ex_rationale": "Motivazione", "ex_needs": "Bisogni affrontati", "ex_evid": "Evidenza, per tipo", "ex_ctx": "Osservazioni registrate sui bisogni collegati: solo contesto, possono riguardare altri interventi.",
    "ex_need_obs": "osservazione sul bisogno", "ex_no_assert": "Nella scheda non è registrata alcuna affermazione con tipo di evidenza.",
    "ex_counter": "Evidenza contraria", "ex_counter_none": "Nessuna elencata nella scheda (l'assenza non è un risultato negativo).", "ex_asw": "Come scritto nella scheda",
    "ex_limits": "Limiti", "ex_lim_1": "Associazione non è modulazione, e modulazione non è recupero; un precedente di un'altra malattia non è un risultato WWOX.",
    "ex_lim_2": "I tipi di evidenza restano separati e non sono mai accorpati; fonti condivise non sono conferme indipendenti.",
    "ex_lim_3": "Le categorie di accesso sono evidenza di accesso trovata nelle fonti (prevalentemente USA) alle date di recupero (non approvazione, non idoneità per una persona, non sicurezza)",
    "ex_lim_4": "Il testo delle schede può citare riferimenti interni del repository (per esempio «CLAIM 031», «A-VGB-5», «T1», «DL-…», «verifica cieca», «nessuna ricevuta nel registro»): non servono alla lettura e non sono consultabili fuori dal repository. Solo gli identificativi nella tabella delle fonti sono pubblici.",
    "ex_miss": "Evidenza mancante e prossimo esperimento", "ex_next": "Passo successivo", "ex_srcs": "Fonti (identificativi pubblici)",
    "ex_gen": "Generato da repurposing_view.py", "ex_share": "Versione condivisibile: vedi il piè di pagina della pagina per le fonti incluse.", "ex_full": "Versione locale completa: non per la ridistribuzione.",
    "ex_std_title": "Scheda candidato WWOX",
    # IT6 P13: one-page synthesis (route #brief=)
    "cd_brief": "Sintesi (1 pagina)", "cd_sel_brief": "Sintesi (1 pagina) della selezione",
    "bf_title": "Sintesi di una pagina", "bf_std_title": "Sintesi WWOX di una pagina", "bf_card": "Scheda",
    "bf_n": "Sintesi esportate: {n}. Una pagina A4 per scheda; i collegamenti sono identificativi pubblici e restano validi fuori da questa cartella.",
    "bf_f1": "Domanda (il bisogno)", "bf_f2": "Candidato / intervento", "bf_f3": "Risultato WWOX", "bf_f4": "Precedente esterno", "bf_f5": "Controevidenze, per categoria",
    "bf_f6": "Dato mancante", "bf_f7": "Prossimo passo", "bf_f8": "Fonti essenziali (al massimo 5)",
    "bf_f5_note": "ordine per categoria: prima sicurezza e danno, poi risultati nulli o sfavorevoli in sistemi WWOX, poi controprove fuori da WWOX; dentro la categoria l'ordine della scheda; non è un giudizio di peso",
    "bf_counter_more": "{n} altre nella scheda",
    "bf_data_date": "Dati aggiornati al", "bf_cat_build": "Catalogo costruito il", "bf_dates_note": "tre date diverse: l'ultimo aggiornamento della ricerca (schede, bisogni, registri dei cicli), la data del registro dei bisogni e la costruzione del catalogo dei composti",
    "bf_dossier": "Dossier completo (3-4 pagine, appendice)", "bf_dossier_open": "Apri il dossier completo",
    "bf_dossier_std": "Nel file autonomo il dossier completo non è incluso: si apre dalla pagina principale con",
    "bf_warn": "Materiale di ricerca per la discussione con il team clinico curante: non è consiglio medico e non è una graduatoria di trattamenti. Associazione non è modulazione, e modulazione non è recupero.",
    "bf_wwox_ctx": "Nessun risultato dell'intervento in un sistema WWOX; osservazione del bisogno collegato",
    "bf_wwox_none": "Nessun risultato in un sistema WWOX registrato",
    "bf_ext_none": "Nessun precedente esterno registrato (l'assenza non è un risultato negativo)",
    "bf_counter_none": "Nessuna controevidenza registrata nella scheda (l'assenza non è un risultato negativo)",
    "bf_missing_none": "Nessun dato mancante indicato dalla scheda", "bf_next_none": "Nessun passo successivo nella scheda",
    "bf_src_none": "Nessuna fonte con identificativo pubblico", "bf_unknown": "Identificativo di scheda sconosciuto.", "bf_no_need": "nessun bisogno collegato",
    # IT6 P13: small evidence graph (server-rendered SVG)
    "nav_chains": "Catene di evidenza",
    "eg_h": "Catene di evidenza: dall'osservazione all'esperimento",
    "eg_lead": "Cinque catene tratte dai cicli di lavoro più recenti, lette da sinistra a destra: osservazione in un sistema WWOX, bisogno, meccanismo, intervento, evidenza, esperimento. Non è una rete di conoscenza e non misura l'efficacia: mostra su che cosa poggia ogni passaggio e che cosa manca.",
    "eg_note_en": "Le etichette dei nodi sono testo scientifico conservato nella lingua originale (inglese).",
    "eg_legend_h": "Legenda", "eg_leg_line": "Tipo di arco (stile della linea e lettera)", "eg_leg_nodes": "Riga sotto il nodo: ambito del dato",
    "eg_leg_R": "risultato sperimentale: l'esperimento citato ha misurato proprio quel legame",
    "eg_leg_I": "inferenza: ragionamento o trasferimento da un altro contesto, non misurato",
    "eg_leg_A": "associazione: compresenza, correlazione o elenco, senza prova di modulazione",
    "eg_scope_wwox": "sistema WWOX", "eg_scope_wwox_other": "WWOX, altro contesto", "eg_scope_non_wwox": "fuori WWOX (altra malattia o proteina)",
    "eg_scope_computational": "analisi su dati pubblici", "eg_scope_proposed": "proposto, non eseguito", "eg_scope_none": "",
    "eg_state_astensione": "astensione", "eg_state_ipotesi": "ipotesi", "eg_state_non_risolto": "NON RISOLTO", "eg_unres": "NON RISOLTO",
    "eg_scroll": "La figura scorre in orizzontale al suo interno; la pagina no.",
    "eg_no_interactome": "Un elenco di interattori (interattoma) non è mai disegnato come arco causale.",
    "eg_table_sum": "Testo alternativo: tabella degli archi", "eg_th_from": "Da", "eg_th_to": "A", "eg_th_type": "Tipo", "eg_th_src": "Fonte", "eg_th_note": "Nota",
    "eg_svg_desc": "{n} nodi e {m} archi; l'elenco completo è nella tabella degli archi sotto la figura.",
    "eg_date": "Catene scritte il", "eg_cue": "Scorri la figura in orizzontale per vedere tutte le colonne →", "wo_brief": "In breve", "bf_needs_rec": "Registro dei bisogni del", "ex_n1": "Scheda esportata: 1. I collegamenti sono identificativi pubblici e restano validi fuori da questa cartella.", "bf_n1": "Sintesi esportata: 1. Una pagina A4 per scheda; i collegamenti sono identificativi pubblici e restano validi fuori da questa cartella.", "eg_open_card": "apri il profilo",
    # IT6 P13: updated priorities and order of work
    "wo_h": "Piano di verifiche per bisogno",
    "wo_note": "Un elenco per bisogno, nell'ordine del registro dei bisogni: non è una sequenza di lavoro, non è una graduatoria di bisogni né di trattamenti e non ha punteggio. Per ogni bisogno: il motivo del prossimo studio (verificare un'ipotesi, chiarire una controevidenza o risolvere una premessa, coerente con le posizioni F, C, P del bisogno), una riga in italiano, la domanda, i dati che potrebbero risolverla, che cosa cambierebbe e la fattibilità realmente nota («non nota» quando non lo è).",
    "wo_update": "Aggiornamento della ricerca", "wo_catalogue": "Catalogo costruito il", "wo_dates_note": "due date diverse: la prima è l'ultimo aggiornamento di questo ordine di lavoro, la seconda la costruzione del catalogo dei composti",
    "wo_kind": "Motivo del prossimo studio", "wo_q": "Domanda", "wo_data": "Dati che potrebbero risolverla", "wo_change": "Che cosa cambierebbe", "wo_feas": "Fattibilità (solo ciò che è noto)",
    "wo_date": "Data", "wo_upd": "Aggiornato da", "wo_cards": "Schede coinvolte", "wo_pos": "Posizioni del bisogno", "wo_no_pos": "nessuna scheda collegata",
    "ws_prevented_early_window": "prevenzione (finestra precoce)", "ws_recovered_post_onset_model": "recupero dopo l'esordio (solo in un modello)",
    "ws_symptom_suppression_reversible": "soppressione sintomatica reversibile", "ws_unmeasured": "non misurato",
    "wo_window": "Finestra di intervento", "bf_window": "Finestra di intervento",
    "wo_see": "piano di verifiche di questo bisogno", "wo_text_en": "Testo scientifico in inglese, come memorizzato.", "wo_more": "Dettagli: dati, effetto, fattibilità",
    # technical drill-down
    "td_sum": "Dettagli tecnici",
    "td_note": "Versioni, impronte digitali, comando di rigenerazione, stati delle fonti e lo screening completo del catalogo. Sono separati dall'esplorazione sopra, in inglese tecnico, esaustivi e non ordinati: non sono elenchi di candidati.",
    "td_sources_h": "Stato delle fonti",
    "td_full_h": "Livello dati completo (lo screening dietro la vista curata)",
    "td_full_note": "Le sezioni seguenti sono lo screening completo del catalogo: imbuto, categorie di accesso, bisogni, matrice completa delle coppie, ogni disposizione di priorità, piste, limiti e dettagli tecnici. Sono esaustive, senza ordine e non sono elenchi di candidati. Testo tecnico in inglese.",
    "td_cit_note": "Titoli, citazioni e identificativi delle fonti sono riportati nella forma originale.",
    # footer
    "ft_h": "Fonti, licenze e attribuzione",
    "ft_build": "versione",
    "ft_embedded": "Incluse come contenuto", "ft_counts": "Contribuiscono solo con identificativi o conteggi (contenuto non incluso)", "ft_rows": "righe di associazione incluse",
    "ft_ids": "Gli identificativi bibliografici (PubMed, DOI, ChEMBL) sono identificativi pubblici di opere citate; i titoli mostrati provengono da registri PubMed raccolti nel modulo. Nulla di quanto qui riportato è consiglio medico.",
    "ft_version": "versione",
    "ft_idsrc": "Identificativi e fatti bibliografici (nessun contenuto di terzi oltre l'identificativo)",
    "ft_classb": "Contenuto share-alike distribuito in un file separato, non in questa pagina",
    "ft_classb_note": "Il contenuto ChEMBL (CC BY-SA 3.0) non è incorporato in questa pagina: i record ChEMBL e i meccanismi curati dei composti delle schede sono in un file a parte, con il proprio testo di licenza e la propria riga di credito. Questa pagina e quel file sono distribuiti insieme ma non fusi.",
    "ft_classb_where": "File nel pacchetto:",
    "ft_note_share": "Versione condivisibile: una riga di terze parti è inclusa solo se la sua provenienza è nell'elenco delle fonti consentite del repository. Tutto il resto compare come identificativo o conteggio. Nessuna attribuzione è stata rimossa. Licenze e attribuzioni sono riportate nella forma originale.",
    "ft_note_full": "Versione locale completa: include righe di terze parti (ChEMBL, DGIdb, openFDA, MATRIX) alle loro condizioni; le righe derivate da DGIdb non sono autorizzate alla diffusione pubblica e il contenuto ChEMBL è CC BY-SA 3.0. Per la circolazione usare la versione condivisibile.",
    # misc
    "chip_goal": "Obiettivo",
    "pub_year": "anno",
    "ui_lang_note": "Testi di orientamento in italiano; titoli, citazioni, identificativi, passaggi delle fonti e nomi dei composti restano nella forma originale.",
}

UI_IT7 = {
    # navigation
    "nav_selection": "Selezione", "nav_hyp": "Ipotesi a confronto", "nav_pred": "Prova e contesti",
    "sec_print": "Stampa questa sezione (A4)", "sec_title": "Sezione", "sec_unknown": "Sezione sconosciuta.",
    # selection funnel
    "sel_h": "Selezione dei composti: dal catalogo al prossimo test",
    "sel_lead": "Un imbuto costruito da unità misurate, in quest'ordine: catalogati, utilizzabili con un calcolo, valutati davvero, pertinenti per meccanismo, pronti per un test con nome. Ogni indicatore dice la sua unità e il suo denominatore; i composti sconosciuti o esclusi sono contati con il motivo. Non è una graduatoria e non è uno screening del catalogo.",
    "sel_units": "Unità. Un record è una voce di fonte (un sale o uno stereoisomero contano ciascuno una volta, e non sono farmaci distinti). Una famiglia è il «composto» di questo censimento e il numero di famiglie è un limite superiore dei composti distinti, perché le voci di sola fonte non si uniscono mai per nome. Una scheda è un intervento o una classe studiata, non un composto.",
    "sel_pv_h": "Presenti nel catalogo non significa valutati",
    "sel_pv_present_h": "Presenti nel catalogo", "sel_pv_present": "voci di fonte e famiglie elencate: una presenza in elenco, non un giudizio sul composto.",
    "sel_pv_eval_h": "Valutati", "sel_pv_eval0": "dai due metodi sul catalogo", "sel_pv_eval1": "famiglie nel confronto pilota (sottoinsieme esplorativo, non uno screening)", "sel_pv_eval2": "record con una lettura pertinente in un sistema WWOX",
    "sel_c_ind": "Indicatore", "sel_c_unit": "Unità", "sel_c_rec": "Record", "sel_c_fam": "Famiglie", "sel_c_den": "Denominatore", "sel_c_note": "Che cosa significa e che cosa manca",
    "sel_u_rf": "record e famiglie", "sel_u_f": "famiglie", "sel_u_r": "record", "sel_u_rows": "righe di bersaglio", "sel_u_cards": "schede", "sel_u_needs": "bisogni",
    "sel_of": "di", "sel_testable": "dei testabili", "sel_all": "del totale", "sel_pilot": "del sottoinsieme pilota",
    "sel_s_catalogued": "1. Catalogati", "sel_s_usable": "2. Utilizzabili con un calcolo", "sel_s_evaluated": "3. Valutati davvero", "sel_s_pertinent": "4. Pertinenti per meccanismo", "sel_s_ready": "5. Pronti per un test con nome",
    "sel_i_catalogued": "Catalogati", "sel_n_catalogued": "Le famiglie sono un limite superiore: lo stesso farmaco può comparire come famiglia ChEMBL e come famiglia di sola fonte.",
    "sel_i_source_only": "di cui famiglie di sola fonte, identità non risolta", "sel_n_source_only": "Non sono mai unite per nome.",
    "sel_i_l1": "Con almeno una riga di bersaglio", "sel_n_l1": "Una riga di meccanismo curato o di interazione: è una presenza in una banca dati.",
    "sel_i_l2": "Con azione documentata, superate le regole anti-artefatto", "sel_n_l2": "L'azione è quella che la fonte dichiara, non necessariamente una modulazione farmacologica: sono ammessi anche antigeni vaccinali, proteine esogene e agenti sequestranti.",
    "sel_i_mnet": "Utilizzabili dal metodo di rete (M-net): azione con segno su un bersaglio umano con identificativo stabile", "sel_n_mnet": "Un segno dichiarato dalla fonte, non misurato: non è potenza e non è rilevanza per WWOX.",
    "sel_i_mnet_corr": "di cui con una riga corroborata da ChEMBL o GtoPdb", "sel_n_mnet_corr": "Le tre fonti non sono voti indipendenti: si sovrappongono.",
    "sel_i_mnet_dgidb_only": "di cui voci della sola DGIdb, modalità sconosciuta", "sel_n_mnet_dgidb_only": "Un anticorpo o un peptide non si distingue da una piccola molecola; gli elenchi di DGIdb sono presi come dichiarati.",
    "sel_i_rows_excluded": "Righe di bersaglio escluse dalle regole anti-artefatto", "sel_n_rows_excluded": "Motivi: identità non confermata, artefatti di fonte, rischio di alias.",
    "sel_i_msig_testable": "Testabili dal metodo di firma (M-sig): hanno una chiave strutturale", "sel_n_msig_testable": "È il denominatore corretto per le quote M-sig.",
    "sel_i_msig_unknown": "Sconosciuti per M-sig: nessuna chiave strutturale", "sel_n_msig_unknown": "Non è un risultato negativo: senza struttura la firma non si può cercare. Motivi, in record:",
    "sel_b_dgidb_only": "solo DGIdb", "sel_b_chembl_selected": "ChEMBL senza struttura", "sel_b_openfda_unii_only": "solo openFDA", "sel_b_matrix_only": "solo MATRIX",
    "sel_i_msig_any": "Con una firma di composto in qualsiasi contesto cellulare (M-sig)", "sel_n_msig_any": "La quota sul solo testabile è la lettura corretta; quella sul totale la sottostima perché la maggior parte non si può testare.",
    "sel_i_msig_neural": "Con una firma in cellule di lignaggio neurale (M-sig, definizione stretta)", "sel_n_msig_neural": "Cellule neurali di genotipo sconosciuto, nessuna perturbazione di WWOX, nessuna glia, firme per lo più a una sola concentrazione.",
    "sel_i_eval_methods": "Valutati dai due metodi su tutto il catalogo", "sel_n_eval_methods": "Zero: «utilizzabile» è un requisito sull'input, non un risultato; nessun composto è stato punteggiato o ordinato dai metodi sul catalogo.",
    "sel_i_eval_p3": "Valutati nel confronto pilota", "sel_n_eval_p3": "Famiglie scelte per disponibilità di dati tra quelle del sottoinsieme pilota: NON è uno screening del catalogo. Il risultato misura l'opposizione di un modulo in cellule neurali selvatiche, non un effetto in cellule prive di WWOX.",
    "sel_i_eval_wwox_readout": "Con una lettura pertinente in un sistema WWOX", "sel_n_eval_wwox_readout": "Interventi con un'osservazione WWOX pertinente: è cosa diversa dal punteggio dei metodi.",
    "sel_i_need_link": "Con un legame documentato a un bisogno (bersaglio di intervento)", "sel_n_need_link": "Associazione di bersaglio: non è una predizione direzionale né un effetto osservato.",
    "sel_i_need_action": "di cui con un'azione dichiarata su un bersaglio del bisogno", "sel_n_need_action": "L'azione è dichiarata dalla fonte; la direzione verso il bisogno è risolta solo dove una riga di ruolo lo permette.",
    "sel_i_card_linked": "Famiglie collegate a una scheda curata", "sel_n_card_linked": "Il sottoinsieme che ha un'ipotesi scritta e un prossimo passo.",
    "sel_i_cards": "Schede curate", "sel_n_cards": "Interventi o classi, non composti: includono dieta, vettori e integratori.",
    "sel_i_cards_next": "Schede con un prossimo passo nominato (escluse le astensioni)", "sel_n_cards_next": "«Pronta per un test con nome» non significa «consigliata»: nessun composto è raccomandato e nessun dato individuale è usato.",
    "sel_i_needs_plan": "Bisogni con una voce nel piano di verifiche", "sel_n_needs_plan": "Il piano segue l'ordine del registro dei bisogni, senza graduatoria.",
    "sel_ov_h": "Sovrapposizione dei due metodi (firma neurale stretta contro rete), sul solo testabile",
    "sel_ov_note": "Nel «né l'uno né l'altro» del totale cadono anche i composti senza chiave strutturale, il cui stato M-sig è sconosciuto e non negativo: per questo qui il denominatore è il solo testabile.",
    "sel_ov_both": "entrambi", "sel_ov_net": "solo rete", "sel_ov_sig": "solo firma", "sel_ov_none": "nessuno dei due", "sel_ov_den": "denominatore",
    "sel_k_h": "Che cosa conta ogni numero: legami biologici e risultati sperimentali",
    "sel_k_note": "Unità: celle (famiglia o intervento × bisogno) della matrice; i livelli non si sommano mai e nessuno è una quota di malattia trattata.",
    "sel_k_l1": "Legame biologico: bersaglio dell'intervento documentato per il bisogno (associazione)", "sel_k_l2": "Coerenza meccanicistica: direzione coerente con il bisogno / opposta / direzione non risolta",
    "sel_k_l3": "Effetto osservato, di cui in un sistema WWOX", "sel_k_l4": "Recupero osservato in un sistema WWOX, di cui sperimentale",
    "sel_warn_share": "Una quota di vie biologiche o di bersagli collegati non è una quota di malattia trattata: un legame di bersaglio è un'associazione documentata, non una predizione direzionale né un effetto osservato.",
    "sel_warn_prob": "Nessuna probabilità clinica calibrata è mostrata, perché nessuna è stata validata; il percentile del modello non è mostrato affatto.",
    # hypotheses
    "hyp_model_none": "nessuna posizione del modello per questa ipotesi",
    "hyp_axis": "Confronto dei metodi sull'asse glicolisi/lattato: nessun vantaggio dimostrato, esplorativo",
    "hyp_axis_note": "Riguarda i metodi di ordinamento sul sottoinsieme pilota, non un giudizio sul composto: per questo composto il modello non dà alcuna posizione.",
    "hyp_r_firewalled": "Escluso di proposito dal confronto dei metodi perché ha una scheda curata (così il confronto non poteva essere regolato sui composti già discussi).",
    "hyp_r_not_compound": "Non è un composto con una riga di bersaglio: il metodo di rete non si applica.",
    "hyp_r_outside_question": "Fuori dalla domanda del confronto, che riguardava un modulo di trascritti glicolisi/lattato: proteine, recettori e glia non ne erano oggetto.",
    "hyp_usable": "I composti sono nel censimento degli utilizzabili (hanno l'input che un metodo richiede) ma non sono stati valutati.",
    "hyp_intro_model": "Posizione del modello: che cosa dice di questa ipotesi il confronto dei metodi (la prova predittiva, più sotto). Oggi non dice nulla di positivo per nessuna delle nove: «nessuna posizione» significa non valutata, non respinta, e «nessun vantaggio dimostrato» riguarda un metodo sul sottoinsieme pilota, mai un composto.",
    "hyp_key": "Chiave delle lettere: F ipotesi favorevole, C controevidenza da chiarire, P premessa mancante; il numero dice da dove viene il sostegno (1 controllato in un sistema WWOX, 2 sottile in WWOX, 3 dal bersaglio o da un'altra malattia). Sono posizioni, non un ordine.",
    "ctx_d_higher": "più alto", "ctx_d_lower": "più basso", "ctx_d_no_resolvable_sign": "nessun segno risolvibile", "ctx_d_UNKNOWN": "sconosciuto", "ctx_d_higher_sign_only": "più alto (solo segno)",
    "ctx_d_lower_sign_only": "più basso (solo segno)", "ctx_d_lower_non_specific": "più basso, non specifico", "ctx_d_set_dependent": "dipende dall'insieme di geni", "ctx_d_sparse": "dati troppo scarsi",
    "ctx_d_at_null_edge": "al margine del rumore", "ctx_d_changed_unsigned": "cambiato, senza segno", "ctx_c_note": "Nota", "ctx_v_no_resolved_sign": "nessun segno risolto nei sistemi misurati",
    "pred_ci_first": "intervallo di confidenza al 90%",
    "hyp_h": "Ipotesi a confronto: priorità di ricerca, posizione del modello ed evidenza osservata",
    "hyp_lead": "Nove ipotesi che coprono i due obiettivi di ricerca e diversi tipi di intervento, scelte per copertura e non per merito. Tre cose restano separate, in blocchi distinti: la priorità di ricerca (posizione F, C o P e motivo del piano di verifiche: dice dove portare il prossimo studio, non se il farmaco funziona), la posizione del modello e l'evidenza osservata in un sistema WWOX. Nessun punteggio combinato, nessun ordine.",
    "hyp_note_en": "Il testo scientifico dei blocchi è in inglese, come nel confronto originale. Concentrazioni e percentuali citate dalle fonti descrivono studi esterni: non sono una guida alla dose e non sono evidenza WWOX.",
    "hyp_prio": "Priorità di ricerca", "hyp_prio_card": "scheda", "hyp_prio_on": "sul bisogno", "hyp_plan": "Piano di verifiche",
    "hyp_model": "Posizione del modello",
    "hyp_obs": "Evidenza osservata in un sistema WWOX", "hyp_dem": "Favorevole: premessa dimostrata", "hyp_opp": "Contraria: effetti opposti o controevidenza", "hyp_missing": "Mancante: premessa non dimostrata",
    "hyp_ext": "Precedenti esterni (non sono evidenza WWOX)", "hyp_ctx": "Contesto di applicabilità", "hyp_track": "Track e genotipo", "hyp_depth": "Profondità del beneficio cercato", "hyp_next": "Prossimo esperimento", "hyp_status": "Stato dell'esperimento",
    "hyp_more": "Dettagli: contesto, evidenza favorevole, contraria e mancante, prossimo esperimento",
    "hyp_none_plan": "nessuna voce nel piano",
    # predictive test
    "pred_h": "Prova predittiva: un confronto esplorativo di metodi", "pred_label": "ESPLORATIVO: un risultato computazionale non è efficacia terapeutica",
    "pred_q": "Domanda", "pred_methods": "Metodi", "pred_prereg": "Pre-registrazione", "pred_prereg_txt": "Domanda, metodi, soglie e criteri sono stati registrati prima di aprire qualsiasi valore di valutazione; un emendamento ha congelato di nuovo gli input, ancora prima di aprirne uno. Nessun criterio è stato cambiato dopo un risultato.",
    "pred_universe": "Universo valutato", "pred_universe_txt": "famiglie con {s} firme, scelte per disponibilità di dati tra le {p} del sottoinsieme pilota ({c} famiglie nel catalogo): un sottoinsieme esplorativo, NON uno screening del catalogo.",
    "pred_threshold": "Soglia registrata e potenza", "pred_threshold_txt": "Soglia rho {t}; con {n} famiglie il minimo effetto rilevabile è circa {m}: effetti più piccoli non sono esclusi. «Nessun vantaggio» significa nessun guadagno rilevabile, non che i composti non agiscano sul modulo.",
    "pred_verdict_h": "Verdetto per metodo", "pred_c_cmp": "Confronto", "pred_c_verdict": "Verdetto", "pred_c_num": "Numeri", "pred_c_reopen": "Si riapre se",
    "pred_v_no_added_value": "nessun vantaggio aggiunto (nessun segnale rilevabile)", "pred_v_not_detected_not_excluded": "effetto non rilevato, non escluso", "pred_v_inconclusive": "non conclusivo",
    "pred_limits_h": "Limiti",
    "pred_methods_ids": "REF-1 riferimento senza segno; NET-EXT rete con segno solo esterna; NET-WWOX rete con archi WWOX; SIG via della firma",
    # contexts
    "ctx_h": "Confronto tra contesti: concordanze e discordanze tra i sistemi con perdita di WWOX",
    "ctx_lead": "Per ogni quantità, che cosa mostrano i sistemi in cui WWOX è perso. Livello del trascritto salvo dove indicato; i contesti sono più numerosi dei modelli indipendenti.",
    "ctx_facts": "{cells} celle ({contexts} contesti × {quantities} quantità): {measured} con una misura o un dato riportato e {unknown} sconosciute. Le sconosciute sono lacune, non zeri. Contando i modelli e non le colonne, i sistemi indipendenti sono circa {models}.",
    "ctx_no_subgroup": "Nessun sottogruppo di pazienti è sostenuto da questi dati: nessuna etichetta di risposta, nessun gruppo computazionale offerto come biomarcatore. I contesti sono sistemi modello, non pazienti.",
    "ctx_models_h": "Modelli", "ctx_c_q": "Quantità", "ctx_c_hi": "più alto (n. contesti)", "ctx_c_lo": "più basso (n. contesti)", "ctx_c_ns": "nessun segno (n. contesti)", "ctx_c_unk": "sconosciuto (n. contesti)", "ctx_c_models": "modelli con segno risolto", "ctx_c_verdict": "Lettura",
    "ctx_v_concordant": "concordante", "ctx_v_discordant": "discordante", "ctx_v_single_system": "un solo sistema", "ctx_v_no_data": "nessun dato",
    "ctx_def": "La lettura è derivata dalla regola, non assegnata a mano. Discordante: segni risolti di direzione opposta. Concordante: lo stesso segno risolto in almeno due modelli e nessuno opposto. Un solo sistema: segno risolto in un solo modello. Nessun segno risolto: le celle misurate sono tutte dentro il rumore. Nessun dato: nulla è misurato. Un segno è «risolto» solo se distinguibile dal rumore con il criterio della fonte, e si contano i modelli, non le colonne. La lettura prudente del documento originale può essere più cauta: la nota di ogni riga lo dice.",
    "ctx_full": "Matrice completa (quantità × contesto)", "ctx_total": "Totale",
}
UI_IT.update(UI_IT7)


POS_IT = {
    "F1": {"short": "ipotesi favorevole, esito WWOX controllato",
           "label": "F1 · Ipotesi favorevole, esito WWOX controllato",
           "plain": "Un risultato favorevole in un sistema WWOX, letto contro un gruppo non trattato dello stesso genotipo da un testo completo o parziale, senza risultati nulli, sfavorevoli o misti in WWOX accanto, e con un passo successivo indicato. È un controllo della qualità di lettura, non la misura di un effetto."},
    "F2": {"short": "ipotesi favorevole, esito WWOX debole",
           "label": "F2 · Ipotesi favorevole, esito WWOX debole",
           "plain": "Un risultato favorevole in un sistema WWOX, ma non controllato (casi clinici, confronto solo con wild type) o di profondità o specificità limitata, senza risultati nulli o sfavorevoli accanto. Lo studio serve a capire se il segnale è reale."},
    "F3": {"short": "ipotesi favorevole dal bersaglio, non provata in WWOX",
           "label": "F3 · Ipotesi favorevole dal bersaglio, non provata in WWOX",
           "plain": "Il bisogno ha osservazioni in sistemi WWOX, ma l'intervento non è stato testato in WWOX; ciò che esiste viene da altre malattie o da saggi sul bersaglio, senza controsegnali. Un passo successivo è indicato."},
    "C1": {"short": "evidenza contraria da chiarire, esito WWOX nullo o sfavorevole",
           "label": "C1 · Evidenza contraria da chiarire, esito WWOX nullo o sfavorevole",
           "plain": "L'unico risultato con segno in WWOX è nullo o sfavorevole. Lo studio serve a capire se quel risultato è reale (dose, tempi, genotipo, profondità di lettura), non a confermare una speranza."},
    "C2": {"short": "evidenza contraria da chiarire, esito WWOX misto",
           "label": "C2 · Evidenza contraria da chiarire, esito WWOX misto",
           "plain": "Per questo bisogno, risultati favorevoli e nulli o sfavorevoli in WWOX stanno uno accanto all'altro. Lo studio serve a capire quale dei due regga."},
    "C3": {"short": "evidenza contraria da chiarire, danno o nullo da fuori WWOX",
           "label": "C3 · Evidenza contraria da chiarire, danno o segnale nullo da fuori WWOX",
           "plain": "Nessun risultato con segno in WWOX; ciò che esiste fuori da WWOX (altra malattia, sicurezza, etichetta) è dannoso o nullo, senza un segnale favorevole accanto. Lo studio serve a capire se vale anche per WWOX."},
    "P1": {"short": "premessa mancante, astensione",
           "label": "P1 · Premessa mancante, astensione",
           "plain": "La scheda è un'astensione: manca un dato prima di poter progettare un test. Il dato mancante è la prima cosa da ottenere."},
    "P2": {"short": "premessa mancante, nessun passo successivo",
           "label": "P2 · Premessa mancante, nessun passo successivo indicato",
           "plain": "La scheda non indica un passo successivo per questo bisogno, quindi da essa non si può proporre alcuno studio."},
    "P3": {"short": "premessa mancante, nessun elemento favorevole registrato",
           "label": "P3 · Premessa mancante, nessun elemento favorevole registrato",
           "plain": "Nessun risultato con segno dell'intervento in WWOX e nessuna evidenza contraria da chiarire da fuori WWOX; inoltre manca ogni sostegno favorevole registrato per questo bisogno oppure manca ogni osservazione in sistemi WWOX sul bisogno. La scheda collega il bisogno solo per meccanismo; ciò che manca è dichiarato nei criteri."},
}
SCOPE_IT = {
    "WWOX_EXPERIMENT_IN_DEE_SYSTEM": "Esperimento WWOX in un sistema DEE",
    "WWOX_CLINICAL_CASE": "Caso clinico WWOX (non controllato)",
    "WWOX_BIOLOGY_OTHER_CONTEXT": "Biologia WWOX in un altro contesto",
    "OTHER_DISEASE_PRECEDENT": "Precedente in un'altra malattia",
    "COMPUTATIONAL_RESULT": "Risultato computazionale",
    "TARGET_ENGAGEMENT": "Saggio enzimatico o privo di cellule",
    "EXTERNAL_DATABASE_RECORD": "Voce di una base dati esterna",
    "SAFETY_SIGNAL": "Segnale di sicurezza",
    "UNVERIFIED_HYPOTHESIS": "Ipotesi non verificata",
    "UNCLASSIFIED": "Tipo di evidenza non registrato a livello di affermazione",
}
GOALS_IT = {"deep_recovery": "Recupero ampio e duraturo (ripristinare la funzione WWOX perduta)", "partial_benefit": "Beneficio parziale utile (farmaci, integratori, diete)"}
THREAD_IT = {
    "WWOX restoration": ("Ripristino di WWOX", "Riportare WWOX stesso: aggiungere il gene, correggere il trascritto, superare un codone di stop, salvare una proteina mal ripiegata o aumentare l'espressione endogena."),
    "Stress signalling and metabolism": ("Stress cellulare e metabolismo", "Vie di stress e di energia che appaiono alterate quando WWOX manca: risposta integrata allo stress, gestione di piruvato e lattato, respirazione mitocondriale, equilibrio redox."),
    "Network excitability": ("Eccitabilità di rete", "Perché i neuroni scaricano troppo: guadagno eccitatorio, inibizione debole, la premessa cloro e GABA, canali del calcio di tipo T."),
    "Signalling": ("Segnalazione di crescita e sopravvivenza", "Vie di crescita e sopravvivenza che WWOX normalmente frena: GSK3beta, Wnt/beta-catenina, mTOR e autofagia."),
    "Development and glia": ("Sviluppo e glia", "Sviluppo del cervello e cellule di supporto: mielina, proliferazione dei progenitori (MYC), neuroinfiammazione e gliosi."),
    "Symptom-level": ("Sintomi", "Sintomi trattati di per sé: crisi e spasmi, glicemia e crescita."),
}
NEED_IT = {
    "NEED-WWOX-GENE-ADDITION": "Ripristinare la proteina WWOX nei neuroni aggiungendo il gene",
    "NEED-WWOX-SPLICE-CORRECTION": "Ripristinare il trascritto WWOX corretto in un allele con accettore di splicing canonico alterato",
    "NEED-WWOX-PTC-READTHROUGH": "Superare un codone di stop prematuro in un allele non senso di WWOX",
    "NEED-WWOX-MISSENSE-PROTEIN-RESCUE": "Salvare una proteina WWOX destabilizzata da una variante missenso del dominio SDR",
    "NEED-WWOX-ENDOGENOUS-BOOST": "Aumentare l'espressione endogena di WWOX",
    "NEED-ISR-ATTENUATION": "Risposta integrata allo stress",
    "NEED-PDH-PYRUVATE-AXIS": "Ingresso del piruvato nel ciclo di Krebs",
    "NEED-LACTATE-LDH": "Lattato e attività della lattato deidrogenasi",
    "NEED-MITOCHONDRIAL-RESPIRATION": "Respirazione mitocondriale e capacità di fosforilazione ossidativa",
    "NEED-EXCITATORY-GAIN-GLUTAMATE-RECEPTOR": "Guadagno eccitatorio di rete e scariche a raffica",
    "NEED-INHIBITORY-HYPOFUNCTION": "Controllo inibitorio",
    "NEED-GABA-CHLORIDE-GRADIENT": "Gradiente del cloro e polarità GABA",
    "NEED-SEIZURE-CONTROL-SYMPTOMATIC": "Controllo di crisi e spasmi come bisogno sintomatico",
    "NEED-T-TYPE-CALCIUM": "Sensibilità all'etosuccimide della crisi provocata nella perdita di Wwox",
    "NEED-MYELINATION": "Ipomielinizzazione",
    "NEED-GSK3B-DEREPRESSION": "Derepressione di GSK3beta",
    "NEED-WNT-BETA-CATENIN": "Segnale Wnt/beta-catenina elevato negli organoidi privi di WWOX",
    "NEED-MYC-PROGENITOR-PROLIFERATION": "Aumento di MYC e spostamento dello stato dei progenitori nella glia radiale priva di WWOX",
    "NEED-MTOR-AUTOPHAGY": "Segnalazione mTOR e autofagia",
    "NEED-NEUROINFLAMMATION-GLIA": "Neuroinfiammazione e gliosi",
    "NEED-REDOX-OXIDATIVE-STRESS": "Equilibrio redox e specie reattive dell'ossigeno",
    "NEED-SYSTEMIC-GLYCAEMIA-GROWTH": "Scompenso metabolico sistemico",
}
STATUS_IT = {"abstention": "astensione", "hypothesis": "ipotesi", "controversial": "controversa", "deferred with reason": "rinviata con motivo"}
COUNTRY_IT = {"US evidence found": "evidenza di accesso trovata (prevalentemente USA)", "no country evidence obtained": "nessuna evidenza per paese ottenuta"}
CRIT_IT = {
    "the card is not an abstention": "la scheda non è un'astensione",
    "a next step is named": "è indicato un passo successivo",
    "a signed result of the intervention in a WWOX system exists": "esiste un risultato con segno dell'intervento in un sistema WWOX",
    "no null, unfavourable or mixed result in a WWOX system": "nessun risultato nullo, sfavorevole o misto in un sistema WWOX",
    "a favourable WWOX readout has an untreated same-genotype comparator": "un esito favorevole in WWOX ha un confronto non trattato dello stesso genotipo",
    "a favourable WWOX readout is from a full or partial text reading": "un esito favorevole in WWOX deriva dalla lettura del testo completo o parziale",
    "a favourable WWOX readout carries no reading-limit flag": "un esito favorevole in WWOX non porta limiti di lettura (profondità, lettura grafica, solo micrografie, lettura parziale)",
    "a favourable WWOX readout carries no design-limit flag": "un esito favorevole in WWOX non porta limiti di disegno sperimentale (composto strumentale, aspecifico anche nel selvatico, un solo esperimento, caso singolo, senza strumento, senza braccio knockout)",
    "the signed rows behind this position were read beyond abstract, query or unknown depth": "le righe con segno su cui poggia questa posizione sono state lette oltre l'abstract, la query o una profondità ignota",
    "one and the same readout meets all four": "uno stesso esito soddisfa tutti e quattro i criteri",
    "an outside-WWOX harm or null signal stands without a favourable outside signal": "fuori da WWOX esiste un segnale di danno o nullo, senza segnale favorevole esterno",
    "some favourable support for the intervention is recorded on this need (other-disease readout or target-engagement assay)": "per questo bisogno è registrato qualche sostegno favorevole all'intervento (esito in un'altra malattia o saggio sul bersaglio)",
    "the need has a WWOX-system observation": "il bisogno ha un'osservazione in un sistema WWOX",
}

FAV_SIGNS = {"benefit", "partial_benefit", "normalised_vs_wild_type"}
CARRIER_SIGNS = {"benefit"}   # IT6 P2: a partial benefit (postponement, intermediate level) is favourable for the result but never carries F1
WWOX_KINDS = {"readout_in_wwox_system", "case_report_wwox_clinical", "genotype_comparison_vs_wild_type"}
OUT_KINDS = {"readout_other_disease", "safety_signal", "label_statement", "case_report_uninformative"}
# IT6 P2: how well the source was read is kept apart from how sound the experiment was; both weaken F1, only the page says which
READING_FLAGS = ("reading_depth", "graphical", "micrographs", "partial_read", "abstract_only")
DESIGN_FLAGS = ("tool_compound", "nonspecific", "one_experiment", "case_level", "no_instrument", "no_knockout_arm")
WEAK_FLAGS = READING_FLAGS + DESIGN_FLAGS
NOT_RECOVERY = "not_a_recovery_comparison"
FIRM_DEPTHS = {"complete_fulltext_read", "partial_fulltext_read"}


def classify_rows(rows: list[dict], depth_of: dict | None = None) -> dict:
    """Facts for one card x one need from pertinence rows (keys: assertion_id, evidence_kind, sign, flags, comparator). Pure."""
    depth_of = depth_of or {}
    w_all = [r for r in rows if r.get("evidence_kind") in WWOX_KINDS]
    # a wild-type-only comparison flagged not_a_recovery_comparison is listed but counts neither way
    w = [r for r in w_all if NOT_RECOVERY not in str(r.get("flags") or "")]
    o = [r for r in rows if r.get("evidence_kind") in OUT_KINDS]
    cnt = Counter(r.get("sign") for r in w)
    n_fav = sum(cnt[s] for s in FAV_SIGNS)
    n_null, n_unf, n_mix = cnt["null"], cnt["harm"], cnt["mixed"]
    if n_fav and not (n_null or n_unf or n_mix):
        result = "favourable"
    elif n_fav or n_mix:
        result = "mixed" if (n_null or n_unf or n_mix) else "favourable"
    elif n_unf:
        result = "unfavourable"
    elif n_null:
        result = "null"
    elif w_all:
        result = "unresolved"
    else:
        result = "none"
    firm, ctrl_any, deep_any, clean_r_any, clean_d_any, weak_r, weak_d, tool = [], False, False, False, False, set(), set(), False
    for r in w:
        fl = str(r.get("flags") or "")
        tool = tool or "tool_compound" in fl
        if r.get("sign") in CARRIER_SIGNS and r.get("evidence_kind") == "readout_in_wwox_system":
            controlled = str(r.get("comparator") or "").startswith(("untreated_same_genotype", "before_and_after"))
            deep = depth_of.get(r.get("assertion_id")) in FIRM_DEPTHS
            bad = [f for f in fl.split(";") if f and any(k in f for k in WEAK_FLAGS)]
            bad_r = [f for f in bad if any(k in f for k in READING_FLAGS)]
            bad_d = [f for f in bad if f not in bad_r]
            ctrl_any, deep_any, clean_r_any, clean_d_any = ctrl_any or controlled, deep_any or deep, clean_r_any or not bad_r, clean_d_any or not bad_d
            weak_r.update(bad_r)
            weak_d.update(bad_d)
            if controlled and deep and not bad:
                firm.append(r.get("assertion_id"))
    qualifiers = [r.get("assertion_id") for r in w_all if r.get("sign") == "not_normalised_vs_wild_type"]
    te = [r for r in rows if r.get("evidence_kind") == "target_engagement_assay"]
    o_fav = sum(1 for r in o if r.get("evidence_kind") == "readout_other_disease" and r.get("sign") in FAV_SIGNS)
    # IT6 P2: a target-engagement assay that shows no or poor engagement is counter-evidence like any other null (it was invisible: DR-E02-001/004)
    o_counter = sum(1 for r in o if r.get("sign") in ("harm", "null")) + sum(1 for r in te if r.get("sign") in ("harm", "null"))
    return {"result": result, "n_fav": n_fav, "n_null": n_null, "n_unf": n_unf, "n_mix": n_mix, "n_incomplete": sum(1 for r in w_all if r.get("sign") == "not_normalised_vs_wild_type"), "n_unresolved": cnt["unresolved"] + cnt["unquantified"],
            "n_wwox_rows": len(w_all), "n_counted_rows": len(w), "n_not_recovery": len(w_all) - len(w), "firm": firm, "ctrl_any": ctrl_any, "deep_any": deep_any, "clean_read_any": clean_r_any, "clean_design_any": clean_d_any, "weak_reading": sorted(weak_r), "weak_design": sorted(weak_d), "tool": tool, "qualifiers": qualifiers, "o_fav": o_fav, "o_counter": o_counter, "n_other_rows": len(o), "n_target_engagement": sum(1 for r in rows if r.get("evidence_kind") == "target_engagement_assay"),
            "n_engagement_fav": sum(1 for r in te if r.get("sign") in FAV_SIGNS)}


def display_facts(rows: list[dict], depth_of: dict | None = None) -> dict:
    """IT6 P2: facts that are SHOWN and never decide a position (kept out of classify_rows so that the guard hash covers decisions only).
    shallow_* = no signed row of that sign set was read beyond abstract, query or unknown depth; the sign set is the one that gives the position its family
    (F1/F2: favourable WWOX rows; C1/C2: null, harm or mixed WWOX rows; F3: favourable outside rows; C3: harm or null outside rows)."""
    depth_of = depth_of or {}
    w = [r for r in rows if r.get("evidence_kind") in WWOX_KINDS and NOT_RECOVERY not in str(r.get("flags") or "")]
    te = [r for r in rows if r.get("evidence_kind") == "target_engagement_assay"]
    o = [r for r in rows if r.get("evidence_kind") in OUT_KINDS] + te
    sets = {"F_w": [r for r in w if r.get("sign") in FAV_SIGNS], "C_w": [r for r in w if r.get("sign") in ("null", "harm", "mixed")],
            "F_o": [r for r in o if r.get("sign") in FAV_SIGNS and r.get("evidence_kind") in ("readout_other_disease", "target_engagement_assay")], "C_o": [r for r in o if r.get("sign") in ("harm", "null")]}
    shallow = {k: bool(v) and not any(depth_of.get(r.get("assertion_id")) in FIRM_DEPTHS for r in v) for k, v in sets.items()}
    n = {k: len(v) for k, v in sets.items()}
    downstream = sorted({r.get("assertion_id") for r in w if "endpoint_downstream_of_need" in str(r.get("flags") or "")})
    return {"shallow": shallow, "n_set": n, "downstream": downstream}


def card_compounds(cid: str, pert: list[dict], links: dict) -> set:
    """ChEMBL ids a card is about: those linked in catalog/card_links.json plus those named as the subject of its pertinence rows. Pure."""
    ids = {x["chembl_id"] for x in (links.get(cid) or {}).get("links", []) if x.get("chembl_id")}
    ids |= {r["subject"] for r in pert if r["card_id"] == cid and str(r.get("subject") or "").startswith("CHEMBL")}
    return ids


def sibling_counters(cid: str, nid: str, pert: list[dict], links: dict) -> dict:
    """IT6 P2: harm or null rows on the SAME need that other cards hold for a compound this card is also about. {other card: n rows}.
    A position is computed from the card's own rows; this makes visible what a sibling card of the same compound found on the need. Pure."""
    mine = card_compounds(cid, pert, links)
    out: dict = {}
    if not mine:
        return out
    for r in pert:
        if r["card_id"] == cid or r["need_id"] != nid or r.get("sign") not in ("harm", "null"):
            continue
        subj = str(r.get("subject") or "")
        theirs = {subj} if subj.startswith("CHEMBL") else card_compounds(r["card_id"], pert, links)
        if theirs & mine:
            out[r["card_id"]] = out.get(r["card_id"], 0) + 1
    return out


def assign_need_position(facts: dict, abstention: bool, has_next_step: bool, need_has_wwox_obs: bool) -> tuple[str, list[tuple[str, bool]]]:
    """THE rule: (position id, criteria as (plain-words statement, met)) for one card x one need. No score, no best-of-needs.
    facts is the output of classify_rows. Order of tests: abstention; no next step; the WWOX-system result; what exists outside WWOX; the need's own observations."""
    res = facts["result"]
    crit = [("the card is not an abstention", not abstention), ("a next step is named", has_next_step)]
    if abstention:
        return "P1", crit
    if not has_next_step:
        return "P2", crit
    crit += [("a signed result of the intervention in a WWOX system exists", res in ("favourable", "mixed", "null", "unfavourable"))]
    if res in ("favourable", "mixed", "null", "unfavourable"):
        crit += [("no null, unfavourable or mixed result in a WWOX system", res == "favourable")]
        if res == "favourable":
            firm = bool(facts["firm"])
            crit += [("a favourable WWOX readout has an untreated same-genotype comparator", facts["ctrl_any"]),
                     ("a favourable WWOX readout is from a full or partial text reading", facts["deep_any"]),
                     ("a favourable WWOX readout carries no reading-limit flag" + (" (found: " + ", ".join(facts["weak_reading"]) + ")" if facts["weak_reading"] else ""), facts["clean_read_any"]),
                     ("a favourable WWOX readout carries no design-limit flag" + (" (found: " + ", ".join(facts["weak_design"]) + ")" if facts["weak_design"] else ""), facts["clean_design_any"]),
                     ("one and the same readout meets all four", firm)]
            return ("F1" if firm else "F2"), crit
        return {"mixed": "C2", "null": "C1", "unfavourable": "C1"}[res], crit
    support = facts["o_fav"] + facts["n_engagement_fav"]   # IT6 P2: C3 and F3 now read the same support (a favourable engagement assay is a favourable outside signal)
    crit += [("an outside-WWOX harm or null signal stands without a favourable outside signal", facts["o_counter"] > 0 and support == 0)]
    if facts["o_counter"] > 0 and support == 0:
        return "C3", crit
    crit += [("some favourable support for the intervention is recorded on this need (other-disease readout or target-engagement assay)", support > 0), ("the need has a WWOX-system observation", need_has_wwox_obs)]
    return ("F3" if (need_has_wwox_obs and support > 0) else "P3"), crit


def overview_positions(links: dict) -> list[str]:
    """The overview of a card: the SET of its need-level positions, in the fixed display order of GROUPS. Never a single winner."""
    have = {l["group"] for l in links.values()}
    return [g["id"] for g in GROUPS if g["id"] in have]


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


# ------------------------------------------------------------------ IT6 P13: one-page brief, small evidence graph, work order
GRAPH_NAME = "view/evidence_graph.json"
WORK_ORDER_NAME = "view/work_order.json"
GRAPH_SCHEMA = "legend.wwox.evidence_graph/1"
WORK_ORDER_SCHEMA = "legend.wwox.work_order/1"
GRAPH_COLUMNS = ["osservazione WWOX", "bisogno", "meccanismo", "intervento", "evidenza", "esperimento"]
EDGE_TYPES = ["risultato sperimentale", "inferenza", "associazione"]
EDGE_CODE = {"risultato sperimentale": "R", "inferenza": "I", "associazione": "A"}
NODE_SCOPES = ("wwox", "wwox_other", "non_wwox", "computational", "proposed", "none")
CHAIN_STATES = ("astensione", "ipotesi", "non risolto")
WO_KINDS = ["verificare un'ipotesi", "chiarire una controevidenza", "risolvere una premessa"]
KIND_OF_FAMILY = {"F": WO_KINDS[0], "C": WO_KINDS[1], "P": WO_KINDS[2]}
WO_KEYS = {"need", "kind", "question", "data", "would_change", "feasibility", "date", "updated_by", "cards", "docs", "window_state", "summary_it", "feasibility_it"}
WINDOW_STATES = ("prevented_early_window", "recovered_post_onset_model", "symptom_suppression_reversible", "unmeasured")   # P7, rescue_window_it6 section 5: the 'window state' column
WINDOW_WORDING_RE = re.compile(r"early-window", re.I)   # a prevented/early-window state must be stated in the card or need wording itself
ISO_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
INTERACTOME_RE = re.compile(r"interactom|interactor|pull-?down|co-?ip\b", re.I)
NODE_LABEL_MAX = 150
BRIEF_SOURCES_MAX = 5


def allowed_kinds(groups) -> set:
    """Kinds of next study a need may carry, from the F/C/P positions the view assigns to it: a favourable hypothesis allows verifying it, counter-evidence allows clarifying it, a missing premise allows resolving it.
    A need with no card position has no hypothesis and no counter-evidence on record, so only its premise can be addressed."""
    kinds = {KIND_OF_FAMILY[g[0]] for g in groups if g and g[0] in KIND_OF_FAMILY}
    return kinds or {WO_KINDS[2]}


def _doc_problems(docs, dr, where) -> list[str]:
    errs = []
    if not isinstance(docs, dict) or not docs:
        return [f"{where}: docs must be a non-empty map id -> {{path, label}}"]
    for k, v in docs.items():
        if not isinstance(v, dict) or not v.get("label") or not v.get("path"):
            errs.append(f"{where}: doc {k!r} needs a path and a label")
        elif dr is not None and not (dr / v["path"]).exists():
            errs.append(f"{where}: doc {k!r} points to a file that does not exist: {v['path']}")
    return errs


def validate_evidence_graph(doc: dict, card_ids, need_ids, titles: dict, dr: Path | None = None) -> list[str]:
    """Problems of the hand-authored graph (empty list = valid). Every card id, need id and PMID must exist; every edge has a type from the closed list, a source id that exists, and goes forward through the
    columns; every chain has the six columns and is connected from an observation to an experiment; an interactome or list of interactors is never an endpoint of a causal edge."""
    errs: list[str] = []
    if doc.get("schema") != GRAPH_SCHEMA:
        errs.append(f"schema must be {GRAPH_SCHEMA}")
    if doc.get("columns") != GRAPH_COLUMNS:
        errs.append(f"columns must be exactly {GRAPH_COLUMNS}")
    if doc.get("edge_types") != EDGE_TYPES:
        errs.append(f"edge_types must be exactly {EDGE_TYPES}")
    docs = doc.get("docs")
    errs += _doc_problems(docs, dr, "graph")
    docs = docs if isinstance(docs, dict) else {}
    chains = doc.get("chains")
    if not isinstance(chains, list) or not chains:
        return errs + ["no chains"]
    seen_chain = set()
    card_ids, need_ids = set(card_ids), set(need_ids)
    for ch in chains:
        cid = ch.get("id")
        w = f"chain {cid!r}"
        if not cid or cid in seen_chain:
            errs.append(f"{w}: missing or duplicate chain id")
        seen_chain.add(cid)
        for k in ("title", "question"):
            if not ch.get(k):
                errs.append(f"{w}: {k} is empty")
        if ch.get("state") not in CHAIN_STATES:
            errs.append(f"{w}: state must be one of {CHAIN_STATES}")
        nodes: dict = {}
        for n in ch.get("nodes") or []:
            nid = n.get("id")
            if not nid or nid in nodes:
                errs.append(f"{w}: missing or duplicate node id {nid!r}")
                continue
            nodes[nid] = n
            if n.get("col") not in GRAPH_COLUMNS:
                errs.append(f"{w}/{nid}: column {n.get('col')!r} is not one of the six")
            lab = n.get("label")
            if not lab or len(lab) > NODE_LABEL_MAX:
                errs.append(f"{w}/{nid}: label empty or longer than {NODE_LABEL_MAX} characters")
            if n.get("scope") not in NODE_SCOPES:
                errs.append(f"{w}/{nid}: scope must be one of {NODE_SCOPES}")
            for c in n.get("cards") or []:
                if c not in card_ids:
                    errs.append(f"{w}/{nid}: dangling card id {c!r}")
            for x in n.get("needs") or []:
                if x not in need_ids:
                    errs.append(f"{w}/{nid}: dangling need id {x!r}")
            for p in n.get("pmids") or []:
                if str(p) not in titles:
                    errs.append(f"{w}/{nid}: PMID {p!r} is not in the source-title cache (unknown PMID)")
            if n.get("col") == "bisogno" and not n.get("needs"):
                errs.append(f"{w}/{nid}: a need node must reference a need id")
            if n.get("col") == "intervento" and not n.get("cards"):
                errs.append(f"{w}/{nid}: an intervention node must reference a card id")
        for col in GRAPH_COLUMNS:
            if not any(n.get("col") == col for n in nodes.values()):
                errs.append(f"{w}: no node in column {col!r}")
        idx = {c: i for i, c in enumerate(GRAPH_COLUMNS)}
        out_e: dict = {k: [] for k in nodes}
        in_e: dict = {k: [] for k in nodes}
        for e in ch.get("edges") or []:
            a, b = e.get("from"), e.get("to")
            we = f"{w} edge {a!r}->{b!r}"
            if a not in nodes or b not in nodes:
                errs.append(f"{we}: dangling node id")
                continue
            if e.get("type") not in EDGE_TYPES:
                errs.append(f"{we}: edge type {e.get('type')!r} is not one of {EDGE_TYPES}")
            src = str(e.get("source") or "")
            kind, _, sid = src.partition(":")
            if kind == "PMID":
                if sid not in titles:
                    errs.append(f"{we}: source PMID {sid!r} is not in the source-title cache (unknown PMID)")
            elif kind == "DOC":
                if sid not in docs:
                    errs.append(f"{we}: source document {sid!r} is not declared in docs")
            else:
                errs.append(f"{we}: an edge needs a source id, 'PMID:<id>' or 'DOC:<id>'")
            if idx.get(nodes[a].get("col"), 0) >= idx.get(nodes[b].get("col"), 0):
                errs.append(f"{we}: an edge must go forward through the columns")
            for nid in (a, b):
                nd = nodes[nid]
                if (nd.get("interactome") or INTERACTOME_RE.search(nd.get("label") or "")) and e.get("type") != "associazione":
                    errs.append(f"{we}: an interactome or a list of interactors is an association, never a causal edge ({nid})")
            out_e[a].append(b)
            in_e[b].append(a)
        for nid, nd in nodes.items():
            if not out_e[nid] and not in_e[nid]:
                errs.append(f"{w}/{nid}: node is on no edge")

        def reach(start, nxt):
            seen, stack = set(start), list(start)
            while stack:
                for m in nxt[stack.pop()]:
                    if m not in seen:
                        seen.add(m)
                        stack.append(m)
            return seen
        firsts = [k for k, n in nodes.items() if n.get("col") == GRAPH_COLUMNS[0]]
        lasts = [k for k, n in nodes.items() if n.get("col") == GRAPH_COLUMNS[-1]]
        fw, bw = reach(firsts, out_e), reach(lasts, in_e)
        for nid in nodes:
            if nid not in fw:
                errs.append(f"{w}/{nid}: not reachable from an observation")
            if nid not in bw:
                errs.append(f"{w}/{nid}: does not lead to an experiment")
    return errs


def validate_work_order(doc: dict, need_ids: list, groups_by_need: dict, card_ids, dr: Path | None = None, texts: dict | None = None) -> list[str]:
    """Problems of the hand-authored work order. Entries follow the order of the needs register (no ranking), the kind agrees with the F/C/P positions of that need, no score or rank field exists."""
    errs: list[str] = []
    if doc.get("schema") != WORK_ORDER_SCHEMA:
        errs.append(f"schema must be {WORK_ORDER_SCHEMA}")
    if doc.get("kinds") != WO_KINDS:
        errs.append(f"kinds must be exactly {WO_KINDS}")
    if not ISO_DATE_RE.match(str(doc.get("research_update") or "")):
        errs.append("research_update must be an ISO date")
    docs = doc.get("docs")
    errs += _doc_problems(docs, dr, "work order")
    docs = docs if isinstance(docs, dict) else {}
    texts = texts or {}
    if set(doc.get("window_states") or {}) != set(WINDOW_STATES):
        errs.append(f"window_states must be exactly {WINDOW_STATES}")

    def win_problems(items, key, w):
        out = []
        for it in items or []:
            st = it.get("state") if isinstance(it, dict) else None
            if st not in WINDOW_STATES:
                out.append(f"{w}: window state {st!r} is not one of {WINDOW_STATES}")
            elif st == "prevented_early_window" and key in texts and not WINDOW_WORDING_RE.search(texts[key]):
                out.append(f"{w}: state {st!r} is not backed by the wording of {key} (no 'early-window' statement)")
        return out
    for cid, cw in (doc.get("card_windows") or {}).items():
        if cid not in set(card_ids):
            errs.append(f"card_windows: dangling card id {cid!r}")
        errs += win_problems([{"state": x} for x in cw.get("states") or []], cid, f"card_windows {cid!r}")
        if not cw.get("states") or not str(cw.get("note") or "").strip():
            errs.append(f"card_windows {cid!r}: states and note are required")
    entries = doc.get("entries")
    if not isinstance(entries, list) or not entries:
        return errs + ["no entries"]
    pos = {n: i for i, n in enumerate(need_ids)}
    last, seen = -1, set()
    card_ids = set(card_ids)
    for e in entries:
        nid = e.get("need")
        w = f"work order {nid!r}"
        if nid not in pos:
            errs.append(f"{w}: dangling need id")
            continue
        if nid in seen:
            errs.append(f"{w}: duplicate entry")
        seen.add(nid)
        if pos[nid] <= last:
            errs.append(f"{w}: entries must follow the order of the needs register (no ranking)")
        last = max(last, pos[nid])
        for k in sorted(set(e) - WO_KEYS):
            errs.append(f"{w}: unknown field {k!r} (no score, rank or probability field exists)")
        for k in ("question", "data", "would_change", "feasibility", "summary_it", "feasibility_it"):
            if not str(e.get(k) or "").strip():
                errs.append(f"{w}: {k} is empty (write 'non nota' in feasibility_it when feasibility is not known)")
        if "not known" in str(e.get("feasibility")) and "non nota" not in str(e.get("feasibility_it")):
            errs.append(f"{w}: the English feasibility says 'not known' but feasibility_it does not say 'non nota'")
        if re.search(r"\bnon nota\b", str(e.get("feasibility"))):
            errs.append(f"{w}: Italian words inside the English feasibility text; put them in feasibility_it")
        if not ISO_DATE_RE.match(str(e.get("date") or "")):
            errs.append(f"{w}: date must be an ISO date")
        if e.get("kind") not in WO_KINDS:
            errs.append(f"{w}: kind {e.get('kind')!r} is not one of {WO_KINDS}")
        elif e["kind"] not in allowed_kinds(groups_by_need.get(nid) or ()):
            errs.append(f"{w}: kind {e['kind']!r} does not agree with the positions of the need {sorted(groups_by_need.get(nid) or [])}")
        errs += win_problems(e.get("window_state"), nid, w)
        for it in e.get("window_state") or []:
            if not str(it.get("note") or "").strip():
                errs.append(f"{w}: every window state needs a note")
        for c in e.get("cards") or []:
            if c not in card_ids:
                errs.append(f"{w}: dangling card id {c!r}")
        for d in e.get("docs") or []:
            if d not in docs:
                errs.append(f"{w}: document {d!r} is not declared in docs")
    return errs


def resolve_graph(doc: dict, titles: dict) -> dict:
    """The graph as embedded in the page: document paths stay out (only labels), every edge source is resolved to a printable id and title."""
    docs = {k: v["label"] for k, v in doc["docs"].items()}
    chains = []
    for ch in doc["chains"]:
        edges = []
        for e in ch["edges"]:
            kind, _, sid = e["source"].partition(":")
            src = {"kind": kind, "id": sid, "label": f"PMID {sid}" if kind == "PMID" else docs[sid], "title": titles[sid]["title"] if kind == "PMID" else None}
            edges.append({"from": e["from"], "to": e["to"], "type": e["type"], "source": e["source"], "src": src, "note": e.get("note") or ""})
        nodes = [{"id": n["id"], "col": n["col"], "scope": n["scope"], "label": n["label"], "pmids": [str(p) for p in n.get("pmids") or []], "cards": list(n.get("cards") or []),
                  "needs": list(n.get("needs") or []), "unresolved": bool(n.get("unresolved"))} for n in ch["nodes"]]
        chains.append({"id": ch["id"], "title": ch["title"], "state": ch["state"], "question": ch["question"], "nodes": nodes, "edges": edges})
    return {"date": doc.get("date"), "columns": list(GRAPH_COLUMNS), "edge_types": list(EDGE_TYPES), "docs": [{"id": k, "label": v} for k, v in docs.items()], "chains": chains}


def resolve_work_order(doc: dict, groups_by_need: dict) -> dict:
    docs = {k: v["label"] for k, v in doc["docs"].items()}
    entries = [{"need": e["need"], "kind": e["kind"], "question": e["question"], "data": e["data"], "would_change": e["would_change"], "feasibility": e["feasibility"], "date": e["date"],
                "updated_by": list(e.get("updated_by") or []), "cards": list(e.get("cards") or []), "docs": [{"id": d, "label": docs[d]} for d in e.get("docs") or []],
                "window_state": [dict(x) for x in e.get("window_state") or []], "summary_it": e["summary_it"], "feasibility_it": e["feasibility_it"],
                "positions": sorted(groups_by_need.get(e["need"]) or [])} for e in doc["entries"]]
    return {"research_update": doc["research_update"], "kinds": list(WO_KINDS), "entries": entries, "window_states": list(WINDOW_STATES),
            "card_windows": {k: {"states": list(v["states"]), "note": v["note"]} for k, v in sorted((doc.get("card_windows") or {}).items())}}


def load_curated_docs(dr: Path, cands: list, cneeds: list, titles: dict, texts: dict | None = None) -> tuple[dict, dict]:
    """Reads and validates view/evidence_graph.json and view/work_order.json against the cards, the needs and the title cache. An invalid file is a build error, never a silent omission."""
    card_ids = [c["id"] for c in cands]
    need_ids = [n["id"] for n in cneeds]
    groups: dict = {n: set() for n in need_ids}
    for c in cands:
        for nid, l in c["links"].items():
            groups[nid].add(l["group"])
    out = []
    for name, fn, args in ((GRAPH_NAME, validate_evidence_graph, (card_ids, need_ids, titles, dr)), (WORK_ORDER_NAME, validate_work_order, (need_ids, groups, card_ids, dr, texts))):
        p = dr / name
        if not p.exists():
            raise SystemExit(f"{name} is missing: the evidence graph and the work order are part of the view")
        doc = jload(p)
        errs = fn(doc, *args)
        if errs:
            raise SystemExit(f"{name} is invalid:\n  " + "\n  ".join(errs))
        out.append(doc)
    return resolve_graph(out[0], titles), resolve_work_order(out[1], groups)


SAFETY_RE = re.compile(r"\b(safety|adverse|toxic\w*|harm\w*|MRI|neuropath\w*|pro-?convuls\w*|hepat\w*|serious|withdrawn|contraindicat\w*|tumou?r\w*)\b", re.I)
WWOX_NULL_RE = re.compile(r"(?=.*\b(?:Wwox|WWOX|knockout|organoid|null mouse)\b)(?=.*\b(?:null|no (?:effect|benefit|difference|change)|did not|not (?:recovered|reproduc\w+)|unfavourable|worse|failed|negative|ineffective)\b)", re.I | re.S)
PLACEHOLDER_RE = re.compile(r"^\s*see\b[^.]*\babove\.?\s*$", re.I)
ID_PAREN_RE = re.compile(r"\s*\([^()]*(?:CLAIM \d+|DL-[A-Z]+-\d+|HYP-\d{8}-\d+|MECHANISM_TRANSFER_FIREWALL|\bN-\d+\b|needs audit|\bmanifest\b)[^()]*\)")
ID_BARE_RE = re.compile(r"\b(?:(?:[Mm]ap )?N-\d+\b:?\s*|CLAIM \d+|DL-[A-Z]+-\d+|HYP-\d{8}-\d+|MECHANISM_TRANSFER_FIREWALL|DR-[A-Z0-9]+-\d+|[A-Z]-[A-Z]{2,4}-\d+)\b")
COUNTER_CATEGORIES = ("sicurezza e danno", "risultati nulli o sfavorevoli in sistemi WWOX", "controprove fuori da WWOX e limiti")


def scrub_ids(t: str) -> str:
    """Repository identifiers (CLAIM 031, DL-..., HYP-..., assertion ids) mean nothing outside the repository: they are dropped from the one-page text (the dossier keeps the card text whole)."""
    t = ID_PAREN_RE.sub("", str(t or ""))
    t = ID_BARE_RE.sub("", t)
    return re.sub(r"\s+([,.;:])", r"\1", re.sub(r"\s{2,}", " ", t)).strip()


def clip_sentence(t, n: int, hard: float = 3.0) -> str:
    """Shorten at a sentence boundary, never inside a sentence: the last boundary within n; else the end of the first sentence if it is within hard*n; only a single sentence longer than that is cut, at a clause."""
    t = " ".join(str(t or "").split())
    if len(t) <= n * 1.2:
        return t
    ends = [m.start() for m in re.finditer(r"(?<=[.;])\s+(?=[A-Z(\[0-9])", t)]
    within = [e for e in ends if e <= n]
    if within:
        return t[:within[-1]].rstrip()
    first = [e for e in ends if e <= n * hard]
    if first:
        return t[:first[0]].rstrip()
    if len(t) <= n * hard:
        return t
    cut = t[:int(n * hard)]
    i = max(cut.rfind("; "), cut.rfind(", "))
    return (cut[:i] if i > n * 0.5 else cut[:cut.rfind(" ")]).rstrip(",;") + " …"


def counter_category(text: str) -> int:
    """Deterministic category of a counter-evidence statement: 0 safety or harm signal, 1 null or unfavourable result in a WWOX system, 2 counter-evidence from outside WWOX and design limits."""
    if SAFETY_RE.search(text):
        return 0
    return 1 if WWOX_NULL_RE.search(text) else 2


def order_counter(items: list, flip: bool = False) -> list:
    """(category, text) items in category order; inside a category the stored order of the card, then of the need, is kept (stable sort). `flip` exists for the regression test only."""
    return sorted(items, key=lambda it: -it[0] if flip else it[0])


def make_brief(c: dict, nmap: dict) -> dict:
    """The one-page synthesis of a card: fields assembled from the card and its needs only (no new claim). Fallback sentences are Italian orientation text; everything else is the stored scientific text, shortened only at sentence boundaries."""
    U = UI_IT
    wsc = ("WWOX_EXPERIMENT_IN_DEE_SYSTEM", "WWOX_CLINICAL_CASE")
    order = sorted(c["needs"], key=lambda n: (len(nmap[n]["cards"]), n))
    obs = [o for n in order for o in nmap[n]["obs"]]
    w_obs = [o for o in obs if o["scope"] in wsc]

    def is_wwox_obs(o):
        return o["scope"] == "WWOX_BIOLOGY_OTHER_CONTEXT" or (o["scope"] == "COMPUTATIONAL_RESULT" and re.search(r"knock|wwox", str(o.get("model") or ""), re.I))

    def is_wwox_assert(a):
        return a["scope"] == "UNCLASSIFIED" and re.search(r"WWOX|WOREE", a.get("system") or "", re.I) and not re.search(r"NOT WWOX", (a.get("system") or "") + " " + (a.get("genotype") or ""), re.I)
    o_obs = [o for o in obs if o["scope"] not in wsc and not is_wwox_obs(o)]
    own = [a for a in c["asserts"] if a["scope"] in wsc]
    other = [a for a in c["asserts"] if a["scope"] not in wsc and a["scope"] != "SAFETY_SIGNAL" and not is_wwox_assert(a)]
    safety = [a for a in c["asserts"] if a["scope"] == "SAFETY_SIGNAL"]

    def fa(a, tgt=True):
        # the tested target or tool compound is named first: a result of d-APV on the NMDAR must not read as a result of the card's own intervention
        head = (clip(a["target"], 110) + ": ") if (tgt and a.get("target") and a["target"] not in a["text"]) else ""
        return head + a["text"] + (" – " + clip_sentence(a.get("note_full") or a["note"], 220) if a.get("note") else "") + (f" [{a['species']}]" if a.get("species") else "")
    if own:
        wwox = " | ".join(fa(a) for a in own[:2])
    elif w_obs:
        wwox = U["bf_wwox_ctx"] + ": " + clip_sentence(w_obs[0]["full"] or w_obs[0]["short"], 300)
    else:
        wwox = U["bf_wwox_none"]
    ext_items = [fa(a, False) for a in other[:2]] + [clip_sentence(o["full"] or o["short"], 260) for o in o_obs[:1]]
    external = " | ".join(ext_items[:2]) if ext_items else U["bf_ext_none"]
    items = []
    for a in c["asserts"]:
        if a["scope"] == "SAFETY_SIGNAL" or a.get("sign") == "harm":
            items.append((0, fa(a)))
        elif a.get("sign") == "null":
            items.append((1 if a["scope"] in wsc else 2, fa(a)))
    for t in list(c["against"]) + [t for n in order for t in nmap[n]["counter"]]:
        if not PLACEHOLDER_RE.match(str(t)):
            items.append((counter_category(str(t)), str(t)))
    seen, uniq_items = set(), []
    for cat, t in order_counter(items):
        k = re.sub(r"\W+", " ", t.lower())[:80]
        if k not in seen:
            seen.add(k)
            uniq_items.append((cat, t))
    if not uniq_items and c.get("against_note") and not PLACEHOLDER_RE.match(str(c["against_note"])):
        uniq_items = [(counter_category(str(c["against_note"])), str(c["against_note"]))]
    counter = [{"cat": cat, "category": COUNTER_CATEGORIES[cat], "text": scrub_ids(clip_sentence(t, 240, 1.5))} for cat, t in uniq_items[:3]]
    if not counter:
        counter = [{"cat": None, "category": None, "text": U["bf_counter_none"]}]
    more = max(0, len(uniq_items) - 3)
    pm: list[str] = []

    def add(p):
        if p and str(p) not in pm:
            pm.append(str(p))
    for a in own:
        [add(p) for p in a["pmids"]]
    for o in w_obs:
        add(o.get("pmid"))
    for a in other:
        [add(p) for p in a["pmids"]]
    for o in o_obs:
        add(o.get("pmid"))
    for a in safety:
        [add(p) for p in a["pmids"]]
    titled = {p["id"]: p for p in c["pmids"]}
    pm = [p for p in pm if p in titled and titled[p].get("title")] + [p for p in pm if p not in titled or not titled[p].get("title")]
    sources = [{"kind": "PMID", "id": p, "title": (titled.get(p) or {}).get("title"), "journal": (titled.get(p) or {}).get("journal"), "year": (titled.get(p) or {}).get("year")} for p in pm[:BRIEF_SOURCES_MAX]]
    if not sources:
        sources = [{"kind": "ChEMBL", "id": x, "title": None, "journal": None, "year": None} for x in c["chembl"][:BRIEF_SOURCES_MAX]]
    return {"wwox": scrub_ids(clip_sentence(wwox, 520)), "external": scrub_ids(clip_sentence(external, 340)), "counter": counter, "counter_more": more,
            "missing": scrub_ids(clip_sentence(c["missing"], 280)) if c.get("missing") else U["bf_missing_none"],
            "next": scrub_ids(clip_sentence(c["next_full"], 600)) if c.get("next_full") else U["bf_next_none"], "sources": sources}


# ------------------------------------------------------------------ IT7 P7: selection funnel, hypothesis comparison, predictive test, context concordance
P2_DIR, P3_DIR, P4_DIR, P5_DIR = "usable_compounds_it7_p2_20261029", "network_comparison_it7_p3_20261029", "context_differences_it7_p4_20261029", "pharmacological_comparison_it7_p5_20261029"
PRED_NAME, CTX_NAME = "view/predictive_test.json", "view/context_verdicts.json"
PRED_SCHEMA, CTX_SCHEMA = "legend.wwox.predictive_test/1", "legend.wwox.context_verdicts/1"
VERDICT_CODES = ("no_added_value", "not_detected_not_excluded", "inconclusive")
CTX_VERDICT_CODES = ("concordant", "discordant", "single_system", "no_resolved_sign", "no_data")
RESOLVED = {"higher": 1, "lower": -1}                       # a direction distinguishable from noise by the source's own criterion
NO_SIGNAL = {"no_resolvable_sign", "lower_non_specific", "at_null_edge", "sparse"}
P5_COLUMNS = ("record_id", "hypothesis_cards", "intervention_and_type", "research_objective", "genotype_lesion_applicability_track", "depth_of_benefit_sought", "need_link", "PRIORITY_position_and_work_order_reason",
              "MODEL_position_P3_P2", "OBSERVED_wwox_specific_evidence", "premise_demonstrated", "premise_missing", "external_precedents_with_reading_depth", "potentially_opposed_effects",
              "next_decision_changing_experiment", "experiment_status")


def read_tsv(p: Path) -> list[dict]:
    with open(p, encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def recompute_p2(dr: Path) -> dict:
    """Every funnel count of the usable-compound census, recomputed from the per-record flags (record_usability.tsv.gz), so that a number printed by the page can be traced to rows."""
    with gzip.open(dr / P2_DIR / "record_usability.tsv.gz", "rt", encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    fam: dict[str, list[dict]] = {}
    for r in rows:
        fam.setdefault(r["family_id"], []).append(r)
    UNK = "UNKNOWN_NO_STRUCTURE_KEY"

    def rec(fn):
        return sum(1 for r in rows if fn(r))

    def fm(fn):
        return sum(1 for f in fam.values() if any(fn(r) for r in f))
    corr = lambda r: r["Mnet_usable"] == "1" and ("ChEMBL" in r["Mnet_source_groups"] or "GtoPdb" in r["Mnet_source_groups"])
    out = {"records": {}, "families": {}}
    for unit, n, f in (("records", len(rows), rec), ("families", len(fam), fm)):
        d = out[unit]
        d["L0_catalogued"] = n
        d["L1_with_any_target_row"] = f(lambda r: r["any_target_row"] == "1")
        d["L2_documented_action_row_passes_artefact_rules"] = f(lambda r: r["stated_action"] == "1")
        d["L3_Mnet_usable_signed_action_on_human_target_with_stable_id"] = f(lambda r: r["Mnet_usable"] == "1")
        d["L3b_Mnet_corroborated_by_ChEMBL_or_GtoPdb_support"] = f(corr)
        d["Msig_any_context_trt_cp_signature"] = f(lambda r: r["Msig_any_context"] == "1")
        d["Msig_neural_lineage_context_strict"] = f(lambda r: r["Msig_neural_strict"] == "1")
    out["records"]["Msig_UNKNOWN_NO_STRUCTURE_KEY"] = rec(lambda r: r["Msig_any_context"] == UNK)
    out["families"]["Msig_UNKNOWN_NO_STRUCTURE_KEY"] = sum(1 for f in fam.values() if all(r["Msig_any_context"] == UNK for r in f))
    for unit in ("records", "families"):
        out[unit]["Msig_testable_denominator_has_structure_key"] = out[unit]["L0_catalogued"] - out[unit]["Msig_UNKNOWN_NO_STRUCTURE_KEY"]
    # neural strict x M-net over the testable denominator
    r_both = rec(lambda r: r["Msig_any_context"] != UNK and r["Mnet_usable"] == "1" and r["Msig_neural_strict"] == "1")
    r_net = rec(lambda r: r["Msig_any_context"] != UNK and r["Mnet_usable"] == "1" and r["Msig_neural_strict"] != "1")
    r_sig = rec(lambda r: r["Msig_any_context"] != UNK and r["Mnet_usable"] != "1" and r["Msig_neural_strict"] == "1")
    out["records"]["overlap_neural_testable"] = {"both": r_both, "only_net_usable": r_net, "only_sig_neural": r_sig, "neither": out["records"]["Msig_testable_denominator_has_structure_key"] - r_both - r_net - r_sig}
    testable = [f for f in fam.values() if any(r["Msig_any_context"] != UNK for r in f)]
    f_net = lambda f: any(r["Mnet_usable"] == "1" for r in f)
    f_sig = lambda f: any(r["Msig_neural_strict"] == "1" for r in f)
    both = sum(1 for f in testable if f_net(f) and f_sig(f))
    only_net = sum(1 for f in testable if f_net(f) and not f_sig(f))
    only_sig = sum(1 for f in testable if not f_net(f) and f_sig(f))
    out["families"]["overlap_neural_testable"] = {"both": both, "only_net_usable": only_net, "only_sig_neural": only_sig, "neither": len(testable) - both - only_net - only_sig}
    return out


def validate_p2_counts(counts: dict, re_: dict, units: dict) -> list[str]:
    """Problems between counts.json, the recomputation from the per-record flags, and the catalogue's own units. Empty list = every printed count is traceable."""
    errs = []
    for unit in ("records", "families"):
        for k, v in re_[unit].items():
            if k == "overlap_neural_testable":
                ref = counts["funnel"][unit]["overlap_Mnet_vs_Msig_neural_strict_testable_only"]
                for kk, vv in v.items():
                    if ref.get(kk) != vv:
                        errs.append(f"{unit} overlap {kk}: counts.json {ref.get(kk)} but the rows give {vv}")
                if sum(ref[x] for x in ("both", "only_net_usable", "only_sig_neural", "neither")) != ref["denominator"]:
                    errs.append(f"{unit} overlap does not add up to its denominator")
            elif counts["funnel"][unit].get(k) != v:
                errs.append(f"{unit} {k}: counts.json {counts['funnel'][unit].get(k)} but the rows give {v}")
    if counts["catalogue"]["records"] != units["catalogue_records"] or counts["catalogue"]["families_all_record_definition"] != units["families"]:
        errs.append("catalogue size in counts.json differs from the coverage summary units")
    if counts["funnel"]["records"]["actually_evaluated"] != 0 or counts["funnel"]["families"]["actually_evaluated"] != 0:
        errs.append("the census must state actually_evaluated = 0")
    return errs


def dig(o, path: str):
    for part in path.split("."):
        o = o[int(part)] if isinstance(o, list) else o[part]
    return o


def validate_predictive(doc: dict, p3: dict, e1: dict, dr: Path | None = None) -> list[str]:
    errs = []
    if doc.get("schema") != PRED_SCHEMA:
        errs.append(f"schema must be {PRED_SCHEMA}")
    if doc.get("exploratory") is not True:
        errs.append("the predictive test must carry the exploratory label")
    for k in ("question", "question_it", "limits_it", "methods", "verdicts"):
        if not doc.get(k):
            errs.append(f"{k} is empty")
    srcs = {"p3": p3, "e1": e1}
    for v in doc.get("verdicts") or []:
        w = f"verdict {v.get('id')!r}"
        if v.get("verdict") not in VERDICT_CODES:
            errs.append(f"{w}: verdict must be one of {VERDICT_CODES}")
        if not v.get("reopen_it") or not v.get("comparison_it"):
            errs.append(f"{w}: comparison_it and reopen_it are required")
        for n in v.get("numbers") or []:
            try:
                val = dig(srcs[v.get("source", "p3")], n["path"])
                if n.get("minus"):
                    val = val - dig(srcs[v.get("source", "p3")], n["minus"])
            except (KeyError, IndexError, TypeError):
                errs.append(f"{w}: path {n.get('path')!r} is not in the data")
                continue
            if round(val, n["digits"]) != n["expect"]:
                errs.append(f"{w}: {n['id']} is {round(val, n['digits'])} in the data but the text expects {n['expect']}")
        for x in v.get("external_values") or []:   # a value that sits in a verifier's report and not in a data file: the report must still contain it
            if dr is not None and (dr.parent / x["check_file"]).exists() and x["check_text"] not in (dr.parent / x["check_file"]).read_text(encoding="utf-8"):   # a partial copy of the module (a test fixture) has no report to read
                errs.append(f"{w}: {x['id']}: {x['check_text']!r} is not in {x['check_file']}")
    if p3.get("nU") != 256 or doc.get("universe", {}).get("pilot_families") is None:
        errs.append("the evaluated universe must be the 256 families of the P3 comparison, stated as a pilot subset")
    return errs


def context_stats(rows: list[dict], cv: dict) -> dict:
    """Per quantity: counts of higher / lower / no resolvable sign / unknown cells, the models with a resolved sign, and the verdict check."""
    models = cv["models"]
    q_ids = list(dict.fromkeys(r["quantity_id"] for r in rows))
    out = {}
    for q in q_ids:
        cells = [r for r in rows if r["quantity_id"] == q]
        n = Counter()
        res: dict[str, set] = {}
        measured_models = set()
        for r in cells:
            d = r["direction"]
            if d == "UNKNOWN":
                n["unknown"] += 1
                continue
            measured_models.add(models[r["context_id"]])
            if d in RESOLVED:
                n["higher" if RESOLVED[d] > 0 else "lower"] += 1
                res.setdefault(models[r["context_id"]], set()).add(RESOLVED[d])
            else:
                n["other"] += 1
        signs = {s for v in res.values() for s in v}
        out[q] = {"quantity": cells[0]["quantity"], "cells": len(cells), "higher": n["higher"], "lower": n["lower"], "other": n["other"], "unknown": n["unknown"],
                  "models_measured": len(measured_models), "models_resolved": len(res), "signs": sorted(signs),
                  "models_same_sign": max((sum(1 for v in res.values() if s in v) for s in signs), default=0), "directions": {r["context_id"]: r["direction"] for r in cells}}
    return out


def derive_context_verdict(s: dict) -> str:
    """The reading of one quantity, by the rule printed on the page: discordant (resolved signs of both directions), concordant (one resolved sign in at least two models), single system (a resolved sign in one model only),
    no resolved sign (measured cells, all inside noise), no data (nothing measured). A sign is resolved only where the source's own criterion says so (higher or lower; a sign-only or non-specific direction is not)."""
    if s["models_measured"] == 0:
        return "no_data"
    if len(s["signs"]) >= 2:
        return "discordant"
    if len(s["signs"]) == 1:
        return "concordant" if s["models_same_sign"] >= 2 else "single_system"
    return "no_resolved_sign"


def validate_contexts(cv: dict, rows: list[dict], stats: dict) -> list[str]:
    errs = []
    if cv.get("schema") != CTX_SCHEMA:
        errs.append(f"schema must be {CTX_SCHEMA}")
    ctxs = list(dict.fromkeys(r["context_id"] for r in rows))
    qs = list(stats)
    pairs = Counter((r["quantity_id"], r["context_id"]) for r in rows)
    if any(v != 1 for v in pairs.values()) or len(pairs) != len(ctxs) * len(qs):
        errs.append("the matrix must hold every (quantity, context) pair exactly once")
    unk = sum(1 for r in rows if r["direction"] == "UNKNOWN")
    got = {"contexts": len(ctxs), "quantities": len(qs), "cells": len(rows), "unknown": unk, "measured": len(rows) - unk, "models": len(set(cv.get("models", {}).values()))}
    for k, v in (cv.get("expect") or {}).items():
        if got.get(k) != v:
            errs.append(f"{k}: the matrix gives {got.get(k)} but the text expects {v}")
    for c in ctxs:
        if c not in cv.get("models", {}):
            errs.append(f"context {c} has no model")
    for m in set(cv.get("models", {}).values()):
        if m not in cv.get("model_labels_it", {}):
            errs.append(f"model {m} has no Italian label")
    if set(cv.get("verdicts", {})) != set(qs):
        errs.append("a name and a note are required for every quantity and for no other")
    for q, v in (cv.get("verdicts") or {}).items():
        s = stats.get(q)
        if s is None:
            continue
        if v.get("expect") not in CTX_VERDICT_CODES:
            errs.append(f"{q}: expect must be one of {CTX_VERDICT_CODES}")
        elif derive_context_verdict(s) != v["expect"]:
            errs.append(f"{q}: the rule gives {derive_context_verdict(s)!r} but the note was written for {v['expect']!r}")
        if not v.get("quantity_it") or not v.get("note_it"):
            errs.append(f"{q}: quantity_it and note_it are required")
    return errs


def eng_clean(t: str) -> str:
    """English text printed on the Italian page carries no repository file name (the Italian placeholder the shareable policy would insert would sit inside an English sentence)."""
    return FILE_TOKEN_RE.sub("a repository record", str(t))


def classify_model(text: str) -> dict:
    """What the P5 model cell says, as codes: whether an axis result of the P3 comparison is quoted (it is about the methods on the pilot subset, never a position of the compound), why the compound has no model position,
    and whether the compound is in the usable census."""
    t = text.strip()
    reasons = []
    if "firewalled" in t:
        reasons.append("firewalled")
    if re.search(r"not a compound question|no compound target row|no signed target row", t):
        reasons.append("not_compound")
    if re.search(r"transcript module|receptor-physiology|not the glycolysis module|not a transcript question", t):
        reasons.append("outside_question")
    return {"axis": t.startswith("P3") and "NO ADDED VALUE" in t, "reasons": reasons, "usable": "usable by the network method" in t}


def validate_hypotheses(rows: list[dict], card_ids, need_ids, wo_needs) -> list[str]:
    errs = []
    if not rows or any(set(P5_COLUMNS) - set(r) for r in rows):
        return ["the pharmacological comparison lacks required columns"]
    for r in rows:
        w = r["record_id"]
        for c in [x.strip() for x in r["hypothesis_cards"].split(";") if x.strip()]:
            if c not in card_ids:
                errs.append(f"{w}: card {c!r} does not exist")
        for n in re.findall(r"NEED-[A-Z0-9][A-Z0-9-]*", r["need_link"]):
            if n not in need_ids:
                errs.append(f"{w}: need {n!r} does not exist")
        m = r["MODEL_position_P3_P2"].strip()
        if not (m.startswith("None") or (m.startswith("P3") and "NO ADDED VALUE" in m)):
            errs.append(f"{w}: the model position is neither 'None' nor a P3 'NO ADDED VALUE': the Italian label would be wrong")
        elif m.startswith("P3") and "No model position for this compound" not in m:
            errs.append(f"{w}: a P3 axis result without 'No model position for this compound' would read as a position of the compound")
        elif not classify_model(m)["reasons"]:
            errs.append(f"{w}: no reason (firewalled, not a compound question, outside the question) can be read from the model cell")
        for k in P5_COLUMNS:
            if not r[k].strip():
                errs.append(f"{w}: column {k} is empty (write UNKNOWN, never leave it blank)")
    return errs


def build_it7(dr: Path, funnel: dict, mx: dict, units: dict, cur: dict) -> dict:
    """The four IT7 sections, every number read from the measured sources and checked against them at build time. An inconsistency is a build error."""
    cands = {c["id"]: c for c in cur["cands"]}
    need_ids = [n["id"] for n in cur["needs"]]
    # ---- selection funnel (P2 census)
    counts = jload(dr / P2_DIR / "counts.json")
    errs = validate_p2_counts(counts, recompute_p2(dr), units)
    if errs:
        raise SystemExit("usable-compound census does not reproduce:\n  " + "\n  ".join(errs))
    f = counts["funnel"]
    R, F = f["records"], f["families"]
    p3 = jload(dr / P3_DIR / "results/results_summary.json")
    e1 = jload(dr / P3_DIR / "results/e1_p47t_summary.json")
    pilot = counts["pilot"]
    n_ready = sum(1 for c in cur["cands"] if c.get("next") and not c["abstention"])
    wo_entries = cur["work_order"]["entries"]

    def ind(i, rec=None, fam=None, den_rec=None, den_fam=None, unit="rf", **extra):
        d = {"id": i, "records": rec, "families": fam, "den_records": den_rec, "den_families": den_fam, "unit": unit}
        d.update(extra)
        return d
    n_rec, n_fam = R["L0_catalogued"], F["L0_catalogued"]
    t_rec, t_fam = R["Msig_testable_denominator_has_structure_key"], F["Msig_testable_denominator_has_structure_key"]
    unk_by_origin = counts["match_rule_sensitivity"]["records_without_structure_key_by_origin"]
    steps = [
        {"id": "catalogued", "indicators": [
            ind("catalogued", n_rec, n_fam),
            ind("source_only", None, units["source_only_families_unresolved_identity"], None, n_fam, unit="f")]},
        {"id": "usable", "indicators": [
            ind("l1", R["L1_with_any_target_row"], F["L1_with_any_target_row"], n_rec, n_fam),
            ind("l2", R["L2_documented_action_row_passes_artefact_rules"], F["L2_documented_action_row_passes_artefact_rules"], n_rec, n_fam),
            ind("mnet", R["L3_Mnet_usable_signed_action_on_human_target_with_stable_id"], F["L3_Mnet_usable_signed_action_on_human_target_with_stable_id"], n_rec, n_fam),
            ind("mnet_corr", R["L3b_Mnet_corroborated_by_ChEMBL_or_GtoPdb_support"], F["L3b_Mnet_corroborated_by_ChEMBL_or_GtoPdb_support"], R["L3_Mnet_usable_signed_action_on_human_target_with_stable_id"], F["L3_Mnet_usable_signed_action_on_human_target_with_stable_id"]),
            ind("mnet_dgidb_only", counts["Mnet_origin_records"]["dgidb_only"], None, R["L3_Mnet_usable_signed_action_on_human_target_with_stable_id"], None, unit="r"),
            ind("rows_excluded", counts["row_counts"]["rows_excluded_by_catalogue_artefact_rules"], None, counts["row_counts"]["rows_total"], None, unit="rows"),
            ind("msig_testable", t_rec, t_fam, n_rec, n_fam),
            ind("msig_unknown", R["Msig_UNKNOWN_NO_STRUCTURE_KEY"], F["Msig_UNKNOWN_NO_STRUCTURE_KEY"], n_rec, n_fam,
                breakdown=[{"id": k, "records": unk_by_origin[k]} for k in ("dgidb_only", "chembl_selected", "openfda_unii_only", "matrix_only")]),
            ind("msig_any", R["Msig_any_context_trt_cp_signature"], F["Msig_any_context_trt_cp_signature"], n_rec, n_fam, testable_rec=t_rec, testable_fam=t_fam),
            ind("msig_neural", R["Msig_neural_lineage_context_strict"], F["Msig_neural_lineage_context_strict"], n_rec, n_fam, testable_rec=t_rec, testable_fam=t_fam)]},
        {"id": "evaluated", "indicators": [
            ind("eval_methods", 0, 0, n_rec, n_fam),
            ind("eval_p3", None, p3["nU"], None, pilot["union_families"], unit="f", den2_fam=n_fam),
            ind("eval_wwox_readout", funnel["evaluated_records"], None, n_rec, None, unit="r")]},
        {"id": "pertinent", "indicators": [
            ind("need_link", funnel["records_with_link"], funnel["families_with_link"], n_rec, n_fam),
            ind("need_action", funnel["records_with_action"], funnel["families_with_action"], n_rec, n_fam),
            ind("card_linked", None, pilot["card_linked_families"], None, n_fam, unit="f"),
            ind("cards", len(cur["cands"]), None, None, None, unit="cards")]},
        {"id": "ready", "indicators": [
            ind("cards_next", n_ready, None, len(cur["cands"]), None, unit="cards"),
            ind("needs_plan", len(wo_entries), None, len(need_ids), None, unit="needs")]}]
    selection = {
        "census_generated": counts["catalogue"]["generated_utc"], "steps": steps,
        "overlap": {"records": {k: R["overlap_Mnet_vs_Msig_neural_strict_testable_only"][k] for k in ("both", "only_net_usable", "only_sig_neural", "neither", "denominator")},
                    "families": {k: F["overlap_Mnet_vs_Msig_neural_strict_testable_only"][k] for k in ("both", "only_net_usable", "only_sig_neural", "neither", "denominator")}},
        "kinds": {"L1_documented": mx["L1_documented"], "L2": {k: mx["L2_states"].get(k, 0) for k in ("coherent", "opposed", "direction_unresolved")}, "L3": mx["L3_observed"], "L3_wwox_system": mx["L3_states"].get("observed_wwox_system", 0),
                  "L4": mx["L4_observed"], "L4_experimental": mx["L4_states"].get("observed_experimental", 0), "cells": mx["cells_nonempty"]},
        "pilot": {"union_families": pilot["union_families"], "both_methods_families": pilot["both_methods_families"], "card_linked_families": pilot["card_linked_families"], "p3_universe": p3["nU"], "p3_signatures": p3["n_signatures"]},
    }
    # ---- hypotheses (P5 comparison)
    rows5 = read_tsv(dr / P5_DIR / "comparison.tsv")
    errs = validate_hypotheses(rows5, set(cands), set(need_ids), {e["need"] for e in wo_entries})
    if errs:
        raise SystemExit("pharmacological comparison is inconsistent with the cards and needs:\n  " + "\n  ".join(errs))
    wo_by = {e["need"]: e for e in wo_entries}
    hyp = []
    for r in rows5:
        cids = [x.strip() for x in r["hypothesis_cards"].split(";") if x.strip()]
        nids = list(dict.fromkeys(re.findall(r"NEED-[A-Z0-9][A-Z0-9-]*", r["need_link"])))
        m = r["MODEL_position_P3_P2"].strip()
        hyp.append({"id": r["record_id"], "cards": cids, "needs": nids, "title": " · ".join(cands[c]["short"] for c in cids),
                    "positions": {c: [{"need": n_, "group": cands[c]["links"][n_]["group"]} for n_ in nids if n_ in cands[c]["links"]] for c in cids},
                    "work_order": [{"need": n, "kind": wo_by[n]["kind"]} for n in nids if n in wo_by],
                    "model": "none", **{("model_" + k): v for k, v in classify_model(m).items()},
                    "objective": clip_sentence(r["research_objective"], 160), "track": clip_sentence(r["genotype_lesion_applicability_track"], 260), "depth": clip_sentence(r["depth_of_benefit_sought"], 260),
                    "observed": clip_sentence(eng_clean(r["OBSERVED_wwox_specific_evidence"]), 520), "demonstrated": clip_sentence(eng_clean(r["premise_demonstrated"]), 360), "missing": clip_sentence(eng_clean(r["premise_missing"]), 360),
                    "external": clip_sentence(eng_clean(r["external_precedents_with_reading_depth"]), 520), "opposed": clip_sentence(eng_clean(r["potentially_opposed_effects"]), 420),
                    "next": clip_sentence(eng_clean(r["next_decision_changing_experiment"]), 420), "status": clip_sentence(r["experiment_status"], 160)})
    # ---- predictive test (P3)
    pred = jload(dr / PRED_NAME)
    errs = validate_predictive(pred, p3, e1, dr)
    if errs:
        raise SystemExit(f"{PRED_NAME} is invalid:\n  " + "\n  ".join(errs))
    verdicts = []
    for v in pred["verdicts"]:
        src = e1 if v.get("source") == "e1" else p3
        nums = []
        for n in v["numbers"]:
            val = dig(src, n["path"]) - (dig(src, n["minus"]) if n.get("minus") else 0)
            nums.append({"id": n["id"], "value": round(val, n["digits"]), "digits": n["digits"]})
        for x in v.get("external_values") or []:
            nums.append({"id": x["id"], "value": x["value"], "digits": x["digits"]})
        verdicts.append({"id": v["id"], "comparison_it": v["comparison_it"], "verdict": v["verdict"], "numbers": nums, "reopen_it": v["reopen_it"]})
    predictive = {"exploratory": True, "question": pred["question"], "question_it": pred["question_it"], "methods": pred["methods"], "preregistration": pred["preregistration"], "threshold": pred["threshold"],
                  "minimum_detectable_effect": pred["minimum_detectable_effect"], "universe": {"families": p3["nU"], "signatures": p3["n_signatures"], "pilot_families": pred["universe"]["pilot_families"], "catalogue_families": n_fam},
                  "verdicts": verdicts, "limits_it": pred["limits_it"]}
    # ---- context concordance (P4)
    cv = jload(dr / CTX_NAME)
    mrows = read_tsv(dr / P4_DIR / "context_matrix.tsv")
    st = context_stats(mrows, cv)
    errs = validate_contexts(cv, mrows, st)
    if errs:
        raise SystemExit(f"{CTX_NAME} or the context matrix is invalid:\n  " + "\n  ".join(errs))
    unk = sum(1 for r in mrows if r["direction"] == "UNKNOWN")
    ctx_ids = list(dict.fromkeys(r["context_id"] for r in mrows))
    contexts = {"cells": len(mrows), "unknown": unk, "measured": len(mrows) - unk, "contexts": len(ctx_ids), "quantities": len(st), "models": len(set(cv["models"].values())),
                "model_labels_it": cv["model_labels_it"], "models_of": cv["models"], "context_ids": ctx_ids,
                "rows": [{"id": q, "quantity": s["quantity"], "quantity_it": cv["verdicts"][q]["quantity_it"], "verdict": derive_context_verdict(s), "higher": s["higher"], "lower": s["lower"], "other": s["other"],
                          "unknown": s["unknown"], "models_resolved": s["models_resolved"], "models_measured": s["models_measured"], "directions": [s["directions"][c] for c in ctx_ids], "note_it": cv["verdicts"][q]["note_it"]} for q, s in st.items()],
                "verdict_counts": dict(Counter(derive_context_verdict(s) for s in st.values()))}
    return {"selection": selection, "hypotheses": hyp, "predictive": predictive, "contexts": contexts}


def research_update_date(dr: Path, *dates) -> str | None:
    """Date of the newest research content, kept apart from the needs-register date and from the catalogue build date: the latest of the dates given (needs register, work order, graph) and of the dated cycle records of the module (a file or directory name ending _YYYYMMDD)."""
    found = [d for d in dates if d]
    for p in sorted(dr.iterdir()):
        m = re.search(r"_(20\d\d)(\d\d)(\d\d)(?:\.\w+)?$", p.name)
        if m:
            found.append("-".join(m.groups()))
    return max(found) if found else None


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
    titles = load_titles(dr)   # PMID -> {"title","journal","year"}; offline, from the tracked cache plus the join cache
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
                        "readout": o.get("readout"), "level": o.get("readout_level"), "limits": clip(o.get("limits"), 220), "pmid": o.get("pmid"), "cite": cite_of(titles, o.get("pmid"))})
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
                            "depth": a.get("reading_depth"), "target": clip(a.get("target_id") or "", 140), "sign": (pr or {}).get("sign"), "kind": (pr or {}).get("evidence_kind"), "pmids": ids})
        # per-link statistics from the module's pertinence table
        lk = {}
        depth_of = {x["id"]: x["depth"] for x in asserts}
        def _ok_acc(a):   # shareable: only categories stated from a class-A scope (IT5 P13)
            return (not shareable) or access_category_allowed(a, allow)[0]
        acc_c = sorted({a for r in card_rows.get(cid, []) for a in (r.get("access_categories") or []) if a != "unknown/unverified" and _ok_acc(a)})
        for nid in lneeds:
            rs = [r for r in pert if r["card_id"] == cid and r["need_id"] == nid]
            n_w = sum(1 for r in rs if r["evidence_kind"] == "readout_in_wwox_system" and r["counts_L3"] == "yes")
            n_c = sum(1 for r in rs if r["evidence_kind"] == "case_report_wwox_clinical")
            n_o = sum(1 for r in rs if r["evidence_kind"] == "readout_other_disease")
            n_null = sum(1 for r in rs if r["sign"] == "null")
            n_harm = sum(1 for r in rs if r["sign"] == "harm")
            has_next = bool(nxt)
            fx = classify_rows(rs, depth_of)
            pos, crit = assign_need_position(fx, bool(absn), has_next, bool(nmap[nid]["n_wwox_obs"]))
            by_id = {r["assertion_id"]: r for r in rs}
            carrier = [f'{i}: {clip(by_id[i].get("basis"), 110)} [{clip(by_id[i].get("flags"), 110)}]' for i in fx["firm"]]
            tags = []
            if fx["tool"]:
                tags.append("tool compound, not a candidate drug")
            if (pos.startswith("F") or pos == "P3") and fx["o_counter"]:
                tags.append(f'counter-evidence outside WWOX in rows ({fx["o_counter"]})')
            dfx = display_facts(rs, depth_of)
            fam_set = {"F1": "F_w", "F2": "F_w", "C1": "C_w", "C2": "C_w", "F3": "F_o", "C3": "C_o"}.get(pos)
            if fam_set:   # a criterion, not a tag: how the rows behind the position were read (decides nothing)
                crit = crit + [("the signed rows behind this position were read beyond abstract, query or unknown depth (found: " + str(dfx["n_set"][fam_set]) + " row(s))", not dfx["shallow"][fam_set])]
            if dfx["downstream"]:
                tags.append("the signed WWOX row(s) " + ", ".join(dfx["downstream"]) + " measure an endpoint downstream of the need, not the need's own readout")
            for sib, n in sorted(sibling_counters(cid, nid, pert, links).items()):
                tags.append(f"same compound, other card {sib}: {n} null or harm row(s) on this need")
            if pos == "F1" and fx["qualifiers"]:
                tags.append("beside a 'not normalised vs wild type' arm (" + ", ".join(fx["qualifiers"]) + ")")
            if fx["n_not_recovery"]:
                tags.append(f'{fx["n_not_recovery"]} wild-type-only comparison row(s) counted neither way')
            wdepths = sorted({depth_of.get(r["assertion_id"]) or "not recorded" for r in rs if r["evidence_kind"] in WWOX_KINDS})
            wcomp = sorted({(r.get("comparator") or "none stated") for r in rs if r["evidence_kind"] in WWOX_KINDS})
            reasons = [
                ("Result in WWOX systems", f'{fx["result"]}: {fx["n_fav"]} favourable, {fx["n_null"]} null, {fx["n_unf"]} unfavourable, {fx["n_mix"]} mixed, {fx["n_incomplete"]} not normalised, {fx["n_unresolved"]} unresolved or unquantified signed WWOX-system row(s); {nmap[nid]["n_wwox_obs"]} WWOX-system observation(s) on the need'),
                ("Depth and quality", ("WWOX-side reading depths: " + ", ".join(wdepths) + "; comparators: " + ", ".join(wcomp) + f'; {len(fx["firm"])} favourable row(s) are controlled, deep enough and unflagged' if fx["n_wwox_rows"] else "no WWOX-side row to grade") + ("; carried by " + " | ".join(carrier) if carrier else "") + ("; row flags: " + clip("; ".join(sorted({f for r in rs if r["evidence_kind"] in WWOX_KINDS for f in str(r.get("flags") or "").split(";") if f})), 240) if fx["n_wwox_rows"] else "") + "; sources are not pooled and shared sources are not independent"),
                ("Outside WWOX", f'{fx["n_other_rows"]} other-disease, safety or label row(s): {fx["o_fav"]} favourable, {fx["o_counter"]} harm or null; {fx["n_target_engagement"]} target-engagement assay row(s); need direction: {nmap[nid]["dir"]} on {nmap[nid]["dir_on"]} ({clip(nmap[nid]["dir_cert"], 90)})'),
                ("Counter-evidence", ("pro and contra written as prose in the card (not itemised); " if against_note and not against else "") + f'{len(against)} itemised card item(s); {len(nmap[nid]["counter"])} need item(s); {n_null} null and {n_harm} harm signal(s) in the pertinent assertions'),
                ("Decisive premise", clip(absd.get("missing_datum") if absn and absd.get("missing_datum") else (nk[0] if nk else "none recorded"), 200)),
                ("Next step", ("named in the card; the rule does not judge what the step would reveal, read it in the profile" if has_next else "none named")),
                ("Feasibility actually known", ("US access evidence: " + ", ".join(acc_c) if acc_c else "not known (no access evidence obtained); shown, not assumed, and not used to place the card")),
                ("Criteria", "met: " + ("; ".join(t for t, m in crit if m) or "none") + ". Not met: " + ("; ".join(t for t, m in crit if not m) or "none")),
            ]
            lk[nid] = {"group": pos, "kind": POS_BY_ID[pos]["kind"], "result": fx["result"], "depth_class": ("controlled" if fx["firm"] else ("limited" if fx["n_wwox_rows"] else "none")),
                       "tags": tags, "carrier": carrier, "counter_in_rows": bool(fx["o_counter"] or fx["n_null"] or fx["n_unf"] or fx["n_mix"]),
                       "criteria": [{"text": t, "met": m} for t, m in crit], "n_w": n_w, "n_c": n_c, "n_o": n_o, "n_null": n_null, "n_harm": n_harm, "reasons": reasons}
        # catalogue side
        rws = card_rows.get(cid, [])
        chembl = sorted({x["chembl_id"] for x in (links.get(cid) or {}).get("links", []) if x.get("chembl_id")})
        acc = sorted({a for r in rws for a in (r.get("access_categories") or []) if (not shareable) or access_category_allowed(a, allow)[0]})
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
        name = inp["candidate"]["name"].split(" (")[0].strip()
        pre = name.split(": ")[0]
        name = pre if pre_count[pre] == 1 else name
        cands.append({
            "id": cid, "name": inp["candidate"]["name"], "short": clip(name, 80), "folder": folder, "goal": goal, "track": track, "tracks": tracks, "status": card_status(card)[0], "status_raw": clip(card_status(card)[1], 200),
            "abstention": bool(absn), "needs": lneeds, "links": lk, "positions": overview_positions(lk), "assessment": card.get("assessment"), "summary": card.get("directional_summary"),
            "why": clip(f.get("indication_and_transfer") or f.get("identity"), 420), "why_full": f.get("indication_and_transfer") or f.get("identity"),
            "identity": clip(f.get("identity"), 360), "mechanism": clip(f.get("mechanism"), 360), "novelty": clip(f.get("novelty_for_woree"), 360),
            "expected": clip(f.get("expected_contribution"), 200), "access_text": clip(f.get("time_to_access"), 240), "pharm": clip(f.get("pharmacology"), 360),
            "against": against, "against_note": against_note, "for": for_, "transfer_limits": efa.get("transfer_limits"), "not_known": nk,
            "missing": absd.get("missing_datum") if absd.get("missing_datum") else (nk[0] if nk else None), "reopen": clip(absd.get("search_record"), 260) if absd.get("search_record") else None,
            "next": clip(nxt, 360), "next_full": nxt, "limits": card.get("limits") or [], "asserts": asserts, "n_disease_assertions": len(inp.get("disease_assertions") or ([inp["disease_assertion"]] if inp.get("disease_assertion") else [])),
            "access": acc, "country": ("US evidence found" if acc and acc != ["unknown/unverified"] else "no country evidence obtained"), "chembl": chembl, "actions": act,
            "pmids": [{"id": k, "role": v, "title": (titles.get(k) or {}).get("title"), "journal": (titles.get(k) or {}).get("journal"), "year": (titles.get(k) or {}).get("year")} for k, v in sorted(pm.items())], "dois": dois, "scope_counts": scope_counts,
            "card_path": (f"../{folder}/{cid}.card.json" if not shareable else CARD_FILE_NOTE_IT.format(id=cid)), "n_prio": sum(len(prio_by_row.get(r["row_id"], [])) for r in rws),
            "disp": dict(sorted(Counter(p["disposition"] for r in rws for p in prio_by_row.get(r["row_id"], [])).items())),
        })
    dup = Counter(c["short"] for c in cands)
    for c in cands:   # two cards can share a display name (for example two PDK-inhibition cards): the id tells them apart
        if dup[c["short"]] > 1:
            c["short"] = f'{c["short"]} [{c["id"].split("_")[0]}]'
    for c in cands:   # IT6 P13: the one-page synthesis (8 fields) is assembled here, from the card and its needs only
        c["brief"] = make_brief(c, nmap)
    wtexts = {cid: json.dumps(v[0], ensure_ascii=False) for cid, v in cards.items()}
    wtexts.update({n["id"]: json.dumps(n, ensure_ascii=False) for n in needs})
    eg, wo = load_curated_docs(dr, cands, cneeds, titles, wtexts)
    for c in cands:   # window state (prevented / recovered after onset / reversible suppression / not measured), shown as chips next to the brief
        c["brief"]["window"] = wo["card_windows"].get(c["id"])
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
    research_update = research_update_date(dr, needs_doc.get("built_on"), wo["research_update"], eg.get("date"))
    meta = {"data_date": research_update, "research_update": research_update, "needs_built_on": needs_doc.get("built_on"), "catalogue_generated": stats.get("generated_utc"), "dgidb_export": "2024-06-10", "source": ctx["source"],
            "n_cards": len(cands), "n_needs": n_total, "n_cards_by_goal": dict(Counter(c["goal"] for c in cands)), "n_abstentions": sum(1 for c in cands if c["abstention"])}
    return {"meta": meta, "scopes": [{"code": c, "label": l, "glyph": g} for c, l, g in SCOPES], "goals": GOALS, "tracks": TRACKS, "threads": threads, "needs": cneeds, "cands": cands,
            "groups": GROUPS, "group_note": GROUP_NOTE, "gaps": gaps, "evidence_graph": eg, "work_order": wo}


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
            lab = tag[7:]
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
    identifiers = [{"label": k, "licence": v.get("licence"), "attribution": v.get("attribution"), "url": v.get("url")} for k, v in (allow.get("identifier_sources") or {}).items()]
    class_b = [{"label": k, "licence": v.get("licence"), "credit": v.get("credit"), "path": v.get("path"), "records_of": v.get("records_of")} for k, v in (allow.get("class_b_files") or {}).items()]
    return {"source": source, "embedded": embedded, "counts_only": counts_only, "identifiers": identifiers, "class_b": class_b,
            "note": "Shareable build: a third-party row is embedded only when its provenance is on the allowlist (the repository's allowlist of sources). Everything else appears as an identifier or a count. No attribution has been removed."}


def build_payload(dr: Path = DEFAULT_DR, source: str = "full", with_ranking: bool = True) -> dict:
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

    def cpath(cid):
        """Link to a card file. The shareable build has no repository-relative path: a card is reached through its profile in the same page."""
        p = card_path(dr, cid)
        return (f"#cand-{cid}" if p else None) if shareable else p

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
            cards.append({"id": cid, "att": c.get("attachment") if isinstance(c, dict) else None, "path": cpath(cid)})
        nm, ok = row_label(r)
        acc = r.get("access_categories") or []
        st = r.get("status_class") or []
        mod = r.get("modality") if isinstance(r.get("modality"), list) else [r.get("modality")]
        if shareable:   # IT5 P13: a row's status class and modality derive from ChEMBL/MATRIX/DGIdb statements; access categories only from class-A scopes. The page never reads st/mod of a row.
            if ok:
                kept = [c for c in acc if access_category_allowed(c, allow)[0]]
                for c in kept:
                    lab = access_category_allowed(c, allow)[1]
                    if lab:
                        emitted["access:" + lab] += 1
                acc = kept
            else:   # identifier and counts only; per-row attributes of a withheld record are not embedded
                acc = []
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
            "pha": [(cr.get("pharmacology_safety_info") or {}).get("safety_assessment"), [] if shareable else ((cr.get("pharmacology_safety_info") or {}).get("status_class") or [])],
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
            "cards": [{"id": c, "path": cpath(c)} for c in (src.get("cards") or [])],
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
        "excluded_rows": share_excluded_rows(cc.get("excluded_rows") or {}) if shareable else (cc.get("excluded_rows") or {}),
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
                               "cards": [{"id": c["card_id"], "path": cpath(c["card_id"])} for c in r["cards"]]})
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
    cur.update(build_it7(dr, funnel, summary["matrix"], summary["units"], cur))
    if with_ranking:
        rk = build_ranking(dr, cur, source)
        if rk:
            cur["ranking"] = rk
    cur["footer"] = build_footer(source, allow, emitted, srcs)
    P_out = {
        "source": source, "cur": cur,
        "schema": SCHEMA, "funnel": funnel, "access": access, "matrix_summary": mx, "observations": ob,
        "dispositions": [{"id": d, "n": pr["by_disposition"].get(d, 0), "cells": (pr.get("by_disposition_cells") or {}).get(d, pr["by_disposition"].get(d, 0)),
                          "fam": (pr.get("by_disposition_distinct_families_or_rows") or {}).get(d), "def": (prios.get("dispositions") or {}).get(d)} for d in disp_list],
        "has_distinct": bool(pr.get("by_disposition_distinct_families_or_rows")),
        "exploration_flagged": pr["exploration_flagged"], "needs": need_out, "rows": rows, "pairs": pairs, "strings": strings,
        "tech": tech, "excluded_detail": excluded_detail, "leads": leads.get("dispositions") or [], "leads_note": leads.get("_note"), "card_leads": card_leads, "orphan_priorities": len(orphan), "ranking_note": prios.get("ranking"), "no_probability": prios.get("no_probability"),
        "level_defs": dict(matrix.get("levels") or {}), "pair_unit": matrix.get("unit"),
    }
    return apply_prose_policy(P_out, allow) if shareable else P_out


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
    share = P["source"] == "shareable"   # no repository-relative link in the shareable build: file names are printed as text
    if share:
        ld.append('<p>A catalogue target listing (a stated action, or none) is a source statement, not a recommendation. Reasoned endings of searches, including abstentions and opposite mechanisms, each with what would reopen it. File names below are repository records, printed as text (they are not part of this package).</p>')
    else:
        ld.append('<p>A catalogue target listing (a stated action, or none) is a source statement, not a recommendation. Reasoned endings of searches, including abstentions and opposite mechanisms, each with what would reopen it. Same content as the section "Catalogue-derived leads" of <a href="../../repurposing_batch_selection_20261028_module.md">the handoff</a> (<code>../../repurposing_batch_selection_20261028_module.md</code>). Sources: <code>coverage/lead_dispositions.json</code>.</p>')
    ld.append(f'<h3>Lead dispositions ({num("leads.n", len(P["leads"]))})</h3>')
    for d in P["leads"]:
        card = (f'<code>{E(d["card"])}</code>' if share else f'<a href="../{E(d["card"])}">{E(d["card"])}</a>') if d.get("card") else "no card"
        rec = d.get("record")
        reca = (f'<code>{E(rec)}</code>' if share else f'<a href="../{E(rec)}">{E(rec)}</a>') if rec else "none"
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
<html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>__TITLE__</title>
<style>__CSS__</style></head><body>
<a class="skip" href="#main">__SKIP__</a>
<header><div class="in"><h1>__H1__</h1>
<p class="subline">__SUB__</p></div></header>
__BANNER__<nav aria-label="__NAVLABEL__"><div class="in"><a href="#overview">__N_OV__</a><a href="#ranking">__N_RK__</a><a href="#threads">__N_TH__</a><a href="#chains">__N_EG__</a><a href="#charts">__N_CH__</a><a href="#selection">__N_SE__</a><a href="#hypotheses">__N_HY__</a><a href="#predictive">__N_PR2__</a><a href="#navigate">__N_NAV__</a><a href="#candidates">__N_CA__</a><a href="#priorities-cur">__N_PR__</a><a href="#compare">__N_CP__</a><a href="#technical">__N_TD__</a></div></nav>
<main id="main">
__CURATED__
<details id="technical" class="techwrap"><summary class="techsum">__TD_SUM__</summary>
<p class="mut technote">__TD_NOTE__</p>
<section id="funnel"><h2>Imbuto dal catalogo ai valutati: che cosa è contato, in quale unità</h2>__FUNNEL__</section>
<section id="access"><h2>Distribuzione per categoria di accesso</h2>__ACCESS__</section>
<section id="filters"><h2>Filtri per la matrice completa <span class="mut">(sezioni seguenti; shareable through the URL hash, for example <code>#f=disp:exploration_candidate&amp;need:NEED-ISR-ATTENUATION</code>)</span></h2>
<div class="filters">
<label>Access category<select id="f-access"></select></label><label>Need<select id="f-need"></select></label>
<label>Need evidence scope<select id="f-scope"></select></label><label>Observation scope (L3/L4)<select id="f-oscope"></select></label>
<label>Track<select id="f-track"></select></label><label>Recovery goal<select id="f-goal"></select></label>
<label>Disposition<select id="f-disp"></select></label><label>Text search<input type="search" id="f-q" placeholder="name, id, target, card, hypothesis"></label></div>
<div class="bar-actions"><button id="f-reset">reset filters</button><span><span class="cnt" id="cnt-pairs">0</span> of <span id="cnt-pairs-of">0</span> pairs match; <span class="cnt" id="cnt-prio">0</span> of <span id="cnt-prio-of">0</span> prioritised; <span class="cnt" id="cnt-needs">0</span> needs shown</span></div>
<div class="chips" id="lvl-now" aria-live="polite"></div><div class="chips" id="disp-now"></div></section>
<section id="needs"><h2>Bisogni: direzione, Track, obiettivo, prove, livelli, lacune</h2>
<p class="mut">A need is a place where the record observed something and an intervention could be aimed. Needs whose direction is <i>uncertain</i> are exploration only: L2 is not evaluable there. Level counts are cells (family, need) and are never summed across levels or needs.</p>
<div class="needs" id="needs-list"></div></section>
<section id="matrix"><h2>Matrice: interventi e famiglie di composti x bisogni</h2>
<p class="mut">Pair unit: __PAIRUNIT__. Four levels are shown side by side and never summed or scored. Scope is shown on L3 and L4.</p>
__LEVELS__
<div class="pager" id="pg-m"></div><div id="matrix-list"></div></section>
<section id="priorities"><h2>Disposizioni: una per coppia, con motivi per criterio</h2>
__DISPOSITIONS__
<div class="note">Dispositions are distinct: <b>source queried without result</b> (the sources were asked and returned no row for the record), <b>incomplete or failed query</b> (a source was not in state OK; this is never a negative) and <b>not relevant / no catalogue link found</b> and <b>insufficient data</b> (a decision from the data that exist) are different statements and are not merged.</div>
<div class="pager" id="pg-p"></div><div id="prio-list"></div></section>
<section id="leads"><h2>Piste derivate dal catalogo e loro disposizioni</h2>__LEADS__</section>
<section id="limits"><h2>Limiti dichiarati</h2>__LIMITS__</section>
<section id="tech-versions"><h2>Versioni, fonti, impronte digitali e rigenerazione</h2>__TECH__</section>
</details>
</main>
<footer id="attribution" aria-label="Fonti e licenze">__FOOTER__</footer>
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


def fmt_it(n) -> str:
    return f"{n:,}".replace(",", ".") if isinstance(n, int) else str(n)


def pct_it(p) -> str:
    return f"{p}".replace(".", ",") + "%"


def numit(key: str, value) -> str:
    """Headline number in Italian digit grouping; data-v keeps the raw value so a test can compare it with the source JSON."""
    return f'<b class="num" data-k="{E(key)}" data-v="{E(str(value))}">{E(fmt_it(value))}</b>'


def pos_chip(pid: str, n: int | None = None, long: bool = False) -> str:
    """Letter chip: the letter, its meaning in words and a border style carry the sense; the colour never does alone."""
    p = POS_IT[pid]
    lab = pid + (" " + p["short"] if long else "")
    return f'<span class="grp {pid.lower()}" title="{E(p["label"])}">{E(lab)}' + (f' ×{n}' if n else "") + '</span>'


def scope_chip(code: str, n: int | None = None) -> str:
    g = next((x[2] for x in SCOPES if x[0] == code), "?")
    return f'<span class="sc s-{E(code)}"><span class="gl" aria-hidden="true">{E(g)}</span>{E(SCOPE_IT.get(code, code))}' + (f' ×{n}' if n else "") + '</span>'


STATE_IT = {"ok": "ok", "failed": "interrogazione non riuscita", "incomplete": "incompleta", "stale": "dati non aggiornati", "truncated": "parziale", "not_fetched": "non acquisita", "other": "stato non riconosciuto"}


def state_label_it(x: dict) -> str:
    """Plain Italian for a source state; the raw code stays in the technical table."""
    return "esportazione non aggiornata" if "EXPORT" in str(x["status"]).upper() and x["state_class"] == "stale" else STATE_IT.get(x["state_class"], "stato non riconosciuto")


def render_banner(P: dict) -> str:
    """One compact line: the source states stay visible; versions, details and the state table live in the technical drill-down."""
    bad = [x for x in P["tech"]["sources"] if x["state_class"] != "ok"]
    if not bad:
        return ""
    U = UI_IT
    chips = " ".join(f'<span class="st st-{x["state_class"]}" data-banner="{E(x["id"])}">{E(x["name"].split(" (")[0])}: {E(state_label_it(x))}</span>' for x in bad)
    return (f'<div class="warnbar" id="source-banner" role="note"><b>{E(U["source_limited"])}:</b> {chips} <a href="#technical">{E(U["see_tech"])}</a>. <span class="btail">{E(U["source_limited_tail"])}</span></div>')


def thread_view(cur: dict, t: dict) -> dict:
    """Everything one thread card shows, computed from the payload (no rule is applied here: positions are read, never assigned)."""
    needs = [n for n in cur["needs"] if n["id"] in t["needs"]]
    links = [(c, nid, c["links"][nid]) for c in cur["cands"] for nid in t["needs"] if nid in c["links"]]
    by_card: dict[str, list[str]] = {}
    for c, nid, l in links:
        by_card.setdefault(c["id"], []).append(l["group"])
    cmap = {c["id"]: c for c in cur["cands"]}
    ev = Counter(o["scope"] for n in needs for o in n["obs"])
    return {"needs": needs, "links": links, "by_card": by_card, "cmap": cmap, "ev": ev,
            "pos": Counter(l["group"] for _, _, l in links),
            "n_no_wwox": sum(1 for n in needs if n["n_wwox_obs"] == 0), "n_no_l4": sum(1 for n in needs if n["no_l4"]),
            "n_links_wwox": sum(1 for _, _, l in links if l["result"] != "none"),
            "deep": sum(1 for n in needs if n["goal"] == "deep_recovery"), "partial": sum(1 for n in needs if n["goal"] == "partial_benefit"),
            "tracks": Counter(n["track"] or "none" for n in needs)}


def render_overview(P: dict) -> str:
    """First screen, server-rendered from the payload so that it reads without JavaScript. All orientation text comes from UI_IT."""
    cur = P["cur"]
    meta, cands, needs = cur["meta"], cur["cands"], cur["needs"]
    U = UI_IT
    from urllib.parse import quote
    n_pos = Counter(l["group"] for c in cands for l in c["links"].values())   # need-level links per position; a card is never given one position

    def tile(key, val, unit, desc):
        return f'<div class="tile"><span class="big">{numit(key, val)}</span><span class="u">{E(unit)}</span><span class="d">{E(desc)}</span></div>'
    tiles = "".join([tile("cur.needs", len(needs), U["unit_needs"], U["d_needs"]), tile("cur.threads", len(cur["threads"]), U["unit_threads"], U["d_threads"]),
                     tile("cur.cards", len(cands), U["unit_cards"], U["d_cards"]), tile("cur.abstentions", meta["n_abstentions"], U["unit_abst"], U["d_abst"])])
    fam = {"F": ("fam_F", "fam_F_txt"), "C": ("fam_C", "fam_C_txt"), "P": ("fam_P", "fam_P_txt")}
    legend = "".join(f'<span class="lg lg-{k.lower()}"><span class="grp {k.lower()}1" title="{E(U[b])}">{k}</span> <b>{E(U[a])}</b></span>' for k, (a, b) in fam.items())
    legend_all = "".join(f'<li>{pos_chip(g["id"])} <b>{E(POS_IT[g["id"]]["short"])}.</b> <span class="mini">{E(POS_IT[g["id"]]["plain"])}</span></li>' for g in GROUPS)
    gtxt = {"deep_recovery": ("deep", U["goal_deep"], U["goal_deep_long"]), "partial_benefit": ("partial", U["goal_partial"], U["goal_partial_long"])}
    panels = []
    for g, (cls, title, long_) in gtxt.items():
        cs = [c for c in cands if c["goal"] == g]
        ns = [n for n in needs if n["goal"] == g]
        tr = Counter(c["track"] or "none" for c in cs)
        lk = Counter(l["group"][0] for c in cands for nid, l in c["links"].items() if NM_GOAL(needs, nid) == g)   # by the goal of the NEED: every link is counted once, none is dropped
        panels.append(
            f'<div class="goal {cls}" data-goal="{g}"><h3>{E(title)}</h3><p class="mini">{E(long_)}</p>'
            f'<div class="kv"><b>{E(U["needs_with_aim"])}:</b> {numit("cur.goal." + g + ".needs", len(ns))}</div>'
            f'<div class="kv"><b>{E(U["cards_with_aim"])}:</b> {numit("cur.goal." + g + ".cards", len(cs))} ({E(U["of_which_abst"].format(n=sum(1 for c in cs if c["abstention"])))})</div>'
            f'<div class="kv"><b>{E(U["track_field"])}:</b> ' + "; ".join(f'Track {E(k)}: {v}' if k != "none" else f'{E(U["track_none"])}: {v}' for k, v in sorted(tr.items())) + '</div>'
            f'<div class="kv"><b>{E(U["goal_links"])}:</b> ' + " ".join(f'<span class="grp {k.lower()}1">{k}</span> ×{lk[k]}' for k in "FCP" if lk[k]) + f' <span class="mini mut">({sum(lk.values())})</span></div></div>')
    n_cross = sum(1 for c in cands if c["goal"] for nid in c["links"] if NM_GOAL(needs, nid) and NM_GOAL(needs, nid) != c["goal"])
    n_links = sum(len(c["links"]) for c in cands)
    cards = []
    for t in cur["threads"]:
        v = thread_view(cur, t)
        nm, tx = THREAD_IT.get(t["id"], (t["name"], t["text"]))
        cn = sorted(v["by_card"], key=lambda i: v["cmap"][i]["short"].lower())
        chips = "".join(f'<a class="cc" href="#cand-{E(i)}" data-open="{E(i)}">{E(v["cmap"][i]["short"])} ' + "".join(pos_chip(g) for g in sorted(set(v["by_card"][i]))) + '</a>' for i in cn[:6])
        more = f'<span class="mini mut"> +{len(cn) - 6} {E(U["th_more"])}</span>' if len(cn) > 6 else ""
        miss = []
        for i in cn:
            c = v["cmap"][i]
            if c.get("missing") and len(miss) < 3:
                miss.append(f'<li><b>{E(c["short"])}:</b> {E(clip(c["missing"], 170))}</li>')
        cards.append(
            f'<article class="thread" data-thread="{E(t["id"])}"><h3>{E(nm)}</h3><p class="tx">{E(tx)}</p>'
            f'<p class="dim"><b>{E(U["th_aim"])}:</b> {v["deep"]} {E(U["th_needs_n"])} {E(U["th_deep"])} · {v["partial"]} {E(U["th_needs_n"])} {E(U["th_partial"])} · '
            + " · ".join(f'Track {E(k)} {n}' for k, n in sorted(v["tracks"].items()) if k != "none") + '</p>'
            f'<div class="row"><span class="lab">{E(U["th_cands"])}</span>' + (chips + more if chips else f'<span class="mut">{E(U["th_cands_none"])}</span>') + '</div>'
            f'<div class="row"><span class="lab">{E(U["th_why"])}</span>' + (" ".join(pos_chip(k, n) for k, n in sorted(v["pos"].items())) or f'<span class="mut">{E(U["th_cands_none"])}</span>') + '</div>'
            f'<div class="row"><span class="lab">{E(U["th_evid"])}</span>' + ("".join(scope_chip(k, n) for k, n in sorted(v["ev"].items(), key=lambda kv: (-kv[1], kv[0]))) or f'<span class="mut">{E(U["th_evid_none"])}</span>') + f'<span class="mini mut"> {E(U["th_obs_note"])}</span></div>'
            f'<div class="row gap"><span class="lab">{E(U["th_gap"])}</span><ul class="mini"><li>{v["n_no_wwox"]} / {len(v["needs"])} {E(U["th_gap_wwox"])}</li><li>{v["n_no_l4"]} / {len(v["needs"])} {E(U["th_gap_l4"])}</li></ul>'
            + (f'<details class="inl"><summary>{E(U["th_gap_card"])}</summary><ul class="mini">{"".join(miss)}</ul></details>' if miss else '') + '</div>'
            f'<a class="go" href="#c=thread:{quote(t["id"])}">{E(U["th_explore"])}</a></article>')
    dd = meta["data_date"]
    srcnote = U["src_share" if P["source"] == "shareable" else "src_full"]
    return (
        f'<section id="overview" aria-labelledby="h-over"><h2 id="h-over">{E(U["ov_h"])}</h2>'
        f'<div class="legendrow" role="group" aria-label="{E(U["legend_h"])}"><b>{E(U["legend_h"])}:</b> {legend}</div>'
        f'<p class="lead">{E(U["ov_lead"])} <span class="mini mut">{E(U["need_gloss"])}</span></p>'
        f'<div class="warnstrip" role="note"><b>{E(U["warn_h"])}.</b> {E(U["warn_1"])} {E(U["warn_2"])}</div>'
        f'<details class="inl howto"><summary>{E(U["how_sum"])}</summary><div class="twocol"><div class="how"><h3>{E(U["how_h"])}</h3><ol><li>{E(U["how_1"])}</li><li>{E(U["how_2"])}</li><li>{E(U["how_3"])}</li><li>{E(U["how_4"])}</li></ol><p class="mini">{E(U["warn_3"])}</p></div>'
        f'<div class="legendbox"><p class="mini mut">{E(U["legend_note"])}</p><ul class="poslist">{legend_all}</ul></div></div></details>'
        f'<p class="meta-line"><b>{E(U["data_date"])}:</b> <span data-k="meta.data_date" data-v="{E(str(dd))}">{E(str(dd))}</span> · <b>{E(U["bf_needs_rec"])}</b> <span data-k="meta.needs_built_on" data-v="{E(str(meta["needs_built_on"]))}">{E(str(meta["needs_built_on"]))}</span> · <b>{E(U["bf_cat_build"])}</b> <span data-k="meta.catalogue_generated" data-v="{E(str(meta["catalogue_generated"]))}">{E(str(meta["catalogue_generated"]))}</span> · <b>{E(U["perimeter"])}:</b> {E(U["perimeter_txt"])} · {E(srcnote)}</p>'
        f'<h3 id="threads">{E(U["th_h"])}</h3><p class="mini mut">{E(U["th_note"])}</p><div class="threads">' + "".join(cards) + '</div>'
        f'<h3>{E(U["goals_h"])}</h3><p class="mini mut">{E(U["goals_note"])} {E(U["goal_cross"].format(total=n_links, cross=n_cross))}</p><div class="goals">' + "".join(panels) + '</div>'
        f'<h3>{E(U["facts_h"])}</h3><div class="tiles">' + tiles + f'</div><p class="mini mut">{E(U["unit_note"])}</p></section>')


# ------------------------------------------------------------------ IT6 P13: server-rendered evidence graph (inline SVG) and work order
EG_COLW, EG_PITCH, EG_PADX, EG_HEADH, EG_LINEH, EG_PADY, EG_GAP, EG_CHARS = 172, 196, 8, 30, 15, 6, 14, 24


def _wrap(text: str, width: int) -> list[str]:
    return textwrap.wrap(str(text), width=width, break_long_words=True, break_on_hyphens=False) or [""]


def layout_chain(ch: dict) -> dict:
    """Pure geometry of one chain: boxes per node (x, y, w, h, text lines), the width and the height. Deterministic; columns are vertically centred on the tallest one."""
    U = UI_IT
    cols: dict[str, list[dict]] = {c: [] for c in GRAPH_COLUMNS}
    for n in ch["nodes"]:
        lines = _wrap(n["label"], EG_CHARS)
        tag = U.get("eg_scope_" + n["scope"], "")
        if n["unresolved"]:
            tag = (U["eg_unres"] + (" · " + tag if tag else ""))
        tag_lines = _wrap(tag, 28) if tag else []
        h = EG_PADY * 2 + len(lines) * EG_LINEH + len(tag_lines) * (EG_LINEH - 1)
        cols[n["col"]].append({"n": n, "lines": lines, "tag": tag_lines, "h": h})
    heights = {c: sum(b["h"] for b in bs) + EG_GAP * max(0, len(bs) - 1) for c, bs in cols.items()}
    top = max(heights.values())
    boxes: dict[str, dict] = {}
    for ci, c in enumerate(GRAPH_COLUMNS):
        y = EG_HEADH + 8 + (top - heights[c]) / 2
        for b in cols[c]:
            boxes[b["n"]["id"]] = {"x": EG_PADX + ci * EG_PITCH, "y": round(y, 1), "w": EG_COLW, "h": b["h"], "lines": b["lines"], "tag": b["tag"], "n": b["n"]}
            y += b["h"] + EG_GAP
    return {"boxes": boxes, "width": EG_PADX * 2 + (len(GRAPH_COLUMNS) - 1) * EG_PITCH + EG_COLW, "height": int(EG_HEADH + 8 + top + 12)}


def render_chain_svg(ch: dict) -> str:
    U = UI_IT
    lay = layout_chain(ch)
    W, H, boxes = lay["width"], lay["height"], lay["boxes"]
    cid = E(ch["id"])
    parts = [f'<svg class="eg" xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="eg-t-{cid} eg-d-{cid}">'
             f'<title id="eg-t-{cid}">{E(ch["title"])}</title><title id="eg-d-{cid}">{E(U["eg_svg_desc"].format(n=len(ch["nodes"]), m=len(ch["edges"])))}</title>'
             f'<defs><marker id="eg-ar-{cid}" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="7" markerHeight="7" orient="auto"><path class="eg-ar" d="M0,0 L8,4 L0,8 z"/></marker></defs>']
    for ci, c in enumerate(GRAPH_COLUMNS):
        parts.append(f'<text class="eg-ch" x="{EG_PADX + ci * EG_PITCH}" y="{EG_HEADH - 10}">{E(c)}</text>')
    for e in ch["edges"]:
        a, b = boxes[e["from"]], boxes[e["to"]]
        x1, y1, x2, y2 = a["x"] + a["w"], a["y"] + a["h"] / 2, b["x"] - 2, b["y"] + b["h"] / 2
        d = (x2 - x1) / 2
        code = EDGE_CODE[e["type"]]
        parts.append(f'<g class="eg-e" data-edge-type="{E(e["type"])}"><path class="eg-line e-{code}" d="M{x1:.1f},{y1:.1f} C{x1 + d:.1f},{y1:.1f} {x2 - d:.1f},{y2:.1f} {x2:.1f},{y2:.1f}" marker-end="url(#eg-ar-{cid})"/>'
                     f'<g class="eg-b"><circle cx="{(x1 + x2) / 2:.1f}" cy="{(y1 + y2) / 2:.1f}" r="8"/><text x="{(x1 + x2) / 2:.1f}" y="{(y1 + y2) / 2 + 3.2:.1f}">{code}</text></g></g>')
    for nid, bx in boxes.items():
        n = bx["n"]
        txt = "".join(f'<tspan x="{bx["x"] + 6}" y="{bx["y"] + EG_PADY + EG_LINEH * (i + 1) - 3}">{E(t)}</tspan>' for i, t in enumerate(bx["lines"]))
        ty = bx["y"] + EG_PADY + EG_LINEH * len(bx["lines"])
        txt += "".join(f'<tspan class="tag" x="{bx["x"] + 6}" y="{ty + (EG_LINEH - 1) * (i + 1) - 2}">{E(t)}</tspan>' for i, t in enumerate(bx["tag"]))
        cls = f'eg-n sc-{E(n["scope"])}' + (" unres" if n["unresolved"] else "")
        body = f'<g class="{cls}" data-node="{E(nid)}" data-col="{E(n["col"])}"><rect x="{bx["x"]}" y="{bx["y"]}" width="{bx["w"]}" height="{bx["h"]}" rx="5"/><text>{txt}</text></g>'
        if n["cards"]:
            body = f'<a href="#cand-{E(n["cards"][0])}" data-open="{E(n["cards"][0])}"><title>{E(U["eg_open_card"])}: {E(n["cards"][0])}</title>{body}</a>'
        parts.append(body)
    parts.append("</svg>")
    return "".join(parts)


def render_evidence_graph(P: dict) -> str:
    """Section 'Catene': five chains as inline SVG (no JavaScript needed), a legend, and a table of the edges as the text alternative. The figure scrolls inside its own container."""
    U = UI_IT
    eg = P["cur"]["evidence_graph"]
    sw = "".join(f'<li><svg class="eg-sw" width="46" height="12" viewBox="0 0 46 12" aria-hidden="true" focusable="false"><path class="eg-line e-{EDGE_CODE[t]}" d="M2,6 L44,6"/></svg> <b>{EDGE_CODE[t]}</b> <span class="mini">{E(U["eg_leg_" + EDGE_CODE[t]])}</span></li>' for t in EDGE_TYPES)
    out = [f'<section id="chains" aria-labelledby="h-chains"><h2 id="h-chains">{E(U["eg_h"])}</h2><p class="lead">{E(U["eg_lead"])}</p>'
           f'<p class="mini mut">{E(U["eg_note_en"])} {E(U["eg_no_interactome"])} {E(U["eg_scroll"])} {E(U["eg_date"])} <span data-k="cur.graph_date" data-v="{E(str(eg["date"]))}">{E(str(eg["date"]))}</span>.</p>'
           f'<div class="eg-legend" role="group" aria-label="{E(U["eg_legend_h"])}"><b>{E(U["eg_legend_h"])}.</b> {E(U["eg_leg_line"])}:<ul class="eg-leg">{sw}</ul>'
           f'<p class="mini">{E(U["eg_leg_nodes"])}: ' + "; ".join(E(U["eg_scope_" + s]) for s in ("wwox", "wwox_other", "non_wwox", "computational", "proposed")) + f'. {E(U["eg_unres"])}: <span class="grp c1">{E(U["eg_unres"])}</span></p></div>']
    for ch in eg["chains"]:
        nm = {n["id"]: n for n in ch["nodes"]}
        rows = "".join(
            f'<tr><td>{E(nm[e["from"]]["label"])}<div class="mut">{E(nm[e["from"]]["col"])}</div></td><td>{E(nm[e["to"]]["label"])}<div class="mut">{E(nm[e["to"]]["col"])}</div></td>'
            f'<td><b>{E(e["type"])}</b> <span class="mut">({EDGE_CODE[e["type"]]})</span></td><td>{E(e["src"]["label"])}' + (f' <span class="mut">{E(e["src"]["title"])}</span>' if e["src"]["title"] else "") + f'</td><td>{E(e["note"])}</td></tr>'
            for e in ch["edges"])
        out.append(
            f'<article class="chain" id="chain-{E(ch["id"])}" data-chain="{E(ch["id"])}" data-state="{E(ch["state"])}"><h3>{E(ch["title"])} <span class="grp {"c1" if ch["state"] == "non risolto" else "p1"}">{E(U["eg_state_" + ch["state"].replace(" ", "_")])}</span></h3>'
            f'<p class="mini">{E(ch["question"])}</p><p class="mini eg-cue">{E(U["eg_cue"])}</p><div class="eg-fig" tabindex="0" role="group" aria-label="{E(ch["title"])}">{render_chain_svg(ch)}</div>'
            f'<details class="inl"><summary>{E(U["eg_table_sum"])} ({len(ch["edges"])})</summary><table class="tbl"><thead><tr><th>{E(U["eg_th_from"])}</th><th>{E(U["eg_th_to"])}</th><th>{E(U["eg_th_type"])}</th><th>{E(U["eg_th_src"])}</th><th>{E(U["eg_th_note"])}</th></tr></thead><tbody>{rows}</tbody></table></details></article>')
    out.append("</section>")
    return "".join(out)


def render_work_order(P: dict) -> str:
    """Work order per need, server-rendered inside the priorities section: the reason for the next study, the question, and (one click further) the data, the effect and the feasibility actually known."""
    U = UI_IT
    cur = P["cur"]
    wo = cur["work_order"]
    cat = str(cur["meta"].get("catalogue_generated"))
    kcls = {WO_KINDS[0]: "v", WO_KINDS[1]: "c", WO_KINDS[2]: "p"}
    nm = {n["id"]: n for n in cur["needs"]}
    items = []
    for e in wo["entries"]:
        n = nm[e["need"]]
        pos = "".join(pos_chip(g) for g in e["positions"]) or f'<span class="mut">{E(U["wo_no_pos"])}</span>'
        ws = "".join(f'<li><span class="chip ws ws-{E(x["state"])}" title="{E(x["note"])}">{E(U["ws_" + x["state"]])}</span> <span class="mini">{E(x["note"])}</span></li>' for x in e["window_state"])
        win = f'<div class="wo-win"><b class="mini">{E(U["wo_window"])}:</b><ul class="mini">{ws}</ul></div>' if ws else ""
        upd = (f'<dt>{E(U["wo_upd"])}</dt><dd>{E(", ".join(e["updated_by"]))}</dd>') if e["updated_by"] else ""
        cards = ", ".join(E(c) for c in e["cards"])
        items.append(
            f'<article class="wo-item" id="wo-{E(e["need"])}" data-need="{E(e["need"])}" data-kind="{E(e["kind"])}"><h4>{E(NEED_IT.get(e["need"], n["short"]))} <span class="mut">{E(e["need"])}</span></h4>'
            f'<div class="wo-meta"><span class="chip wo-k wo-k-{kcls[e["kind"]]}" title="{E(U["wo_kind"])}">{E(U["wo_kind"])}: <b>{E(e["kind"])}</b></span> <span class="mini mut">{E(U["wo_pos"])}:</span> {pos}</div>'
            f'<p class="wo-sum"><b>{E(U["wo_brief"])}.</b> {E(e["summary_it"])}</p><p class="wo-q"><b>{E(U["wo_q"])}.</b> {E(e["question"])}</p>{win}'
            f'<details class="inl"><summary>{E(U["wo_more"])}</summary><dl class="wo-dl"><dt>{E(U["wo_data"])}</dt><dd>{E(e["data"])}</dd><dt>{E(U["wo_change"])}</dt><dd>{E(e["would_change"])}</dd>'
            f'<dt>{E(U["wo_feas"])}</dt><dd class="wo-feas"><b>{E(e["feasibility_it"])}</b><br>{E(e["feasibility"])}</dd><dt>{E(U["wo_date"])}</dt><dd>{E(e["date"])}</dd>{upd}<dt>{E(U["wo_cards"])}</dt><dd>{cards}</dd></dl>'
            f'<p class="mini mut">{E(U["wo_text_en"])}</p></details></article>')
    return (f'<div id="work-order" class="wo-wrap"><h3>{E(U["wo_h"])}</h3><p class="note">{E(U["wo_note"])}</p>'
            f'<p class="meta-line"><b>{E(U["wo_update"])}:</b> <span data-k="cur.work_order_date" data-v="{E(wo["research_update"])}">{E(wo["research_update"])}</span> · <b>{E(U["wo_catalogue"])}:</b> <span data-k="cur.catalogue_generated" data-v="{E(cat)}">{E(cat)}</span> <span class="mini mut">({E(U["wo_dates_note"])})</span></p>'
            + "".join(items) + '</div>')


# ------------------------------------------------------------------ IT7 P7: server-rendered sections (no JavaScript needed to read them)
def dec_it(v: float, digits: int) -> str:
    return f"{v:.{digits}f}".replace(".", ",")


def pct_str(a, b) -> str:
    return f"{100 * a / b:.1f}"


def pct_span(key: str, a, b, suffix: str) -> str:
    p = pct_str(a, b)
    return f'<span class="mut">(<span data-k="{E(key)}" data-v="{p}">{E(p.replace(".", ","))}%</span> {E(suffix)}{E(fmt_it(b))})</span>'


def sel_values(i: dict) -> str:
    U = UI_IT
    k = "sel." + i["id"]
    parts = []
    for lab, a, den, tk, dk, den2 in (("sel_c_rec", i["records"], i["den_records"], "records", "den_records", None), ("sel_c_fam", i["families"], i["den_families"], "families", "den_families", None)):
        if a is None:
            continue
        s = f'<span class="sel-v">{E(U[lab])} {numit(k + "." + tk, a)}'
        if den:
            s += " " + pct_span(k + "." + tk + ".pct", a, den, U["sel_of"] + " ")
        if tk == "families" and i.get("den2_fam"):
            s += " " + pct_span(k + ".families.pct_catalogue", a, i["den2_fam"], U["sel_of"] + " ")
        if i.get("testable_rec") and tk == "records":
            s += " " + pct_span(k + ".records.pct_testable", a, i["testable_rec"], U["sel_testable"] + " ")
        if i.get("testable_fam") and tk == "families":
            s += " " + pct_span(k + ".families.pct_testable", a, i["testable_fam"], U["sel_testable"] + " ")
        parts.append(s + "</span>")
    return " ".join(parts)


def render_selection(P: dict) -> str:
    """Selection funnel from measured units (usable-compound census, recomputed from the per-record flags at build time): every indicator carries its unit, its denominator, its overlaps and its unknown or excluded share."""
    U = UI_IT
    S = P["cur"]["selection"]
    cat = next(i for st in S["steps"] for i in st["indicators"] if i["id"] == "catalogued")
    ev = {i["id"]: i for st in S["steps"] for i in st["indicators"]}
    steps = []
    for st in S["steps"]:
        items = []
        for i in st["indicators"]:
            unit = U["sel_u_" + i["unit"]]
            if i["unit"] in ("cards", "needs", "r", "rows") and i.get("records") is not None:   # single-number indicators print the number once
                vals = f'<span class="sel-v">{numit("sel." + i["id"] + ".value", i["records"])}' + (" " + pct_span("sel." + i["id"] + ".pct", i["records"], i["den_records"], U["sel_of"] + " ") if i.get("den_records") else "") + "</span>"
            else:
                vals = sel_values(i)
            extra = ""
            if i.get("breakdown"):
                extra = " " + "; ".join(f'{E(U["sel_b_" + b["id"]])} {numit("sel.msig_unknown.reason." + b["id"], b["records"])}' for b in i["breakdown"]) + "."
            items.append(f'<div class="sel-ind" data-ind="{E(i["id"])}"><div class="sel-lab"><b>{E(U["sel_i_" + i["id"]])}</b> <span class="mut">[{E(unit)}]</span></div><div class="sel-vals">{vals}</div>'
                         f'<p class="mini sel-note">{E(U["sel_n_" + i["id"]])}{extra}</p></div>')
        steps.append(f'<div class="sel-step" data-step="{E(st["id"])}"><h3>{E(U["sel_s_" + st["id"]])}</h3>{"".join(items)}</div>')
    ov = S["overlap"]
    ovk = (("both", "sel_ov_both"), ("only_net_usable", "sel_ov_net"), ("only_sig_neural", "sel_ov_sig"), ("neither", "sel_ov_none"), ("denominator", "sel_ov_den"))
    rows = "".join(
        f'<tr><th scope="row">{E(U["sel_u_" + u[0]])}</th>' + "".join(f'<td data-label="{E(U[lab])}">{numit("sel.overlap." + u + "." + k, ov[u][k])}</td>' for k, lab in ovk) + "</tr>"
        for u in ("records", "families"))
    K = S["kinds"]
    kinds = (f'<ul class="sel-kinds"><li><b>{E(U["sel_k_l1"])}:</b> {numit("sel.kinds.L1", K["L1_documented"])}</li>'
             f'<li><b>{E(U["sel_k_l2"])}:</b> {numit("sel.kinds.L2.coherent", K["L2"]["coherent"])} / {numit("sel.kinds.L2.opposed", K["L2"]["opposed"])} / {numit("sel.kinds.L2.unresolved", K["L2"]["direction_unresolved"])}</li>'
             f'<li><b>{E(U["sel_k_l3"])}:</b> {numit("sel.kinds.L3", K["L3"])} ({numit("sel.kinds.L3w", K["L3_wwox_system"])})</li>'
             f'<li><b>{E(U["sel_k_l4"])}:</b> {numit("sel.kinds.L4", K["L4"])} ({numit("sel.kinds.L4e", K["L4_experimental"])})</li></ul>')
    pv = (f'<div class="sel-pv"><div class="sel-pv-b"><h4>{E(U["sel_pv_present_h"])}</h4><p><b>{numit("sel.pv.records", cat["records"])}</b> record · <b>{numit("sel.pv.families", cat["families"])}</b> {E(U["sel_u_f"])}: {E(U["sel_pv_present"])}</p></div>'
          f'<div class="sel-pv-b"><h4>{E(U["sel_pv_eval_h"])}</h4><ul><li><b>{numit("sel.pv.eval_methods", ev["eval_methods"]["records"])}</b> {E(U["sel_pv_eval0"])}</li>'
          f'<li><b>{numit("sel.pv.eval_p3", ev["eval_p3"]["families"])}</b> {E(U["sel_pv_eval1"])}</li><li><b>{numit("sel.pv.eval_wwox", ev["eval_wwox_readout"]["records"])}</b> {E(U["sel_pv_eval2"])}</li></ul></div></div>')
    return (f'<section id="selection" aria-labelledby="h-sel"><h2 id="h-sel">{E(U["sel_h"])}</h2><p class="lead">{E(U["sel_lead"])}</p><p class="mini mut">{E(U["sel_units"])}</p>'
            f'<h3>{E(U["sel_pv_h"])}</h3>{pv}{"".join(steps)}'
            f'<h3>{E(U["sel_ov_h"])}</h3><div class="scrollx"><table class="tbl stk"><thead><tr><th></th><th>{E(U["sel_ov_both"])}</th><th>{E(U["sel_ov_net"])}</th><th>{E(U["sel_ov_sig"])}</th><th>{E(U["sel_ov_none"])}</th><th>{E(U["sel_ov_den"])}</th></tr></thead><tbody>{rows}</tbody></table></div>'
            f'<p class="mini mut">{E(U["sel_ov_note"])}</p><h3>{E(U["sel_k_h"])}</h3><p class="mini mut">{E(U["sel_k_note"])}</p>{kinds}'
            f'<div class="note"><p>{E(U["sel_warn_share"])}</p><p><b>{E(U["sel_warn_prob"])}</b></p></div>'
            f'<p class="noprint"><a class="btnlink" href="#section=selection">{E(U["sec_print"])}</a></p></section>')


def render_hypotheses(P: dict) -> str:
    """Nine hypotheses compared; priority, model position and observed evidence are separate blocks, and favourable, contrary and missing evidence are separate labelled fields."""
    U = UI_IT
    cur = P["cur"]
    cm = {c["id"]: c for c in cur["cands"]}
    arts = []
    for h in cur["hypotheses"]:
        prio = "".join(
            f'<div class="hyp-card"><b>{E(cm[c]["short"])}</b> <span class="mut">{E(c)}</span> ' + (" ".join(f'{pos_chip(x["group"])} <span class="mini mut">{E(U["hyp_prio_on"])} {E(NEED_IT.get(x["need"], x["need"]))}</span>' for x in h["positions"][c]) or f'<span class="mut">{E(U["cd_no_need"])}</span>') + "</div>"
            for c in h["cards"])
        plan = "".join(f'<div class="mini"><b>{E(U["hyp_plan"])}:</b> <span class="chip wo-k">{E(w["kind"])}</span> <span class="mut">{E(NEED_IT.get(w["need"], w["need"]))}</span></div>' for w in h["work_order"]) or f'<div class="mini mut">{E(U["hyp_none_plan"])}</div>'
        reasons = "".join(f'<li>{E(U["hyp_r_" + r])}</li>' for r in h["model_reasons"])
        axis = f'<p class="mini"><span class="chip model-ok">{E(U["hyp_axis"])}</span> {E(U["hyp_axis_note"])}</p>' if h["model_axis"] else ""
        usable = f'<p class="mini">{E(U["hyp_usable"])}</p>' if h["model_usable"] else ""
        arts.append(
            f'<article class="hyp" id="hyp-{E(h["id"])}" data-hyp="{E(h["id"])}" data-model="{E(h["model"])}" data-axis="{1 if h["model_axis"] else 0}"><h3>{E(h["title"])} <span class="mut">{E(h["id"])}</span></h3>'
            f'<div class="hyp-three"><div class="hyp-b hyp-prio"><h4>{E(U["hyp_prio"])}</h4>{prio}{plan}</div>'
            f'<div class="hyp-b hyp-model"><h4>{E(U["hyp_model"])}</h4><p><span class="chip model-na">{E(U["hyp_model_none"])}</span></p>{axis}<ul class="mini">{reasons}</ul>{usable}</div>'
            f'<div class="hyp-b hyp-obs"><h4>{E(U["hyp_obs"])}</h4><p class="mini">{E(h["observed"])}</p></div></div>'
            f'<details class="inl"><summary>{E(U["hyp_more"])}</summary><dl class="hyp-dl"><dt>{E(U["hyp_track"])}</dt><dd>{E(h["track"])}</dd><dt>{E(U["hyp_depth"])}</dt><dd>{E(h["depth"])}</dd>'
            f'<dt>{E(U["hyp_dem"])}</dt><dd>{E(h["demonstrated"])}</dd><dt>{E(U["hyp_opp"])}</dt><dd>{E(h["opposed"])}</dd><dt>{E(U["hyp_missing"])}</dt><dd>{E(h["missing"])}</dd>'
            f'<dt>{E(U["hyp_ext"])}</dt><dd>{E(h["external"])}</dd><dt>{E(U["hyp_next"])}</dt><dd>{E(h["next"])}</dd><dt>{E(U["hyp_status"])}</dt><dd>{E(h["status"])}</dd></dl></details></article>')
    return (f'<section id="hypotheses" aria-labelledby="h-hyp"><h2 id="h-hyp">{E(U["hyp_h"])}</h2><p class="lead">{E(U["hyp_lead"])}</p><p class="mini">{E(U["hyp_intro_model"])}</p><p class="mini">{E(U["hyp_key"])}</p><p class="mini mut">{E(U["hyp_note_en"])} <b>{E(U["sel_warn_prob"])}</b></p>'
            + "".join(arts) + f'<p class="noprint"><a class="btnlink" href="#section=hypotheses">{E(U["sec_print"])}</a></p></section>')


def render_predictive(P: dict) -> str:
    """Predictive test (compact) and context concordance (compact), each from measured files; numbers are formatted with the Italian decimal comma."""
    U = UI_IT
    cur = P["cur"]
    pr, cx = cur["predictive"], cur["contexts"]
    vrows = []
    for vi, v in enumerate(pr["verdicts"]):
        nums = "; ".join(f'{E(n["id"])} <b data-k="pred.v{vi}.{ni}" data-v="{n["value"]}">{E(dec_it(n["value"], n["digits"]))}</b>' for ni, n in enumerate(v["numbers"]))
        vrows.append(f'<tr data-verdict="{E(v["verdict"])}"><td data-label="{E(U["pred_c_cmp"])}">{E(v["comparison_it"])}</td><td data-label="{E(U["pred_c_verdict"])}"><span class="chip vd vd-{E(v["verdict"])}">{E(U["pred_v_" + v["verdict"]])}</span></td><td data-label="{E(U["pred_c_num"])}">{nums}</td><td class="mini" data-label="{E(U["pred_c_reopen"])}">{E(v["reopen_it"])}</td></tr>')
    meths = "".join(f'<li><b>{E(m["id"])}</b> {E(m["it"])}</li>' for m in pr["methods"])
    uni = pr["universe"]
    uni_txt = (f'<b data-k="pred.universe" data-v="{uni["families"]}">{E(fmt_it(uni["families"]))}</b> ' + E(U["pred_universe_txt"].format(s=fmt_it(uni["signatures"]), p=fmt_it(uni["pilot_families"]), c=fmt_it(uni["catalogue_families"]))))
    thr = E(U["pred_threshold_txt"].format(t=dec_it(pr["threshold"], 2), n=uni["families"], m=dec_it(pr["minimum_detectable_effect"], 3)))
    crow = []
    for r in cx["rows"]:
        lab = lambda k: E(U[k])
        crow.append(f'<tr data-q="{E(r["id"])}" data-verdict="{E(r["verdict"])}"><th scope="row">{E(r["quantity_it"])}<div class="mini mut">{E(r["id"])} · {E(r["note_it"])}</div></th>'
                    f'<td data-label="{lab("ctx_c_hi")}">{numit("ctx." + r["id"] + ".higher", r["higher"])}</td><td data-label="{lab("ctx_c_lo")}">{numit("ctx." + r["id"] + ".lower", r["lower"])}</td>'
                    f'<td data-label="{lab("ctx_c_ns")}">{numit("ctx." + r["id"] + ".other", r["other"])}</td><td data-label="{lab("ctx_c_unk")}">{numit("ctx." + r["id"] + ".unknown", r["unknown"])}</td>'
                    f'<td data-label="{lab("ctx_c_models")}">{numit("ctx." + r["id"] + ".models", r["models_resolved"])} / {numit("ctx." + r["id"] + ".measured", r["models_measured"])}</td>'
                    f'<td data-label="{lab("ctx_c_verdict")}"><span class="chip vd vd-{E(r["verdict"])}">{E(U["ctx_v_" + r["verdict"]])}</span></td></tr>')
    heads = "".join(f"<th>{E(c)}</th>" for c in cx["context_ids"])
    wide = "".join(f'<tr><th scope="row">{E(r["quantity_it"])}<div class="mini mut">{E(r["id"])}</div></th>' + "".join(f"<td>{E(U['ctx_d_' + d])}</td>" for d in r["directions"]) + "</tr>" for r in cx["rows"])
    mod = "; ".join(f'{E(c)}: {E(cx["model_labels_it"][cx["models_of"][c]])}' for c in cx["context_ids"])
    facts = U["ctx_facts"].format(cells=f'<b data-k="ctx.cells" data-v="{cx["cells"]}">{fmt_it(cx["cells"])}</b>', contexts=f'<b data-k="ctx.contexts" data-v="{cx["contexts"]}">{cx["contexts"]}</b>',
                                  quantities=f'<b data-k="ctx.quantities" data-v="{cx["quantities"]}">{cx["quantities"]}</b>', measured=f'<b data-k="ctx.measured" data-v="{cx["measured"]}">{cx["measured"]}</b>',
                                  unknown=f'<b data-k="ctx.unknown" data-v="{cx["unknown"]}">{cx["unknown"]}</b>', models=f'<b data-k="ctx.models" data-v="{cx["models"]}">{cx["models"]}</b>')
    return (f'<section id="predictive" aria-labelledby="h-pred"><h2 id="h-pred">{E(U["pred_h"])}</h2><p class="note"><b>{E(U["pred_label"])}</b></p>'
            f'<dl class="pred-dl"><dt>{E(U["pred_q"])}</dt><dd>{E(pr["question_it"])}</dd><dt>{E(U["pred_methods"])}</dt><dd><ul class="mini">{meths}</ul></dd>'
            f'<dt>{E(U["pred_prereg"])}</dt><dd>{E(U["pred_prereg_txt"])}</dd><dt>{E(U["pred_universe"])}</dt><dd>{uni_txt}</dd><dt>{E(U["pred_threshold"])}</dt><dd>{thr}</dd></dl>'
            f'<h3>{E(U["pred_verdict_h"])}</h3><div class="scrollx"><table class="tbl pred-t stk"><thead><tr><th>{E(U["pred_c_cmp"])}</th><th>{E(U["pred_c_verdict"])}</th><th>{E(U["pred_c_num"])}</th><th>{E(U["pred_c_reopen"])}</th></tr></thead><tbody>{"".join(vrows)}</tbody></table></div>'
            f'<h3>{E(U["pred_limits_h"])}</h3><ul class="mini">{"".join("<li>" + E(x) + "</li>" for x in pr["limits_it"])}</ul><p class="mini"><b>{E(U["sel_warn_prob"])}</b></p>'
            f'<h2 id="contexts">{E(U["ctx_h"])}</h2><p class="lead">{E(U["ctx_lead"])}</p><p>{facts}</p><div class="note"><b>{E(U["ctx_no_subgroup"])}</b></div><p class="mini mut">{E(U["ctx_def"])}</p>'
            f'<div class="scrollx"><table class="tbl ctx-t stk"><thead><tr><th>{E(U["ctx_c_q"])}</th><th>{E(U["ctx_c_hi"])}</th><th>{E(U["ctx_c_lo"])}</th><th>{E(U["ctx_c_ns"])}</th><th>{E(U["ctx_c_unk"])}</th><th>{E(U["ctx_c_models"])}</th><th>{E(U["ctx_c_verdict"])}</th></tr></thead><tbody>{"".join(crow)}</tbody></table></div>'
            f'<details class="inl"><summary>{E(U["ctx_full"])}</summary><p class="mini mut">{E(U["ctx_models_h"])}: {mod}</p><div class="scrollx"><table class="tbl"><thead><tr><th></th>{heads}</tr></thead><tbody>{wide}</tbody></table></div></details>'
            f'<p class="noprint"><a class="btnlink" href="#section=predictive">{E(U["sec_print"])}</a></p></section>')


def NM_GOAL(needs: list, nid: str):
    return next((n["goal"] for n in needs if n["id"] == nid), None)


def render_charts(P: dict) -> str:
    """The five graphics, server-rendered (inline HTML and CSS, no script). Each carries its unit, its denominator and how to read it."""
    U, cur, f, a = UI_IT, P["cur"], P["funnel"], P["access"]
    needs, cands = cur["needs"], cur["cands"]
    out = [f'<section id="charts" aria-labelledby="h-ch"><h2 id="h-ch">{E(U["ch_h"])}</h2><p class="mini mut">{E(U["ch_note"])}</p>']
    # 1. funnel
    fam, rec = f["families"], f["records"]
    rows = [("records", U["g1_records"], rec, U["g1_u_records"], 100.0, f'data-step="records"', None),
            ("families", U["g1_families"], fam, U["g1_u_families"], 100.0, 'data-step="families"', None),
            ("families_with_link", U["g1_fam_link"], f["families_with_link"], U["g1_u_families"], pct(f["families_with_link"], fam), 'data-step="families_with_link"', U["g1_share"].format(den=fmt_it(fam))),
            ("families_with_action", U["g1_fam_act"], f["families_with_action"], U["g1_u_families"], pct(f["families_with_action"], fam), 'data-step="families_with_action"', U["g1_share"].format(den=fmt_it(fam)))]
    h = [f'<div class="chart" id="g1"><h3>{E(U["g1_h"])}</h3><p class="mini mut">{E(U["g1_how"])}</p><ol class="fun">']
    for key, lab, val, unit, p, attr, sharetxt in rows:
        share = f'<span class="pc">{pct_it(p)} <span class="mini mut">{E(sharetxt)}</span></span>' if sharetxt else ""
        h.append(f'<li {attr}><div class="fl">{E(lab)}</div><div class="fv">{numit("funnel." + key, val)} <span class="unit">{E(unit)}</span>{share}</div>{bar(p)}</li>')
    h.append(f'<li data-step="cards"><div class="fl">{E(U["g1_cards"])}</div><div class="fv">{numit("cur.cards", len(cands))} <span class="unit">{E(U["g1_u_cards"])}</span></div><p class="mini mut">{E(U["g1_cards_note"])}</p></li></ol>')
    h.append(f'<p class="mini">{E(U["g1_rec_sub"].format(link=fmt_it(f["records_with_link"]), act=fmt_it(f["records_with_action"])))}</p>'
             f'<span hidden data-k="funnel.records_with_link" data-v="{f["records_with_link"]}"></span><span hidden data-k="funnel.records_with_action" data-v="{f["records_with_action"]}"></span>'
             f'<p class="mini mut">{E(U["g1_note"])}</p></div>')
    out.append("".join(h))
    # 2. access
    tot = a["total"]
    order = ["supplement", "OTC", "prescription", "experimental", "unknown/unverified"]
    g2 = [f'<div class="chart" id="g2"><h3>{E(U["g2_h"])}</h3><p class="mini mut">{E(U["g2_how"].format(den=fmt_it(tot)))}</p><ul class="acc">']
    for k in order + sorted(set(a["overlapping"]) - set(order)):
        if k in a["overlapping"]:
            v = a["overlapping"][k]
            g2.append(f'<li data-access="{E(k)}"><span class="al">{E(U.get("acc_" + k, k))}</span><span class="av">{numit("access." + k, v)} {E(U["g2_unit"])} · {pct_it(pct(v, tot))} {E(U["g2_of"])} {fmt_it(tot)}</span>{bar(pct(v, tot))}</li>')
    g2.append(f'</ul><p class="mini">{numit("access.unknown", a["unknown"])} {E(U["g2_of"])} {fmt_it(tot)} {E(U["g2_unit"])} ({pct_it(pct(a["unknown"], tot))}) {E(U["g2_unknown"])}.</p><p class="mini mut">{E(U["g2_note"])}</p></div>')
    out.append("".join(g2))
    # 3. matrix per thread
    g3 = [f'<div class="chart" id="g3"><h3>{E(U["g3_h"])}</h3><p class="mini mut">{E(U["g3_how"])}</p>']
    g3.append('<p class="mxleg">' + "".join(f'{pos_chip(i, long=True)} ' for i in ("F1", "F2", "F3", "C1", "C2", "C3", "P1", "P2", "P3")) + '</p>')
    for t in cur["threads"]:
        nm = THREAD_IT.get(t["id"], (t["name"], ""))[0]
        v = thread_view(cur, t)
        cs = sorted({c["id"] for c, _, _ in v["links"]}, key=lambda i: v["cmap"][i]["short"].lower())
        if not cs:
            continue
        g3.append(f'<h4>{E(nm)}</h4><div class="mxwrap"><table class="mx stack"><thead><tr><th scope="col">{E(U["g3_cand"])}</th>' + "".join(f'<th scope="col">{E(NEED_IT.get(n["id"], n["short"]))}</th>' for n in v["needs"]) + '</tr></thead><tbody>')
        for i in cs:
            c = v["cmap"][i]
            g3.append(f'<tr><th scope="row">{E(c["short"])}</th>')
            for n in v["needs"]:
                l = c["links"].get(n["id"])
                lab = NEED_IT.get(n["id"], n["short"])
                if l:
                    g3.append(f'<td data-label="{E(lab)}">{pos_chip(l["group"])}<span class="mxt">{E(U["g3_cell_" + l["group"]])}</span></td>')
                else:
                    g3.append(f'<td class="empty" data-label="{E(lab)}"><span aria-label="{E(U["g3_empty"])}">·</span></td>')
            g3.append('</tr>')
        g3.append('</tbody></table></div>')
    g3.append('</div>')
    out.append("".join(g3))
    # 4. targets <-> candidates (catalogue action rows attached to cards)
    tg: dict[str, dict] = {}
    for c in cands:
        for x in c["actions"]:
            e = tg.setdefault(str(x["target"]), {"c": {}, "n": set()})
            e["c"].setdefault(c["id"], set()).add((x["action"], x["cons"]))
            e["n"].add(x["need"])
    g4 = [f'<div class="chart" id="g4"><h3>{E(U["g4_h"])}</h3><p class="mini mut">{E(U["g4_how"])}</p>']
    if tg:
        g4.append(f'<div class="bip"><div class="bh"><span>{E(U["g4_target"])}</span><span>{E(U["g4_cands"])}</span></div>')
        cmap = {c["id"]: c for c in cands}
        nmap = {n["id"]: n for n in needs}
        for t_, e in sorted(tg.items()):
            cl = []
            for cid, acts in sorted(e["c"].items(), key=lambda kv: cmap[kv[0]]["short"].lower()):
                for act, cons in sorted(acts):
                    opp = "oppos" in str(cons)
                    cl.append(f'<span class="bc{" opp" if opp else ""}">{E(cmap[cid]["short"])}: {E(U.get("act_" + str(act), str(act)))} <span class="mini">({E(U.get("cons_" + str(cons), str(cons).replace("_", " ")))})</span></span>')
            g4.append(f'<div class="br"><div class="bt"><b>{E(t_)}</b><div class="mini mut">{E(U["g4_needs"])}: ' + E("; ".join(NEED_IT.get(n, nmap[n]["short"] if n in nmap else n) for n in sorted(e["n"]))) + f'</div></div><div class="bl">{"".join(cl)}</div></div>')
        g4.append('</div>')
    else:
        g4.append(f'<p class="state-none">{E(U["g4_none_share"] if P["source"] == "shareable" else U["g4_none"])}</p>')
    g4.append(f'<p class="mini mut">{E(U["g4_note"])}</p></div>')
    out.append("".join(g4))
    # 5. coverage and gaps
    g5 = [f'<div class="chart" id="g5"><h3>{E(U["g5_h"])}</h3><p class="mini mut">{E(U["g5_how"])}</p><div class="mxwrap"><table class="mx stack cov"><thead><tr><th scope="col">{E(U["g5_need"])}</th><th scope="col">{E(U["g5_c1"])}</th><th scope="col">{E(U["g5_c2"])}</th><th scope="col">{E(U["g5_c3"])}</th><th scope="col">{E(U["g5_c4"])}</th></tr></thead><tbody>']
    cmap = {c["id"]: c for c in cands}
    for t in cur["threads"]:
        nm = THREAD_IT.get(t["id"], (t["name"], ""))[0]
        g5.append(f'<tr class="grow"><th colspan="5" scope="colgroup">{E(nm)}</th></tr>')
        for n in needs:
            if n["id"] not in t["needs"]:
                continue
            ncs = [cmap[i] for i in n["cards"] if i in cmap]
            with_res = sum(1 for c in ncs if c["links"].get(n["id"], {}).get("result", "none") != "none")
            yn = lambda b: f'<span class="yn {"y" if b else "n"}">{E(U["g5_yes"] if b else U["g5_no"])}</span>'
            g5.append(f'<tr data-need="{E(n["id"])}"><th scope="row">{E(NEED_IT.get(n["id"], n["short"]))}</th>'
                      f'<td data-label="{E(U["g5_c1"])}">{yn(n["n_wwox_obs"] > 0)} <span class="mini">{n["n_wwox_obs"]} {E(U["g5_obs1"] if n["n_wwox_obs"] == 1 else U["g5_obs"])}</span></td>'
                      f'<td data-label="{E(U["g5_c2"])}"><span class="mini">{len(ncs)} {E(U["g5_cards1"] if len(ncs) == 1 else U["g5_cards"])}</span></td>'
                      f'<td data-label="{E(U["g5_c3"])}">{yn(with_res > 0)} <span class="mini">{with_res} {E(U["g5_cards1"] if with_res == 1 else U["g5_cards"])}</span></td>'
                      f'<td data-label="{E(U["g5_c4"])}">{yn(not n["no_l4"])}</td></tr>')
    g5.append(f'</tbody></table></div><p class="mini mut">{E(U["g5_note"])}</p></div>')
    out.append("".join(g5))
    out.append("</section>")
    return "".join(out)


def render_footer(P: dict) -> str:
    U = UI_IT
    ft = P["cur"]["footer"]
    h = [f'<h2>{E(U["ft_h"])} ({E(U["ft_build"])} {E(ft["source"])})</h2><p>{E(U["ft_note_share"] if ft["source"] == "shareable" else U["ft_note_full"])}</p><h3>{E(U["ft_embedded"])}</h3><ul>']
    for e in ft["embedded"]:
        u = f' <a href="{E(e["url"])}" rel="noopener noreferrer">{E(e["url"])}</a>' if e.get("url") else ""
        n = f' ({e["rows"]} {E(U["ft_rows"])})' if e.get("rows") else ""
        h.append(f'<li><b>{E(e["label"])}</b>{n}: {E(str(e.get("licence") or ""))}. {E(str(e.get("attribution") or ""))}{u}</li>')
    h.append("</ul>")
    if ft["counts_only"]:
        h.append(f'<h3>{E(U["ft_counts"])}</h3><ul>')
        for e in ft["counts_only"]:
            h.append(f'<li><b>{E(e["label"])}</b>: {E(e["terms"])}' + (f'; {E(U["ft_version"])} {E(str(e["version"]))}' if e.get("version") else "") + "</li>")
        h.append("</ul>")
    if ft.get("identifiers"):
        h.append(f'<h3>{E(U["ft_idsrc"])}</h3><ul>')
        for e in ft["identifiers"]:
            u = f' <a href="{E(e["url"])}" rel="noopener noreferrer">{E(e["url"])}</a>' if e.get("url") else ""
            h.append(f'<li><b>{E(e["label"])}</b>: {E(str(e.get("licence") or ""))}. {E(str(e.get("attribution") or ""))}{u}</li>')
        h.append("</ul>")
    if ft.get("class_b"):
        h.append(f'<h3>{E(U["ft_classb"])}</h3><p class="mini">{E(U["ft_classb_note"])}</p><ul>')
        for e in ft["class_b"]:
            h.append(f'<li><b>{E(e["label"])}</b>: {E(str(e.get("licence") or ""))}. {E(str(e.get("credit") or ""))}. {E(U["ft_classb_where"])} <code>{E(str(e.get("path") or ""))}</code></li>')
        h.append("</ul>")
    h.append(f'<p class="mini">{E(U["ft_ids"])}</p>')
    return "".join(h)


# ------------------------------------------------------------------ IT8 P9: provisional, explainable, updatable ranking of the interventions
RANK_DIR = "ranking_it8_p9_20261029"
RK_GROUP_IDS = ["G1", "G2a", "G2b", "G3", "G4a", "G4b", "G5", "GU"]
RK_CLASSES = ["ORD", "WEAK", "INSUFF", "EXCL"]
RK_VIEWS = ["general", "broad", "partial"]
RK_LINKS = ["effect_observed_in_wwox_system", "directionally_compatible_documented_action", "documented_association_target_listed", "other_disease_precedent_only", "card_inference_by_mechanism_no_catalogue_row"]
RK_EVQ = ["favourable_controlled", "favourable_thin", "favourable_thin_specificity_uncertain", "contested", "no_wwox_test_target_supported", "no_wwox_test_target_hypothesis", "weak_pertinence_or_outside_counter", "premise_missing"]


def rk_digest_ok(o) -> bool:
    return isinstance(o, dict) and o.get("summary", {}).get("schema") == "legend.wwox.ranking/1"


def validate_ranking(R: dict, cands: dict, need_ids: set) -> list[str]:
    """The page and the generated data must agree: every reference resolves and every headline count is recomputed from the units."""
    errs = []
    units = {u["id"]: u for u in R["units"]}
    if len(units) != len(R["units"]):
        errs.append("duplicate unit ids")
    seen = Counter(c for u in R["units"] for c in u["cards"])
    if set(seen) != set(cands) or any(n != 1 for n in seen.values()):
        errs.append(f"the units do not cover the cards exactly once: missing {sorted(set(cands) - set(seen))}, unknown {sorted(set(seen) - set(cands))}")
    for u in R["units"]:
        if u["class"] not in RK_CLASSES:
            errs.append(f"{u['id']}: unknown class {u['class']!r}")
        for obj, va in u["views"].items():
            if va.get("member") and va.get("group") not in RK_GROUP_IDS:
                errs.append(f"{u['id']}.{obj}: unknown group {va.get('group')!r}")
            if va.get("member") and va.get("lead_need") and va["lead_need"] not in need_ids:
                errs.append(f"{u['id']}.{obj}: need {va['lead_need']!r} does not exist")
            if va.get("member") and va.get("group") == "G1" and va.get("lead") != "F1":
                errs.append(f"{u['id']}.{obj}: G1 requires the F1 position")
        for p in u["pathways"]:
            if p["need"] not in need_ids:
                errs.append(f"{u['id']}: pathway need {p['need']!r} does not exist")
            if p["link_evidence"] not in RK_LINKS:
                errs.append(f"{u['id']}: unknown link evidence {p['link_evidence']!r}")
        # the group is a function of the card positions: recompute it from the page's own card data
        for c in u["cards"]:
            for nid, lk in (cands[c].get("links") or {}).items():
                got = next((p for p in u["pathways"] if p["need"] == nid), None)
                if got is None:
                    errs.append(f"{u['id']}: card {c} links {nid} but the unit has no pathway row")
    for view, s in R["selections"].items():
        for uid in s["top"]:
            if uid not in units:
                errs.append(f"selection {view}: unknown unit {uid}")
            elif s["groups"][uid] not in R["meta"]["selectable_groups"]:
                errs.append(f"selection {view}: {uid} stands in group {s['groups'][uid]}, which is not selectable")
        if len(s["top"]) > 10:
            errs.append(f"selection {view}: more than ten items")
        if set(s["top"]) & {a["id"] for a in s["apart"]}:
            errs.append(f"selection {view}: an item is both listed and apart")
    for r in R.get("uncarded") or []:
        if r["class"] not in RK_CLASSES or (r["related_unit"] and r["related_unit"] not in units):
            errs.append(f"uncarded {r['item_id']}: invalid class or unit")
    n_rank = sum(1 for u in R["units"] if u["class"] != "EXCL")
    if R["meta"]["units_ranked"] != n_rank:
        errs.append(f"units_ranked {R['meta']['units_ranked']} != recomputed {n_rank}")
    cls = Counter(u["class"] for u in R["units"])
    if {k: cls.get(k, 0) for k in RK_CLASSES} != R["meta"]["by_class"]:
        errs.append("by_class does not match the units")
    return errs


def build_ranking(dr: Path, cur: dict, source: str):
    """Projection of ranking_it8_p9_20261029/ranking.json into the page. Full edition: everything. Shareable edition: no catalogue member names, no status classes, no
    potency or exposure text from the pharmacological table, and only class-A access statements (openFDA NDC, MATRIX) per compound; the other access categories survive as counts."""
    p = dr / RANK_DIR / "ranking.json"
    if not p.exists():
        return None
    J = jload(p)
    if not rk_digest_ok(J):
        raise SystemExit(f"{RANK_DIR}/ranking.json has an unknown schema")
    full = source == "full"
    cands = {c["id"]: c for c in cur["cands"]}
    need_ids = {n["id"] for n in cur["needs"]}
    S = J["summary"]
    units = []
    for u in J["units"]:
        views = {}
        for obj, va in u["views"].items():
            if not va.get("member"):
                views[obj] = {"member": False}
                continue
            ev = va["evidence"]
            views[obj] = {"member": True, "declared": va["declared"], "group": va["group"], "lead": va.get("lead"), "lead_need": va.get("lead_need"), "positions": va["positions"],
                          "contested": bool(va.get("contested")), "counter_needs": va.get("counter_needs") or [], "evq": va["evidence_quality"], "group_reason": va["group_reason"],
                          "evidence": {k: ev.get(k) for k in ("in_wwox", "carrier_of_position", "id", "text", "scope", "species", "genotype", "depth", "pmids", "other_favourable_wwox_assertions")} | {"flags": (ev.get("flags") or [])[:8]},
                          "next": {k: va["next"].get(k) for k in ("kind", "question", "would_change", "feasibility", "need")}, "triggers": va["triggers"], "main_limit": va["main_limit"],
                          "lead_summary": va.get("lead_summary") or {}}
        comp = u["components"]
        ph = comp["P_pharmacology"]
        items = [i for i in u["access_items"] if full or i["licence_class"] == "A"]
        withheld = [i for i in u["access_items"] if not (full or i["licence_class"] == "A")]
        if full:
            acc_text = u["access"]
        elif items:
            acc_text = " | ".join(f"{i['member']}: {i['category']} ({i['jurisdiction']}; {i['source']}; {i['strength']}; {i['date']})" for i in items) + " -- descriptive listing evidence, not efficacy or safety"
            if withheld:
                acc_text += f" | {len(withheld)} further access statement(s) withheld in this edition (licence class B/C)"
        elif withheld:
            acc_text = f"{len(withheld)} access statement(s) withheld in this edition (licence class B/C); category counts only"
        else:
            acc_text = u["access"]
        pm = {"state": ph["state"], "record": ph["record"]}
        if full:
            pm.update({"potency_with_assay_context": ph["potency_with_assay_context"], "human_exposure": ph["human_exposure"], "brain_penetration": ph["brain_penetration"]})
        units.append({
            "id": u["unit_id"], "label": u["label"], "kind": u["kind"], "class": u["class"], "class_reason": u["class_reason"], "cards": u["cards"], "tracks": u["tracks"], "goals": u["declared_goals"],
            "depth": u["evaluation_depth"], "depth_text": u["evaluation_depth_text"], "views": views, "merge_reason": u["merge_reason"],
            "comp": {"W": comp["W_wwox_evidence"], "M": {"text": comp["M_mechanism"]["text"], "l2": comp["M_mechanism"]["l2"], "opposed_needs": comp["M_mechanism"]["opposed_needs"], "n_families": len(comp["M_mechanism"]["families"])},
                     "T": comp["T_transferability"], "P": pm, "X": comp["X_counter_evidence"], "U": comp["U_uncertainty"]},
            "access": acc_text, "access_cats": sorted({i["category"] for i in items}) if not full else u["access_categories"],
            "pathways": [{k: p_[k] for k in ("need", "thread", "objective", "need_direction", "position", "position_by_card", "same_need_conflict", "link_evidence", "opposed_action", "wwox_observations_on_need")} for p_ in u["pathways"]],
            "members": ([{"name": m["name"], "family": m["family_id"], "roles": m["roles"], "status": m["status_class"], "twins": m["name_twins_not_merged"]} for m in u["members"]] if full else len(u["members"])),
            "pmids": u["pmids"], "receipts": u["receipts_on_cited_pmids"], "model_exclusions": u["model_exclusions"], "comparison_record": u["comparison_record"],
            "depth_of_benefit_sought": u["depth_of_benefit_sought"],
        })
    inv = S["inventory"]
    hist = []
    ch = dr / RANK_DIR / "changes.tsv"
    if ch.exists():
        rows = read_tsv(ch)
        by = {}
        for r in rows:
            d = by.setdefault(r["snapshot"], {"snapshot": r["snapshot"], "n": 0, "reasons": Counter(), "kinds": Counter()})
            d["n"] += 1
            d["reasons"][r["reason_class"]] += 1
            d["kinds"][r["kind_of_change"]] += 1
        hist = [{"snapshot": k, "n": v["n"], "reasons": dict(sorted(v["reasons"].items())), "kinds": dict(sorted(v["kinds"].items()))} for k, v in sorted(by.items())]
    trig = read_tsv(dr / RANK_DIR / "triggers.tsv")
    R = {
        "meta": {"as_of": S["as_of"], "rules_version": S["rules_version"], "order_digest": S["order_digest"], "needs_total": S["needs_total"], "units_total": len(units),
                 "units_ranked": S["units"]["ranked_interventions"], "by_class": {k: S["units"]["by_class"][v] for k, v in {"ORD": "EVALUATED AND ORDERABLE", "WEAK": "EVALUATED WITH WEAK PERTINENCE OR COUNTER-EVIDENCE", "INSUFF": "STILL INSUFFICIENTLY EVALUATED", "EXCL": "EXCLUDED FROM A SPECIFIC COMPARISON WITH REASON"}.items()},
                 "selectable_groups": [g for g in RK_GROUP_IDS if g in ("G1", "G2a", "G2b", "G3", "G4a")], "groups_en": {g: S["groups"][g] for g in RK_GROUP_IDS}, "classes_en": S["classes"],
                 "reason_classes": S["reason_classes"], "non_assessment_changes": S["non_assessment_changes"], "p3_note": S["p3_note"], "plain_statement": S["plain_statement"]},
        "units": units,
        "selections": {v: {"top": s["top"], "groups": s["top_groups"], "objective": s["top_objective"], "apart": [{"id": a["unit_id"], "group": a["group"], "objective": a["objective"]} for a in s["not_in_top_listed_apart"]], "n_listed": s["n_listed"], "cut_rule": s["cut_rule"]}
                       for v, s in S["selections"].items()},
        "inventory": {k: inv[k] for k in ("families", "records", "by_class", "by_first_order", "need_linked_families_q1_q2_q3", "need_linked_families_plus_units", "distinct_display_names_total", "distinct_display_names_in_q1",
                                          "q1_with_opposed_action_elsewhere", "mnet_usable_families", "msig_neural_families", "need_linked_by_access_category", "all_families_by_access_category")},
        "queue": {"compounds": S["deepening_queue_compounds"]},
        "uncarded": [({k: r[k] for k in ("item_id", "item", "kind", "class", "evaluation_depth", "provenance", "related_unit", "reason", "what_would_reopen", "source_pointers")} if full else
                      {"item_id": r["item_id"], "item": "item without a card (name withheld in this edition)", "kind": r["kind"], "class": r["class"], "evaluation_depth": r["evaluation_depth"], "provenance": r["provenance"],
                       "related_unit": r["related_unit"], "reason": "withheld in this edition (names and reasons of items without a card are in the full edition)", "what_would_reopen": "", "source_pointers": ""}) for r in J.get("uncarded") or []],
        "triggers": [{k: t[k] for k in ("trigger", "what", "detected_by", "re_evaluates", "reason_class_when_order_moves")} for t in trig],
        "history": hist,
    }
    errs = validate_ranking(R, cands, need_ids)
    if errs:
        raise SystemExit("the ranking is inconsistent with the cards and needs:\n  " + "\n  ".join(errs))
    return R


UI_IT8 = {
    "nav_ranking": "Graduatoria",
    "rk_h": "Graduatoria provvisoria degli interventi per priorità di verifica",
    "rk_lead": "Un primo ordine, spiegabile e aggiornabile, degli interventi che LEGEND ha individuato finora. Esprime la promessa scientifica e la priorità del prossimo studio. Non è una previsione validata di beneficio clinico, non è una probabilità di successo, non è una raccomandazione terapeutica e non è consiglio medico.",
    "rk_not_h": "Che cosa non è",
    "rk_not_1": "Non è un punteggio: i gruppi sono ordinali, hanno componenti visibili e nessun peso nascosto. Nessuna percentuale va letta come probabilità di successo.",
    "rk_not_2": "Non è una classifica di sicurezza o di efficacia: l'accesso (prescrizione, banco, integratore) è solo una descrizione di fonte, con data e giurisdizione.",
    "rk_not_3": "Un intervento «ancora da valutare» non è «poco promettente»: non sta in fondo, sta in un gruppo a parte con il dato mancante nominato.",
    "rk_not_4": "L'evidenza di altre malattie sostiene un meccanismo o un esperimento, mai un risultato in WWOX. La stessa evidenza non è contata più volte (preprint, articolo, banca dati, articoli che la citano).",
    "rk_how_h": "Come leggerla",
    "rk_how_1": "Il gruppo (G1…GU) dice quanto è forte oggi il motivo per studiare ancora l'intervento. Dentro un gruppo c'è un pareggio: l'ordine alfabetico non significa nulla.",
    "rk_how_2": "Tre viste: generale, recupero ampio e duraturo, beneficio parziale o ponte. Lo stesso intervento può stare in gruppi diversi perché ogni vista usa solo i bisogni del proprio obiettivo; un risultato forte sui sintomi non cancella l'interesse per un'ipotesi di recupero ampio, e viceversa.",
    "rk_how_3": "Track A/B (dipendenza dalla variante o dalla lesione) è un campo separato dal gruppo: profondità del beneficio e applicabilità genetica sono dimensioni diverse.",
    "rk_how_4": "Un dato assente è «sconosciuto», non zero. Ogni conteggio ha il suo denominatore e non è una quota di malattia trattata; collegare più bisogni non fa salire il gruppo.",
    "rk_groups_h": "Gruppi di priorità",
    "rk_g_G1": "G1 · Caso più forte oggi, specifico per WWOX", "rk_g_G2a": "G2a · Favorevole ma sottile, esito WWOX con limiti di lettura o disegno",
    "rk_g_G2b": "G2b · Favorevole ma sottile, specificità incerta", "rk_g_G3": "G3 · Evidenza WWOX contesa o solo nulla",
    "rk_g_G4a": "G4a · Ipotesi dal bersaglio, azione coerente documentata", "rk_g_G4b": "G4b · Ipotesi dal bersaglio, direzione non stabilita",
    "rk_g_G5": "G5 · Pertinenza debole o controevidenza fuori da WWOX", "rk_g_GU": "GU · Non ancora ordinabile: premessa mancante",
    "rk_gp_G1": "Un risultato favorevole in un sistema WWOX, letto contro un gruppo non trattato dello stesso genotipo, senza flag di limite e senza risultati nulli o sfavorevoli accanto (posizione F1: un filtro di qualità di lettura, non una misura dell'effetto).",
    "rk_gp_G2a": "Un risultato favorevole in un sistema WWOX con soli limiti di lettura o di disegno (non controllato, grafico, un solo esperimento), senza risultati nulli accanto (posizione F2).",
    "rk_gp_G2b": "Come G2a, ma l'effetto compare anche nel wild type oppure è stato ottenuto con un composto-strumento che non è un farmaco candidato.",
    "rk_gp_G3": "Risultati favorevoli e nulli o sfavorevoli in WWOX uno accanto all'altro, oppure solo un risultato nullo: lo studio serve a capire quale regga (posizioni C2, C1).",
    "rk_gp_G4a": "Nessun test dell'intervento in WWOX; sostegno favorevole fuori da WWOX; il bisogno ha osservazioni in WWOX; è documentata un'azione coerente con la direzione del bisogno (posizione F3).",
    "rk_gp_G4b": "Come G4a ma senza un'azione coerente documentata: direzione incerta, azione irrisolta o nessuna identità in catalogo (posizione F3).",
    "rk_gp_G5": "Nessun risultato con segno in WWOX, e un segnale di danno o nullo da fuori WWOX senza nulla di favorevole accanto, oppure un collegamento solo per meccanismo (posizioni C3, P3).",
    "rk_gp_GU": "Un'astensione: manca un dato prima di poter progettare un test, o nessun bisogno collegato di questo obiettivo ha una posizione. Non è un giudizio di scarsa promessa.",
    "rk_sel_note": "Una selezione elenca al massimo dieci interventi dei gruppi G1, G2a, G2b, G3 e G4a, solo quando la valutazione li sostiene; mai riempita per arrivare a dieci. I pareggi restano interi. G4b e i gruppi seguenti sono elencati a parte.",
    "rk_ctl_view": "Vista", "rk_v_general": "Generale (il gruppo migliore tra i due obiettivi)", "rk_v_broad": "Recupero ampio e duraturo", "rk_v_partial": "Beneficio parziale o ponte",
    "rk_f_class": "Classe", "rk_f_group": "Gruppo", "rk_f_track": "Track", "rk_f_need": "Bisogno / via", "rk_f_access": "Categoria di accesso", "rk_f_evq": "Qualità dell'evidenza in WWOX", "rk_f_q": "Cerca", "rk_f_any": "tutti",
    "rk_f_q_ph": "nome, scheda, bisogno",
    "rk_btn_tsv": "Scarica TSV (righe visibili)", "rk_btn_json": "Scarica JSON (elenco completo)", "rk_btn_print1": "Stampa una pagina (A4)", "rk_btn_printall": "Stampa tutta la sezione", "rk_btn_reset": "Azzera i filtri",
    "rk_count": "{n} di {m} interventi", "rk_f_noscope": "(nessuno)",
    "rk_top_h": "Selezione per la vista scelta", "rk_top_none": "Nessun intervento di questa vista sta in un gruppo selezionabile.", "rk_apart_h": "Elencati a parte (non sono «in fondo»)", "rk_apart_note": "Gruppo e motivo sono nella tabella completa; un gruppo a parte non è un giudizio di scarsa promessa.",
    "rk_i_group": "Gruppo", "rk_i_obj": "Obiettivo di ricerca", "rk_i_track": "Applicabilità (Track)", "rk_i_access": "Accesso (descrittivo: non efficacia né sicurezza)", "rk_i_context": "Contesto",
    "rk_i_reason": "Motivo principale", "rk_i_evid": "Migliore evidenza pertinente", "rk_i_limit": "Limite principale", "rk_i_paths": "Bisogni e vie", "rk_i_next": "Prossimo esperimento o controllo utile",
    "rk_i_rise": "Potrebbe salire se", "rk_i_fall": "Potrebbe scendere se", "rk_i_leave": "Potrebbe uscire dalla selezione se", "rk_i_src": "Fonti", "rk_i_date": "Valutato il", "rk_i_depth": "Profondità di valutazione",
    "rk_i_counter": "Controevidenza su altri bisogni di questo obiettivo", "rk_i_also": "Nell'altro obiettivo", "rk_i_feas": "Fattibilità del prossimo passo (separata dalla promessa biologica)", "rk_i_class": "Classe",
    "rk_pos_on": "posizione", "rk_none": "nessuna", "rk_unknown": "sconosciuto", "rk_not_member": "non è tra gli interventi di questo obiettivo",
    "rk_t_h": "Elenco completo", "rk_t_note": "Tutti gli interventi, anche quelli non ordinabili: nessuno è omesso. Il gruppo di ogni vista è un risultato della regola, non una scelta a mano.",
    "rk_t_unit": "Intervento", "rk_t_class": "Classe", "rk_t_gen": "Generale", "rk_t_broad": "Recupero ampio", "rk_t_part": "Parziale o ponte", "rk_t_lead": "Posizione guida", "rk_t_evq": "Evidenza in WWOX", "rk_t_ctr": "Controevidenza",
    "rk_t_acc": "Accesso", "rk_t_depth": "Profondità", "rk_t_track": "Track", "rk_t_cards": "Schede", "rk_yes": "sì", "rk_no": "no",
    "rk_c_h": "Componenti: le stesse dimensioni del modulo, senza punteggio", "rk_c_note": "Evidenza WWOX, coerenza meccanicistica, trasferibilità, farmacologia, controevidenza, incertezza. Sono descrizioni, non pesi. La fattibilità è separata.",
    "rk_c_W": "Evidenza in WWOX", "rk_c_M": "Coerenza meccanicistica", "rk_c_T": "Trasferibilità", "rk_c_P": "Farmacologia", "rk_c_X": "Controevidenza", "rk_c_U": "Incertezza: misurato, ipotizzato, sconosciuto",
    "rk_c_rep": "Replica", "rk_c_ex": "Esclusioni dai confronti", "rk_c_sum": "Componenti, bisogni e vie", "rk_c_merge": "Perché è una sola voce", "rk_c_mem": "Composti in catalogo (uniti per famiglia; gemelli per nome non uniti)",
    "rk_c_members_n": "famiglie di catalogo collegate",
    "rk_c_pot": "Potenza nel contesto del saggio", "rk_c_exp": "Esposizione umana", "rk_c_brain": "Penetrazione nel cervello", "rk_c_expl": "Informazione esplorativa IT7 (non guida la graduatoria)",
    "rk_x_w": "asserzioni nulle, dannose o miste in sistemi WWOX", "rk_x_o": "asserzioni nulle o dannose fuori da WWOX", "rk_x_n": "voci di controevidenza a livello di bisogno (del bisogno, non dell'intervento)", "rk_x_opp": "bisogni con azione documentata opposta",
    "rk_p_h": "Bisogni e vie coinvolte", "rk_p_need": "Bisogno", "rk_p_thread": "Filone", "rk_p_obj": "Obiettivo", "rk_p_pos": "Posizione", "rk_p_link": "Tipo di legame", "rk_p_opp": "Azione opposta",
    "rk_p_den": "{n} bisogni collegati su {m}: un conteggio di legami, non una quota di malattia trattata; non fa salire il gruppo.",
    "rk_p_comp": "Previsione computazionale: nessuna per questo intervento. Il confronto pilota IT7 era esplorativo, ha escluso di proposito le schede curate e non può guidare la graduatoria da solo.",
    "rk_p_shared": "Bisogni condivisi con altri interventi", "rk_p_conflict": "due schede dello stesso intervento hanno posizioni diverse su questo bisogno; resta la posizione che non nasconde la controevidenza",
    "rk_le_effect_observed_in_wwox_system": "effetto osservato nel sistema pertinente", "rk_le_directionally_compatible_documented_action": "azione documentata compatibile con la direzione",
    "rk_le_documented_association_target_listed": "associazione documentata (bersaglio elencato)", "rk_le_other_disease_precedent_only": "solo precedente in un'altra malattia",
    "rk_le_card_inference_by_mechanism_no_catalogue_row": "inferenza della scheda per meccanismo, nessuna riga di catalogo",
    "rk_evq_favourable_controlled": "favorevole, controllata", "rk_evq_favourable_thin": "favorevole, sottile", "rk_evq_favourable_thin_specificity_uncertain": "favorevole, sottile, specificità incerta",
    "rk_evq_contested": "contesa", "rk_evq_no_wwox_test_target_supported": "nessun test in WWOX, bersaglio sostenuto", "rk_evq_no_wwox_test_target_hypothesis": "nessun test in WWOX, ipotesi dal bersaglio",
    "rk_evq_weak_pertinence_or_outside_counter": "pertinenza debole o controevidenza esterna", "rk_evq_premise_missing": "premessa mancante",
    "rk_cl_ORD": "VALUTATO E ORDINABILE", "rk_cl_WEAK": "VALUTATO CON PERTINENZA DEBOLE O CONTROEVIDENZA", "rk_cl_INSUFF": "ANCORA INSUFFICIENTEMENTE VALUTATO", "rk_cl_EXCL": "ESCLUSO DA UN CONFRONTO SPECIFICO, CON MOTIVO",
    "rk_cl_ORD_t": "almeno un bisogno collegato ha una posizione favorevole (F1, F2 o F3)", "rk_cl_WEAK_t": "valutato a livello di scheda ma ogni posizione è controevidenza o legame solo per meccanismo",
    "rk_cl_INSUFF_t": "ogni scheda è un'astensione o non indica un passo: manca un dato prima di un test; non è messo in fondo", "rk_cl_EXCL_t": "un asse di endpoint senza candidato: non è un intervento e non c'è nulla da ordinare",
    "rk_inv_h": "Inventario: dal catalogo agli interventi ordinati", "rk_inv_lead": "Si parte dal catalogo; un composto presente solo in una banca dati non ha, per definizione, una motivazione WWOX. Le famiglie uniscono sali e parenti per chiave strutturale; i gemelli per nome non sono uniti e non gonfiano le posizioni, perché ogni intervento è una sola voce.",
    "rk_inv_units": "Voci della graduatoria", "rk_inv_units_n": "{u} voci ({r} interventi ordinabili o no, {x} assi esclusi) da {c} schede su {c} (tutte coperte una sola volta)",
    "rk_inv_fam": "Catalogo: {r} record, {f} famiglie", "rk_inv_fam_note": "Le famiglie sono un limite superiore (lo stesso farmaco può comparire in due famiglie). Nessuna famiglia fuori dalle voci sopra ha una scheda: sono tutte «ancora insufficientemente valutate», con la profondità dichiarata.",
    "rk_inv_q": "Primo ordine delle famiglie del catalogo (per annotazioni esistenti; non è una graduatoria di promessa)",
    "rk_q_Q1": "Q1 · bersaglio elencato con azione coerente con la direzione, su un bisogno con direzione valutabile (profondità E1c)", "rk_q_Q2": "Q2 · bersaglio elencato su un bisogno di direzione incerta o azione irrisolta: solo lista di esplorazione (E1)",
    "rk_q_Q3": "Q3 · collegato solo da un membro di via, contato a parte (E1p)", "rk_q_Q4": "Q4 · azione documentata ma nessun bisogno del modulo collegato (E0a)", "rk_q_Q5": "Q5 · solo record di banca dati (E0)", "rk_q_UNIT": "membri di una voce già ordinata (E3)",
    "rk_inv_of": "di", "rk_inv_names": "{n} nomi distinti in Q1 (dopo raggruppamento per nome e sale, solo per la visualizzazione)", "rk_inv_access": "Categorie di accesso nelle famiglie collegate ai bisogni (si sovrappongono)",
    "rk_inv_opp": "famiglie Q1 con un'azione opposta su un altro bisogno", "rk_inv_queue": "Coda di approfondimento: {n} composti di Q1 su bisogni con osservazioni in WWOX, con stato approvato o accesso non ignoto. Se approfonditi entrerebbero come fratelli di una voce esistente, non come posizioni nuove.",
    "rk_inv_depth_h": "Profondità di valutazione dichiarata", "rk_inv_depth": "E4 scheda con letture oltre l'abstract · E3 scheda con asserzioni · E2 scheda di astensione · E1c/E1/E1p/E0a/E0 solo catalogo (dal più al meno collegato ai bisogni).",
    "rk_ev_h": "Evoluzione: come cambia e quando", "rk_ev_lead": "L'ordine si rigenera da un solo comando, senza nuovo scheduler: senza informazione nuova il risultato è identico byte per byte. Ogni versione è un'istantanea datata; quando un gruppo cambia si dichiara la ragione, e l'ingresso di nuovi composti o la risoluzione di un pareggio non sono scambiati per un cambio di giudizio.",
    "rk_ev_asof": "Dati al", "rk_ev_rules": "Regole versione", "rk_ev_digest": "Impronta dell'ordine", "rk_ev_snaps": "Istantanee registrate", "rk_ev_none": "nessuna ancora: la prima istantanea fissa questo ordine",
    "rk_ev_reasons": "Classi di ragione di un cambio di valutazione", "rk_ev_non": "Cambi che non sono un cambio di giudizio",
    "rk_r_new_evidence": "nuova evidenza", "rk_r_counter_evidence": "controevidenza", "rk_r_identity_correction": "correzione di identità", "rk_r_better_pharmacological_qualification": "migliore qualificazione farmacologica",
    "rk_r_context_change": "cambio di contesto", "rk_r_method_revision": "revisione del metodo", "rk_r_new_entry": "ingresso di un nuovo composto", "rk_r_tie_resolution": "risoluzione di un pareggio",
    "rk_trg_h": "Quali novità fanno rivalutare", "rk_trg_note": "Le novità che fanno rivalutare un intervento sono rilevate da un'impronta dei suoi ingressi; l'impronta alza una bandiera, un lettore decide. Il radar quotidiano esistente segnala le fonti cambiate.",
    "rk_trg_c_t": "Novità", "rk_trg_c_d": "Come si rileva", "rk_trg_c_r": "Che cosa si rivaluta",
    "rk_one_h": "Sintesi di una pagina", "rk_one_note": "La selezione generale e le due selezioni per obiettivo in una pagina A4. I campi completi sono nelle schede sopra.",
    "rk_one_c_i": "Intervento", "rk_one_c_g": "Gruppo", "rk_one_c_why": "Motivo principale", "rk_one_c_lim": "Limite principale", "rk_one_c_chg": "Che cosa potrebbe cambiare la posizione",
    "rk_plain_h": "Dichiarazione", "rk_p3": "Informazione esplorativa IT7: il confronto di rete e di firma (256 famiglie) non è stato rilevato né escluso, ha escluso di proposito le schede curate e non può guidare da solo nessuna posizione. Nessuna voce è ordinata o riordinata da esso.",
    "rk_denom_groups": "voci per gruppo e vista", "rk_total": "Totale",
    "rk_unc_h": "Altri interventi individuati, senza scheda", "rk_unc_note": "Cercati, esclusi o con effetto potenzialmente opposto, ma senza una scheda: non sono ordinati e non stanno in fondo. Ognuno ha classe, profondità e che cosa lo riaprirebbe. Una ricerca che si astiene non ha mostrato che l'elemento sia poco promettente.",
    "rk_unc_c_i": "Elemento", "rk_unc_c_c": "Classe", "rk_unc_c_d": "Profondità", "rk_unc_c_r": "Motivo e che cosa lo riaprirebbe", "rk_unc_c_u": "Voce collegata", "rk_unc_n": "{n} voci senza scheda",
}
UI_IT.update(UI_IT8)


def rk_label(u: dict) -> str:
    return u["label"]


def rk_g(g: str, long: bool = False) -> str:
    U = UI_IT
    if g not in RK_GROUP_IDS:
        return E(str(g))
    return f'<span class="grp rg rg-{g}" title="{E(U["rk_gp_" + g])}">{E(U["rk_g_" + g] if long else g)}</span>'


def rk_units_by_id(R: dict) -> dict:
    return {u["id"]: u for u in R["units"]}


def rk_item(R: dict, view: str, uid: str, full: bool) -> str:
    U = UI_IT
    u = rk_units_by_id(R)[uid]
    sel = R["selections"][view]
    obj = sel["objective"][uid]
    va = u["views"][obj]
    other = "partial" if obj == "broad" else "broad"
    ov = u["views"][other]
    ev = va["evidence"]
    ls = va.get("lead_summary") or {}
    lead_need = va["lead_need"]
    pw = {p["need"]: p for p in u["pathways"]}
    sg = ", ".join(f"{n} {k}" for k, n in (ls.get("wwox_signs") or {}).items()) or "no signed WWOX-system assertion"
    ctx = (f'{ev["species"] or "—"}; {ev["genotype"] or "—"}; {ev["depth"] or "—"}' if ev["in_wwox"] else f'no WWOX-system result of the intervention; best signal outside WWOX ({ev["scope"] or "none"}; {ev["species"] or "—"})')
    reason = (f'{R["meta"]["groups_en"][va["group"]]["label"]}: lead position {va["lead"]} on {lead_need}. On that need: {sg}; outside WWOX {ls.get("outside_favourable", 0)} favourable and {ls.get("outside_null_or_harm", 0)} null or harm. '
              f'Mechanism: {u["comp"]["M"]["text"]}.')
    paths = "; ".join(f'{NEED_IT.get(p["need"], p["need"])} [{p["position"]}; {U["rk_le_" + p["link_evidence"]]}' + ("; azione opposta" if p["opposed_action"] else "") + "]" for p in u["pathways"])
    srcs = " ".join(f'<a href="https://pubmed.ncbi.nlm.nih.gov/{E(p)}/" rel="noopener noreferrer">PMID {E(p)}</a>' for p in u["pmids"]) or E(U["rk_none"])
    lim = va["main_limit"]
    ev_txt = (("carrier of the position, " if ev.get("carrier_of_position") else "") + f'{ev["id"]}: {ev["text"]}') + (f' (+{ev["other_favourable_wwox_assertions"]} other favourable WWOX-system assertion(s) on the unit)' if ev.get("other_favourable_wwox_assertions") else "")
    ctr = ", ".join(NEED_IT.get(n, n) for n in va["counter_needs"])
    oth = ""
    if ov.get("member"):
        oth = f'<dt>{E(U["rk_i_also"])}</dt><dd>{rk_g(ov["group"])} <span class="mini mut">{E(OBJ_IT[other])}: {E(U["rk_pos_on"])} {E(str(ov.get("lead")))}</span></dd>'
    nx = va["next"]
    return (f'<article class="rk-item" data-unit="{E(uid)}" data-view="{E(view)}"><h4>{E(str(sel["top"].index(uid) + 1))}. {E(rk_label(u))} {rk_g(va["group"])}</h4>'
            f'<dl class="rk-dl">'
            f'<dt>{E(U["rk_i_obj"])}</dt><dd>{E(OBJ_IT[obj])}</dd>'
            f'<dt>{E(U["rk_i_track"])}</dt><dd>{E(", ".join("Track " + t for t in u["tracks"]) or U["rk_unknown"])}</dd>'
            f'<dt>{E(U["rk_i_access"])}</dt><dd>{E(u["access"])}</dd>'
            f'<dt>{E(U["rk_i_context"])}</dt><dd>{E(ctx)}</dd>'
            f'<dt>{E(U["rk_i_reason"])}</dt><dd>{E(reason)}</dd>'
            f'<dt>{E(U["rk_i_evid"])}</dt><dd>{E(ev_txt)}</dd>'
            f'<dt>{E(U["rk_i_limit"])}</dt><dd>{E(lim)}</dd>'
            + (f'<dt>{E(U["rk_i_counter"])}</dt><dd>{E(ctr)}</dd>' if ctr else "")
            + oth
            + f'<dt>{E(U["rk_i_paths"])}</dt><dd>{E(paths)} <span class="mini mut">{E(U["rk_p_den"].format(n=len(u["pathways"]), m=R["meta"]["needs_total"]))}</span></dd>'
            f'<dt>{E(U["rk_i_next"])}</dt><dd>{E(nx["question"])} <span class="mini mut">[{E(nx.get("kind") or "—")}]</span></dd>'
            f'<dt>{E(U["rk_i_feas"])}</dt><dd>{E(nx.get("feasibility") or "—")}</dd>'
            f'<dt>{E(U["rk_i_rise"])}</dt><dd>{E(va["triggers"]["rise"])}' + (f' <span class="mini">{E(nx["would_change"])}</span>' if nx.get("would_change") else "") + '</dd>'
            f'<dt>{E(U["rk_i_fall"])}</dt><dd>{E(va["triggers"]["fall"])}</dd>'
            f'<dt>{E(U["rk_i_leave"])}</dt><dd>{E(va["triggers"]["leave"])}</dd>'
            f'<dt>{E(U["rk_i_src"])}</dt><dd>{srcs}</dd>'
            f'<dt>{E(U["rk_i_date"])}</dt><dd>{E(R["meta"]["as_of"])} <span class="mini mut">{E(U["rk_i_depth"])}: {E(u["depth"])} {E(u["depth_text"])}</span></dd></dl></article>')


def rk_row_attrs(R: dict, u: dict) -> str:
    g = {v: (u["views"][v].get("group") if u["views"][v].get("member") else "") for v in ("broad", "partial")}
    gen = [x for x in (g["broad"], g["partial"]) if x]
    gen_g = min(gen, key=RK_GROUP_IDS.index) if gen else ("" if u["class"] == "EXCL" else "GU")
    evq = sorted({u["views"][v]["evq"] for v in ("broad", "partial") if u["views"][v].get("member") and u["views"][v].get("evq")})
    needs = sorted({p["need"] for p in u["pathways"]})
    return (f'data-unit="{E(u["id"])}" data-class="{u["class"]}" data-g-general="{E(gen_g)}" data-g-broad="{E(g["broad"])}" data-g-partial="{E(g["partial"])}" data-track="{E(" ".join(u["tracks"]))}" '
            f'data-needs="{E(" ".join(needs))}" data-access="{E(" ".join(u["access_cats"] or ["none"]))}" data-evq="{E(" ".join(evq))}" '
            f'data-text="{E((u["label"] + " " + " ".join(u["cards"]) + " " + " ".join(NEED_IT.get(n, n) for n in needs)).lower())}"')


def rk_unit_detail(R: dict, u: dict, full: bool) -> str:
    U = UI_IT
    c = u["comp"]
    W, M, T, Pm, X, Un = c["W"], c["M"], c["T"], c["P"], c["X"], c["U"]
    pths = u["pathways"]
    shared = {}
    for o in R["units"]:
        if o["id"] == u["id"]:
            continue
        for p in o["pathways"]:
            shared.setdefault(p["need"], []).append(o["id"])
    prow = "".join(f'<tr><td data-label="{E(U["rk_p_need"])}">{E(NEED_IT.get(p["need"], p["need"]))}<div class="mut mini">{E(p["need"])}</div></td><td data-label="{E(U["rk_p_thread"])}">{E(THREAD_IT.get(p["thread"], (p["thread"],))[0])}</td>'
                   f'<td data-label="{E(U["rk_p_obj"])}">{E(OBJ_IT[p["objective"]])}</td><td data-label="{E(U["rk_p_pos"])}">{pos_chip(p["position"])}'
                   + (f' <span class="mini mut">{E(U["rk_p_conflict"])}: {E("; ".join(f"{k}={v}" for k, v in sorted(p["position_by_card"].items())))}</span>' if p["same_need_conflict"] else "") + '</td>'
                   f'<td data-label="{E(U["rk_p_link"])}">{E(U["rk_le_" + p["link_evidence"]])}</td><td data-label="{E(U["rk_p_opp"])}">{E(U["rk_yes"] if p["opposed_action"] else U["rk_no"])}</td>'
                   f'<td data-label="{E(U["rk_p_shared"])}">{E(", ".join(shared.get(p["need"], [])) or "—")}</td></tr>' for p in pths)
    members = ""
    if full and isinstance(u["members"], list) and u["members"]:
        members = f'<h5>{E(U["rk_c_mem"])}</h5><ul class="mini">' + "".join(f'<li>{E(m["name"])} <span class="mut">{E(m["family"])}; {E(", ".join(m["roles"]))}; {E(", ".join(m["status"] or []) or "—")}'
                                                                                       + (f'; name twins not merged: {E(", ".join(m["twins"]))}' if m["twins"] else "") + '</span></li>' for m in u["members"]) + "</ul>"
    elif not full:
        members = f'<p class="mini mut">{E(U["rk_c_members_n"])}: {numit("rk.members." + u["id"], u["members"])}</p>'
    pharm = f'<dd>{E(Pm["state"])}' + (f'<br><span class="mini">{E(U["rk_c_pot"])}: {E(Pm["potency_with_assay_context"])}<br>{E(U["rk_c_exp"])}: {E(Pm["human_exposure"])}<br>{E(U["rk_c_brain"])}: {E(Pm["brain_penetration"])}</span>' if "potency_with_assay_context" in Pm else "") + "</dd>"
    return (f'<details class="inl rk-detail" data-unit="{E(u["id"])}"><summary>{E(U["rk_c_sum"])}</summary><dl class="rk-dl">'
            f'<dt>{E(U["rk_c_W"])}</dt><dd>{E(W["text"])} <span class="mini mut">{E(U["rk_c_rep"])}: {E(W["replication"])}; wild-type-only assertions {W["wild_type_only_assertions"]}</span></dd>'
            f'<dt>{E(U["rk_c_M"])}</dt><dd>{E(M["text"])}</dd>'
            f'<dt>{E(U["rk_c_T"])}</dt><dd>track {E(", ".join(T["track"]) or "UNKNOWN")}; species {E(", ".join(T["species_of_wwox_assertions"]))}' + (f'; {E(" ".join(T["transfer_limits"])[:420])}' if T["transfer_limits"] else "") + '</dd>'
            f'<dt>{E(U["rk_c_P"])}</dt>{pharm}'
            f'<dt>{E(U["rk_c_X"])}</dt><dd>{X["wwox_null_harm_mixed"]} {E(U["rk_x_w"])}; {X["outside_wwox_null_or_harm"]} {E(U["rk_x_o"])}; {X["need_level_counter_items"]} {E(U["rk_x_n"])}; {len(X["opposed_action_needs"])} {E(U["rk_x_opp"])}'
            + (f' <span class="mini mut">{E("; ".join(X["tags"][:4]))}</span>' if X["tags"] else "") + '</dd>'
            f'<dt>{E(U["rk_c_U"])}</dt><dd>{E(Un["text"])}; unknown: {E("; ".join(Un["unknown"]))}</dd>'
            + (f'<dt>{E(U["rk_c_merge"])}</dt><dd>{E(u["merge_reason"])}</dd>' if u["merge_reason"] else "")
            + (f'<dt>{E(U["rk_c_ex"])}</dt><dd>{E(", ".join(U["hyp_r_" + r] for r in u["model_exclusions"]))}</dd>' if u["model_exclusions"] else "")
            + f'</dl><h5>{E(U["rk_p_h"])}</h5><div class="scrollx"><table class="tbl stk"><thead><tr><th>{E(U["rk_p_need"])}</th><th>{E(U["rk_p_thread"])}</th><th>{E(U["rk_p_obj"])}</th><th>{E(U["rk_p_pos"])}</th><th>{E(U["rk_p_link"])}</th><th>{E(U["rk_p_opp"])}</th><th>{E(U["rk_p_shared"])}</th></tr></thead><tbody>'
            + (prow or f'<tr><td colspan="7" data-label="{E(U["rk_p_need"])}">{E(U["rk_none"])}</td></tr>') + f'</tbody></table></div><p class="mini mut">{E(U["rk_p_den"].format(n=len(pths), m=R["meta"]["needs_total"]))} {E(U["rk_p_comp"])}</p>' + members + '</details>')


OBJ_IT = {"broad": "Recupero ampio e duraturo", "partial": "Beneficio parziale o ponte"}


def render_ranking(P: dict) -> str:
    R = P["cur"].get("ranking")
    if not R:
        return ""
    U = UI_IT
    full = P["source"] == "full"
    units = R["units"]
    M = R["meta"]
    groups_legend = "".join(f'<li>{rk_g(g)} <b>{E(U["rk_g_" + g].split(" · ", 1)[1])}.</b> <span class="mini">{E(U["rk_gp_" + g])}</span></li>' for g in RK_GROUP_IDS)
    cl_rows = "".join(f'<tr><th scope="row">{E(U["rk_cl_" + k])}</th><td>{numit("rk.class." + k, M["by_class"][k])}</td><td class="mini">{E(U["rk_cl_" + k + "_t"])}</td></tr>' for k in RK_CLASSES)
    # top lists (all three rendered; the page script shows the chosen one)
    blocks = []
    for v in RK_VIEWS:
        s = R["selections"][v]
        items = "".join(rk_item(R, v, uid, full) for uid in s["top"]) or f'<p class="state-none">{E(U["rk_top_none"])}</p>'
        by = rk_units_by_id(R)
        apart = "".join(f'<li>{rk_g(a["group"])} {E(by[a["id"]]["label"])} <span class="mini mut">({E(OBJ_IT[a["objective"]])})</span></li>' for a in s["apart"])
        blocks.append(f'<div class="rk-view" data-view="{v}"><h3>{E(U["rk_top_h"])}: {E(U["rk_v_" + v])} ({numit("rk.top." + v, len(s["top"]))})</h3>{items}'
                      f'<details class="inl"><summary>{E(U["rk_apart_h"])} ({numit("rk.apart." + v, len(s["apart"]))})</summary><p class="mini mut">{E(U["rk_apart_note"])}</p><ul class="mini rk-apart">{apart}</ul></details></div>')
    # filter controls
    needs = sorted({p["need"] for u in units for p in u["pathways"]})
    accs = sorted({a for u in units for a in (u["access_cats"] or ["none"])})
    opt = lambda vals, lab: f'<option value="">{E(U["rk_f_any"])}</option>' + "".join(f'<option value="{E(v)}">{E(lab(v))}</option>' for v in vals)
    controls = (f'<div id="rk-ctl" role="group" aria-label="{E(U["rk_ctl_view"])}"><div class="fbar">'
                f'<label>{E(U["rk_ctl_view"])}<select id="rk-view">' + "".join(f'<option value="{v}">{E(U["rk_v_" + v])}</option>' for v in RK_VIEWS) + '</select></label>'
                f'<label>{E(U["rk_f_class"])}<select id="rk-class">' + opt(RK_CLASSES, lambda v: U["rk_cl_" + v]) + '</select></label>'
                f'<label>{E(U["rk_f_group"])}<select id="rk-group">' + opt(RK_GROUP_IDS, lambda v: U["rk_g_" + v]) + '</select></label>'
                f'<label>{E(U["rk_f_track"])}<select id="rk-track">' + opt(["A", "B"], lambda v: "Track " + v) + '</select></label>'
                f'<label>{E(U["rk_f_need"])}<select id="rk-need">' + opt(needs, lambda v: NEED_IT.get(v, v)) + '</select></label>'
                f'<label>{E(U["rk_f_access"])}<select id="rk-access">' + opt(accs, lambda v: U.get("acc_" + v, v)) + '</select></label>'
                f'<label>{E(U["rk_f_evq"])}<select id="rk-evq">' + opt(RK_EVQ, lambda v: U["rk_evq_" + v]) + '</select></label>'
                f'<label>{E(U["rk_f_q"])}<input type="search" id="rk-q" placeholder="{E(U["rk_f_q_ph"])}"></label></div>'
                f'<div class="bar-actions noprint"><button type="button" id="rk-reset">{E(U["rk_btn_reset"])}</button><button type="button" id="rk-tsv">{E(U["rk_btn_tsv"])}</button><button type="button" id="rk-json">{E(U["rk_btn_json"])}</button>'
                f'<a class="btnlink" href="#section=rankingprint">{E(U["rk_btn_print1"])}</a><a class="btnlink" href="#section=ranking">{E(U["rk_btn_printall"])}</a><span class="cnt" id="rk-count" aria-live="polite"></span></div></div>')
    # full table
    def grp_cell(u, v):
        va = u["views"][v]
        if not va.get("member"):
            return f'<span class="mut mini">{E(U["rk_not_member"])}</span>' if u["class"] != "EXCL" else "—"
        return rk_g(va["group"]) + (' <span class="mini" title="counter-evidence on another need of this objective">◆</span>' if va["contested"] else "")
    trs = []
    def best_group(x):
        return min([RK_GROUP_IDS.index(x["views"][v]["group"]) for v in ("broad", "partial") if x["views"][v].get("member")] or [99])
    for u in sorted(units, key=lambda x: (best_group(x), x["label"].lower())):
        gen = [u["views"][v]["group"] for v in ("broad", "partial") if u["views"][v].get("member")]
        gen_g = min(gen, key=RK_GROUP_IDS.index) if gen else ("—" if u["class"] == "EXCL" else "GU")
        lead = ", ".join(f'{v}: {u["views"][v]["lead"]}' for v in ("broad", "partial") if u["views"][v].get("member") and u["views"][v].get("lead")) or "—"
        evq = ", ".join(sorted({U["rk_evq_" + u["views"][v]["evq"]] for v in ("broad", "partial") if u["views"][v].get("member") and u["views"][v].get("evq")})) or "—"
        ctr = u["comp"]["X"]
        trs.append(f'<tr class="rk-row" {rk_row_attrs(R, u)}><th scope="row" data-label="{E(U["rk_t_unit"])}">{E(u["label"])}<div class="mut mini">{E(u["id"])} · {E(" ".join(u["cards"]))}</div></th>'
                   f'<td data-label="{E(U["rk_t_class"])}"><span class="chip rk-cl rk-cl-{u["class"]}" title="{E(U["rk_cl_" + u["class"] + "_t"])}">{E(U["rk_cl_" + u["class"]])}</span></td>'
                   f'<td data-label="{E(U["rk_t_gen"])}">{rk_g(gen_g) if gen_g != "—" else "—"}</td><td data-label="{E(U["rk_t_broad"])}">{grp_cell(u, "broad")}</td><td data-label="{E(U["rk_t_part"])}">{grp_cell(u, "partial")}</td>'
                   f'<td data-label="{E(U["rk_t_lead"])}">{E(lead)}</td><td data-label="{E(U["rk_t_evq"])}">{E(evq)}</td>'
                   f'<td data-label="{E(U["rk_t_ctr"])}">{ctr["wwox_null_harm_mixed"]} / {ctr["outside_wwox_null_or_harm"]}</td><td data-label="{E(U["rk_t_track"])}">{E(", ".join(u["tracks"]) or "—")}</td>'
                   f'<td data-label="{E(U["rk_t_acc"])}">{E(", ".join(U.get("acc_" + a, a) for a in (u["access_cats"] or ["—"])))}</td><td data-label="{E(U["rk_t_depth"])}">{E(u["depth"])}</td></tr>'
                   f'<tr class="rk-row-detail" data-unit="{E(u["id"])}"><td colspan="11">{rk_unit_detail(R, u, full)}</td></tr>')
    table = (f'<div class="scrollx"><table class="tbl stk rk-table" id="rk-table"><thead><tr><th>{E(U["rk_t_unit"])}</th><th>{E(U["rk_t_class"])}</th><th>{E(U["rk_t_gen"])}</th><th>{E(U["rk_t_broad"])}</th><th>{E(U["rk_t_part"])}</th>'
             f'<th>{E(U["rk_t_lead"])}</th><th>{E(U["rk_t_evq"])}</th><th>{E(U["rk_t_ctr"])} <span class="mini">(WWOX / {E("fuori")})</span></th><th>{E(U["rk_t_track"])}</th><th>{E(U["rk_t_acc"])}</th><th>{E(U["rk_t_depth"])}</th></tr></thead><tbody>'
             + "".join(trs) + '</tbody></table></div>')
    # inventory
    I = R["inventory"]
    q_rows = "".join(f'<tr><th scope="row">{E(U["rk_q_" + k])}</th><td>{numit("rk.inv.q." + k, I["by_first_order"].get(k, 0))}</td><td class="mini">{E(U["rk_inv_of"])} {numit("rk.inv.families." + k, I["families"])} {E(U["sel_u_f"])}</td></tr>' for k in ("Q1", "Q2", "Q3", "Q4", "Q5", "UNIT"))
    acc_rows = ", ".join(f'{E(U.get("acc_" + k, k))} {numit("rk.inv.acc." + k, v)}' for k, v in sorted(I["need_linked_by_access_category"].items()))
    unc_rows = "".join(f'<tr><th scope="row" data-label="{E(U["rk_unc_c_i"])}">{E(r["item"])}<div class="mini mut">{E(r["item_id"])} · {E(r["kind"])}</div></th><td data-label="{E(U["rk_unc_c_c"])}"><span class="chip rk-cl rk-cl-{r["class"]}">{E(U["rk_cl_" + r["class"]])}</span></td>'
                       f'<td data-label="{E(U["rk_unc_c_d"])}">{E(r["evaluation_depth"])}</td><td data-label="{E(U["rk_unc_c_r"])}">{E(r["reason"])}' + (f' <span class="mini mut">{E(r["what_would_reopen"])}</span>' if r["what_would_reopen"] else "") + '</td>'
                       f'<td data-label="{E(U["rk_unc_c_u"])}">{E(r["related_unit"] or "—")}</td></tr>' for r in R.get("uncarded") or [])
    unc = (f'<h4>{E(U["rk_unc_h"])} ({numit("rk.unc.n", len(R.get("uncarded") or []))})</h4><p class="mini mut">{E(U["rk_unc_note"])}</p><div class="scrollx"><table class="tbl stk"><thead><tr><th>{E(U["rk_unc_c_i"])}</th><th>{E(U["rk_unc_c_c"])}</th><th>{E(U["rk_unc_c_d"])}</th><th>{E(U["rk_unc_c_r"])}</th><th>{E(U["rk_unc_c_u"])}</th></tr></thead><tbody>{unc_rows}</tbody></table></div>') if R.get("uncarded") else ""
    inv = (f'<h3>{E(U["rk_inv_h"])}</h3><p class="mini">{E(U["rk_inv_lead"])}</p>'
           f'<table class="tbl rk-plain"><thead><tr><th>{E(U["rk_t_class"])}</th><th>{E(U["rk_inv_units"])}</th><th></th></tr></thead><tbody>{cl_rows}</tbody></table>'
           f'<p class="mini">{E(U["rk_inv_units_n"].format(u=len(units), r=M["units_ranked"], x=M["by_class"]["EXCL"], c=len(P["cur"]["cands"])))}</p>'
           f'<p class="mini"><b>{numit("rk.inv.records", I["records"])}</b> record · <b>{numit("rk.inv.families", I["families"])}</b> {E(U["sel_u_f"])}. {E(U["rk_inv_fam_note"])}</p>'
           f'<h4>{E(U["rk_inv_q"])}</h4><table class="tbl rk-plain"><tbody>{q_rows}</tbody></table>'
           f'<p class="mini">{E(U["rk_inv_names"].format(n=I["distinct_display_names_in_q1"]))}. {E(U["rk_inv_opp"])}: {numit("rk.inv.opp", I["q1_with_opposed_action_elsewhere"])}.</p>'
           f'<p class="mini"><b>{E(U["rk_inv_access"])}:</b> {acc_rows}.</p>'
           f'<p class="mini">{E(U["rk_inv_queue"].format(n=R["queue"]["compounds"]))}</p>'
           f'<p class="mini"><b>{E(U["rk_inv_depth_h"])}:</b> {E(U["rk_inv_depth"])}</p>' + unc)
    # evolution
    hist = R["history"]
    hrows = "".join(f'<li><code>{E(h["snapshot"])}</code> · {h["n"]} · ' + ", ".join(f'{E(U.get("rk_r_" + k, k))} {v}' for k, v in h["reasons"].items()) + '</li>' for h in hist) or f'<li class="mut">{E(U["rk_ev_none"])}</li>'
    trig = "".join(f'<tr><th scope="row" data-label="{E(U["rk_trg_c_t"])}"><code>{E(t["trigger"])}</code> {E(t["what"])}</th><td data-label="{E(U["rk_trg_c_d"])}">{E(t["detected_by"])}</td><td data-label="{E(U["rk_trg_c_r"])}">{E(t["re_evaluates"])}</td></tr>' for t in R["triggers"])
    evo = (f'<h3>{E(U["rk_ev_h"])}</h3><p class="mini">{E(U["rk_ev_lead"])}</p>'
           f'<p class="mini"><b>{E(U["rk_ev_asof"])}:</b> {E(M["as_of"])} · <b>{E(U["rk_ev_rules"])}:</b> {E(M["rules_version"])} · <b>{E(U["rk_ev_digest"])}:</b> <code>{E(M["order_digest"])}</code></p>'
           f'<p class="mini"><b>{E(U["rk_ev_snaps"])}:</b></p><ul class="mini">{hrows}</ul>'
           f'<p class="mini"><b>{E(U["rk_ev_reasons"])}:</b> ' + ", ".join(E(U["rk_r_" + k]) for k in M["reason_classes"]) + f'. <b>{E(U["rk_ev_non"])}:</b> ' + ", ".join(E(U["rk_r_" + k]) for k in M["non_assessment_changes"]) + '.</p>'
           f'<h4>{E(U["rk_trg_h"])}</h4><p class="mini">{E(U["rk_trg_note"])}</p><div class="scrollx"><table class="tbl stk"><thead><tr><th>{E(U["rk_trg_c_t"])}</th><th>{E(U["rk_trg_c_d"])}</th><th>{E(U["rk_trg_c_r"])}</th></tr></thead><tbody>{trig}</tbody></table></div>')
    return (f'<section id="ranking" aria-labelledby="h-rk8"><h2 id="h-rk8">{E(U["rk_h"])}</h2><p class="lead">{E(U["rk_lead"])}</p>'
            f'<div class="note"><b>{E(U["rk_not_h"])}.</b><ul class="mini"><li>{E(U["rk_not_1"])}</li><li>{E(U["rk_not_2"])}</li><li>{E(U["rk_not_3"])}</li><li>{E(U["rk_not_4"])}</li></ul></div>'
            f'<details class="inl howto" open><summary>{E(U["rk_how_h"])}</summary><ol class="mini"><li>{E(U["rk_how_1"])}</li><li>{E(U["rk_how_2"])}</li><li>{E(U["rk_how_3"])}</li><li>{E(U["rk_how_4"])}</li></ol>'
            f'<h4>{E(U["rk_groups_h"])}</h4><ul class="poslist rk-groups">{groups_legend}</ul><p class="mini">{E(U["rk_sel_note"])}</p><p class="mini mut">{E(U["rk_p3"])}</p></details>'
            + controls + "".join(blocks) + f'<h3>{E(U["rk_t_h"])} (<span id="rk-n">{len(units)}</span>)</h3><p class="mini mut">{E(U["rk_t_note"])}</p>' + table + inv + evo
            + f'<p class="noprint"><a class="btnlink" href="#section=ranking">{E(U["sec_print"])}</a></p></section>')


def render_ranking_onepage(P: dict) -> str:
    R = P["cur"].get("ranking")
    if not R:
        return ""
    U = UI_IT
    by = rk_units_by_id(R)
    parts = []
    s = R["selections"]["general"]
    rows = ""
    for uid in s["top"]:
        u = by[uid]
        obj = s["objective"][uid]
        va = u["views"][obj]
        ls = va.get("lead_summary") or {}
        sg = ", ".join(f"{n} {k}" for k, n in (ls.get("wwox_signs") or {}).items()) or "no signed WWOX-system assertion"
        why = f'{va["lead"]} on {NEED_IT.get(va["lead_need"], va["lead_need"])}; {sg}'
        rows += (f'<tr><th scope="row" data-label="{E(U["rk_one_c_i"])}">{E(u["label"])}<div class="mini mut">{E(OBJ_IT[obj])} · Track {E(",".join(u["tracks"]) or "?")}</div></th><td data-label="{E(U["rk_one_c_g"])}">{rk_g(va["group"])}</td>'
                 f'<td data-label="{E(U["rk_one_c_why"])}">{E(clip(why, 120))}</td><td data-label="{E(U["rk_one_c_lim"])}">{E(clip(va["main_limit"], 70))}</td><td data-label="{E(U["rk_one_c_chg"])}">{E(clip(va["triggers"]["rise"], 70))}</td></tr>')
    parts.append(f'<h3>{E(U["rk_v_general"])}</h3><table class="tbl stk rk-one"><colgroup><col style="width:24%"><col style="width:7%"><col style="width:27%"><col style="width:21%"><col style="width:21%"></colgroup><thead><tr><th>{E(U["rk_one_c_i"])}</th><th>{E(U["rk_one_c_g"])}</th><th>{E(U["rk_one_c_why"])}</th><th>{E(U["rk_one_c_lim"])}</th><th>{E(U["rk_one_c_chg"])}</th></tr></thead><tbody>{rows}</tbody></table>')
    for v in ("broad", "partial"):
        sv = R["selections"][v]
        parts.append(f'<p class="mini"><b>{E(U["rk_v_" + v])}:</b> ' + "; ".join(f'{E(by[x]["label"])} {rk_g(sv["groups"][x])}' for x in sv["top"]) + '</p>')
    return (f'<section id="rankingprint" aria-labelledby="h-rk1"><h2 id="h-rk1">{E(U["rk_one_h"])}</h2><p class="mini">{E(U["rk_lead"])}</p><p class="mini mut">{E(U["rk_one_note"])} {E(U["rk_ev_asof"])}: {E(R["meta"]["as_of"])}; {E(U["rk_ev_rules"])} {E(R["meta"]["rules_version"])}.</p>'
            + "".join(parts) + f'<p class="mini">{E(U["rk_sel_note"])}</p><p class="noprint"><a class="btnlink" href="#section=rankingprint">{E(U["sec_print"])}</a></p></section>')


def ui_payload() -> dict:
    """Italian orientation strings for the page script (D.ui): one dict, no logic."""
    ui = dict(UI_IT)
    ui.update({"pos": POS_IT, "scopeL": SCOPE_IT, "goalL": GOALS_IT, "thread": {k: {"name": v[0], "text": v[1]} for k, v in THREAD_IT.items()}, "need": NEED_IT,
               "statusL": STATUS_IT, "countryL": COUNTRY_IT, "crit": CRIT_IT})
    return ui


TOKEN_RE = re.compile(r"\{\{(\w+)\}\}")


def fill_tokens(text: str) -> str:
    """Replace {{key}} tokens of an asset with the escaped Italian string; an unknown key is a build error, never a silent blank."""
    def one(m):
        if m.group(1) not in UI_IT:
            raise SystemExit(f"asset token {{{{{m.group(1)}}}}} has no Italian string in UI_IT")
        return E(UI_IT[m.group(1)])
    return TOKEN_RE.sub(one, text)


def render(P: dict, dr: Path = DEFAULT_DR) -> str:
    st = render_static(P)
    P = dict(P, ui=ui_payload())
    if P["source"] == "shareable":
        _allow = load_allowlist(dr)
        P["ui"] = _map_strings(P["ui"], lambda x: scrub_file_tokens(x, _allow))
    data = json.dumps(P, ensure_ascii=False, sort_keys=True, separators=(",", ":")).replace("</", "<\\/").replace("<!--", "<\\!--")
    U = UI_IT
    page = TEMPLATE
    cur_html = fill_tokens(read_asset(dr, "curated.html"))
    cur_html = cur_html.replace("__OVERVIEW__", render_overview(P)).replace("__GRAPH__", render_evidence_graph(P)).replace("__WORKORDER__", render_work_order(P)).replace("__SELECTION__", render_selection(P)).replace("__HYPOTHESES__", render_hypotheses(P)).replace("__PREDICTIVE__", render_predictive(P)).replace("__CHARTS__", render_charts(P)).replace("__RANKING__", render_ranking(P)).replace("__RANKPRINT__", render_ranking_onepage(P))
    page = page.replace("__CSS__", CSS + read_asset(dr, "curated.css")).replace("__JS__", JS).replace("__CJS__", read_asset(dr, "curated.js"))
    page = page.replace("__CURATED__", cur_html).replace("__FOOTER__", render_footer(P))
    for k, key in (("TITLE", "page_title"), ("SKIP", "skip"), ("H1", "h1"), ("SUB", "sub"), ("NAVLABEL", "nav_label"), ("N_OV", "nav_overview"), ("N_RK", "nav_ranking"), ("N_TH", "nav_threads"), ("N_EG", "nav_chains"), ("N_CH", "nav_charts"), ("N_SE", "nav_selection"), ("N_HY", "nav_hyp"), ("N_PR2", "nav_pred"), ("N_NAV", "nav_navigate"),
                   ("N_CA", "nav_cards"), ("N_PR", "nav_priority"), ("N_CP", "nav_compare"), ("N_TD", "nav_tech"), ("TD_SUM", "td_sum"), ("TD_NOTE", "td_note")):
        page = page.replace(f"__{k}__", E(U[key]))
    page = page.replace("__BANNER__", render_banner(P))
    st = dict(st)
    st.pop("BANNER", None)
    for k, v in st.items():
        page = page.replace(f"__{k}__", v)
    page = page.replace("__PAIRUNIT__", E(str(P["pair_unit"])))
    if P["source"] == "shareable":   # static text written in this builder may name repository files: describe them (the data object is scrubbed in build_payload)
        allow = load_allowlist(dr)
        parts = re.split(r"(<script\b[^>]*>.*?</script>|<style\b[^>]*>.*?</style>)", page, flags=re.S)
        page = "".join(scrub_file_tokens(x, allow) if x.startswith("<script") else (x if x.startswith("<style") else re.sub(r">([^<]+)<", lambda m: ">" + scrub_file_tokens(m.group(1), allow) + "<", x)) for x in parts)
    page = page.replace("__DATA__", data)  # last: the data may contain placeholder-like text
    return page


def build(dr: Path = DEFAULT_DR, source: str = "full") -> str:
    out = render(build_payload(dr, source), dr)
    n = len(out.encode("utf-8"))
    if n > MAX_BYTES:
        raise SystemExit(f"view is {n} bytes, above the {MAX_BYTES} budget: trim the projection")
    return out


# ------------------------------------------------------------------ real viewport emulation (Chromium DevTools Protocol, stdlib only)
VIEWPORTS = [(360, 780, True), (390, 844, True), (768, 1024, False), (1280, 900, False)]   # (width, height, mobile emulation)
CHROMIUM_CANDIDATES = ["/snap/chromium/current/usr/lib/chromium-browser/chrome", "chromium", "chromium-browser", "google-chrome"]


def find_chromium() -> str | None:
    import shutil
    return next((b for b in CHROMIUM_CANDIDATES if shutil.which(b) or Path(b).exists()), None)


class Cdp:
    """A minimal websocket client (RFC 6455, text frames) for one Chromium page target. Launches the browser WITHOUT any sandbox-bypass flag.
    The window size is irrelevant: Emulation.setDeviceMetricsOverride sets the real layout viewport, which is then MEASURED, not assumed."""

    def __init__(self, binary: str, tmpdir: str):
        import socket
        import subprocess
        import time
        import urllib.request
        with socket.socket() as so:
            so.bind(("127.0.0.1", 0))
            self.port = so.getsockname()[1]
        self.proc = subprocess.Popen([binary, "--headless=new", "--disable-gpu", f"--remote-debugging-port={self.port}", f"--user-data-dir={tmpdir}", "about:blank"],
                                     stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        url = None
        for _ in range(100):
            try:
                tabs = json.loads(urllib.request.urlopen(f"http://127.0.0.1:{self.port}/json/list", timeout=2).read())
                url = next((t["webSocketDebuggerUrl"] for t in tabs if t.get("type") == "page"), None)
                if url:
                    break
            except Exception:
                pass
            time.sleep(0.2)
        if not url:
            self.close()
            raise RuntimeError("Chromium DevTools endpoint did not come up")
        self.sock = socket.create_connection(("127.0.0.1", self.port), timeout=60)
        self._handshake(url.split(f":{self.port}", 1)[1])
        self.n = 0
        self.events: list = []

    def _handshake(self, path: str):
        import base64
        import os
        key = base64.b64encode(os.urandom(16)).decode()
        self.sock.sendall((f"GET {path} HTTP/1.1\r\nHost: 127.0.0.1:{self.port}\r\nUpgrade: websocket\r\nConnection: Upgrade\r\nSec-WebSocket-Key: {key}\r\nSec-WebSocket-Version: 13\r\n\r\n").encode())
        buf = b""
        while b"\r\n\r\n" not in buf:
            buf += self.sock.recv(4096)
        if b" 101 " not in buf.split(b"\r\n", 1)[0]:
            raise RuntimeError("websocket upgrade refused: " + buf[:80].decode("latin1"))
        self.buf = buf.split(b"\r\n\r\n", 1)[1]

    def _read(self, n: int) -> bytes:
        while len(self.buf) < n:
            chunk = self.sock.recv(1 << 16)
            if not chunk:
                raise RuntimeError("websocket closed")
            self.buf += chunk
        out, self.buf = self.buf[:n], self.buf[n:]
        return out

    def _send(self, text: str):
        import os
        import struct
        data = text.encode()
        head = bytearray([0x81])
        if len(data) < 126:
            head.append(0x80 | len(data))
        elif len(data) < 65536:
            head += bytes([0x80 | 126]) + struct.pack(">H", len(data))
        else:
            head += bytes([0x80 | 127]) + struct.pack(">Q", len(data))
        mask = os.urandom(4)
        self.sock.sendall(bytes(head) + mask + bytes(b ^ mask[i % 4] for i, b in enumerate(data)))

    def _recv(self) -> dict:
        import struct
        msg = b""
        while True:
            b1, b2 = self._read(2)
            op, ln = b1 & 0x0F, b2 & 0x7F
            if ln == 126:
                ln = struct.unpack(">H", self._read(2))[0]
            elif ln == 127:
                ln = struct.unpack(">Q", self._read(8))[0]
            payload = self._read(ln)
            if op == 8:
                raise RuntimeError("websocket closed by the browser")
            if op in (1, 0):
                msg += payload
                if b1 & 0x80:
                    return json.loads(msg.decode())

    def call(self, method: str, **params):
        self.n += 1
        mid = self.n
        self._send(json.dumps({"id": mid, "method": method, "params": params}))
        while True:
            m = self._recv()
            if m.get("id") == mid:
                if "error" in m:
                    raise RuntimeError(f"{method}: {m['error']}")
                return m.get("result") or {}
            if "method" in m:
                self.events.append(m["method"])

    def wait_event(self, name: str, tries: int = 400):
        for _ in range(tries):
            if name in self.events:
                self.events.remove(name)
                return True
            m = self._recv()
            if "method" in m:
                self.events.append(m["method"])
        return False

    def evaluate(self, expr: str):
        r = self.call("Runtime.evaluate", expression=expr, returnByValue=True, awaitPromise=True)
        if "exceptionDetails" in r:
            raise RuntimeError("page script error: " + json.dumps(r["exceptionDetails"])[:300])
        return (r.get("result") or {}).get("value")

    def close(self):
        try:
            self.proc.terminate()
            self.proc.wait(timeout=10)
        except Exception:
            self.proc.kill()


MEASURE_JS = r"""(function(){var iw=__REQ__,de=document.documentElement,off=[];
function scrolls(e){for(var p=e.parentElement;p&&p!==document.body;p=p.parentElement){var o=getComputedStyle(p).overflowX;if(o==='auto'||o==='scroll'||o==='hidden')return true}return false}
var all=document.body.getElementsByTagName('*');for(var i=0;i<all.length&&off.length<6;i++){var e=all[i],r=e.getBoundingClientRect();if(r.width&&r.right>iw+1&&getComputedStyle(e).position!=='fixed'&&!scrolls(e)&&e.offsetParent!==null)off.push(e.tagName.toLowerCase()+(e.id?'#'+e.id:'')+(e.className&&e.className.baseVal===undefined?'.'+String(e.className).split(' ')[0]:'')+' right='+Math.round(r.right))}
return {legendBottom:(function(){var e=document.querySelector('.legendrow');return e?Math.round(e.getBoundingClientRect().bottom+window.scrollY):null})(),innerWidth:window.innerWidth,scrollWidth:de.scrollWidth,bodyScrollWidth:document.body.scrollWidth,clientWidth:de.clientWidth,visualViewportWidth:window.visualViewport?Math.round(window.visualViewport.width):null,ready:document.body.getAttribute('data-cur-ready'),offenders:off}})()"""


def brief_chars(c: dict) -> int:
    b = c["brief"]
    return sum(len(str(b[k])) for k in ("wwox", "external", "counter", "missing", "next")) + sum(len(str(s.get("title") or "")) + 40 for s in b["sources"]) + len(c["name"])


def scenarios(P: dict) -> list[tuple[str, str]]:
    cur = P["cur"]
    ids = [c["id"] for c in cur["cands"]]
    th = next((t["id"] for t in cur["threads"] if t["id"] == "Network excitability"), cur["threads"][0]["id"])
    a, b = (ids + ids)[:2]
    from urllib.parse import quote
    longest = max(cur["cands"], key=lambda c: (brief_chars(c), c["id"]))["id"]   # the card whose one-page synthesis is the longest: the worst case for the page limit
    return [("first_screen", ""), ("filtered_thread", "#c=thread:" + quote(th)), ("comparison", f"#compare={a},{b}"), ("export_card", "#export=" + a), ("technical_open", "#tech-versions"),
            ("brief", "#brief=" + longest), ("evidence_graph", "#chains"), ("work_order", "#work-order"),
            ("selection", "#selection"), ("hypotheses", "#hypotheses"), ("predictive", "#predictive"), ("contexts", "#contexts"),
            ("section_selection", "#section=selection"), ("section_predictive", "#section=predictive"),
            ("ranking", "#ranking"), ("section_rankingprint", "#section=rankingprint")]


def measure_viewports(html_path: Path, shots: Path | None = None, widths: list | None = None) -> list[dict]:
    """For each viewport and scenario: the page's OWN innerWidth and documentElement.scrollWidth, read after Emulation.setDeviceMetricsOverride.
    Returns [] when no Chromium exists (the caller reports that, never a fake pass). Print layout is measured with print media emulation at A4 width."""
    import base64
    import tempfile
    binary = find_chromium()
    if not binary:
        return []
    P = json.loads(re.search(r'<script id="data" type="application/json">(.*?)</script>', html_path.read_text(encoding="utf-8"), re.S).group(1).replace("<\\/", "</").replace("<\\!--", "<!--"))
    out = []
    with tempfile.TemporaryDirectory() as td:
        cdp = Cdp(binary, td)
        try:
            cdp.call("Page.enable")
            runs = [(w, h, mo) for (w, h, mobile) in VIEWPORTS if not widths or w in widths for mo in ((True, False) if mobile else (False,))]
            for (w, h, mobile) in runs:
                cdp.call("Emulation.setDeviceMetricsOverride", width=w, height=h, deviceScaleFactor=1, mobile=mobile)
                for name, frag in scenarios(P):
                    cdp.call("Page.navigate", url="about:blank")
                    cdp.events.clear()
                    cdp.call("Page.navigate", url=f"file://{html_path}{frag}")
                    cdp.wait_event("Page.loadEventFired")
                    cdp.evaluate("new Promise(function(r){setTimeout(r,500)})")
                    m = cdp.evaluate(MEASURE_JS.replace("__REQ__", str(w)))
                    m.update({"requested": w, "scenario": name, "mobile": mobile, "overflow": m["scrollWidth"] > w or m["innerWidth"] > w})
                    if shots and (mobile or w > 390):
                        shots.mkdir(parents=True, exist_ok=True)
                        anchor = {"comparison": "#compare", "filtered_thread": "#navigate", "technical_open": "#tech-versions", "export_card": "body", "evidence_graph": "#chains", "work_order": "#work-order", "selection": "#selection", "ranking": "#ranking", "section_rankingprint": "body", "hypotheses": "#hypotheses", "predictive": "#predictive", "contexts": "#contexts"}.get(name, "body")
                        y = cdp.evaluate("(function(){var e=document.querySelector(%s);return e?Math.max(0,Math.round(e.getBoundingClientRect().top+scrollY)-8):0})()" % json.dumps(anchor))
                        lm = cdp.call("Page.getLayoutMetrics")["cssContentSize"]
                        tall = name in ("export_card", "comparison", "brief", "evidence_graph", "selection", "hypotheses", "predictive", "contexts", "ranking") and w <= 390
                        clip = {"x": 0, "y": y, "width": w, "height": min(int(lm["height"]) - y, 3000 if tall else h), "scale": 1}
                        shot = cdp.call("Page.captureScreenshot", format="png", clip=clip, captureBeyondViewport=True)
                        fp = shots / f"{name}_{m['innerWidth']}px.png"
                        fp.write_bytes(base64.b64decode(shot["data"]))
                        m["shot"] = fp.name
                    out.append(m)
            # print layout: A4 width (794 css px), print media emulated; the page must not overflow and the export view must paginate
            cdp.call("Emulation.setDeviceMetricsOverride", width=794, height=1123, deviceScaleFactor=1, mobile=False)
            cdp.call("Emulation.setEmulatedMedia", media="print")
            sc_by = dict(scenarios(P))
            for name, frag in (("print_first_screen", ""), ("print_export_card", sc_by["export_card"]), ("print_brief", sc_by["brief"]), ("print_brief_all", "#brief=" + ",".join(c["id"] for c in P["cur"]["cands"])),
                              ("print_section_selection", sc_by["section_selection"]), ("print_section_hypotheses", "#section=hypotheses"), ("print_section_predictive", sc_by["section_predictive"]),
                              ("print_section_rankingprint", sc_by["section_rankingprint"]), ("print_section_ranking", "#section=ranking")):
                cdp.call("Page.navigate", url="about:blank")
                cdp.events.clear()
                cdp.call("Page.navigate", url=f"file://{html_path}{frag}")
                cdp.wait_event("Page.loadEventFired")
                cdp.evaluate("new Promise(function(r){setTimeout(r,500)})")
                m = cdp.evaluate(MEASURE_JS.replace("__REQ__", "794"))
                pdf = cdp.call("Page.printToPDF", paperWidth=8.27, paperHeight=11.69, printBackground=True, preferCSSPageSize=True)
                raw = base64.b64decode(pdf["data"])
                m.update({"requested": 794, "scenario": name, "mobile": False, "overflow": m["scrollWidth"] > 794 or m["innerWidth"] > 794, "pdf_pages": len(re.findall(rb"/Type\s*/Page[^s]", raw)), "pdf_bytes": len(raw)})
                if shots and name in ("print_export_card", "print_brief", "print_section_selection", "print_section_hypotheses", "print_section_predictive", "print_section_rankingprint", "print_section_ranking"):
                    (shots / f"{name[6:]}_print.pdf").write_bytes(raw)
                out.append(m)
            cdp.call("Emulation.setEmulatedMedia", media="")
        finally:
            cdp.close()
    return out


def main(argv=None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if argv and argv[0] in ("audit-shareable", "package"):   # IT5 P13: the proof and the package live in their own small modules
        if argv[0] == "audit-shareable":
            import repurposing_shareable_audit as _m
            return _m.main(["audit"] + argv[1:])
        import repurposing_shareable_package as _m
        return _m.main(argv[1:])
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0], formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", nargs="?", choices=["run", "check", "positions", "titles", "viewports"], help="(also: audit-shareable, package: see the module docstring) run: write the view; check: exit 1 if a file is stale; positions: print one TSV line per card x need with the inputs and the position (for re-derivation); titles: report (or with --refresh, fill) the source-title cache; viewports: measure the page at 360/390/768/1280 px with a real device-metrics emulation")
    ap.add_argument("--dr", type=Path, default=DEFAULT_DR, help="drug_repurposing directory (default: the module)")
    ap.add_argument("--source", choices=list(SOURCES), default=None,
                    help="run: full (default) embeds every row, written to view/index.html; shareable embeds only allowlisted rows (view/shareable_sources.json), written to view/index_shareable.html. check: both unless given")
    ap.add_argument("--out", type=Path, default=None, help="output file (default: <dr>/view/index.html or index_shareable.html); with check and no --source, only valid for one source")
    ap.add_argument("--refresh", action="store_true", help="titles: fetch the missing titles (NCBI esummary, keyless, one call per 100 ids, no e-mail or tool parameter) into view/source_titles.json")
    ap.add_argument("--refetch", action="store_true", help="titles --refresh: fetch every referenced PMID again, not only the missing ones")
    ap.add_argument("--shots", type=Path, default=None, help="viewports: directory for screenshots (omit for measurements only)")
    a = ap.parse_args(argv)
    if not a.command:
        ap.print_help()
        return 0
    if a.command == "titles":
        ids = referenced_pmids(a.dr)
        if a.refresh:
            doc = refresh_titles(a.dr, ids, refetch=a.refetch)
            have = doc["titles"]
        else:
            have = (jload(a.dr / TITLES_NAME).get("titles") if (a.dr / TITLES_NAME).exists() else {}) or {}
        miss = [i for i in ids if i not in have]
        print(f"{len(ids)} referenced PMIDs; {len(ids) - len(miss)} titled in {TITLES_NAME}; {len(miss)} without a title" + (": " + ", ".join(miss) if miss else ""))
        return 0 if (not miss or not a.refresh) else 1
    if a.command == "viewports":
        src = a.source or "shareable"
        out = a.out or (a.dr / "view" / OUT_NAME[src])
        if not find_chromium():
            print("SKIP: no Chromium binary found; no viewport was measured")
            return 0
        res = measure_viewports(out.resolve(), a.shots)
        print("requested\tmobile_emulation\tinnerWidth\tscrollWidth\tvisualViewport\toverflow\tscenario\tnote")
        print("# first screen: bottom of the F/C/P legend (css px from the top) against the viewport height: " + ", ".join(f'{m["requested"]}x{h}: {m["legendBottom"]}' for m in res for (w, h, _mob) in VIEWPORTS if m["scenario"] == "first_screen" and m["mobile"] and w == m["requested"] and m["requested"] <= 390))
        bad = 0
        for m in res:
            bad += bool(m["overflow"])
            print(f'{m["requested"]}\t{m["mobile"]}\t{m["innerWidth"]}\t{m["scrollWidth"]}\t{m["visualViewportWidth"]}\t{"OVERFLOW" if m["overflow"] else "ok"}\t{m["scenario"]}\t' + ("; ".join(m["offenders"]) or (f'pdf pages {m["pdf_pages"]}' if "pdf_pages" in m else "")))
        return 1 if bad else 0
    if a.command == "positions":
        cur = build_payload(a.dr, a.source or "full")["cur"]
        nm = {n["id"]: n for n in cur["needs"]}
        print("\t".join(["card", "need", "result_in_wwox", "depth_class", "position", "kind", "counter_in_rows", "criteria_not_met"]))
        for c in cur["cands"]:
            for nid, l in c["links"].items():
                print("\t".join([c["id"], nid, l["result"], l["depth_class"], l["group"], l["kind"], str(l["counter_in_rows"]), "; ".join(x["text"] for x in l["criteria"] if not x["met"])]))
            if not c["links"]:
                print("\t".join([c["id"], "(no linked need)", "", "", "", "", "", ""]))
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
