"""ADV-246 (IT, 2026-11-25): read-off of the Fig 1D box edges (Steinberg 2026, Brain; accepted-manuscript PDF page 32, figure raster 1430 x 1348, no vector drawing).
Axis calibration from the y-axis tick marks (rows of the 1000/800/400/200/0 ticks); per box, rows where a dark horizontal run crosses the box are listed (outline edges, median line).
Usage: python3 measure_fig1d_adv246.py <image.jpeg>. Not author data; resolution stated in the result."""
import subprocess, sys
img = sys.argv[1]
X0, Y0, W, H = 440, 615, 135, 225
raw = subprocess.run(["convert", img, "-crop", f"{W}x{H}+{X0}+{Y0}", "+repage", "txt:-"], capture_output=True, text=True, check=True).stdout.splitlines()[1:]
lum = {}
for l in raw:
    c, rest = l.split(":", 1); x, y = map(int, c.split(","))
    hx = rest.split("#")[1][:6]; r, g, b = (int(hx[i:i+2], 16) for i in (0, 2, 4)); lum[(x + X0, y + Y0)] = (r + g + b) / 3
TICK = {1000: 623, 800: 665, 400: 748, 200: 790, 0: 832}
k = (1000 - 0) / (TICK[0] - TICK[1000])
val = lambda y: (TICK[0] - y) * k
BOX = {"WT": (449, 466), "WWOX-KO": (469, 486), "WPM D": (489, 505), "WPM S": (509, 525), "WSM S": (529, 545), "LM-iPS": (549, 565)}
print("units per pixel %.2f" % k)
# row profile: per box, the median over the box width of each row's luminance (robust to dots); an outline or median line is a row clearly darker than both neighbours in a column-wise vote.
import statistics
for name, (a, b) in BOX.items():
    prof = {y: statistics.median(lum[(x, y)] for x in range(a, b + 1)) for y in range(Y0, Y0 + H)}
    base = statistics.median(prof.values())
    cand = [y for y in range(Y0 + 1, Y0 + H - 1) if prof[y] < prof[y - 1] - 12 and prof[y] <= prof[y + 1] + 2 and prof[y] < 235]
    print(name, [(y, round(val(y)), round(prof[y])) for y in cand])
