#!/usr/bin/env python3
"""Regression tests for phenotypic_neighbors.py (synthetic ontology only)."""

from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("phenotypic_neighbors.py")
SPEC = importlib.util.spec_from_file_location("phenotypic_neighbors", MODULE_PATH)
assert SPEC and SPEC.loader
PN = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = PN
SPEC.loader.exec_module(PN)


# A tiny is_a tree:  HP:0000001 (root)
#                      └ HP:0000100 (neuro)
#                          ├ HP:0000110 (seizure)
#                          │   └ HP:0000111 (focal seizure, rare/specific)
#                          └ HP:0000120 (developmental delay)
MINI_OBO = """
[Term]
id: HP:0000001
name: root

[Term]
id: HP:0000100
name: neuro
is_a: HP:0000001 ! root

[Term]
id: HP:0000110
name: seizure
is_a: HP:0000100 ! neuro

[Term]
id: HP:0000111
name: focal seizure
is_a: HP:0000110 ! seizure

[Term]
id: HP:0000120
name: developmental delay
is_a: HP:0000100 ! neuro
"""

# QUERY shares the specific focal-seizure term with NEAR, and only the general
# neuro ancestor with FAR.
MINI_HPOA = "\t".join(
    ["database_id", "disease_name", "qualifier", "hpo_id", "reference",
     "evidence", "onset", "frequency", "sex", "modifier", "aspect",
     "biocuration"]
) + "\n" + "\n".join(
    "\t".join([d, n, q, hp] + [""] * 8)
    for d, n, q, hp in [
        ("OMIM:1", "QUERY", "", "HP:0000111"),
        ("OMIM:1", "QUERY", "", "HP:0000120"),
        ("OMIM:2", "NEAR", "", "HP:0000111"),
        ("OMIM:2", "NEAR", "", "HP:0000120"),
        ("OMIM:3", "FAR", "", "HP:0000100"),
        ("OMIM:4", "NEG", "NOT", "HP:0000111"),  # negated -> excluded
    ]
)


class PhenotypicNeighborTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        root = Path(self.tmp.name)
        self.obo = root / "hp.obo"
        self.hpoa = root / "phenotype.hpoa"
        self.obo.write_text(MINI_OBO, encoding="utf-8")
        self.hpoa.write_text(MINI_HPOA, encoding="utf-8")
        self.profiles, self.names = PN.load_hpoa(self.hpoa)
        self.ancestors = PN.build_ancestors(PN.load_hp_parents(self.obo))
        self.ic = PN.information_content(self.profiles, self.ancestors)

    def test_negated_annotation_excluded(self) -> None:
        self.assertNotIn("HP:0000111", self.profiles.get("OMIM:4", set()))

    def test_ancestors_include_self_and_root(self) -> None:
        anc = self.ancestors("HP:0000111")
        self.assertIn("HP:0000111", anc)
        self.assertIn("HP:0000100", anc)
        self.assertIn("HP:0000001", anc)

    def test_specific_term_has_higher_ic_than_general(self) -> None:
        self.assertGreater(self.ic["HP:0000111"], self.ic["HP:0000100"])

    def test_near_ranks_above_far(self) -> None:
        ranked = PN.rank_neighbours(
            "OMIM:1", self.profiles, self.names, self.ancestors, self.ic,
            min_shared=1,
        )
        order = [disease for _, disease, _, _ in ranked]
        self.assertEqual(order[0], "OMIM:2")  # NEAR (shares specific term)
        self.assertIn("OMIM:3", order)        # FAR still present
        self.assertLess(order.index("OMIM:2"), order.index("OMIM:3"))

    def test_missing_query_raises(self) -> None:
        with self.assertRaises(KeyError):
            PN.rank_neighbours(
                "OMIM:999", self.profiles, self.names, self.ancestors,
                self.ic, min_shared=1,
            )


if __name__ == "__main__":
    unittest.main()
