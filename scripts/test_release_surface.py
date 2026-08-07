#!/usr/bin/env python3
"""Ensure .gitignore cannot silently remove public capabilities at publication."""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import tempfile
import unittest
import unicodedata
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_IGNORED_PARTS = {
    ".DS_Store",
    "__pycache__",
    "node_modules",
}
EXPECTED_IGNORED_SUFFIXES = {".pyc", ".log", ".dcd"}
REQUIRED_ROOT_FILES = {
    ".gitignore",
    "LICENSE",
    "README.md",
    "DATA_SOURCES.md",
    "THIRD_PARTY_NOTICES.md",
}
FORBIDDEN_PUBLIC_DIRECTORIES = {
    "_qa",
    "backup",
    "files",
    "overlay",
    "staging",
}
MAX_PUBLIC_FILE_BYTES = 20 * 1024 * 1024


def tracked_paths() -> frozenset[str]:
    """Files in the index — i.e. the ones that actually reach a published clone."""
    completed = subprocess.run(
        ["git", "-C", str(ROOT), "ls-files", "-z"],
        check=False, capture_output=True, text=True,
    )
    return frozenset(entry for entry in completed.stdout.split("\0") if entry)


def tracked_public_content_roots() -> frozenset[str]:
    """Top-level directories that hold at least one tracked (published) file.

    Derived from the index rather than hardcoded, so it can't go stale as the
    repository grows. A directory with no tracked files (`grants/`, `staging/`,
    `files/`, `backup/`, ...) is deliberately private working material, not a
    silently-hidden public capability — it is exempt by construction, the same
    way `unpublishable_paths` in public_release_gate.py exempts it.
    """
    return frozenset(
        entry.split("/", 1)[0] for entry in tracked_paths() if "/" in entry
    )


def is_expected_generated_path(relative: Path) -> bool:
    return (
        any(part in EXPECTED_IGNORED_PARTS for part in relative.parts)
        or relative.suffix in EXPECTED_IGNORED_SUFFIXES
        or relative.parts[:1] == ("md-output",)
    )


def unexpectedly_ignored_files() -> list[str]:
    files = sorted(
        path.relative_to(ROOT)
        for path in ROOT.rglob("*")
        if path.is_file() and path.name != ".gitignore"
    )
    with tempfile.TemporaryDirectory(prefix="legend-ignore-audit-") as temporary:
        audit_root = Path(temporary)
        subprocess.run(
            ["git", "init", "--quiet", str(audit_root)],
            check=True,
            capture_output=True,
            text=True,
        )
        shutil.copy2(ROOT / ".gitignore", audit_root / ".gitignore")
        completed = subprocess.run(
            ["git", "-C", str(audit_root), "check-ignore", "--no-index", "--stdin"],
            input="\n".join(path.as_posix() for path in files) + "\n",
            check=False,
            capture_output=True,
            text=True,
        )
        ignored = {
            Path(line)
            for line in completed.stdout.splitlines()
            if line.strip()
        }
    # Checking "is this exact path tracked" is vacuous: a file that just got
    # newly hidden by an ignore-rule edit is untracked in the working tree by
    # definition (that's what "hidden" means), so it would never appear in the
    # index either. The actual risk is a public *directory* — one that already
    # ships tracked content — silently losing a new file to a broad pattern
    # like `*private*`. Scope the check to that: an ignored-and-untracked file
    # is a problem only when it sits under a directory the release already
    # tracks; directories with zero tracked files are private working areas by
    # construction (mirrors `unpublishable_paths` in public_release_gate.py).
    public_roots = tracked_public_content_roots()
    return sorted(
        path.as_posix()
        for path in ignored
        if not is_expected_generated_path(path) and path.parts[0] in public_roots
    )


