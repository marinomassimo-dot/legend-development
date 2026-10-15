#!/usr/bin/env python3
"""Reconcile the ops an integrator extracted from a commit candidate against the count the
candidate itself declares — before anything is propagated.

🔴 WHY THIS EXISTS. BATCH_20261004_007 (2026-10-04) received nineteen candidates in three
authoring formats, and nothing in the repository parsed all three. The integrator's first two
parser iterations silently produced ZERO ops for two candidates that declared several, and one
op with no record id for a third. A silent zero is the dangerous failure: a batch that reads
`0 ops` for a candidate propagates nothing and can still report the candidate as processed. The
byte-level editor (`record_scoped_edit.py`) cannot catch it, because an op that was never built is
not an op that was refused. The batch report asked for exactly one thing — *print `ops_parsed`
beside the number the candidate's own text declares, and refuse on a mismatch* — the same shape
as `growth_anchors.py`'s cardinality check, applied to the extraction step.

The three formats, as observed in that batch:

  A  a fenced ```json array of op objects ({"op": "replace-within", "id": ..., "old": ..., "new": ...})
  B  `### Op N - `RECORD`, `replace-within` (...)` headings, each with `- `old` ...: `...`` and
     `- `new`: `...`` bullets
  C  `### N.M `<file>` — record `RECORD`` headings, each over a Markdown table
     `| # | op | old | new |` with one op per row (a paired-fence variant — an unlabelled ``` old
     fence followed by an unlabelled ``` new fence under the same heading — is parsed too)

The declared count is read from the candidate's prose: *«two `replace-within` ops»*, *«6
record-scoped ops»*, *«1 op»*. Every such phrase is collected, and the parsed count is accepted
when it equals one of the declared numbers or the sum of the distinct per-target declarations
(a candidate that says *«one op on CLAIM 032»* and *«one op on DIS-026»* declares two).

Verdicts (exit code):
  MATCH        0   ops_parsed agrees with the declaration
  UNDECLARED   0   ops were parsed and the prose declares no count — reported, not refused;
                   --strict turns it into a refusal
  NO_OPS       0   nothing parsed and nothing in the text looks like an op: a genuinely
                   op-less candidate (a proposal, a report)
  SILENT_ZERO  3   nothing parsed, but the text carries op structure (an `Op N` heading, a
                   `replace-within` token, a fenced json op array) — the extraction failed
  MISMATCH     3   ops_parsed disagrees with every declared count

    python3 framework/scripts/candidate_ops_reconcile.py <candidate.md> [...]
    python3 framework/scripts/candidate_ops_reconcile.py --json --strict <candidate.md>
    python3 framework/scripts/candidate_ops_reconcile.py --ops-out ops.json <candidate.md>   # the parsed ops, for record_scoped_edit.py apply

Read-only toward every file it is given; `--ops-out` writes only the path named.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

OP_NAMES = ("replace", "replace-within", "insert-before", "insert-after", "append", "delete")

NUMBER_WORDS = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8,
    "nine": 9, "ten": 10, "eleven": 11, "twelve": 12, "a single": 1, "single": 1,
}

# «two `replace-within` ops», «6 record-scoped ops», «1 op», «a single op», «three ops»
DECLARED = re.compile(
    r"\b(?P<n>\d+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|a single|single)"
    r"(?:\s+(?:further|more|new|additional))?"
    r"(?:"
    r"(?:\s+(?:record-scoped|`?(?:replace-within|replace|insert-before|insert-after|append|delete)`?))*\s+ops?\b"
    r"|\s+`(?:replace-within|replace|insert-before|insert-after|append|delete)`(?=\s*[),.;])"
    r")"
    r"(?!\(s\))(?!\s+per\b)",
    re.IGNORECASE,
)
TARGET_RECORDS = re.compile(r"^\*\*Target records?:\*\*(.*)$", re.MULTILINE)

FENCE_JSON = re.compile(r"^```json[^\n]*\n(.*?)^```[ \t]*$", re.MULTILINE | re.DOTALL)
HEADING_OP = re.compile(r"^#{2,5}\s+(?:\d+\s*[-·–—]\s*)?(?:Exact\s+)?Op(?:\s+\d+)?(?=\s*(?:[-·–—(:]|$))[^\n]*$",
                        re.MULTILINE | re.IGNORECASE)
NO_OPS_DECLARED = re.compile(r"\b(?:NO OPS|no ops owed|no ops are owed|outcome: NO OPS)\b")
HEADING_NM = re.compile(r"^#{2,5}\s+\d+\.\d+\b[^\n]*$", re.MULTILINE)
HEADING_ANY = re.compile(r"^#{1,5}\s", re.MULTILINE)
BULLET_OLD = re.compile(r"^-\s+`old`[^:\n]*:\s*(.*)$", re.MULTILINE)  # also matches a bare `old` paragraph below
BULLET_NEW = re.compile(r"^-\s+`new`[^:\n]*:\s*(.*)$", re.MULTILINE)
TABLE_ROW = re.compile(r"^\|\s*([A-Za-z]*\d+)\s*\|\s*(replace-within|replace|insert-before|insert-after|append|delete)\s*\|(.*)\|\s*$",
                       re.MULTILINE)
RECORD_IN_HEADING = re.compile(r"`([A-Z][A-Z-]*\s?[A-Z0-9][A-Z0-9-]*)`")
UNLABELLED_FENCE = re.compile(r"^```[ \t]*\n(.*?)^```[ \t]*$", re.MULTILINE | re.DOTALL)


def _strip_ticks(s: str) -> str:
    s = s.strip()
    if len(s) >= 2 and s[0] == "`" and s[-1] == "`":
        return s[1:-1]
    return s


def _sections(text: str, heading_re: re.Pattern[str]) -> list[tuple[str, str]]:
    """(heading line, body up to the next heading of any level) for every heading_re match."""
    out: list[tuple[str, str]] = []
    matches = list(heading_re.finditer(text))
    for m in matches:
        start = m.end()
        nxt = HEADING_ANY.search(text, start)
        body = text[start: nxt.start() if nxt else len(text)]
        out.append((m.group(0), body))
    return out


def parse_format_a(text: str) -> list[dict[str, Any]]:
    ops: list[dict[str, Any]] = []
    for m in FENCE_JSON.finditer(text):
        try:
            data = json.loads(m.group(1))
        except json.JSONDecodeError:
            continue
        items = data if isinstance(data, list) else [data]
        for item in items:
            if isinstance(item, dict) and item.get("op") in OP_NAMES:
                ops.append({**item, "_format": "A"})
    return ops


def _default_record(text: str) -> str | None:
    """The one record a `**Target records:**` line names, when it names exactly one."""
    m = TARGET_RECORDS.search(text)
    if not m:
        return None
    ids = {i for i in RECORD_IN_HEADING.findall(m.group(1)) if not i.endswith(".md")}
    return ids.pop() if len(ids) == 1 else None


VERTICAL_ROW = re.compile(r"^\|\s*(op|old|new|text)\s*\|\s*(.*?)\s*\|\s*$", re.MULTILINE | re.IGNORECASE)
RECORD_FIELD = re.compile(r"^\*\*Record:\*\*\s*`([^`]+)`", re.MULTILINE)
OP_FIELD = re.compile(r"^\*\*Op:\*\*\s*`([^`]+)`", re.MULTILINE)
ANY_OP_TOKEN = re.compile(r"`(replace-within|replace|insert-before|insert-after|append(?:_to_field)?|delete)`",
                          re.IGNORECASE)


def _record_ids(fragment: str) -> list[str]:
    """Backticked record tokens, minus op names (`APPEND`) and file names."""
    return [i for i in RECORD_IN_HEADING.findall(fragment)
            if not i.endswith(".md") and i.lower().replace("_to_field", "") not in OP_NAMES]


def _record_for(heading: str, body: str, text: str, default: str | None) -> str | None:
    ids = _record_ids(heading)
    if ids:
        return ids[-1]
    m = RECORD_FIELD.search(body)
    if m:
        return m.group(1)
    head = body.strip().split("\n", 1)[0]
    ids = _record_ids(head)
    if ids:
        return ids[0]
    # the enclosing `## N · Ops — ..., record `ID`` heading, if any, above this one
    pos = text.find(heading)
    level = len(heading) - len(heading.lstrip("#"))
    for parent in reversed(list(re.finditer(r"^#{1,5}\s[^\n]*$", text[:pos], re.MULTILINE))):
        plevel = len(parent.group(0)) - len(parent.group(0).lstrip("#"))
        if plevel >= level:
            continue
        pids = _record_ids(parent.group(0))
        if pids:
            return pids[-1]
        break
    return default


def _kind_for(heading: str, body: str) -> str:
    for src in (heading, OP_FIELD.search(body).group(1) if OP_FIELD.search(body) else "",
                body.strip().split("\n", 1)[0]):
        m = ANY_OP_TOKEN.search(src)
        if m:
            k = m.group(1).lower()
            return "append" if k == "append_to_field" else k
    return "replace-within"


def _ops_in_section(heading: str, body: str, text: str, default: str | None, fmt: str) -> list[dict[str, Any]]:
    rec = _record_for(heading, body, text, default)
    kind = _kind_for(heading, body)
    ops: list[dict[str, Any]] = []
    # 1. one op per horizontal table row: | # | op | old | new |
    for label, k, rest in TABLE_ROW.findall(body):
        cells = [c.strip() for c in rest.split("|")]
        if len(cells) >= 2:
            ops.append({"op": k, "id": rec, "old": _strip_ticks(cells[0]), "new": _strip_ticks(cells[1]),
                        "_label": label, "_format": fmt + "-table"})
    if ops:
        return ops
    # 2. vertical field tables: | op | … | / | old | … | / | new | … |, one op per `op` row
    cur: dict[str, Any] | None = None
    for key, val in VERTICAL_ROW.findall(body):
        key = key.lower()
        if key == "op":
            cur = {"op": _strip_ticks(val).lower(), "id": rec, "_format": fmt + "-vtable"}
            ops.append(cur)
        elif cur is not None:
            cur[key] = _strip_ticks(val)
    ops = [o for o in ops if o.get("op") in OP_NAMES and ("old" in o or "new" in o or "text" in o)]
    if ops:
        return ops
    # 3. `- `old` …: …` / `- `new`: …` bullets, paired in order
    olds, news = BULLET_OLD.findall(body), BULLET_NEW.findall(body)
    if olds and news:
        return [{"op": kind, "id": rec, "old": _strip_ticks(o), "new": _strip_ticks(n), "_format": fmt + "-bullets"}
                for o, n in zip(olds, news)]
    # 4. paired unlabelled fences (old then new)
    fences = UNLABELLED_FENCE.findall(body)
    if len(fences) >= 2:
        return [{"op": kind, "id": rec, "old": fences[i].rstrip("\n"), "new": fences[i + 1].rstrip("\n"),
                 "_format": fmt + "-fences"} for i in range(0, len(fences) - 1, 2)]
    # 5. an append / insert with only the text to add
    if kind in ("append", "insert-before", "insert-after") and (fences or body.strip()):
        return [{"op": kind, "id": rec, "text": (fences[0] if fences else body.strip()), "_format": fmt + "-append"}]
    return []


def parse_format_b(text: str) -> list[dict[str, Any]]:
    """`### Op N …` / `## Exact op` headings."""
    default = _default_record(text)
    ops: list[dict[str, Any]] = []
    for heading, body in _sections(text, HEADING_OP):
        ops.extend(_ops_in_section(heading, body, text, default, "B"))
    return ops


def parse_format_c(text: str) -> list[dict[str, Any]]:
    """`### N.M …` headings."""
    default = _default_record(text)
    ops: list[dict[str, Any]] = []
    for heading, body in _sections(text, HEADING_NM):
        ops.extend(_ops_in_section(heading, body, text, default, "C"))
    return ops


def parse_ops(text: str) -> list[dict[str, Any]]:
    return parse_format_a(text) + parse_format_b(text) + parse_format_c(text)


def declared_counts(text: str) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for m in DECLARED.finditer(text):
        raw = m.group("n").lower()
        n = int(raw) if raw.isdigit() else NUMBER_WORDS[raw]
        line_no = text.count("\n", 0, m.start()) + 1
        out.append({"n": n, "line": line_no, "phrase": m.group(0)})
    return out


def looks_like_it_has_ops(text: str) -> bool:
    return bool(HEADING_OP.search(text) or FENCE_JSON.search(text)
                or re.search(r"`replace-within`|\"op\":\s*\"", text) or TABLE_ROW.search(text))


def reconcile(path: Path, strict: bool = False) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    ops = parse_ops(text)
    decl = declared_counts(text)
    parsed = len(ops)
    numbers = sorted({d["n"] for d in decl})
    # per-target declarations summed: «one op on X ... one op on Y» = 2, on one line or across lines
    per_line: dict[int, list[int]] = {}
    for d in decl:
        per_line.setdefault(d["line"], []).append(d["n"])
    line_sums = {sum(v) for v in per_line.values() if len(v) > 1}
    first_per_line = sum(v[0] for v in per_line.values())
    total = first_per_line if len(per_line) > 1 else None
    acceptable = set(numbers) | line_sums | ({total} if total is not None else set())
    missing_id = [i for i, o in enumerate(ops, 1) if not o.get("id") and not o.get("heading")]
    if parsed == 0 and not decl and (NO_OPS_DECLARED.search(text) or not looks_like_it_has_ops(text)):
        verdict = "NO_OPS"
    elif parsed == 0:
        verdict = "SILENT_ZERO"
    elif not decl:
        verdict = "UNDECLARED"
    elif parsed in acceptable:
        verdict = "MATCH"
    else:
        verdict = "MISMATCH"
    refused = verdict in ("SILENT_ZERO", "MISMATCH") or (strict and verdict == "UNDECLARED") \
        or (strict and bool(missing_id))
    return {"candidate": str(path), "ops_parsed": parsed, "declared": decl, "declared_numbers": numbers,
            "declared_sum_of_distinct_lines": total, "declared_line_sums": sorted(line_sums),
            "formats": sorted({o["_format"] for o in ops}), "ops_without_record_id": missing_id,
            "verdict": verdict, "refused": refused, "ops": ops}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("candidates", nargs="+", type=Path)
    ap.add_argument("--json", action="store_true", help="one JSON object per candidate (ops included)")
    ap.add_argument("--strict", action="store_true",
                    help="also refuse UNDECLARED and any op with no record id")
    ap.add_argument("--ops-out", type=Path, help="write the parsed ops of a SINGLE candidate here, "
                    "in record_scoped_edit.py `apply --ops` shape (the _format/_label keys stripped)")
    args = ap.parse_args(argv)
    if args.ops_out and len(args.candidates) != 1:
        ap.error("--ops-out takes exactly one candidate")
    worst = 0
    for path in args.candidates:
        if not path.is_file():
            print(f"UNREADABLE: {path}", file=sys.stderr)
            worst = max(worst, 2)
            continue
        r = reconcile(path, strict=args.strict)
        if args.json:
            print(json.dumps(r, ensure_ascii=False))
        else:
            decl = ", ".join(f"{d['n']} (l.{d['line']})" for d in r["declared"]) or "none"
            print(f"{r['verdict']:<11} ops_parsed={r['ops_parsed']:<3} declared={decl:<28} "
                  f"formats={','.join(r['formats']) or '-'}  {path.name}")
            if r["ops_without_record_id"]:
                print(f"            ops with no record id: {r['ops_without_record_id']}")
        if r["refused"]:
            worst = max(worst, 3)
        if args.ops_out:
            clean = [{k: v for k, v in o.items() if not k.startswith("_")} for o in r["ops"]]
            args.ops_out.write_text(json.dumps(clean, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return worst


if __name__ == "__main__":
    sys.exit(main())
