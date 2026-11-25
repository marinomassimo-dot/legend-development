# Blind report, ADV-282 increment 3 (checker: sonnet, effort high, 2026-11-25)

Hypothesis-level reading of open-access papers; not medical advice. Only the files named in the input
file were opened (list at the end). I did not open the framework protocols the dispatch preamble mentions,
because the task rules say to use only the files named in the input file. Scripts are in
`/home/desktop/.claude/jobs/ae0002e7/tmp/adv282/blind3/work/` and were run with `python3 -I -P -E`.

---

## DA-I01-002 (PDK1, Kosla 2019, GSE126075)

**VERDICT: MUST CHANGE.**

What I could reproduce from the deposit (`GSE126075_TPMexpression_all_genes_all_samples_merged.txt.gz`,
`..._TSScoordinates_..._F5mapped.txt.gz`; human H9-derived neural stem cells, one library per sample):

- PDK1 has a single mapped promoter, `p5@PDK1`. The deposited values (simple TPM) are: progenitor control 5.156,
  progenitor shWWOX 3.558, day-14 neuron control 3.304, day-14 neuron shWWOX 1.571.
- Multiplying by the library sizes in `bed_streamed_tagcounts_and_sha256.tsv` gives integer tag counts:
  about 163 vs 51 (progenitors) and 108 vs 64 (neurons). So n = 1 library per arm is confirmed.
- The Poisson 95% half-width of the log2 shift is 0.454 (progenitors) and 0.446 (neurons). This matches
  "interval about 0.45".
- Log2 shift with library-size normalisation (what the deposited TPM encodes):
  progenitors -0.535, neurons -1.072. **Both are negative.**
- Log2 shift re-centred on the median gene shift (progenitors median +0.20; neurons median -1.45; genes with
  at least 20 tags in both libraries): progenitors -0.74, neurons +0.38 (matched-expression genes: -0.84 and +0.38).
  The sentence's -0.67 and +0.44 are close to this family but I **could not reproduce -0.67, +0.44 or
  p about 0.49 exactly** (my empirical two-sided p of PDK1 against the all-gene centred distribution is 0.32
  progenitors and 0.52 neurons; matched-expression 0.36 and 0.66). NOT REPRODUCED. The normalisation behind the numbers is not stated.

Problems in the sentence:

1. "the interval (about 0.45, Poisson) spans zero". With the stated -0.67 and a half-width of 0.45 the interval is
   [-1.12, -0.22], which does **not** span zero. With my library-size shift (-0.535) it is [-0.99, -0.08], also
   excluding zero. Only the neuron value (+0.44 ± 0.45 = [-0.01, +0.89]) touches zero. As worded, the progenitor
   half of the claim is false by the sentence's own numbers. What is supportable is the gene-wide null (the spread of shifts across
   genes has SD about 1.0 log2 in both stages), which dwarfs ±0.45.
