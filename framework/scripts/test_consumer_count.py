#!/usr/bin/env python3
"""Regressions for `consumer_count.py`: the two false joins of ADV-279, on the lines that made them, no network."""
import tempfile
import unittest
from pathlib import Path

import consumer_count as cc

# CLAIM 024: "paper 204" is the corpus placeholder; PAPER 204 is PMID 33958783, an unrelated genetics study.
CLAIM_LINE = "**Source:** PAPER 055. Il pointer storico `paper 204 (corpus 181–220)` è conservato come audit trail."
# DL-MECH-056: PMID 36979157 stands only in a list of records to skip.
AGENDA = ("**Next-search agenda:** `READ_NEXT` PMID 36530994, dopo collegamento audit-only del corrigendum PMID 37095367 e skip "
          "dei record già letti 37248434, 36979157, 36828035 e 36572673.")


def fixture(tmp: str) -> Path:
    base = Path(tmp) / cc.MODEL
    (base / "registries").mkdir(parents=True)
    (base / "research").mkdir()
    (base / "registries" / "paper_registry_current.md").write_text(
        "## PAPER 204 — genetics\n- **Identifier:** PMID 33958783\n\n## PAPER 055 — source\n- **Identifier:** PMID 35716775\n",
        encoding="utf-8")
    (base / "registries" / "claim_registry_current.md").write_text(
        f"## CLAIM 024 — tandem\n{CLAIM_LINE}\n\n## CLAIM 099 — real use\nSource: [[paper_registry_current#PAPER 204]].\n",
        encoding="utf-8")
    (base / "research" / "discovery_ledger_current.md").write_text(
        f"### DL-MECH-056 — SNP\n- **Fonte:** PMID 37324196.\n\n{AGENDA}\n\n### DL-MECH-115 — SDR\n- **Fonte:** PMID 37248434.\n",
        encoding="utf-8")
    return Path(tmp)


class TheTwoFalseJoins(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = fixture(tmp.name)

    def found(self, key, old_rule=False):
        names = cc.consumers([key], cc.registry_ids(self.root), cc.units(self.root, old_rule), old_rule)[key]
        return [name.split(":", 2)[2].split(" —")[0] for name in names]

    def test_a_placeholder_number_does_not_join_the_registry_paper(self):
        self.assertEqual(self.found("33958783"), ["CLAIM 099"])
        self.assertEqual(self.found("33958783", old_rule=True), ["CLAIM 024", "CLAIM 099"])

    def test_a_next_search_agenda_line_is_not_a_use(self):
        self.assertEqual(self.found("36979157"), [])
        self.assertEqual(self.found("36979157", old_rule=True), ["DL-MECH-056"])

    def test_a_use_outside_the_agenda_line_still_counts(self):
        self.assertEqual(self.found("37248434"), ["DL-MECH-115"])
        self.assertEqual(self.found("37324196"), ["DL-MECH-056"])

    def test_identifiers_still_ignore_case(self):
        claim = self.root / cc.MODEL / "registries" / "claim_registry_current.md"
        claim.write_text("## CLAIM 001\ndoi 10.1000/ABC.5\n", encoding="utf-8")
        self.assertEqual(self.found("10.1000/abc.5"), ["CLAIM 001"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
