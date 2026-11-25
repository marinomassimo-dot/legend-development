"""Clipping check per lane: darkest grey and count of pixels at or below 3 inside the 46 + 48 kDa window of each lane.
Usage: python3 clip_panels1lm.py <folder holding 1L_wwox.pgm and 1M_wwox.pgm>. Companion of measure_panels1lm.py."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from measure_panels1lm import pgm  # noqa: E402

LANES = {"1L": ([137, 243, 343, 435, 529, 627, 717], 99, 18, 8, 38), "1M": ([118, 224, 325, 420, 528, 635, 733], 102, 18, 7, 41)}

for name, (cx, y0, d, h, half) in LANES.items():
    w, ht, px = pgm(f"{sys.argv[1]}/{name}_wwox.pgm")
    out = []
    for c in cx:
        vals = [px[r][x] for r in range(y0 - d - h, y0 + h + 1) for x in range(c - half, min(w, c + half + 1))]
        out.append((min(vals), sum(v <= 3 for v in vals), round(100 * sum(v <= 3 for v in vals) / len(vals), 1)))
    print(name, "(darkest grey, pixels <= 3, percent of window):", out)
