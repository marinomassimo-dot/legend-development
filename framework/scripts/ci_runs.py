#!/usr/bin/env python3
"""What the CI and publication workflows concluded for a commit — read from the public API, with a mandatory deadline when waiting.

A mandate record that says COMPLETE while "CI pending" is written in its prose describes the moment it was written, and nobody can tell afterwards whether
the run ever ended. The supported way to hold such a wait is a BLOCKED step whose blocker names the run and whose unblock is its conclusion
(cross_session_transport.md section 12); this tool reads the conclusion so that the step can be closed with evidence (run number, workflow, SHA, conclusion).

    python3 framework/scripts/ci_runs.py status <sha>                 # one line per workflow run on that commit
    python3 framework/scripts/ci_runs.py times <sha>                  # the slowest suites a concluded gate run published (public annotation; exit 3 = none published)
    python3 framework/scripts/ci_runs.py status <sha>                 # a red gate run also lists its failing suites and tests, read from the public annotations (no login)
    python3 framework/scripts/ci_runs.py wait <sha> --timeout 1800    # progressive polling (2, 4, then 8 minutes), ONE shared read of the latest runs serves every commit and every waiter on the machine; exit 0 all runs concluded success
    python3 framework/scripts/ci_runs.py queue                        # the open runs of the public release gate (in progress or queued): position, run, sha, branch, age; the count, the age of the oldest and the conclusions of the last 100 runs, so a change to the gate's concurrency can be measured before and after; ONE request, exit 0 whenever the API was read, 2 when it was not (a rate limit is printed with its reset)

Exit codes: 0 every run on the commit concluded success · 1 a run concluded with anything else · 3 no run seen for the commit · 124 the deadline passed with a run
still in progress (or none yet) · 2 invalid invocation or the API unreadable. No token is used (the repository is public; the unauthenticated limit is 60 requests an
hour, so `wait` polls every two minutes, shares one answer per commit with every other waiter on the machine (a cache under $TMPDIR, five seconds shorter than the interval) and, when the limit is reached, sleeps until the reset the API announces, inside its deadline). `no run seen` is not `success`: a push whose workflow has not started yet reads exit 3, and `wait` keeps polling it.
"""
from __future__ import annotations

import argparse
import calendar
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


