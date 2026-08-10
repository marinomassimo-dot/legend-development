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
        # Every ratchet the module declares must be present in an injected measurement, or
        # `evaluate` raises instead of judging. Derived from `RATCHET_KEYS` rather than listed,
        # so the next ratchet added does not break ten unrelated policy tests and tempt whoever
        # adds it to make `evaluate` tolerant of a missing key — which would turn a broken
        # measurement into a clean bill of health, the one reading this module must never give.
        for key, _label in ga.RATCHET_KEYS:
            self.live.setdefault(key, [])
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


class PanelRelationRatchetBites(unittest.TestCase):
    """The coverage half of `panel_text_relation`, and the property that makes it a ratchet."""

    def setUp(self) -> None:
        self.stack = TemporaryDirectory()
        self.harness = Harness(self.stack)
        self.addCleanup(self.stack.cleanup)
        self.addCleanup(self.harness.restore)

    def test_it_is_declared_as_a_ratchet_and_not_reimplemented(self) -> None:
        """PATTERN_ALREADY_SOLVED_GATE: one definition, used by every site that ratchets."""
        self.assertIn("panel_relation_legacy", dict(ga.RATCHET_KEYS))

    def test_a_first_measurement_is_an_introduction_not_a_violation(self) -> None:
        """A ratchet that cannot be introduced is a ratchet nobody adds.

        `tighten` refuses on a violation, `record` refuses when a ratchet grew, `--bootstrap`
        refuses once any anchor exists — so before this distinction existed there was no path
        from "new measurement" to "anchored baseline" at all.
        """
        # Anchor a ledger that predates the ratchet — the key is absent from the measurement,
        # so `record --bootstrap` cannot write it into history. That is the real situation:
        # ten events already on the chain, none of which knows this key exists.
        del self.harness.live["panel_relation_legacy"]
        self.assertEqual(0, self.harness.run("record", "--bootstrap", "--batch", "B0"))
        self.assertNotIn("panel_relation_legacy", self.harness.events()[-1]["anchors"],
                         "fixture is not reproducing a pre-ratchet ledger")

        self.harness.live["panel_relation_legacy"] = ["PMID1", "PMID2"]
        violations, improvements, _ = ga.evaluate(self.harness.root, "wwox")
        self.assertEqual([], [item for item in violations if "panel_relation" in item])
        self.assertTrue(any("RATCHET_INTRODUCED" in item for item in improvements))
        # And the way out is the ordinary one, with no command that can also lower a baseline.
        self.assertEqual(0, self.harness.run("tighten", "--batch", "B1"))
        self.assertEqual(["PMID1", "PMID2"],
                         self.harness.events()[-1]["anchors"]["panel_relation_legacy"])

    def test_a_manifest_that_omits_the_field_after_the_baseline_is_a_violation(self) -> None:
        """This is 'the validator refuses new work without it', expressed as coverage."""
        self.harness.live["panel_relation_legacy"] = ["PMID1"]
        self.assertEqual(0, self.harness.run("record", "--bootstrap", "--batch", "B0"))
        self.harness.live["panel_relation_legacy"] = ["PMID1", "PMID_NEW"]
        violations, _, _ = ga.evaluate(self.harness.root, "wwox")
        self.assertTrue(any("RATCHET_VIOLATION" in item and "PMID_NEW" in item
                            for item in violations))

    def test_a_swap_at_equal_count_is_still_a_violation(self) -> None:
        """The count is not the constraint. A number would have said 'unchanged'."""
        self.harness.live["panel_relation_legacy"] = ["PMID1"]
        self.assertEqual(0, self.harness.run("record", "--bootstrap", "--batch", "B0"))
        self.harness.live["panel_relation_legacy"] = ["PMID_OTHER"]
        violations, _, _ = ga.evaluate(self.harness.root, "wwox")
        self.assertTrue(any("RATCHET_VIOLATION" in item for item in violations))

    def test_lowering_the_baseline_by_hand_does_not_lower_the_ratchet(self) -> None:
        """🔴 The constraint that holds the whole thing up.

        Updating a baseline must cost at least as much as complying with it. Editing the
        manifest — the gesture that has already happened here once, diligent comment and all —
        must not move the constraint, because the constraint lives in the hash-chained ledger
        and the manifest is only its readout. If this test ever passes trivially, the ratchet
        has become a number again.
        """
        self.harness.live["panel_relation_legacy"] = ["PMID1", "PMID2"]
        self.assertEqual(0, self.harness.run("record", "--bootstrap", "--batch", "B0"))
        manifest_path = self.harness.root / ga.MANIFEST_REL
        manifest_path.write_text(
            manifest_path.read_text(encoding="utf-8")
            .replace("panel_relation_legacy_baseline: 2", "panel_relation_legacy_baseline: 99")
            .replace('panel_relation_legacy_ids: ["PMID1", "PMID2"]',
                     'panel_relation_legacy_ids: []'),
            encoding="utf-8")
        self.harness.live["panel_relation_legacy"] = ["PMID1", "PMID2", "PMID3"]
        violations, _, _ = ga.evaluate(self.harness.root, "wwox")
        self.assertTrue(any("RATCHET_VIOLATION" in item and "PMID3" in item
                            for item in violations),
                        "a hand-edited manifest moved the constraint; the ledger is the anchor")

    def test_the_measurement_reads_manifests_and_one_bare_locator_is_enough(self) -> None:
        """Membership is per manifest: nineteen classified and one bare is one bare."""
        root = self.harness.root
        directory = root / "disease-models/wwox/research/deepdive_manifests"
        directory.mkdir(parents=True)
        def write(name, relations):
            (directory / name).write_text(json.dumps({
                "verbatim_locators": {"entries": [
                    {"panel_text_relation": rel} if rel else {} for rel in relations]}}),
                encoding="utf-8")
        write("PMID111.json", ["text_only", "panel_only"])
        write("PMID222.json", ["text_only", None])
        write("PMID333.json", [])
        self.assertEqual(["PMID222"], ga.measure_panel_relation_legacy(root, "wwox"))

    def test_an_unreadable_manifest_counts_as_unknown_not_as_clean(self) -> None:
        root = self.harness.root
        directory = root / "disease-models/wwox/research/deepdive_manifests"
        directory.mkdir(parents=True)
        (directory / "PMID444.json").write_text("{ truncated", encoding="utf-8")
        self.assertEqual(["PMID444"], ga.measure_panel_relation_legacy(root, "wwox"))


