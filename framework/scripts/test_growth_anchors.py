#!/usr/bin/env python3
"""Regression suite for the self-anchoring growth constraints.

The property under test is not "the tool runs". It is the one the growth principle demands:
**updating a constraint must cost at least as much as complying with it.** Every test below
tries to move an anchor *without* having done the corresponding work, and asserts that the
attempt is refused. A suite that only checked the happy path would pass against a recorder
that anchors anything it is told.
"""
from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

sys.path.insert(0, str(Path(__file__).resolve().parent))
import growth_anchors as ga  # noqa: E402


MANIFEST = """# state

## 6.2 GROWTH ANCHORS

```yaml
growth_anchor_events: 0
growth_anchor_head: null
```

```yaml
registry_only_fulltext_declarations_baseline: 2
registry_only_fulltext_declaration_ids: ["PAPER 001", "PAPER 002"]
unread_premise_baseline: 2
unread_premise_measured_on: 2026-01-01
```
"""


class Harness:
    """A temp workspace whose measurement is injected, so tests are about policy not parsing."""

    def __init__(self, stack: TemporaryDirectory):
        self.root = Path(stack.name)
        (self.root / "framework/state").mkdir(parents=True)
        (self.root / ga.MANIFEST_REL).write_text(MANIFEST, encoding="utf-8")
        self.live = {
            "structural": {"claims": 10, "papers": 20, "corpus": 30, "literature": 40},
            "registry_only_fulltext": ["PAPER 001", "PAPER 002"],
            "unread_premises": ["111", "222"],
            # Well under the trigger, so the existing policy tests stay about the policy
            # they were written for. The scale tests raise these deliberately.
            "registry_bytes": {"claims": 1_000, "literature": 2_000, "papers": 3_000},
        }
        self._original = ga.measure_all
        ga.measure_all = lambda root, disease: json.loads(json.dumps(self.live))

    def restore(self):
        ga.measure_all = self._original

    def run(self, *argv) -> int:
        return ga.main(["--root", str(self.root), *argv])

    def manifest(self) -> str:
        return (self.root / ga.MANIFEST_REL).read_text(encoding="utf-8")

    def events(self) -> list[dict]:
        return ga.load_ledger(self.root / ga.LEDGER_REL)


