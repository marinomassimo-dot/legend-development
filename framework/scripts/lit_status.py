#!/usr/bin/env python3
"""LIT `Status` — validator and migration for `literature_tracking_log_current.md`.

## Where the vocabulary lives, and why this file keeps no copy of it

The log declares its own `## Status vocabulary` table. That table is the canonical home: a
scientific current file, changed only through BATCH_COMMIT. This module PARSES it on every run
and restates none of its values — `legend_lint.VALID_PAPER_STATES` already restates the same ten
words for the paper registry, which is the shape a drift starts from. A change to the vocabulary
is therefore a change to the table, made by the Orchestrator in a batch; nothing here moves.

## The defect (HARNESS-P-20260914 P9a, measured 2026-09-14)

Nothing checked a LIT record against the table. 397 records: 386 carry `**Status:**` with 28
distinct raw values, 11 older ones carry their state under `**Current status:**`. Outside the
table: 17 `processed — complete_fulltext_read`, 1 `processed — partial_fulltext_read`, 17
`completed — [[paper_registry_current#PAPER n]] (…)`, 1 `archived`, 2 `filtered_in — …`.

## Record classes

- `VALID` — `**Status:**` carries a table value.
- `LEGACY_FORM` — `**Status:**` carries `<table value> — <qualifier>` or
  `completed — [[paper_registry_current#PAPER n]] …`.
- `LEGACY_FIELD` — the state is under `**Current status:**`.
- `NOT_IN_VOCABULARY` — any other value.
- `MISSING_STATUS` — neither field.

## The migration — conservative, lossless, and NOT run by the harness

`migrate` rewrites only state lines and inserts `**Status note:**` lines; every other line is
byte-identical, and it is idempotent.
- `<value> — <qualifier>` → `**Status:** <value>` + `**Status note:** <qualifier>`.
- `**Current status:**` → `**Status:**`, with the same rule for a qualifier.
- `completed — [[…#PAPER n]] …` → the promoted PAPER record's own `Status` when that is a table
  value, with the whole original kept as the note (link included). Otherwise left and reported.
- Anything else is LEFT and reported as `unmapped`. `archived` on `LIT-0401` (a retracted
  primary, "never use as evidence") is the live case: no table value is true of it, so it remains
  unmapped. Lifecycle Status and publication integrity are different dimensions; the
  existing seed publication-integrity flags and batch_queue eligibility carry the latter.
  No lifecycle spelling, including archived, cancels an integrity hold.

🔴 Running `migrate --write` against the canonical log is a BATCH_COMMIT act under LEGEND_CORE section 21e. Without `--write` it prints a unified diff and writes nothing.

## Grandfathering in LINT

`lit_status_legacy.json` records every non-VALID record by identity AND exact value at the time
the validator was introduced. LINT warns on those and BLOCKS on anything else outside the
table — a new record, or a grandfathered one that drifted to a different bad value. The snapshot
can only shrink: regenerate it (`snapshot --write-json`) after the migration lands.
"""

from __future__ import annotations

import argparse
import difflib
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import coverage_report  # noqa: E402
import growth_anchors  # noqa: E402

REPO = HERE.parents[1]
DEFAULT_LOG = REPO / growth_anchors.REGISTRIES["literature"].format(disease="wwox")
DEFAULT_PAPERS = REPO / growth_anchors.REGISTRIES["papers"].format(disease="wwox")
SNAPSHOT = HERE / "lit_status_legacy.json"

VALID = "VALID"
LEGACY_FORM = "LEGACY_FORM"
LEGACY_FIELD = "LEGACY_FIELD"
NOT_IN_VOCABULARY = "NOT_IN_VOCABULARY"
MISSING_STATUS = "MISSING_STATUS"

LIT_HEADING = growth_anchors.HEADINGS["literature"]
VOCAB_SECTION = re.compile(r"(?ms)^##\s+Status vocabulary\s*$(?P<body>.*?)(?=^##\s|^---\s*$|\Z)")
VOCAB_ROW = re.compile(r"(?m)^\|\s*`(?P<value>[^`]+)`\s*\|")
STATE_LINE = re.compile(r"(?m)^\*\*(?P<field>Status|Current status):\*\*[ \t]*(?P<value>.*)$")
QUALIFIED = re.compile(r"^(?P<base>[a-z_]+)\s+—\s+(?P<qualifier>.+)$")
COMPLETED = re.compile(r"^completed\s+—\s+(?P<link>\[\[paper_registry_current#(?P<paper>PAPER \d+)\]\].*)$")


@dataclass(frozen=True)
class Record:
    record: str
    kind: str
    field: str   # "Status" | "Current status" | ""
    value: str

    @property
    def fingerprint(self) -> str:
        return f"{self.field or '<none>'}: {self.value}"


def vocabulary(text: str) -> set[str] | None:
    section = VOCAB_SECTION.search(text)
    if section is None:
        return None
    values = {m.group("value").strip() for m in VOCAB_ROW.finditer(section.group("body"))}
    return values or None


def _spans(text: str):
    marks = list(LIT_HEADING.finditer(text))
    for index, mark in enumerate(marks):
        end = marks[index + 1].start() if index + 1 < len(marks) else len(text)
        yield mark.group(1), mark.end(), end


def classify(field: str, value: str, vocab: set[str]) -> str:
    if not field:
        return MISSING_STATUS
    qualified = QUALIFIED.match(value)
    known = (value in vocab or (qualified and qualified.group("base") in vocab)
             or COMPLETED.match(value))
    if field == "Current status":
        return LEGACY_FIELD if known else NOT_IN_VOCABULARY
    if value in vocab:
        return VALID
    return LEGACY_FORM if known else NOT_IN_VOCABULARY


