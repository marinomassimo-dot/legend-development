#!/usr/bin/env python3
import sys as _s
if len(_s.argv) > 1 and _s.argv[1] in ("-h", "--help"):
    print("IT10 P2.1 research script; reads inputs named in README.md of this folder; no options. Run with python3 -I from this folder.")
    raise SystemExit(0)
"""IT10 P2.1: mechanical check that every quoted fragment in the 'verbatim locator' columns of premises_it10_p21.tsv and direction_evidence_it10_p21.tsv occurs in the
source texts that were read (whitespace/case/alpha-normalised; '...' splits a quote into fragments). Usage: python3 -I quote_check_it10_p21.py <scratch_dir> <shared_fulltext_dir>
Fragments from repository analyses (a5, RESULTS.md) and from line-numbered layout text (a9) are reported as NOT FOUND and verified by eye (disclosed in the README)."""
import csv, glob, re, sys
import xml.etree.ElementTree as ET
S, FT = sys.argv[1], sys.argv[2]
def norm(t): return re.sub(r"\s+", " ", t.replace("’", "'").replace("‐", "-").replace("–", "-")).lower().replace("alpha", "α")
corpus = ""
for p in glob.glob(S + "/s/ft/*/full.xml"):
    try: corpus += " " + "".join(ET.parse(p).getroot().itertext())
    except Exception: pass
for p in glob.glob(S + "/s/ft/*/abstract.txt") + glob.glob(S + "/s/pmcpages/*.txt") + [FT + "/PMC4211377_PMID25012504_pmc_html_fulltext_2026-10-30.txt", FT + "/PMID42397075_Steinberg2026_OUP-AM_layout.txt"]:
    corpus += " " + open(p, errors="ignore").read()
for p in [FT + "/PMID35328751_Baryla2022_PMC.xml", FT + "/PMID34268881_Steinberg2021_PMC_r2.xml"]:
    corpus += " " + "".join(ET.parse(p).getroot().itertext())
corpus = norm(corpus)
here = __file__.rsplit("/", 1)[0] if "/" in __file__ else "."
bad = tot = 0
for f, col in [("premises_it10_p21.tsv", "verbatim locator"), ("direction_evidence_it10_p21.tsv", "locator")]:
    for r in csv.DictReader(open(here + "/" + f), delimiter="\t"):
        for q in re.findall(r"'([^']{12,})'", r[col]):
            for seg in [norm(x.strip()) for x in q.split("...")]:
                if len(seg) < 12: continue
                tot += 1
                if seg not in corpus: bad += 1; print("NOT FOUND:", r["id"], "|", seg[:110])
print("fragments", tot, "not found", bad)
