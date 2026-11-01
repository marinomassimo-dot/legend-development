import json
import os
import subprocess
import tempfile
import unittest
from pathlib import Path

import prospective_eval as pe

HDR = "unit_id\tintervention\tsystem_context\tendpoint\tcomparator\tresult\tobjective_match\torigin_group\tpub_date\tprovenance\n"


def row(u, res, match="yes", grp="O1", date="2099-01-01"):
    return "%s\tX\tmouse\tseizure score\tvehicle\t%s\t%s\t%s\t%s\tPMID:1\n" % (u, res, match, grp, date)


def vc(root, *a):
    return subprocess.run(["git", "-C", str(root), *a], capture_output=True, text=True, check=True).stdout


class T(unittest.TestCase):
    def setUp(self):
        self.d = tempfile.TemporaryDirectory()
        r = Path(self.d.name)
        vc(r, "init", "-q")
        vc(r, "config", "user.email", "t@example.invalid")
        vc(r, "config", "user.name", "t")
        (r / "units.tsv").write_text("unit_id\tlabel\nA\ta\nB\tb\nC\tc\n")
        (r / "selections.tsv").write_text("view\tposition_in_list\tunit_id\tobjective\ngeneral\t1\tA\tobj\ngeneral\t2\tB\tobj\n")
        (r / "mem.tsv").write_text("unit_id\twwox_assertions\nC\t5\nA\t1\n")
        (r / "rules.py").write_text("R=1\n")
        vc(r, "add", ".")
        vc(r, "commit", "-qm", "x")
        self.r = r
        self.out = r / "fr"
        pe.main(["freeze", "--repo", str(r), "--out", str(self.out), "--task", "t", "--pool", str(r / "units.tsv"),
                 "--selection", str(r / "selections.tsv"), "--aux", str(r / "mem.tsv"), "--rules", str(r / "rules.py"),
                 "--top-n", "2"])
        self.fz = str(self.out / "FREEZE.json")

    def tearDown(self):
        self.d.cleanup()

    def score(self, body, descriptive=True):
        p = self.r / "o.tsv"
        p.write_text(HDR + body)
        rec, bad = pe.verify(self.fz)
        self.assertEqual(bad, [])
        return pe.score(rec, pe.tsv(p), descriptive)[0]

    def test_freeze_record(self):
        rec = json.loads(Path(self.fz).read_text())
        for k in ("frozen_at_utc", "git_commit", "selection", "inputs", "method_version", "baseline_B1_top", "pool_ids"):
            self.assertIn(k, rec)
        self.assertEqual(rec["selection"], ["A", "B"])
        self.assertEqual(rec["baseline_B1_top"], ["C", "A"])
        self.assertTrue(all(len(i["sha256"]) == 64 for i in rec["inputs"].values()))

    def test_tested_but_contrary_or_null_is_not_success(self):
        s = self.score(row("A", "contrary") + row("B", "null", grp="O2"))
        self.assertEqual(s["arms"]["selection"]["units_with_success"], [])
        self.assertEqual(s["arms"]["selection"]["units_with_contrary"], ["A"])
        self.assertEqual(s["arms"]["selection"]["units_with_null"], ["B"])

    def test_favourable_off_objective_is_not_success(self):
        s = self.score(row("A", "favourable", match="no"))
        self.assertEqual(s["arms"]["selection"]["units_with_success"], [])
        self.assertEqual(s["per_unit"]["A"]["off_objective"], 1)

    def test_unknown_stays_unknown(self):
        s = self.score(row("A", "undeterminable", match="unknown"))
        self.assertEqual(s["determinate_origin_groups"], 0)
        self.assertEqual(s["arms"]["selection"]["units_only_off_objective_or_undeterminable"], ["A"])
        self.assertEqual(s["arms"]["selection"]["units_with_success"], [])

    def test_same_origin_twice_counts_once(self):
        s = self.score(row("A", "favourable") + row("A", "favourable"))
        self.assertEqual(s["per_unit"]["A"]["success"], 1)
        self.assertEqual(s["determinate_origin_groups"], 1)

    def test_one_origin_over_two_units_counts_once_toward_the_rule(self):
        s = self.score(row("A", "favourable", grp="O1") + row("B", "favourable", grp="O1"))
        self.assertEqual(s["determinate_origin_groups"], 1)
        self.assertEqual(s["arms"]["selection"]["units_with_success"], ["A", "B"])

    def test_favourable_with_unknown_match_is_unknown(self):
        s = self.score(row("A", "favourable", match="unknown"))
        self.assertEqual(s["per_unit"]["A"]["undeterminable"], 1)

    def test_conflicting_rows_in_one_origin_are_unresolved(self):
        s = self.score(row("A", "favourable") + row("A", "contrary"))
        self.assertEqual(s["per_unit"]["A"]["undeterminable"], 1)
        self.assertEqual(s["per_unit"]["A"]["success"], 0)

    def test_pre_freeze_rows_excluded_and_no_claim_below_rule(self):
        p = self.r / "o.tsv"
        p.write_text(HDR + row("A", "favourable", date="2000-01-01"))
        s, ok = pe.score(pe.verify(self.fz)[0], pe.tsv(p), False)
        self.assertEqual(s["rows_used"], 0)
        self.assertFalse(ok)
        self.assertTrue(s["claim"].startswith("none"))

    def test_minimal_rule_met(self):
        p = self.r / "o.tsv"
        p.write_text(HDR + row("A", "favourable", grp="O1") + row("B", "favourable", grp="O2") + row("B", "null", grp="O3"))
        s, ok = pe.score(pe.verify(self.fz)[0], pe.tsv(p), False)
        self.assertTrue(ok)

    def test_digest_mismatch_refuses(self):
        (self.out / "frozen" / "selections.tsv").write_text("view\tposition_in_list\tunit_id\tobjective\ngeneral\t1\tC\tobj\n")
        p = self.r / "o.tsv"
        p.write_text(HDR + row("A", "favourable"))
        self.assertEqual(pe.main(["evaluate", "--freeze", self.fz, "--outcomes", str(p)]), 3)

    def test_later_live_change_does_not_change_the_prediction(self):
        (self.r / "selections.tsv").write_text("view\tposition_in_list\tunit_id\tobjective\ngeneral\t1\tC\tobj\n")
        rec, bad = pe.verify(self.fz)
        self.assertEqual(bad, [])
        self.assertEqual(rec["selection"], ["A", "B"])

    def test_freeze_refuses_uncommitted_input_and_second_freeze(self):
        (self.r / "units.tsv").write_text("unit_id\tlabel\nZ\tz\n")
        with self.assertRaises(SystemExit):
            pe.main(["freeze", "--repo", str(self.r), "--out", str(self.r / "fr2"), "--task", "t",
                     "--pool", str(self.r / "units.tsv"), "--selection", str(self.r / "selections.tsv"),
                     "--rules", str(self.r / "rules.py")])
        with self.assertRaises(SystemExit):
            pe.main(["freeze", "--repo", str(self.r), "--out", str(self.out), "--task", "t",
                     "--pool", str(self.r / "units.tsv"), "--selection", str(self.r / "selections.tsv"),
                     "--rules", str(self.r / "rules.py")])


