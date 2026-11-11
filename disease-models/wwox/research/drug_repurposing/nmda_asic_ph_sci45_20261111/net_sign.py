"""Net-sign table of PREREGISTRATION.md. Per target: direction and fraction of its own current for a fall of pHo from pH0 by d.
Inputs are parameters passed in the PARAMS table below, to be set from the VERIFIED tables (output/ after verify/audit.md corrections); the K2P rows come from SCI45 P1 (pH50, Imin, pools).
Writes net_sign.tsv. A net sign for the neuron is written only if every contributing target has a source magnitude on a common axis; otherwise 'net sign not defined'."""
import csv, pathlib
HERE = pathlib.Path(__file__).resolve().parent
def frac_open(ph, p50, n, imin): return imin + (1 - imin) / (1 + 10 ** (n * (p50 - ph)))
# name, direction of an acid fall on the neuron, p50, hill, Imin, pool/size note, axis note (set after verification)
PARAMS = [
 ("TREK-1 (K2P)", "depolarising (outward K+ current lost)", 7.51, 1.0, 0.25, "pool 0.53 of resting conductance, adult KO (INFERENZA); slope not tabulated (1 assumed)", "conductance at rest"),
 ("TASK-1 (K2P)", "depolarising (outward K+ current lost)", 7.3, 1.0, 0.0, "TASK-1/3 pool 0.26 of holding current at -60 mV, juvenile layer V (INFERENZA); TASK-1 RNA 1/17 of TASK-3; Imin not available (upper bound)", "holding current"),
 ("TASK-3 (K2P)", "depolarising (outward K+ current lost)", 6.47, 1.0, 0.0, "as above", "holding current"),
 ("NMDAR GluN1-1a/GluN2A (Kostakis 2011)", "inhibitory (inward current lost)", 7.21, 1.45, 0.0, "oocytes 22-24 C, Mg-free, pH 9 reference; zero floor assumed (INFERENZA)", "recombinant current, Mg-free"),
 ("NMDAR GluN1-1b/GluN2A (Kostakis 2011)", "inhibitory (inward current lost)", 6.96, 2.70, 0.0, "exon-5 form; as above", "recombinant current, Mg-free"),
 ("NMDAR GluN2A (Tian 2021, GluN1 K178AzF mutant before UV)", "inhibitory (inward current lost)", 7.00, 1.91, 0.0, "oocytes room temperature, -60 mV, 0.3 mM Ba2+, Mg-free (V7)", "recombinant current, Mg-free"),
 ("NMDAR GluN2B (Tian 2021, same background)", "inhibitory (inward current lost)", 7.60, 1.37, 0.0, "as above (V7)", "recombinant current, Mg-free"),
 ("NMDAR GluN1-4a/GluN2B WT (Regan 2019 Table 4)", "inhibitory (inward current lost)", 7.50, 1.0, 0.0, "oocytes about 23 C, -40 mV, 0.5 mM Ba2+, Mg-free; slope not reported (1 assumed); pH IC50 7.50 +/- 0.02, n 6, rechecked by the Orchestrator in the text", "recombinant current, Mg-free"),
]
rows = []
for name, direction, p50, n, imin, pool, axis in PARAMS:
    for ph0 in (7.4, 7.2):
        for d in (0.1, 0.2, 0.3):
            f = 1 - frac_open(ph0 - d, p50, n, imin) / frac_open(ph0, p50, n, imin)
            rows.append([name, direction, p50, n, imin, ph0, d, round(f, 3), pool, axis])
# ASIC1a: no current for pH 7.4 -> 7.2; steady-state desensitisation only (verified numbers set after V7)
rows.append(["ASIC1a", "inward current only near and below pH 7.0 (about 2-3 percent of maximum; model 0.9 percent); 7.4 to 7.2 opens none and, after 60 s, leaves 84 percent of channels available (about 21 percent at equilibrium per the authors)", "", "", "", 7.4, 0.2, "0 current", "native cortical neurons: no significant current at 7.1", "fraction of channels available, not current"])
with open(HERE / "net_sign.tsv", "w", newline="") as fh:
    w = csv.writer(fh, delimiter="\t", lineterminator="\n")
    w.writerow(["target", "direction_of_acid_fall", "pH50", "hill", "Imin", "pH0", "delta_pH", "fraction_of_own_current_lost", "pool_or_size_note", "axis"]); w.writerows(rows)
axes = {r[9] for r in rows}
print("axes:", sorted(axes))
print("NET SIGN:", "defined" if len(axes) == 1 else "not defined (targets are on different axes: directions only)")
