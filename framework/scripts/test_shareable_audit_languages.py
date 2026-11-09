#!/usr/bin/env python3
"""IT38: a translated page is not refused for a word of its own language that coincides with a catalogue compound name, but only when that word is verifiably in the repository's
authorised translation of that language; a name typed into the visible HTML, a row or an identifier is still refused, in every language."""
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace

sys.path.insert(0, str(Path(__file__).resolve().parent))
import repurposing_shareable_audit as au  # noqa: E402


def ref():
    return SimpleNamespace(names={"casa": "CAT:A", "nada": "CAT:B", "memantina": "CAT:E", "tiratricol": "CAT:T", "zd7288": "CAT:D", "memantine": "CAT:M", "casa blanca": "CAT:G"},
                           texts={}, ident={}, own_grams=set(), titles=set(), journals=set())


def dr_with(lang="es", translation="libre de crisis en casa; no dice nada; la memantina"):
    d = Path(tempfile.mkdtemp())
    (d / "view" / "i18n").mkdir(parents=True)
    (d / "view" / "i18n" / f"content_{lang}.json").write_text(json.dumps({"k": {"text": translation}}), encoding="utf-8")
    (d / "view" / "i18n" / "content_source.json").write_text(json.dumps({"k": {"text": "seizure-free at home; says nothing; memantine"}}), encoding="utf-8")
    return d


def run(items, excuse):
    rep = au.Report()
    au.scan_strings(items, ref(), rep, "page", excuse)
    return rep


P_NEUTRAL = {"source": "shareable", "rows": [{"name": "Tiratricol-free row"}], "ui": {"u": "casa"}, "strings": []}


class VerifiableTranslationWords(unittest.TestCase):
    def setUp(self):
        self.ex = au.translation_excuse(dr_with(), P_NEUTRAL, "es")

    def test_everyday_words_present_in_the_authorised_translation_are_not_names(self):
        for text in ("libre de crisis en casa", "no dice nada", "la memantina"):
            rep = run([("p", text)], self.ex)
            self.assertTrue(rep.ok, (text, rep.violations))

    def test_reproduced_without_the_rule_the_same_text_is_refused(self):
        self.assertFalse(run([("p", "libre de crisis en casa")], None).ok)

    def test_a_name_typed_into_the_visible_html_is_refused_in_a_translated_page(self):
        for text in ("el brazo recibe tiratricol", "con ZD7288 a 50 uM"):
            rep = run([("p", text)], self.ex)
            self.assertFalse(rep.ok, text)
            self.assertIn("forbidden-name", {v["kind"] for v in rep.violations})

    def test_a_word_that_is_in_the_neutral_data_of_the_page_is_not_excused(self):
        ex = au.translation_excuse(dr_with(translation="el tiratricol aparece aqui"), P_NEUTRAL, "es")      # even if a translation file carried it, a row name is data, not translation
        self.assertFalse(run([("p", "tiratricol")], ex).ok)

    def test_a_word_in_the_english_source_is_not_excused(self):
        ex = au.translation_excuse(dr_with(translation="memantine en la traduccion"), P_NEUTRAL, "es")
        self.assertFalse(run([("p", "memantine")], ex).ok)

    def test_an_identifier_and_a_multi_word_name_are_never_excused(self):
        ex = au.translation_excuse(dr_with(translation="zd7288 casa blanca"), P_NEUTRAL, "es")
        self.assertFalse(run([("p", "zd7288")], ex).ok)
        self.assertFalse(run([("p", "casa blanca")], ex).ok)

    def test_an_english_page_has_no_exemption_and_the_language_is_read_from_the_page(self):
        self.assertIsNone(au.translation_excuse(dr_with(), P_NEUTRAL, "en"))
        self.assertEqual(au.PAGE_LANG_RX.search('<html lang="es">').group(1), "es")

    def test_the_same_function_serves_data_page_and_rendered_surfaces(self):
        for label in ("data", "page", "rendered"):
            rep = au.Report()
            au.scan_strings([("p", "libre de crisis en casa")], ref(), rep, label, self.ex)
            self.assertTrue(rep.ok, label)
            rep = au.Report()
            au.scan_strings([("p", "recibe tiratricol")], ref(), rep, label, self.ex)
            self.assertFalse(rep.ok, label)


DR = Path(__file__).resolve().parents[2] / "disease-models/wwox/research/drug_repurposing"


@unittest.skipUnless(__import__("os").environ.get("LEGEND_CATALOG_CACHE") and (DR / "view/index_shareable.es.html").exists(), "needs the local catalogue cache and the built editions")
class RealEditions(unittest.TestCase):
    """The committed shareable editions: legitimate translated text passes; a name typed into the VISIBLE HTML (outside the embedded data) is caught in every language, English included."""

    @classmethod
    def setUpClass(cls):
        cls.ref = au.Reference(DR)

    def page(self, lang):
        name = "index_shareable.html" if lang == "en" else f"index_shareable.{lang}.html"
        return (DR / "view" / name).read_text(encoding="utf-8")

    def test_each_edition_passes_and_a_visible_insertion_is_refused_in_each(self):
        for lang in ("en", "it", "fr", "es", "de"):
            text = self.page(lang)
            rep, _ = au.audit_html(text, DR, self.ref)
            self.assertEqual([v for v in rep.violations if v["kind"] == "forbidden-name"], [], lang)
            mutated = text.replace("</body>", "<p>El brazo recibe tiratricol en cultivo.</p></body>", 1)
            rep2, _ = au.audit_html(mutated, DR, self.ref)
            self.assertIn("forbidden-name", {v["kind"] for v in rep2.violations}, lang)


if __name__ == "__main__":
    unittest.main(verbosity=2)
