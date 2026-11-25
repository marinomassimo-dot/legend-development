#!/usr/bin/env python3
"""Regressions for `held_content_check.py`: the shapes found on the held tree (ADV-279), on fixture bytes, no network."""
import contextlib
import io
import tempfile
import unittest
import zipfile
from pathlib import Path

import held_content_check as hc

JPEG = b"\xff\xd8\xff\xe0" + b"\x00" * 40
WEBP = b"RIFF\x10\x00\x00\x00WEBPVP8 " + b"\x00" * 20
PDF = b"%PDF-1.7\n" + b"0" * 40
CHALLENGE = b"<!DOCTYPE html><html><head><title>Just a moment...</title></head><body></body></html>"
NOT_FOUND = b"<!DOCTYPE html><html><head><title>HTTP 404 [Not Found]</title></head></html>"
ERROR_BEAN = b'<?xml version="1.0"?><ns4:errorBean xmlns:ns4="urn:x"><errMsg>no</errMsg></ns4:errorBean>'
ARTICLE = b"<?xml version='1.0'?><article><front><title>Error bean farming and the 404 locus</title></front></article>"


class Verdicts(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)

    def put(self, name: str, data: bytes) -> Path:
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        return path

    def test_each_shape_found_on_the_held_tree_is_unusable(self):
        for name, data in (("f1.jpg", b""), ("f2.jpg", CHALLENGE), ("f3.jpg", NOT_FOUND), ("a.pdf", CHALLENGE),
                           ("b.pdf", b'{"error":"PDF link has expired"}'), ("supp.zip", ERROR_BEAN),
                           ("cut.zip", b"PK\x03\x04" + b"\x00" * 30), ("t.xls", NOT_FOUND), ("page.html", CHALLENGE),
                           ("r.xml", ERROR_BEAN), ("empty.xml", b"")):
            with self.subTest(name=name):
                found = hc.check(self.put(name, data))
                self.assertIsNotNone(found)
                self.assertTrue(found[1], found)

    def test_real_files_and_an_article_that_names_an_error_are_not_listed(self):
        archive = self.root / "ok.zip"
        with zipfile.ZipFile(archive, "w") as handle:
            handle.writestr("a.txt", "x")
        for path in (self.put("f.jpg", JPEG), self.put("p.pdf", PDF), self.put("art.xml", ARTICLE), archive,
                     self.put("long.html", CHALLENGE + b" " * hc.INTERSTITIAL_MAX), self.put("notes.log", b"")):
            with self.subTest(name=path.name):
                self.assertIsNone(hc.check(path))

    def test_an_image_under_another_image_name_is_readable(self):
        reason, unusable = hc.check(self.put("fig.gif", WEBP))
        self.assertFalse(unusable)
        self.assertIn("webp", reason)

    def run_main(self, *argv):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = hc.main(list(argv))
        return code, out.getvalue(), err.getvalue()

    def test_exit_codes_and_what_is_printed(self):
        self.put("good/f.jpg", JPEG)
        self.put("good/fig.gif", WEBP)
        code, out, _ = self.run_main(str(self.root / "good"))
        self.assertEqual((code, out), (0, ""))
        self.assertIn("fig.gif", self.run_main(str(self.root / "good"), "--names")[1])
        bad = self.put("bad/f.pdf", CHALLENGE)
        code, out, err = self.run_main(str(bad))
        self.assertEqual(code, 1)
        self.assertEqual(out.split("\t")[0], "bot challenge page")
        self.assertIn("1 unusable", err)
        self.assertEqual(self.run_main(str(self.root / "absent"))[0], 2)

    def test_skipped_folders_and_symlinks_are_not_opened(self):
        self.put(f"tree/{hc.SKIP_DIRS[0]}/sealed.pdf", b"")
        self.put("tree/ok.pdf", PDF)
        (self.root / "tree" / "loop").symlink_to(self.root / "tree")
        self.assertEqual([p.name for p in hc.walk([self.root / "tree"])], ["ok.pdf"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
