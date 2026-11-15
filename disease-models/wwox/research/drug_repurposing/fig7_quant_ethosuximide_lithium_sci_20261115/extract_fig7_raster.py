#!/usr/bin/env python3
"""Fig 7b (ethosuximide) and Fig 7d (lithium) of PMID 32000863 measured on RASTER images, calibrated on the axis ticks.

The ethosuximide panels (7b) exist only as a raster in this paper: in the article PDF they are inside one embedded
1785 x 1424 px JPEG-derived image (300 ppi), and the publisher's figure file is a 1946 x 1627 px PNG. The lithium panels (7d)
are vector in the PDF (see extract_fig7d_vector.py), so the same raster procedure can be run on the PNG's 7d panels and
compared with the exact vector values: that comparison is the validation of this procedure.

Procedure (no pixel is judged by eye):
  1. image: `pdf:<article.pdf>` (the page-12 embedded image) or a PNG path;
  2. per panel (rows given by --panels): the y-axis tick marks (short dark horizontal marks left of the y axis) are
     detected; stage 0 is the lowest tick, px per stage is the median tick spacing; the x calibration is a straight line
     through the centres of the x-axis tick labels (5..60 for 7b, 0..60 for 7d);
  3. each series is a colour (red = PTZ, blue = control or LiCl, green = PTZ + ETS); a pixel is a series pixel by colour
     distance. For each sample minute the marker's vertical extent is read in the narrow column strip at the marker centre;
     the marker BODY is the run of rows with at least `body_min_px` series pixels inside the marker width, the error bar
     is the thin run above it. The data point is the body's bottom edge minus the swatch-measured half height
     (legend swatch: the marker centred on its legend line);
  4. means are reported raw and snapped to the lattice k/N of integer Racine stages (N = animals stated in the legend);
     the distance of the raw values to the lattice is reported as a check, not hidden by the snap.
Occluded markers (a later-drawn colour on top) give no body run and are written as empty, never interpolated.
Run:  python3 -I extract_fig7_raster.py <image> <panel_set> <out_tsv>      (--help prints this text; offline)
  <image>      pdf:<path-to-article.pdf>   or   <path-to-png>
  <panel_set>  one of: pdf_b, png_b, png_d   (panel row ranges and the series, set in PANEL_SETS below)
"""
import os
import sys

import numpy as np

# panel_set -> axis x (px, centre of the y-axis line), [(genotype, y_lo, y_hi)] row ranges holding that panel's y ticks,
# series colours with N per genotype, sample step in minutes, labelled x ticks
PANEL_SETS = {
    "pdf_b": dict(x_max=830, legend_dx=(125, 200), legend_dy_stage=1.8, axis_x=158.5, step=1.0, xlabels=list(range(5, 61, 5)),
                  panels=[("+/+", 340, 640), ("+/-", 710, 1010), ("-/-", 1090, 1395)],
                  series={"+/+": [("control", "blue", 4), ("PTZ", "red", 20), ("PTZ+ETS", "green", 16)],
                          "+/-": [("control", "blue", 5), ("PTZ", "red", 18), ("PTZ+ETS", "green", 12)],
                          "-/-": [("control", "blue", 4), ("PTZ", "red", 6), ("PTZ+ETS", "green", 6)]}),
    "png_b": dict(x_max=880, legend_dx=(125, 330), legend_dy_stage=1.8, axis_x=210.5, step=1.0, xlabels=list(range(5, 61, 5)),
                  panels=[("+/+", 495, 800), ("+/-", 870, 1175), ("-/-", 1245, 1550)],
                  series={"+/+": [("control", "blue", 4), ("PTZ", "red", 20), ("PTZ+ETS", "green", 16)],
                          "+/-": [("control", "blue", 5), ("PTZ", "red", 18), ("PTZ+ETS", "green", 12)],
                          "-/-": [("control", "blue", 4), ("PTZ", "red", 6), ("PTZ+ETS", "green", 6)]}),
    "png_d": dict(x_max=1935, legend_dx=(400, 540), legend_dy_stage=1.9, axis_x=1216.5, step=0.5, xlabels=list(range(0, 61, 5)),
                  panels=[("+/+", 585, 870), ("+/-", 925, 1215), ("-/-", 1275, 1560)],
                  series={"+/+": [("PTZ", "red", 12), ("PTZ+LiCl", "blue", 8)],
                          "+/-": [("PTZ", "red", 12), ("PTZ+LiCl", "blue", 12)],
                          "-/-": [("PTZ", "red", 6), ("PTZ+LiCl", "blue", 7)]}),
}


def colour_masks(a):
    r, g, b = a[:, :, 0], a[:, :, 1], a[:, :, 2]
    return {
        "red": (r > 170) & (g < 100) & (b < 100),
        "green": (g > 110) & (r < 100) & (b < 100),
        "blue": (b > 100) & (r < 90) & (g < 90) & (b > g + 50),
    }


