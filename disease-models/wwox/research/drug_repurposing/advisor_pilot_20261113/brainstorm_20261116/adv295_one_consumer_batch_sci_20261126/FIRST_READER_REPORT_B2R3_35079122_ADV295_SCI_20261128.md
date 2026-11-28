# ADV-295 block 2, record 3 (PMID 35079122): first reader report, verbatim

Subagent hand-back saved verbatim by SCI on 2026-11-28 (legend-delegate, claude-sonnet-5-5, effort high read back from the transcript). Model output, hypothesis level, not medical advice; not edited.

**Incomplete, read before use.** The hand-back ends inside its last list of source files. The delegate afterwards tried to say that its response had been stopped by a safety classifier while the hand-back was running, and that the reading should be treated as missing unless a complete report had arrived. Sections 1 to 5 are present; the tail of the source list is not. SCI did not ask for the content again and did not re-run the reader. The strict count of this record does not depend on this report (it has no WRONG, and the blind reader returned no MUST CHANGE).

---

FIRST READER, Record 8 (DL-MECH-170), PMID 35079122. Read 2026-11-28. Hypothesis-level reading of public literature; not medical advice.

Header flag: the first author is **El Khoueiry**, not Cabungcal (Cabungcal is second). The authors are El Khoueiry, Cabungcal, Rovó, Fournier, Do and Steullet, Mol Psychiatry, published 2022. The held file names and the "Record 8" heading say "Cabungcal 2022". The consumer sentence itself cites only the PMID.

**Bottom line:** no strict candidate. The "decrease" is the paper's own result and its direction is right. It needs age, model, region and evidence level. The "lesion-specific in sign" clause cannot be judged from this paper alone.

## 1. Statements

