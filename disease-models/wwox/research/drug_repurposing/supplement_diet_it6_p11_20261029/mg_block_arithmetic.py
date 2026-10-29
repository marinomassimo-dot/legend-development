#!/usr/bin/env python3
"""Back-of-envelope arithmetic for IT6-P11 (scientist-b, 2026-10-29). NOT a model of the burst and NOT a measurement.

Question: if the knockout pyramidal neuron rests about 5.6 mV more depolarised than the wild-type one (Table 1 of
PMID 34634460), how much more NMDAR conductance escapes the extracellular Mg2+ block at rest, and how much would a
modest rise in extracellular Mg2+ take away again?

Inputs, both read in the sources and both from OTHER cell types than the one the question concerns:
  * resting potentials, layer II/III pyramidal neurons, Wwox neuron-specific knockout slices, PMID 34634460 Table 1:
    wild type -79.25, heterozygote -75.51, knockout -73.62 mV (mean values as printed);
  * external Mg2+ IC50 of the whole-cell NMDA-evoked current, P7 rat substantia nigra dopaminergic neurons
    (J Physiol 2014, PMID 24614743, control condition): 20.9, 53.3, 173 micromolar at -90, -70, -50 mV.
Assumptions that are NOT from a source and are therefore UNVERIFIED for cortex: single-site occupancy
(Hill coefficient 1), log-linear voltage dependence of the IC50 between -90 and -70 mV, and that the IC50 of a mixed
GluN2B/GluN2D dopaminergic population stands for the GluN2A/GluN2B population of juvenile neocortex.
The recording ACSF Mg2+ is the incubation ACSF's 1.3 mM (the recording perfusate is not stated separately: UNVERIFIED).
"""
import sys as _sys
if len(_sys.argv) > 1 and _sys.argv[1] in ('-h', '--help'):
    print(__doc__)
    raise SystemExit(0)

import math, csv, sys

IC50 = {-90: 20.9, -70: 53.3, -50: 173.0}  # micromolar
slope = math.log(IC50[-70] / IC50[-90]) / 20.0  # per mV, between -90 and -70


def ic50(v):
    return IC50[-90] * math.exp(slope * (v + 90.0))


def unblocked(v, mg_mm):
    return 1.0 / (1.0 + (mg_mm * 1000.0) / ic50(v))


RMP = {"wild type": -79.25, "heterozygote": -75.51, "knockout": -73.62}
rows = []
for g, v in RMP.items():
    for mg in (1.0, 1.3, 1.5, 1.6, 1.7):
        rows.append([g, v, mg, round(ic50(v), 1), round(100 * unblocked(v, mg), 2)])
w = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
w.writerow(["genotype", "resting_potential_mV", "external_Mg_mM", "interpolated_IC50_uM", "unblocked_percent_of_Mg_free_current"])
w.writerows(rows)
print()
ko, wt = unblocked(RMP["knockout"], 1.3), unblocked(RMP["wild type"], 1.3)
print(f"knockout / wild type unblocked fraction at 1.3 mM: {ko / wt:.2f}")
for rise in (0.15, 0.30):
    mg = 1.3 * (1 + rise)
    print(f"knockout, Mg2+ raised by {int(rise * 100)} percent ({mg:.2f} mM): unblocked fraction falls to {unblocked(RMP['knockout'], mg) / ko:.2f} of its value at 1.3 mM")
print("a complete NMDAR block (d-APV in the source) would take this fraction to 0")
