"""Recalculate the sampled peak and nominal culture-to-plasma ratio from Table S2."""
from pathlib import Path
import re
import subprocess
import sys

pdf = Path(sys.argv[1]) / "deepening_downloads/nr_loop_20261124/human_plasma_s1.pdf"
page = subprocess.check_output(["pdftotext", "-f", "3", "-l", "3", "-layout", str(pdf), "-"], text=True)
rows = []
for line in page.splitlines():
    fields = line.split()
    if len(fields) == 5 and all(re.fullmatch(r"\d+(?:\.\d+)?", v) for v in fields):
        rows.append(tuple(map(float, fields)))
assert len(rows) == 10 and rows[0][0] == 0 and rows[-1][0] == 167.6
peak = max(nam for hour, nam, *_ in rows if 0 < hour < 24)
print("participants\tfirst_day_plasma_NAM_peak_uM\twildtype_bath_NAM_uM\tbath_to_peak")
print(f"1\t{peak:g}\t1000\t{1000/peak:.2f}")
