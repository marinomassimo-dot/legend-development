import sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import alias_scan_it26 as m


class T(unittest.TestCase):
    def test_zhx2_raf_is_caught(self):          # the IT25 positive control
        self.assertEqual(m.suspect(["AFR1", "RAF"], {"ZHX2", "KIAA0854"}, {"RAF1", "BRAF"}, "ZHX2"), [("RAF", "RAF1")])

    def test_hgnc_listed_alias_is_not_suspect(self):
        self.assertEqual(m.suspect(["RAF"], {"ZHX2", "RAF"}, {"RAF1"}, "ZHX2"), [])

    def test_short_alias_ignored(self):
        self.assertEqual(m.suspect(["R2"], set(), {"R2X"}, "RRM2"), [])

    def test_own_symbol_not_a_hit(self):
        self.assertEqual(m.suspect(["PIK3"], set(), {"PIK3CG"}, "PIK3CG"), [])

    def test_scan_pipeline(self):
        rows = m.scan([dict(reason_class="listing_tier_claim_not_carried", name="Sorafenib", genes="ZHX2", claim_source="TALC")],
                      [dict(name="Sorafenib", family_id="F1")], [dict(family_id="F1", target_symbol="RAF1")],
                      [dict(symbol="ZHX2", alias_symbol=["KIAA0854"])], {"ZHX2": {"alias": ["RAF"]}})
        self.assertEqual([(r["compound"], r["gene"], r["ncbi_only_alias"]) for r in rows], [("Sorafenib", "ZHX2", "RAF")])

    def test_collide_distinct_substances_flagged_salt_not(self):    # IT27: E-3810 is rabeprazole and lucitanib; the sodium salt is no collision
        mol = lambda i, par, key, name, syn: dict(molecule_chembl_id=i, pref_name=name, molecule_hierarchy=dict(parent_chembl_id=par),
                                                  molecule_structures=dict(standard_inchi_key=key + "-UHFFFAOYSA-N"), molecule_synonyms=[dict(molecule_synonym=x) for x in syn])
        res = m.collide([mol("C1", "C1", "AAAAAAAAAAAAAA", "RABEPRAZOLE", ["E-3810", "Pariet"]),
                         mol("C2", "C1", "AAAAAAAAAAAAAA", "RABEPRAZOLE SODIUM", ["E-3810 SODIUM", "E-3810"]),
                         mol("C3", "C3", "BBBBBBBBBBBBBB", "LUCITANIB", ["E-3810", "S-80881"]),
                         mol("C4", "C4", "CCCCCCCCCCCCCC", "CAPIVASERTIB", ["AZD5363"]),
                         mol("C5", "C5", "CCCCCCCCCCCCCC", "CAPIVASERTIB HCL", ["AZD5363"])])
        self.assertEqual(list(res), ["E3810"])
        self.assertEqual(sorted(x[2] for x in res["E3810"]), ["LUCITANIB", "RABEPRAZOLE"])   # AZD5363 shared by a salt pair: not flagged


if __name__ == "__main__":
    unittest.main(verbosity=2)
