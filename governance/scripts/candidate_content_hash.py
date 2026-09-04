#!/usr/bin/env python3
"""Compute CANDIDATE_CONTENT_HASH over the candidate content domain, per P5.

The domain rule and the version prefix are NOT duplicated here. They are parsed out of § P5 of
plan_defined_parameters.md, the same way governance_fingerprint.py parses § P2.2, so the
governance document stays the single authoritative definition and this script cannot drift from
it. If P5 stops parsing, this fails loudly rather than falling back to a built-in default.

🔴 **The rule is read from the tip being hashed, never from the working tree.** A candidate is
hashed under the governance its own commit carries, so the hash is a function of `(base, tip)`
alone. Reading the rule from the checkout made it a function of `(base, tip, whichever branch
happened to be checked out)`: the same tip produced different values from different branches,
which is the reproducibility failure the whole recipe exists to prevent. The defect was latent
while every candidate was hashed from its own branch and became observable the first time two
branches carried different governance.

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
PARAMETERS_PATH = "governance/plan_defined_parameters.md"


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


def parse_p5(tip: str) -> tuple[str, list[str]]:
    """Read the version prefix and the control-plane roots out of § P5 **at `tip`**.

    Never from the working tree: the rule must travel with the commit being hashed, or the same
    tip yields different hashes from different checkouts. Raise rather than guess or fall back.
    """
    try:
        text = _git("show", f"{tip}:{PARAMETERS_PATH}")
    except DomainError as exc:
        raise DomainError(
            f"the domain rule is absent at {tip}: {PARAMETERS_PATH} could not be read there "
            f"({exc}). A tip that does not carry § P5 cannot be hashed under it, and this "
            f"command will not substitute the working tree's copy."
        ) from exc

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
    _, roots = parse_p5(tip)
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


def serialize_domain(base_head: str, tip: str) -> tuple[str, list[str], list[str], str]:
    """Build the explicit, versioned domain representation that IS the hashed object.

    The hash is not defined as "whatever this script does". It is defined over these bytes, which
    any implementation can rebuild from `(base, tip)` alone — so the digest is checkable by a tool
    nobody has written yet, and this script becomes one implementation of a published recipe
    rather than the recipe itself.
    """
    version, _ = parse_p5(tip)
    included, excluded = domain(tip)
    serialized = f"{version}\n{base_head}\n" + "".join(f"{entry}\n" for entry in included)
    return serialized, included, excluded, version


def compute(base_head: str, tip: str) -> tuple[str, list[str], list[str], str]:
    version, _ = parse_p5(tip)
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
    parser.add_argument("--emit-domain", action="store_true",
                        help="print the explicit domain representation itself, the bytes that are "
                             "hashed, so a third party can rebuild and re-digest them")
    args = parser.parse_args()

    try:
        base = _git("rev-parse", args.base).strip()
        tip = _git("rev-parse", args.tip).strip()
        digest, included, excluded, version = compute(base, tip)
    except DomainError as exc:
        print(f"DOMAIN FAILED: {exc}", file=sys.stderr)
        return 2

    if args.emit_domain:
        serialized, _, _, _ = serialize_domain(base, tip)
        sys.stdout.write(serialized)
        return 0

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
