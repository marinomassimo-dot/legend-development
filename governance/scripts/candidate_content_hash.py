#!/usr/bin/env python3
"""Compute CANDIDATE_CONTENT_HASH over the candidate content domain, per P5.

The domain rule and the version prefix are NOT duplicated here. They are parsed out of § P5 of
plan_defined_parameters.md, the same way governance_fingerprint.py parses § P2.2, so the
governance document stays the single authoritative definition and this script cannot drift from
it. If P5 stops parsing, this fails loudly rather than falling back to a built-in default.

Why a script and not a shell pipeline: the revision-4 defect was one byte. `$(...)` command
substitution strips trailing newlines, so a value computed through a shell variable and a value
computed through a pipe differ, invisibly, on the same tree. Nothing here goes through a shell.

  candidate_content_hash.py --base <base-head> --tip <commit>
  candidate_content_hash.py --base <base-head> --tip <commit> --show-domain
"""

from __future__ import annotations

import argparse
import hashlib
import re
import subprocess
import sys
from pathlib import Path

GOVERNANCE_DIR = Path(__file__).resolve().parent.parent
REPO_ROOT = GOVERNANCE_DIR.parent
PARAMETERS = GOVERNANCE_DIR / "plan_defined_parameters.md"


class DomainError(RuntimeError):
    """The domain could not be read from governance. Never fall back to a default."""


def _git(*args: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(REPO_ROOT), *args],
        capture_output=True, text=True, check=False,
    )
    if result.returncode != 0:
        raise DomainError(f"git {' '.join(args)} failed: {result.stderr.strip()}")
    return result.stdout


def parse_p5() -> tuple[str, list[str]]:
    """Read the version prefix and the control-plane roots out of § P5. Raise rather than guess."""
    try:
        text = PARAMETERS.read_text(encoding="utf-8")
    except OSError as exc:
        raise DomainError(f"cannot read {PARAMETERS}: {exc}") from exc

    start = text.find("## P5 ")
    if start == -1:
        raise DomainError("§ P5 not found in plan_defined_parameters.md")
    section = text[start:]
    end = section.find("\n## ", 1)
    if end != -1:
        section = section[:end]

    version = re.search(r"^CANDIDATE_HASH_VERSION:\s*(\S+)\s*$", section, re.MULTILINE)
    if not version:
        raise DomainError("CANDIDATE_HASH_VERSION not declared in § P5")

    block = re.search(r"^CONTROL_PLANE_ROOTS:\s*$(.*?)^```", section, re.MULTILINE | re.DOTALL)
    if not block:
        raise DomainError("CONTROL_PLANE_ROOTS block not found in § P5")
    roots = [
        line.strip().lstrip("-").strip()
        for line in block.group(1).splitlines()
        if line.strip().startswith("-")
    ]
    if not roots:
        raise DomainError("CONTROL_PLANE_ROOTS is empty; an empty exclusion must be explicit")
    for root in roots:
        if not root.endswith("/"):
            raise DomainError(f"control-plane root must name a directory ending in '/': {root!r}")
    return version.group(1), roots


def domain(tip: str) -> tuple[list[str], list[str]]:
    """Split the tree at `tip` into (included lines, excluded paths), both path-sorted."""
    _, roots = parse_p5()
    included: list[str] = []
    excluded: list[str] = []
    for line in _git("ls-tree", "-r", "--full-tree", tip).splitlines():
        if not line:
            continue
        try:
            path = line.split("\t", 1)[1]
        except IndexError:
            raise DomainError(f"unparseable ls-tree line: {line!r}") from None
        if any(path.startswith(root) for root in roots):
            excluded.append(path)
        else:
            included.append(line)
    included.sort(key=lambda entry: entry.split("\t", 1)[1])
    excluded.sort()
    return included, excluded


def compute(base_head: str, tip: str) -> tuple[str, list[str], list[str], str]:
    version, _ = parse_p5()
    included, excluded = domain(tip)
    # Byte layout is pinned explicitly: every entry, including the last, is newline-terminated.
    serialized = f"{version}\n{base_head}\n" + "".join(f"{entry}\n" for entry in included)
    return hashlib.sha256(serialized.encode("utf-8")).hexdigest(), included, excluded, version


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", required=True, help="BASE_HEAD the candidate is bound to")
    parser.add_argument("--tip", required=True, help="commit whose tree defines the domain")
    parser.add_argument("--show-domain", action="store_true",
                        help="print the entry count and every excluded path")
    args = parser.parse_args()

    try:
        base = _git("rev-parse", args.base).strip()
        tip = _git("rev-parse", args.tip).strip()
        digest, included, excluded, version = compute(base, tip)
    except DomainError as exc:
        print(f"DOMAIN FAILED: {exc}", file=sys.stderr)
        return 2

    if args.show_domain:
        print(f"version        {version}")
        print(f"base_head      {base}")
        print(f"tip            {tip}")
        print(f"included       {len(included)} entries")
        print(f"excluded       {len(excluded)} entries (control plane):")
        for path in excluded:
            print(f"  - {path}")
    print(digest)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
