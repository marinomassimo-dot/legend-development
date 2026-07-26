#!/usr/bin/env python3
"""batch_queue.py — turn a dated bibliography snapshot into a resumable work queue.

The problem this solves is mundane and real: somebody willing to contribute opens the
repository and does not know *which paper to read next*. The registries say what has been
processed; they do not say what is still outstanding against a defined search.

So the queue is built from two clearly separated things:

  1. **A seed corpus** — a dated, inert snapshot of a literature search (`corpus_seed_*.tsv`).
     It is allowed to be static because it *is* a snapshot: it carries its date and never
     claims to be current. Adding a newer snapshot does not invalidate an older one.

  2. **Status** — derived here, every run, by joining the seed against the registries on
     PMID and DOI. Nothing about status is hand-maintained, so the queue cannot drift into
     disagreeing with the canonical state.

The join is deliberately **exact-identifier only**. Fuzzy title matching, preprint-versus-
published disambiguation and aggregate-line splitting belong to the intake skill, which is
a different and larger job; pretending to reimplement it here would produce a second,
weaker classifier. Records the identifiers cannot resolve are reported as `unmatched`,
which is an honest "run the intake gate on this", not a claim that they are new.

Usage:
    python3 framework/scripts/batch_queue.py [--root .] [--disease wwox]
                                             [--out FILE] [--json] [--check FILE]
                                             [--limit N]

No external dependencies. Read-only toward every registry.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path

sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[2] / ".claude" / "skills"
        / "legend-study-intake-triage" / "scripts"),
)
import study_dedup_triage as triage  # noqa: E402
import fulltext_receipts as receipts  # noqa: E402

# What the reader is actually asking: "which of these has nobody processed yet?"
# The answer comes from the intake gate, which is the authoritative classifier — this file
# used to answer it with its own exact-identifier join, which is a weaker duplicate and
# left 45% of the corpus in an "unmatched" bucket that meant "you go find out".
ACTION = {
    "NEW": "start here — never seen by the system",
    "CORPUS_CATALOGUED": "start here — catalogued, never processed",
    "OUT_OF_SCOPE_LIKELY": "later in the queue — no scope signal in the title",
    "AMBIGUOUS": "resolve identifiers first",
    "AGGREGATE_LINE": "split the row first",
    "IN_PIPELINE": "already in flight",
    "KNOWN_INTEGRATED": "done — see read depth",
}
ACTION_RANK = {
    "NEW": 0,
    "CORPUS_CATALOGUED": 1,
    "AMBIGUOUS": 2,
    "AGGREGATE_LINE": 3,
    "OUT_OF_SCOPE_LIKELY": 4,
    "IN_PIPELINE": 5,
    "KNOWN_INTEGRATED": 6,
}

PMID = re.compile(r"PMID\s*:?\s*(\d{7,8})", re.IGNORECASE)
DOI = re.compile(r"\b10\.\d{4,9}/[^\s\)\]\|,;]+")
ENTRY = re.compile(
    r"(?m)^##\s+(PAPER\s+\d+|CORPUS\s+P\d+|CORPUS-STUB-\d+)\s*$"
)

FULL_TEXT_MARKERS = (
    "full text reviewed",
    "full text verificato",
    "complete_fulltext_read",
    "full text read",
)
PARTIAL_MARKERS = ("partial full text", "parziale")
DEPTH_RANK = {
    "unmatched": 0,
    "catalogued only": 1,
    "screened": 2,
    "abstract only": 3,
    "partial full text": 4,
    "full text": 5,
}
RECEIPT_DEPTH = {
    "retrieved_not_read": "catalogued only",
    "queried_not_full_read": "catalogued only",
    "abstract_only": "abstract only",
    "partial_fulltext_read": "partial full text",
    "complete_fulltext_read": "full text",
}


def normalise_doi(value: str) -> str:
    return value.strip().rstrip(".").lower()


def identifiers(field: str) -> tuple[set[str], set[str]]:
    """Extract identifiers from an entry's *own* identifier field.

    A tracking entry may store an exact PMID either as ``PMID 41153369`` or as the
    bare value ``41153369``. Bare 7–8 digit values are safe to interpret here because
    the caller has already isolated the dedicated Identifier field; applying the same
    rule to an entire record body would recreate the cited-identifier inheritance bug.
    """
    pmids = set(PMID.findall(field))
    if not pmids:
        pmids.update(re.findall(r"(?<![A-Za-z0-9])(\d{7,8})(?![A-Za-z0-9])", field))
    dois = {normalise_doi(value) for value in DOI.findall(field)}
    return pmids, dois


def store_deepest(index: dict[str, dict[str, str]], key: str, entry: dict[str, str]) -> None:
    """Keep the deepest evidence record, independent of physical file order."""
    current = index.get(key)
    if current is None or DEPTH_RANK[entry["depth"]] > DEPTH_RANK[current["depth"]]:
        index[key] = entry


def registry_index(registries: Path) -> dict[str, dict[str, str]]:
    """Map every known PMID and DOI to the record that owns it, plus its read depth."""
    index: dict[str, dict[str, str]] = {}
    papers_path = registries / "paper_registry_current.md"
    if not papers_path.is_file():
        raise SystemExit(f"missing registry: {papers_path}")
    text = papers_path.read_text(encoding="utf-8")
    ledger = registries / "fulltext_read_receipts.jsonl"
    try:
        receipt_index = receipts.receipt_depth_index(ledger)
    except ValueError as error:
        raise SystemExit(f"invalid or missing full-text receipt ledger: {error}") from error

    marks = list(ENTRY.finditer(text))
    for position, mark in enumerate(marks):
        end = marks[position + 1].start() if position + 1 < len(marks) else len(text)
        body = text[mark.end() : end]
        record_id = " ".join(mark.group(1).split())
        depth_field = ""
        match = re.search(r"(?m)^\*\*Evidence depth:\*\*\s*(.*)$", body)
        if match:
            depth_field = match.group(1).lower()
        if any(marker in depth_field for marker in PARTIAL_MARKERS):
            depth = "partial full text"
        elif any(marker in depth_field for marker in FULL_TEXT_MARKERS):
            depth = "full text"
        elif record_id.startswith("CORPUS"):
            depth = "catalogued only"
        else:
            depth = "abstract only"
        entry = {"record": record_id, "depth": depth}
        # Only the record's own Identifier field. Indexing every identifier that appears
        # anywhere in the body would attribute a record's read depth to every paper it
        # merely cites — an overstatement of coverage by roughly six-fold when measured.
        identifier = re.search(r"(?m)^\*\*Identifier:\*\*\s*(.*)$", body)
        own = identifier.group(1) if identifier else ""
        pmids, dois = identifiers(own)
        for pmid in pmids:
            store_deepest(index, f"pmid:{pmid}", entry)
        for doi in dois:
            store_deepest(index, f"doi:{doi}", entry)

    tracking = registries / "literature_tracking_log_current.md"
    if tracking.is_file():
        log = tracking.read_text(encoding="utf-8")
        # Same restriction: the declared identifier of the entry, not identifiers cited in it.
        for line in re.findall(r"(?m)^\*\*Identifier value:\*\*\s*(.*)$", log):
            pmids, dois = identifiers(line)
            for pmid in pmids:
                store_deepest(
                    index,
                    f"pmid:{pmid}",
                    {"record": "tracking log", "depth": "screened"},
                )
            for doi in dois:
                store_deepest(
                    index,
                    f"doi:{doi}",
                    {"record": "tracking log", "depth": "screened"},
                )
    for key, receipt in receipt_index.items():
        store_deepest(
            index,
            key,
            {
                "record": f"receipt {receipt['event_id']}",
                "depth": RECEIPT_DEPTH[receipt["evidence_depth"]],
            },
        )
    return index


def load_seeds(registries: Path) -> tuple[list[dict[str, str]], int]:
    """Load the union of dated snapshots, deduplicated by PMID (or DOI fallback).

    A later snapshot may legitimately repeat older papers. The queue counts papers, not
    export occurrences, so the latest occurrence wins while every source filename remains
    attached for provenance.
    """
    seeds_by_key: dict[str, dict[str, str]] = {}
    occurrences = 0
    def snapshot_order(path: Path) -> tuple[str, str]:
        match = re.search(r"_(\d{8})\.tsv$", path.name)
        return (match.group(1) if match else "", path.name)

    for path in sorted(registries.glob("corpus_seed_*.tsv"), key=snapshot_order):
        with path.open(encoding="utf-8", newline="") as handle:
            for row in csv.DictReader(handle, delimiter="\t"):
                occurrences += 1
                pmid = row.get("pmid", "").strip()
                doi = normalise_doi(row.get("doi", ""))
                key = f"pmid:{pmid}" if pmid else f"doi:{doi}"
                if key in {"pmid:", "doi:"}:
                    raise SystemExit(f"seed row without PMID or DOI: {path}")
                previous = seeds_by_key.get(key)
                sources = set(previous.get("_sources", "").split(";")) if previous else set()
                sources.discard("")
                sources.add(path.name)
                row["_sources"] = ";".join(sorted(sources))
                seeds_by_key[key] = row
    return list(seeds_by_key.values()), occurrences


_BUILD_CACHE: dict[tuple[str, str], dict] = {}


def build(root: Path, disease: str) -> dict:
    """Memoised: classifying the seed through the intake gate is the expensive step
    (hundreds of fuzzy comparisons per record), and callers legitimately ask for the same
    report several times in one process — the regression suite most of all."""
    key = (str(Path(root).resolve()), disease)
    cached = _BUILD_CACHE.get(key)
    if cached is not None:
        return cached
    report = _build_uncached(Path(root), disease)
    _BUILD_CACHE[key] = report
    return report


def _build_uncached(root: Path, disease: str) -> dict:
    registries = root / "disease-models" / disease / "registries"
    index = registry_index(registries)
    seeds, occurrences = load_seeds(registries)

    # The authoritative classification comes from the intake gate itself, run here over the
    # seed corpus. Reusing it means there is exactly one classifier in the repository.
    records = triage.build_index(root)
    identifier_index = triage.build_identifier_index(root)

    queue: list[dict[str, str]] = []
    counts = {"full text": 0, "partial full text": 0, "abstract only": 0, "catalogued only": 0, "screened": 0, "unmatched": 0}
    actions: dict[str, int] = {}
    for seed in seeds:
        hit = index.get(f"pmid:{seed.get('pmid','')}")
        if hit is None and seed.get("doi"):
            hit = index.get(f"doi:{normalise_doi(seed['doi'])}")
        depth = hit["depth"] if hit else "unmatched"
        counts[depth] = counts.get(depth, 0) + 1

        line = (
            f"{seed.get('title','')}. — PMID {seed.get('pmid','')}"
            f" · DOI {seed.get('doi','')} · YEAR {seed.get('year','')}"
        )
        verdict = triage.match_row(
            {"line": line, "raw": "", "aggregate": "no"}, records, identifier_index
        )
        triage_class = verdict["class"]
        actions[triage_class] = actions.get(triage_class, 0) + 1

        queue.append(
            {
                "triage_class": triage_class,
                "action": ACTION.get(triage_class, triage_class),
                "pmid": seed.get("pmid", ""),
                "year": seed.get("year", ""),
                "title": seed.get("title", ""),
                "free_full_text": seed.get("free_full_text", ""),
                "type": seed.get("type", ""),
                "depth": depth,
                "record": hit["record"] if hit else "",
                "source": seed["_sources"],
            }
        )

    def sort_key(item: dict[str, str]) -> tuple:
        # what to do about it first, then free full text, then most recent
        return (
            ACTION_RANK.get(item["triage_class"], 9),
            DEPTH_RANK.get(item["depth"], 9),
            0 if item["free_full_text"] == "yes" else 1,
            -int(item["year"] or 0),
        )

    queue.sort(key=sort_key)
    START_HERE = {"NEW", "CORPUS_CATALOGUED"}
    outstanding = [item for item in queue if item["triage_class"] in START_HERE]
    ready_now = [
        item
        for item in outstanding
        if item["free_full_text"] == "yes" and item["depth"] != "full text"
    ]
    years = [int(seed["year"]) for seed in seeds if seed.get("year", "").isdigit()]
    return {
        "disease": disease,
        "seed_files": sorted(
            {source for seed in seeds for source in seed["_sources"].split(";")}
        ),
        "seed_occurrences": occurrences,
        "duplicate_occurrences": occurrences - len(seeds),
        "seed_total": len(seeds),
        "free_full_text": sum(1 for seed in seeds if seed.get("free_full_text") == "yes"),
        "year_min": min(years) if years else None,
        "year_max": max(years) if years else None,
        "published_since_2020": sum(year >= 2020 for year in years),
        "counts": counts,
        "actions": actions,
        "outstanding": len(outstanding),
        "ready_now": len(ready_now),
        "queue": queue,
    }


def render(report: dict, limit: int) -> str:
    counts = report["counts"]
    total = report["seed_total"] or 1
    head = [
        f"# Batch queue — {report['disease'].upper()}",
        "",
        "> **Generated file — do not edit by hand.** Regenerate with:",
        "> ```bash",
        f"> python3 framework/scripts/batch_queue.py --disease {report['disease']} \\",
        f">     --out disease-models/{report['disease']}/registries/batch_queue.md",
        "> ```",
        "",
        "## ▶ Start here",
        "",
        f"**{report['outstanding']} records have not been processed.** "
        f"**{report['ready_now']}** of them have a free full text and can be worked immediately.",
        "",
        "| Verdict | Records | What it means |",
        "|---|---:|---|",
        f"| 🟢 **`NEW`** | {report['actions'].get('NEW', 0)} | never seen by the system — **the front of the queue** |",
        f"| 🟢 **`CORPUS_CATALOGUED`** | {report['actions'].get('CORPUS_CATALOGUED', 0)} | catalogued and deduplicated, never analytically processed |",
        f"| 🟡 `OUT_OF_SCOPE_LIKELY` | {report['actions'].get('OUT_OF_SCOPE_LIKELY', 0)} | no scope signal in the title — later in the queue, **never discarded** |",
        f"| 🟡 `AMBIGUOUS` | {report['actions'].get('AMBIGUOUS', 0)} | identifiers must be resolved before ingest |",
        f"| ⏳ `IN_PIPELINE` | {report['actions'].get('IN_PIPELINE', 0)} | already in flight |",
        f"| ✅ `KNOWN_INTEGRATED` | {report['actions'].get('KNOWN_INTEGRATED', 0)} | done — read depth in the table below |",
        "",
        "The two green rows are the answer to *\"where do I start?\"*. The table further down lists",
        "every record in this order, so a second person can take the next unclaimed row without",
        "coordinating with anyone.",
        "",
        "> **These verdicts are not computed here.** They come from the intake gate",
        "> (`legend-study-intake-triage`), imported and run over the seed corpus, so the repository",
        "> has exactly one classifier. An earlier version of this file answered with its own",
        "> identifier join and left 45% of the corpus in an `unmatched` bucket that really meant",
        "> \"go and find out yourself\" — a queue that hands the work back is not a queue.",
        "",
        "## What this is for",
        "",
        "If you want to run a batch and do not know where to take the papers from, take them",
        "from here. This joins a **dated bibliography snapshot** against the registries and shows",
        "what is still outstanding, most useful first.",
        "",
        "Two files, two different natures. The seed corpus is a *snapshot* — it carries its date",
        "and never claims to be current. The status column is *derived on every run*, so it cannot",
        "quietly disagree with the canonical state. When a snapshot is exhausted, add another one",
        "next to it; older snapshots stay valid as history.",
        "",
        f"**Seed corpus:** {', '.join(f'`{name}`' for name in report['seed_files'])} — "
        f"{report['seed_total']} records, {report['free_full_text']} with free full text.",
        f"Coverage years: **{report['year_min']}–{report['year_max']}**; "
        f"{report['published_since_2020']} records are from 2020 onward. This is therefore a",
        "broad historical-plus-recent corpus, not a recent-only list.",
        (
            f"The snapshots contain {report['seed_occurrences']} export occurrences; "
            f"{report['duplicate_occurrences']} repeated occurrence(s) are deduplicated in this queue."
        ),
        "",
        "**Provenance and limit.** The current seed is an operator-curated PubMed Clipboard",
        "export dated 2026-07-05. The exact upstream query and selection procedure were not",
        "retained, so this is a useful worklist — **not a systematic or exhaustive WWOX search**.",
        "`free_full_text=yes` records PubMed's `Free PMC article` flag at export time; it does",
        "not redistribute or license the article text.",
        "",
        "## Read depth of what *has* been touched",
        "",
        "| Status | Records | Share |",
        "|---|---:|---:|",
    ]
    labels = [
        ("unmatched", "**Not found by identifier** — run the intake gate"),
        ("catalogued only", "**Catalogued, never processed** — the reading debt"),
        ("screened", "Known to the tracking log only"),
        ("abstract only", "Processed from the abstract"),
        ("partial full text", "Partial full text read"),
        ("full text", "Full text read"),
    ]
    for key, label in labels:
        value = counts.get(key, 0)
        head.append(f"| {label} | {value} | {value / total:.0%} |")
    head += [
        "",
        "⚠️ This second table combines registry state with the authoritative append-only",
        "`fulltext_read_receipts.jsonl`. Historical registry-only full-text declarations remain",
        "visible but are separated from receipt-backed completion in `coverage_report.md`.",
        "",
        "> `unmatched` means the exact PMID/DOI join found nothing — not that the paper is new.",
        "> Preprint-versus-published pairs, aggregate lines and title-only records need the intake",
        "> gate, which does fuzzy matching and disambiguation this join deliberately does not:",
        "> ```bash",
        "> python3 .claude/skills/legend-study-intake-triage/scripts/study_dedup_triage.py \\",
        ">     --workspace . --input <your_export.txt> --out triage.md",
        "> ```",
        "",
        (
            "## Complete outstanding queue"
            if limit <= 0
            else f"## Next up — first {limit} outstanding records"
        ),
        "",
        "| PMID | Year | FT | Type | Status | Title |",
        "|---|---:|:---:|---|---|---|",
    ]
    shown = 0
    for item in report["queue"]:
        if item["depth"] not in {"unmatched", "catalogued only", "screened"}:
            continue
        if limit > 0 and shown >= limit:
            break
        free = "✅" if item["free_full_text"] == "yes" else "—"
        title = item["title"].replace("|", "\\|")
        head.append(
            f"| [{item['pmid']}](https://pubmed.ncbi.nlm.nih.gov/{item['pmid']}/) "
            f"| {item['year']} | {free} | {item['type']} | {item['depth']} | {title} |"
        )
        shown += 1
    head += [
        "",
        (
            f"*(showing all {shown} outstanding records)*"
            if limit <= 0
            else f"*(showing {shown} of {report['outstanding']}; regenerate with `--limit 0` for all)*"
        ),
        "",
        "## Already processed from this seed",
        "",
        "These records are not reading debt. Their row-level depth is still shown so an",
        "abstract-only paper can be upgraded to a full-text deep dive without being mistaken",
        "for an entirely unprocessed record.",
        "",
        "| PMID | Year | FT | Evidence depth | Registry record | Title |",
        "|---|---:|:---:|---|---|---|",
    ]
    processed = 0
    for item in report["queue"]:
        if item["depth"] not in {"abstract only", "partial full text", "full text"}:
            continue
        free = "✅" if item["free_full_text"] == "yes" else "—"
        title = item["title"].replace("|", "\\|")
        head.append(
            f"| [{item['pmid']}](https://pubmed.ncbi.nlm.nih.gov/{item['pmid']}/) "
            f"| {item['year']} | {free} | {item['depth']} | {item['record']} | {title} |"
        )
        processed += 1
    head += [
        "",
        f"*(showing all {processed} processed records from the seed)*",
        "",
        "## How to work one",
        "",
        "```bash",
        "# 1. is it really new? the intake gate decides, not this table",
        "python3 .claude/skills/legend-study-intake-triage/scripts/study_dedup_triage.py \\",
        "    --workspace . --input one_record.txt --out triage.md",
        "```",
        "",
        "Then, in an agent runtime: *\"deep dive PMID …\"* for a canonical claim, or",
        "*\"squeeze PMID … for leads\"* for the discovery ledger. See [`SKILLS.md`](../../../SKILLS.md).",
        "",
        "**A low rank here is a queue position, never a verdict.** Nothing in this table authorizes",
        "not reading something: the ranking exists to order the work, and an unread record stays",
        "tracked until it is read. See [`gold_is_in_the_details.md`](../../../framework/master/gold_is_in_the_details.md).",
        "",
        "## Add a newer PubMed Clipboard snapshot",
        "",
        "Save the PubMed Clipboard email/export as plain text outside the repository, then run:",
        "",
        "```bash",
        "python3 framework/scripts/pubmed_clipboard_to_seed.py \\",
        "    --input /path/to/pubmed_clipboard.txt \\",
        "    --out disease-models/wwox/registries/corpus_seed_pubmed_YYYYMMDD.tsv",
        "python3 framework/scripts/batch_queue.py \\",
        "    --out disease-models/wwox/registries/batch_queue.md",
        "```",
        "",
        "The converter emits bibliographic fields only; mail headers and sender/recipient data",
        "are discarded. Keep the date in the filename. Repeated PMIDs across snapshots are",
        "counted once in the queue, with every seed filename retained as provenance.",
        "",
        "## Scope",
        "",
        "Bibliographic metadata only — identifiers, titles, years, open-access flags and processing",
        "state. No full texts are redistributed, and no individual-level information appears here.",
    ]
    return "\n".join(head) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--disease", default="wwox")
    parser.add_argument("--out", default="")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--check", default="")
    parser.add_argument(
        "--limit",
        type=int,
        default=0,
        help="maximum outstanding rows in Markdown; 0 (default) means the complete queue",
    )
    args = parser.parse_args()

    report = build(Path(args.root), args.disease)

    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
        return 0

    rendered = render(report, args.limit)

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
