#!/usr/bin/env python3
"""Golden and refusal tests for aed_matrix.py (a synthetic fixture: no scientific content)."""
from __future__ import annotations

import contextlib
import hashlib
import io
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import aed_matrix as am  # noqa: E402

RULE = {
    "rule_version": "fixture-1",
    "tier_rubric": {"0": "none", "1": "indirect", "2": "system, no contrast", "3": "system with contrast"},
    "directness_rubric": {"0": "none", "1": "plausible", "2": "same pathway", "3": "primary target"},
    "endpoints": ["seizure", "development"], "age_windows": ["A", "B"],
    "classes": ["c1", "c2", "c3"], "discriminating_top_set_max_share": [1, 3],
    "never_specific_threads": ["T3"], "zero_directness_threads": ["T4"],
    "rank_by": "score_all", "permutations": 40, "seed": 7,
}
HEADER = am.CELL_COLUMNS


def cell(cid, thread, cls, sign="match", tier=3, directness=3, endpoint="seizure", age="A", axis="X",
         origin="o1", gc="yes", dg="no", agent="", unit="cells"):
    return dict(zip(HEADER, [cid, thread, cls, agent, endpoint, age, sign, str(tier), str(directness),
                             axis, origin, gc, dg, unit, "fixture"]))


CELLS = [
    cell("k1", "T1", "c1", tier=3, directness=3, axis="X", origin="o1"),                 # 9
    cell("k2", "T2", "c1", tier=2, directness=2, axis="G", origin="o2", age="B"),        # 4
    cell("k3", "T2", "c2", tier=2, directness=3, axis="G", origin="o2", gc="no"),        # 6
    cell("k4", "T3", "c2", tier=2, directness=3, axis="G", origin="o2", gc="yes"),       # same key: not 12
    cell("k5", "T1", "c3", sign="aggravation", tier=3, directness=2, axis="X", origin="o1"),
    cell("k6", "T2", "c3", tier=1, directness=1, axis="G", origin="o9", age="B"),        # 1
    cell("k7", "T2", "c3", sign="unknown", age="B", origin="o8"),
    cell("k8", "T2", "c2", sign="neutral", origin="o7"),
    cell("k9", "T1", "c2", tier=3, directness=3, endpoint="development", origin="o5"),   # 9, other endpoint
]


def write(tmp: Path, rows, rule=None, name="cells.tsv"):
    cells, rule_path = tmp / name, tmp / "rule.json"
    cells.write_text("\t".join(HEADER) + "\n" + "".join("\t".join(r[c] for c in HEADER) + "\n" for r in rows))
    rule_path.write_text(json.dumps(rule or RULE, sort_keys=True))
    return cells, rule_path


def table(text: str):
    lines = [l for l in text.splitlines() if l.count("\t") == len(am.OUT_COLUMNS) - 1]
    head = lines[0].split("\t")
    return [dict(zip(head, l.split("\t"))) for l in lines[1:]]


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def score(self, rows=None, rule=None, *extra):
        cells, rule_path = write(self.dir, CELLS if rows is None else rows, rule)
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = am.main(["--root", str(self.dir), "score", str(cells), str(rule_path), *extra])
        return code, out.getvalue(), err.getvalue()

    def row(self, text, endpoint, window, cls):
        return next(r for r in table(text) if (r["endpoint"], r["window"], r["class_id"]) == (endpoint, window, cls))


