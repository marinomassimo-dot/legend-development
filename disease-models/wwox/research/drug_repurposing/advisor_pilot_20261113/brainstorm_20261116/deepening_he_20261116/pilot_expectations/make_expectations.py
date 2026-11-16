#!/usr/bin/env python3
"""Build the table of expected sign and size per pilot arm from the FROZEN model runs (I19 arms, OAT, GRID), as numbers read from the committed summaries.

    python3 make_expectations.py --runs <sim_harness/runs_20261116> --out <file.md>

Nothing is computed beyond ratios of medians over 20 seeds; the mapping of a pilot arm class to a model parameter step is SCI's labelling (scan_i19.json, scan_oat.json) and is an assumption, stated in the table. Not medical advice.
"""
import argparse, csv
from pathlib import Path
ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter); ap.add_argument("--runs"); ap.add_argument("--out"); a = ap.parse_args()
if not (a.runs and a.out):
    ap.print_help(); raise SystemExit(0)
R = Path(a.runs)
rd = lambda n: {r["point"]: r for r in csv.DictReader(open(R / n / "summary.tsv"), delimiter="\t")}
I19, OAT, GRID = rd("i19"), rd("oat"), rd("grid")
f = lambda x, nd=2: "n/a" if x in ("nan", "", None) else f"{float(x):.{nd}f}"
def ratio(a_, b_): return "n/a" if b_ in ("nan", "", None) or float(b_) == 0 or a_ in ("nan", "") else f"{float(a_) / float(b_):.2f}x"
ARMS = [(1, "GABA-A positive modulator, tonic-preferring (neurosteroid-type label)", "tonic GABA-A weight x1.2"), (7, "GABA-A positive modulator, synaptic-preferring (benzodiazepine-type / non-benzodiazepine label)", "phasic GABA-A weight x1.2"),
        (3, "NMDAR pore blocker or GluN2B NAM at a fractional block (the pore blocker and the NAM differ only in how much NMDAR current is removed)", "NMDAR weight x0.9"),
        (2, "T-type blocker (one protocol)", "T-type trigger weight x0.75"), (5, "T-type enhancer (the opposite step, as a model check; not a pilot arm)", "T-type trigger weight x1.25"),
        (4, "sodium-channel blocker, pyramidal component only (AH1 single-component arm)", "noise amplitude x0.9 (SCI's label: sigma x0.9)"), (6, "duration-only arm (resource-type; no pilot class named)", "resource depletion x0.6")]
b0, b1, b2 = I19["arm=0|geno=0"], I19["arm=0|geno=1"], I19["arm=0|geno=2"]
L = ["# Expected sign and size per pilot arm, from the frozen model runs (HE with SCI; draft for SCI to amend; 2026-11-16; hypothesis generator, not evidence; not medical advice)", "",
     "Written for: SCI (owner of the model and the brief), ADV. Source: `sim_harness/runs_20261116/{i19,oat,grid}` (20 seeds each, frozen by digest before the runs; K1-K6, S1-S7, G1-G2 all PASS). **Reading rule:** these are sizes of a model STEP (a parameter scaled by the factor shown), not of a drug at a dose; the class-to-parameter mapping is SCI's labelling and an assumption; a measured size that is much larger or of the other sign says the model lacks a term (for example an interneuron-specific sodium effect), which is itself the informative result. Written beside the brief's arms before any slice exists.", "",
     f"Baseline (no step): S-KO incidence {f(b0['incidence_median'])}, {f(b0['n_bursts_median'], 0)} bursts per 40 slices x 600 s (median over seeds), median burst duration {f(b0['dur_median_s_median'], 3)} s; S-HT incidence {f(b1['incidence_median'])} ({f(b1['n_bursts_median'], 0)} bursts); S-WT incidence {f(b2['incidence_median'])} ({f(b2['n_bursts_median'], 0)} bursts).", "",
     "## Per arm (I19 run; ratios are step over baseline at the same genotype)", "",
     "| pilot arm class | model step | S-KO: bursts (ratio) | S-KO: duration (ratio) | S-KO: bursts per bursting slice (ratio) | S-HT: incidence (baseline 0.20) | sign |", "|---|---|---|---|---|---|---|"]
