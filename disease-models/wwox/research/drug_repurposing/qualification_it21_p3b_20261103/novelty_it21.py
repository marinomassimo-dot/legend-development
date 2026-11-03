#!/usr/bin/env python3
"""IT21 P3b novelty perimeter: a whole-word name search over the module's text files (cards, needs, READMEs, tables), by top-level directory.

  python3 novelty_it21.py TERM [TERM ...]        one line per term: directories that name it, and whether a card or a need does
  python3 novelty_it21.py --registries TERM ...  adds the routed registry search (registry_records.py) as whole-word counts

A hit in a catalogue-wide table (the 11,208-row or 992-row generator tables) only shows that the name is in the catalogue; those directories are listed
under `bulk_tables` and never count as LEGEND having examined the compound. The perimeter is this module and the registries; it is not a literature claim.
"""
import sys
if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
    print(__doc__)
    raise SystemExit(0)
import json, re, subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
DR = HERE.parent
REPO = DR.parents[3]
SKIP_DIRS = {"catalog", "clinical_census_20261020_raw", "gse156243", "qualification_it21_p3b_20261103"}
BULK = ("generation_it21_p2", "generation_it10_p1", "generation_it9_p1", "generation_it9_p2", "usable_compounds_it7_p2", "hypotheses_it20", "coverage", "catalogue_", "join", "ranking_it8_p9")
EXTS = {".md", ".tsv", ".json", ".txt", ".py"}


def files():
    for p in DR.rglob("*"):
        if p.suffix in EXTS and p.is_file() and p.stat().st_size < 6_000_000:
            top = p.relative_to(DR).parts[0]
            if top in SKIP_DIRS:
                continue
            yield p, top


def search(terms):
    pats = {t: re.compile(r"(?<![A-Za-z0-9])" + re.escape(t) + r"(?![A-Za-z0-9])", re.I) for t in terms}
    res = {t: {} for t in terms}
    cache = [(p, top, p.read_text(errors="ignore")) for p, top in files()]
    for t, pat in pats.items():
        for p, top, txt in cache:
            n = len(pat.findall(txt))
            if n:
                res[t].setdefault(top, []).append((str(p.relative_to(DR)), n))
    return res


def main():
    args = sys.argv[1:]
    reg = False
    if args[0] == "--registries":
        reg, args = True, args[1:]
    res = search(args)
    for t in args:
        d = res[t]
        bulk = sorted(k for k in d if k.startswith(BULK))
        rec = sorted(k for k in d if not k.startswith(BULK))
        card_need = [f for k in rec for f, n in d[k] if f.startswith(("cards/", "needs/"))]
        print("%s | record_dirs=%d %s | bulk_tables=%d | card_or_need=%s" % (t, len(rec), ",".join(rec)[:260], len(bulk), card_need[:3] or "none"))
        if reg:
            out = subprocess.run([sys.executable, str(REPO / "framework/scripts/registry_records.py"), "get", "--theme", t, "--json", "--limit", "60"], capture_output=True, text=True, cwd=str(REPO)).stdout
            try:
                recs = json.loads(out)["records"]
                pat = re.compile(r"(?<![A-Za-z0-9])" + re.escape(t) + r"(?![A-Za-z0-9])", re.I)
                ids = [r["record_id"][:30] for r in recs if pat.search(r.get("text", ""))]
                print("    registries whole-word records=%d %s" % (len(ids), ids[:5]))
            except Exception as e:
                print("    registries error", e)


main()
