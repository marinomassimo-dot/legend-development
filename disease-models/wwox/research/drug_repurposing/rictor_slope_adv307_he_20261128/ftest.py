"""Extra, outside the PREREG: can the paper's F = 0.305 (two regression slopes) be reproduced from the sheet?"""
import sys, importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("a", Path(__file__).with_name("analyse.py")); a = importlib.util.module_from_spec(spec); spec.loader.exec_module(a)
S = a.slices(a.sheet1(sys.argv[1]))


def fit(pts):
    x, y = zip(*pts); slope, icpt, _ = a.ols(list(x), list(y))
    return slope, sum((q - icpt - slope * p) ** 2 for p, q in pts), sum((p - sum(x) / len(x)) ** 2 for p in x), \
        sum((p - sum(x) / len(x)) * (q - sum(y) / len(y)) for p, q in pts), sum((q - sum(y) / len(y)) ** 2 for q in y)


for name, pt in (("time on distance", lambda d, t: (d, t)), ("distance on time", lambda d, t: (t, d)),
                 ("per-point velocity d/t on time", lambda d, t: (t, d / t))):
    g = {k: [pt(r[1], r[2]) for s in S if s["genotype"] == k for r in s["rows"]] for k in ("Control", "CKO")}
    f = {k: fit(v) for k, v in g.items()}
    sse_sep = sum(v[1] for v in f.values()); n = sum(len(v) for v in g.values())
    sxx = sum(v[2] for v in f.values()); sxy = sum(v[3] for v in f.values()); syy = sum(v[4] for v in f.values())
    sse_common = syy - sxy ** 2 / sxx
    F = (sse_common - sse_sep) / (sse_sep / (n - 4))
    print(f"{name}: slope control {f['Control'][0]:.4f} CKO {f['CKO'][0]:.4f} F(1,{n-4}) = {F:.3f}")
