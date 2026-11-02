#!/usr/bin/env python3
"""Tests for check_reference.py (IT19 P5 step 2). Run: python3 test_check_reference.py"""
import contextlib
import io
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import check_reference as cr  # noqa: E402

SEL = [{"pair_id": "P01", "need_id": "N1", "parent_chembl_id": "C1"}]


def row(**kw):
    base = {"pair_id": "P01", "need_id": "N1", "parent_chembl_id": "C1", "compound": "x",
            "reference_label": "compatible", "status": "determinate_functional",
            "target_at_measured_resolution": "Cav3.2", "action_and_context": "block",
            "measure_type": "functional electrophysiology", "source_kind": "abstract",
            "source_locator": "PubMed:1 abstract", "dependency_on_module_sources": "independent_of_module_input",
            "resolution_note": "measured on a need gene", "error_attribution": "none"}
    base.update(kw)
    return base


class Checks(unittest.TestCase):
    def test_clean_table_passes(self):
        errs, summary = cr.check(SEL, [row()])
        self.assertEqual(errs, [])
        self.assertEqual(summary["usable_rows"], 1)

    def test_binding_only_cannot_give_a_direction(self):
        errs, _ = cr.check(SEL, [row(measure_type="radioligand binding only")])
        self.assertTrue(any("binding-only" in e for e in errs))

    def test_unknown_must_say_what_is_missing(self):
        errs, _ = cr.check(SEL, [row(reference_label="unknown", status="unknown_no_source_in_bounded_search", resolution_note="")])
        self.assertTrue(any("does not state what is missing" in e for e in errs))

    def test_label_status_and_dependency_vocabularies(self):
        errs, _ = cr.check(SEL, [row(reference_label="likely")])
        self.assertTrue(any("outside the vocabulary" in e for e in errs))
        errs, _ = cr.check(SEL, [row(dependency_on_module_sources="trust me")])
        self.assertTrue(any("dependency" in e for e in errs))
        errs, _ = cr.check(SEL, [row(status="looks_right")])
        self.assertTrue(any("determinate label with status" in e for e in errs))

    def test_missing_pair_is_reported(self):
        errs, _ = cr.check(SEL + [{"pair_id": "P02", "need_id": "N1", "parent_chembl_id": "C2"}], [row()])
        self.assertTrue(any("pair ids differ" in e for e in errs))

    def test_real_tables_are_clean(self):
        errs, summary = cr.check(cr.read_tsv(HERE / "selection.tsv"), cr.read_tsv(HERE / "reference_it19_p5.tsv"))
        self.assertEqual(errs, [])
        self.assertEqual(summary["rows"], 32)

    def test_help_is_safe(self):
        with tempfile.TemporaryDirectory() as d:
            r = subprocess.run([sys.executable, str(HERE / "check_reference.py"), "--help"], cwd=d, capture_output=True, text=True)
            self.assertEqual(r.returncode, 0)
            self.assertEqual(list(Path(d).iterdir()), [])
        with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
            cr.main([])


if __name__ == "__main__":
    unittest.main(verbosity=2)