class ReleaseSurfaceTests(unittest.TestCase):
    def test_example_agent_policy_does_not_bypass_permissions(self) -> None:
        settings = json.loads(
            (ROOT / ".claude" / "settings.json.example").read_text(
                encoding="utf-8"
            )
        )
        mode = settings.get("permissions", {}).get("defaultMode")
        self.assertNotEqual(
            "bypassPermissions",
            mode,
            "The public host template must not disable permission checks",
        )

    def test_github_actions_are_pinned_to_commit_shas(self) -> None:
        workflow = (
            ROOT / ".github" / "workflows" / "public-release-gate.yml"
        ).read_text(encoding="utf-8")
        unpinned = [
            line.strip()
            for line in workflow.splitlines()
            if "uses:" in line
            and not re.search(r"@[0-9a-f]{40}(?:\s|$)", line)
        ]
        self.assertEqual(
            [],
            unpinned,
            "GitHub Actions must be pinned to immutable commit SHAs",
        )

    def test_no_public_file_is_silently_gitignored(self) -> None:
        ignored = unexpectedly_ignored_files()
        self.assertEqual(
            [],
            ignored,
            "Public files hidden by .gitignore:\n" + "\n".join(ignored),
        )

    def test_required_release_files_exist(self) -> None:
        missing = sorted(
            name for name in REQUIRED_ROOT_FILES if not (ROOT / name).is_file()
        )
        self.assertEqual([], missing)

    # 🔴 These two asked the local disk a question only the published surface can answer, and
    # a live research workspace always answers wrong: `backup/`, `files/` and `staging/` exist
    # here by design and are gitignored, and one locally cached full text is over the size cap.
    # Both failures were true and permanent, so this file was permanently red — and on
    # 2026-08-06 it swallowed a real defect: two new shebang entrypoints shipped non-executable
    # and were reported as "only the environmental red". An alarm you have learned to ignore is
    # an alarm that will absorb the next real one, which is the argument this repository spent
    # the day making about seals over living state, arriving by the door nobody was watching.
    #
    # The fix is not to split the file or to weaken the checks: it is to ask the question they
    # actually mean. What ships is what git tracks. `tracked_paths()` was already here — its
    # own docstring already said a directory holding no tracked files is fine — and these two
    # simply did not use it. Scoping to tracked content is *stricter*, not looser: an
    # accidentally committed private root or oversized blob still fails, and now it fails
    # somewhere anyone will read.
    def test_no_private_quarantine_root_holds_tracked_content(self) -> None:
        offenders = sorted(
            path for path in tracked_paths()
            if path.split("/", 1)[0] in FORBIDDEN_PUBLIC_DIRECTORIES
        )
        self.assertEqual(
            [], offenders,
            "these tracked files live under a private quarantine root:\n  "
            + "\n  ".join(offenders))

    def test_no_symlinks_or_oversized_public_files(self) -> None:
        symlinks = []
        oversized = []
        for relative in sorted(tracked_paths()):
            path = ROOT / relative
            if path.is_symlink():
                symlinks.append(relative)
            elif path.is_file() and path.stat().st_size > MAX_PUBLIC_FILE_BYTES:
                oversized.append(f"{relative}: {path.stat().st_size} bytes")
        self.assertEqual([], symlinks, "Symlinks require explicit release review")
        self.assertEqual([], oversized, "Oversized files:\n" + "\n".join(oversized))

    def test_paths_have_no_case_or_unicode_normalization_collisions(self) -> None:
        folded: dict[str, list[str]] = defaultdict(list)
        for path in ROOT.rglob("*"):
            relative = path.relative_to(ROOT).as_posix()
            key = unicodedata.normalize("NFC", relative).casefold()
            folded[key].append(relative)
        collisions = [items for items in folded.values() if len(items) > 1]
        self.assertEqual([], collisions)

    def test_shebang_python_entrypoints_are_executable(self) -> None:
        failures = []
        for path in ROOT.rglob("*.py"):
            if not path.read_bytes().startswith(b"#!"):
                continue
            if not path.stat().st_mode & 0o111:
                failures.append(path.relative_to(ROOT).as_posix())
        self.assertEqual(
            [],
            failures,
            "Shebang entrypoints missing executable mode:\n"
            + "\n".join(failures),
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
