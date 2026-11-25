#!/usr/bin/env python3
"""Which held files are not what their name says: error pages, empty downloads and damaged archives saved as papers.

Why it exists (ADV-279, 2026-11-25). A study was selected for its two held "figures", which were HTML "HTTP 404" pages saved
under image names. A first pass over the held tree found 34 unusable files among 6,270 documents, images and archives; no
read receipt named any of them, so the damage was in counting what is readable. Nothing looked at the bytes at save time.

What it does: reads the first bytes of each file and compares them with the extension; opens a zip's directory. For text
formats (.xml, .html, .txt) it reports empty files and the interstitial pages seen on this host (bot challenge, reCAPTCHA,
403/404 title, an error body). An image saved under another image extension is readable and is listed only with --names.

Print-only: it writes nothing, removes nothing, fetches nothing and gates nothing. A file it does not list is not thereby
the right article: this checks the kind of bytes, not their content.

    python3 framework/scripts/held_content_check.py <file or folder> ...   # after saving: exit 1 if any is unusable
    python3 framework/scripts/held_content_check.py                        # every file under files/
    python3 framework/scripts/held_content_check.py --names                # also images saved under another image extension

Output: one line per file, `reason<TAB>bytes<TAB>path`. Exit 0 none unusable, 1 at least one, 2 nothing to check.
"""
from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
import zipfile
from pathlib import Path

# Folders never opened: sealed custodian sets and private operator inputs.
SKIP_DIRS = ("adv174_negraes_custodian_he", "adv175_predictor_for_it", "operator_inputs", "privacy_local_it8")
HEAD_BYTES = 4096
INTERSTITIAL_MAX = 60_000  # the pages seen are 5 to 49 KB; a real article page is larger than this bound or has its own title
IMAGES = {"jpeg", "png", "gif", "tiff", "webp"}
WANT = {
    ".jpg": "jpeg", ".jpeg": "jpeg", ".png": "png", ".gif": "gif", ".tif": "tiff", ".tiff": "tiff", ".webp": "webp",
    ".svg": "svg", ".pdf": "pdf", ".zip": "zip", ".docx": "zip", ".xlsx": "zip", ".pptx": "zip",
    ".doc": "ole", ".xls": "ole", ".ppt": "ole", ".gz": "gzip", ".tgz": "gzip",
}
TEXT = (".xml", ".html", ".htm", ".txt")
INTERSTITIALS = (
    ("bot challenge page", re.compile(rb"<title>\s*Just a moment|recaptcha/challenge", re.I)),
    ("HTTP error page", re.compile(rb"<title>[^<]{0,60}(HTTP (Error )?40[34]|40[34][^<]{0,12}(Not Found|Forbidden)|Access Denied|Page Not Found)", re.I)),
    ("error body", re.compile(rb"<(?:\w+:)?errorBean[\s>]|^\s*\{\s*\"error\"\s*:")),
)


def kind(head: bytes) -> str:
    """The format the first bytes announce; 'other' when none of the known ones."""
    if not head:
        return "empty"
    if head.startswith(b"\xff\xd8\xff"):
        return "jpeg"
    if head.startswith(b"\x89PNG\r\n\x1a\n"):
        return "png"
    if head.startswith((b"GIF87a", b"GIF89a")):
        return "gif"
    if head.startswith((b"II*\x00", b"MM\x00*")):
        return "tiff"
    if head[:4] == b"RIFF" and head[8:12] == b"WEBP":
        return "webp"
    if head.startswith((b"PK\x03\x04", b"PK\x05\x06")):
        return "zip"
    if head.startswith(b"\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1"):
        return "ole"
    if head.startswith(b"\x1f\x8b"):
        return "gzip"
    low = head.lstrip(b"\xef\xbb\xbf \t\r\n").lower()
    if low.startswith((b"<!doctype html", b"<html")) or b"<html" in low[:600]:
        return "html"
    if b"%PDF-" in head[:1024]:  # after the HTML test: a page may quote the marker
        return "pdf"
    if low.startswith(b"<svg") or (low.startswith(b"<?xml") and b"<svg" in low[:600]):
        return "svg"
    if low.startswith(b"<"):
        return "xml"
    return "other"


def check(path: Path) -> tuple[str, bool] | None:
    """(reason, unusable) for a file that is not what its name says, else None. Unknown extensions are not judged."""
    ext = path.suffix.lower()
    if ext not in WANT and ext not in TEXT:
        return None
    size = path.stat().st_size
    with path.open("rb") as handle:
        head = handle.read(HEAD_BYTES)
    if not head:
        return "empty file", True
    page = None
    if size <= INTERSTITIAL_MAX:
        page = next((label for label, pattern in INTERSTITIALS if pattern.search(head)), None)
    if ext in TEXT:
        return (page, True) if page else None
    got, want = kind(head), WANT[ext]
    if got != want:
        if got in IMAGES and want in IMAGES:
            return f"readable {got} saved as {ext}", False
        return page or f"{got} content saved as {ext}", True
    if got == "zip":
        try:
            zipfile.ZipFile(path).close()
        except (zipfile.BadZipFile, OSError):
            return "damaged zip", True
    return None


def walk(targets: list[Path]):
    """Regular files under the targets; symlinks are neither followed nor judged, the skipped folders never entered."""
    for target in targets:
        if target.is_file() and not target.is_symlink():
            yield target
            continue
        for folder, dirs, names in os.walk(target):
            dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS)
            for name in sorted(names):
                path = Path(folder) / name
                if path.is_file() and not path.is_symlink():
                    yield path


def default_files_dir() -> Path | None:
    """`files/` of this checkout, or of the primary checkout when this is a linked worktree that carries none."""
    here = Path(__file__).resolve().parents[2]
    done = subprocess.run(["git", "-C", str(here), "rev-parse", "--path-format=absolute", "--git-common-dir"],
                          capture_output=True, text=True)
    candidates = [here] + ([Path(done.stdout.strip()).parent] if done.returncode == 0 else [])
    return next((base / "files" for base in candidates if (base / "files" / "fulltext").is_dir()), None)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="List held files that are not what their name says. Print-only.")
    ap.add_argument("paths", nargs="*", help="files or folders (default: files/)")
    ap.add_argument("--names", action="store_true", help="also list images saved under another image extension")
    args = ap.parse_args(argv)
    targets = [Path(p) for p in args.paths]
    if not targets:
        held = default_files_dir()
        targets = [held] if held else []
    missing = [str(t) for t in targets if not t.exists()]
    if missing or not targets:
        print(f"ERROR: nothing to check ({', '.join(missing) or 'no files/ on this host'})", file=sys.stderr)
        return 2
    seen = unusable = names = 0
    for path in walk(targets):
        seen += 1
        found = check(path)
        if found is None:
            continue
        reason, bad = found
        unusable += bad
        names += not bad
        if bad or args.names:
            print(f"{reason}\t{path.stat().st_size}\t{path}")
    print(f"{seen} file(s) seen, {unusable} unusable, {names} readable under another image name", file=sys.stderr)
    return 1 if unusable else 0


if __name__ == "__main__":
    sys.exit(main())
