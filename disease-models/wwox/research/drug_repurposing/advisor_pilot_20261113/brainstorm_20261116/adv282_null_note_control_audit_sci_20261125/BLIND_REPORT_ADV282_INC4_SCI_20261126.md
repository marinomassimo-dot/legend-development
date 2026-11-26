# Blind report, ADV-282 increment 4 (verbatim, SCI 2026-11-26)

Delegate: legend-delegate, model sonnet, effort high stated in the dispatch; read back from its transcript census: claude-sonnet-5-5 on 35 of 35 turns, effort high on 35 of 35, 43,892 output tokens, 4.33 million cache-read, peak context 209,360. The report below was delivered by its SubagentHandback call and is copied byte for byte from the delegate transcript (subagents/agent-a538b7d3ac912bec8.jsonl); the packet it answered is `BLIND_SENTENCES_ADV282_INC4_SCI_20261126.md` (sha256 6cf8cbdc...). My first reading was frozen before this report (FIRST_READ_ADV282_INC4_SCI_20261126.tsv, sha256 bb199685...).

---

BLIND VERIFICATION, ADV-282 increment 4 (8 blocks). I worked only from the held sources and the two repository ChEMBL tables listed in the packet. No network, nothing written into the repository, scratch in /home/desktop/.claude/jobs/7f7fcdaa/tmp/blind4/.

SUMMARY

| ID | Class | Verdict |
|---|---|---|
| DA-L01-005 | KO loss CHECK PRESENT; NAC engagement CHECK ABSENT | ADD |
| DR-A02-010 | CHECK PRESENT BUT NOT MATCHED | ADD |
| DR-A01-007 | CHECK ABSENT | MUST CHANGE (HDAC6 clause) |
| DR-A02-006 | CHECK PRESENT | ADD |
| DR-A02-007 | CHECK PRESENT BUT NOT MATCHED | ADD |
| DR-B01-002 | CHECK PRESENT (FA-A, 24 h) / PRESENT BUT NOT MATCHED (DEB, FA-C) | MUST CHANGE |
| DR-P9-009 | CHECK ABSENT | ADD |
| DR-E01-002 | CHECK PRESENT BUT NOT MATCHED (citation) | ADD |

Gupta 2023 limits: figure images and S1 File (underlying data) are not held. Fig 1 to 7 numbers beyond the text and legends are therefore not checkable, and I do not give any.

---

## DA-L01-005 (Cheng 2023, PMC10613160)

**Class.**
- Knockout: CHECK PRESENT.
  - Wwox protein is absent in Wwox-/- MEFs, both early and late passage, in Fig 2e. Fig 4c is described in the legend as showing WWOX. Fig 6g shows no WWOX band in late-passage -/- MEFs, with or without NAC.
  - The microarray in Supp Fig 8 is on passage-1 MEFs. Fig 2e early passage shows WWOX absent in -/- at that stage.
- NAC (compound): CHECK ABSENT.
  - Query: DHE, ROS or flow cytometry in the NAC-treated groups of Fig 6 and in the Results text, article XML, 2026-11-26. DHE (Fig 6a) is shown only for untreated Wwox+/+, +/- and -/- MEFs.
  - The paper never shows that 1 mM NAC lowered ROS in these cells. The ROS lowering is inferred from the rescue.

**In-study check:** yes (knockout). **Other effect:** the same knockout also gives lower p16 and p21 and a failure to senesce (Fig 2). That is a different endpoint.

**Verdict: ADD.** All stated facts are supported, but qualifications are missing.

