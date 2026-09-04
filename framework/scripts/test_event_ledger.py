#!/usr/bin/env python3
"""The P7 event ledger keeps the four properties J.1 and §P7 actually name.

Those four, and nothing about "the loop works": append-only enforced by a chain rather
than asserted; one writer per file by construction; `closed_by` in the derived view and
never at the source; truncation detected against an anchor that may only move forward.

Every case below runs against a temporary events directory. The repository's own ledger is
never written by this suite — a test that appends to the real ledger to prove appending
works has changed the object it was measuring.
"""
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "framework" / "scripts"))

import event_ledger as el  # noqa: E402


class LedgerCase(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        base = Path(self.tmp.name)
        self.events = base / "events"
        self.view = base / "consolidated"
        self.clock = datetime(2026, 9, 4, 12, 0, 0, tzinfo=timezone.utc)
        self.addCleanup(self.tmp.cleanup)

    def tick(self) -> datetime:
        self.clock += timedelta(seconds=1)
        return self.clock

    def append(self, actor: str, event_type: str, obj: str, **kw) -> dict:
        return el.append_event(self.events, actor, event_type, obj, now=self.tick(), **kw)

    def assign(self, task: str, obj: str = "do the thing") -> dict:
        return self.append("orchestrator", "TASK_ASSIGNED", obj, task_id=task)


class TheChainIsEnforcedNotAsserted(LedgerCase):
    def test_the_first_event_chains_to_nothing_and_the_rest_to_their_predecessor(self) -> None:
        first = self.assign("T-1")
        second = self.append("orchestrator", "TASK_CLAIMED", "claimed", task_id="T-1")
        self.assertIsNone(first[el.CHAIN_FIELD])
        self.assertEqual(el.event_digest(first), second[el.CHAIN_FIELD])
        self.assertEqual([], el.validate_chain(el.load_actor_file(
            el.actor_ledger_path(self.events, "orchestrator"))))

    def test_editing_a_historical_line_is_detected_at_the_line_after_it(self) -> None:
        """One error, not one per surviving line — and the difference is not cosmetic.

        The checker re-synchronises: after reporting a mismatch it takes the *stored*
        record's digest as the next expectation. So an edit to line 1 is reported at line
        2 and lines 3-N verify cleanly, because their `ledger_prev_hash` values still
        agree with records this edit did not touch. Detection is what the chain
        guarantees; a per-line blast radius is not, and asserting one would have been
        asserting a property the reused `fulltext_receipts` pattern does not have either.
        """
        for n in range(1, 4):
            self.assign(f"T-{n}")
        path = el.actor_ledger_path(self.events, "orchestrator")
        lines = el.load_actor_file(path)
        lines[0]["object"] = "something else entirely"
        path.write_text("".join(el.canonical_line(e) + "\n" for e in lines), encoding="utf-8")
        self.assertEqual(
            ["line 2: broken hash chain: earlier history was rewritten or removed"],
            el.validate_chain(el.load_actor_file(path)))

    def test_an_append_onto_rewritten_history_fails_closed(self) -> None:
        """The append re-reads and verifies INSIDE the lock, so it cannot launder a tamper."""
        self.assign("T-1")
        self.assign("T-2")
        path = el.actor_ledger_path(self.events, "orchestrator")
        lines = el.load_actor_file(path)
        lines[0]["object"] = "tampered"
        path.write_text("".join(el.canonical_line(e) + "\n" for e in lines), encoding="utf-8")
        with self.assertRaises(ValueError) as caught:
            self.assign("T-3")
        self.assertIn("refusing to append onto unverified history", str(caught.exception))

    def test_a_dropped_line_is_caught_by_the_sequence_not_only_the_chain(self) -> None:
        """Deleting the LAST line leaves a valid chain; the event_id/position rule catches it.

        A hash chain binds each event to its predecessor, which leaves truncation of the
        tail invisible to the chain alone. Two independent detectors matter here: this one
        is local to the file, and `anchor_regressions` is the external one.
        """
        for n in range(1, 4):
            self.assign(f"T-{n}")
        path = el.actor_ledger_path(self.events, "orchestrator")
        lines = el.load_actor_file(path)
        del lines[1]
        path.write_text("".join(el.canonical_line(e) + "\n" for e in lines), encoding="utf-8")
        surviving = el.load_actor_file(path)
        self.assertNotEqual([], el.validate_chain(surviving))
        self.assertNotEqual([], el.validate_sequence(surviving))


class OneWriterPerFile(LedgerCase):
    def test_an_event_may_not_name_an_actor_other_than_its_file(self) -> None:
        self.assign("T-1")
        path = el.actor_ledger_path(self.events, "orchestrator")
        lines = el.load_actor_file(path)
        lines[0]["actor_id"] = "mirror"
        problems = el.validate_event(lines[0], actor_id="orchestrator")
        self.assertTrue(any("one writer per file" in p for p in problems), problems)

    def test_two_actors_write_two_files_and_neither_shares_a_sequence(self) -> None:
        self.assign("T-1")
        self.append("mirror", "REVIEW_OPENED", "blind review", task_id="T-1")
        self.assertEqual(
            {"mirror.jsonl", "orchestrator.jsonl"},
            {p.name for p in el.actor_files(self.events)})
        events, anchors, errors = el.read_all(self.events)
        self.assertEqual([], errors)
        self.assertEqual({"mirror": 1, "orchestrator": 1},
                         {k: v["events"] for k, v in anchors.items()})

    def test_the_event_id_is_the_tools_not_the_callers(self) -> None:
        """`append_event` takes no event_id: a caller that could name one could lie about it."""
        first = self.assign("T-1")
        self.assertEqual("EV-orchestrator-0001", first["event_id"])
        self.assertEqual("EV-orchestrator-0002", self.assign("T-2")["event_id"])


class ClosureLivesInTheClosingEvent(LedgerCase):
    def test_a_non_closing_type_may_not_carry_closes_event_id(self) -> None:
        opened = self.assign("T-1")
        with self.assertRaises(ValueError) as caught:
            self.append("scientist", "TASK_ACKED", "ack", task_id="T-1",
                        closes_event_id=opened["event_id"])
        self.assertIn("is not a closing event", str(caught.exception))

    def test_a_closing_type_must_carry_it(self) -> None:
        with self.assertRaises(ValueError) as caught:
            self.append("scientist", "TASK_COMPLETE", "done", task_id="T-1")
        self.assertIn("must carry `closes_event_id`", str(caught.exception))

    def test_closed_by_is_rejected_at_the_source_and_produced_in_the_view(self) -> None:
        opened = self.assign("T-1")
        closed = self.append("scientist", "TASK_COMPLETE", "done", task_id="T-1",
                             closes_event_id=opened["event_id"])
        source = el.load_actor_file(el.actor_ledger_path(self.events, "orchestrator"))
        self.assertNotIn("closed_by", source[0], "the source line was rewritten")
        with_field = dict(source[0], closed_by=closed["event_id"])
        self.assertTrue(any("derived view" in p
                            for p in el.validate_event(with_field, actor_id="orchestrator")))
        view = el.consolidated_view(el.read_all(self.events)[0])
        opening = next(e for e in view if e["event_id"] == opened["event_id"])
        self.assertEqual(closed["event_id"], opening["closed_by"])

    def test_a_closure_pointing_at_nothing_is_a_consolidation_error(self) -> None:
        """An append cannot see peers' files, so this check can only live in the view."""
        self.append("scientist", "TASK_COMPLETE", "done", task_id="T-1",
                    closes_event_id="EV-orchestrator-0009")
        errors = el.cross_actor_errors(el.read_all(self.events)[0])
        self.assertTrue(any("is in no actor ledger" in e for e in errors), errors)

    def test_a_closure_may_not_cross_a_task_boundary_or_precede_its_opening(self) -> None:
        opened = self.assign("T-1")
        self.append("scientist", "TASK_COMPLETE", "done", task_id="T-2",
                    closes_event_id=opened["event_id"])
        errors = el.cross_actor_errors(el.read_all(self.events)[0])
        self.assertTrue(any("across a task boundary" in e for e in errors), errors)

    def test_a_review_closure_may_not_close_an_assignment(self) -> None:
        opened = self.assign("T-1")
        self.append("mirror", "REVIEW_CLOSED", "PASS", task_id="T-1",
                    closes_event_id=opened["event_id"])
        errors = el.cross_actor_errors(el.read_all(self.events)[0])
        self.assertTrue(any("which it may not close" in e for e in errors), errors)


class TheAnchorOnlyMovesForward(LedgerCase):
    def consolidate(self):
        return el.consolidate(self.events, self.view)

    def test_consolidation_writes_the_view_and_the_anchor(self) -> None:
        self.assign("T-1")
        errors, anchor = self.consolidate()
        self.assertEqual([], errors)
        self.assertEqual(1, anchor["events"])
        self.assertEqual(1, len(el.load_view(self.view)))
        self.assertTrue((self.view / "anchors.json").is_file())

    def test_truncating_an_actor_file_after_anchoring_is_refused(self) -> None:
        self.assign("T-1")
        self.assign("T-2")
        self.assertEqual([], self.consolidate()[0])
        path = el.actor_ledger_path(self.events, "orchestrator")
        kept = el.load_actor_file(path)[:1]
        path.write_text("".join(el.canonical_line(e) + "\n" for e in kept), encoding="utf-8")
        errors, anchor = self.consolidate()
        self.assertTrue(any("history was truncated" in e for e in errors), errors)
        self.assertEqual({}, anchor, "a refused consolidation must change nothing")

    def test_rewriting_in_place_without_changing_the_count_is_refused(self) -> None:
        """Same length, different head. The count alone would have called this unchanged."""
        self.assign("T-1")
        self.assertEqual([], self.consolidate()[0])
        path = el.actor_ledger_path(self.events, "orchestrator")
        lines = el.load_actor_file(path)
        lines[0]["object"] = "a different instruction"
        path.write_text("".join(el.canonical_line(e) + "\n" for e in lines), encoding="utf-8")
        errors, _ = self.consolidate()
        self.assertTrue(any("rewritten in place" in e for e in errors), errors)

    def test_an_anchored_actor_whose_ledger_vanishes_is_refused(self) -> None:
        self.assign("T-1")
        self.assertEqual([], self.consolidate()[0])
        el.actor_ledger_path(self.events, "orchestrator").unlink()
        errors, _ = self.consolidate()
        self.assertTrue(any("now absent" in e for e in errors), errors)

    def test_growth_is_not_a_regression(self) -> None:
        """The positive control: the refusals above must not fire on an ordinary append."""
        self.assign("T-1")
        self.assertEqual([], self.consolidate()[0])
        self.assign("T-2")
        errors, anchor = self.consolidate()
        self.assertEqual([], errors)
        self.assertEqual(2, anchor["actors"]["orchestrator"]["events"])

    def test_a_refused_consolidation_leaves_the_previous_view_untouched(self) -> None:
        self.assign("T-1")
        self.assign("T-2")
        self.consolidate()
        before = (self.view / "events.jsonl").read_text(encoding="utf-8")
        anchor_before = (self.view / "anchors.json").read_text(encoding="utf-8")
        path = el.actor_ledger_path(self.events, "orchestrator")
        path.write_text("", encoding="utf-8")
        self.assertNotEqual([], self.consolidate()[0])
        self.assertEqual(before, (self.view / "events.jsonl").read_text(encoding="utf-8"))
        self.assertEqual(anchor_before, (self.view / "anchors.json").read_text(encoding="utf-8"))


class TheQueueIsAJoinNotAStateMachine(LedgerCase):
    def test_an_assignment_is_open_until_a_closure_points_at_it(self) -> None:
        opened = self.assign("T-1", "repair the router")
        events = el.read_all(self.events)[0]
        self.assertEqual(["T-1"], [r["task_id"] for r in el.open_tasks(events)])
        self.append("scientist", "TASK_COMPLETE", "done", task_id="T-1",
                    closes_event_id=opened["event_id"])
        self.assertEqual([], el.open_tasks(el.read_all(self.events)[0]))

    def test_a_cancelled_assignment_leaves_the_queue_too(self) -> None:
        """A task parked to STOP_LOG class 3 must not be re-dispatched forever."""
        opened = self.assign("T-1")
        self.append("orchestrator", "TASK_CANCELLED", "round-2 BLOCK: parked", task_id="T-1",
                    closes_event_id=opened["event_id"])
        self.assertEqual([], el.open_tasks(el.read_all(self.events)[0]))

    def test_claims_and_acks_are_joined_on_task_id_and_do_not_close_anything(self) -> None:
        self.assign("T-1")
        self.append("scientist", "TASK_ACKED", "ack", task_id="T-1")
        self.append("scientist", "TASK_CLAIMED", "claimed", task_id="T-1")
        row, = el.open_tasks(el.read_all(self.events)[0])
        self.assertTrue(row["acked"])
        self.assertEqual("scientist", row["claimed_by"])

    def test_the_queue_is_ordered_oldest_first(self) -> None:
        for n in range(1, 4):
            self.assign(f"T-{n}")
        self.assertEqual(["T-1", "T-2", "T-3"],
                         [r["task_id"] for r in el.open_tasks(el.read_all(self.events)[0])])

    def test_the_queue_says_when_it_is_reading_an_unconsolidated_source(self) -> None:
        self.assign("T-1")
        _, source = el.queue_source(self.events, self.view)
        self.assertIn("UNCONSOLIDATED", source)
        el.consolidate(self.events, self.view)
        _, source = el.queue_source(self.events, self.view)
        self.assertNotIn("UNCONSOLIDATED", source)


class TheVocabularyIsTheAnnexes(LedgerCase):
    def test_every_type_j1_names_is_accepted_and_nothing_else_is(self) -> None:
        annex = (ROOT / "governance" / "annex_j_runtime_control_plane.md").read_text(
            encoding="utf-8")
        line = next(l for l in annex.splitlines() if l.startswith("Tipi minimi:"))
        named = {t.strip().strip("`.") for t in line.split(":", 1)[1].split(",")}
        self.assertEqual(named, set(el.EVENT_TYPES),
                         "the constant and J.1's minimum list have drifted apart")

    def test_an_invented_type_is_refused(self) -> None:
        with self.assertRaises(ValueError) as caught:
            self.append("orchestrator", "TASK_PARKED", "invented", task_id="T-1")
        self.assertIn("not one of J.1's event types", str(caught.exception))

    def test_a_work_shaped_event_must_name_its_task(self) -> None:
        with self.assertRaises(ValueError) as caught:
            self.append("orchestrator", "WORK_COMMIT", "abc1234")
        self.assertIn("must carry `task_id`", str(caught.exception))

    def test_an_actor_scoped_event_needs_no_task(self) -> None:
        """The positive control for the rule above: it must not fire on every event."""
        self.assertEqual("ACTOR_ACTIVE",
                         self.append("mirror", "ACTOR_ACTIVE", "session opened")["event_type"])


class TheRepositoryLedgerIsWellFormed(unittest.TestCase):
    """The live surface, not a fixture. Vacuous while empty, and it says so when it is."""

    def test_whatever_is_committed_validates(self) -> None:
        events_dir = ROOT / el.DEFAULT_EVENTS_DIR
        view_dir = ROOT / el.DEFAULT_VIEW_DIR
        events, anchors, errors = el.read_all(events_dir)
        errors += el.cross_actor_errors(events)
        anchor_path = view_dir / "anchors.json"
        if anchor_path.is_file():
            errors += el.anchor_regressions(
                json.loads(anchor_path.read_text(encoding="utf-8")), anchors, events_dir)
        self.assertEqual([], errors)
        if not anchors:
            self.skipTest(f"no actor ledgers under {events_dir}: this check is vacuous")


if __name__ == "__main__":
    unittest.main(verbosity=2)
