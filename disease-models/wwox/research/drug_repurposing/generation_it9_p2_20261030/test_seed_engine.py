#!/usr/bin/env python3
"""Unit tests with positive checks for seed_engine.py on a synthetic graph with hand-computed answers (no repository data needed).

  test_seed_engine.py          runs all checks, exit 0 on success
"""
import sys
if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
    print(__doc__); raise SystemExit(0)
import importlib.util, os, tempfile
from pathlib import Path
HERE = Path(__file__).resolve().parent
_saved = sys.argv; sys.argv = ["seed_engine.py", "selftest"]
spec = importlib.util.spec_from_file_location("seed_engine", HERE / "seed_engine.py")
se = importlib.util.module_from_spec(spec); spec.loader.exec_module(se); sys.argv = _saved
import numpy as np

def mk(seed_rows):
    edges = [("A", "B", 1), ("B", "C", -1), ("D", "C", 1)]
    g = se.Graph(edges, extras=["Z"])
    rows = [dict(family_id=f, target_symbol=t, mean_sign=str(s), groups="ChEMBL", scopes="x") for f, t, s in
            [("X", "A", -1), ("Y", "A", 1), ("W", "D", -1), ("V", "C", -1), ("U", "Z", -1)]]
    return se.Engine(g, se.Compounds(rows), se.Seeds(seed_rows))

def unit(gene, sign, level=1.0):
    return dict(unit_id="s:" + gene, seed_id="s", gene=gene, sign=sign, level=level, status="defined" if sign else "uncertain", readout_level="transcript", evidence_class="transcript_contrast")

def q(e, s):
    i, d = e.quick(s); return {f: i[e.comp.fidx[f]] + d[e.comp.fidx[f]] for f in e.comp.fams}

ok, _ = se.selftest(); assert ok, "selftest"
s = se.Seeds([unit("C", 1)]); e = mk(s.units); r = q(e, s)
assert abs(r["X"] + 0.5) < 1e-12 and abs(r["Y"] - 0.5) < 1e-12 and abs(r["W"] - 1.0) < 1e-12 and abs(r["V"] - 1.0) < 1e-12 and r["U"] == 0, r     # known answers
r0 = q(e, se.Seeds([])); assert all(v == 0 for v in r0.values())                                                                                      # seeds removed -> zero baseline
rf = q(e, se.Seeds([unit("C", -1)])); assert all(abs(rf[k] + r[k]) < 1e-12 for k in r)                                                                # sign flip negates
r2 = q(e, se.Seeds([unit("C", 1, 0.4)])); assert all(abs(r2[k] - 0.4 * r[k]) < 1e-12 for k in r)                                                     # linearity in level
ru = q(e, se.Seeds([unit("C", 0, 1.0)])); assert abs(ru["Y"] - 0.5) < 1e-12                                                                           # uncertain unit = + arm
arms = e.arms(); assert abs(arms["full"][e.comp.fidx["X"]] + 0.5) < 1e-12
assert se.call_label(0.3, 0.1) == "opposes" and se.call_label(-0.3, 0.1) == "mimics" and se.call_label(0.05, 0.1).endswith("conditional_on_uncertain_seeds") and se.call_label(0, 0) == "none"
# firewall: refused classes and mixed levels
d = tempfile.mkdtemp()
hdr = "seed_id\tgene\tkind\tmembers\tdirection\tlevel\tdirection_status\treadout_level\tevidence_class\tspecies\tortholog_map\tsource_ref\tnote\n"
def tryload(row, **kw):
    p = os.path.join(d, "s.tsv"); open(p, "w").write(hdr + row + "\n")
    try:
        se.load_seeds(p, **kw); return "loaded"
    except SystemExit as ex:
        return str(ex)
assert tryload("S1\tPDK1\tgene\t\tdown\t1\tdefined\ttranscript\ttranscript_contrast\thuman\t\tx\t") == "loaded"
assert "firewall" in tryload("S1\tPDK1\tgene\t\tdown\t1\tdefined\ttranscript\tintervention_response\thuman\t\tx\t")
assert "firewall" in tryload("S1\tPDK1\tgene\t\tdown\t1\tdefined\ttranscript\tcard\thuman\t\tx\t")
assert "ortholog_map" in tryload("S1\tPDK1\tgene\t\tdown\t1\tdefined\ttranscript\ttranscript_contrast\tmouse\t\tx\t")
assert tryload("S1\tPDK1\tgene\t\tdown\t1\tdefined\ttranscript\ttranscript_contrast\tmouse\tHGNC link\tx\t") == "loaded"
p = os.path.join(d, "m.tsv"); open(p, "w").write(hdr + "S1\tPDK1\tgene\t\tdown\t1\tdefined\ttranscript\ttranscript_contrast\thuman\t\tx\t\nS2\tGFAP\tgene\t\tup\t1\tdefined\tprotein\tprotein_state\thuman\t\tx\t\n")
try:
    se.load_seeds(p); raise AssertionError("mixed levels accepted")
except SystemExit as ex:
    assert "mixed readout levels" in str(ex)
assert len(se.load_seeds(p, allow_mixed=True)) == 2
# process seed spreads level over members
open(p, "w").write(hdr + "S1\tSET:X\tprocess\tA;B;C;D\tup\t1\tdefined\ttranscript\ttranscript_contrast\thuman\t\tx\t\n")
ps = se.load_seeds(p); assert len(ps) == 4 and abs(ps.units[0]["level"] - 0.5) < 1e-12
# decomposition: per-unit contributions sum to the score
s2 = se.Seeds([unit("C", 1), unit("D", -1, 0.5)]); e2 = mk(s2.units)
S = s2.unit_matrix(e2.g.idx, e2.g.N); C = se.score(e2.A, S, e2.F) + se.score(e2.A, e2.g.influence_ind(S), e2.F)
tot = q(e2, s2); assert all(abs(C[e2.comp.fidx[f]].sum() - tot[f]) < 1e-12 for f in tot)
print("test_seed_engine: all checks passed")
