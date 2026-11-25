#!/usr/bin/env python3
"""Which studies of the receipt ledger have their bytes on this host, counted by name AND by SHA-256.

Why it exists (ADV-267, 2026-11-25). "No held artefact" was decided by file name (a PMID, a preprint id, a DOI or the receipt's
own file name appearing in a name under two folders). SCI's ADV-264 hashed the folders by hand and found that 79 of the 500
studies so counted (15.8 percent) DO have bytes: the receipt's `source_fingerprint` equals the digest of a file held under
another name. A reading queue ordered by that class sends readers to re-acquire what is already here.

What it does: keeps a digest index of every regular file under `files/` (and any `--extra` folder), cached under the host state
folder and refreshed incrementally (a file is hashed again only when its size or mtime changed; hard links are hashed once).
A study is HELD when the name rule finds a file (`files/fulltext`, `files/deepening_downloads`, document suffixes) OR the digest
of any of its receipts is in the index; a digest-only hit is reported with its path.

Print-only: it writes its own cache and nothing else, fetches nothing and gates nothing. HELD says the bytes are on this host.
It says nothing about whether anybody read them (the ledger answers that), and a name-rule hit is not a digest-verified one,
so the two are counted apart. `files/` is gitignored: the counts are facts about this disk, never a committed surface.

    python3 framework/scripts/held_studies.py                     # counts for studies whose latest receipt is partial
    python3 framework/scripts/held_studies.py --depth complete    # another depth; `all` for every study
    python3 framework/scripts/held_studies.py --pmid 12345678     # one study: how it is held, and where
    python3 framework/scripts/held_studies.py --rows digest       # the studies the name rule misses, with their paths
"""
from __future__ import annotations

import argparse
import collections
import json
import os
import re
import subprocess
import sys
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from evidence_presence import sha256_of  # noqa: E402
from repo_root import RootError, add_root_argument, resolve_root_argument  # noqa: E402

LEDGER = "disease-models/wwox/registries/fulltext_read_receipts.jsonl"
NAME_DIRS = ("fulltext", "deepening_downloads")
NAME_SUFFIXES = (".xml", ".pdf", ".html", ".htm", ".txt")
DEPTHS = {"partial": "partial_fulltext_read", "complete": "complete_fulltext_read", "abstract": "abstract_only",
          "queried": "queried_not_full_read", "retrieved": "retrieved_not_read"}
CACHE_ENV = "LEGEND_HELD_INDEX"
HEX64 = re.compile(r"[0-9a-f]{64}")


def default_cache() -> Path:
    named = os.environ.get(CACHE_ENV)
    if named:
        return Path(named)
    return Path(os.environ.get("XDG_STATE_HOME") or Path.home() / ".local" / "state") / "legend" / "held_digest_index.json"


def files_dir(root: Path) -> Path | None:
    """`files/` of this checkout, or of the primary checkout when this is a linked worktree that carries none."""
    candidates = [root]
    done = subprocess.run(["git", "-C", str(root), "rev-parse", "--path-format=absolute", "--git-common-dir"],
                          capture_output=True, text=True)
    if done.returncode == 0:
        candidates.append(Path(done.stdout.strip()).parent)
    for base in candidates:
        folder = base / "files"
        if any((folder / name).is_dir() for name in NAME_DIRS):
            return folder
    return None


def walk(folders: list[Path]):
    """(path, stat) of every non-empty regular file; symlinks are neither followed nor counted."""
    for folder in folders:
        for directory, _, names in os.walk(folder):
            for name in sorted(names):
                path = os.path.join(directory, name)
                try:
                    info = os.lstat(path)
                except OSError:
                    continue
                if os.path.isfile(path) and not os.path.islink(path) and info.st_size:
                    yield path, info


def load_cache(cache: Path) -> dict[str, list]:
    try:
        data = json.loads(cache.read_text(encoding="utf-8"))
        return data["files"] if isinstance(data.get("files"), dict) else {}
    except (OSError, ValueError, KeyError, AttributeError):
        return {}


def save_cache(cache: Path, entries: dict[str, list]) -> None:
    cache.parent.mkdir(parents=True, exist_ok=True)
    handle, name = tempfile.mkstemp(prefix=cache.name, dir=cache.parent)
    with os.fdopen(handle, "w", encoding="utf-8") as out:
        json.dump({"version": 1, "files": entries}, out)
    os.replace(name, cache)


