#!/usr/bin/env python3
"""Mutation tests for the v3 provenance filters (PRE_REGISTRATION_V3.md S3). Each assertion holds with the filter on and FAILS (is inverted) with the filter off.

  test_v3_filters.py [--actions DIR]      DIR defaults to results/actions (built by build_actions_v3.py); the v2 table ../results is used as the filter-off control
"""
import sys
if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
    print(__doc__); raise SystemExit(0)
import csv, gzip, importlib.util
from pathlib import Path
HERE = Path(__file__).resolve().parent
actions = Path(sys.argv[sys.argv.index("--actions") + 1]) if "--actions" in sys.argv else HERE / "results" / "actions"
_saved = sys.argv; sys.argv = ["seed_engine_v3.py", "selftest"]
spec = importlib.util.spec_from_file_location("seed_engine_v3", HERE / "seed_engine_v3.py")
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); sys.argv = _saved
se = m.se
import numpy as np

# synthetic network: A -P(+)-> B -T(+)-> S ; X -P(+)-> S ; Y -T(+)-> S ; M -P(+)-> GNAO1 -T(+)-> S ; A -P(+)-> PS (protein seed) ; Y -T(+)-> PS
edges = [("A", "B", 1, "P"), ("B", "S", 1, "T"), ("X", "S", 1, "P"), ("Y", "S", 1, "T"), ("M", "GNAO1", 1, "C"), ("GNAO1", "S", 1, "T"), ("A", "PS", 1, "P"), ("Y", "PS", 1, "T")]
def influence(seedgene, level, mode):
    m.MODE = mode
    g = m.Graph3(edges, extras=[]); g.level = level
    S = np.zeros((1, g.N)); S[0, g.idx[seedgene]] = 1.0
    v = g.influence_ind(S)[0]
    return {k: float(v[g.idx[k]]) for k in ("A", "B", "X", "Y", "M", "GNAO1")}
v3 = influence("S", "expression", "v3"); al = influence("S", "expression", "all")
assert v3["B"] != 0 and v3["A"] != 0 and v3["Y"] != 0                      # T into the seed, P* before it: admitted
assert v3["X"] == 0 and al["X"] != 0                                       # (a) P edge straight into an expression seed: 0 in v3, nonzero when the filter is off
assert v3["M"] == 0 and v3["GNAO1"] != 0 and al["M"] != 0                  # (c) coupling edge in a chain: 0 in v3, nonzero when off
pv3 = influence("PS", "protein", "v3"); pal = influence("PS", "protein", "all")
assert pv3["A"] != 0 and pv3["Y"] == 0 and pal["Y"] != 0                   # (b) T edge into a protein seed: 0 in v3, nonzero when off; P onto the protein admitted
m.MODE = "v3"
# chain explanation follows the same grammar
g = m.Graph3(edges, extras=[]); g.level = "expression"
assert g.best_chain("A", "S") is not None and g.best_chain("X", "S") is None and g.best_chain("M", "S") is None
# compound-side rules on the built tables (positive) and on the v2 table (the filter-off control must violate them)
def rows(d):
    return [r for r in csv.DictReader(gzip.open(Path(d) / "family_actions.tsv.gz", "rt"), delimiter="\t")]
def anyrows(d):
    return [r for r in csv.DictReader(gzip.open(Path(d) / "family_targets_any.tsv.gz", "rt"), delimiter="\t")]
v3rows, v2rows = rows(actions), rows(HERE.parent / "results")
tg = lambda rs, fam: {r["target_symbol"] for r in rs if r["family_id"] == fam}
assert tg(v3rows, "FAM:CAT:CHEMBL2105804") == {"MTTP"} and "P4HB" in tg(v2rows, "FAM:CAT:CHEMBL2105804")        # (d) complex member not named is not credited (implitapide)
assert "P4HB" not in tg(v3rows, "FAM:CAT:DGIDB:71634dc5ca10") and "P4HB" in tg(v2rows, "FAM:CAT:DGIDB:71634dc5ca10")  # ... and the DGIdb copy does not bring it back
assert "PDK1" not in {r["target_symbol"] for r in anyrows(actions) if r["family_id"] == "FAM:CAT:CHEMBL1650595"} and \
       "PDK1" in {r["target_symbol"] for r in anyrows(HERE.parent / "results") if r["family_id"] == "FAM:CAT:CHEMBL1650595"}   # (e) alias collision: AR-12's PDK1 claim dropped, PDPK1 kept
assert "PDPK1" in tg(v3rows, "FAM:CAT:CHEMBL1650595")
flags = {r["family_id"] for r in csv.DictReader(gzip.open(actions / "family_flags.tsv.gz", "rt"), delimiter="\t")}
assert "FAM:CAT:CHEMBL1200760" in flags                                                                              # (f) balsalazide (prodrug) flagged UNCERTAIN_ACTIVE_MOIETY
assert all("UNCERTAIN_ACTIVE_MOIETY" in r["flags"] for r in v3rows if r["family_id"] == "FAM:CAT:CHEMBL1200760")
assert tg(v3rows, "FAM:CAT:CHEMBL1218") == {"MTNR1A", "MTNR1B"}                                                      # paralog family still credits all members (ramelteon)
print("test_v3_filters: all checks passed")
