#!/usr/bin/env python3
"""Probes for `benchmark_input_surface.py` — one per clause of every PASS sentence.

The method this suite is built on, and the reason it exists at all: **take the tool's PASS
sentence literally and construct the cheapest state that makes it false while the tool still
prints it.** Every blocking defect Mirror found in revision 1 of the benchmark tooling was of
that shape. Not one of them was in a FAIL path — every negative control the author wrote was
caught. They were all in what the tool never looked at:

  * `verify` printed *"allowlist is exhaustive, no prior output"* over a tree whose symlinks
    `iter_files` skipped by construction;
  * `locators` printed *"every cited artifact is inside the surface"* while admitting
    `output/../../../…`, and while admitting LEGEND's own prior dossier at the path the
    repository always cites it by, because that path starts with an allowed prefix;
  * `--post-read` skipped every forbidden path under an output slot, when the collision it was
    written for is exactly ONE path;
  * `freeze` accepted `--actor-id` and `--benchmark-id` as free text and would happily record
    A's tree as `scientist-b`;
  * the population's caption window was a fixed integer and ran into the next caption.

So each test below is a probe against a clause, and every null finding carries a POSITIVE
CONTROL — a state in which the detector is shown to fire — because a check that never fires and
a check that cannot fire look identical from the outside.

Runs without the article packet: the fixtures are synthetic and byte-small. The population
tests over the real PDFs live with the derivation, not here; what this file pins is the
BOUNDING RULE, on a fixture whose right answer is known by construction.
"""

from __future__ import annotations

import inspect
import json
import os
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TOOL = ROOT / "framework/scripts/benchmark_input_surface.py"

FORBIDDEN_COLLIDING = "disease-models/wwox/research/deepdive_manifests/PMID42397075.json"
FORBIDDEN_NON_COLLIDING = (
    "disease-models/wwox/research/fulltext_dossiers/PMID42397075_partial_locators.md")
# A real render's opening bytes. The point is only that they do not decode as UTF-8: that
# is the predicate the prefix exemption is written on since revision 3 (Mirror M-2).
PNG_BYTES = b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\xff\xfe\xfd\x00\x01\x02\x03"

# 🔴 THE CENSUS ORACLE, AND WHY IT IS A LITERAL.
#
# Mirror `M-3`: `test_the_census_names_every_unchecked_file_and_counts_them` asserted a set
# that excluded the five decodable scan-exempt paths its own fixture declared, so the test
# written to prove the census complete certified it incomplete. The reason it could is that
# its expectation was read off the shape of the implementation instead of off the fixture.
#
# So this expectation is HAND-WRITTEN from what `build_fixture` puts on disk, path by path.
# It is not computed from the spec, not derived by calling `scan_skip_reason()`, and not
# obtained by running the tool. If the implementation's skip logic changes, this literal does
# not move with it — which is the entire point of an oracle. `expected = filter(actual)` can
# only ever agree with itself.
FIXTURE_PRESENT_AT_HANDOVER = {
    "ASSIGNMENT.md",
    "CLAUDE.md",
    "benchmark/BENCHMARK_INSTRUCTIONS.md",
    "benchmark/MODE_DIRECTIVE.md",
    "benchmark/OUTPUT_SCHEMA.md",
    "roles/scientist.md",
    "files/paper.txt",
    "disease-models/wwox/research/deepdive_manifests/.gitkeep",
    "disease-models/wwox/research/fulltext_dossiers/.gitkeep",
    "output/.gitkeep",
    "output/renders/.gitkeep",
}
# The one file in the fixture the scan actually reads: allowlisted, `.md`, decodable, and not
# on the exempt list. Everything else is skipped for one of the reasons below.
FIXTURE_SCANNED_AT_HANDOVER = {"roles/scientist.md"}
FIXTURE_CENSUS_AT_HANDOVER = {
    "ASSIGNMENT.md": "scan_exempt_input",
    "CLAUDE.md": "scan_exempt_input",
    "benchmark/BENCHMARK_INSTRUCTIONS.md": "scan_exempt_input",
    "benchmark/MODE_DIRECTIVE.md": "scan_exempt_input",
    "benchmark/OUTPUT_SCHEMA.md": "scan_exempt_input",
    "files/paper.txt": "scan_exempt_input",
    "disease-models/wwox/research/deepdive_manifests/.gitkeep": "suffix_not_scanned",
    "disease-models/wwox/research/fulltext_dossiers/.gitkeep": "suffix_not_scanned",
    "output/.gitkeep": "suffix_not_scanned",
    "output/renders/.gitkeep": "suffix_not_scanned",
}
IDENTIFIER = "42397075"


def run(*arguments: str) -> subprocess.CompletedProcess:
    environment = os.environ.copy()
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    return subprocess.run([sys.executable, str(TOOL), *arguments],
                          capture_output=True, text=True, env=environment)


