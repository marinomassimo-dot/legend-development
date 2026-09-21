#!/usr/bin/env python3
"""Apply a narrow, pre-authorized edit to ONE record of an append-only JSONL ledger — or refuse.

🔴 WHY THIS EXISTS
------------------
On 2026-09-21 the publication gate blocked on the tail record of
`fulltext_read_receipts.jsonl`: a published study's parental attribution sat in the same JSONL
record as reference-genotype language, and the gate — which reads one record as one window and
has no allowlist by design — could not tell whose family was meant. The ledger is append-only
and hash-chained, so the text could not be superseded by appending: a `receipt_correction` is a
NEW line, and the old line is what the gate scans. The Operator authorized a scope-limited edit
to that one record, naming exactly what could change and what could not.

The edit was applied by hand under an ad-hoc assertion, and **the assertion caught the author's
own first attempt**, which named the wrong `evidence_basis` index and would have rewritten the
wrong sentence. Nothing was written. That is the whole argument for this tool: when an authorized
change is narrow, the narrowness should be EXECUTABLE, not a matter of care. Care is what was
already being exercised, and it had the index wrong.

🔴 WHAT THIS TOOL IS NOT
------------------------
It is **not** a waiver, an allowlist, or a way around a gate, and it grants no authority of its
own. It refuses unless the caller states, up front, the exact substitution and the exact field
that may absorb it; every other key of the record must survive byte-identical, INCLUDING the
identity and integrity fields (`study_id`, `source_fingerprint`, `source_locator`,
`evidence_depth`, `coverage`, `prior_receipt`, `ledger_prev_hash`). Authorisation remains a
human act recorded outside this file; this tool only makes an authorized scope enforceable.

It edits ONE record and, by default, only the LAST one — because rewriting a tail line leaves
every other line's `ledger_prev_hash` untouched, while rewriting an interior line invalidates
the chain from there on. `--allow-interior` exists so the refusal is explicit rather than
implied, and it still refuses to write: it reports what would break.

Disease-agnostic and ledger-agnostic: any JSONL whose records are objects.

Run:
  scoped_record_edit.py --file <path> --id-key event_id --id <ID> \\
      --field <dotted.path> --old <text> --new <text> [--apply]

Without `--apply` it is a dry run that prints the diff and the scope proof, and writes nothing.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


class Refusal(Exception):
    """A scope violation. Nothing has been written when this is raised."""


def _walk(value: Any, dotted: str) -> tuple[Any, Any, Any]:
    """Return (container, key, current) for a dotted path, where a list index is an integer."""
    container: Any = None
    key: Any = None
    current = value
    for part in dotted.split("."):
        if isinstance(current, list):
            try:
                idx = int(part)
            except ValueError as exc:
                raise Refusal(f"{dotted!r}: {part!r} is not a list index") from exc
            if not 0 <= idx < len(current):
                raise Refusal(f"{dotted!r}: index {idx} out of range ({len(current)} items)")
            container, key, current = current, idx, current[idx]
        elif isinstance(current, dict):
            if part not in current:
                raise Refusal(f"{dotted!r}: no key {part!r}")
            container, key, current = current, part, current[part]
        else:
            raise Refusal(f"{dotted!r}: {part!r} cannot be resolved on a {type(current).__name__}")
    return container, key, current


def _diff_keys(before: dict, after: dict) -> list[str]:
    return sorted(k for k in set(before) | set(after) if before.get(k) != after.get(k))


def scoped_edit(lines: list[str], *, id_key: str, record_id: str, field: str,
                old: str, new: str, allow_interior: bool) -> tuple[list[str], dict]:
    """Return (new_lines, proof). Raises Refusal and writes nothing on any scope violation."""
    if old == new:
        raise Refusal("--old and --new are identical; there is nothing to authorize")

    indexes = [i for i, line in enumerate(lines) if line.strip()]
    if not indexes:
        raise Refusal("the ledger has no records")

    hits = []
    for i in indexes:
        try:
            record = json.loads(lines[i])
        except json.JSONDecodeError as exc:
            raise Refusal(f"line {i + 1} is not valid JSON: {exc}") from exc
        if not isinstance(record, dict):
            raise Refusal(f"line {i + 1} is not a JSON object")
        if str(record.get(id_key)) == record_id:
            hits.append((i, record))
    if not hits:
        raise Refusal(f"no record has {id_key} == {record_id!r}")
    if len(hits) > 1:
        raise Refusal(f"{len(hits)} records share {id_key} == {record_id!r}; refusing to guess")

    index, before = hits[0]
    is_tail = index == indexes[-1]
    if not is_tail and not allow_interior:
        raise Refusal(
            f"record {record_id!r} is line {index + 1} of {indexes[-1] + 1}, not the tail. "
            "Rewriting an interior record invalidates every following ledger_prev_hash. "
            "Re-run with --allow-interior to see what would break; it still will not write.")

    container, key, current = _walk(before, field)
    if not isinstance(current, str):
        raise Refusal(f"{field!r} holds a {type(current).__name__}, not a string")
    occurrences = current.count(old)
    if occurrences == 0:
        raise Refusal(f"{field!r} does not contain the authorized --old text")
    if occurrences > 1:
        raise Refusal(
            f"{field!r} contains the --old text {occurrences} times; an authorization that "
            "cannot say which occurrence is not a scope")

    after = json.loads(json.dumps(before))
    a_container, a_key, _ = _walk(after, field)
    a_container[a_key] = current.replace(old, new)

    changed = _diff_keys(before, after)
    top = field.split(".")[0]
    if changed != [top]:
        raise Refusal(
            "the substitution would change more than the authorized field: "
            + ", ".join(changed or ["nothing"]))

    # The identity and integrity fields are named explicitly, so a future edit to _diff_keys
    # cannot quietly stop protecting them.
    for guarded in ("study_id", "source_fingerprint", "source_locator", "evidence_depth",
                    "coverage", "prior_receipt", "ledger_prev_hash", "event_id", "record_kind"):
        if guarded == top:
            raise Refusal(f"{guarded!r} is an identity or integrity field and is never editable here")
        if guarded in before and before[guarded] != after.get(guarded):
            raise Refusal(f"{guarded!r} would change; refusing")

    out = list(lines)
    out[index] = json.dumps(after, ensure_ascii=False, sort_keys=True)
    proof = {
        "record": record_id,
        "line": index + 1,
        "of": indexes[-1] + 1,
        "is_tail": is_tail,
        "field": field,
        "changed_top_level_keys": changed,
        "chars_removed": len(current) - len(after and a_container[a_key]),
    }
    return out, proof


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--file", required=True)
    ap.add_argument("--id-key", default="event_id")
    ap.add_argument("--id", required=True)
    ap.add_argument("--field", required=True,
                    help="dotted path within the record, e.g. evidence_basis.3")
    ap.add_argument("--old", required=True)
    ap.add_argument("--new", required=True)
    ap.add_argument("--allow-interior", action="store_true")
    ap.add_argument("--apply", action="store_true",
                    help="without this the run is a dry run and writes nothing")
    args = ap.parse_args(argv[1:])

    path = Path(args.file)
    try:
        raw = path.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"REFUSED: cannot read {args.file}: {exc}", file=sys.stderr)
        return 1
    trailing_newline = raw.endswith("\n")
    lines = raw.split("\n")

    try:
        out, proof = scoped_edit(
            lines, id_key=args.id_key, record_id=args.id, field=args.field,
            old=args.old, new=args.new, allow_interior=args.allow_interior)
    except Refusal as refusal:
        print(f"REFUSED: {refusal}", file=sys.stderr)
        return 1

    print(json.dumps(proof, indent=2, sort_keys=True))
    if not args.apply:
        print("DRY RUN — nothing written. Re-run with --apply once the scope above is the "
              "authorized one.")
        return 0
    if not proof["is_tail"]:
        print("REFUSED: --allow-interior reports, it does not write.", file=sys.stderr)
        return 1
    text = "\n".join(out)
    if trailing_newline and not text.endswith("\n"):
        text += "\n"
    path.write_text(text, encoding="utf-8")
    print(f"APPLIED to {args.file}. Re-anchor and re-validate the ledger before publishing.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
