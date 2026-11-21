"""RP-040 bars (SCI window W): measure bar tops of raster bar charts with numpy.

Usage: python3 -I measure_bars_rp040_w.py IMAGE X0 Y0 W H [--dump]
Reads the crop through ImageMagick `convert` (raw RGB), finds the y axis (longest dark vertical run
in the crop), its tick rows (short dark runs just left of the axis), and the bars (columns whose
colour is not white and not near-black over a long run), and prints bar x-extent, top row, and the
tick rows. Mapping tick rows to labels is done by the caller (labels read from the image).
"""
import subprocess, sys
import numpy as np

def load(path, x0, y0, w, h):
    raw = subprocess.run(["convert", path, "-crop", f"{w}x{h}+{x0}+{y0}", "+repage", "-depth", "8", "rgb:-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, dtype=np.uint8).reshape(h, w, 3).astype(int)

def main():
    path, x0, y0, w, h = sys.argv[1], *map(int, sys.argv[2:6])
    a = load(path, x0, y0, w, h)
    lum = a.mean(axis=2)
    dark = lum < 90
    # y axis: column with longest dark vertical run
    best = (0, None)
    for x in range(w):
        col = dark[:, x]
        run = m = 0
        for v in col:
            run = run + 1 if v else 0
            m = max(m, run)
        if m > best[0]:
            best = (m, x)
    ax = best[1]
    ticks = [y for y in range(h) if dark[y, max(0, ax - 4):ax - 0].sum() >= 3 and not dark[y, :max(0, ax - 8)].all()]
    # collapse adjacent rows
    groups = []
    for y in ticks:
        if groups and y - groups[-1][-1] <= 1:
            groups[-1].append(y)
        else:
            groups.append([y])
    print("axis_x_in_crop", ax, "axis_run", best[0])
    print("tick_rows", [round(float(np.mean(g)), 2) for g in groups])
    # bars: columns right of axis with a non-white, non-dark (filled) run
    sat = (lum < 235) & (~dark)
    cols = []
    for x in range(ax + 2, w):
        ys = np.where(sat[:, x])[0]
        cols.append((x, len(ys), int(ys.min()) if len(ys) else -1))
    # print contiguous column bands with many filled pixels
    band = []
    for x, n, top in cols:
        if n >= 15:
            band.append((x, n, top))
        elif band:
            xs = [b[0] for b in band]
            print("bar x", xs[0], xs[-1], "tops(first,quartiles)", [b[2] for b in band][:: max(1, len(band) // 6)])
            band = []
    if band:
        xs = [b[0] for b in band]
        print("bar x", xs[0], xs[-1], "tops", [b[2] for b in band][:: max(1, len(band) // 6)])

main()
