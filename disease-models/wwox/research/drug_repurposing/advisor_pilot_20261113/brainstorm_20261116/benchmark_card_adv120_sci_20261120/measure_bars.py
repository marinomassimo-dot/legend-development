"""ADV-120 sitting 2: measure every bar of a bar chart (Obeid 2026 raster, 500 ppi), left to right.

A bar = a run of columns in which one colour fills at least MINH rows above the baseline; its value is the
top edge of the colour in the bar's central columns; the error cap is the highest black run above the bar top
within the bar's x range. Two y calibrations (tick marks, tick-label centres) as in measure_dots.py.
Usage: measure_bars.py <crop.png> <x_axis_row> <y_axis_col> <yticks csv> [minh] [small|-] [labwin lo,hi offsets]
Colours: navy (wild type) and purple (knockout) as drawn in Fig 6; any other colour is ignored.
"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from measure_fig3B import load, runs
from measure_xy_panel import merged_label_centres

COL = {
    'navy': lambda a: (a[..., 2] > 90) & (a[..., 0] < 70) & (a[..., 1] < 70) & (a[..., 2] - a[..., 0] > 70),
    'purple': lambda a: (a[..., 0] > 90) & (a[..., 0] < 200) & (a[..., 1] < 100) & (a[..., 2] > 130) & (a[..., 2] - a[..., 1] > 60),
    'red': lambda a: (a[..., 0] > 200) & (a[..., 1] < 70) & (a[..., 2] < 70),
    'green': lambda a: (a[..., 1] > 90) & (a[..., 0] < 90) & (a[..., 1] - a[..., 0] > 60) & (a[..., 2] < 120),
}


def main():
    path, xrow, ycol = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    yticks = sorted([float(v) for v in sys.argv[4].split(',')], reverse=True)
    minh = int(sys.argv[5]) if len(sys.argv) > 5 else 25
    small = len(sys.argv) > 6 and sys.argv[6] == "small"   # 200 ppi panels: short ticks, no label calibration
    a = load(path)
    blk = (a.max(axis=2) < 90) & ((a.max(axis=2) - a.min(axis=2)) < 25)
    left = (((a.max(axis=2) < 110) & ((a.max(axis=2) - a.min(axis=2)) < 30))[:, ycol - 6:ycol - 1].sum(axis=1) >= 4) if small else (blk[:, ycol - 16:ycol - 7].sum(axis=1) >= 8)
    yt = [(s + e) / 2.0 for s, e in runs(left) if e - s >= (1 if small else 2) and s < xrow + 8]
    lo_off, hi_off = (int(v) for v in sys.argv[7].split(',')) if len(sys.argv) > 7 else (90, 24)
    labmask = blk if not (len(sys.argv) > 7) else ((a.max(axis=2) < 130) & ((a.max(axis=2) - a.min(axis=2)) < 35))
    lab = [c for c, hh in merged_label_centres(labmask, ycol - lo_off, ycol - hi_off, 10, xrow + 25) if hh > 12]
    out = {'y_ticks_px_found': yt, 'y_label_centres_px_all': lab}
    if len(lab) > len(yticks):
        lab = lab[-len(yticks):]   # a stray text object (a significance mark) above the first label
    out['y_label_centres_px_used'] = lab
    fitA = np.polyfit(yt, yticks, 1) if len(yt) == len(yticks) else None
    fitB = np.polyfit(lab, yticks, 1) if len(lab) == len(yticks) else None
    if small and fitA is not None:
        fitB = np.polyfit([yt[0], yt[-1]], [yticks[0], yticks[-1]], 1)   # end-point check only
    assert fitA is not None or fitB is not None, out
    if fitA is None and fitB is not None and len(sys.argv) > 7:
        # no tick marks (2021 charts): A = all label centres; B = baseline row for the lowest value + top label for the highest
        fitA = fitB
        fitB = np.polyfit([xrow, lab[0]], [yticks[-1], yticks[0]], 1)
        out['calibration_note'] = 'A = label centres; B = x-axis row (lowest tick value) and top label (highest)'
    fitA = fitA if fitA is not None else fitB
    fitB = fitB if fitB is not None else fitA
    vA = lambda r: round(float(fitA[0] * r + fitA[1]), 2)
    vB = lambda r: round(float(fitB[0] * r + fitB[1]), 2)
    bars = []
    for cname, f in COL.items():
        m = f(a)
        m[:, :ycol + 5] = False
        m[xrow - 1:, :] = False
        colfill = m.sum(axis=0) >= minh
        for s, e in runs(colfill):
            if e - s + 1 < 15:
                continue
            c0, c1 = s + (e - s) // 4, e - (e - s) // 4
            tops = [int(np.nonzero(m[:, c])[0].min()) for c in range(c0, c1 + 1) if m[:, c].any()]
            top = float(np.median(tops))
            # error cap: black run above the bar top inside the bar's x range
            caps = []
            for r in range(max(5, int(top) - 90), int(top) - 1):
                for rs, re in runs(blk[r, s:e + 1]):
                    if re - rs + 1 >= 10:
                        caps.append(r)
            cap = float(min(caps)) if caps else None
            bars.append({'colour': cname, 'x_centre_px': (s + e) / 2.0, 'width_px': e - s + 1, 'top_row': top,
                         'value_A': vA(top), 'value_B': vB(top),
                         'cap_value_A': vA(cap) if cap is not None else None,
                         'cap_minus_top_A': round(vA(cap) - vA(top), 2) if cap is not None else None})
    bars.sort(key=lambda b: b['x_centre_px'])
    out['bars_left_to_right'] = bars
    print(json.dumps(out, indent=1, default=lambda o: o.item() if hasattr(o, 'item') else str(o)))


if __name__ == '__main__':
    main()
