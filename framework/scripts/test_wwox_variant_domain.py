#!/usr/bin/env python3
"""Regressions for wwox_variant_domain.py: the classes fixed before the join, deletions never read as missense, the P47T model-line mark, unparsed strings kept."""
import csv, subprocess, sys, tempfile, unittest
from pathlib import Path

TOOL = Path(__file__).resolve().parent / "wwox_variant_domain.py"


class VariantDomain(unittest.TestCase):
    def run_tool(self, variants: list[str]) -> dict:
        tmp = Path(tempfile.mkdtemp()); src, dst = tmp / "in.tsv", tmp / "out.tsv"
        src.write_text("child_id\thgvs_p\n" + "".join(f"c{i}\t{v}\n" for i, v in enumerate(variants)), encoding="utf-8")
        r = subprocess.run([sys.executable, str(TOOL), "--table", str(src), "--out", str(dst)], capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr)
        return {row["hgvs_input"]: row for row in csv.DictReader(open(dst, encoding="utf-8"), delimiter="\t")}

    def test_positions_fall_in_the_fixed_classes_and_boundaries_are_inclusive(self) -> None:
        m = self.run_tool(["p.Gln15Ter", "p.Lys16Glu", "p.Ala49Val", "p.Gly50Asp", "p.Ala56Val", "p.Leu57Pro", "p.Ala90Val", "p.Gly91Asp", "p.Ala124Val", "p.Gly125Asp", "p.Gln230Pro", "p.Ser414Ala"])
        got = {k: v["class"] for k, v in m.items()}
        self.assertEqual(got["p.Gln15Ter"], "N_terminal_disordered"); self.assertEqual(got["p.Lys16Glu"], "WW1"); self.assertEqual(got["p.Ala49Val"], "WW1")
        self.assertEqual(got["p.Gly50Asp"], "linker_1"); self.assertEqual(got["p.Ala56Val"], "linker_1"); self.assertEqual(got["p.Leu57Pro"], "WW2"); self.assertEqual(got["p.Ala90Val"], "WW2")
        self.assertEqual(got["p.Gly91Asp"], "linker_2"); self.assertEqual(got["p.Ala124Val"], "linker_2"); self.assertEqual(got["p.Gly125Asp"], "SDR_catalytic_region"); self.assertEqual(got["p.Ser414Ala"], "SDR_catalytic_region")
        self.assertIn("mito_targeting_209-273", m["p.Gln230Pro"]["subflags"])

    def test_deletions_and_frameshifts_are_their_own_types_not_missense(self) -> None:
        m = self.run_tool(["p.Gly100_Glu105del", "p.Lys104del", "p.Arg120fs", "p.Gly45_Ala60del", "p.Arg372Ter"])
        self.assertEqual(m["p.Gly100_Glu105del"]["variant_type"], "in_frame_deletion"); self.assertEqual(m["p.Lys104del"]["variant_type"], "in_frame_deletion")
        self.assertEqual(m["p.Arg120fs"]["variant_type"], "frameshift"); self.assertIn("downstream_lost", m["p.Arg120fs"]["spans_classes"])
        span = m["p.Gly45_Ala60del"]                                                                  # touches WW1, linker_1 and WW2: every class it touches, in its own row
        self.assertEqual((span["class"], span["spans_classes"]), ("WW1", "linker_1;WW2"))
        self.assertEqual(m["p.Arg372Ter"]["variant_type"], "nonsense")

    def test_the_p47t_model_line_mark_unparsed_strings_and_splice_rows(self) -> None:
        m = self.run_tool(["p.Pro47Thr", "p.(Pro47Thr)", "p.P47T", "p.Pro47Ala", "c.1057-2A>G", "p.X", "something else"])
        for k in ("p.Pro47Thr", "p.(Pro47Thr)", "p.P47T"):
            self.assertIn("same_variant_as_model_line: P47T knock-in line", m[k]["model_line_mark"]); self.assertEqual(m[k]["class"], "WW1")
        self.assertEqual(m["p.Pro47Ala"]["model_line_mark"], "")                                         # a different substitution at the same position is not the model line's variant
        self.assertEqual(m["c.1057-2A>G"]["variant_type"], "splice_no_protein_position")
        self.assertEqual((m["p.X"]["variant_type"], m["something else"]["variant_type"]), ("unparsed", "unparsed"))   # kept verbatim, never guessed

    def test_the_held_classification_is_joined_by_variant_in_any_notation(self) -> None:
        tmp = Path(tempfile.mkdtemp()); held = tmp / "held.csv"
        held.write_text("protein,pos,ddG,dist_cat,class\np.Pro47Thr,47,2.8059,12.1,stability (rescuable window)\np.Gln230Pro,230,1.5143,30.2,other\n", encoding="utf-8")
        src, dst = tmp / "in.tsv", tmp / "out.tsv"
        src.write_text("child_id\thgvs_p\na\tp.P47T\nb\tp.(Gln230Pro)\nc\tp.Leu99Pro\n", encoding="utf-8")
        r = subprocess.run([sys.executable, str(TOOL), "--table", str(src), "--out", str(dst), "--held-classified", str(held)], capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr)
        rows = {x["child_id"]: x for x in csv.DictReader(open(dst, encoding="utf-8"), delimiter="\t")}
        self.assertEqual(rows["a"]["held_class"], "stability (rescuable window)"); self.assertEqual(rows["a"]["held_ddG"], "2.8059")
        self.assertEqual(rows["b"]["held_class"], "other"); self.assertEqual(rows["c"]["held_class"], "")        # a variant the held table does not list stays blank

    def test_a_missing_column_is_refused_and_help_is_safe(self) -> None:
        tmp = Path(tempfile.mkdtemp()); (tmp / "t.tsv").write_text("child_id\tother\nx\ty\n", encoding="utf-8")
        r = subprocess.run([sys.executable, str(TOOL), "--table", str(tmp / "t.tsv"), "--out", str(tmp / "o.tsv")], capture_output=True, text=True)
        self.assertNotEqual(r.returncode, 0); self.assertIn("no column", r.stderr + r.stdout)
        self.assertEqual(subprocess.run([sys.executable, str(TOOL), "--help"], capture_output=True, text=True).returncode, 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
