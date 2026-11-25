#!/usr/bin/env python3
"""ADV-284 label check (2026-11-25, after IT's blind verifier B): the three quantities for the two blind-reader rows of DR-D01-001, same inputs.
CD   = critical difference, unadjusted: t(.975,df) * sp * sqrt(1/n1+1/n2)                    (the difference that reaches P .05 in a two-group t test)
CDT  = Tukey HSD critical difference, four arms: q(.05;4,df)/sqrt(2) * sp * sqrt(1/n1+1/n2)   (the difference that reaches P .05 in the paper's Tukey test)
SDD  = detectable difference at 80 percent power, unadjusted: (t(.975,df)+t(.80,df)) * sp * sqrt(1/n1+1/n2)
SDDT = detectable difference at 80 percent power under the Tukey critical value: (q/sqrt(2)+t(.80,df)) * sp * sqrt(1/n1+1/n2)
Quantiles are tabulated values (Student t; studentized range q at alpha .05, k = 4 arms). Run: python3 -I -P -E sdd_label_check_adv284.py"""
import math
# row: (n1, n2, df, sp, t.975, t.80, q(.05;4,df))   sp = pooled SD read from pixels by the blind reader (ADV-284 blind report section 3)
ROWS = {"pooled WT v A51, plotted points 17 v 15": (17, 15, 30, 17.2, 2.042, 0.854, 3.845),
        "WT NT v A51, legend organoids 4 v 7":     (4, 7, 9, 16.1, 2.262, 0.883, 4.415)}
print("row | CD (t only) | CDT (Tukey) | SDD (t + power) | SDDT (Tukey + power)")
for k, (n1, n2, df, sp, t1, t2, q) in ROWS.items():
    se = sp * math.sqrt(1 / n1 + 1 / n2)
    print(f"{k} | {t1*se:.1f} | {q/math.sqrt(2)*se:.1f} | {(t1+t2)*se:.1f} | {(q/math.sqrt(2)+t2)*se:.1f}")
