#!/usr/bin/env python3
"""P9 arithmetic, stated as arithmetic (inputs named; nothing here is a measurement).
(1) d-APV occupancy at the concentration applied by Breton 2021 (50 uM), from ChEMBL equilibrium constants on rat
    recombinant GluN1/GluN2A-D in oocytes (two documents), assuming a competitive antagonist and agonist well below its
    EC50 (an UPPER bound on occupancy; endogenous glutamate in a slice lowers it by the factor 1+[A]/EC50).
(2) Memantine/ketamine potency ratio between two holding potentials in one document (ChEMBL assay descriptions).
(3) Mg2+ block of the NMDAR at the resting potentials of Table 1 of Breton 2021, with the Jahr-Stevens form
    B(V) = 1/(1 + ([Mg]/3.57 mM) * exp(-0.062 * V[mV])); the two constants are literature values NOT re-verified here.
(4) Counting time needed to estimate a burst rate, from the two baselines reported by Breton 2021 (main text 2.29 and Table S1 0.84 bursts/min).
Run: python3 arithmetic_p9.py > arithmetic_p9_output.txt"""
import json, math
from pathlib import Path
here = Path(__file__).parent
raw = json.loads((here / "toolcompound_raw.json").read_text())
print("(1) d-APV occupancy at 50 uM (upper bound, no agonist competition); Ki in nM from ChEMBL (CHEMBL84612)")
ki = {}
for r in raw["rows"]:
    if r["compound"].startswith("D-AP5") and r["standard_type"] == "Ki":
        ki.setdefault((r["document_chembl_id"], r["target_pref_name"]), float(r["standard_value"]))
for (doc, tgt), k in sorted(ki.items()):
    occ = 50000.0 / (50000.0 + k)
    print(f"  {doc}  {tgt:45s} Ki {k:8.0f} nM  occupancy {100*occ:5.1f}%  | with agonist at 1x EC50 (Ki doubled) {100*50000/(50000+2*k):5.1f}%")
print("\n(2) one document, two holding potentials (CHEMBL6083260, human GluN1/GluN2A or GluN1/GluN2B in HEK293, ChEMBL assay descriptions)")
pairs = {"memantine GluN2A": (840, 28070), "memantine GluN2B": (780, 25630), "ketamine GluN2A": (500, 53320), "ketamine GluN2B": (510, 15220)}
for k, (a, b) in pairs.items():
    print(f"  {k}: IC50 {a} nM at -60 mV, {b} nM at -40 mV  -> ratio {b/a:.0f}-fold for 20 mV")
print("\n(3) unblocked fraction at 1.3 mM Mg2+ (Breton incubation ACSF), Jahr-Stevens form (constants unverified)")
def unblocked(v, mg=1.3): return 1/(1 + (mg/3.57)*math.exp(-0.062*v))
for lab, v in [("wild type RMP -79.25 mV", -79.25), ("heterozygote RMP -75.51 mV", -75.51), ("knockout RMP -73.62 mV", -73.62)]:
    print(f"  {lab}: unblocked {100*unblocked(v):.2f}%  (x{unblocked(v)/unblocked(-79.25):.2f} vs wild type)")
print("  (means of Table 1 pyramidal neurons; the function is non-linear, so this illustrates direction and size, not a per-cell value)")
print("\n(4) counting time for a burst rate; the source reports TWO baselines for the same 119 bursts, 18 slices, 9 animals:")
print("    main text 2.29 [1.1-4.2] bursts/min (median interval 26.2 s) and supplementary Table S1 0.84 [0.57-1.53] bursts/min (min 0.36, max 3.89)")
for n in (10, 25, 50, 100):
    print(f"  {n:3d} bursts: {n/2.29:6.1f} min at 2.29/min, {n/0.84:6.1f} min at 0.84/min, {n/0.57:6.1f} min at 0.57/min; Poisson relative SE {100/math.sqrt(n):4.0f}%")
