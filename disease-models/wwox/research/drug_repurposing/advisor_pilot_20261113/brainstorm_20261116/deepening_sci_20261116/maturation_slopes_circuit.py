#!/usr/bin/env python3
"""I13: could the fall of tonic-inhibition and circuit transcripts in the Wwox-null mouse be a maturation lag?  A pointer, not a test.
Uses the held GSE150123 time course (human cortical spheroids, 62 samples, 6 iPSC lines, 25 to 650 days; ELAPSED culture time, not measured maturation; human, not
mouse P13 to P17) and the line-aware slope code of gse156243/maturation_calibration.py. Reports, per human gene, the mean of per-line slopes of log2 CPM against
log10 day and the between-line 95% t interval (five or six lines: wide). A gene that rises steeply with time is one whose fall in a delayed-maturation tissue is expected.
    python3 maturation_slopes_circuit.py --help
    python3 maturation_slopes_circuit.py run <out_tsv>"""
import sys
if len(sys.argv) != 3 or sys.argv[1] != "run":
    print(__doc__); raise SystemExit(0)
import importlib.util, math, statistics
from pathlib import Path
src = Path(__file__).resolve().parents[3] / "gse156243" / "maturation_calibration.py"
spec = importlib.util.spec_from_file_location("mc", src); mc = importlib.util.module_from_spec(spec); spec.loader.exec_module(mc)
mc.verify_inputs()
GENES = ["GABRD", "GABRA5", "GABRA1", "GABRG2", "GRIN2B", "GRIN2A", "GRIN1", "SLC12A5", "SLC12A2", "NPY", "NPY2R", "SST", "PVALB", "SLC6A1", "SNAP25", "SYT1", "GAD1"]
s2e = mc.symbol_to_ensg(); wanted = {g: s2e[g] for g in GENES if g in s2e}
meta, data = mc.calibration_matrix(wanted)
titles = sorted(data); days = [float(meta[t]["differentiation day"]) for t in titles]; lines = [meta[t]["iPSc line"] for t in titles]; logd = [math.log10(d) for d in days]
rows = []
for g in wanted:
    y = [math.log2(data[t]["genes"].get(g, 0.0) / data[t]["total"] * 1e6 + 1) for t in titles]
    sl = mc._line_slopes(lines, logd, y); k = len(sl)
    m = statistics.fmean(sl.values()); sd = statistics.stdev(sl.values()); half = mc._T975.get(k - 1, 1.96) * sd / math.sqrt(k)
    mean_cpm = statistics.fmean(2 ** v - 1 for v in y)
    rows.append((g, round(m, 2), round(m - half, 2), round(m + half, 2), k, round(mean_cpm, 2)))
with open(sys.argv[2], "w") as f:
    f.write("gene_human\tmean_line_slope_log2CPM_per_log10day\tci95_low\tci95_high\tlines\tmean_CPM_all_samples\n")
    for r in rows: f.write("\t".join(str(x) for x in r) + "\n")
print(open(sys.argv[2]).read())
