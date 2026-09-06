#!/usr/bin/env python3
"""Check that repository-local Python paths documented in Markdown still exist.

This is deliberately independent from the release gate.  It protects a common
losslessness failure mode: prose and examples survive a rewrite while the
executable they promise has disappeared or moved.
"""

from __future__ import annotations

import re
import os
import subprocess
import sys
import unittest
import tempfile
from unittest.mock import patch
from pathlib import Path

from public_release_gate import is_nested_checkout


ROOT = Path(__file__).resolve().parents[1]
PYTHON_PATH = re.compile(
    r"(?<![A-Za-z0-9_.-])"
    r"(?P<path>(?:\.\.?/)*(?:[A-Za-z0-9_.-]+/)+[A-Za-z0-9_.-]+\.py)"
)
REPO_PREFIXES = (
    ".claude/",
    "disease-models/",
    "framework/",
    "scripts/",
)
IGNORED_PARTS = frozenset({".git", ".venv", "node_modules", "__pycache__"})


def markdown_files() -> list[Path]:
    found = []
    for directory, children, files in os.walk(ROOT):
        children[:] = [name for name in children if name not in IGNORED_PARTS
                       and name != "backup" and not is_nested_checkout(Path(directory) / name)]
        found.extend(Path(directory) / name for name in files if name.endswith(".md"))
    return sorted(found)


def resolve_reference(document: Path, reference: str) -> Path | None:
    """Return a repository-local target, or None for illustrative/external paths."""
    if "..." in reference or reference.endswith("/X.py"):
        return None
    if reference.startswith(("./", "../")):
        target = (document.parent / reference).resolve()
        try:
            target.relative_to(ROOT)
        except ValueError:
            return None
        return target
    if reference.startswith(REPO_PREFIXES):
        return ROOT / reference
    return None


def missing_documented_commands() -> list[str]:
    missing: list[str] = []
    for document in markdown_files():
        relative_document = document.relative_to(ROOT)
        for line_number, line in enumerate(
            document.read_text(encoding="utf-8", errors="replace").splitlines(), 1
        ):
            for match in PYTHON_PATH.finditer(line):
                reference = match.group("path")
                target = resolve_reference(document, reference)
                if target is not None and not target.is_file():
                    missing.append(
                        f"{relative_document}:{line_number}: {reference} "
                        f"-> {target.relative_to(ROOT)}"
                    )
    return missing


def documented_cli_invocations() -> list[tuple[Path, int, Path, str]]:
    """Return documented local Python commands, joining shell continuations."""
    invocations = []
    command = re.compile(
        r"\bpython3\s+"
        r"(?P<path>(?:\.\.?/)?[A-Za-z0-9_.-]+"
        r"(?:/[A-Za-z0-9_.-]+)*\.py)\b"
        r"(?P<arguments>.*)"
    )
    for document in markdown_files():
        lines = document.read_text(
            encoding="utf-8", errors="replace"
        ).splitlines()
        index = 0
        while index < len(lines):
            line_number = index + 1
            logical_line = lines[index].strip()
            while logical_line.endswith("\\") and index + 1 < len(lines):
                index += 1
                logical_line = (
                    logical_line[:-1] + " " + lines[index].strip()
                )
            match = command.search(logical_line)
            if match:
                reference = match.group("path")
                target = resolve_reference(document, reference)
                if target is not None and target.is_file():
                    # A command written inside a markdown code span ends at the closing
                    # backtick; everything after it is prose. Without this the closing
                    # backtick is captured as part of the first argument and becomes a
                    # bogus sub-command — `fulltext_receipts.py verify` in five session
                    # evaluations of 2026-08-05/06 was reported as "--help exited 2" for
                    # exactly that reason. The records are historical evidence and are not
                    # edited to make a checker pass; the checker is the defect and is fixed
                    # here.
                    arguments = match.group("arguments").split("`", 1)[0]
                    invocations.append(
                        (document, line_number, target, arguments)
                    )
            index += 1
    return invocations


class DocumentedCommandIntegrityTests(unittest.TestCase):
    def test_markdown_scan_prunes_peer_worktrees_but_keeps_local_documents(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            local = root / "README.md"
            local.write_text("local")
            peer = root / "nested-peer"
            peer.mkdir()
            (peer / ".git").write_text("gitdir: elsewhere")
            (peer / "README.md").write_text("peer")
            with patch.dict(markdown_files.__globals__, ROOT=root):
                self.assertEqual([local], markdown_files())

    def test_repository_local_python_commands_exist(self) -> None:
        missing = missing_documented_commands()
        self.assertEqual(
            [],
            missing,
            "Documented repository-local Python targets are missing:\n"
            + "\n".join(missing),
        )

    def test_documented_cli_flags_exist(self) -> None:
        environment = os.environ.copy()
        environment["PYTHONDONTWRITEBYTECODE"] = "1"
        help_by_target = {}
        problems = []
        for document, line_number, target, arguments in documented_cli_invocations():
            # Sub-command aware. Top-level `--help` never lists a sub-command's own flags, so
            # a checker that only asks for it silently stops protecting every tool built with
            # `add_subparsers` — `fulltext_receipts.py record --receipt` and
            # `growth_anchors.py record --batch` among them. Found on 2026-08-07 when the
            # second of those was documented and reported as three missing flags that all
            # exist. The key is (target, sub-command) so each sub-command is asked once.
            words = arguments.split()
            subcommand = words[0] if words and not words[0].startswith("-") else None
            key = (target, subcommand)
            if key not in help_by_target:
                command = [sys.executable, str(target)]
                if subcommand:
                    command.append(subcommand)
                command.append("--help")
                completed = subprocess.run(
                    command,
                    cwd=ROOT,
                    env=environment,
                    check=False,
                    capture_output=True,
                    text=True,
                    timeout=15,
                )
                help_by_target[key] = completed.stdout + completed.stderr
                if completed.returncode:
                    problems.append(
                        f"{target.relative_to(ROOT)}"
                        f"{' ' + subcommand if subcommand else ''}: --help exited "
                        f"{completed.returncode}"
                    )
            for flag in re.findall(
                r"(?<![\w-])--[A-Za-z][A-Za-z0-9-]*", arguments
            ):
                if flag not in help_by_target[key]:
                    problems.append(
                        f"{document.relative_to(ROOT)}:{line_number}: "
                        f"{target.relative_to(ROOT)} does not expose {flag}"
                    )
        self.assertFalse(
            problems,
            "Documented CLI contracts are stale:\n" + "\n".join(problems),
        )


if __name__ == "__main__":
    result = unittest.main(verbosity=2, exit=False)
    sys.exit(not result.result.wasSuccessful())
