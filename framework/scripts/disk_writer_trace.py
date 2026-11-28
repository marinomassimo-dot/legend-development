"""Read-only trace of who writes to the disk while free space swings (ADV-299, HE, 2026-11-28).

Samples the free space of a path every INTERVAL seconds for MINUTES minutes. On every sample-to-sample drop of DROP_MB or
more it records (a) which watched top-level directories received files modified since the previous sample, with their
bytes (an upper bound on growth: a rewritten file counts whole), and (b) the processes whose cumulative `write_bytes`
(/proc/<pid>/io, your own processes only) grew most since the previous sample, with the largest regular file each holds
open (/proc/<pid>/fd). At the end it adds the per-process write totals for the whole run. One TSV, a few hundred lines.

It reads and measures; it deletes nothing, kills nothing, and writes only the TSV named by --out.

Usage: python3 disk_writer_trace.py --out OUT.tsv [--minutes 30] [--interval 10] [--drop-mb 100] [--path /]
           [--watch DIR ...]    (default watch: ~/.codex ~/legend_browser_tmp /tmp ~/.claude <repo>/files ~/.cache)
"""
from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

MB = 1024 * 1024
FIND_TIMEOUT = 15


def drops(free_mb: list[float], drop_mb: float) -> list[tuple[int, float]]:
    """(index, size in MB) of every sample whose free space is at least drop_mb below the previous sample."""
    return [(i, free_mb[i - 1] - free_mb[i]) for i in range(1, len(free_mb)) if free_mb[i - 1] - free_mb[i] >= drop_mb]


def proc_writes() -> dict[int, tuple[int, str]]:
    """pid -> (write_bytes, command head) for the processes this user may read."""
    out: dict[int, tuple[int, str]] = {}
    for entry in os.listdir("/proc"):
        if not entry.isdigit():
            continue
        try:
            with open(f"/proc/{entry}/io") as handle:
                fields = dict(line.split(": ") for line in handle.read().splitlines() if ": " in line)
            with open(f"/proc/{entry}/cmdline", "rb") as handle:
                head = handle.read().replace(b"\0", b" ").decode("utf-8", "replace").strip()[:90]
            out[int(entry)] = (int(fields.get("write_bytes", "0")), head)
        except (OSError, ValueError):
            continue
    return out


def biggest_open_file(pid: int) -> tuple[int, str]:
    best = (0, "")
    try:
        for fd in os.listdir(f"/proc/{pid}/fd"):
            try:
                target = os.readlink(f"/proc/{pid}/fd/{fd}")
                if not target.startswith("/"):
                    continue
                size = os.stat(f"/proc/{pid}/fd/{fd}").st_size
                if size > best[0] and os.path.isfile(target):
                    best = (size, target)
            except OSError:
                continue
    except OSError:
        pass
    return best


def recent_bytes(directory: str, since_epoch: float) -> int:
    """Bytes in regular files under `directory` modified after `since_epoch` (upper bound on growth)."""
    stamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(since_epoch))
    try:
        done = subprocess.run(["find", directory, "-xdev", "-type", "f", "-newermt", stamp, "-printf", "%s\\n"],
                              capture_output=True, text=True, timeout=FIND_TIMEOUT)
        return sum(int(x) for x in done.stdout.split() if x.isdigit())
    except (subprocess.TimeoutExpired, OSError):
        return -1


def run(path: str, minutes: float, interval: float, drop_mb: float, watch: list[str], out: Path, sleep=time.sleep, clock=time.time) -> None:
    rows: list[str] = []
    totals: dict[int, int] = {}
    heads: dict[int, str] = {}
    free: list[float] = []
    stamps: list[float] = []
    previous = proc_writes()
    end = clock() + minutes * 60
    while True:
        now = clock()
        free.append(shutil.disk_usage(path).free / MB)
        stamps.append(now)
        current = proc_writes()
        grown = sorted(((current[p][0] - previous[p][0], p) for p in current if p in previous and current[p][0] > previous[p][0]), reverse=True)
        for delta, pid in grown:
            totals[pid] = totals.get(pid, 0) + delta
            heads[pid] = current[pid][1]
        rows.append(f"sample\t{time.strftime('%H:%M:%S', time.localtime(now))}\t{free[-1]:.0f}\t\t")
        if len(free) > 1 and free[-2] - free[-1] >= drop_mb:
            rows.append(f"DROP\t{time.strftime('%H:%M:%S', time.localtime(now))}\t{free[-1]:.0f}\t{free[-2] - free[-1]:.0f} MB\t")
            for directory in watch:
                size = recent_bytes(directory, stamps[-2])
                if size != 0:
                    rows.append(f"dir\t\t\t{size / MB:.0f} MB modified since previous sample\t{directory}")
            for delta, pid in grown[:5]:
                size, target = biggest_open_file(pid)
                rows.append(f"proc\t\t\t{delta / MB:.0f} MB written since previous sample\tpid {pid} {current[pid][1]} | biggest open file {size / MB:.0f} MB {target}")
        previous = current
        if now >= end:
            break
        sleep(max(0.0, interval - (clock() - now)))
    for pid, total in sorted(totals.items(), key=lambda kv: -kv[1])[:10]:
        rows.append(f"total\t\t\t{total / MB:.0f} MB written over the run\tpid {pid} {heads.get(pid, '')}")
    rows.append(f"summary\t\t{free[-1]:.0f}\tfree start {free[0]:.0f} MB, end {free[-1]:.0f} MB, min {min(free):.0f} MB, drops of {drop_mb:.0f} MB or more: {len(drops(free, drop_mb))}\t")
    out.write_text("kind\ttime\tfree_mb\tmeasure\tdetail\n" + "\n".join(rows) + "\n", encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--out", required=True)
    ap.add_argument("--minutes", type=float, default=30)
    ap.add_argument("--interval", type=float, default=10)
    ap.add_argument("--drop-mb", type=float, default=100)
    ap.add_argument("--path", default="/")
    ap.add_argument("--watch", nargs="*")
    args = ap.parse_args(argv)
    home = Path.home()
    repo = Path(__file__).resolve().parents[2]
    watch = args.watch or [str(home / ".codex"), str(home / "legend_browser_tmp"), "/tmp", str(home / ".claude"), str(repo / "files"), str(home / ".cache")]
    run(args.path, args.minutes, args.interval, args.drop_mb, [w for w in watch if os.path.isdir(w)], Path(args.out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
