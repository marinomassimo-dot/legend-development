#!/usr/bin/env python3
"""Ask one control-plane reader the same question from several directories, and diff the answers.

## Why this is a command

The defect it exists to expose produced no error and no warning: `lease_state.py` resolved its
record against `os.getcwd()`, so from the repository root it read a 5-record lease and from the
orchestrator worktree a 9-record one, **both exit 0, both printing the same shape of answer.**
The only way to notice was to run it twice and compare — which is what this does, so that
noticing does not depend on somebody thinking to.

It is a probe, not a gate. It reports what each directory produced; it does not decide which
answer is right, and it does not know which control-plane objects are simultaneously relevant.

## Usage

    control_plane_probe.py --tool framework/scripts/lease_state.py <dir> [<dir> ...]
    control_plane_probe.py <dir> [<dir> ...]        # defaults to lease_state.py

Exit 0 when every supplied directory produced the same answer, 1 when they diverged, 2 when the
probe itself could not run. **Divergence is not automatically a defect**: two actor worktrees
holding different lease histories genuinely differ, and saying which of them is authoritative is
a governance question. Exit 1 means *these directories disagree*, nothing more.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEFAULT_TOOL = HERE / "lease_state.py"

EVIDENCE_PREFIXES = ("CONTROL_PLANE_SOURCE_PATH", "CONTROL_PLANE_SOURCE_SHA256",
                     "CONTROL_PLANE_RECORD_COUNT")


def probe(tool: Path, where: Path, extra: list[str]) -> dict:
    result = subprocess.run([sys.executable, str(tool), *extra],
                            capture_output=True, text=True, cwd=str(where))
    output = result.stdout + result.stderr
    evidence = {}
    for line in output.splitlines():
        for prefix in EVIDENCE_PREFIXES:
            if line.startswith(prefix):
                evidence[prefix] = line[len(prefix):].strip()
    verdict = ""
    for line in output.splitlines():
        stripped = line.strip()
        if stripped.startswith(("ACTIVE by derivation", "VERDICT", "LEASE STATE UNDERIVABLE")):
            verdict = stripped
    return {"exit": result.returncode, "evidence": evidence, "verdict": verdict}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("directories", nargs="+", type=Path)
    parser.add_argument("--tool", type=Path, default=DEFAULT_TOOL)
    parser.add_argument("--arg", action="append", default=[],
                        help="extra argument passed to the tool; repeatable")
    arguments = parser.parse_args(argv)

    if not arguments.tool.is_file():
        print(f"probe cannot run: {arguments.tool} is not a file", file=sys.stderr)
        return 2

    rows = []
    for where in arguments.directories:
        if not where.is_dir():
            rows.append((str(where), {"exit": None, "evidence": {}, "verdict": "(no such directory)"}))
            continue
        rows.append((str(where), probe(arguments.tool, where, arguments.arg)))

    width = max(len(name) for name, _ in rows)
    print(f"tool: {arguments.tool}")
    print(f"{'CWD'.ljust(width)}  EXIT  SOURCE / VERDICT")
    print("-" * (width + 90))
    signatures = set()
    for name, result in rows:
        evidence = result["evidence"]
        signature = (evidence.get("CONTROL_PLANE_SOURCE_SHA256"),
                     evidence.get("CONTROL_PLANE_RECORD_COUNT"),
                     result["exit"])
        signatures.add(signature)
        source = evidence.get("CONTROL_PLANE_SOURCE_PATH", "(the tool reports no source)")
        count = evidence.get("CONTROL_PLANE_RECORD_COUNT", "?")
        print(f"{name.ljust(width)}  {str(result['exit']).rjust(4)}  {source}")
        print(f"{''.ljust(width)}        records={count}  {result['verdict'][:70]}")

    print(f"\n{len(signatures)} distinct answer(s) across {len(rows)} directory(ies).")
    if len(signatures) > 1:
        print("DIVERGENT — the same command produced different control-plane objects or exits.\n"
              "This is a measurement, not a verdict: two actor worktrees holding different\n"
              "histories genuinely differ, and which is authoritative is not this tool's to say.",
              file=sys.stderr)
        return 1
    print("UNIFORM — every directory produced the same object and the same exit.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
