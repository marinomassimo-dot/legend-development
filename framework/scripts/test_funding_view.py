#!/usr/bin/env python3
"""Tests for funding_view.py: ordinal, no sums, cost only from the operator's file, unknown stays unknown."""
from __future__ import annotations

import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import funding_view as fv  # noqa: E402


def row(i: str, portfolio: str, **kw: str) -> dict:
    base = {c: "" for c in fv.OPP_COLS}
    base.update(opp_id=i, portfolio=portfolio, name=f"cand {i}", study_class="x", resolves_links="L1",
                L1="unknown", L2="unknown", L3="IPOTESI", L4="unknown", chain_notes="n", decision_named="yes",
                decision_text="d", null_control="partly", safety_cell="unknown", rows_that_change_decision="unknown", assay_id="A1",
                ordering_page_row="1", blind_check="not checked", read_state="r", cost_item="item1", sources="s")
    base.update(kw)
    return base


def write(d: Path, rows: list[dict], costs: list[list[str]] | None = None) -> None:
    (d / "opportunities.tsv").write_text(
        "\t".join(fv.OPP_COLS) + "\n" + "".join("\t".join(r[c] for c in fv.OPP_COLS) + "\n" for r in rows), encoding="utf-8")
    (d / "cost_ranges.tsv").write_text(
        "\t".join(fv.COST_COLS) + "\n" + "".join("\t".join(c) + "\n" for c in (costs or [])), encoding="utf-8")


class FundingView(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = Path(tempfile.mkdtemp(prefix="funding_view_test_"))
        self.addCleanup(shutil.rmtree, self.tmp, True)

    def test_first_line_and_default_cost_not_supplied(self) -> None:
        write(self.tmp, [row("O1", "ambitious"), row("O2", "conservative")])
        t = fv.render(self.tmp)
        self.assertLess(t.index("Funding order is not research order"), t.index("data-table"))
        self.assertIn("not supplied", t)
        self.assertNotIn("supplied</td>", t.replace("not supplied</td>", ""))

    def test_unknown_is_lowest_and_printed(self) -> None:
        o = row("O1", "ambitious", L1="DATO-matching", L2="unknown", L3="INFERENZA", L4="IPOTESI")
        self.assertEqual(fv.weakest(o), ["L2"])
        self.assertIn(">unknown<", self._r([o]))

    def _r(self, rows: list[dict]) -> str:
        write(self.tmp, rows)
        return fv.render(self.tmp)

    def test_resolved_is_yes_only_when_every_tied_weakest_link_is_resolved(self) -> None:
        o = row("O1", "ambitious", L1="unknown", L2="unknown", L3="IPOTESI", L4="IPOTESI", resolves_links="L1,L2")
        self.assertEqual(fv.resolved(o), "yes")
        o = row("O1", "ambitious", L1="unknown", L2="unknown", L3="unknown", L4="IPOTESI", resolves_links="L1,L2")
        self.assertEqual(fv.resolved(o), "partly")
        o = row("O1", "ambitious", L1="DATO-matching", L2="DATO-matching", L3="unknown", L4="IPOTESI", resolves_links="L1,L2")
        self.assertEqual(fv.resolved(o), "no")

    def test_ties_stay_ties_and_weakest_marks_all_ties(self) -> None:
        o = row("O1", "ambitious", L1="unknown", L2="unknown")
        self.assertEqual(fv.weakest(o), ["L1", "L2", "L4"])
        rows = [row("O1", "ambitious", assay_id="A1"), row("O2", "conservative", assay_id="A2")]
        write(self.tmp, rows)
        r = fv.dense_rank(fv.keys(fv.load(self.tmp)[0])["A"])
        self.assertEqual(r["O1"], r["O2"], "identical keys must share one rank, not be broken by id")

    def test_cost_never_changes_any_ordering(self) -> None:
        rows = [row("O1", "ambitious"), row("O2", "conservative", assay_id="A2", decision_named="unknown")]
        write(self.tmp, rows)
        before = {n: fv.dense_rank(k) for n, k in fv.keys(fv.load(self.tmp)[0]).items()}
        write(self.tmp, rows, [["item1", "1", "2", "EUR", "quote", "2026-11-19"]])
        after = {n: fv.dense_rank(k) for n, k in fv.keys(fv.load(self.tmp)[0]).items()}
        self.assertEqual(before, after)
        t = fv.render(self.tmp)
        self.assertIn("1 to 2 EUR", t)

    def test_bad_cost_row_is_refused(self) -> None:
        write(self.tmp, [row("O1", "ambitious")], [["item1", "5", "2", "EUR", "q", "d"]])
        with self.assertRaises(fv.ViewError):
            fv.load(self.tmp)
        write(self.tmp, [row("O1", "ambitious")], [["item1", "1", "2", "EUR", "", "d"]])
        with self.assertRaises(fv.ViewError):
            fv.load(self.tmp)

    def test_unknown_class_value_is_refused(self) -> None:
        write(self.tmp, [row("O1", "ambitious", L1="strong")])
        with self.assertRaises(fv.ViewError):
            fv.load(self.tmp)

    def test_pair_cost_needs_both_and_one_currency(self) -> None:
        a, b = row("O1", "ambitious", cost_item="i1"), row("O2", "conservative", cost_item="i2")
        c1 = {"i1": {"lo": 1.0, "hi": 2.0, "currency": "EUR"}}
        self.assertEqual(fv.pair_cost(a, b, c1), "not supplied (1 of 2)")
        c2 = {**c1, "i2": {"lo": 3.0, "hi": 4.0, "currency": "USD"}}
        self.assertIn("different currencies", fv.pair_cost(a, b, c2))
        c3 = {**c1, "i2": {"lo": 3.0, "hi": 4.0, "currency": "EUR"}}
        self.assertIn("4 to 6 EUR", fv.pair_cost(a, b, c3))

    def test_info_sensitivity_only_with_two_dossiers(self) -> None:
        rows = [row("O1", "ambitious", rows_that_change_decision="2"), row("O2", "conservative")]
        write(self.tmp, rows)
        self.assertIn("not available; 1 of 2", fv.render(self.tmp))
        rows[1]["rows_that_change_decision"] = "1"
        write(self.tmp, rows)
        self.assertIn('data-table="info"', fv.render(self.tmp))

    def test_committed_table_loads_and_preview_is_current(self) -> None:
        self.assertEqual(fv.main(["check"]), 0)
        opps, costs = fv.load(fv.DEFAULT_DIR)
        self.assertGreaterEqual(len(opps), 6)
        self.assertEqual(costs, {}, "agents never write cost_ranges.tsv; only the operator supplies rows")

    def test_tool_has_no_write_path_to_cost_file(self) -> None:
        src = Path(fv.__file__).read_text(encoding="utf-8")
        self.assertNotIn("cost_ranges.tsv\").write", src)
        self.assertNotIn("open(d / \"cost_ranges.tsv\", \"w", src)


if __name__ == "__main__":
    unittest.main(verbosity=2)
