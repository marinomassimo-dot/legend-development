#!/usr/bin/env python3
"""Run the engine (run + tests) on every seed table of a directory, under both degree-matching variants (registered total-degree; M2 in-degree), then summarise.

  run_battery.py --seeds-dir seeds_p1 --extra seeds_provisional.tsv --actions results --out results [--nnull 1000]
Writes results/{proposals,contributions,funnel,tests}_<set>[_indeg].* and results/tests_summary.tsv. Deterministic. About 20 s per set and variant.
"""
import sys
if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
    print(__doc__); raise SystemExit(0)
import argparse, glob, os, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
ap = argparse.ArgumentParser()
ap.add_argument("--seeds-dir", required=True); ap.add_argument("--extra", action="append", default=[]); ap.add_argument("--actions", required=True)
ap.add_argument("--out", required=True); ap.add_argument("--nnull", type=int, default=1000)
a = ap.parse_args()
files = sorted(f for f in glob.glob(os.path.join(a.seeds_dir, "*.tsv")) if not f.endswith("manifest.tsv")) + a.extra
for f in files:
    base = os.path.basename(f)[:-4]
    label = base if base.startswith("provisional") or base.startswith("p1_") else "p1_" + base
    if base == "seeds_provisional":
        label = "provisional"
    for match, suf in (("total", ""), ("indeg", "_indeg")):
        for cmd in ("run", "tests"):
            args = [sys.executable, os.path.join(HERE, "seed_engine.py"), cmd, "--seeds", f, "--actions", a.actions, "--label", label + suf, "--out", a.out, "--match", match]
            if cmd == "tests":
                args += ["--nnull", str(a.nnull)]
            r = subprocess.run(args, capture_output=True, text=True)
            print(label + suf, cmd, "rc", r.returncode, flush=True)
            if r.returncode:
                print(r.stderr[-600:])
subprocess.run([sys.executable, os.path.join(HERE, "summarize_tests.py"), "--dir", a.out, "--out", os.path.join(a.out, "tests_summary.tsv")])
