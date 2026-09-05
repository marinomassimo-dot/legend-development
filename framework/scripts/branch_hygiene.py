#!/usr/bin/env python3
"""What is not on `main`, and how old is it — the weekly hygiene report of LEGEND_CORE §21e.

Under `DEC-20260905-AGILE-HARNESS-MODE` a worktree is a place to work during a task, never a
place to keep work: every author lands its own task branch on `main` at task end and deletes
it, and nothing stays unmerged at rest. A rule like that is only as real as the instrument
that shows when it is broken, and before this script existed the fact was invisible — on
2026-09-05 six actor branches carried 291 commits that were not in the model, some of them
for over two weeks, and the repository had diagnosed the condition three times without
anyone being able to list it in one command.

This is a REPORT, not a gate. It never mutates anything, it never exits non-zero on what it
finds (only on a git it cannot talk to), and it ends with the landing recipe rather than
with a verdict — Harness Engineering runs it every Monday and acts on the table.

Classes, one per branch:

  MAIN                          the integration branch itself
  LAND_OVERDUE                  ahead of main, and older than --max-age-days (default 1)
  IN_PROGRESS                   ahead of main, within the age limit
  DELETE_READY                  nothing ahead of main, not checked out anywhere
  DELETE_BLOCKED_CHECKED_OUT    nothing ahead of main, but a worktree has it checked out

Usage:
  python3 framework/scripts/branch_hygiene.py                 # markdown report
  python3 framework/scripts/branch_hygiene.py --json          # same data, machine-readable
  python3 framework/scripts/branch_hygiene.py --max-age-days 3 --exclude-pattern '^codex/'
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Optional

MAIN = "MAIN"
LAND_OVERDUE = "LAND_OVERDUE"
IN_PROGRESS = "IN_PROGRESS"
DELETE_READY = "DELETE_READY"
DELETE_BLOCKED_CHECKED_OUT = "DELETE_BLOCKED_CHECKED_OUT"

CLASS_ORDER = (LAND_OVERDUE, IN_PROGRESS, DELETE_BLOCKED_CHECKED_OUT, DELETE_READY, MAIN)


class GitError(RuntimeError):
    pass


def git(args: List[str], cwd: Path) -> str:
    result = subprocess.run(["git", *args], cwd=str(cwd), capture_output=True, text=True)
    if result.returncode != 0:
        raise GitError(f"git {' '.join(args)}: {result.stderr.strip()}")
    return result.stdout


def repo_root(start: Path) -> Path:
    return Path(git(["rev-parse", "--show-toplevel"], start).strip())


def worktrees(root: Path) -> List[Dict[str, object]]:
    """`git worktree list --porcelain`, plus a dirty count per checkout that still exists."""
    out: List[Dict[str, object]] = []
    current: Dict[str, object] = {}
    for line in git(["worktree", "list", "--porcelain"], root).splitlines():
        if not line.strip():
            if current:
                out.append(current)
                current = {}
            continue
        key, _, value = line.partition(" ")
        if key == "worktree":
            current = {"path": value, "branch": None, "head": None}
        elif key == "HEAD":
            current["head"] = value
        elif key == "branch":
            current["branch"] = value.replace("refs/heads/", "", 1)
        elif key == "detached":
            current["branch"] = None
    if current:
        out.append(current)
    for entry in out:
        path = Path(str(entry["path"]))
        if not path.exists():
            entry["missing"] = True
            entry["dirty"] = None
            continue
        entry["missing"] = False
        try:
            porcelain = git(["status", "--porcelain"], path)
            entry["dirty"] = len([ln for ln in porcelain.splitlines() if ln.strip()])
        except GitError:
            entry["dirty"] = None
    return out


def branches(root: Path, main: str, now: dt.datetime) -> List[Dict[str, object]]:
    rows: List[Dict[str, object]] = []
    listing = git(["for-each-ref", "--format=%(refname:short)%09%(committerdate:iso-strict)",
                   "refs/heads"], root)
    for line in listing.splitlines():
        if not line.strip():
            continue
        name, _, date = line.partition("\t")
        # `iso-strict` writes a trailing `Z` for UTC, which `fromisoformat` accepts only
        # from Python 3.11; the explicit offset is understood everywhere.
        when = dt.datetime.fromisoformat(date.strip().replace("Z", "+00:00"))
        if when.tzinfo is None:
            when = when.replace(tzinfo=dt.timezone.utc)
        age_days = max(0, int((now - when).total_seconds() // 86400))
        if name == main:
            behind = ahead = 0
        else:
            counts = git(["rev-list", "--left-right", "--count", f"{main}...{name}"], root)
            left, _, right = counts.strip().partition("\t")
            behind, ahead = int(left or 0), int(right or 0)
        rows.append({"branch": name, "ahead": ahead, "behind": behind,
                     "last_commit": when.isoformat(), "age_days": age_days})
    return rows


def classify(rows: List[Dict[str, object]], trees: List[Dict[str, object]],
             main: str, max_age_days: int) -> List[Dict[str, object]]:
    checked_out = {str(t["branch"]): str(t["path"]) for t in trees if t.get("branch")}
    for row in rows:
        name = str(row["branch"])
        row["checked_out_at"] = checked_out.get(name)
        if name == main:
            row["class"] = MAIN
        elif int(row["ahead"]) > 0:
            row["class"] = LAND_OVERDUE if int(row["age_days"]) > max_age_days else IN_PROGRESS
        elif row["checked_out_at"]:
            row["class"] = DELETE_BLOCKED_CHECKED_OUT
        else:
            row["class"] = DELETE_READY
    rows.sort(key=lambda r: (CLASS_ORDER.index(str(r["class"])), -int(r["age_days"]),
                             str(r["branch"])))
    return rows


def totals_line(rows: List[Dict[str, object]]) -> str:
    n = len(rows)
    ahead = sum(int(r["ahead"]) for r in rows)
    overdue = sum(1 for r in rows if r["class"] == LAND_OVERDUE)
    ready = sum(1 for r in rows if r["class"] == DELETE_READY)
    return (f"{n} branches · {ahead} ahead-of-main commits total · "
            f"{overdue} LAND_OVERDUE · {ready} DELETE_READY")


def landing_recipe(root: Path) -> str:
    return "\n".join([
        "```",
        "# from the root checkout, or from your worktree with `git -C <root>`:",
        f"git -C {root} merge --no-ff <branch>      # or --ff-only when main has not moved",
        "git branch -d <branch>                    # safe delete: refuses if unmerged",
        "git worktree remove <path>                # only for a worktree whose chat is closed; refuses if dirty",
        "```",
    ])


def render_markdown(root: Path, rows: List[Dict[str, object]],
                    trees: List[Dict[str, object]], max_age_days: int) -> str:
    lines = [f"# Branch hygiene — {root}", "",
             f"Rule: LEGEND_CORE §21e · a branch ahead of `main` for more than "
             f"{max_age_days} day(s) is LAND_OVERDUE.", "",
             "| class | branch | ahead | behind | age (days) | last commit | checked out at |",
             "|---|---|---|---|---|---|---|"]
    for r in rows:
        lines.append(f"| {r['class']} | `{r['branch']}` | {r['ahead']} | {r['behind']} | "
                     f"{r['age_days']} | {str(r['last_commit'])[:10]} | "
                     f"{r['checked_out_at'] or '—'} |")
    lines += ["", f"**{totals_line(rows)}**", "", "## Worktrees", "",
              "| path | branch | dirty files | state |", "|---|---|---|---|"]
    for t in trees:
        state = "MISSING" if t.get("missing") else ("dirty" if t.get("dirty") else "clean")
        dirty = "?" if t.get("dirty") is None else str(t.get("dirty"))
        lines.append(f"| {t['path']} | `{t.get('branch') or '(detached)'}` | {dirty} | {state} |")
    lines += ["", "## Landing recipe", "", landing_recipe(root), ""]
    return "\n".join(lines)


def build_report(root: Path, main: str, max_age_days: int, include: Optional[str],
                 exclude: Optional[str], now: Optional[dt.datetime] = None) -> Dict[str, object]:
    now = now or dt.datetime.now(dt.timezone.utc)
    trees = worktrees(root)
    rows = branches(root, main, now)
    if include:
        rows = [r for r in rows if re.search(include, str(r["branch"])) or r["branch"] == main]
    if exclude:
        rows = [r for r in rows if not re.search(exclude, str(r["branch"])) or r["branch"] == main]
    rows = classify(rows, trees, main, max_age_days)
    return {"root": str(root), "main": main, "max_age_days": max_age_days,
            "generated": now.isoformat(), "branches": rows, "worktrees": trees,
            "totals": totals_line(rows), "landing_recipe": landing_recipe(root)}


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--root", default=".", help="any path inside the repository")
    parser.add_argument("--main", default="main", help="the integration branch (default: main)")
    parser.add_argument("--max-age-days", type=int, default=1,
                        help="a branch ahead of main and older than this is LAND_OVERDUE")
    parser.add_argument("--include-pattern", default=None, help="regex; keep matching branches")
    parser.add_argument("--exclude-pattern", default=None, help="regex; drop matching branches")
    parser.add_argument("--json", action="store_true", help="emit JSON instead of markdown")
    args = parser.parse_args(argv)
    try:
        root = repo_root(Path(args.root).resolve())
        report = build_report(root, args.main, args.max_age_days,
                              args.include_pattern, args.exclude_pattern)
    except GitError as exc:
        print(f"branch_hygiene: {exc}", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print(render_markdown(root, list(report["branches"]), list(report["worktrees"]),
                              args.max_age_days))
    return 0


if __name__ == "__main__":
    sys.exit(main())
