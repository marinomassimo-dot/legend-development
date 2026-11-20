"""ADV-120 sitting 2: measure marker values on a line or scatter panel of Obeid 2026 (raster, 500 ppi).

Two independent y calibrations: A = protruding tick marks (when the axis has them), B = vertical centres
of the printed tick labels. x is calibrated from the tick marks under the axis.
Markers = erosion cores of each colour mask (square marker ~15 px; a 5 px line is removed).
Usage: measure_xy_panel.py <crop.png> <x_axis_row> <y_axis_col> <xticks csv> <yticks csv> <ages csv> [series csv]
Prints JSON. A series whose marker is hidden behind another marker at an age is reported as occluded.
"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from measure_fig3B import load, runs, box_erode, components

MASKS = {
    'WT': lambda a: (a[..., 0] < 70) & (a[..., 1] < 70) & (a[..., 2] > 100) & (a[..., 2] - a[..., 0] > 80) & (a[..., 2] - a[..., 1] > 80),
    'KO': lambda a: (a[..., 0] > 100) & (a[..., 0] < 200) & (a[..., 1] < 100) & (a[..., 2] > 130) & (a[..., 2] - a[..., 1] > 60),
    'LD': lambda a: (a[..., 0] < 60) & (a[..., 1] > 70) & (a[..., 1] - a[..., 0] > 60) & (a[..., 1] - a[..., 2] > 25),
    'HD': lambda a: (a[..., 0] > 200) & (a[..., 1] < 70) & (a[..., 2] < 70),
}


def merged_label_centres(dark, c0, c1, r0, r1):
    v = dark[r0:r1, c0:c1].sum(axis=1) > 0
    rr = [(s + r0, e + r0) for s, e in runs(v)]
    out = []
    for s, e in rr:
        if out and s - out[-1][1] < 12:
            out[-1] = (out[-1][0], e)
        else:
            out.append((s, e))
    return [((s + e) / 2.0, e - s + 1) for s, e in out]


def main():
    path, xrow, ycol = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    xticks = [float(v) for v in sys.argv[4].split(',')]
    yticks = [float(v) for v in sys.argv[5].split(',')]
    ages = [float(v) for v in sys.argv[6].split(',')]
    series = sys.argv[7].split(',') if len(sys.argv) > 7 else list(MASKS)
    a = load(path)
    dark = a.sum(axis=2) < 150
    h, w = dark.shape
    # x ticks (all lengths): dark rows just under the axis
    below = dark[xrow + 6:xrow + 14, :].sum(axis=0) >= 6
    xt = [(s + e) / 2.0 for s, e in runs(below)]
    out = {'x_ticks_px_found': xt}
    # anchor on the first and last found ticks; snap each labelled value to the nearest found tick
    # (some axes carry unlabelled minor ticks, e.g. every third of a decade)
    xs = sorted(xt)
    lin = lambda v: xs[0] + (xs[-1] - xs[0]) * (v - xticks[0]) / (xticks[-1] - xticks[0])
    snapped = [min(xs, key=lambda t: abs(t - lin(v))) for v in xticks]
    out['x_ticks_used_px'] = snapped
    fx = np.polyfit(xticks, snapped, 1)
    day = lambda c: (c - fx[1]) / fx[0]
    # y calibration A: tick marks left of the axis
    left = dark[:, ycol - 16:ycol - 7].sum(axis=1) >= 8
    yt = [(s + e) / 2.0 for s, e in runs(left) if e - s >= 2 and s < xrow + 8]
    out['y_ticks_px_found'] = yt
    fitA = None
    if len(yt) == len(yticks):
        fitA = np.polyfit(yt, sorted(yticks, reverse=True), 1)
    # calibration B: label centres
    lab = [c for c, hh in merged_label_centres(dark, ycol - 70, ycol - 24, 40, xrow + 25) if hh > 12]
    out['y_label_centres_px'] = lab
    fitB = None
    if len(lab) == len(yticks):
        fitB = np.polyfit(lab, sorted(yticks, reverse=True), 1)
    assert fitA is not None or fitB is not None, 'no y calibration'
    fitA = fitA if fitA is not None else fitB
    fitB = fitB if fitB is not None else fitA
    out['y_px_per_unit_A'] = float(-1 / fitA[0])
    out['y_px_per_unit_B'] = float(-1 / fitB[0])
    res = {}
    for name in series:
        m = MASKS[name](a)
        m[:, :ycol + 6] = False
        core = box_erode(m, 9)
        mk = []
        for c in components(core):
            rr = [p[0] for p in c]; cc = [p[1] for p in c]
            mk.append(((min(cc) + max(cc)) / 2.0, (min(rr) + max(rr)) / 2.0, max(cc) - min(cc) + 10, max(rr) - min(rr) + 10))
        rows = []
        for ag in ages:
            cpx = fx[0] * ag + fx[1]
            cand = [k for k in mk if abs(k[0] - cpx) <= 10]
            if not cand:
                # fallback: the visible edges of a partly hidden marker (marker is ~17 px square: centre = edge -/+ 8.5 px)
                cols = slice(int(cpx) - 7, int(cpx) + 8)
                vis = np.nonzero(m[:, cols].sum(axis=1) >= 8)[0]
                vis = vis[(vis > 20) & (vis < xrow - 6)]
                if len(vis) == 0:
                    rows.append({'age': ag, 'status': 'no marker (absent, hidden, or clipped by the axis)'})
                else:
                    # first contiguous visible run only (a legend marker may lie in the same column band)
                    first = next(iter(runs(np.isin(np.arange(vis.max() + 1), vis))))
                    top, bot = float(first[0]), float(first[1])
                    f = lambda r: round(float(fitA[0] * r + fitA[1]), 2)
                    rows.append({'age': ag, 'status': 'partly occluded: edge-derived candidates (upper edge assumed or lower edge assumed)',
                                 'visible_rows_px': (top, bot), 'value_if_upper_edge_visible': f(top + 8.5),
                                 'value_if_lower_edge_visible': f(bot - 8.5)})
                continue
            k = min(cand, key=lambda t: abs(t[0] - cpx))
            rows.append({'age': ag, 'value_A': round(float(fitA[0] * k[1] + fitA[1]), 2),
                         'value_B': round(float(fitB[0] * k[1] + fitB[1]), 2),
                         'marker_px_wh': (int(k[2]), int(k[3]))})
        res[name] = rows
    out['series'] = res
    print(json.dumps(out, indent=1, default=lambda o: o.item() if hasattr(o, 'item') else str(o)))


if __name__ == '__main__':
    main()
