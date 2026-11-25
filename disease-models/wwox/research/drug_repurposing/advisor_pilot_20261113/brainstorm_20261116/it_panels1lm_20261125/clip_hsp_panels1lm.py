"""HSP90 clipping check per lane: share of pixels at grey <= 5 in the band window (peak row +- 8) of each lane.
Usage: python3 clip_hsp_panels1lm.py <folder holding 1L_hsp.pgm and 1M_hsp.pgm>. Companion of measure_panels1lm.py."""
import statistics as S
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from measure_panels1lm import pgm, rowmean  # noqa: E402

for name, centres in (("1L", None), ("1M", None)):
    w, h, px = pgm(f"{sys.argv[1]}/{name}_hsp.pgm")
    rows = range(8, h - 6)
    col = [S.mean(sorted((255 - px[r][x] for r in rows), reverse=True)[:8]) for x in range(w)]
    runs, start = [], None
    for x, v in enumerate(col + [0]):
        if v >= 0.4 * max(col) and start is None:
            start = x
        elif v < 0.4 * max(col) and start is not None:
            if x - start > w / 30:
                runs.append((start, x - 1))
            start = None
    out = []
    for a, b in runs:
        pk = max(range(18, h - 16), key=lambda r: sum(255 - px[r][x] for x in range(a, b + 1)))
        vals = [px[r][x] for r in range(pk - 8, pk + 9) for x in range(a, b + 1)]
        out.append((a, min(vals), round(100 * sum(v <= 5 for v in vals) / len(vals), 1)))
    print(name, "per run (start column, darkest grey, percent of pixels <= 5):", out)
