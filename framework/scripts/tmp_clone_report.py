#!/usr/bin/env python3
"""Report which clone-shaped folders under /tmp are dead and how much disk each one really holds; remove only the ones you name.

    python3 framework/scripts/tmp_clone_report.py                      # report only; deletes nothing, ever
    python3 framework/scripts/tmp_clone_report.py --older-than 3 --no-size
    python3 framework/scripts/tmp_clone_report.py --remove /tmp/legend-battery-x /tmp/it53_ci [--dry-run]

Why. On 2026-11-24 `/` was 100% full (219 MB free) and a landing died midway; the cause was battery clones under /tmp, and `du` made it
look worse and less actionable than it was because hard-linked `files/` counts once per tree. The checks below are the ones the Advisor applied by
hand when it freed 4.2 GB (ADV-207, 2026-11-24), written down so nobody has to reinvent them.

What counts as a candidate: a direct child of the temp root (default /tmp) that owns a `.git`, is named `legend-*`, or is named `tmp*` and holds a clone one level down
(`tmp*/trial_clone/.git`; 2026-11-25, ADV: such a folder, 17 days old, was invisible here), owned by you. Never listed,
never removable: `claude-*` (session scratchpads belong to the sessions), anything not a plain directory, anything owned by another user.

A candidate is REMOVABLE only when every check passes; otherwise it is KEEP with the reasons:
  * the git tree is clean (`git status --porcelain` empty) AND holds no ignored file except regenerable caches (`__pycache__`, `.pytest_cache`, `.mypy_cache`, `.ruff_cache`, `.hypothesis`, `*.pyc`, `*.pyo`):
    `git status` omits ignored files, and an ignored analysis output can be the only copy (a hand check on 2026-11-24 used plain `git status`), so any other ignored path is KEEP and is named;
  * every local branch, every tag and HEAD is an ancestor of the main ref in THIS repository (`--main-ref`, default development/main), by sha: a commit
    this repository has never seen, or one main does not contain, is unpublished work;
  * no stash (`refs/stash`);
  * no process has its working directory inside it or names it in its command line (this tool's own process excepted);
  * its newest direct entry or git bookkeeping file is older than `--older-than` days (default 1);
  * a `.git` FILE means a linked worktree: that is `git worktree remove`'s business, never this tool's.
A candidate with no `.git` of its own that holds clones one level down is REMOVABLE only when every nested clone passes the git checks above AND the folder holds nothing else (anything beside the clones is named and keeps it).
A folder with no `.git` and no nested clone has nothing to verify against; it is KEEP, except the scratch names this repository's own tools create and leak when
killed (`legend-public-gate-*`, `legend-candidate-tree-*`, `legend-landing-suites-*`, `legend-landing-base-*`), which need only the process and age checks.

Folders freeing under `--min-mb` (default 5) are counted but not listed, so hundreds of leaked 0 MB test fixtures do not bury the clones that matter.

Size: `freed` = bytes of the inodes ALL of whose hard links lie inside the folder (what removing it would really free); `shared` = bytes of inodes also
linked from outside it (nothing is freed for those). Sizes are allocated blocks, not apparent size. `--no-size` skips the walk.

`--remove` takes exact directory paths (no globs, no `..`, no symlinks), re-runs every check at that moment, refuses any folder that is not REMOVABLE and
deletes the rest with the checks passed in the same run. There is no sweep mode. `--dry-run` prints what would be removed. Exit 0 when nothing was refused, 1 when a named folder was refused.
"""
from __future__ import annotations

import argparse
import os
import shutil
import stat
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRATCH_NAMES = ("legend-public-gate-", "legend-candidate-tree-", "legend-landing-suites-", "legend-landing-base-")
# The only ignored paths that may be lost with a clone: caches a tool rebuilds by itself. Any other ignored path (an analysis output, a run folder, `files/`) can be the one unique
# copy of something and BLOCKS removal (Codex review 23, 2026-11-24: a clean repo whose only ignored file was files/unique-analysis.txt was reported REMOVABLE).
CACHE_DIRS = {"__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache", ".hypothesis"}
CACHE_SUFFIXES = (".pyc", ".pyo")


