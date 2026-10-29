#!/usr/bin/env python3
"""Regressions for receipt_linkage.py. Run: python3 -B framework/scripts/test_receipt_linkage.py -v"""
import json, sys, tempfile, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import receipt_linkage as rl  # noqa: E402


class Linkage(unittest.TestCase):
    def setUp(self):
        self.t = tempfile.TemporaryDirectory()
        self.root = Path(self.t.name)
        led = self.root / "disease-models" / "x" / "registries"
        led.mkdir(parents=True)
        (led / "fulltext_read_receipts.jsonl").write_text(
            json.dumps({"event_id": "FTR-20260101-1-01", "evidence_depth": "partial_fulltext_read", "event_at": "2026-01-02T00:00:00Z", "ledger_prev_hash": None}) + "\n")
        self.d = self.root / "docs"
        self.d.mkdir()

    def tearDown(self):
        self.t.cleanup()

    def render(self, text, **kw):
        (self.d / "a.md").write_text(text)
        return rl.render(self.root, self.d, "x", kw.get("stale_only", False))

    def test_recorded_event_named_staged_is_flagged_as_superseded(self):
        out = self.render("receipt FTR-20260101-1-01 staged for the integrator\n")
        self.assertIn("1 recorded in the ledger, 0 not; 1 citing lines", out)
        self.assertIn("RECORDED (partial_fulltext_read, 2026-01-02)", out)

    def test_unknown_event_is_reported_not_ledgered_and_not_flagged(self):
        out = self.render("receipt FTR-20260101-9-01 staged\n")
        self.assertIn("NOT IN LEDGER", out)
        self.assertIn("0 recorded in the ledger, 1 not; 0 citing lines", out)

    def test_recorded_event_without_stale_wording_is_not_flagged(self):
        out = self.render("see FTR-20260101-1-01 for the depth\n", stale_only=True)
        self.assertIn("0 citing lines", out)
        self.assertNotIn("Lines to read", out)


if __name__ == "__main__":
    unittest.main(verbosity=2)
