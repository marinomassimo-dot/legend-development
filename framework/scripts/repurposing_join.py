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
import hashlib
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import registry_records as rr  # noqa: E402  the routed way to read a registry, never grep
import repurposing_bridge as bridge  # noqa: E402
import repurposing_adapter as adapters  # noqa: E402

ROOT = HERE.parents[1]
DISEASE = "wwox"
MODEL = ROOT / "disease-models" / DISEASE
DEFAULT_OUT = MODEL / "research" / "drug_repurposing" / "join"
MECHANISM_MAP = MODEL / "analysis" / "mechanism_intervention_map.md"
PATHOGRAPH = MODEL / "analysis" / "data" / "pathograph_export.jsonl"
MANIFESTS = MODEL / "research" / "deepdive_manifests"
ADJUDICATIONS = MODEL / "research" / "page_adjudications"
RECEIPT_LEDGER = MODEL / "research" / "fulltext_read_receipts.jsonl"

# The three axes the mandate calls live. Plain data: delete a row and the axis is gone.
AXES = {
    "proteostasis": ["proteostasis", "chaperone", "phenylbutyrate", "misfolding", "SDR", "missense",
                     "proteasome", "HSP70", "UPR", "ERAD", "solubility"],
    "calcium": ["T-type", "CACNA1G", "CACNA1H", "CACNA1I", "calcium channel", "Ca2+", "Ca²⁺",
                "ethosuximide", "bursting", "NMDAR", "network"],
    "wnt": ["Wnt", "MYC", "GSK3", "mTOR", "beta-catenin", "β-catenin", "tankyrase", "lithium",
            "rapamycin", "everolimus"],
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
GENE_TOKEN = re.compile(r"\b[A-Z][A-Z0-9]{2,7}\b")
PMID_IN_TEXT = re.compile(r"\bPMID[\s:_-]*(\d{6,9})\b")
MECHANISM_RECORD = re.compile(r"^### ([RN]-\d{2}) — (.+?)$", re.M)
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
                    "pmids": sorted(set(PMID_IN_TEXT.findall(record.text)))})
    return out


def lead_queries(root: Path) -> list[dict]:
    out = []
    for record in rr.parse_records(root, DISEASE, "discovery_ledger_current"):
        if record.kind != "record" or not record.record_id.upper().lstrip("🔴 ").startswith("DL-"):
            continue
        fields = record_fields(record.text)
        causal = fields.get("Causal statement", "") or fields.get("Catena di ragionamento", "")
        out.append({"query_id": f"Q-{rr.identity_token(record.record_id)}",
                    "kind": "lead", "origin_id": rr.identity_token(record.record_id),
                    "origin_file": record.path, "origin_line": record.line,
                    "origin_title": record.record_id[:300],
                    "terms": gene_tokens(record.record_id + " " + causal),
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
                    "pmids": sorted(set(PMID_IN_TEXT.findall(row["text"])))})
    return out


def derive_queries(root: Path = ROOT, axis: str = "") -> list[dict]:
    queries = claim_queries(root) + lead_queries(root) + mechanism_queries() + pathograph_queries()
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


def strongest_depth(events: list[dict]) -> str:
    best, rank = "UNKNOWN", -1
    for event in events:
        state = str(event.get("reading_depth") or event.get("event_type") or event.get("coverage") or "")
        if DEPTH_RANK.get(state, -1) > rank:
            best, rank = state, DEPTH_RANK.get(state, -1)
    return best


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


def manifest_evidence(pmid: str) -> dict:
    """What the manifest for one paper evidences, with the audit status of its locators.

    A locator count is len(entries) — never len(mapping), the defect that cost this repository a
    day (`harness_mandate_20261022.md` § 6)."""
    path = MANIFESTS / f"PMID{pmid}.json"
    row = {"pmid": pmid, "manifest": relative(path) if path.exists() else "",
           "locator_count": 0, "audited_entries": 0, "unaudited_contradictions": 0,
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
        auditors = declaration.get("auditors")
        count = len(auditors) if isinstance(auditors, list) else int(auditors or 0)
        verdict = str(declaration.get("verdict") or "UNSTATED")
        row["contradiction_verdicts"].append({"verdict": verdict, "auditors": count})
        if count:
            row["audited_entries"] += 1
        else:
            row["unaudited_contradictions"] += 1
    row["audit_status"] = ("AUDIT_FILE_PRESENT" if row["adjudication_files"]
                           else "UNAUDITED" if row["locator_count"]
                           else "NO_LOCATORS")
    return row


def evidence_for(query: dict, receipts: dict[str, list[dict]]) -> dict:
    rows = []
    for pmid in query.get("pmids", []):
        events = receipts.get(pmid, [])
        row = manifest_evidence(pmid)
        row["reading_depth"] = strongest_depth(events) if events else "NO_RECEIPT"
        row["receipt_events"] = len(events)
        row["evidence_label"] = "WWOX EVIDENCE (receipted in this repository)"
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
             "abstention": "NO_RECEIPTED_EVIDENCE_FOR_THIS_QUERY" if not rows else None}
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
        result = module.query(request)
        cache_dir.mkdir(parents=True, exist_ok=True)
        cached.write_text(json.dumps(result, indent=1, ensure_ascii=False, sort_keys=True), encoding="utf-8")
        hits.append(result)
    return hits


