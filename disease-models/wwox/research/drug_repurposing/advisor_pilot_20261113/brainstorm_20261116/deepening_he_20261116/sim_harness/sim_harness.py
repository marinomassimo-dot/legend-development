#!/usr/bin/env python3
"""Reproducible simulation harness: seeded parameter scans, configuration frozen by hash BEFORE any run, outputs hashed, predictions scored only afterwards.

    python3 sim_harness.py freeze --model ADAPTER.py [--also FILE ...] --scan scan.json --seeds N --base-seed S --out DIR
    python3 sim_harness.py run    --out DIR --expect-freeze-sha256 HEX [--workers K]
    python3 sim_harness.py score  --out DIR
    python3 sim_harness.py check  --out DIR --point LABEL
    python3 sim_harness.py --help

Model contract (numpy only, no network): the adapter file defines PARAMS = {name: [default, low, high, note]} and simulate(params: dict, seed: int) -> dict of floats.
Every other file the adapter imports must be listed with --also so it is frozen too.
scan.json: {"design": "grid" | "oat" | "lhs", "fixed": {param: value}, "silent_metric": "n_bursts", "silent_below": 5, "predictions": [...]}
  grid: "grid": {param: [values]}            cartesian product, label "p=v|q=w" (sorted by name)
  oat:  "oat": {"params": [..], "fraction": 0.4}   the baseline plus each parameter at (1-f) and (1+f) of its (fixed or default) value; labels "base", "p-40", "p+40"
  lhs:  "lhs": {"params": {p: [low, high]}, "n": 64, "seed": 5}   seeded Latin hypercube, labels "lhs000".."lhs063"
predictions (frozen with the scan, scored only after the run): {"id", "statement", "metric", "a": LABEL, "b": LABEL, "expect": "a_gt_b" | "a_lt_b", "min_fraction": 0.8}
  scored as the fraction of seeds (the same seed at both points, so paired) in which the expectation holds; PASS when that fraction >= min_fraction.
  A seed where either side is nan (a silent point has no interval) counts as NOT holding and is reported in n_undefined_seeds.
Rule 'hash before result': freeze.sha256 is committed (or sent) before `run`; `run` refuses unless --expect-freeze-sha256 equals the digest of freeze.json and the model,
extra files and scan still hash to what freeze.json says. A mismatch is a refusal, never a warning. Same machine, same Python and numpy: results.tsv is byte-identical for any
worker count. Across machines floating-point libraries can differ in the last digits; `check` reports the largest relative difference. Mechanism-level tool; not a claim about any model.
"""
import argparse, csv, hashlib, importlib.util, itertools, json, math, multiprocessing as mp, statistics, sys
from pathlib import Path

