#!/usr/bin/env python3
"""Regressions for `reseal_dismech_baseline.py` — what a re-seal may and may not absorb.

🔴 WHY THIS EXISTS
------------------
A re-seal moves an anchor and re-hashes what is sealed, which zeroes every drift signal the
baseline was carrying — including signals that belong to somebody else. On 2026-09-27
BATCH_20260927_003 re-sealed for its own `CLAIM 016` correction and, in the same write, absorbed
a `PAPER 019` scope drift left standing by BATCH_20260927_001. It disclosed that in prose
afterwards, which is the best a tool with no opinion allows. The tool now has an opinion: every
drifted sealed block must be named with `--absorb`, or already acknowledged against the digest
the registry holds now. This suite is what keeps that opinion.

Everything runs in a throw-away git repository built with the real repository's layout, so the
two scripts under test find their own `REPO`/`REPO_ROOT` inside the fixture and no sealed file
of this repository is read, written or re-sealed.

Run: `python3 disease-models/wwox/analysis/scripts/test_reseal_dismech_baseline.py`
"""
from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
RESEAL = "disease-models/wwox/analysis/scripts/reseal_dismech_baseline.py"
PROTOCOL = "disease-models/wwox/analysis/scripts/dismech_independent_protocol.py"
CLAIMS = "disease-models/wwox/registries/claim_registry_current.md"
PAPERS = "disease-models/wwox/registries/paper_registry_current.md"
LEDGER = "disease-models/wwox/registries/fulltext_read_receipts.jsonl"
BASELINE = "disease-models/wwox/analysis/data/dismech_phase2_baseline.json"
OUTPUT = "disease-models/wwox/analysis/data/dismech_sidecar_016_024_035.jsonl"
AUTHORED = "disease-models/wwox/analysis/data/dismech_authored_assertions.json"
DRIFT_LOG = "disease-models/wwox/analysis/data/dismech_drift_acknowledgements.jsonl"

CLAIM_REGISTRY = """# Claim registry

## CLAIM 016

**Status:** consolidated baseline

GSK3beta abundance, as first sealed.

---

## CLAIM 024

**Status:** working hypothesis

Untouched by any test below.

---
"""
PAPER_REGISTRY = """# Paper registry

## PAPER 019

**Claim links:** CLAIM 016

As first sealed.

---
"""

sys.path.insert(0, str(HERE))
import dismech_independent_protocol as protocol  # noqa: E402
import reseal_dismech_baseline as reseal  # noqa: E402  (the ordinal rules are pure functions)


