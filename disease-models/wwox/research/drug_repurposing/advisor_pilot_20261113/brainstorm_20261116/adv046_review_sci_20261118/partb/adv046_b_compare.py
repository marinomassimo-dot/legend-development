#!/usr/bin/env python3
"""ADV-046 part B: do the existing models tell single from combined mechanisms, and explanations that give the same observable?

HYPOTHESIS GENERATOR, NOT EVIDENCE. Mechanism level only. No dose, no agent. Reference genotype class only. numpy only; seeded.
Protocol, definitions, predictions and decision rules: PART_B_PREREGISTRATION_ADV046_SCI_20261118.md (hashed before any run).
No term and no state variable is added to the held models. rebound_oscillator.py and homeostat_toy.py are imported unchanged
and their sha256 are checked at start. Everything the script varies is an existing parameter or a prescribed waveform:
  depth d      : J_N x (1 - d)                       (existing weight; the map from the evoked-response depth to d is ASSUMED linear)
  Ih knob      : hcn_block (existing parameter; hyperpolarising drive removal; no sag variable exists)
  disinhibition: phasic_gain = max(0, 1 - e d)       (existing parameter; the coupling e is an ASSUMED swept value, not a model term)
  slow unblock : a prescribed J_N(t) waveform         (kinetics are NOT REPRESENTED as a state; the waveform is an input)
  adaptation   : the held homeostat toy (w on J_A and J_N), tau_w as in the held toy
Modes: --smoke | --part1 SEED OUT | --part2 OUT [--workers N] | --decide P1A P1B P2 OUT
"""
import argparse
import hashlib
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.normpath(os.path.join(HERE, "..", "..", "deepening_sci_20261116"))
sys.path.insert(0, MODEL_DIR)

HELD = {
    "rebound_oscillator.py": "c050b8ff0a1ba8fe5ef340f2a57168ecf578f161be12392c42fec98851b89419",
    "homeostat_toy.py": "a48855081414110fb02b5c58550844b54225f3bf548dcf40da676df36e0ac420",
}


def check_models():
    for name, want in HELD.items():
        got = hashlib.sha256(open(os.path.join(MODEL_DIR, name), "rb").read()).hexdigest()
        if got != want:
            raise SystemExit("model file changed: %s %s" % (name, got))


check_models()
from rebound_oscillator import BASE, simulate  # noqa: E402
import homeostat_toy as ht  # noqa: E402

# ---------------- part 1: steady state, burst rate against matched NMDAR depth ----------------
DEPTHS = [0.0, 0.05, 0.10, 0.15, 0.20, 0.30, 0.50]
HCN = [0.1, 0.2, 0.4]
ECOUP = [2.0, 4.0, 8.0, 16.0]
NREP = 40
T1 = 600.0
BURN1 = 60.0
BAND = (0.7, 1.3)
FLOOR = 0.15
NBOOT = 2000


def p1_sets():
    sets = []
    for d in DEPTHS:
        sets.append(dict(kind="C0", d=d, hcn=0.0, e=0.0))
    for h in HCN:
        for d in DEPTHS:
            sets.append(dict(kind="C1", d=d, hcn=h, e=0.0))
    for e in ECOUP:
        for d in DEPTHS:
            sets.append(dict(kind="C2", d=d, hcn=0.0, e=e))
    return sets


def part1(seed):
    sets = p1_sets()
    P = dict(BASE)
    P["J_N"] = np.array([BASE["J_N"] * (1.0 - s["d"]) for s in sets])
    P["hcn_block"] = np.array([s["hcn"] for s in sets])
    P["phasic_gain"] = np.array([max(0.0, 1.0 - s["e"] * s["d"]) for s in sets])
    res = simulate(P, T1, seed, nrep=NREP, burn=BURN1)
    counts = []
    for i in range(len(sets)):
        grp = res[i * NREP:(i + 1) * NREP]
        counts.append([sum(1 for dd in d if dd > 0.1) for (o, d) in grp])
    counts = np.array(counts, float)  # (sets, networks): bursts per network over T1
    rng = np.random.default_rng(seed + 1)
    ctrl = counts[0]
    out = []

    def boot_ratio(num, den):
        a = rng.integers(0, len(num), (NBOOT, len(num)))
        b = rng.integers(0, len(den), (NBOOT, len(den)))
        n = num[a].mean(1)
        m = den[b].mean(1)
        ok = m > 0
        r = n[ok] / m[ok]
        return float(np.quantile(r, 0.025)), float(np.quantile(r, 0.975))

    for i, s in enumerate(sets):
        c0 = counts[i]
        row = dict(s)
        row["rate_per_min"] = float(c0.mean() / (T1 / 60.0))
        row["ratio_ctrl"] = float(c0.mean() / ctrl.mean())
        lo, hi = boot_ratio(c0, ctrl)
        row["ratio_ctrl_ci"] = [lo, hi]
        row["silent_frac"] = float((c0 == 0).mean())
        # same depth, J_N only (d-APV-like reference)
        j = [k for k, t in enumerate(sets) if t["kind"] == "C0" and t["d"] == s["d"]][0]
        ref = counts[j]
        row["ratio_vs_C0_same_depth"] = float(c0.mean() / ref.mean()) if ref.mean() > 0 else None
        if ref.mean() > 0 and c0.mean() > 0:
            row["ratio_vs_C0_ci"] = list(boot_ratio(c0, ref))
        else:
            row["ratio_vs_C0_ci"] = None
        out.append(row)
    return dict(seed=seed, nrep=NREP, T=T1, rows=out)


