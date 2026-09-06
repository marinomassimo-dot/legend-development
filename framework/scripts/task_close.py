#!/usr/bin/env python3
"""Land a committed, verified task, detach its worktree and safely delete its branch.

Run from your own task worktree after the required checks (LEGEND_CORE §21e).
The default keeps that worktree for the next task. --remove-worktree is for a closed chat
and is refused while the worktree holds untracked OR ignored files, or is locked.
No staging, force, stash, reset, push or conflict resolution is performed. A merge that
conflicts is aborted so the checkout holding main stays exactly as it was; the task branch
and worktree are kept, and the repair is made on the task side before retrying.
"""
from __future__ import annotations

import argparse
import os
import shlex
import sys
from pathlib import Path

from branch_hygiene import GitError, git, repo_root, worktrees


def clean(path: Path, include_ignored: bool = False) -> None:
    flags = ["status", "--porcelain", "--untracked-files=all", "--ignore-submodules=none"]
    if include_ignored:
        flags.append("--ignored")
    if git(flags, path).strip():
        raise GitError(f"checkout is not clean: {path}")
    for marker in ("MERGE_HEAD", "CHERRY_PICK_HEAD", "REVERT_HEAD", "rebase-merge", "rebase-apply"):
        location = Path(git(["rev-parse", "--git-path", marker], path).strip())
        if not location.is_absolute():
            location = path / location
        if location.exists():
            raise GitError(f"unfinished Git operation ({marker}): {path}")


def protect_ignored(destination: Path, tip: str) -> None:
    """Check ignored files and directory/file collisions before Git touches main.

    --no-overwrite-ignore alone does not protect every non-fast-forward merge strategy.
    Collapse ignored directories so local caches and nested worktrees are not traversed.
    """
    ignored = git(["ls-files", "--others", "--ignored", "--exclude-standard",
                   "--directory", "-z"], destination).split("\0")
    base = git(["merge-base", "HEAD", tip], destination).strip()
    changed = git(["diff", "--name-only", "--no-renames", "-z", base, tip], destination).split("\0")
    for local in filter(None, ignored):
        local = local.rstrip("/")
        for target in filter(None, changed):
            if local == target or target.startswith(local + "/") or local.startswith(target + "/"):
                raise GitError(f"landing would overlap ignored material on main: {local}")


def close_task(start: Path, remove_worktree: bool = False,
               dry_run: bool = False, resume_branch: str | None = None) -> list[list[str]]:
    source = repo_root(start).resolve()
    trees = worktrees(source)
    mains = [Path(str(t["path"])).resolve() for t in trees if t["branch"] == "main"]
    if len(mains) != 1:
        raise GitError("main must be checked out in exactly one worktree")
    destination = mains[0]
    current = git(["branch", "--show-current"], source).strip()
    branch = resume_branch or current
    if not branch or branch == "main" or source == destination:
        raise GitError("run from your own task worktree, never from main")
    git(["check-ref-format", f"refs/heads/{branch}"], source)
    if current and current != branch:
        raise GitError("the requested branch is not the current task")
    if any(t["branch"] == branch and Path(str(t["path"])).resolve() != source for t in trees):
        raise GitError("the branch is checked out in another worktree")
    tip = git(["rev-parse", "--verify", f"refs/heads/{branch}"], source).strip()
    if git(["rev-parse", "HEAD"], source).strip() != tip:
        raise GitError("HEAD differs from the task branch; refusing detached resume")
    if remove_worktree and source == Path(str(trees[0]["path"])).resolve():
        raise GitError("the primary checkout cannot be removed")
    if remove_worktree and any(Path(str(t["path"])).resolve() == source and t.get("locked")
                               for t in trees):
        raise GitError("the task worktree is locked; keeping its branch and checkout")

    commands = [["git", "-C", str(destination), "merge", "--no-ff", "--no-edit",
                 "--no-overwrite-ignore", f"refs/heads/{branch}"],
                ["git", "-C", str(source), "switch", "--detach", "HEAD"],
                ["git", "-C", str(destination), "branch", "-d", "--", branch]]
    if remove_worktree:
        commands.append(["git", "-C", str(destination), "worktree", "remove", str(source)])
    clean(source, remove_worktree)
    clean(destination)
    protect_ignored(destination, tip)
    if dry_run:
        return commands

    common = Path(git(["rev-parse", "--git-common-dir"], source).strip())
    if not common.is_absolute():
        common = source / common
    lock = common / "legend-task-close.lock"
    try:
        descriptor = os.open(lock, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    except FileExistsError as exc:
        raise GitError(f"another task_close holds {lock}; inspect before retrying, and remove "
                       "the file by hand only when no closure is running") from exc
    try:
        os.close(descriptor)
        clean(source, remove_worktree)
        clean(destination)
        if git(["branch", "--show-current"], destination).strip() != "main":
            raise GitError("destination changed branch; retry after inspection")
        if git(["rev-parse", "HEAD"], source).strip() != tip:
            raise GitError("task HEAD changed; retry after inspection")
        if git(["branch", "--show-current"], source).strip() != current:
            raise GitError("task checkout changed branch; retry after inspection")
        protect_ignored(destination, tip)
        try:
            git(commands[0][3:], destination)
        except GitError as exc:
            # The destination is the checkout every actor lands on: a conflicted merge left
            # there would refuse every other closure until a human resolved it by hand.
            # Abort it, so main is exactly as before; the task branch and worktree stay
            # intact and the repair happens on the task side (merge main into the branch).
            merge_head = Path(git(["rev-parse", "--git-path", "MERGE_HEAD"], destination).strip())
            if not merge_head.is_absolute():
                merge_head = destination / merge_head
            if merge_head.exists():
                git(["merge", "--abort"], destination)
            raise GitError("landing conflicts with main; main restored unchanged, task branch "
                           f"kept for repair (merge main into {branch}, resolve, commit, "
                           f"retry): {exc}") from exc
        if git(["rev-parse", f"refs/heads/{branch}"], source).strip() != tip:
            raise GitError("task branch moved during landing; keeping it")
        git(["merge-base", "--is-ancestor", tip, "refs/heads/main"], destination)
        clean(destination)
        clean(source, remove_worktree)
        if git(["rev-parse", "HEAD"], source).strip() != tip:
            raise GitError("task HEAD changed during landing; keeping the branch")
        git(commands[1][3:], source)
        git(commands[2][3:], destination)
        if remove_worktree:
            git(commands[3][3:], destination)
    finally:
        lock.unlink()
    return commands


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--remove-worktree", action="store_true",
                        help="also remove the task worktree (closed chat); refused when it "
                             "holds untracked or ignored files, or is locked")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--branch", help="resume after detachment, only when HEAD is this branch's tip")
    args = parser.parse_args(argv)
    try:
        commands = close_task(Path.cwd(), args.remove_worktree, args.dry_run, args.branch)
    except (GitError, OSError) as exc:
        print(f"task_close: {exc}", file=sys.stderr)
        return 2
    print("\n".join(shlex.join(command) for command in commands))
    print("DRY_RUN" if args.dry_run else "TASK_CLOSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
