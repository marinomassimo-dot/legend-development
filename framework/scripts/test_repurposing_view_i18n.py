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


def mask(x, key=""):
    """Same structure and every number, identifier and key; free text (a label that is translated) is blanked; a dict keyed by translated file labels is compared by its values."""
    if isinstance(x, dict):
        if key == "generated_from":
            return sorted(json.dumps(v, sort_keys=True) for v in x.values())
        return {k: mask(v, k) for k, v in x.items() if k != "ui"}
    if isinstance(x, list):
        return [mask(v, key) for v in x]
    if isinstance(x, str):
        return x if re.fullmatch(r"[A-Za-z0-9_.:+/#-]{1,40}", x) and not re.fullmatch(r"[a-z]{4,}", x) else ""
    return x


def raw_kinds_left(page: str) -> list:
    """Work-order kind values (Italian enum) still in the visible text of a page. Not counted: the `data-kind` attributes (machine keys, the same in every language, like the filter ids) and the
    two authored sentences that QUOTE a value between single quotes (work-order prose of the gene-addition and premise entries: a lead for the content catalogue, not this mapping)."""
    body = re.sub(r"<script\b.*?</script>|<style\b.*?</style>", "", page, flags=re.S)
    body = html.unescape(re.sub(r'data-kind="[^"]*"', "", body))
    return [k for k in rv.WO_KINDS if re.sub(r"'" + re.escape(k) + r"'", "", body).count(k)]


def italian_ui_strings_left(page: str, lang: str) -> list:
    """Italian interface strings (UI_IT values of 14 or more characters whose translation in `lang` differs) found in the visible text of a non-Italian page, outside the passages marked as
    original-language-only. ADV-128 (2026-11-21): ten section headings, the deepened-case and pilot tables and their notes were typed in Italian in the generator, outside the catalogue, and
    only a painted-text scan saw them; a string that is in UI_IT is a string the catalogue translates, so any Italian value found on a translated page is a site that bypasses U[...]."""
    ui = json.loads((DR / "view/i18n/ui_source.json").read_text(encoding="utf-8"))
    tr = json.loads((DR / "view/i18n" / f"ui_{lang}.json").read_text(encoding="utf-8"))
    body = re.sub(r"<script\b.*?</script>|<style\b.*?</style>", "", page, flags=re.S)
    body = re.sub(r"<(\w+)\b[^>]*(?:class=\"orig\"|lang=\"it\")[^>]*>.*?</\1>", "", body, flags=re.S)
    nodes = {re.sub(r"\s+", " ", html.unescape(t)).strip() for t in re.findall(r">([^<>]+)<", body)}      # whole text nodes: a label printed raw is a node of its own; a value quoted inside an authored sentence is not
    return sorted(v for k, v in ui.items() if k.startswith("UI_IT.") and len(v) >= 14 and tr.get(k) != v and v in nodes)


@unittest.skipUnless(HAVE, "module data or translation files absent")
class InventoryIsCheckedWhereTheActorRunsIt(unittest.TestCase):
    """2026-11-12: a curated passage was edited, `i18n --what check` passed, and only the suite found the stale inventory in the battery."""

    def test_a_passage_missing_from_the_committed_inventory_fails_the_check_with_its_fix(self):
        import contextlib
        import io
        from unittest import mock
        ui = json.loads((DR / "view/i18n/ui_source.json").read_text(encoding="utf-8"))
        content = json.loads((DR / "view/i18n/content_source.json").read_text(encoding="utf-8"))
        edited = {**content, "0" * 12: {"src": "en", "text": "a passage the inventory does not hold yet"}}
        out = io.StringIO()
        with mock.patch.object(rv, "i18n_collect", return_value=(ui, edited)), contextlib.redirect_stdout(out):
            self.assertEqual(rv.i18n_check(DR), 1)
        self.assertIn("inventory STALE: view/i18n/content_source.json", out.getvalue())
        self.assertIn("i18n --what collect", out.getvalue())
        self.assertNotIn("ui_source.json differs", out.getvalue())  # the part that is current is not blamed

    def test_a_current_inventory_adds_nothing_to_the_check(self):
        import contextlib
        import io
        from unittest import mock
        ui = json.loads((DR / "view/i18n/ui_source.json").read_text(encoding="utf-8"))
        content = json.loads((DR / "view/i18n/content_source.json").read_text(encoding="utf-8"))
        out = io.StringIO()
        with mock.patch.object(rv, "i18n_collect", return_value=(ui, content)), contextlib.redirect_stdout(out):
            self.assertEqual(rv.i18n_check(DR), 0)
        self.assertNotIn("inventory STALE", out.getvalue())


