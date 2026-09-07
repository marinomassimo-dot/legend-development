#!/usr/bin/env python3
"""Where is the repository authority root? One answer, or a refusal — never a guess.

## The defect this exists to remove

Three tools resolved a control-plane path against `os.getcwd()`:

    lease_state.py    DEFAULT_HOME    = "runtime/orchestrator_lease.md"
    legend_lint.py    positional root, default "."
    sync_epochs.py    --root,         default "."

So the answer depended on where the caller was standing. Measured, one repository, one tool:

    cwd = repository root          5 lease records, exit 0
    cwd = orchestrator worktree    9 lease records, exit 0      <- a different object
    cwd = framework/scripts        exit 2, "cannot read runtime/orchestrator_lease.md"
    cwd = /tmp                     exit 2

and `legend_lint.py` with no argument returns `VERDICT: PASS` from the repository root and
**`VERDICT: BLOCK_SYSTEM`** from a subdirectory of the same checkout. A false BLOCK is not
safer than a false PASS; it is the same defect wearing the other sign, and it trains readers
to disbelieve the gate.

## Why not the script's own location

`growth_anchors.py` already solves this with `HERE.parent.parent`, and that is deterministic —
but it is deterministic about the wrong thing. It answers with **the checkout the script lives
in**, so invoking one worktree's copy of a tool from another worktree silently reports on the
first. Worse, it **never refuses**: from `/tmp`, from a directory that is not a repository at
all, it confidently returns a root and reads a lease file. A primitive that always answers
cannot fail closed, and control-plane questions are exactly the ones that must.

## What this does instead

`git rev-parse --show-toplevel`, which resolves any directory inside a working tree to that
tree's root, and **fails outside one**. Same checkout, any subdirectory, one answer; no
repository, no answer.

## 🔴 What this deliberately does NOT decide

It binds to **the worktree the caller is in**, which is today's behaviour at the root and is
therefore not a semantic change. It does **not** bind to the shared repository behind every
worktree (`--git-common-dir`), and the difference is not cosmetic:

Annex I.3 states **`Un solo ACTIVE`** — one ACTIVE lease, an invariant of the laboratory, which
`lease_state.py` calls *"fatal in every mode"*. Under per-worktree lease records that invariant
is **unverifiable**: two worktrees each holding one ACTIVE lease both report
`ACTIVE by derivation: 1` and both exit 0, which is precisely what a healthy singleton looks
like. Reproduced with fixtures, not argued.

Making the control plane one object for the whole laboratory would fix that — and would also
change which lease record is authoritative, discarding four leases that exist on one worktree
and not the other. **That is a governance decision about the relevance set, not a path helper**,
and this module stops at the boundary rather than resolving it by import order.
"""
from __future__ import annotations

import subprocess
from pathlib import Path


class RootError(RuntimeError):
    """The repository authority root is not derivable. Never fall back to the cwd."""


def repo_root(start: Path | str | None = None) -> Path:
    """The working tree containing `start` (default: the current directory).

    Raises rather than returning a plausible wrong answer. There is no fallback: a control-plane
    path resolved against an arbitrary directory is how one tool came to report on two different
    objects depending on where it was launched.
    """
    where = Path(start) if start is not None else Path.cwd()
    if not where.is_dir():
        where = where.parent
    result = subprocess.run(
        ["git", "-C", str(where), "rev-parse", "--show-toplevel"],
        capture_output=True, text=True)
    if result.returncode != 0:
        raise RootError(
            f"{where} is not inside a git working tree, so the repository authority root cannot "
            f"be derived. Refusing rather than resolving control-plane paths against the "
            f"current directory")
    return Path(result.stdout.strip())


def control_plane(relative: str, start: Path | str | None = None) -> Path:
    """A control-plane surface, resolved against the authority root.

    Use this for `runtime/`, `ledger/` and `framework/state/` paths. The indirection exists so
    that if the relevance-set question above is ever settled — one control plane for the
    laboratory rather than one per worktree — there is a single place to settle it.
    """
    return repo_root(start) / relative


def add_root_argument(parser, flag: str = "--root") -> None:
    """Give a CLI a `--root` that defaults to the derived root, never to `.`.

    `default="."` is the cwd defect spelled as an argument default: it looks explicit and
    behaves exactly like resolving against the working directory.
    """
    parser.add_argument(flag, default=None,
                        help="repository root (default: derived from the working tree)")


def resolve_root_argument(value: str | None) -> Path:
    return Path(value).resolve() if value else repo_root()