Findings:
1. ROS (Fig 6a): the late-passage -/- DHE histogram is shifted right, and early passage is overlapping. This matches the text ("substantially increased level", Discussion "no apparent differences" early). Fig 6a is a single flow histogram per genotype. The legend gives no n and no quantification or statistics.
2. Microarray (Supp Fig 8, PDF p.15):
   - The heatmap has one column per genotype, Wwox+/- against Wwox-/-. The comparator is heterozygous, not wild type.
   - The legend states no n. "One sample per genotype" fits the figure but is not stated in the text.
   - No statistics are shown. All 16 rows (Cyp1a1, G6pdx, Gstp1 x2, Mpo x2, Nfe2l2, Nos3 x2, Nqo1, Park2 x2, Prdx4 x2, Sod3, Trim30a) are redder in -/-, on a log2 scale clipped at about ±1. Nfe2l2 and Nqo1 are among them, so the direction is correct.
   - The Discussion says "significant increases". There is no test behind that word.
3. "NAC rescues senescence escape":
   - Fig 6c: SA-β-gal positive is about 1.5% in -/- and about 35% in -/- with 1 mM NAC (with +/+ about 35% and +/- about 17%, all read from the bar chart). Fig 6f shows p16 promoter methylation is blocked. Fig 6g shows p16, p21 and p53 restored.
   - NAC was given continuously from MEF isolation, so this is prevention during passaging, not reversal of an established escape.
   - There is no NAC-treated Wwox+/+ or +/- group in Fig 6c, so non-specific NAC effects on senescence cannot be excluded.
4. The "initial antioxidant response" clause matches the Discussion. The authors say it is "unclear". "Non-neural" is correct (MEFs).

**Proposed wording.** "ROS is higher in late-passage Wwox-/- MEFs than in +/+ and +/- (DHE flow, Fig 6a, one representative histogram per genotype, no quantification given) and not different at early passage. In passage-1 MEFs the microarray (Supp Fig 8, one column per genotype, +/- vs -/-, no n or statistics stated) shows a set of redox genes, including Nfe2l2 and Nqo1, higher in -/-. 1 mM NAC given continuously from isolation restores SA-β-gal positivity (about 35%, Fig 6c) and p16/p21 (Fig 6g); ROS lowering by NAC was not measured. Non-neural. The authors leave an initial antioxidant response as an open question."

---

## DR-A02-010 (Gupta 2023, Tg-S466L, low-dose carfilzomib)

**Class: CHECK PRESENT BUT NOT MATCHED.**
- Same paper, same drug, same strain: Fig 1C shows Hsp70 and Hsp27 induction after 10 mg/kg retro-orbital carfilzomib at 24 h. That is a higher rate, a different route and a shorter time.
- Proteasome activity (Fig 4) was measured only in R266K, R336C, I278T and T191M, at 10 mg/kg retro-orbital for 24 h. S466L was not assayed.
- The low-dose arm (Fig 7: 2.1 mg/kg/day, 1 week, osmotic pump) has no proteasome-activity readout. Its only pharmacodynamic readout is Hsp70, which was absent.

**In-study check:** yes, but at higher dose and in other strains. **Other effect:** high-dose S466L rescue of tHcy, activity and CBS protein (Fig 1A-C, text Results "Carfilzomib rescue of Tg-S466L").

**Verdict: ADD.**

Findings (locators: Methods "Drug studies", Fig 1, Fig 7 legend, Results last paragraph of "Low dose/long-duration studies", Discussion):
1. "Low-exposure" is misleading for total dose. The 24 h subcutaneous pump arm was 15 mg/kg (Fig 1). The 1-week arm was 2.1 mg/kg/day x 7 = 14.7 mg/kg. The total dose is about equal and the rate is seven times lower. Both arms use the same route (osmotic pump) in the same strain.
2. "No Hsp70 induction" does not show absent engagement. In Fig 1C the 15 mg/kg subcutaneous 24 h arm also had no Hsp70 induction (Results: "did not observe induction in S.C. mice") and yet lowered tHcy and raised CBS activity and protein.
3. "Tolerated" is not shown for this arm.
   - No weights, blood counts or clinical observations are reported for the carfilzomib low-dose arm.
   - The only support is the authors' general statements: abstract "low-doses are less toxic", Discussion "non-toxic doses".
