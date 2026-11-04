#!/usr/bin/env python3
"""IT23 P3: run NORDic's own simulator class (NORDic.UTILS.utils_sim.MPBN_SIM) on one cell of the Q5 network and show how a
'perturbation' is encoded there: mutation_permanent={node: "0"} replaces the node's rule by the constant 0 (a CLAMP, identical
for a genetic knockdown and for a drug), compared with the explicit drug-switch (rule modification) used in sim_q5.py.
usage: python -I nordic_encoding_check.py [--help]     (needs the venv with NORDic installed; no network, no credentials)"""
import sys
if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
    print(__doc__); raise SystemExit(0)
import os, tempfile, pandas as pd
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sim_q5 as s
from NORDic.UTILS.utils_sim import MPBN_SIM

prem = ("COFACTOR", 1, 0, 0, 1)
r = s.rules("damaging_mediator", *prem)
fn = os.path.join(tempfile.mkdtemp(prefix="q5_bnet_"), "q5.bnet")
open(fn, "w").write("\n".join(f"{k}, {v}" for k, v in r.items()) + "\n")
names = list(r)
init = pd.DataFrame({"s": [1 if n in ("WWOX_loss", "ACT2") else 0 for n in names]}, index=names)
def nordic(mut):
    sim = MPBN_SIM(seednb=0, njobs=1)
    A = sim.up_to_attractors(fn, init, init, mutation_permanent=mut, verbose=False)
    keep = ["IL6_tx", "IL6_sig", "TNF_sig", "IL1B_sig", "RELA", "STAT3", "MYELIN_OL"]
    return A.loc[keep].astype(float).to_dict()
print("NORDic MPBN_SIM, no perturbation:                 ", nordic({}))
print("NORDic MPBN_SIM, mutation_permanent IL6_sig='0' (what DS would call 'IL6 neutraliser'):", nordic({"IL6_sig": "0"}))
print("NORDic MPBN_SIM, mutation_permanent IL6_tx='0'  (a genetic knockdown of the transcript):", nordic({"IL6_tx": "0"}))
print("NORDic MPBN_SIM, mutation_permanent RELA='0':      ", nordic({"RELA": "0"}))
print("-> in NORDic a drug and a knockout are the same call; the layer is whatever node the caller chose. A fixed 0 is not a dose, not an")
print("   exposure window, not partial inhibition, not a state-dependent effect.")
f, o = s.run_cell("damaging_mediator", prem, "none")
print("sim_q5 untreated (own mpbn call):", [s.summarise(a)["MYELIN_OL"] for a in o])