def groups(idx, gap=1):
    if len(idx) == 0:
        return []
    out, cur = [], [idx[0]]
    for v in idx[1:]:
        if v - cur[-1] <= gap:
            cur.append(v)
        else:
            out.append(cur)
            cur = [v]
    out.append(cur)
    return [(c[0], c[-1]) for c in out]


def y_calibration(dark, axis_x, y_lo, y_hi):
    x0, x1 = int(axis_x) - 10, int(axis_x) - 1
    t = dark[:, x0:x1].sum(axis=1)
    rows = [r for r in range(y_lo, y_hi) if t[r] >= 3]
    gp = [(a + b) / 2 for a, b in groups(rows)]
    if len(gp) < 5:
        raise RuntimeError(f"too few y ticks ({len(gp)}) in rows {y_lo}-{y_hi}")
    d = np.diff(gp)
    s = float(np.median(d))
    keep = [gp[0]]
    for v in gp[1:]:
        if abs((v - keep[-1]) / s - round((v - keep[-1]) / s)) < 0.15:
            keep.append(v)
    idx = [round((v - keep[0]) / s) for v in keep]
    # least squares row = r0 + k * s, k counted downward from the top tick
    k = np.array(idx, float)
    A = np.vstack([np.ones_like(k), k]).T
    r0, s = np.linalg.lstsq(A, np.array(keep), rcond=None)[0]
    n_ticks = int(round(max(idx))) + 1
    y_zero = r0 + max(idx) * s  # lowest tick = stage 0
    return float(y_zero), float(s), n_ticks, len(gp)


def x_calibration(a, y_zero, axis_x, labels, x_max):
    """x = c0 + c1 * minute from the centres of the tick-label glyph groups under the axis (grey threshold 150)."""
    dark = a.max(axis=2) < 150
    r0, r1 = int(round(y_zero)) + 6, int(round(y_zero)) + 17
    cols = np.where(dark[r0:r1, int(axis_x) + 2: int(x_max)].sum(axis=0) >= 1)[0] + int(axis_x) + 2
    centres = [(lo + hi) / 2 for lo, hi in groups(list(cols), gap=4)]
    m_all = list(labels)
    if len(centres) < len(m_all):
        raise RuntimeError(f"x labels found {len(centres)}, expected {len(m_all)}")
    # drop stray groups: keep the subset (in order) that is best explained by a straight line through the labels
    import itertools
    m = np.array(m_all, float)
    A = np.vstack([np.ones_like(m), m]).T
    best = None
    for sub in itertools.combinations(centres, len(m_all)):
        sol = np.linalg.lstsq(A, np.array(sub), rcond=None)[0]
        res = float(np.max(np.abs(A @ sol - np.array(sub))))
        if best is None or res < best[0]:
            best = (res, sub)
    pts = list(best[1])
    m = np.array(m_all, float)
    A = np.vstack([np.ones_like(m), m]).T
    (c0, c1) = np.linalg.lstsq(A, np.array(pts), rcond=None)[0]
    resid = float(np.max(np.abs(A @ np.array([c0, c1]) - np.array(pts))))
    return float(c0), float(c1), resid


def swatch_geometry(masks, colour, x_lo, x_hi, y_lo, y_hi):
    """Half height from the marker's body centre... measured as (bottom edge of the body) - (centre row of the legend line)."""
    m = masks[colour][y_lo:y_hi, x_lo:x_hi]
    cnt = m.sum(axis=1)
    rows = np.where(cnt >= max(8, int(0.5 * cnt.max())))[0]
    if len(rows) == 0:
        return None
    line_rows = groups(list(rows))
    best = max(line_rows, key=lambda g: m[g[0]: g[1] + 1].sum())
    line_centre = (best[0] + best[1]) / 2 + y_lo
    # marker body = rows where the colour fills the middle of the window wider than the line stroke
    mid = int(np.argmax(m.sum(axis=0)))  # the marker's own column: the legend line is horizontal and thin
    wid = m[:, max(0, mid - 6): mid + 7].sum(axis=1)
    body = np.where(wid >= 5)[0]
    bg = groups(list(body))
    cand = [g for g in bg if g[0] <= (best[0] + best[1]) / 2 <= g[1]]
    if not cand:
        return None
    g = cand[0]
    return dict(line_centre=line_centre, bottom=g[1] + y_lo + 0.5, top=g[0] + y_lo - 0.5, height=g[1] - g[0] + 1)


