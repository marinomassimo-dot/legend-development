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
    "data_date": "Data dei dati",
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
    "ex_card": "Scheda", "ex_data_date": "Data dei dati", "ex_needs_rec": "registro dei bisogni", "ex_cat_build": "versione del catalogo",
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
    "bf_f1": "Domanda (il bisogno)", "bf_f2": "Candidato / intervento", "bf_f3": "Risultato WWOX", "bf_f4": "Precedente esterno", "bf_f5": "Controevidenza decisiva",
    "bf_f6": "Dato mancante", "bf_f7": "Prossimo passo", "bf_f8": "Fonti essenziali (al massimo 5)",
    "bf_f5_note": "la prima voce che la scheda o il bisogno elencano; non è un giudizio di peso",
    "bf_counter_more": "altre voci nel dossier completo: {n}",
    "bf_data_date": "Data dei dati", "bf_cat_build": "Costruzione del catalogo", "bf_dates_note": "due date diverse: la prima è l'ultimo aggiornamento dei dati, la seconda la costruzione del catalogo dei composti",
    "bf_dossier": "Dossier completo (3-4 pagine, appendice)", "bf_dossier_open": "Apri il dossier completo",
    "bf_dossier_std": "Nel file autonomo il dossier completo non è incluso: si apre dalla pagina principale con",
    "bf_warn": "Materiale di ricerca per la discussione con il team clinico curante: non è consiglio medico e non è una graduatoria di trattamenti. Associazione non è modulazione, e modulazione non è recupero.",
    "bf_wwox_ctx": "Nessun risultato dell'intervento in un sistema WWOX; osservazione del bisogno collegato",
    "bf_wwox_none": "Nessun risultato in un sistema WWOX registrato",
    "bf_ext_none": "Nessun precedente esterno registrato (l'assenza non è un risultato negativo)",
    "bf_counter_none": "Nessuna elencata nella scheda (l'assenza non è un risultato negativo)",
    "bf_missing_none": "Nessun dato mancante indicato dalla scheda", "bf_next_none": "Nessun passo successivo nella scheda",
    "bf_src_none": "Nessuna fonte con identificativo pubblico", "bf_unknown": "Identificativo di scheda sconosciuto.", "bf_no_need": "nessun bisogno collegato",
    # IT6 P13: small evidence graph (server-rendered SVG)
    "nav_chains": "Catene",
    "eg_h": "Catene decisive: dall'osservazione all'esperimento",
    "eg_lead": "Cinque catene dei cicli dell'iterazione 6, lette da sinistra a destra: osservazione in un sistema WWOX, bisogno, meccanismo, intervento, evidenza, esperimento. Non è una rete di conoscenza e non misura l'efficacia: mostra su che cosa poggia ogni passaggio e che cosa manca.",
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
    "eg_date": "Catene scritte il", "eg_open_card": "apri il profilo",
    # IT6 P13: updated priorities and order of work
    "wo_h": "Ordine di lavoro: che cosa verificare, bisogno per bisogno",
    "wo_note": "Un elenco per bisogno, nell'ordine del registro dei bisogni: non è una graduatoria di bisogni né di trattamenti e non ha punteggio. Per ogni bisogno: il motivo del prossimo studio (verificare un'ipotesi, chiarire una controevidenza o risolvere una premessa, coerente con le posizioni F, C, P del bisogno), la domanda, i dati che potrebbero risolverla, che cosa cambierebbe e la fattibilità realmente nota («non nota» quando non lo è).",
    "wo_update": "Aggiornamento della ricerca", "wo_catalogue": "Costruzione del catalogo", "wo_dates_note": "due date diverse: la prima è l'ultimo aggiornamento di questo ordine di lavoro, la seconda la costruzione del catalogo dei composti",
    "wo_kind": "Motivo del prossimo studio", "wo_q": "Domanda", "wo_data": "Dati che potrebbero risolverla", "wo_change": "Che cosa cambierebbe", "wo_feas": "Fattibilità realmente nota",
    "wo_date": "Data", "wo_upd": "Aggiornato da", "wo_cards": "Schede coinvolte", "wo_pos": "Posizioni del bisogno", "wo_no_pos": "nessuna scheda collegata",
    "wo_see": "ordine di lavoro di questo bisogno", "wo_text_en": "Testo scientifico in inglese, come memorizzato.", "wo_more": "Dettagli: dati, effetto, fattibilità",
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
WO_KEYS = {"need", "kind", "question", "data", "would_change", "feasibility", "date", "updated_by", "cards", "docs"}
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


