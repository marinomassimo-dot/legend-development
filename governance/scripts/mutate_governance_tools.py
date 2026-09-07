#!/usr/bin/env python3
"""Mutation battery for `lease_state.py` and `governance_fingerprint.py`.

## Why a suite passing is not the same as a suite working

Both tools guard properties nothing else in the repository re-derives: whether a lease is ACTIVE,
and what an actor's `APPLICABLE_GOVERNANCE_FINGERPRINT` is. Their suites are green. Green says the
tools behave correctly on the inputs the tests supply; it does not say the tests would notice if
the tools stopped behaving correctly at all.

**Each arm below puts back a defect the tool exists to prevent and requires that tool's own suite
to go red.** An arm that leaves the suite green is a hole in the suite, reported as `SURVIVED`.

## Why a stale anchor is counted separately and never as a catch

If an arm's anchor text no longer occurs exactly once, the defect was never introduced — so the
suite was never asked anything, and recording that as a catch would inflate the battery's own
score with cases it did not run. It is reported as `STALE_ANCHOR` and makes the battery exit
non-zero, because a battery that quietly stops testing is worse than one that fails.

## It mutates a COPY

The subject directory is copied to a temporary tree and mutated there. Point it at a checkout,
never at a working tree you care about:

    mutate_governance_tools.py <path-to-a-checkout>
"""
from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

LEASE = "framework/scripts/lease_state.py"
LEASE_SUITE = "framework/scripts/test_lease_state.py"
FINGERPRINT = "governance/scripts/governance_fingerprint.py"
FINGERPRINT_SUITE = "governance/scripts/test_governance_fingerprint.py"

# (label, target, old span, replacement, suite that must go red)
ARMS: list[tuple[str, str, str, str, str]] = [
    ("lease: expiry stops being terminal — every unreleased lease derives ACTIVE",
     LEASE,
     'return "STALE" if now >= _parse_ts(expires_raw) else "ACTIVE"',
     'return "ACTIVE"',
     LEASE_SUITE),

    ("lease: RELEASED_AT stops winning over the clock",
     LEASE,
     'if record.get("RELEASED_AT"):\n        return "RELEASED"',
     'if False:\n        return "RELEASED"',
     LEASE_SUITE),

    ("lease: a record with neither timestamp is guessed instead of refused",
     LEASE,
     'raise RecordError("record has neither RELEASED_AT nor EXPIRES_AT; state is underivable")',
     'return "ACTIVE"',
     LEASE_SUITE),

    ("lease: the singleton invariant stops being checked",
     LEASE,
     'print(f"INVARIANT VIOLATED: {len(live)} leases derive ACTIVE — {live}. "',
     'print(f"ok {len(live)} "',
     LEASE_SUITE),

    ("fingerprint: composition stops being order-independent",
     FINGERPRINT,
     "    return sorted(identifiers)",
     "    return list(identifiers)",
     FINGERPRINT_SUITE),

    ("fingerprint: CORE no longer has to include the actor's own contract",
     FINGERPRINT,
     'raise CompositionError("CORE must include the actor\'s own role contract")',
     "pass",
     FINGERPRINT_SUITE),

    ("fingerprint: an unparseable § P2.2 falls back instead of raising",
     FINGERPRINT,
     'raise CompositionError("the CORE block in § P2.2 did not parse")',
     'block = re.match(r"(CORE = x)", "CORE = x")',
     FINGERPRINT_SUITE),

    ("fingerprint: an unknown role is accepted instead of refused",
     FINGERPRINT,
     'raise CompositionError(f"unknown role {role!r}; known: {\', \'.join(sorted(roles))}")',
     "return []",
     FINGERPRINT_SUITE),
]


def run(root: Path, suite: str) -> int:
    return subprocess.run([sys.executable, str(root / suite)],
                          capture_output=True, text=True, cwd=root).returncode


def main() -> int:
    source = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    workspace = Path(tempfile.mkdtemp())
    base = workspace / "base"
    shutil.copytree(source, base, symlinks=True, ignore=shutil.ignore_patterns(".git"))

    print("=== BASELINE — every suite must be green before any arm can be interpreted ===")
    healthy = True
    for suite in sorted({arm[4] for arm in ARMS}):
        code = run(base, suite)
        healthy &= code == 0
        print(f"  {'GREEN' if code == 0 else 'RED  '}  {suite}")
    if not healthy:
        print("\nBASELINE NOT GREEN — a red arm would prove nothing. Stopping.", file=sys.stderr)
        shutil.rmtree(workspace, ignore_errors=True)
        return 2

    print("\n=== ARMS ===")
    caught = survived = stale = 0
    for index, (label, target, old, new, suite) in enumerate(ARMS):
        work = workspace / f"arm{index}"
        shutil.copytree(base, work, symlinks=True)
        path = work / target
        text = path.read_text(encoding="utf-8")
        if text.count(old) != 1:
            print(f"  STALE_ANCHOR  {label}\n"
                  f"                anchor occurs {text.count(old)}x in {target} — the defect was "
                  f"NOT reintroduced, so nothing was tested")
            stale += 1
            continue
        path.write_text(text.replace(old, new), encoding="utf-8")
        if run(work, suite) != 0:
            print(f"  CAUGHT        {label}")
            caught += 1
        else:
            print(f"  SURVIVED      {label}\n"
                  f"                {suite} stayed GREEN with the defect in place")
            survived += 1

    print(f"\ncaught {caught} · survived {survived} · stale anchors {stale} · of {len(ARMS)} arms")
    shutil.rmtree(workspace, ignore_errors=True)
    return 0 if survived == 0 and stale == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