# ---------------- part 2: time course after washout ----------------
F = 0.3          # J_N multiplier during the exposure (the held toy cell used 0.3)
D_HOLD = 1800.0
RAMP = ht.RAMP
POST = 7200.0
WIN = [("W1", 0.0, 1800.0), ("W2", 1800.0, 3600.0), ("W3", 3600.0, 7200.0)]  # seconds after the start of washout
CELLS = [
    dict(id="K0", tau_w=None, tau_off=None),
    dict(id="K1_10", tau_w=None, tau_off=600.0),
    dict(id="K1_20", tau_w=None, tau_off=1200.0),
    dict(id="K1_40", tau_w=None, tau_off=2400.0),
    dict(id="K1_80", tau_w=None, tau_off=4800.0),
    dict(id="K2_3600", tau_w=3600.0, tau_off=None),
    dict(id="K2_1800", tau_w=1800.0, tau_off=None),
    dict(id="K3_3600_20", tau_w=3600.0, tau_off=1200.0),
    dict(id="K3_3600_40", tau_w=3600.0, tau_off=2400.0),
    dict(id="K3_1800_20", tau_w=1800.0, tau_off=1200.0),
]


def make_m(tau_off):
    t_dn0 = ht.BURN + ht.PRE
    t_dn1 = t_dn0 + RAMP
    t_up0 = t_dn1 + D_HOLD

    def m(t):
        if t < t_dn0:
            return 1.0
        if t < t_dn1:
            return 1.0 + (F - 1.0) * (t - t_dn0) / RAMP
        if t < t_up0:
            return F
        if tau_off is None:
            if t < t_up0 + RAMP:
                return F + (1.0 - F) * (t - t_up0) / RAMP
            return 1.0
        return 1.0 - (1.0 - F) * float(np.exp(-(t - t_up0) / tau_off))
    return m, t_dn1, t_up0


def cell2(spec, a0):
    m, t_dn1, t_up0 = make_m(spec["tau_off"])
    T = t_up0 + POST
    res, um, wt = ht.run(m, T, ht.N_NET, ht.SEED, spec["tau_w"], a0)
    pre = ht.rate(res, ht.BURN, ht.BURN + ht.PRE)
    out = dict(spec)
    out["rate_pre"] = pre
    out["hold_over_pre"] = ht.rate(res, t_dn1, t_up0) / pre if pre > 0 else None
    wins = {}
    for name, a, b in WIN:
        t0, t1 = t_up0 + a, t_up0 + b
        r = ht.rate(res, t0, t1) / pre if pre > 0 else None
        es = [m(t) * w for (t, w) in wt if t0 <= t < t1]
        wins[name] = dict(rate_over_pre=r, E=float(np.mean(es)) if es else None)
    out["windows"] = wins
    # held-toy integrity quantities (same boundaries as RESULT_HOMEOSTAT_TOY: t_up1 = t_up0 + RAMP)
    t_up1 = t_up0 + RAMP
    out["early_held_def"] = ht.rate(res, t_up1, t_up1 + 120.0) / pre
    out["mid_held_def"] = ht.rate(res, t_up1 + 120.0, t_up1 + 720.0) / pre
    return out


def _work(args):
    spec, a0 = args
    return cell2(spec, a0)