4. Results say "No significant differences ... in either the tHcy or CBS activity". The Discussion says "only a slight increase in liver CBS activity and no lowering of serum tHcy". The n is not given in the text.
5. "A very slight rise in protein in some animals" matches ("some of the carfilzomib-treated samples had a very slight increase in CBS protein", "much lower than in controls").

**Proposed wording.** "One week of carfilzomib by osmotic pump (2.1 mg/kg/day, about 14.7 mg/kg in total, about equal to the 15 mg/kg given over 24 h that rescued S466L in Fig 1) gave no significant change in tHcy or liver CBS activity; the Discussion calls the activity change 'slight'. Some animals had a very slight rise in CBS protein and there was no Hsp70 induction, but the 15 mg/kg 24 h arm also lacked Hsp70 induction while rescuing, and proteasome inhibition was not measured at this schedule. Tolerability of this arm is asserted by the authors but no data are shown. The allele rescued at the higher rate was therefore not rescued at the lower rate of delivery."

---

## DR-A01-007 (Guiberson 2018, Supp Fig 12a, sodium butyrate on G544D)

**Class: CHECK ABSENT.**
- Query: acetylat*, histone, HDAC, deacetyl* in the article XML text and the 28-page supplement pdftotext, 2026-11-26. Result: 0 hits in both.
- No HDAC activity, histone acetylation or any readout of butyrate action exists in the paper.
- Sodium butyrate appears only as one of 7 compounds in the 5 mM HEK293T screen (Supp Fig 12a).

**In-study check:** no. **Other effect (same endpoint, other construct):** WT Munc18-1 total protein with sodium butyrate. I read the bar at about 195% (points about 140, 207, 228) with no asterisk (Supp Fig 12a, WT panel, last bar).

**Verdict: MUST CHANGE.** One clause is unsupported.

Findings:
1. G544D, sodium butyrate 5 mM (Supp Fig 12a, G544D panel, last bar).
   - I read the bar at about 102% of control, points about 90, 93, 128.
   - No significance mark. n = 3 independent experiments (legend). The note's "about 1.05" is within reading error.
   - The same panel shows 5 mM 4-phenylbutyrate at about 183% with * for G544D.
2. "The text lists only the phenylbutyrate class and two osmolytes as stabilising": the text says "4-phenylbutyrate, sorbitol, and trehalose". "Class" is the repository's word, not the paper's.
3. HDAC comparison against both ChEMBL tables (proteostasis_pba_a01.tsv, hdac_enzyme_potency_chembl_20261029.tsv).
   - CHEMBL1671826 (2011): butyric acid IC50 is 16, 12, 9 and 15 µM on HDAC1, 2, 3 and 8. 4-Phenylbutyric acid is 64, 65, 260 and 93 µM. Butyric acid is more potent on those four.
   - CHEMBL5136998 (2022): butyric acid HDAC1 is 300 µM against sodium 4-phenylbutyrate at 162 µM, so butyric acid is weaker. This matches the note's "third document". In that document butyric acid, not sodium butyrate, is listed.
   - Sodium butyrate itself is from CHEMBL5096206 (HDAC1, 2, 3 and 8 at 16, 12, 9 and 15 µM, same values as butyric acid in 1671826). The "document-dependent" statement is correct.
4. **Unsupported clause: "it does not engage HDAC6 at the applied level".**
   - The only butyrate HDAC6 value held is IC50 > 2,000,000 nM (> 2 mM), butyric acid, CHEMBL1671826 / CHEMBL1680140.
   - The applied level is 5 mM, above the 2 mM bound. A ">2 mM" bound cannot show non-engagement at 5 mM.
   - No HDAC6 value for sodium butyrate is held, and the paper has no readout.
   - The claim is unsettled, not verified.
