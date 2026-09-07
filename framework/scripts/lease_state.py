#!/usr/bin/env python3
"""Derive ORCHESTRATOR_LEASE state. Never trust the stored STATUS field.

Why this exists: on 2026-08-18 a lease record read `STATUS: ACTIVE` twenty-nine seconds after
its own EXPIRES_AT, and nothing moved it, because nothing owned the transition. STATUS is a
DERIVED value stored without its recipe. This tool is the recipe.

The derivation uses three inputs and never the stored field:

    RELEASED_AT present   -> RELEASED   (terminal; wins over the clock)
    now >= EXPIRES_AT     -> STALE      (terminal by expiry)
    otherwise             -> ACTIVE

THE SINGLETON IS AN INVARIANT, NOT A FINDING. Annex I.3 exists to guarantee one ACTIVE lease.
Two ACTIVE leases means two writers over one shared resource, so it is checked in EVERY mode
and always exits non-zero. It must not be possible to invoke this tool in a way that reports
two live leases and calls the result clean. (Mirror, REV-SUNSET-DEC3-MIRROR-001, blocking.)

`--check` additionally reports conditions that a readable record does NOT by itself prevent,
which is the whole point of VISIBILITY != LIFECYCLE ENFORCEMENT:

  * DISAGREEMENT              the stored STATUS differs from the derived state. Visibility
                              gives you the raw material for the comparison; only running it
                              performs the comparison.
  * EXPIRED_WITHOUT_RENEWAL   a lease that reached EXPIRES_AT with LAST_RENEWED absent or equal
                              to ACTIVATED_AT.

  NAMED FOR WHAT IT MEASURES. An earlier revision called this EXPIRED_UNUSED, which claimed
  more than the data supports: nothing in the record format records USE, so renewal is the only
  observable proxy, and it is a poor one. The record shipped with this tool contains three
  leases that were never renewed and were demonstrably used — each held a canonical batch. A
  lease that is used without being renewed is indistinguishable here from one that is never
  used at all, and the condition is named for the property it can actually test.

  The motivating failure (a lease acquired, never used, expired before GATE 0 was asserted)
  is DETECTED by this condition and is not IMPLIED by it. Nothing runs between turns, so the
  window itself stays unwatched; closing that needs the P7 event ledger, not this tool.

Exit codes:  0 clean · 1 finding (--check) · 2 could not read or parse · 3 invariant violated
"""

from __future__ import annotations

import argparse
import datetime as _dt
import hashlib
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from repo_root import RootError, control_plane  # noqa: E402

# 🔴 Relative on purpose — it is a name inside the repository, not a path from the
# working directory. It is joined to the DERIVED root, never to the cwd: resolving it
# against wherever the caller stood made this tool read a 5-record lease from the
# repository root and a 9-record one from the orchestrator worktree, both exit 0.
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
    if derived == "STALE":
        renewed = record.get("LAST_RENEWED", "").strip()
        activated = record.get("ACTIVATED_AT", "").strip()
        if not renewed or renewed == activated:
            out.append(
                f"lease #{index} EXPIRED_WITHOUT_RENEWAL: reached EXPIRES_AT with LAST_RENEWED "
                "absent or equal to ACTIVATED_AT. Renewal is a proxy for use and a poor one — "
                "an unrenewed lease may still have been used. Detected at consultation; "
                "nothing watched the window itself."
            )
    return out


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--home", default=None,
                        help=f"lease record (default: {DEFAULT_HOME} under the derived repository root)")
    parser.add_argument("--check", action="store_true",
                        help="report disagreements and expired-unused leases; exit 1 on any")
    parser.add_argument("--now", help="ISO-8601 instant to derive against; defaults to the clock")
    args = parser.parse_args(argv)

    try:
        now = _parse_ts(args.now) if args.now else _dt.datetime.now(_dt.timezone.utc)
        home = Path(args.home) if args.home else control_plane(DEFAULT_HOME)
        records = parse(home)
        derived = [derive(record, now) for record in records]
    except (RecordError, RootError) as exc:
        print(f"LEASE STATE UNDERIVABLE: {exc}", file=sys.stderr)
        return 2

    # 🔴 Say WHICH object was measured. The same command, run from two directories, read a
    # 5-record lease and a 9-record one and printed the same shape of answer both times; the
    # only way to tell them apart was to already know. A derived answer that does not name its
    # source cannot be reconciled with another derived answer, and reconciling them is the
    # whole of the control-plane problem. This is evidence, not policy: it asserts nothing
    # about which object SHOULD have been read.
    print(f"CONTROL_PLANE_SOURCE_PATH {home}")
    print(f"CONTROL_PLANE_SOURCE_SHA256 {hashlib.sha256(home.read_bytes()).hexdigest()}")
    print(f"CONTROL_PLANE_RECORD_COUNT {len(records)}")
    print(f"now (derivation instant)  {now.isoformat()}")
    for index, (record, state) in enumerate(zip(records, derived), start=1):
        stored = record.get("STATUS", "—").strip() or "—"
        print(f"  lease #{index}  derived={state:<9} stored={stored:<9} "
              f"expires={record.get('EXPIRES_AT', '—')} released={record.get('RELEASED_AT', '—')}")

    live = [index for index, state in enumerate(derived, start=1) if state == "ACTIVE"]
    print(f"ACTIVE by derivation: {len(live)}" + (f" — lease #{live[0]}" if len(live) == 1 else ""))

    # The singleton is an INVARIANT: checked in every mode, before --check is consulted, and
    # always fatal. A tool that can report two live leases and exit 0 is fail-open on exactly
    # the condition Annex I.3 exists to guarantee.
    if len(live) > 1:
        print(f"INVARIANT VIOLATED: {len(live)} leases derive ACTIVE — {live}. "
              "Two writers over one shared resource; Annex I.3 singleton broken.", file=sys.stderr)
        return 3

    if not args.check:
        return 0

    problems: list[str] = []
    for index, (record, state) in enumerate(zip(records, derived), start=1):
        problems.extend(findings(record, state, index))
    for problem in problems:
        print(f"FINDING: {problem}")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
