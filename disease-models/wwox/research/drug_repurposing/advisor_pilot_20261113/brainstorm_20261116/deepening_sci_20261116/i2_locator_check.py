#!/usr/bin/env python3
"""Second reading of IT's I2 per-child extraction (mechanical half): does every locator fragment of every exposure row occur, as a verbatim substring after whitespace
normalisation (and tag stripping for XML), in the held source file it names?  Fragments are the pieces between the extractor's ellipsis marks.
    python3 i2_locator_check.py --help
    python3 i2_locator_check.py run <exposures.tsv> <files_dir> <out_tsv>
Reports per row and per locator column: fragments checked, fragments found, and the missing ones. Not a judgement of the coding; a check that the quoted words exist."""
import sys
if len(sys.argv) != 5 or sys.argv[1] != "run":
    print(__doc__); raise SystemExit(0)
import csv, os, re, unicodedata
def norm(t, markup=False):
    t = re.sub(r"<[^>]+>", " ", t) if markup else t
    t = unicodedata.normalize("NFKC", t)
    t = t.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"').replace("–", "-").replace("—", "-").replace("­", "")
    return re.sub(r"\s+", " ", t).strip().lower()
cache = {}
def text(fn):
    if fn not in cache:
        p = os.path.join(sys.argv[3], fn)
        cache[fn] = norm(open(p, errors="ignore").read(), markup=fn.endswith((".xml", ".html"))) if os.path.exists(p) else None
    return cache[fn]
rows = list(csv.DictReader(open(sys.argv[2]), delimiter="\t"))
out = []
tot = found = 0
for i, r in enumerate(rows):
    for col in ("locator_outcome", "locator_semiology", "locator_age"):
        v = r[col].strip()
        if not v or v.lower() == "not_stated":
            continue
        for part in v.split(" || "):
            m = re.match(r"^(PMID\S+?\.(?:txt|xml|pdf|html|json)): (.*)$", part.strip(), re.S)
            if not m:
                out.append((i + 2, r["report_id"], col, "UNPARSED", part[:80])); tot += 1; continue
            fn, body = m.group(1), m.group(2)
            t = text(fn)
            for frag in [f.strip() for f in re.split(r"…|\.\.\.", body)]:
                if len(frag) < 6:
                    continue
                tot += 1
                if t is None:
                    out.append((i + 2, r["report_id"], col, "FILE_MISSING " + fn, frag[:80]))
                elif norm(frag, markup=fn.endswith((".xml", ".html"))) in t:
                    found += 1
                else:
                    out.append((i + 2, r["report_id"], col, "NOT_FOUND in " + fn, frag[:120]))
with open(sys.argv[4], "w", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n"); w.writerow(["tsv_line", "report_id", "column", "status", "fragment_start"]); w.writerows(out)
print(f"fragments checked {tot}; found {found}; not found or unparsed {len(out)}")
