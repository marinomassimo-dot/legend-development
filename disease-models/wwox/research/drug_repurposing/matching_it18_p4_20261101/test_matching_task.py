import contextlib
import gzip
import io
import json
import tempfile
import unittest
from pathlib import Path

import matching_task as m

D, I = m.DEC, m.INC


def row(need_dir, targets, need_u=None, rowsets=None, need="N", parent="C1"):
    """targets: {uniprot: (symbol, class, reason)}"""
    t = {u: (s, c, w, "RAW") for u, (s, c, w) in targets.items()}
    return {"need": need, "need_direction": need_dir, "parent": parent, "split": m.dt.split_of(parent), "targets": t,
            "module_uniprots": frozenset(need_u or targets), "rowsets": rowsets or set()}


def E(classes):
    return {"classes": set(classes), "raw": set(), "pmids": set()}


class Labels(unittest.TestCase):
    def test_l_follows_need_direction_and_abstains_on_uncertain(self):
        self.assertEqual(m.label_l(row("down", {"P1": ("G", D, "ok")})), (m.COMPAT, "matches_need_direction"))
        self.assertEqual(m.label_l(row("down", {"P1": ("G", I, "ok")})), (m.OPPOS, "reverses_need_direction"))
        self.assertEqual(m.label_l(row("uncertain", {"P1": ("G", D, "ok")}))[1], "need_direction_uncertain")
        self.assertEqual(m.label_l(row("restore", {"P1": ("G", D, "ok")}))[0], m.INDET)

    def test_l_abstains_on_partial_conflict_and_opposite_targets(self):
        self.assertEqual(m.label_l(row("down", {"P1": ("G", None, "no_direction")}))[1], "action_partial_or_unknown")
        self.assertEqual(m.label_l(row("down", {"P1": ("G", None, "conflict")}))[1], "action_conflict_within_target")
        self.assertEqual(m.label_l(row("down", {"P1": ("G", D, "ok"), "P2": ("H", I, "ok")}))[1], "opposite_directions_across_targets")

    def test_x_uses_prior_not_need(self):
        pri = {"P1": (I, "target_majority", 0, 3)}
        self.assertEqual(m.label_x(row("down", {"P1": ("G", I, "ok")}), pri)[0], m.COMPAT)
        self.assertEqual(m.label_x(row("uncertain", {"P1": ("G", D, "ok")}), pri)[0], m.OPPOS)
        pri2 = {"P1": (I, "", 0, 0), "P2": (D, "", 0, 0)}
        self.assertEqual(m.label_x(row("down", {"P1": ("G", D, "ok"), "P2": ("H", D, "ok")}), pri2)[0], m.INDET)

    def test_v2_group_record_rule(self):
        big = frozenset("P%d" % i for i in range(10))
        r = row("down", {"P1": ("G", D, "ok")}, need_u={"P1", "P2"}, rowsets={big})
        self.assertEqual(m.label_l(r)[0], m.COMPAT)
        self.assertEqual(m.label_l(r, "v2")[1], "group_record_mostly_outside_module_targets")
        r2 = row("down", {"P1": ("G", D, "ok")}, need_u={"P1", "P2"}, rowsets={big, frozenset({"P1", "P2", "P3"})})
        self.assertEqual(m.label_l(r2, "v2")[0], m.COMPAT)


class Reference(unittest.TestCase):
    def test_truth_unknown_is_not_negative(self):
        r = row("down", {"P1": ("G", D, "ok")})
        self.assertEqual(m.truth(r, {}, ["P1"])[0], "unknown_no_counterpart")
        self.assertEqual(m.truth(r, {("C1", "P1"): E([None])}, ["P1"])[0], "no_direction")
        self.assertEqual(m.truth(r, {("C1", "P1"): E([D])}, ["P1"])[0], m.COMPAT)
        self.assertEqual(m.truth(r, {("C1", "P1"): E([I])}, ["P1"])[0], m.OPPOS)
        self.assertEqual(m.truth(r, {("C1", "P1"): E([D]), ("C1", "P2"): E([I])}, ["P1", "P2"])[0], "mixed")

    def test_score_counts_wrong_compatible_and_base_rate(self):
        rows = [row("down", {"P1": ("G", D, "ok")}, parent=p) for p in ("A", "B", "C", "D")]
        for r in rows:
            r["split"] = "eval"
        gt = {("A", "P1"): E([D]), ("B", "P1"): E([I]), ("C", "P1"): E([D])}
        lab = {p: {(r["need"], r["parent"]): (m.COMPAT, "") for r in rows} for p in ("X", "L")}
        res, tr = m.score_split(rows, lab, gt, {"N": ["P1"]}, "eval")
        self.assertEqual(res["T"]["n_determinate"], 3)
        self.assertAlmostEqual(res["T"]["base_rate"], 0.6667)
        self.assertEqual(res["L"]["truly_opposite_labelled_compatible"], ["B"])
        self.assertEqual(res["reference_category_counts"]["unknown_no_counterpart"], 1)
        self.assertIn("fewer than 40", m.decide(res)["L_vs_T"])
        self.assertIn("no measured WWOX contribution", m.decide(res)["L_vs_X"])


