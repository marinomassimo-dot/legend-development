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

From a shell (a battery clone, a verify copy) never choose the directory name yourself: a fixed
name such as /tmp/bat_it38 is taken by whoever is first, and the second session then works inside
the first one's checkout (2026-11-08: a `git checkout` in another session's battery clone moved
its working tree mid-run). Let the module choose, and hand the box to the long-lived process:

    D=$(python3 framework/scripts/owned_scratch.py --make legend-battery-)   # a new, empty box
    ... clone into "$D/clone", start the run, note its PID ...
    python3 framework/scripts/owned_scratch.py --adopt "$D" --owner <PID>   # the run owns it now
    python3 framework/scripts/owned_scratch.py --release "$D"                # when you are done

What is refused, by design:
  * a box is never reused: `make` creates a new directory every call and has no name argument;
  * `release` removes only a real directory directly inside the temp directory, owned by this
    user, that carries an owner file, and whose owner is this process or is gone. A live
    other owner's box is refused — the owner file is a claim, not a licence to delete;
  * `reap` ignores a directory with no owner file (it was not made here, however it is named)
    and one whose owner is alive; a recycled PID is a different process only if the start time
    was recorded — where it could not be, the box is kept (the safe direction).

Exit codes: 0 done (the reaped boxes are printed) · 2 invalid invocation or a refused release.
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


class Refused(RuntimeError):
    """A release that would remove something this module cannot show to be a releasable box."""


def _identity(pid: int) -> str:
    start = process_wait.start_ticks(pid)
    return f"{pid}:{start}" if start is not None else f"{pid}"


def make(prefix: str, owner: int | None = None) -> Path:
    """A new empty temporary directory stamped with the owner's PID:START (default: this process).

    The name is chosen by `mkdtemp`, so two calls never return the same directory and an
    existing directory is never reused or adopted by name.
    """
    box = Path(tempfile.mkdtemp(prefix=prefix))
    (box / OWNER).write_text(_identity(owner or os.getpid()) + "\n", encoding="utf-8")
    return box


def owner_of(box: Path) -> tuple[int, int | None] | None:
    """The recorded owner of ``box``, or None when there is no readable owner file."""
    try:
        return process_wait.parse_identity((box / OWNER).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None


def owner_alive(box: Path) -> bool:
    """True while the recorded owner is the live incarnation. A box with no usable owner file is
    not ours to judge, so it counts as alive and is never reaped."""
    owner = owner_of(box)
    return True if owner is None else process_wait.pid_alive(*owner)


def _check_releasable(box: Path, caller: int | None = None) -> None:
    """Raise Refused unless ``box`` is a box of this module whose owner is this process (or the
    ``caller`` that ran this command line) or is gone."""
    if box.is_symlink() or not box.is_dir():
        raise Refused(f"{box} is not a real directory")
    if box.resolve().parent != Path(tempfile.gettempdir()).resolve():
        raise Refused(f"{box} is not directly inside the temp directory")
    if box.stat().st_uid != os.getuid():
        raise Refused(f"{box} belongs to another user")
    owner = owner_of(box)
    if owner is None:
        raise Refused(f"{box} has no owner file: it was not made by owned_scratch")
    if owner[0] not in (os.getpid(), caller) and process_wait.pid_alive(*owner):
        raise Refused(f"{box} is owned by process {owner[0]}, which is still running")


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


def release(box: Path, repo: Path | None = None, caller: int | None = None) -> None:
    """Remove ``box``: the worktrees of ``repo`` registered inside it, then the directory.

    Raises Refused (and removes nothing) unless the box passes ``_check_releasable``.
    """
    _check_releasable(box, caller)
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
        if not box.is_dir() or box.is_symlink() or box.stat().st_uid != os.getuid() \
                or owner_alive(box):
            continue
        reaped.append(box)
        if not dry_run:
            release(box, repo)
    return reaped


def _box_command(args) -> int:
    if args.make:
        if os.sep in args.make:
            raise ValueError("a box prefix must be a bare name")
        # Until adopted the box belongs to the caller's shell (the parent), not to this short CLI.
        print(make(args.make, args.owner or os.getppid()))
        return 0
    box = Path(args.adopt or args.release)
    if args.release:
        release(box, Path(args.repo) if args.repo else None, os.getppid())
        print(f"RELEASED {box}")
        return 0
    if args.owner <= 0 or not process_wait.pid_alive(args.owner):
        raise ValueError("--adopt needs --owner of a running process")
    _check_releasable(box, os.getppid())          # same proof of being a box of ours before it changes hands
    (box / OWNER).write_text(_identity(args.owner) + "\n", encoding="utf-8")
    print(f"ADOPTED {box} by {args.owner}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--make", metavar="PREFIX", help="create a new box and print its path")
    mode.add_argument("--adopt", metavar="BOX", help="hand BOX to --owner (a running PID)")
    mode.add_argument("--release", metavar="BOX", help="remove BOX if its owner is gone or you")
    parser.add_argument("--owner", type=int, default=0, help="PID that owns the box")
    parser.add_argument("--prefix", help="the box name prefix to reap")
    parser.add_argument("--repo", default="", help="also remove this repository's worktrees "
                                                     "registered inside a reaped box")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    try:
        if args.make or args.adopt or args.release:
            return _box_command(args)
        if not args.prefix:
            parser.error("--prefix is required to reap")
        boxes = reap(args.prefix, Path(args.repo) if args.repo else None, args.dry_run)
    except (ValueError, Refused) as exc:
        print(f"owned_scratch: {exc}", file=sys.stderr)
        return 2
    for box in boxes:
        print(("WOULD_REAP " if args.dry_run else "REAPED ") + str(box))
    print(f"{len(boxes)} box(es)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
