#!/usr/bin/env python3
"""Regression suite for the SYNC_EPOCH ledger.

The point of this ledger is that a decision about the shared checkout — including the
decision NOT to move it — outlives the session that made it. So the tests pin the two
things that make a record trustworthy rather than merely present: that the chain refuses a
rewritten past, and that a measurement keeps the name of whoever actually took it.
"""
from __future__ import annotations

import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

SPEC = importlib.util.spec_from_file_location(
    "sync_epochs", Path(__file__).with_name("sync_epochs.py"))
assert SPEC and SPEC.loader
epochs = importlib.util.module_from_spec(SPEC)
sys.modules["sync_epochs"] = epochs
SPEC.loader.exec_module(epochs)

ANCHOR_BLOCK = (
    "# manifest\n\n```yaml\n"
    "sync_epoch_ledger_path: framework/state/sync_epochs.jsonl\n"
    "sync_epoch_ledger_events: 0\n"
    "sync_epoch_ledger_head: null\n"
    "```\n"
)


def event(**overrides) -> dict:
    record = {
        "schema_version": 1,
        "event_id": "SYNC-20260811-001",
        "recorded_at": "2026-08-11",
        "record_kind": "contemporaneous",
        "workspace": "/repo",
        "action": "NO_MOVE",
        "previous_commit": "a" * 40,
        "current_commit": "a" * 40,
        "branch_or_detached": "DETACHED",
        "reason": "merge_dependency",
        "dependency_commit": "none",
        "landed_artifacts": [],
        "actors_required_to_consume": [],
        "invalidates_active_work": False,
        "required_action_by_readers": "none",
        "validation_status": "LINT PASS",
        "announced_by": "Plan",
        "observations": [{
            "measured_by": "Plan", "measured_at": "2026-08-11", "workspace": "/repo",
            "branch_or_detached": "main", "commit": "a" * 40,
            "measurement": "git worktree list", "result": "detached at a…",
        }],
    }
    record.update(overrides)
    return record


class EventValidation(unittest.TestCase):
    def test_a_wellformed_event_passes(self) -> None:
        self.assertEqual(epochs.validate_event(event()), [])

    def test_a_move_that_changes_nothing_is_not_a_move(self) -> None:
        """🔴 The invariant that makes the two actions mean different things. A record saying
        MOVE while naming one commit twice is not a typo — it is a claim nobody can check."""
        errors = epochs.validate_event(event(action="MOVE"))
        self.assertTrue(any("is not a move" in item for item in errors), errors)

    def test_a_no_move_across_two_commits_is_refused(self) -> None:
        errors = epochs.validate_event(event(current_commit="b" * 40))
        self.assertTrue(any("recorded as unmoved" in item for item in errors), errors)

    def test_an_unattributed_observation_is_refused(self) -> None:
        """🔴 The separation this ledger exists for. An observation with no `measured_by`
        silently becomes Plan's, which is how a borrowed number turns into a declared one."""
        broken = event()
        del broken["observations"][0]["measured_by"]
        errors = epochs.validate_event(broken)
        self.assertTrue(any("observations[0].measured_by" in item for item in errors), errors)

    def test_every_observation_field_is_required(self) -> None:
        for field in epochs.OBSERVATION_FIELDS:
            with self.subTest(field=field):
                broken = copy.deepcopy(event())
                broken["observations"][0][field] = "  "
                errors = epochs.validate_event(broken)
                self.assertTrue(any(f"observations[0].{field}" in item for item in errors))

    def test_an_empty_consumer_list_is_allowed_but_must_be_present(self) -> None:
        """An absent list and an empty list are the same JSON to a reader and completely
        different facts: "nobody must consume this" is a decision, a missing field is not."""
        self.assertEqual(epochs.validate_event(event(actors_required_to_consume=[])), [])
        broken = event()
        del broken["actors_required_to_consume"]
        self.assertIn("missing required field: actors_required_to_consume",
                      epochs.validate_event(broken))

    def test_other_declared_needs_a_reason(self) -> None:
        errors = epochs.validate_event(event(reason="other_declared"))
        self.assertTrue(any("reason_detail" in item for item in errors), errors)
        self.assertEqual(
            epochs.validate_event(event(reason="other_declared",
                                        reason_detail="the shared checkout already carries it")),
            [])

    def test_a_reconstruction_must_declare_its_time_precision(self) -> None:
        errors = epochs.validate_event(event(record_kind="contemporaneous_reconstruction"))
        self.assertTrue(any("time_precision" in item for item in errors), errors)
        self.assertEqual(
            epochs.validate_event(event(record_kind="contemporaneous_reconstruction",
                                        time_precision="unknown")),
            [])

    def test_invalid_enums_are_refused(self) -> None:
        for field, value in (("action", "MAYBE"), ("reason", "felt_like_it"),
                             ("record_kind", "guess")):
            with self.subTest(field=field):
                self.assertTrue(epochs.validate_event(event(**{field: value})))

    def test_a_hedge_is_not_a_boolean(self) -> None:
        errors = epochs.validate_event(event(invalidates_active_work="probably not"))
        self.assertTrue(any("never a prose hedge" in item for item in errors), errors)