def validate_work_order(doc: dict, need_ids: list, groups_by_need: dict, card_ids, dr: Path | None = None) -> list[str]:
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
        for k in ("question", "data", "would_change", "feasibility"):
            if not str(e.get(k) or "").strip():
                errs.append(f"{w}: {k} is empty (write 'non nota' when feasibility is not known)")
        if not ISO_DATE_RE.match(str(e.get("date") or "")):
            errs.append(f"{w}: date must be an ISO date")
        if e.get("kind") not in WO_KINDS:
            errs.append(f"{w}: kind {e.get('kind')!r} is not one of {WO_KINDS}")
        elif e["kind"] not in allowed_kinds(groups_by_need.get(nid) or ()):
            errs.append(f"{w}: kind {e['kind']!r} does not agree with the positions of the need {sorted(groups_by_need.get(nid) or [])}")
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
                "positions": sorted(groups_by_need.get(e["need"]) or [])} for e in doc["entries"]]
    return {"research_update": doc["research_update"], "kinds": list(WO_KINDS), "entries": entries}


def load_curated_docs(dr: Path, cands: list, cneeds: list, titles: dict) -> tuple[dict, dict]:
    """Reads and validates view/evidence_graph.json and view/work_order.json against the cards, the needs and the title cache. An invalid file is a build error, never a silent omission."""
    card_ids = [c["id"] for c in cands]
    need_ids = [n["id"] for n in cneeds]
    groups: dict = {n: set() for n in need_ids}
    for c in cands:
        for nid, l in c["links"].items():
            groups[nid].add(l["group"])
    out = []
    for name, fn, args in ((GRAPH_NAME, validate_evidence_graph, (card_ids, need_ids, titles, dr)), (WORK_ORDER_NAME, validate_work_order, (need_ids, groups, card_ids, dr))):
        p = dr / name
        if not p.exists():
            raise SystemExit(f"{name} is missing: the evidence graph and the work order are part of the view")
        doc = jload(p)
        errs = fn(doc, *args)
        if errs:
            raise SystemExit(f"{name} is invalid:\n  " + "\n  ".join(errs))
        out.append(doc)
    return resolve_graph(out[0], titles), resolve_work_order(out[1], groups)


