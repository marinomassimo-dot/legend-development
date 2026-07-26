#!/usr/bin/env python3
"""Read-only status monitor for optional exploratory MD screen runs."""

from __future__ import annotations

import argparse
import json
import platform
import subprocess
import time
from pathlib import Path


DEFAULT_ROOT = Path("md-output/helix-screen")


def process_running(pattern: str) -> bool | None:
    """Return process state when pgrep exists, otherwise None."""
    try:
        completed = subprocess.run(
            ["pgrep", "-qf", pattern],
            check=False,
            capture_output=True,
            text=True,
        )
    except FileNotFoundError:
        return None
    return completed.returncode == 0


def mac_power_state() -> dict[str, object]:
    if platform.system() != "Darwin":
        return {"available": False, "reason": "pmset is macOS-only"}
    try:
        completed = subprocess.run(
            ["pmset", "-g", "batt"],
            check=False,
            capture_output=True,
            text=True,
        )
    except FileNotFoundError:
        return {"available": False, "reason": "pmset unavailable"}
    if completed.returncode != 0:
        return {"available": False, "reason": "pmset failed"}
    text = completed.stdout
    source = "AC" if "AC Power" in text else "battery"
    percent = None
    for token in text.replace(";", " ").split():
        if token.endswith("%") and token[:-1].isdigit():
            percent = int(token[:-1])
            break
    return {"available": True, "source": source, "percent": percent}


def last_progress(state_file: Path) -> dict[str, object] | None:
    try:
        lines = [
            line
            for line in state_file.read_text(
                encoding="utf-8", errors="replace"
            ).splitlines()
            if line.strip()
        ]
    except OSError:
        return None
    if len(lines) < 2:
        return None
    header = lines[0].split("\t")
    values = lines[-1].split("\t")
    row = dict(zip(header, values))
    return {
        "step": row.get("#\"Step\"") or row.get("Step") or values[0],
        "speed": (
            row.get("Speed (ns/day)")
            or row.get("Speed")
            or (values[-1] if values else None)
        ),
    }


def inspect_run(directory: Path, now: float, stale_minutes: int) -> dict[str, object]:
    summary = directory / "summary.json"
    state = directory / "state.tsv"
    if summary.is_file():
        try:
            payload = json.loads(summary.read_text(encoding="utf-8"))
            status = "complete"
        except (OSError, json.JSONDecodeError):
            payload = None
            status = "invalid_summary"
        return {
            "run": directory.name,
            "status": status,
            "summary": payload,
        }
    if state.is_file():
        age_minutes = max(0.0, (now - state.stat().st_mtime) / 60)
        return {
            "run": directory.name,
            "status": "stalled" if age_minutes > stale_minutes else "running_or_recent",
            "last_update_minutes": round(age_minutes, 1),
            "progress": last_progress(state),
        }
    return {"run": directory.name, "status": "prepared_no_state"}


def inspect(root: Path, expected_runs: int, stale_minutes: int) -> dict[str, object]:
    now = time.time()
    directories = sorted(path for path in root.glob("*_seed*") if path.is_dir())
    runs = [inspect_run(path, now, stale_minutes) for path in directories]
    complete = sum(run["status"] == "complete" for run in runs)
    stalled = sum(run["status"] == "stalled" for run in runs)
    failures = []
    log = root / "run.log"
    if log.is_file():
        failures = [
            line
            for line in log.read_text(
                encoding="utf-8", errors="replace"
            ).splitlines()
            if "FAILED" in line
        ]
    worker = process_running("md_helix_screen.py")
    overall = "complete" if complete >= expected_runs else "incomplete"
    if failures:
        overall = "failed"
    elif stalled:
        overall = "stalled"
    elif worker:
        overall = "running"
    return {
        "status": "EXPLO",
        "root": str(root),
        "overall": overall,
        "expected_runs": expected_runs,
        "discovered_runs": len(runs),
        "complete_runs": complete,
        "failed_records": failures,
        "worker_process_running": worker,
        "power": mac_power_state(),
        "runs": runs,
    }


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    parser.add_argument("--expected-runs", type=int, default=12)
    parser.add_argument("--stale-minutes", type=int, default=40)
    parser.add_argument("--json", action="store_true")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    if args.expected_runs < 1 or args.stale_minutes < 1:
        raise SystemExit("--expected-runs and --stale-minutes must be positive")
    payload = inspect(args.root, args.expected_runs, args.stale_minutes)
    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        print(
            f"MD screen: {payload['overall']} — "
            f"{payload['complete_runs']}/{payload['expected_runs']} complete"
        )
        for run in payload["runs"]:
            suffix = ""
            if "last_update_minutes" in run:
                suffix = f" ({run['last_update_minutes']} min since update)"
            print(f"  {run['run']}: {run['status']}{suffix}")
        for failure in payload["failed_records"]:
            print(f"  failure: {failure}")
        power = payload["power"]
        if power.get("available") and power.get("source") == "battery":
            print(
                "  warning: battery power may reduce sustained accelerator "
                "throughput or interrupt a long run"
            )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