class GrowthAnchorTests(unittest.TestCase):
    def setUp(self) -> None:
        self._stack = TemporaryDirectory()
        self.h = Harness(self._stack)
        self.assertEqual(0, self.h.run("record", "--bootstrap", "--batch", "B0"))

    def tearDown(self) -> None:
        self.h.restore()
        self._stack.cleanup()

    # ---------------------------------------------------------------- the central property

    def test_declared_delta_that_does_not_match_the_registries_is_refused(self) -> None:
        """The whole design in one test: you cannot anchor a number you did not earn."""
        self.h.live["structural"]["claims"] = 14          # four claims really were added
        self.assertEqual(1, self.h.run("record", "--batch", "B1", "--claims", "+3"))
        self.assertEqual(1, len(self.h.events()), "a refused record must not append")

    def test_declared_delta_that_matches_is_recorded_and_reanchored(self) -> None:
        self.h.live["structural"]["claims"] = 14
        self.assertEqual(0, self.h.run("record", "--batch", "B1", "--claims", "+4"))
        self.assertEqual(2, len(self.h.events()))
        self.assertEqual(0, self.h.run("check"))

    def test_record_without_any_declaration_is_refused(self) -> None:
        """Silence must not anchor. A recorder that accepts nothing anchors anything."""
        self.h.live["structural"]["claims"] = 14
        self.assertEqual(2, self.h.run("record", "--batch", "B1"))
        self.assertEqual(1, len(self.h.events()))

    def test_record_without_batch_is_refused(self) -> None:
        self.h.live["structural"]["claims"] = 14
        self.assertEqual(2, self.h.run("record", "--claims", "+4"))
        self.assertEqual(1, len(self.h.events()))

    def test_undeclared_growth_blocks_check(self) -> None:
        self.h.live["structural"]["papers"] = 21
        self.assertEqual(1, self.h.run("check"))

    def test_undeclared_shrinkage_also_blocks(self) -> None:
        """Records disappearing is at least as alarming as records appearing."""
        self.h.live["structural"]["papers"] = 19
        self.assertEqual(1, self.h.run("check"))

    # ---------------------------------------------------------------- ratchets

    def test_new_unread_premise_is_a_violation(self) -> None:
        self.h.live["unread_premises"] = ["111", "222", "333"]
        self.assertEqual(1, self.h.run("check"))

    def test_new_registry_only_declaration_is_a_violation(self) -> None:
        self.h.live["registry_only_fulltext"] = ["PAPER 001", "PAPER 002", "PAPER 003"]
        self.assertEqual(1, self.h.run("check"))

    def test_ratchet_swap_at_equal_count_is_still_a_violation(self) -> None:
        """Identity, not cardinality: trading one grandfathered ID for a new one is not free."""
        self.h.live["registry_only_fulltext"] = ["PAPER 001", "PAPER 099"]
        self.assertEqual(1, self.h.run("check"))

    def test_fallen_ratchet_is_reported_then_tightened_without_a_typed_number(self) -> None:
        self.h.live["unread_premises"] = ["111"]
        self.assertEqual(0, self.h.run("check"), "an improvement is not a failure")
        self.assertEqual(0, self.h.run("tighten", "--batch", "B1"))
        self.assertIn("unread_premise_baseline: 1", self.h.manifest())
        self.h.live["unread_premises"] = ["111", "222"]
        self.assertEqual(1, self.h.run("check"), "the ratchet must not be re-loosenable")

    def test_tighten_refuses_to_paper_over_a_violation(self) -> None:
        self.h.live["unread_premises"] = ["111", "999"]
        self.assertEqual(1, self.h.run("tighten", "--batch", "B1"))
        self.assertEqual(1, len(self.h.events()))

    def test_structural_record_cannot_launder_a_worsening_ratchet(self) -> None:
        """A batch must not smuggle a ratchet regression through an honest counts record."""
        self.h.live["structural"]["claims"] = 11
        self.h.live["unread_premises"] = ["111", "222", "333"]
        self.assertEqual(1, self.h.run("record", "--batch", "B1", "--claims", "+1"))
        self.assertEqual(1, len(self.h.events()))

    def test_there_is_no_command_that_loosens_a_ratchet(self) -> None:
        self.assertNotIn("loosen", ga.COMMANDS)
        self.assertNotIn("reset", ga.COMMANDS)

    # ---------------------------------------------------------------- ledger integrity

    def test_tampered_event_breaks_the_chain(self) -> None:
        path = self.h.root / ga.LEDGER_REL
        events = self.h.events()
        events[0]["anchors"]["structural"]["claims"] = 999
        path.write_text("\n".join(ga.canonical_line(e) for e in events) + "\n",
                        encoding="utf-8")
        self.h.live["structural"]["claims"] = 999
        self.assertEqual(1, self.h.run("check"),
                         "editing history to match a lie must not produce a pass")

    def test_truncated_tail_is_caught_by_the_manifest_anchor(self) -> None:
        self.h.live["structural"]["claims"] = 11
        self.assertEqual(0, self.h.run("record", "--batch", "B1", "--claims", "+1"))
        path = self.h.root / ga.LEDGER_REL
        lines = path.read_text(encoding="utf-8").splitlines()
        path.write_text("\n".join(lines[:-1]) + "\n", encoding="utf-8")
        self.assertEqual(1, self.h.run("verify"))

    def test_verify_passes_on_an_intact_ledger(self) -> None:
        self.assertEqual(0, self.h.run("verify"))

    def test_append_refuses_on_a_broken_chain(self) -> None:
        path = self.h.root / ga.LEDGER_REL
        events = self.h.events()
        events[0][ga.CHAIN_FIELD] = "deadbeef"
        path.write_text(ga.canonical_line(events[0]) + "\n", encoding="utf-8")
        self.h.live["structural"]["claims"] = 11
        # The property is "refused and nothing appended", not a particular exit code:
        # asserting the number would make the test brittle about something it does not govern.
        self.assertNotEqual(0, self.h.run("record", "--batch", "B1", "--claims", "+1"))
        self.assertEqual(1, len(self.h.events()))

    def test_double_bootstrap_is_refused(self) -> None:
        self.assertEqual(2, self.h.run("record", "--bootstrap", "--batch", "B1"))


