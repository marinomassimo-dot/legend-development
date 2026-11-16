#!/usr/bin/env python3
"""Read the medians of the three genotype curves in Fig. 4 panels B (mEPSC amplitude) and C (mEPSC frequency) of Breton 2021 by pixel geometry, as PREREGISTRATION_FIG4_MEPSC_SECOND_READ.md fixes it.

    python3 read_fig4_curves.py calibrate --img gr4.jpg --out <dir>      stage 1: axis lines and ticks only (no curve is read)
    python3 read_fig4_curves.py read      --img gr4.jpg --out <dir>      stage 2: curve medians, f, uncertainty (run only after stage 1 is accepted and this script is committed)
    python3 read_fig4_curves.py --help

Panels are located by the search windows PANEL (pixel boxes of the 708 x 675 figure; chosen from the figure layout, not from any curve value). Not medical advice.
"""
import argparse, json, sys
from pathlib import Path
ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument("stage", nargs="?", choices=["calibrate", "read"]); ap.add_argument("--img"); ap.add_argument("--out")
a = ap.parse_args()
if not (a.stage and a.img and a.out):
    ap.print_help(); sys.exit(0)
import numpy as np, pymupdf
pm = pymupdf.Pixmap(a.img); im = np.frombuffer(pm.samples, np.uint8).reshape(pm.height, pm.width, pm.n)[:, :, :3].astype(int)
R, G, B = im[:, :, 0], im[:, :, 1], im[:, :, 2]
dark = (R < 90) & (G < 90) & (B < 90)                       # black class
blue = (B > 140) & (R < 110) & (G < 110)
red = (R > 170) & (G < 90) & (B < 90)
# panel search boxes (x0, x1, y0, y1) in figure pixels, from the layout; units and tick values are fixed by the preregistration
PANEL = {"B": {"box": (315, 560, 0, 215), "xticks": [-50 + 5 * i for i in range(11)], "unit": "pA"},
         "C": {"box": (245, 560, 160, 330), "xticks": [10 * i for i in range(9)], "unit": "Hz"}}
YT = [0.2 * i for i in range(6)]
def runs(mask1d, minlen):
    out, s = [], None
    for i, v in enumerate(list(mask1d) + [False]):
        if v and s is None: s = i
        if not v and s is not None:
            if i - s >= minlen: out.append((s, i - 1))
            s = None
    return out
def calibrate(name):
    """Amendment 1: anchors are the axis lines (no tick marks are resolved); the printed labels are the cross-check."""
    x0, x1, y0, y1 = PANEL[name]["box"]; sub = dark[y0:y1, x0:x1]
    base_row = int(np.argmax(sub.sum(axis=1))) + y0                 # x-axis line: the row with the most dark pixels in the box
    left_col = int(np.argmax(sub.sum(axis=0))) + x0                 # y-axis line: the column with the most dark pixels
    rows = [base_row - 1, base_row, base_row + 1]
    xs = [x for x in range(x0, x1) if dark[rows, x].sum() >= 2]
    right_end = max(xs)                                              # right end of the x-axis line
    ycol = [y for y in range(y0, y1) if dark[y, left_col - 1:left_col + 2].any()]
    top = min(ycol)                                                  # top end of the y-axis line
    xt = PANEL[name]["xticks"]; xmin, xmax = xt[0], xt[-1]
    px = lambda v: left_col + (v - xmin) / (xmax - xmin) * (right_end - left_col)
    # label centres: clusters of dark pixels in the band just below the axis, gap > 4 px separates labels
    band = dark[base_row + 5:base_row + 16, x0:x1].any(axis=0)
    cl = [((s + e) / 2 + x0, e - s + 1) for s, e in runs(band, 1)]
    merged = []
    for c, w in cl:
        if merged and c - merged[-1][0] < 6: merged[-1] = ((merged[-1][0] + c) / 2, merged[-1][1] + w)
        else: merged.append((c, w))
    dev = []
    for v in xt:
        near = min(merged, key=lambda m: abs(m[0] - px(v))) if merged else None
        dev.append({"label_value": v, "predicted_px": round(px(v), 1), "nearest_label_cluster_px": (round(near[0], 1) if near else None)})
    mx = max((abs(d["predicted_px"] - d["nearest_label_cluster_px"]) for d in dev if d["nearest_label_cluster_px"] is not None), default=None)
    return {"baseline_row": base_row, "left_col": left_col, "right_end": right_end, "top_of_y_axis": top, "label_cross_check": dev, "largest_label_deviation_px": mx}
