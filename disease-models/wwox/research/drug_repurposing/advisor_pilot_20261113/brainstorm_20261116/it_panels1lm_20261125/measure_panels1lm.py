"""Read-off densitometry of Brain 2026 Supp Fig 1L and 1M (and 1K, exploratory) from the embedded images of File012.
Usage: python3 -I measure_panels1lm.py <File012.pdf> <empty working folder>. Plain Python; ImageMagick converts to PGM.
Frozen method: PREREG_PANELS1LM_IT_20261125.md plus its amendment. Every number is a read-off from a JPEG, not author data."""
import statistics as S
import subprocess
import sys
from pathlib import Path

import pymupdf

PANELS = {  # name: (page index, HSP90 xref, WWOX xref, lane labels, printed values (None = no printed value))
    "1L": (5, 34, 33, ["JH WT", "WSM S2", "WSM S5", "LM-iPS", "WSM S2 AAV9", "WSM S5 AAV9", "LM-iPS AAV9"], [1, None, None, 0.2, 0.4, 0.4, 0.9]),
    "1M": (6, 37, 38, ["JH WT", "WPM S1", "WPM D1", "WPM D3", "WPM S1 AAV9", "WPM D1 AAV9", "WPM D3 AAV9"], [1, 0.1, 0.1, 0.3, 7, None, None]),
    "1K": (4, 29, 30, ["JH WT", "JH WKO-1C", "JH WKO-2C", "JH WKO-1C AAV9", "JH WKO-2C AAV9"], [1, None, None, 0.8, 1.4]),
}


def pgm(path):
    data = Path(path).read_bytes()
    head = data.split(None, 4)
    w, h = int(head[1]), int(head[2])
    px = data[-w * h:]
    return w, h, [list(px[r * w:(r + 1) * w]) for r in range(h)]


def load(doc, page, xref, work, tag):
    im = doc.extract_image(xref)
    raw = work / f"{tag}.{im['ext']}"
    raw.write_bytes(im["image"])
    out = work / f"{tag}.pgm"
    subprocess.run(["convert", str(raw), "-colorspace", "Gray", "-depth", "8", str(out)], check=True)
    info = [i for i in doc[page].get_image_info(xrefs=True) if i["xref"] == xref][0]
    return pgm(out), info["bbox"]


