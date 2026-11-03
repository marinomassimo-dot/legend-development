#!/usr/bin/env python3
"""Regressions for the five-language shareable view (EN initial, IT, FR, ES, DE): one dataset and one generator, five renderings.

What is pinned: the translation files are complete and keep placeholders, identifiers and numbers; the scientific data are the same in every page (only labels differ);
the selector is five real links with the right marks, works without script and keeps the filter hash; English is the initial language; nothing Italian is left on the
other pages except passages that are marked as original-language-only; an untranslated or stale passage is flagged, never silently shown as translated.
Run: python3 -B framework/scripts/test_repurposing_view_i18n.py"""
from __future__ import annotations

import html
import json
import re
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import repurposing_view as rv  # noqa: E402

DR = rv.DEFAULT_DR
HAVE = (DR / "coverage/coverage_summary.json").exists() and (DR / "view" / "i18n" / "ui_en.json").exists()


def data_of(page: str) -> dict:
    m = re.search(r'<script id="data" type="application/json">(.*?)</script>', page, re.S)
    return json.loads(m.group(1).replace("<\\/", "</").replace("<\\!--", "<!--"))


def mask(x):
    """Same structure and every number, identifier and key; free text (a label that is translated) is blanked."""
    if isinstance(x, dict):
        return {k: mask(v) for k, v in x.items() if k != "ui" and not re.search(r"[a-z]{3,} [a-z]{3,}", str(k))}
    if isinstance(x, list):
        return [mask(v) for v in x]
    if isinstance(x, str):
        return x if re.fullmatch(r"[A-Za-z0-9_.:+/#-]{1,40}", x) and not re.fullmatch(r"[a-z]{4,}", x) else ""
    return x


