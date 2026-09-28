#!/usr/bin/env python3
"""Land a committed, verified task, detach its worktree and safely delete its branch.

Run from your own task worktree after the required checks (LEGEND_CORE §21e).
The default keeps that worktree for the next task. --remove-worktree is for a closed chat
and is refused while the worktree holds untracked OR ignored files, or is locked.
A task may be cut from `origin/main` rather than from a local `main` that carries other actors'
unpublished commits (`git worktree add --no-track -b task/<id> <path> origin/main`); it lands the
same way. After landing, a `PUSH_NOTE` on stderr lists the commits a push of main would publish
that this task did not make — information for the pusher, never a refusal.

No staging, force, stash, reset, push or conflict resolution is performed. A merge that
conflicts is aborted so the checkout holding main stays exactly as it was; the task branch
and worktree are kept, and the repair is made on the task side before retrying.

Before landing, the committed generated surfaces are verified against the EXACT merge result
(`candidate_tree_freshness.py`): only the checks whose inputs the landing changes run, and a
STALE surface refuses the landing with its regeneration commands — H0 (2026-09-24) found four
surfaces stale because direct landings changed their inputs and nothing on that path looked.
The only override is a stated reason, `--stale-surfaces-because "<why>"`, which is printed.
"""
from __future__ import annotations

import argparse
import os
import shlex
import sys
from pathlib import Path

from branch_hygiene import GitError, git, repo_root, worktrees
import candidate_tree_freshness as freshness


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


def check_freshness(source: Path, tip: str, main_sha: str,
                    stale_because: str | None) -> None:
    """Refuse a landing whose merge result leaves a generated surface stale, unless told why.

    A conflicted candidate is not judged here: the merge itself refuses it, naming the path.
    """
    try:
        report = freshness.evaluate(source, mode="merge", tip=tip, base=main_sha)
    except freshness.CandidateError as exc:
        if "conflicts" in str(exc):
            return
        report_text, code = f"candidate_tree_freshness: {exc}", 2
    else:
        report_text, code = freshness.render(report), report.exit_code
    if code == 0:
        checked = sum(r.status == freshness.FRESH for r in report.results)
        verdict = (f"FRESH on the merge result ({checked} checked" if checked
                   else "not affected by this landing (none checked")
        print(f"task_close: generated surfaces {verdict}, {report.seconds:.1f}s)",
              file=sys.stderr)
        return
    if stale_because and stale_because.strip():
        print(f"task_close: landing although the merge result is not fresh, because: "
              f"{stale_because.strip()}\n{report_text}", file=sys.stderr)
        return
    raise GitError("the merge result leaves generated surfaces stale or unverifiable; nothing "
                   "was landed. Regenerate on the task branch, commit, retry — or state why "
                   f"it is safe with --stale-surfaces-because \"<reason>\".\n{report_text}")


def close_task(start: Path, remove_worktree: bool = False,
               dry_run: bool = False, resume_branch: str | None = None,
               stale_because: str | None = None) -> list[list[str]]:
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

    commands = [["git", "-C", str(destination), "merge", "--no-ff", "-m", "repository: integrate task",
                 "--no-overwrite-ignore", f"refs/heads/{branch}"],
                ["git", "-C", str(source), "switch", "--detach", "HEAD"],
                ["git", "-C", str(destination), "branch", "-d", "--", branch]]
    if remove_worktree:
        commands.append(["git", "-C", str(destination), "worktree", "remove", str(source)])
    clean(source, remove_worktree)
    clean(destination)
    protect_ignored(destination, tip)
    checked_main = git(["rev-parse", "HEAD"], destination).strip()
    check_freshness(source, tip, checked_main, stale_because)
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
        current_main = git(["rev-parse", "HEAD"], destination).strip()
        if current_main != checked_main:
            # main moved while the surfaces were checked: the merge result is a different
            # tree, so it is checked again — under the lock, where task_close cannot race it.
            check_freshness(source, tip, current_main, stale_because)
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
        # A task branch cut from `origin/main` tracks it, and `branch -d` then measures "fully
        # merged" against that upstream — which has not moved until main is pushed, so the
        # delete was refused AFTER a correct landing (2026-09-28). Ancestry in main was verified
        # just above; the upstream is dropped only now, and only for this branch.
        if git(["for-each-ref", "--format=%(upstream)", f"refs/heads/{branch}"],
               destination).strip():
            git(["branch", "--unset-upstream", branch], destination)
        git(commands[2][3:], destination)
        if remove_worktree:
            git(commands[3][3:], destination)
    finally:
        lock.unlink()
    return commands


def unpublished_foreign(start: Path, tip: str) -> list[str]:
    """Commits a push of main would publish that the task did not make — informational only.

    Measured against main's upstream as last fetched (no network). Empty when main has no
    upstream. The landing merge itself is excluded with the other merges."""
    try:
        upstream = git(["rev-parse", "--abbrev-ref", "--symbolic-full-name", "main@{upstream}"],
                       start).strip()
        out = git(["log", "--no-merges", "--format=%h %an %s", f"{upstream}..main", f"^{tip}"],
                  start)
    except GitError:
        return []
    return [line for line in out.splitlines() if line.strip()]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--remove-worktree", action="store_true",
                        help="also remove the task worktree (closed chat); refused when it "
                             "holds untracked or ignored files, or is locked")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--branch", help="resume after detachment, only when HEAD is this branch's tip")
    parser.add_argument("--stale-surfaces-because", dest="stale_because", default=None,
                        metavar="REASON",
                        help="land even though the merge result leaves a generated surface "
                             "stale or unverifiable, for this stated reason (printed)")
    args = parser.parse_args(argv)
    try:
        commands = close_task(Path.cwd(), args.remove_worktree, args.dry_run, args.branch,
                              args.stale_because)
    except (GitError, OSError) as exc:
        print(f"task_close: {exc}", file=sys.stderr)
        return 2
    print("\n".join(shlex.join(command) for command in commands))
    print("DRY_RUN" if args.dry_run else "TASK_CLOSED")
    try:
        tip = git(["rev-parse", "HEAD"], Path.cwd()).strip()
        foreign = unpublished_foreign(Path.cwd(), tip)
    except (GitError, OSError):
        foreign = []
    if foreign:
        # Flushed first so the note is the LAST thing in a merged stream: piped stdout is
        # block-buffered and stderr is not, so without this `task_close 2>&1 | tail -3` printed
        # the git commands and TASK_CLOSED and cut the note off — measured 2026-09-28, when a
        # push published a peer's unpushed batch that this note had named.
        sys.stdout.flush()
        print(f"PUSH_NOTE: pushing main now also publishes {len(foreign)} commit(s) this task "
              "did not make (as of the last fetch):", file=sys.stderr)
        for line in foreign:
            print(f"  {line}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
