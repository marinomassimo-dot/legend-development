#!/usr/bin/env python3
"""Regressions for discovery_lead.py — the discovery ledger's validated writer (N2, 2026-10-20)."""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import discovery_lead as dl  # noqa: E402

LEDGER_TEXT = """# Discovery Ledger

## MECH — indizi

### DL-MECH-007 — An older lead

- **Tag:** IPOTESI
- **Status:** open

### DL-BIO-002 — A biomarker lead

- **Tag:** DATO
"""


def spec(**overrides) -> dict:
    base = {"kind": "MECH", "title": "A new lead from a reading",
            "tag": "DATO + INFERENZA", "source": "scientist-b, task T, receipt FTR-X-01",
            "causal_statement": "X lowers Y in system Z (measured).",
            "falsifier": "Y unchanged in Z with X knocked down.",
            "transfer_limit": "Z is not the reference genotype."}
    base.update(overrides)
    return base


class DiscoveryLeadWriter(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.ledger = self.root / dl.LEDGER.format(disease="wwox")
        self.ledger.parent.mkdir(parents=True)
        self.ledger.write_text(LEDGER_TEXT, encoding="utf-8")

    def write(self, name: str, data: dict) -> Path:
        path = self.root / name
        path.write_text(json.dumps(data), encoding="utf-8")
        return path

    def cli(self, *args: str) -> subprocess.CompletedProcess:
        return subprocess.run([sys.executable, str(HERE / "discovery_lead.py"), "--root",
                               str(self.root), *args], capture_output=True, text=True)

    def test_validation_names_every_reason(self) -> None:
        errors = dl.validate(spec(kind="X", tag="GUESS", status="done", title="",
                                  extra=1, source="mail me at a.b@example.org"))
        joined = "; ".join(errors)
        for needle in ("title", "kind", "tag", "status", "unknown", "e-mail"):
            self.assertIn(needle, joined)
        self.assertEqual([], dl.validate(spec()))

    def test_dry_run_numbers_and_writes_nothing(self) -> None:
        path = self.write("a.json", spec())
        lines = dl.append(self.root, "wwox", [path], apply=False)
        self.assertEqual(["WOULD APPEND DL-MECH-008 — A new lead from a reading  (a.json)"], lines)
        self.assertEqual(LEDGER_TEXT, self.ledger.read_text(encoding="utf-8"))

    def test_staged_leads_from_two_actors_get_distinct_numbers_and_append_once(self) -> None:
        for actor, title in (("scientist-a", "Lead A"), ("scientist-b", "Lead B")):
            src = self.write(f"{actor}.json", spec(title=title))
            result = self.cli("stage", str(src), "--actor", actor)
            self.assertEqual(0, result.returncode, result.stderr)
        result = self.cli("append", "--staged", "--apply")
        self.assertEqual(0, result.returncode, result.stderr)
        text = self.ledger.read_text(encoding="utf-8")
        self.assertIn("### DL-MECH-008 — Lead A", text)
        self.assertIn("### DL-MECH-009 — Lead B", text)
        self.assertEqual(1, text.count("leads appended by the validated writer"))
        again = self.cli("append", "--staged", "--apply")
        self.assertEqual(0, again.returncode, again.stderr)
        self.assertEqual(text, self.ledger.read_text(encoding="utf-8"), "not idempotent")
        # The appended record reads back whole, through the tool sessions use.
        self.assertIsNotNone(dl.HEADING.search(text))
        self.assertTrue(text.startswith(LEDGER_TEXT), "an existing byte moved")

    def test_one_bad_spec_appends_nothing(self) -> None:
        good = self.write("good.json", spec())
        bad = self.write("bad.json", spec(falsifier=""))
        with self.assertRaisesRegex(ValueError, "nothing appended"):
            dl.append(self.root, "wwox", [good, bad], apply=True)
        self.assertEqual(LEDGER_TEXT, self.ledger.read_text(encoding="utf-8"))

    def test_a_duplicate_title_and_an_existing_staged_file_are_refused(self) -> None:
        self.assertTrue(dl.validate(spec(title="An older lead"), LEDGER_TEXT))
        src = self.write("x.json", spec())
        self.assertEqual(0, self.cli("stage", str(src), "--actor", "scientist-c").returncode)
        self.assertNotEqual(0, self.cli("stage", str(src), "--actor", "scientist-c").returncode)

    def test_the_real_ledger_numbers_parse(self) -> None:
        real = HERE.parents[1] / dl.LEDGER.format(disease="wwox")
        if not real.is_file():
            self.skipTest("live ledger absent")
        numbers = dl.next_numbers(real.read_text(encoding="utf-8"))
        self.assertGreater(numbers["MECH"], 100)


if __name__ == "__main__":
    unittest.main(verbosity=2)
