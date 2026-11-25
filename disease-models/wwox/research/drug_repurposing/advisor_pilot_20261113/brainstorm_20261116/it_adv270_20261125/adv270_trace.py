"""Pixel trace of Fig 2b (PMID 25012504) from the publisher JPEG; ratios only.
usage: python3 adv270_trace.py <fig2.jpg>   (needs ImageMagick `convert` and numpy)"""
import subprocess, sys, numpy as np
src = sys.argv[1]
raw = subprocess.run(['convert', src, '-crop', '257x140+318+28', '+repage', 'ppm:-'], capture_output=True).stdout
# parse P6
parts = raw.split(b'\n', 3); w, h = map(int, parts[1].split()); a = np.frombuffer(parts[3], np.uint8).reshape(h, w, 3).astype(int)
R, G, B = a[..., 0], a[..., 1], a[..., 2]
red = (R > 150) & (G < 110) & (B < 110)
blue = (B > 120) & (R < 110) & (G < 110)
# y axis: tick labels are blurred; calibrate 0 and 500 from the axis ends (rows of axis labels)
# rows (crop coords): label '500' near y=8, '0' near y=128  -> 120 px per 500 units
def val(y): return (128 - y) / 120 * 500
# phases by x in crop coords (crop is 257 wide; 4x enlarged image x/4)
ph = {'basal': (22, 86), 'oligo': (95, 130), 'fccp': (140, 188), 'rot': (200, 226)}
def trace(mask, lo, hi):
    ys = []
    for x in range(lo, hi):
        col = np.where(mask[:, x])[0]
        col = col[col > 26]   # rows above 26 hold the legend text
        if len(col) and col.max() - col.min() <= 12:   # skip columns holding a vertical line or a transition
            ys.append(np.median(col))
    return np.array(ys)
for name, m in (('WT', blue), ('KO', red)):
    for p, (lo, hi) in ph.items():
        y = trace(m, lo, hi)
        if p == 'fccp':
            print(name, p, 'first-third mean', round(val(y[:len(y)//3].mean()), 0), 'last-third mean', round(val(y[-len(y)//3:].mean()), 0), 'n_cols', len(y))
        else:
            print(name, p, 'mean', round(val(y.mean()), 0), 'n_cols', len(y))