class GoldenScores(Base):
    def test_pooled_seizure_scores_and_ranks(self):
        code, out, _ = self.score()
        self.assertEqual(code, 0)
        c1, c2, c3 = (self.row(out, "seizure", "pooled", c) for c in ("c1", "c2", "c3"))
        self.assertEqual((c1["rank"], c2["rank"], c3["rank"]), ("1", "2", "3"))
        self.assertEqual((c1["score_all"], c2["score_all"], c3["score_all"]), ("13", "6", "1"))

    def test_one_origin_counts_once_across_threads(self):
        # k3 (T2) and k4 (T3) share the key (G, o2): 6, never 12
        self.assertEqual(self.row(self.score()[1], "seizure", "pooled", "c2")["score_all"], "6")

    def test_a_generic_thread_never_feeds_the_specific_score(self):
        out = self.score()[1]
        self.assertEqual(self.row(out, "seizure", "pooled", "c2")["score_specific"], "0")
        self.assertEqual(self.row(out, "seizure", "pooled", "c1")["score_specific"], "13")

    def test_aggravation_is_its_own_column_and_never_netted(self):
        c3 = self.row(self.score()[1], "seizure", "pooled", "c3")
        self.assertEqual((c3["aggravation_score"], c3["score_all"]), ("6", "1"))

    def test_unknown_and_neutral_are_counted_apart_and_not_scored(self):
        out = self.score()[1]
        self.assertEqual(self.row(out, "seizure", "pooled", "c3")["unknown_cells"], "1")
        self.assertEqual(self.row(out, "seizure", "pooled", "c3")["neutral_cells"], "0")
        self.assertEqual(self.row(out, "seizure", "pooled", "c2")["neutral_cells"], "1")
        self.assertEqual(self.row(out, "seizure", "pooled", "c2")["unknown_cells"], "0")

    def test_endpoints_are_scored_once_each_and_never_summed(self):
        out = self.score()[1]
        self.assertEqual(self.row(out, "development", "pooled", "c2")["score_all"], "9")
        self.assertEqual(self.row(out, "seizure", "pooled", "c2")["score_all"], "6")
        self.assertFalse(any(r["endpoint"] not in ("seizure", "development") for r in table(out)))

    def test_age_windows_are_printed_next_to_the_pooled_ranking(self):
        out = self.score()[1]
        self.assertEqual({r["window"] for r in table(out) if r["endpoint"] == "seizure"}, {"pooled", "A", "B"})
        self.assertEqual(self.row(out, "seizure", "A", "c1")["score_all"], "9")
        self.assertEqual(self.row(out, "seizure", "B", "c1")["score_all"], "4")

    def test_stability_line_names_top_class_and_the_count(self):
        out = self.score()[1]
        line = next(l for l in out.splitlines() if l.startswith("[seizure] top class"))
        self.assertIn("top class c1", line)
        self.assertIn("kept in", line)


class AmendmentOne(Base):
    def test_the_thread_set_is_data_and_its_digest_is_printed(self):
        rows = CELLS + [cell("n1", "T99", "c3", tier=1, directness=1, axis="Q", origin="o99")]
        code, out, _ = self.score(rows)
        self.assertEqual(code, 0)
        threads = sorted({r["thread_id"] for r in rows})
        digest = hashlib.sha256("\n".join(threads).encode()).hexdigest()
        self.assertIn(f"threads {len(threads)} sha256 {digest}", out)
        self.assertIn("T99", out)

    def test_a_cell_needs_a_locator(self):
        bad = dict(cell("a", "T1", "c1"), source_locator="")
        self.assertIn("source_locator is required", self.refused_with([bad]))

    def refused_with(self, rows):
        code, _, err = self.score(rows)
        self.assertEqual(code, 2, err)
        return err

    def test_tie_labels_follow_the_third_rule(self):
        share = [1, 3]
        self.assertEqual(am.tie_label(0, 15, share), "no_scored_class")
        self.assertEqual(am.tie_label(1, 15, share), "discriminating")
        self.assertEqual(am.tie_label(5, 15, share), "tie_set_weak")
        self.assertEqual(am.tie_label(6, 15, share), "not_discriminating")

    def test_top_set_size_and_informativeness_are_reported(self):
        rows = [cell("a", "T1", "c1", origin="o1"), cell("b", "T2", "c2", axis="Y", origin="o2")]
        out = self.score(rows)[1]
        r = self.row(out, "seizure", "pooled", "c1")
        self.assertEqual((r["top_set_size"], r["informativeness"], r["top_set_label"]),
                         ("2", "0.333", "not_discriminating"))
        self.assertEqual(self.row(out, "seizure", "pooled", "c1")["tied_with"], "c2")

    def test_equal_tiers_make_the_null_undefined_not_a_p_value(self):
        rows = [cell("a", "T1", "c1", tier=2, directness=3, origin="o1"),
                cell("b", "T2", "c2", tier=2, directness=2, axis="Y", origin="o2")]
        out = self.score(rows)[1]
        r = self.row(out, "seizure", "pooled", "c1")
        self.assertEqual((r["null_mean"], r["excess"], r["null_ge_fraction"]), ("undefined",) * 3)
        self.assertIn("null undefined (equal tiers", out)

    def test_unequal_tiers_keep_a_defined_null(self):
        r = self.row(self.score()[1], "seizure", "pooled", "c1")
        self.assertNotEqual(r["null_mean"], "undefined")

    def test_a_window_with_no_match_cell_is_a_frozen_null_ordering(self):
        rows = [c for c in CELLS if c["endpoint"] == "seizure"]
        out = self.score(rows)[1]
        dev = [r for r in table(out) if r["endpoint"] == "development" and r["window"] == "pooled"]
        self.assertEqual(len(dev), 3)
        self.assertEqual({r["top_set_label"] for r in dev}, {"not_scorable_null_ordering"})
        self.assertEqual({r["rank"] for r in dev}, {"null"})
        self.assertEqual({r["score_all"] for r in dev}, {"0"})
        self.assertIn("[development pooled] not scorable", out)

    def test_per_thread_sum_sits_next_to_the_origin_collapsed_score(self):
        r = self.row(self.score()[1], "seizure", "pooled", "c2")
        self.assertEqual((r["score_all"], r["score_per_thread_sum"]), ("6", "12"))

    def test_origin_collapse_that_changes_the_top_set_is_named(self):
        rows = [cell("a", "T1", "c1", tier=2, directness=2, origin="O"), cell("b", "T2", "c1", tier=2, directness=2, origin="O"),
                cell("c", "T3", "c1", tier=2, directness=2, origin="O"),
                cell("d", "T1", "c2", tier=3, directness=2, axis="Y", origin="P")]
        out = self.score(rows)[1]
        self.assertEqual(self.row(out, "seizure", "pooled", "c1")["score_per_thread_sum"], "12")
        self.assertEqual(self.row(out, "seizure", "pooled", "c1")["rank_per_thread_sum"], "1")
        self.assertEqual(self.row(out, "seizure", "pooled", "c2")["rank"], "1")
        self.assertIn("origin collapse changes the top set: per-thread sum {c1} -> origin-collapsed {c2}", out)

    def test_a_single_origin_is_named(self):
        rows = [cell("a", "T1", "c1", origin="O"), cell("b", "T2", "c2", origin="O")]
        self.assertIn("single origin O carries every match cell", self.score(rows)[1])

    def test_two_cell_enumeration_is_reported_and_capped(self):
        self.assertIn("two-cell tier enumeration: top class kept in", self.score()[1])
        with unittest_patch_cap(1):
            self.assertIn("two-cell tier enumeration not run", self.score()[1])