2. "the sign is not concordant across stages". This holds only after median re-centring. Under library-size
   normalisation (the deposit's own TPM) both stages are decreases (-0.54, -1.07). The two stage libraries differ
   hugely in composition (summed TPM over the clusters: neuron control 269,602; neuron shWWOX 91,718;
   progenitors 619,266 vs 616,711), so the normalisation choice flips the neuron sign. The sentence does not
   say which normalisation it used.
3. "its control": the paper's text calls the comparator hNPC/shScrambled (Results, Methods), but the GEO sample
   metadata for GSM3590948/GSM3590950 say `wwox expression: wild type`, `Series_overall_design` says "native and
   silenced", and the sample titles are "hNSC" and "neurons". Which control the CAGE library is cannot be settled from the held bytes.
4. "radial-glia markers lower": supported in part. Progenitor shWWOX vs control TPM: FABP7 40.3 -> 18.4,
   PAX6 7.76 -> 0.77, SOX2 40.4 -> 13.7 (lower); NES 52.1 -> 46.0, VIM 1996 -> 1834, HES1 25.2 -> 25.7 (about unchanged).
   MAP2 70.8 -> 38.8. So "some" radial-glia and stemness markers, not all.

Suggested replacement for the middle of the note: "Progenitors: PDK1 CAGE tags 163 (control) vs 51 (shWWOX), n = 1 library
per arm. Library-size-normalised log2 shift -0.54 in progenitors and -1.07 in day-14 neurons (both decreases; Poisson
95% half-width about 0.45, so the progenitor Poisson interval alone excludes zero); after median re-centring
(-0.74 and +0.38) the neuron sign reverses and PDK1 sits inside the all-gene spread of shifts (SD about 1.0 log2).
The direction therefore depends on normalisation, and with n = 1 no decrease is demonstrated."

**CHECK CLASS: CHECK PRESENT** (progenitors, protein) / CHECK PRESENT BUT NOT MATCHED (neurons, protein).

- In-study check: **yes**. `PMID31543760_assets/Data_Sheet_1.pdf`, Supplementary Figure 1 (page 1 of the PDF; viewed
  rendered at 80 dpi): Western blot of native hNPC, hNPC/shScrambled, hNPC/shWWOX; the WWOX band is clearly
  weaker in shWWOX than in either control (GAPDH loading). Single blot, not quantified, no n. This is in the
  progenitors (same cell type; the CAGE sample is the same cell line, 2D culture stated).
- Day-14 neurons: no protein check after differentiation. The deposit itself shows the WWOX gene-level TPM:
  neuron control 2.54 -> shWWOX 0.52 (about 83 vs 21 tags; log2 -2.30, median-centred about -0.8): transcript
  lowered in the neurons.
- Progenitors, deposit transcript: WWOX gene-level TPM 2.90 -> 3.35 (log2 +0.21): the CAGE data show **no transcript
  loss** in progenitors, so the knockdown rests on the Western alone.
- other effect of the same manipulation: **yes** (mitochondrial redox potential, adhesion, 2,282 differentially
  expressed genes; article Results and Figures 2-3; Data_Sheet_1 Supplementary Table 1 lists PDK1 with a PCA
  contribution of 0.726 among oxidative-stress genes).

Replicate unit: one CAGE library per arm (human neural stem cell line, H9-derived, passage not stated).
Figure images of the article (g001-g011) were held but not needed for this block.

---

## DA-K01-005 (cytoplasmic HIF-1alpha, Baryla 2022)

**VERDICT: ADD.**

Verified: Results (section 2.6.1) say cytoplasmic HIF1α is decreased in WWOX KO vs CONTR in normoxia-normoglycaemia
(2-fold, p<0.01) and hypoxia-normoglycaemia (nearly 2-fold, p<0.001) and "One repetition is shown in the Figure 6".
Figure 6a (`ijms-23-03326-g006.jpg`, left panel, viewed at 200% and 500%): values read by eye (fold change,
CONTR then KO): NN 1.0 vs 0.55 (1.8-fold), NH 0.92 vs 0.9, HN 2.07 vs 1.26 (1.6-fold), HH 2.12 vs 2.46. Cytoplasm
SEM bars are tiny although n is not stated anywhere (no "n =" in the article; statistics are "one-way ANOVA with repeated measures"). The other
two conditions carry no KO-vs-CONTR bracket; the text does not say "not significant" for them explicitly.

Needed additions:

1. **Time.** The Methods (4.6) say subfractions were isolated "after 6 h culture", but the Figure 6 caption says "after 48 h incubation". The note
   quotes 6 h only. Replacement: "6 h (Methods) or 48 h (Figure 6 caption), not reconciled".
2. **Star count.** The NN KO-vs-CONTR bracket in Figure 6a carries a single star (read at 1000% crop, low JPEG
   resolution) whereas the text says p<0.01. Say "p<0.01 in the text; one star in the figure".
3. **Same paper, other HIF1α readouts disagree.** Total HIF1α by immunofluorescence at 6 h (Figure 8c; text 2.6.3)
   is **higher** in KO in NN (about 4 -> 16 integrated density units, p<0.01) and NH (about 10.5 -> 21, p<0.01),
   not different in HN and HH; HIF1A mRNA is up 1.9-fold in NN (p<0.05), 1.5-fold in HN (p<0.05); HRE-luciferase is up in NN, NH, HH. A reader who sees only the
   cytoplasmic decrease would miss that in NN the same cells show total HIF1α up and cytoplasmic HIF1α down.
4. **"the MEF increase is nuclear".** The held Baryla text (Discussion) says only that Wwox-deficient MEFs
   "exhibited increased HIF1α protein levels and its activity" (Aqeilan/Abu-Remaileh reference 26); no compartment is
   given. The compartment statement is not supported by any held file. NOT CHECKED against the MEF paper itself (not held).
5. n not stated, one repetition shown, KO is a Cas9/sgRNA lentiviral "set" with puromycin selection (clonality not
   described; "polyclonal pool" is the repository's word, not the paper's).

**CHECK CLASS: CHECK PRESENT.** In-study check: **yes**. Figure 6a, same blot, same cell line (1BR.3.N human skin
fibroblasts), same conditions: cytoplasmic WWOX protein is lower in KO in all four conditions (text: more than 4-fold NN and NH,
3-fold HN and HH; my figure read: CONTR 1.0/1.1/0.52/0.58 vs KO 0.20/0.15/0.13/0.14). Basal protein loss also in
Figure 1a,c (WWOX/GAPDH 0.43 vs 0.05, about 8.5-fold) and mRNA 1e (0.35 vs 0.12). other effect of the same manipulation:
**yes** (HK, LDH, lactate, glucose uptake, HRE; Figures 2-5).

---

## DA-K01-006 (nuclear HIF-1alpha, Baryla 2022)

**VERDICT: ADD.**

Verified verbatim: Results 2.6.1 "We didn't observed WWOX influence on HIF1α protein in nuclear fraction." Discussion:
"We determined that knock-out of WWOX leads to increased HIF1A mRNA and protein level together with its
translocation to the nucleus and raise of its transactivation function." The paraphrase is accurate.

Needed additions:

1. **Nuclear WWOX was not lowered in normoxia-normoglycaemia.** Results: nuclear WWOX is "significantly lower also in nucleus" only in
   NH, HN and HH (all p<0.05). Figure 6b (viewed 200%): nuclear WWOX bars CONTR 1.0/3.05/2.3/2.5, KO 1.7/0.45/0.2/0.1,
   no bracket for NN. So in NN the nuclear null is not paired with a nuclear knockdown.
2. **The null is wide.** Figure 6b nuclear HIF1α (read by eye, CONTR then KO): NN 1.0 vs 5.4 (SEM about 3.8), NH 1.5 vs 1.2,
   HN 5.7 vs 6.8, HH 5.4 vs 0.85. A 5-fold mean difference in NN is "not significant" only because of the spread; n is not stated.
   "Not a demonstrated equivalence" already covers this in words; the numbers would help.
3. "what survives of that sentence is the HRE reporter and mRNA result". The paper's total-protein readout also supports
   a protein increase in part: Figure 8c total HIF1α up in KO in NN and NH (p<0.01), and HIF1A mRNA rose in every condition (significant in NN and HN). The
   sentence omits this. HRE reporter up in NN (p<0.01), NH (p<0.05), HH (p<0.01), not HN.
4. Time conflict 6 h (Methods) vs 48 h (Figure 6 caption), as in DA-K01-005.

**CHECK CLASS: CHECK PRESENT** in 3 of 4 conditions (nuclear WWOX lower in NH, HN, HH); for NN, CHECK PRESENT BUT NOT
MATCHED (cytoplasmic WWOX lowered, nuclear not). In-study check: **yes**, Figure 6b and Results 2.6.1. other effect of
the same manipulation: **yes**, same as above.

---

## DA-I01-004 (PDH activity, Baryla 2022)

**VERDICT: ADD.**

Verified: Results 2.5 wording ("activities of pyruvate dehydrogenase kinase (PDK) and citrate synthase (CS) were not
changed" in NN; "did not contribute to the changes in hexokinase, pyruvate dehydrogenase, and citrate synthase
activity" in NH; "We didn't observed any significantly important differences in the activity of pyruvate
dehydrogenase, lactate dehydrogenase, and citrate synthase" in HN; "no significant effect on enzymes activity" in HH).
Methods 4.10 describe only a PDH colorimetric kit (BioVision); Figure 5b is titled "Pyruvate dehydrogenase". n is
not stated; no phosphorylated PDH is measured (no p-PDH, Ser293 or E1α hit in the article). The note is accurate on these points.

Needed additions:

1. "hexokinase activity, LDH activity and lactate were higher" holds only in some conditions (Figure 5, viewed 200%,
   with text): hexokinase higher in NN (**, 1.6-fold) and HN (***); not in NH (KO 13.3 vs CONTR 16.7, no mark) and
   no within-condition mark in HH; LDH higher in NN (**, 1.4-fold) and NH (**) only; lactate higher in all four
   (NN **, NH ***, HN ***, HH **, text 1.6-fold NN, 1.3-fold HH). Add "in some conditions (hexokinase NN, HN; LDH NN, NH; lactate all four)".
2. PDH values by eye (mU/mL, CONTR vs KO, mean ± SEM bars large): NN 2.25 vs 3.05 (SEM about 1.7), NH 6.75 vs 6.1, HN 4.9 vs 7.2,
   HH 5.7 vs 5.55. The HN KO mean is 47% above control and NN 36% above; the null has a very wide error bar and an unstated n. The only
   significant PDH comparison in Figure 5b is CONTR NN vs CONTR NH.
3. The same paper reports that WWOX **overexpression** lowers PDH activity (p<0.001, HN and HH; Results 2.5; Figure S3, text
   only, the .tif not opened), so the PDH kit can read a change; this is an assay control, not the same manipulation.
4. HH: WWOX mRNA (Figure 4a: CONTR 1.0 vs KO 0.78, ns) and total WWOX by immunofluorescence (Figure 8c, ns; text "did not
   modify the total intracellular content of WWOX") are **not** lowered in hypoxia-hyperglycaemia, which is the condition where "no effect on enzyme activities" is
   stated; the Western (Figure 6a) does show cytoplasmic loss there. Mention that the HH null sits next to a knockdown that was inconsistent across assays.

**CHECK CLASS: CHECK PRESENT** (with the HH exception in point 4). In-study check: **yes**. Figure 1 (WWOX protein about 8.5-fold,
mRNA about 3-fold lower in KO), Figure 4a (48 h, WWOX mRNA lower in NN, NH, HN), Figure 8c (6 h, WWOX lower NN, NH, HN),
Figure 6 (Western). other effect of the same manipulation: **yes** (hexokinase, LDH, lactate, glucose uptake, HRE, HIF1A mRNA; Figures 2-5).
PDH assay time: 48 h (Figure 5 caption). Replicate unit: not stated.

---

## DR-W2-002 (memantine, GRIN gain-of-function, Karnstedt 2026)

**VERDICT: MUST CHANGE.**

Verified (article Results 3.4, Figure 2 legend, S2 sheet): 14 of 19 GoF individuals improved; 10 sustained plus 4 initial
effect that faded (#3, #7, #11, #22); behaviour 12 of 17 (S2: improved #3, #7, #22, #1, #21, #24, #5, #14, #26, #27, #33, #34;
none #25, #6, #13, #32, #20; n.a. #10, #11), development 6 of 12 (improved #11, #3, #21, #5, #14, #33; none in 6; 7 n.a.), seizure frequency reduced in 7 of 18
(#7, #14, #20, #26, #27, #33, #34; #34's S2 text is ambiguous). Three GoF individuals (#10, #25, #32) had increased seizure frequency (S2 and text).
Recomputed Fisher exact tests reproduce the authors' values: 14/19 vs 3/15 p=0.0049; 12/17 vs 3/15 p=0.0060; 6/12 vs 1/14 p=0.026; 7/18 vs 2/10 p=0.417.

**False statement: "at variant level counting sustained effect only the authors report P = 0.0698, not significant".** The
Results (section 3.5, last paragraph) attach P = .0698 to a different question: whether a 9 Å distance from the memantine binding site separates the GoF
individuals who benefited from those who did not. It is the **individual-level** analysis (redundant variants counted
separately; initial effect and no effect counted as negative; 7 true positives, 7 true negatives, 3 false negatives, 2 false positives; I recompute Fisher p = 0.0698).
The **variant-level** analysis (any positive effect for a residue; 7/5/2/0) gives p = .0210, which the authors call significant (I recompute 0.0210). Neither
test concerns GoF vs other variants or the 10-sustained-of-19 count. If the repository wants a sustained-only GoF-vs-comparator test, my own
calculation (not the authors') is 10/19 vs 3/15, Fisher p = 0.079.

Suggested replacement: "(the authors' P = 0.0698 refers to a 9 Å distance-to-binding-site classification among the 19 GoF individuals,
individual level, initial effect counted as negative; at variant level P = 0.0210; GoF vs the 15-person comparator group 14/19 vs 3/15, P = 0.0049)".

Also: "three gain-of-function individuals worsened" is specifically increased seizure frequency (#10 after 4 days, #25 after about 3 months, #32 over 18 months); other
domains are not reported as worse. Add dose and exposure: standard 0.5 mg/kg/day (range 0.11-4 mg/kg/day, S2), treatment 4 days to 22 months (mean about 7 months), median age 9 years;
duration was not specified for 7 individuals; concomitant antiseizure drugs listed for most (S2). Rating is subjective, from clinicians and parents, no blinding, no control group (Methods; Limitations).

**CHECK CLASS: CHECK PRESENT BUT NOT MATCHED.** The variant's functional effect was measured directly in this paper
(Xenopus laevis oocytes, two-electrode voltage clamp, six functional parameters plus memantine IC50; S1 methods; Table 1 IC50 values with n), but in a
heterologous system, not in the patients, and for part of the variants the values are reproduced from earlier publications (Table 1 "Functional data source"). No
memantine level, adherence or target effect was measured in the patients. In-study check: **no** for the patient-level drug exposure; **yes** (oocytes, Table 1, Figure 1, S1) for the
variant function. other effect of the same manipulation: **yes** (clinical improvements in 14 of 19).

---

## DR-W2-003 (memantine, comparator group, Karnstedt 2026)

**VERDICT: MUST CHANGE.**

Verified: 3 of 15 improved (S2: #9, #15, #23; all recorded as "mild positive" and parent- or family-reported; #23 is reported by "parents and
kindergarden", so "parent-reported only" is slightly narrow); seizure reduction 2 of 10 vs 7 of 18 in GoF, p = 0.417 (I recompute 0.417); the authors also state the
seizure difference "did not reach significance".

**Wrong count: "group of 15 includes 4 non-pathogenic variants".** Results 3.1: "Five nonpathogenic variants were classified as variants of
unknown significance (#8, #19, #29, #31) or likely benign (#28)". All five are in the 15-person comparator group (S2 sheet; Table 1). The count is five (four VUS, one likely benign).
(The Results also say #19 was "excluded from further genotype-phenotype analyses", although the 3/15 and 2/10 denominators still appear to include it; NOT RESOLVED by the paper.)

**Missing and important: both seizure reductions come from non-pathogenic-variant carriers.** The comparator carriers with epilepsy are #8, #12, #15, #16, #17, #19, #23, #28, #29, #31 (10).
Only #28 (seizure-free for 10 months except one episode; variant likely benign, not functionally tested) and #29 (3-4 seizures a day to one per 3 months; VUS, not tested) improved, and
the authors recorded both as "no effect" in the Conclusion row. None of the 5 pathogenic LoF/indeterminate carriers with epilepsy (#12, #15, #16, #17, #23) had a seizure reduction
(my calculation, 0/5 vs GoF 7/18, Fisher p = 0.27, not a test the authors made). The paper itself says (Results 3.4, paragraph after the epilepsy counts): "two had reduced seizure frequency or even became seizure-free after memantine treatment" about the five VUS/likely benign individuals. So "seizure reduction 2 of 10 ... not different from GoF" would mislead a reader into thinking LoF carriers had seizure responses.

Also: "The direction of the receptor lesion, not the presence of an NMDAR gene, separated responders" is the authors' retrospective, unblinded reading; the
GoF group's "benefit" includes 4 faded effects; strict LoF carriers (likely or possibly LoF: #2, #9, #12, #15, #16, #17, #19, #30) had 2 mild responders (#9, #15) of 8 (my count).

Suggested replacement of the clause in parentheses and the seizure sentence: "(the 15 include 5 variants the authors call nonpathogenic: four VUS and one likely benign)" and "seizure reduction 2 of 10, both in carriers of untested nonpathogenic-classified variants (#28 likely benign, #29 VUS) whom the authors rated 'no effect'; none in the 5 pathogenic LoF or indeterminate carriers with epilepsy".

**CHECK CLASS: CHECK PRESENT BUT NOT MATCHED.** Variant function: memantine IC50 measured for 8 of 15 (n.a. for #2, #8, #17, #28, #29, #30, #31); functional category for 4 of the 15 rests on none (#8 null by frameshift, #28, #29, #31 "not tested"); oocytes not patients; no
drug level or target effect in patients. In-study check: **no** for drug exposure; **yes** (oocytes) for variant function in part. other effect of the same manipulation: **yes** (GoF improvements, same paper).

---

## DR-W2-007 (perampanel among seven drugs, Teplyshova 2024)

**VERDICT: ADD.**

Verified (article, Case report, "History of epilepsy"): "Various antiseizure medications have been prescribed: phenobarbital, valproic acid, carbamazepine,
topiramate, levetiracetam, ethosuximide, and perampanel. No sustained positive effect of treatment was detected." Seven drugs. One adult (40 years old, follow-up more than 40 years; homozygous WWOX p.Thr12Met, "likely pathogenic").

Needed additions:

1. "exposure and timing are unknown" is too strong. The paper gives the current regimen "in recent years": valproic acid 1,000 mg/day, levetiracetam 2,000 mg/day,
   **perampanel 6 mg/day**, and says seizure frequency "has remained extremely high throughout the disease course, reaching 10-30 paroxysms daily". Start dates, durations, doses of the other four drugs
   and any per-drug response are not given. Replacement: "perampanel is currently taken at 6 mg/day together with valproate and levetiracetam; start age and duration are not given".
2. The authors' word is "sustained": transient responses are not excluded and the paper does not report any.
3. Exposure was not verified by drug level or adherence (no serum level, plasma or concentration hit in the text).

**CHECK CLASS: CHECK ABSENT.** No drug level, no target effect, and no functional measurement of the p.Thr12Met variant (only in-silico predictors, CADD 31, ACMG PM2, PM5, PP3, PP4). Query: regex search of the held article text
on 2026-11-25 for serum level, plasma, concentration, blood level, trough, drug level, in vitro, western, functional stud: zero hits for each. In-study check: **no**. other effect of the same manipulation: **no** (no per-drug
response is reported; Figures 1-3 are a photograph and two EEGs at age 36). Figure files were held (3 jpgs); I only checked their size and captions.

---

## DR-K01-006 (HIF-1alpha raising or lowering and seizures)

**VERDICT: ADD** for the one held source. For three of the four PMIDs the source bytes are missing (24889205, 36655171, 42276303), so the DMOG/KC7F2, HIF-1alpha-overexpression/CaV3.2 and
activity-LDHA-AMPK statements are **NOT ASSESSABLE / NOT CHECKED**.

What the held full text (PMID 34021541, Pan 2021, Aging) shows:

- "lowering HIF-1alpha, HDAC5 and PFKFB3 together accompanied fewer seizures": correct as "accompanied", but the manipulation was **miR-485 agomir** (lentiviral, hippocampal injection two weeks before lithium-pilocarpine), which lowered HDAC5, HIF1α and PFKFB3 protein together (Results, "miR-485 inhibits epilepsy through HDAC5/HIF1α/PFKFB3 axis in vivo", Figure 5A, text only; the figure image is not held). HIF1α was never lowered on its own for the in vivo seizure score. The causal evidence is the reverse experiment: overexpression of HDAC5, HIF1α or PFKFB3 on top of the agomir restored seizure grades (Table 2, n = 10 per group, Racine grade counts grade 0-V:
  agomir + oe-NC 0,6,4,0,0,0; + oe-HDAC5 0,0,0,3,2,5; + oe-HIF1α 0,0,0,2,2,6; + oe-PFKFB3 0,0,0,1,1,8; epilepsy + agomir-NC + oe-NC 0,0,0,1,1,8). All Table 2 rows sum to 10.
- Species: ICR **mice** (Methods; male, 6 weeks, n = 90, nine groups of 10). The Abstract calls it "a rat model", which contradicts the Methods; the repository should say mouse.
- Table 1 (epilepsy + miR-485 agomir, grades 0-V: 6,3,1,0,0,0) and Table 2 (epilepsy + agomir + oe-NC: 0,6,4,0,0,0) give different grade distributions for the same treatment; they are different groups of 10 mice (nine groups in Methods).
- Cell model: hippocampal neurons in magnesium-free medium, "Experiments were repeated three times".
- Sentence says the row is "abstract level" for 34021541; full text is now held, so that tag is out of date for this paper.
- CaV3.2 and "no WWOX to CACNA link": not in this paper, NOT CHECKED.

**CHECK CLASS (for the held paper only): CHECK PRESENT.** In-study check: **yes** for 34021541 (Results text for Figure 5A: agomir lowered HDAC5, HIF1α and PFKFB3 in mouse brain; Figure 2C-D: sh-HDAC5 efficiency and HDAC5 protein; Figure 3C: HIF1α overexpression raised HIF1α protein with sh-HDAC5 in cells; Figure images not held, text only).
For the other three PMIDs: NOT ASSESSABLE (no bytes). other effect of the same manipulation: **yes** (apoptosis, SOD, GSH-Px, MDA, 8-OHdG, cytokines; Figures 1-5).

---

## Summary table

| id | class | in-study check | other effect of same manipulation | verdict |
|---|---|---|---|---|
| DA-I01-002 | CHECK PRESENT (progenitor protein, Western); neurons PRESENT BUT NOT MATCHED | yes, Data_Sheet_1 Suppl Fig 1 (progenitors only; CAGE WWOX transcript not lower in progenitors) | yes (redox potential, adhesion, 2,282 DEGs) | MUST CHANGE |
| DA-K01-005 | CHECK PRESENT | yes, Fig 6a, Fig 1 | yes | ADD |
| DA-K01-006 | CHECK PRESENT in 3 of 4 conditions (NN nuclear WWOX not lowered) | yes, Fig 6b | yes | ADD |
| DA-I01-004 | CHECK PRESENT (HH inconsistent across assays) | yes, Figs 1, 4a, 6, 8c | yes | ADD |
| DR-W2-002 | CHECK PRESENT BUT NOT MATCHED | patient drug exposure: no; variant function (oocytes): yes, Table 1, Fig 1, S1 | yes (14/19 improved) | MUST CHANGE |
| DR-W2-003 | CHECK PRESENT BUT NOT MATCHED | drug exposure: no; variant function: partial (IC50 for 8/15) | yes | MUST CHANGE |
| DR-W2-007 | CHECK ABSENT (2026-11-25, regex on held article) | no | no | ADD |
| DR-K01-006 | held paper CHECK PRESENT; other 3 PMIDs NOT ASSESSABLE | yes for 34021541 (text, figures not held) | yes | ADD |

One-line reasons:

- DA-I01-002 (MUST CHANGE): "interval spans zero" is false for -0.67 ± 0.45 (excludes zero), "sign not concordant" holds only after median re-centring (library-size log2 shifts are -0.54 and -1.07, both negative), and -0.67 / +0.44 / p 0.49 are not reproducible from the deposit.
- DA-K01-005 (ADD): fraction time is 6 h in Methods but 48 h in the Figure 6 caption; total HIF1α by immunofluorescence goes up in NN and NH; the NN bracket shows one star vs "p<0.01"; "MEF increase is nuclear" is not in any held file; n unstated.
- DA-K01-006 (ADD): nuclear WWOX was not lowered in NN; nuclear HIF1α NN mean is 5.4-fold with SEM about 3.8; total-protein (immunofluorescence) increase omitted from "what survives"; 6 h vs 48 h.
- DA-I01-004 (ADD): "HK, LDH, lactate higher" holds only in some conditions (HK NN, HN; LDH NN, NH; lactate all four); PDH SEMs are wide; WWOX not lowered in HH by mRNA or immunofluorescence; WWOX overexpression lowers PDH, so the assay can move.
- DR-W2-002 (MUST CHANGE): P = 0.0698 belongs to the 9 Å distance classification (individual level), not to GoF sustained-effect counting; variant-level P is 0.0210; "worsened" means increased seizure frequency.
- DR-W2-003 (MUST CHANGE): the paper counts five nonpathogenic variants (four VUS, one likely benign), not four; both seizure reductions (2 of 10) come from the untested nonpathogenic carriers #28 and #29, none from pathogenic LoF or indeterminate carriers.
- DR-W2-007 (ADD): the paper gives the current regimen (perampanel 6 mg/day with valproate 1,000 and levetiracetam 2,000 mg/day, seizures 10-30 per day), so "exposure unknown" is too strong; the authors' qualifier is "sustained", so transient benefit is not excluded.
- DR-K01-006 (ADD): only one of four PMIDs is held; for it, the manipulation was a miR-485 agomir in ICR mice (the Abstract's "rat" is wrong), HIF1α was not lowered alone in vivo, and the sentence's "abstract level" tag is out of date; the other three PMIDs' statements are NOT CHECKED.

## Files opened

Input: `/home/desktop/.claude/jobs/ae0002e7/tmp/adv282/blind3/BLIND_SENTENCES_ADV282_INC3_SCI_20261125.md`

Held sources (all under `/home/desktop/legend-development/files/`):
- `geo/GSE126075/`: `gse126075_soft_full.txt`, `GSM3590948.txt` to `GSM3590951.txt`, `GSE126075_TPMexpression_all_genes_all_samples_merged.txt.gz`, `GSE126075_TSScoordinates_TPMexpression_all_samples_F5mapped.txt.gz`, `bed_streamed_tagcounts_and_sha256.tsv`
- `fulltext/PMID31543760_Kosla2019_PMC.xml` (the EPMC copy has the same byte size; not opened separately)
- `fulltext/PMID31543760_assets/`: `Data_Sheet_1.pdf` (rendered page 1) and `Data_Sheet_1_pdftotext.txt`; directory listing of the rest, `Data_Sheet_2/4_pdftotext.txt` first lines only (gene lists); `Data_Sheet_3.pdf` not opened
- `figures/PMID31543760/`: not opened (listing only)
- `fulltext/PMID35328751_Baryla2022_PMC.xml`
- `figures/PMID35328751/`: `ijms-23-03326-g001.jpg`, `g004.jpg` (top panels), `g005.jpg`, `g006.jpg`, `g008.jpg`
- `fulltext/PMID35328751_assets/s001/Supplementary_figures_captions_pdftotext.txt`; the .tif supplementary figures and the zip were not opened
- `fulltext/PMID41489401_Karnstedt2026_Epilepsia_PMC13075606.xml`, `..._supp_S1_functional.docx` (text of the methods read; the S1 tables were not read in full), `..._supp_S2_clinical.xlsx` (whole sheet, all 34 columns)
- `fulltext/PMID39507621_Teplyshova2024_PMC_r2.xml`; `PMID39507621_Teplyshova2024_assets/` listing and image sizes only
- `fulltext/PMID34021541_ADV272_PMC8202868_epmc_20261125.xml`

Not opened or not available: PMIDs 24889205, 36655171, 42276303 (not held). Figure images for 34021541 (not held).