def lane_centres(img, n, marker):
    """Centres of the n widest dark runs in the HSP90 column profile."""
    w, h, p = img
    col = [S.mean(sorted((255 - p[r][x] for r in range(h)), reverse=True)[:max(6, h // 12)]) for x in range(w)]
    for frac in (0.50, 0.40, 0.60, 0.35, 0.65, 0.30, 0.70, 0.25, 0.20, 0.15):
        thr = frac * max(col)
        runs, start = [], None
        for x, v in enumerate(col + [0]):
            if v >= thr and start is None:
                start = x
            elif v < thr and start is not None:
                runs.append((start, x - 1))
                start = None
        runs = [r for r in runs if r[1] - r[0] >= w / (n * 4)]
        runs = [r for r in runs if r[0] > 2]
        if len(runs) == n + marker:
            return [(a + b) / 2 for a, b in runs[marker:]], frac
    raise SystemExit(f"could not find {n} lanes")


def rowmean(img, c, half, r):
    return S.mean(255 - img[2][r][x] for x in range(max(0, c - half), min(img[0], c + half + 1)))


def window(img, c, half, r0, r1, gap, far, below_only=False):
    """Net darkness summed over rows r0..r1, background = median of rows gap..far beyond the window."""
    h = img[1]
    above = [] if below_only else list(range(r0 - far, r0 - gap + 1))
    bg_rows = [r for r in above + list(range(r1 + gap, r1 + far + 1)) if 0 <= r < h]
    vals = [255 - img[2][r][x] for r in bg_rows for x in range(max(0, c - half), min(img[0], c + half + 1))]
    if not vals:  # a window with no background rows (only possible for blank noise windows at the strip edge)
        return float("nan")
    bg = S.median(vals)
    return sum(rowmean(img, c, half, r) - bg for r in range(max(0, r0), min(h, r1 + 1)))


def main(pdf, work):
    doc = pymupdf.open(pdf)
    work = Path(work)
    for name, (page, xh, xw, labels, printed) in PANELS.items():
        H, bh = load(doc, page, xh, work, name + "_hsp")
        if name != "1K":  # trim the image border rows of the HSP90 strip (top 8, bottom 6): a frame line and a stray band at the edges
            full = H[1]
            H = (H[0], full - 14, H[2][8:full - 6])
            bh = (bh[0], bh[1] + 8 * (bh[3] - bh[1]) / full, bh[2], bh[3] - 6 * (bh[3] - bh[1]) / full)
        X, bx = load(doc, page, xw, work, name + "_wwox")
        n = len(labels)
        if name == "1K":  # exploratory panel: the lane centres of ADV-251, given in WWOX-strip pixels (both 1K strips share the page extent)
            ch, frac = [c * H[0] / X[0] for c in (130, 227, 325, 422, 526)], None
        else:
            ch, frac = lane_centres(H, n, 1 if name == "1L" else 0)
        ppt_h = H[0] / (bh[2] - bh[0])
        ppt_x = X[0] / (bx[2] - bx[0])
        cx = [int(round((bh[0] + c / ppt_h - bx[0]) * ppt_x)) for c in ch]
        pitch_x = S.median(b - a for a, b in zip(cx, cx[1:]))
        pitch_h = S.median(b - a for a, b in zip(ch, ch[1:]))
        half_x, half_h = int(0.4 * pitch_x), int(0.4 * pitch_h)
        ypp = X[1] / (bx[3] - bx[1])
        s = ypp / 1.946
        hw, gap, far = int(round(6 * s)), int(round(20 * s)), int(round(50 * s))
        d_pt = 0.1413 * (51.6 if page in (5, 6) else 59.4)
        D = int(round(d_pt * ypp))
        lo, hi = int(0.30 * X[1]), int(0.80 * X[1])
        y0 = max(range(lo, hi), key=lambda r: rowmean(X, cx[0], half_x, r))
        hs = H[1] / (bh[3] - bh[1]) / 1.946
        hh, hgap, hfar = int(round(8 * hs)), int(round(20 * hs)), int(round(40 * hs))
        peaks = [max(range(hh, H[1] - hh), key=lambda r, c=int(c): rowmean(H, c, half_h, r)) for c in ch]
        hsp = [window(H, int(c), half_h, pk - hh, pk + hh, max(2, hgap // 2), hfar) for c, pk in zip(ch, peaks)]
        shift = [int(round((pk - peaks[0]) / (H[1] / (bh[3] - bh[1])) * ypp)) for pk in peaks]
        print(f"=== {name}: lanes {n} (threshold {frac}); centres on WWOX strip {cx}; y0 {y0} of {X[1]}; D {D}; h {hw}; HSP peaks {peaks}; shifts {shift}")
        wt_min = min(X[2][r][x] for r in range(y0 - hw, y0 + hw + 1) for x in range(cx[0] - half_x, cx[0] + half_x + 1))
        img_min = min(min(row) for row in X[2])
        flat = [r for r in range(y0 - hw, y0 + hw + 1) if min(X[2][r][x] for x in range(cx[0] - half_x, cx[0] + half_x + 1)) <= img_min]
        print(f"    saturation: darkest grey in WT 46 kDa window {wt_min}; image minimum {img_min}; rows reaching the minimum {len(flat)}")
        variants = {}
        for vname, top, shifted, below_only in (("V2", D + hw, False, False), ("V1", hw, False, False), ("V2shift", D + hw, True, False), ("V1shift", hw, True, False),
                                              ("V2bgBelow*", D + hw, False, True), ("V1bgBelow*", hw, False, True), ("V2shiftBgBelow*", D + hw, True, True)):
            nets, noise = [], []
            for i, c in enumerate(cx):
                off = shift[i] if shifted else 0
                r0, r1 = y0 - top + off, y0 + hw + off
                nets.append(window(X, c, half_x, r0, r1, gap, far, below_only))
                width = r1 - r0 + 1
                blanks = []
                for a in range(r1 + 8, X[1] - width, max(4, width // 3)):
                    v = window(X, c, half_x, a, a + width - 1, 4, far, below_only)
                    if v == v:
                        blanks.append(v)
                noise.append(S.pstdev(blanks) if len(blanks) > 2 else float("nan"))
            variants[vname] = (nets, noise)
        for vname, (nets, noise) in variants.items():
            for normed in (True, False):
                base = nets[0] / (hsp[0] if normed else 1)
                row = []
                rs = []
                for i in range(n):
                    ratio = (nets[i] / (hsp[i] if normed else 1)) / base
                    below = not (noise[i] != noise[i]) and nets[i] < 3 * noise[i]
                    cell = f"{labels[i]}={ratio:.3f}{'(below)' if below else ''}"
                    if printed[i] is not None and i:
                        cell += f"[print {printed[i]}, r {ratio / printed[i]:.2f}]"
                        if not below:
                            rs.append(ratio / printed[i])
                    row.append(cell)
                code, gm = "NONE", float("nan")
                if rs:
                    gm = S.geometric_mean([max(v, 1e-6) for v in rs])
                    if all(1 / 1.5 <= v <= 1.5 for v in rs):
                        code = "REPRODUCED"
                    elif all(gm / 1.5 <= v <= gm * 1.5 for v in rs):
                        code = "UP_TO_ONE_FACTOR"
                    else:
                        code = "NOT_REPRODUCED"
                tag = vname + (" HSP90" if normed else " alone")
                print(f"    {tag:22s} {code:17s} gm r {gm:.2f} | " + "; ".join(row))
        print("    WWOX nets and noise (V2):", [(round(a), round(b)) for a, b in zip(*variants["V2"])])
        print("    HSP90 nets:", [round(v) for v in hsp])


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
