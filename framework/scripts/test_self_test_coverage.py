#!/usr/bin/env python3
"""Tests for self_test_coverage.py — the meta-test, tested against real history.

🔴 The case that matters is not synthetic. ``erratum_scope_check.py`` exists in this
repository in two states: at ``0e33f0f^`` its self-test reported **12/12 green while the tool
crashed corpus-wide**, because the self-test *"exercises parse_panel and intersects and never
calls check_manifest"*; at ``0e33f0f`` the orchestrator added two branch cases that call
``check_manifest`` itself. Both versions are in git. ``HistoricalDefect`` measures both and
asserts ``False`` then ``True``.

That is the whole claim of this tool, checked against the event that motivated it rather than
against a fixture written to match what the tool already does — which is the failure mode the
tool exists to detect, and would be an embarrassing one to commit here.

A meta-test whose own suite never drove its own entry point would be the same joke one level
up, so ``TheToolDrivesItself`` runs ``main()`` over a real subset of the real script tree.
"""

from __future__ import annotations

import io
import json
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import self_test_coverage as stc  # noqa: E402

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent

TOOL = '''#!/usr/bin/env python3
import argparse, sys

def helper(text):
    return text.strip().lower()

def do_work(path):
    return helper(open(path).read())

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    args = ap.parse_args()
    print(do_work(args.path))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
'''

SUITE_HELPER_ONLY = '''#!/usr/bin/env python3
import sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import widget

class T(unittest.TestCase):
    def test_helper(self):
        self.assertEqual(widget.helper("  A "), "a")

if __name__ == "__main__":
    unittest.main()
'''

SUITE_DRIVES_MAIN = '''#!/usr/bin/env python3
import subprocess, sys, tempfile, unittest
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import widget

class T(unittest.TestCase):
    def test_helper(self):
        self.assertEqual(widget.helper("  A "), "a")

    def test_cli(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "in.txt"
            target.write_text("HELLO")
            out = subprocess.run([sys.executable, str(HERE / "widget.py"), str(target)],
                                 capture_output=True, text=True)
            self.assertEqual(out.stdout.strip(), "hello")

if __name__ == "__main__":
    unittest.main()
'''

SUITE_SKIPS_FOR_ABSENT_BYTES = '''#!/usr/bin/env python3
import sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import widget

class T(unittest.TestCase):
    def test_helper(self):
        self.assertEqual(widget.helper("  A "), "a")

    @unittest.skip("real artefact absent: files/ is gitignored in this checkout")
    def test_real_artifact(self):
        pass

if __name__ == "__main__":
    unittest.main()
'''


def _tree(tmp: Path, suite: str) -> Path:
    scripts = tmp / "framework" / "scripts"
    scripts.mkdir(parents=True, exist_ok=True)
    (scripts / "widget.py").write_text(TOOL, encoding="utf-8")
    (scripts / "test_widget.py").write_text(suite, encoding="utf-8")
    return tmp


class EntryPointIsIdentifiedStatically(unittest.TestCase):
    def test_main_and_its_direct_callees(self) -> None:
        entry = stc.entry_point_of(TOOL)
        self.assertTrue(entry["main"])
        self.assertEqual(entry["callees"], ["do_work"])

    def test_a_self_test_dispatch_is_not_a_callee(self) -> None:
        """Otherwise `main` turning around into its own fixtures would count as driving it."""
        source = ("def self_test():\n    return 0\n\n"
                  "def work():\n    return 1\n\n"
                  "def main():\n    if True:\n        return self_test()\n    return work()\n")
        self.assertEqual(stc.entry_point_of(source)["callees"], ["work"])

    def test_a_module_without_main(self) -> None:
        entry = stc.entry_point_of("def f():\n    return 1\n")
        self.assertFalse(entry["main"])

    def test_self_test_detection_needs_a_real_flag_not_a_mention(self) -> None:
        """This module's own first version failed exactly here (see has_self_test)."""
        self.assertFalse(stc.has_self_test('"""Docs mentioning --self-test."""\n'))
        self.assertTrue(stc.has_self_test(
            'import argparse\n'
            'def main():\n'
            '    ap = argparse.ArgumentParser()\n'
            '    ap.add_argument("--self-test", action="store_true")\n'))