def part2(workers):
    a0 = ht.calibrate()
    jobs = [(c, a0) for c in CELLS]
    if workers > 1:
        import multiprocessing as mp
        with mp.Pool(workers) as pool:
            rows = pool.map(_work, jobs)
    else:
        rows = [_work(j) for j in jobs]
    return dict(a0=a0, f=F, D=D_HOLD, post=POST, cells=rows)


# ---------------- decision: the frozen statements ----------------
def rclass(x):
    if x is None:
        return None
    return "below" if x < 0.7 else ("above" if x > 1.3 else "within")


def eclass(x, band):
    if x is None:
        return None
    return "below" if x < 1 - band else ("above" if x > 1 + band else "within")


def _get(p1, kind, d, hcn=0.0, e=0.0):
    for r in p1["rows"]:
        if r["kind"] == kind and abs(r["d"] - d) < 1e-9 and abs(r["hcn"] - hcn) < 1e-9 and abs(r["e"] - e) < 1e-9:
            return r
    raise KeyError((kind, d, hcn, e))


def distinguishable(r):
    """vs the same-depth J_N-only cell: point outside BAND and CI excluding 1; floor cells are not distinguishable."""
    c0 = r["_c0"]
    if r["ratio_ctrl"] < FLOOR and c0 < FLOOR:
        return None  # floor
    q = r["ratio_vs_C0_same_depth"]
    ci = r["ratio_vs_C0_ci"]
    if q is None or ci is None:
        return None
    if q < BAND[0] and ci[1] < 1.0:
        return "below"
    if q > BAND[1] and ci[0] > 1.0:
        return "above"
    return "no"


def attach_c0(p1):
    for r in p1["rows"]:
        r["_c0"] = _get(p1, "C0", r["d"])["ratio_ctrl"]


def decide(p1a, p1b, p2):
    attach_c0(p1a)
    attach_c0(p1b)
    out = {}
    per = {}
    for tag, p1 in (("A", p1a), ("B", p1b)):
        s = {}
        deep = [r for r in p1["rows"] if abs(r["d"] - 0.5) < 1e-9]
        s["B1"] = all(r["ratio_ctrl"] <= FLOOR for r in deep)
        mid_depths = [0.05, 0.10, 0.15, 0.20, 0.30]
        for key, h in (("B2a", 0.1), ("B2b", 0.2)):
            n = sum(1 for d in mid_depths if distinguishable(_get(p1, "C1", d, hcn=h)) == "below")
            s[key] = n >= 2
        low = [0.05, 0.10, 0.15, 0.20]
        above = any(distinguishable(_get(p1, "C2", d, e=e)) == "above" for d in low for e in ECOUP)
        below = any(distinguishable(_get(p1, "C1", d, hcn=h)) == "below" for d in low for h in HCN)
        s["B3"] = bool(above and below)

        def rises(e):
            ctrl_ok = False
            for d in [0.05, 0.10, 0.15, 0.20, 0.30]:
                r = _get(p1, "C2", d, e=e)
                if r["ratio_ctrl"] >= 1.2 and r["ratio_ctrl_ci"][0] > 1.0:
                    ctrl_ok = True
            return ctrl_ok
        s["B4a"] = not (rises(2.0) or rises(4.0))
        s["B4b"] = rises(8.0)
        s["B4c"] = rises(16.0)
        ok = True
        for h in (0.2, 0.4):
            alone = _get(p1, "C1", 0.0, hcn=h)["ratio_ctrl"]
            for d in (0.10, 0.15):
                comb = _get(p1, "C1", d, hcn=h)["ratio_ctrl"]
                c0 = _get(p1, "C0", d)["ratio_ctrl"]
                if comb <= 0 or alone <= 0 or c0 <= 0:
                    ok = False
                    continue
                if abs(np.log(comb) - np.log(c0) - np.log(alone)) > 0.25:
                    ok = False
        s["B5"] = ok
        per[tag] = s
    for k in per["A"]:
        out[k] = dict(A=per["A"][k], B=per["B"][k], value=bool(per["A"][k] and per["B"][k]))
    # part 2
    cells = {c["id"]: c for c in p2["cells"]}

    def rc(cid, w):
        return rclass(cells[cid]["windows"][w]["rate_over_pre"])
    out["B6"] = dict(value=0.9 <= cells["K0"]["windows"]["W2"]["rate_over_pre"] <= 1.1)
    out["B7"] = dict(value=(rc("K1_20", "W2") == "within" and rc("K1_40", "W2") == "below"))
    out["B8"] = dict(value=(rc("K2_3600", "W2") == "above" and rc("K2_1800", "W2") == "above"))
    out["B9"] = dict(value=(any(rc(c, "W2") == "below" for c in cells if c.startswith("K1"))
                            and any(rc(c, "W2") == "above" for c in cells if c.startswith("K2"))))
    canc = []
    for cid in cells:
        if not cid.startswith("K3"):
            continue
        _, tw, to = cid.split("_")
        k1 = "K1_" + to
        k2 = "K2_" + tw
        for w in ("W1", "W2", "W3"):
            r3 = cells[cid]["windows"][w]["rate_over_pre"]
            r1 = cells[k1]["windows"][w]["rate_over_pre"] if k1 in cells else None
            r2 = cells[k2]["windows"][w]["rate_over_pre"] if k2 in cells else None
            if r1 is None or r2 is None or r3 is None:
                continue
            if 0.9 <= r3 <= 1.1 and not (0.9 <= r1 <= 1.1) and not (0.9 <= r2 <= 1.1):
                canc.append((cid, w, r3, r1, r2))
    out["B10"] = dict(value=len(canc) > 0, cases=canc)
    # E-class table at both bands, and rate classes, for the report (not scored)
    table = {}
    for cid, c in cells.items():
        table[cid] = {w: dict(rate=c["windows"][w]["rate_over_pre"], rate_class=rclass(c["windows"][w]["rate_over_pre"]),
                              E=c["windows"][w]["E"], E_class_10=eclass(c["windows"][w]["E"], 0.10),
                              E_class_5=eclass(c["windows"][w]["E"], 0.05)) for w in ("W1", "W2", "W3")}
    out["table_part2"] = table
    # informativeness verdict
    for tag, p1 in (("A", p1a), ("B", p1b)):
        ok = False
        for d in [0.05, 0.10, 0.15, 0.20, 0.30]:
            c0 = _get(p1, "C0", d)["ratio_ctrl"]
            for h in HCN:
                if c0 >= FLOOR and distinguishable(_get(p1, "C1", d, hcn=h)) == "below":
                    ok = True
        out["INF1_" + tag] = ok
    out["INF1"] = out["INF1_A"] and out["INF1_B"]
    out["INF2"] = out["B9"]["value"]
    out["VERDICT"] = "INFORMATIVE" if (out["INF1"] and out["INF2"]) else ("PARTLY" if (out["INF1"] or out["INF2"]) else "NOT INFORMATIVE")
    return out


