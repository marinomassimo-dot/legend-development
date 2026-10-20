#!/usr/bin/env python3
"""Regression for manifest_scaffold.py: digests computed, absent artefact refused, overwrite refused."""
import hashlib, json, sys, tempfile, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import manifest_scaffold as m


def spec(path):
    return dict(pmid="1", doi="10.1/x", receipt="FTR-1", group_assessment={}, field_density={}, multihop={},
                corpus_crossquery={}, retraction_result="ok", indexed_evidence="e",
                artifacts=[dict(path=path, kind="article_text", note="n")], entries=[])


class Scaffold(unittest.TestCase):
    def test_digest_is_computed_from_the_file(self):
        with tempfile.TemporaryDirectory() as d:
            d = Path(d); (d / "a.xml").write_bytes(b"abc")
            out = m.build(spec("a.xml"), d)
            self.assertEqual(out["source_artifacts"][0]["sha256"], hashlib.sha256(b"abc").hexdigest())
            self.assertEqual(out["schema_version"], 2)

    def test_absent_artefact_and_missing_slot_are_refused(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(FileNotFoundError):
                m.build(spec("nope.xml"), Path(d))
            s = spec("a.xml"); del s["multihop"]
            with self.assertRaises(ValueError):
                m.build(s, Path(d))

    def test_cli_refuses_overwrite(self):
        with tempfile.TemporaryDirectory() as d:
            d = Path(d); (d / "a.xml").write_bytes(b"abc"); (d / "s.json").write_text(json.dumps(spec("a.xml")))
            args = ["--spec", str(d / "s.json"), "--root", str(d), "--out", str(d)]
            self.assertEqual(m.main(args), 0)
            self.assertEqual(m.main(args), 3)
            self.assertEqual(m.main(args + ["--force"]), 0)


if __name__ == "__main__":
    unittest.main()