class FullViewEnumsAreTranslated(unittest.TestCase):
    """The local full view is built per language too (`--source full --lang en`): the same enum must not leak there (ADV-127)."""

    def test_the_page_script_maps_the_work_order_kind_before_printing_it(self):
        """The static HTML test cannot see what the page script paints: the kind chip of the ranking and the 'next named test' paragraph are written by assets/curated.js (ADV-127 painted check:
        16 raw values at 1280 px after the Python sites were fixed). Every print of a work-order kind goes through woKind(), which reads T.wo_kind_v/c/p."""
        js = (DR / "view/assets/curated.js").read_text(encoding="utf-8")
        self.assertIn("function woKind(", js)
        self.assertEqual(re.findall(r"esc\((?:WO\[[^\]]+\]|wo)\.kind\)", js), [])
        for key in rv.KIND_KEY.values():
            self.assertIn(key, js)

    @unittest.skipUnless(HAVE, "module data or translation files absent")
    def test_no_work_order_kind_and_no_italian_interface_string_in_a_non_italian_full_build(self):
        for lg in ("en", "de"):
            page = rv.build(DR, "full", lg)
            self.assertEqual(raw_kinds_left(page), [], lg)
            self.assertEqual(italian_ui_strings_left(page, lg), [], lg)


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
        self.assertNotRegex(self.pages["en"], r"<script[^>]+\bsrc=|<link[^>]+rel=\"stylesheet\"")

    def test_other_languages_carry_the_original_language_notes(self):
        for lg in ("it", "fr", "es", "de"):
            self.assertIn('id="langnote"', self.pages[lg], lg)
            self.assertIn('class="mini mut technote"><span class="orig"', self.pages[lg], lg)
        self.assertNotIn('id="langnote"', self.pages["en"])

    def test_no_italian_interface_string_is_printed_outside_the_catalogue_on_another_page(self):
        for lg in ("en", "fr", "es", "de"):
            self.assertEqual(italian_ui_strings_left(self.pages[lg], lg), [], lg)

    def test_a_data_enum_written_in_italian_is_never_printed_raw_on_another_page(self):
        """2026-11-20 (ADV-127): the work-order kind (WO_KINDS) reached every non-Italian page as '[verificare un'ipotesi]' in 28 places, because the renderers printed the enum value and the
        catalogue check only sees interface strings. Each value has a UI key per language now; no value may appear in a non-Italian shareable build, and the Italian build still shows them."""
        for lg in ("en", "fr", "es", "de"):
            self.assertEqual(raw_kinds_left(self.pages[lg]), [], lg)
        self.assertEqual(raw_kinds_left(self.pages["it"]), list(rv.WO_KINDS))                  # the Italian page is where the values belong
        for key in rv.KIND_KEY.values():
            self.assertIn(key, rv.UI_IT)
            for lg in ("en", "fr", "es", "de"):
                self.assertNotEqual(json.loads((DR / "view/i18n" / f"ui_{lg}.json").read_text(encoding="utf-8"))["UI_IT." + key], rv.UI_IT[key], (lg, key))

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
                    if len(t) >= 25 and len(rv.IT_WORDS.findall(re.sub(r"\bIL-?\d\w*", "", t).lower())) >= 3 and len(rv.EN_WORDS.findall(t.lower())) < 2]
            self.assertEqual(left, [], lg)

    def test_a_translated_passage_is_never_shown_as_original_language_only_on_the_rendered_page(self):
        # 2026-11-18 dashboard audit: the catalogues were complete (582 of 582) and the rendered FR/ES/DE pages still carried ~23 original-language markers, because the redaction
        # formulas were localised BEFORE the lookup by hash and the text lost its identity. Pinned on the page that is produced, not on the catalogue.
        for lg in ("fr", "es", "de"):
            body = re.sub(r"<script\b.*?</script>|<style\b.*?</style>", "", self.pages[lg], flags=re.S)
            body = re.sub(r'<p class="mini mut technote">.*?</p>', "", body, flags=re.S)                 # the one intentional marker: the technical section stays in its original language
            marked = [html.unescape(re.sub(r"<[^>]+>", "", m)).strip()[:80] for m in re.findall(r'<(?:\w+)\b[^>]*class="orig"[^>]*>.*?</(?:\w+)>', body, flags=re.S)]
            self.assertEqual(marked, [], lg)

    def test_a_catalogue_translation_that_kept_an_italian_formula_gets_the_page_language_formula(self):
        # the formula is a placeholder of the shareable policy: one translation per passage, the formula localised at render time (never one translation per formula variant)
        for lg in ("fr", "es", "de"):
            body = re.sub(r"<script\b.*?</script>|<style\b.*?</style>", "", self.pages[lg], flags=re.S)
            self.assertNotIn("non incluso in questo pacchetto (", html.unescape(body), lg)
            self.assertNotIn("un registro del repository", html.unescape(body), lg)

    def test_a_passage_quoting_a_localised_formula_keeps_its_identity_for_the_lookup(self):
        saved = {k: dict(v) for k, v in rv.TRANS.items()}
        try:
            rv.load_translations(DR)
            rv.CUR["lang"] = "fr"
            allow = rv.load_allowlist(DR)                                                     # localises the formulas for the page language and records how to undo it for identity
            self.assertTrue(rv.CUR["unswap"])
            it_formula, fr_formula = rv.CUR["swaps"][0]
            source = f"An English passage that quotes {it_formula} inside a sentence."
            rv.TRANS["fr"]["content"][rv.text_hash(source)] = f"Un passage traduit qui cite {it_formula} dans une phrase."
            shown = rv.lx(source.replace(it_formula, fr_formula))                             # what the page builder hands over after the policy swap
            self.assertNotIn('class="orig"', shown)
            self.assertIn('lang="fr"', shown)
            self.assertIn(fr_formula, html.unescape(shown))                                   # the redaction formula is the page language's, the placeholder is not lost
            self.assertNotIn(it_formula, html.unescape(shown))
            del rv.TRANS["fr"]["content"][rv.text_hash(source)]
            self.assertIn('class="orig"', rv.lx(source.replace(it_formula, fr_formula)))      # no translation: still flagged, not silently passed off
        finally:
            rv.CUR["lang"] = "it"
            rv.CUR["unswap"] = []
            rv.CUR["swaps"] = []
            rv.TRANS.clear()
            rv.TRANS.update(saved)

    def test_every_freshly_built_page_passes_the_shareable_audit(self):
        # 2026-11-19: once a passage was correctly translated, the Spanish "de 105" (2 of 105 probe sets) matched the catalogue name 'DE 105' in the forbidden-name scan and refused the
        # package. The audit is not loosened; the translation avoids the adjacency. Pinned on freshly built pages (the committed editions can be stale), so the next collision of this kind
        # fails here, with the page and the name, before it blocks a package.
        import repurposing_shareable_audit as au
        for lg, page in self.pages.items():
            rep, _ = au.audit_html(page, DR)
            self.assertEqual([(v["kind"], str(v.get("value"))[:80]) for v in rep.violations], [], lg)

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
