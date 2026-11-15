#!/usr/bin/env python3
"""Fig 7d of PMID 32000863 (Cheng 2020, Acta Neuropathol Commun 8:6), read from the VECTOR geometry of the open article PDF.

The lithium panels (page 12 of the PDF, three stacked time courses: +/+, +/-, -/-) are drawn as vector paths, so every
data marker, error bar and axis tick has an exact coordinate; nothing is measured on pixels. The script
  1. finds the three x-axes (long black horizontal strokes) and, for each panel, its 7 y ticks (stage 0..6) and 13 x ticks
     (0..60 min, step 5), and calibrates both axes by a straight line through the tick coordinates;
  2. collects the filled red (PTZ) and blue (PTZ + LiCl) markers inside the panel, de-duplicated by centre;
  3. attaches to each marker the vertical error-bar stroke of the same colour at the same x (the bars are drawn upward);
  4. writes one row per marker: genotype, arm, minute, mean stage, SEM (stage units).
Marker anchor: a square marker is centred on its data point; a triangle's anchor is checked against the polyline vertices
of the same series (reported as `anchor_offset_check` in the log) and the offset is applied to all triangles.
Run:  python3 -I extract_fig7d_vector.py <article.pdf> <out_dir>      (--help prints this text; offline, read-only)
Output: fig7d_vector_points.tsv, fig7d_vector_log.txt
"""
import os
import sys

RED, BLUE = (1.0, 0.0, 0.0), (0.0, 0.0, 0.75)


def is_col(c, ref):
    return c is not None and len(c) == 3 and all(abs(a - b) < 0.02 for a, b in zip(c, ref))
PAGE_INDEX = 11  # page 12 of 16
GENOTYPES = ["+/+", "+/-", "-/-"]  # panel order top to bottom


def line_fit(xs, ys):
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    b = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
    a = my - b * mx
    resid = max(abs(a + b * x - y) for x, y in zip(xs, ys))
    return a, b, resid