def is_regenerable(path: str) -> bool:
    parts = [x for x in path.rstrip("/").split("/") if x]
    return bool(parts) and (any(x in CACHE_DIRS for x in parts) or parts[-1].endswith(CACHE_SUFFIXES))


def git(repo: Path, *args: str, timeout: int = 120) -> subprocess.CompletedProcess:
    # --no-optional-locks: a plain `git status` rewrites .git/index (the stat refresh), which would reset the very age this tool reads: measured 2026-11-24, a second report showed 0.0 days for folders the first had seen at 1.3.
    return subprocess.run(["git", "--no-optional-locks", "-C", str(repo), *args], capture_output=True, text=True, timeout=timeout)


def nested_clones(d: Path) -> list[Path]:
    """Direct subfolders of `d` (never symlinks) that own a `.git`."""
    try:
        return sorted(Path(e.path) for e in os.scandir(d) if not e.is_symlink() and e.is_dir(follow_symlinks=False) and os.path.lexists(os.path.join(e.path, ".git")))
    except OSError:
        return []


def candidates(tmp: Path) -> list[Path]:
    """Direct children that look like clones, owned by this user; never claude-* and never a symlink."""
    out = []
    try:
        entries = sorted(os.scandir(tmp), key=lambda e: e.name)
    except OSError:
        return out
    for e in entries:
        try:
            if e.is_symlink() or not e.is_dir(follow_symlinks=False) or e.name.startswith("claude-"):
                continue
            if e.stat(follow_symlinks=False).st_uid != os.getuid():
                continue
            if os.path.lexists(os.path.join(e.path, ".git")) or e.name.startswith("legend-") or (e.name.startswith("tmp") and nested_clones(Path(e.path))):
                out.append(Path(e.path))
        except OSError:
            continue
    return out


def own_chain() -> set[int]:
    """This process and its ancestors: the shell that launched `--remove /tmp/x` carries /tmp/x in its own command line, and the first version refused itself because of it."""
    chain, pid = set(), os.getpid()
    while pid > 1 and pid not in chain:
        chain.add(pid)
        try:
            with open(f"/proc/{pid}/stat") as fh:
                pid = int(fh.read().rsplit(")", 1)[1].split()[1])      # field 4 (ppid), after the ")" that closes the command name
        except (OSError, ValueError, IndexError):
            break
    return chain


def process_holders(d: Path) -> list[str]:
    """Pids whose cwd is inside d or whose command line names d (this process and its ancestors excepted)."""
    skip, ds, hits = own_chain(), str(d), []
    try:
        pids = [p for p in os.listdir("/proc") if p.isdigit() and int(p) not in skip]
    except OSError:
        return hits
    for p in pids:
        try:
            cwd = os.readlink(f"/proc/{p}/cwd")
            if cwd == ds or cwd.startswith(ds + "/"):
                hits.append(f"{p} (cwd)")
                continue
            with open(f"/proc/{p}/cmdline", "rb") as fh:
                if ds.encode() in fh.read():
                    hits.append(f"{p} (cmdline)")
        except OSError:
            continue
    return hits


def newest_mtime(d: Path) -> float:
    """Newest of the folder, its direct entries (`.git` excepted) and the git files that move only when someone works in it. Not `.git/index` and not the `.git` folder itself:
    a stat-refreshing `git status` rewrites them, and the first version of this tool reset the age of every folder it had examined that way."""
    best = 0.0
    try:
        best = d.stat().st_mtime
        for e in os.scandir(d):
            if e.name == ".git":
                continue
            try:
                best = max(best, e.stat(follow_symlinks=False).st_mtime)
            except OSError:
                pass
        for name in ("HEAD", "FETCH_HEAD", "ORIG_HEAD", "logs/HEAD"):
            try:
                best = max(best, (d / ".git" / name).stat().st_mtime)
            except OSError:
                pass
    except OSError:
        pass
    return best


