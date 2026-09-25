#!/usr/bin/env python3
"""Regressions for the locator-propagation obligation (`locator_propagation.py`).

The defect, measured 2026-09-14 before this suite existed: verification wave W4 corrected a bar
count from six to twelve. The correction reached the discovery ledger, a dossier and a queue
entry, and never reached the two persisted locators — at `4c1a5dd`, `PMID33058734.json`
entries[27] and entries[29] still asserted "six bars" with no `contradicts_locator`. The batch
report of that day wrote the obligation down in a table cell; nothing counted it, and no check
could, because an obligation had no form a check could read.

The harness half is built here: a one-line declaration a science actor writes where the
correction is recorded, and a detector that resolves each declaration against its manifest.
The harness never writes a manifest; applying the amendment is the science actors' act.
Expectations were fixed before `locator_propagation.py` existed.
"""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

LINE_27 = ('LOCATOR_PROPAGATION_OBLIGATION: PMID33058734 entries[27] proposition '
           'retired="six bars" source=ALDAZ-VERIFY-W4')
LINE_29 = ('LOCATOR_PROPAGATION_OBLIGATION: PMID33058734 entries[29] proposition '
           'retired="six bars" source=ALDAZ-VERIFY-W4')


def entry(proposition: str, declared: bool = False) -> dict:
    out = {"proposition": proposition, "snippet": "Figure 4. Caption title long enough to quote",
           "surface": "figure", "anchor": "Figure 4"}
    if declared:
        out["contradicts_locator"] = {"what_changed": "count corrected", "audit": {"auditors": 1}}
    return out


class Workspace:
    def __init__(self, tmp: str) -> None:
        self.root = Path(tmp)
        self.research = self.root / "disease-models/wwox/research"
        self.manifests = self.research / "deepdive_manifests"
        self.manifests.mkdir(parents=True)

    def manifest(self, pmid: str, entries: list[dict]) -> None:
        (self.manifests / f"PMID{pmid}.json").write_text(
            json.dumps({"pmid": pmid, "verbatim_locators": {"entries": entries}}),
            encoding="utf-8")

    def note(self, name: str, text: str) -> None:
        path = self.research / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def historical_state(self, *, fixed: bool) -> None:
        """entries[27] and [29] as at 4c1a5dd (six, undeclared) or 24c5384 (twelve, declared)."""
        filler = [entry(f"filler proposition {i}") for i in range(30)]
        word = "twelve bars" if fixed else "six bars"
        filler[27] = entry(f"NO asterisk on any of the {word} across panels A, B and C", fixed)
        filler[29] = entry(f"NO asterisk on any of the {word} of Figure 6", fixed)
        self.manifest("33058734", filler)