def main():
    if "--help" in sys.argv or "-h" in sys.argv or len(sys.argv) < 3:
        print(__doc__)
        return 0
    import pymupdf
    pdf, out = sys.argv[1], sys.argv[2]
    os.makedirs(out, exist_ok=True)
    page = pymupdf.open(pdf)[PAGE_INDEX]
    dr = page.get_drawings()
    log = []
    right = [d for d in dr if d["rect"].x0 > 330 and d["rect"].y0 > 225 and d["rect"].y1 < 490]
    blk = [d for d in right if d["type"] == "s" and d["color"] == (0.0, 0.0, 0.0) and len(d["items"]) == 1]

    def pts(d):
        it = d["items"][0]
        return [(q.x, q.y) for q in it[1:] if hasattr(q, "x")]

    axes = sorted([d for d in blk if d["rect"].width > 150 and d["rect"].height < 0.1], key=lambda d: d["rect"].y0)
    assert len(axes) == 3, len(axes)
    rows = []
    for g, ax in zip(GENOTYPES, axes):
        y0 = ax["rect"].y0
        xt = sorted(d["rect"].x0 for d in blk if d["rect"].width < 0.1 and abs(d["rect"].y0 - y0) < 0.2 and 1.0 < d["rect"].height < 1.6)
        yt = sorted([d["rect"].y0 for d in blk if d["rect"].height < 0.1 and 0.9 < d["rect"].width < 1.6 and y0 - 75 < d["rect"].y0 <= y0 + 0.2 and 354 < d["rect"].x0 < 356], reverse=True)
        assert len(xt) == 13 and len(yt) == 7, (g, len(xt), len(yt))
        ax_a, ax_b, rx = line_fit(list(range(0, 61, 5)), xt)  # x = a + b*minute
        ay_a, ay_b, ry = line_fit(list(range(7)), yt)  # y = a + b*stage
        log.append(f"{g}: x-axis y={y0:.2f}; 13 x ticks, {ax_b/1:.4f} pt/min, tick-line residual {rx:.3f} pt; 7 y ticks, {-ay_b:.4f} pt/stage, residual {ry:.3f} pt")
        lo, hi = y0 - 75, y0 + 3

        def inside(d):
            r = d["rect"]
            return r.y0 >= lo and r.y1 <= hi and r.x0 >= 354 and r.x1 <= 526

        markers = {"PTZ": {}, "PTZ+LiCl": {}}
        bars = {"PTZ": [], "PTZ+LiCl": []}
        for d in right:
            if not inside(d):
                continue
            col = d["color"] if d["type"] == "s" else d["fill"]
            arm = "PTZ" if is_col(col, RED) else "PTZ+LiCl" if is_col(col, BLUE) else None
            if arm is None:
                continue
            r = d["rect"]
            if d["type"] in ("f", "fs") and 1.9 < r.width < 2.6 and 1.9 < r.height < 2.6:
                cx, cy = (r.x0 + r.x1) / 2, (r.y0 + r.y1) / 2
                markers[arm][(round(cx, 1), round(cy, 1))] = (cx, cy, arm == "PTZ", r.height)
            elif d["type"] == "s" and len(d["items"]) == 1 and r.width < 0.1 and 0.3 < r.height < 60:
                bars[arm].append((r.x0, r.y0, r.y1))
        # triangle anchor: compare with polyline vertices of the same colour
        poly = {a: [] for a in markers}
        for d in right:
            if inside(d) and d["type"] == "s" and len(d["items"]) > 20:
                arm = "PTZ" if is_col(d["color"], RED) else "PTZ+LiCl" if is_col(d["color"], BLUE) else None
                if arm:
                    for it in d["items"]:
                        poly[arm] += [(q.x, q.y) for q in it[1:] if hasattr(q, "x")]
        for arm in markers:
            offs = []
            for (cx, cy, sq, h) in markers[arm].values():
                near = [v for v in poly[arm] if abs(v[0] - cx) < 0.15 and abs(v[1] - cy) < 3]
                if near:
                    offs.append(min(near, key=lambda v: abs(v[1] - cy))[1] - cy)
            offs.sort()
            med = offs[len(offs) // 2] if offs else float("nan")
            log.append(f"{g} {arm}: {len(markers[arm])} markers; anchor_offset_check vs polyline vertices (pt, median over {len(offs)}): {med:.3f}; max |offset| {max(map(abs, offs)) if offs else float('nan'):.3f}")
            kept = [m for m in sorted(markers[arm].values()) if abs(((m[0] - ax_a) / ax_b) * 2 - round(((m[0] - ax_a) / ax_b) * 2)) < 0.08]
            log.append(f"{g} {arm}: {len(markers[arm]) - len(kept)} marker(s) off the half-minute grid dropped (legend swatches); {len(kept)} kept")
            for (cx, cy, sq, h) in kept:
                data_y = cy + (0.0 if sq else med)
                minute = (cx - ax_a) / ax_b
                mean = (data_y - ay_a) / ay_b
                ups = [y0b for (bx, y0b, y1b) in bars[arm] if abs(bx - cx) < 0.2 and abs(y1b - data_y) < 0.3 for _ in [0]]
                top = min([y0b for (bx, y0b, y1b) in bars[arm] if abs(bx - cx) < 0.2 and min(y0b, y1b) <= data_y + 0.3 and max(y0b, y1b) >= data_y - 0.3] + [data_y])
                bot = max([y1b for (bx, y0b, y1b) in bars[arm] if abs(bx - cx) < 0.2 and min(y0b, y1b) <= data_y + 0.3 and max(y0b, y1b) >= data_y - 0.3] + [data_y])
                rows.append((g, arm, round(minute, 2), round(mean, 3), round((data_y - top) / -ay_b, 3), round((bot - data_y) / -ay_b, 3)))
    rows.sort(key=lambda r: (GENOTYPES.index(r[0]), r[1], r[2]))
    with open(os.path.join(out, "fig7d_vector_points.tsv"), "w", encoding="utf-8") as fh:
        fh.write("genotype\tarm\tminute\tmean_stage\tbar_up_stage\tbar_down_stage\n")
        for r in rows:
            fh.write("\t".join(map(str, r)) + "\n")
    with open(os.path.join(out, "fig7d_vector_log.txt"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(log) + "\n")
    print("\n".join(log))
    print(f"{len(rows)} rows written")
    return 0


if __name__ == "__main__":
    sys.exit(main())
