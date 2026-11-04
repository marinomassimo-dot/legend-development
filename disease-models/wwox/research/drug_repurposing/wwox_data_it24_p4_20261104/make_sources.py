"""Writes sources.tsv: URL, access date, sha256, size for every third-party input used (no raw files are committed). Usage: python3 -I make_sources.py <outfile> <path>=<url> ..."""
import sys, hashlib, os
out = sys.argv[1]
with open(out, "w") as f:
    f.write("url\taccessed\tsha256\tbytes\tlocal_name\n")
    for a in sys.argv[2:]:
        p, u = a.split("=", 1)
        h = hashlib.sha256(open(p, "rb").read()).hexdigest()
        f.write(f"{u}\t2026-11-04\t{h}\t{os.path.getsize(p)}\t{os.path.basename(p)}\n")
