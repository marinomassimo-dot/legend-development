#!/usr/bin/env python3
"""Run the v4 engine (v3 + F5 member junction) over every P1 seed table under the three nulls (total-degree, in-degree, admissible in-degree), then the candidate
tables. The compound side is the v3 one (read-only). Labels and file names equal v3's, so make_candidates / dispose_it10.py read them unchanged.

  run_v4.py --out DIR [--junction on|off] [--nnull 500]
"""
import sys
if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
    print(__doc__); raise SystemExit(0)
import argparse, glob, os, subprocess
from pathlib import Path
HERE = Path(__file__).resolve().parent
DR = HERE.parents[1]
V3 = DR / "generation_it9_p2_20261030" / "v3"
ap = argparse.ArgumentParser(); ap.add_argument("--out", required=True); ap.add_argument("--junction", default="on"); ap.add_argument("--nnull", type=int, default=500)
a = ap.parse_args()
out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
seeds_dir = DR / "generation_it9_p2_20261030" / "seeds_p1"
files = sorted(f for f in glob.glob(str(seeds_dir / "*.tsv")) if not f.endswith("manifest.tsv"))
for f in files:
    sn = os.path.basename(f)[:-4]
    for match, suf in (("total", ""), ("indeg", "_indeg"), ("adm", "_adm")):
        cmd = [sys.executable, str(HERE / "seed_engine_v4.py"), "run", "--seeds", f, "--actions", str(V3 / "results" / "actions"), "--label", f"p1_{sn}{suf}",
               "--out", str(out), "--match", match, "--mode", "v3", "--junction", a.junction, "--nnull", str(a.nnull), "--top", "3500"]
        r = subprocess.run(cmd, capture_output=True, text=True)
        print(sn, match, "rc", r.returncode, flush=True)
        if r.returncode: print(r.stderr[-500:])
import gzip, shutil                       # the engine writes plain TSV; the v3 tables are gzipped (candidate maker reads *.tsv.gz)
for f in glob.glob(str(out / "proposals_p1_*.tsv")) + glob.glob(str(out / "contributions_p1_*.tsv")):
    with open(f, "rb") as fi, gzip.GzipFile(f + ".gz", "wb", mtime=0) as fo:
        shutil.copyfileobj(fi, fo)
    os.remove(f)
if not (out / "actions").exists():
    os.symlink(os.path.relpath(V3 / "results" / "actions", out), out / "actions")
r = subprocess.run([sys.executable, str(V3 / "make_candidates_v3.py"), "--engine", str(HERE / "seed_engine_v4.py"), "--seeds-dir", str(seeds_dir), "--results", str(out), "--out", str(out)],
                   capture_output=True, text=True)
print(r.stdout[-1500:]); print(r.stderr[-500:])
