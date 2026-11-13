#!/usr/bin/env python3
"""HE50 item 5: the ISR list is read from the case, its count is checked against what the case declares, and no state is invented for a gene a table does not carry."""
import csv, sys, unittest
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import isr_states as st  # noqa: E402


class IsrStates(unittest.TestCase):
    def test_the_list_is_the_twelve_symbols_of_the_question_and_not_the_eleven_the_note_declares(self):
        syms, _ = st.case_symbols()
        self.assertEqual(len(syms), 12)
        self.assertEqual(len(set(syms)), 12)                                       # a range expansion that repeated a symbol would hide a miscount
        self.assertEqual(syms[:4], ["EIF2AK1", "EIF2AK2", "EIF2AK3", "EIF2AK4"])
        self.assertIn("PPP1R15B", syms)                                            # the symbol a list of eleven loses in practice

    def test_every_listed_gene_has_both_species_and_a_stated_state_and_none_is_called_neuron_enriched_by_default(self):
        syms, _ = st.case_symbols()
        rows = list(csv.DictReader(open(HERE / "isr_cell_class_states.tsv", encoding="utf-8"), delimiter="\t"))
        self.assertEqual(sorted({r["gene"] for r in rows}), sorted(syms))
        self.assertEqual({(r["gene"], r["species"]) for r in rows}, {(g, s) for g in syms for s in ("mouse", "human")})
        self.assertTrue(all(r["state"] in ("NEURON_ENRICHED", "OTHER_ENRICHED", "SHARED", "NOT_DETECTED_IN_TABLE", "NOT_IN_TABLE", "NO_NEURON_CLASS") for r in rows))
        self.assertTrue(all("NOT_IN_TABLE" != r["state"] for r in rows))           # all twelve are carried; an absent symbol would read NOT_IN_TABLE (unknown, not low)

    def test_the_replicate_counts_the_tables_state_are_the_ones_the_inputs_give(self):
        mouse = list(csv.DictReader(open(HERE / "isr_expression_mouse.tsv", encoding="utf-8"), delimiter="\t"))
        self.assertEqual({r["n_samples"] for r in mouse}, {"2"})                   # two replicate files per class: more would be an ambiguous symbol averaged
        human = list(csv.DictReader(open(HERE / "isr_expression_human.tsv", encoding="utf-8"), delimiter="\t"))
        self.assertEqual(len({(r["gene"], r["group"]) for r in human}), len(human))  # no symbol on two rows of one group


if __name__ == "__main__":
    unittest.main(verbosity=2)