class unittest_patch_cap:
    def __init__(self, cap):
        self.cap = cap

    def __enter__(self):
        self.old, am.PAIR_RUN_CAP = am.PAIR_RUN_CAP, self.cap

    def __exit__(self, *exc):
        am.PAIR_RUN_CAP = self.old


class Determinism(Base):
    def test_two_runs_are_byte_identical(self):
        first, second = self.score()[1], self.score()[1]
        self.assertEqual(first, second)

    def test_the_permutation_keeps_every_class_degree(self):
        rows = [dict(zip(HEADER, [f"k{i}", "T1", c, "", "seizure", "A", "match", "1", "1", "X", f"o{i}",
                                  "yes", "no", "cells", "f"])) for i, c in enumerate("aaabbc")]
        for index in range(5):
            moved = am.permuted(rows, 7, index)
            self.assertEqual(sorted(r["class_id"] for r in moved), sorted(r["class_id"] for r in rows))
        self.assertNotEqual([r["class_id"] for r in am.permuted(rows, 7, 0)],
                            [r["class_id"] for r in am.permuted(rows, 7, 1)])

    def test_the_permutation_does_not_depend_on_row_order(self):
        a = am.permuted(CELLS, 7, 3)
        b = am.permuted(list(reversed(CELLS)), 7, 3)
        self.assertEqual({r["cell_id"]: r["class_id"] for r in a}, {r["cell_id"]: r["class_id"] for r in b})

    def test_a_broad_class_is_not_credited_for_breadth(self):
        rows = [cell(f"b{i}", "T1", "c1", tier=1, directness=1, axis=f"x{i}", origin=f"o{i}") for i in range(4)]
        rows += [cell("n1", "T1", "c2", tier=3, directness=3, axis="y", origin="p1")]
        out = self.score(rows)[1]
        self.assertEqual(self.row(out, "seizure", "pooled", "c1")["score_all"], "4")
        # c1 owns 4 cells of 5: shuffling labels gives it ~4 of 5 cells' values, so little excess
        self.assertLess(float(self.row(out, "seizure", "pooled", "c1")["excess"]), 3.0)


