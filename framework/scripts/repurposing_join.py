#!/usr/bin/env python3
"""The join: LEGEND's own receipted evidence bound to the external sources, one command.

    repurposing_join.py run [--axis NAME] [--live] [--out DIR]

This is the part of the repurposing module that nothing outside LEGEND can have. It is
deterministic (same inputs, same bytes), re-runnable, and incremental: `run` compares its output
with the previous state file and prints what changed — ADDED / CHANGED / UNCHANGED / REMOVED per
query and per card — so refreshing after a Scientist batch is one command and reads as a diff.

Four stages, each written to the output directory as plain JSON:

  1. QUERIES — derived from the claim registry, the discovery ledger, the mechanism-intervention
     map's repurposing records and the pathograph export. Every query carries the record it came
     from: id, repo-relative file and line. No query is typed by hand.
  2. EVIDENCE — per query, from the receipt ledger and the deep-dive manifests: reading depth,
     locator count (len(entries), never len(mapping)), and the audit status of what the locators
     declare — a `contradicts_locator` verdict with its auditor count, zero auditors meaning
     UNAUDITED, plus any page_adjudications file naming that paper. External hits are labelled
     NOT WWOX EVIDENCE and never substituted for this table.
  3. CARDS — composed by `repurposing_bridge.build_card` from the evidence table plus the adapter
     hits. Derived, never typed, so a card cannot drift from the manifests it rests on.
  4. MEASURE NEXT — per card: the single measurement that would split the dependence (when every
     assertion rests on one reading, that is the dependence), a one-line experiment sketch, and
     the claim or lead the measurement would move.

Nothing here is medical advice, no dose or administration is emitted, nothing is scored or
ranked, and abstention is a first-class output. The four scientific current files are read and
never written.
"""
from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import json
import re
import sys
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import registry_records as rr  # noqa: E402  the routed way to read a registry, never grep
import repurposing_bridge as bridge  # noqa: E402
import repurposing_adapter as adapters  # noqa: E402
import eutils  # noqa: E402  the shared, polite NCBI door (throttle + cache); no key, no e-mail

ROOT = HERE.parents[1]
DISEASE = "wwox"
MODEL = ROOT / "disease-models" / DISEASE
DEFAULT_OUT = MODEL / "research" / "drug_repurposing" / "join"
MECHANISM_MAP = MODEL / "analysis" / "mechanism_intervention_map.md"
CURATED_CARDS = MODEL / "research" / "drug_repurposing" / "cards"  # hand-made, qualified cards (the `<id>.packet.json` is read)
CURATED_CARDS_EARLY = MODEL / "research" / "drug_repurposing" / "cards_early"  # the early-benefit cards (ids carry a hyphen)
PATHOGRAPH = MODEL / "analysis" / "data" / "pathograph_export.jsonl"
MANIFESTS = MODEL / "research" / "deepdive_manifests"
ADJUDICATIONS = MODEL / "research" / "page_adjudications"
RECEIPT_LEDGER = MODEL / "registries" / "fulltext_read_receipts.jsonl"  # fulltext_receipts.default_ledger_path

# The axes the mandate calls live (three) plus the early-benefit row. Plain data: delete a row and the axis is gone.
AXES = {
    "proteostasis": ["proteostasis", "chaperone", "phenylbutyrate", "misfolding", "SDR", "missense",
                     "proteasome", "HSP70", "UPR", "ERAD", "solubility"],
    "calcium": ["T-type", "CACNA1G", "CACNA1H", "CACNA1I", "calcium channel", "Ca2+", "Ca²⁺",
                "ethosuximide", "bursting", "NMDAR", "network"],
    "wnt": ["Wnt", "MYC", "GSK3", "mTOR", "beta-catenin", "β-catenin", "tankyrase", "lithium",
            "rapamycin", "everolimus"],
    # One data row from the Scientist's early-benefit candidate file (blind spots, 2026-10-23); `growth`
    # is left out on purpose: it matches pathograph lines about body weight.
    "early_benefit": ["vigabatrin", "ketogenic", "ethosuximide", "cannabidiol", "ACTH", "corticosteroid",
                      "epileptic spasm", "seizure control", "early benefit"],
}

# Tokens that look like a gene symbol but are this repository's own vocabulary, a unit, or an
# epistemic tag. Explicit, because a silent filter is a measurement nobody can check.
STOPWORDS = {
    "DATO", "INFERENZA", "IPOTESI", "ESPANSIONE", "CLAIM", "PAPER", "PMID", "PMC", "DOI", "LIT",
    "BATCH", "WM", "FTR", "CC", "LEGEND", "UNKNOWN", "NOT", "AND", "THE", "FOR", "WITH", "ONLY",
    "DNA", "RNA", "MRI", "DTI", "EEG", "ECOG", "SWD", "KO", "WT", "LD", "HD", "ICV", "QPCR",
    "TIER", "REVIVAL", "TRIGGER", "PREMISE", "TAG", "BLOCCO", "BLOCK", "SPLIT", "READY", "GAP",
    "NO", "YES", "NONE", "ALL", "ANY", "ONE", "TWO", "NEW", "OLD", "SEE", "PER", "VIA", "VS",
}
HOPS = 3  # rounds of record-to-record inheritance; D measured the fixed point inside three
HIT_CAP = 100  # hits kept per cached adapter response; the total before the cap is recorded
GENE_TOKEN = re.compile(r"\b[A-Z][A-Z0-9]{2,7}\b")
PMID_IN_TEXT = re.compile(r"\bPMID[\s:_-]*(\d{6,9})\b")
CLAIM_IN_TEXT = re.compile(r"\bCLAIM[ _](\d{3})\b")
LEAD_IN_TEXT = re.compile(r"\b(DL-[A-Z]+-\d{3})\b")
PAPER_IN_TEXT = re.compile(r"\bPAPER[ _](\d{3})\b")
MECHANISM_RECORD = re.compile(r"^### ([RN]-\d{2}) — (.+?)$", re.M)
CARD_REF = re.compile(r"cards(?:_early)?/([A-Za-z0-9_-]+)\.card\.json")  # a map record names its curated card by path
LOCATOR_ENTRIES = re.compile(r"PMID(\d+)\.json verbatim_locators\.entries((?:\s*\[\d+\],?)+)")
RECEIPT_ID = re.compile(r"FTR-\d{8}-\d{8}-\d{2}")
MAP_FIELD = re.compile(r"^\|\s*\*\*([A-Z_]+)\*\*\s*\|\s*(.+?)\s*\|\s*$", re.M)


# ---------------------------------------------------------------- small shared helpers

def digest(value) -> str:
    raw = json.dumps(value, sort_keys=True, ensure_ascii=False, allow_nan=False).encode()
    return hashlib.sha256(raw).hexdigest()[:16]


def gene_tokens(text: str, limit: int = 6) -> list[str]:
    seen: list[str] = []
    for token in GENE_TOKEN.findall(text):
        if token in STOPWORDS or token in seen:
            continue
        seen.append(token)
        if len(seen) >= limit:
            break
    return seen


def record_fields(text: str) -> dict[str, str]:
    """The declared `(name, value)` pairs of a record — `registry_records.declared_fields` reads
    ONE line, so the record is walked line by line and the first declaration of a name wins."""
    fields: dict[str, str] = {}
    for line in text.splitlines():
        for name, value in rr.declared_fields(line) + rr.declared_fields(line, bulleted=True):
            fields.setdefault(name, value)
    return fields