def write(path: Path, text: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


ASSIGNMENT_A = """---
artifact: FIXTURE — assignment
actor_id: scientist-a
task_id: FIX-001-A
mode: PRIMARY_EVIDENCE_READ
benchmark_id: FIX-001
parallel_read_group: FIX-001
---
fixture assignment for scientist-a
"""

ASSIGNMENT_B = ASSIGNMENT_A.replace("scientist-a", "scientist-b").replace("FIX-001-A", "FIX-001-B")

INSTRUCTIONS = """---
artifact: FIXTURE — common instructions
instructions_version: 7
benchmark_id: FIX-001
---
common instructions
"""

OUTPUT_SCHEMA = """---
artifact: FIXTURE — output schema
schema_version: 3
manifest_schema_version: 2
benchmark_id: FIX-001
---
output schema
"""


def build_fixture(root: Path) -> tuple[Path, Path]:
    """A two-actor surface pair and the spec that describes it. Nothing here is the real one."""
    source = root / "src"
    write(source / "instructions/ASSIGNMENT.scientist-a.md", ASSIGNMENT_A)
    write(source / "instructions/ASSIGNMENT.scientist-b.md", ASSIGNMENT_B)
    write(source / "instructions/BENCHMARK_INSTRUCTIONS.md", INSTRUCTIONS)
    write(source / "instructions/OUTPUT_SCHEMA.md", OUTPUT_SCHEMA)
    write(source / "instructions/MODE_A.md", "mode a directive\n")
    write(source / "instructions/MODE_B.md", "mode b directive\n")
    write(source / "roles/scientist.md", "the contract, with no identifier in it\n")
    # 🔴 CLAUDE.md is in the fixture because Mirror `M-3`'s reproducer is CLAUDE.md: the real
    # spec exempts it from the scan, and the same forbidden bytes that produced two findings
    # at roles/scientist.md produced a VERDICT: PASS and no mention at CLAUDE.md. A fixture
    # that omits the exempt-input class cannot probe the class.
    write(source / "CLAUDE.md", "the router, with no identifier in it\n")
    write(source / "paper.txt", "PMID 42397075 — the paper itself, exempt from the scan\n")

    spec = {
        "spec_version": 2,
        "benchmark_id": "FIX-001",
        "pmid": "42397075",
        "actors": ["scientist-a", "scientist-b"],
        "source_files": [{"source": "paper.txt", "surface": "files/paper.txt"}],
        "common_files": [
            {"source": "instructions/BENCHMARK_INSTRUCTIONS.md",
             "surface": "benchmark/BENCHMARK_INSTRUCTIONS.md"},
            {"source": "instructions/OUTPUT_SCHEMA.md", "surface": "benchmark/OUTPUT_SCHEMA.md"},
            {"source": "roles/scientist.md", "surface": "roles/scientist.md"},
            {"source": "CLAUDE.md", "surface": "CLAUDE.md"},
        ],
        "per_actor_files": {
            "scientist-a": [
                {"source": "instructions/ASSIGNMENT.scientist-a.md", "surface": "ASSIGNMENT.md"},
                {"source": "instructions/MODE_A.md", "surface": "benchmark/MODE_DIRECTIVE.md"}],
            "scientist-b": [
                {"source": "instructions/ASSIGNMENT.scientist-b.md", "surface": "ASSIGNMENT.md"},
                {"source": "instructions/MODE_B.md", "surface": "benchmark/MODE_DIRECTIVE.md"}],
        },
        "per_actor_may_be_identical": [],
        "empty_dirs": ["disease-models/wwox/research/deepdive_manifests",
                       "disease-models/wwox/research/fulltext_dossiers",
                       "output", "output/renders"],
        "forbidden_prior_output_paths": [FORBIDDEN_COLLIDING, FORBIDDEN_NON_COLLIDING],
        "expected_output_paths": [FORBIDDEN_COLLIDING,
                                  "disease-models/wwox/research/fulltext_dossiers/PMID42397075.md",
                                  "output/receipt.json"],
        "expected_output_prefixes": ["output/renders/"],
        "content_scan": {
            "pattern": "42397075",
            "text_suffixes": [".md", ".txt", ".json"],
            "exempt_surface_paths": ["files/paper.txt", "ASSIGNMENT.md",
                                     "benchmark/BENCHMARK_INSTRUCTIONS.md",
                                     "benchmark/OUTPUT_SCHEMA.md",
                                     "benchmark/MODE_DIRECTIVE.md",
                                     "CLAUDE.md"],
        },
    }
    spec_path = write(root / "spec.json", json.dumps(spec, indent=2))
    surfaces = root / "surfaces"
    result = run("build", "--spec", str(spec_path), "--source-root", str(source),
                 "--out", str(surfaces))
    assert result.returncode == 0, result.stdout + result.stderr
    return spec_path, surfaces


class SurfaceFixture(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        self.spec, self.surfaces = build_fixture(self.root)
        self.a = self.surfaces / "FIX-001/scientist-a"
        self.b = self.surfaces / "FIX-001/scientist-b"

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def verify(self, *extra: str) -> subprocess.CompletedProcess:
        return run("verify", "--spec", str(self.spec), "--surfaces", str(self.surfaces), *extra)

    # 🔴 THE MODE IS A RUNTIME FACT, NEVER THE TEST'S NAME (Mirror `M-4`).
    #
    # `test_every_present_file_is_either_scanned_or_named_and_never_both` asserted against
    # constants called `FIXTURE_PRESENT_AT_HANDOVER` / `FIXTURE_CENSUS_AT_HANDOVER` and made
    # every one of its assertions under `--post-read`. It passed — because on a fixture with
    # no reader output the two censuses coincide — so the name claimed the handover mode,
    # the run exercised the post-read one, and the coincidence hid a mode in which the
    # census did not exist at all. Redirecting that single call to the mode its constants
    # are named for produced ten silent files.
    #
    # So: the two helpers below return the argv they actually used, and `assert_mode()`
    # checks the claim on BOTH the command line and the tool's own printed `MODE` line,
    # which is emitted on every run including a failing one. A fixture name is not evidence.
    MODE_PRE = "pre-handover (HANDOVER GATE)"
    MODE_POST = "--post-read"

    def verify_pre(self) -> tuple[subprocess.CompletedProcess, tuple[str, ...]]:
        """THE HANDOVER GATE — §5 step 1 of the protocol, no flag. `(result, argv)`."""
        argv = ("verify", "--spec", str(self.spec), "--surfaces", str(self.surfaces))
        return run(*argv), argv

    def verify_post(self) -> tuple[subprocess.CompletedProcess, tuple[str, ...]]:
        """After the freeze — a different contract (§4.4). `(result, argv)`."""
        argv = ("verify", "--spec", str(self.spec), "--surfaces", str(self.surfaces),
                "--post-read")
        return run(*argv), argv

    def assert_mode(self, result: subprocess.CompletedProcess,
                    argv: tuple[str, ...], mode: str) -> None:
        self.assertEqual(mode == self.MODE_POST, "--post-read" in argv,
                         f"the invocation does not exercise {mode}: {argv}")
        self.assertIn(f"MODE  {mode}", result.stdout,
                      f"the tool did not report running in {mode}")
        other = self.MODE_PRE if mode == self.MODE_POST else self.MODE_POST
        self.assertNotIn(f"MODE  {other}", result.stdout)

    @staticmethod
    def census(stdout: str, actor: str = "scientist-a") -> dict[str, str]:
        """`{path: class}` parsed out of one actor's printed `[UNCHECKED]` lines.

        Parsing the tool's OUTPUT, not calling its functions: what a reviewer reads is what
        is asserted. `[UNCHECKED] <actor>  <rel>  — <class>: <reason>; …`
        """
        rows: dict[str, str] = {}
        for line in stdout.splitlines():
            # Anchored, not a substring search: the PASS sentence names `[UNCHECKED]` in
            # prose, and a parser that matches prose reports whatever the prose says.
            if not line.strip().startswith("[UNCHECKED] "):
                continue
            body = line.strip()[len("[UNCHECKED] "):]
            named, rest = body.split("  ", 1)
            if named.strip() != actor:
                continue
            rel, described = rest.split("  — ", 1)
            rows[rel.strip()] = described.split(":", 1)[0].strip()
        return rows

    @staticmethod
    def census_rows(stdout: str) -> int:
        """How many `[UNCHECKED]` rows were printed, over both actors.

        🔴 Anchored for the same reason `census()` is: counting lines that merely CONTAIN
        `[UNCHECKED] ` counts the PASS sentence's prose, and a count that includes its own
        description is the arithmetic version of the defect this file is about.
        """
        return sum(1 for line in stdout.splitlines()
                   if line.strip().startswith("[UNCHECKED] "))

    @staticmethod
    def present(surface: Path) -> set[str]:
        """Every regular file under a surface, walked here rather than asked of the tool."""
        return {str(path.relative_to(surface)) for path in surface.rglob("*")
                if path.is_file() and not path.is_symlink()}


class ExAnteVerifyTests(SurfaceFixture):
    def test_positive_control_a_clean_pair_passes(self) -> None:
        """The control every negative below is measured against."""
        result = self.verify()
        self.assertEqual(0, result.returncode, result.stdout)
        self.assertIn("VERDICT: PASS", result.stdout)

    def test_a_file_symlink_is_reported_not_skipped(self) -> None:
        """`iter_files` skips symlinks; nothing else used to look at them."""
        outside = write(self.root / "outside/prior_manifest.json", '{"prior": true}\n')
        (self.a / "roles/linked.md").symlink_to(outside)
        result = self.verify()
        self.assertEqual(1, result.returncode, result.stdout)
        self.assertIn("SYMLINK", result.stdout)

    def test_a_directory_symlink_is_reported_not_walked(self) -> None:
        target = self.root / "outside/manifests"
        target.mkdir(parents=True)
        write(target / "PMID42397075.json", "{}\n")
        (self.a / "output/linkdir").symlink_to(target, target_is_directory=True)
        result = self.verify()
        self.assertEqual(1, result.returncode, result.stdout)
        self.assertIn("SYMLINK", result.stdout)

    def test_parity_break_is_caught(self) -> None:
        with (self.b / "roles/scientist.md").open("a", encoding="utf-8") as handle:
            handle.write("x")
        result = self.verify()
        self.assertEqual(1, result.returncode, result.stdout)
        self.assertIn("PARITY BROKEN", result.stdout)

    def test_identical_mode_directives_are_caught(self) -> None:
        """Two identical directives means there is no experiment."""
        (self.b / "benchmark/MODE_DIRECTIVE.md").write_text(
            (self.a / "benchmark/MODE_DIRECTIVE.md").read_text(encoding="utf-8"),
            encoding="utf-8")
        result = self.verify()
        self.assertEqual(1, result.returncode, result.stdout)
        self.assertIn("NOT DIFFERING", result.stdout)

    def test_prior_output_in_a_slot_before_handover_is_caught(self) -> None:
        write(self.a / FORBIDDEN_COLLIDING, "{}\n")
        result = self.verify()
        self.assertEqual(1, result.returncode, result.stdout)
        self.assertIn("NOT EMPTY", result.stdout)
        self.assertIn("PRIOR OUTPUT", result.stdout)

    def test_identifier_leak_outside_the_packet_is_caught(self) -> None:
        write(self.a / "roles/scientist.md", "this contract names PMID 42397075\n")
        result = self.verify()
        self.assertEqual(1, result.returncode, result.stdout)
        self.assertIn("IDENTIFIER LEAK", result.stdout)


class PostReadExclusionTests(SurfaceFixture):
    """Mirror B-4 — the exemption must be the declared output set, not the whole slot."""

    def _plausible_reading(self) -> None:
        """What an honest reader leaves behind: its own manifest, dossier, receipt, renders.

        🔴 The render here is BYTES, not markdown. Until revision 3 this fixture wrote
        `output/renders/fig1.md` and the tool passed it, which is exactly the hole Mirror
        `M-2` names: the render slot was exempt by position, so a text file in it was
        skipped by the allowlist check and by the scan. A render is pixels; the fixture
        now says so, and `test_a_decodable_file_under_the_render_prefix_is_caught` is the
        negative control that the old fixture was standing in front of.
        """
        for surface in (self.a, self.b):
            write(surface / FORBIDDEN_COLLIDING, '{"pmid": "42397075"}\n')
            write(surface / "disease-models/wwox/research/fulltext_dossiers/PMID42397075.md",
                  "# dossier for PMID 42397075\n")
            write(surface / "output/receipt.json", '{"pmid": "42397075"}\n')
            (surface / "output/renders").mkdir(parents=True, exist_ok=True)
            (surface / "output/renders/fig1.png").write_bytes(PNG_BYTES)

    def test_positive_control_an_honest_reading_passes_post_read(self) -> None:
        """The reader's own outputs name the paper by construction and must not fire.

        🔴 Checked, not merely asserted (`SLR-plan-0003` L-1, and Mirror `M-3` is its second
        instance). Until revision 4 this control asserted `rc == 0` and `VERDICT: PASS` and
        nothing else, so it passed identically over a tree where ten present files per
        surface were skipped by the scan and named by nothing. A positive control that only
        checks the verdict cannot see a defect that leaves the verdict alone. It now pins
        the whole census of the honest tree, against a hand-written expectation.
        """
        self._plausible_reading()
        result = self.verify("--post-read")
        self.assertEqual(0, result.returncode, result.stdout)
        self.assertIn("VERDICT: PASS", result.stdout)
        expected = dict(FIXTURE_CENSUS_AT_HANDOVER)
        expected[FORBIDDEN_COLLIDING] = "blind_spot"
        expected["disease-models/wwox/research/fulltext_dossiers/PMID42397075.md"] = \
            "scan_exempt_present"
        expected["output/receipt.json"] = "scan_exempt_present"
        expected["output/renders/fig1.png"] = "undecodable_prefix"
        self.assertEqual(expected, self.census(result.stdout), result.stdout)

    def test_the_blind_spot_is_printed_by_name_and_is_exactly_one_path(self) -> None:
        self._plausible_reading()
        result = self.verify("--post-read")
        blind = [line for line in result.stdout.splitlines() if "[BLIND SPOT]" in line]
        self.assertEqual(1, len(blind), result.stdout)
        self.assertIn(FORBIDDEN_COLLIDING, blind[0])

    def test_a_non_colliding_forbidden_path_under_a_slot_is_caught_post_read(self) -> None:
        """🔴 The defect: six such paths were skipped along with the one that collides."""
        self._plausible_reading()
        write(self.a / FORBIDDEN_NON_COLLIDING, "LEGEND's prior dossier\n")
        result = self.verify("--post-read")
        self.assertEqual(1, result.returncode, result.stdout)
        self.assertIn("PRIOR OUTPUT", result.stdout)
        self.assertIn(FORBIDDEN_NON_COLLIDING, result.stdout)

    def test_an_undeclared_file_under_a_slot_is_caught_post_read(self) -> None:
        self._plausible_reading()
        write(self.a / "output/smuggled.md", "not an expected output\n")
        result = self.verify("--post-read")
        self.assertEqual(1, result.returncode, result.stdout)
        self.assertIn("NOT ALLOWLISTED", result.stdout)

    def test_a_symlink_appearing_after_the_reading_is_caught(self) -> None:
        self._plausible_reading()
        outside = write(self.root / "outside/notes.md", "elsewhere\n")
        (self.a / "output/renders/link.md").symlink_to(outside)
        result = self.verify("--post-read")
        self.assertEqual(1, result.returncode, result.stdout)
        self.assertIn("SYMLINK", result.stdout)


class ExpectedOutputPrefixTests(SurfaceFixture):
    """Mirror M-2 — the exemption is spread over two keys, so both must be accounted for.

    🔴 The defect these probe: `_is_expected_output()` admitted a path by the exact list OR
    by `expected_output_prefixes`, and `declared_blind_spots()` intersected only the exact
    list. So the prefix was an exemption that was never computed and never printed, and a
    copy of prior LEGEND output at `output/renders/smuggled.md` passed `--post-read` with a
    `VERDICT: PASS` and a `blind spot: size 1` beside it, while the same bytes one directory
    away produced `NOT ALLOWLISTED` + `IDENTIFIER LEAK`.

    Every case asserts the REASON and not only the exit code. `SLR-mirror-0010` §4 is the
    argument: Mirror's own first battery reported 13/13 caught, and all thirteen were
    `rc=2` from argparse rejecting an unknown flag before any check ran.
    """

    def _reading(self) -> None:
        for surface in (self.a, self.b):
            write(surface / FORBIDDEN_COLLIDING, '{"pmid": "42397075"}\n')
            write(surface / "output/receipt.json", '{"pmid": "42397075"}\n')

    def test_positive_control_a_binary_render_under_the_prefix_passes(self) -> None:
        """The control: the exemption must still work for what it was written for."""
        self._reading()
        (self.a / "output/renders/fig3f.png").write_bytes(PNG_BYTES)
        result = self.verify("--post-read")
        self.assertEqual(0, result.returncode, result.stdout)
        self.assertIn("VERDICT: PASS", result.stdout)
        self.assertIn("[UNCHECKED] scientist-a  output/renders/fig3f.png", result.stdout)

    def test_a_decodable_file_under_the_render_prefix_is_caught(self) -> None:
        """The finding itself: forbidden bytes at `output/renders/`, on both checks."""
        self._reading()
        write(self.a / "output/renders/smuggled.md",
              "LEGEND's prior dossier on 42397075, smuggled under the render slot\n")
        result = self.verify("--post-read")
        self.assertEqual(1, result.returncode, result.stdout)
        self.assertIn("NOT ALLOWLISTED scientist-a  output/renders/smuggled.md", result.stdout)
        self.assertIn("IDENTIFIER LEAK scientist-a  output/renders/smuggled.md", result.stdout)

    def test_the_same_bytes_are_caught_under_the_prefix_and_outside_it(self) -> None:
        """🔴 The control that made M-2 a hole rather than a design: one directory apart."""
        self._reading()
        payload = "prior LEGEND output on 42397075\n"
        write(self.a / "output/renders/copy.md", payload)
        write(self.b / "disease-models/wwox/research/fulltext_dossiers/NOTES.md", payload)
        result = self.verify("--post-read")
        self.assertEqual(1, result.returncode, result.stdout)
        for actor, rel in (("scientist-a", "output/renders/copy.md"),
                           ("scientist-b",
                            "disease-models/wwox/research/fulltext_dossiers/NOTES.md")):
            self.assertIn(f"NOT ALLOWLISTED {actor}  {rel}", result.stdout)
            self.assertIn(f"IDENTIFIER LEAK {actor}  {rel}", result.stdout)

    def test_a_nested_directory_under_the_prefix_is_not_a_way_in(self) -> None:
        self._reading()
        write(self.a / "output/renders/deep/nested/smuggled.md", "42397075 again\n")
        result = self.verify("--post-read")
        self.assertEqual(1, result.returncode, result.stdout)
        self.assertIn("NOT ALLOWLISTED scientist-a  output/renders/deep/nested/smuggled.md",
                      result.stdout)

    def test_a_renamed_copy_wearing_a_render_extension_is_caught(self) -> None:
        """The exemption is on bytes, not on a suffix: `.png` does not make it pixels."""
        self._reading()
        write(self.a / "output/renders/innocent.png", "prior output about 42397075\n")
        result = self.verify("--post-read")
        self.assertEqual(1, result.returncode, result.stdout)
        self.assertIn("NOT ALLOWLISTED scientist-a  output/renders/innocent.png", result.stdout)

    def test_an_empty_render_prefix_contributes_nothing_to_the_census(self) -> None:
        """🔴 Renamed at revision 4: it used to say *an empty unchecked surface* while
        asserting four files, which was the same over-claim one scale down."""
        self._reading()
        result = self.verify("--post-read")
        self.assertEqual(0, result.returncode, result.stdout)
        self.assertEqual({}, {rel: name for rel, name in self.census(result.stdout).items()
                              if name == "undecodable_prefix"}, result.stdout)
        # `output/renders/.gitkeep` is present and censused; no OTHER path under the prefix is.
        under = [rel for rel in self.census(result.stdout) if rel.startswith("output/renders/")]
        self.assertEqual(["output/renders/.gitkeep"], sorted(under), result.stdout)

    def test_several_legitimate_renders_are_each_named_in_the_census(self) -> None:
        self._reading()
        for name in ("a.png", "b.png", "c.jpg"):
            (self.a / "output/renders" / name).write_bytes(PNG_BYTES)
        result = self.verify("--post-read")
        self.assertEqual(0, result.returncode, result.stdout)
        census = self.census(result.stdout)
        for name in ("a.png", "b.png", "c.jpg"):
            self.assertEqual("undecodable_prefix", census.get(f"output/renders/{name}"),
                             result.stdout)
        self.assertIn(f"[UNCHECKED SURFACE] {self.census_rows(result.stdout)} present "
                      "file(s)", result.stdout)

    def test_a_hostile_file_beside_a_legitimate_render_does_not_hide_behind_it(self) -> None:
        self._reading()
        (self.a / "output/renders/ok.png").write_bytes(PNG_BYTES)
        write(self.a / "output/renders/hostile.md", "42397075 prior output\n")
        result = self.verify("--post-read")
        self.assertEqual(1, result.returncode, result.stdout)
        self.assertIn("NOT ALLOWLISTED scientist-a  output/renders/hostile.md", result.stdout)
        self.assertIn("[UNCHECKED] scientist-a  output/renders/ok.png", result.stdout)

    def test_a_file_arriving_late_under_the_prefix_is_caught_on_the_next_run(self) -> None:
        """The tree passed a moment ago; the guarantee is about the run, not the history."""
        self._reading()
        (self.a / "output/renders/fig1.png").write_bytes(PNG_BYTES)
        before = self.verify("--post-read")
        self.assertEqual(0, before.returncode, before.stdout)
        write(self.a / "output/renders/late.md", "42397075 arriving afterwards\n")
        after = self.verify("--post-read")
        self.assertEqual(1, after.returncode, after.stdout)
        self.assertIn("NOT ALLOWLISTED scientist-a  output/renders/late.md", after.stdout)

    def test_the_census_is_exactly_the_present_files_the_scan_did_not_read(self) -> None:
        """The guarantee, as an assertion — against a HAND-WRITTEN expectation.

        🔴 Mirror `M-3`. The predecessor of this test was called
        `test_the_census_names_every_unchecked_file_and_counts_them` and docstringed *"the
        printed list IS the unchecked surface"*, and it asserted a three-path set over a
        fixture that declared five decodable scan-exempt paths, every one of them present
        and none of them in the assertion. It excluded from the denominator exactly the
        population the census was missing, so the test written to prove completeness
        certified the incompleteness instead — `L-1` of `SLR-plan-0003`, a second time, in
        the revision that recorded `L-1`.

        The name is narrower now because the guarantee is: the census is the set of present
        files whose CONTENT the identifier scan did not read — which is not the same as
        "unverified", and the printed reasons say what did still run.

        The expectation is `FIXTURE_CENSUS_AT_HANDOVER` plus the three paths this test
        writes itself. It is a literal, so it cannot follow the implementation anywhere.
        """
        self._reading()
        (self.a / "output/renders/fig1.png").write_bytes(PNG_BYTES)
        result = self.verify("--post-read")
        self.assertEqual(0, result.returncode, result.stdout)

        expected = dict(FIXTURE_CENSUS_AT_HANDOVER)
        expected[FORBIDDEN_COLLIDING] = "blind_spot"
        expected["output/receipt.json"] = "scan_exempt_present"
        expected["output/renders/fig1.png"] = "undecodable_prefix"
        self.assertEqual(expected, self.census(result.stdout), result.stdout)
        self.assertIn(f"[UNCHECKED SURFACE] {self.census_rows(result.stdout)} present "
                      "file(s)", result.stdout)

    def _partition_by_effect(self, mode: str) -> tuple[set[str], set[str]]:
        """`(scanned, censused)` over a handover-state tree, measured in `mode`.

        🔴 This helper never asks the tool which files it skips, and never re-implements the
        skip predicate: `expected = implementation_filter(actual)` can only agree with
        itself, and that is how a census and its test were wrong together. Instead, for
        every present file it plants the paper's identifier in that file and observes
        whether the scan REPORTS it. Scanning is measured by its consequence.

        🔴 And `mode` is a parameter rather than a constant, because a partition is a
        property OF A RUN (Mirror `M-4`). Every call asserts the mode it claims, on argv and
        on the tool's printed `MODE` line, before it reads a single population out of the
        output.
        """
        self.assertEqual(FIXTURE_PRESENT_AT_HANDOVER, self.present(self.a),
                         "the fixture moved; the hand-written oracle must move with it")
        scanned: set[str] = set()
        censused: set[str] = set()
        for rel in sorted(FIXTURE_PRESENT_AT_HANDOVER):
            target = self.a / rel
            original = target.read_bytes()
            try:
                target.write_bytes(original + f"\nPMID {IDENTIFIER} planted here\n".encode())
                result, argv = (self.verify_post() if mode == self.MODE_POST
                                else self.verify_pre())
                self.assert_mode(result, argv, mode)
                if f"IDENTIFIER LEAK scientist-a  {rel}" in result.stdout:
                    scanned.add(rel)
                if rel in self.census(result.stdout):
                    censused.add(rel)
            finally:
                target.write_bytes(original)
        return scanned, censused

    def _assert_partition(self, mode: str) -> None:
        scanned, censused = self._partition_by_effect(mode)
        self.assertEqual(set(), scanned & censused,
                         f"[{mode}] a file reported as skipped and scanned in the same run")
        silent = FIXTURE_PRESENT_AT_HANDOVER - scanned - censused
        self.assertEqual(FIXTURE_PRESENT_AT_HANDOVER, scanned | censused,
                         f"[{mode}] SILENT: {sorted(silent)}")
        self.assertEqual(FIXTURE_SCANNED_AT_HANDOVER, scanned,
                         f"[{mode}] the scanned population is not the one the fixture is "
                         "built for")
        self.assertEqual(FIXTURE_CENSUS_AT_HANDOVER.keys(), censused,
                         f"[{mode}] the censused population is not the fixture's")
        self.assertTrue(scanned, f"[{mode}] positive control: the scan never fired, so "
                                 "nothing above is evidence about the tool")

    def test_every_present_file_is_either_scanned_or_named_at_handover(self) -> None:
        """The `M-3` invariant measured by effect, in the mode that GATES HANDOVER.

        🔴 This is the negative control revision 4 lacked, and the whole of Mirror `M-4`.
        The constants are named `…_AT_HANDOVER` and, until this test existed, nothing
        asserted anything about the pre-handover census — because there was none. Every
        assertion here runs under `verify` with no flag, asserted as a runtime fact.

        A file that neither leaks nor appears in the census is a silent one, and there must
        be none. A file that does both would be the census lying in the other direction.
        """
        self._assert_partition(self.MODE_PRE)

    def test_every_present_file_is_either_scanned_or_named_post_read(self) -> None:
        """The same invariant in the other mode. Two modes, two controls, no borrowing.

        On a handover-state tree the two censuses coincide, and that coincidence is
        precisely what let one test stand for both. It is now asserted twice rather than
        assumed once, and each assertion names the run it was measured in.
        """
        self._assert_partition(self.MODE_POST)

    def test_freeze_calls_a_decodable_file_under_the_prefix_unexpected(self) -> None:
        """🔴 freeze used to agree with the verifier about a file neither had looked at."""
        self._reading()
        write(self.a / "output/renders/smuggled.md", "42397075 prior output\n")
        receipt = self.root / "receipt.json"
        result = run("freeze", "--surface", str(self.a), "--actor-id", "scientist-a",
                     "--benchmark-id", "FIX-001", "--spec", str(self.spec),
                     "--first-pass-state", "COMPLETE_DECLARED_BY_ACTOR", "--out", str(receipt))
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        record = json.loads(receipt.read_text(encoding="utf-8"))
        self.assertIn("output/renders/smuggled.md", record["UNEXPECTED_FILE_SET"])
        self.assertNotIn("output/renders/smuggled.md", record["OUTPUT_FILE_SET"])

    def test_freeze_still_calls_a_binary_render_an_output(self) -> None:
        """The positive control for the row above: the legitimate case must not move."""
        self._reading()
        (self.a / "output/renders/fig1.png").write_bytes(PNG_BYTES)
        receipt = self.root / "receipt-ok.json"
        result = run("freeze", "--surface", str(self.a), "--actor-id", "scientist-a",
                     "--benchmark-id", "FIX-001", "--spec", str(self.spec),
                     "--first-pass-state", "COMPLETE_DECLARED_BY_ACTOR", "--out", str(receipt))
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        record = json.loads(receipt.read_text(encoding="utf-8"))
        self.assertIn("output/renders/fig1.png", record["OUTPUT_FILE_SET"])
        self.assertEqual([], record["UNEXPECTED_FILE_SET"])


class ScanSkipClassTests(SurfaceFixture):
    """Mirror `M-3` — one probe per condition under which the content scan skips a file.

    🔴 The defect these probe: the scan skipped on FOUR conditions and the census enumerated
    the three populations produced by ONE of them, while the tool printed *"every file whose
    bytes this tool could decode was scanned"* and the protocol tabulated the same claim. On
    a clean build of the real benchmark that is sixteen present files per surface, and the
    identical forbidden bytes that produce two findings at `roles/scientist.md` produced a
    `VERDICT: PASS` with no mention at all at `CLAUDE.md`.

    Every case asserts the printed CLASS, not the exit code — `SLR-mirror-0010` §4 and
    `SLR-mirror-0011` §3 are both about batteries that measured their own invocation. The
    scanned cases are the positive controls: without them, "nothing was reported" and "the
    scan never ran" are the same observation.
    """

    # A forbidden prior-output artifact, in the shape that matters: real prose, identifiers
    # in it, and nothing about it that a path could reveal.
    HOSTILE = f"LEGEND's prior dossier for PMID {IDENTIFIER}, copied whole.\n" * 4

    def _reading(self) -> None:
        for surface in (self.a, self.b):
            write(surface / FORBIDDEN_COLLIDING, f'{{"pmid": "{IDENTIFIER}"}}\n')
            write(surface / "output/receipt.json", f'{{"pmid": "{IDENTIFIER}"}}\n')

    def _plant(self, rel: str, payload: bytes, differ: bool = False) -> None:
        """Write the same bytes into BOTH surfaces — the version parity cannot see.

        🔴 Writing to one surface only is caught by `PARITY BROKEN`, and a battery that
        does that is measuring the parity check while believing it measures the scan. The
        adversary's move is the identical edit to both trees, which is also Mirror `P-4`:
        `build --emit-digests` records what these files were and `verify` consumes it
        nowhere, so parity is the only comparison and it compares A with B.
        """
        for surface, actor in ((self.a, "scientist-a"), (self.b, "scientist-b")):
            target = surface / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            # `differ=True` for a per-actor path: the spec requires those two to be unequal,
            # so identical hostile bytes there would be caught by `NOT DIFFERING` — again the
            # wrong check answering the question.
            target.write_bytes(payload + (f"\n{actor}\n".encode() if differ else b""))

    def test_positive_control_the_scan_fires_on_an_allowlisted_scanned_file(self) -> None:
        """The discriminator. Everything below is read against this one."""
        self._reading()
        self._plant("roles/scientist.md", self.HOSTILE.encode())
        result = self.verify("--post-read")
        self.assertEqual(1, result.returncode, result.stdout)
        self.assertIn("IDENTIFIER LEAK scientist-a  roles/scientist.md", result.stdout)
        self.assertIn("IDENTIFIER LEAK scientist-b  roles/scientist.md", result.stdout)
        self.assertNotIn("PARITY BROKEN", result.stdout)
        self.assertNotIn("roles/scientist.md", self.census(result.stdout))

    def test_positive_control_the_same_file_clean_is_scanned_and_silent(self) -> None:
        """A scanned file that is clean must appear in NEITHER population's output."""
        self._reading()
        result = self.verify("--post-read")
        self.assertEqual(0, result.returncode, result.stdout)
        self.assertNotIn("roles/scientist.md", result.stdout.split("VERDICT")[0])

    def test_the_same_bytes_are_named_at_an_exempt_path_and_caught_at_a_scanned_one(self)\
            -> None:
        """🔴 Mirror `M-3`'s reproducer, as one test: identical bytes, four paths.

        Two are caught and two are exempt from the scan — which is the design. What was the
        defect is that the two exempt ones were also invisible. Now they are named, with the
        class and the reason, and the difference between "not scanned" and "not mentioned"
        is the whole finding.
        """
        self._reading()
        for rel in ("CLAUDE.md", "roles/scientist.md", "output/renders/smuggled.md"):
            self._plant(rel, self.HOSTILE.encode())
        self._plant("benchmark/MODE_DIRECTIVE.md", self.HOSTILE.encode(), differ=True)
        result = self.verify("--post-read")

        self.assertEqual(1, result.returncode, result.stdout)
        self.assertNotIn("PARITY BROKEN", result.stdout)
        self.assertNotIn("NOT DIFFERING", result.stdout)
        # caught
        self.assertIn("IDENTIFIER LEAK scientist-a  roles/scientist.md", result.stdout)
        self.assertIn("NOT ALLOWLISTED scientist-a  output/renders/smuggled.md", result.stdout)
        self.assertIn("IDENTIFIER LEAK scientist-a  output/renders/smuggled.md", result.stdout)
        # exempt from the scan — and NAMED, which is what revision 3 did not do
        census = self.census(result.stdout)
        self.assertEqual("scan_exempt_input", census.get("CLAUDE.md"), result.stdout)
        self.assertEqual("scan_exempt_input", census.get("benchmark/MODE_DIRECTIVE.md"),
                         result.stdout)
        for rel in ("roles/scientist.md", "output/renders/smuggled.md"):
            self.assertNotIn(rel, census, "a scanned file must not be censused")

    def test_hostile_bytes_under_a_non_text_suffix_are_named_not_silent(self) -> None:
        """`.gitkeep` is allowlisted, present, decodable, and never opened by the scan."""
        self._reading()
        self._plant("output/.gitkeep", self.HOSTILE.encode())
        result = self.verify("--post-read")
        self.assertEqual(0, result.returncode, result.stdout)
        self.assertEqual("suffix_not_scanned", self.census(result.stdout).get("output/.gitkeep"),
                         result.stdout)

    def test_an_allowlisted_text_file_that_is_not_utf8_is_named_and_flagged_unexpected(self)\
            -> None:
        """The fourth skip condition, and the only class the protocol does NOT declare.

        A `.md` file that is not text reaches the decode guard, is skipped, and was silent.
        It stays a `PASS` — the file is allowlisted and nothing here proves it hostile — but
        the census marks it `EXPECTED_BY_PROTOCOL NO` and counts it separately, because an
        allowlisted markdown file full of UTF-16 is an anomaly and not a design.
        """
        self._reading()
        self._plant("roles/scientist.md", self.HOSTILE.encode("utf-16"))
        result = self.verify("--post-read")
        self.assertEqual(0, result.returncode, result.stdout)
        self.assertEqual("undecodable_text", self.census(result.stdout).get("roles/scientist.md"),
                         result.stdout)
        self.assertIn("EXPECTED_BY_PROTOCOL NO", result.stdout)
        self.assertIn("[UNCHECKED SURFACE] 2 of them are NOT a consequence the protocol "
                      "declares", result.stdout)

    def test_a_non_utf8_hostile_payload_under_the_render_prefix_is_named(self) -> None:
        """Prior output re-encoded into bytes no scan can read still gets a line of its own."""
        self._reading()
        self._plant("output/renders/fig1.png", self.HOSTILE.encode("utf-16"))
        result = self.verify("--post-read")
        self.assertEqual(0, result.returncode, result.stdout)
        self.assertEqual("undecodable_prefix",
                         self.census(result.stdout).get("output/renders/fig1.png"),
                         result.stdout)

    def test_every_skip_class_present_at_once_is_reported_with_its_own_reason(self) -> None:
        """Six classes in one tree, because a census that is right one class at a time is
        not yet a census."""
        self._reading()
        (self.a / "output/renders/fig1.png").write_bytes(PNG_BYTES)
        self._plant("CLAUDE.md", self.HOSTILE.encode())
        self._plant("output/.gitkeep", self.HOSTILE.encode())
        self._plant("benchmark/OUTPUT_SCHEMA.md", self.HOSTILE.encode("utf-16"))
        self._plant("roles/scientist.md", self.HOSTILE.encode("utf-16"))
        result = self.verify("--post-read")
        self.assertEqual(0, result.returncode, result.stdout)
        census = self.census(result.stdout)
        self.assertEqual("blind_spot", census.get(FORBIDDEN_COLLIDING), result.stdout)
        self.assertEqual("scan_exempt_present", census.get("output/receipt.json"), result.stdout)
        self.assertEqual("undecodable_prefix", census.get("output/renders/fig1.png"),
                         result.stdout)
        self.assertEqual("scan_exempt_input", census.get("CLAUDE.md"), result.stdout)
        self.assertEqual("suffix_not_scanned", census.get("output/.gitkeep"), result.stdout)
        # 🔴 `benchmark/OUTPUT_SCHEMA.md` is BOTH exempt and undecodable. The class reported
        # must be the reason the scan ACTUALLY stopped, which is the exempt list, because
        # that test returns first. A census that reported the other one would be describing
        # a code path that did not run.
        self.assertEqual("scan_exempt_input", census.get("benchmark/OUTPUT_SCHEMA.md"),
                         result.stdout)
        # ... and the same bytes at a path that is allowlisted but NOT exempt reach the
        # decode guard instead, which is the class the protocol does not declare.
        self.assertEqual("undecodable_text", census.get("roles/scientist.md"), result.stdout)
        self.assertEqual(6, len(set(census.values())), sorted(set(census.values())))

    def test_the_census_survives_a_file_arriving_after_a_clean_run(self) -> None:
        self._reading()
        before = self.verify("--post-read")
        self.assertEqual(0, before.returncode, before.stdout)
        self._plant("CLAUDE.md", self.HOSTILE.encode())
        after = self.verify("--post-read")
        self.assertEqual(0, after.returncode, after.stdout)
        self.assertEqual(self.census(before.stdout), self.census(after.stdout),
                         "an edit to an exempt input must not move the census")


class HandoverGateCensusTests(SurfaceFixture):
    """Mirror `M-4` — the census, and the two contracts, at the run that GATES HANDOVER.

    🔴 The defect these probe: the census block sat behind `if args.post_read:` while the
    `PASS` sentence printed *"SCANNED and [UNCHECKED] partition the present files … no
    present file is skipped by the identifier scan without appearing in that list"* in both
    modes. `unchecked_surface()` already took the mode as a parameter, defaulting to `True`,
    with its only call site inside the guard — so the parameter existed, was threaded
    correctly, and could never be `False` from the CLI. On a clean build of the real
    benchmark that is **sixteen present files per surface, before any reader exists**, and
    the whole of `controlled_benchmark_ab.md` encoded UTF-16 into an allowlisted `.md` in
    both surfaces passed the handover gate with the path named **zero** times.

    Every case here asserts the MODE it ran in, from the tool's own output, before it
    asserts anything else — because the instrument that found `M-4` was already in the
    suite, pointed at the other mode, asserting constants named for this one.
    """

    # The whole forbidden artifact, not a token: prose with identifiers in it, of the kind a
    # copy of prior LEGEND output actually is.
    #
    # 🔴 THE `§` IS LOAD-BEARING, and it cost this battery four red rows to learn — twice,
    # because the first repair was wrong for the same reason as the thing it repaired.
    #
    # Mirror `P-7` records that a **pure-ASCII** payload in BOM-less UTF-16 is bytes all
    # below 0x80, so `read_text(encoding="utf-8", errors="strict")` SUCCEEDS: the file is
    # genuinely scanned and is right not to be in the census. `REV-SCIAB-MIRROR-004` §8
    # bounds it with *"it disappears the moment the payload contains one non-ASCII
    # character, which the real forbidden artifacts all do"*. **That criterion is too
    # loose, and this battery measured it.** UTF-16LE encodes `—` U+2014 as `14 20` and
    # `‘’ “”` U+2018-201D as `18 20 … 1D 20` — every byte below 0x80. The typographic
    # characters LEGEND prose is actually full of are non-ASCII and still decode.
    #
    # The true criterion is a byte, not a character: the payload must contain a code point
    # one of whose UTF-16 bytes is ≥ 0x80 and lands where UTF-8 cannot read it — `§`
    # U+00A7 → `A7 00`, an emoji, an accented Latin letter — or carry a BOM, which is
    # `FF FE` and invalid UTF-8 on its own. The real artifacts do satisfy it (`§`, `🔴`),
    # so `P-7` stays narrow and Mirror's conclusion stands; its stated test does not.
    HOSTILE_TEXT = (f"LEGEND's prior dossier for PMID {IDENTIFIER} — Aqeilan et al., "
                    "copied whole into the surface, §4.3.\n") * 8

    def _plant_both(self, rel: str, payload: bytes) -> None:
        """Identical bytes into BOTH surfaces — the move parity is blind to (Mirror `P-4`).

        A payload written to one surface only is caught by `PARITY BROKEN`, and a battery
        that does that measures the parity check while believing it measures the scan.
        """
        for surface in (self.a, self.b):
            target = surface / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(payload)

    def test_positive_control_a_clean_pair_passes_the_handover_gate(self) -> None:
        """The discriminator. Every negative below is read against this one."""
        result, argv = self.verify_pre()
        self.assert_mode(result, argv, self.MODE_PRE)
        self.assertEqual(0, result.returncode, result.stdout)
        self.assertIn("VERDICT: PASS (pre-handover)", result.stdout)

    def test_positive_control_the_scan_fires_at_the_handover_gate(self) -> None:
        """UTF-8 hostile text: the gate must catch it. Without this, every `PASS` below is
        equally consistent with a scan that never ran."""
        self._plant_both("roles/scientist.md", self.HOSTILE_TEXT.encode("utf-8"))
        result, argv = self.verify_pre()
        self.assert_mode(result, argv, self.MODE_PRE)
        self.assertEqual(1, result.returncode, result.stdout)
        self.assertIn("IDENTIFIER LEAK scientist-a  roles/scientist.md", result.stdout)
        self.assertIn("IDENTIFIER LEAK scientist-b  roles/scientist.md", result.stdout)
        self.assertNotIn("PARITY BROKEN", result.stdout)
        self.assertNotIn("roles/scientist.md", self.census(result.stdout))

    def test_the_handover_gate_censuses_every_file_the_scan_did_not_read(self) -> None:
        """The census exists pre-handover, and it is exactly the fixture's literal.

        🔴 Revision 4 printed **nothing** here. The expectation is `FIXTURE_CENSUS_AT_HANDOVER`,
        hand-written from what `build_fixture` puts on disk — the same literal the post-read
        control uses, asserted separately, because two modes agreeing is a measurement and
        not a reason to measure once.
        """
        result, argv = self.verify_pre()
        self.assert_mode(result, argv, self.MODE_PRE)
        self.assertEqual(0, result.returncode, result.stdout)
        self.assertEqual(FIXTURE_CENSUS_AT_HANDOVER, self.census(result.stdout),
                         result.stdout)
        self.assertIn(f"[UNCHECKED SURFACE] {self.census_rows(result.stdout)} present "
                      "file(s)", result.stdout)

    def test_the_handover_gate_names_the_exempt_input_it_did_not_read(self) -> None:
        """The sharpest single path of `M-4`: `CLAUDE.md` is `scan_exempt_input`, so the
        gate never opens it — and revision 4 never said so. Hostile bytes there are still
        invisible to the scan by design; what changed is that the file is now NAMED, so a
        reviewer reads which files the `PASS` did not cover."""
        self._plant_both("CLAUDE.md", self.HOSTILE_TEXT.encode("utf-8"))
        result, argv = self.verify_pre()
        self.assert_mode(result, argv, self.MODE_PRE)
        self.assertEqual(0, result.returncode, result.stdout)
        self.assertEqual("scan_exempt_input", self.census(result.stdout)["CLAUDE.md"])
        self.assertEqual("scan_exempt_input", self.census(result.stdout, "scientist-b")
                         ["CLAUDE.md"])
        self.assertNotIn("IDENTIFIER LEAK", result.stdout)

    def test_the_handover_gate_names_a_non_text_suffix_it_never_opened(self) -> None:
        """`.gitkeep` holds an output slot open: allowlisted, present, decodable, and
        outside `text_suffixes`, so the scan never reads it in either mode."""
        result, argv = self.verify_pre()
        self.assert_mode(result, argv, self.MODE_PRE)
        self.assertEqual("suffix_not_scanned",
                         self.census(result.stdout)["output/renders/.gitkeep"])

    # ---- EXPECTED_BY_PROTOCOL: NO — blocking here, informational there (§4.4) ----

    UTF16_CASES = (
        ("utf-16-le", False), ("utf-16-le", True),
        ("utf-16-be", False), ("utf-16-be", True),
        ("utf-16", True),
    )

    @staticmethod
    def _encode(text: str, encoding: str, bom: bool) -> bytes:
        raw = text.encode(encoding)
        if bom and encoding == "utf-16-le":
            raw = b"\xff\xfe" + raw
        if bom and encoding == "utf-16-be":
            raw = b"\xfe\xff" + raw
        return raw

    def test_a_utf16_allowlisted_text_file_blocks_the_handover_gate(self) -> None:
        """🔴 THE HOSTILE CASE, in the mode that decides whether a surface is handed over.

        The payload is prior LEGEND output re-encoded UTF-16 and written IDENTICALLY into
        both surfaces at an allowlisted `.md` the scan normally reads. `read_text(strict)`
        fails, so the scan cannot see it and parity cannot either. Revision 4 answered
        `VERDICT: PASS` with the path named zero times.

        The expected result is taken from what `controlled_benchmark_ab.md` §4.4 DECLARES,
        not read off revision 4's behaviour. Two parts, with different standing. §2.2 makes
        Plan the only writer until handover and `build` copies without templating, so a
        text-suffixed file that is not text is a state `build` cannot produce from a text
        source — the source root carries one, or the surface was patched, which §3 forbids
        by name; either way the pre-handover guarantee cannot be said over it. That much is
        derived. That the response is a FINDING with `rc=1`, rather than an enumeration
        under a narrowed guarantee row, is §4.4's declared POLICY CHOICE (a) — see its
        POLICY CHOICE block. This test pins the declared rule; it does not prove the rule
        was the only one available.
        """
        for encoding, bom in self.UTF16_CASES:
            with self.subTest(encoding=encoding, bom=bom):
                self._plant_both("roles/scientist.md",
                                 self._encode(self.HOSTILE_TEXT, encoding, bom))
                result, argv = self.verify_pre()
                self.assert_mode(result, argv, self.MODE_PRE)
                self.assertEqual(1, result.returncode, result.stdout)
                self.assertIn("UNANTICIPATED   scientist-a  roles/scientist.md",
                              result.stdout)
                self.assertIn("UNANTICIPATED   scientist-b  roles/scientist.md",
                              result.stdout)
                # named in the census too, with its class — a finding is not a substitute
                # for the enumeration, it is the second thing said about the same file
                self.assertEqual("undecodable_text",
                                 self.census(result.stdout)["roles/scientist.md"])
                self.assertIn("EXPECTED_BY_PROTOCOL NO", result.stdout)
                self.assertIn("pre-handover that is a finding above", result.stdout)
                self.assertNotIn("VERDICT: PASS", result.stdout)
                # the scan could not read it, so it must NOT be reported as a leak: the
                # finding is the anomaly, and calling it a leak would be a wrong reason
                self.assertNotIn("IDENTIFIER LEAK", result.stdout)
                self.assertNotIn("PARITY BROKEN", result.stdout)

    def test_the_same_utf16_file_is_informational_after_the_freeze(self) -> None:
        """The other half of §4.4, and the guard against over-reading the row above.

        Post-read the writer is the reader, who may legitimately emit UTF-16; what the
        protocol claims there is ENUMERATION, and Mirror `REV-SCIAB-MIRROR-004` §9 ruled
        `EXPECTED_BY_PROTOCOL: NO` informational on exactly that ground. Identical bytes,
        identical paths, one flag apart: named, counted, and `PASS`.
        """
        self._plant_both("roles/scientist.md",
                         self._encode(self.HOSTILE_TEXT, "utf-16-le", True))
        result, argv = self.verify_post()
        self.assert_mode(result, argv, self.MODE_POST)
        self.assertEqual(0, result.returncode, result.stdout)
        self.assertIn("VERDICT: PASS (--post-read)", result.stdout)
        self.assertEqual("undecodable_text",
                         self.census(result.stdout)["roles/scientist.md"])
        self.assertIn("2 of them are NOT a consequence the protocol declares — read those "
                      "lines first.", result.stdout)
        self.assertNotIn("UNANTICIPATED", result.stdout)

    def test_positive_control_the_same_payload_in_utf8_is_read_and_caught(self) -> None:
        """The anti-vacuity guard for the two rows above: the difference between them is
        the ENCODING, not the path, the payload or the invocation. In UTF-8 the same bytes
        at the same path in the same mode produce a leak rather than an anomaly."""
        self._plant_both("roles/scientist.md", self.HOSTILE_TEXT.encode("utf-8"))
        result, argv = self.verify_pre()
        self.assert_mode(result, argv, self.MODE_PRE)
        self.assertEqual(1, result.returncode, result.stdout)
        self.assertIn("IDENTIFIER LEAK scientist-a  roles/scientist.md", result.stdout)
        self.assertNotIn("UNANTICIPATED", result.stdout)
        self.assertNotIn("roles/scientist.md", self.census(result.stdout))

    def test_positive_control_a_clean_utf16_file_still_blocks_at_handover(self) -> None:
        """The rule is about the STATE, not about the payload. A UTF-16 file with nothing
        forbidden in it is still a file `build` cannot have produced from a text source, and
        the gate cannot say `all of it observed` over it. Without this control the finding
        above would be indistinguishable from a leak detector that happens to fire."""
        self._plant_both("roles/scientist.md",
                         "un'osservazione del tutto innocua, §1 — niente identificatori\n"
                         .encode("utf-16-le"))
        result, argv = self.verify_pre()
        self.assert_mode(result, argv, self.MODE_PRE)
        self.assertEqual(1, result.returncode, result.stdout)
        self.assertIn("UNANTICIPATED   scientist-a  roles/scientist.md", result.stdout)
        self.assertNotIn("IDENTIFIER LEAK", result.stdout)

    def test_bomless_utf16_decodes_as_utf8_unless_a_byte_exceeds_7f(self) -> None:
        """🔴 Mirror `P-7`, pinned as behaviour — and its stated criterion corrected.

        `read_text(encoding="utf-8", errors="strict")` succeeds on BOM-less UTF-16 whenever
        every byte is below 0x80, and then the file is GENUINELY SCANNED: the regex runs
        over a NUL-interleaved decoding and finds nothing. The census is right to omit it —
        the scan did open it — so this is a limit of the scan, not a hole in the census,
        and *nothing scanned leaked an identifier* stays literally true.

        `REV-SCIAB-MIRROR-004` §8 bounds `P-7` with *"it disappears the moment the payload
        contains one non-ASCII character"*. Row 2 falsifies that: `—` U+2014 is non-ASCII
        and encodes to `14 20` in UTF-16LE, both below 0x80 — as do the en dash and all four
        curly quotes, which is most of what makes real prose non-ASCII. The criterion is a
        BYTE, not a character. Row 3 is the one that actually holds, and the real forbidden
        artifacts satisfy it via `§` and `🔴`, so Mirror's conclusion survives its test.
        """
        base = f"prior dossier for PMID {IDENTIFIER}, copied whole\n"
        rows = (
            ("pure ASCII", base, False),
            ("em dash and curly quotes — all non-ASCII, all bytes < 0x80",
             f"— ‘{base}’", False),
            ("section sign U+00A7 → A7 00", f"§4.3 {base}", True),
        )
        for label, payload, undecodable in rows:
            with self.subTest(payload=label):
                self._plant_both("roles/scientist.md", payload.encode("utf-16-le"))
                result, argv = self.verify_pre()
                self.assert_mode(result, argv, self.MODE_PRE)
                if undecodable:
                    self.assertEqual(1, result.returncode, result.stdout)
                    self.assertIn("UNANTICIPATED   scientist-a  roles/scientist.md",
                                  result.stdout)
                    self.assertEqual("undecodable_text",
                                     self.census(result.stdout)["roles/scientist.md"])
                else:
                    self.assertEqual(0, result.returncode, result.stdout)
                    self.assertIn("VERDICT: PASS (pre-handover)", result.stdout)
                    self.assertNotIn("roles/scientist.md", self.census(result.stdout))
                    self.assertNotIn("UNANTICIPATED", result.stdout)

        # A BOM is `FF FE`, which is not valid UTF-8 on its own, so the same pure-ASCII
        # payload that passes above is undecodable the moment it carries one.
        self._plant_both("roles/scientist.md", b"\xff\xfe" + base.encode("utf-16-le"))
        with_bom, bom_argv = self.verify_pre()
        self.assert_mode(with_bom, bom_argv, self.MODE_PRE)
        self.assertEqual(1, with_bom.returncode, with_bom.stdout)
        self.assertIn("UNANTICIPATED   scientist-a  roles/scientist.md", with_bom.stdout)

    def test_the_handover_gate_exempts_no_forbidden_path(self) -> None:
        """The blind spot is a post-read object, and the pre-handover row of §4.4 says the
        gate exempts nothing. The colliding path is the one `--post-read` must skip; here it
        is a finding, and the printed blind-spot line says the mode exempts none."""
        self._plant_both(FORBIDDEN_COLLIDING, b'{"pmid": "42397075"}\n')
        result, argv = self.verify_pre()
        self.assert_mode(result, argv, self.MODE_PRE)
        self.assertEqual(1, result.returncode, result.stdout)
        self.assertIn(f"PRIOR OUTPUT    scientist-a  {FORBIDDEN_COLLIDING}", result.stdout)
        self.assertIn("[BLIND SPOT] none in this mode", result.stdout)
        post, post_argv = self.verify_post()
        self.assert_mode(post, post_argv, self.MODE_POST)
        self.assertNotIn(f"PRIOR OUTPUT    scientist-a  {FORBIDDEN_COLLIDING}", post.stdout)


class CensusContractTests(unittest.TestCase):
    """Structural guards on the census itself, read from the module rather than its output."""

    @staticmethod
    def _module():
        import importlib.util
        spec = importlib.util.spec_from_file_location("bis_under_test", TOOL)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    def test_every_class_the_predicate_can_return_has_an_explanation(self) -> None:
        """🔴 The census prints from `SCAN_SKIP_CLASSES` keyed by what `scan_skip_reason()`
        returns. A new skip condition without a matching entry must be a loud error, not a
        file that silently stops being printed — which is Mirror `M-3` in one line."""
        module = self._module()
        source = inspect.getsource(module.scan_skip_reason)
        returned = set(re.findall(r'return "([a-z_]+)"', source))
        self.assertEqual(set(module.SCAN_SKIP_CLASSES), returned,
                         "SCAN_SKIP_CLASSES and scan_skip_reason() disagree")
        for name, described in module.SCAN_SKIP_CLASSES.items():
            self.assertTrue(described["reason"].strip(), name)
            self.assertTrue(described["still_covered_by"].strip(), name)
            self.assertIn(described["expected"], (True, False), name)

    def test_the_scan_and_the_census_call_the_same_predicate(self) -> None:
        """The equality `actual unscanned == declared unscanned` must hold by construction.

        Revision 3 maintained it with two copies of the skip rule and one of them was three
        conditions short. Two call sites, one function: that is the whole repair.
        """
        module = self._module()
        for function in (module.cmd_verify, module.unchecked_surface):
            self.assertIn("scan_skip_reason", inspect.getsource(function),
                          f"{function.__name__} does not go through the shared predicate")

    def test_every_scan_exempt_path_in_the_real_spec_is_an_allowlisted_path(self) -> None:
        """The census tells a reviewer an exempt input *still took the allowlist check*.

        That sentence is only true if every exempt path is in the allowlist, so this is the
        probe behind the claim rather than the claim repeated. A path exempt from the scan
        and absent from the allowlist would be checked by nothing at all.
        """
        module = self._module()
        spec = json.loads((ROOT / "framework/eval/benchmarks/BENCH-AB-001/surface_spec.json")
                          .read_text(encoding="utf-8"))
        for actor in spec["actors"]:
            allowed = module._allowed_paths(spec, actor)
            allowed |= {f"{rel}/.gitkeep" for rel in spec["empty_dirs"]}
            for rel in spec["content_scan"]["exempt_surface_paths"]:
                self.assertIn(rel, allowed, f"{rel} is exempt from the scan for {actor} "
                                            "and is not in the allowlist")


class LocatorTests(SurfaceFixture):
    """Mirror B-4 — a citation may not leave the surface by prefix, by `..`, or by name."""

    def _manifest(self, artifact: str) -> None:
        write(self.a / FORBIDDEN_COLLIDING, json.dumps({
            "source_artifacts": [{"path": "files/paper.txt"}],
            "verbatim_locators": {"entries": [{"artifact": artifact}]},
        }))

    def locators(self) -> subprocess.CompletedProcess:
        return run("locators", "--spec", str(self.spec), "--surface", str(self.a),
                   "--actor-id", "scientist-a", "--pmid", "42397075")

    def test_positive_control_citations_inside_the_surface_pass(self) -> None:
        self._manifest("output/renders/fig1.png")
        result = self.locators()
        self.assertEqual(0, result.returncode, result.stdout)
        self.assertIn("VERDICT: PASS", result.stdout)

    def test_forbidden_prior_output_under_an_output_prefix_is_rejected(self) -> None:
        """🔴 The path the repository always cites LEGEND's own dossier by."""
        self._manifest(FORBIDDEN_NON_COLLIDING)
        result = self.locators()
        self.assertEqual(1, result.returncode, result.stdout)
        self.assertIn("FORBIDDEN SOURCE", result.stdout)

    def test_traversal_out_of_the_tree_is_rejected(self) -> None:
        self._manifest("output/../../../etc/passwd")
        result = self.locators()
        self.assertEqual(1, result.returncode, result.stdout)
        self.assertIn("TRAVERSAL", result.stdout)

    def test_traversal_to_a_sibling_inside_the_tree_is_rejected(self) -> None:
        """`output/../secret_notes.md` normalizes INSIDE the tree and is still not allowlisted."""
        self._manifest("output/../secret_notes.md")
        result = self.locators()
        self.assertEqual(1, result.returncode, result.stdout)
        self.assertIn("OUTSIDE SURFACE", result.stdout)
        self.assertIn("NON-CANONICAL", result.stdout)

    def test_absolute_paths_are_rejected(self) -> None:
        self._manifest("/etc/passwd")
        result = self.locators()
        self.assertEqual(1, result.returncode, result.stdout)
        self.assertIn("ABSOLUTE PATH", result.stdout)

    def test_a_missing_manifest_refuses_with_code_two_not_one(self) -> None:
        """A refusal and a finding must not be indistinguishable by return code."""
        result = self.locators()
        self.assertEqual(2, result.returncode, result.stdout + result.stderr)
        self.assertIn("REFUSE", result.stderr)


class FreezeReceiptTests(SurfaceFixture):
    """Mirror B-3 — the receipt has to verify what it says, and detect substitution."""

    def freeze(self, actor: str, surface: Path, out: Path,
               *extra: str) -> subprocess.CompletedProcess:
        return run("freeze", "--surface", str(surface), "--actor-id", actor,
                   "--benchmark-id", "FIX-001", "--spec", str(self.spec),
                   "--out", str(out), *extra)

    def test_an_honest_freeze_carries_every_required_field(self) -> None:
        out = self.root / "receipt-a.json"
        result = self.freeze("scientist-a", self.a, out)
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        receipt = json.loads(out.read_text(encoding="utf-8"))
        for field in ("RECEIPT_SCHEMA_VERSION", "BENCHMARK_ID", "ACTOR_ID", "TASK_ID", "MODE",
                      "INSTRUCTIONS_VERSION", "OUTPUT_SCHEMA_VERSION",
                      "MANIFEST_SCHEMA_VERSION", "SURFACE_RELATIVE", "SURFACE_COMMIT",
                      "FREEZE_TIMESTAMP_UTC", "FIRST_PASS_STATE", "TREE_SHA256", "FILE_COUNT",
                      "OUTPUT_FILE_SET", "FILES", "GUARANTEE_PROVIDED",
                      "FAILURE_MODE_STILL_POSSIBLE"):
            self.assertIn(field, receipt, f"receipt is missing {field}")
        # Read from the tree, not from the command line.
        self.assertEqual("FIX-001-A", receipt["TASK_ID"])
        self.assertEqual("PRIMARY_EVIDENCE_READ", receipt["MODE"])
        self.assertEqual("7", str(receipt["INSTRUCTIONS_VERSION"]))
        self.assertEqual("3", str(receipt["OUTPUT_SCHEMA_VERSION"]))

    def test_the_receipt_records_no_machine_specific_absolute_path(self) -> None:
        out = self.root / "receipt-a.json"
        self.freeze("scientist-a", self.a, out)
        text = out.read_text(encoding="utf-8")
        self.assertNotIn(str(self.surfaces), text)
        self.assertIn("FIX-001/scientist-a", text)

    def test_freezing_one_actors_tree_under_the_other_name_refuses(self) -> None:
        """🔴 Revision 1 froze A's tree as `scientist-b` and recorded it without a murmur."""
        result = self.freeze("scientist-b", self.a, self.root / "bad.json")
        self.assertEqual(2, result.returncode, result.stdout + result.stderr)
        self.assertIn("ASSIGNMENT.md", result.stderr)

    def test_freezing_under_a_wrong_benchmark_id_refuses(self) -> None:
        result = run("freeze", "--surface", str(self.a), "--actor-id", "scientist-a",
                     "--benchmark-id", "BENCH-XX-999", "--out", str(self.root / "bad.json"))
        self.assertEqual(2, result.returncode, result.stdout + result.stderr)

    def test_freezing_a_tree_holding_a_symlink_refuses(self) -> None:
        outside = write(self.root / "outside/x.md", "elsewhere\n")
        (self.a / "output/link.md").symlink_to(outside)
        result = self.freeze("scientist-a", self.a, self.root / "bad.json")
        self.assertEqual(2, result.returncode, result.stdout + result.stderr)

    def test_an_invalid_first_pass_state_refuses(self) -> None:
        result = run("freeze", "--surface", str(self.a), "--actor-id", "scientist-a",
                     "--benchmark-id", "FIX-001", "--first-pass-state", "PROBABLY_DONE",
                     "--out", str(self.root / "bad.json"))
        self.assertNotEqual(0, result.returncode)


class FreezeTamperTests(SurfaceFixture):
    def setUp(self) -> None:
        super().setUp()
        write(self.a / "output/receipt.json", '{"first": true}\n')
        self.receipt = self.root / "receipt-a.json"
        result = run("freeze", "--surface", str(self.a), "--actor-id", "scientist-a",
                     "--benchmark-id", "FIX-001", "--spec", str(self.spec),
                     "--out", str(self.receipt))
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)

    def check(self, surface: Path | None = None) -> subprocess.CompletedProcess:
        return run("verify-freeze", "--receipt", str(self.receipt),
                   "--surface", str(surface or self.a))

    def test_positive_control_an_untouched_tree_passes(self) -> None:
        result = self.check()
        self.assertEqual(0, result.returncode, result.stdout)
        self.assertIn("VERDICT: PASS", result.stdout)

    def test_one_edited_byte_is_detected(self) -> None:
        with (self.a / "roles/scientist.md").open("a", encoding="utf-8") as handle:
            handle.write("x")
        result = self.check()
        self.assertEqual(1, result.returncode, result.stdout)
        self.assertIn("MODIFIED", result.stdout)

    def test_substitution_at_equal_file_count_is_detected(self) -> None:
        """Two trees of equal count holding different files is what a count says agree."""
        write(self.a / "output/receipt.json", '{"second": true}\n')
        result = self.check()
        self.assertEqual(1, result.returncode, result.stdout)
        self.assertIn("MODIFIED", result.stdout)
        self.assertIn("output/receipt.json", result.stdout)

    def test_an_added_file_is_detected(self) -> None:
        write(self.a / "output/extra.md", "added after the freeze\n")
        result = self.check()
        self.assertEqual(1, result.returncode, result.stdout)
        self.assertIn("ADDED", result.stdout)

    def test_a_removed_file_is_detected(self) -> None:
        (self.a / "output/receipt.json").unlink()
        result = self.check()
        self.assertEqual(1, result.returncode, result.stdout)
        self.assertIn("REMOVED", result.stdout)

    def test_a_symlink_appearing_after_the_freeze_is_detected(self) -> None:
        outside = write(self.root / "outside/y.md", "elsewhere\n")
        (self.a / "output/renders/link.md").symlink_to(outside)
        result = self.check()
        self.assertEqual(1, result.returncode, result.stdout)
        self.assertIn("SYMLINK APPEARED", result.stdout)

    def test_a_receipt_pointed_at_the_other_actors_tree_fails_on_identity(self) -> None:
        result = self.check(self.b)
        self.assertEqual(1, result.returncode, result.stdout)
        self.assertIn("IDENTITY MISMATCH", result.stdout)


class PopulationBoundingTests(unittest.TestCase):
    """Mirror B-1 — the bounding rule, on a fixture whose right answer is known.

    The real derivation runs over the article and its five supplements and is checked by
    re-running it; what is pinned here is the RULE, on captions built so that a fixed window
    of any size would get them wrong.
    """

    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def derive(self, text: str) -> dict:
        source = self.root / "src"
        write(source / "captions.txt", text)
        spec = {
            "spec_version": 2, "benchmark_id": "FIX-POP", "actors": ["x", "y"],
            "source_files": [{"source": "captions.txt", "surface": "files/captions.txt"}],
            "common_files": [], "per_actor_files": {"x": [], "y": []}, "empty_dirs": [],
            "forbidden_prior_output_paths": [], "expected_output_paths": [],
            "expected_output_prefixes": [],
            "content_scan": {"pattern": "zzz", "exempt_surface_paths": []},
            "population": {"sources": [{
                "source": "captions.txt", "surface": "files/captions.txt", "extraction": "regex",
                "rules": [{
                    "kind": "figure",
                    "pattern": r"^(?P<label>Figure \d+)\s+\S",
                    "sub_unit_kind": "panel",
                    "sub_unit_pattern": r"[(\[]([A-Z])(?=[)(])",
                    "sub_unit_range_pattern": r"[(\[]([A-Z])\s*[-–]\s*([A-Z])[)\]]",
                }],
            }]},
        }
        spec_path = write(self.root / "spec.json", json.dumps(spec))
        out = self.root / "pop.json"
        result = run("population", "--spec", str(spec_path), "--source-root", str(source),
                     "--out", str(out))
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        return json.loads(out.read_text(encoding="utf-8"))

    def panels(self, record: dict, label: str) -> list[str]:
        for unit in record["units"]:
            if unit["label"] == label:
                return unit["sub_units"]
        self.fail(f"no unit labelled {label!r}")

    def test_a_short_caption_does_not_absorb_the_next_one(self) -> None:
        """🔴 The defect, exactly: a short caption followed by a long-lettered neighbour."""
        record = self.derive(
            "Figure 1 first. (A) one. (B) two.\n"
            "Figure 2 second. (C) three. (D) four. (E) five. (F) six. (G) seven.\n")
        self.assertEqual(["A", "B"], self.panels(record, "Figure 1"))
        self.assertEqual(["C", "D", "E", "F", "G"], self.panels(record, "Figure 2"))

    def test_a_long_caption_is_not_truncated(self) -> None:
        """The other direction: a window long enough to over-run is also long enough to cut."""
        filler = "Text that goes on. " * 400
        record = self.derive(
            f"Figure 1 first. (A) one. {filler} (B) two. {filler} (C) three.\n"
            "Figure 2 second. (D) four.\n")
        self.assertEqual(["A", "B", "C"], self.panels(record, "Figure 1"))
        self.assertEqual(["D"], self.panels(record, "Figure 2"))

    def test_a_single_panel_figure_reports_one_panel(self) -> None:
        record = self.derive("Figure 1 only one. (A) the only panel.\nFigure 2 next. (B) b.\n")
        self.assertEqual(["A"], self.panels(record, "Figure 1"))

    def test_a_figure_with_no_lettered_panel_reports_none(self) -> None:
        record = self.derive("Figure 1 unlettered, a single image.\nFigure 2 next. (A) a.\n")
        self.assertEqual([], self.panels(record, "Figure 1"))

    def test_a_panel_range_is_expanded_not_approximated(self) -> None:
        record = self.derive("Figure 1 ranged. [A(i)] one. (C-F) the range. (H) eight.\n")
        self.assertEqual(["A", "C", "D", "E", "F", "H"], self.panels(record, "Figure 1"))

    def test_the_last_caption_is_bounded_by_the_end_of_the_segment(self) -> None:
        record = self.derive("Figure 1 first. (A) one.\nFigure 2 last. (B) two. (C) three.\n")
        self.assertEqual(["B", "C"], self.panels(record, "Figure 2"))

    def test_a_repeated_label_is_one_unit_and_still_bounds_its_predecessor(self) -> None:
        """This paper reprints every figure label in a trailing size listing."""
        record = self.derive(
            "Figure 1 first. (A) one. (B) two.\n"
            "Figure 2 second. (C) three.\n"
            "Figure 1 165x156 mm (DPI)\n"
            "Figure 2 140x90 mm (DPI)\n")
        self.assertEqual(2, record["counts"]["units"])
        self.assertEqual(["A", "B"], self.panels(record, "Figure 1"))
        self.assertEqual(["C"], self.panels(record, "Figure 2"))

    def test_a_kind_that_measures_zero_is_still_reported(self) -> None:
        """`main_table: 0` is a measurement; its absence would be an omission."""
        source = self.root / "src"
        write(source / "captions.txt", "Figure 1 one. (A) a.\n")
        spec = {
            "spec_version": 2, "benchmark_id": "FIX-POP", "actors": ["x", "y"],
            "source_files": [{"source": "captions.txt", "surface": "files/captions.txt"}],
            "common_files": [], "per_actor_files": {"x": [], "y": []}, "empty_dirs": [],
            "forbidden_prior_output_paths": [], "expected_output_paths": [],
            "expected_output_prefixes": [],
            "content_scan": {"pattern": "zzz", "exempt_surface_paths": []},
            "population": {"sources": [{
                "source": "captions.txt", "surface": "files/captions.txt", "extraction": "regex",
                "rules": [{"kind": "figure", "pattern": r"^(?P<label>Figure \d+)\s+\S"},
                          {"kind": "table", "pattern": r"^(?P<label>Table \d+)\s+[A-Z]"}],
            }]},
        }
        spec_path = write(self.root / "spec.json", json.dumps(spec))
        out = self.root / "pop.json"
        run("population", "--spec", str(spec_path), "--source-root", str(source),
            "--out", str(out))
        record = json.loads(out.read_text(encoding="utf-8"))
        self.assertEqual(0, record["counts"]["by_kind"]["table"])
        self.assertEqual(1, record["counts"]["by_kind"]["figure"])

    def test_an_unaccounted_packet_source_is_refused(self) -> None:
        """A source that is neither enumerated nor declared empty is unmeasurable coverage."""
        source = self.root / "src"
        write(source / "captions.txt", "Figure 1 one. (A) a.\n")
        write(source / "supplement.txt", "a supplement nobody wrote a rule for\n")
        spec = {
            "spec_version": 2, "benchmark_id": "FIX-POP", "actors": ["x", "y"],
            "source_files": [{"source": "captions.txt", "surface": "files/captions.txt"},
                             {"source": "supplement.txt", "surface": "files/supplement.txt"}],
            "common_files": [], "per_actor_files": {"x": [], "y": []}, "empty_dirs": [],
            "forbidden_prior_output_paths": [], "expected_output_paths": [],
            "expected_output_prefixes": [],
            "content_scan": {"pattern": "zzz", "exempt_surface_paths": []},
            "population": {"sources": [{
                "source": "captions.txt", "surface": "files/captions.txt", "extraction": "regex",
                "rules": [{"kind": "figure", "pattern": r"^(?P<label>Figure \d+)\s+\S"}],
            }]},
        }
        spec_path = write(self.root / "spec.json", json.dumps(spec))
        result = run("population", "--spec", str(spec_path), "--source-root", str(source))
        self.assertEqual(1, result.returncode, result.stdout)
        self.assertIn("UNACCOUNTED SOURCE", result.stdout)

    def test_declaring_the_source_empty_makes_it_pass(self) -> None:
        """The positive control for the refusal above: the declaration is what closes it."""
        source = self.root / "src"
        write(source / "captions.txt", "Figure 1 one. (A) a.\n")
        write(source / "supplement.txt", "author contributions only\n")
        spec = {
            "spec_version": 2, "benchmark_id": "FIX-POP", "actors": ["x", "y"],
            "source_files": [{"source": "captions.txt", "surface": "files/captions.txt"},
                             {"source": "supplement.txt", "surface": "files/supplement.txt"}],
            "common_files": [], "per_actor_files": {"x": [], "y": []}, "empty_dirs": [],
            "forbidden_prior_output_paths": [], "expected_output_paths": [],
            "expected_output_prefixes": [],
            "content_scan": {"pattern": "zzz", "exempt_surface_paths": []},
            "population": {
                "declared_empty_sources": [
                    {"source": "supplement.txt", "reason": "author contributions; no unit"}],
                "sources": [{
                    "source": "captions.txt", "surface": "files/captions.txt",
                    "extraction": "regex",
                    "rules": [{"kind": "figure", "pattern": r"^(?P<label>Figure \d+)\s+\S"}],
                }],
            },
        }
        spec_path = write(self.root / "spec.json", json.dumps(spec))
        result = run("population", "--spec", str(spec_path), "--source-root", str(source))
        self.assertEqual(0, result.returncode, result.stdout)


class SpecContractTests(unittest.TestCase):
    """The shipped BENCH-AB-001 spec must satisfy the invariants the protocol states about it."""

    @classmethod
    def setUpClass(cls) -> None:
        path = ROOT / "framework/eval/benchmarks/BENCH-AB-001/surface_spec.json"
        cls.spec = json.loads(path.read_text(encoding="utf-8"))

    def test_the_declared_blind_spot_is_exactly_one_path(self) -> None:
        blind = set(self.spec["expected_output_paths"]) & set(
            self.spec["forbidden_prior_output_paths"])
        self.assertEqual({FORBIDDEN_COLLIDING}, blind)

    def test_the_prefix_key_is_accounted_for_and_not_only_the_exact_key(self) -> None:
        """🔴 Mirror M-2 — the exemption is two keys; a census over one of them is false.

        The intersection above is a statement about `expected_output_paths` alone. This
        test is here so that a future prefix cannot be added without the spec saying what
        admits a path under it, which is the sentence the tool implements.
        """
        self.assertEqual(["output/renders/"], self.spec["expected_output_prefixes"])
        note = " ".join(self.spec["_expected_output_prefix_note"])
        self.assertIn("CANNOT decode it as UTF-8 text", note)
        self.assertIn("exempt from nothing", note)

    def test_no_forbidden_path_hides_under_a_declared_output_prefix(self) -> None:
        """A forbidden path under a prefix would be exempt by position and never printed."""
        for forbidden in self.spec["forbidden_prior_output_paths"]:
            for prefix in self.spec["expected_output_prefixes"]:
                self.assertFalse(forbidden.startswith(prefix),
                                 f"{forbidden} sits under the exempt prefix {prefix}")

    def test_every_packet_source_is_enumerated_or_declared_empty(self) -> None:
        packet = {entry["source"] for entry in self.spec["source_files"]}
        enumerated = {entry["source"] for entry in self.spec["population"]["sources"]}
        declared = {entry["source"]
                    for entry in self.spec["population"].get("declared_empty_sources", [])}
        self.assertEqual(set(), packet - enumerated - declared)
        self.assertEqual(set(), enumerated & declared)

    def test_no_population_rule_uses_a_fixed_character_window(self) -> None:
        """The bound is the next label or the end of the segment. Never an integer."""
        for source in self.spec["population"]["sources"]:
            for rule in source["rules"]:
                self.assertNotIn("panel_window", rule)
                self.assertNotIn("window", rule)

    def test_exactly_two_paths_differ_between_the_actors(self) -> None:
        per_actor = self.spec["per_actor_files"]
        for actor, entries in per_actor.items():
            self.assertEqual(2, len(entries), f"{actor} has {len(entries)} per-actor files")


if __name__ == "__main__":
    unittest.main(verbosity=2)
