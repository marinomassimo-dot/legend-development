#!/usr/bin/env python3
"""Catch mechanical rewrite scars in reader-facing public Markdown.

This is deliberately narrower than a style checker: it guards only malformed
cross-language substitutions and broken grammar patterns already observed
during de-identification. Content owners fix the prose; this test only reports
the exact residual locations.
"""

from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PUBLIC_PROSE_ROOTS = (
    ROOT / "framework" / "manuals",
    ROOT / "disease-models" / "wwox",
)

MALFORMED = (
    re.compile(r"(?i)\bTransferability-to-il\b"),
    re.compile(r"(?i)\bl'operatore rischio\b"),
    re.compile(r"(?i)\bmancal genotipo\b"),
    re.compile(r"(?i)\bdel the\b"),
    re.compile(r"(?i)\bpossiede both\b"),
    re.compile(r"(?i)\bfor both worked-example alleles\b"),
    re.compile(r"(?i)\bof the splice-site allele\b"),
)


def reader_facing_markdown():
    for base in PUBLIC_PROSE_ROOTS:
        for path in sorted(base.rglob("*.md")):
            # Retained third-party/legacy reports are provenance artifacts, not
            # public narrative rewritten by this project.
            if "analysis/data" in path.relative_to(ROOT).as_posix():
                continue
            yield path


class PublicProseQualityTests(unittest.TestCase):
    def test_no_known_mechanical_rewrite_scars(self) -> None:
        findings = []
        for path in reader_facing_markdown():
            for number, line in enumerate(
                path.read_text(encoding="utf-8").splitlines(), 1
            ):
                if any(pattern.search(line) for pattern in MALFORMED):
                    findings.append(
                        f"{path.relative_to(ROOT)}:{number}: {line.strip()}"
                    )
        self.assertFalse(
            findings,
            "Mechanical de-identification/translation scars remain:\n"
            + "\n".join(findings),
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
