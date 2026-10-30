#!/usr/bin/env python3
"""Amendment 5c: rerun the full v3 variant (run + tests) under the admissible-in-degree null (--match adm), labels p1_<set>_adm.
  run_adm_v3.py --seeds-dir ../seeds_p1 --extra ../seeds_provisional.tsv --out results [--nnull 1000]"""
import sys
if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
    print(__doc__); raise SystemExit(0)
import argparse, glob, os, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
ap = argparse.ArgumentParser(); ap.add_argument("--seeds-dir", required=True); ap.add_argument("--extra", action="append", default=[]); ap.add_argument("--out", required=True); ap.add_argument("--nnull", type=int, default=1000)
a = ap.parse_args()
files = sorted(f for f in glob.glob(os.path.join(a.seeds_dir, "*.tsv")) if not f.endswith("manifest.tsv")) + a.extra
for f in files:
    base = os.path.basename(f)[:-4]; lab = "provisional" if base == "seeds_provisional" else base
    for cmd in ("run", "tests"):
        args = [sys.executable, os.path.join(HERE, "seed_engine_v3.py"), cmd, "--seeds", f, "--actions", os.path.join(a.out, "actions"), "--label", f"p1_{lab}_adm", "--out", a.out, "--match", "adm", "--mode", "v3"]
        if cmd == "tests": args += ["--nnull", str(a.nnull)]
        r = subprocess.run(args, capture_output=True, text=True); print(lab, cmd, "rc", r.returncode, flush=True)
        if r.returncode: print(r.stderr[-400:])
