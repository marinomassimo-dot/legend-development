"""RP-040 bars (SCI window W): top row of a bar by fill-colour mask.

Usage: python3 -I fill_tops_rp040_w.py IMAGE X0 Y0 W H XA XB [XA XB ...]
Each XA XB is the bar's x-extent inside the crop. The fill colour is sampled 6 rows above the baseline
(the median of the bar's interior at the lowest rows), the mask is colour distance < 45, and the top is the
first masked row, taken in the outer quarters of the bar so the error-bar stem is not read.
"""
import subprocess, sys
import numpy as np

path, x0, y0, w, h = sys.argv[1], *map(int, sys.argv[2:6])
raw = subprocess.run(["convert", path, "-crop", f"{w}x{h}+{x0}+{y0}", "+repage", "-depth", "8", "rgb:-"],
                     capture_output=True, check=True).stdout
a = np.frombuffer(raw, dtype=np.uint8).reshape(h, w, 3).astype(int)
spans = list(map(int, sys.argv[6:]))
for xa, xb in zip(spans[0::2], spans[1::2]):
    q = max(1, (xb - xa) // 4)
    # sample colour: rows from the bottom third of the crop, median over the span, ignoring white and dark
    block = a[h // 2:h - 20, xa + q:xb - q + 1].reshape(-1, 3)
    keep = block[(block.mean(axis=1) > 40) & (block.mean(axis=1) < 235)]
    col = np.median(keep, axis=0)
    dist = np.sqrt(((a - col) ** 2).sum(axis=2))
    mask = dist < 45
    res = []
    for xs in (range(xa, xa + q + 1), range(xb - q, xb + 1)):
        cols = [np.where(mask[:, x])[0] for x in xs]
        cols = [c.min() for c in cols if len(c)]
        res.append(float(np.median(cols)) if cols else None)
    print("bar", xa, xb, "fill_rgb", col.astype(int).tolist(), "top_rows(left,right)", res)