def disk_sizes(d: Path) -> tuple[int, int]:
    """(freed, shared) bytes: allocated blocks of the inodes all of whose links are inside d, and of those that are also linked outside."""
    seen: dict[tuple[int, int], list[int]] = {}      # (dev, ino) -> [links seen inside, nlink, bytes]
    stack = [str(d)]
    while stack:
        cur = stack.pop()
        try:
            it = os.scandir(cur)
        except OSError:
            continue
        with it:
            for e in it:
                try:
                    st = e.stat(follow_symlinks=False)
                except OSError:
                    continue
                if stat.S_ISDIR(st.st_mode):
                    stack.append(e.path)
                    continue
                k = (st.st_dev, st.st_ino)
                if k in seen:
                    seen[k][0] += 1
                else:
                    seen[k] = [1, st.st_nlink, st.st_blocks * 512]
    freed = sum(v[2] for v in seen.values() if v[0] >= v[1])
    shared = sum(v[2] for v in seen.values() if v[0] < v[1])
    return freed, shared


def resolve_main(repo: Path, main_ref: str) -> str | None:
    r = git(repo, "rev-parse", "--verify", "--quiet", f"{main_ref}^{{commit}}")
    return r.stdout.strip() or None if r.returncode == 0 else None


def git_checks(d: Path, repo: Path, main_sha: str) -> tuple[list[str], list[str]]:
    """(reasons to keep, notes) from the git state of the clone at `d`, which owns a `.git`. Read-only."""
    reasons: list[str] = []
    notes: list[str] = []
    gitpath = d / ".git"
    if gitpath.is_file():
        reasons.append("linked worktree: remove it with `git worktree remove`, not with this tool")
    else:
        try:
            st = git(d, "status", "--porcelain")
            if st.returncode != 0:
                reasons.append("git status failed: " + (st.stderr.strip()[:120] or str(st.returncode)))
            elif st.stdout.strip():
                lines = st.stdout.strip().splitlines()
                reasons.append(f"dirty tree: {len(lines)} path(s), first `{lines[0][:90]}`")
            ig = git(d, "ls-files", "--others", "--ignored", "--exclude-standard", "--directory")
            if ig.returncode != 0:
                reasons.append("could not list ignored files: " + (ig.stderr.strip()[:100] or str(ig.returncode)))
            else:
                ignored = [l for l in ig.stdout.splitlines() if l]
                kept = [l for l in ignored if not is_regenerable(l)]
                if kept:
                    reasons.append(f"ignored non-cache path(s), possibly the only copy: {len(kept)} (" + ", ".join(f"`{k}`" for k in kept[:4]) + (", ..." if len(kept) > 4 else "") + ")")
                if len(ignored) > len(kept):
                    notes.append(f"{len(ignored) - len(kept)} regenerable cache entr{'y' if len(ignored) - len(kept) == 1 else 'ies'} ignored")
            if git(d, "rev-parse", "--verify", "--quiet", "refs/stash").returncode == 0:
                reasons.append("stash present")
            shas: dict[str, str] = {}
            head = git(d, "rev-parse", "--verify", "--quiet", "HEAD^{commit}")
            if head.returncode == 0:
                shas[head.stdout.strip()] = "HEAD"
            refs = git(d, "for-each-ref", "--format=%(objectname) %(refname)", "refs/heads", "refs/tags")
            for line in refs.stdout.splitlines():
                sha, _, ref = line.partition(" ")
                shas.setdefault(sha, ref)
            if not shas:
                reasons.append("no readable commit to compare with main")
            for sha, ref in shas.items():
                if git(repo, "cat-file", "-e", f"{sha}^{{commit}}").returncode != 0:
                    reasons.append(f"{ref} {sha[:12]} is unknown to the main repository (unpublished commit)")
                elif git(repo, "merge-base", "--is-ancestor", sha, main_sha).returncode != 0:
                    reasons.append(f"{ref} {sha[:12]} is not contained in main")
        except subprocess.TimeoutExpired:
            reasons.append("a git command timed out")
    return reasons, notes


