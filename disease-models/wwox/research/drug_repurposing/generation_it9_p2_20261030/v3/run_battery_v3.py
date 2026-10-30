#!/usr/bin/env python3
"""v3 battery: for every seed table, (1) full v3 (edge modes + v3 compound table): run + tests under both nulls; (2) F1 only (edge modes + v2 compound table): run; (3) F2/F3 only
(all edges + v3 compound table): run. Labels p1_<set>[_indeg] (full), f1_<set>[_indeg], f2_<set>[_indeg]. Then summarize_tests.py on the full-v3 tests.

  run_battery_v3.py --seeds-dir ../seeds_p1 --extra ../seeds_provisional.tsv --out results [--nnull 1000]
"""
import sys
if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
    print(__doc__); raise SystemExit(0)
import argparse, glob, os, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
ap = argparse.ArgumentParser(); ap.add_argument("--seeds-dir", required=True); ap.add_argument("--extra", action="append", default=[]); ap.add_argument("--out", required=True); ap.add_argument("--nnull", type=int, default=1000)
a = ap.parse_args()
A3, A2 = os.path.join(a.out, "actions"), os.path.join(HERE, "..", "results")
files = sorted(f for f in glob.glob(os.path.join(a.seeds_dir, "*.tsv")) if not f.endswith("manifest.tsv")) + a.extra
def go(args):
    r = subprocess.run([sys.executable, os.path.join(HERE, "seed_engine_v3.py")] + args, capture_output=True, text=True)
    print(" ".join(args[:1] + args[args.index("--label"):args.index("--label") + 2]), "rc", r.returncode, flush=True)
    if r.returncode: print(r.stderr[-500:])
for f in files:
    base = os.path.basename(f)[:-4]; lab = "provisional" if base == "seeds_provisional" else base
    for match, suf in (("total", ""), ("indeg", "_indeg")):
        common = ["--seeds", f, "--out", a.out, "--match", match]
        go(["run", "--actions", A3, "--label", f"p1_{lab}{suf}", "--mode", "v3"] + common)
        go(["tests", "--actions", A3, "--label", f"p1_{lab}{suf}", "--nnull", str(a.nnull), "--mode", "v3"] + common)
        go(["run", "--actions", A2, "--label", f"f1_{lab}{suf}", "--mode", "v3"] + common)
        go(["run", "--actions", A3, "--label", f"f2_{lab}{suf}", "--mode", "all"] + common)
subprocess.run([sys.executable, os.path.join(HERE, "..", "summarize_tests.py"), "--dir", a.out, "--out", os.path.join(a.out, "tests_summary.tsv")])