def validate(text: str) -> list[Record]:
    vocab = vocabulary(text)
    if vocab is None:
        return []
    out = []
    for rid, start, end in _spans(text):
        lines = {m.group("field"): m.group("value").strip() for m in STATE_LINE.finditer(text, start, end)}
        field = "Status" if "Status" in lines else ("Current status" if "Current status" in lines else "")
        value = lines.get(field, "")
        out.append(Record(rid, classify(field, value, vocab), field, value))
    return out


def legacy_snapshot(text: str) -> dict[str, str]:
    return {r.record: r.fingerprint for r in validate(text) if r.kind != VALID}


def load_snapshot(path: Path = SNAPSHOT) -> dict[str, str]:
    return json.loads(path.read_text(encoding="utf-8"))["records"]


def paper_statuses(papers_text: str) -> dict[str, str]:
    return {e["_id"]: e.get("status", "").strip() for e in coverage_report.parse_entries(papers_text)}


def migrate(text: str, papers_text: str) -> tuple[str, dict]:
    vocab = vocabulary(text)
    report: dict = {"changed": [], "unmapped": []}
    if vocab is None:
        report["unmapped"].append({"record": "*", "value": "", "reason": "no Status vocabulary table"})
        return text, report
    papers = paper_statuses(papers_text)
    pieces: list[str] = []
    cursor = 0
    for rid, start, end in _spans(text):
        match = STATE_LINE.search(text, start, end)
        if match is None:
            report["unmapped"].append({"record": rid, "value": "", "reason": "no Status field"})
            continue
        field, value = match.group("field"), match.group("value").strip()
        status, note, reason = None, None, ""
        qualified, completed = QUALIFIED.match(value), COMPLETED.match(value)
        if value in vocab:
            status = value
        elif qualified and qualified.group("base") in vocab:
            status, note = qualified.group("base"), qualified.group("qualifier")
        elif completed:
            target = papers.get(completed.group("paper"))
            if target in vocab:
                status, note = target, value
            else:
                reason = (f"{completed.group('paper')} has Status {target!r}, not a table value"
                          if target is not None else f"{completed.group('paper')} not in the paper registry")
        else:
            reason = "no table value is true of it; the vocabulary is a BATCH_COMMIT decision"
        if status is None:
            report["unmapped"].append({"record": rid, "value": value, "reason": reason})
            continue
        replacement = f"**Status:** {status}" + (f"\n**Status note:** {note}" if note else "")
        if field == "Status" and note is None:
            continue
        pieces.append(text[cursor:match.start()])
        pieces.append(replacement)
        cursor = match.end()
        report["changed"].append({"record": rid, "before": f"**{field}:** {value}",
                                  "after": replacement})
    pieces.append(text[cursor:])
    return "".join(pieces), report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    sub = parser.add_subparsers(dest="command", required=True)
    check = sub.add_parser("validate")
    check.add_argument("--log", default=str(DEFAULT_LOG))
    move = sub.add_parser("migrate")
    move.add_argument("--log", required=True)
    move.add_argument("--papers", default=str(DEFAULT_PAPERS))
    move.add_argument("--write", action="store_true",
                      help="rewrite --log in place. Against the canonical log this is a BATCH_COMMIT act.")
    snap = sub.add_parser("snapshot")
    snap.add_argument("--log", default=str(DEFAULT_LOG))
    snap.add_argument("--write-json")
    args = parser.parse_args(argv)

    text = Path(args.log).read_text(encoding="utf-8")
    if args.command == "validate":
        records = validate(text)
        if not records and vocabulary(text) is None:
            print("UNCHECKED: no `## Status vocabulary` table in the log")
            return 0
        counts: dict[str, int] = {}
        for record in records:
            counts[record.kind] = counts.get(record.kind, 0) + 1
            if record.kind != VALID:
                print(f"{record.kind} {record.record} {record.fingerprint}")
        print(" | ".join(f"{k.lower()}: {v}" for k, v in sorted(counts.items())))
        return 0
    if args.command == "snapshot":
        payload = {"_note": "Non-VALID LIT records at the time of writing, by identity and exact value. "
                            "LINT warns on these and blocks on anything else outside the log's Status "
                            "vocabulary table. It may only shrink; regenerate after a migration lands.",
                   "source": growth_anchors.REGISTRIES["literature"].format(disease="wwox"),
                   "records": legacy_snapshot(text)}
        rendered = json.dumps(payload, ensure_ascii=False, indent=1, sort_keys=True) + "\n"
        if args.write_json:
            Path(args.write_json).write_text(rendered, encoding="utf-8")
        print(f"records: {len(payload['records'])}")
        return 0
    new_text, report = migrate(text, Path(args.papers).read_text(encoding="utf-8"))
    sys.stdout.writelines(difflib.unified_diff(
        text.splitlines(keepends=True), new_text.splitlines(keepends=True),
        fromfile=args.log, tofile=f"{args.log} (migrated)", n=1))
    for row in report["unmapped"]:
        print(f"UNMAPPED {row['record']} {row['value']!r}: {row['reason']}")
    print(f"changed: {len(report['changed'])} | unmapped: {len(report['unmapped'])}"
          + (" | WRITTEN" if args.write and new_text != text else " | dry run, nothing written"))
    if args.write and new_text != text:
        Path(args.log).write_text(new_text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