5. "No pan-HDAC or HDAC6-selective arm exists in this paper" holds: the word HDAC does not occur in the article or supplement. Note that butyrate is itself a class I HDAC inhibitor by the table and the paper never says so.
6. "A measured null in a cell that is not comparable": HEK293T, transient transfection, 48 h, n = 3, G544D and WT only.

**Proposed wording.** "Sodium butyrate (5 mM, same applied level as 4-phenylbutyrate) left G544D total protein at about 1.0 of control, no significance mark (Supp Fig 12a, n = 3, HEK293T, 48 h); on WT the bar is about 1.95, scattered, unmarked. The text lists 4-phenylbutyrate, sorbitol and trehalose as stabilising. In ChEMBL, butyric acid is more potent than 4-phenylbutyric acid on HDAC1, 2, 3 and 8 in CHEMBL1671826 but weaker on HDAC1 than sodium phenylbutyrate in CHEMBL5136998, so the potency premise is document-dependent. The only HDAC6 value held for butyric acid is IC50 > 2 mM, below the 5 mM applied, so HDAC6 engagement at the applied level is not settled. The paper contains no readout of butyrate's HDAC action and no pan-HDAC or HDAC6-selective arm. A measured null in a non-neuronal, transfected cell."

---

## DR-A02-006 (Gupta 2023, Tg-T191M; Mijatovic 2024)

**Class: CHECK PRESENT.**
- Same paper, same strain, same dose and time as the activity test. Fig 4D shows proteasome activity in T191M liver after carfilzomib (10 mg/kg retro-orbital, 24 h) and bortezomib (0.49 mg/kg/day pump, 36 to 48 h).
- Text: "Overall, with the exception of the Tg-R266K strain, both proteasome inhibitors were equally effective in reducing proteasome activity".
- Fig 2D (Hsp70, Hsp27): "In ... Tg-T191M mice, carfilzomib-treatment showed greater induction of both Hsp70 and Hsp27".
- I could not check the T191M values or n, because the figures are not held.

**In-study check:** yes. **Other effect:** CBS protein rose in T191M. Results: "For all of these alleles, we observed the highest levels of CBS protein in bortezomib-treated mice, but did see lesser increases in carfilzomib treated mice" (Fig 2D). The T191M tHcy result is not stated in the text.

**Verdict: ADD.**

Findings:
1. The quotes check out: "Neither proteasome inhibitor was able to restore significant enzymatic activity to the Tg-T191M strain, although treatment with bortezomib did seem to stimulate a very small amount of enzyme activity".
2. Mijatovic (HEK293A CBS-KO, stable T191M):
   - 20 nM bortezomib for 24 h raised the live-cell AzMC signal to 259% of vehicle-treated T191M, p < 0.05 (Fig 6b). Half-life rose 6.8-fold (Fig 5d).
   - Baseline T191M lysates had "essentially no activity" (Fig 1d and Fig 2c,d).
   - The authors say bortezomib- and eeyarestatin-treated cells "exhibited signs of cell damage and apoptosis".
   - So "gained activity" is a relative gain from a near-zero baseline, in a cell showing damage. Whether it reached WT level is not in the note.
3. The Mijatovic Discussion says proteasome inhibitors "partially rescued protein expression and activity of several pathogenic CBS variants modeled in transgenic mice including I278T and T191M (Gupta et al., 2013, 2023)". This is more generous than Gupta 2023's T191M wording. The note's description is right.
4. Missing for a reader: the proteasome was inhibited and CBS protein rose in T191M, yet activity did not. A "null" here is not a no-engagement null.

**Proposed wording.** "In Tg-T191M liver neither inhibitor restored significant CBS activity ('a very small amount' with bortezomib), although proteasome inhibition was confirmed (Fig 4D, carfilzomib about equal to bortezomib) and CBS protein rose with both (Fig 2D, more with bortezomib). The same allele gained activity with bortezomib in HEK293A CBS-KO cells (259% of vehicle T191M, Mijatovic Fig 6b) from an essentially zero lysate baseline, with signs of cytotoxicity, so context and readout differ. The HEK paper summarises the mouse work as 'partially rescued ... I278T and T191M', more generous than the mouse paper; the mouse paper's wording is used."