class CandidateBacklogIsDerivedNotDeclared(unittest.TestCase):
    """Read-and-not-promoted, measured the only way it can be measured without a new field."""

    def setUp(self) -> None:
        self.stack = TemporaryDirectory()
        self.root = Path(self.stack.name)
        self.addCleanup(self.stack.cleanup)
        (self.root / "framework/state").mkdir(parents=True)
        (self.root / "staging").mkdir()

    def _manifest(self, scope: str) -> None:
        (self.root / ga.MANIFEST_REL).write_text(
            f'batch_20260810_001_scope: "{scope}"\n', encoding="utf-8")

    def _candidate(self, name: str, body: str = "") -> None:
        (self.root / "staging" / name).write_text(body or "# candidate\n", encoding="utf-8")

    def test_a_candidate_named_in_a_scope_is_consumed(self) -> None:
        self._manifest("PROPAGATED 1: CC-20260806-19936220 landed.")
        self._candidate("commit_candidate_20260806_19936220.md")
        self.assertEqual([], ga.measure_candidate_backlog(self.root, "wwox"))

    def test_a_candidate_named_nowhere_is_pending(self) -> None:
        self._manifest("PROPAGATED 0.")
        self._candidate("commit_candidate_20260806_19936220.md")
        self.assertEqual(["CC-20260806-19936220"],
                         ga.measure_candidate_backlog(self.root, "wwox"))

    def test_two_punctuations_of_one_identifier_meet(self) -> None:
        """`CC-2026-07-05-001` and `CC-20260705-001` are the same candidate.

        Comparing raw strings would report every candidate as pending — a number always wrong
        in the alarming direction, which trains people to ignore it.
        """
        self._manifest("PROPAGATED 1: CC-2026-07-05-001 landed.")
        self._candidate("commit_candidate_20260705_001.md")
        self.assertEqual([], ga.measure_candidate_backlog(self.root, "wwox"))

    def test_a_compressed_range_names_exactly_one_candidate(self) -> None:
        """🔴 The live corpus produced this on the counter's first run.

        `CC-20260726-001/002/003` reads fine to a person and names one candidate to a machine,
        so 002 and 003 read as pending forever. The counter is right and the record was
        unreadable; the manifest note has been expanded rather than the matcher loosened,
        because a matcher that guessed at ranges would eventually guess wrong in the quiet
        direction — reporting work as done that nobody did.
        """
        self._manifest("PROPAGATED 3: CC-20260726-001/002/003 landed.")
        for suffix in ("001", "002", "003"):
            self._candidate(f"commit_candidate_20260726_{suffix}.md")
        self.assertEqual(["CC-20260726-002", "CC-20260726-003"],
                         ga.measure_candidate_backlog(self.root, "wwox"))

    def test_the_declared_identifier_wins_over_the_file_name(self) -> None:
        """The file name is a convention; the ID is what a batch scope will name."""
        self._manifest("PROPAGATED 1: CC-20260810-CLAIM004-REVIEW landed.")
        self._candidate("commit_candidate_something_else.md",
                        "**Candidate ID:** CC-20260810-CLAIM004-REVIEW\n")
        self.assertEqual([], ga.measure_candidate_backlog(self.root, "wwox"))

    def test_a_non_candidate_markdown_file_is_not_counted(self) -> None:
        self._manifest("PROPAGATED 0.")
        self._candidate("batch_inferential_sweep_20260726.md")
        self.assertEqual([], ga.measure_candidate_backlog(self.root, "wwox"))

    def test_an_absent_staging_directory_is_not_a_backlog_of_zero_by_accident(self) -> None:
        """`staging/` is gitignored, so worktrees do not have it — the surface-census case.

        The honest reading of an absent directory is 'not visible from here', and the honest
        behaviour is to contribute nothing without failing. What this test pins is that the
        absence is not an exception: a check that raised here would be red in every worktree.
        """
        self._manifest("PROPAGATED 0.")
        (self.root / "staging").rmdir()
        self.assertEqual([], ga.measure_candidate_backlog(self.root, "wwox"))

    def test_the_trigger_fires_at_five_and_not_at_four(self) -> None:
        four = {"candidate_backlog": [f"CC-{n}" for n in range(4)]}
        five = {"candidate_backlog": [f"CC-{n}" for n in range(5)]}
        self.assertEqual([], ga.candidate_backlog_trigger(four))
        self.assertTrue(ga.candidate_backlog_trigger(five)[0].startswith("CANDIDATE_BACKLOG"))

    def test_the_trigger_names_the_candidates_not_only_the_count(self) -> None:
        """A number says something is due; the names say what. The next batch needs both."""
        live = {"candidate_backlog": [f"CC-2026081{n}-001" for n in range(5)]}
        line = ga.candidate_backlog_trigger(live)[0]
        for identifier in live["candidate_backlog"]:
            self.assertIn(identifier, line)

    def test_it_is_a_trigger_and_not_a_ratchet(self) -> None:
        """A ratchet would make accumulating candidates an offence, and it is not one.

        Between batches the backlog is supposed to grow: the system reads faster than it
        propagates. What must not happen is that it grows silently.
        """
        self.assertNotIn("candidate_backlog", dict(ga.RATCHET_KEYS))


if __name__ == "__main__":
    unittest.main(verbosity=2)
