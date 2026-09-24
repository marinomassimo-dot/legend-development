#!/usr/bin/env python3
"""Wait for a process or a file by IDENTITY, with a mandatory deadline — never by name.

WHY THIS EXISTS
---------------
`pgrep -f <job>` matches the full command line of every process, including the one asking.
A waiter whose own command line names its target — an `until` loop, a `watch`, a wrapper —
answers "is the target alive?" with "yes, I am" and can never finish. It happened twice:
on 2026-09-22 two waiters polled `pgrep -f run_release_regressions` for 2h08m and 2h04m, and
on 2026-09-24 another polled `pgrep -f "while read t"` for 2h53m, each waiting for itself.
The first repair lived in `disease-models/wwox/analysis/scripts/md_status.py`, one analysis
tool's private copy; this module is now the ONE home of that logic and `md_status` imports it.

    python3 framework/scripts/process_wait.py --pid 12345 --timeout 900
    python3 framework/scripts/process_wait.py --pid-file run.pid --timeout 900
    python3 framework/scripts/process_wait.py --file out/DONE --timeout 900
    python3 framework/scripts/process_wait.py --identity 12345   # prints "12345:<start>"

Identity, in order of strength:
  - `PID:START` (from `--identity`, or a pid file holding it): the kernel start time pins one
    incarnation, so a recycled PID is a different process and the wait completes;
  - `PID` alone: that process, whatever it is called;
  - `--file`: a completion file the job itself writes last.
A zombie (exited, not yet reaped by its parent) counts as finished. Waiting on this process
or one of its ancestors is refused: it could only end by timeout.

`--timeout` is required: every wait ends. Prefer the runtime's own completion notification
when there is one; this is for when there is not.

Exit codes: 0 the target finished (or the file exists) · 124 the deadline passed first ·
2 invalid invocation or identity (malformed PID, unreadable pid file, self-wait).
"""
from __future__ import annotations

import argparse
import os
import subprocess
import sys
import time
from pathlib import Path

TIMED_OUT = 124
INVALID = 2


def _stat_fields(pid: int) -> list[str] | None:
    """Fields of /proc/<pid>/stat after the command name, or None where /proc cannot say."""
    try:
        raw = Path(f"/proc/{pid}/stat").read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None
    # The command name is parenthesised and may itself contain spaces or parentheses.
    return raw[raw.rfind(")") + 2:].split()


def start_ticks(pid: int) -> int | None:
    """Kernel start time of `pid` (clock ticks since boot), or None where unknowable."""
    fields = _stat_fields(pid)
    try:
        return int(fields[19]) if fields else None   # field 22 of stat; 20th after the name
    except (IndexError, ValueError):
        return None


def parent_of(pid: int) -> int | None:
    """Parent PID via /proc, falling back to ps. None when unknowable."""
    fields = _stat_fields(pid)
    if fields:
        try:
            return int(fields[1])
        except (IndexError, ValueError):
            pass
    try:
        completed = subprocess.run(["ps", "-o", "ppid=", "-p", str(pid)],
                                   check=False, capture_output=True, text=True)
    except OSError:
        return None
    value = completed.stdout.strip()
    return int(value) if value.isdigit() else None


def self_and_ancestors() -> set[int]:
    """PIDs that must never be counted as the target: this process and every ancestor."""
    pids: set[int] = set()
    pid: int | None = os.getpid()
    while pid and pid > 0 and pid not in pids:
        pids.add(pid)
        pid = parent_of(pid)
    return pids


def pid_alive(pid: int, start: int | None = None) -> bool:
    """Liveness of one specific process (and incarnation, when `start` is given)."""
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        pass                      # it exists; we may not signal it
    except OSError:
        return False
    fields = _stat_fields(pid)
    if fields and fields[0] == "Z":
        return False              # exited; only the parent's reap is outstanding
    if start is not None and start_ticks(pid) not in (None, start):
        return False              # the PID was recycled: that incarnation is gone
    return True


def parse_identity(text: str) -> tuple[int, int | None]:
    """`PID` or `PID:START` → (pid, start). Anything else raises ValueError."""
    head, sep, tail = text.strip().partition(":")
    if not head.isdigit() or int(head) <= 0 or (sep and not tail.isdigit()):
        raise ValueError(f"not a process identity: {text.strip()!r}")
    return int(head), (int(tail) if tail else None)


def process_running(pattern: str, pid_file: Path | str | None = None) -> bool | None:
    """Worker state, preferring identity over textual matching.

    A recorded PID is authoritative. The `pgrep` fallback is DISCOVERY for runs started
    outside the caller, never identity, and it excludes this process and its ancestors so a
    pattern cannot match the asker. None means pgrep is unavailable here.
    """
    if pid_file is not None:
        try:
            pid, start = parse_identity(Path(pid_file).read_text(encoding="utf-8"))
        except (OSError, ValueError):
            pass
        else:
            return pid_alive(pid, start)
    try:
        completed = subprocess.run(["pgrep", "-f", pattern],
                                   check=False, capture_output=True, text=True)
    except FileNotFoundError:
        return None
    matched = {int(token) for token in completed.stdout.split() if token.isdigit()}
    return bool(matched - self_and_ancestors())


def wait(done, timeout: float, interval: float = 1.0) -> bool:
    """Poll `done()` until it is true or `timeout` seconds pass. True means done."""
    deadline = time.monotonic() + timeout
    while True:
        if done():
            return True
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            return False
        time.sleep(min(interval, remaining))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Wait for a process or a file by identity, with a mandatory deadline.")
    target = parser.add_mutually_exclusive_group(required=True)
    target.add_argument("--pid", help="PID or PID:START of the process to wait for")
    target.add_argument("--pid-file", help="file holding PID or PID:START")
    target.add_argument("--file", help="completion file the job writes last")
    target.add_argument("--identity", metavar="PID",
                        help="print PID:START for a live process, to record in a pid file")
    parser.add_argument("--timeout", type=float, help="seconds; required for every wait")
    parser.add_argument("--interval", type=float, default=1.0)
    args = parser.parse_args(argv)

    if args.identity is not None:
        try:
            pid, _ = parse_identity(args.identity)
        except ValueError as error:
            print(f"INVALID: {error}", file=sys.stderr)
            return INVALID
        start = start_ticks(pid) if pid_alive(pid) else None
        if start is None:
            print(f"INVALID: no live process {pid} with a readable start time", file=sys.stderr)
            return INVALID
        print(f"{pid}:{start}")
        return 0

    if args.timeout is None or args.timeout <= 0:
        print("INVALID: --timeout is required and must be positive; every wait ends",
              file=sys.stderr)
        return INVALID

    if args.file is not None:
        path = Path(args.file)
        done = path.exists
        label = f"file {path}"
    else:
        try:
            text = args.pid if args.pid is not None else Path(args.pid_file).read_text(
                encoding="utf-8")
            pid, start = parse_identity(text)
        except (OSError, ValueError) as error:
            print(f"INVALID: {error}", file=sys.stderr)
            return INVALID
        if pid in self_and_ancestors():
            print(f"INVALID: {pid} is this waiter or one of its ancestors; it could only "
                  "end by timeout", file=sys.stderr)
            return INVALID
        done = lambda: not pid_alive(pid, start)  # noqa: E731
        label = f"process {pid}" + (f":{start}" if start is not None else "")

    if wait(done, args.timeout, args.interval):
        print(f"DONE: {label}")
        return 0
    print(f"TIMED_OUT: {label} after {args.timeout:g}s", file=sys.stderr)
    return TIMED_OUT


if __name__ == "__main__":
    raise SystemExit(main())