---

## DR-A02-007 (Gupta 2023, Tg-I278T, low-dose bortezomib)

**Class: CHECK PRESENT BUT NOT MATCHED.**
- Direct proteasome-activity assay: Fig 4C, I278T, but at 0.49 mg/kg/day for 36 to 48 h, which is a higher rate.
- At the low dose the only pharmacodynamic readout is Hsp70 and Hsp27 induction. Fig 6D, 0.8 mg/kg twice weekly for 14 days: "clearly induced by the bortezomib". That is indirect.
- The 32-day, 12-injection experiment (Fig 5) has no engagement readout.

**In-study check:** yes (Fig 6D Hsp induction; Fig 4C high-dose proteasome). **Other effect:** tHcy fall (Fig 5B, Fig 6B); WBC and lymphocyte fall (Fig 5E).

**Verdict: ADD.**

Findings (Fig 5 and Fig 6 legends, Results "Low dose/long-duration studies", Discussion):
1. Numbers verified. tHcy mean 345 to 179 µM, linear trend P < 0.001, 12 injections over 32 days. Treated animals had significantly reduced WBC and lymphocytes. One of eight treated animals had liver CBS activity outside the control range and also the lowest tHcy, greatest weight loss and lowest WBC and lymphocyte counts. "Still over 170 µM (normal in mouse is 3-7 µM)".
2. "Tolerated exposure" conflicts with the source.
   - The authors say "even at low dosage there is immune toxicity".
   - The Fig 5D legend marks one animal as "moribund at time of sacrifice" (the circled animal).
   - Average weight "may have been a small decrease at d32".
   - The authors' sentence "non-toxic doses" sits beside their own toxicity finding. The note should say "better tolerated", not "tolerated".
3. The tHcy fall has no concurrent diluent-injected control.
   - Fig 5B tests against the d0 time point only.
   - The Discussion concedes "it is possible that the tHcy lowering we observed was due to the injection and handling of the animals". Reviewer 2 raised the same point.
   - The note presents the halving without this caveat.
4. "No significant activity gain": the authors add that this "probably is due to the limited sensitivity of the assay at very low activity levels". This is a qualifier for the null.
5. The row endpoint says "alone or with a heat-shock co-inducer", but the note omits the combination arm (Fig 6).
   - Bortezomib 0.8 mg/kg twice weekly with or without bimoclomol (250 mg/L) for 14 days gave a similar tHcy fall in both groups (Fig 6B) and no significant CBS activity difference (Fig 6C).
   - Hsp70 and Hsp27 were induced by bortezomib, with no noticeable extra increase from bimoclomol (Fig 6D).
   - No evidence that bimoclomol was active in vivo (Reviewer 2 point 3).
6. The authors' conclusion is quoted correctly ("neither drug appears to be effective when used at non-toxic doses ... probably not feasible").

**Proposed wording.** "Better-tolerated (not toxicity-free) dosing, 12 s.c. injections over 32 days: the activity gain was not significant (authors: assay sensitivity is limited at very low activity), and WBC and lymphocytes were still significantly reduced; one animal was moribund. tHcy fell from a mean of 345 to 179 µM (linear trend P < 0.001, compared with day 0 only, with no diluent-injection control; the authors allow handling as an explanation) and stayed far above normal (3 to 7 µM). One of eight treated animals had CBS activity outside the control range and also the lowest tHcy, greatest weight loss and lowest WBC. Adding bimoclomol to low-dose bortezomib (14 d, 0.8 mg/kg twice weekly) changed neither tHcy, activity nor Hsp induction (Hsp70/27 were induced by bortezomib alone). The authors conclude proteasome inhibitors are probably not feasible as monotherapy at non-toxic doses."

---

## DR-B01-002 (Hristodor 2025, FA, amlexanox vs ataluren)

