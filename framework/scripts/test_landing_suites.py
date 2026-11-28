#!/usr/bin/env python3
"""Tests for landing_suites.py: which suites each kind of changed path selects, what the change is measured against, and that the tool only prints."""
from __future__ import annotations

import io
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import landing_suites as ls  # noqa: E402

REPO = Path(__file__).resolve().parents[2]


def names(changed):
    return {Path(s).name for s in ls.select(changed, REPO)}


class Selection(unittest.TestCase):
    def test_every_rule_names_a_suite_that_exists_here(self) -> None:
        self.assertEqual([], [suite for suite, _ in ls.RULES if not (REPO / suite.split()[0]).is_file()])

    def test_a_new_script_selects_the_command_routing_and_isolation_suites(self) -> None:
        self.assertEqual({"test_release_surface.py", "test_documented_commands.py", "test_tool_routing.py", "test_strategic_advisor.py"}, names([("A", "framework/scripts/new_tool.py")]))

    def test_a_test_file_change_selects_the_closed_world_guard(self) -> None:
        guard = "test_no_closed_world_assertions_on_live_state.py"
        for scope in ("framework/scripts", "scripts", "disease-models/wwox/analysis/scripts"):
            self.assertIn(guard, names([("M", f"{scope}/test_something.py")]), scope)
        self.assertNotIn(guard, names([("M", "framework/scripts/something.py")]))

    def test_a_registry_change_selects_the_queue_and_the_pathograph(self) -> None:
        got = names([("M", "disease-models/wwox/registries/paper_registry_current.md")])
        self.assertLessEqual({"test_batch_queue.py", "test_pathograph.py", "test_documented_commands.py", "test_link_targets.py"}, got)
        self.assertNotIn("test_coverage_report.py", got)

    def test_a_claim_or_paper_registry_change_selects_the_suites_that_assert_on_it(self) -> None:
        for registry in ("claim_registry_current.md", "paper_registry_current.md"):
            got = names([("M", f"disease-models/wwox/registries/{registry}")])
            self.assertLessEqual({"test_trace_claim_foundation.py", "test_growth_anchors.py", "test_generate_semantic_graph.py", "test_build_evidence_index.py",
                                  "test_dependency_integrity.py", "test_locator_count_crosscheck.py", "test_canonical_structure.py", "test_dismech_independent_protocol.py"}, got, registry)

    def test_each_input_of_the_dismech_sidecar_selects_its_reproduction_test(self) -> None:
        wanted = "test_derive_dismech_sidecar.py SerialisationTests.test_committed_sidecar_reproduces_byte_for_byte"
        for path in ("registries/claim_registry_current.md", "registries/paper_registry_current.md", "registries/fulltext_read_receipts.jsonl",
                     "analysis/data/dismech_authored_assertions.json"):
            self.assertIn(wanted, names([("M", f"disease-models/wwox/{path}")]), path)

    def test_a_receipt_selects_the_two_derived_pages(self) -> None:
        got = names([("M", "disease-models/wwox/registries/fulltext_read_receipts.jsonl")])
        self.assertLessEqual({"test_coverage_report.py", "test_reading_state.py", "test_structured_data_integrity.py"}, got)

    def test_a_table_selects_the_integrity_suite_only_among_the_document_suites(self) -> None:
        got = names([("A", "disease-models/wwox/research/x/table.tsv")])
        self.assertEqual({"test_release_surface.py", "test_structured_data_integrity.py"}, got)

    def test_a_card_change_selects_its_copy_suite_and_the_title_class(self) -> None:
        got = ls.select([("M", "disease-models/wwox/research/drug_repurposing/cards_early/EB-X-01.card.json")], REPO)
        self.assertIn("framework/scripts/test_repurposing_view.py Titles", got)
        self.assertTrue(any(suite.endswith("test_cards_early_it13_p22.py") for suite in got), got)
        self.assertNotIn("framework/scripts/test_repurposing_view.py", got)
        self.assertIn("python3 -B framework/scripts/test_repurposing_view.py Titles < /dev/null", ls.command_for(got))

    def test_a_card_or_packet_change_selects_the_checker_of_its_own_folder(self) -> None:
        """A change made of .json files only selects no document suite, so a unit value in card text would reach main unchecked."""
        base = "disease-models/wwox/research/drug_repurposing"
        for folder, other in (("cards", "cards_early"), ("cards_early", "cards")):
            for kind in ("packet", "card"):
                got = ls.select([("M", f"{base}/{folder}/X-01.{kind}.json")], REPO)
                self.assertIn(f"{base}/{folder}/check_cards.py", got, (folder, kind))
                self.assertNotIn(f"{base}/{other}/check_cards.py", got, (folder, kind))
        bridge = ls.select([("M", "framework/scripts/repurposing_bridge.py")], REPO)      # the checkers compare stored cards with what the bridge builds
        self.assertLessEqual({f"{base}/cards/check_cards.py", f"{base}/cards_early/check_cards.py"}, set(bridge))

    def test_a_title_cache_change_selects_the_title_class_and_not_the_long_view_suite(self) -> None:
        got = ls.select([("M", "disease-models/wwox/research/drug_repurposing/view/source_titles.json")], REPO)
        self.assertIn("framework/scripts/test_repurposing_view.py Titles", got)
        self.assertNotIn("framework/scripts/test_repurposing_view.py", got)

    def test_a_needs_change_selects_the_freshness_and_ranking_suites(self) -> None:
        got = names([("M", "disease-models/wwox/research/drug_repurposing/needs/needs.json")])
        self.assertLessEqual({"test_candidate_tree_freshness.py", "test_ranking_it8.py"}, got)

    def test_a_current_file_outside_the_registries_selects_the_batch_queue(self) -> None:
        got = names([("M", "disease-models/wwox/research/discovery_ledger_current.md")])
        self.assertIn("test_batch_queue.py", got)
        self.assertNotIn("test_batch_queue.py", names([("M", "disease-models/wwox/research/notes.md")]))

    def test_a_mechanism_map_change_selects_only_the_curated_link_class_of_the_join(self) -> None:
        got = ls.select([("M", "disease-models/wwox/analysis/mechanism_intervention_map.md")], REPO)
        self.assertIn("framework/scripts/test_repurposing_join.py CuratedLink", got)
        self.assertNotIn("framework/scripts/test_repurposing_join.py", got)

    def test_a_path_no_rule_knows_selects_nothing(self) -> None:
        self.assertEqual(set(), names([("M", "disease-models/wwox/research/x/notes.txt")]))

    def test_a_suite_added_under_a_research_folder_is_named_itself_and_a_deleted_one_is_not(self) -> None:
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            suite = "disease-models/wwox/research/pkg/test_wwox.py"
            (root / suite).parent.mkdir(parents=True)
            (root / suite).write_text("", encoding="utf-8")
            self.assertEqual([suite], ls.select([("A", suite)], root))
            self.assertEqual([], ls.select([("D", suite)], root))


