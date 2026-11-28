"""ADV-330 arithmetic: hom vs WT, Suppl. Table 2/3 of PMID 36828035 (mean, SEM, n as printed). Normal-approximation 95% interval (t = 2.07, df about 23) is an approximation, stated as such."""
import math
rows = {  # analyte, unit: (WT mean, WT sem, hom mean, hom sem)
 "Glucose mg/dL": (296, 25.47, 254.33, 22.52),
 "Urea nitrogen (BUN) mg/dL": (19.11, 1.14, 20.86, 1.24),
 "Calcium mg/dL": (11.57, 0.15, 11.26, 0.26),
 "White blood cells 10^3/uL": (5.71, 0.74, 4.08, 0.45),
}
bench = {  # systemic null P18 vs WT (CLAIM 036, PMID 19936220): null, wt
 "Glucose mg/dL": (143.5, 250.6), "Urea nitrogen (BUN) mg/dL": (37.3, 17.7)}
nWT, nHom, t = 9, 16, 2.07
print("analyte | WT mean | hom mean | diff | rel % | 95% CI of diff (approx) | null-sized change at this WT mean")
for k, (a, sa, b, sb) in rows.items():
    d = b - a; se = math.hypot(sa, sb); lo, hi = d - t*se, d + t*se
    nb = ""
    if k in bench:
        n, w = bench[k]; rel = (n - w)/w; nb = f"{rel*100:+.0f}% = {rel*a:+.1f}"
    print(f"{k} | {a} | {b} | {d:+.2f} | {d/a*100:+.1f} | [{lo:+.1f}, {hi:+.1f}] | {nb}")
