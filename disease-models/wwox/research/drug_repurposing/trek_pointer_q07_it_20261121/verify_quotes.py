"""Check that each quotation in README.md occurs in the primary text (Tanaka 2025, PMID 40365404, PMC12067145). Pass the text file path.
The text is NOT stored in the repository: fetch it once from the PMC open-data bucket
(https://pmc-oa-opendata.s3.amazonaws.com/PMC12067145.1/PMC12067145.1.txt; expected SHA-256 below) and run:
    python3 verify_quotes.py PATH_TO_TEXT"""
import hashlib
import re
import sys

EXPECT = "0fd006949e81c64d5a3b6f962c2ef45df2a15f7066a7663bbfcc704deb706399"
QUOTES = [
    "a potent (TREK-1 IC50 = 15 nM), selective (>10 μM versus other K2P channels except TREK-2), and CNS penetrant (rat K p = 0.98) TREK inhibitor",
    "14c proved to be >67-fold selective over other K2P channels",
    "In human manual patch clamp (MPC), 14c was a potent TREK-1 inhibitor (IC50 = 15 nM), and therefore, more accurately described as a dual TREK-1/2 inhibitor.",
    "we evaluated 14c in mouse MPC, and it was a potent TREK-1 inhibitor (IC50 = 67 nM)",
]
data = open(sys.argv[1], "rb").read()
print("sha256", hashlib.sha256(data).hexdigest(), "OK" if hashlib.sha256(data).hexdigest() == EXPECT else "DIFFERENT BYTES")
t = re.sub(r"\s+", " ", data.decode("utf-8"))
bad = 0
for q in QUOTES:
    ok = q in t
    bad += not ok
    print("FOUND" if ok else "MISSING", q[:70])
hits = [m.start() for m in re.finditer(r"room temperature|°C|℃", t)]
print("temperature mentions:", len(hits), "(all in the synthesis-scheme footnote; none in the electrophysiology text: read them to confirm)")
sys.exit(1 if bad else 0)