class ScaleTriggerTests(unittest.TestCase):
    """The third policy: nothing is wrong, something is due.

    A registry can be perfectly anchored and still have outgrown the shape it is. These
    tests are about the one property that makes such a signal survive: it must not be
    silenceable more cheaply than it is satisfiable.
    """

    def setUp(self) -> None:
        self._stack = TemporaryDirectory()
        self.h = Harness(self._stack)
        self.assertEqual(0, self.h.run("record", "--bootstrap", "--batch", "B0"))

    def tearDown(self) -> None:
        self.h.restore()
        self._stack.cleanup()

    def over(self, size: int | None = None) -> None:
        self.h.live["registry_bytes"]["literature"] = size or (
            ga.REGISTRY_SIZE_TRIGGER_BYTES + 1)

    def grow(self, claims: int = 2) -> int:
        self.h.live["structural"]["claims"] += claims
        return self.h.run("record", "--batch", "B1", "--claims", f"+{claims}")

    def test_a_registry_under_the_trigger_says_nothing(self) -> None:
        self.assertEqual([], ga.scale_triggers(self.h.live, {}))

    def test_crossing_the_trigger_is_reported_but_does_not_fail_check(self) -> None:
        """It must not block a suite: an architectural question is not a broken anchor."""
        self.over()
        self.assertEqual(0, self.h.run("check"))
        self.assertTrue(ga.scale_triggers(self.h.live, {}))

    def test_a_batch_may_not_anchor_further_growth_while_the_decision_is_outstanding(self):
        """Where it bites, and the reason it is not merely advisory."""
        self.over()
        self.assertEqual(1, self.grow())

    def test_acknowledging_without_reasoning_is_refused(self) -> None:
        self.over()
        self.assertEqual(2, self.h.run("acknowledge-scale", "--batch", "B1"))

    def test_acknowledging_unblocks_the_batch_and_quiets_the_report(self) -> None:
        self.over()
        self.assertEqual(0, self.h.run("acknowledge-scale", "--batch", "B1", "--note",
                                       "deferred: sharding blocked on the wikilink resolver"))
        self.assertEqual([], ga.scale_triggers(self.h.live, ga.tail_state(self.h.events())))
        self.assertEqual(0, self.grow())

    def test_an_acknowledgement_expires_once_the_file_grows_past_the_margin(self) -> None:
        """Without this, `deferred` becomes permanent and the trigger is decoration."""
        self.over()
        self.h.run("acknowledge-scale", "--batch", "B1", "--note", "deferred once")
        state = ga.tail_state(self.h.events())
        acknowledged = self.h.live["registry_bytes"]["literature"]
        self.h.live["registry_bytes"]["literature"] = int(
            acknowledged * (1 + ga.SCALE_ACK_MARGIN)) + 1
        triggers = ga.scale_triggers(self.h.live, state)
        self.assertTrue(triggers)
        self.assertIn("expired", triggers[0])
        self.assertEqual(1, self.grow(), "an expired deferral must block again")

    def test_a_registry_cannot_be_acknowledged_before_it_crosses_the_trigger(self) -> None:
        """A pre-emptive acknowledgement would be silence bought before the question."""
        self.assertEqual(0, self.h.run("acknowledge-scale", "--batch", "B1", "--note", "early"))
        self.assertEqual({}, (ga.tail_state(self.h.events()) or {}).get("scale_ack", {}))

    def test_acknowledgement_survives_a_later_ordinary_batch(self) -> None:
        """A `record` event must not drop the acknowledgement it did not touch."""
        self.over()
        self.h.run("acknowledge-scale", "--batch", "B1", "--note", "deferred")
        self.assertEqual(0, self.grow())
        state = ga.tail_state(self.h.events())
        self.assertIn("literature", state.get("scale_ack", {}))


class MeasurementIsSingleSourced(unittest.TestCase):
    """The counting patterns must stay one definition, because two definitions drift."""

    def test_literature_pattern_matches_non_numeric_identifiers(self) -> None:
        found = ga.HEADINGS["literature"].findall("## LIT-0001\n## LIT-EX-002\n")
        self.assertEqual(["LIT-0001", "LIT-EX-002"], found,
                         "a first draft missed the LIT-EX records and would have "
                         "re-anchored the count six lower than the check it replaced")

    def test_corpus_pattern_matches_both_placeholder_spellings(self) -> None:
        found = ga.HEADINGS["corpus"].findall("## CORPUS P295\n## CORPUS-STUB-119\n")
        self.assertEqual(["CORPUS P295", "CORPUS-STUB-119"], found)

    def test_headings_do_not_match_prose_mentioning_a_record(self) -> None:
        for pattern in ga.HEADINGS.values():
            self.assertEqual([], pattern.findall("see ## CLAIM 005 in passing\n"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
