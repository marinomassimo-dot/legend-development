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
    return sorted(
        path.as_posix()
        for path in ignored
        if not is_expected_generated_path(path)
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

    def test_private_quarantine_roots_are_absent(self) -> None:
        present = sorted(
            name
            for name in FORBIDDEN_PUBLIC_DIRECTORIES
            if (ROOT / name).exists()
        )
        self.assertEqual([], present)

    def test_no_symlinks_or_oversized_public_files(self) -> None:
        symlinks = []
        oversized = []
        for path in ROOT.rglob("*"):
            relative = path.relative_to(ROOT)
            if path.is_symlink():
                symlinks.append(relative.as_posix())
            elif path.is_file() and path.stat().st_size > MAX_PUBLIC_FILE_BYTES:
                oversized.append(
                    f"{relative.as_posix()}: {path.stat().st_size} bytes"
                )
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
