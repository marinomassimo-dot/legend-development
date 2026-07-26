#!/usr/bin/env python3
"""Keep public capability claims aligned with the shipped release manifest."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class PublicClaimsContractTests(unittest.TestCase):
    def test_capability_status_claims_match_manifest(self) -> None:
        capabilities = (ROOT / "CAPABILITIES.md").read_text(encoding="utf-8")
        manifest = json.loads(
            (ROOT / "release" / "losslessness_manifest.json").read_text(
                encoding="utf-8"
            )
        )
        unfinished = [
            item["id"]
            for item in manifest["components"]
            if item["status"] in {"PARTIAL", "PENDING_CONTENT_REWRITE"}
        ]
        absolute_claim = re.search(
            r"(?i)(?:nothing.{0,40}(?:is|was).{0,20}lost|"
            r"carries the full machine)",
            capabilities,
        )
        self.assertFalse(
            bool(unfinished and absolute_claim),
            "CAPABILITIES makes an absolute lossless/full-machine claim while "
            "the release manifest still has unfinished components:\n"
            + "\n".join(unfinished),
        )

    def test_capability_file_does_not_describe_restored_scripts_as_excluded(self) -> None:
        capabilities = (ROOT / "CAPABILITIES.md").read_text(encoding="utf-8")
        shipped_python = [
            path
            for path in ROOT.rglob("*.py")
            if ".git" not in path.parts and "__pycache__" not in path.parts
        ]
        stale = re.search(
            r"(?im)^\s*-\s*\*\*Scripts\*\*\s*[—-]\s*excluded\b",
            capabilities,
        )
        self.assertFalse(
            bool(stale and shipped_python),
            "CAPABILITIES says scripts are excluded even though public "
            f"Python runtime is shipped ({len(shipped_python)} files).",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
