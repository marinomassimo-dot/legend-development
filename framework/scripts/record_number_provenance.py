#!/usr/bin/env python3
"""Every number in an orchestration record must sit beside what produced it.

WHY THIS EXISTS
---------------
Twice in one session an operator-facing number was quoted into a record instead of derived,
and both were caught by someone else: a false-positive baseline attributed to the wrong paper
was copied from the retrospective into a dispatch (two streams measured it), and a self-test
baseline of "26/46" was copied from a closing report into the orchestration record (Mirror
found it derivable from no run and it was struck). SPECIFICATION_NUMBER_PROVENANCE_GATE had
landed that afternoon; it had no instrument. This is the instrument, proportional to the
defect: a review queue, never a block.

WHAT IT CHECKS
--------------
Over `disease-models/*/analysis/orchestration_reviews/*.md`, every Markdown table row that
carries a ratio (`17/1458`, `26 of 46`) or a before/after arrow (`13 → 10`) must also carry,
in the same row, at least one of: a backticked command or tool name (`something.py`, a
`--flag`), a 7+ hex commit hash, or a struck-through value (a corrected number is anchored
by its correction). Rows with none are `UNANCHORED_NUMBER`. Prose outside tables is not
screened: the tables are where a reader takes a number as settled.

    python3 framework/scripts/record_number_provenance.py [--queue] [--json]
    python3 framework/scripts/record_number_provenance.py --self-test

Exit codes: 0 screened (findings do not change it) · 2 invalid invocation · 3 nothing screened.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RECORD_GLOB = "disease-models/*/analysis/orchestration_reviews/*.md"

RATIO = re.compile(r"\b\d+\s*(?:/|of)\s*\d+\b")
ARROW = re.compile(r"\b\d+\s*(?:→|->)\s*\*{0,2}\d+")
ANCHOR = re.compile(
    r"`[^`]*(?:\.py|\.sh|--[a-z]|[a-z_]+\.py)[^`]*`"   # a command or tool in backticks
    r"|\b[0-9a-f]{7,40}\b"                              # a commit hash
    r"|~~[^~]+~~"                                       # a struck value, anchored by its correction
    r"|`[A-Z_]{4,}`"                                    # a named check or verdict token
)


@dataclass
class Row:
    source: str
    line: int
    text: str


@dataclass
class Result:
    verdict: str
    screened_files: int = 0
    screened_rows: int = 0
    digest: str = ""
    missing: str = ""
    numbered: int = 0
    unanchored: list[Row] = field(default_factory=list)


def screen(root: Path = ROOT) -> Result:
    paths = sorted(root.glob(RECORD_GLOB))
    if not paths:
        return Result(verdict="INSUFFICIENT_DATA", missing=f"no records match {RECORD_GLOB}")
    digest = hashlib.sha256()
    result = Result(verdict="SCREENED")
    for path in paths:
        raw = path.read_bytes()
        digest.update(raw)
        result.screened_files += 1
        for number, line in enumerate(raw.decode("utf-8", errors="replace").splitlines(), 1):
            if not line.lstrip().startswith("|") or set(line.strip()) <= set("|-: "):
                continue
            result.screened_rows += 1
            if not (RATIO.search(line) or ARROW.search(line)):
                continue
            result.numbered += 1
            if not ANCHOR.search(line):
                result.unanchored.append(Row(str(path.relative_to(root)), number, line.strip()[:160]))
    result.digest = digest.hexdigest()
    return result


def render(result: Result, queue: bool) -> str:
    if result.verdict == "INSUFFICIENT_DATA":
        return f"INSUFFICIENT_DATA: {result.missing}"
    lines = [f"screened: records={result.screened_files} table_rows={result.screened_rows} "
             f"digest={result.digest[:16]}",
             f"rows carrying a number: {result.numbered}; unanchored: {len(result.unanchored)}"]
    if queue:
        for row in result.unanchored:
            lines.append(f"  [UNANCHORED_NUMBER] {row.source}:{row.line}  {row.text}")
    return "\n".join(lines)


def self_test() -> int:
    import tempfile
    passed = failed = 0

    def check(name, cond):
        nonlocal passed, failed
        passed += cond; failed += (not cond)
        print(("  ok   " if cond else "  FAIL ") + name)

    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        check("empty tree is INSUFFICIENT_DATA", screen(root).verdict == "INSUFFICIENT_DATA")
        d = root / "disease-models" / "x" / "analysis" / "orchestration_reviews"
        d.mkdir(parents=True)
        (d / "r.md").write_text(
            "| a | b |\n|---|---|\n"
            "| anchored | 17/1458 by `tool.py` |\n"
            "| hashed | 13 → 10 at `abc1234` |\n"
            "| struck | ~~26/46~~ quoted from a report |\n"
            "| bare | 26/46 called; 13 → 10 |\n"
            "prose 3/4 outside a table\n", encoding="utf-8")
        r = screen(root)
        check("four numbered rows, one unanchored", r.numbered == 4 and len(r.unanchored) == 1)
        check("the bare row is the one named", r.unanchored[0].line == 6)
        check("the digest names what was screened", len(r.digest) == 64)
    live = screen()
    check("runs over the real records", live.verdict == "SCREENED" and live.screened_files > 0)
    print(f"\nself-test: {passed} passed, {failed} failed")
    return 0 if failed == 0 else 1


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--queue", action="store_true")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args(argv)
    if args.self_test:
        return self_test()
    result = screen(args.root)
    if args.json:
        print(json.dumps({"verdict": result.verdict, "records": result.screened_files,
                          "table_rows": result.screened_rows, "numbered": result.numbered,
                          "unanchored": [vars(r) for r in result.unanchored],
                          "digest": result.digest, "missing": result.missing}, indent=1))
    else:
        print(render(result, args.queue))
    return 3 if result.verdict == "INSUFFICIENT_DATA" else 0


if __name__ == "__main__":
    sys.exit(main())