| id | verbatim | verdict | grounds (quote and locator) |
|---|---|---|---|
| R8-S01 | "The T-type change" | ADD | The measure is whole-cell, ex vivo T-Ca2+ current density in mouse thalamic reticular nucleus (TRN) neurons. Supplement, Patch-clamp: "most recorded TRN neurons were presumably PV neurons". CaV3.3 immunolabel was measured only in adults (Fig 1M-O). |
| R8-S02 | "is lesion-specific in sign" | NOT ASSESSABLE | It needs PMID 40834072. This paper compares no pair of insults with opposite sign. Its own claim is convergence: "a common, convergent mechanism" (Introduction, last paragraph; Discussion, first paragraph). It never mentions Cntnap2. |
| R8-S03 | "[lesion-specific in] ... age" | ADD | Gclm-KO alone: no difference at PND20-30 (Fig 2C, D), decrease at PND60-75 (Fig 1B, G). With a PND10-20 challenge, or after prenatal MAM, the decrease is already present at PND20-30 (Fig 2D, Fig 4H). So onset age depends on the model. The parenthesis gives no age. The adult and young comparisons also used different slice preparations (see section 4). |
| R8-S04 | "lesion" (covering oxidative stress) | ADD | No lesion is applied. The perturbations are a germline Gclm knockout, GBR-12909 or BSO+GBR-12909 injections at PND10-20, and prenatal MAM. Search "lesion": 0 hits. |
| R8-S05 | "an increase in Cntnap2, PMID 40834072" | NOT ASSESSABLE | That paper is not held for this task and was not opened. To carry the contrast it needs: a direct T-type current measurement (not inferred from burst firing or from a blocker's effect), the cell type and region (TRN or not), species and age, the direction with n and test, and ideally data at both an early and a late age. If the region or cell type differs from TRN, the sign difference cannot be assigned to the "lesion". |
| R8-S06 | "a decrease" | ADD | Direction is correct: "we found a reduction of T-Ca2+ current density in adulthood, but not at peripuberty" (Abstract). Region, species, ages, size and evidence level are missing. |
| R8-S07 | "under developmental oxidative stress" | ADD | This is the paper's title framing, but oxidative stress alone is not sufficient at peripuberty. Discussion: "In peripubertal Gclm-KO mice however, both T-Ca2+ and SK currents are not affected despite the presence of OxS" (that OxS is cited from earlier work, not measured here). Causal support is NAC rescue in GBR-treated KO only. MAM shows co-occurrence: "we did not assess the effect of NAC on T-Ca2+ currents in MAM mice". Oxidative stress in adult KO was not measured in this paper (only PND40 histology panels exist, Figs 3A-B and 4A-B). |
| R8-S08 | "PMID 35079122" as source of the decrease | CORRECT | Figs 1, 2 and 4 report it. |

## 2. Corrected sentences (no WRONG; one per ADD)

- **S01:** "The T-type current density measured ex vivo in mouse TRN neurons (presumably mostly PV neurons) ..."
- **S03:** "... in Gclm-KO mice the decrease is seen at PND60-75 but not at PND20-30; after an added PND10-20 challenge or prenatal MAM it is already present at PND20-30."
- **S04:** "... insult- or model-specific (genetic redox deficit, early-life pharmacological challenge, prenatal MAM), not a tissue lesion."
- **S06:** "... lower T-type current density (by eye about 30% in adult KO and 50-60% in the young challenged or MAM groups, at the most hyperpolarized potentials; cell-level statistics)."
- **S07:** "... a decrease in mouse models combining or accompanying developmental oxidative stress; oxidative stress in the constitutive KO alone had not produced it by PND20-30."
- **Whole sentence:** "Whether the T-type change depends on the type of insult, in sign or age, is a cross-study hypothesis: PMID 35079122 finds lower T-type current density in mouse TRN neurons (Gclm-KO at PND60-75 but not PND20-30; at PND20-30 only after a PND10-20 GBR-12909 challenge in Gclm-KO, BSO plus GBR-12909 in WT, or prenatal MAM), to be set against an increase reported for Cntnap2 (PMID 40834072, not checked here)."

## 3. Strict candidates (WRONG as written)

None. The one borderline is the opening generalisation (S02). It depends on the unheld paper and on whether the two studies measured the same quantity in the same cells, so I did not call it WRONG.

## Record facts (explicit checks)

**Models, sex, age**
- Gclm-KO was backcrossed to C57BL/6J for more than 10 generations. WT mice came from WT x WT breeding.
- GBR-12909 5 mg/kg, PND10-20: daily in KO, every other day in WT. Those WT also got BSO 3.8 mmol/kg s.c. daily.
- MAM 25 mg/kg i.p. into C57BL/6JRj dams at gestational day 16; controls were to get NaCl.
- NAC 2.4 g/L in drinking water, PND2 to sacrifice, in GBR-treated KO.
- Electrophysiology used both sexes at PND20-30 or PND60-75. Immunohistochemistry used males only. No sex analysis is reported (search "sex": 0).

**Measurement**
- T current was isolated by a voltage protocol in TTX 1 µM plus apamin 100 nM (an SK blocker), at about 25 °C.
- No T-type blocker was used, so T-type identity rests on the protocol. Searches for named blockers all returned 0.
- Channel protein was measured by immunolabel voxel counts. No transcript data (searches "mRNA", "PCR", "transcript": 0).

**Adult Gclm-KO, firing (Fig 1)**
- Fig 1A: bursting at resting potential in 3/12 KO vs 10/13 WT neurons, Fisher p=0.02 (I recompute 0.017).
- Fig 1C-D: single-burst threshold -69.3 ± 2.2 mV (KO) vs -64.9 ± 1.9 (WT); no p or asterisk.
- Fig 1E-F: repetitive-burst threshold -82.5 ± 4.3 vs -69.2 ± 2.3 mV, p=0.02. Legend n: KO 6, WT 8.

**Adult Gclm-KO, currents and channels**
- Fig 1B (current at resting potential): means by eye -1.82 (WT) vs -1.10 (KO) pA/pF, about 40% lower. p=0.034, **one-tailed** t-test.
- Fig 1G: F=31.92, DFn 1, DFd 289, p<0.0001; WT 9 and KO 10 cells. At -110 mV, by eye, about -3.75 vs -2.65. No per-voltage post-hoc asterisk (checked on an enlarged crop).
- Fig 1H (SK current): F=36.34, same n; asterisk at -110 mV.
- Fig 1K-L: CaV3.2 not different, n=5 per genotype (KO numerically higher, by eye about 25 vs 19 x10^3).
- Fig 1N-O: CaV3.3 lower, n=4 per genotype, by eye about 35 vs 83 x10^3. By region: anterior ***, medial *, posterior not marked.

**Young mice (Fig 2)**
- Fig 2A-B: burst thresholds not significantly different. n: WT 11, KO 12, KO-GBR 10, BSO-GBR 11.
- Fig 2C (current at resting potential): Kruskal-Wallis **p=0.062**, not significant. n: 24, 19, 9, 9.
- Fig 2D: F=36.98, DFn 3, DFd 1029; n not stated. Post-hoc marks at about -90 to -110 mV for both challenged groups. By eye at -110: WT and KO about -7, KO-GBR about -3.5, BSO-GBR about -3.7.
- Fig 2F: SK current also lower; Fig 2E: correlation maintained.

**NAC and GSH (Fig 3)**
- NAC lowered 8-oxo-dG and raised PV and PNN counts (A-D, 5 mice per group). Burst thresholds unchanged (E-F).
- Fig 3G: current at resting potential in NAC group **higher** than WT (p=0.026) and than KO-GBR (p=0.012). Legend n: WT 24, KO-GBR 7, NAC 12.
- Fig 3H: maximal current restored, with a depolarized shift of inactivation (F=60.96). Fig 3I-J: SK current parallels it.
- Fig 3K-M: 100 µM GSH for 5 min raised current, significantly at -70 mV and above in KO-GBR, not in WT.
- So treated conditions show an increase relative to WT at depolarized potentials.

**MAM (Fig 4)**
- Fig 4A-D: more 8-oxo-dG and fewer PV and PNN+PV cells, 4 mice per group.
- Fig 4E-F: threshold trend only; MAM n=13, WT 11.
- Fig 4G: current at resting potential not significant; MAM 12, WT 24.
- Fig 4H: F=73.63, DFd 578; by eye about -2.9 vs -7.0 at -110. Fig 4I: SK current lower, F=61.58. Fig 4J: correlation maintained.

**Does the paper claim a decrease, and sign or age specificity?** It claims a decrease or "hypofunction" throughout. It speaks to age of onset ("emerges later during late adolescence/early adulthood" in Gclm-KO). It makes no claim of sign specificity.

## 4. Additions that matter and are not in the sentence

I opened no other consumer text, so I cannot say whether any consumer holds these.

1. **Fig 1B n disagrees with its legend.** The legend says KO n=11, WT n=10. By eye the plot has **11 WT and 9 KO** points. A t-test on my eye-read points gives t=1.93, df=18, one-tailed p=0.035 (reported 0.034) and **two-tailed p about 0.069**.
2. **Replicates are cells.** No animal numbers are given for electrophysiology. The two-way ANOVA treats each cell-by-voltage value as independent: DFd 289 = 19 cells x 17 voltages - 34, and DFd 578 = 36 x 17 - 34. No repeated-measures term is evident.
3. **The age contrast is confounded by preparation** (supplement, Slice preparation). Young: sucrose solution, horizontal slices. Adult: NMDG solution with ascorbate, pyruvate and L-cysteine, coronal slices. Those are redox-active additives in a redox study. Maximal WT current is about -7 pA/pF young vs -3.75 adult (by eye).
4. **The MAM electrophysiology control looks like the Gclm WT group** (by eye). Fig 4G "control WT n=24" has the same point pattern as Fig 2C WT, and the Fig 4E-F and 4H WT values match Figs 2 and 3. If so, it is not the NaCl-exposed offspring.
5. **Missing controls.** I found no vehicle-injected WT, GBR-alone WT or BSO-alone arm; the only vehicle described is MAM's NaCl.
6. **Proportion error.** The text says WT bursting "71.4%, 10/13", but 10/13 is 76.9%. 71.4% would be 10/14, which gives p=0.047.
7. **GBR route.** Text and supplement say i.p.; the Fig 2G drawing says s.c.
8. **Histology age.** Fig 3 and 4 legends say PND40; the Results text describes the MAM histology as peripubertal PND20-30.
9. **No randomization;** the experimenter knew genotype or treatment during recording, and analysis was blind (supplement).

## 5. What I opened, limits, disk

**Opened**
- The article XML, converted to text and read in full (reference list excluded).
- All 4 main figure jpgs, viewed, with enlarged crops of the dot plots and Fig 1G-H.
- The supplement docx: my clean paragraph extraction, read in full (45 paragraphs: methods and 6 references; 0 tables, 0 drawings, no media). There are no supplementary figures or tables.
- The held supplement .txt: only lines 1-251, which are bloated with EndNote code. The docx extraction replaces it.
- The PMC PDF: it is the 10-page article itself, with 4 embedded images. I extracted text and images but did not read it page by page or render pages.
- The "Record 8" section and the "Matching rule" section.

**Searches for negatives**
- Date 2026-11-28. Files: my text conversion of `PMID35079122_Cabungcal2022_PMC_r2.xml` and of `41380_2021_1425_MOESM1_ESM.docx`. Method: `grep -o -i -F -- "<keyword>"`, one keyword per search.
- 0 hits in both files: Cntnap, Wwox, lesion, mibefradil, TTA-P2, TTA-A2, NNC, ethosuximide, Z944, Z-944, nickel, Ni2+, CaV3.1, Cacna1g, mRNA, PCR, Western, transcript, sex, litter, seizure, epilep.
- "blocker": 1 hit, supplement (apamin). "vehicle": 1 hit, supplement (MAM NaCl).

**Not done:** PMID 40834072 not opened. PMID 42422765 not touched. No other repository file opened or searched.

**Failures:** PIL is not installed, so I used ImageMagick. One CMYK crop converted badly and was redone from the held jpg.

**Disk:** about 3.4 MB of scratch plus 3 KB of scripts under `/home/desktop/.claude/jobs/fc428159/tmp/`, both directories **deleted**. Free space was 2.6 GB before and 2.5 GB after (shared machine), never near 1.0 GB. Nothing downloaded, nothing written in the repository.

Sources, under `/home/desktop/legend-development/files/`:
-