**Class.**
- FA-A LCL, MMC survival: CHECK PRESENT. Amlexanox 25 µM for 24 h induced full-length FANCA to "almost 9%" of healthy control (baseline "just under 5%"), Fig 1C, same cells and dose. The MMC test was 24 h with 25 µM, n = 3 (Fig 4 legend).
- DEB aberrations (FA-A, 1 to 3 weeks, Fig 4C-E): PRESENT BUT NOT MATCHED. Protein was measured only at 24 h.
- FA-C fibroblast micronuclei: PRESENT BUT NOT MATCHED. Amlexanox FANCC protein is not reported in the held text (only "partially effective only on FANCA" in the abstract, and Supp Fig 3 is for ataluren).
- FA-F MMC: the engagement readout is negative (Fig 1B, no FANCF increase), so that null is uninformative for read-through.

**In-study check:** yes. **Other effect (yes):** amlexanox lowered p53 by about 40% in FA-A (Fig 2D, n = 10; FA-F Fig 2B none) and pSTAT2 by about 50% (Fig 5C, n = 5).

**Verdict: MUST CHANGE.**

Findings:
1. The note never names amlexanox, or ataluren as the comparator. The comparator did rescue.
   - Ataluren gave 2.1-fold (FA-F) and 1.5-fold (FA-A) higher survival after MMC (Fig 3A,B).
   - Ataluren almost abolished DEB aberrations (Fig 3C-H).
   - Ataluren cut micronuclei by 27% in FA-C fibroblasts (Fig 7D).
   - In FA-A, ataluren induced FANCA to about 11% against amlexanox's 9%, and only ataluren rescued the phenotype. The note reads as if the head-to-head showed no rescue. That holds for amlexanox only.
2. "Full-length protein induced in one arm and not in the other" is unclear.
   - The "arms" are cell lines, not drugs: FANCA yes, FANCF no (Fig 1B).
   - FANCC is not mentioned.
   - The baseline (<5%) is omitted. The induction is from under 5% to about 9%.
3. "NMD not relieved": the text says FANCA mRNA is reduced 3-fold in FA-A and "neither amlexanox nor ataluren was able to rescue FANCA transcription" (Supp Fig 1A,B, not held). FA-F has no NMD activation, so there is nothing to relieve there.
4. "The effect that was seen is attributed ... to TBK1/IKKe inhibition, not read-through."
   - The effect is unnamed. It is the p53 fall and the pSTAT2 fall.
   - It is the authors' hypothesis ("we hypothesized", "our interpretation", "suggest"), resting on pSTAT2 and NF-κB-inhibitor comparisons. No direct TBK1 or IRF3 readout is shown.
   - The Discussion also says "admittedly a partial effect on FANCA protein expression and p53 reduction, indicating a broader spectrum of action". The authors' attributions also vary between TBK1/IKKε, NF-κB and cGAS/STING.
5. The phenotype nulls rest on: survival, n = 3 (Fig 4A,B); DEB in FA-A only, one dose (Fig 4C-E); micronuclei in FA-C by "no significant effects", n = 8 fields (fields are not independent replicates; the amlexanox bar is not visible because figures are not held).
6. A correct, useful point the note could add: the authors argue ~10% of protein "should be sufficient" (CF analogy), yet amlexanox's ~9% did not rescue.

**Proposed wording.** "Amlexanox (25 µM) induced full-length FANCA in FA-A lymphoblastoid cells from under 5% to about 9% of control (ataluren about 11%), not FANCF in FA-F cells, and did not raise FANCA mRNA (NMD persisted, Supp Fig 1). It gave no improvement in MMC survival (FA-A and FA-F, n = 3), DEB aberrations (FA-A, up to 3 weeks) or FA-C micronuclei, whereas the comparator ataluren improved all three. Amlexanox did lower p53 (about 40%, FA-A) and pSTAT2 (about 50%); the authors hypothesise TBK1/IKKε-IRF3/NF-κB inhibition rather than read-through as the cause, without a direct TBK1 readout. Their conclusion is that partial p53 lowering and about 9% protein were not sufficient for phenotypic rescue."

