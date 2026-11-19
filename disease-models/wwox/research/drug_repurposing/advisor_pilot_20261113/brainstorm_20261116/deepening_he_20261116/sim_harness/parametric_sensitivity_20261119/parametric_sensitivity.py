#!/usr/bin/env python3
"""PARAMETRIC SENSITIVITY of the simulated crossing strengths (HE, ADV-096, 2026-11-19; hypothesis generator, not evidence; not medical advice.)

    python3 parametric_sensitivity.py scan OUT_SCAN.json [--stage baseline|rest|full]   the scan the harness freezes: one bisect cell per variant and class, S-KO
    python3 parametric_sensitivity.py report RUN_DIR [RUN_DIR ...] [--published PUBLISHED_SUMMARY.tsv]   run dirs are combined (baseline first)

Uses sim_harness.py's own `fixed` block per bisect cell: no change to the harness, to SCI's frozen model or to the published bisect folder. Variants: the baseline; four parameters at a low and a high
value, one at a time; three JOINT scenarios chosen for biological meaning. Every variant is a PARAMETER change of the same equations: it is not a validation on alternative biological structures, and a
technical reproduction of the baseline does not show biological validity. **Kv7 is NOT in the model: kv7_offset is an ASSUMED stand-in (a drive offset), not a current.**
What the report does NOT do: it ranks no classes, computes no rank correlation and names no winner. Crossing strengths use a different listed multiplier per arm, and different arms change different
parameters, so an order across classes is imposed by the coefficients or by the model's sensitivity, not a pharmacological superiority. Only two kinds of comparison are identifiable: the SAME class across
variants (same arm, same coefficient), and classes that move the SAME parameter (d-APV and the NMDAR pore blocker: both J_N), which are judged on the multiplier of that parameter. The final bisection
bracket is a numerical resolution, not a confidence interval; seeds (3) are shown beside it, not merged with it; "no crossing within [0,3]" is not "no possible effect"; the composite arm
(neurosteroid-type: J_tonic and J_I together at the fixed ratio 1.2 to 1.1) depends on that chosen ratio. Crossing is a model step, not a dose."""
from __future__ import annotations
import csv, json, math, sys
from pathlib import Path

CLASSES = {1: "d-APV-type", 2: "NMDAR pore", 4: "AMPA", 5: "T-type", 6: "synaptic GABA-A", 7: "neurosteroid-type", 8: "sodium (pyramidal)"}
ARM = {1: {"J_N": 0.3}, 2: {"J_N": 0.8}, 4: {"J_A": 0.8}, 5: {"J_T": 0.75}, 6: {"J_I": 1.2}, 7: {"J_tonic": 1.2, "J_I": 1.1}, 8: {"sigma": 0.9}}   # as in the frozen adapter (checked by the test)
ONE = {"ji_mult": (0.5, 1.5), "cl_tau_mult": (0.5, 2.0), "nmda_mult": (0.8, 1.25), "kv7_offset": (-0.05, 0.05)}
JOINT = {"joint_highCl_lowInh": {"cl_tau_mult": 2.0, "ji_mult": 0.5}, "joint_hyperexcitable": {"nmda_mult": 1.25, "kv7_offset": 0.05},
         "joint_inhibited": {"nmda_mult": 0.8, "kv7_offset": -0.05, "cl_tau_mult": 0.5}}
NOTE = "Kv7 is NOT in the model: kv7_offset is an ASSUMED stand-in. Parameter changes of the same equations, not alternative biological structures. A crossing is a model step, not a dose; a final bracket is a numerical resolution, not a confidence interval."


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


def mult(a: int, x: float) -> str:
    return " and ".join(f"{p} x{m ** x:.3f}" for p, m in ARM[a].items())


def load(run: Path) -> tuple[dict, dict]:
    cells: dict = {}; per_seed: dict = {}
    for r in csv.DictReader(open(run / "summary.tsv"), delimiter="\t"):
        v, a = r["point"].split("__arm"); ok = r["status"] == "crossed"
        cells[(v, int(a))] = (float(r["estimate"]) if ok else math.inf, float(r["bracket_lo"]), float(r["bracket_hi"]))
    for r in csv.DictReader(open(run / "results.tsv"), delimiter="\t"):
        v, a = r["point"].split("__arm")
        per_seed.setdefault((v, int(a)), {}).setdefault(round(float(r["strength"]), 6), []).append(float(r["rel_bursts"]))
    return cells, per_seed


def seeds_at(per_seed: dict, key: tuple, x: float, below: bool) -> str:
    vals = per_seed.get(key, {}).get(round(x, 6), [])
    return f"{sum((v < 0.5) == below for v in vals)}/{len(vals)}" if vals else "n/a"


