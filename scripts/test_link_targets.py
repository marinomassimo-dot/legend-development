#!/usr/bin/env python3
"""Validate deep-link targets that the file-existence gate cannot check.

Standard Markdown fragments are checked against GitHub-style heading slugs.
LEGEND wikilinks are checked by stable record ID: the ID must occur as a
record definition in the resolved target, and record families must point to
the correct registry type.  Human-readable text after an ID is treated as a
label because translated editions may legitimately translate that text.
"""

from __future__ import annotations

import importlib.util
import os
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]

# One definition of "this directory is another checkout", shared with the publication gate.
_GATE_PATH = Path(__file__).with_name("public_release_gate.py")
_SPEC = importlib.util.spec_from_file_location("public_release_gate", _GATE_PATH)
assert _SPEC and _SPEC.loader
GATE = importlib.util.module_from_spec(_SPEC)
sys.modules[_SPEC.name] = GATE
_SPEC.loader.exec_module(GATE)
# `backup/` holds the snapshots that Phase 3 of the BATCH_COMMIT protocol *requires* before
# any canonical write. A snapshot is a byte-identical copy of the current files, so scanning
# it makes every canonical record resolve to two files and every relative link inside the copy
# dangle — i.e. obeying the protocol failed this test. A check that punishes the mandatory
# backup teaches sessions to skip it, so the copies are excluded by name.
SKIP_PARTS = {".git", "__pycache__", ".venv", "venv", "node_modules", "backup"}
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]*]\(([^)]+)\)")
WIKILINK = re.compile(r"\[\[([^\]]+)]]")
HEADING = re.compile(r"^\s{0,3}#{1,6}\s+(.+?)\s*$")
RECORD_ID = re.compile(
    r"\b(?:CLAIM|PAPER|CORPUS)\s+\d{3}\b"
    r"|\b(?:RL|RC|TX|DL-(?:BIO|MECH|MOL|REPO)|FM|DIS)-"
    r"[A-Z0-9-]*\d{3}\b"
    r"|\bHYP-\d{8}-\d{2}\b"
    # `LIT-` records are the lifecycle entries of the literature tracking log. The log holds
    # 380 of them — 10 three-digit and 370 four-digit — and until now no family claimed them,
    # so a wikilink naming one was resolved like free text. No such wikilink exists yet: this
    # is a forward guard, and it says so rather than claiming to have validated anything.
    r"|\bLIT-\d{3,4}\b"
)
EXAMPLE_FRAGMENT = re.compile(
    r"^(?:heading|ID|ID-NNN|PAPER NNN|CLAIM NNN|RL-XXX-NNN|"
    r"BC-001|CME-001)$"
)
EXPECTED_TARGET = {
    "CLAIM": "claim_registry_current",
    "PAPER": "paper_registry_current",
    "CORPUS": "paper_registry_current",
    "RL": "research_lines_current",
    "RC": "research_candidates_current",
    "TX": "therapeutic_strategies_current",
    "HYP": "therapeutic_hypotheses_ledger_current",
    "DL": "discovery_ledger_current",
    "FM": "discovery_ledger_current",
    "DIS": "dismissal_ledger_current",
    "LIT": "literature_tracking_log_current",
}


def markdown_files(root: Path = ROOT) -> list[Path]:
    """Markdown of *this* checkout only.

    🔴 `rglob` walked into any checkout mounted inside this one, so a worktree's copy of the
    registries became a second definition of every record: duplicate basenames for the
    resolver, and every dangling link in another repository reported as a defect in this one.
    Pruning, not an ignore rule — the audit is supposed to see gitignored files, it is just
    not supposed to see other repositories.
    """
    found: list[Path] = []
    for dirpath, dirnames, filenames in os.walk(root):
        here = Path(dirpath)
        dirnames[:] = [name for name in dirnames
                       if name not in SKIP_PARTS
                       and not GATE.is_nested_checkout(here / name)]
        found.extend(here / name for name in filenames if name.endswith(".md"))
    return sorted(found)


