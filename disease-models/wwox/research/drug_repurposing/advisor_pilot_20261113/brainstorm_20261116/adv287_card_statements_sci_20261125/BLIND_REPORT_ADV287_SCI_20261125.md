# ADV-287 blind report (reader: sonnet, effort high as stated by the dispatcher)

Scope notes. The folder holds 20 files: statement_01..06 and 08..21 (there is no statement_07; I did not look for it). Hypothesis level, reference genotype class only, nothing here is medical advice. No web, no PubMed, no contact. I did not open the Obeid article, its manifest or receipts. One grep of mine for a label sentence surfaced a single line of a producer file (src_11.md) whose content is identical to the material I had been given; I used no verdict from it. All Python was run with `python3 -P -E`. Extractor prose (verdicts, "matches") was ignored; every number below was re-derived from table rows, held full text, held figures or held raw tables as named.

---

## 01 (H02, "three independent centres ... between 22.1 and 44.7 percent")
1. Arithmetic printed: range 22.1 to 44.7 percent; "three centres"; no other.
2. Recomputed (human children, vigabatrin; per imaged child). Held abstracts and full texts: Beijing 38/172 = 22.09 (full text, PMID 36601084; 172 is what remains of 390 imaged after 18 + 193 + 7 exclusions: 390-218 = 172, checked); Beijing sister report 25/77 = 32.5 (same department); Emory 18/64 = 28.1; Dammam 34/76 = 44.7; Toronto (PMID 20384718 abstract) 25/81 = 30.9; Washington DC (PMID 18783433 abstract) 7/22 = 31.8 (8/23 = 34.8); UCLA 2024 (full text) 17/56 = 30.4 imaged (17/108 = 15.7 per treated); Dutch registry (full text) 27/76 = 35.5; UCLA 2017 (abstract) 6/40 = 15.0 (asymptomatic subset only; 10/45 = 22.2 only if the 4 symptomatic cases sit inside the 45, not stated). evidence_b1.tsv rows B1-01, 08, 11, 12, 13, 35, 36, 39, 40, 41 exist as described. The sentence's three (Beijing, Emory, Dammam) reproduce 22.1, 28.1, 44.7.
3. INCOMPLETE. Span: "three independent centres". The same table carries at least seven centres with an imaged-child rate (Beijing, Emory, Dammam, Toronto, Washington DC, UCLA, Dutch registry); all clean imaged-denominator rates fall inside 22.1-44.7, but UCLA 2017 (6/40 = 15.0, subset) lies below, and the Beijing 22.1 uses a denominator that dropped 193 imaged children for exposure over one year. "One partial full text, others abstract" is true only of the three named; Dutch and UCLA 2024 were read at full text. Depth: table + full text (36601084, 39570186, 39641935) + abstracts.

## 02 (A01, "about 8 to 78 times the class's HDAC enzyme IC50")
1. Arithmetic printed: ratio range 8 to 78 (applied level / IC50).
2. Recomputed (human recombinant HDAC, PBA IC50 uM: HDAC1 64, HDAC2 65, HDAC3 260, HDAC6 240, HDAC8 93; sodium PBA HDAC1 162; HeLa extract Ki 2.8). Applied PBA levels in held TSV proteostasis_pba_a01.tsv: 0.5 mM (Delahanty), 2 mM (DeLeeuw, Song), 5 mM (Guiberson; HEK293T per Supp Fig 12 caption, worms in the TSV row), 10 mM (Shah, HEK293). 2000/240 = 8.3 and 5000/64 = 78.1 are the extremes only for 2 and 5 mM against HDAC1 (64) and HDAC6 (240). With all cell levels: 10 mM/64 = 156; 0.5 mM/240 = 2.1; over all five recombinant PBA IC50s the span is 1.9-156 (0.5/260 = 1.9). Against the extract Ki 2.8 uM: 179 to 3,571. Butyrate (class member, applied 2 and 5 mM): 6.7-312.5 on HDAC1, at most 1.0-2.5 on HDAC6.
3. INCOMPLETE. Span: "about 8 to 78 times the class's". It is PBA only, two precedents (2 and 5 mM), HDAC1 and HDAC6 only; the 10 mM and 0.5 mM levels, HDAC2/3/8, the Ki and butyrate are left out and widen the span to roughly 2 to 156 (PBA, recombinant). Depth: table (TSV rows, all read); applied-level primaries not reopened.

