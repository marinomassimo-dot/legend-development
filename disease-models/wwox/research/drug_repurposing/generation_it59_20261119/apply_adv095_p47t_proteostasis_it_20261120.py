"""IT59 (2026-11-20), ADV-097 item 3: (1) SCI's P47T proteostasis screen (registered NOT_SUPPORTED_T in the cerebral regions) carried as one dated line on the nearest existing row WO-03 (no row exists for INV-13 and none is made);
(2) SCI's wording correction: for the organoid deposit 'two knockout clusters' means two groups of knockout libraries (cko1 with cko2, cko3 with cko4), bulk RNA-seq, clonal identity not stated: IT's same-day lines on WO-04, WO-07 and WO-21 are corrected in place.
No status change; cards and ranking inputs are not edited. Idempotent."""
import csv
from pathlib import Path

DR = Path(__file__).resolve().parent.parent
REC = " Record: advisor_pilot_20261113/brainstorm_20261116/adv097_consumption_it_20261119/CONSUMPTION_RECORD_ADV097_IT_20261119.md section 12."
WO03 = (" [IT 2026-11-20, ADV-097 consumption, on SCI's P47T proteostasis screen (pre-registered; registered verdict NOT_SUPPORTED_T in the cerebral regions for the heat-shock, HSP70-constitutive, UPR, autophagy-lysosome and proteasome sets; held tables of the P47T hypomorph, 5 against 5 animals, mixed sex, age not stated): "
        "no transcript-level premise for a chaperone or proteostasis route in the missense hypomorph's cerebral tissue; NOT evidence of no load (heat-shock induction can be post-transcriptional, the null bands are wide); the cerebellar rise of the UPR, lysosome and proteasome sets is post hoc and composition-confounded (no Purkinje or granule score; 4 against 3). It does not speak to the Q230P-class allele (another missense, another domain). "
        "IN-SILICO part still able to change the comparison: none left in the held tables; MEASUREMENT only an experiment supplies: whether the Q230P-class protein is made and then cleared (proteasome or lysosome) and whether any returning protein is functional, unchanged. The chaperone and proteostasis units (U01, U03, U05) are not edited: no candidate added, none removed." + REC + "]")
p = DR / "batch_sci_20261105/map/open_questions_map.tsv"
rows = list(csv.reader(open(p, newline="", encoding="utf-8"), delimiter="\t"))
i = rows[0].index("status_evidence"); j = rows[0].index("last_touched")
n = 0
FIX = (("in both organoid clusters (raw -0.39 and -0.34", "in both groups of knockout libraries (cko1 with cko2, cko3 with cko4; raw -0.39 and -0.34"),
       ("higher raw in both organoid clusters (+0.46, +0.52)", "higher raw in both groups of knockout libraries (+0.46, +0.52)"),
       ("Wnt targets higher raw in both knockout clusters, +0.71 and +0.77", "Wnt targets higher raw in both groups of knockout libraries, +0.71 and +0.77"))
for r in rows[1:]:
    if r[0] == "WO-03" and "on SCI's P47T proteostasis screen" not in r[i]:
        r[i] += WO03; r[j] = "2026-11-20"; n += 1
    for a, b in FIX:
        if a in r[i]:
            r[i] = r[i].replace(a, b); n += 1
with open(p, "w", newline="", encoding="utf-8") as f:
    csv.writer(f, delimiter="\t", lineterminator="\n").writerows(rows)
print("ok", n)