def card_for(query: dict, table: dict, hits: list[dict]) -> dict | None:
    """A bridge packet composed from the evidence table and the adapter hits, then built by the
    bridge itself. Composed, never typed: every assertion names the record it came from."""
    candidate = query.get("candidate")
    if not candidate:
        return None
    disease_assertion = {
        "id": f"DA-{query['query_id']}",
        "target_id": query.get("target", "UNKNOWN")[:120] or "UNKNOWN",
        "endpoint": "UNKNOWN",
        "direction": "UNKNOWN",
        "source": f"{query['origin_file']} {query['origin_id']}",
        "locator": f"{query['origin_file']}:{query['origin_line']}",
        "epistemic_status": "IPOTESI",
        "reading_depth": (table["rows"][0]["reading_depth"] if table["rows"] else "UNKNOWN"),
        "context": {key: "UNKNOWN" for key in bridge.CONTEXT},
    }
    if disease_assertion["reading_depth"] not in bridge.READING:
        disease_assertion["reading_depth"] = "UNKNOWN"
    external = [hit for hit in hits if hit.get("status") == "MATCH_FOUND"]
    packet = {
        "schema_version": 1,
        "route": "RECUPERO_PROFONDO",
        "candidate": {"id": query["query_id"], "name": candidate},
        "disease_assertion": disease_assertion,
        "drug_assertions": [],
        "label_lookup": {"status": "NOT_ATTEMPTED"},
        "p4_fields": {
            "endpoint_pursued": "UNKNOWN",
            "functional_evidence_available": "UNKNOWN",
            "temporal_or_model_limit": "UNKNOWN",
            "cellular_context": {key: "UNKNOWN" for key in bridge.P4_CONTEXT},
        },
        "p4_roadmap_fields": {
            "indication_and_transfer": query.get("intervention", "UNKNOWN")[:400],
            "verification_scope": (f"derived by repurposing_join.py from {query['origin_file']}:"
                                   f"{query['origin_line']}; evidence table digest {table['digest']}"),
        },
        "derived_by": "framework/scripts/repurposing_join.py",
        "legend_evidence": table,
        "external_sources": [
            {"adapter": hit.get("adapter"), "status": hit.get("status"),
             "retrieved_at": hit.get("retrieved_at"), "source_version": hit.get("source_version"),
             "licence": hit.get("licence"), "citation": hit.get("citation"),
             "requests_sent": hit.get("requests_sent"), "hit_count": len(hit.get("hits") or []),
             "evidence_label": "NOT WWOX EVIDENCE"}
            for hit in hits
        ],
    }
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
            packet["label_lookup"] = {"status": "NOT_ATTEMPTED"}
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
        return {"dependence": "NO_RECEIPTED_EVIDENCE",
                "measurement": "a first receipted reading of a paper that measures this mechanism "
                               "in a WWOX system; until then the external hits stand alone and are NOT WWOX EVIDENCE",
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
        table = evidence_for(query, receipts)
        tables.append(table)
        hits = run_adapters(query, cache_dir, live)
        card = card_for(query, table, hits)
        if card is not None:
            cards.append({"query_id": query["query_id"], "card": card})
    before = previous_state(out_dir)
    state = {"queries": {q["query_id"]: q["digest"] for q in queries},
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
    p_diff = sub.add_parser("diff", help="diff one derived card against a hand-made card in cards/")
    p_diff.add_argument("query_id")
    p_diff.add_argument("handmade", type=Path)
    p_diff.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args(argv)
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
