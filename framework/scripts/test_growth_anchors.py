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
