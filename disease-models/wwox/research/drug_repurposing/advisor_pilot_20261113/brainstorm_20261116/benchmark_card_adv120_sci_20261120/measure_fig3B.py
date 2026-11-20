"""ADV-120 sitting 2: measure Obeid 2026 Fig 3B (survival curves) from the 500 ppi supplement raster.

Input: a PNG crop of panel 3B at native resolution (see the result file for the crop recipe).
No vector layer exists in the article PDF (stated in the pre-registration), so the route is raster.
Calibration (stated, not assumed): x from the four printed ticks 0, 100, 200, 300 found by script;
y from the vertical centres of the printed tick labels 0, 50, 100 (the y axis has no protruding
ticks), cross-checked against the x-axis row.
Two independent passes per series:
  pass 1: horizontal step segments (levels and the x extent of each level);
  pass 2: event squares (centroids), by a window-erosion on the colour mask.
Usage: measure_fig3B.py <crop.png> <x_axis_row> <y_axis_col>
"""
import subprocess, sys, json
import numpy as np


def load(path):
    w, h = map(int, subprocess.check_output(['identify', '-format', '%w %h', path]).split())
    raw = subprocess.check_output(['convert', path, '-depth', '8', 'rgb:-'])
    return np.frombuffer(raw, dtype=np.uint8).reshape(h, w, 3).astype(int)


def runs(v):
    out, s = [], None
    for i, x in enumerate(v):
        if x and s is None:
            s = i
        if not x and s is not None:
            out.append((s, i - 1))
            s = None
    if s is not None:
        out.append((s, len(v) - 1))
    return out


def label_centres(dark, col_lo, col_hi, row_lo, row_hi):
    """vertical centres of the printed digit groups left of the y axis (tick labels)"""
    v = dark[row_lo:row_hi, col_lo:col_hi].sum(axis=1) > 0
    rr = [(s + row_lo, e + row_lo) for s, e in runs(v)]
    # merge runs closer than 12 rows (digits of one label)
    merged = []
    for s, e in rr:
        if merged and s - merged[-1][1] < 12:
            merged[-1] = (merged[-1][0], e)
        else:
            merged.append((s, e))
    return [((s + e) / 2.0, e - s + 1) for s, e in merged]


MASKS = {
    'WT': lambda a: (a[..., 0] < 70) & (a[..., 1] < 70) & (a[..., 2] > 100) & (a[..., 2] - a[..., 0] > 80) & (a[..., 2] - a[..., 1] > 80),
    'KO': lambda a: (a[..., 0] > 100) & (a[..., 0] < 200) & (a[..., 1] < 100) & (a[..., 2] > 130) & (a[..., 2] - a[..., 1] > 60),
    'LD': lambda a: (a[..., 0] < 60) & (a[..., 1] > 90) & (a[..., 2] < 110) & (a[..., 1] - a[..., 0] > 80) & (a[..., 1] - a[..., 2] > 50),
    'HD': lambda a: (a[..., 0] > 200) & (a[..., 1] < 70) & (a[..., 2] < 70),
}


