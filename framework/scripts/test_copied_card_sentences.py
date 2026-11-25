#!/usr/bin/env python3
"""Regressions for copied_card_sentences.py: a card sentence that changed and is still held by a copy."""
from __future__ import annotations
import json, subprocess, sys, unittest
from pathlib import Path
from tempfile import TemporaryDirectory

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import copied_card_sentences as copies  # noqa: E402

DR = "disease-models/wwox/research/drug_repurposing"
CARD = f"{DR}/cards/E04_ketogenic_lactate_axis.card.json"
TABLE = f"{DR}/ranking_it8_p9_20261029/investigations.tsv"
PAGE = f"{DR}/view/index.en.html"
# The case of 2026-11-25, from the history of the repository (card change 0abb8243e): the card gained a qualifier, the table kept the old text.
OLD = ("A ketogenic-diet response is reported in 3 of 5 WOREE individuals (lactate 2.4 to 3.3 mmol/L in one individual); the Pdk1 transcript "
       "and serum-lactate datum in the Wwox-null MEF and mouse paper is non-neural and measures no PDH.")
NEW = ("A ketogenic-diet response is reported in 3 of 5 WOREE individuals (lactate 2.4 to 3.3 mmol/L in one individual; registry statement, "
       "no held source passage, ADV-259); the Pdk1 transcript and serum-lactate datum in the Wwox-null MEF and mouse paper is non-neural and measures no PDH.")
LEAD = "A regulator-level inflammatory signature is positive in three forebrain regions of the homozygous animals."
ADDED = "Without two of the five mutant animals one of the three regions no longer meets the threshold (a post hoc check)."


