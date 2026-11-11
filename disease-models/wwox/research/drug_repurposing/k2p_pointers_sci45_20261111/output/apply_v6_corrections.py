"""Apply the V6 minor corrections (verify/audit.md) as annotations to the producer tables. Idempotent."""
import csv, pathlib
HERE = pathlib.Path(__file__).resolve().parent
ANN = [
 ("decisive.tsv","prop_id","D10","statement","V6: 'acting on unstimulated basal flux' is the producer's reading of the SI protocol (INFERENZA), not a statement of the paper; the abstract says >91-fold selectivity while the Results say >150-fold."),
 ("decisive.tsv","prop_id","D01","locator","V6: the chemical name of 14c is on SI p. S24; S28 is the 13c NMR page and S29 the 14c NMR drawing (4-F-phenyl)."),
 ("decisive.tsv","prop_id","D02","statement","V6 verified: 15 nM (abstract and Results, human manual patch clamp), 67 nM (mouse), 0.26 uM (Tl+ flux, Table 3, Fig 4), 0.15 uM (QPatch, SI Table S2 p. S4). 10 uM/0.15 uM = 66.7 matches '>67-fold'; 10/0.26 = 38. Not decidable from the SI: which is the true human patch-clamp value, the protocol, pH, temperature, species; whether 15 nM is a unit or decimal slip (INFERENZA). A reader may carry the Tl+ 0.26 uM (CHO human TREK-1, room temperature, HBSS + 20 mM HEPES, pH not stated; DATO) and QPatch 0.15 uM (method absent) and should quote 0.15-0.26 uM."),
 ("decisive.tsv","prop_id","D09","statement","V6: the supplement IC50 0.2 +/- 0.1 uM (Hill 1.1, +40 mV) is not compatible with the main text at face value: at 245 nM the main text shows 26 percent block (about 56 expected) and at 10 uM 81 percent (about 98 expected); the two main-text points imply an IC50 near 1.2 uM (INFERENZA); the paper explains neither (+20 vs +40 mV, cumulative application and incomplete equilibration are possible)."),
 ("pointers.tsv","tool_id","T3","assay","V6: 'compound added then Tl+ for 20 min' is an interpretation; the Methods say 'thallium' and never name the compound step; room temperature is stated for dye loading only."),
 ("pointers.tsv","tool_id","T5","assay","V6: unstimulated basal flux is the producer's reading of the SI protocol (INFERENZA)."),
]
for fn, kc, key, col, text in ANN:
    p = HERE / fn
    rows = list(csv.reader(open(p, newline=""), delimiter="\t")); h = rows[0]
    ki, ci = h.index(kc), h.index(col)
    for r in rows[1:]:
        if r[ki] == key:
            if text in r[ci]: break
            r[ci] = (r[ci] + " [" + text + "]").strip(); break
    else: raise SystemExit(key)
    csv.writer(open(p, "w", newline=""), delimiter="\t", lineterminator="\n").writerows(rows)
# one extra row: the new slope source found by the verifier
p = HERE / "trek1_ph_slope.tsv"
rows = list(csv.reader(open(p, newline=""), delimiter="\t")); h = rows[0]
row = ["V6-1", "oocytes (mouse TREK-1)", "mouse", "22.5 C", "not carried", "extracellular pH range of the paper", "7.51 +/- 0.06 (pK1/2, n 30)", "Hill coefficient not tabulated (Imin 0.25 tabulated)", "stated (pK, Imin); slope not stated", "PMID 21765396 (Bagriantsen 2011), Supplementary Table S1", "Supplementary Table S1 (verifier V6)", "partial_fulltext_read"]
row = [x.replace("Bagriantsen", "Bagriantsev") for x in row]
if len(row) == len(h) and row[0] not in {r[0] for r in rows}:
    rows.append(row); csv.writer(open(p, "w", newline=""), delimiter="\t", lineterminator="\n").writerows(rows)
elif len(row) != len(h): raise SystemExit(("slope cols", len(row), len(h)))
print("ok")
