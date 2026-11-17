#!/usr/bin/env python3
"""Which commits did a shared branch lose? A read-only look at the reflog of a ref (default `main`) for tips that are no longer on it.

Why (2026-11-17, HE, ADV scoped continuation (c)): the shared root `main` is written by several actors, and a `reset` to `development/main` by one of them dropped commits another had
just made (a8dc81367 and f9aed6973 for Plan and IT; the reflog shows six such resets that day). No tool stated which dropped commit was still unpublished. This lists each tip the reflog ever
held and says one of: published (an ancestor of the upstream), on another branch, equivalent upstream (the same patch re-landed under another SHA, by `git cherry`), or DROPPED (none of those).
It reads and reports; with `--rescue` it only adds local refs `refs/rescue/<ref>/<sha12>` for the DROPPED ones so that nothing is garbage-collected. It never resets, merges, cherry-picks or edits a worktree,
and it does not know who ran the reset.
Limits: a reflog is local and expires; a commit made and reset away on another clone is not seen; `git cherry` compares patches, so a landing that edited the patch reads DROPPED (a false alarm, not a loss).
"""
from __future__ import annotations

import argparse
import subprocess
import sys


def git(root: str, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-C", root, *args], capture_output=True, text=True)


def classify(root: str, sha: str, upstream: str, ref: str) -> str:
    if git(root, "merge-base", "--is-ancestor", sha, upstream).returncode == 0:
        return "published"
    parents = git(root, "rev-list", "--parents", "-n1", sha).stdout.split()[1:]
    others = [b.strip().lstrip("* ") for b in git(root, "branch", "-a", "--contains", sha).stdout.splitlines() if b.strip().lstrip("* ") != ref]
    if others:
        return "on branch " + others[0]
    if parents:
        patches = [l[:1] for l in git(root, "cherry", upstream, sha, parents[0]).stdout.splitlines() if l.strip()]
        if patches and all(p == "-" for p in patches):
            return "equivalent upstream"
    return "DROPPED"


def scan(root: str, ref: str, upstream: str, limit: int) -> list[tuple[str, str, str, str]]:
    rows, seen = [], set()
    for line in git(root, "reflog", "show", ref, "--format=%H%x09%gs", "-n", str(limit)).stdout.splitlines():
        sha, _, why = line.partition("\t")
        if sha in seen or not sha:
            continue
        seen.add(sha)
        verdict = classify(root, sha, upstream, ref)
        if verdict != "published":
            rows.append((sha, verdict, git(root, "log", "-1", "--format=%an | %s", sha).stdout.strip()[:100], why[:60]))
    return rows


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--root", default=".", help="a checkout of the repository (default: the current directory)")
    ap.add_argument("--ref", default="main")
    ap.add_argument("--upstream", default="development/main")
    ap.add_argument("--limit", type=int, default=400, help="reflog entries to read")
    ap.add_argument("--rescue", action="store_true", help="add refs/rescue/<ref>/<sha12> for each DROPPED tip (local, non-destructive)")
    args = ap.parse_args(argv)
    if git(args.root, "rev-parse", "--verify", "-q", args.upstream).returncode != 0:
        print(f"REFUSED: {args.upstream} is not a ref here")
        return 2
    rows = scan(args.root, args.ref, args.upstream, args.limit)
    dropped = [r for r in rows if r[1] == "DROPPED"]
    for sha, verdict, subject, why in rows:
        print(f"{sha[:12]}  {verdict:20s}  {subject}   [{why}]")
        if args.rescue and verdict == "DROPPED":
            git(args.root, "update-ref", f"refs/rescue/{args.ref}/{sha[:12]}", sha)
    print(f"{len(rows)} tip(s) of {args.ref} not on {args.upstream} by ancestry; {len(dropped)} DROPPED"
          + (" (rescue refs written)" if args.rescue and dropped else "") + f"; read from the last {args.limit} reflog entries")
    return 1 if dropped else 0


if __name__ == "__main__":
    sys.exit(main())