def describe(cells: dict, per_seed: dict, v: str, a: int, base: dict) -> str:
    s, lo, hi = cells[(v, a)]
    if math.isinf(s):
        return f"{CLASSES[a]}: no crossing within [0, 3] ({mult(a, 3.0)} at the far end): an explored-range result, not an impossibility of effect"
    seeds = f"seeds below 0.5 at the crossed end {seeds_at(per_seed, (v, a), hi, True)}, at the uncrossed end above {seeds_at(per_seed, (v, a), lo, False)}"
    text = f"{CLASSES[a]}: s {s:.3f} (bracket {lo:.3f} to {hi:.3f}, numerical resolution {hi - lo:.3f}), {mult(a, s)}; {seeds}"
    if v != "base" and (("base", a) in base):
        b = base[("base", a)]
        if math.isinf(b[0]):
            text += "; the baseline did not cross within [0, 3]: the shift is not measurable"
        else:
            text += "; vs the baseline of this class: " + ("indistinguishable at this resolution" if lo <= b[2] and b[1] <= hi else ("needs a larger parameter change" if lo > b[2] else "needs a smaller parameter change"))
    return text


def report(runs: list[Path], published: Path | None = None) -> str:
    cells: dict = {}; per_seed: dict = {}
    for r in runs:
        c, p = load(r); cells.update(c); per_seed.update(p)
    vs = sorted({v for v, _ in cells}, key=lambda v: (v != "base", v)); missing = [f"{v}__arm{a}" for v in vs for a in CLASSES if (v, a) not in cells]
    lines = ["PARAMETRIC SENSITIVITY, S-KO. " + NOTE, f"Coverage: {len(cells)} cells found in {len(runs)} run folder(s) for {len(vs)} variants x {len(CLASSES)} classes; missing: {', '.join(missing) if missing else 'none'}.",
             "Same equations with other parameter values: not a validation on alternative biological structures; a reproduction of the baseline is technical, not biological. No ranks, no rank correlation, no winner."]
    if "base" in vs and published:
        pub = {int(r["point"][3]): (float(r["estimate"]) if r["status"] == "crossed" else math.inf, float(r["bracket_lo"]), float(r["bracket_hi"])) for r in csv.DictReader(open(published), delimiter="\t") if r["point"].endswith("_KO") and int(r["point"][3]) in CLASSES}
        same = [a for a in CLASSES if ("base", a) in cells and (math.isinf(cells[("base", a)][0]) == math.isinf(pub[a][0])) and (math.isinf(pub[a][0]) or (cells[("base", a)][1] <= pub[a][2] and pub[a][1] <= cells[("base", a)][2]))]
        lines.append(f"Baseline reproduction: {len(same)} of {len(CLASSES)} classes agree with the published bisect within the numerical resolution (brackets overlap; the published run used 5 seeds and 6 halvings, this one 3 seeds and 5).")
    for v in vs:
        lines.append(f"## variant {v}")
        lines += ["- " + describe(cells, per_seed, v, a, cells) for a in CLASSES if (v, a) in cells]
        if all((v, a) in cells and not math.isinf(cells[(v, a)][0]) for a in (1, 2)):
            (s1, l1, h1), (s2, l2, h2) = cells[(v, 1)], cells[(v, 2)]
            m1, m2 = sorted(sorted(ARM[1]["J_N"] ** x for x in (l1, h1))), sorted(ARM[2]["J_N"] ** x for x in (l2, h2))
            lines.append(f"- same-parameter pair (J_N): {CLASSES[1]} {m1[0]:.3f} to {m1[1]:.3f} and {CLASSES[2]} {m2[0]:.3f} to {m2[1]:.3f}: " + ("indistinguishable on the multiplier scale" if m1[0] <= m2[1] and m2[0] <= m1[1] else "distinguishable on the multiplier scale at this resolution"))
    lines.append("Not identifiable here: any order or superiority between classes that act on different parameters (J_N, J_A, J_T, J_I, sigma): the multipliers above describe the model's sensitivity to each parameter, not pharmacological potency, and are not compared.")
    lines.append("What this does not show: biological validity, the effect at any exposure, or that a class absent from a crossing cannot act. Three seeds cannot separate seed variability from numerical resolution below the bracket width; read the seed counts beside the bracket.")
    return "\n".join(lines)


def main(argv: list[str]) -> int:
    if len(argv) >= 2 and argv[0] == "scan":
        stage = argv[argv.index("--stage") + 1] if "--stage" in argv else "baseline"
        sc = scan(stage); Path(argv[1]).write_text(json.dumps(sc, indent=1, sort_keys=True) + "\n"); print(f"scan {stage}: {len(sc['bisect']['cells'])} cells"); return 0
    if len(argv) >= 2 and argv[0] == "report":
        pub = Path(argv[argv.index("--published") + 1]) if "--published" in argv else None
        dirs = [Path(x) for x in argv[1:] if x != "--published" and not x.endswith("summary.tsv")]
        print(report(dirs, pub)); return 0
    print(__doc__); return 0 if argv[:1] in (["-h"], ["--help"]) else 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
