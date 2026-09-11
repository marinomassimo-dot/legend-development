#!/usr/bin/env python3
"""coverage_report.py — make the reading debt visible, with an honest denominator.

LEGEND's parity-of-sources rule says a low-priority paper is *reading debt*, never a
discarded source. A rule like that is rhetoric unless somebody can count it. This script
derives, from the registries themselves, how much of the known corpus has actually been
read — and at which depth.

It is a **view, not a second source of truth**. Nothing here is hand-maintained: rerun it
and the numbers follow the registries. That is deliberate — a hand-pasted bibliography
freezes on the day it was pasted and then quietly disagrees with the canonical state.

Depth vocabulary (strongest first):

    full_text      a full text was read; the entry says so explicitly
    abstract       the record exists and was screened/classified, but no full text was read
    catalogued     a corpus placeholder: known, deduplicated, never analytically processed
    filtered       explicitly filtered out or archived, with the reason kept

Usage:
    python3 framework/scripts/coverage_report.py [--root .] [--disease wwox]
                                                 [--out FILE] [--json] [--check FILE]

`--check` re-derives the report and compares it to an existing file, so a stale committed
report fails a regression instead of misleading a reader.

No external dependencies. Read-only toward every registry.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

import fulltext_receipts as receipts
import derived_inputs  # noqa: E402
import growth_anchors

# The record conventions are defined once, in `growth_anchors.py`, and imported — never
# restated. This file used to restate them, and knew only `PAPER n` and `CORPUS Pn`. The 168
# `CORPUS-STUB-n` records were not merely absent from the denominator: an unrecognised heading
# does not split, so their bodies were absorbed into the preceding record and their `**Key:**`
# lines overwrote its fields. See the comment on `RECORD_PATTERNS` for what that did to
# `PAPER 032`.
ENTRY = growth_anchors.PAPER_REGISTRY_RECORD
TRACKING_ENTRY = growth_anchors.HEADINGS["literature"]
FIELD = re.compile(r"(?m)^\*\*(?P<key>[^:*]+):\*\*\s*(?P<value>.*)$")
PMID = re.compile(r"PMID[:\s]*(\d{7,8})")
DOI = re.compile(r"\b10\.\d{4,9}/[^\s\)\]\|,;]+", re.I)
YEAR = re.compile(r"\b(19|20)\d{2}\b")

FULL_TEXT_MARKERS = (
    "full text reviewed",
    "full text verificato",
    "complete_fulltext_read",
    "full text read",
)
PARTIAL_MARKERS = ("partial full text", "parziale")
FILTERED_STATES = ("filtered_out", "archived", "superseded")
DEPTH_RANK = {
    "filtered": 0,
    "catalogued": 1,
    "abstract": 2,
    "partial_full_text": 3,
    "full_text": 4,
}
RECEIPT_DEPTH = {
    "retrieved_not_read": "catalogued",
    "queried_not_full_read": "catalogued",
    "abstract_only": "abstract",
    "partial_fulltext_read": "partial_full_text",
    "complete_fulltext_read": "full_text",
}


def parse_entries(text: str) -> list[dict[str, str]]:
    entries: list[dict[str, str]] = []
    marks = list(ENTRY.finditer(text))
    for index, mark in enumerate(marks):
        end = marks[index + 1].start() if index + 1 < len(marks) else len(text)
        body = text[mark.end() : end]
        fields = {
            match.group("key").strip().lower(): match.group("value").strip()
            for match in FIELD.finditer(body)
        }
        fields["_id"] = " ".join(mark.group(1).split())
        fields["_kind"] = "PAPER" if fields["_id"].startswith("PAPER") else "CORPUS"
        fields["_body"] = body
        entries.append(fields)
    return entries


def first_year(entry: dict[str, str]) -> str:
    """Best-effort publication year, from the year field or the source citation."""
    for key in ("year", "journal/source", "identifier"):
        match = YEAR.search(entry.get(key, ""))
        if match:
            return match.group(0)
    return ""


def classify_depth(entry: dict[str, str]) -> str:
    depth = entry.get("evidence depth", "").lower()
    status = entry.get("status", "").lower()
    # Partial is checked first and independently: an entry may declare a partial read
    # without using any of the full-text markers, and must never round up to "read".
    if any(marker in depth for marker in PARTIAL_MARKERS):
        return "partial_full_text"
    if any(marker in depth for marker in FULL_TEXT_MARKERS):
        return "full_text"
    if any(state in status for state in FILTERED_STATES):
        return "filtered"
    if entry["_kind"] == "CORPUS" or "placeholder" in status or "not_processed" in status:
        return "catalogued"
    return "abstract"


def entry_receipt(entry: dict[str, str], index: dict[str, dict]) -> dict | None:
    identifier = entry.get("identifier", "")
    candidates = []
    for pmid in PMID.findall(identifier):
        if f"pmid:{pmid}" in index:
            candidates.append(index[f"pmid:{pmid}"])
    for doi in DOI.findall(identifier):
        key = f"doi:{receipts.normalise_doi(doi)}"
        if key in index:
            candidates.append(index[key])
    if not candidates:
        return None
    return max(candidates, key=lambda item: receipts.DEPTHS[item["evidence_depth"]])


def effective_depth(entry: dict[str, str], receipt: dict | None) -> str:
    registry_depth = classify_depth(entry)
    if receipt is None:
        return registry_depth
    receipt_depth = RECEIPT_DEPTH[receipt["evidence_depth"]]
    return max((registry_depth, receipt_depth), key=lambda item: DEPTH_RANK[item])


def receipt_owners(
    entries: list[dict[str, str]], index: dict[str, dict]
) -> dict[str, dict]:
    """Assign each receipt to one registry owner, preferring promoted PAPER over CORPUS.

    Promoted studies may retain their old CORPUS placeholder as an audit trail. A receipt
    describes the study, not both records; counting it twice would silently inflate coverage.
    """
    matches: dict[str, list[dict[str, str]]] = {}
    by_event: dict[str, dict] = {}
    for entry in entries:
        receipt = entry_receipt(entry, index)
        if receipt is None:
            continue
        matches.setdefault(receipt["event_id"], []).append(entry)
        by_event[receipt["event_id"]] = receipt
    owners: dict[str, dict] = {}
    for event_id, candidates in matches.items():
        owner = next(
            (entry for entry in candidates if entry["_kind"] == "PAPER"),
            candidates[0],
        )
        owners[owner["_id"]] = by_event[event_id]
    return owners


def receipt_matches_registry(receipt: dict, entries: list[dict[str, str]]) -> bool:
    study = receipt["study_id"]
    pmid = str(study.get("pmid") or "")
    doi = receipts.normalise_doi(study.get("doi"))
    for entry in entries:
        identifier = entry.get("identifier", "")
        if pmid and pmid in PMID.findall(identifier):
            return True
        if doi and doi in {receipts.normalise_doi(value) for value in DOI.findall(identifier)}:
            return True
    return False


def build(root: Path, disease: str) -> dict:
    registries = root / "disease-models" / disease / "registries"
    papers_path = registries / "paper_registry_current.md"
    if not papers_path.is_file():
        raise SystemExit(f"missing registry: {papers_path}")
    papers = papers_path.read_text(encoding="utf-8")
    entries = parse_entries(papers)

    ledger_path = receipts.default_ledger_path(root, disease)
    try:
        receipt_events = receipts.load_ledger(ledger_path)
        receipt_index = receipts.receipt_depth_index(ledger_path)
    except ValueError as error:
        raise SystemExit(f"invalid or missing full-text receipt ledger: {error}") from error

    owners = receipt_owners(entries, receipt_index)
    matched_receipt_events = sum(
        receipt_matches_registry(receipt, entries) for receipt in receipt_events
    )
    effective = [(entry, owners.get(entry["_id"])) for entry in entries]
    depths = Counter(effective_depth(entry, receipt) for entry, receipt in effective)
    kinds = Counter(entry["_kind"] for entry in entries)

    receipt_backed_complete = sum(
        1
        for entry, receipt in effective
        if receipt is not None and receipt["evidence_depth"] == "complete_fulltext_read"
    )
    registry_only_full = sum(
        1
        for entry, receipt in effective
        if classify_depth(entry) == "full_text"
        and (receipt is None or receipt["evidence_depth"] != "complete_fulltext_read")
    )

    pmids = set(PMID.findall(papers))
    tracking_path = registries / "literature_tracking_log_current.md"
    tracked = 0
    if tracking_path.is_file():
        tracking = tracking_path.read_text(encoding="utf-8")
        tracked = len(TRACKING_ENTRY.findall(tracking))
        pmids |= set(PMID.findall(tracking))

    debt = [
        {
            "id": entry["_id"],
            "title": entry.get("short title", "") or entry.get("full title", ""),
            "year": first_year(entry),
            "status": entry.get("status", ""),
        }
        for entry in entries
        if effective_depth(entry, owners.get(entry["_id"])) == "catalogued"
    ]

    return {
        "disease": disease,
        "entries_total": len(entries),
        "paper_records": kinds.get("PAPER", 0),
        "corpus_placeholders": kinds.get("CORPUS", 0),
        "tracking_entries": tracked,
        "unique_pmids": len(pmids),
        "depth": dict(sorted(depths.items(), key=lambda item: -item[1])),
        "reading_debt_count": len(debt),
        "reading_debt": debt,
        "receipt_ledger": str(ledger_path.relative_to(root)),
        "receipt_events": len(receipt_events),
        "contemporaneous_receipts": sum(
            event["record_kind"] == "contemporaneous_receipt" for event in receipt_events
        ),
        "legacy_reconstructions": sum(
            event["record_kind"] == "legacy_reconstruction" for event in receipt_events
        ),
        # Administrative rows attest no reading of their own. They are counted separately
        # rather than left out: two buckets over four kinds is a sentence that silently stops
        # summing, and a reader who adds the printed numbers and finds them short of the
        # event total has no way to tell a missing bucket from a missing record.
        "identity_corrections": sum(
            event["record_kind"] == "identity_correction" for event in receipt_events
        ),
        "receipt_invalidations": sum(
            event["record_kind"] == "receipt_invalidation" for event in receipt_events
        ),
        "receipt_backed_complete_records": receipt_backed_complete,
        "registry_only_full_records": registry_only_full,
        "receipt_events_without_registry_match": len(receipt_events) - matched_receipt_events,
    }


def render(report: dict) -> str:
    depth = report["depth"]
    total = report["entries_total"] or 1

    def row(label: str, key: str, meaning: str) -> str:
        count = depth.get(key, 0)
        return f"| {label} | {count} | {count / total:.0%} | {meaning} |"

    lines = [
        f"# Corpus coverage and reading debt — {report['disease'].upper()}",
        "",
        "> **Generated file — do not edit by hand.** Regenerate with:",
        "> ```bash",
        f"> python3 framework/scripts/coverage_report.py --disease {report['disease']} \\",
        f">     --out disease-models/{report['disease']}/registries/coverage_report.md",
        "> ```",
        "> It is a *view* over the canonical registries plus the append-only receipt ledger,",
        "> never a second source of truth. A regression",
        "> test re-derives it and fails if this file has drifted.",
        "",
        "## Why this page exists",
        "",
        "LEGEND ranks sources to order reading, **never to justify not reading them**. A source",
        "that has not been read yet is *reading debt* — tracked, not discarded. That principle is",
        "only credible if the debt is countable, so here it is counted, including the part that",
        "makes the project look incomplete. It is supposed to look incomplete: the denominator is",
        "the whole known corpus, not the part already processed.",
        "",
        "## Coverage",
        "",
        "| Depth | Records | Share | What it means |",
        "|---|---:|---:|---|",
        row("**Full text depth**", "full_text", "complete receipt or legacy registry declaration; trace split below"),
        row("Partial full text", "partial_full_text", "some sections read; explicitly declared incomplete"),
        row("Abstract / screened", "abstract", "classified from metadata and abstract; no full text read"),
        row("Catalogued only", "catalogued", "known, deduplicated, never analytically processed — **the debt**"),
        row("Filtered / superseded", "filtered", "explicitly set aside, with the reason preserved"),
        "",
        f"- **{report['paper_records']}** promoted `PAPER` records · **{report['corpus_placeholders']}** `CORPUS` placeholders",
        f"- **{report['tracking_entries']}** lifecycle entries in the literature tracking log",
        f"- **{report['unique_pmids']}** unique PMIDs known across the registries",
        "",
        "## Receipt trace",
        "",
        f"- Authoritative ledger: `{report['receipt_ledger']}`",
        f"- **{report['receipt_events']}** append-only events: "
        f"**{report['contemporaneous_receipts']}** contemporaneous · "
        f"**{report['legacy_reconstructions']}** conservative legacy reconstructions · "
        f"**{report['receipt_invalidations']}** invalidation(s) · "
        f"**{report['identity_corrections']}** identity correction(s)",
        f"- **{report['receipt_backed_complete_records']}** registry records have a persisted "
        "`complete_fulltext_read` receipt",
        f"- **{report['registry_only_full_records']}** records still rely on a historical registry "
        "full-text declaration without a surviving complete coverage receipt",
        f"- **{report['receipt_events_without_registry_match']}** receipt event(s) do not yet map "
        "to a registry record",
        "",
        "A full-text marker in the registry is preserved as historical state, but it is not",
        "retroactively converted into a complete receipt. Only a contemporaneous or adequately",
        "evidenced legacy receipt with a complete coverage map closes the trace.",
        "",
        "## ⚠️ Historical reading debt",
        "",
        "The registry is known to",
        "under-record. An audit on 2026-07-25 against the private working archive found **80**",
        "distinct full texts that had actually been retrieved and worked; **43** of their PMIDs are",
        "present in this registry, and only **5** of those carried a declared `Evidence depth`.",
        "The remaining records were read but never had the field set — the work happened, but",
        "a public receipt cannot be reconstructed without surviving evidence.",
        "",
        "Back-filling them is evidence work: it requires checking each record against surviving",
        "dossiers or the retrieved text, not flipping a field because a PDF exists. A",
        "downloaded file is not a read paper, in the same way that protein abundance is not",
        "function — see `PROTEIN_STATE_IDENTITY_GATE` in the learned-gates registry. Until that",
        "back-fill is done, **treat the full-text figure here as a floor, not an estimate.**",
        "",
        "The number is published in this direction on purpose. Understating your own coverage is",
        "the safe error; the unsafe one is a metric that reads a filename as evidence of reading.",
        "",
        "## How to read these numbers honestly",
        "",
        "A high catalogued count is **not** a backlog failure — it is the anti-false-negative design",
        "working. Every one of those records was deduplicated against the registries and kept with its",
        "identifiers, so it can be retrieved the moment a new mechanism makes it relevant. The failure",
        "mode this prevents is the opposite one: a paper screened out, forgotten, and never reconsidered.",
        "",
        "It happened once, and it is why the reading-debt tooling exists: a paper sat in the corpus",
        "marked high-relevance and unread while the same conclusion was reconstructed from scratch",
        "in silico. Surface those first:",
        "",
        "```bash",
        "python3 framework/scripts/unread_gold.py .",
        "```",
        "",
        "## Bringing new studies in",
        "",
        "Never start from a raw bibliography. Deduplicate it against the registries first — the intake",
        "gate answers *known / in-pipeline / new / ambiguous* before any retrieval effort is spent:",
        "",
        "```bash",
        "python3 .claude/skills/legend-study-intake-triage/scripts/study_dedup_triage.py \\",
        "    --workspace . --input your_pubmed_export.txt --out triage.md",
        "```",
        "",
        "Then the batch sweep and the priority matrix order what to read first. See [`SKILLS.md`](../../../SKILLS.md).",
        "",
        "## Scope",
        "",
        "Bibliographic metadata only — identifiers, titles, processing state. No full texts are",
        "redistributed and no individual-level information appears here.",
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--disease", default="wwox")
    parser.add_argument("--out", default="")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--check", default="", help="compare against an existing report and fail on drift")
    derived_inputs.add_argument(parser)
    args = parser.parse_args()

    if args.out and not (args.json or args.check):
        # 2026-09-09 C22: derived surfaces bind to committed inputs, or say why not — checked
        # before anything is read, so the refusal does not depend on parseability.
        root = Path(args.root)
        state = derived_inputs.input_state(
            root, [root / "disease-models" / args.disease / "registries"],
            exclude=[Path(args.out)])
        refused = derived_inputs.refuse_if_dirty(state, reason=args.inputs_dirty_because,
                                                 surface=args.out)
        if refused is not None:
            return refused

    report = build(Path(args.root), args.disease)

    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
        return 0

    rendered = render(report)

    if args.check:
        existing = Path(args.check)
        if not existing.is_file():
            print(f"MISSING: {existing}", file=sys.stderr)
            return 1
        if existing.read_text(encoding="utf-8") != rendered:
            print(f"DRIFT: {existing} no longer matches the registries", file=sys.stderr)
            return 1
        print(f"OK: {existing} matches the registries")
        return 0

    if args.out:
        Path(args.out).write_text(rendered, encoding="utf-8")
        print(f"written: {args.out}")
    else:
        print(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