## 03 (H02, "the one cohort reporting its exposed denominator gives about 26 percent per exposed child")
1. Arithmetic printed: about 26 percent per exposed child.
2. Recomputed. Dammam abstract: 76 imaged = 57.6 percent of cohort, so cohort = 76/0.576 = 131.9; 34/132 = 25.8 percent (the denominator is derived, the abstract prints only the 57.6 percent). Cohorts whose held text prints a treated denominator: Beijing "533 children with IS who had VGB exposure were screened" (38/533 = 7.1; 193 imaged long-exposure children unscored); UCLA 2024 "Among 108 children with detailed vigabatrin exposure data ... 17" (17/108 = 15.7); Dutch "80 TSC patients treated with vigabatrin" (27/80 = 33.8 derived; paper prints 27/76 = 35.5); Toronto "95 treated" (25/95 = 26.3 derived); UCLA 2017 "143 documented, 104 with exposure data" (10/143 = 7.0 or 10/104 = 9.6, derived). B1 rows B1-35 (80) and B1-36 (108, 17) state these too.
3. WRONG (borderline INCOMPLETE). Span: "the one cohort reporting its exposed denominator". At least Beijing, UCLA 2024 and the Dutch registry print a treated denominator in held full text, and Dammam itself does not print one (it is derived from a percent). The 26 percent arithmetic for Dammam is right, but per-exposed-child values run 7.0-26.3; 26 is the top of the spread, not a lone value. Depth: table + full text + abstracts.

## 04 (E02, "one comparator document with LDH5 and LDH1 inhibition of 7 percent at 2 millimolar and no value at 0.5 millimolar")
1. Arithmetic: none.
2. Recomputed from the raw ChEMBL pull (collected.json.gz, Q03, racemate CHEMBL1983350; human LDH, pyruvate, UV-VIS): document CHEMBL4311969 holds four Inhibition rows: LDH5 2 mM = 7.0 %, LDH1 2 mM = 7.0 %, LDH5 0.5 mM and LDH1 0.5 mM with null value and relation. The only other LDH-related rows for this molecule are four fold-change rows (0.27, 0.33, 0.70, 0.49) on mouse hepatocyte GO/LDHA in a second document (CHEMBL5120856); they are not LDH5/LDH1 percent inhibition.
3. CORRECT. Raw-row depth. Note for the reader: a second LDHA-related document exists but is a different measure, which the sentence does not claim to cover.

## 05 (H02, "22 percent in exposed infants against 4 percent in naive infants (205 infants, ten sites, readers blinded)")
1. Arithmetic: 22 vs 4 percent; N = 205; none to derive.
2. Held abstract (Europe PMC core, PMID 19054414): "332 cranial MRIs from 205 infants (aged <or=24 months) with IS treated at 10 sites in the United States and Canada"; "MRIs were read by two neuroradiologists blinded to treatment group"; "prevalence ... (22% vs. 4%; p < 0.001)" for vigabatrin-treated vs vigabatrin-naive. Label 5.3 repeats N=205, 22% vs 4%.
3. CORRECT at abstract depth. Arm sizes are not printed, so counts cannot be recomputed; the 668 older children/adults with null difference are a separate stratum.

## 06 (H02, "18 of 64 children (28.1 percent) had the finding")
1. 18/64 = 0.28125 = 28.1 percent.
2. Abstract (PMID 42735667): "Sixty-four patients met the inclusion criteria, of whom 18 (28.1%) developed VABAM"; 46 negatives matches 34/46 = 73.9; 9/18 = 50.0.
3. CORRECT. Abstract depth. The denominator is children with at least two MRIs before and during treatment; the sentence does not say so (not a numerical defect).

## 08 (F03, "mouse brain to plasma ratio about 0.015 to 0.02 and efflux at the blood-brain barrier")
1. Arithmetic: none beyond the quoted ratio range.
2. Held: producer table row (Toellner 2015, mouse) with verbatim abstract sentence "so that the brain:plasma ratio (~0.015-0.02) was not altered"; rat figures (Loescher 2024, 0.004-0.022, 14 regions) are a different species and the sentence says mouse. The only mouse ratio in the table is this one, so 0.015-0.02 is one document's range, not a cross-document spread. The abstract itself is not held.
3. CORRECT, at a depth below the abstract (secondary table holding a verbatim abstract sentence). "Efflux at the BBB" is supported only by the probenecid design and the mouse Oat3/MRP4 paper in the same table, not by a quoted sentence for this ratio.

