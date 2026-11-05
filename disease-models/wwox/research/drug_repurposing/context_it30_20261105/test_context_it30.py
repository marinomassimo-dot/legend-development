#!/usr/bin/env python3
"""IT30: invariants of the compound-context adapter. Offline. Usage: test_context_it30.py (runs the checks; any argument prints this text)."""
import sys
if len(sys.argv) > 1:
    print(__doc__); raise SystemExit(0)
import csv, importlib.util, tempfile, unittest
from pathlib import Path
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("cc", HERE / "compound_context_it30.py")
cc = importlib.util.module_from_spec(spec); spec.loader.exec_module(cc)
COLS = ["row_id", "endpoint", "intervention", "intervention_type", "action_on_target", "target_symbol", "system", "cell_type_or_stage", "stress_or_context",
        "control", "direction_on_endpoint", "effect_note", "measure_level", "attribution", "composition_or_autonomous", "source_id", "source_depth", "locator_quote",
        "transfer_conditions", "transfer_breakers"]


def make(rows):
    d = tempfile.mkdtemp()
    with open(Path(d) / "evidence_it29_D.tsv", "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=COLS, delimiter="\t", lineterminator="\n"); w.writeheader()
        for i, (name, direction, system) in enumerate(rows, 1):
            r = {c: "" for c in COLS}
            r.update(row_id=f"X{i:02d}", intervention=name, intervention_type="compound", direction_on_endpoint=direction, system=system,
                     attribution="compound_only", source_id=f"PMID{i}", target_symbol="")
            w.writerow(r)
    return str(Path(d) / "evidence_it29_D.tsv")


def run(rows):
    f = make(rows)
    cc.DR = Path(f).parent.parent  # glob is joined to DR; use an absolute pattern below
    single, panel = cc.build(f)
    return cc.summarise(single), panel


class T(unittest.TestCase):
    def test_a_sign_that_flips_with_context_is_flagged_and_names_both_contexts(self):
        s, _ = run([("drugx", "favourable", "model A"), ("drugx", "adverse", "model B")])
        self.assertEqual(s[0]["conflict"], "sign_flips_with_context")
        q = cc.question(s[0])
        self.assertIn("model A", q); self.assertIn("model B", q); self.assertIn("no class transfer", q)

    def test_a_combination_or_a_class_is_never_split_into_compounds(self):
        s, panel = run([("drugx + drugy", "favourable", "m"), ("drugx, drugy", "favourable", "m"), ("five H1 antagonists", "null", "m"), ("drugx versus drugy", "null", "m")])
        self.assertEqual(s, []); self.assertEqual(len(panel), 4)

    def test_unknown_is_not_turned_into_a_conflict_or_a_negative(self):
        s, _ = run([("drugx", "undetermined", "m1"), ("drugx", "undetermined", "m2")])
        self.assertEqual(s[0]["conflict"], "no_conflict_recorded")

    def test_the_output_carries_no_target_and_no_class(self):
        s, _ = run([("drugx", "favourable", "m")])
        self.assertFalse({"target", "target_symbol", "class", "main_target"} & set(s[0]))

    def test_on_the_committed_evidence_both_cases_yield_conditional_questions(self):
        with open(HERE / "results/conditional_questions_it30.tsv", encoding="utf-8") as fh:
            qs = list(csv.DictReader(fh, delimiter="\t"))
        self.assertTrue(any("myelination" in q["theme"] for q in qs))
        self.assertTrue(any("epilepsy" in q["theme"] for q in qs))
        for q in qs:
            self.assertTrue(q["evidence_rows"])
        cls = [q for q in qs if q["conflict"] == "sign_flips_with_lesion_class"]
        self.assertEqual({q["compound"] for q in cls}, {"sodium_channel_blocker (class level)", "gaba_transaminase_inhibitor (class level)", "kv7_opener (class level)"})
        for q in cls:
            self.assertIn("no transfer to a named compound", q["question"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
