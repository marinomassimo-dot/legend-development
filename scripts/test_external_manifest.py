#!/usr/bin/env python3
"""Validate the public external-workshop routing contract."""

from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "_external_repos" / "MANIFEST.md"
ALLOWED_STATUSES = {"DESCRIBED", "AUDITED", "REPRODUCED", "REJECTED"}
MINIMUM_ROUTES = 37


def operational_rows() -> list[list[str]]:
    text = MANIFEST.read_text(encoding="utf-8")
    section = text.split("## Complete operational routing inventory", 1)[1]
    section = section.split("\n## ", 1)[0]
    rows = []
    in_table = False
    for line in section.splitlines():
        if line.startswith("| Tool/resource |"):
            in_table = True
            continue
        if not in_table or not line.startswith("|"):
            continue
        if re.match(r"^\|[-|]+\|$", line.replace(" ", "")):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        rows.append(cells)
    return rows


class ExternalManifestTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.rows = operational_rows()

    def test_complete_inventory_has_expected_breadth(self) -> None:
        self.assertGreaterEqual(len(self.rows), MINIMUM_ROUTES)

    def test_tool_names_are_unique(self) -> None:
        names = [row[0].strip("`") for row in self.rows if row]
        self.assertEqual(len(names), len(set(names)))

    def test_every_route_satisfies_the_seven_field_contract(self) -> None:
        failures = []
        for row in self.rows:
            if len(row) != 7:
                failures.append(f"wrong field count {len(row)}: {row}")
                continue
            tool, capability, location, pin, licence, runtime, status = row
            if not all((tool, capability, location, pin, licence, runtime, status)):
                failures.append(f"empty field: {tool or row}")
            if not (
                "https://" in location
                or "http://" in location
                or "bundled under" in location
            ):
                failures.append(f"{tool}: no public/bundled location")
            if status not in ALLOWED_STATUSES:
                failures.append(f"{tool}: invalid status {status}")
            if status == "REJECTED" and "DO NOT USE" not in licence:
                failures.append(f"{tool}: rejected route lacks DO NOT USE")
            if "/" in pin and not pin.startswith("`"):
                failures.append(f"{tool}: ambiguous pin {pin}")
        self.assertFalse(failures, "\n".join(failures))

    def test_superpowers_is_explicitly_external_and_unpinned(self) -> None:
        matches = [row for row in self.rows if row[0] == "Superpowers plugin"]
        self.assertEqual(1, len(matches))
        self.assertEqual("UNPINNED", matches[0][3])
        self.assertEqual("DESCRIBED", matches[0][6])


if __name__ == "__main__":
    unittest.main(verbosity=2)