def relative(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


# ---------------------------------------------------------------- 1 · queries

def claim_queries(root: Path) -> list[dict]:
    out = []
    for record in rr.parse_records(root, DISEASE, "claim_registry_current"):
        if record.kind != "record" or not record.record_id.upper().startswith("CLAIM"):
            continue
        fields = record_fields(record.text)
        title = fields.get("Title", "")
        terms = gene_tokens(title + " " + fields.get("Pathway", ""))
        out.append({"query_id": f"Q-{record.record_id.replace(' ', '')}",
                    "kind": "claim", "origin_id": record.record_id,
                    "origin_file": record.path, "origin_line": record.line,
                    "origin_title": title[:300],
                    "terms": terms,
                    "papers_named": sorted({f"PAPER {n}" for n in PAPER_IN_TEXT.findall(record.text)}),
                    "pmids": sorted(set(PMID_IN_TEXT.findall(record.text)))})
    return out


def paper_pmids(root: Path) -> dict[str, list[str]]:
    """PAPER id -> the PMIDs its registry record declares in `Identifier`. Read by record with
    the routed parser (never grep): the registries cite papers by PAPER id far more often than
    by PMID, so without this map most claims and leads would look unreceipted."""
    out: dict[str, list[str]] = {}
    for record in rr.parse_records(root, DISEASE, "paper_registry_current"):
        if record.kind != "record" or not record.record_id.upper().startswith("PAPER"):
            continue
        fields = record_fields(record.text)
        found = PMID_IN_TEXT.findall(fields.get("Identifier", "")) or PMID_IN_TEXT.findall(record.text[:600])
        # A PAPER record that cites no PMID stays in the map with an empty list: it EXISTS, and the
        # abstention must be able to tell "no paper cited" from "no such record".
        out[rr.identity_token(record.record_id)] = sorted(set(found))
    return out


def lead_queries(root: Path) -> list[dict]:
    out = []
    for record in rr.parse_records(root, DISEASE, "discovery_ledger_current"):
        # The id is what the heading carries after ANY leading marker (red, star, target, warning,
        # medal ... — 7 of 226 leads were dropped when only the red circle was stripped).
        if record.kind != "record" or not rr.identity_token(record.record_id).startswith("DL-"):
            continue
        fields = record_fields(record.text)
        causal = fields.get("Causal statement", "") or fields.get("Catena di ragionamento", "")
        out.append({"query_id": f"Q-{rr.identity_token(record.record_id)}",
                    "kind": "lead", "origin_id": rr.identity_token(record.record_id),
                    "origin_file": record.path, "origin_line": record.line,
                    "origin_title": record.record_id[:300],
                    "terms": gene_tokens(record.record_id + " " + causal),
                    "claims_named": sorted({f"CLAIM {n}" for n in CLAIM_IN_TEXT.findall(record.text)}),
                    "leads_named": sorted(set(LEAD_IN_TEXT.findall(record.text)) - {rr.identity_token(record.record_id)}),
                    "papers_named": sorted({f"PAPER {n}" for n in PAPER_IN_TEXT.findall(record.text)}),
                    "pmids": sorted(set(PMID_IN_TEXT.findall(record.text)))})
    return out


def mechanism_queries(path: Path = MECHANISM_MAP) -> list[dict]:
    """The map's repurposing records R-01.. and its negative-translation records N-01.., each
    carrying the candidate named in its own heading — the only place a candidate NAME is taken
    from, so the module never invents one."""
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8")
    starts = [(m.start(), m.group(1), m.group(2)) for m in MECHANISM_RECORD.finditer(text)]
    out = []
    for index, (offset, record_id, heading) in enumerate(starts):
        end = starts[index + 1][0] if index + 1 < len(starts) else len(text)
        body = text[offset:end]
        fields = dict(MAP_FIELD.findall(body))
        # The candidate is the name the heading opens with: everything before the first bracket
        # or the first verdict arrow, so a negative-translation heading does not carry its
        # verdict into the candidate's own name.
        candidate = re.split(r"\(|→|-->|\*\*", heading)[0].strip(" —*")
        out.append({"query_id": f"Q-{record_id}", "kind": "mechanism_record",
                    "origin_id": record_id, "origin_file": relative(path),
                    "origin_line": text[:offset].count("\n") + 1,
                    "origin_title": heading[:300], "candidate": candidate,
                    "terms": gene_tokens(heading + " " + fields.get("TARGET", "") + " " + fields.get("MECHANISM", "")),
                    "intervention": fields.get("INTERVENTION", bold_field(body, "Failure mode"))[:400],
                    "target": fields.get("TARGET", "UNKNOWN")[:300],
                    "decisive_test": fields.get("DECISIVE_PRECLINICAL_TEST",
                                                bold_field(body, "REVIVAL_TRIGGER"))[:400],
                    "record_class": "repurposing" if record_id.startswith("R-") else "negative_translation",
                    "claims_named": sorted({f"CLAIM {n}" for n in CLAIM_IN_TEXT.findall(body)}),
                    "leads_named": sorted(set(LEAD_IN_TEXT.findall(body))),
                    "papers_named": sorted({f"PAPER {n}" for n in PAPER_IN_TEXT.findall(body)}),
                    "curated_cards": sorted(set(CARD_REF.findall(body))),
                    "pmids": sorted(set(PMID_IN_TEXT.findall(body)))})
    return out


def bold_field(body: str, name: str) -> str:
    """A `**Name:**` prose field of the map's negative-translation records, which carry prose
    where the repurposing records carry a table."""
    match = re.search(rf"\*\*`?{re.escape(name)}`?:?\*\*:?\s*(.+)", body)
    return match.group(1).strip() if match else "UNKNOWN"


def pathograph_queries(path: Path = PATHOGRAPH, limit: int = 40) -> list[dict]:
    """Relational propositions the export already bound to a claim: the mechanism lines LEGEND
    declares. Capped, sorted, and every row names the claim it was bound to."""
    if not path.exists():
        return []
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        try:
            record = json.loads(line)
        except ValueError:
            continue
        if record.get("kind") != "relational_proposition":
            continue
        claims = record.get("bound_claims") or []
        if not claims:
            continue
        split = record.get("lexical_split") or {}
        rows.append({"claim": sorted(str(claim) for claim in claims)[0],
                     "claims": sorted(str(claim) for claim in claims),
                     "text": str(record.get("text") or "")[:400],
                     "candidate_id": str(record.get("candidate_id") or ""),
                     "source_ref": str(record.get("source_ref") or ""),
                     "left": str(split.get("left") or ""), "right": str(split.get("right") or ""),
                     "relation": str(record.get("connective_class") or record.get("lexicon_class") or "UNTYPED"),
                     "review_state": str(record.get("review_state") or "")})
    # CAUSAL lines first, then associative: a causal line is what a mechanism query wants, and
    # the export is explicit that an UNTYPED or ASSOCIATIVE edge is not a causal claim.
    rows.sort(key=lambda row: (row["relation"] != "CAUSAL", row["claim"], row["candidate_id"]))
    out = []
    for row in rows[:limit]:
        out.append({"query_id": f"Q-PG-{row['candidate_id'][-12:] or digest(row)}",
                    "kind": "mechanism_line",
                    "origin_id": row["claim"], "origin_file": relative(path),
                    "origin_line": 0, "origin_title": row["text"],
                    "terms": gene_tokens(f"{row['left']} {row['right']} {row['text']}"),
                    "relation_type": row["relation"], "review_state": row["review_state"],
                    "bound_claims": row["claims"], "bound_from": row["source_ref"],
                    # `bound_from` names the manifest (PMIDnnnnnnnn.json|entries[i]) or the registry
                    # heading the line was bound from: it is evidence the line carries, so it is read.
                    "pmids": sorted(set(PMID_IN_TEXT.findall(row["text"])) | set(PMID_IN_TEXT.findall(row["source_ref"])))})
    return out


def derive_queries(root: Path = ROOT, axis: str = "") -> list[dict]:
    claims = claim_queries(root)
    leads = lead_queries(root)
    queries = claims + leads + mechanism_queries() + pathograph_queries()
    # The leverage: a lead, a map record or a pathograph line that names a claim or a lead
    # inherits that record's receipted papers, so its evidence table is the evidence LEGEND
    # already holds, not an empty one. Up to HOPS hops, and the route is written into the query
    # (`pmids_via_records`) so a reader sees where each paper came from.
    papers = paper_pmids(root)
    # First hop: every query resolves the PAPER ids it names itself.
    for query in queries:
        own = {pmid: [paper] for paper in query.get("papers_named") or [] for pmid in papers.get(paper, [])
               if pmid not in query["pmids"]}
        if own:
            query["pmids_via_records"] = {pmid: names for pmid, names in sorted(own.items())}
            query["pmids"] = sorted(set(query["pmids"]) | set(own))
    # Following hops (at most HOPS rounds): a record that names a claim or a lead inherits that
    # record's papers, and a lead that cites a lead passes the papers on. A pathograph line IS bound
    # to the claim it names, so only a claim or lead is barred from naming itself.
    record_query = {claim["origin_id"]: claim for claim in claims}
    record_query.update({lead["origin_id"]: lead for lead in leads})
    for _ in range(HOPS):
        grew = False
        for query in queries:
            named = (list(query.get("claims_named") or []) + list(query.get("bound_claims") or [])
                     + list(query.get("leads_named") or []))
            if query["kind"] in ("claim", "lead"):
                named = [name for name in named if name != query["origin_id"]]
            inherited = {}
            for name in named:
                for pmid in (record_query.get(name) or {}).get("pmids", []):
                    if pmid not in query["pmids"]:
                        inherited.setdefault(pmid, []).append(name)
            if inherited:
                grew = True
                via = dict(query.get("pmids_via_records") or {})
                for pmid, names in inherited.items():
                    via[pmid] = sorted(set(names))
                query["pmids_via_records"] = dict(sorted(via.items()))
                query["pmids"] = sorted(set(query["pmids"]) | set(inherited))
        if not grew:
            break
    # What each query could name and what that reached: the abstention (stage 2) reads this, so a
    # record with no paper says WHICH link is missing, not only that nothing was found.
    for query in queries:
        names = sorted(set(query.get("claims_named") or []) | set(query.get("bound_claims") or [])
                       | set(query.get("leads_named") or []) | set(query.get("papers_named") or []))
        known = {name: (name in record_query or name in papers) for name in names}
        reached = {name for name in names if (record_query.get(name) or {}).get("pmids") or papers.get(name)}
        query["linkage"] = {"ids_named": names,
                            "ids_reaching_a_pmid": sorted(reached),
                            "ids_in_registry_without_pmid": sorted(n for n in names if known[n] and n not in reached),
                            "ids_not_found_in_registry": sorted(n for n in names if not known[n])}
    if axis:
        wanted = [term.lower() for term in AXES[axis]]
        queries = [q for q in queries
                   if any(term in json.dumps(q, ensure_ascii=False).lower() for term in wanted)]
    for query in queries:
        query["axis"] = axis or "all"
        query["digest"] = digest({k: v for k, v in query.items() if k != "digest"})
    queries.sort(key=lambda q: q["query_id"])
    return queries


# ---------------------------------------------------------------- 2 · evidence table

def load_receipts(path: Path = RECEIPT_LEDGER) -> dict[str, list[dict]]:
    by_pmid: dict[str, list[dict]] = {}
    if not path.exists():
        return by_pmid
    for line in path.read_text(encoding="utf-8").splitlines():
        try:
            event = json.loads(line)
        except ValueError:
            continue
        pmid = str((event.get("study_id") or {}).get("pmid") or event.get("pmid") or "")
        if pmid:
            by_pmid.setdefault(pmid, []).append(event)
    return by_pmid


DEPTH_RANK = {"complete_fulltext_read": 4, "partial_fulltext_read": 3, "queried_not_full_read": 2,
              "abstract_only": 1, "retrieved_not_read": 0}


def strongest_event(events: list[dict]) -> tuple[str, str]:
    """(depth, event_id) of the strongest standing receipt; the receipt id travels with the
    depth because the bridge refuses a complete-read declaration without its receipt."""
    best, best_id, rank = "UNKNOWN", "", -1
    for event in events:
        state = str(event.get("evidence_depth") or event.get("reading_depth") or "")
        if DEPTH_RANK.get(state, -1) > rank:
            best, best_id, rank = state, str(event.get("event_id") or ""), DEPTH_RANK.get(state, -1)
    return best, best_id


def strongest_depth(events: list[dict]) -> str:
    return strongest_event(events)[0]


def adjudication_files(pmid: str) -> list[str]:
    if not ADJUDICATIONS.is_dir():
        return []
    hits = []
    for path in sorted(ADJUDICATIONS.glob("locator_audit_*.md")):
        if pmid in path.name:
            hits.append(relative(path))
            continue
        try:
            if pmid in path.read_text(encoding="utf-8"):
                hits.append(relative(path))
        except OSError:
            continue
    return hits


#: Words that say a triple FAILED, and words that say one HELD. Matched as substrings because
#: `verdicts` is not a controlled field in practice: 30 distinct strings are in use, 16 of them
#: paragraphs (`deepdive_manifest.CONTRADICTION_AUDIT_VERDICTS` carries the ratchet that holds
#: that drift from growing). Substring matching is the honest read of a field like that.
_ADVERSE_WORDS = ("OVERSHOOT", "UNDERSHOOT", "UNSUPPORTED", "NOT_IN_SOURCE", "ANCHOR_MISMATCH")
_CLEARING_WORDS = ("SUPPORTED", "SUPPORTS", "CONFIRMED", "CORRECTED", "WITHDRAWN")


def adverse_and_not_cleared(verdict: str) -> bool:
    """An audit condemned this entry and no later verdict says the repair holds.

    `SUPPORTED` is checked before the adverse words because `UNSUPPORTED` contains neither it
    nor the reverse cleanly: a verdict list reading OVERSHOOT then SUPPORTED is a repair that
    was re-judged and held, which is not this state.
    """
    text = verdict.upper()
    # UNSUPPORTED contains SUPPORTED, so it is removed before the clearing words are looked for.
    without_unsupported = text.replace("UNSUPPORTED", "")
    cleared = any(word in without_unsupported for word in _CLEARING_WORDS)
    return any(word in text for word in _ADVERSE_WORDS) and not cleared


def manifest_evidence(pmid: str) -> dict:
    """What the manifest for one paper evidences, with the audit status of its locators.

    A locator count is len(entries) — never len(mapping), the defect that cost this repository a
    day (`harness_mandate_20261022.md` § 6)."""
    path = MANIFESTS / f"PMID{pmid}.json"
    row = {"pmid": pmid, "manifest": relative(path) if path.exists() else "",
           "locator_count": 0, "audited_entries": 0, "unaudited_contradictions": 0,
           "repair_unverified": 0,
           "contradiction_verdicts": [], "adjudication_files": adjudication_files(pmid)}
    if not path.exists():
        row["audit_status"] = "NO_MANIFEST"
        return row
    try:
        manifest = json.loads(path.read_text(encoding="utf-8"))
    except ValueError:
        row["audit_status"] = "MANIFEST_UNREADABLE"
        return row
    entries = (manifest.get("verbatim_locators") or {}).get("entries") or []
    row["locator_count"] = len(entries)
    for entry in entries:
        declaration = entry.get("contradicts_locator")
        if not isinstance(declaration, dict):
            continue
        # Real manifests nest the audit: contradicts_locator.audit.{auditors:int, verdicts:[...]}
        # (locator_contradiction_audit.py). The flat shape is read too, for older manifests.
        audit = declaration.get("audit") if isinstance(declaration.get("audit"), dict) else declaration
        auditors = audit.get("auditors")
        count = len(auditors) if isinstance(auditors, list) else int(auditors or 0)
        verdicts = audit.get("verdicts")
        if not isinstance(verdicts, list):
            verdicts = [audit.get("verdict")] if audit.get("verdict") else []
        verdict = "/".join(str(v) for v in verdicts) or "UNSTATED"
        row["contradiction_verdicts"].append({"verdict": verdict, "auditors": count})
        if not count:
            row["unaudited_contradictions"] += 1
        elif adverse_and_not_cleared(verdict):
            # Condemned, repaired, never re-judged. `auditors` is 1 because of the audit that
            # found the defect, so this used to read as audited and the debt was invisible: a
            # held research candidate sat three days on exactly this, and only a hand check
            # found it (measured 2026-10-24: 178 entries across 71 manifests).
            row["repair_unverified"] += 1
        else:
            row["audited_entries"] += 1
    row["audit_status"] = ("AUDIT_FILE_PRESENT" if row["adjudication_files"]
                           else "CONTRADICTIONS_AUDITED" if row["audited_entries"] and not row["unaudited_contradictions"]
                           else "UNAUDITED" if row["locator_count"]
                           else "NO_LOCATORS")
    return row


# ---- the bound paper of a one-paper query: is it a primary article, and does it contain the endpoint?

NOT_PRIMARY = {"Review", "Systematic Review", "Meta-Analysis", "Editorial", "Comment", "Letter", "News",
               "Published Erratum", "Retraction of Publication", "Biography", "Interview", "Guideline",
               "Practice Guideline", "Introductory Journal Article", "Preprint"}
GENERIC = {"first", "then", "measure", "measured", "state", "versus", "with", "same", "only", "model",
           "arm", "design", "dose", "dosing", "rescue", "between", "from", "that", "this", "into"}
BOLD = re.compile(r"\*\*(.+?)\*\*")


def endpoint_terms(query: dict) -> list[str]:
    """The words of the endpoint the record itself puts in bold in its decisive test (or revival
    trigger). Empty when the record states none: then the binding is UNDECLARED, never guessed."""
    words: list[str] = []
    for span in BOLD.findall(query.get("decisive_test") or ""):
        for word in re.findall(r"\w{4,}", span.casefold()):
            if word not in GENERIC and word not in words:
                words.append(word)
    return words


def fetch_pubmed_record(pmid: str) -> dict:
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&retmode=xml&id={pmid}"
    code, body = eutils.fetch(url)
    if code != 200:
        return {"pmid": pmid, "status": "QUERY_ERROR", "error": f"HTTP {code}"}
    try:
        article = ET.fromstring(body).find(".//PubmedArticle")
    except ET.ParseError:
        article = None
    if article is None:
        return {"pmid": pmid, "status": "NO_MATCH_FOUND", "error": ""}
    title = "".join(article.find(".//ArticleTitle").itertext()) if article.find(".//ArticleTitle") is not None else ""
    abstract = " ".join("".join(t.itertext()) for t in article.findall(".//AbstractText"))
    return {"pmid": pmid, "status": "MATCH_FOUND", "error": "", "title": title,
            "publication_types": [t.text for t in article.findall(".//PublicationTypeList/PublicationType") if t.text],
            # a bag of words, not the abstract: enough to test a term, not a copy of the text
            "words": sorted(set(re.findall(r"\w{4,}", (title + " " + abstract).casefold()))),
            "retrieved_at": datetime.now(timezone.utc).strftime("%Y-%m-%d"), "source": "NCBI PubMed efetch"}


def bound_check(pmid: str, query: dict, cache_dir: Path, live: bool) -> dict:
    """Cheap screen of the one paper a REPLICATE row is bound to: its PubMed publication types
    (a review is not a measurement) and whether the endpoint words appear in its title/abstract.
    A screen, not a reading: the verdict lists what was found and missing so a human decides."""
    cached = cache_dir / f"{pmid}.json"
    record = None
    if cached.exists():
        record = json.loads(cached.read_text(encoding="utf-8"))
    elif live:
        record = fetch_pubmed_record(pmid)
        if record["status"] == "MATCH_FOUND":
            cache_dir.mkdir(parents=True, exist_ok=True)
            cached.write_text(json.dumps(record, indent=1, ensure_ascii=False, sort_keys=True), encoding="utf-8")
    if record is None or record["status"] != "MATCH_FOUND":
        return {"binding": "NOT_CHECKED", "reason": "offline with no cached PubMed record" if record is None
                else f"PubMed {record['status']}: {record.get('error', '')}"}
    types = record["publication_types"]
    terms = endpoint_terms(query)
    found = [t for t in terms if t in set(record["words"])]
    missing = [t for t in terms if t not in found]
    reasons = []
    if set(types) & NOT_PRIMARY:
        reasons.append(f"not a primary article (PubMed type: {', '.join(sorted(set(types) & NOT_PRIMARY))})")
    if not terms:
        reasons.append("the record declares no endpoint (no bold span in its decisive test): name the readout and its unit")
    elif missing:
        reasons.append(f"endpoint words not in its title/abstract: {', '.join(missing)}")
    return {"binding": "UNVERIFIED" if reasons else "PRIMARY_WITH_ENDPOINT_WORDS",
            "reason": "; ".join(reasons), "publication_types": types, "title": record["title"][:160],
            "endpoint_words_found": found, "endpoint_words_missing": missing,
            "retrieved_at": record["retrieved_at"], "source": record["source"]}


def abstention_for(query: dict) -> str:
    """Why a query reaches no paper, as a measured state plus the one datum that is missing.

      LINKAGE_GAP — the join cannot see a paper: the record names no identifier that reaches a
                    PMID (nothing named, or the names are not in the registry). The paper may
                    well exist; the record does not point to it.
      NO_PAPER    — the identifiers it names (or the claim/lead record itself) exist in the
                    registry and cite no PMID: the registry holds no paper for this record.

    Neither says anything about the literature: a gap in the join is not an absence in the world."""
    link = query.get("linkage") or {}
    named = link.get("ids_named") or []
    if query.get("kind") in ("claim", "lead") and not named:
        return ("NO_PAPER: the registry record itself cites no PMID or PAPER id and names no other record; "
                "missing datum: a citation in the record")
    if not named:
        return ("LINKAGE_GAP: the record names no PMID, PAPER, CLAIM or DL- id; "
                "missing datum: one identifier in the record that resolves to a PMID (the SOURCE_IDS line)")
    empty, lost = link.get("ids_in_registry_without_pmid") or [], link.get("ids_not_found_in_registry") or []
    if empty and not lost:
        return (f"NO_PAPER: the record names {', '.join(empty)}, which exist in the registry and cite no PMID; "
                "missing datum: a paper cited by any record reached")
    return (f"LINKAGE_GAP: the record names {', '.join(named)} but none reaches a PMID"
            + (f" ({', '.join(lost)} not found in the registry)" if lost else "")
            + "; missing datum: an identifier whose registry record cites a paper")


def curated_packets(query: dict) -> list[dict]:
    """The hand-made packets a map record names (`cards/<id>.card.json` in its own text). The curated
    qualifications - target, endpoint, direction, context, source, depth, locator - are read as written."""
    packets = []
    for name in query.get("curated_cards") or []:
        path = curated_packet_path(name)
        if path is not None:
            packets.append(json.loads(path.read_text(encoding="utf-8")))
    return packets


def curated_packet_path(name: str) -> Path | None:
    """`cards/` first, then `cards_early/`; the two directories never share an id."""
    for folder in (CURATED_CARDS, CURATED_CARDS_EARLY):
        path = folder / f"{name}.packet.json"
        if path.exists():
            return path
    return None


def packet_assertions(packets: list[dict]) -> tuple[list[dict], list[dict]]:
    """Disease-side and drug-side assertions of the packets, one row per id."""
    out: list[list[dict]] = [[], []]
    for packet in packets:
        diseases = packet.get("disease_assertions") or [packet.get("disease_assertion")]
        for side, rows in ((0, diseases), (1, packet.get("drug_assertions") or [])):
            for row in rows:
                if row and row["id"] not in {r["id"] for r in out[side]}:
                    out[side].append(row)
    return out[0], out[1]


def cites_reading(assertion: dict, row: dict) -> bool:
    """An assertion is about a reading when it carries that reading's receipt or names its PMID in its
    source or locator. Nothing else binds an assertion to a paper."""
    if assertion.get("receipt") and assertion["receipt"] == row.get("receipt_id"):
        return True
    text = f"{assertion.get('source', '')} {assertion.get('locator', '')}"
    return bool(re.search(rf"PMID[\s_]?{re.escape(row['pmid'])}\b", text))


def evidence_for(query: dict, receipts: dict[str, list[dict]], checks: dict[str, dict] | None = None) -> dict:
    rows = []
    curated = [a for side in packet_assertions(curated_packets(query)) for a in side]
    for pmid in query.get("pmids", []):
        events = receipts.get(pmid, [])
        row = manifest_evidence(pmid)
        if checks and pmid in checks:
            row["bound_check"] = checks[pmid]
        depth, event_id = strongest_event(events) if events else ("NO_RECEIPT", "")
        row["reading_depth"] = depth
        row["receipt_id"] = event_id
        row["receipt_events"] = len(events)
        # A receipt documents the READING. It says nothing about whether the system read is WWOX-DEE,
        # WWOX biology elsewhere, a precedent in another disease or a computation: that scope comes from
        # a curated assertion that cites the reading, and is UNQUALIFIED (said, not inferred) otherwise.
        cited = [a for a in curated if cites_reading(a, row)]
        row["evidence_scope"] = sorted({a.get("evidence_scope", "UNQUALIFIED") for a in cited}) or ["UNQUALIFIED"]
        row["scope_basis"] = ([a["id"] for a in cited] if cited else
                              "no curated assertion cites this reading; the system it studied is not qualified here")
        row["evidence_label"] = "READING DOCUMENTED (receipt in this repository); applicability to WWOX-DEE not implied"
        rows.append(row)
    rows.sort(key=lambda row: row["pmid"])
    depths = {row["reading_depth"] for row in rows}
    table = {"query_id": query["query_id"], "origin_id": query["origin_id"],
             "rows": rows,
             "papers": len(rows),
             "complete_reads": sum(1 for row in rows if row["reading_depth"] == "complete_fulltext_read"),
             "locators": sum(row["locator_count"] for row in rows),
             "unaudited_contradictions": sum(row["unaudited_contradictions"] for row in rows),
             "depths": sorted(depths),
             "abstention": None if rows else abstention_for(query)}
    table["digest"] = digest({k: v for k, v in table.items() if k != "digest"})
    return table


# ---------------------------------------------------------------- 3 · adapter hits and cards

def adapter_calls(query: dict) -> list[tuple[str, dict]]:
    """Which adapter is asked what, derived from the query's own terms. Deliberately small."""
    calls: list[tuple[str, dict]] = []
    candidate = query.get("candidate")
    if candidate:
        calls.append(("chembl", {"drug": candidate}))
        calls.append(("openfda", {"drug": candidate}))
    for term in query.get("terms", [])[:2]:
        calls.append(("pubtator3", {"gene": term}))
    if query.get("kind") == "claim":
        calls.append(("opentargets", {"ensembl_id": "ENSG00000186153", "size": 10}))
    return calls


def run_adapters(query: dict, cache_dir: Path, live: bool) -> list[dict]:
    hits = []
    for name, request in adapter_calls(query):
        key = f"{name}_{digest(request)}.json"
        cached = cache_dir / key
        if cached.exists() and not live:
            hits.append(json.loads(cached.read_text(encoding="utf-8")))
            continue
        if not live:
            hits.append({"adapter": name, "status": "NOT_ATTEMPTED", "request": request,
                         "hits": [], "evidence_label": "NOT WWOX EVIDENCE",
                         "note": "offline run and no cached response: NOT_ATTEMPTED is not NO_MATCH_FOUND",
                         "retrieved_at": "", "source_version": "UNKNOWN", "licence": "", "citation": "",
                         "requests_sent": [], "error": ""})
            continue
        module = adapters.load(name)
        try:
            result = module.query(request)
        except Exception as exc:  # a crashing adapter is a QUERY_ERROR for this query, not a crash of the join
            result = {"adapter": name, "status": "QUERY_ERROR", "request": request, "hits": [],
                      "evidence_label": "NOT WWOX EVIDENCE", "note": "adapter raised; see error",
                      "retrieved_at": "", "source_version": "UNKNOWN", "licence": "", "citation": "",
                      "requests_sent": [], "error": f"{type(exc).__name__}: {exc}"}
        # The cache keeps the adapter's verbatim fields but caps the hit list: a PubTator query on a
        # common gene returns thousands of pairs, and the join needs the count and the first page,
        # not a megabyte per query in the repository. The cap is written into the record.
        total = len(result.get("hits") or [])
        if total > HIT_CAP:
            result["hits"] = result["hits"][:HIT_CAP]
            result["hits_total_before_cap"] = total
            result["hits_cap"] = HIT_CAP
        cache_dir.mkdir(parents=True, exist_ok=True)
        cached.write_text(json.dumps(result, indent=1, ensure_ascii=False, sort_keys=True), encoding="utf-8")
        hits.append(result)
    return hits


def first_hits(result: dict, limit: int = 3) -> list[str]:
    """The first few hits, named the way the source names them, so a reader of the card can see
    WHAT matched (a class name searched on ChEMBL matches some molecule; the name says which)."""
    names = []
    for hit in (result.get("hits") or [])[:limit]:
        label = (hit.get("pref_name") or hit.get("mechanism_of_action") or hit.get("disease_name")
                 or hit.get("generic_name") or hit.get("preferred_term") or hit.get("compound")
                 or (f"{hit.get('type')} {hit.get('source')} -> {hit.get('target')}" if hit.get("type") else None)
                 or hit.get("kind") or "")
        names.append(str(label)[:120])
    return names


UNQUALIFIED_DIMENSIONS = {
    "track": "UNQUALIFIED", "route": "UNQUALIFIED",
    "route_note": ("no curated card is linked to this record: Track A (variant-independent) / Track B (variant- or "
                   "lesion-specific) and deep recovery / partial benefit are NOT determined by its content, and the "
                   "join assigns neither"),
}


def qualification(packets: list[dict]) -> tuple[str, dict]:
    """Route and mission dimensions as the curated card(s) wrote them; UNQUALIFIED when none is linked or
    when several disagree. Track and route are two independent fields and are never merged or defaulted.
    A card written before Track was qualified (the early-benefit cards, the A-D series) carries a route and
    no `mission_dimensions` block: its route is read as written, its Track is not guessed, and the note names it."""
    if not packets:
        return "UNQUALIFIED", dict(UNQUALIFIED_DIMENSIONS)
    stated = [p for p in packets if p.get("mission_dimensions")]
    silent = [p["candidate"]["id"] for p in packets if not p.get("mission_dimensions")]
    if len(packets) == 1 and stated:
        return packets[0]["route"], copy.deepcopy(packets[0]["mission_dimensions"])
    routes = {p["route"] for p in packets}
    route = routes.pop() if len(routes) == 1 else "UNQUALIFIED"
    tracks = {p["mission_dimensions"]["track"] for p in stated}
    track = tracks.pop() if len(tracks) == 1 else "UNQUALIFIED"
    base = copy.deepcopy(stated[0]["mission_dimensions"]) if stated else {}
    note = ("qualified by several curated cards: " + "; ".join(p["candidate"]["id"] for p in packets)
            if len(packets) > 1 else f"qualified by one curated card: {packets[0]['candidate']['id']}")
    if silent:
        note += ("; Track is read only from the card(s) that state it - " + ", ".join(silent)
                 + (" state(s) a route and no Track (written before Track was qualified)"))
    return route, {**base, "track": track, "route": route, "route_note": note}


def ledger_receipt_ids() -> set[str]:
    return set(RECEIPT_ID.findall(RECEIPT_LEDGER.read_text(encoding="utf-8"))) if RECEIPT_LEDGER.exists() else set()


def curated_checks(assertions: list[dict]) -> list[dict]:
    """Do the identifiers a curated assertion carries still resolve? The receipt must be in the ledger and
    every manifest entry its locator names must exist. This checks that the link is live, not that the
    assertion is true: that is the verifier's reading of the entry itself."""
    ids, out = ledger_receipt_ids(), []
    for row in assertions:
        entry = {"assertion": row["id"], "receipt": row.get("receipt") or None,
                 "receipt_in_ledger": (row["receipt"] in ids) if row.get("receipt") else None, "manifest_entries": []}
        for pmid, raw in LOCATOR_ENTRIES.findall(row.get("locator", "")):
            wanted = [int(n) for n in re.findall(r"\d+", raw)]
            count = manifest_evidence(pmid)["locator_count"]
            entry["manifest_entries"].append({"manifest": relative(MANIFESTS / f"PMID{pmid}.json"), "entries": wanted,
                                              "locator_count": count, "resolved": all(n < count for n in wanted)})
        if entry["receipt"] or entry["manifest_entries"]:
            out.append(entry)
    return out


def tsv_rows(path: Path) -> list[dict] | None:
    if not path.exists():
        return None
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


CHEMBL_LIMIT = 100  # mechanisms requested per target in chembl_target_mechanisms.py; reaching it would be a truncation


def target_compounds(census: dict) -> dict:
    """TARGET -> COMPOUNDS from retrievals already run (DGIdb, ChEMBL curated mechanisms, Open Targets lists),
    read from the census folder a curated packet names. This is a different operation from the adapters'
    search BY NAME (`external_sources`): it answers 'what acts on this target', keyed by identity (HGNC symbol,
    UniProt, Ensembl, ChEMBL target), and keeps per source the action, the source, the query status, the
    coverage and the truncation. A source that was not asked says NOT_ATTEMPTED; one that does not know the
    symbol says UNMATCHED; one that was asked and listed nothing says NO_MATCH_FOUND. None of these is absence
    of pharmacology, and nothing here is WWOX evidence."""
    folder = ROOT / census["dir"]
    resolution = {r["hgnc_symbol"]: r for r in tsv_rows(folder / "target_resolution.tsv") or []}
    dg_rows = tsv_rows(folder / "dgidb_interactions.tsv")
    dg_path = folder / "dgidb_packet.json"
    dg_pack = json.loads(dg_path.read_text(encoding="utf-8")) if dg_path.exists() else {}
    dg_asked = {n for b in dg_pack.get("batches", []) for n in (b.get("variables") or {}).get("names", [])}
    dg_unmatched = set(dg_pack.get("unmatched_symbols", []))
    ch_rows = tsv_rows(folder / "chembl_mechanisms.tsv")
    ch_path = folder / "chembl_target_log.json"
    ch_log = json.loads(ch_path.read_text(encoding="utf-8")) if ch_path.exists() else {}
    ot_rows = tsv_rows(folder / "opentargets_lists.tsv")
    ot_counts = tsv_rows(folder / "opentargets_adapter_counts.tsv")
    targets = []
    for symbol in census["symbols"]:
        ident = resolution.get(symbol)
        entry = {"symbol": symbol,
                 "identity": ({"hgnc_id": ident["hgnc_id"], "uniprot": ident["uniprot"], "ensembl_gene": ident["ensembl_gene"],
                               "chembl_single_protein_target": ident["chembl_single_protein_target"] or "NONE_RESOLVED",
                               "note": ident.get("collision_or_note", "")} if ident else "UNRESOLVED: symbol absent from target_resolution.tsv"),
                 "sources": {}}
        warn = ("IDENTITY COLLISION: " + ident["collision_or_note"][:200]) if ident and ident["collision_or_note"].startswith("COLLISION") else ""
        # DGIdb, keyed by HGNC symbol
        if dg_rows is None or symbol not in dg_asked:
            dg = {"status": "NOT_ATTEMPTED", "compounds": []}
        elif symbol in dg_unmatched:
            dg = {"status": "UNMATCHED", "compounds": [], "note": "DGIdb does not know this symbol; that is not a gene with no drugs"}
        else:
            comps = [{"name": r["drug"], "action": r["action_types"], "sources": r["sources"], "approved": r["approved"],
                      "n_publications": r["n_pubs"], **({"identity_warning": warn} if warn else {})}
                     for r in dg_rows if r["gene"] == symbol]
            dg = {"status": "MATCH_FOUND" if comps else "NO_MATCH_FOUND", "compounds": comps}
        dg.update({"source": "DGIdb GraphQL via kg_thin_slice.drug_packet", "packet_status": dg_pack.get("status", "UNKNOWN"),
                   "coverage": "UNKNOWN" if dg["status"] == "NOT_ATTEMPTED" else dg_pack.get("coverage_statement", "UNKNOWN"),
                   "truncation": "NOT_RECORDED: interaction pagination is not kept per symbol in the census",
                   "query": relative(dg_path)})
        entry["sources"]["dgidb"] = dg
        # ChEMBL curated mechanisms, keyed by UniProt accession
        asked = any(symbol in key.split("_") or key == symbol for key in ch_log)
        if ch_rows is None or not asked:
            ch = {"status": "NOT_ATTEMPTED", "compounds": []}
        else:
            comps = [{"name": r["pref_name"] or r["molecule_chembl_id"], "molecule": r["molecule_chembl_id"], "action": r["action_type"],
                      "mechanism": r["mechanism"], "max_phase": r["max_phase"], "target": r["target_chembl_id"],
                      "target_type": r["target_type"], "references": r["refs"]}
                     for r in ch_rows if ident and r["uniprot"] == ident["uniprot"]]
            ch = {"status": "MATCH_FOUND" if comps else "NO_MATCH_FOUND", "compounds": comps}
            ch["truncation"] = {"limit_per_target": CHEMBL_LIMIT, "truncated": len(comps) >= CHEMBL_LIMIT}
        ch.update({"source": "ChEMBL REST, curated mechanisms of the target", "query": relative(ch_path),
                   "coverage": "COMPLETE_FOR_QUERIES_RUN" if asked else "UNKNOWN",
                   "note": "a PROTEIN FAMILY target is shared by its members: the action is the family's, not the isoform's"})
        entry["sources"]["chembl_mechanisms"] = ch
        # Open Targets lists, keyed by Ensembl gene id
        ensembl = ident["ensembl_gene"] if ident else ""
        counts = [r for r in ot_counts or [] if r["ensembl"] == ensembl]
        if ot_rows is None or not counts:
            ot = {"status": "NOT_ATTEMPTED", "compounds": []}
        else:
            listed = [r for r in ot_rows if r["ensembl"] == ensembl]
            total = int(counts[0]["list_count"] or 0)
            ot = {"status": "MATCH_FOUND" if listed else "NO_MATCH_FOUND",
                  "compounds": [{"name": r["name"], "molecule": r["molecule"], "drug_type": r["drugType"],
                                 "max_clinical_stage": r["maxClinicalStage"], "indications": r["diseases"], "action": "NOT_REPORTED"}
                                for r in listed],
                  "count_reported": total, "adapter_count": counts[0]["adapter_count"],
                  "truncation": {"truncated": len(listed) < total, "listed": len(listed), "reported": total}}
        ot.update({"source": "Open Targets Platform GraphQL, drugAndClinicalCandidates", "coverage": "COMPLETE_FOR_QUERIES_RUN" if ot["status"] != "NOT_ATTEMPTED" else "UNKNOWN",
                   "query": relative(folder / "opentargets_lists.tsv")})
        entry["sources"]["opentargets"] = ot
        targets.append(entry)
    return {"operation": "TARGET_TO_COMPOUNDS", "evidence_label": "NOT WWOX EVIDENCE", "census": census["dir"], "targets": targets,
            "not_this": "a search by candidate name is in external_sources; the two answer different questions and neither stands for the other"}


def card_for(query: dict, table: dict, hits: list[dict]) -> dict | None:
    """A bridge packet composed from the evidence table and the adapter hits, then built by the
    bridge itself. Composed, never typed: every assertion names the record it came from.

    When the map record names a curated card, that card's QUALIFIED assertions (target, endpoint, direction,
    context, source, depth, locator, receipt, scope), route and mission dimensions are the card's content, as
    written; the join adds the live evidence table, the adapters' name lookups and the target -> compounds
    census beside them and rewrites none. With no curated card there is one unqualified disease row and the
    route is UNQUALIFIED: the join does not decide deep recovery vs partial benefit, or Track A vs B."""
    candidate = query.get("candidate")
    if not candidate:
        return None
    packets = curated_packets(query)
    route, dimensions = qualification(packets)
    verification = (f"derived by repurposing_join.py from {query['origin_file']}:"
                    f"{query['origin_line']}; evidence table digest {table['digest']}")
    derived_roadmap = {"indication_and_transfer": query.get("intervention", "UNKNOWN")[:400],
                       "verification_scope": verification}
    if packets:
        diseases, drugs = packet_assertions(packets)
        packet = copy.deepcopy(packets[0])
        packet.update({"disease_assertions": copy.deepcopy(diseases), "drug_assertions": copy.deepcopy(drugs)})
        packet.pop("disease_assertion", None)
        packet["curated_candidate"] = packet["candidate"]
        packet["curated_from"] = [relative(curated_packet_path(name)).split("drug_repurposing/", 1)[-1]
                                  for name in query["curated_cards"] if curated_packet_path(name) is not None]
        packet["curation_checks"] = curated_checks(diseases + drugs)
        packet["p4_roadmap_fields"] = packet.get("p4_roadmap_fields") or derived_roadmap
        census = [packet_.get("target_census") for packet_ in packets if packet_.get("target_census")]
        if census:
            packet["target_compounds"] = target_compounds(
                {"dir": census[0]["dir"], "symbols": sorted({s for c in census for s in c["symbols"]})})
    else:
        disease_assertion = {
            "id": f"DA-{query['query_id']}",
            "target_id": query.get("target", "UNKNOWN")[:120] or "UNKNOWN",
            "endpoint": "UNKNOWN",
            "direction": "UNKNOWN",
            "source": f"{query['origin_file']} {query['origin_id']}",
            "locator": f"{query['origin_file']}:{query['origin_line']}",
            "epistemic_status": "IPOTESI",
            "evidence_scope": "UNQUALIFIED",
            "reading_depth": (table["rows"][0]["reading_depth"] if table["rows"] else "UNKNOWN"),
            "context": {key: "UNKNOWN" for key in bridge.CONTEXT},
        }
        if disease_assertion["reading_depth"] not in bridge.READING:
            disease_assertion["reading_depth"] = "UNKNOWN"
        if table["rows"] and table["rows"][0].get("receipt_id"):
            disease_assertion["receipt"] = table["rows"][0]["receipt_id"]
        packet = {
            "schema_version": 1,
            "disease_assertion": disease_assertion,
            "drug_assertions": [],
            "label_lookup": {"status": "NOT_ATTEMPTED"},
            "p4_fields": {
                "endpoint_pursued": "UNKNOWN",
                "functional_evidence_available": "UNKNOWN",
                "temporal_or_model_limit": "UNKNOWN",
                "cellular_context": {key: "UNKNOWN" for key in bridge.P4_CONTEXT},
            },
            "p4_roadmap_fields": derived_roadmap,
        }
    external = [hit for hit in hits if hit.get("status") == "MATCH_FOUND"]
    packet.update({
        "route": route,
        "mission_dimensions": dimensions,
        "candidate": {"id": query["query_id"], "name": candidate},
        "derived_by": "framework/scripts/repurposing_join.py",
        "legend_evidence": table,
        "external_sources": [
            {"adapter": hit.get("adapter"), "status": hit.get("status"),
             "operation": "SEARCH_BY_NAME_OR_IDENTIFIER",
             "retrieved_at": hit.get("retrieved_at"), "source_version": hit.get("source_version"),
             "licence": hit.get("licence"), "citation": hit.get("citation"),
             "requests_sent": hit.get("requests_sent"), "hit_count": len(hit.get("hits") or []),
             "hits_total_before_cap": hit.get("hits_total_before_cap"),
             "first_hits": first_hits(hit), "error": hit.get("error") or "",
             "evidence_label": "NOT WWOX EVIDENCE"}
            for hit in hits
        ],
    })
    label = next((hit for hit in hits if hit.get("adapter") == "openfda"), None)
    if label and label.get("status") in bridge.LOOKUP_STATUS:
        packet["label_lookup"] = {
            "status": label["status"],
            "coverage": "COMPLETE_FOR_QUERIES_RUN" if label["status"] in ("MATCH_FOUND", "NO_MATCH_FOUND") else "UNKNOWN",
            "method": "primary",
            "queries": [str(item) for item in (label.get("requests_sent") or [])] or [],
            "source": "openFDA drug label (Data provided by the U.S. Food and Drug Administration)",
            "retrieved_at": label.get("retrieved_at") or "UNKNOWN",
            "client_version": "framework/adapters/openfda.py",
        }
        if label["status"] == "NOT_ATTEMPTED":
            packet["label_lookup"] = {"status": "NOT_ATTEMPTED"} if not packets else packets[0]["label_lookup"]
        elif label["status"] == "MATCH_FOUND":
            first = next((h for h in label.get("hits") or [] if h.get("kind") == "label"), {})
            names = first.get("generic_name") or []
            packet["label_lookup"]["product_name"] = (names[0] if names else "UNKNOWN")
            packet["label_lookup"]["spl_id"] = first.get("set_id") or "UNKNOWN"
    card = bridge.build_card(packet)
    card["external_sources"] = packet["external_sources"]
    card["legend_evidence"] = table
    card["measure_next"] = measure_next(query, table, external)
    return card


# ---------------------------------------------------------------- 4 · what to measure next

def measure_next(query: dict, table: dict, external: list[dict]) -> dict:
    """The single measurement that would split the dependence, derived from the table.

    The dependence is what the rows actually show: no receipted paper at all, one paper carrying
    the whole query, or several papers of which only one was read to the end. Each case names a
    different measurement, and every case names the record the measurement would move."""
    moves = f"{query['origin_id']} ({query['origin_file']}:{query['origin_line']})"
    if not table["rows"]:
        state = table["abstention"].split(":")[0]
        return {"dependence": state,
                "measurement": ("the link from this record to a paper: " if state == "LINKAGE_GAP"
                                else "a first paper for this record: ")
                               + table["abstention"].split("missing datum: ")[-1]
                               + "; until then the external hits stand alone and are NOT WWOX EVIDENCE",
                "experiment_sketch": "route the query to a Scientist batch as a reading row, not to a laboratory",
                "would_move": moves, "external_hits": len(external)}
    if table["papers"] == 1:
        row = table["rows"][0]
        return {"dependence": f"ONE_PAPER ({row['pmid']}, depth {row['reading_depth']}, "
                              f"{row['locator_count']} locators, audit {row['audit_status']})",
                "measurement": "an independent measurement of the same endpoint in a second system, "
                               "or the same system from a second laboratory: the query rests on one reading",
                "experiment_sketch": "replicate the one measurement this query stands on, changing the "
                                     "laboratory or the model but not the endpoint",
                "would_move": moves, "external_hits": len(external)}
    if table["complete_reads"] == 0:
        return {"dependence": f"{table['papers']}_PAPERS_NONE_READ_COMPLETE",
                "measurement": "a complete full-text read of the strongest of these papers, with its receipt",
                "experiment_sketch": "no laboratory work: the next informative act is a reading",
                "would_move": moves, "external_hits": len(external)}
    if table["unaudited_contradictions"]:
        return {"dependence": f"{table['unaudited_contradictions']}_UNAUDITED_CONTRADICTIONS",
                "measurement": "a blind locator audit of the contradicting entries before this query "
                               "touches a baseline claim",
                "experiment_sketch": "legend-locator-audit over the declared triples",
                "would_move": moves, "external_hits": len(external)}
    return {"dependence": f"{table['papers']}_PAPERS_{table['complete_reads']}_COMPLETE",
            "measurement": "the endpoint the rows disagree on, measured in one system that carries "
                           "both contexts; UNKNOWN context dimensions are what keeps the comparison UNRESOLVED",
            "experiment_sketch": "one experiment holding target and endpoint fixed while the context "
                                 "dimension that is UNKNOWN is the only thing that varies",
            "would_move": moves, "external_hits": len(external)}


# ---------------------------------------------------------------- run, state, change report

def previous_state(out_dir: Path) -> dict:
    path = out_dir / "state.json"
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except ValueError:
        return {}


def run(out_dir: Path, axis: str = "", live: bool = False, limit: int = 0) -> dict:
    out_dir.mkdir(parents=True, exist_ok=True)
    cache_dir = out_dir / "adapter_cache"
    queries = derive_queries(axis=axis)
    if limit:
        queries = queries[:limit]
    receipts = load_receipts()
    tables, cards = [], []
    for query in queries:
        # only a one-paper query is later a REPLICATE row, and only there does the binding matter
        checks = ({pmid: bound_check(pmid, query, out_dir / "pubmed_cache", live) for pmid in query["pmids"]}
                  if len(query.get("pmids", [])) == 1 else None)
        table = evidence_for(query, receipts, checks)
        tables.append(table)
        hits = run_adapters(query, cache_dir, live)
        card = card_for(query, table, hits)
        if card is not None:
            cards.append({"query_id": query["query_id"], "card": card})
    before = previous_state(out_dir)
    state = {"axis": axis or "all",
             "queries": {q["query_id"]: q["digest"] for q in queries},
             "evidence": {t["query_id"]: t["digest"] for t in tables},
             "cards": {c["query_id"]: digest(c["card"]) for c in cards}}
    changes = change_report(before, state)
    (out_dir / "queries.json").write_text(json.dumps(queries, indent=1, ensure_ascii=False, sort_keys=True), encoding="utf-8")
    (out_dir / "evidence.json").write_text(json.dumps(tables, indent=1, ensure_ascii=False, sort_keys=True), encoding="utf-8")
    (out_dir / "cards.json").write_text(json.dumps(cards, indent=1, ensure_ascii=False, sort_keys=True), encoding="utf-8")
    (out_dir / "measure_next.json").write_text(
        json.dumps([{"query_id": c["query_id"], **c["card"]["measure_next"]} for c in cards],
                   indent=1, ensure_ascii=False, sort_keys=True), encoding="utf-8")
    (out_dir / "state.json").write_text(json.dumps(state, indent=1, sort_keys=True), encoding="utf-8")
    return {"axis": axis or "all", "live": live, "queries": len(queries), "evidence_tables": len(tables),
            "cards": len(cards),
            "abstentions": sum(1 for t in tables if t["abstention"]),
            "changes": changes, "out_dir": relative(out_dir)}


def change_report(before: dict, after: dict) -> dict:
    report = {}
    for section in ("queries", "evidence", "cards"):
        old, new = before.get(section, {}), after.get(section, {})
        report[section] = {
            "added": sorted(set(new) - set(old)),
            "changed": sorted(key for key in set(new) & set(old) if new[key] != old[key]),
            "removed": sorted(set(old) - set(new)),
            "unchanged": len([key for key in set(new) & set(old) if new[key] == old[key]]),
        }
    return report


def render(summary: dict) -> str:
    lines = [f"JOIN axis={summary['axis']} live={summary['live']} -> {summary['out_dir']}",
             f"queries {summary['queries']} · evidence tables {summary['evidence_tables']} "
             f"({summary['abstentions']} abstentions) · cards {summary['cards']}"]
    for section, block in summary["changes"].items():
        lines.append(f"{section}: +{len(block['added'])} added · ~{len(block['changed'])} changed · "
                     f"-{len(block['removed'])} removed · {block['unchanged']} unchanged")
        for key in block["added"][:5]:
            lines.append(f"    ADDED   {key}")
        for key in block["changed"][:5]:
            lines.append(f"    CHANGED {key}")
        for key in block["removed"][:5]:
            lines.append(f"    REMOVED {key}")
    return "\n".join(lines)


INDEPENDENT = ("independent = a different laboratory from the bound paper (no shared corresponding or senior "
               "author, no shared institution); a second model from the same laboratory is flagged, not counted, "
               "and a cancer-cell measurement is a second system for a molecular endpoint, not for a network one")


def open_clause(query: dict) -> str:
    """What the record itself leaves open: the map's decisive test (repurposing records) or revival
    trigger (negative-translation records), as written, without its markdown."""
    clause = str(query.get("decisive_test") or "").replace("**", "").strip()
    return "" if clause in ("", "UNKNOWN") else clause[:400]


def acquisition_state(table: dict) -> str:
    """What the repository holds of the papers behind a row, from the receipt ledger: depth counts,
    or the linkage state when no paper is reached. Lawful obtainability is NOT probed here."""
    if not table["rows"]:
        return f"no paper reached ({(table.get('abstention') or 'UNKNOWN').split(':')[0]})"
    counts: dict[str, int] = {}
    for row in table["rows"]:
        counts[row["reading_depth"]] = counts.get(row["reading_depth"], 0) + 1
    return f"{len(table['rows'])} paper(s): " + ", ".join(f"{n} {d}" for d, n in sorted(counts.items()))


SPAN_STOP = GENERIC | {"and", "the", "with", "without", "only", "versus", "then"}
MEASURED, MECHANISM, MISSING = ("MEASURED_OBSERVATION_TO_REPLICATE", "MECHANISM_STILL_TO_VERIFY",
                                "READING_OR_QUALIFICATION_MISSING")


def span_tokens(text: str) -> set[str]:
    return {w for w in re.findall(r"\w{2,}", text.casefold()) if w not in SPAN_STOP}


def endpoint_classes(query: dict, card: dict) -> list[dict]:
    """Classify each endpoint the record's decisive test names (its bold spans), against the CURATED
    observations bound to the record - never against the words of an abstract.

      MEASURED_OBSERVATION_TO_REPLICATE - a curated, receipted full-text observation has this target and
          endpoint (every word of the span is in its target_id/endpoint). Replication keeps endpoint and
          changes laboratory or model; its context, locator, limits and the nulls/oppositions are listed.
      MECHANISM_STILL_TO_VERIFY - the reading is qualified and complete but no observation measures this
          endpoint: it is an experiment the study did not run, so doing it is a NEW experiment and never
          a replication of the study. Observations that share the molecule but not the endpoint are listed.
      READING_OR_QUALIFICATION_MISSING - carries a `cause` field, one of NO_ENDPOINT_DECLARED (the record names
          no bold endpoint), NO_CURATED_OBSERVATION, OBSERVATION_WEAKER_THAN_FULLTEXT (the matching one is
          weaker than a complete full-text read), NO_COMPLETE_READING_BOUND.

    This is a screen over fields a Scientist already qualified, not an extractor: the verdict names the
    assertions and locators it rests on so a verifier can open them."""
    packet = card["input"]
    disease = packet.get("disease_assertions") or []
    spans = [m.strip() for m in BOLD.findall(query.get("decisive_test") or "")]
    complete = [row for row in card["legend_evidence"]["rows"] if row["reading_depth"] == "complete_fulltext_read"]
    out = []
    for span in spans or ["(the record declares no endpoint)"]:
        tokens = span_tokens(span)
        matched = [a for a in disease if tokens and tokens <= span_tokens(f"{a['target_id']} {a['endpoint']}")]
        related = [a for a in disease if a not in matched and tokens
                   and next(iter(sorted(tokens, key=lambda t: span.casefold().find(t)))) in span_tokens(f"{a['target_id']} {a['endpoint']}")]
        strong = [a for a in matched if a["reading_depth"] == "complete_fulltext_read" and a.get("receipt")]

        def view(a):
            return {"id": a["id"], "direction": a["direction"], "scope": a.get("evidence_scope", "UNQUALIFIED"),
                    "reading_depth": a["reading_depth"], "species": a["context"]["species"],
                    "genotype": a["context"]["genotype"], "locator": a["locator"], "limits": a.get("measured_result_note", ""),
                    "sign_vs_contrast": a.get("sign_vs_contrast", {})}
        cause = ""
        if not spans:
            kind, cause, why = MISSING, "NO_ENDPOINT_DECLARED", ("the record names no endpoint (no bold span in its decisive test), "
                                                                 "so no observation can be matched to it: name the readout and its unit")
        elif not disease:
            kind, cause, why = MISSING, "NO_CURATED_OBSERVATION", "no curated observation is linked to this record"
        elif strong:
            kind, why = MEASURED, ("a full-text observation with this target and endpoint exists, in the context shown; "
                                   "replicate the endpoint in an independent laboratory or model")
        elif matched:
            kind, cause, why = MISSING, "OBSERVATION_WEAKER_THAN_FULLTEXT", "the matching observation is weaker than a complete full-text read: read or qualify it first"
        elif complete:
            kind, why = MECHANISM, ("the bound reading is complete and does not measure this endpoint; measuring it is a new "
                                    "experiment, not a replication of the study")
        else:
            kind, cause, why = MISSING, "NO_COMPLETE_READING_BOUND", "no complete full-text reading is bound to this record"
        out.append({"endpoint": span, "class": kind, "cause": cause, "why": why, "observations": [view(a) for a in matched],
                    "same_molecule_other_endpoint": [view(a) for a in related]})
    return out


def handoff_rows(cards: list[dict], queries: dict[str, dict]) -> list[dict]:
    """The feedback loop into research: each card's measure-next becomes one row the next batch
    can act on. Four row kinds, decided by the dependence the join measured, never by hand:

      SELECT   — no paper reached (LINKAGE_GAP: the record points to none; NO_PAPER: the registry
                 holds none for it): the read-only selector names the link or proposes reading rows;
      READ     — one or more papers but none read to the end: a Scientist's complete read;
      REPLICATE— the whole query rests on one reading: the selector looks for an independent
                 measurement of the same endpoint; the bound paper is screened first (primary
                 article? endpoint words present?) and the row says so;
      AUDIT    — the locators carry contradictions nobody audited: a blind locator audit before
                 the query may touch a baseline claim.

    `ask` is the record's own open clause when it has one, else the join's act; `acquisition` is what
    the repository holds of the papers behind the row. A row is an assignment, not a conclusion;
    nothing in it is a dose or a recommendation."""
    rows = []
    for item in cards:
        card, query = item["card"], queries.get(item["query_id"], {})
        table, nxt = card["legend_evidence"], card["measure_next"]
        dep = nxt["dependence"]
        pmids = [row["pmid"] for row in table["rows"]]
        binding, classes = None, None
        if dep in ("LINKAGE_GAP", "NO_PAPER"):
            kind, who, pmid_list = "SELECT", "read-only selector", []
            act = nxt["measurement"]
        elif dep.startswith("ONE_PAPER"):
            kind, who, pmid_list = "REPLICATE", "read-only selector, then a Scientist", pmids
            binding = dict(table["rows"][0].get("bound_check") or {"binding": "NOT_CHECKED", "reason": "no check recorded"})
            classes = endpoint_classes(query, card)
            measured = [c for c in classes if c["class"] == MEASURED]
            mech = [c for c in classes if c["class"] == MECHANISM]
            missing = [c for c in classes if c["class"] == MISSING]
            if measured:
                # The link is a full-text locator. The abstract screen stays, labelled as what it is: words in
                # an abstract do not make or unmake a link that a locator supports.
                binding = {"binding": "BOUND_BY_FULLTEXT_LOCATOR",
                           "reason": "; ".join(f"{c['endpoint']}: " + ", ".join(o["id"] for o in c["observations"]) for c in measured),
                           "abstract_screen": binding}
            act = ("; ".join(
                [f"REPLICATE (same endpoint, other laboratory or model): {', '.join(c['endpoint'] for c in measured)}"] * bool(measured)
                + [f"NOT a replication, a new experiment to verify the mechanism: {', '.join(c['endpoint'] for c in mech)}"] * bool(mech)
                + [f"READING OR QUALIFICATION MISSING ({', '.join(sorted({c['cause'] for c in missing}))}): {', '.join(c['endpoint'] for c in missing)}"] * bool(missing))
                + "; " + INDEPENDENT)
            if not measured and binding["binding"] != "PRIMARY_WITH_ENDPOINT_WORDS":
                act += (f". BIND FIRST: {binding['binding']} - {binding.get('reason', '')} (abstract screen only): replace the "
                        "bound paper with a primary article that contains the endpoint before searching")
        elif "NONE_READ_COMPLETE" in dep:
            kind, who, pmid_list = "READ", "Scientist", pmids
            act = "complete full-text read of the strongest of these papers, with its receipt and manifest"
        elif "UNAUDITED_CONTRADICTIONS" in dep:
            kind, who = "AUDIT", "an auditor who is not the reader"
            pmid_list = [row["pmid"] for row in table["rows"] if row["unaudited_contradictions"]]
            act = ("blind locator audit (legend-locator-audit) of the contradicts_locator entries in these "
                   "manifests before the query touches a baseline claim")
        else:
            kind, who, pmid_list = "READ", "Scientist", pmids
            act = nxt["measurement"]
        clause = open_clause(query)
        external = [f"{s['adapter']} {s['status']} ({s.get('retrieved_at') or 'not attempted'})"
                    for s in card.get("external_sources", [])]
        rows.append({"query_id": item["query_id"], "kind": kind, "who": who,
                     "candidate": card["input"]["candidate"]["name"],
                     "origin": nxt["would_move"], "dependence": dep, "pmids": pmid_list,
                     "ask": clause or act, "ask_source": "record open clause" if clause else "join act",
                     "act": act, "acquisition": acquisition_state(table), "binding": binding,
                     "endpoint_classes": classes,
                     "qualification": qualification_view(card),
                     "external_sources": external,
                     "lead_spec": lead_spec(item["query_id"], card, query, classes) if kind == "REPLICATE" else None})
    rows.sort(key=lambda row: (row["kind"], row["query_id"]))
    return rows


def qualification_view(card: dict) -> dict | None:
    """What the linked curated card(s) already say about this record, read from the derived card: the next batch
    starts from the card, not from the record's papers. None when no curated card is linked."""
    packet = card["input"]
    if not packet.get("curated_from"):
        return None
    comparisons: dict[str, int] = {}
    for item in card["comparisons"]:
        comparisons[item["status"]] = comparisons.get(item["status"], 0) + 1
    dims = packet.get("mission_dimensions") or {}
    return {"cards": list(packet["curated_from"]), "route": packet.get("route"), "track": dims.get("track"),
            "disease_rows": len(packet.get("disease_assertions") or []),
            "drug_rows": len(packet.get("drug_assertions") or []), "comparisons": comparisons,
            "summary": card["directional_summary"],
            "card_next_measurement": ((packet.get("p4_card") or {}).get("next_measurement") or "")[:300]}


def lead_spec(query_id: str, card: dict, query: dict, classes: list[dict] | None = None) -> dict:
    """A discovery-ledger spec (the shape `discovery_lead.py check` validates) for a dependence
    worth remembering as a lead: the query stands on one reading. Status open; tag INFERENZA;
    falsifier and transfer limit are required fields, so they are written. It is staged by a
    Scientist, never appended by the join."""
    row = card["legend_evidence"]["rows"][0]
    name = card["input"]["candidate"]["name"]
    check = row.get("bound_check") or {}
    measured = [c for c in classes or [] if c["class"] == MEASURED]
    bound = ("bound paper screened: " + check["binding"] + (f" ({check['reason']})" if check.get("reason") else "")
             if check else "bound paper not screened")
    if measured:  # the link is a full-text locator; the abstract screen is not the test of it
        bound = ("bound by full-text locator: " + "; ".join(
            f"{c['endpoint']} -> " + ", ".join(f"{o['id']} ({o['locator']})" for o in c["observations"]) for c in measured)
            + "; abstract screen (not the test): " + (check.get("binding") or "not run"))
    return {
        "kind": "MECH", "status": "open", "tag": "INFERENZA",
        "title": f"{name}: the repurposing query rests on a single reading "
                 f"(PMID {row['pmid']}); an independent measurement would split the dependence",
        "source": (f"framework/scripts/repurposing_join.py handoff, {card['legend_evidence']['query_id']}, derived from "
                   f"{query.get('origin_file', '')}:{query.get('origin_line', '')}; manifest {row['manifest']} "
                   f"({row['locator_count']} locators, audit {row['audit_status']}); receipt {row.get('receipt_id', '')}; "
                   f"{bound}"),
        "causal_statement": (f"INFERENZA: every assertion the module can bind for '{name}' traces to one "
                             f"receipted reading; a second measurement of the same endpoint in a second "
                             f"system or laboratory is the single datum that would move {card['measure_next']['would_move']}"),
        "falsifier": (f"a primary article from an independent laboratory that measures the same endpoint "
                      f"({', '.join(c['endpoint'] for c in classes or [] if c['class'] == MEASURED) or ', '.join(check.get('endpoint_words_found') or []) or 'endpoint to be named by the Scientist'}) "
                      f"refutes the single-reading dependence, and refutes the direction if it disagrees; "
                      f"{INDEPENDENT}"),
        "transfer_limit": ("a measurement in another system transfers to the reference genotype only for the "
                           "molecular endpoint it measured, not for network, phenotype or dose-response; every "
                           "external-database statement about the candidate is NOT WWOX EVIDENCE"),
    }


def render_handoff(rows: list[dict], date: str, axis: str,
                   evidence: list[dict] | None = None) -> str:
    lines = [
        f"# Module handoff — rows for the next Scientist batch ({date}, axis {axis or 'all'})",
        "",
        "Rendered by `python3 framework/scripts/repurposing_join.py handoff` from `join/cards.json`; never typed.",
        "Each row is what the join measured about the dependence behind one candidate and the one act that would",
        "split it. A row is an assignment for the read-only selector, a Scientist or an auditor — not a conclusion,",
        "not a ranking, not a dose. Every external source named is **NOT WWOX EVIDENCE** and carries its retrieval",
        "date; its licence and citation are in the card and in `drug_repurposing/ACKNOWLEDGEMENTS.md`.",
        "Not medical advice.",
        "",
        "`Ask` is the record's own open clause where it has one (else the join's act). `Acquisition` is what the",
        "receipt ledger holds of the papers behind the row; whether a paper is lawfully obtainable is not probed.",
        "States: `LINKAGE_GAP` = the record points to no paper the join can resolve (the paper may exist);",
        "`NO_PAPER` = the registry holds no paper for the record. Neither is a statement about the literature.",
        f"REPLICATE: {INDEPENDENT}.",
        "",
        "| Kind | Query | Candidate (from the mechanism map heading) | Dependence measured | PMIDs | Ask | Acquisition | To do | Who | Would move |",
        "|---|---|---|---|---|---|---|---|---|---|",
    ]
    for row in rows:
        todo = row["act"] if row["ask_source"] == "record open clause" else "(the Ask)"
        lines.append(f"| {row['kind']} | `{row['query_id']}` | {row['candidate'][:60]} | {row['dependence'][:80]} | "
                     f"{', '.join(row['pmids']) or '—'} | {row['ask']} | {row['acquisition']} | {todo} | {row['who']} | {row['origin']} |")
    counts = {}
    for row in rows:
        counts[row["kind"]] = counts.get(row["kind"], 0) + 1
    lines += ["", "Counts: " + " · ".join(f"{k} {v}" for k, v in sorted(counts.items())), ""]
    qualified = [row for row in rows if row.get("qualification")]
    if qualified:
        lines += ["## Records already qualified by a curated card (start from the card, not from the papers)",
                  "", "A curated card carries target, endpoint, direction, context, source, depth, locator and limits as a Scientist "
                  "wrote them; the join reads them and adds nothing. `route` and `track` are two independent fields (Track is read only "
                  "from the card that states it). Comparison statuses are sign comparisons on equal target, endpoint and context: "
                  "`UNRESOLVED` means no matched comparison exists, not that the biology is unresolved. The card's own next measurement "
                  "is shown; it is not a recommendation.", "",
                  "| Query | Candidate | Curated card(s) | Route | Track | Disease / drug rows | Comparisons | Summary | Card's next measurement |",
                  "|---|---|---|---|---|---|---|---|---|"]
        for row in qualified:
            q = row["qualification"]
            comp = ", ".join(f"{k} {v}" for k, v in sorted(q["comparisons"].items())) or "none (no drug-side row)"
            lines.append(f"| `{row['query_id']}` | {row['candidate'][:50]} | {', '.join(q['cards'])} | {q['route']} | {q['track']} | "
                         f"{q['disease_rows']} / {q['drug_rows']} | {comp} | {q['summary']} | {q['card_next_measurement'] or 'UNKNOWN'} |")
        lines.append("")
    classified = [row for row in rows if row.get("endpoint_classes") and row["binding"]["binding"] == "BOUND_BY_FULLTEXT_LOCATOR"]
    if classified:
        lines += ["## REPLICATE rows: what each endpoint is, against the curated observations",
                  "", "`MEASURED_OBSERVATION_TO_REPLICATE` = a receipted full-text observation with this target and endpoint exists "
                  "(its context and locator below); `MECHANISM_STILL_TO_VERIFY` = the reading does not measure it, so measuring it "
                  "is a new experiment and not a replication; `READING_OR_QUALIFICATION_MISSING` = nothing curated or complete to "
                  "stand on. Matching is on the curated target/endpoint fields, never on abstract words.", ""]
        for row in classified:
            lines.append(f"- `{row['query_id']}` {row['candidate'][:70]}")
            for c in row["endpoint_classes"]:
                lines.append(f"  - **{c['endpoint']}** - `{c['class']}`" + (f" (cause `{c['cause']}`)" if c.get("cause") else "") + f": {c['why']}")
                for o in c["observations"]:
                    sign = "; ".join(f"{k}: {v}" for k, v in sorted((o.get("sign_vs_contrast") or {}).items()))
                    lines.append(f"    - {o['id']} {o['direction']} ({o['scope']}; {o['reading_depth']}; {o['species']}; "
                                 f"{o['genotype']}) - locator {o['locator']} - limits: {o['limits']}" + (f" - sign relative to: {sign}" if sign else ""))
                for o in c["same_molecule_other_endpoint"]:
                    lines.append(f"    - same molecule, other endpoint (not a match): {o['id']} {o['direction']} ({o['scope']}; "
                                 f"{o['reading_depth']}) - locator {o['locator']}")
        lines.append("")

    # The debt that no row carries. An entry an audit CONDEMNED keeps `auditors: 1` from that
    # audit, so a repair nobody re-judged reads as audited; a held candidate sat three days on
    # exactly this. It is reported once, not as a row per query: half the queries touch one, and
    # a queue that lists them all is a queue nobody reads.
    unverified = {r.get("manifest") for q in (evidence or []) for r in q.get("rows") or []
                  if (r.get("repair_unverified") or 0) and r.get("manifest")}
    reached = sum(1 for q in (evidence or [])
                  if any((r.get("repair_unverified") or 0) for r in q.get("rows") or []))
    if unverified:
        lines += [
            f"**Repaired but not re-judged:** {len(unverified)} of the manifests these queries "
            f"reach hold a locator an audit found adverse whose repair no later audit has judged; "
            f"{reached} of {len(evidence or [])} queries reach one. They are not rows here, because "
            "half the queue would be one row — an audit of them is owed, and a claim resting on one "
            "rests on an unverified repair.", ""]
    specs = [row["lead_spec"] for row in rows if row.get("lead_spec")]
    if specs:
        lines += ["## Lead specs (for `discovery_lead.py check`; a Scientist stages them, the join never appends)", ""]
        for spec in specs:
            lines += ["```json", json.dumps(spec, indent=1, ensure_ascii=False), "```", ""]
    return "\n".join(lines)


def diff_against_handmade(derived_card: dict, handmade: dict) -> dict:
    """What the derived card carries that the hand-written one does not, and the other way round.

    The hand-made cards in `cards/` were typed from the manifests and are therefore free to
    drift; the derived card cannot. The comparison is on the fields both claim to carry, and on
    the values of the two the module is judged by: the directional summary and the abstention."""
    def flat(card: dict, prefix: str = "") -> dict:
        out = {}
        for key, value in sorted(card.items()):
            name = f"{prefix}{key}"
            if isinstance(value, dict):
                out.update(flat(value, f"{name}."))
            else:
                out[name] = value
        return out

    left, right = flat(derived_card), flat(handmade)
    shared = sorted(set(left) & set(right))
    return {
        "only_in_derived": sorted(set(left) - set(right)),
        "only_in_handmade": sorted(set(right) - set(left)),
        "same_value": [key for key in shared if left[key] == right[key]],
        "different_value": [{"field": key, "derived": str(left[key])[:200], "handmade": str(right[key])[:200]}
                            for key in shared if left[key] != right[key]],
        "directional_summary": {"derived": derived_card.get("directional_summary"),
                                "handmade": handmade.get("directional_summary")},
        "abstention": {"derived": derived_card.get("abstention"), "handmade": handmade.get("abstention")},
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("run", "queries"):
        sp = sub.add_parser(name)
        sp.add_argument("--axis", choices=sorted(AXES), default="")
        sp.add_argument("--out", type=Path, default=DEFAULT_OUT)
        sp.add_argument("--limit", type=int, default=0)
        if name == "run":
            sp.add_argument("--live", action="store_true", help="call the adapters; otherwise cached or NOT_ATTEMPTED")
            sp.add_argument("--json", action="store_true")
    p_hand = sub.add_parser("handoff", help="rows for the next batch from join/cards.json (SELECT / READ / REPLICATE / AUDIT)")
    p_hand.add_argument("--out", type=Path, default=DEFAULT_OUT)
    p_hand.add_argument("--date", required=True, help="YYYY-MM-DD written into the file (deterministic, never the clock)")
    p_hand.add_argument("--write", type=Path, default=None, help="write the Markdown here (e.g. research/repurposing_batch_selection_<date>_module.md)")
    p_hand.add_argument("--json", action="store_true")
    p_tgt = sub.add_parser("targets", help="TARGET -> COMPOUNDS from a census folder of retrievals already run (no network)")
    p_tgt.add_argument("--dir", required=True, help="repo-relative folder holding target_resolution.tsv, dgidb_*, chembl_*, opentargets_*")
    p_tgt.add_argument("symbols", nargs="+", help="HGNC symbols as written in target_resolution.tsv")
    p_diff = sub.add_parser("diff", help="diff one derived card against a hand-made card in cards/")
    p_diff.add_argument("query_id")
    p_diff.add_argument("handmade", type=Path)
    p_diff.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args(argv)
    if args.command == "handoff":
        cards = json.loads((args.out / "cards.json").read_text(encoding="utf-8"))
        queries = {q["query_id"]: q for q in json.loads((args.out / "queries.json").read_text(encoding="utf-8"))}
        state = json.loads((args.out / "state.json").read_text(encoding="utf-8")) if (args.out / "state.json").exists() else {}
        rows = handoff_rows(cards, queries)
        ev_path = args.out / "evidence.json"
        evidence = json.loads(ev_path.read_text(encoding="utf-8")) if ev_path.exists() else []
        text = render_handoff(rows, args.date, state.get("axis", ""), evidence)
        if args.write:
            args.write.write_text(text, encoding="utf-8")
            print(f"written {relative(args.write)}: {len(rows)} row(s)")
        elif args.json:
            print(json.dumps(rows, indent=1, ensure_ascii=False))
        else:
            print(text)
        return 0
    if args.command == "targets":
        print(json.dumps(target_compounds({"dir": args.dir, "symbols": args.symbols}), indent=1, ensure_ascii=False))
        return 0
    if args.command == "diff":
        cards = json.loads((args.out / "cards.json").read_text(encoding="utf-8"))
        derived = next((row["card"] for row in cards if row["query_id"] == args.query_id), None)
        if derived is None:
            print(f"no derived card for {args.query_id} in {relative(args.out / 'cards.json')}", file=sys.stderr)
            return 2
        handmade = json.loads(args.handmade.read_text(encoding="utf-8"))
        print(json.dumps(diff_against_handmade(derived, handmade), indent=1, ensure_ascii=False, sort_keys=True))
        return 0
    if args.command == "queries":
        queries = derive_queries(axis=args.axis)
        if args.limit:
            queries = queries[:args.limit]
        print(json.dumps(queries, indent=1, ensure_ascii=False, sort_keys=True))
        return 0
    summary = run(args.out, axis=args.axis, live=args.live, limit=args.limit)
    print(json.dumps(summary, indent=1, ensure_ascii=False, sort_keys=True) if args.json else render(summary))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
