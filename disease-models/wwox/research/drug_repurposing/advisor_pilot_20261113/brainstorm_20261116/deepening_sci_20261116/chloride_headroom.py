#!/usr/bin/env python3
"""I6 within-burst chloride model (hypothesis generator, not evidence; all constants ASSUMED unless noted).
One compartment, intracellular chloride c (mM). During a burst of duration D the GABA-A conductance is g(t) = g0*(1+pam) and chloride flows in at a rate
proportional to the driving force (V - E_Cl(c)); between and during bursts a first-order extrusion with time constant tau_c (KCC2) pulls c to c_eq.
E_Cl = -26.7 mV * ln(Cl_o / c) (Nernst at ~35 C, Cl_o = 130 mM: ASSUMED slice ACSF). V is the membrane potential of the cell during the burst (V_burst, ASSUMED -55 mV).
delta0 = the chloride rise (mM) produced by one baseline burst (pam 0) starting at c_eq = 6 mM: UNKNOWN, so it is scanned (0.5 to 8 mM).
    python3 chloride_headroom.py --help
    python3 chloride_headroom.py run <out_tsv> [V_rest_mV]   (default -65; the held S-WT and S-KO values are -79.25 and -73.62)
Outputs, per (c_eq, tau_c, delta0, pam): E_Cl at burst onset, at burst end, whether GABA-A has become depolarising relative to V_burst
(E_Cl > V_REF = -65 mV, i.e. depolarising from rest; influx stops at E_Cl = V_burst so E_Cl can approach but not pass V_burst), and the time inside the burst at which it crosses; plus the pre-burst chloride in the repeating regime (burst every 26.2 s)."""
import sys
if len(sys.argv) not in (3, 4) or sys.argv[1] != "run":
    print(__doc__); raise SystemExit(0)
import math
CL_O, VB, D, T_INT = 130.0, -55.0, 0.66, 26.2
V_REF = float(sys.argv[3]) if len(sys.argv) == 4 else -65.0   # resting potential used by the I1 model: GABA-A is depolarising from rest when E_Cl > V_REF
E = lambda c: -26.7 * math.log(CL_O / c)
def influx_const(delta0, ref_c=6.0, g=1.0):
    # chloride rise over D at pam 0 starting at ref_c, ignoring extrusion: delta0 = k*(VB-E(c))*D approx; calibrate k with the ref driving force
    return delta0 / ((VB - E(ref_c)) * D)
def burst(c0, k, pam, tau_c, c_eq, dt=0.002):
    c = c0; t = 0.0; cross = None
    while t < D:
        dc = k * (1 + pam) * (VB - E(c)) - (c - c_eq) / tau_c
        c = max(c + dt * dc, 1.0); t += dt
        if cross is None and E(c) > V_REF:
            cross = t
    return c, cross
def relax(c, c_eq, tau_c, T):
    return c_eq + (c - c_eq) * math.exp(-T / tau_c)
rows = []
for c_eq in (4.0, 6.0, 8.0, 10.0):
    for tau_c in (5.0, 15.0, 60.0):
        for delta0 in (0.5, 1.0, 2.0, 4.0, 8.0):
            k = influx_const(delta0)
            for pam in (0.0, 0.5, 1.0, 2.0):
                c = c_eq
                for _ in range(8):      # 8 bursts at the held interval reach the repeating regime for tau_c <= 60 s
                    pre = c
                    c_end, cross = burst(c, k, pam, tau_c, c_eq)
                    c = relax(c_end, c_eq, tau_c, T_INT - D)
                rows.append((c_eq, tau_c, delta0, pam, round(E(c_eq), 1), round(E(pre), 1), round(E(c_end), 1), "yes" if E(c_end) > V_REF else "no",
                             "" if cross is None else round(cross, 3)))
with open(sys.argv[2], "w") as f:
    f.write("c_eq_mM\ttau_c_s\tdelta0_mM\tpam\tE_Cl_at_c_eq_mV\tE_Cl_pre_burst_mV\tE_Cl_burst_end_mV\tdepolarising_by_end\tcross_time_s\n")
    for r in rows:
        f.write("\t".join(str(x) for x in r) + "\n")
print(len(rows), "rows")
# summary: the smallest pam that makes GABA-A depolarising before the burst ends, per (c_eq, delta0), tau_c = 15 s
for c_eq in (4.0, 6.0, 8.0, 10.0):
    line = []
    for d0 in (0.5, 1.0, 2.0, 4.0, 8.0):
        hit = [r[3] for r in rows if r[0] == c_eq and r[1] == 15.0 and r[2] == d0 and r[7] == "yes"]
        line.append(f"d0={d0}: {'pam>=' + str(min(hit)) if hit else 'none<=2'}")
    print(f"c_eq={c_eq} (E_Cl {E(c_eq):.1f} mV):", "; ".join(line))