class SyntheticSuites(unittest.TestCase):
    """The two shapes, built from scratch, with nothing else different between them."""

    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = Path(self._tmp.name)
        self.addCleanup(self._tmp.cleanup)
        self.tracer = stc._tracer_dir()

    def _measure(self, suite: str) -> dict:
        root = _tree(self.tmp, suite)
        return stc.measure_script(root / "framework" / "scripts" / "widget.py",
                                  self.tracer, root, timeout=120)

    def test_a_suite_that_only_calls_a_helper_is_false(self) -> None:
        row = self._measure(SUITE_HELPER_ONLY)
        self.assertEqual(row["suites"][0]["rc"], 0, "the suite itself is green")
        self.assertFalse(row["entry_point_called"])

    def test_a_suite_that_drives_the_cli_in_a_subprocess_is_true(self) -> None:
        """The instrumentation must see into child processes, or every CLI reads as untested."""
        row = self._measure(SUITE_DRIVES_MAIN)
        self.assertTrue(row["entry_point_called"])
        self.assertTrue(row["entry_point_evidence"]["main_entered"])
        self.assertEqual(row["entry_point_evidence"]["callees_entered"], ["do_work"])

    def test_absent_bytes_degrade_to_a_declared_skip_not_to_a_false_green(self) -> None:
        """🔴 files/ is gitignored: 398 of 616 declared artefacts are absent from this checkout.

        A real-artefact case that silently passes when the bytes are missing is the same
        defect this tool exists to detect, one level up. It must be visible as a skip.
        """
        self.assertEqual(self._measure(SUITE_HELPER_ONLY)["real_artifact_case"], "false")
        self.assertEqual(
            self._measure(SUITE_SKIPS_FOR_ABSENT_BYTES)["real_artifact_case"],
            "skipped_declared")

    def test_a_case_reading_a_corpus_root_is_true(self) -> None:
        root = _tree(self.tmp, SUITE_HELPER_ONLY)
        corpus = root / "disease-models" / "wwox"
        corpus.mkdir(parents=True)
        (corpus / "artefact.json").write_text("{}", encoding="utf-8")
        (root / "framework" / "scripts" / "test_widget.py").write_text(
            SUITE_HELPER_ONLY.replace(
                'self.assertEqual(widget.helper("  A "), "a")',
                'self.assertEqual(widget.helper("  A "), "a")\n'
                '        widget.do_work(str(Path(__file__).resolve().parents[2] '
                '/ "disease-models" / "wwox" / "artefact.json"))'),
            encoding="utf-8")
        row = stc.measure_script(root / "framework" / "scripts" / "widget.py",
                                 self.tracer, root, timeout=120)
        self.assertEqual(row["real_artifact_case"], "true")
        self.assertIn("disease-models/wwox/artefact.json", row["real_artifact_paths"])


class HistoricalDefect(unittest.TestCase):
    """🔴 The real case: erratum_scope_check.py before and after commit 0e33f0f.

    Before, its self-test was 12/12 green and the tool crashed on every corpus-wide run. This
    is the measurement that proves the criterion is the right one — a fixture written by the
    tool's own author could not.
    """

    REPAIR = "0e33f0f"

    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = Path(self._tmp.name)
        self.addCleanup(self._tmp.cleanup)
        self.tracer = stc._tracer_dir()

    def _version(self, rev: str) -> str:
        result = subprocess.run(
            ["git", "show", f"{rev}:framework/scripts/erratum_scope_check.py"],
            cwd=str(ROOT), capture_output=True, text=True)
        if result.returncode != 0:
            self.skipTest(f"history absent from this checkout: {rev} ({result.stderr.strip()})")
        return result.stdout

    def _measure(self, source: str) -> dict:
        scripts = self.tmp / "framework" / "scripts"
        scripts.mkdir(parents=True, exist_ok=True)
        target = scripts / "erratum_scope_check.py"
        target.write_text(source, encoding="utf-8")
        return stc.measure_script(target, self.tracer, self.tmp, timeout=300)

    def test_before_the_repair_the_self_test_is_green_and_never_calls_the_tool(self) -> None:
        row = self._measure(self._version(f"{self.REPAIR}^"))
        self.assertEqual(row["suites"][0]["rc"], 0,
                         "the historical self-test passed — that is the entire problem")
        self.assertIn("check_manifest", row["entry_point"]["callees"])
        self.assertFalse(row["entry_point_called"])
        self.assertEqual(row["entry_point_evidence"]["callees_entered"], [])

    def test_after_the_repair_the_self_test_calls_the_tool(self) -> None:
        row = self._measure(self._version(self.REPAIR))
        self.assertEqual(row["suites"][0]["rc"], 0)
        self.assertTrue(row["entry_point_called"])
        self.assertEqual(row["entry_point_evidence"]["callees_entered"], ["check_manifest"])


class TheToolDrivesItself(unittest.TestCase):
    """This suite calls the tool's own top-level entry point, over the real script tree."""

    def test_main_over_a_real_subset(self) -> None:
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            code = self._main()
        self.assertEqual(code, 0)
        self.assertIn("SELF-TEST ENTRY-POINT COVERAGE", buffer.getvalue())

    def _main(self) -> int:
        argv = sys.argv
        sys.argv = ["self_test_coverage.py", "--script", "screen_verdict.py",
                    "--script", "repo_root.py", "--workers", "2"]
        try:
            return stc.main()
        finally:
            sys.argv = argv

    def test_survey_returns_the_two_declared_keys_for_every_row(self) -> None:
        rows = stc.survey(ROOT, only=["repo_root.py"], workers=1, timeout=300)
        self.assertTrue(rows)
        for row in rows:
            self.assertIn(row["real_artifact_case"], ("true", "false", "skipped_declared"))
            self.assertIsInstance(row["entry_point_called"], bool)
            json.dumps(row)  # the report has to survive --json

    def test_every_expected_unreachable_name_exists(self) -> None:
        """An exclusion is a decision with a reason, never a name silently absent."""
        for name in stc.EXPECTED_UNREACHABLE:
            with self.subTest(name=name):
                self.assertTrue((ROOT / name).exists(), f"{name} is not in the tree")


if __name__ == "__main__":
    unittest.main(verbosity=2)