def digest(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def block_digest(text: str, block: str) -> str:
    return digest(protocol.registry_scope_bytes(text, [block]))


class ResealFixture(unittest.TestCase):
    """A repository shaped like this one, with a baseline of the real shape."""

    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory(prefix="legend-reseal-test-")
        self.addCleanup(self._tmp.cleanup)
        self.repo = Path(self._tmp.name) / "repo"
        for relative in (RESEAL, PROTOCOL):
            (self.repo / relative).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(HERE / Path(relative).name, self.repo / relative)
        self.write(CLAIMS, CLAIM_REGISTRY)
        self.write(PAPERS, PAPER_REGISTRY)
        self.write(LEDGER, "".join(
            json.dumps({"event_id": f"FTR-{n:02d}"}) + "\n" for n in range(1, 4)))
        self.write(AUTHORED, json.dumps({"assertions": []}) + "\n")
        self.write(OUTPUT, json.dumps({"record_kind": "header"}) + "\n")
        self.write(BASELINE, json.dumps(self.baseline(), indent=2, sort_keys=True) + "\n")
        self.git("init", "-q", "-b", "main")
        self.git("config", "user.name", "reseal-test")
        self.git("config", "user.email", "reseal@example.invalid")
        self.commit("seed")

    # ----------------------------------------------------------------- fixture helpers

    def write(self, relative: str, text: str) -> None:
        path = self.repo / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def read_baseline(self) -> dict:
        return json.loads((self.repo / BASELINE).read_text(encoding="utf-8"))

    def baseline(self) -> dict:
        ledger_bytes = (self.repo / LEDGER).read_bytes()
        prefix = b"".join(ledger_bytes.splitlines(keepends=True)[:2])
        return {
            "frozen_at": "2026-09-01T00:00:00Z",
            "git_head_at_freeze": "0" * 40,
            "inputs": {
                "authored_assertions": {
                    "path": AUTHORED,
                    "sha256": digest((self.repo / AUTHORED).read_bytes())},
                "claim_registry": {
                    "path": CLAIMS, "verification_policy": "sealed_scope",
                    "scope_blocks": ["CLAIM 016", "CLAIM 024"],
                    "scope_sha256": digest(protocol.registry_scope_bytes(
                        CLAIM_REGISTRY, ["CLAIM 016", "CLAIM 024"])),
                    "scope_block_sha256": {
                        "CLAIM 016": block_digest(CLAIM_REGISTRY, "CLAIM 016"),
                        "CLAIM 024": block_digest(CLAIM_REGISTRY, "CLAIM 024")}},
                "paper_registry": {
                    "path": PAPERS, "verification_policy": "sealed_scope",
                    "scope_blocks": ["PAPER 019"],
                    "scope_sha256": digest(protocol.registry_scope_bytes(
                        PAPER_REGISTRY, ["PAPER 019"])),
                    "scope_block_sha256": {
                        "PAPER 019": block_digest(PAPER_REGISTRY, "PAPER 019")}},
                "receipt_ledger": {
                    "path": LEDGER, "verification_policy": "append_only_prefix",
                    "prefix_event_count": 2, "prefix_sha256": digest(prefix),
                    "prefix_tail_event_id": "FTR-02",
                    "sha256": digest(ledger_bytes)},
            },
            "output": {"path": OUTPUT, "records": 1,
                       "sha256": digest((self.repo / OUTPUT).read_bytes())},
            "revision": "rev.1 (the seal under test)",
        }

    def git(self, *args: str) -> str:
        return subprocess.run(["git", *args], cwd=self.repo, check=True,
                              capture_output=True, text=True).stdout.strip()

    def commit(self, message: str) -> None:
        self.git("add", "-A")
        self.git("commit", "-q", "-m", message)

    def reseal(self, *args: str) -> subprocess.CompletedProcess:
        return subprocess.run([sys.executable, RESEAL, *args], cwd=self.repo,
                              capture_output=True, text=True)

    def drift_claim_016(self) -> None:
        self.write(CLAIMS, CLAIM_REGISTRY.replace(
            "GSK3beta abundance, as first sealed.",
            "GSK3beta abundance, withdrawn: single-lane densitometry, NOT_TESTED."))

    def drift_paper_019(self) -> None:
        """Somebody else's batch moved a sealed paper block and left the drift standing."""
        self.write(PAPERS, PAPER_REGISTRY.replace(
            "As first sealed.", "Edited by an earlier, unrelated batch."))


class AnUndeclaredAbsorptionIsRefused(ResealFixture):
    def test_the_paper_019_case_is_refused_and_nothing_is_written(self) -> None:
        """The 2026-09-27 defect, reproduced: one batch's re-seal, two batches' drift."""
        self.drift_claim_016()
        self.drift_paper_019()
        self.commit("this batch's claim edit, plus a drift left by an earlier batch")
        before = (self.repo / BASELINE).read_bytes()
        done = self.reseal("--revision", "rev.2 (CLAIM 016 withdrawn)", "--absorb", "CLAIM 016")
        self.assertEqual(2, done.returncode, done.stdout + done.stderr)
        self.assertIn("REFUSED", done.stdout)
        self.assertIn("PAPER 019", done.stdout)
        self.assertNotIn("CLAIM 016\n", done.stdout.split("Name each block")[0])
        self.assertEqual(before, (self.repo / BASELINE).read_bytes(),
                         "a refused re-seal must not write")

    def test_check_mode_reports_the_refusal_too(self) -> None:
        """`--check` is the mode a batch runs first; it must not look clean."""
        self.drift_paper_019()
        self.commit("unrelated drift")
        done = self.reseal("--check")
        self.assertEqual(2, done.returncode, done.stdout + done.stderr)
        self.assertIn("PAPER 019", done.stdout)

    def test_naming_every_drifted_block_is_accepted(self) -> None:
        self.drift_claim_016()
        self.drift_paper_019()
        self.commit("both")
        done = self.reseal("--revision", "rev.2 (both declared)",
                           "--absorb", "CLAIM 016", "--absorb", "PAPER 019")
        self.assertEqual(0, done.returncode, done.stdout + done.stderr)
        sealed = self.read_baseline()
        self.assertEqual("rev.2 (both declared)", sealed["revision"])
        self.assertEqual(self.git("rev-parse", "HEAD"), sealed["git_head_at_freeze"])
        current = (self.repo / CLAIMS).read_text(encoding="utf-8")
        self.assertEqual(block_digest(current, "CLAIM 016"),
                         sealed["inputs"]["claim_registry"]["scope_block_sha256"]["CLAIM 016"])
        self.assertEqual(digest(protocol.registry_scope_bytes(current, ["CLAIM 016", "CLAIM 024"])),
                         sealed["inputs"]["claim_registry"]["scope_sha256"])

    def test_an_untouched_block_keeps_its_hash(self) -> None:
        """Re-sealing is not a licence to move what did not move."""
        self.drift_claim_016()
        self.commit("claim 016 only")
        before = self.read_baseline()["inputs"]["claim_registry"]["scope_block_sha256"]
        done = self.reseal("--revision", "rev.2 (016)", "--absorb", "CLAIM 016")
        self.assertEqual(0, done.returncode, done.stdout + done.stderr)
        after = self.read_baseline()["inputs"]["claim_registry"]["scope_block_sha256"]
        self.assertEqual(before["CLAIM 024"], after["CLAIM 024"])
        self.assertNotEqual(before["CLAIM 016"], after["CLAIM 016"])

    def test_absorbing_a_block_that_did_not_drift_is_only_a_note(self) -> None:
        done = self.reseal("--check", "--absorb", "CLAIM 024")
        self.assertEqual(0, done.returncode, done.stdout + done.stderr)
        self.assertIn("has not drifted", done.stdout)


class AnAcknowledgementLicensesAnAbsorption(ResealFixture):
    """The protocol's own drift log is the other way to declare an absorption."""

    def acknowledge(self, block: str, live_sha256: str) -> None:
        self.write(DRIFT_LOG, json.dumps({
            "block": block, "live_sha256": live_sha256,
            "verdict": "no_reissue_needed", "by": "reseal-test"}) + "\n")

    def test_an_acknowledgement_bound_to_the_current_digest_is_enough(self) -> None:
        self.drift_paper_019()
        self.acknowledge("PAPER 019",
                         block_digest((self.repo / PAPERS).read_text(encoding="utf-8"),
                                      "PAPER 019"))
        self.commit("drift plus its acknowledgement")
        done = self.reseal("--revision", "rev.2 (acknowledged)")
        self.assertEqual(0, done.returncode, done.stdout + done.stderr)

    def test_a_stale_acknowledgement_does_not_carry_over(self) -> None:
        """An acknowledgement expires when the block moves again — `unresolved_drift`'s rule."""
        self.drift_paper_019()
        self.acknowledge("PAPER 019", "0" * 64)
        self.commit("drift plus a stale acknowledgement")
        done = self.reseal("--revision", "rev.2 (stale ack)")
        self.assertEqual(2, done.returncode, done.stdout + done.stderr)
        self.assertIn("PAPER 019", done.stdout)


class TheOtherRefusals(ResealFixture):
    def test_writing_without_a_revision_is_refused(self) -> None:
        self.drift_claim_016()
        self.commit("claim 016")
        done = self.reseal("--absorb", "CLAIM 016")
        self.assertEqual(2, done.returncode, done.stdout + done.stderr)
        self.assertIn("--revision is required", done.stdout)

    def test_an_uncommitted_declared_path_is_refused(self) -> None:
        self.drift_claim_016()
        done = self.reseal("--revision", "rev.2 (dirty)", "--absorb", "CLAIM 016")
        self.assertEqual(2, done.returncode, done.stdout + done.stderr)
        self.assertIn("not committed", done.stdout)

    def test_the_refused_path_is_printed_whole_and_unstaged_is_the_case_that_bit(self) -> None:
        """The refusal names a file, so the name has to be copyable.

        Until 2026-09-28 it was not. `_dirty` sliced `status --porcelain`'s fixed two-column
        prefix with `line[3:]`, while `_git` returns `stdout.strip()` — which eats the LEADING
        space of a worktree-only modification (` M path` -> `M path`), so the slice ate the
        path's first character and the refusal printed `isease-models/wwox/...`. The test above
        never saw it because it asserts only the sentence. It bit the FIRST line of the output
        and only for UNSTAGED changes, which is why this case leaves the drift unstaged and
        the next one stages it: a fixture that stages its change cannot reproduce the defect.
        """
        self.drift_claim_016()
        done = self.reseal("--revision", "rev.2 (dirty)", "--absorb", "CLAIM 016")
        self.assertEqual(2, done.returncode, done.stdout + done.stderr)
        self.assertIn(f"  - {CLAIMS}", done.stdout)
        self.assertNotIn(CLAIMS[1:] + "\n", done.stdout.replace(CLAIMS, ""))

    def test_a_staged_declared_path_is_refused_and_named_whole_too(self) -> None:
        self.drift_claim_016()
        subprocess.run(["git", "add", "--", CLAIMS], cwd=self.repo, check=True,
                       capture_output=True)
        done = self.reseal("--revision", "rev.2 (staged)", "--absorb", "CLAIM 016")
        self.assertEqual(2, done.returncode, done.stdout + done.stderr)
        self.assertIn(f"  - {CLAIMS}", done.stdout)

    def test_a_moved_append_only_prefix_is_an_incident(self) -> None:
        lines = (self.repo / LEDGER).read_text(encoding="utf-8").splitlines()
        lines[0] = json.dumps({"event_id": "FTR-01", "rewritten": True})
        self.write(LEDGER, "\n".join(lines) + "\n")
        self.commit("the ledger prefix was rewritten")
        done = self.reseal("--revision", "rev.2 (prefix)")
        self.assertNotEqual(0, done.returncode)
        self.assertIn("incident, not a re-seal", done.stdout + done.stderr)

    def test_appending_to_the_ledger_never_re_seals_the_prefix(self) -> None:
        with (self.repo / LEDGER).open("a", encoding="utf-8") as handle:
            handle.write(json.dumps({"event_id": "FTR-04"}) + "\n")
        self.commit("a receipt was appended")
        before = self.read_baseline()["inputs"]["receipt_ledger"]
        done = self.reseal("--revision", "rev.2 (append)")
        self.assertEqual(0, done.returncode, done.stdout + done.stderr)
        self.assertEqual(before, self.read_baseline()["inputs"]["receipt_ledger"],
                         "an append-only input must come out of a re-seal untouched")

    def test_a_removed_sealed_block_is_a_clean_refusal(self) -> None:
        self.write(CLAIMS, CLAIM_REGISTRY.split("## CLAIM 024")[0])
        self.commit("CLAIM 024 removed")
        done = self.reseal("--revision", "rev.2 (removed)", "--absorb", "CLAIM 024")
        self.assertNotEqual(0, done.returncode)
        self.assertNotIn("Traceback", done.stderr)
        self.assertIn("no longer resolves", done.stdout + done.stderr)

    def test_a_plain_input_is_re_hashed(self) -> None:
        self.write(AUTHORED, json.dumps({"assertions": ["one"]}) + "\n")
        self.commit("authored assertions edited")
        done = self.reseal("--revision", "rev.2 (authored)")
        self.assertEqual(0, done.returncode, done.stdout + done.stderr)
        self.assertEqual(digest((self.repo / AUTHORED).read_bytes()),
                         self.read_baseline()["inputs"]["authored_assertions"]["sha256"])


class TheRevisionLabelMustGoUp(unittest.TestCase):
    """The ordinal rules, exercised on the pure functions — no git, no fixture needed."""

    def test_the_ordinal_is_read_from_the_label(self) -> None:
        self.assertEqual(18, reseal.label_ordinal("rev.18 (BATCH_X): why"))
        self.assertEqual(7, reseal.label_ordinal("rev. 7 (spaced)"))
        self.assertIsNone(reseal.label_ordinal("the seal of 2026-09-28"))

    def test_the_field_wins_over_the_label(self) -> None:
        self.assertEqual(20, reseal.stored_ordinal(
            {"revision": "rev.3 (mis-spelled)", "revision_ordinal": 20}))

    def test_a_pre_field_baseline_is_ordered_by_its_label(self) -> None:
        """The live baseline carries `rev.18` and no field; no migration may be needed."""
        self.assertEqual(18, reseal.stored_ordinal({"revision": "rev.18 (BATCH_20260928_001)"}))

    def test_a_lower_label_is_refused(self) -> None:
        ordinal, refusal = reseal.next_ordinal({"revision": "rev.18"}, "rev.3 (oops)", None)
        self.assertIsNone(ordinal)
        self.assertIn("does not exceed", refusal)
        self.assertIn("rev.19", refusal, "the refusal must say which label would be accepted")

    def test_a_duplicate_label_is_refused(self) -> None:
        """`rev.16` was written twice in 2026-08; distinct is not enough, monotone is."""
        ordinal, refusal = reseal.next_ordinal({"revision": "rev.16"}, "rev.16 (again)", None)
        self.assertIsNone(ordinal)
        self.assertIn("does not exceed", refusal)

    def test_a_higher_label_is_accepted(self) -> None:
        self.assertEqual((19, None), reseal.next_ordinal({"revision": "rev.18"}, "rev.19 (up)",
                                                         None))

    def test_a_label_without_an_ordinal_is_refused_unless_one_is_given(self) -> None:
        ordinal, refusal = reseal.next_ordinal({"revision": "rev.18"}, "the September seal", None)
        self.assertIsNone(ordinal)
        self.assertIn("could not be ordered", refusal)
        self.assertEqual((19, None), reseal.next_ordinal(
            {"revision": "rev.18"}, "the September seal", 19))

    def test_an_explicit_ordinal_must_still_go_up(self) -> None:
        ordinal, refusal = reseal.next_ordinal({"revision": "rev.18"}, "rev.99 (label lies)", 2)
        self.assertIsNone(ordinal)
        self.assertIn("does not exceed", refusal)

    def test_the_superseded_seal_is_captured_whole(self) -> None:
        entry = reseal.history_entry({"revision": "rev.17 — extractor strips separators",
                                      "frozen_at": "2026-08-07T00:00:00Z",
                                      "git_head_at_freeze": "497f4ee"})
        self.assertEqual(17, entry["revision_ordinal"])
        self.assertIn("extractor strips separators", entry["revision"])
        self.assertEqual("497f4ee", entry["git_head_at_freeze"])


class TheLabelHistorySurvivesAReseal(ResealFixture):
    def test_a_lower_label_is_refused_end_to_end_and_writes_nothing(self) -> None:
        self.drift_claim_016()
        self.commit("this batch's own edit")
        before = (self.repo / BASELINE).read_bytes()
        done = self.reseal("--revision", "rev.1 (same as stored)", "--absorb", "CLAIM 016")
        self.assertEqual(2, done.returncode, done.stdout + done.stderr)
        self.assertIn("does not exceed", done.stdout)
        self.assertEqual(before, (self.repo / BASELINE).read_bytes())

    def test_check_refuses_a_bad_label_before_reporting_changes(self) -> None:
        """A label that will be refused is better learned in --check than after the work."""
        done = self.reseal("--check", "--revision", "rev.1 (stale)")
        self.assertEqual(2, done.returncode, done.stdout + done.stderr)
        self.assertIn("does not exceed", done.stdout)

    def test_a_reseal_records_the_ordinal_and_keeps_the_previous_note(self) -> None:
        self.drift_claim_016()
        self.commit("this batch's own edit")
        head = self.git("rev-parse", "HEAD")
        done = self.reseal("--revision", "rev.2 (CLAIM 016 withdrawn)", "--absorb", "CLAIM 016")
        self.assertEqual(0, done.returncode, done.stdout + done.stderr)
        baseline = self.read_baseline()
        self.assertEqual(2, baseline["revision_ordinal"])
        self.assertEqual([{"revision": "rev.1 (the seal under test)", "revision_ordinal": 1,
                           "frozen_at": "2026-09-01T00:00:00Z",
                           "git_head_at_freeze": "0" * 40}],
                         baseline["revision_history"])
        self.assertEqual(head, baseline["git_head_at_freeze"])

    def test_history_accumulates_and_never_records_the_new_anchor_for_the_old_label(self) -> None:
        self.drift_claim_016()
        self.commit("first edit")
        first_head = self.git("rev-parse", "HEAD")
        self.assertEqual(0, self.reseal("--revision", "rev.2 (first)",
                                        "--absorb", "CLAIM 016").returncode)
        self.commit("the baseline itself")
        self.write(AUTHORED, json.dumps({"assertions": ["second"]}) + "\n")
        self.commit("second edit")
        self.assertEqual(0, self.reseal("--revision", "rev.5 (second, skipping 3 and 4)").returncode)
        baseline = self.read_baseline()
        self.assertEqual(5, baseline["revision_ordinal"])
        self.assertEqual([1, 2], [entry["revision_ordinal"]
                                 for entry in baseline["revision_history"]])
        self.assertEqual(first_head, baseline["revision_history"][1]["git_head_at_freeze"],
                         "the superseded entry must carry the anchor it was sealed on")

    def test_history_is_printable_and_writes_nothing(self) -> None:
        before = (self.repo / BASELINE).read_bytes()
        done = self.reseal("--history")
        self.assertEqual(0, done.returncode, done.stdout + done.stderr)
        self.assertIn("rev.1 (the seal under test)", done.stdout)
        self.assertEqual(before, (self.repo / BASELINE).read_bytes())

    def test_history_prints_every_commit_and_never_deduplicates_a_repeated_label(self) -> None:
        """🔴 THE MISCOUNT ITSELF. The version this replaced skipped a label it had already
        printed, so a repeated label collapsed into one row: 13 printed entries against 16
        commits, and three actors counted this history as 13, 15 and 16. A repeat is the finding.
        """
        # rev.1 (the seal under test) is already committed by the fixture. Write the SAME label
        # twice, as rev.16 really was on 2026-08-04 and 2026-08-06.
        for step, label in enumerate(("rev.4 — the repeated label", "rev.4 — the repeated label",
                                      "rev.9 — after the repeat"), start=1):
            self.write(AUTHORED, json.dumps({"assertions": [f"edit {step}"]}) + "\n")
            self.commit(f"edit {step}")
            ordinal = ("--revision-ordinal", str(step + 3)) if step == 2 else ()
            done = self.reseal("--revision", label, *ordinal)
            self.assertEqual(0, done.returncode, done.stdout + done.stderr)
            self.commit(f"the baseline itself {step}")

        printed = self.reseal("--history")
        self.assertEqual(0, printed.returncode, printed.stdout + printed.stderr)
        rows = [line for line in printed.stdout.splitlines()
                if "the repeated label" in line and line.startswith("  ")
                and "revision_history" not in line]
        self.assertGreaterEqual(len([row for row in rows if "] rev.4" in row]), 2,
                                "a label written twice must be printed twice:\n" + printed.stdout)

        series = next(line for line in printed.stdout.splitlines()
                      if line.startswith("ordinal series"))
        self.assertIn("1 -> 4 -> 4 -> 9", series, printed.stdout)
        # 🔴 And the caveat the rule states out loud: the git-side series is DERIVED from the
        # label's spelling, which is all a pre-field seal has. The second seal here was written
        # with --revision-ordinal 5 under a label that still says rev.4, so the field says 5 and
        # the derivation says 4. The rule is printed beside the series precisely so that reading
        # the difference is possible instead of surprising.
        self.assertEqual([1, 4, 5], [entry["revision_ordinal"]
                                     for entry in self.read_baseline()["revision_history"]])

        # The three counts, each labelled, so nobody has to choose which one "the count" is.
        commits = int(next(line for line in printed.stdout.splitlines()
                           if "commits touching the file" in line).split(":")[1])
        labels = int(next(line for line in printed.stdout.splitlines()
                          if "distinct label STRINGS" in line).split(":")[1])
        self.assertGreater(commits, labels,
                           "the two counts must be reported separately and must differ here")
        self.assertIn("DERIVATION RULE:", printed.stdout)
        self.assertIn("git log --follow", printed.stdout)
        # and the three conventions are named where the next writer will read them
        for convention in ("monotone-per-line", "reset-on-branch", "highest-ever + 1"):
            self.assertIn(convention, printed.stdout, f"{convention} is not named")
        self.assertIn("the next seal must be rev.", printed.stdout)

    def test_the_three_conventions_are_named_in_the_tool_itself(self) -> None:
        """Not only in the printed output: a reader opening the source must meet them too, so
        the next writer cannot invent a fourth without reading about the first three."""
        for convention in ("monotone-per-line", "reset-on-branch", "highest-ever + 1"):
            self.assertIn(convention, reseal.__doc__ or "")
        self.assertEqual(3, len(reseal.CONVENTIONS))
        self.assertIn("EXCEED", dict(reseal.CONVENTIONS)["highest-ever + 1"])


class TheHelpStatesTheContractTheBodyEnforces(unittest.TestCase):
    """🔴 `--help` is the only documentation most callers read, and it said less than the body.

    The body's contract is that the ordinal is derived ONCE, at the write, and that ordering is
    never read off the spelling — the reason `rev.14` (2026-09-27) is later than `rev.17`
    (2026-08-07). `--revision`'s help line said only "revision label to record (required to
    write)", which is compatible with the opposite design, so a caller reading the help alone
    would compare labels as text. The shipped behaviour was right; the text was not.
    """

    def help_for(self, option: str) -> str:
        """The REAL `--help`, through the real entry point: a help string asserted from the
        parser object could pass while the shipped CLI printed something else."""
        done = subprocess.run([sys.executable, str(HERE / "reseal_dismech_baseline.py"),
                               "--help"], capture_output=True, text=True,
                              env={**os.environ, "COLUMNS": "100"})
        self.assertEqual(done.returncode, 0, done.stdout + done.stderr)
        # `rindex`: the flag appears first in the wrapped usage line, where no help text lives.
        start = done.stdout.rindex(option)
        return done.stdout[start:start + 700]

    def test_revision_help_names_the_derivation_and_the_monotonicity(self) -> None:
        text = self.help_for("--revision REVISION")
        for phrase in ("ONCE", "revision_ordinal", "exceed", "spelling"):
            self.assertIn(phrase, text, f"--revision help does not state {phrase!r}")

    def test_revision_help_carries_the_counterexample_that_makes_it_concrete(self) -> None:
        text = self.help_for("--revision REVISION")
        self.assertIn("rev.14", text)
        self.assertIn("rev.17", text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
