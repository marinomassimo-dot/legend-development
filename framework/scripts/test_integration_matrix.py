#!/usr/bin/env python3
"""Every finding the integration matrix claims to detect, exhibited by a repository built here.

🔴 The fixture is synthetic on purpose. Run against the real candidates, this suite would assert
whatever those candidates happen to be doing today, and would go green the moment they were
merged — a test of the calendar rather than of the tool. Each branch below exists to carry
exactly one defect, and each test also proves the fixture is capable of failing.

The stub runner reproduces only the interface `integration_matrix` reads: `--list` prints one
suite per line, and a plain run prints `- <suite>: exit <n>` for each failure. Nothing else about
the release battery is simulated, because nothing else is consulted.
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOOL = HERE / "integration_matrix.py"

RUNNER = '''#!/usr/bin/env python3
import sys
TESTS = (
{entries}
)
FAILING = {failing!r}
STREAM = sys.{stream}
SILENT = {silent!r}
if "--list" in sys.argv:
    print("\\n".join(TESTS))
    raise SystemExit(0)
if not SILENT:
    for name in TESTS:
        if name in FAILING:
            print(f"- {{name}}: exit 1", file=STREAM)
raise SystemExit(1 if any(t in FAILING for t in TESTS) else 0)
'''


def runner_source(entries: list[str], failing: list[str],
                  stream: str = "stdout", silent: bool = False) -> str:
    body = "\n".join(f'    "{entry}",' for entry in entries)
    return RUNNER.format(entries=body, failing=failing, stream=stream, silent=silent)


class Fixture(unittest.TestCase):
    """A repository with a base and one branch per defect class."""

    def setUp(self) -> None:
        self.box = Path(tempfile.mkdtemp(prefix="integration-matrix-fixture-"))
        self.addCleanup(shutil.rmtree, self.box, True)
        self.repo = self.box / "repo"
        (self.repo / "scripts").mkdir(parents=True)
        self.git("init", "-q", "-b", "main")
        self.git("config", "user.email", "fixture@example.invalid")
        self.git("config", "user.name", "Fixture")
        self.write_runner(["suite_a.py", "suite_b.py"], ["suite_b.py"])
        (self.repo / "tool.py").write_text("#!/usr/bin/env python3\nprint('x')\n",
                                           encoding="utf-8")
        self.git("add", "scripts/run_release_regressions.py", "tool.py")
        self.git("update-index", "--chmod=+x", "tool.py")
        self.commit("base")
        self.base = self.rev("HEAD")

    # ---- helpers -------------------------------------------------------
    def git(self, *args: str, check: bool = True) -> subprocess.CompletedProcess:
        return subprocess.run(["git", "-C", str(self.repo), *args],
                              check=check, capture_output=True, text=True)

    def commit(self, message: str) -> None:
        self.git("commit", "-q", "-m", message)

    def rev(self, ref: str) -> str:
        return self.git("rev-parse", ref).stdout.strip()

    def runner_inventory(self) -> list[str]:
        proc = subprocess.run([sys.executable, "scripts/run_release_regressions.py", "--list"],
                              cwd=str(self.repo), capture_output=True, text=True)
        return [line.strip() for line in proc.stdout.splitlines() if line.strip()]

    def write_runner(self, entries: list[str], failing: list[str],
                     stream: str = "stdout", silent: bool = False) -> None:
        path = self.repo / "scripts" / "run_release_regressions.py"
        path.write_text(runner_source(entries, failing, stream, silent), encoding="utf-8")
        # 🔴 The stub carries a shebang, so an unexecutable stub is itself a mode-bit
        # offender and every fixture inherits one finding it never asked for. The first
        # run of this suite reported `mode_bit_offenders == ['scripts/run_...py']` on the
        # clean branch: a defect of the fixture reading as a defect of the tool.
        path.chmod(0o755)

    def branch(self, name: str, start: str | None = None) -> None:
        self.git("checkout", "-q", "-b", name, start or self.base)

    def back(self) -> None:
        self.git("checkout", "-q", "main")

    def run_tool(self, *candidates: str, extra: list[str] | None = None):
        report = self.box / "report.json"
        command = [sys.executable, str(TOOL), "--repo", str(self.repo),
                   "--base", self.base, "--json", str(report)]
        for candidate in candidates:
            command += ["--candidate", candidate]
        command += extra or []
        proc = subprocess.run(command, capture_output=True, text=True)
        parsed = json.loads(report.read_text()) if report.exists() else None
        if report.exists():
            report.unlink()
        return proc, parsed

    # ---- branches, one defect each -------------------------------------
    def adds_a_suite(self, name: str = "suite_c.py", failing: bool = False,
                     start: str | None = None) -> str:
        self.branch(f"adds-{name}", start)
        existing = ["suite_a.py", "suite_b.py"]
        if start:
            existing = [line for line in self.runner_inventory()]
        failures = ["suite_b.py"] + ([name] if failing else [])
        self.write_runner(existing + [name], failures)
        self.git("add", "scripts/run_release_regressions.py")
        self.commit(f"enrol {name}")
        self.back()
        return f"adds-{name}"

    def drops_a_suite(self, start: str | None = None) -> str:
        """🔴 Branched from its predecessor when one is given, so the loss arrives through a
        CLEAN merge. Branched from the base it would conflict on the runner, the union guard
        would refuse it, and the test would be measuring the refusal instead of the loss."""
        self.branch("drops", start)
        self.write_runner(["suite_a.py"], ["suite_b.py"])
        self.git("add", "scripts/run_release_regressions.py")
        self.commit("drop suite_b from the inventory")
        self.back()
        return "drops"

    def duplicates_a_suite(self) -> str:
        self.branch("duplicates")
        self.write_runner(["suite_a.py", "suite_b.py", "suite_a.py"], ["suite_b.py"])
        self.git("add", "scripts/run_release_regressions.py")
        self.commit("enrol suite_a twice")
        self.back()
        return "duplicates"

    def drops_the_mode_bit(self) -> str:
        self.branch("modebit")
        self.git("update-index", "--chmod=-x", "tool.py")
        self.commit("drop the executable bit")
        self.back()
        return "modebit"

    def repairs_a_failure(self, start: str | None = None) -> str:
        self.branch("repairs", start)
        self.write_runner(["suite_a.py", "suite_b.py"], [])
        self.git("add", "scripts/run_release_regressions.py")
        self.commit("repair suite_b")
        self.back()
        return "repairs"


class WhatOnlyCompositionMoves(Fixture):

    def test_the_baseline_step_reports_no_movement(self):
        proc, report = self.run_tool(self.adds_a_suite())
        step = report["steps"][0]
        self.assertEqual(step["runner_entries"], 3)
        self.assertEqual(step["new_failures"], [])
        self.assertEqual(step["vanished_failures"], [])
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)

    def test_a_lost_runner_entry_is_visible_as_a_count(self):
        first = self.adds_a_suite()
        proc, report = self.run_tool(first, self.drops_a_suite(start=first))
        self.assertEqual(report["steps"][0]["runner_entries"], 3)
        self.assertEqual(report["steps"][1]["runner_entries"], 1,
                         "a merge that removes inventory entries went unnoticed")

    def test_a_dropped_suite_shows_as_an_unexplained_vanishing_not_as_a_repair(self):
        """🔴 The finding the whole tool exists for.

        `drops` removes `suite_b.py` from the inventory. The suite does not start passing; it
        stops being run, and the failure list gets shorter either way. Without the declaration
        the vanishing is reported unexplained, which is the fail-closed answer.
        """
        first = self.adds_a_suite()
        proc, report = self.run_tool(first, self.drops_a_suite(start=first))
        step = report["steps"][1]
        self.assertEqual(step["vanished_failures"], ["suite_b.py"])
        self.assertEqual(step["unexplained_vanishings"], ["suite_b.py"])
        self.assertEqual(proc.returncode, 1)
        self.assertIn("VANISHED-UNEXPLAINED", proc.stdout)

    def test_a_declared_repair_vanishes_without_a_finding(self):
        """The control in the other direction: a real repair must not read as a defect."""
        first = self.adds_a_suite()
        repairs = self.repairs_a_failure(start=first)
        proc, report = self.run_tool(first, repairs,
                                     extra=[f"--declares={repairs}=suite_b.py"])
        step = report["steps"][1]
        self.assertEqual(step["vanished_failures"], ["suite_b.py"])
        self.assertEqual(step["unexplained_vanishings"], [])
        self.assertEqual(proc.returncode, 0, proc.stdout)

    def test_the_same_repair_undeclared_is_a_finding(self):
        """Proves the previous test is answered by the declaration and not by the branch."""
        first = self.adds_a_suite()
        proc, report = self.run_tool(first, self.repairs_a_failure(start=first))
        self.assertEqual(report["steps"][1]["unexplained_vanishings"], ["suite_b.py"])
        self.assertEqual(proc.returncode, 1)

    def test_a_new_failure_is_attributed_to_the_step_that_introduced_it(self):
        first = self.adds_a_suite()
        proc, report = self.run_tool(
            first, self.adds_a_suite("suite_d.py", failing=True, start=first))
        self.assertEqual(report["steps"][1]["new_failures"], ["suite_d.py"])
        self.assertEqual(proc.returncode, 1)

    def test_a_duplicate_enrolment_is_detected(self):
        proc, report = self.run_tool(self.duplicates_a_suite())
        self.assertEqual(report["steps"][0]["duplicate_entries"], ["suite_a.py"])
        self.assertEqual(proc.returncode, 1)

    def test_a_lost_mode_bit_is_detected(self):
        proc, report = self.run_tool(self.drops_the_mode_bit())
        self.assertEqual(report["steps"][0]["mode_bit_offenders"], ["tool.py"])
        self.assertEqual(proc.returncode, 1)

    def test_a_binary_blob_neither_crashes_the_check_nor_is_flagged(self):
        """🔴 A PNG begins with byte 0x89, which is not valid UTF-8.

        The first version of `mode_bit_offenders` read every 100644 blob as text and died on
        the first image in the real repository, nine minutes into a ten-step run. Committed as
        a fixture rather than as a note, because the class of defect is "the tool has never met
        this repository's own contents".
        """
        self.branch("binary")
        (self.repo / "image.png").write_bytes(b"\x89PNG\r\n\x1a\n" + b"\x00" * 32)
        self.git("add", "image.png")
        self.commit("a binary blob at 100644")
        self.back()
        proc, report = self.run_tool("binary")
        self.assertIsNotNone(report, proc.stdout + proc.stderr)
        self.assertEqual(report["steps"][0]["mode_bit_offenders"], [])
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)

    def test_the_mode_bit_check_is_capable_of_reporting_nothing(self):
        """Without this, the check above is satisfied by a function that always finds one."""
        proc, report = self.run_tool(self.adds_a_suite())
        self.assertEqual(report["steps"][0]["mode_bit_offenders"], [])


class TheVerdictAndTheListMustAgree(Fixture):
    """🔴 The defect this tool exists to detect, found inside this tool.

    A real ten-candidate run reported `FAILS 0` at every one of ten steps. The release runner
    writes its test output to stdout and its verdict to **stderr**, and the first version read
    stdout only. Every fixture in this file printed to stdout, so seventeen passing tests said
    nothing about it: **the tested surface and the defective surface were disjoint.**
    """

    def test_failures_reported_on_stderr_are_counted(self):
        self.branch("stderr-runner")
        self.write_runner(["suite_a.py", "suite_b.py"], ["suite_b.py"], stream="stderr")
        self.git("add", "scripts/run_release_regressions.py")
        self.commit("a runner that reports on stderr, like the real one")
        self.back()
        proc, report = self.run_tool("stderr-runner")
        self.assertEqual(report["steps"][0]["failures"], ["suite_b.py"],
                         "a failure on stderr was read as no failure at all")

    def test_a_nonzero_exit_naming_nothing_is_refused_not_read_as_zero(self):
        """The repair that outlives this particular stream mistake.

        Reading both streams fixes today's runner. Refusing a verdict that disagrees with its
        own list is what catches the next one.
        """
        self.branch("silent-runner")
        self.write_runner(["suite_a.py", "suite_b.py"], ["suite_b.py"], silent=True)
        self.git("add", "scripts/run_release_regressions.py")
        self.commit("a runner that fails and says nothing")
        self.back()
        proc, report = self.run_tool("silent-runner")
        self.assertEqual(proc.returncode, 3, proc.stdout + proc.stderr)
        self.assertIn("named no failing suite", proc.stderr)

    def test_a_clean_runner_still_reports_zero(self):
        """Without this, the two above are satisfied by a tool that refuses everything."""
        self.branch("clean-runner")
        self.write_runner(["suite_a.py", "suite_b.py"], [])
        self.git("add", "scripts/run_release_regressions.py")
        self.commit("nothing fails")
        self.back()
        proc, report = self.run_tool("clean-runner")
        self.assertEqual(report["steps"][0]["failures"], [])
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)


class ItDecidesNothing(Fixture):

    def test_candidate_tips_are_unchanged_by_the_simulation(self):
        first, second = self.adds_a_suite(), self.duplicates_a_suite()
        before = {ref: self.rev(ref) for ref in (first, second)}
        proc, report = self.run_tool(first, second)
        self.assertTrue(report["summary"]["candidate_identity_preserved"])
        for step in report["steps"]:
            self.assertEqual(step["tip_before"], step["tip_after"])
        self.assertEqual({ref: self.rev(ref) for ref in (first, second)}, before,
                         "the simulation moved a candidate branch")

    def test_a_supplied_content_hash_is_carried_through_verbatim(self):
        first = self.adds_a_suite()
        proc, report = self.run_tool(first, extra=[f"--content-hash={first}=abc123"])
        self.assertEqual(report["steps"][0]["content_hash"], "abc123")

    def test_a_declaration_for_a_ref_that_is_not_a_candidate_is_refused(self):
        first = self.adds_a_suite()
        proc, _ = self.run_tool(first, extra=["--declares=not-a-candidate=suite_b.py"])
        self.assertNotEqual(proc.returncode, 0)
        self.assertIn("not candidates", proc.stderr + proc.stdout)

    def test_the_order_is_taken_and_not_chosen(self):
        """Two orders of the same set are two different reports, and the tool produces both."""
        first, second = self.adds_a_suite(), self.adds_a_suite("suite_d.py")
        _, forward = self.run_tool(first, second)
        _, backward = self.run_tool(second, first)
        self.assertEqual([s["candidate"] for s in forward["steps"]], [first, second])
        self.assertEqual([s["candidate"] for s in backward["steps"]], [second, first])


class UnionIsRefusedWhereItWouldDestroy(Fixture):

    def test_two_pure_additions_to_one_file_resolve_by_union(self):
        left = self.adds_a_suite("suite_c.py")
        right = self.adds_a_suite("suite_d.py")
        proc, report = self.run_tool(left, right)
        self.assertEqual(report["steps"][1]["conflict"], "union")
        self.assertEqual(report["steps"][1]["runner_entries"], 4,
                         "union must keep both additions")
        self.assertEqual(report["steps"][1]["duplicate_entries"], [])

    def test_a_conflict_that_also_deletes_is_refused(self):
        """🔴 Union applied here would resurrect `suite_b.py` in the inventory, and the merge
        going through would be the only evidence anyone looked at."""
        adds = self.adds_a_suite("suite_c.py")
        self.branch("deletes")
        self.write_runner(["suite_a.py"], [])
        self.git("add", "scripts/run_release_regressions.py")
        self.commit("remove suite_b deliberately")
        self.back()
        proc, report = self.run_tool(adds, "deletes")
        self.assertEqual(proc.returncode, 3, proc.stdout + proc.stderr)
        self.assertIn("not a pure-addition conflict", proc.stderr)

    def test_the_refusal_leaves_no_simulation_branch_behind(self):
        adds = self.adds_a_suite("suite_c.py")
        self.branch("deletes2")
        self.write_runner(["suite_a.py"], [])
        self.git("add", "scripts/run_release_regressions.py")
        self.commit("remove suite_b deliberately")
        self.back()
        self.run_tool(adds, "deletes2")
        branches = self.git("branch", "--format=%(refname:short)").stdout.split()
        self.assertNotIn("integration-matrix-simulation", branches)


if __name__ == "__main__":
    sys.exit(0 if unittest.main(exit=False, verbosity=2).result.wasSuccessful() else 1)
