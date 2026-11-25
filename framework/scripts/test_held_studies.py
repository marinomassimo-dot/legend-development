#!/usr/bin/env python3
"""Regressions for `held_studies.py`: a fixture `files/` with a misnamed file, a hand-made ledger, no network."""
import contextlib
import hashlib
import io
import json
import os
import tempfile
import unittest
from pathlib import Path

import debt_report
import held_studies as hs

PARTIAL = "partial_fulltext_read"
NAMED, MISNAMED, GONE = b"named by pmid", b"held under another name", b"bytes nobody kept"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def receipt(n, pmid=None, doi=None, fingerprint=None, depth=PARTIAL, locator="", at="2026-01-01T00:00:00Z"):
    return {"record_kind": "contemporaneous_receipt", "event_id": f"FTR-20260101-X{n}-1", "event_at": at,
            "study_id": {k: v for k, v in (("pmid", pmid), ("doi", doi)) if v}, "evidence_depth": depth,
            "source_fingerprint": fingerprint, "source_locator": locator}


def fixture(tmp: str) -> Path:
    root = Path(tmp) / "repo"
    files = root / "files"
    (files / "fulltext" / "rescued").mkdir(parents=True)
    (files / "supplement").mkdir()
    (files / "fulltext" / "PMID11111111_Named2020.xml").write_bytes(NAMED)
    (files / "fulltext" / "rescued" / "PMC524435_article_page.html").write_bytes(MISNAMED)
    events = [receipt(1, pmid="11111111", fingerprint=sha(NAMED)),
              receipt(2, pmid="22222222", fingerprint=sha(MISNAMED)),
              receipt(3, pmid="33333333", fingerprint=sha(GONE)),
              receipt(4, pmid="44444444", fingerprint=None),
              receipt(5, doi="10.1/abc", fingerprint=sha(MISNAMED), depth="complete_fulltext_read")]
    ledger = root / hs.LEDGER
    ledger.parent.mkdir(parents=True)
    ledger.write_text("".join(json.dumps(e) + "\n" for e in events), encoding="utf-8")
    return root


class TheTwoRules(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = fixture(tmp.name)
        self.cache = Path(tmp.name) / "state" / "index.json"

    def measure(self, **kw):
        return hs.measure(self.root, self.cache, **kw)

    def test_a_misnamed_file_is_held_by_digest_and_its_path_is_named(self):
        rows, _ = self.measure()
        self.assertEqual(rows["11111111"]["held"], "name")
        self.assertEqual(rows["22222222"]["held"], "digest")
        self.assertTrue(rows["22222222"]["by_digest"][0].endswith("PMC524435_article_page.html"))
        self.assertEqual(rows["33333333"]["held"], "no")
        self.assertEqual(hs.counts(rows, PARTIAL), {"studies": 4, "held": 2, "held_by_name": 1, "held_by_digest_only": 1,
                                                    "not_held": 2, "not_held_without_any_digest": 1})
        self.assertEqual(rows["10.1/abc"]["held"], "digest")

    def test_the_second_run_hashes_nothing_and_a_changed_file_is_hashed_again(self):
        _, first = self.measure()
        self.assertEqual(first["hashed"], 2)
        self.assertEqual(self.measure()[1]["hashed"], 0)
        target = self.root / "files" / "fulltext" / "rescued" / "PMC524435_article_page.html"
        target.write_bytes(GONE)
        os.utime(target, ns=(1, 1))
        rows, again = self.measure()
        self.assertEqual(again["hashed"], 1)
        self.assertEqual((rows["22222222"]["held"], rows["33333333"]["held"]), ("no", "digest"))
        target.unlink()
        self.assertEqual(self.measure()[0]["33333333"]["held"], "no")

    def test_a_hard_link_is_hashed_once_and_a_symlink_is_not_evidence(self):
        folder = self.root / "files" / "supplement"
        os.link(self.root / "files" / "fulltext" / "PMID11111111_Named2020.xml", folder / "copy.xml")
        outside = self.root / "outside.bin"
        outside.write_bytes(GONE)
        os.symlink(outside, folder / "link.bin")
        rows, numbers = self.measure()
        self.assertEqual((numbers["files"], numbers["unique_inodes"], numbers["hashed"]), (3, 2, 2))
        self.assertEqual(rows["33333333"]["held"], "no")

    def test_an_extra_folder_counts_and_a_plain_run_keeps_its_cache_entry(self):
        extra = self.root / "rescue"
        extra.mkdir()
        (extra / "x.dat").write_bytes(GONE)
        self.assertEqual(self.measure(extra=[extra])[0]["33333333"]["held"], "digest")
        self.assertEqual(self.measure()[0]["33333333"]["held"], "no")
        self.assertEqual(self.measure(extra=[extra])[1]["hashed"], 0)

    def test_a_checkout_without_files_is_not_measured_rather_than_zero(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertIsNone(hs.measure(Path(tmp), self.cache))
            self.assertIn("not measured", debt_report.held_lines(Path(tmp), self.cache)[0][0])
        self.assertFalse(self.cache.exists())

    def test_the_debt_report_never_builds_the_index_cold_and_reads_it_once_built(self):
        lines, data = debt_report.held_lines(self.root, self.cache)
        self.assertIn("not indexed yet", lines[0])
        self.assertFalse(self.cache.exists())
        self.measure()
        lines, data = debt_report.held_lines(self.root, self.cache)
        self.assertIn("by digest only 1", lines[0])
        self.assertEqual(data["partial"]["not_held"], 2)

    def test_the_command_prints_counts_and_the_digest_only_rows(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = hs.main(["--root", str(self.root), "--cache", str(self.cache), "--rows", "digest"])
        self.assertEqual(code, 0)
        self.assertIn("by name 1, by digest only 1", out.getvalue())
        self.assertIn("22222222", out.getvalue())


if __name__ == "__main__":
    unittest.main(verbosity=2)