## 09 (A01, "Supp Fig 12a ... about 2.35 fold with trehalose and about 1.8 fold with sorbitol, both marked")
1. 2.35 and 1.8 fold (read-off values).
2. Figure SuppFig12_p19.png opened by eye (axis 0-300, percent of control, G544D panel of 12a, HEK293T): trehalose 200 mM about 235-237 with one asterisk; sorbitol 200 mM about 178-180 with one asterisk; sorbitol 400 and trehalose 400 about 78 and 90 with no mark. Caption: n = 3 independent experiments, means +/- SEM. The only mutant in panel a is G544D.
3. CORRECT (figure by eye, about +/-10). The sentence omits the 200 mM concentration; the 400 mM arms gave no rise. In panel b the same cells' G544D sorbitol bar is about 105 and unmarked, so the sorbitol effect is not stable between panels of the same figure; the sentence is scoped to 12a.

## 10 (P11, "half-inhibitory Mg2+ about threefold smaller at -70 than at -50 mV, about 2.5-fold smaller at -90 than at -70 mV")
1. 173/53.3 and 53.3/20.9.
2. Held abstract quotation (locators.tsv L12; rat P7 substantia nigra dopaminergic neurones, whole cell NMDA current): IC50 20.9, 53.3, 173 uM at -90, -70, -50 mV. 173/53.3 = 3.25; 53.3/20.9 = 2.55; 173/20.9 = 8.3 (not printed).
3. CORRECT. "About threefold" rounds 3.25 down by about 8 percent. Abstract-quotation depth; article body not held. The sentence does not name species or preparation (rat P7 dopaminergic neurones, not cortex).

## 11 (L01, "no potency row), monkey brain content similar to plasma, 97% protein bound, CYP3A4 substrate, half-life 57 h (label)")
1. Arithmetic: none.
2. Per element. 97 percent: quoted in a held verifier table (Skyclarys label quotation); label bytes not held. "No potency row": the raw ChEMBL JSON for omaveloxolone (CHEMBL4303525) holds two EC50 rows (anti-necroptotic, human HT-29 1,410 nM, mouse L929 5,250 nM) and no KEAP1/NRF2 row, so the clause is true only for NRF2/KEAP1. Monkey brain content, CYP3A4 substrate, 57 h: no held bytes (no Reisman 2019 file, no label file); no held table quotes "substrate" or a half-life.
3. NOT ASSESSABLE for four of five elements (monkey brain, CYP3A4, 57 h, label-sourced numbers) because the sources are not held and no external fetch is allowed; one element checks against a held quotation; the "no potency row" clause is accurate only when read as "no NRF2 potency row".

## 12 (F01, "No consistent GRIN2B or GRIN2D shift at 4 versus 2 libraries")
1. None.
2. I recomputed from the raw Salmon count table GSE156243 (human WWOX-KO organoid, KO cko1-4, WT cwt1-2; library sizes 38.73, 41.15, 38.21, 34.21 | 37.26, 29.98 M). GRIN2B CPM 27.53, 45.46, 27.43, 20.84 | 26.63, 20.25: KO mean 30.32, WT 23.44, ratio 1.29; 3 of 4 KO above the highest WT (by 0.9 and 0.8 CPM for two of them), cko4 inside the WT pair. GRIN2D CPM 72.54, 71.90, 114.43, 104.51 | 98.78, 88.63: ratio 0.97, 2 above and 2 below. (GRIN2A, not in the sentence: 3.47, 4 of 4 above.)
3. CORRECT. Raw-table depth. GRIN2B group means differ by about 29 percent; with two WT libraries "no consistent shift" is a fair description, not a proof of none.

## 13 (J01, GFAP-positive cells 470/255, 620/330, 1100/540, 1570/850: "a roughly constant half")
1. 255/470, 330/620, 540/1100, 850/1570.
2. Figure 5B opened by eye (rat cortex, +/+ open vs lde/lde grey, PND 5, 10, 15, 21; ** on all four): about 470/255, 620/330, 1100/540, 1570/850. Ratios 0.54, 0.53, 0.49, 0.54. No other age or genotype in panel B.
3. CORRECT (figure by eye, +/-30). "From the first age measured" = PND 5. The western GFAP (panel E) is lower only at PND 15; the sentence is about cell counts.

