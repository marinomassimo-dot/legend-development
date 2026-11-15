#!/usr/bin/env python3
"""Validation of the Fig 7 extractions of PMID 32000863 (Cheng 2020), written to validation.tsv.

Checks, each a number and not a judgement:
  A. Fig 7b control series (stage 0 by construction in the paper's design): the raster mean must be 0 (calibration of the y axis);
  B. Fig 7b read from two files (the article PDF's embedded image and the publisher PNG): mean and maximum absolute difference per
     series, in stage units (this bounds the extraction, not the figure's own content);
  C. lattice distance of the Fig 7b raw means to k/N, in lattice steps, for the series whose lattice step is wider than 5 px
     (the null mice, N = 6 or 4): the vector data of 7d lie on their lattices to within 0.02 steps, so a raster series that lies
     within 0.25 step has an error below a quarter of 1/N;
  D. Fig 7d read as a raster (publisher PNG, 0.5 min sample spacing, markers overlapping) against the exact vector values: mean error
     and mean absolute error per series. This is a harder case than 7b (one-minute spacing) and is a bound, not a calibration of 7b.
Run:  python3 -I validate_fig7.py <fig7d_vector_points.tsv> <b_pdf.tsv> <b_png.tsv> <d_png.tsv> <out_dir>     (--help prints this text)
"""
import csv
import os
import sys


def read(p):
    with open(p, encoding="utf-8") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def mean(v):
    return sum(v) / len(v) if v else float("nan")


def main():
    if "--help" in sys.argv or "-h" in sys.argv or len(sys.argv) < 6:
        print(__doc__)
        return 0
    vec, bp, bn, dn, out = sys.argv[1:6]
    os.makedirs(out, exist_ok=True)
    rows = []
    P = {(r["genotype"], r["arm"], float(r["minute"])): r for r in read(bp) if r["mean_stage_raw"] != ""}
    N = {(r["genotype"], r["arm"], float(r["minute"])): r for r in read(bn) if r["mean_stage_raw"] != ""}
    series = sorted({k[:2] for k in P})
    for g, arm in series:
        kp = [k for k in P if k[:2] == (g, arm)]
        kn = [k for k in N if k[:2] == (g, arm)]
        both = [k for k in kp if k in N]
        diffs = [float(P[k]["mean_stage_raw"]) - float(N[k]["mean_stage_raw"]) for k in both]
        rows.append(["B_pdf_vs_png", g, arm, f"measured pdf {len(kp)} png {len(kn)} both {len(both)}",
                     f"mean diff {mean(diffs):+.3f}; mean abs diff {mean([abs(x) for x in diffs]):.3f}; max abs diff {max([abs(x) for x in diffs]) if diffs else float('nan'):.3f}"])
        if arm == "control":
            for name, d in (("pdf", P), ("png", N)):
                v = [float(d[k]["mean_stage_raw"]) for k in d if k[:2] == (g, arm)]
                rows.append(["A_control_is_zero", g, arm, name, f"mean {mean(v):+.3f}; min {min(v):+.3f}; max {max(v):+.3f}; n {len(v)} (one minute may carry the one animal that scored above 0)"])
        if g == "-/-" and arm in ("PTZ", "PTZ+ETS"):
            for name, d in (("pdf", P), ("png", N)):
                dist = [float(d[k]["lattice_distance_steps"]) for k in d if k[:2] == (g, arm)]
                rows.append(["C_lattice", g, arm, name, f"{len(dist)} points; median {sorted(dist)[len(dist) // 2]:.2f} step; share within 0.25 step {sum(1 for x in dist if x < 0.25) / len(dist):.2f}"])
    V = {(r["genotype"], r["arm"], round(float(r["minute"]) * 2) / 2): float(r["mean_stage"]) for r in read(vec)}
    D = {(r["genotype"], r["arm"], float(r["minute"])): float(r["mean_stage_raw"]) for r in read(dn) if r["mean_stage_raw"] != ""}
    for g, arm in sorted({k[:2] for k in D}):
        ks = [k for k in D if k[:2] == (g, arm) and k in V]
        e = [D[k] - V[k] for k in ks]
        rows.append(["D_7d_raster_vs_vector", g, arm, f"{len(ks)} of 121 points", f"mean error {mean(e):+.3f}; mean abs error {mean([abs(x) for x in e]):.3f}; max abs {max(abs(x) for x in e):.2f}"])
    # lattice property of the exact vector data
    ND = {("+/+", "PTZ"): 12, ("+/+", "PTZ+LiCl"): 8, ("+/-", "PTZ"): 12, ("+/-", "PTZ+LiCl"): 12, ("-/-", "PTZ"): 6, ("-/-", "PTZ+LiCl"): 7}
    for (g, arm), n in ND.items():
        v = [x for (gg, aa, _), x in V.items() if (gg, aa) == (g, arm)]
        dist = [abs(x * n - round(x * n)) for x in v]
        rows.append(["E_vector_lattice", g, arm, f"N {n}", f"{len(v)} points; max distance to k/N {max(dist):.3f} step; share within 0.1 step {sum(1 for x in dist if x < 0.1) / len(dist):.2f}"])
    with open(os.path.join(out, "validation.tsv"), "w", encoding="utf-8") as fh:
        fh.write("check\tgenotype\tseries\tscope\tresult\n")
        for r in rows:
            fh.write("\t".join(r) + "\n")
    for r in rows:
        print("\t".join(r))
    return 0


if __name__ == "__main__":
    sys.exit(main())