class Stability(Base):
    def test_a_one_point_lead_is_reported_as_fragile(self):
        rows = [cell("a", "T1", "c1", tier=2, directness=2, origin="o1"),
                cell("b", "T1", "c2", tier=2, directness=2, axis="Y", origin="o2"),
                cell("c", "T2", "c2", tier=1, directness=1, axis="Z", origin="o3")]
        top, kept, total, moved = am.stability(rows, ["c1", "c2"], {"rank_by": "score_all"})
        self.assertEqual(top, "c2")
        self.assertLess(kept, total)
        self.assertTrue(moved)

    def test_a_wide_lead_is_stable(self):
        top, kept, total, moved = am.stability([c for c in CELLS if c["endpoint"] == "seizure"],
                                               ["c1", "c2", "c3"], {"rank_by": "score_all"})
        self.assertEqual((top, kept, total, moved), ("c1", total, total, []))


class AgentRanking(Base):
    def test_not_licensed_without_a_separating_key(self):
        rows = [cell("a", "T1", "c1", agent="ag1", origin="o1"), cell("b", "T1", "c1", agent="ag2", origin="o1")]
        self.assertIn("not licensed", am.agent_ranking(rows, "c1", "score_all"))

    def test_licensed_when_a_key_separates_two_agents(self):
        rows = [cell("a", "T1", "c1", agent="ag1", origin="o1"),
                cell("b", "T1", "c1", agent="ag2", axis="G", origin="o2", tier=1, directness=1)]
        text = am.agent_ranking(rows, "c1", "score_all")
        self.assertIn("ag1=9", text)
        self.assertIn("ag2=1", text)


class Refusals(Base):
    def refused(self, rows=None, rule=None, *extra):
        code, _, err = self.score(rows, rule, *extra)
        self.assertEqual(code, 2, err)
        return err

    def test_missing_column(self):
        cells, rule_path = write(self.dir, CELLS)
        cells.write_text("cell_id\tthread_id\nk1\tT1\n")
        with contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(am.main(["--root", str(self.dir), "score", str(cells), str(rule_path)]), 2)

    def test_cell_without_origin_or_axis(self):
        self.assertIn("origin_id is required", self.refused([cell("a", "T1", "c1", origin="")]))
        self.assertIn("axis is required", self.refused([cell("a", "T1", "c1", axis="")]))

    def test_vocabulary_is_closed(self):
        self.assertIn("sign", self.refused([cell("a", "T1", "c1", sign="maybe")]))
        self.assertIn("class_id", self.refused([cell("a", "T1", "zz")]))
        self.assertIn("age", self.refused([cell("a", "T1", "c1", age="Z")]))
        self.assertIn("endpoint", self.refused([cell("a", "T1", "c1", endpoint="other")]))
        self.assertIn("integer 0-3", self.refused([cell("a", "T1", "c1", tier=4)]))

    def test_duplicate_cell_id(self):
        self.assertIn("duplicate", self.refused([cell("a", "T1", "c1"), cell("a", "T2", "c2", origin="o3")]))

    def test_zero_directness_thread_must_carry_zero(self):
        self.assertIn("directness 0", self.refused([cell("a", "T4", "c1", directness=2)]))
        code, _, _ = self.score([cell("a", "T4", "c1", directness=0)])
        self.assertEqual(code, 0)

    def test_drug_by_genotype_implies_genotype_contrast(self):
        self.assertIn("both to yes", self.refused([cell("a", "T1", "c1", gc="no", dg="yes")]))

    def test_rule_without_a_rubric_or_with_bad_rank(self):
        bad = dict(RULE, tier_rubric={"0": "none"})
        self.assertIn("tier_rubric", self.refused(None, bad))
        self.assertIn("rank_by", self.refused(None, dict(RULE, rank_by="score_net")))
        self.assertIn("lacks", self.refused(None, {k: v for k, v in RULE.items() if k != "seed"}))

    def test_pinned_digest_must_match(self):
        cells, rule_path = write(self.dir, CELLS)
        good = hashlib.sha256(rule_path.read_bytes()).hexdigest()
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(am.main(["score", str(cells), str(rule_path), "--expect-rule-sha256", good]), 0)
            self.assertEqual(am.main(["score", str(cells), str(rule_path), "--expect-rule-sha256", "0" * 64]), 2)

    def test_no_cells_scores_nothing_and_exits_zero(self):
        code, out, _ = self.score([])
        self.assertEqual(code, 0)
        self.assertIn("no cells", out)