## 14 (A02, allele dependence: S466L, I278T/R266K/R336C, T191M, G307S)
1. Counts: 1 + 3 + 1 + 1 = 6 alleles.
2. Held full text (Gupta 2023, PMID 37319242; figures not held). S466L: high-dose carfilzomib gave liver CBS activity "as high as ... some in Tg-hCBS mice" and tHcy under 5 uM; low-dose carfilzomib (2.1 mg/kg/day) "amount of rescue was minimal". I278T/R266K/R336C: bortezomib "much more effective than carfilzomib in restoring CBS activity". T191M: "Neither proteasome inhibitor was able to restore significant enzymatic activity ... although treatment with bortezomib did seem to stimulate a very small amount of enzyme activity". G307S: not tested in this paper; Introduction states bortezomib "was not effective in restoring function to the p.G307S allele" (refs 11-14); ref 14 title: "effects on CBS activity but not stability".
3. INCOMPLETE. Spans: "one not at all in the mouse (T191M)" omits the "very small amount" of activity with bortezomib (the paper says no significant activity); "a stable but inactive allele (G307S) not at all" places an allele not tested in this paper among tested ones; the outcomes depend on drug and exposure (S466L at low dose also minimal) as well as on allele. Counts and allele assignments otherwise match. Full-text depth, figures not seen.

## 15 (B01, "About 57 percent ... in the largest genotype-classified cohort are null/null (56.8 percent ... 50 individuals from 45 families, PMID 40875931")
1. 56.8 rounds to about 57.
2. Held manifest locators of 40875931: 50 individuals, 45 families; "Forty-four of the 50 cases were included"; N/N 25 (56.8), N/M 13 (29.5), M/M 6 (13.6); 25/44 = 56.8, 25+13+6 = 44. Held full text of Oliver 2023 (PMID 36779245): "We stratified all 75 cases into ... null/null (n = 45), null/missense (n = 15), missense/missense (n = 15)": 45/75 = 60.0 percent; the 75 = 13 new + 62 literature cases.
3. INCOMPLETE. Span: "the largest genotype-classified cohort". 75 genotype-classified individuals (Oliver 2023, held) exceed the 44 classified here, and give 60.0 percent. The 56.8 percent is right for the 2025 cohort (the Oliver set is a pooled cohort, so the superlative may be argued, but the comparator is left out). Manifest and full-text depth; the 40875931 article itself is not held.

## 16 (H02, rodent and dog lesions "inside the human range", neonatal/juvenile rat vacuoles "distinct")
1. None.
2. Held SPL, 5.4: IME "seen in animals at doses within the human therapeutic range. A no-effect dose was not established in rodents or dogs"; neonatal/juvenile rat gray-matter vacuolar changes "considered distinct from the IME observed in vigabatrin treated adult animals"; young-animal effects "at doses lower than those producing neurotoxicity in adult animals ... plasma levels substantially lower than those achieved clinically". 8.4: juvenile rat no-effect dose 5 mg/kg/day, AUC under 1/30 of paediatric; juvenile dog lowest effect dose 30 mg/kg/day.
3. CORRECT as to both clauses. Not stated in the sentence: the young-animal vacuoles occurred at exposures below clinical exposure, so "distinct" is not a reassurance. Version held is 2025-12-17, the card cites 2026-06-15; not compared.

## 17 (K01, leave-one-out: HPC and PFC at least 60 percent, cortex without M6 0.21, 0.38, 0.22)
1. Ratios 0.21, 0.38, 0.22; threshold 0.60.
2. I recomputed from the per-animal set means (mouse GSE215425 P47T vs WT; HPC, CTX, PFC 5 vs 5), and checked that the held unit_values file holds these regions/sets. Minimum leave-one-out ratio: HPC 0.629, 0.814, 0.737; PFC 0.617, 0.849, 0.742 (HYPOXIA, GLYCOLYSIS, APOPTOSIS); CTX without M6 0.212, 0.378, 0.216. No sign change in any removal. Cerebellum (4 vs 3), not named: HYPOXIA falls to 0.16 without F8.
3. CORRECT. Table recomputed from animal values. The sentence is scoped to three regions.

## 18 (H02 next measurement: Wwox-deficient juvenile model, vigabatrin vs vehicle, blinded EM, interaction test)
1. None.
2. A proposed design: no number or source value to recompute.
3. NOT ASSESSABLE (a design, not a statement of a source). Its premises (published rat dosing windows, survival of a neuron-specific deletion) sit in other fields and were not tested here.

