#!/usr/bin/env python3
"""I13/I8: which single change reproduces the held layer II/III pyramidal intrinsic profile of the Wwox S-KO (Breton 2021 Table 1)?
Single-compartment conductance model (hypothesis generator, not evidence; every conductance ASSUMED; tuned only to the WILD-TYPE row by a seeded random search).
    python3 intrinsic_profile_model.py --help
    python3 intrinsic_profile_model.py run <out_tsv>
Held targets (S-WT / S-HT / S-KO means): RMP -79.25 / -75.51 / -73.62 mV; input resistance 102.9 / 143.3 / 143.0 MOhm; tau 18.55 / 18.79 / 21.25 ms (ns);
sag at -200 pA 1.18 / 2.04 / 2.57 mV; post-inhibitory rebound 0.96 / 1.24 / 1.86 mV (HT ns). Sag = steady state minus most negative deflection (the paper's definition);
rebound = peak after the pulse minus the mean before it; the -200 pA pulse is assumed 500 ms long (not stated in the text read: ASSUMED).
Components: resting K+ leak gK (E -97), tonic GABA-A gG (E -80), non-selective cation leak gC (E -20), HCN-like Ih gh (E -35), T-type-like gT (E +50), capacitance C.
Rin and tau are read from the instantaneous conductance at rest (gates frozen), sag and rebound from a time simulation."""
import sys
if len(sys.argv) != 3 or sys.argv[1] != "run":
    print(__doc__); raise SystemExit(0)
import numpy as np
DT = 0.2  # ms
sig = lambda x: 1.0/(1.0+np.exp(-x))
def gates_inf(V):
    return sig(-(V+85)/7), sig(-(V+57)/6.2), sig((-(V+81))/4*-1*-1) if False else 1/(1+np.exp((V+81)/4))
def i_ion(V, mh, hT, P):
    mT = sig((V+57)/6.2)
    return P["gK"]*(V+97) + P["gG"]*(V+80) + P["gC"]*(V+20) + P["gh"]*mh*(V+35) + P["gT"]*mT**2*hT*(V-50)
def rest(P):
    lo, hi = -100.0, -40.0
    for _ in range(60):
        V = 0.5*(lo+hi); mh = 1/(1+np.exp((V+85)/7)); hT = 1/(1+np.exp((V+81)/4))
        if i_ion(V, mh, hT, P) > 0: hi = V
        else: lo = V
    return 0.5*(lo+hi)
def g_inst(V, P):
    mh = 1/(1+np.exp((V+85)/7)); hT = 1/(1+np.exp((V+81)/4)); e = 0.01
    return (i_ion(V+e, mh, hT, P) - i_ion(V-e, mh, hT, P))/(2*e)
def g_ss(V, P):
    e = 0.01
    f = lambda v: i_ion(v, 1/(1+np.exp((v+85)/7)), 1/(1+np.exp((v+81)/4)), P)
    return (f(V+e) - f(V-e))/(2*e)
def pulse_sim(P, V0, I=-200.0, Tp=300.0, Tpulse=500.0, Tpost=300.0):
    V = V0; mh = 1/(1+np.exp((V+85)/7)); hT = 1/(1+np.exp((V+81)/4)); n = int((Tp+Tpulse+Tpost)/DT); out = np.empty(n)
    for i in range(n):
        t = i*DT; Ii = I if Tp <= t < Tp+Tpulse else 0.0
        V += DT*(Ii - i_ion(V, mh, hT, P))/P["C"]
        mh += DT*(1/(1+np.exp((V+85)/7)) - mh)/150.0; hT += DT*(1/(1+np.exp((V+81)/4)) - hT)/50.0
        out[i] = V
    return out
def metrics(P):
    V0 = rest(P); rin = 1000.0/g_ss(V0, P); tau = P["C"]*1000.0/(g_inst(V0, P)*1000.0)*1.0
    tr = pulse_sim(P, V0); a = int(300/DT); b = int(800/DT)
    base = tr[a-int(50/DT):a].mean(); pulse = tr[a:b]; ss = pulse[-int(50/DT):].mean(); sag = ss - pulse.min(); reb = tr[b:].max() - base
    return V0, rin, tau, sag, reb
TARGET = (-79.25, 102.88, 18.55, 1.18, 0.96)
rng = np.random.default_rng(13)
best = None
for _ in range(3000):
    P = dict(gK=rng.uniform(2, 9), gG=rng.uniform(0.3, 4.0), gC=rng.uniform(0.2, 2.5), gh=rng.uniform(0.1, 4.0), gT=rng.uniform(1, 40), C=100.0)
    V0 = rest(P); G = g_inst(V0, P)
    if G <= 0: continue
    P["C"] = 18.55*G   # pF when G in nS and tau in ms: tau = C/G
    m = metrics(P)
    loss = abs(m[0]-TARGET[0])/1.0 + 3.0*abs(np.log(m[1]/TARGET[1])) + abs(m[2]-TARGET[2])/18.55 + abs(m[3]-TARGET[3]) + abs(m[4]-TARGET[4])
    if best is None or loss < best[0]: best = (loss, P, m)
WT = best[1]
manips = [("tonic GABA-A conductance gG x0.0", {"gG": 0.0}), ("tonic GABA-A conductance gG x0.5", {"gG": WT["gG"]*0.5}),
          ("K+ leak gK x0.5", {"gK": WT["gK"]*0.5}), ("K+ leak gK x0.7", {"gK": WT["gK"]*0.7}),
          ("HCN-like Ih gh x2", {"gh": WT["gh"]*2}), ("HCN-like Ih gh x0.5", {"gh": WT["gh"]*0.5}),
          ("T-type-like gT x2", {"gT": WT["gT"]*2}), ("capacitance x0.72 (smaller cell, tau kept by lower C)", {"C": WT["C"]*0.72}),
          ("cation leak gC x0.0", {"gC": 0.0}),
          ("cell size x0.72 (every conductance and C x0.72: same densities, smaller cell)", {k: WT[k]*0.72 for k in ("gK","gG","gC","gh","gT","C")}),
          ("cell size x0.72 and K+ leak density x0.85", {**{k: WT[k]*0.72 for k in ("gG","gC","gh","gT","C")}, "gK": WT["gK"]*0.72*0.85}), ("gG x0.5 and gh x1.5", {"gG": WT["gG"]*0.5, "gh": WT["gh"]*1.5})]
with open(sys.argv[2], "w") as f:
    f.write("manipulation\tRMP_mV\tRin_MOhm\ttau_ms\tsag_mV\trebound_mV\n")
    f.write("HELD S-WT mean\t-79.25\t102.88\t18.55\t1.18\t0.96\nHELD S-HT mean\t-75.51\t143.26\t18.79\t2.04\t1.24\nHELD S-KO mean\t-73.62\t143.03\t21.25\t2.57\t1.86\n")
    f.write("model WT (tuned to the WT row)\t" + "\t".join(f"{x:.2f}" for x in best[2]) + "\n")
    for name, ch in manips:
        m = metrics(dict(WT, **ch)); f.write(name + "\t" + "\t".join(f"{x:.2f}" for x in m) + "\n")
print(open(sys.argv[2]).read()); print("WT parameters:", {k: round(v, 2) for k, v in WT.items()})