class TheLedgerIsAppendOnly(unittest.TestCase):
    def workspace(self) -> Path:
        temp = TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        (root / "framework" / "state").mkdir(parents=True)
        epochs.default_manifest(root).write_text(ANCHOR_BLOCK, encoding="utf-8")
        return root

    def test_recording_chains_and_reanchors(self) -> None:
        root = self.workspace()
        epochs.append_event(event(), ledger=epochs.default_ledger(root),
                            manifest=epochs.default_manifest(root))
        self.assertEqual(epochs.verify(root), [])
        text = epochs.default_manifest(root).read_text(encoding="utf-8")
        self.assertIn("sync_epoch_ledger_events: 1", text)

    def test_a_second_event_links_to_the_first(self) -> None:
        root = self.workspace()
        ledger, manifest = epochs.default_ledger(root), epochs.default_manifest(root)
        first = epochs.append_event(event(), ledger=ledger, manifest=manifest)
        second = epochs.append_event(
            event(event_id="SYNC-20260811-002", action="MOVE",
                  current_commit="b" * 40, reason="batch_commit_open"),
            ledger=ledger, manifest=manifest)
        self.assertIsNone(first[epochs.chain.CHAIN_FIELD])
        self.assertEqual(second[epochs.chain.CHAIN_FIELD],
                         epochs.chain.receipt_digest(first))
        self.assertEqual(epochs.verify(root), [])

    def test_a_rewritten_past_breaks_the_chain(self) -> None:
        root = self.workspace()
        ledger, manifest = epochs.default_ledger(root), epochs.default_manifest(root)
        epochs.append_event(event(), ledger=ledger, manifest=manifest)
        epochs.append_event(event(event_id="SYNC-20260811-002"),
                            ledger=ledger, manifest=manifest)
        lines = ledger.read_text(encoding="utf-8").splitlines()
        first = json.loads(lines[0])
        first["reason"] = "urgent_gate"
        lines[0] = json.dumps(first, ensure_ascii=False, sort_keys=True)
        ledger.write_text("\n".join(lines) + "\n", encoding="utf-8")
        with self.assertRaises(ValueError) as caught:
            epochs.load_ledger(ledger)
        self.assertIn("broken hash chain", str(caught.exception))

    def test_a_truncated_tail_is_caught_by_the_anchor_and_not_the_chain(self) -> None:
        """🔴 The reason an external anchor exists at all: lopping the last events off leaves
        a perfectly self-consistent prefix, so only a count held elsewhere can see it."""
        root = self.workspace()
        ledger, manifest = epochs.default_ledger(root), epochs.default_manifest(root)
        epochs.append_event(event(), ledger=ledger, manifest=manifest)
        epochs.append_event(event(event_id="SYNC-20260811-002"),
                            ledger=ledger, manifest=manifest)
        lines = ledger.read_text(encoding="utf-8").splitlines()
        ledger.write_text(lines[0] + "\n", encoding="utf-8")
        self.assertEqual(epochs.chain.validate_ledger_chain(epochs.load_ledger(ledger)), [])
        problems = epochs.verify(root)
        self.assertTrue(any("truncated" in item for item in problems), problems)

    def test_a_duplicate_event_id_is_refused(self) -> None:
        root = self.workspace()
        ledger, manifest = epochs.default_ledger(root), epochs.default_manifest(root)
        epochs.append_event(event(), ledger=ledger, manifest=manifest)
        with self.assertRaises(ValueError) as caught:
            epochs.append_event(event(), ledger=ledger, manifest=manifest)
        self.assertIn("already recorded", str(caught.exception))

    def test_an_invalid_event_is_refused_before_anything_is_written(self) -> None:
        root = self.workspace()
        ledger, manifest = epochs.default_ledger(root), epochs.default_manifest(root)
        with self.assertRaises(ValueError):
            epochs.append_event(event(action="MOVE"), ledger=ledger, manifest=manifest)
        self.assertFalse(ledger.exists())

    def test_a_manifest_without_the_anchor_pair_refuses_the_append(self) -> None:
        """🔴 And the refusal must leave NOTHING behind.

        The first version of this test asserted only that a `ValueError` was raised — and it
        passed while the writer appended the event and then failed to anchor it, leaving the
        ledger in the exact state this module's own LINT check calls `BLOCK_SYSTEM`. The
        error message even said so: *"the ledger was appended but could not be anchored"*.
        **A test for a refusal has to assert what was not written**, or it certifies the
        exception and ignores the damage behind it.
        """
        root = self.workspace()
        epochs.default_manifest(root).write_text("# no anchor here\n", encoding="utf-8")
        with self.assertRaises(ValueError) as caught:
            epochs.append_event(event(), ledger=epochs.default_ledger(root),
                                manifest=epochs.default_manifest(root))
        self.assertIn("refusing to append", str(caught.exception))
        self.assertFalse(epochs.default_ledger(root).exists(),
                         "the event was written despite the refusal")

    def test_a_refusal_never_extends_an_existing_ledger(self) -> None:
        """The same property with history already present: a rejected append must leave the
        prior ledger byte-identical, not merely 'not much longer'."""
        root = self.workspace()
        ledger, manifest = epochs.default_ledger(root), epochs.default_manifest(root)
        epochs.append_event(event(), ledger=ledger, manifest=manifest)
        before = ledger.read_bytes()
        manifest.write_text("# anchor removed by someone else\n", encoding="utf-8")
        with self.assertRaises(ValueError):
            epochs.append_event(event(event_id="SYNC-20260811-002"),
                                ledger=ledger, manifest=manifest)
        self.assertEqual(ledger.read_bytes(), before)