---

## DR-P9-009 (Wang 2026, memantine, PMID 41288262)

The held bytes include the full text XML, so the row's "abstract_only" understates what is held.

**Class: CHECK ABSENT.**
- Query: serum, plasma, concentration, "level of memantine" and adherence checks in the full text, 2026-11-26. No memantine level or target effect was measured.
- Adherence is by prescription and retention (91% at 24 weeks), and "irregular adherence" was an exclusion.

**In-study check:** no. **Other effect:** none separate. The seizure outcomes are the endpoint.

**Verdict: ADD.**

Findings:
1. Non-randomised: correct. It is a prospective, single-centre cohort.
2. "Adult" misleads. Median age was 63 (memantine 64, non-memantine 62), all with cognitive impairment, and the study is in an elderly Chinese cohort.
3. Counts and design points a reader needs.
   - 101 on memantine (10 mg/day) against 110 not. Follow-up 24 weeks.
   - Increased seizure frequency (>= 25%): 7 (7%) against 5 (5%). New-onset BTCS 0 against 0. Status epilepticus 0 against 1.
   - Four of the seven memantine-arm cases were attributed by the authors to missed antiseizure medication.
   - The groups differed at baseline: lower MMSE and MoCA, more depression/anxiety and more antidepressants (12% vs 1%) on memantine. Allocation followed patient choice, and 60 declined for fear of seizures.
   - Baseline seizure frequency was low (median 2 per 24 weeks; 28% had no seizures in the prior 24 weeks). Events were self- or caregiver-reported by diary.
   - The authors state the sample is small and AEs "may have been underestimated". Their own conclusion is cautious ("Previous warnings might have been disproportionate"; randomised trials needed).
4. "Not children, not a developmental epilepsy, not benefit": all correct. No efficacy outcome was measured.

**Proposed wording.** "Elderly adults with epilepsy and cognitive impairment (median age 63), non-randomised, patient-chosen add-on memantine 10 mg/day for 24 weeks: increased seizure frequency 7/101 against 5/110, no new-onset BTCS, status epilepticus 0 against 1. Small, self-reported, with baseline imbalances and low baseline seizure frequency, so rare worsening may be missed. It bears on the warning for this population, not on children, a developmental epilepsy, or benefit."

---

## DR-E01-002 (DNL343, JAMA Netw Open 2026, PMID 42771346; abstract only)

**Class: CHECK PRESENT BUT NOT MATCHED.**
- The abstract reports engagement only as a citation of "a prior phase 1B trial": "target engagement based on integrated stress response biomarkers in blood and cerebrospinal fluid".
- It reports no engagement readout for this trial's own participants.
- Whether the prior trial used 200 mg/d is not stated in the abstract.
- For the present trial's patients: NOT ASSESSABLE (abstract only).

**In-study check:** no. **Other effect:** none reported (secondary outcomes "not statistically different"; AE rates similar).

**Verdict: ADD.**

Findings:
1. Numbers match the abstract. DRR 1.04 (95% credible interval 0.83 to 1.32), probability DRR < 1 = 0.37, 24-week placebo-controlled, 200 mg/d, 186 on DNL343 against 63 regimen placebo plus shared placebo (139 in total).
2. "No benefit" is stronger than the abstract. The authors write "did not show evidence of slowing disease progression". The interval allows modest slowing (down to DRR 0.83) as well as worsening up to 1.32. The note should say "no evidence of benefit".
3. "Target engagement and proof of mechanism in the earlier phase" is attributed correctly to the earlier trial. The note should say that this trial's own engagement was not reported in the abstract.
4. "Adults with ALS" is correct (mean age 59.3). The compound (DNL343, eIF2B activator) is not named in the note.