def heading_slug(title: str) -> str:
    title = re.sub(r"\s+#+\s*$", "", title)
    title = re.sub(r"<[^>]+>", "", title)
    title = re.sub(r"[`*_~]", "", title).strip().casefold()
    title = "-".join(title.split())
    return "".join(
        character
        for character in title
        if character in "-_" or character.isalnum()
    )


def heading_slugs(path: Path) -> set[str]:
    slugs: set[str] = set()
    counts: dict[str, int] = {}
    in_fence = False
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if re.match(r"^\s*```", line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        match = HEADING.match(line)
        if not match:
            continue
        base = heading_slug(match.group(1))
        occurrence = counts.get(base, 0)
        counts[base] = occurrence + 1
        slugs.add(base if occurrence == 0 else f"{base}-{occurrence}")
    return slugs


def record_definitions(path: Path) -> set[str]:
    definitions: set[str] = set()
    in_fence = False
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if re.match(r"^\s*```", line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        is_definition = bool(
            HEADING.match(line)
            or re.match(r"^\s*-\s+\*\*(?:FM|DIS)-", line)
        )
        if is_definition:
            definitions.update(match.group(0) for match in RECORD_ID.finditer(line))
    return definitions


def record_family(record_id: str) -> str:
    return re.match(r"[A-Z]+", record_id).group(0)  # type: ignore[union-attr]


class LinkTargetTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.files = markdown_files()
        cls.by_name: dict[str, list[Path]] = {}
        for path in cls.files:
            for key in {path.name.casefold(), path.stem.casefold()}:
                cls.by_name.setdefault(key, []).append(path)

    def resolve_wikilink(self, source: Path, name: str) -> list[Path]:
        direct = (source.parent / name).resolve()
        candidates = [
            candidate
            for candidate in (direct, direct.with_suffix(".md"))
            if candidate in self.files
        ]
        if candidates:
            return list(dict.fromkeys(candidates))
        key = Path(name).name.casefold()
        stem = Path(name).stem.casefold()
        return list(
            dict.fromkeys(self.by_name.get(key, []) + self.by_name.get(stem, []))
        )

    def test_markdown_fragments_resolve_to_headings(self) -> None:
        problems = []
        cache = {path: heading_slugs(path) for path in self.files}
        for source in self.files:
            in_fence = False
            for number, line in enumerate(
                source.read_text(encoding="utf-8", errors="replace").splitlines(),
                1,
            ):
                if re.match(r"^\s*```", line):
                    in_fence = not in_fence
                    continue
                if in_fence:
                    continue
                for match in MARKDOWN_LINK.finditer(line):
                    raw = match.group(1).strip().split()[0].strip("<>")
                    if raw.startswith(("http:", "https:", "mailto:")):
                        continue
                    if "#" not in raw:
                        continue
                    path_part, fragment = raw.split("#", 1)
                    target = (
                        source
                        if not path_part
                        else (source.parent / unquote(path_part)).resolve()
                    )
                    if target not in cache:
                        continue
                    if heading_slug(unquote(fragment)) not in cache[target]:
                        problems.append(
                            f"{source.relative_to(ROOT)}:{number}: {raw}"
                        )
        self.assertFalse(
            problems,
            "Markdown fragments with no target heading:\n" + "\n".join(problems),
        )

    def test_wikilink_record_ids_match_target_type_and_exist(self) -> None:
        problems = []
        definitions = {path: record_definitions(path) for path in self.files}
        for source in self.files:
            in_fence = False
            for number, line in enumerate(
                source.read_text(encoding="utf-8", errors="replace").splitlines(),
                1,
            ):
                if re.match(r"^\s*```", line):
                    in_fence = not in_fence
                    continue
                if in_fence:
                    continue
                for match in WIKILINK.finditer(line):
                    raw = match.group(1).split("|", 1)[0].strip()
                    if "#" not in raw:
                        continue
                    name, fragment = raw.split("#", 1)
                    if EXAMPLE_FRAGMENT.match(fragment) or not name:
                        continue
                    id_match = RECORD_ID.search(fragment)
                    if not id_match:
                        continue
                    record_id = id_match.group(0)
                    targets = self.resolve_wikilink(source, name)
                    if len(targets) != 1:
                        problems.append(
                            f"{source.relative_to(ROOT)}:{number}: "
                            f"{raw} resolves to {len(targets)} files"
                        )
                        continue
                    target = targets[0]
                    family = record_family(record_id)
                    expected = EXPECTED_TARGET.get(family)
                    if expected and target.stem != expected:
                        problems.append(
                            f"{source.relative_to(ROOT)}:{number}: {record_id} "
                            f"must target {expected}, not {target.stem}"
                        )
                    elif record_id not in definitions[target]:
                        problems.append(
                            f"{source.relative_to(ROOT)}:{number}: {record_id} "
                            f"is not defined in {target.relative_to(ROOT)}"
                        )
        self.assertFalse(
            problems,
            "Wikilink record-target failures:\n" + "\n".join(problems),
        )

    def test_wikilink_fragments_match_exact_headings(self) -> None:
        """Obsidian heading links require the complete heading text after #."""
        problems = []
        headings = {
            path: {
                re.sub(r"\s+#+\s*$", "", match.group(1)).strip()
                for line in path.read_text(
                    encoding="utf-8", errors="replace"
                ).splitlines()
                if (match := HEADING.match(line))
            }
            for path in self.files
        }
        for source in self.files:
            in_fence = False
            for number, line in enumerate(
                source.read_text(encoding="utf-8", errors="replace").splitlines(),
                1,
            ):
                if re.match(r"^\s*```", line):
                    in_fence = not in_fence
                    continue
                if in_fence:
                    continue
                for match in WIKILINK.finditer(line):
                    raw = match.group(1).split("|", 1)[0].strip()
                    if "#" not in raw:
                        continue
                    name, fragment = raw.split("#", 1)
                    if (
                        not name
                        or fragment.startswith("^")
                        or EXAMPLE_FRAGMENT.match(fragment)
                    ):
                        continue
                    targets = self.resolve_wikilink(source, name)
                    if len(targets) != 1:
                        continue
                    if fragment not in headings[targets[0]]:
                        problems.append(
                            f"{source.relative_to(ROOT)}:{number}: {raw}"
                        )
        preview = problems[:60]
        remainder = len(problems) - len(preview)
        if remainder:
            preview.append(f"... and {remainder} additional mismatches")
        self.assertFalse(
            problems,
            "Obsidian wikilink fragments do not exactly match headings "
            f"({len(problems)}):\n" + "\n".join(preview),
        )


class NestedCheckoutIsNotOurs(unittest.TestCase):
    """The test builds the condition instead of hoping to be run somewhere that has it.

    🔴 This class exists because of how the sibling defect was missed. The fix was verified
    from inside a worktree, where a nested checkout cannot exist — so the suite was green and
    could not have been anything else. A test that depends on the ambient checkout having the
    right shape is not a test of the code; it is a test of where you happened to run it.
    """

    def mount(self) -> tuple[Path, Path]:
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        (root / "own.md").write_text("# Ours\n", encoding="utf-8")
        nested = root / ".claude" / "worktrees" / "session"
        nested.mkdir(parents=True)
        subprocess.run(["git", "init", "-q"], cwd=nested, check=True)
        stray = nested / "broken.md"
        stray.write_text("[[claim_registry_current#CLAIM 999]]\n", encoding="utf-8")
        return root, stray

    def test_markdown_of_a_nested_checkout_is_not_collected(self) -> None:
        root, stray = self.mount()
        collected = markdown_files(root)
        self.assertIn(root / "own.md", collected)
        self.assertNotIn(stray, collected)

    def test_the_walk_would_otherwise_have_found_it(self) -> None:
        """Proves the fixture is capable of failing, which is the point of the class."""
        root, stray = self.mount()
        self.assertIn(stray, sorted(root.rglob("*.md")))


if __name__ == "__main__":
    unittest.main(verbosity=2)
