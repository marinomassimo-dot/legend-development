"""ADV-120 sitting 2: measure mean markers with coloured error bars (Obeid 2026 supplement S4A, 200 ppi raster).

Marker = erosion core of the colour mask; error bar = extent of the same colour in the marker's column band
(mean +/- SD per the legend). Calibration A: all y tick marks; B: first and last tick only (end-point check).
Usage: measure_errorbar_points.py <crop.png> <y_axis_col> <yticks csv, top to bottom>
"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from measure_fig3B import load, runs, box_erode, components
from measure_xy_panel import MASKS


def main():
    path, ycol = sys.argv[1], int(sys.argv[2])
    yticks = [float(v) for v in sys.argv[3].split(',')]
    a = load(path)
    blk = (a.max(axis=2) < 90) & ((a.max(axis=2) - a.min(axis=2)) < 25)
    left = blk[:, ycol - 14:ycol - 3].sum(axis=1) >= 6
    yt = [(s + e) / 2.0 for s, e in runs(left)]
    assert len(yt) == len(yticks), (yt, yticks)
    fA = np.polyfit(yt, yticks, 1)
    fB = np.polyfit([yt[0], yt[-1]], [yticks[0], yticks[-1]], 1)
    v = lambda f, r: round(float(f[0] * r + f[1]), 2)
    out = {'y_ticks_px': yt, 'y_px_per_unit': float(-1 / fA[0]), 'series': {}}
    for name, mf in MASKS.items():
        m = mf(a)
        m[:, :ycol + 6] = False
        comps = components(box_erode(m, 7))
        res = []
        for c in comps:
            rr = [p[0] for p in c]; cc = [p[1] for p in c]
            cx, cy = (min(cc) + max(cc)) / 2.0, (min(rr) + max(rr)) / 2.0
            band = m[:, int(cx) - 1:int(cx) + 2].any(axis=1)
            rows = np.nonzero(band)[0]
            top, bot = float(rows.min()), float(rows.max())
            res.append({'x_px': cx, 'mean_A': v(fA, cy), 'mean_B': v(fB, cy), 'upper_end_A': v(fA, top), 'lower_end_A': v(fA, bot),
                        'half_range_A': round((v(fA, top) - v(fA, bot)) / 2, 2), 'core_px': len(c)})
        out['series'][name] = res
    print(json.dumps(out, indent=1, default=lambda o: o.item() if hasattr(o, 'item') else str(o)))


if __name__ == '__main__':
    main()