def fetch_json(url: str):
    with urllib.request.urlopen(urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"}), timeout=30) as r:
        return json.load(r)


def failing_tests(run_id: int, repo: str, fetch=fetch_json) -> list[str]:
    """2026-11-21 (HE): the names of the failing suites and tests of one red run, WITHOUT a login. The log needs one (403) and the artifact needs one, but the Regression-tests step of the workflow repeats its failing
    suites and assertion lines as annotations titled `release regression`, and the check-runs API serves annotations to anyone (IT30). Two requests, read-only: the jobs of the run, then the annotations of each failed job.
    Each line is cut at 170 characters (an assertion line can carry a whole page). The workflow caps the list at 40 lines, so a list that long may be incomplete."""
    out: list[str] = []
    for job in fetch(f"https://api.github.com/repos/{repo}/actions/runs/{run_id}/jobs").get("jobs", []):
        if job.get("conclusion") != "failure":
            continue
        for note in fetch(f"https://api.github.com/repos/{repo}/check-runs/{job['id']}/annotations?per_page=100"):
            if note.get("title") == "release regression":
                out.append(" ".join(str(note.get("message", "")).split())[:170])
    return out


def suite_times(runs: list[dict], repo: str, fetch=fetch_json) -> list[str]:
    """The per-suite times the regression runner published as a `suite time` annotation on a concluded gate run (two requests per run).
    Empty when no concluded gate run carries one: a run from before 2026-11-25, or one that never reached the runner's last line."""
    lines: list[str] = []
    for r in runs:
        if r.get("name") != GATE or r.get("status") != "completed" or not r.get("id"):
            continue
        for job in fetch(f"https://api.github.com/repos/{repo}/actions/runs/{r['id']}/jobs").get("jobs", []):
            for note in fetch(f"https://api.github.com/repos/{repo}/check-runs/{job['id']}/annotations?per_page=100"):
                if note.get("title") == "suite time":
                    lines.append(f"#{r['run_number']} {r.get('conclusion')} ({r['head_sha'][:8]})")
                    lines += [f"  {part}" for part in str(note.get("message", "")).split("; ")]
    return lines


def failure_lines(runs: list[dict], repo: str, fetch=fetch_json) -> list[str]:
    """Lines to print under the status of a commit whose gate run failed. Never changes a verdict: when the annotations cannot be read the line says so."""
    lines: list[str] = []
    for r in runs:
        if r.get("name") != "Public release gate" or r.get("status") != "completed" or r.get("conclusion") != "failure" or not r.get("id"):
            continue
        try:
            names = failing_tests(r["id"], repo, fetch)
        except Exception as exc:  # network or rate limit: a missing detail is not a verdict
            lines.append(f"  #{r['run_number']}: failing tests not read ({exc.__class__.__name__}: {exc})")
            continue
        lines += [f"  #{r['run_number']} {n}" for n in names] or [f"  #{r['run_number']}: no 'release regression' annotation (the failing step may not be the regression step)"]
    return lines


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


OPEN_STATES = ("in_progress", "queued", "waiting", "pending", "requested")
GATE = "Public release gate"


def parse_time(value: str | None) -> float | None:
    """An API timestamp (`2026-11-24T22:01:05Z`) as epoch seconds, or None."""
    if not value:
        return None
    try:
        return float(calendar.timegm(time.strptime(value, "%Y-%m-%dT%H:%M:%SZ")))
    except ValueError:
        return None


def human_age(seconds: float | None) -> str:
    if seconds is None:
        return "unknown"
    minutes = int(max(seconds, 0) // 60)
    return f"{minutes // 60}h{minutes % 60:02d}m" if minutes >= 60 else f"{minutes}m"


def queue_view(runs: list[dict], now: float, workflow: str = GATE) -> dict:
    """The open runs of one workflow from ONE list of runs, oldest first (position 1 is the oldest), and what the list says about how runs end.
    A run is open while it is in progress, queued, waiting or pending; its age runs from `created_at` (the push), because a queued run waits too. `window` counts the
    conclusions of the completed runs of that workflow in the same list (at most the latest hundred), so a `cancelled` count that appears after a concurrency change can be read."""
    mine = [r for r in runs if r.get("name") == workflow]
    opened = sorted((r for r in mine if r.get("status") in OPEN_STATES), key=lambda r: (parse_time(r.get("created_at")) or now, r.get("run_number", 0)))
    rows = [{"position": n, "run": r.get("run_number"), "sha": str(r.get("head_sha", ""))[:8], "branch": r.get("head_branch"), "event": r.get("event"),
             "status": r.get("status"), "age_seconds": (now - parse_time(r.get("created_at"))) if parse_time(r.get("created_at")) is not None else None}
            for n, r in enumerate(opened, 1)]
    window: dict[str, int] = {}
    for r in mine:
        if r.get("status") == "completed":
            window[r.get("conclusion") or "none"] = window.get(r.get("conclusion") or "none", 0) + 1
    times = [parse_time(r.get("created_at")) for r in mine]
    times = [x for x in times if x is not None]
    return {"workflow": workflow, "open": len(rows), "in_progress": sum(1 for r in rows if r["status"] == "in_progress"),
            "queued": sum(1 for r in rows if r["status"] != "in_progress"),
            "oldest_age_seconds": rows[0]["age_seconds"] if rows else None, "rows": rows, "window": window,
            "window_runs": len(mine), "window_span_seconds": (now - min(times)) if times else None}


def render_queue(view: dict) -> list[str]:
    head = f"QUEUE {view['workflow']}: {view['open']} open ({view['in_progress']} in progress, {view['queued']} queued)"
    lines = [head + (f", oldest {human_age(view['oldest_age_seconds'])}" if view["rows"] else "")]
    lines += [f"  {r['position']:>2}. #{r['run']} {r['sha']} {r['branch']} {r['event']} {r['status']} age {human_age(r['age_seconds'])}" for r in view["rows"]]
    done = ", ".join(f"{k} {v}" for k, v in sorted(view["window"].items())) or "none"
    lines.append(f"  window: {view['window_runs']} runs of this workflow over {human_age(view['window_span_seconds'])} (one list of at most 100 runs of every workflow); completed: {done}")
    return lines


def verdict(runs: list[dict]) -> tuple[int, list[str]]:
    """(exit code, lines) from the workflow_runs of one commit."""
    if not runs:
        return 3, ["no workflow run seen for this commit"]
    lines = [f"#{r['run_number']} {r['name']}: {r['status']}" + (f" {r['conclusion']}" if r.get("conclusion") else "") + f" ({r['head_sha'][:8]})" for r in sorted(runs, key=lambda r: r["run_number"])]
    if any(r["status"] != "completed" for r in runs):
        return 124, lines
    return (0 if all(r["conclusion"] == "success" for r in runs) else 1), lines


def red_streak(runs: list[dict], branch: str = "main") -> dict:
    """What the latest completed runs of the publication gate on one branch say, from ONE list of runs (no extra request): the newest completed run, and when it is red, the oldest run of the unbroken red
    streak that ends at it. 2026-11-20 (ADV-108): the regression step was red from #1513 (e4275e32) and was found about seven hours and some forty commits later, because the local publication gate does not run
    the regression suites and nobody read CI. A run still in progress is skipped, never read as green or red. Returns {} when no completed run of that branch is in the list."""
    done = sorted((r for r in runs if r.get("status") == "completed" and r.get("head_branch") == branch and r.get("name") == "Public release gate"), key=lambda r: r["run_number"], reverse=True)
    if not done:
        return {}
    latest = done[0]
    out = {"latest": latest["run_number"], "latest_sha": latest["head_sha"][:8], "conclusion": latest.get("conclusion"), "red": latest.get("conclusion") != "success"}
    if out["red"]:
        first, n = latest, 1
        for r in done[1:]:
            if r.get("conclusion") == "success":
                break
            first, n = r, n + 1
        out.update(first_red=first["run_number"], first_red_sha=first["head_sha"][:8], streak=n)
    return out


def queue_command(a) -> int:
    """`queue`: one request, no cache read (a queue is only worth reading fresh); the answer also feeds the per-commit cache like every other list read."""
    repo = slug(a.remote)
    try:
        recent = fetch_recent(repo)
    except urllib.error.HTTPError as exc:
        pause = reset_wait(exc.headers, time.time()) if exc.code in (403, 429) else None
        print(f"cannot read the API: {exc}" + (f" (rate limit; resets in {pause / 60:.0f} min)" if pause is not None else ""), file=sys.stderr)
        return 2
    except Exception as exc:  # network: say so, never read it as an empty queue
        print(f"cannot read the API: {exc}", file=sys.stderr)
        return 2
    now = time.time()
    write_recent(repo, recent, now)
    view = queue_view(recent, now, a.workflow)
    print(json.dumps(view, indent=2) if a.json else "\n".join(render_queue(view)))
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name in ("status", "wait", "times"):
        p = sub.add_parser(name)
        p.add_argument("sha")
        p.add_argument("--remote", default="development")
        if name == "wait":
            p.add_argument("--timeout", type=int, required=True)
    pq = sub.add_parser("queue", help="the open runs of the public release gate, with position, age and the conclusions of the last 100 runs")
    pq.add_argument("--remote", default="development")
    pq.add_argument("--workflow", default=GATE)
    pq.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    if a.cmd == "queue":
        return queue_command(a)
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
        if a.cmd == "times":
            try:
                lines = suite_times(runs, repo)
            except Exception as exc:  # network or rate limit: said, never read as "no times published"
                print(f"cannot read the annotations: {exc}", file=sys.stderr)
                return 2
            print("\n".join(lines) if lines else "no `suite time` annotation on a concluded gate run of this commit")
            return 0 if lines else 3
        code, lines = verdict(runs)
        if a.cmd == "status" or code in (0, 1) or time.time() >= end:
            if code == 1:
                lines = lines + failure_lines(runs, repo)
            print("\n".join(lines))
            return code if not (a.cmd == "wait" and code == 3) else 124
        time.sleep(min(interval(time.time() - started), max(1.0, end - time.time())))


if __name__ == "__main__":
    sys.exit(main())
