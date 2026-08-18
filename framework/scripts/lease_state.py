#!/usr/bin/env python3
"""Derive ORCHESTRATOR_LEASE state. Never trust the stored STATUS field.

Why this exists: on 2026-08-18 a lease record read `STATUS: ACTIVE` twenty-nine seconds after
its own EXPIRES_AT, and nothing moved it, because nothing owned the transition. STATUS is a
DERIVED value stored without its recipe. This tool is the recipe.

The derivation uses three inputs and never the stored field:

    RELEASED_AT present   -> RELEASED   (terminal; wins over the clock)
    now >= EXPIRES_AT     -> STALE      (terminal by expiry)
    otherwise             -> ACTIVE

`--check` additionally reports two conditions that a readable record does NOT by itself
prevent, which is the whole point of VISIBILITY != LIFECYCLE ENFORCEMENT:

  * DISAGREEMENT   the stored STATUS differs from the derived state. Visibility gives you the
                   raw material for this comparison; only running the comparison performs it.
  * EXPIRED_UNUSED a lease that reached EXPIRES_AT with no recorded use between ACTIVATED_AT
                   and expiry. Observed once (lease #3). This tool makes it DETECTABLE at the
                   next consultation. It does not make it IMPOSSIBLE: nothing runs between
                   turns, so the window itself is unwatched. That limit is stated here rather
                   than papered over.

Exit codes:  0 clean · 1 finding · 2 could not read or parse the record
"""

from __future__ import annotations

import argparse
import datetime as _dt
import re
import sys
from pathlib import Path

DEFAULT_HOME = "runtime/orchestrator_lease.md"

FIELD = re.compile(r"^\s{2,}([A-Z_]+):\s*([^#\n]*?)\s*(?:#.*)?$")
BLOCK_START = re.compile(r"^LEASE:\s*$")
TERMINAL = {"RELEASED", "STALE"}


class RecordError(RuntimeError):
    """The record could not be read or parsed. Never guess a lease state."""


def _parse_ts(raw: str) -> _dt.datetime:
    text = raw.strip().replace("Z", "+00:00")
    try:
        stamp = _dt.datetime.fromisoformat(text)
    except ValueError as exc:
        raise RecordError(f"unparseable timestamp {raw!r}") from exc
    if stamp.tzinfo is None:
        raise RecordError(f"timestamp {raw!r} carries no timezone; refusing to assume UTC")
    return stamp


def parse(path: Path) -> list[dict[str, str]]:
    """Return every LEASE block in the record, in file order."""
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        raise RecordError(f"cannot read {path}: {exc}") from exc

    records: list[dict[str, str]] = []
    current: dict[str, str] | None = None
    for line in lines:
        if BLOCK_START.match(line):
            current = {}
            records.append(current)
            continue
        if current is None:
            continue
        match = FIELD.match(line)
        if match:
            current[match.group(1)] = match.group(2)
        elif line.strip() and not line.startswith(" "):
            current = None  # block ended at the first unindented non-empty line
    if not records:
        raise RecordError(f"no LEASE block found in {path}")
    return records


def derive(record: dict[str, str], now: _dt.datetime) -> str:
    """Derive the state from RELEASED_AT, EXPIRES_AT and the clock. Never from STATUS."""
    if record.get("RELEASED_AT"):
        return "RELEASED"
    expires_raw = record.get("EXPIRES_AT")
    if not expires_raw:
        raise RecordError("record has neither RELEASED_AT nor EXPIRES_AT; state is underivable")
    return "STALE" if now >= _parse_ts(expires_raw) else "ACTIVE"


def findings(record: dict[str, str], derived: str, index: int) -> list[str]:
    out: list[str] = []
    stored = record.get("STATUS", "").strip()
    if stored and stored != derived:
        out.append(
            f"lease #{index} DISAGREEMENT: stored STATUS={stored!r}, derived={derived!r}. "
            "The stored field is not authoritative."
        )
    if derived == "STALE" and not record.get("LAST_USED"):
        renewed = record.get("LAST_RENEWED", "").strip()
        activated = record.get("ACTIVATED_AT", "").strip()
        if not renewed or renewed == activated:
            out.append(
                f"lease #{index} EXPIRED_UNUSED: reached EXPIRES_AT with no use recorded after "
                "ACTIVATED_AT. Detected at consultation; nothing watched the window itself."
            )
    return out


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--home", default=DEFAULT_HOME, help=f"lease record (default {DEFAULT_HOME})")
    parser.add_argument("--check", action="store_true",
                        help="report disagreements and expired-unused leases; exit 1 on any")
    parser.add_argument("--now", help="ISO-8601 instant to derive against; defaults to the clock")
    args = parser.parse_args(argv)

    try:
        now = _parse_ts(args.now) if args.now else _dt.datetime.now(_dt.timezone.utc)
        records = parse(Path(args.home))
        derived = [derive(record, now) for record in records]
    except RecordError as exc:
        print(f"LEASE STATE UNDERIVABLE: {exc}", file=sys.stderr)
        return 2

    print(f"now (derivation instant)  {now.isoformat()}")
    for index, (record, state) in enumerate(zip(records, derived), start=1):
        stored = record.get("STATUS", "—").strip() or "—"
        print(f"  lease #{index}  derived={state:<9} stored={stored:<9} "
              f"expires={record.get('EXPIRES_AT', '—')} released={record.get('RELEASED_AT', '—')}")

    live = [index for index, state in enumerate(derived, start=1) if state == "ACTIVE"]
    print(f"ACTIVE by derivation: {len(live)}" + (f" — lease #{live[0]}" if len(live) == 1 else ""))

    if not args.check:
        return 0

    problems: list[str] = []
    for index, (record, state) in enumerate(zip(records, derived), start=1):
        problems.extend(findings(record, state, index))
    if len(live) > 1:
        problems.append(f"SINGLETON VIOLATED: {len(live)} leases derive ACTIVE — {live}")

    for problem in problems:
        print(f"FINDING: {problem}")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