def examine(d: Path, repo: Path, main_sha: str, older_days: float, now: float, size: bool = True) -> dict:
    """{'verdict': REMOVABLE|KEEP, 'reasons': [...], 'freed': int|None, 'shared': int|None, 'age_days': float, 'notes': [...]}. Read-only."""
    reasons: list[str] = []
    notes: list[str] = []
    gitpath = d / ".git"
    age = (now - max([newest_mtime(d)] + ([] if os.path.lexists(gitpath) else [newest_mtime(c) for c in nested_clones(d)]))) / 86400
    if age < older_days:
        reasons.append(f"touched {age:.1f} days ago (< {older_days:g})")
    holders = process_holders(d)
    if holders:
        reasons.append("in use by process " + ", ".join(holders[:4]))
    if os.path.lexists(gitpath):
        found, noted = git_checks(d, repo, main_sha)
        reasons += found
        notes += noted
    elif not d.name.startswith(SCRATCH_NAMES):
        inner = nested_clones(d)
        if not inner:
            reasons.append("not a git clone: nothing to verify it against")
        for clone in inner:
            found, noted = git_checks(clone, repo, main_sha)
            reasons += [f"{clone.name}: {r}" for r in found]
            notes += [f"{clone.name}: {n}" for n in noted]
        if inner:
            try:
                beside = sorted(e.name for e in os.scandir(d) if Path(e.path) not in inner)
            except OSError as exc:
                beside = [f"unreadable ({exc.strerror})"]
            if beside:
                reasons.append(f"holds {len(beside)} entr{'y' if len(beside) == 1 else 'ies'} beside the clone(s), possibly the only copy: " + ", ".join(f"`{n}`" for n in beside[:4]) + (", ..." if len(beside) > 4 else ""))
    freed = shared = None
    if size:
        freed, shared = disk_sizes(d)
    return {"verdict": "KEEP" if reasons else "REMOVABLE", "reasons": reasons, "freed": freed, "shared": shared, "age_days": age, "notes": notes}


def mb(n: int | None) -> str:
    return "-" if n is None else f"{n / 1e6:,.0f}"


def report(tmp: Path, repo: Path, main_ref: str, older_days: float, size: bool) -> tuple[list[tuple[Path, dict]], str | None]:
    main_sha = resolve_main(repo, main_ref)
    if not main_sha:
        print(f"REFUSED: main ref {main_ref!r} does not resolve in {repo}; nothing can be compared. Fetch it or pass --main-ref.", file=sys.stderr)
        return [], None
    now = time.time()
    rows = [(d, examine(d, repo, main_sha, older_days, now, size)) for d in candidates(tmp)]
    rows.sort(key=lambda r: (r[1]["verdict"] != "REMOVABLE", -(r[1]["freed"] or 0), r[0].name))
    return rows, main_sha


