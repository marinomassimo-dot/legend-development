"""Unzip one HPA download into a directory (SCI44 A2). usage: python3 -I hpa_unzip_peek.py <zip> <outdir>
No network. Reads local files given as arguments.
"""
import sys
if "--help" in sys.argv or "-h" in sys.argv:
    print(__doc__)
    sys.exit(0)
import sys, zipfile
src, outdir = sys.argv[1], sys.argv[2]
with zipfile.ZipFile(src) as z:
    for n in z.namelist():
        z.extract(n, outdir)
        print(n)
