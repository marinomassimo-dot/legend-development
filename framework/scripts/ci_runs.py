#!/usr/bin/env python3
"""What the CI and publication workflows concluded for a commit — read from the public API, with a mandatory deadline when waiting.

A mandate record that says COMPLETE while "CI pending" is written in its prose describes the moment it was written, and nobody can tell afterwards whether
the run ever ended. The supported way to hold such a wait is a BLOCKED step whose blocker names the run and whose unblock is its conclusion
(cross_session_transport.md section 12); this tool reads the conclusion so that the step can be closed with evidence (run number, workflow, SHA, conclusion).

    python3 framework/scripts/ci_runs.py status <sha>                 # one line per workflow run on that commit
    python3 framework/scripts/ci_runs.py wait <sha> --timeout 1800    # progressive polling (2, 4, then 8 minutes), ONE shared read of the latest runs serves every commit and every waiter on the machine; exit 0 all runs concluded success

Exit codes: 0 every run on the commit concluded success · 1 a run concluded with anything else · 3 no run seen for the commit · 124 the deadline passed with a run
still in progress (or none yet) · 2 invalid invocation or the API unreadable. No token is used (the repository is public; the unauthenticated limit is 60 requests an
hour, so `wait` polls every two minutes, shares one answer per commit with every other waiter on the machine (a cache under $TMPDIR, five seconds shorter than the interval) and, when the limit is reached, sleeps until the reset the API announces, inside its deadline). `no run seen` is not `success`: a push whose workflow has not started yet reads exit 3, and `wait` keeps polling it.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]


def slug(remote: str = "development", repo: Path = REPO) -> str:
    """owner/name of the GitHub repository behind `remote` (a clone of a local path has no GitHub remote: say so, do not guess)."""
    for name in dict.fromkeys((remote, "origin")):
        url = subprocess.run(["git", "-C", str(repo), "remote", "get-url", name], capture_output=True, text=True).stdout.strip()
        m = re.search(r"github\.com[:/]([^/]+/[^/.]+?)(?:\.git)?$", url)
        if m:
            return m.group(1)
    raise SystemExit(f"no GitHub repository behind remote {remote!r} or 'origin' in {repo}")


def reset_wait(headers, now: float) -> float | None:
    """Seconds to wait before the unauthenticated rate limit (60 requests an hour) opens again, from the `X-RateLimit-Reset` header; None when it is not a rate-limit answer."""
    try:
        if str(headers.get("X-RateLimit-Remaining", "")) != "0":
            return None
        return max(0.0, float(headers.get("X-RateLimit-Reset")) - now) + 2
    except (TypeError, ValueError):
        return None


def fetch_runs(sha: str, repo: str) -> list[dict]:
    url = f"https://api.github.com/repos/{repo}/actions/runs?head_sha={sha}&per_page=50"
    with urllib.request.urlopen(urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"}), timeout=30) as r:
        return json.load(r)["workflow_runs"]


def fetch_recent(repo: str) -> list[dict]:
    """The latest runs of every commit in ONE request (100 at most): with several commits in flight, one read per commit used the whole unauthenticated hour (60 requests); one read of the list serves them all."""
    url = f"https://api.github.com/repos/{repo}/actions/runs?per_page=100"
    with urllib.request.urlopen(urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"}), timeout=30) as r:
        return json.load(r)["workflow_runs"]


def interval(waited: float) -> float:
    """Progressive attention: a publication run lasts about an hour, so the first minutes are polled every two minutes, then every four, then every eight. Verdicts of other commits ride on the same read."""
    return POLL if waited < 600 else 2 * POLL if waited < 2400 else 4 * POLL


POLL = 120   # seconds between reads: a publication run lasts about an hour, so one-minute polling alone used the whole unauthenticated hour (60 requests)


def cache_dir() -> Path:
    return Path(os.environ.get("TMPDIR") or "/tmp") / f"legend-ci-runs-{os.getuid()}"


def read_shared(sha: str, repo: str, ttl: float, now: float):
    """One read of the API serves every waiter on this machine: a recent answer for the same repository and commit is reused, and a declared rate-limit
    pause is honoured by all of them without another request. Returns ('runs', list) | ('pause', seconds) | None (nothing fresh: ask the API)."""
    d = cache_dir()
    try:
        until = float(json.loads((d / "ratelimit.json").read_text())["until"])
        if until > now:
            return "pause", until - now
    except (OSError, ValueError, KeyError):
        pass
    try:
        got = json.loads((d / f"{repo.replace('/', '_')}_{sha}.json").read_text())
        done = bool(got["runs"]) and all(r.get("status") == "completed" for r in got["runs"])
        if done or now - float(got["at"]) < ttl:      # a concluded run never changes: its verdict is read from the file for good, with no request
            return "runs", got["runs"]
    except (OSError, ValueError, KeyError):
        pass
    return None


def write_shared(sha: str, repo: str, runs: list[dict] | None, now: float, pause: float | None = None) -> None:
    d = cache_dir()
    try:
        d.mkdir(mode=0o700, exist_ok=True)
        if pause is not None:
            (d / "ratelimit.json").write_text(json.dumps({"until": now + pause}))
        elif runs is not None:
            (d / f"{repo.replace('/', '_')}_{sha}.json").write_text(json.dumps({"at": now, "runs": runs}))
    except OSError:
        pass        # a cache that cannot be written only costs a request


def read_stale(sha: str, repo: str):
    """The last answer for this commit whatever its age, with its age in seconds, or None: what `status` shows while a declared rate-limit pause forbids a request (said as old, never as current)."""
    try:
        got = json.loads((cache_dir() / f"{repo.replace('/', '_')}_{sha}.json").read_text())
        return got["runs"], time.time() - float(got["at"])
    except (OSError, ValueError, KeyError):
        return None


def write_recent(repo: str, recent: list[dict], now: float) -> None:
    """One list read feeds the per-commit entries of every commit it holds, so a waiter on any of them finds its answer (and a concluded one stays)."""
    by: dict[str, list[dict]] = {}
    for r in recent:
        by.setdefault(r.get("head_sha", ""), []).append(r)
    for sha, runs in by.items():
        if re.fullmatch(r"[0-9a-f]{40}", sha):
            write_shared(sha, repo, runs, now)


def verdict(runs: list[dict]) -> tuple[int, list[str]]:
    """(exit code, lines) from the workflow_runs of one commit."""
    if not runs:
        return 3, ["no workflow run seen for this commit"]
    lines = [f"#{r['run_number']} {r['name']}: {r['status']}" + (f" {r['conclusion']}" if r.get("conclusion") else "") + f" ({r['head_sha'][:8]})" for r in sorted(runs, key=lambda r: r["run_number"])]
    if any(r["status"] != "completed" for r in runs):
        return 124, lines
    return (0 if all(r["conclusion"] == "success" for r in runs) else 1), lines


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name in ("status", "wait"):
        p = sub.add_parser(name)
        p.add_argument("sha")
        p.add_argument("--remote", default="development")
        if name == "wait":
            p.add_argument("--timeout", type=int, required=True)
    a = ap.parse_args(argv)
    if not re.fullmatch(r"[0-9a-f]{7,40}", a.sha):
        print("a commit SHA (7-40 hex digits) is required", file=sys.stderr)
        return 2
    if len(a.sha) < 40:     # the API matches the full SHA only
        full = subprocess.run(["git", "-C", str(REPO), "rev-parse", "--verify", "-q", a.sha + "^{commit}"], capture_output=True, text=True).stdout.strip()
        if not full:
            print(f"{a.sha} is not a commit of this repository: give the full 40-digit SHA", file=sys.stderr)
            return 2
        a.sha = full
    repo = slug(a.remote)
    started = time.time()
    end = started + (a.timeout if a.cmd == "wait" else 0)
    while True:
        fresh = read_shared(a.sha, repo, POLL - 5 if a.cmd == "wait" else 30, time.time())
        try:
            if fresh and fresh[0] == "pause":
                raise urllib.error.HTTPError("", 403, "rate limit declared by another reader", {"X-RateLimit-Remaining": "0", "X-RateLimit-Reset": str(time.time() + fresh[1] - 2)}, None)
            if fresh:
                runs = fresh[1]
            else:
                recent = fetch_recent(repo)                                  # one request for every commit in flight
                write_recent(repo, recent, time.time())
                runs = [r for r in recent if r.get("head_sha") == a.sha]
                if not runs:                                                 # older than the latest hundred, or not yet seen: ask for this commit alone
                    runs = fetch_runs(a.sha, repo)
                    write_shared(a.sha, repo, runs, time.time())
        except urllib.error.HTTPError as exc:
            pause = reset_wait(exc.headers, time.time()) if exc.code in (403, 429) else None
            if pause is not None:
                write_shared(a.sha, repo, None, time.time(), pause)
            if pause is not None and a.cmd == "wait" and time.time() + pause < end:
                time.sleep(pause)               # the limit is a pause, not a verdict: wait for the reset inside the deadline
                continue
            if pause is not None and a.cmd == "status":
                old = read_stale(a.sha, repo)
                if old:                                                        # the pause forbids a request; the last answer is shown as OLD, with its age, never as current
                    code, lines = verdict(old[0])
                    print("\n".join(lines) + f"\n(last answer, {old[1] / 60:.0f} min old; rate limit pause, resets in {pause / 60:.0f} min: not current)")
                    return code
            print(f"cannot read the API: {exc}" + (f" (rate limit; resets in {pause / 60:.0f} min)" if pause is not None else ""), file=sys.stderr)
            return 124 if pause is not None and a.cmd == "wait" else 2
        except Exception as exc:  # network: say so, never read it as "no run"
            print(f"cannot read the API: {exc}", file=sys.stderr)
            return 2
        code, lines = verdict(runs)
        if a.cmd == "status" or code in (0, 1) or time.time() >= end:
            print("\n".join(lines))
            return code if not (a.cmd == "wait" and code == 3) else 124
        time.sleep(min(interval(time.time() - started), max(1.0, end - time.time())))


if __name__ == "__main__":
    sys.exit(main())