class CopiedSentences(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.git("init", "-q")
        self.git("config", "user.email", "fixture" + "@" + "invalid")
        self.git("config", "user.name", "t")

    def git(self, *args: str) -> str:
        return subprocess.run(["git", "-C", str(self.root), *args], check=True, capture_output=True, text=True).stdout.strip()

    def write(self, files: dict) -> str:
        for rel, text in files.items():
            path = self.root / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
        self.git("add", "-A")
        self.git("commit", "-qm", "c", "--allow-empty")
        return self.git("rev-parse", "HEAD")

    @staticmethod
    def card(*sentences: str) -> str:
        return json.dumps({"input": {"not_known": list(sentences)}})

    @staticmethod
    def page(*items: str) -> str:
        return "<script>const DATA=" + json.dumps({"items": list(items)}).replace("<", "\\u003c") + ";</script>\n"

    def run_check(self, before: dict, after: dict):
        base = self.write(before)
        self.write(after)
        return copies.find(self.root, base)

    def test_the_ketogenic_case_names_the_files_the_card_and_the_exact_old_text(self) -> None:
        row = "4\t" + OLD + "\tE3\n"
        findings, _ = self.run_check({CARD: self.card(OLD), TABLE: row, PAGE: self.page(OLD)}, {CARD: self.card(NEW), PAGE: self.page(NEW, OLD)})
        self.assertEqual(findings, [{"card": CARD, "old": OLD, "files": [TABLE, PAGE]}])
        done = subprocess.run([sys.executable, str(HERE / "copied_card_sentences.py"), "--repo", str(self.root), "--base", "HEAD~1"], capture_output=True, text=True)
        self.assertEqual(done.returncode, 1, done.stderr)
        for expected in (CARD, TABLE, "old text: " + OLD):
            self.assertIn(expected, done.stdout)

    def test_every_copy_rebuilt_or_edited_passes(self) -> None:
        findings, counts = self.run_check({CARD: self.card(OLD), TABLE: OLD + "\n", PAGE: self.page(OLD)},
                                          {CARD: self.card(NEW), TABLE: NEW + "\n", PAGE: self.page(NEW)})
        self.assertEqual((findings, counts["cards_changed"]), ([], 1))

    def test_a_qualifier_appended_at_the_end_is_missed_by_no_copy_that_lacks_it(self) -> None:
        findings, _ = self.run_check({CARD: self.card(LEAD), TABLE: LEAD + "\n"}, {CARD: self.card(LEAD + " " + ADDED)})
        self.assertEqual([(f["old"], f["files"]) for f in findings], [(LEAD, [TABLE])])

    @staticmethod
    def cut_page(shown: str, **flag) -> str:
        return "<script>const DATA=" + json.dumps({"pharm": shown, **flag, "pmids": []}, separators=(",", ":"), ensure_ascii=False) + ";</script>\n"

    def test_a_marked_cut_of_the_new_string_is_not_behind(self) -> None:
        """The shareable edition prints the first 360 characters and flags the cut; ranking.json ends a clip with an ellipsis."""
        new = LEAD + " " + ADDED
        ranking = f"{DR}/ranking_it8_p9_20261029/ranking.json"
        for name, files in (("flag", {PAGE: self.cut_page(LEAD, pharm_cut=True)}),
                            ("ellipsis in the addition", {ranking: json.dumps({"p": new[:len(LEAD) + 8] + "\u2026"})}),
                            ("ellipsis at the old end", {ranking: json.dumps({"p": LEAD + "\u2026"})})):
            with self.subTest(name):
                self.assertEqual(self.run_check({CARD: self.card(LEAD)}, {CARD: self.card(new), **files})[0], [])

    def test_a_cut_page_that_was_not_rebuilt_or_cuts_another_text_is_behind(self) -> None:
        for name, new, page in (("whole old text, no flag", LEAD + " " + ADDED, self.cut_page(LEAD)),
                                ("the new string starts otherwise", "A narrowing first sentence stands before it now. " + LEAD, self.cut_page(LEAD, pharm_cut=True))):
            with self.subTest(name):
                findings, _ = self.run_check({CARD: self.card(LEAD), PAGE: page}, {CARD: self.card(new)})
                self.assertEqual([(f["old"], f["files"]) for f in findings], [(LEAD, [PAGE])])

    def test_a_page_that_shows_the_new_string_in_parts_is_not_behind(self) -> None:
        findings, _ = self.run_check({CARD: self.card(LEAD), PAGE: self.page(LEAD)}, {CARD: self.card(LEAD + " " + ADDED), PAGE: self.page(LEAD, ADDED)})
        self.assertEqual(findings, [])

    def test_a_short_qualifier_is_missing_from_a_copy_that_lacks_it_and_present_in_one_that_has_it(self) -> None:
        new = LEAD + " (one animal)."
        findings, _ = self.run_check({CARD: self.card(LEAD), TABLE: LEAD + "\n", PAGE: self.page(LEAD)}, {CARD: self.card(new), PAGE: self.page(new)})
        self.assertEqual([f["files"] for f in findings], [[TABLE]])

    def test_quotation_marks_in_a_page_do_not_hide_a_stale_sentence(self) -> None:
        old = 'The authors call the change "partial correction" although neither dose reaches significance against the untreated animals.'
        findings, _ = self.run_check({CARD: self.card(old), PAGE: self.page(old)}, {CARD: self.card(ADDED)})
        self.assertEqual([f["files"] for f in findings], [[PAGE]])

    def test_a_clipped_start_of_a_replaced_string_is_found(self) -> None:
        old = ("The reading of the transport panel rests on a cell line that does not express the channel in question and therefore says nothing "
               "about the neuron; the second panel, run in a primary culture of cortical neurons at one concentration only, was not repeated by anyone.")
        new = old.replace("does not express", "weakly expresses")
        findings, _ = self.run_check({CARD: self.card(old), TABLE: old[:copies.CLIP] + "...\n"}, {CARD: self.card(new)})
        self.assertEqual([f["files"] for f in findings], [[TABLE]])

    def test_a_short_common_string_is_never_a_finding(self) -> None:
        short = "abstract only; not read"
        findings, _ = self.run_check({CARD: self.card(short), TABLE: short + "\n", PAGE: self.page(short, short)}, {CARD: self.card("full text read")})
        self.assertEqual(findings, [])

    def test_a_text_another_card_still_holds_is_not_old(self) -> None:
        other = f"{DR}/cards/E02_ldh_inhibition.card.json"
        findings, _ = self.run_check({CARD: self.card(LEAD), other: self.card(LEAD), TABLE: LEAD + "\n"}, {CARD: self.card(ADDED)})
        self.assertEqual(findings, [])

    def test_a_change_without_a_card_reads_no_surface(self) -> None:
        findings, counts = self.run_check({CARD: self.card(OLD), TABLE: "x\n"}, {TABLE: OLD + "\n"})
        self.assertEqual((findings, counts), ([], {"cards_changed": 0, "surfaces": 0, "old_texts": 0}))

    def test_a_check_that_cannot_run_exits_3(self) -> None:
        self.write({CARD: self.card(OLD)})
        done = subprocess.run([sys.executable, str(HERE / "copied_card_sentences.py"), "--repo", str(self.root), "--base", "no-such-rev"], capture_output=True, text=True)
        self.assertEqual(done.returncode, 3)
        self.assertIn("COPIED_CARD_SENTENCES_ERROR", done.stderr)


if __name__ == "__main__":
    unittest.main(verbosity=2)