def refresh(folders: list[Path], cache: Path, jobs: int = 4) -> tuple[dict[str, str], dict]:
    """digest -> first path holding it, plus the numbers of the refresh. Only new or changed files are hashed.

    The cache keeps entries of folders not walked this time, so a run with `--extra` does not make the next plain run re-hash.
    """
    started = time.monotonic()
    old = load_cache(cache)
    current: dict[str, list] = {}
    by_inode: dict[tuple, str] = {}
    pending: dict[tuple, list[str]] = {}
    seen_bytes: dict[tuple, int] = {}
    for path, info in walk(folders):
        inode = (info.st_dev, info.st_ino)
        seen_bytes[inode] = info.st_size
        held = old.get(path)
        if held and held[0] == info.st_size and held[1] == info.st_mtime_ns:
            current[path] = held
            by_inode[inode] = held[2]
        else:
            current[path] = [info.st_size, info.st_mtime_ns, None]
            pending.setdefault(inode, []).append(path)

    def digest(item):
        inode, paths = item
        if inode in by_inode:
            return paths, by_inode[inode], 0
        try:
            return paths, sha256_of(Path(paths[0])), seen_bytes[inode]
        except OSError:
            return paths, None, 0

    hashed = hashed_bytes = 0
    with ThreadPoolExecutor(max_workers=max(1, jobs)) as pool:
        for paths, value, size in pool.map(digest, pending.items()):
            hashed += bool(size)
            hashed_bytes += size
            for path in paths:
                if value is None:
                    current.pop(path, None)
                else:
                    current[path][2] = value
    walked = tuple(str(folder) + os.sep for folder in folders)
    kept = {path: entry for path, entry in old.items() if not path.startswith(walked)}
    entries = {**kept, **current}
    if entries != old:
        save_cache(cache, entries)
    index: dict[str, str] = {}
    for path in sorted(current):
        index.setdefault(current[path][2], path)
    return index, {"files": len(current), "unique_inodes": len(seen_bytes), "unique_bytes": sum(seen_bytes.values()),
                   "hashed": hashed, "hashed_bytes": hashed_bytes, "seconds": round(time.monotonic() - started, 1)}


def studies(ledger: Path) -> dict[str, list[dict]]:
    """Contemporaneous receipts per study: PMID, else DOI, else the study token of the event id (ADV-219's key)."""
    out: dict[str, list[dict]] = collections.defaultdict(list)
    for line in ledger.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        event = json.loads(line)
        if event.get("record_kind") != "contemporaneous_receipt":
            continue
        study = event.get("study_id") or {}
        key = study.get("pmid") or study.get("doi")
        if not key:
            match = re.match(r"FTR-\d{8}-(.+)-\d+$", event["event_id"])
            key = match.group(1) if match else event["event_id"]
        out[str(key)].append(event)
    for events in out.values():
        events.sort(key=lambda e: (e.get("event_at", ""), e.get("event_id", "")))
    return dict(out)


def name_index(folder: Path) -> dict[str, list]:
    names: dict[str, list[str]] = collections.defaultdict(list)
    ids: dict[str, list[str]] = collections.defaultdict(list)
    for sub in NAME_DIRS:
        for directory, _, files in os.walk(folder / sub):
            for name in files:
                if not name.lower().endswith(NAME_SUFFIXES):
                    continue
                path = os.path.join(directory, name)
                names[name].append(path)
                for match in re.finditer(r"PMID(\d+)|(PPR\d+)", name):
                    ids[match.group(1) or match.group(2)].append(path)
    return {"names": names, "ids": ids, "lower": [(name.lower(), paths) for name, paths in names.items()]}


def name_matches(key: str, latest: dict, index: dict) -> list[str]:
    """The name rule as ADV-219 froze it: an identifier in the file name, or the file name the latest receipt points at."""
    found: list[str] = []
    if re.fullmatch(r"\d{5,9}", key) or key.startswith("PPR"):
        found += index["ids"].get(key, [])
    elif "/" in key:
        for needle in (key.lower().replace("/", "_"), key.lower().replace("/", "-")):
            for name, paths in index["lower"]:
                if needle in name:
                    found += paths
    located = re.sub(r"^.*\): ", "", os.path.basename(latest.get("source_locator") or ""))
    if located:
        found += index["names"].get(located, [])
    return sorted(set(found))


def digest_matches(events: list[dict], digests: dict[str, str]) -> list[str]:
    wanted = {e.get("source_fingerprint") for e in events}
    return sorted({digests[d] for d in wanted if isinstance(d, str) and HEX64.fullmatch(d) and d in digests})


