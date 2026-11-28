"""After the fact: what filled the disk in a time window, with no earlier snapshot (HE, 2026-11-28).

`disk_writer_trace.py` answers only while it is running. This reads each file's birth time (statx) and reports, by area:
(a) BORN: allocated bytes of inodes created inside the window and still present;
(b) OLDER_MODIFIED: full allocated size of older regular files changed since the window start (an upper bound on growth);
(c) DELETED_OPEN: bytes of deleted files your own processes still hold open;
plus the free space now. Hard links count once. A worktree under `.claude/worktrees/` is one area; elsewhere an area is
the first four path components.

Limits: deleted files leave no trace; growth of an appended file cannot be separated from its old size; unreadable
directories are counted, not read. Where the filesystem gives no birth time the run exits 2 instead of printing zero.
It reads only: it deletes nothing and writes only to standard output.

Usage: python3 disk_born.py --since 2026-11-28T14:48 [--until 2026-11-28T16:31] [--root /] [--top 12]
       (times without an offset are UTC)
"""
from __future__ import annotations

import argparse
import ctypes
import datetime as dt
import os
import re
import shutil
import stat as st_mod
import sys
from collections import Counter

AT_FDCWD, AT_SYMLINK_NOFOLLOW, STATX_BTIME = -100, 0x100, 0x800
GB = 1e9
WORKTREE = re.compile(r"(.*?/\.claude/worktrees/[^/]+)(?:/|$)")


def birth_time(path: str) -> float | None:
    """Epoch seconds of creation, or None when statx or the filesystem cannot tell."""
    try:
        libc = ctypes.CDLL(None, use_errno=True)
        buf = ctypes.create_string_buffer(256)
        if libc.statx(AT_FDCWD, os.fsencode(path), AT_SYMLINK_NOFOLLOW, STATX_BTIME, buf) != 0:
            return None
    except (AttributeError, OSError):
        return None
    if not int.from_bytes(buf.raw[0:4], sys.byteorder) & STATX_BTIME:
        return None
    seconds = int.from_bytes(buf.raw[80:88], sys.byteorder, signed=True)
    return seconds + int.from_bytes(buf.raw[88:92], sys.byteorder) / 1e9


def area(path: str) -> str:
    match = WORKTREE.match(path)
    if match:
        return match.group(1)
    return "/".join(os.path.dirname(path).split("/")[:5]) or "/"


def parse_time(text: str) -> float:
    when = dt.datetime.fromisoformat(text.replace("Z", "+00:00"))
    return (when if when.tzinfo else when.replace(tzinfo=dt.timezone.utc)).timestamp()


def scan(root: str, since: float, until: float, birth=birth_time) -> dict:
    """Walk one filesystem. Only entries whose ctime reaches `since` can have been born or changed in the window."""
    device = os.lstat(root).st_dev
    born: Counter = Counter()
    modified: Counter = Counter()
    seen: set[int] = set()
    unreadable = [0]
    candidates = without_birth = 0

    def failed(_error) -> None:
        unreadable[0] += 1

    for directory, subdirs, files in os.walk(root, onerror=failed):
        kept = []
        for name in subdirs + files:
            path = os.path.join(directory, name)
            try:
                info = os.lstat(path)
            except OSError:
                continue
            if info.st_dev != device:
                continue
            if name in subdirs:
                kept.append(name)
            if info.st_ctime < since or info.st_ino in seen:
                continue
            seen.add(info.st_ino)
            candidates += 1
            created = birth(path)
            if created is None:
                without_birth += 1
                continue
            size = info.st_blocks * 512
            if since <= created <= until:
                born[area(path)] += size
            elif created < since <= info.st_mtime and st_mod.S_ISREG(info.st_mode):
                modified[area(path)] += size
        subdirs[:] = [name for name in subdirs if name in kept]
    return {"born": born, "modified": modified, "candidates": candidates,
            "without_birth": without_birth, "unreadable": unreadable[0]}


def deleted_open(root: str) -> int:
    """Allocated bytes of deleted files on root's filesystem that processes you may inspect still hold open."""
    device, seen, total = os.lstat(root).st_dev, set(), 0
    for pid in filter(str.isdigit, os.listdir("/proc")):
        try:
            handles = os.listdir(f"/proc/{pid}/fd")
        except OSError:
            continue
        for handle in handles:
            link = f"/proc/{pid}/fd/{handle}"
            try:
                target = os.readlink(link)
                if not target.endswith(" (deleted)") or target.startswith(("/memfd", "/dev")):
                    continue
                info = os.stat(link)
            except OSError:
                continue
            if info.st_dev == device and info.st_ino not in seen:
                seen.add(info.st_ino)
                total += info.st_blocks * 512
    return total


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--since", required=True)
    ap.add_argument("--until")
    ap.add_argument("--root", default="/")
    ap.add_argument("--top", type=int, default=12)
    args = ap.parse_args(argv)
    since = parse_time(args.since)
    until = parse_time(args.until) if args.until else dt.datetime.now(dt.timezone.utc).timestamp()
    if until < since:
        ap.error("--until is before --since")
    result = scan(args.root, since, until)
    if result["candidates"] and result["without_birth"] == result["candidates"]:
        print("NO_BIRTH_TIME: statx gave no creation time for any changed file; nothing can be attributed.")
        return 2
    for title, key, note in (("BORN", "born", "created in the window, still present"),
                             ("OLDER_MODIFIED", "modified", "older files changed since the start; full size, not growth")):
        counts = result[key]
        print(f"{title} {sum(counts.values()) / GB:.2f} GB ({note})")
        for name, size in counts.most_common(args.top):
            print(f"  {size / GB:7.2f}  {name}")
    print(f"DELETED_OPEN {deleted_open(args.root) / GB:.2f} GB")
    print(f"FREE_NOW {shutil.disk_usage(args.root).free / GB:.2f} GB")
    print(f"unreadable directories: {result['unreadable']}; changed entries without birth time: {result['without_birth']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
