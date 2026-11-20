"""ADV-120 sitting 2: measure dot-plot and bar panels of Obeid 2026 (raster, 500 ppi).

Per colour group: individual dots (erosion cores; merged dots are counted by core area), the black mean
bar and the two SD caps (black horizontal runs), or, for bar charts, the top of the filled bar.
Two y calibrations: A = protruding tick marks, B = vertical centres of the printed tick labels.
Usage: measure_dots.py <crop.png> <x_axis_row> <y_axis_col> <yticks csv> <dots|bars> [groups csv]
"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from measure_fig3B import load, runs, box_erode, components
from measure_xy_panel import MASKS, merged_label_centres


def main():
    path, xrow, ycol = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    yticks = sorted([float(v) for v in sys.argv[4].split(',')], reverse=True)
    mode = sys.argv[5]
    groups = sys.argv[6].split(',') if len(sys.argv) > 6 else ['WT', 'KO', 'LD', 'HD']
    a = load(path)
    dark = a.sum(axis=2) < 150
    left = dark[:, ycol - 16:ycol - 7].sum(axis=1) >= 8
    yt = [(s + e) / 2.0 for s, e in runs(left) if e - s >= 2 and s < xrow + 8]
    lab = [c for c, hh in merged_label_centres(dark, ycol - 90, ycol - 24, 20, xrow + 25) if hh > 12]
    out = {'y_ticks_px_found': yt, 'y_label_centres_px': lab}
    fitA = np.polyfit(yt, yticks, 1) if len(yt) == len(yticks) else None
    fitB = np.polyfit(lab, yticks, 1) if len(lab) == len(yticks) else None
    assert fitA is not None or fitB is not None, out
    fitA = fitA if fitA is not None else fitB
    fitB = fitB if fitB is not None else fitA
    vA = lambda r: round(float(fitA[0] * r + fitA[1]), 2)
    vB = lambda r: round(float(fitB[0] * r + fitB[1]), 2)
    out['y_px_per_unit_A'] = float(-1 / fitA[0])
    # black horizontal runs between 30 and 260 px (mean bars and SD caps), away from the axes
    bk = []
    for r in range(15, xrow - 4):
        for s, e in runs(dark[r, ycol + 8:]):
            if 30 <= e - s + 1 <= 260:
                bk.append((r, s + ycol + 8, e + ycol + 8))
    # cluster rows
    cl = []
    for r, s, e in bk:
        if cl and r - cl[-1]['r1'] <= 1 and abs((s + e) / 2 - cl[-1]['cx']) < 15:
            cl[-1]['r1'] = r
            cl[-1]['len'] = max(cl[-1]['len'], e - s + 1)
        else:
            cl.append({'r0': r, 'r1': r, 'cx': (s + e) / 2.0, 'len': e - s + 1})
    res = {}
    for g in groups:
        m = MASKS[g](a)
        m[:, :ycol + 6] = False
        m[xrow - 4:, :] = False
        rec = {}
        if mode == 'dots':
            core = box_erode(m, 7)
            comps = components(core)
            single = [len(c) for c in comps]
            unit = float(np.median(single)) if single else 1.0
            pts = []
            for c in comps:
                rr = [p[0] for p in c]; cc = [p[1] for p in c]
                pts.append((float(np.mean(cc)), float(np.mean(rr)), len(c) / unit))
            rec['dots_cores'] = len(pts)
            rec['dots_estimated_n_by_area'] = round(sum(p[2] for p in pts), 1)
            vals = [vA(p[1]) for p in pts]
            rec['dot_values_A'] = sorted(vals)
            rec['dot_mean_A'] = round(float(np.mean(vals)), 2) if vals else None
            rec['dot_sd_A'] = round(float(np.std(vals, ddof=1)), 2) if len(vals) > 1 else None
            cx = float(np.mean([p[0] for p in pts])) if pts else None
            rec['group_x_centroid_px'] = cx
            if cx is not None:
                near = [k for k in cl if abs(k['cx'] - cx) < 70]
                rec['black_runs'] = [{'row': (k['r0'] + k['r1']) / 2.0, 'len_px': k['len'], 'A': vA((k['r0'] + k['r1']) / 2.0),
                                      'B': vB((k['r0'] + k['r1']) / 2.0)} for k in near]
        else:
            filled = [r for r in range(m.shape[0]) if m[r].sum() >= 70]
            if filled:
                top = float(min(filled)); cxs = np.nonzero(m[int(top) + 10])[0]
                rec['bar_top_row'] = top
                rec['bar_value_A'] = vA(top); rec['bar_value_B'] = vB(top)
                cx = float(cxs.mean()) if len(cxs) else None
                rec['bar_x_centre_px'] = cx
                if cx is not None:
                    near = [k for k in cl if abs(k['cx'] - cx) < 80]
                    rec['black_runs'] = [{'row': (k['r0'] + k['r1']) / 2.0, 'len_px': k['len'], 'A': vA((k['r0'] + k['r1']) / 2.0)} for k in near]
        res[g] = rec
    out['groups'] = res
    print(json.dumps(out, indent=1, default=lambda o: o.item() if hasattr(o, 'item') else str(o)))


if __name__ == '__main__':
    main()