VERSION = "1"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def canon(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"))


def load_model(path):
    spec = importlib.util.spec_from_file_location("frozen_model", str(path))
    mod = importlib.util.module_from_spec(spec)
    sys.path.insert(0, str(Path(path).resolve().parent))
    spec.loader.exec_module(mod)
    if not hasattr(mod, "PARAMS") or not hasattr(mod, "simulate"):
        raise SystemExit("the model file must define PARAMS and simulate(params, seed)")
    return mod


def points_of(scan, params):
    """[(label, {param: value})] for the scan design. The values are final (defaults and fixed overlaid)."""
    base = {k: v[0] for k, v in params.items()}
    base.update(scan.get("fixed", {}))
    design = scan["design"]
    out = []
    if design == "grid":
        names = sorted(scan["grid"])
        for vals in itertools.product(*[scan["grid"][n] for n in names]):
            out.append(("|".join(f"{n}={v:g}" for n, v in zip(names, vals)), {**base, **dict(zip(names, vals))}))
    elif design == "oat":
        f = scan["oat"]["fraction"]; pct = f"{round(f * 100):d}"
        out.append(("base", dict(base)))
        for n in scan["oat"]["params"]:
            out.append((f"{n}-{pct}", {**base, n: base[n] * (1 - f)})); out.append((f"{n}+{pct}", {**base, n: base[n] * (1 + f)}))
    elif design == "lhs":
        import numpy as np
        spec = scan["lhs"]; names = sorted(spec["params"]); n = spec["n"]; rng = np.random.default_rng(spec["seed"])
        cols = []
        for nm in names:
            perm = rng.permutation(n); u = (perm + rng.random(n)) / n; lo, hi = spec["params"][nm]; cols.append(lo + u * (hi - lo))
        for i in range(n):
            out.append((f"lhs{i:03d}", {**base, **{nm: float(cols[j][i]) for j, nm in enumerate(names)}}))
    else:
        raise SystemExit(f"unknown design {design!r}")
    labels = [l for l, _ in out]
    if len(set(labels)) != len(labels):
        raise SystemExit("duplicate point labels")
    for l, p in out:
        for k in p:
            if k not in params:
                raise SystemExit(f"parameter {k!r} (point {l}) is not in the model PARAMS")
    return out


def freeze(a):
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    if (out / "freeze.json").exists():
        raise SystemExit("freeze.json already exists: a frozen configuration is never overwritten (use a new --out)")
    mod = load_model(a.model); scan = json.loads(Path(a.scan).read_text())
    pts = points_of(scan, mod.PARAMS)
    labels = {l for l, _ in pts}
    for pr in scan.get("predictions", []):
        for k in ("a", "b"):
            if pr[k] not in labels:
                raise SystemExit(f"prediction {pr['id']}: label {pr[k]!r} is not a point of this scan (labels: {sorted(labels)[:12]} ...)")
    oob = [l for l, p in pts if any(not (mod.PARAMS[k][1] <= v <= mod.PARAMS[k][2]) for k, v in p.items())]
    fr = {"harness_version": VERSION, "harness_sha256": sha(__file__), "files": {Path(f).name: sha(f) for f in [a.model] + list(a.also or [])}, "adapter": Path(a.model).name,
          "params": {k: v for k, v in sorted(mod.PARAMS.items())}, "scan": scan, "scan_sha256": sha(a.scan), "seeds": a.seeds, "base_seed": a.base_seed,
          "points": len(pts), "calls": len(pts) * a.seeds, "points_outside_declared_bounds": oob}
    (out / "scan.json").write_bytes(Path(a.scan).read_bytes())
    for f in [a.model] + list(a.also or []):
        (out / "model_files").mkdir(exist_ok=True); (out / "model_files" / Path(f).name).write_bytes(Path(f).read_bytes())
    (out / "freeze.json").write_text(json.dumps(fr, indent=1, sort_keys=True) + "\n")
    d = sha(out / "freeze.json"); (out / "freeze.sha256").write_text(d + "  freeze.json\n")
    print(f"FROZEN {d}  points {len(pts)} seeds {a.seeds} calls {fr['calls']} outside_bounds {len(oob)}")


def verify_freeze(out, expect):
    fr = json.loads((out / "freeze.json").read_text())
    if fr.get("harness_sha256") and fr["harness_sha256"] != sha(__file__):
        raise SystemExit("REFUSED: sim_harness.py is not the version that froze this configuration")
    if sha(out / "freeze.json") != expect:
        raise SystemExit("REFUSED: freeze.json does not hash to --expect-freeze-sha256")
    for name, h in fr["files"].items():
        if sha(out / "model_files" / name) != h:
            raise SystemExit(f"REFUSED: model file {name} no longer hashes to the frozen value")
    if sha(out / "scan.json") != fr["scan_sha256"]:
        raise SystemExit("REFUSED: scan.json no longer hashes to the frozen value")
    return fr


def _call(args):
    path, params, seed = args
    mod = load_model(path)
    return mod.simulate(dict(params), int(seed))


def fmt(x):
    return repr(float(x))


def run_points(out, fr, workers):
    mod = load_model(out / "model_files" / fr["adapter"]); scan = json.loads((out / "scan.json").read_text())
    pts = points_of(scan, mod.PARAMS); seeds = [fr["base_seed"] + i for i in range(fr["seeds"])]
    jobs = [(str(out / "model_files" / fr["adapter"]), p, s) for _, p in pts for s in seeds]
    if workers > 1:
        with mp.get_context("spawn").Pool(workers) as pool:
            res = pool.map(_call, jobs, chunksize=1)
    else:
        res = [_call(j) for j in jobs]
    return pts, seeds, res


def run(a):
    out = Path(a.out); fr = verify_freeze(out, a.expect_freeze_sha256)
    if (out / "results.tsv").exists():
        raise SystemExit("results.tsv exists: a run is never overwritten")
    pts, seeds, res = run_points(out, fr, a.workers)
    pn = sorted(fr["params"]); mk = sorted({k for r in res for k in r if k != "events"})
    with open(out / "results.tsv", "w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n"); w.writerow(["point", "seed"] + pn + mk)
        i = 0
        for label, p in pts:
            for s in seeds:
                r = res[i]; i += 1; w.writerow([label, s] + [fmt(p[k]) for k in pn] + [fmt(r.get(k, float("nan"))) for k in mk])
    rows = list(csv.DictReader(open(out / "results.tsv"), delimiter="\t"))
    scan = fr["scan"]; sm, sb = scan.get("silent_metric"), scan.get("silent_below")
    with open(out / "summary.tsv", "w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n"); w.writerow(["point", "n_seeds"] + [f"{m}_{q}" for m in mk for q in ("median", "q1", "q3")] + (["fraction_silent"] if sm else []))
        for label, _ in pts:
            rr = [r for r in rows if r["point"] == label]; cells = []
            for m in mk:
                v = sorted(float(r[m]) for r in rr if not math.isnan(float(r[m])))
                if len(v) >= 2:
                    qs = statistics.quantiles(v, n=4, method="inclusive"); cells += [fmt(statistics.median(v)), fmt(qs[0]), fmt(qs[2])]
                else:
                    cells += [fmt(v[0]) if v else "nan", "nan", "nan"]
            w.writerow([label, len(rr)] + cells + ([fmt(sum(float(r[sm]) < sb for r in rr) / len(rr))] if sm else []))
    man = {"freeze_sha256": a.expect_freeze_sha256, "results_sha256": sha(out / "results.tsv"), "summary_sha256": sha(out / "summary.tsv"), "rows": len(rows),
           "python": sys.version.split()[0], "numpy": __import__("numpy").__version__}
    (out / "run_manifest.json").write_text(json.dumps(man, indent=1, sort_keys=True) + "\n")
    (out / "results.sha256").write_text(f"{man['results_sha256']}  results.tsv\n{man['summary_sha256']}  summary.tsv\n")
    print(f"RUN {man['results_sha256']}  rows {len(rows)}")


def score(a):
    out = Path(a.out); fr = json.loads((out / "freeze.json").read_text())
    if not (out / "results.tsv").exists():
        raise SystemExit("no results.tsv: run first")
    rows = list(csv.DictReader(open(out / "results.tsv"), delimiter="\t")); by = {}
    for r in rows:
        by.setdefault(r["point"], {})[int(r["seed"])] = r
    with open(out / "predictions_scored.tsv", "w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n"); w.writerow(["id", "metric", "a", "b", "expect", "fraction_holding", "n_undefined_seeds", "min_fraction", "verdict", "median_a", "median_b", "statement"])
        for p in fr["scan"].get("predictions", []):
            sa, sb_ = by[p["a"]], by[p["b"]]; seeds = sorted(set(sa) & set(sb_)); m = p["metric"]
            va = [float(sa[s][m]) for s in seeds]; vb = [float(sb_[s][m]) for s in seeds]
            und = sum(math.isnan(x) or math.isnan(y) for x, y in zip(va, vb))      # a silent point has no interval: undefined, counted as NOT holding, never dropped
            ok = [(x > y) if p["expect"] == "a_gt_b" else (x < y) for x, y in zip(va, vb)]      # a comparison with nan is False
            fr_ = sum(ok) / len(ok); fin = lambda v: [x for x in v if not math.isnan(x)]
            ma = statistics.median(fin(va)) if fin(va) else float("nan"); mb = statistics.median(fin(vb)) if fin(vb) else float("nan")
            w.writerow([p["id"], m, p["a"], p["b"], p["expect"], f"{fr_:.3f}", und, p.get("min_fraction", 0.8), "PASS" if fr_ >= p.get("min_fraction", 0.8) else "FAIL", fmt(ma), fmt(mb), p["statement"]])
    print((out / "predictions_scored.tsv").read_text())


def check(a):
    out = Path(a.out); fr = json.loads((out / "freeze.json").read_text())
    mod = load_model(out / "model_files" / fr["adapter"]); scan = json.loads((out / "scan.json").read_text())
    pt = dict(points_of(scan, mod.PARAMS))[a.point]; rows = [r for r in csv.DictReader(open(out / "results.tsv"), delimiter="\t") if r["point"] == a.point]
    worst = 0.0; identical = True
    for r in rows:
        res = mod.simulate(dict(pt), int(r["seed"]))
        for k, v in res.items():
            if k == "events" or k not in r: continue
            if fmt(v) != r[k]:
                identical = False
            ref = float(r[k]); worst = max(worst, abs(float(v) - ref) / (abs(ref) or 1.0))
    print(f"CHECK point {a.point}: seeds {len(rows)}; byte-identical {identical}; largest relative difference {worst:.3g}")
    sys.exit(0 if worst < 1e-9 else 1)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter); sub = ap.add_subparsers(dest="cmd")
    f = sub.add_parser("freeze"); f.add_argument("--model", required=True); f.add_argument("--also", nargs="*"); f.add_argument("--scan", required=True); f.add_argument("--seeds", type=int, required=True); f.add_argument("--base-seed", type=int, required=True); f.add_argument("--out", required=True)
    r = sub.add_parser("run"); r.add_argument("--out", required=True); r.add_argument("--expect-freeze-sha256", required=True); r.add_argument("--workers", type=int, default=1)
    s = sub.add_parser("score"); s.add_argument("--out", required=True)
    c = sub.add_parser("check"); c.add_argument("--out", required=True); c.add_argument("--point", required=True)
    a = ap.parse_args()
    {"freeze": freeze, "run": run, "score": score, "check": check}.get(a.cmd, lambda _: ap.print_help())(a)


if __name__ == "__main__":
    main()
