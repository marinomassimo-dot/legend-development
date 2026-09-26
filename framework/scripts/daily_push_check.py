#!/usr/bin/env python3
"""Report local work absent from the development repository; never change a Git ref.

The report is a local observation, not proof that every actor's clone is published.
Install the hourly cron probe documented in framework/scripts/README.md; --scheduled
selects 19:45 Europe/Rome across daylight-saving changes.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from zoneinfo import ZoneInfo


DESTINATION = "github.com/marinomassimo-dot/legend-development"
ROME = ZoneInfo("Europe/Rome")


class CheckError(Exception):
    pass


def git(root: Path, *args: str, timeout: int = 20) -> str:
    env = dict(os.environ, GIT_TERMINAL_PROMPT="0")
    try:
        result = subprocess.run(["git", *args], cwd=root, env=env, text=True,
                                capture_output=True, timeout=timeout, check=False)
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise CheckError(f"git {' '.join(args)}: {exc}") from exc
    if result.returncode:
        raise CheckError(f"git {' '.join(args)}: {result.stderr.strip() or result.stdout.strip()}")
    return result.stdout.strip()


def is_development_url(url: str) -> bool:
    match = re.fullmatch(
        r"(?:git@github\.com:|ssh://git@github\.com/|https://github\.com/)"
        r"([^\s]+?)(?:\.git)?/?", url.strip(), re.IGNORECASE)
    return bool(match and f"github.com/{match.group(1).lower()}" == DESTINATION)


def development_remote(root: Path) -> str:
    matches = []
    for name in git(root, "remote").splitlines():
        if is_development_url(git(root, "remote", "get-url", "--push", name)):
            matches.append(name)
    if not matches:
        raise CheckError(f"no push remote names {DESTINATION}")
    return sorted(matches, key=lambda name: (name != "development", name != "origin", name))[0]


def remote_main(root: Path, remote: str) -> str:
    lines = git(root, "ls-remote", "--heads", remote, "main", timeout=30).splitlines()
    matches = [line.split()[0] for line in lines if line.endswith("refs/heads/main")]
    if len(matches) != 1 or not re.fullmatch(r"[0-9a-fA-F]{40,64}", matches[0]):
        raise CheckError(f"{remote}/main has no unique SHA")
    return matches[0]


def local_branches(root: Path, baseline: str) -> list[dict[str, object]]:
    # A remote SHA can be visible via ls-remote before this clone has its object.
    if not git(root, "cat-file", "-t", baseline) == "commit":
        raise CheckError("remote main SHA is not in the local object store; fetch and rerun")
    rows = []
    refs = git(root, "for-each-ref", "--format=%(refname:short)%09%(objectname)",
               "refs/heads")
    for line in refs.splitlines():
        name, sha = line.split("\t", 1)
        # Backup refs intentionally preserve older snapshots and are explicitly excluded
        # from development publication. They are not a daily landing task.
        if name.startswith("backup/"):
            continue
        count = int(git(root, "rev-list", "--count", f"{baseline}..{sha}"))
        if not count:
            continue
        # A cherry-picked patch can have a new commit ID while its content is already
        # on main. Counting IDs alone would warn forever about the old task branch.
        novel = sum(line.startswith("+") for line in git(root, "cherry", baseline, sha).splitlines())
        if novel:
            rows.append({"branch": name, "sha": sha,
                         "commits_absent_from_remote_main": count,
                         "novel_patches": novel})
    return rows


def dirty_worktrees(root: Path) -> tuple[list[str], list[str]]:
    """Separate owned branch work from detached scratch worktrees.

    Detached worktrees remain visible for inspection, but a test fixture left dirty
    under /tmp is not evidence that an actor has unpublished task work.
    """
    active, detached = [], []
    for block in git(root, "worktree", "list", "--porcelain").split("\n\n"):
        lines = block.splitlines()
        location = next((line[9:] for line in lines if line.startswith("worktree ")), None)
        if location is None:
            continue
        path = Path(location)
        if path.exists() and git(path, "status", "--porcelain", "--untracked-files=all"):
            (active if any(line.startswith("branch ") for line in lines) else detached).append(
                str(path))
    return active, detached


def report(root: Path, now: dt.datetime) -> dict[str, object]:
    root = Path(git(root, "rev-parse", "--show-toplevel"))
    result: dict[str, object] = {
        "checked_at": now.astimezone(dt.timezone.utc).isoformat(),
        "actor_to_notify": "orchestrator", "destination": DESTINATION,
        "repository": str(root), "status": "UNKNOWN", "unpublished": [],
        "dirty_worktrees": [], "detached_dirty_worktrees": [],
    }
    try:
        remote = development_remote(root)
        sha = remote_main(root, remote)
        result["remote"] = remote
        result["remote_main_sha"] = sha
        result["unpublished"] = local_branches(root, sha)
        result["dirty_worktrees"], result["detached_dirty_worktrees"] = dirty_worktrees(root)
        result["status"] = "UNPUBLISHED" if result["unpublished"] or result["dirty_worktrees"] else "CURRENT"
    except CheckError as exc:
        result["error"] = str(exc)
    return result


def state_path() -> Path:
    base = Path(os.environ.get("XDG_STATE_HOME", str(Path.home() / ".local/state")))
    return base / "legend" / "daily_push_check.json"


def scheduled_time(now: dt.datetime) -> bool:
    local = now.astimezone(ROME)
    return (local.hour, local.minute) == (19, 45)


def write_report(path: Path, result: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + f".{os.getpid()}.tmp")
    temporary.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
    os.replace(temporary, path)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--output", type=Path, default=state_path())
    parser.add_argument("--scheduled", action="store_true", help="run only at 19:45 Europe/Rome")
    args = parser.parse_args(argv)
    now = dt.datetime.now(dt.timezone.utc)
    if args.scheduled and not scheduled_time(now):
        return 0
    try:
        result = report(args.repo, now)
        write_report(args.output, result)
    except (CheckError, OSError) as exc:
        print(f"daily_push_check: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False))
    return 0 if result["status"] == "CURRENT" else 1


if __name__ == "__main__":
    raise SystemExit(main())
