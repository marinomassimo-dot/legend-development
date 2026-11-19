#!/usr/bin/env python3
"""PARAMETRIC SENSITIVITY of the simulated class order (HE, ADV-096, 2026-11-19; hypothesis generator, not evidence; not medical advice.)

    python3 parametric_sensitivity.py scan OUT_SCAN.json [--stage baseline|rest|full]   the scan the harness freezes: one bisect cell per variant and class, S-KO
    python3 parametric_sensitivity.py report RUN_DIR [--published PUBLISHED_SUMMARY.tsv]

Uses sim_harness.py's own `fixed` block per bisect cell: no change to the harness, to SCI's frozen model or to the published bisect folder. Variants: the baseline; four parameters at a low and a high value,
one at a time; three JOINT scenarios chosen for biological meaning. Every variant is a PARAMETER change of the one circuit structure: no structural alternative (a different circuit element) is built.
**Kv7 is NOT in the model: kv7_offset is an ASSUMED stand-in (a drive offset), not a current.** Each class is reported on two scales. The MULTIPLIER scale (the fractional change of the targeted parameter
at which the burst count halves) is the primary one. The STRENGTH scale s uses a different listed multiplier per arm (e.g. d-APV J_N x0.3, NMDAR pore blocker J_N x0.8), so an order in s is partly IMPOSED by
those coefficients and its stability is not read as superiority; two classes that move the same parameter and whose brackets overlap tie on the multiplier scale. The metric itself is a choice: the key is |ln multiplier|, symmetric for a decrease and an increase; in percent AMPA (-27%) and synaptic GABA-A (+37%) would swap, so their relative order is metric-dependent. Across different parameters the multiplier
scale says only how large a change the model needs, not which class is better. A class that keeps its rank is robust to THESE parameters only, not shown correct. Crossing is a model step, not a dose."""
from __future__ import annotations
import csv, json, math, statistics, sys
from collections import defaultdict
from pathlib import Path

CLASSES = {1: "d-APV-type", 2: "NMDAR pore", 4: "AMPA", 5: "T-type", 6: "synaptic GABA-A", 7: "neurosteroid-type", 8: "sodium (pyramidal)"}
ARM = {1: {"J_N": 0.3}, 2: {"J_N": 0.8}, 4: {"J_A": 0.8}, 5: {"J_T": 0.75}, 6: {"J_I": 1.2}, 7: {"J_tonic": 1.2, "J_I": 1.1}, 8: {"sigma": 0.9}}   # as in the frozen adapter (checked by the test)
ONE = {"ji_mult": (0.5, 1.5), "cl_tau_mult": (0.5, 2.0), "nmda_mult": (0.8, 1.25), "kv7_offset": (-0.05, 0.05)}
JOINT = {"joint_highCl_lowInh": {"cl_tau_mult": 2.0, "ji_mult": 0.5}, "joint_hyperexcitable": {"nmda_mult": 1.25, "kv7_offset": 0.05},
         "joint_inhibited": {"nmda_mult": 0.8, "kv7_offset": -0.05, "cl_tau_mult": 0.5}}
NOTE = "Kv7 is NOT in the model: kv7_offset is an ASSUMED stand-in. Parameter changes of one structure, not structural alternatives. A class that keeps its rank is robust to these parameters only, not shown correct. A crossing is a model step, not a dose."


def variants(stage: str) -> dict[str, dict[str, float]]:
    out: dict[str, dict[str, float]] = {} if stage == "rest" else {"base": {}}
    if stage in ("full", "rest"):
        for name, (lo, hi) in ONE.items():
            out[f"{name}_lo"], out[f"{name}_hi"] = {name: lo}, {name: hi}
        out.update(JOINT)
    return out


def scan(stage: str, iterations: int = 5) -> dict:
    cells = [{"label": f"{v}__arm{a}", "fixed": {"arm": a, "geno": 0, **fx}, "observable": "rel_bursts", "threshold": 0.5, "direction": "crosses below", "note": f"{CLASSES[a]}, S-KO, variant {v}"}
             for v, fx in variants(stage).items() for a in CLASSES]
    return {"design": "bisect", "bisect": {"parameter": "strength", "bracket": [0.0, 3.0], "iterations": iterations, "cells": cells}, "predictions": [], "caveats": NOTE}


