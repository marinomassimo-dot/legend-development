#!/usr/bin/env python3
"""Regressions for `scoped_record_edit.py`.

Every test here is a REFUSAL test except three. That ratio is the point: the tool exists because
care was already being exercised on 2026-09-21 and still named the wrong element index, so what
must be exercised is the set of ways it says no.

Run: `python3 framework/scripts/test_scoped_record_edit.py`
"""
from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from scoped_record_edit import Refusal, scoped_edit  # noqa: E402


def record(event_id: str, basis: list[str], **extra) -> str:
    base = {
        "event_id": event_id,
        "record_kind": "contemporaneous_receipt",
        "study_id": {"pmid": "1", "doi": "10.0/x"},
        "evidence_depth": "partial_fulltext_read",
        "source_locator": "files/fulltext/x.txt",
        "source_fingerprint": "a" * 64,
        "coverage": {"abstract": "read"},
        "prior_receipt": None,
        "ledger_prev_hash": "b" * 64,
        "evidence_basis": basis,
    }
    base.update(extra)
    return json.dumps(base, sort_keys=True)


def ledger(*records: str) -> list[str]:
    return list(records) + [""]


ARGS = dict(id_key="event_id", field="evidence_basis.1", old="MATERNAL X", new="X",
            allow_interior=False)


class ScopedEditApplies(unittest.TestCase):
    def test_tail_record_one_field_one_occurrence(self):
        lines = ledger(record("A", ["keep", "a MATERNAL X fact", "keep"]))
        out, proof = scoped_edit(lines, record_id="A", **ARGS)
        after = json.loads(out[0])
        self.assertEqual(after["evidence_basis"][1], "a X fact")
        self.assertTrue(proof["is_tail"])
        self.assertEqual(proof["changed_top_level_keys"], ["evidence_basis"])

    def test_every_other_field_survives_byte_identical(self):
        before_line = record("A", ["keep", "a MATERNAL X fact"])
        out, _ = scoped_edit(ledger(before_line), record_id="A", **ARGS)
        before, after = json.loads(before_line), json.loads(out[0])
        for key in before:
            if key != "evidence_basis":
                self.assertEqual(before[key], after[key], key)
        self.assertEqual(before["evidence_basis"][0], after["evidence_basis"][0])

    def test_other_records_are_untouched(self):
        lines = ledger(record("A", ["a MATERNAL X fact"]), record("B", ["a MATERNAL X fact"]))
        out, _ = scoped_edit(lines, record_id="B", field="evidence_basis.0", id_key="event_id",
                             old="MATERNAL X", new="X", allow_interior=False)
        self.assertEqual(out[0], lines[0])
        self.assertEqual(json.loads(out[1])["evidence_basis"][0], "a X fact")


class ScopedEditRefuses(unittest.TestCase):
    def refuses(self, fragment, **kwargs):
        merged = {**ARGS, **kwargs}
        with self.assertRaises(Refusal) as caught:
            scoped_edit(merged.pop("lines"), record_id=merged.pop("record_id"), **merged)
        self.assertIn(fragment, str(caught.exception))

    def test_wrong_index_writes_nothing(self):
        # The 2026-09-21 incident, reproduced: the phrase is at index 3, the caller said 1.
        self.refuses("does not contain the authorized --old text",
                     lines=ledger(record("A", ["a", "b", "c", "a MATERNAL X fact"])),
                     record_id="A")

    def test_interior_record_refused_by_default(self):
        self.refuses("not the tail",
                     lines=ledger(record("A", ["x", "a MATERNAL X fact"]), record("B", ["y"])),
                     record_id="A")

    def test_interior_record_with_flag_still_names_the_breakage(self):
        lines = ledger(record("A", ["x", "a MATERNAL X fact"]), record("B", ["y"]))
        _, proof = scoped_edit(lines, record_id="A", **{**ARGS, "allow_interior": True})
        self.assertFalse(proof["is_tail"])  # the CLI refuses to write on this

    def test_ambiguous_occurrence_refused(self):
        self.refuses("2 times",
                     lines=ledger(record("A", ["x", "MATERNAL X and MATERNAL X"])),
                     record_id="A")

    def test_unknown_record_refused(self):
        self.refuses("no record has", lines=ledger(record("A", ["x", "a MATERNAL X fact"])),
                     record_id="Z")

    def test_duplicate_ids_refused_rather_than_guessed(self):
        self.refuses("share", lines=ledger(record("A", ["x", "a MATERNAL X fact"]),
                                           record("A", ["x", "a MATERNAL X fact"])),
                     record_id="A")

    def test_identity_field_is_never_editable(self):
        self.refuses("identity or integrity field",
                     lines=ledger(record("A", ["x"], note="a MATERNAL X fact")),
                     record_id="A", field="source_fingerprint", old="a" * 64, new="c" * 64)

    def test_no_op_substitution_refused(self):
        self.refuses("identical", lines=ledger(record("A", ["x", "a MATERNAL X fact"])),
                     record_id="A", old="X", new="X")

    def test_non_string_field_refused(self):
        self.refuses("not a string", lines=ledger(record("A", ["x"], n=3)),
                     record_id="A", field="n", old="3", new="4")

    def test_missing_key_refused(self):
        self.refuses("no key", lines=ledger(record("A", ["x", "a MATERNAL X fact"])),
                     record_id="A", field="nope.0")

    def test_index_out_of_range_refused(self):
        self.refuses("out of range", lines=ledger(record("A", ["x"])),
                     record_id="A", field="evidence_basis.9")

    def test_malformed_line_refused(self):
        self.refuses("not valid JSON", lines=["{not json}", ""], record_id="A")

    def test_empty_ledger_refused(self):
        self.refuses("no records", lines=[""], record_id="A")


if __name__ == "__main__":
    unittest.main(verbosity=2)
