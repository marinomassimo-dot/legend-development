#!/usr/bin/env python3
"""Self-audit (same actor, NOT blind): re-reads the verbatim fragments behind the premises of
premises.tsv from the local source text, at the stated line numbers, and the figure hashes.
Usage: selfaudit_reread.py [--help]   (run from anywhere; reads files/fulltext in the main checkout)"""
import hashlib, re, sys
from pathlib import Path
if len(sys.argv) > 1:
    print(__doc__); sys.exit(0)
HERE = Path(__file__).resolve().parent
ROOT = next(p for p in [HERE, *HERE.parents] if (p / "CLAUDE.md").exists())
# worktrees do not carry files/ (untracked evidence store): fall back to the main checkout
cands = [ROOT / "files" / "fulltext", Path("/home/desktop/legend-development/files/fulltext")]
FT = next(p for p in cands if p.exists())
OUP = FT / "PMID42397075_Steinberg2026_OUP-AM_layout.txt"
REP = FT / "PMID33914858_Repudi2021_Brain_operator_supplied.txt"
CHONG = FT / "PMID36537114_Chong2023_SGchunks_text_2026-10-21.txt"
def norm(s): return re.sub(r"\s+", " ", s).strip()
CHECKS = [
 # (premise, file, first line, last line, fragment that must be inside the normalised joined window)
 ("PR1", OUP, 645, 650, "identified the proto-oncogene MYC (also known as c-Myc) as the top significantly upregulated gene in WWOX-deficient RGs (Fig. 3F)"),
 ("PR2a", OUP, 575, 579, "relatively milder disease) exhibited an RG population similar to WT"),
 ("PR2b", OUP, 584, 588, "Importantly, this was not the case in our patient- derived organoids"),
 ("PR2c", OUP, 689, 694, "This increase in MYC expression was observed also in the RGs from SCAR12 and WOREE organoids (Fig. 3J-K"),
 ("PR3a", REP, 377, 381, "premature death (S-Control, n = 13; S-KO, n = 15)"),
 ("PR3b", REP, 657, 663, "Conditional deletion of"),
 ("PR3c", REP, 345, 349, "All (100%) of the N-KO mice died"),
 ("PR3d", REP, 359, 363, "which is expressed at E12.5 and results in Wwox deletion particu-"),
 ("PR4a", OUP, 1106, 1112, "we infected week 10 organoids with either AAV9-WWOX (see"),
 ("PR4b", OUP, 1151, 1157, "WWOX restoration increased the expression of both markers in WOREE organoids but"),
 ("PR4c", OUP, 1172, 1182, "the infection with AAV9-WWOX of WOREE organoids did not affect"),
 ("PR4d", OUP, 1430, 1436, "neuronal WWOX expression was not detected in neural organoids at this point"),
 ("PR5a", OUP, 945, 948, "we performed a MYC inhibition experiment, using a multi-kinase inhibitor (A51)"),
 ("PR5b", OUP, 978, 985, "MYC inhibition, with no change in CTIP2+ neurons, and a mild increase in SATB2+ populations"),
 ("PR5c1", OUP, 380, 380, "Experiments were performed in independent differentiations, except for single-cell RNA-"),
 ("PR5c2", OUP, 386, 387, "seq, MYC inhibition and NSCs CHIP-Seq, using multiple biological replicates"),
 ("PR5d", OUP, 415, 419, "No randomization or blinding was applied in this study."),
 ("PR6", OUP, 662, 668, "across developmental time in human forebrain samples"),
 ("PR7a", OUP, 765, 770, "in WWOX-KO organoids but not in WT (Fig. 4D)"),
 ("PR10", CHONG, 8, 8, "progressive microcephaly, and premature death"),
]
bad = 0
for pid, path, a, b, frag in CHECKS:
    lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
    window = norm(" ".join(re.sub(r"^\s*\d+\s{2,}", "", l) for l in lines[a-1:b]))
    ok = norm(frag) in window
    bad += (not ok)
    print(f"{pid}\t{path.name}\tL{a}-{b}\t{'FOUND' if ok else 'NOT FOUND'}")
HASH = {
 "fig_p34_1430x1589.png": "e072368ea710687ffcd422532b160a687ad02f162cf5e3f78e5b603f59acbc56",
 "fig_p36_1430x1754.jpeg": "23a4ecd347184d9bbe5ef1e59c818bc732486d77da3913b58ee4ae134cad8f4a",
}
for name, h in HASH.items():
    p = FT / "PMID42397075_Steinberg2026_assets" / "figs" / name
    got = hashlib.sha256(p.read_bytes()).hexdigest()
    print(f"{name}\tsha256\t{'MATCH' if got == h else 'DIFFERENT ' + got}")
    bad += (got != h)
print("PROBLEMS", bad)
sys.exit(1 if bad else 0)
