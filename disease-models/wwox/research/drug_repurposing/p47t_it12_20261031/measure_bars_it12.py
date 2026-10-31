#!/usr/bin/env python3
"""IT12 P2-P47T: pixel measurement of NES bar lengths in Fig 8b and Fig 9c of PMC10835625 (raster JPG; no vector source exists on the PMC surface).
Usage: measure_bars_it12.py run IMG8 IMG9 OUT   (pymupdf + numpy; --help prints this). Axis calibration is read from the tick marks found by the script and printed."""
import sys
if len(sys.argv) < 2 or sys.argv[1] != "run":
    print(__doc__); raise SystemExit(0)
import numpy as np, pymupdf
def load(p):
    pm = pymupdf.Pixmap(p); a = np.frombuffer(pm.samples, np.uint8).reshape(pm.height, pm.width, pm.n)[:, :, :3].astype(int); return a
def runs(mask):
    out = []; s = None
    for i, v in enumerate(mask):
        if v and s is None: s = i
        if not v and s is not None: out.append((s, i - 1)); s = None
    if s is not None: out.append((s, len(mask) - 1))
    return out
res = []
# ---- Fig 8b: panel b occupies x > 1150; axis ticks (0, 0.5 ... 2.5) are dark vertical ticks below the axis line near y~830
a8 = load(sys.argv[2]); H, W, _ = a8.shape
dark = (a8.sum(2) < 200)
# find the horizontal axis line of panel b: a long dark row in x 1150..1600 with y 780..870
cand = [(int(dark[y, 1150:].sum()), y) for y in range(780, 880)]
yaxis = max(cand)[1]
# tick marks: dark pixels just below axis line
tick_cols = [x for x in range(1150, W) if dark[yaxis + 6:yaxis + 14, x].sum() >= 6]
tk = [(s + e) / 2 for s, e in runs(np.isin(np.arange(W), tick_cols))]
print("fig8b axis y", yaxis, "tick x", tk)
x0, x25 = tk[0], tk[-1]; scale = (x25 - x0) / 2.5
def nes8(xend): return (xend - x0) / scale
# bars: coloured (blue-ish) pixels; classify rows by colour. PFC light fill (200-215,230,245) with blue outline; CTX medium (0,150-170,255); HPC dark navy (0,20-40,140-160)
def classify(px):
    r, g, b = px
    if r < 40 and g < 60 and 110 < b < 190: return "HPC"
    if r < 40 and 120 < g < 190 and b > 220: return "CTX"
    return None
rows = {}
for y in range(100, yaxis - 5):
    for x in range(1190, W):
        c = classify(a8[y, x])
        if c: rows.setdefault(y, {}).setdefault(c, []).append(x)
# group by contiguous y per colour
for col in ["HPC", "CTX"]:
    ys = [y for y in rows if col in rows[y] and len(rows[y][col]) > 40]
    for s, e in runs(np.isin(np.arange(H), ys)):
        xs = max(max(rows[y][col]) for y in range(s, e + 1) if col in rows[y]) if e - s >= 8 else None
        if xs: res.append(["Fig8b", col, "y %d-%d" % (s, e), "%.2f" % nes8(xs)])
# PFC: outlined light bars; outline colour approx (0,150,230)?; measure rightmost outline pixel in the band between CTX bar bottom and next HPC bar top is fiddly: use light-blue fill
for y in range(100, yaxis - 5):
    for x in range(1190, W):
        r, g, b = a8[y, x]
        if 190 < r < 225 and 220 < g < 245 and b > 240:
            rows.setdefault(y, {}).setdefault("PFC", []).append(x)
ys = [y for y in rows if "PFC" in rows[y] and len(rows[y]["PFC"]) > 40]
for s, e in runs(np.isin(np.arange(H), ys)):
    if e - s >= 8:
        xs = max(max(rows[y]["PFC"]) for y in range(s, e + 1) if "PFC" in rows[y]); res.append(["Fig8b", "PFC", "y %d-%d" % (s, e), "%.2f" % nes8(xs + 3)])
# ---- Fig 9c: single colour bars (0,150,255); axis ticks 0..3 below axis at y~1520-1535
a9 = load(sys.argv[3]); H9, W9, _ = a9.shape
dk9 = (a9.sum(2) < 200)
cand = [(int(dk9[y, 540:960].sum()), y) for y in range(1480, 1560)]
y9 = max(cand)[1]
tc = [x for x in range(540, 960) if dk9[y9 + 5:y9 + 14, x].sum() >= 6]
tk9 = [(s + e) / 2 for s, e in runs(np.isin(np.arange(W9), tc))]
print("fig9c axis y", y9, "tick x", tk9)
z0, z3 = tk9[0], tk9[-1]; sc9 = (z3 - z0) / 3.0
blue = (a9[:, :, 0] < 40) & (a9[:, :, 1] > 120) & (a9[:, :, 1] < 190) & (a9[:, :, 2] > 220)
bars = [y for y in range(700, y9 - 5) if blue[y, 548:960].sum() > 40]
labels = ["OXIDATIVE_PHOSPHORYLATION", "FATTY_ACID_METABOLISM", "ADIPOGENESIS", "REACTIVE_OXYGEN_SPECIES_PATHWAY", "CHOLESTEROL_HOMEOSTASIS", "APOPTOSIS", "INFLAMMATORY_RESPONSE", "IL6_JAK_STAT3_SIGNALING", "GLYCOLYSIS", "HYPOXIA"]
bl = [(s, e) for s, e in runs(np.isin(np.arange(H9), bars)) if e - s >= 15]
for lab, (s, e) in zip(labels, bl):
    xs = max(np.where(blue[(s + e) // 2, 548:960])[0]) + 548
    res.append(["Fig9c_CB", lab, "y %d-%d" % (s, e), "%.2f" % ((xs - z0) / sc9)])
print("fig9c bars found", len(bl))
L8 = ["TNFA_SIGNALING_VIA_NFKB", "IL6_JAK_STAT3_SIGNALING", "INFLAMMATORY_RESPONSE", "HYPOXIA", "APOPTOSIS", "GLYCOLYSIS"]
cnt = {}
for r in res:
    if r[0] == "Fig8b":
        k = cnt.get(r[1], 0); cnt[r[1]] = k + 1; r[2] = L8[k] + " [" + r[2] + "]"
with open(sys.argv[4], "w") as fh:
    fh.write("figure\tseries_or_set\tpixel_rows\tNES_by_pixel_measurement_approx\n")
    for r in res: fh.write("\t".join(r) + "\n")
for r in res: print(r)
