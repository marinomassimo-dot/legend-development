"""ADV-121: error-bar extent beyond each marker of Fig 3C (Obeid 2026, body weight), raster 500 ppi.

For each series and age: find the marker (erosion core of its colour mask, as in ADV-120 measure_xy_panel.py),
take the central three columns of the unerased colour mask, follow the contiguous vertical run through the marker
centre, and read its top and bottom ends. The legend says error bars are mean +/- SD, so the half-length is one SD.
A bar that does not protrude beyond the marker (end within `slack` px of the marker half-height) is recorded as
"hidden": its half-length is at most the marker half-height (a ceiling, not a value).
Lengths depend on the y scale only (not on the offset), so calibrations A and B give the same length when their
scales agree; both scales are printed.
Usage: measure_bars_3C.py <crop.png> <x_axis_row> <y_axis_col> <xticks csv> <yticks csv> <ages csv>
(the ADV-120 folder holds the helpers; this script inserts its path before importing).
"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
ADV120 = os.path.join(os.path.dirname(HERE), 'benchmark_card_adv120_sci_20261120')
sys.path.insert(0, ADV120)
import numpy as np
from measure_fig3B import load, runs, box_erode, components
from measure_xy_panel import MASKS


def main():
    path, xrow, ycol = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    xticks = [float(v) for v in sys.argv[4].split(',')]
    yticks = [float(v) for v in sys.argv[5].split(',')]
    ages = [float(v) for v in sys.argv[6].split(',')]
    slack = 3
    a = load(path)
    dark = a.sum(axis=2) < 150
    below = dark[xrow + 6:xrow + 14, :].sum(axis=0) >= 6
    xs = sorted((s + e) / 2.0 for s, e in runs(below))
    lin = lambda v: xs[0] + (xs[-1] - xs[0]) * (v - xticks[0]) / (xticks[-1] - xticks[0])
    snapped = [min(xs, key=lambda t: abs(t - lin(v))) for v in xticks]
    fx = np.polyfit(xticks, snapped, 1)
    left = dark[:, ycol - 16:ycol - 7].sum(axis=1) >= 8
    yt = [(s + e) / 2.0 for s, e in runs(left) if e - s >= 2 and s < xrow + 8]
    assert len(yt) == len(yticks), 'y ticks not found'
    fitA = np.polyfit(yt, sorted(yticks, reverse=True), 1)
    ppu = float(-1 / fitA[0])
    out = {'y_px_per_unit_A': ppu, 'y_ticks_px': yt, 'slack_px': slack, 'series': {}}
    for name in ['WT', 'KO', 'LD', 'HD']:
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
                rows.append({'age': ag, 'status': 'no marker core (hidden or absent)'})
                continue
            cx, cy, mw, mh = min(cand, key=lambda t: abs(t[0] - cpx))
            c0 = int(round(cx))
            # marker edges from the core (core = marker eroded by 9 px: edge = core end +/- 5)
            rr_core = None
            half_marker = 8.5
            top_edge = cy - mh / 2.0
            bot_edge = cy + mh / 2.0
            occluded = mh < 15
            # caps: rows with a horizontal run of >= 11 colour pixels inside cx +/- 9 columns, outside the marker
            win = m[:, c0 - 9:c0 + 10].sum(axis=1)
            cap = np.nonzero(win >= 11)[0]
            def end_of(direction):
                if direction < 0:
                    edge = top_edge if not occluded else top_edge
                    rows_ = [r for r in cap if r < edge - 1.5 and r > edge - 60]
                else:
                    edge = bot_edge
                    rows_ = [r for r in cap if r > edge + 1.5 and r < edge + 60]
                if not rows_:
                    return None
                # first contiguous group nearest the marker
                rows_ = sorted(rows_, key=lambda r: abs(r - edge))
                g = [rows_[0]]
                for r in rows_[1:]:
                    if abs(r - g[-1]) <= 1: g.append(r)
                    else: break
                return float(sum(g)) / len(g)
            up_row = end_of(-1); dn_row = end_of(+1)
            if occluded:
                # a partly occluded marker: take the centre from the edge on the side where the bar was found
                if up_row is not None and dn_row is None:
                    cy = top_edge + half_marker
                elif dn_row is not None and up_row is None:
                    cy = bot_edge - half_marker
            up = None if up_row is None else cy - up_row
            dn = None if dn_row is None else dn_row - cy
            row = {'age': ag, 'marker_centre_px': (cx, cy), 'marker_h_px': mh, 'marker_occluded': occluded,
                   'cap_row_up_px': up_row, 'cap_row_down_px': dn_row, 'upper_arm_px': up, 'lower_arm_px': dn}
            arms = [v for v in (up, dn) if v is not None]
            if arms and max(arms) > half_marker + 1:
                row['status'] = 'bar protrudes'
                row['sd_units_A'] = round(max(arms) / ppu, 3)
                row['sd_units_upper_only'] = None if up is None else round(up / ppu, 3)
                row['sd_units_lower_only'] = None if dn is None else round(dn / ppu, 3)
            else:
                row['status'] = 'hidden within marker'
                row['sd_ceiling_units_A'] = round(half_marker / ppu, 3)
            rows.append(row)
        out['series'][name] = rows
    print(json.dumps(out, indent=1, default=lambda o: o.item() if hasattr(o, 'item') else str(o)))


if __name__ == '__main__':
    main()