def box_erode(mask, k):
    ii = np.pad(mask.astype(np.int64), ((1, 0), (1, 0))).cumsum(0).cumsum(1)
    h, w = mask.shape
    s = ii[k:, k:] - ii[:-k, k:] - ii[k:, :-k] + ii[:-k, :-k]
    out = np.zeros_like(mask)
    out[k // 2:k // 2 + h - k + 1, k // 2:k // 2 + w - k + 1] = (s == k * k)
    return out


def components(mask):
    pts = set(zip(*np.nonzero(mask)))
    comps = []
    while pts:
        stack = [pts.pop()]
        c = list(stack)
        while stack:
            r, q = stack.pop()
            for dr in (-1, 0, 1):
                for dq in (-1, 0, 1):
                    n = (r + dr, q + dq)
                    if n in pts:
                        pts.remove(n)
                        stack.append(n)
                        c.append(n)
        comps.append(c)
    return comps


def main():
    path, xrow, ycol = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    a = load(path)
    dark = a.sum(axis=2) < 150
    h, w = dark.shape
    # x calibration from tick columns just below the x axis
    below = dark[xrow + 6:xrow + 25, :].sum(axis=0) >= 12
    xt = [(s + e) / 2.0 for s, e in runs(below)]
    assert len(xt) == 4, xt
    xdays = np.array([0, 100, 200, 300.0])
    px_per_day = np.polyfit(xdays, xt, 1)
    day = lambda col: (col - px_per_day[1]) / px_per_day[0]
    # y calibration A: tick-label centres (labels 0, 50, 100 from the bottom)
    lab = label_centres(dark, ycol - 30, ycol - 14, 60, xrow + 20)
    lab = [c for c, hgt in lab if hgt > 15]
    lab = sorted(lab)[:3]
    assert len(lab) == 3, lab
    pct_lab = np.array([100, 50, 0.0])
    fitA = np.polyfit(lab, pct_lab, 1)            # pct = a*row + b
    # calibration B: x-axis row = 0 percent, and the 100 label centre = 100 percent
    fitB = np.polyfit([xrow, lab[0]], [0.0, 100.0], 1)
    ypctA = lambda r: fitA[0] * r + fitA[1]
    ypctB = lambda r: fitB[0] * r + fitB[1]
    out = {'x_ticks_px': xt, 'x_px_per_day': float(px_per_day[0]),
           'y_label_centres_px': lab, 'y_px_per_pct_A': float(-1 / fitA[0]),
           'axis_row': xrow}
    # exclude the legend (inside the plot, right half, middle rows) and the axes
    res = {}
    for name, f in MASKS.items():
        m = f(a)
        m[:, :ycol + 6] = False
        m[:60, :] = False
        # legend box: columns right of day 135, rows between about 58 and 8 percent
        r_lo = int((lab[2] - lab[0]) * 0 + lab[0] + 0.42 * (lab[2] - lab[0]))
        r_hi = int(lab[0] + 0.93 * (lab[2] - lab[0]))
        c_lo = int(px_per_day[1] + px_per_day[0] * 135)
        m[r_lo:r_hi, c_lo:] = False
        # pass 1: horizontal segments >= 25 columns long, row bands
        segs = []
        for r in range(h):
            for s, e in runs(m[r, :]):
                if e - s + 1 >= 25:
                    segs.append((r, s, e))
        bands = []
        for r, s, e in segs:
            if bands and r - bands[-1]['r1'] <= 1 and not (e < bands[-1]['s'] - 5 or s > bands[-1]['e'] + 5):
                b = bands[-1]
                b['r1'] = r
                b['s'] = min(b['s'], s)
                b['e'] = max(b['e'], e)
            else:
                bands.append({'r0': r, 'r1': r, 's': s, 'e': e})
        p1 = []
        for b in bands:
            rc = (b['r0'] + b['r1']) / 2.0
            p1.append({'pct_A': round(ypctA(rc), 2), 'pct_B': round(ypctB(rc), 2),
                       'day_from': round(day(b['s']), 1), 'day_to': round(day(b['e']), 1),
                       'band_rows': (b['r0'], b['r1'])})
        # pass 2: squares (interior of 15x15 full windows)
        core = box_erode(m, 15)
        sq = []
        for c in components(core):
            rr = [p[0] for p in c]
            cc = [p[1] for p in c]
            rcen, ccen = (min(rr) + max(rr)) / 2.0, (min(cc) + max(cc)) / 2.0
            sq.append({'day': round(day(ccen), 1), 'pct_A': round(ypctA(rcen), 2), 'pct_B': round(ypctB(rcen), 2),
                       'size_px': (max(cc) - min(cc) + 1 + 14, max(rr) - min(rr) + 1 + 14)})
        sq.sort(key=lambda d: d['day'])
        res[name] = {'pass1_horizontal_segments': p1, 'pass2_squares': sq}
    out['series'] = res
    # pass 3: vertical profile at fixed ages (independent of pass 1 and 2); every colour run in the column
    ages = [10, 15, 20, 30, 45, 60, 75, 90, 100, 150, 200, 250, 295]
    prof = {}
    for name, f in MASKS.items():
        m = f(a)
        m[:, :ycol + 6] = False
        m[:60, :] = False
        r_lo = int(lab[0] + 0.42 * (lab[2] - lab[0])); r_hi = int(lab[0] + 0.93 * (lab[2] - lab[0]))
        m[r_lo:r_hi, int(px_per_day[1] + px_per_day[0] * 135):] = False
        pr = {}
        for d in ages:
            col = int(round(px_per_day[1] + px_per_day[0] * d))
            found = []
            for s0, e0 in runs(m[:, col]):
                found.append({'pct_A': round(ypctA((s0 + e0) / 2.0), 1), 'run_px': e0 - s0 + 1})
            pr[str(d)] = found
        prof[name] = pr
    out['pass3_profile_at_ages'] = prof
    print(json.dumps(out, indent=1, default=lambda o: o.item() if hasattr(o, 'item') else str(o)))


if __name__ == '__main__':
    main()
