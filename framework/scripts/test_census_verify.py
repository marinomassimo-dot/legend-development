#!/usr/bin/env python3
"""Regressions for `census_verify.py`.

The defect these exist for is real and happened on 2026-09-22. A delegate's census asserted
eleven reagent terms were absent from the repository. The orchestrator verified it by grepping
the working tree — which by then held the delegate's own census file, naming all eleven. The
re-count came back non-zero and the census looked wrong. It was not wrong; the verification
surface was contaminated by the artefact under verification. A second attempt used
`grep --exclude`, which that deployment's grep ignores, and reproduced the same false mismatch.

`test_the_real_2026_09_22_contamination_is_caught` reproduces exactly that arrangement.

🔴 A fixture that only asserts detection is half a test. Every contamination case below is
paired with the CLEAN case it must not flag — otherwise a checker that reported contamination
unconditionally would pass every contamination test here and be worthless.

The second half of the file covers the ambiguity the tool itself exposed when it was first run
on that incident: `grep -c` counts LINES, `grep -o` counts OCCURRENCES, the two disagree
(cycloheximide: 78 vs 91), and a census almost never says which it used.
"""
from __future__ import annotations

import importlib.util
import subprocess
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("census_verify", HERE / "census_verify.py")
cv = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(cv)


def _run(cwd, *args):
    subprocess.run(args, cwd=cwd, check=True, capture_output=True)


class Fixture:
    """A throwaway git repo: one committed file, optionally one untracked file."""

    def __init__(self, committed: dict[str, str], untracked: dict[str, str] | None = None):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        _run(self.root, "git", "init", "-q")
        _run(self.root, "git", "config", "user.email", "t@example.invalid")
        _run(self.root, "git", "config", "user.name", "t")
        for name, body in committed.items():
            p = self.root / name
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(body, encoding="utf-8")
        _run(self.root, "git", "add", "-A")
        _run(self.root, "git", "commit", "-q", "-m", "fixture")
        for name, body in (untracked or {}).items():
            p = self.root / name
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(body, encoding="utf-8")

    def close(self):
        self.tmp.cleanup()


class ParseClaim(unittest.TestCase):
    def test_plain(self):
        self.assertEqual(cv.parse_claim("ataluren=0"), ("ataluren", 0))
        self.assertEqual(cv.parse_claim("cycloheximide=78"), ("cycloheximide", 78))

    def test_term_may_contain_an_equals_because_it_splits_on_the_last_one(self):
        self.assertEqual(cv.parse_claim("c.1057-2A>G=3"), ("c.1057-2A>G", 3))
        self.assertEqual(cv.parse_claim("a=b=7"), ("a=b", 7))

    def test_malformed_is_refused(self):
        for bad in ("ataluren", "=5", "ataluren=many", "ataluren="):
            with self.assertRaises(Exception, msg=f"{bad!r} should be refused"):
                cv.parse_claim(bad)


class Contamination(unittest.TestCase):
    def test_the_real_2026_09_22_contamination_is_caught(self):
        """The census file, written into the tree, names the terms it claims are absent."""
        f = Fixture(
            committed={"corpus/paper.md": "a paper about WWOX with no reagents in it\n"},
            untracked={"analysis/census.md": "terms searched: ataluren UPF2 readthrough — all zero\n"},
        )
        self.addCleanup(f.close)
        res = cv.verify([("ataluren", 0), ("UPF2", 0)], "HEAD", ["."],
                        word=True, icase=True, cwd=str(f.root))
        for row in res["rows"]:
            self.assertEqual(row["at_ref"], 0, row["term"])
            self.assertTrue(row["reproduces"], row["term"])
            self.assertGreater(row["in_worktree"], 0, row["term"])
            self.assertTrue(row["worktree_would_mislead"], row["term"])
            self.assertIn("analysis/census.md", row["contaminating_files"])

    def test_a_clean_tree_is_NOT_flagged(self):
        """The pair to the case above: no untracked file, so nothing may be reported."""
        f = Fixture(committed={"corpus/paper.md": "a paper about WWOX, no reagents\n"})
        self.addCleanup(f.close)
        res = cv.verify([("ataluren", 0)], "HEAD", ["."], word=True, icase=True, cwd=str(f.root))
        row = res["rows"][0]
        self.assertTrue(row["reproduces"])
        self.assertFalse(row["worktree_would_mislead"])
        self.assertEqual(row["contaminating_files"], [])
        self.assertEqual(res["contaminants"], {})

    def test_a_term_genuinely_present_at_the_ref_is_counted_there(self):
        """Contamination detection must not suppress real committed hits."""
        f = Fixture(
            committed={"corpus/paper.md": "we treated cells with cycloheximide\n"},
            untracked={"analysis/census.md": "cycloheximide cycloheximide\n"},
        )
        self.addCleanup(f.close)
        res = cv.verify([("cycloheximide", 1)], "HEAD", ["."], word=True, icase=True, cwd=str(f.root))
        row = res["rows"][0]
        self.assertEqual(row["at_ref"], 1)
        self.assertTrue(row["reproduces"])
        self.assertEqual(row["in_worktree"], 3)

    def test_a_wrong_claim_does_not_reproduce(self):
        f = Fixture(committed={"corpus/paper.md": "cycloheximide\n"})
        self.addCleanup(f.close)
        res = cv.verify([("cycloheximide", 9)], "HEAD", ["."], word=True, icase=True, cwd=str(f.root))
        self.assertFalse(res["rows"][0]["reproduces"])