def ranks(vals: dict[int, float]) -> dict[int, float]:
    order = sorted(vals, key=lambda a: vals[a]); out: dict[int, float] = {}; i = 0
    while i < len(order):
        j = i
        while j + 1 < len(order) and vals[order[j + 1]] == vals[order[i]]:
            j += 1
        for k in order[i:j + 1]:
            out[k] = (i + j) / 2 + 1
        i = j + 1
    return out


def tau(x: dict[int, float], y: dict[int, float]) -> float:
    ks = sorted(x); c = d = tx = ty = 0
    for i, a in enumerate(ks):
        for b in ks[i + 1:]:
            s, t = (x[a] > x[b]) - (x[a] < x[b]), (y[a] > y[b]) - (y[a] < y[b])
            c += s * t > 0; d += s * t < 0; tx += s == 0 and t != 0; ty += t == 0 and s != 0
    den = math.sqrt((c + d + tx) * (c + d + ty))
    return (c - d) / den if den else float("nan")


def mult_ranks(rows: dict[int, tuple[float, float, float]]) -> dict[int, float]:
    """Ranks on the MULTIPLIER scale: key |ln m| of each class's first (primary) parameter at its crossing (smaller = the model needs a smaller change). A class not crossing within the bracket has the key of its
    far end (a lower bound) and sits last. Two classes on the SAME parameter whose brackets overlap are tied."""
    key = {}; span = {}
    for a, (s, lo, hi) in rows.items():
        p, m = next(iter(ARM[a].items())); far = math.isinf(s); s_ = 3.0 if far else s
        key[a] = abs(s_ * math.log(m)) + (1e3 if far else 0.0); span[a] = sorted(abs(x * math.log(m)) for x in ((0.0, 3.0) if far else (lo, hi)))
    for a in rows:
        for b in rows:
            if a < b and next(iter(ARM[a])) == next(iter(ARM[b])) and key[a] < 1e3 and key[b] < 1e3 and span[a][0] <= span[b][1] and span[b][0] <= span[a][1]:
                key[a] = key[b] = (key[a] + key[b]) / 2
    return ranks(key)


def table(name: str, rk: dict[str, dict[int, float]], est: dict, lines: list[str]) -> None:
    b = rk["base"]; others = [v for v in rk if v != "base"]; taus = {v: tau(b, rk[v]) for v in others}
    if not others:
        lines.append(f"-- {name}: baseline only, order: " + " < ".join(f"{CLASSES[a]} ({b[a]:g})" for a in sorted(b, key=b.get)))
        return
    lines.append(f"-- {name}: class | variants keeping the baseline rank | rank range (baseline) | tau to baseline (min, median)")
    for a in sorted(b, key=b.get):
        rs = [rk[v][a] for v in others]
        lines.append(f"{CLASSES[a]} | {sum(r == b[a] for r in rs)}/{len(others)} | {min(rs):g} to {max(rs):g} ({b[a]:g}) | {min(taus.values()):.2f}, {statistics.median(taus.values()):.2f}")
    win = [a for a in b if b[a] == 1.0]
    flips = [v for v in others if [a for a in rk[v] if rk[v][a] == 1.0] != win]
    lines.append(f"winner (rank 1) at baseline: {', '.join(CLASSES[a] for a in win)}; variants that change it: {', '.join(flips) if flips else 'none'}")