class Integrity(T):
    def _reseal(self):
        (self.out / "FREEZE.sha256").write_text("%s  FREEZE.json\n" % pe.sha256(self.fz))

    def _edit(self, **kw):
        rec = json.loads(Path(self.fz).read_text())
        rec.update(kw)
        Path(self.fz).write_text(json.dumps(rec, indent=1, sort_keys=True))

    def _outcomes(self, body):
        p = self.r / "o.tsv"
        p.write_text(HDR + body)
        return str(p)

    def test_tampered_selection_or_instant_refused_by_seal(self):
        self._edit(selection=["C", "A"], frozen_at_utc="2026-01-01T00:00:00Z")
        self.assertEqual(pe.main(["evaluate", "--freeze", self.fz, "--outcomes", self._outcomes(row("A", "favourable"))]), 3)

    def test_resealed_tamper_still_caught_against_frozen_copies(self):
        self._edit(selection=["C", "A"])
        self._reseal()
        self.assertEqual(pe.main(["evaluate", "--freeze", self.fz, "--outcomes", self._outcomes(row("A", "favourable"))]), 3)

    def test_scorer_digest_checked(self):
        self._edit(scorer_sha256="0" * 64)
        self._reseal()
        self.assertTrue(any("scorer" in b for b in pe.verify(self.fz)[1]))

    def test_sealed_addendum_may_list_a_later_scorer(self):
        self._edit(scorer_sha256="0" * 64)
        (self.out / "ADDENDUM.json").write_text(json.dumps({"scorer_versions": [{"sha256": pe.sha256(pe.__file__), "reason": "fix"}]}))
        (self.out / "FREEZE.sha256").write_text("%s  FREEZE.json\n%s  ADDENDUM.json\n" % (pe.sha256(self.fz), pe.sha256(self.out / "ADDENDUM.json")))
        self.assertEqual(pe.verify(self.fz)[1], [])

    def test_rules_digest_checked_against_git(self):
        rec = json.loads(Path(self.fz).read_text())
        rec["inputs"]["rules"]["sha256"] = "1" * 64
        Path(self.fz).write_text(json.dumps(rec, indent=1, sort_keys=True))
        self._reseal()
        self.assertTrue(any("rules" in b for b in pe.verify(self.fz, self.r)[1]))

    def test_b1_top_has_no_id_tie_filler(self):
        (self.r / "mem.tsv").write_text("unit_id\twwox_assertions\nC\t5\n")
        self.assertEqual(pe.b1_top_units(pe.tsv(self.r / "units.tsv"), pe.tsv(self.r / "mem.tsv"), "unit_id", 3), ["C"])

    def test_unknown_unit_id_is_an_error_not_a_count(self):
        body = row("U30", "favourable", grp="O1") + row("Z99", "favourable", grp="O2") + row("A", "favourable", grp="O3")
        self.assertEqual(pe.main(["evaluate", "--freeze", self.fz, "--outcomes", self._outcomes(body)]), 4)

    def test_dates_must_be_iso(self):
        for bad in ("Nov 2026", "2026-11-1", "2026-13-01", "20261101"):
            self.assertEqual(pe.main(["evaluate", "--freeze", self.fz, "--outcomes", self._outcomes(row("A", "favourable", date=bad))]), 4, bad)

    def test_seal_refuses_to_overwrite(self):
        with self.assertRaises(SystemExit):
            pe.seal(self.fz, None)


class Help(unittest.TestCase):
    def test_help_writes_nothing(self):
        with tempfile.TemporaryDirectory() as d:
            subprocess.run(["python3", "-I", str(Path(pe.__file__)), "--help"], cwd=d, check=True, capture_output=True)
            self.assertEqual(os.listdir(d), [])


if __name__ == "__main__":
    unittest.main()