def refuse_reason(arg: str, tmp: Path) -> str | None:
    if any(c in arg for c in "*?[]") or ".." in Path(arg).parts:
        return "a glob or a `..` is never accepted: name each folder exactly"
    p = Path(arg)
    if not p.is_absolute() or p.is_symlink() or not p.is_dir():
        return "not an absolute path to a plain directory"
    if p.resolve().parent != tmp.resolve() or p.name.startswith("claude-") or p.resolve() == tmp.resolve():
        return f"not a direct child of {tmp} (and never claude-*)"
    return None


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--tmp-root", default=os.environ.get("TMPDIR", "/tmp"))
    ap.add_argument("--repo", default=str(ROOT), help="the repository whose main ref the clones are compared with")
    ap.add_argument("--main-ref", default="development/main")
    ap.add_argument("--older-than", type=float, default=1.0, metavar="DAYS")
    ap.add_argument("--no-size", action="store_true", help="skip the (slow) hard-link-aware size walk")
    ap.add_argument("--min-mb", type=float, default=5.0, help="do not list folders that would free less than this (default 5); they are counted in the last line")
    ap.add_argument("--all-rows", action="store_true", help="also list the folders that have no .git (collapsed into one line by default)")
    ap.add_argument("--remove", nargs="+", metavar="DIR", help="remove exactly these folders, each only if it is REMOVABLE right now")
    ap.add_argument("--dry-run", action="store_true", help="with --remove: say what would go, delete nothing")
    a = ap.parse_args(argv)
    tmp, repo = Path(a.tmp_root), Path(a.repo)

    if a.remove:
        main_sha = resolve_main(repo, a.main_ref)
        if not main_sha:
            print(f"REFUSED: main ref {a.main_ref!r} does not resolve in {repo}.", file=sys.stderr)
            return 1
        rc, now = 0, time.time()
        for arg in a.remove:
            bad = refuse_reason(arg, tmp)
            if bad:
                print(f"REFUSED {arg}: {bad}", file=sys.stderr)
                rc = 1
                continue
            d = Path(arg)
            r = examine(d, repo, main_sha, a.older_than, now, size=True)
            if r["verdict"] != "REMOVABLE":
                print(f"REFUSED {arg}: " + "; ".join(r["reasons"]), file=sys.stderr)
                rc = 1
                continue
            if a.dry_run:
                print(f"WOULD REMOVE {arg}  frees {mb(r['freed'])} MB")
                continue
            shutil.rmtree(d)
            print(f"REMOVED {arg}  freed about {mb(r['freed'])} MB")
        return rc

    rows, main_sha = report(tmp, repo, a.main_ref, a.older_than, not a.no_size)
    if main_sha is None:
        return 1
    print(f"main ref {a.main_ref} = {main_sha[:12]}; temp root {tmp}; older than {a.older_than:g} day(s); sizes in MB of allocated blocks; nothing is deleted by a report")
    print(f"{'verdict':<10}{'freed':>8}{'shared':>9}{'days':>6}  folder / reasons")
    nongit = [(d, r) for d, r in rows if any("not a git clone" in x for x in r["reasons"]) and not a.all_rows]
    small = [row for row in rows if row not in nongit and not a.no_size and (row[1]["freed"] or 0) < a.min_mb * 1e6 and not a.all_rows]
    shown = [row for row in rows if row not in nongit and row not in small]
    for d, r in shown:
        extra = ("  " + "; ".join(r["reasons"])) if r["reasons"] else ""
        notes = ("  [" + "; ".join(r["notes"]) + "]") if r["notes"] else ""
        print(f"{r['verdict']:<10}{mb(r['freed']):>8}{mb(r['shared']):>9}{r['age_days']:>6.1f}  {d}{extra}{notes}")
    if nongit:
        print(f"  ... {len(nongit)} folder(s) with no .git are not listed (never removable by this tool unless it is one of the scratch names in the help; --all-rows lists them), "
              f"holding {mb(sum(r['freed'] or 0 for _, r in nongit))} MB that only their owner can judge; the biggest:")
        for d, r in sorted(nongit, key=lambda x: -(x[1]["freed"] or 0))[:8]:
            print(f"    {mb(r['freed']):>8} MB  {r['age_days']:>5.1f} d  {d}")
    if small:
        print(f"  ... {len(small)} folder(s) each freeing under {a.min_mb:g} MB are not listed (together {mb(sum(r['freed'] or 0 for _, r in small))} MB; {sum(1 for _, r in small if r['verdict'] == 'REMOVABLE')} of them REMOVABLE; --min-mb 0 lists them)")
    rem = [r for _, r in rows if r["verdict"] == "REMOVABLE"]
    print(f"{len(rows)} candidate(s); {len(rem)} REMOVABLE, which would free about {mb(sum(r['freed'] or 0 for r in rem))} MB; "
          f"{len(rows) - len(rem)} KEEP. Remove with: tmp_clone_report.py --remove <dir> [<dir> ...]")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