def report(run: Path, published: Path | None = None) -> str:
    est: dict[str, dict[int, tuple[float, float, float]]] = defaultdict(dict)
    for r in csv.DictReader(open(run / "summary.tsv"), delimiter="\t"):
        v, a = r["point"].split("__arm"); ok = r["status"] == "crossed"
        est[v][int(a)] = (float(r["estimate"]) if ok else math.inf, float(r["bracket_lo"]), float(r["bracket_hi"]))
    full = {v: e for v, e in est.items() if len(e) == len(CLASSES)}
    lines = [f"PARAMETRIC SENSITIVITY, S-KO, {len(full)} complete variants of {len(est)}. {NOTE}"]
    if "base" not in full:
        return "\n".join(lines + ["no complete baseline variant: nothing to compare"])
    rk_s = {v: ranks({a: x[0] for a, x in e.items()}) for v, e in full.items()}; rk_m = {v: mult_ranks(e) for v, e in full.items()}
    b = full["base"]
    lines.append("Baseline crossing, per class: " + "; ".join(f"{CLASSES[a]} " + (f"s {b[a][0]:.3f}, {next(iter(ARM[a]))} x{ARM[a][next(iter(ARM[a]))] ** b[a][0]:.3f}" if b[a][0] < math.inf else f"not in [0,3] ({next(iter(ARM[a]))} beyond x{ARM[a][next(iter(ARM[a]))] ** 3:.2f})") for a in sorted(b)))
    if published:
        pub = {int(r["point"][3]): (float(r["estimate"]) if r["status"] == "crossed" else math.inf, float(r["bracket_lo"]), float(r["bracket_hi"])) for r in csv.DictReader(open(published), delimiter="\t") if r["point"].endswith("_KO") and int(r["point"][3]) in CLASSES}
        lines.append(f"Published bisect order in s {'MATCHES' if ranks({a: x[0] for a, x in pub.items()}) == rk_s['base'] else 'DIFFERS FROM'} the baseline variant here (tau {tau(rk_s['base'], ranks({a: x[0] for a, x in pub.items()})):.3f}); on the multiplier scale {'MATCHES' if mult_ranks(pub) == rk_m['base'] else 'DIFFERS FROM'} it (published run: 5 seeds, 6 halvings).")
    table("MULTIPLIER scale (primary)", rk_m, full, lines)
    table("STRENGTH s scale (partly imposed by the listed coefficients: not read as superiority)", rk_s, full, lines)
    imposed = [f"{CLASSES[a]} against {CLASSES[c]}" for a in ARM for c in ARM if a < c and next(iter(ARM[a])) == next(iter(ARM[c])) and (rk_s["base"][a] != rk_s["base"][c]) and rk_m["base"][a] == rk_m["base"][c]]
    lines.append("Comparisons that depend on the listed coefficients (an order in s that the multiplier scale ties): " + (", ".join(imposed) if imposed else "none"))
    lines.append("Composite arm: the neurosteroid-type arm moves J_tonic and J_I together at the fixed ratio 1.2 to 1.1; its place depends on that chosen ratio.")
    n0 = {v: statistics.median([float(r["n_bursts_baseline"]) for r in csv.DictReader(open(run / "results.tsv"), delimiter="\t") if r["point"].startswith(v + "__arm") and r["evaluation"] == "0"] or [math.nan]) for v in full}
    shifted = [f"{v} ({n0[v] / n0['base']:.2f}x)" for v in full if v != "base" and not 0.5 <= n0[v] / n0["base"] <= 2.0]
    lines.append("Variants whose baseline burst count left 0.5x to 2x of the baseline variant (read their order with care): " + (", ".join(shifted) if shifted else "none"))
    lines.append("Classes not crossing within [0,3] are tied last. No probability, no pass or fail, no dose.")
    return "\n".join(lines)


def main(argv: list[str]) -> int:
    if len(argv) >= 2 and argv[0] == "scan":
        stage = argv[argv.index("--stage") + 1] if "--stage" in argv else "baseline"
        sc = scan(stage); Path(argv[1]).write_text(json.dumps(sc, indent=1, sort_keys=True) + "\n"); print(f"scan {stage}: {len(sc['bisect']['cells'])} cells"); return 0
    if len(argv) >= 2 and argv[0] == "report":
        print(report(Path(argv[1]), Path(argv[argv.index("--published") + 1]) if "--published" in argv else None)); return 0
    print(__doc__); return 0 if argv[:1] in (["-h"], ["--help"]) else 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
