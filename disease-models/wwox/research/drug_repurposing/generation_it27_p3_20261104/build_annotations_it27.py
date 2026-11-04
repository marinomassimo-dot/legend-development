#!/usr/bin/env python3
"""IT27 P3: the verified P47T partial-loss mouse contrast (verification_it27_p1_20261104, DESeq2 ~ sex + genotype) as an INFORMATIONAL annotation on the seed rows the generator already holds.

  build_annotations_it27.py write      append the rows to inputs_it22/seed_annotations.tsv (idempotent)
  build_annotations_it27.py --help

Rule fixed before the result was read: for each defined-direction (up/down) gene seed of Q2, Q3 and Q8, compare its sign with the log2FC of the one mouse ortholog (case-insensitive symbol)
in prefrontal cortex, parietal cortex and hippocampus (cerebellum is descriptive only; the three regions are repeated measures of the same ten animals, one experimental origin).
CONCORDANT = all three regions carry the seed's sign, DISCORDANT = all three the opposite sign, MIXED = otherwise; a |log2FC| under 0.15 carries no sign (counts as MIXED). Significance is NOT part of the tag (n 5 v 5, partial-loss missense, tissue mixed).
The tags are informational: they are not in SUPPORT_LIMITING_GUARDS, so they reach the proposal's `seed_guards` column and change no order. Offline, standard library only."""
import sys
if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
    print(__doc__); raise SystemExit(0)
import csv, gzip, collections
from pathlib import Path
H = Path(__file__).resolve().parent
D = H.parent
IN = D / "generation_it22_p1_20261103" / "inputs_it22"
SRC = "verification_it27_p1_20261104 (p1a_all_regions_own_results.tsv.gz, DESeq2 ~sex+genotype; PFC, CTX, HPC; P47T v WT, 5 v 5)"
REGIONS = ("PFC", "CTX", "HPC")
MIN_ABS_LFC = 0.15      # added after the preview showed PSAT1 (-0.03) called DISCORDANT by sign alone: a defect of the first draft, not a choice made for an outcome


def lfc_table():
    t = collections.defaultdict(dict)
    for r in csv.DictReader(gzip.open(D / "verification_it27_p1_20261104/results/p1a_all_regions_own_results.tsv.gz", "rt"), delimiter="\t"):
        if r["region"] in REGIONS:
            t[r["symbol"].upper()][r["region"]] = float(r["log2FoldChange"])
    return t


def tag(direction, lfcs):
    want = 1 if direction == "up" else -1
    s = [(1 if x > 0 else -1) if abs(x) >= MIN_ABS_LFC else 0 for x in lfcs]      # a log2FC under 0.15 carries no sign
    return "CONCORDANT" if all(v == want for v in s) else "DISCORDANT" if all(v == -want for v in s) else "MIXED"


def rows():
    t = lfc_table()
    out = []
    for q in ("Q2_expression_tiersAB", "Q3_expression_tiersAB", "Q8_expression_tiersAB"):
        for r in csv.DictReader(open(IN / "seeds_p1" / f"{q}.tsv"), delimiter="\t"):
            if r["kind"] != "gene" or r["direction"] not in ("up", "down") or r["direction_status"] != "defined":
                continue
            d = t.get(r["gene"].upper())
            if not d or len(d) < 3:
                continue
            lf = [d[x] for x in REGIONS]
            out.append((r["source_ref"], "P47T_PARTIAL_LOSS_MOUSE_" + tag(r["direction"], lf), SRC + "; log2FC " + "/".join(f"{x:+.2f}" for x in lf) + " (PFC/CTX/HPC)"))
    return out


if sys.argv[1] == "write":
    f = IN / "seed_annotations.tsv"
    have = {tuple(r) for r in csv.reader(open(f), delimiter="\t")}
    new = [r for r in rows() if tuple(r) not in have]
    with open(f, "a", newline="") as fh:
        csv.writer(fh, delimiter="\t", lineterminator="\n").writerows(new)
    for r in new:
        print("\t".join(r)[:200])
    print(len(new), "rows appended")