class TheWriterTouchesNothingElse(unittest.TestCase):
    def test_it_writes_only_the_ledger_and_the_anchor(self) -> None:
        """It records who moved a checkout. It must never be able to move one, or to touch a
        scientific file — so the property is pinned on the source, not promised in prose."""
        source = Path(__file__).with_name("sync_epochs.py").read_text(encoding="utf-8")
        for forbidden in ("checkout", "git ", "subprocess", "branch -f", "reset"):
            with self.subTest(forbidden=forbidden):
                self.assertNotIn(f"{forbidden}(", source)
        self.assertNotIn("import subprocess", source)


class TheLintActuallyBites(unittest.TestCase):
    """🔴 A contract enforced only by a reporting tool is documentation.

    Traced to the component that can emit the blocking verdict, and verified adversarially:
    the damage the contract describes must really change the finding set. A check wired in
    and never seen to fail is the shape this repository found four times on 2026-08-11.
    """

    def _lint(self):
        spec = importlib.util.spec_from_file_location(
            "legend_lint", Path(__file__).with_name("legend_lint.py"))
        module = importlib.util.module_from_spec(spec)
        sys.modules["legend_lint"] = module
        spec.loader.exec_module(module)
        return module

    def _root(self) -> Path:
        temp = TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        (root / "framework" / "state").mkdir(parents=True)
        epochs.default_manifest(root).write_text(ANCHOR_BLOCK, encoding="utf-8")
        return root

    def test_a_healthy_ledger_raises_nothing(self) -> None:
        root = self._root()
        epochs.append_event(event(), ledger=epochs.default_ledger(root),
                            manifest=epochs.default_manifest(root))
        findings = []
        self._lint()._check_sync_epochs(findings, str(root))
        self.assertEqual(findings, [])

    def test_a_truncated_ledger_blocks_the_system(self) -> None:
        root = self._root()
        ledger, manifest = epochs.default_ledger(root), epochs.default_manifest(root)
        epochs.append_event(event(), ledger=ledger, manifest=manifest)
        epochs.append_event(event(event_id="SYNC-20260811-002"),
                            ledger=ledger, manifest=manifest)
        ledger.write_text(ledger.read_text(encoding="utf-8").splitlines()[0] + "\n",
                          encoding="utf-8")
        findings = []
        self._lint()._check_sync_epochs(findings, str(root))
        self.assertTrue(findings)
        self.assertEqual({item.severity for item in findings}, {"BLOCK_SYSTEM"})
        self.assertEqual({item.code for item in findings}, {"SYNC_EPOCH_LEDGER_UNTRUSTED"})

    def test_a_repository_with_no_ledger_is_unaffected(self) -> None:
        """An empty state is legitimate: a checkout never realigned has nothing to record,
        and a floor invented here would make that look like damage."""
        temp = TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        findings = []
        self._lint()._check_sync_epochs(findings, temp.name)
        self.assertEqual(findings, [])


class TheCommittedLedgerHolds(unittest.TestCase):
    def test_the_repository_ledger_verifies(self) -> None:
        root = Path(__file__).resolve().parents[2]
        if not epochs.default_ledger(root).exists():
            self.skipTest("no sync epoch ledger in this checkout")
        self.assertEqual(epochs.verify(root), [])


if __name__ == "__main__":
    sys.exit(0 if unittest.main(exit=False, verbosity=2).result.wasSuccessful() else 1)