def make_brief(c: dict, nmap: dict) -> dict:
    """The one-page synthesis of a card: fields assembled from the card and its needs only (no new claim). Fallback sentences are Italian orientation text; everything else is the stored scientific text."""
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

    def fa(a):
        return a["text"] + (" – " + clip(a["note"], 150) if a.get("note") else "") + (f" [{a['species']}]" if a.get("species") else "")
    if own:
        wwox = " | ".join(fa(a) for a in own[:2])
    elif w_obs:
        wwox = U["bf_wwox_ctx"] + ": " + clip(w_obs[0]["short"], 240)
    else:
        wwox = U["bf_wwox_none"]
    ext_items = [fa(a) for a in other[:2]] + [o["short"] for o in o_obs[:1]]
    external = " | ".join(ext_items[:2]) if ext_items else U["bf_ext_none"]
    cnt = [clip(t, 360) for t in c["against"]] + [clip(t, 360) for n in order for t in nmap[n]["counter"]] + [fa(a) for a in safety]
    if cnt:
        counter, more = cnt[0], len(cnt) - 1
    elif c.get("against_note"):
        counter, more = clip(c["against_note"], 360), 0
    else:
        counter, more = U["bf_counter_none"], 0
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
    return {"wwox": clip(wwox, 460), "external": clip(external, 340), "counter": counter, "counter_more": more,
            "missing": clip(c["missing"], 260) if c.get("missing") else U["bf_missing_none"],
            "next": clip(c["next_full"], 380) if c.get("next_full") else U["bf_next_none"], "sources": sources}


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
                            "depth": a.get("reading_depth"), "sign": (pr or {}).get("sign"), "kind": (pr or {}).get("evidence_kind"), "pmids": ids})
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
    eg, wo = load_curated_docs(dr, cands, cneeds, titles)
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
__BANNER__<nav aria-label="__NAVLABEL__"><div class="in"><a href="#overview">__N_OV__</a><a href="#threads">__N_TH__</a><a href="#chains">__N_EG__</a><a href="#charts">__N_CH__</a><a href="#navigate">__N_NAV__</a><a href="#candidates">__N_CA__</a><a href="#priorities-cur">__N_PR__</a><a href="#compare">__N_CP__</a><a href="#technical">__N_TD__</a></div></nav>
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
        f'<p class="meta-line"><b>{E(U["data_date"])}:</b> <span data-k="meta.data_date" data-v="{E(str(dd))}">{E(str(dd))}</span> · <b>{E(U["perimeter"])}:</b> {E(U["perimeter_txt"])} · {E(srcnote)}</p>'
        f'<h3 id="threads">{E(U["th_h"])}</h3><p class="mini mut">{E(U["th_note"])}</p><div class="threads">' + "".join(cards) + '</div>'
        f'<h3>{E(U["goals_h"])}</h3><p class="mini mut">{E(U["goals_note"])} {E(U["goal_cross"].format(total=n_links, cross=n_cross))}</p><div class="goals">' + "".join(panels) + '</div>'
        f'<h3>{E(U["facts_h"])}</h3><div class="tiles">' + tiles + f'</div><p class="mini mut">{E(U["unit_note"])}</p></section>')


