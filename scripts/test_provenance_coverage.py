#!/usr/bin/env python3
"""Verify provenance coverage and integrity anchors for public analysis assets."""

from __future__ import annotations

import fnmatch
import hashlib
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DISEASE = ROOT / "disease-models" / "wwox"
DATA = DISEASE / "analysis" / "data"
DATA_SOURCES = ROOT / "DATA_SOURCES.md"
NOTICES = ROOT / "THIRD_PARTY_NOTICES.md"
SOURCE_NAMES = {
    "AlphaFold": re.compile(r"\bAlphaFold\b", re.I),
    "ClinVar": re.compile(r"\bClinVar\b", re.I),
    "GTEx": re.compile(r"\bGTEx\b", re.I),
    "ESM-2": re.compile(r"\bESM-?2\b", re.I),
    "ThermoMPNN": re.compile(r"\bThermoMPNN\b", re.I),
    "Monarch": re.compile(r"\bMonarch\b", re.I),
    "DisMech": re.compile(r"\bDisMech\b", re.I),
}
OPTIONAL_SOFTWARE = {
    "numpy": "NumPy",
    "openmm": "OpenMM",
    "pdbfixer": "PDBFixer",
    "mdtraj": "MDTraj",
}
HASH_ROW = re.compile(
    r"^\|\s*`(?P<path>analysis/data/[^`]+)`\s*\|\s*"
    r"`(?P<sha>[0-9a-f]{64})`\s*\|$"
)
PATH_ROW = re.compile(r"^\|\s*`(?P<path>analysis/data/[^`]+)`\s*\|")


def markdown_corpus() -> str:
    return "\n".join(
        path.read_text(encoding="utf-8", errors="replace")
        for path in sorted(DISEASE.rglob("*.md"))
    )


def documented_asset_patterns(text: str) -> list[str]:
    return [
        match.group("path")
        for line in text.splitlines()
        if (match := PATH_ROW.match(line))
    ]


class ProvenanceCoverageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sources = DATA_SOURCES.read_text(encoding="utf-8")
        cls.notices = NOTICES.read_text(encoding="utf-8")
        cls.corpus = markdown_corpus()

    def test_every_cited_named_source_has_provenance_and_notice(self) -> None:
        missing = []
        for name, pattern in SOURCE_NAMES.items():
            if not pattern.search(self.corpus):
                continue
            if not pattern.search(self.sources):
                missing.append(f"{name}: missing from DATA_SOURCES.md")
            if not pattern.search(self.notices):
                missing.append(f"{name}: missing from THIRD_PARTY_NOTICES.md")
        self.assertFalse(missing, "\n".join(missing))

    def test_source_matrix_declares_licence_and_publication_status(self) -> None:
        failures = []
        matrix_lines = [
            line for line in self.sources.splitlines()
            if line.startswith("|") and not line.startswith("|---")
        ]
        for name, pattern in SOURCE_NAMES.items():
            if not pattern.search(self.corpus):
                continue
            rows = [line for line in matrix_lines if pattern.search(line)]
            valid = any(
                re.search(r"\b(PUBLIC|MIXED)\b", row)
                and re.search(
                    r"\b(CC BY|MIT|BSD-3-Clause|Public download|Open-access)\b",
                    row,
                    re.I,
                )
                for row in rows
            )
            if not valid:
                failures.append(f"{name}: no matrix row with licence + status")
        self.assertFalse(failures, "\n".join(failures))

    def test_notices_repeat_licence_and_publication_status(self) -> None:
        """The notice must stand alone; readers should not infer DATA status."""
        failures = []
        notice_rows = [
            line for line in self.notices.splitlines()
            if line.startswith("|") and not line.startswith("|---")
        ]
        for name, pattern in SOURCE_NAMES.items():
            if not pattern.search(self.corpus):
                continue
            rows = [line for line in notice_rows if pattern.search(line)]
            valid = any(
                re.search(r"\b(PUBLIC|MIXED)\b", row)
                and re.search(
                    r"\b(CC BY|MIT|BSD-3-Clause|Public distribution|"
                    r"Open aggregate)\b",
                    row,
                    re.I,
                )
                for row in rows
            )
            if not valid:
                failures.append(
                    f"{name}: THIRD_PARTY_NOTICES lacks licence + status row"
                )
        self.assertFalse(failures, "\n".join(failures))

    def test_every_shipped_analysis_asset_has_a_documented_row(self) -> None:
        patterns = documented_asset_patterns(self.sources)
        uncovered = []
        for asset in sorted(path for path in DATA.rglob("*") if path.is_file()):
            relative = asset.relative_to(DISEASE).as_posix()
            if not any(fnmatch.fnmatch(relative, pattern) for pattern in patterns):
                uncovered.append(relative)
        self.assertFalse(uncovered, "Uncovered assets:\n" + "\n".join(uncovered))

    def test_declared_integrity_anchors_match_bytes(self) -> None:
        failures = []
        anchors = []
        for line in self.sources.splitlines():
            match = HASH_ROW.match(line)
            if match:
                anchors.append((match.group("path"), match.group("sha")))
        self.assertGreaterEqual(len(anchors), 4)
        for relative, expected in anchors:
            artifact = DISEASE / relative
            if not artifact.is_file():
                failures.append(f"{relative}: missing")
                continue
            observed = hashlib.sha256(artifact.read_bytes()).hexdigest()
            if observed != expected:
                failures.append(
                    f"{relative}: expected {expected}, observed {observed}"
                )
        self.assertFalse(failures, "\n".join(failures))

    def test_optional_environment_dependencies_have_notices(self) -> None:
        environment = (ROOT / "environment-md.yml").read_text(
            encoding="utf-8"
        ).lower()
        failures = []
        for package, display_name in OPTIONAL_SOFTWARE.items():
            if not re.search(rf"^\s*-\s*{re.escape(package)}=", environment, re.M):
                failures.append(f"{display_name}: absent from environment-md.yml")
                continue
            if display_name.lower() not in self.sources.lower():
                failures.append(f"{display_name}: absent from DATA_SOURCES.md")
            if display_name.lower() not in self.notices.lower():
                failures.append(
                    f"{display_name}: absent from THIRD_PARTY_NOTICES.md"
                )
        self.assertFalse(failures, "\n".join(failures))

    def test_release_analysis_dependencies_have_versioned_notices(self) -> None:
        requirements = (
            ROOT / "requirements-analysis.txt"
        ).read_text(encoding="utf-8")
        dependencies = []
        for line in requirements.splitlines():
            value = line.strip()
            if not value or value.startswith("#"):
                continue
            match = re.fullmatch(
                r"(?P<package>[A-Za-z0-9_.-]+)==(?P<version>[A-Za-z0-9_.+-]+)",
                value,
            )
            self.assertIsNotNone(
                match,
                f"Release dependency must be exactly pinned: {value}",
            )
            dependencies.append(
                (match.group("package"), match.group("version"))
            )
        self.assertTrue(dependencies, "No release-analysis dependencies found")
        missing = [
            f"{package} {version}"
            for package, version in dependencies
            if package.casefold() not in self.notices.casefold()
            or version not in self.notices
        ]
        self.assertFalse(
            missing,
            "Versioned release dependencies missing from notices:\n"
            + "\n".join(missing),
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
