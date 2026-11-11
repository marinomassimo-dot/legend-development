"""Apply the V7 corrections (verify/audit.md) as annotations to the producer tables; add the primary GluN2B/GluN2A rows the verifier reached. Idempotent."""
import csv, pathlib
HERE = pathlib.Path(__file__).resolve().parent
ANN = [
 ("proton_sensitivity.tsv","row_id","PS03","note","V7: the H+ references are Traynelis 1995 (2A) and Traynelis 1995 plus Yi 2018 (2B); Traynelis 1998 sits on the Zn2+ column of Hansen 2021 Table 5."),
 ("proton_sensitivity.tsv","row_id","PS07","note","V7: same column mapping correction as PS03. GluN2B at pH 7.3-7.5 is CONFIRMED by two primaries the producer did not open: Regan 2019 Table 4 (GluN1-4a/GluN2B WT pH IC50 7.50 +/- 0.02, n 6; 100 uM Glu, 30 uM Gly; rechecked by the Orchestrator in the text) and Tian 2021 (2B 7.60 vs 2A 7.00, same lab, GluN1 K178AzF mutant before UV)."),
 ("proton_sensitivity.tsv","row_id","PS04","note","V7: 7.21 - 6.80 = 0.41, not 0.5."),
 ("proton_sensitivity.tsv","row_id","PS12","note","V7: the pH 6.4 spermine experiments used 100 uM glutamate + 10 uM glycine, not NMDA."),
 ("proton_sensitivity.tsv","row_id","PS13","note","V7: the claim 'not one Hill-1 curve' used an unnormalised curve; normalised to pH 7.6 the Hill-1 value at 7.1 is 0.71 against 0.78 +/- 0.07 SD. The steady-state pH50 is mixed with peak fractions. The source for these native numbers is Evlanenkov 2023 (37629153), not Cheriyan 2016 (HEK triheteromer paper): the error was in the Orchestrator's brief."),
 ("proton_sensitivity.tsv","row_id","PS17","note","V7: the 'about 0.15 unit disagreement' between the fitted desensitisation function and the data misreads the authors' deliberate equilibrium correction (pH50 7.26 vs unshifted 7.11 after 60 s). Availability: about 0.84 at 7.2 and 0.46 at 7.1 after 60 s; about 0.21 at 7.2 at equilibrium. The clone carries G212D (0.08 alkaline shift)."),
 ("decisive.tsv","prop_id","N3-D11","statement","V7: see PS17 note; the model charge transport at pH 7.0-7.15 'was not observed in experiments' (Alijevic), omitted by the producer."),
 ("decisive.tsv","prop_id","N4-D15","statement","V7: overclaim: 'all values 20-25 C' should read 'all values with a stated temperature'; the compiled Hansen rows and Evlanenkov state none."),
 ("decisive.tsv","prop_id","N1-D04","statement","V7: GluN2B vs GluN2A: 'GluN2B less proton-sensitive than GluN2A' is CONTRADICTED for recombinant diheteromers (Hansen 2021 Table 5; Tian 2021; Regan 2019). Honest fractions (7.4/7.2/7.0): GluN2A 0.61-0.85 / 0.47-0.74 / 0.31-0.65; GluN2B 0.35-0.56 / 0.22-0.44 / 0.13-0.33. Loss for 7.4 to 7.2: GluN2A 9-26 percent, GluN2B 21-36 percent. Ends of the ranges use Hill 1 (assumed)."),
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
p = HERE / "proton_sensitivity.tsv"
rows = list(csv.reader(open(p, newline=""), delimiter="\t")); h = rows[0]; have = {r[0] for r in rows}
new = [
 ["V7-1","GluN2A (GluN1 K178AzF mutant, before UV)","recombinant","rat (per Tian 2021)","not applicable","room temperature","0","100 uM Glu + Gly, -60 mV, 0.3 mM Ba2+","7.00","1.91","not reported","0.853","0.707","0.500","PMID 34354080 (Tian 2021)","verifier V7 recompute","partial_fulltext_read","verifier-recomputed","V7 addition; wild-type overlap rests on Fig 3d, no wild-type pH number in the text"],
 ["V7-2","GluN2B (same background)","recombinant","rat (per Tian 2021)","not applicable","room temperature","0","100 uM Glu + Gly, -60 mV, 0.3 mM Ba2+","7.60","1.37","not reported","0.347","0.221","0.131","PMID 34354080 (Tian 2021)","verifier V7 recompute","partial_fulltext_read","verifier-recomputed","V7 addition; same lab and conditions as V7-1"],
 ["V7-3","GluN1-4a/GluN2B WT","recombinant","oocytes","not applicable","about 23 C","0","100 uM Glu + 30 uM Gly, -40 mV, 0.5 mM Ba2+","7.50 +/- 0.02 (n 6)","not reported (1 assumed)","not reported","0.443","0.334","0.240","PMID 30659174 (Regan 2019)","Table 4","partial_fulltext_read","measured (pH IC50 40 +/- 1.7 nM); fractions computed with slope 1","V7 addition; Orchestrator recheck of Table 4 in the text"],
]
for r in new:
    assert len(r) == len(h), (r[0], len(r), len(h))
    if r[0] not in have: rows.append(r)
csv.writer(open(p, "w", newline=""), delimiter="\t", lineterminator="\n").writerows(rows)
print("ok")
