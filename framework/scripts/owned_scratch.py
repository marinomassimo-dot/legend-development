#!/usr/bin/env python3
"""Temporary directories that carry their owner's identity, so a dead owner's leftovers are reaped.

WHY THIS EXISTS
---------------
On 2026-09-26 two detached worktrees of this repository were found registered under `/tmp`
(`/tmp/tmpwea7wqn_/tree`, 2026-09-14, and `/tmp/tmp37jhblwn/tree`, 2026-09-26), each holding a
test's planted edit — a broken wikilink appended to `governance/ANNEX_INDEX.md`, an untracked
`vendored_untracked/.git`. Both came from `scripts/test_repository_surface_determinism.py`,
whose `addCleanup` removes the worktree correctly — when it runs. A process killed mid-test
(a shell timeout around the battery, an interrupted session) never reaches it, and the
directory's name (`tmpXXXXXXXX`) said nothing about who made it or whether that process was
still alive, so nobody could safely remove it either.

A cleanup that only runs on the happy path is a leak with a delay. This module makes the
leftover reapable: every box records `PID:START` of its creator (the identity convention of
`process_wait.py`, so a recycled PID is not mistaken for the owner), and `reap()` removes every
box of a given prefix whose owner is gone — the worktrees registered under it first, then the
directory, then `git worktree prune`. A live owner's box is never touched.

    box = owned_scratch.make("legend-candidate-tree-")
    try: ...
    finally: owned_scratch.release(box, repo)
    owned_scratch.reap("legend-candidate-tree-", repo)   # at the next start

    python3 framework/scripts/owned_scratch.py --prefix legend-candidate-tree- [--repo .] [--dry-run]

Exit codes: 0 done (the reaped boxes are printed) · 2 invalid invocation.
"""
from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import process_wait  # noqa: E402

OWNER = ".owner"
# A box without an owner file younger than this is being created right now, not abandoned.
GRACE_SECONDS = 120


def make(prefix: str) -> Path:
    """A fresh temporary directory stamped with this process's PID:START."""
    box = Path(tempfile.mkdtemp(prefix=prefix))
    start = process_wait.start_ticks(os.getpid())
    (box / OWNER).write_text(f"{os.getpid()}:{start if start is not None else ''}".rstrip(":")
                             + "\n", encoding="utf-8")
    return box


def owner_alive(box: Path) -> bool:
    try:
        text = (box / OWNER).read_text(encoding="utf-8").strip()
    except OSError:
        try:
            return time.time() - box.stat().st_mtime < GRACE_SECONDS
        except OSError:
            return False
    try:
        pid, start = process_wait.parse_identity(text)
    except ValueError:
        return False
    return process_wait.pid_alive(pid, start)


def _registered_under(repo: Path, box: Path) -> list[Path]:
    done = subprocess.run(["git", "-C", str(repo), "worktree", "list", "--porcelain"],
                          capture_output=True, text=True, timeout=60)
    if done.returncode != 0:
        return []
    resolved = box.resolve()
    found = []
    for line in done.stdout.splitlines():
        if line.startswith("worktree "):
            path = Path(line[len("worktree "):]).resolve()
            if path == resolved or resolved in path.parents:
                found.append(path)
    return found


def release(box: Path, repo: Path | None = None) -> None:
    """Remove ``box``: the worktrees of ``repo`` registered inside it, then the directory."""
    if repo is not None:
        for tree in _registered_under(repo, box):
            subprocess.run(["git", "-C", str(repo), "worktree", "remove", "--force", "--force",
                            str(tree)], capture_output=True, timeout=120)
    shutil.rmtree(box, ignore_errors=True)
    if repo is not None:
        subprocess.run(["git", "-C", str(repo), "worktree", "prune"], capture_output=True,
                       timeout=120)


def reap(prefix: str, repo: Path | None = None, dry_run: bool = False) -> list[Path]:
    """Release every box named ``prefix*`` in the temp directory whose owner is gone."""
    if not prefix or os.sep in prefix:
        raise ValueError("a reap prefix must be a non-empty bare name")
    reaped = []
    for box in sorted(Path(tempfile.gettempdir()).glob(prefix + "*")):
        if not box.is_dir() or box.is_symlink() or owner_alive(box):
            continue
        reaped.append(box)
        if not dry_run:
            release(box, repo)
    return reaped


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--prefix", required=True, help="the box name prefix to reap")
    parser.add_argument("--repo", default="", help="also remove this repository's worktrees "
                                                     "registered inside a reaped box")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    try:
        boxes = reap(args.prefix, Path(args.repo) if args.repo else None, args.dry_run)
    except ValueError as exc:
        print(f"owned_scratch: {exc}", file=sys.stderr)
        return 2
    for box in boxes:
        print(("WOULD_REAP " if args.dry_run else "REAPED ") + str(box))
    print(f"{len(boxes)} box(es)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