class TheChangeAndTheOutput(unittest.TestCase):
    def setUp(self) -> None:
        self.folder = tempfile.TemporaryDirectory()
        self.root = Path(self.folder.name)
        self.git("init", "-q", "-b", "main")
        self.commit("scripts/test_structured_data_integrity.py", "")
        self.git("checkout", "-q", "-b", "task")
        self.commit("data/mine.tsv", "a\tb\n")
        self.git("checkout", "-q", "main")
        self.commit("data/theirs.md", "x\n")
        self.git("checkout", "-q", "task")

    def tearDown(self) -> None:
        self.folder.cleanup()

    def git(self, *args: str) -> None:
        subprocess.run(["git", "-C", str(self.root), "-c", "user.name=t", "-c", "user.email=t", "-c", "commit.gpgsign=false", *args], check=True, capture_output=True)

    def commit(self, path: str, text: str) -> None:
        (self.root / path).parent.mkdir(parents=True, exist_ok=True)
        (self.root / path).write_text(text, encoding="utf-8")
        self.git("add", path)
        self.git("commit", "-q", "-m", path)

    def run_tool(self, *args: str) -> tuple[int, str]:
        out = io.StringIO()
        with redirect_stdout(out):
            code = ls.main(["--repo", str(self.root), *args])
        return code, out.getvalue()

    def test_only_the_branchs_own_commits_are_judged_not_what_others_landed(self) -> None:
        self.assertEqual([("A", "data/mine.tsv")], ls.changes(self.root, "main"))

    def test_it_prints_the_suites_and_one_command_and_exits_zero(self) -> None:
        code, text = self.run_tool("--base", "main")
        self.assertEqual(0, code)
        self.assertIn("1 suite(s) selected, none run", text)
        self.assertIn("run them: python3 -B scripts/test_structured_data_integrity.py < /dev/null", text)

    def test_it_writes_nothing(self) -> None:
        before = sorted(p.relative_to(self.root).as_posix() for p in self.root.rglob("*") if ".git" not in p.parts)
        self.run_tool("--base", "main")
        self.assertEqual(before, sorted(p.relative_to(self.root).as_posix() for p in self.root.rglob("*") if ".git" not in p.parts))

    def test_a_base_that_does_not_exist_is_refused(self) -> None:
        code, text = self.run_tool("--base", "no/such-branch")
        self.assertEqual(2, code)
        self.assertIn("REFUSED", text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