# ------------------------------------------------------------------ IT6 P13: server-rendered evidence graph (inline SVG) and work order
EG_COLW, EG_PITCH, EG_PADX, EG_HEADH, EG_LINEH, EG_PADY, EG_GAP, EG_CHARS = 150, 176, 8, 30, 13, 6, 14, 22


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
        tag_lines = _wrap(tag, 26) if tag else []
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
            f'<p class="mini">{E(ch["question"])}</p><div class="eg-fig" tabindex="0" role="group" aria-label="{E(ch["title"])}">{render_chain_svg(ch)}</div>'
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
        upd = (f'<dt>{E(U["wo_upd"])}</dt><dd>{E(", ".join(e["updated_by"]))}</dd>') if e["updated_by"] else ""
        cards = ", ".join(E(c) for c in e["cards"])
        items.append(
            f'<article class="wo-item" id="wo-{E(e["need"])}" data-need="{E(e["need"])}" data-kind="{E(e["kind"])}"><h4>{E(NEED_IT.get(e["need"], n["short"]))} <span class="mut">{E(e["need"])}</span></h4>'
            f'<div class="wo-meta"><span class="chip wo-k wo-k-{kcls[e["kind"]]}" title="{E(U["wo_kind"])}">{E(U["wo_kind"])}: <b>{E(e["kind"])}</b></span> <span class="mini mut">{E(U["wo_pos"])}:</span> {pos}</div>'
            f'<p class="wo-q"><b>{E(U["wo_q"])}.</b> {E(e["question"])}</p>'
            f'<details class="inl"><summary>{E(U["wo_more"])}</summary><dl class="wo-dl"><dt>{E(U["wo_data"])}</dt><dd>{E(e["data"])}</dd><dt>{E(U["wo_change"])}</dt><dd>{E(e["would_change"])}</dd>'
            f'<dt>{E(U["wo_feas"])}</dt><dd class="wo-feas">{E(e["feasibility"])}</dd><dt>{E(U["wo_date"])}</dt><dd>{E(e["date"])}</dd>{upd}<dt>{E(U["wo_cards"])}</dt><dd>{cards}</dd></dl>'
            f'<p class="mini mut">{E(U["wo_text_en"])}</p></details></article>')
    return (f'<div id="work-order" class="wo-wrap"><h3>{E(U["wo_h"])}</h3><p class="note">{E(U["wo_note"])}</p>'
            f'<p class="meta-line"><b>{E(U["wo_update"])}:</b> <span data-k="cur.work_order_date" data-v="{E(wo["research_update"])}">{E(wo["research_update"])}</span> · <b>{E(U["wo_catalogue"])}:</b> <span data-k="cur.catalogue_generated" data-v="{E(cat)}">{E(cat)}</span> <span class="mini mut">({E(U["wo_dates_note"])})</span></p>'
            + "".join(items) + '</div>')


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
    cur_html = cur_html.replace("__OVERVIEW__", render_overview(P)).replace("__GRAPH__", render_evidence_graph(P)).replace("__WORKORDER__", render_work_order(P)).replace("__CHARTS__", render_charts(P))
    page = page.replace("__CSS__", CSS + read_asset(dr, "curated.css")).replace("__JS__", JS).replace("__CJS__", read_asset(dr, "curated.js"))
    page = page.replace("__CURATED__", cur_html).replace("__FOOTER__", render_footer(P))
    for k, key in (("TITLE", "page_title"), ("SKIP", "skip"), ("H1", "h1"), ("SUB", "sub"), ("NAVLABEL", "nav_label"), ("N_OV", "nav_overview"), ("N_TH", "nav_threads"), ("N_EG", "nav_chains"), ("N_CH", "nav_charts"), ("N_NAV", "nav_navigate"),
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
            ("brief", "#brief=" + longest), ("evidence_graph", "#chains"), ("work_order", "#work-order")]


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
                        anchor = {"comparison": "#compare", "filtered_thread": "#navigate", "technical_open": "#tech-versions", "export_card": "body", "evidence_graph": "#chains", "work_order": "#work-order"}.get(name, "body")
                        y = cdp.evaluate("(function(){var e=document.querySelector(%s);return e?Math.max(0,Math.round(e.getBoundingClientRect().top+scrollY)-8):0})()" % json.dumps(anchor))
                        lm = cdp.call("Page.getLayoutMetrics")["cssContentSize"]
                        tall = name in ("export_card", "comparison", "brief", "evidence_graph") and w <= 390
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
            for name, frag in (("print_first_screen", ""), ("print_export_card", sc_by["export_card"]), ("print_brief", sc_by["brief"]), ("print_brief_all", "#brief=" + ",".join(c["id"] for c in P["cur"]["cands"]))):
                cdp.call("Page.navigate", url="about:blank")
                cdp.events.clear()
                cdp.call("Page.navigate", url=f"file://{html_path}{frag}")
                cdp.wait_event("Page.loadEventFired")
                cdp.evaluate("new Promise(function(r){setTimeout(r,500)})")
                m = cdp.evaluate(MEASURE_JS.replace("__REQ__", "794"))
                pdf = cdp.call("Page.printToPDF", paperWidth=8.27, paperHeight=11.69, printBackground=True, preferCSSPageSize=True)
                raw = base64.b64decode(pdf["data"])
                m.update({"requested": 794, "scenario": name, "mobile": False, "overflow": m["scrollWidth"] > 794 or m["innerWidth"] > 794, "pdf_pages": len(re.findall(rb"/Type\s*/Page[^s]", raw)), "pdf_bytes": len(raw)})
                if shots and name in ("print_export_card", "print_brief"):
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
