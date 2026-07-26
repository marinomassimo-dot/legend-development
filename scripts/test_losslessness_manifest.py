#!/usr/bin/env python3
"""Fail-closed structural checks for the public losslessness manifest."""

from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "release" / "losslessness_manifest.json"
ALLOWED_STATUSES = {
    "PRESERVED",
    "RESTORED",
    "ABSTRACTED",
    "PARTIAL",
    "PENDING_CONTENT_REWRITE",
    "LEGACY_UNREPRODUCIBLE",
    "EXCLUDED_PRIVATE",
    "EXCLUDED_THIRD_PARTY",
}
MUST_EXIST = {
    "PRESERVED",
    "RESTORED",
    "ABSTRACTED",
    "PARTIAL",
    "LEGACY_UNREPRODUCIBLE",
    "EXCLUDED_THIRD_PARTY",
}


class LosslessnessManifestTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = json.loads(MANIFEST.read_text(encoding="utf-8"))
        cls.components = cls.payload["components"]

    def test_component_ids_are_unique(self) -> None:
        identifiers = [component["id"] for component in self.components]
        self.assertEqual(len(identifiers), len(set(identifiers)))

    def test_statuses_are_declared_and_allowed(self) -> None:
        vocabulary = set(self.payload["status_vocabulary"])
        self.assertEqual(vocabulary, ALLOWED_STATUSES)
        for component in self.components:
            self.assertIn(component["status"], ALLOWED_STATUSES)
            self.assertTrue(component["lane"])
            self.assertTrue(component["verification"])

    def test_represented_paths_exist(self) -> None:
        missing = []
        for component in self.components:
            if component["status"] not in MUST_EXIST:
                continue
            for relative in component.get("public_paths", []):
                if not (ROOT / relative).exists():
                    missing.append(f"{component['id']}: {relative}")
        self.assertFalse(missing, "Missing represented paths:\n" + "\n".join(missing))

    def test_pending_components_have_planned_targets(self) -> None:
        pending = [
            component for component in self.components
            if component["status"] == "PENDING_CONTENT_REWRITE"
        ]
        self.assertGreaterEqual(len(pending), 1)
        for component in pending:
            self.assertFalse(component.get("public_paths"))
            self.assertTrue(component.get("planned_public_paths"))

    def test_pending_targets_have_not_already_materialized(self) -> None:
        stale = []
        for component in self.components:
            if component["status"] != "PENDING_CONTENT_REWRITE":
                continue
            for relative in component.get("planned_public_paths", []):
                if (ROOT / relative).exists():
                    stale.append(f"{component['id']}: {relative}")
        self.assertFalse(
            stale,
            "Materialized targets must be reclassified out of PENDING:\n"
            + "\n".join(stale),
        )

    def test_manifest_paths_are_safe_repository_relative_paths(self) -> None:
        unsafe = []
        for component in self.components:
            for field in ("public_paths", "planned_public_paths"):
                for relative in component.get(field, []):
                    path = Path(relative)
                    if path.is_absolute() or ".." in path.parts:
                        unsafe.append(f"{component['id']} {field}: {relative}")
        self.assertFalse(unsafe, "\n".join(unsafe))

    def test_represented_statuses_have_public_paths(self) -> None:
        missing = []
        for component in self.components:
            if component["status"] not in MUST_EXIST:
                continue
            if not component.get("public_paths"):
                missing.append(component["id"])
        self.assertFalse(
            missing,
            "Represented components without public paths:\n" + "\n".join(missing),
        )

    def test_exclusions_are_not_silent(self) -> None:
        excluded = [
            component for component in self.components
            if component["status"].startswith("EXCLUDED_")
        ]
        self.assertGreaterEqual(len(excluded), 1)
        for component in excluded:
            self.assertTrue(component["source_class"])
            self.assertTrue(component["verification"])


if __name__ == "__main__":
    unittest.main()