**Proposed wording.** "DNL343 200 mg/d, 24-week placebo-controlled: disease rate ratio 1.04 (95% credible interval 0.83 to 1.32; probability of ratio < 1 = 0.37), so no evidence of slowing, though the interval does not exclude a modest effect. The abstract cites target engagement and proof of mechanism from a prior phase 1B trial; none is reported for this trial's participants. Adults with ALS; says nothing about a developmental encephalopathy."

---

## Files I actually opened

Packet and protocol:
- /home/desktop/.claude/jobs/7f7fcdaa/tmp/blind4/BLIND_SENTENCES_ADV282_INC4_SCI_20261126.md
- /home/desktop/legend-development/.claude/worktrees/sci_as_20261126/framework/protocols/delegation_budget.md (read)

Held sources (read whole, via text conversions in the scratch folder):
- /home/desktop/legend-development/files/fulltext/PMID37319242_Gupta2023_PMC10270616_epmc_2026-10-29.xml
- /home/desktop/legend-development/files/fulltext/PMID39041895_Mijatovic2024_PMC11264351_epmc_2026-10-29.xml
- /home/desktop/legend-development/files/fulltext/PMID37897534_Cheng2023_PMC.xml
- /home/desktop/legend-development/files/figures/PMID37897534/18_2023_4950_Fig6_HTML.jpg
- /home/desktop/legend-development/files/figures/PMID37897534/18_2023_4950_Fig2_HTML.jpg
- /home/desktop/legend-development/files/fulltext/PMID37897534_assets/18_2023_4950_MOESM1_ESM.pdf (Supp Fig 8 rendered on page 15; the pdftotext file was also read)
- /home/desktop/legend-development/files/fulltext/PMID30266908_Guiberson2018_PMC6162227.xml
- /home/desktop/legend-development/files/supplement/PMID30266908/41467_2018_6507_MOESM1_ESM.pdf (Supp Fig 12 page 19 rendered; the supplement text was searched for HDAC, histone and acetyl terms, not read cover to cover)
- /home/desktop/legend-development/files/fulltext/PMID40544182_Hristodor2025_PMC_2026-10-20.xml
- /home/desktop/legend-development/files/fulltext/ketamine_kds_it_20261117/p4_harms/PMID41288262_Wang2026_europepmc-fulltextxml.xml
- /home/desktop/legend-development/files/fulltext/ketamine_kds_it_20261117/p4_harms/txt/PMID41288262_Wang2026_abstract.txt
- /home/desktop/legend-development/files/fulltext/adv282_abstracts_sci_20261126/PMID42771346_efetch.xml (abstract and keyword search; the author list was only partly read)

Repository ChEMBL tables:
- /home/desktop/legend-development/disease-models/wwox/research/drug_repurposing/missense_recovery_it5_p8_20261029/hdac_enzyme_potency_chembl_20261029.tsv (all rows seen; the first 12 columns were printed)
- /home/desktop/legend-development/disease-models/wwox/research/drug_repurposing/pharmacology_it5_20261029/proteostasis_pba_a01.tsv (all 39 rows seen; the 12-column cut was widened for the butyrate, PBA and HDAC6 rows)

Scratch (all in /home/desktop/.claude/jobs/7f7fcdaa/tmp/blind4/): strip.py, gupta.txt, cheng.txt, mij.txt, guib.txt, hris.txt, wang.txt, supp_g.txt, and the rendered images supp8-15.png, sg12-19.png, crop12a-19.png.

Not opened: any other file under disease-models/ beyond the two named tables, any result or checkpoint, and the network.

Limits:
- Bar values from raster images are estimates: Supp Fig 12a (about 102 and about 195), Fig 6c (about 35%, 17%, 1.5%).
- Hristodor Supplementary Figures and Data, and Gupta Figs 1 to 7 and S1/S2 Files, are not held, so statements that depend on them rest on the text and legends only.
