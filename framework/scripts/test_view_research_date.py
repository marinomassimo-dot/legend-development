#!/usr/bin/env python3
"""IT39: the published research-update date follows the evidence read, not the names of folders beside the module."""
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import repurposing_view as rv  # noqa: E402


def tree(receipt_dates=(), folders=()):
    t = Path(tempfile.mkdtemp())
    dr = t / "disease-models" / "wwox" / "research" / "drug_repurposing"
    dr.mkdir(parents=True)
    (t / "disease-models" / "wwox" / "registries").mkdir(parents=True)
    (t / "disease-models/wwox/registries/fulltext_read_receipts.jsonl").write_text("".join(json.dumps({"analysis_at": d + "T10:00:00Z"}) + "\n" for d in receipt_dates), encoding="utf-8")
    for f in folders:
        (dr / f).mkdir()
    return dr


class ResearchDate(unittest.TestCase):
    def test_a_new_or_renamed_folder_does_not_move_the_date(self):
        base = rv.research_update_date(tree(["2026-11-08"]), "2026-11-01")
        self.assertEqual(base, "2026-11-08")
        self.assertEqual(rv.research_update_date(tree(["2026-11-08"], ["stage_20261109", "renamed_20270101"]), "2026-11-01"), "2026-11-08")

    def test_a_newer_receipt_or_a_newer_given_date_moves_it(self):
        self.assertEqual(rv.research_update_date(tree(["2026-11-08", "2026-11-12"]), "2026-11-01"), "2026-11-12")
        self.assertEqual(rv.research_update_date(tree(["2026-11-08"]), "2026-11-20"), "2026-11-20")

    def test_no_dates_at_all_is_none(self):
        self.assertIsNone(rv.research_update_date(tree()))


if __name__ == "__main__":
    unittest.main(verbosity=2)
