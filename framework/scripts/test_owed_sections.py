#!/usr/bin/env python3
"""Regression for owed_sections.py: best-of-all-receipts, staged attribution, references apart."""
import json, sys, tempfile, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import owed_sections as o


def ev(eid, pmid, cov, kind="contemporaneous_receipt"):
    return {"event_id": eid, "record_kind": kind, "study_id": {"pmid": pmid}, "coverage": cov}


class OwedSections(unittest.TestCase):
    def run_case(self, ledger_events, staged=None):
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            (d / "l.jsonl").write_text("\n".join(json.dumps(e) for e in ledger_events) + "\n")
            st = d / "stg"
            for actor, e in (staged or []):
                (st / actor).mkdir(parents=True, exist_ok=True)
                (st / actor / (e["event_id"] + ".json")).write_text(json.dumps(e))
            return o.census(o.load(d / "l.jsonl", st))

    def test_supplement_only_latest_receipt_does_not_hide_the_body(self):
        r = self.run_case([ev("A", "1", {"results": "read", "figures": "captions_only"}),
                           ev("B", "1", {"results": "not_read", "figures": "not_read", "supplementary": "read"})])
        self.assertEqual(r["1"]["owed"], {"figures": "captions_only"})

    def test_staged_receipt_closes_debt_and_names_actor(self):
        r = self.run_case([ev("A", "2", {"figures": "captions_only"})],
                          [("scientist-x", ev("S", "2", {"figures": "read"}))])
        self.assertEqual(r["2"]["owed"], {})
        self.assertEqual(r["2"]["staged_by"], ["scientist-x"])

    def test_references_reported_apart_and_legacy_ignored(self):
        r = self.run_case([ev("L", "3", {"figures": "unknown_legacy"}, "legacy_reconstruction"),
                           ev("A", "3", {"results": "read", "references": "not_read"})])
        self.assertEqual(r["3"]["owed"], {})
        self.assertEqual(r["3"]["references"], "not_read")


if __name__ == "__main__":
    unittest.main(verbosity=2)