def held_check(p2):
    held = json.load(open(os.path.join(MODEL_DIR, "homeostat_toy_cells.json")))["c_3600_1800"]
    c = [x for x in p2["cells"] if x["id"] == "K2_3600"][0]
    return dict(early_new=c["early_held_def"], early_held=held["early"], mid_new=c["mid_held_def"], mid_held=held["mid"],
                rate_pre_new=c["rate_pre"], rate_pre_held=held["rate_pre"], hold_new=c["hold_over_pre"],
                a0_new=p2["a0"], a0_held=held["a0"])


def main(argv=None):
    ap = argparse.ArgumentParser(description="ADV-046 part B (hypothesis generator, not evidence).")
    ap.add_argument("--smoke", action="store_true")
    ap.add_argument("--part1", nargs=2, metavar=("SEED", "OUT"))
    ap.add_argument("--part2", metavar="OUT")
    ap.add_argument("--workers", type=int, default=1)
    ap.add_argument("--decide", nargs=4, metavar=("P1A", "P1B", "P2", "OUT"))
    a = ap.parse_args(argv)
    if a.smoke:
        P = dict(BASE)
        simulate(P, 5.0, 1, nrep=2, burn=1.0)
        ht.run(lambda t: 1.0, 5.0, 2, 1, 600.0, 0.1)
        print("smoke ok", len(p1_sets()), "part1 sets;", len(CELLS), "part2 cells")
        return 0
    if a.part1:
        json.dump(part1(int(a.part1[0])), open(a.part1[1], "w"), indent=1)
        print("part1 done")
        return 0
    if a.part2:
        json.dump(part2(a.workers), open(a.part2, "w"), indent=1)
        print("part2 done")
        return 0
    if a.decide:
        p1a = json.load(open(a.decide[0]))
        p1b = json.load(open(a.decide[1]))
        p2 = json.load(open(a.decide[2]))
        res = decide(p1a, p1b, p2)
        res["held_check"] = held_check(p2)
        json.dump(res, open(a.decide[3], "w"), indent=1, default=float)
        print(res["VERDICT"])
        return 0
    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