def classify(by_study: dict[str, list[dict]], names: dict, digests: dict[str, str]) -> dict[str, dict]:
    rows = {}
    for key, events in by_study.items():
        by_name = name_matches(key, events[-1], names)
        by_digest = digest_matches(events, digests)
        rows[key] = {"depth": events[-1].get("evidence_depth"), "by_name": by_name, "by_digest": by_digest,
                     "held": "name" if by_name else "digest" if by_digest else "no",
                     "has_digest": any(isinstance(e.get("source_fingerprint"), str)
                                       and HEX64.fullmatch(e["source_fingerprint"]) for e in events)}
    return rows


def counts(rows: dict[str, dict], depth: str | None = None) -> dict[str, int]:
    chosen = [r for r in rows.values() if depth is None or r["depth"] == depth]
    how = collections.Counter(r["held"] for r in chosen)
    return {"studies": len(chosen), "held": how["name"] + how["digest"], "held_by_name": how["name"],
            "held_by_digest_only": how["digest"], "not_held": how["no"],
            "not_held_without_any_digest": sum(r["held"] == "no" and not r["has_digest"] for r in chosen)}


def measure(root: Path, cache: Path | None = None, extra: list[Path] | None = None, ledger: Path | None = None,
            jobs: int = 4) -> tuple[dict[str, dict], dict] | None:
    """(rows, refresh numbers), or None when this host holds no `files/` to measure."""
    folder = files_dir(root)
    if folder is None:
        return None
    digests, numbers = refresh([folder, *(extra or [])], cache or default_cache(), jobs)
    rows = classify(studies(ledger or root / LEDGER), name_index(folder), digests)
    numbers["files_dir"] = str(folder)
    return rows, numbers


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Which studies of the receipt ledger have their bytes on this host: by name and by SHA-256. Print-only.")
    add_root_argument(ap)
    ap.add_argument("--depth", default="partial", choices=[*DEPTHS, "all"], help="latest-receipt depth to count (default: partial)")
    ap.add_argument("--pmid", action="append", help="one study (PMID, DOI or study key): how it is held and where; repeatable")
    ap.add_argument("--rows", choices=["digest", "not-held"], help="list the studies held by digest only, or not held")
    ap.add_argument("--extra", action="append", default=[], metavar="DIR", help="also index DIR (digest rule only); repeatable")
    ap.add_argument("--cache", help=f"digest index file (default: ${CACHE_ENV}, else the host state folder)")
    ap.add_argument("--ledger", help="receipt ledger to read instead of the checkout's (to reproduce an earlier count)")
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)
    try:
        root = resolve_root_argument(getattr(args, "root", None))
    except RootError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    result = measure(root, Path(args.cache) if args.cache else None, [Path(d).resolve() for d in args.extra],
                     Path(args.ledger) if args.ledger else None, args.jobs)
    if result is None:
        print("held: NOT MEASURED — neither this checkout nor the primary one holds files/fulltext or files/deepening_downloads")
        return 0
    rows, numbers = result
    depth = DEPTHS.get(args.depth)
    if args.pmid:
        chosen = {key: rows.get(key) for key in args.pmid}
    elif args.rows:
        wanted = "digest" if args.rows == "digest" else "no"
        chosen = {k: r for k, r in sorted(rows.items()) if r["held"] == wanted and (depth is None or r["depth"] == depth)}
    else:
        chosen = None
    summary = counts(rows, depth)
    if args.json:
        print(json.dumps({"depth": args.depth, "counts": summary, "index": numbers, "rows": chosen}, indent=1))
        return 0
    print(f"digest index: {numbers['files']} files under {numbers['files_dir']} ({numbers['unique_inodes']} unique inodes, "
          f"{numbers['unique_bytes'] / 1e9:.1f} GB); hashed {numbers['hashed']} ({numbers['hashed_bytes'] / 1e9:.2f} GB) in {numbers['seconds']} s")
    print(f"studies with latest receipt {args.depth}: {summary['studies']} · held {summary['held']} "
          f"(by name {summary['held_by_name']}, by digest only {summary['held_by_digest_only']}) · not held {summary['not_held']} "
          f"(of which {summary['not_held_without_any_digest']} have no receipt digest to look for)")
    for key, row in (chosen or {}).items():
        if row is None:
            print(f"  {key}: no contemporaneous receipt under this key")
            continue
        paths = row["by_name"] or row["by_digest"]
        print(f"  {key}\t{row['depth']}\theld={row['held']}\t" + ("; ".join(paths) if paths else "-"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
