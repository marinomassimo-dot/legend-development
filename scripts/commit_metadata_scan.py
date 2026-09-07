#!/usr/bin/env python3
"""Ref-scoped privacy scan of Git *commit metadata*.

The tree scanners answer "what does this tree contain". Neither of them — not
`public_release_gate.py`, not `independent_privacy_scan.py` — opens a commit object, so
an author or committer address travels to a public remote through a channel no
publication check looks at. A tree can be spotless while every commit carrying it is
stamped with a personal address, and the gate will say PASS.

Scope is the whole point
------------------------
The population is `git rev-list <ref> --not <base>...` — exactly the commits that
publishing *ref* would add to a remote that already has *base*. It is deliberately not
"every ref in the repository":

  * scanning all refs makes one branch's defect block every other branch's publication,
    which is how a check stops being run at all;
  * already-published history cannot be un-published by refusing to push something else,
    so counting it as a finding of *this* ref is a false attribution.

`--base` is therefore required. Without it the scan exits 3 rather than silently
choosing a population, because a check that picks its own denominator reports a number
nobody can reproduce.

Fail closed on an allowlist, not a denylist
-------------------------------------------
Permitted identities are enumerated; anything else is a finding. A denylist would have
to name the private address it is protecting — writing the identifier into a public file
to check that the identifier is not in public files — and it would miss every address
never seen before.

    python3 scripts/commit_metadata_scan.py --ref <ref> --base <base> [--base <base>...]

Exit codes:
  0  every scanned commit carries a permitted identity
  2  at least one finding
  3  invalid invocation, or the control could not fire (result void)
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from dataclasses import asdict, dataclass


# Identities a published LEGEND commit may carry, as SHA-256 digests of the exact address.
#
# Digests rather than literals, for the same reason `public_release_gate.py` stores its
# identifier digests that way: a file that names an address *is* a file containing an
# address, and the tree scanner is right to block it. The literal form of this table was
# written first and measured — it produced seven EMAIL_ADDRESS blocks on this branch,
# making this scanner's own source the only file in the repository failing the tree scan.
#
# Recompute with:
#     python3 -c "import hashlib,sys;print(hashlib.sha256(sys.argv[1].encode()).hexdigest())" ADDRESS
PERMITTED_COMMIT_IDENTITY_DIGESTS = frozenset({
    # the project identity carried by every published LEGEND commit
    "2867e7391c44b7e14b0094822aa9620d152f480883277cbe318f486b107ff0b5",
    # the reserved synthetic identity used by fixture history
    "c135afb8b05884dbfee82b66d73eaba5e2966da67e105e6b07fd4b1583dedaca",
})


def identity_digest(address: str) -> str:
    return hashlib.sha256(address.encode()).hexdigest()

# A commit records two identities and both are published. Checking only the author is the
# common shape of this bug: `git commit --amend --author=...` rewrites one of the two.
IDENTITY_FIELDS = ("author", "committer")


@dataclass(order=True)
class Finding:
    severity: str
    code: str
    commit: str
    field: str
    message: str


def git(args: list[str], root: str) -> str:
    result = subprocess.run(
        ["git", "-C", root, *args],
        check=False, capture_output=True, text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)}: {result.stderr.strip()}")
    return result.stdout


def commits_in_scope(root: str, ref: str, bases: list[str]) -> list[str]:
    """Exactly the commits that publishing *ref* would add to a remote holding *bases*."""
    args = ["rev-list", ref, "--not", *bases]
    return [line for line in git(args, root).split("\n") if line]


def identities(root: str, commit: str) -> dict[str, tuple[str, str]]:
    """Return {field: (name, email)} read from the raw commit object.

    Read from the object rather than a `--format` placeholder: a name containing the
    delimiter would otherwise split into the wrong field, and a malformed record must not
    be silently reshaped into a well-formed one.
    """
    raw = git(["cat-file", "commit", commit], root)
    header = raw.split("\n\n", 1)[0]
    found: dict[str, tuple[str, str]] = {}
    for line in header.split("\n"):
        for field in IDENTITY_FIELDS:
            prefix = field + " "
            if line.startswith(prefix) and field not in found:
                rest = line[len(prefix):]
                if "<" in rest and ">" in rest:
                    name = rest[: rest.index("<")].strip()
                    email = rest[rest.index("<") + 1: rest.index(">")]
                    found[field] = (name, email)
    return found


def scan(
    root: str, ref: str, bases: list[str],
    permitted: frozenset[str] = PERMITTED_COMMIT_IDENTITY_DIGESTS,
) -> tuple[list[Finding], int]:
    findings: list[Finding] = []
    scanned = commits_in_scope(root, ref, bases)
    for commit in scanned:
        seen = identities(root, commit)
        for field in IDENTITY_FIELDS:
            if field not in seen:
                findings.append(Finding(
                    "BLOCK", "UNREADABLE_COMMIT_IDENTITY", commit, field,
                    f"Commit has no readable {field} identity.",
                ))
                continue
            _name, email = seen[field]
            if identity_digest(email) not in permitted:
                findings.append(Finding(
                    "BLOCK", "NON_PROJECT_COMMIT_IDENTITY", commit, field,
                    f"{field} email is not a permitted project identity.",
                ))
    return findings, len(scanned)


def control_can_fire() -> bool:
    """A checker that cannot fail reports PASS on everything.

    The control is on the predicate, not on git: an address outside the allowlist must be
    rejected and a permitted one accepted. If both answers agree, the predicate is dead.
    """
    unlisted = identity_digest("not-a-project-identity@example.invalid")
    rejects = unlisted not in PERMITTED_COMMIT_IDENTITY_DIGESTS
    well_formed = all(len(d) == 64 for d in PERMITTED_COMMIT_IDENTITY_DIGESTS)
    return rejects and well_formed and bool(PERMITTED_COMMIT_IDENTITY_DIGESTS)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="Repository root")
    parser.add_argument("--ref", required=True, help="Ref being published")
    parser.add_argument(
        "--base", action="append", default=[], metavar="REF",
        help="A ref the destination already has. Repeatable. Required.",
    )
    parser.add_argument("--report-json", help="Write machine-readable report")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not args.base:
        print(
            "SCAN_ERROR: --base is required; refusing to choose the population implicitly.",
            file=sys.stderr,
        )
        return 3
    if not control_can_fire():
        print("SCAN_VOID: the identity predicate cannot fire.", file=sys.stderr)
        return 3
    try:
        findings, scanned = scan(args.root, args.ref, args.base)
    except RuntimeError as exc:  # fail closed
        print(f"SCAN_ERROR: {exc}", file=sys.stderr)
        return 3

    blocks = [f for f in findings if f.severity == "BLOCK"]
    result = {
        "verdict": "BLOCK_PUBLICATION" if blocks else "PASS",
        "ref": args.ref,
        "base": args.base,
        "commits_scanned": scanned,
        "block_count": len(blocks),
        "findings": [asdict(f) for f in findings],
    }
    if args.report_json:
        with open(args.report_json, "w", encoding="utf-8") as handle:
            json.dump(result, handle, indent=2, ensure_ascii=False)
            handle.write("\n")

    print("CONTROL  identity predicate live")
    print(f"SCANNED  {scanned} commit(s) in scope for {args.ref}")
    print(f"VERDICT: {result['verdict']}")
    print(f"BLOCKS: {len(blocks)}")
    for finding in sorted(findings):
        print(
            f"[{finding.severity}] {finding.code} "
            f"{finding.commit[:12]} {finding.field} — {finding.message}"
        )
    return 2 if blocks else 0


if __name__ == "__main__":
    raise SystemExit(main())
