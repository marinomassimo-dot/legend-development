#!/usr/bin/env python3
"""Guard the paths and status claims a first-time clone reader encounters."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

from test_documented_commands import markdown_files


ROOT = Path(__file__).resolve().parents[1]
FRONT_DOORS = (
    "README.md",
    "CAPABILITIES.md",
    "ARCHITECTURE.md",
    "CLAUDE.md",
    "framework/protocols/index.md",
    "disease-models/wwox/disease_model.md",
)
ROOT_PREFIXES = (
    ".claude/",
    "disease-models/",
    "framework/",
    "release/",
    "scripts/",
)
INLINE_PATH = re.compile(r"`([^`\n]+\.(?:md|py))`")


class FreshCloneReaderJourneyTests(unittest.TestCase):
    def test_front_doors_exist(self) -> None:
        missing = [path for path in FRONT_DOORS if not (ROOT / path).is_file()]
        self.assertEqual([], missing)

    def test_inline_repository_paths_resolve(self) -> None:
        problems = []
        for document in markdown_files():
            # `backup/` is the BATCH_COMMIT Phase-3 snapshot root: gitignored copies of the
            # canonical files, kept at a different depth, so their relative links no longer
            # resolve. Scanning them made the mandatory pre-commit backup fail this test.
            if ".git" in document.parts or "backup" in document.parts:
                continue
            for number, line in enumerate(
                document.read_text(encoding="utf-8").splitlines(), 1
            ):
                for match in INLINE_PATH.finditer(line):
                    reference = match.group(1)
                    if any(char in reference for char in "*<>{}|$"):
                        continue
                    if reference.startswith(("./", "../")):
                        target = (document.parent / reference).resolve()
                    elif reference.startswith(ROOT_PREFIXES):
                        target = ROOT / reference
                    else:
                        continue
                    if not target.is_file():
                        problems.append(
                            f"{document.relative_to(ROOT)}:{number}: {reference}"
                        )
        self.assertEqual(
            [],
            problems,
            "Reader-facing inline repository paths are missing:\n"
            + "\n".join(problems),
        )

    def test_protocol_index_describes_the_shipped_public_state(self) -> None:
        index = (ROOT / "framework/protocols/index.md").read_text(
            encoding="utf-8"
        )
        stale = (
            "Current files — Scientific (private overlay; not shipped)",
            "disease-level rewrite pending",
            "STRUCTURE READY (empty)",
        )
        present = [phrase for phrase in stale if phrase in index]
        self.assertEqual([], present, "Stale public index claims: " + repr(present))
        for basename in (
            "working_model_current",
            "claim_registry_current",
            "paper_registry_current",
            "literature_tracking_log_current",
        ):
            self.assertIn(f"[[{basename}]]", index)

    def test_release_status_matches_the_green_link_contract(self) -> None:
        manifest = json.loads(
            (ROOT / "release/losslessness_manifest.json").read_text(
                encoding="utf-8"
            )
        )
        components = {item["id"]: item for item in manifest["components"]}
        self.assertEqual("RESTORED", components["deep_link_integrity"]["status"])
        handoff = (ROOT / "release/LINK_MIGRATION_HANDOFF.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("Migration completed", handoff)
        self.assertNotIn("intentionally red", handoff)

    def test_readme_has_a_runnable_first_clone_path(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        normalized = " ".join(readme.split())
        required = (
            "## Quick start after cloning",
            "python3 framework/scripts/legend_lint.py .",
            "python3 scripts/test_link_targets.py",
            "python3 scripts/run_release_regressions.py",
            "open the cloned repository folder directly as an Obsidian vault",
        )
        missing = [text for text in required if text not in normalized]
        self.assertEqual([], missing)


if __name__ == "__main__":
    unittest.main(verbosity=2)