class Metric(unittest.TestCase):
    def test_lines_and_occurrences_disagree_which_is_the_whole_point(self):
        """Two matches on one line: 1 line, 2 occurrences. A census saying '1' and a census
        saying '2' can both be right, which is why the metric must be stated."""
        f = Fixture(committed={"corpus/paper.md": "UPF1 and UPF1 again\nUPF1 alone\n"})
        self.addCleanup(f.close)
        occ = cv.verify([("UPF1", 3)], "HEAD", ["."], word=True, icase=True,
                        metric="occurrences", cwd=str(f.root))
        lines = cv.verify([("UPF1", 2)], "HEAD", ["."], word=True, icase=True,
                          metric="lines", cwd=str(f.root))
        self.assertTrue(occ["rows"][0]["reproduces"], "3 occurrences")
        self.assertTrue(lines["rows"][0]["reproduces"], "2 matching lines")
        self.assertEqual(occ["metric"], "occurrences")
        self.assertEqual(lines["metric"], "lines")

    def test_a_zero_is_a_zero_under_both_metrics(self):
        """Why the eleven claimed zeros were never ambiguous."""
        f = Fixture(committed={"corpus/paper.md": "nothing relevant here\n"})
        self.addCleanup(f.close)
        for metric in ("occurrences", "lines"):
            res = cv.verify([("ataluren", 0)], "HEAD", ["."], word=True, icase=True,
                            metric=metric, cwd=str(f.root))
            self.assertTrue(res["rows"][0]["reproduces"], metric)
            self.assertEqual(res["rows"][0]["at_ref"], 0, metric)


class WordAndCase(unittest.TestCase):
    def test_word_boundary_refuses_the_substring_trap(self):
        """The real one: bare 'ASE' matched 8842 times via database/phase/increase."""
        f = Fixture(committed={"corpus/paper.md": "database phase increase\n"})
        self.addCleanup(f.close)
        bounded = cv.verify([("ASE", 0)], "HEAD", ["."], word=True, icase=True, cwd=str(f.root))
        self.assertTrue(bounded["rows"][0]["reproduces"])
        unbounded = cv.verify([("ASE", 0)], "HEAD", ["."], word=False, icase=True, cwd=str(f.root))
        self.assertFalse(unbounded["rows"][0]["reproduces"],
                         "without -w the substring noise must reappear, or -w proves nothing")


class Render(unittest.TestCase):
    def test_metric_and_verdict_are_both_printed(self):
        f = Fixture(committed={"corpus/paper.md": "cycloheximide\n"})
        self.addCleanup(f.close)
        res = cv.verify([("cycloheximide", 1)], "HEAD", ["."], word=True, icase=True, cwd=str(f.root))
        out = cv.render(res)
        self.assertIn("metric: occurrences", out)
        self.assertIn("VERDICT: PASS", out)

    def test_contamination_is_named_in_the_output_not_merely_counted(self):
        f = Fixture(committed={"corpus/p.md": "x\n"}, untracked={"analysis/census.md": "ataluren\n"})
        self.addCleanup(f.close)
        res = cv.verify([("ataluren", 0)], "HEAD", ["."], word=True, icase=True, cwd=str(f.root))
        out = cv.render(res)
        self.assertIn("analysis/census.md", out)
        self.assertIn("CONTAMINATION", out)


if __name__ == "__main__":
    unittest.main(verbosity=2)
