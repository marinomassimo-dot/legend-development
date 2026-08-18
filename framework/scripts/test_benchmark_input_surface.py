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

import json
import os
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
                                     "benchmark/MODE_DIRECTIVE.md"],
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
        """What an honest reader leaves behind: its own manifest, dossier and receipt."""
        for surface in (self.a, self.b):
            write(surface / FORBIDDEN_COLLIDING, '{"pmid": "42397075"}\n')
            write(surface / "disease-models/wwox/research/fulltext_dossiers/PMID42397075.md",
                  "# dossier for PMID 42397075\n")
            write(surface / "output/receipt.json", '{"pmid": "42397075"}\n')
            write(surface / "output/renders/fig1.md", "a render naming 42397075\n")

    def test_positive_control_an_honest_reading_passes_post_read(self) -> None:
        """The reader's own outputs name the paper by construction and must not fire."""
        self._plausible_reading()
        result = self.verify("--post-read")
        self.assertEqual(0, result.returncode, result.stdout)
        self.assertIn("VERDICT: PASS", result.stdout)

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