class Staging(unittest.TestCase):
    def _fixture(self, d):
        d = Path(d)
        cat = [{"ids": {"chembl": "CHEMBL1"}, "relations": {"parent": None}, "name": "A",
                "targets": [{"source": "ChEMBL curated mechanism", "organism": "Homo sapiens", "inherited_from_parent": None,
                             "uniprot": ["P1"], "action_type": "ANTAGONIST", "reference_ids": [], "target_type": "SINGLE PROTEIN"}]}]
        with gzip.open(d / "cat.jsonl.gz", "wt") as f:
            f.write("\n".join(json.dumps(x) for x in cat) + "\n")
        (d / "needs.json").write_text(json.dumps({"needs": [{"id": "N1", "intervention_direction": {"direction": "down"},
                                                             "targets": [{"symbol": "G1", "target_kind": "intervention_target"}]}]}))
        with gzip.open(d / "targets.jsonl.gz", "wt") as f:
            f.write(json.dumps({"organism": "Homo sapiens", "target_components": [{"accession": "P1", "target_component_synonyms": [
                {"syn_type": "GENE_SYMBOL", "component_synonym": "G1"}, {"syn_type": "GENE_SYMBOL_OTHER", "component_synonym": "G9"}]}]}) + "\n")
        g = d / "g"
        g.mkdir()
        (g / "ligands.csv").write_text('"# v"\n"Ligand ID","ChEMBL ID"\n"7","CHEMBL1"\n')
        (g / "interactions.csv").write_text('"# v"\n"Target Species","Ligand ID","Target UniProt ID","Type","Action","PubMed ID"\n"Human","7","P1","Antagonist","Antagonist",""\n')
        (d / "links.json").write_text(json.dumps({"cards": {}}))
        out = d / "out"
        out.mkdir()
        base = ["--catalog", str(d / "cat.jsonl.gz"), "--needs", str(d / "needs.json"), "--chembl-targets", str(d / "targets.jsonl.gz"),
                "--gtopdb-dir", str(g), "--outdir", str(out)]
        return base, out, d

    def _run(self, argv):
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            return m.main(argv)

    def test_answers_then_score_and_refusals(self):
        with tempfile.TemporaryDirectory() as d:
            base, out, root = self._fixture(d)
            self.assertEqual(self._run(["answers"] + base), 0)
            lock = json.loads((out / "answers_lock.json").read_text())
            self.assertEqual(lock["symbol_to_uniprot"], {"G1": ["P1"]})
            self.assertEqual(lock["universe_rows"], 1)
            # uncommitted lock is refused
            self.assertEqual(self._run(["score"] + base + ["--card-links", str(root / "links.json")]), 2)
            self.assertFalse((out / "results.json").exists())
            self.assertEqual(self._run(["score"] + base + ["--card-links", str(root / "links.json"), "--allow-uncommitted-lock"]), 0)
            res = json.loads((out / "results.json").read_text())
            self.assertEqual(res["lock_sha256"], m.sha256(out / "answers_lock.json"))
            # tampering with the answers after the lock is refused
            (out / "answers.tsv").write_text((out / "answers.tsv").read_text().replace("compatible", "opposite"))
            self.assertEqual(self._run(["score"] + base + ["--card-links", str(root / "links.json"), "--allow-uncommitted-lock"]), 2)

    def test_alias_symbol_never_maps(self):
        with tempfile.TemporaryDirectory() as d:
            _, _, root = self._fixture(d)
            self.assertEqual(m.symbol_to_uniprot(root / "targets.jsonl.gz", {"G9"}), {})

    def test_eval_rows_dropped_when_dev_only(self):
        with tempfile.TemporaryDirectory() as d:
            _, _, root = self._fixture(d)
            keep = m.dt.split_of("CHEMBL1")
            other = {"dev", "eval"} - {keep}
            self.assertEqual(len(m.load_gtopdb_split(root / "g", {}, {keep})), 1)
            self.assertEqual(len(m.load_gtopdb_split(root / "g", {}, other)), 0)

    def test_help_writes_nothing(self):
        with tempfile.TemporaryDirectory() as d:
            before = set(Path(d).iterdir())
            with self.assertRaises(SystemExit):
                with contextlib.redirect_stdout(io.StringIO()):
                    m.main(["--help"])
            self.assertEqual(self._run([]), 0)
            self.assertEqual(set(Path(d).iterdir()), before)


if __name__ == "__main__":
    unittest.main(verbosity=2)