class RuleBeforeCells(unittest.TestCase):
    def git(self, root, *args, date="2026-11-16T08:00:00+00:00"):
        env = {"GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t" + chr(64) + "scratch.invalid",
               "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t" + chr(64) + "scratch.invalid",
               "GIT_COMMITTER_DATE": date, "PATH": "/usr/bin:/bin:/usr/local/bin", "HOME": str(root)}
        subprocess.run(["git", "-C", str(root), *args], check=True, capture_output=True, env=env)

    def commit(self, root, name, text, date):
        (root / name).write_text(text)
        self.git(root, "add", name)
        self.git(root, "commit", "-q", "-m", name, "--date", date, date=date)

    def test_order_is_read_from_git(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.git(root, "init", "-q", "-b", "main")
            cells, rule = write(root, CELLS)
            self.assertEqual(am.rule_order(root, rule, cells), "untracked")
            self.commit(root, "rule.json", rule.read_text(), "2026-11-16T08:00:00+00:00")
            self.commit(root, "cells.tsv", cells.read_text(), "2026-11-16T09:00:00+00:00")
            self.assertEqual(am.rule_order(root, rule, cells), "yes")
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                self.assertEqual(am.main(["--root", str(root), "score", str(cells), str(rule)]), 0)
            self.assertIn("committed before cells: yes", out.getvalue())

    def test_cells_committed_before_the_rule_are_refused(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.git(root, "init", "-q", "-b", "main")
            cells, rule = write(root, CELLS)
            self.commit(root, "cells.tsv", cells.read_text(), "2026-11-16T08:00:00+00:00")
            self.commit(root, "rule.json", rule.read_text(), "2026-11-16T09:00:00+00:00")
            self.assertEqual(am.rule_order(root, rule, cells), "not_ancestor")
            with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(am.main(["--root", str(root), "score", str(cells), str(rule)]), 2)

    def test_same_commit_is_reported_not_trusted(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.git(root, "init", "-q", "-b", "main")
            cells, rule = write(root, CELLS)
            self.git(root, "add", "cells.tsv", "rule.json")
            self.git(root, "commit", "-q", "-m", "both")
            self.assertEqual(am.rule_order(root, rule, cells), "same_commit")


RULE_V1 = Path(__file__).resolve().parents[2] / ("disease-models/wwox/research/drug_repurposing/"
                                                  "advisor_pilot_20261113/brainstorm_20261116/rule.json")
RULE_V1_SHA256 = "679a60894100d26bf4e550e2f49a888e39b8451dfbf428c2157f8b0cb2d94982"  # announced 2026-11-16


class TheCommittedRuleIsTheAnnouncedOne(unittest.TestCase):
    def test_rule_v1_is_valid_and_its_digest_is_the_announced_one(self):
        raw = RULE_V1.read_bytes()
        self.assertEqual(hashlib.sha256(raw).hexdigest(), RULE_V1_SHA256,
                         "rule.json changed: a new digest must be announced and recorded with the freeze")
        rule = json.loads(raw)
        am.check_rule(rule)
        self.assertEqual(len(rule["classes"]), 15)
        self.assertEqual(rule["endpoints"], ["seizure", "development"])

    def test_the_generator_scores_one_cell_under_the_committed_rule(self):
        with tempfile.TemporaryDirectory() as tmp:
            rule = json.loads(RULE_V1.read_text())
            row = cell("k1", "T13", "sodium_channel", endpoint="seizure", age="P13-P15")
            cells = Path(tmp) / "cells.tsv"
            cells.write_text("\t".join(HEADER) + "\n" + "\t".join(row[c] for c in HEADER) + "\n")
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                code = am.main(["score", str(cells), str(RULE_V1), "--expect-rule-sha256", RULE_V1_SHA256])
            self.assertEqual(code, 0)
            self.assertEqual(len(table(out.getvalue())), 2 * 4 * len(rule["classes"]))


class HelpIsSafe(unittest.TestCase):
    def test_help_prints_usage_and_exits_zero(self):
        with contextlib.redirect_stdout(io.StringIO()) as out, self.assertRaises(SystemExit) as stop:
            am.main(["--help"])
        self.assertEqual(stop.exception.code, 0)
        self.assertIn("usage", out.getvalue())


if __name__ == "__main__":
    unittest.main(verbosity=2)