cal = {k: calibrate(k) for k in PANEL}
Path(a.out).mkdir(parents=True, exist_ok=True)
(Path(a.out) / "calibration_stage1.json").write_text(json.dumps(cal, indent=1) + "\n")
print(json.dumps(cal, indent=1))
if a.stage == "calibrate": sys.exit(0)
# ---- stage 2: medians (cumulative probability 0.5) of the black (S-WT), blue (S-HT) and red (S-KO) curves, exactly as the preregistration and Amendment 1 fix them
import math, itertools, csv
INSET = (345, 425, 20, 110)                       # panel B inset (x0, x1, y0, y1): excluded
CLASS = {"S-WT": dark, "S-HT": blue, "S-KO": red}
res = {}
for name, P in PANEL.items():
    c = cal[name]; x0, x1, y0, y1 = P["box"]; xt = P["xticks"]; xmin, xmax = xt[0], xt[-1]
    base_y = c["baseline_row"] + 0.5; top = c["top_of_y_axis"]; row50 = base_y - 0.5 * (base_y - top)
    span = c["right_end"] - c["left_col"]; unit = (xmax - xmin) / span
    out = {"row_p50": row50, "unit_per_px": unit, "genotypes": {}}
    for g, m in CLASS.items():
        pts = []
        for y in range(int(math.floor(row50 - 1)), int(math.ceil(row50 + 1)) + 1):
            if abs(y - row50) > 1.0: continue
            for x in range(c["left_col"] + 2, c["right_end"] - 1):
                if name == "B" and INSET[0] <= x <= INSET[1] and INSET[2] <= y <= INSET[3]: continue
                if m[y, x]: pts.append(x)
        if not pts:
            out["genotypes"][g] = {"status": "hidden (no pixel of the class in the band)"}; continue
        px = float(np.mean(pts)); u = (px - c["left_col"]) / span
        val = xmin + (px - c["left_col"]) * unit
        unc_px = math.sqrt(1.5 ** 2 + (2 * (1 - u)) ** 2 + (2 * u) ** 2)
        out["genotypes"][g] = {"status": "read", "pixels_in_band": len(pts), "median_px": round(px, 2), "median_value": round(val, 3), "uncertainty_value": round(unc_px * unit, 3)}
    # f = (S-HT - S-KO)/(S-WT - S-KO) with the extremes of the uncertainty band; amplitude is read as magnitude (more negative = larger)
    gs = out["genotypes"]
    if all(gs[g]["status"] == "read" for g in CLASS):
        sign = -1 if name == "B" else 1
        v = {g: sign * gs[g]["median_value"] for g in CLASS}; d = {g: gs[g]["uncertainty_value"] for g in CLASS}
        f = (v["S-HT"] - v["S-KO"]) / (v["S-WT"] - v["S-KO"]) if v["S-WT"] != v["S-KO"] else float("nan")
        fs = []
        for sg in itertools.product((-1, 1), repeat=3):
            a, b2, k = (v["S-WT"] + sg[0] * d["S-WT"], v["S-HT"] + sg[1] * d["S-HT"], v["S-KO"] + sg[2] * d["S-KO"])
            if a != k: fs.append((b2 - k) / (a - k))
        sep = abs(v["S-WT"] - v["S-KO"]) > math.sqrt(d["S-WT"] ** 2 + d["S-KO"] ** 2)
        cls = lambda x: "near controls" if x >= 0.75 else ("midway" if x >= 0.25 else "near knockout")
        labels = {cls(x) for x in fs + [f]}
        out["f"] = {"nominal": round(f, 3), "range_min": round(min(fs), 3), "range_max": round(max(fs), 3), "separable": bool(sep),
                    "classification": ("not separable (|S-WT - S-KO| within the combined pixel uncertainty)" if not sep else (cls(f) if len(labels) == 1 else f"undecided (calibration-limited): nominal {cls(f)}, band spans {sorted(labels)}"))}
    res[name] = out
(Path(a.out) / "fig4_mepsc_medians.json").write_text(json.dumps(res, indent=1) + "\n")
print(json.dumps(res, indent=1))