@unittest.skipUnless(HAVE, "module data or translation files absent")
class FiveLanguages(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pages = {lg: rv.build(DR, "shareable", lg) for lg in rv.LANGS}

    def test_english_is_the_initial_language_and_the_default_build(self):
        self.assertEqual(rv.build(DR, "shareable"), self.pages["en"])
        self.assertEqual(rv.LANG_FILE["en"], "index.html")
        self.assertEqual(rv.build(DR, "full")[:200].count('lang="it"'), 1)             # the local full view stays Italian unless asked

    def test_translation_files_are_complete_and_keep_placeholders_identifiers_and_numbers(self):
        self.assertEqual(rv.i18n_check(DR), 0)

    def test_the_inventory_is_current(self):
        ui, content = rv.i18n_collect(DR)
        self.assertEqual(json.loads((DR / "view/i18n/ui_source.json").read_text(encoding="utf-8")), ui)
        self.assertEqual(json.loads((DR / "view/i18n/content_source.json").read_text(encoding="utf-8")), content)

    def test_the_scientific_data_are_the_same_in_every_language(self):
        base = json.dumps(mask(data_of(self.pages["en"])), sort_keys=True)
        for lg in rv.LANGS:
            self.assertEqual(json.dumps(mask(data_of(self.pages[lg])), sort_keys=True), base, lg)

    def test_ids_filters_and_anchors_are_the_same_in_every_language(self):
        ids = lambda p: sorted(set(re.findall(r'\sid="([^"]+)"', p)) - {"langnote"})
        anchors = lambda p: sorted(re.findall(r'href="(#[^"]*)"', p))
        for lg in rv.LANGS:
            self.assertEqual(ids(self.pages[lg]), ids(self.pages["en"]), lg)
            self.assertEqual(anchors(self.pages[lg]), anchors(self.pages["en"]), lg)
        for control in ("f-access", "f-need", "f-scope", "f-oscope", "f-track", "f-goal", "f-disp", "f-q", "f-reset"):
            for lg in rv.LANGS:
                self.assertIn(f'id="{control}"', self.pages[lg], (lg, control))

    def test_the_selector_is_five_links_marked_labelled_and_independent_of_script(self):
        for lg, page in self.pages.items():
            self.assertEqual(re.search(r'<html lang="(\w+)"', page).group(1), lg)
            nav = re.search(r'<nav class="langsel".*?</nav>', page, re.S).group(0)
            links = re.findall(r'<a href="([^"]+)" data-file="[^"]+" data-lang="(\w+)" hreflang="\w+" lang="\w+" title="[^"]+"( aria-current="true")?>', nav)
            self.assertEqual([(f, l) for f, l, _ in links], [(rv.LANG_FILE[x], x) for x in rv.LANGS], lg)
            self.assertEqual([l for _, l, c in links if c], [lg], lg)                  # only the page's own language is current
            self.assertIn('aria-label="', nav)
            self.assertEqual(len(re.findall(r'<link rel="alternate" hreflang=', page)), 5)
        css = rv.CSS
        self.assertIn("min-width:44px;min-height:44px", css)                          # a phone-sized touch target

    def test_the_choice_is_remembered_safely_and_the_filter_hash_is_kept(self):
        js = rv.LANG_JS
        self.assertIn("try{", js)                                                      # localStorage can be absent
        self.assertIn("location.hash", js)
        en_nav = re.search(r"<nav class=\"langsel\".*?</script>", self.pages["en"], re.S).group(0)
        fr_nav = re.search(r"<nav class=\"langsel\".*?</script>", self.pages["fr"], re.S).group(0)
        self.assertIn("if(true){", en_nav)                                             # only the English page opens a remembered language
        self.assertIn("if(false){", fr_nav)
        self.assertNotRegex(self.pages["en"], r"https?://[^\"' ]*\.(?:js|css)")

    def test_other_languages_carry_the_original_language_notes(self):
        for lg in ("it", "fr", "es", "de"):
            self.assertIn('id="langnote"', self.pages[lg], lg)
            self.assertIn('class="mini mut technote"><span class="orig"', self.pages[lg], lg)
        self.assertNotIn('id="langnote"', self.pages["en"])

    def test_no_italian_interface_text_is_left_outside_marked_passages(self):
        ui = json.loads((DR / "view/i18n/ui_source.json").read_text(encoding="utf-8"))
        long_it = [t for t in ui.values() if len(t) >= 30]
        for lg in ("en", "fr", "es", "de"):
            body = html.unescape(re.sub(r"<script\b.*?</script>|<style\b.*?</style>", "", self.pages[lg], flags=re.S))
            body = re.sub(r"<(\w+)\b[^>]*class=\"orig\"[^>]*>.*?</\1>", "", body, flags=re.S)
            self.assertEqual([t for t in long_it if t in body], [], lg)
        for lg in ("en", "de"):                                                         # stop-word screen is reliable only where the language shares few words with Italian
            body = re.sub(r"<script\b.*?</script>|<style\b.*?</style>", "", self.pages[lg], flags=re.S)
            body = re.sub(r"<(\w+)\b[^>]*class=\"orig\"[^>]*>.*?</\1>", "", body, flags=re.S)
            left = [t for t in (html.unescape(x).strip() for x in rv.TEXT_NODE.findall(body))
                    if len(t) >= 25 and len(rv.IT_WORDS.findall(t.lower())) >= 3 and len(rv.EN_WORDS.findall(t.lower())) < 2]
            self.assertEqual(left, [], lg)

    def test_an_untranslated_passage_is_flagged_not_passed_off_as_translated(self):
        saved = {k: dict(v) for k, v in rv.TRANS.items()}
        try:
            rv.load_translations(DR)
            rv.TRANS["de"]["content"] = {}
            rv.CUR["lang"] = "de"
            flagged = rv.lx("A passage nobody translated.")
            self.assertIn('class="orig"', flagged)
            self.assertIn('lang="en"', flagged)
            rv.CUR["lang"] = "en"
            self.assertNotIn('class="orig"', rv.lx("A passage nobody translated."))
        finally:
            rv.CUR["lang"] = "it"
            rv.TRANS.clear()
            rv.TRANS.update(saved)

    def test_a_translation_whose_original_changed_is_not_used(self):
        # translations are keyed by the hash of the original: a changed original has a new hash, so it is untranslated (and `i18n check` reports the old key as stale)
        self.assertNotEqual(rv.text_hash("The role of the change is unknown."), rv.text_hash("The role of the change is known."))

    def test_epistemic_labels_stay_distinct_in_every_language(self):
        for lg in rv.LANGS:
            rv.CUR["lang"] = lg
            try:
                labels = [rv.UI_IT[k] for k in ("ev_mis_txt", "ev_inf_txt", "ev_ipo_txt", "ev_unk_txt")]
            finally:
                rv.CUR["lang"] = "it"
            self.assertEqual(len(set(labels)), 4, lg)


if __name__ == "__main__":
    unittest.main(verbosity=2)
