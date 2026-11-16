#!/usr/bin/env python3
"""Tests for ppxy_scan.py on a synthetic two-entry universe (no network): overlapping motifs, cytoplasmic-only scoring, topology_unknown tier, seeded reproducibility."""
import csv, hashlib, json, subprocess, sys, tempfile, unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCAN = HERE / "ppxy_scan.py"
HDR = ["Entry", "Entry Name", "Gene Names (primary)", "Protein names", "Length", "Keywords", "Topological domain", "Transmembrane", "Sequence"]


def write_universe(d, rows_mouse, rows_human):
    for name, tax, rows in (("mouse", "10090", rows_mouse), ("human", "9606", rows_human)):
        with open(d / f"uniprot_{name}_{tax}.tsv", "w", newline="") as fh:
            w = csv.writer(fh, delimiter="\t", lineterminator="\n"); w.writerow(HDR); w.writerows(rows)
    (d / "MANIFEST.json").write_text(json.dumps({"files": {"a": {"sha256": "0", "release": "test"}}}))


def row(acc, sym, seq, topo="", tm=""):
    return [acc, sym + "_X", sym, sym + " protein", str(len(seq)), "Ion channel", topo, tm, seq]


class Scan(unittest.TestCase):
    def run_scan(self, mouse, human, seed=1):
        d = Path(tempfile.mkdtemp()); out = Path(tempfile.mkdtemp()); write_universe(d, mouse, human)
        r = subprocess.run([sys.executable, str(SCAN), "scan", "--raw", str(d), "--out", str(out), "--seed", str(seed), "--shuffles", "200"], capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr)
        return list(csv.DictReader(open(out / "ppxy_genes.tsv"), delimiter="\t")), list(csv.DictReader(open(out / "ppxy_motifs.tsv"), delimiter="\t")), out

    def test_cytoplasmic_only_and_overlap(self):
        seq = "AAAAPPPYAAAAAAAAAAAAAAAAAAAAAAAAAAAAPPSYKKKKKKPPPPYA"   # PPPY at 5 (extracellular), PPSY at 37, and PPPPY at 47..51 whose only PPxY four-mer is PPPY at 48
        topo = 'TOPO_DOM 1..20; /note="Extracellular"; /evidence="x"; TOPO_DOM 21..%d; /note="Cytoplasmic"; /evidence="x"' % len(seq)
        g, m, _ = self.run_scan([row("P1", "Chan1", seq, topo)], [row("Q1", "CHAN1", seq, topo)])
        mouse = [x for x in g if x["species"] == "mouse"][0]
        self.assertEqual(mouse["topology"], "annotated")
        self.assertEqual(mouse["n_core_PPxY"], "2")                      # PPPY at 5 lies in the extracellular part and is NOT counted
        self.assertEqual(sorted(int(x["pos"]) for x in m if x["species"] == "mouse"), [37, 48])
        self.assertNotIn(5, [int(x["pos"]) for x in m if x["species"] == "mouse"])
        self.assertIn(37, [int(x["pos"]) for x in m if x["species"] == "mouse"])

    def test_topology_unknown_excludes_transmembrane(self):
        seq = "MPPAYMMMMMMMMMMMMMMPPSYQQQ"                               # PPAY inside the annotated TM span 1..18 is excluded, PPSY after it is kept
        g, m, _ = self.run_scan([row("P2", "Chan2", seq, "", "TRANSMEM 1..18; /note=\"Helical\"")], [])
        x = [y for y in g if y["species"] == "mouse"][0]
        self.assertEqual(x["topology"], "topology_unknown"); self.assertEqual(x["n_core_PPxY"], "1")

    def test_seeded_reproducible(self):
        seq = "A" * 30 + "PPSY" + "G" * 30
        topo = 'TOPO_DOM 1..%d; /note="Cytoplasmic"; /evidence="x"' % len(seq)
        a = self.run_scan([row("P3", "Chan3", seq, topo)], [], seed=7)[2]; b = self.run_scan([row("P3", "Chan3", seq, topo)], [], seed=7)[2]
        self.assertEqual(hashlib.sha256((a / "ppxy_genes.tsv").read_bytes()).hexdigest(), hashlib.sha256((b / "ppxy_genes.tsv").read_bytes()).hexdigest())

    def test_help_is_safe(self):
        r = subprocess.run([sys.executable, str(SCAN), "--help"], capture_output=True, text=True)
        self.assertEqual(r.returncode, 0); self.assertIn("fetch", r.stdout)


if __name__ == "__main__":
    unittest.main(verbosity=2)
