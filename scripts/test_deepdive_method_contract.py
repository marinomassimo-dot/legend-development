#!/usr/bin/env python3
"""Check that the public deep-dive package retains the reusable method."""

from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / ".claude" / "skills" / "legend-deepdive"
MANUAL = ROOT / "framework" / "manuals" / "deep_dive_manual.md"


class DeepDiveMethodContractTests(unittest.TestCase):
    def test_deepdive_method_invariants_are_explicit(self) -> None:
        paths = [
            path.read_text(encoding="utf-8")
            for path in sorted(PACKAGE.rglob("*.md"))
        ]
        self.assertTrue(paths, "Public legend-deepdive package is empty")
        self.assertTrue(MANUAL.is_file(), "Public deep-dive manual is missing")
        paths.append(MANUAL.read_text(encoding="utf-8"))
        corpus = "\n".join(paths)
        contracts = {
            "neutral vertical pass before system integration":
                r"(?is)(?:two[- ]pass|neutral|vertical).{0,240}"
                r"(?:horizontal|orizzontale|system integration|canonical)",
            "active tension/contradiction pass":
                r"(?i)(?:tension pass|actively search.{0,100}(?:challenge|contradict)|"
                r"what (?:the paper|study) challenges)",
            "evidence type and recency kept as separate axes":
                r"(?is)(?:evidence type|study type|\bTIPO\b).{0,220}"
                r"(?:recency|currency)",
            "DATO / INFERENZA / IPOTESI separation":
                r"(?is)\b(?:DATO|DATA)\b.{0,220}"
                r"\b(?:INFERENZA|INFERENCE)\b.{0,220}"
                r"\b(?:IPOTESI|HYPOTHESIS)\b",
            "deep biological mechanism output":
                r"(?i)(?:deep biological|biological mechanism|mechanistic core)",
            "cross-domain research expansion":
                r"(?is)(?:cross[- ]domain).{0,180}(?:research|expansion|connection)",
            "strategy space with repurposing and biomarkers":
                r"(?is)(?=.*strategy space)(?=.*repurpos)(?=.*biomarker)",
            "limits and uncertainty":
                r"(?i)(?:limits?\s*(?:and|&)\s*uncertaint|limitations?.{0,80}uncertaint)",
            "commit impact and change log":
                r"(?is)(?:commit impact).{0,220}(?:change log|changelog)",
            "methodology reflection/log":
                r"(?i)(?:methodology log|method reflection|process reflection)",
        }
        missing = [
            label
            for label, pattern in contracts.items()
            if not re.search(pattern, corpus)
        ]
        self.assertFalse(
            missing,
            "Public deep-dive method invariants missing:\n"
            + "\n".join(f"- {label}" for label in missing),
        )

    def test_skill_routes_to_the_full_manual(self) -> None:
        skill = (PACKAGE / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn(
            "framework/manuals/deep_dive_manual.md",
            skill,
            "The executable skill must route users to the full method manual.",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
