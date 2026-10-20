#!/usr/bin/env python3
"""Regressions for figure_legend_pairs.py and the blind triple sampler in locator_audit.py (N7)."""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import figure_legend_pairs as flp  # noqa: E402

# The measured shape: the deposit's g002 is Figure 1 and g001 is Figure 2.
XML = """<article xmlns:xlink="http://www.w3.org/1999/xlink"><body>
<fig id="f1"><label>Figure 1</label><caption><p>Symptom timeline.</p></caption>
  <graphic xlink:href="pone.g002"/></fig>
<fig id="f2"><label>Fig. 2.</label><caption><title>Pathway.</title><p>Bile acids.</p></caption>
  <graphic xlink:href="pone.g001"/></fig>
<fig id="f3"><label>Figure 3</label><caption><p>Blots.</p></caption>
  <graphic xlink:href="pone.g003"/></fig>
</body></article>"""


class FigureLegendPairs(unittest.TestCase):
    def test_the_swapped_deposit_is_flagged_and_the_matching_one_is_not(self) -> None:
        rows = {r["id"]: r for r in flp.pairs(XML)}
        self.assertEqual(["pone.g002"], rows["f1"]["graphics"])
        self.assertIn("NUMBER_DIFFERS", rows["f1"]["flags"])
        self.assertIn("NUMBER_DIFFERS", rows["f2"]["flags"])
        self.assertEqual([], rows["f3"]["flags"])
        self.assertTrue(rows["f2"]["caption"].startswith("Pathway."))

    def test_files_are_matched_by_exact_stem_and_a_missing_one_is_named(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            figures = Path(tmp)
            (figures / "pone.g002.jpg").write_bytes(b"x")
            (figures / "pone.g0010.jpg").write_bytes(b"x")  # must not satisfy g001
            rows = {r["id"]: r for r in flp.pairs(XML, figures)}
            self.assertEqual(["pone.g002.jpg"], rows["f1"]["on_disk"]["pone.g002"])
            self.assertIn("MISSING_FILE", rows["f2"]["flags"])

    def test_unreadable_xml_exits_2(self) -> None:
        with tempfile.NamedTemporaryFile("w", suffix=".xml", delete=False) as handle:
            handle.write("<article><fig>")
        result = subprocess.run([sys.executable, str(HERE / "figure_legend_pairs.py"),
                                 handle.name], capture_output=True, text=True)
        Path(handle.name).unlink()
        self.assertEqual(2, result.returncode)


class BlindTriples(unittest.TestCase):
    def test_the_packet_carries_triples_and_nothing_else(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            manifests = root / "disease-models/wwox/research/deepdive_manifests"
            manifests.mkdir(parents=True)
            entries = [{"proposition": f"P{i}", "snippet": f"Q{i}", "anchor": f"A{i}",
                        "surface": "body", "artifact": "files/x.xml",
                        "experimental_context": {"system": "secret-reader-context"}}
                       for i in range(10)]
            (manifests / "PMID12345678.json").write_text(json.dumps({
                "receipt": "FTR-READER-01", "group_assessment": "reader's view",
                "verbatim_locators": {"entries": entries}}), encoding="utf-8")
            run = lambda *a: subprocess.run(  # noqa: E731
                [sys.executable, str(HERE / "locator_audit.py"), "--root", str(root),
                 "--pmid", "12345678", *a], capture_output=True, text=True)
            first, second = run("--triples", "4"), run("--triples", "4")
            self.assertEqual(0, first.returncode, first.stderr)
            self.assertEqual(first.stdout, second.stdout, "the sample is reproducible")
            packet = json.loads(first.stdout)
            self.assertEqual((4, 10), (packet["sampled"], packet["of"]))
            for leak in ("FTR-READER-01", "reader's view", "secret-reader-context"):
                self.assertNotIn(leak, first.stdout)
            self.assertEqual(10, json.loads(run("--triples", "0").stdout)["sampled"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
