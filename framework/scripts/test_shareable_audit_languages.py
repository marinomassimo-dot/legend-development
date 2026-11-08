#!/usr/bin/env python3
"""IT38: a translated page is not refused for a word of its own language that coincides with a catalogue compound name; a name the audited English source contains still is."""
from __future__ import annotations

import sys
import unittest
from pathlib import Path
from types import SimpleNamespace

sys.path.insert(0, str(Path(__file__).resolve().parent))
import repurposing_shareable_audit as au  # noqa: E402


def ref():
    return SimpleNamespace(names={"casa": "CAT:A", "nada": "CAT:B", "neuer": "CAT:C", "zd7288": "CAT:D", "memantine": "CAT:E", "hormones": "CAT:F", "casa blanca": "CAT:G"},
                           texts={}, ident={}, own_grams=set(), titles=set(), journals=set())


def run(items, vocab):
    rep = au.Report()
    au.scan_strings(items, ref(), rep, "page", vocab)
    return rep


SRC = au.tokens("The tool compound ZD7288 is named once in the English source. Memantine arm.")        # what the audited English page contains
VOCAB = set(SRC)


class SourceGrounded(unittest.TestCase):
    def test_everyday_words_of_the_target_language_are_not_names(self):
        for text in ("libre de crisis en casa mientras", "no dice nada sobre las neuronas", "ist ein neuer Strang", "la teneur en hormones du milieu"):
            rep = run([("p", text)], VOCAB)
            self.assertTrue(rep.ok, (text, rep.violations))
        self.assertGreaterEqual(rep.suppressed["a single word of the page's language that the audited English source does not contain"], 1)

    def test_reproduced_without_the_rule_the_same_text_is_refused(self):
        rep = run([("p", "libre de crisis en casa mientras")], None)
        self.assertFalse(rep.ok)

    def test_positive_control_a_name_the_source_contains_is_still_refused_in_any_language(self):
        for text in ("el brazo con ZD7288 a 50 uM", "un bras avec memantine", "Der Arm mit ZD7288"):
            rep = run([("p", text)], VOCAB)
            self.assertFalse(rep.ok, text)
            self.assertIn("forbidden-name", {v["kind"] for v in rep.violations})

    def test_a_multi_word_name_is_never_excused_by_the_rule(self):
        rep = run([("p", "visita a casa blanca")], VOCAB)
        self.assertFalse(rep.ok)

    def test_the_vocabulary_is_built_from_the_pages_own_strings(self):
        html = '<html><body><script id="data" type="application/json">{"source": "shareable"}</script><p>Tool compound ZD7288</p></body></html>'
        self.assertIn("zd7288", au.source_vocabulary(html))


if __name__ == "__main__":
    unittest.main(verbosity=2)
