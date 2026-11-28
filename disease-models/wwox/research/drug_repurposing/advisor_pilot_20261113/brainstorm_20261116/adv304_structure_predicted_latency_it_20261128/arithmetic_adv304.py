"""ADV-304 arithmetic (IT). Reads readbacks_adv304.tsv; applies the frozen relation f(g) = g*sqrt(-ln g) and the frozen calibration and decision rules.
Run: python3 -I arithmetic_adv304.py readbacks_adv304.tsv"""
import csv, math, sys
v = {r["quantity"]: float(r["value"]) for r in csv.DictReader(open(sys.argv[1]), delimiter="\t")}
f = lambda g: g * math.sqrt(-math.log(g))
print("CALIBRATION on Palma 2022 (WT callosum, P21; clemastine against vehicle)")
meas = v["palma_N1_velocity_clemastine"] / v["palma_N1_velocity_vehicle"]
print(f"  measured N1 velocity ratio {meas:.3f}  ln {math.log(meas):+.3f}")
for b in ("bin0_0.5", "bin0.5_1"):
    g1, g2 = v[f"palma_g_{b}_vehicle"], v[f"palma_g_{b}_clemastine"]
    pr = f(g2) / f(g1)
    ratio = abs(math.log(meas)) / abs(math.log(pr))
    ok = (math.log(pr) < 0) == (math.log(meas) < 0) and 0.5 <= ratio <= 2
    print(f"  {b}: g {g1}->{g2}  R-predicted ratio {pr:.4f} ln {math.log(pr):+.4f}  |ln measured|/|ln predicted| = {ratio:.1f}  usable by the frozen rule: {ok}")
print("APPLICATION to Wwox (NOT validated if calibration fails; descriptive only). Control latency", v["repudi_N1_latency_control"], "ms; readback difference", round(v["repudi_N1_latency_ko"] - v["repudi_N1_latency_control"], 2), "ms")
for d in ("0.5um", "1.0um", "1.5um"):
    gc, gk = v[f"repudi_g_control_{d}"], v[f"repudi_g_ko_{d}"]
    vr = f(gk) / f(gc); shift = (1 / vr - 1) * v["repudi_N1_latency_control"]
    lo = (1 / (f(gk + 0.015) / f(gc - 0.015)) - 1) * v["repudi_N1_latency_control"]; hi = (1 / (f(gk - 0.015) / f(gc + 0.015)) - 1) * v["repudi_N1_latency_control"]
    print(f"  diameter {d}: g {gc}->{gk}  velocity ratio {vr:.3f}  predicted shift {shift:+.2f} ms  (g +-0.015 each: {lo:+.2f} to {hi:+.2f})")