def extract(a, cfg):
    a = a.astype(int)
    dark = a.max(axis=2) < 115
    masks = colour_masks(a)
    out, log = [], []
    for geno, y_lo, y_hi in cfg["panels"]:
        y_zero, spp, nt, found = y_calibration(dark, cfg["axis_x"], y_lo, y_hi)
        c0, c1, xres = x_calibration(a, y_zero, cfg["axis_x"], cfg["xlabels"], cfg["x_max"])
        log.append(f"{geno}: y_zero {y_zero:.1f}px, {spp:.2f} px/stage ({found} tick groups, {nt} ticks); x = {c0:.1f} + {c1:.3f}*min, label residual {xres:.2f}px")
        # legend swatches: region right of the axis, top of the panel
        top = y_zero - 6 * spp
        for name, colour, n in cfg["series"][geno]:
            sw = swatch_geometry(masks, colour, int(cfg["axis_x"] + cfg["legend_dx"][0]), int(cfg["axis_x"] + cfg["legend_dx"][1]), int(top - 14), int(top + cfg["legend_dy_stage"] * spp))
            if sw is None:
                raise RuntimeError(f"no legend swatch for {colour} in {geno}")
            half = sw["bottom"] - sw["line_centre"]
            log.append(f"  swatch {name}/{colour}: body height {sw['height']} px, bottom - line centre {half:.2f} px")
            # sample columns
            k = 0
            nmin = int(round(60 / cfg["step"])) + 1
            for i in range(nmin):
                minute = i * cfg["step"]
                xc = c0 + c1 * minute
                xs = [int(round(xc)) - 1, int(round(xc)) + 1]
                wh = max(1, int(round(0.42 * c1 * cfg["step"])))  # window half width: stays inside this marker's own columns
                minw = max(3, int(round(1.25 * wh)))
                win = masks[colour][:, int(round(xc)) - wh: int(round(xc)) + wh + 1]
                strip = masks[colour][:, xs[0]: xs[1] + 1]
                width_row = win.sum(axis=1)
                rows = np.where(width_row >= minw)[0]
                rows = rows[(rows > y_zero - 6.3 * spp) & (rows < y_zero + 0.6 * spp)]
                bg = groups(list(rows), gap=1)
                if not bg:
                    out.append((geno, name, minute, None, None, "no_body"))
                    continue
                body = max(bg, key=lambda g: g[1])  # lowest body-like run; the bar and cap lie above it
                if body[1] - body[0] + 1 < 4:
                    out.append((geno, name, minute, None, None, "short_run"))
                    continue
                bottom = body[1] + 0.5
                centre = bottom - half
                mean = (y_zero - centre) / spp
                # error bar: contiguous strip pixels above the body top
                col = strip.any(axis=1)
                y = body[0] - 1
                gap = 0
                while y > 0 and (col[y] or gap < 2) and y > y_zero - 6.5 * spp:
                    gap = 0 if col[y] else gap + 1
                    y -= 1
                bar_top = y + gap + 1
                sem = max(0.0, (centre - (bar_top - 0.5)) / spp) if bar_top < body[0] - 1 else 0.0
                flag = "ok" if (body[1] - body[0] + 1) <= sw["height"] + 3 else "tall_run"
                out.append((geno, name, minute, mean, sem, flag))
    return out, log


def load(src):
    import pymupdf
    if src.startswith("pdf:"):
        doc = pymupdf.open(src[4:])
        page = doc[11]
        xref = page.get_images(full=True)[0][0]
        pix = pymupdf.Pixmap(doc, xref)
    else:
        pix = pymupdf.Pixmap(src)
    return np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, pix.n)[:, :, :3]


def main():
    if "--help" in sys.argv or "-h" in sys.argv or len(sys.argv) < 4:
        print(__doc__)
        return 0
    src, pset, out_tsv = sys.argv[1], sys.argv[2], sys.argv[3]
    cfg = PANEL_SETS[pset]
    a = load(src)
    rows, log = extract(a, cfg)
    ns = {(g, n): N for g in cfg["series"] for (n, c, N) in cfg["series"][g]}
    with open(out_tsv, "w", encoding="utf-8") as fh:
        fh.write("genotype\tarm\tminute\tmean_stage_raw\tmean_stage_lattice\tlattice_distance_steps\tsem_up_stage\tflag\n")
        for g, arm, m, mean, sem, flag in rows:
            if mean is None:
                fh.write(f"{g}\t{arm}\t{m}\t\t\t\t\t{flag}\n")
                continue
            N = ns[(g, arm)]
            snapped = round(mean * N) / N
            dist = abs(mean * N - round(mean * N))
            fh.write(f"{g}\t{arm}\t{m}\t{mean:.3f}\t{snapped:.3f}\t{dist:.2f}\t{sem:.3f}\t{flag}\n")
    ok = sum(1 for r in rows if r[3] is not None)
    log.append(f"{ok} of {len(rows)} sample points measured; {len(rows) - ok} without a visible body (occluded or absent)")
    print("\n".join(log))
    return 0


if __name__ == "__main__":
    sys.exit(main())