for arm, cls, step in ARMS:
    k, h = I19[f"arm={arm}|geno=0"], I19[f"arm={arm}|geno=1"]
    d = "lower" if float(k["n_bursts_median"]) < float(b0["n_bursts_median"]) * 0.9 else ("higher" if float(k["n_bursts_median"]) > float(b0["n_bursts_median"]) * 1.1 else "about equal")
    L.append(f"| {cls} | {step} | {f(k['n_bursts_median'], 0)} ({ratio(k['n_bursts_median'], b0['n_bursts_median'])}) | {f(k['dur_median_s_median'], 3)} s ({ratio(k['dur_median_s_median'], b0['dur_median_s_median'])}) | {f(k['mean_bursts_in_bursting_slices_median'], 1)} ({ratio(k['mean_bursts_in_bursting_slices_median'], b0['mean_bursts_in_bursting_slices_median'])}) | {f(h['incidence_median'])} (silent seeds {f(h['fraction_silent'])}) | rate {d} |")
O = lambda p: OAT[p]
L += ["", "## Interval and duration separately (OAT, 40% steps; the I19 run reports no interval)", "",
      "| step | median interval (s) | median duration (s) | bursts per minute | reading for the brief's 6.2 table |", "|---|---|---|---|---|"]
for lab, pt, note in [("baseline", "base", ""), ("T-type trigger weight x0.6", "J_T-40", "interval UP, duration about equal: the T-type blocker prediction of H-B1"), ("T-type trigger weight x1.4", "J_T+40", "the opposite step"),
                      ("NMDAR (sustainer) weight x0.6", "J_N-40", "duration DOWN a lot and interval UP: the NMDAR arm moves both, mostly duration"), ("tonic GABA-A weight x1.4", "J_tonic+40", "the burst rate collapses (silent seeds)"),
                      ("phasic GABA-A weight x1.4", "J_I+40", "rate down, duration down: a synaptic-selective modulator shortens bursts too"), ("adenosine weight x0.6 / x1.4", "J_a-40", "a weak knob (see the I4 two-step design)")]:
    r = O(pt); L.append(f"| {lab} | {f(r['isi_median_s_median'], 1)} | {f(r['dur_median_s_median'], 3)} | {f(r['rate_per_min_median'])} | {note} |")
r = O("J_a+40"); L[-1] = L[-1].replace("| a weak knob (see the I4 two-step design) |", f"| x1.4: {f(r['rate_per_min_median'])} per minute against {f(O('base')['rate_per_min_median'])} baseline: a weak knob (see the I4 two-step design) |")
L += ["", "## GABA-A potentiation at graded steps (GRID; the sign question of the brief's HSCI-2)", "", "| pam (potentiation step) | S-KO bursts | silent seeds |", "|---|---|---|"]
for pt in ("load_coupling=0|pam=0", "load_coupling=0|pam=0.3", "load_coupling=0|pam=0.6", "load_coupling=1|pam=0.3"):
    g = GRID[pt]; L.append(f"| {pt.replace(chr(124), ', ')} | {f(g['n_bursts_median'], 0)} | {f(g['fraction_silent'])} |")
L += ["", "Reading: in this model a GABA-A potentiation suppresses bursts and does not raise them, with or without chloride-load coupling (G1 and G2 PASS); an observed RISE of the burst rate under a GABA-A positive modulator (HSCI-2) would be a result the model does not produce, and is the discriminating observation between the rebound-ignition and the restoration-of-inhibition pictures.", "",
      "## What each outcome would change (for the pilot's decision page)", "- A tonic-preferring step that suppresses more than a phasic-preferring step at the same fractional change (S-HT incidence 0.00 against 0.025; S-KO bursts ratio in the table): supports the tonic-brake reading (I13); the opposite order, or no difference, weakens it.", "- A T-type step that lengthens the interval without changing the duration, and an NMDAR step that shortens the duration: H-B1 (two-stage) as the model reads it; both moving in proportion: a single gain.", "- A sodium-channel step: the single-component noise arm (sigma x0.9) predicts SUPPRESSION; aggravation (AH1) is predicted only by the MIXED arm (pyramidal noise down AND interneuron inhibition down: SCI's arm 9, sigma x0.9 with J_I x0.7: S-KO bursts -12%, S-HT incidence 0.17 -> 0.38, S-WT 0.11 -> 0.25, predictions hashed first; see PILOT_ARM_EXPECTATIONS_SCI.md). Correction 2026-11-16 22:35Z (SCI): an earlier version of this line said the model lacks the term; it does not.", "", "Limits: model steps, not doses; 20 seeds of one frozen model; the labels that map a pilot arm to a parameter are assumptions; the S-HT incidence is the model's reading of the held 0/11, 4/23, 36/42 gradient, not a measurement."]
Path(a.out).write_text("\n".join(L) + "\n"); print("\n".join(L[:14]))