## 19 (J01, anakinra NORSE/FIRES: "up to 73 percent within two weeks in a pooled uncontrolled review of 75 patients", 14-patient series)
1. 73 percent; 75 patients; 14 patients.
2. Neither abstract (PMID 38430119, 40614647) is held; only the repository's own table, which says 75 patients, 52 on anakinra, up to 73 percent within two weeks (tocilizumab 70), and the 14-patient series with "no evidence of efficacy on the long-term neurological outcome was demonstrated". 52/75 = 69.3.
3. NOT ASSESSABLE at source. Lead for a reader with access: whether 73 percent is of the 52 anakinra-treated or of 75, and the tocilizumab arm (70) the sentence leaves out. The sentence itself does not say "of 75".

## 20 (H02, "the labelled indication age is 1 month to 2 years, the age range of the N=205 study is not stated")
1. None.
2. Held SPL 1.2/8.4: indication "1 month to 2 years of age"; 5.3 gives "infants ... (N=205)" with no age range. Held abstract of PMID 19054414 (205 infants, 332 MRIs, ten sites, 22 vs 4): "205 infants (aged <or=24 months)". The N=205 label study is identified with this paper by 205/22/4.
3. WRONG for the span "the age range of the N=205 study is not stated": the study's abstract states it (24 months or less; only an upper bound, no lower bound). True only if "not stated" means "not stated in the label". Abstract and label depth.

## 21 (P11, DQ/SQ p 0.09 not reproduced; 0.055 and 0.114 for 26 and 22; ranges for other sizes)
1. p values for a 2x2 of 4/n1 vs 0/n2.
2. Held full text (Yadav 2022, PMID 35222658), Table 2: "DQ/SQ | Normal | 4 | 0 | 0.09", the only DQ/SQ row; headers n = 26 and n = 22. I implemented chi-square and two-sided Fisher: 26/22 gives 0.055 and 0.114; 13/13 gives 0.030 and 0.096; 22/22 0.036/0.108; 24/24 0.037/0.109; 13/11 0.044/0.098; 12/12 0.028/0.093; 15/10 0.075/0.125; 24/17 0.076/0.128; 25/18 0.075/0.127; every paper-derived size lies inside 0.030-0.075 and 0.096-0.128. No paper-derived size gives 0.09 (Fisher 12/12 is 0.093, a size the paper does not support; the Discussion prints P = 0.094).
3. CORRECT for what is checkable. The sentence does not list the "other sizes tried", so its ends of range reproduce only as the 13/13 lower end and by sizes of the upper-end kind (15/10, 24/17), none read from the paper. (Aside, not in the sentence: Table 1's spasms-per-episode row 3/23 vs 7/17 gives uncorrected chi-square 0.119 and Fisher 0.164 by my computation, not the 0.085 and 0.152 in the extractor's note.)

---

## Class counts
CORRECT 11 (04, 05, 06, 08, 09, 10, 12, 13, 16, 17, 21); INCOMPLETE 4 (01, 02, 14, 15); WRONG 2 (03, 20); NOT ASSESSABLE 3 (11, 18, 19). Total 20.

## Where I was unsure
- 03: WRONG vs INCOMPLETE. The rubric fits both (a count "one" that is false, cohorts left out of a count); I chose WRONG because three held full texts print a treated denominator and the lone cohort does not.
- 20: WRONG vs CORRECT-as-label-scope vs INCOMPLETE. "N=205 study" is identified with Wheless 2009 only by matching numbers; the abstract gives an upper bound, not a full range.
- 14: INCOMPLETE vs WRONG for T191M "not at all"; the paper says "no significant" and "very small amount", so I judged it an omission.
- 15: the superlative depends on whether a 13 + 62 pooled set is a "cohort"; the 2025 paper itself was read only through manifest locators.
- 09, 10: CORRECT with scope omissions (200 mM concentration; rat dopaminergic neurones); 3.25 as "about threefold".
- 08: ratio quoted only through a secondary table with a verbatim sentence; the efflux clause is inferred.
- 21: the stated ranges depend on unlisted sizes.
- 16: numerically fine; whether "but" reads as reassurance is a framing judgement.
- 11, 19: sources not held; NOT ASSESSABLE is a statement about access, not about truth.