class TheObligationIsVisibleAndCountable(unittest.TestCase):
    def setUp(self) -> None:
        import locator_propagation  # noqa: PLC0415 - absent before the fix, by design
        self.mod = locator_propagation
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.ws = Workspace(self._tmp.name)

    def states(self) -> dict[tuple[str, int], str]:
        return {(o.pmid, o.entry): o.state for o in self.mod.scan(self.ws.root, "wwox").obligations}

    def test_the_historical_state_is_two_open_obligations(self) -> None:
        self.ws.historical_state(fixed=False)
        self.ws.note("2026-09-14_BATCH_report.md", f"# report\n\n{LINE_27}\n{LINE_29}\n")
        self.assertEqual({("33058734", 27): self.mod.OPEN, ("33058734", 29): self.mod.OPEN},
                         self.states())
        self.assertEqual(2, self.mod.scan(self.ws.root, "wwox").count(self.mod.OPEN))

    def test_a_declared_revision_discharges_it(self) -> None:
        self.ws.historical_state(fixed=True)
        self.ws.note("report.md", f"{LINE_27}\n{LINE_29}\n")
        self.assertEqual({self.mod.DISCHARGED}, set(self.states().values()))

    def test_a_silent_rewrite_is_not_a_discharge(self) -> None:
        """The retired text is gone but nobody declared the revision: the audit trail the
        contradiction procedure exists for is missing, so this is reported, not closed."""
        self.ws.historical_state(fixed=False)
        entries = json.loads((self.ws.manifests / "PMID33058734.json").read_text())
        entries["verbatim_locators"]["entries"][27]["proposition"] = "twelve bars, rewritten"
        (self.ws.manifests / "PMID33058734.json").write_text(json.dumps(entries))
        self.ws.note("report.md", f"{LINE_27}\n")
        self.assertEqual({("33058734", 27): self.mod.UNDECLARED_DISCHARGE}, self.states())

    def test_matching_ignores_case_and_whitespace_but_not_words(self) -> None:
        self.ws.manifest("1", [entry("no asterisk on any of the SIX\n  bars")])
        self.ws.note("n.md", 'LOCATOR_PROPAGATION_OBLIGATION: PMID1 entries[0] proposition retired="six bars"\n')
        self.assertEqual({("1", 0): self.mod.OPEN}, self.states())

    def test_a_waiver_closes_it_with_its_reason(self) -> None:
        self.ws.historical_state(fixed=False)
        self.ws.note("report.md", f"{LINE_27}\n"
                     'LOCATOR_PROPAGATION_WAIVED: PMID33058734 entries[27] proposition '
                     'retired="six bars" reason="the correction was itself withdrawn by W5"\n')
        result = self.mod.scan(self.ws.root, "wwox")
        self.assertEqual({("33058734", 27): self.mod.WAIVED}, self.states())
        self.assertIn("withdrawn by W5", result.obligations[0].detail)

    def test_an_unresolvable_target_is_named_not_dropped(self) -> None:
        self.ws.manifest("2", [entry("one entry only")])
        self.ws.note("n.md",
                     'LOCATOR_PROPAGATION_OBLIGATION: PMID2 entries[5] proposition retired="x y"\n'
                     'LOCATOR_PROPAGATION_OBLIGATION: PMID3 entries[0] snippet retired="x y"\n')
        self.assertEqual({("2", 5): self.mod.UNRESOLVABLE, ("3", 0): self.mod.UNRESOLVABLE},
                         self.states())

    def test_a_malformed_declaration_is_a_finding_with_its_location(self) -> None:
        self.ws.manifest("1", [entry("x")])
        self.ws.note("n.md", "text\nLOCATOR_PROPAGATION_OBLIGATION: PMID1 entry 0 six bars\n")
        result = self.mod.scan(self.ws.root, "wwox")
        self.assertEqual([], result.obligations)
        self.assertEqual(1, len(result.malformed))
        self.assertIn("n.md:2", result.malformed[0])

    def test_only_revision_fields_can_carry_an_obligation(self) -> None:
        """`snippet` and `proposition` are locator_contradiction_audit.REVISION_FIELDS; an
        obligation on any other field has no revision procedure behind it."""
        self.assertIs(self.mod.REVISION_FIELDS, __import__("locator_contradiction_audit").REVISION_FIELDS)
        self.ws.manifest("1", [entry("x")])
        self.ws.note("n.md", 'LOCATOR_PROPAGATION_OBLIGATION: PMID1 entries[0] anchor retired="Figure 4"\n')
        self.assertEqual(1, len(self.mod.scan(self.ws.root, "wwox").malformed))

    def test_a_duplicate_declaration_counts_once(self) -> None:
        self.ws.historical_state(fixed=False)
        self.ws.note("a.md", f"{LINE_27}\n")
        self.ws.note("sub/b.md", f"{LINE_27}\n")
        self.assertEqual(1, self.mod.scan(self.ws.root, "wwox").count(self.mod.OPEN))

    def test_the_harness_never_writes_a_manifest(self) -> None:
        self.ws.historical_state(fixed=False)
        self.ws.note("report.md", f"{LINE_27}\n")
        before = (self.ws.manifests / "PMID33058734.json").read_bytes()
        self.mod.main(["--root", str(self.ws.root), "--disease", "wwox"])
        self.assertEqual(before, (self.ws.manifests / "PMID33058734.json").read_bytes())


class LintCountsOpenObligations(unittest.TestCase):
    """The proof of the defect: LINT said nothing while the two locators stayed stale."""

    def test_lint_reports_open_obligations_without_blocking(self) -> None:
        import legend_lint  # noqa: PLC0415
        with tempfile.TemporaryDirectory() as tmp:
            ws = Workspace(tmp)
            ws.historical_state(fixed=False)
            ws.note("2026-09-14_BATCH_report.md", f"{LINE_27}\n{LINE_29}\n")
            findings: list = []
            legend_lint._check_locator_propagation(findings, tmp)
        opened = [f for f in findings if f.code == "LOCATOR_PROPAGATION_OPEN"]
        self.assertEqual(2, len(opened), findings)
        self.assertTrue(all(f.severity == "WARN_BUT_PROCEED" for f in opened))
        self.assertTrue(any("entries[27]" in f.message for f in opened))


if __name__ == "__main__":
    unittest.main(verbosity=2)
