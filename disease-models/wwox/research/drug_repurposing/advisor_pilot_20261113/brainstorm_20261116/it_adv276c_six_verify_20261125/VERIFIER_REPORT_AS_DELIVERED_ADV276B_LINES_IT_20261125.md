<!-- IT blind verifier (legend-delegate; asked sonnet, effort high), 2026-11-25, registry lines of ADV-276b batch 1 (PMIDs 40500435, 24086726, 41007296). Delivered text, unchanged except that the job scratch path is written as <job scratch>. Statements: statements_adv276b_lines.md. Hypothesis level; not medical advice. -->

BLIND VERIFICATION REPORT (checked only against <job scratch>/v276b/src)

## Verdict table

| ID | Verdict | In one line |
|---|---|---|
| W1 | SUPPORTED for the high-fructose arms, but reword | As written it overshoots: Figure 3b also contains pups of control-diet dams, in both WT and knockout. |
| W2 | SUPPORTED | My independent readings agree. |
| W3 | SUPPORTED, within what I could see | No uninjected brain lactate appears in the text, legends or Figure 3. |
| S1 | SUPPORTED | The bound holds, but a tighter one exists for the genetic risk score (GRS) model. |
| S2 | SUPPORTED as printed | GRS rows use other n, and Table 1 conflicts with the glucose n. |
| S3 | SUPPORTED | The Power column is footnoted alpha = 0.05. |
| S4 | SUPPORTED | I get p = 0.957 for the printed effect and SE. |
| P1 | SUPPORTED from the main text | The forest plot itself was not available to me. |

## PMID 40500435 (mouse)

### W1
Locators (40500435.txt):
- Line 617 (Fig 3a legend): "Wildtype (WT) and Slc2a5–/– (KO) P7 mice born to and nursed by dams on control diet (CD) or high fructose (HF) diet, injected intraperitoneally with 4 g/kg [2-13C]-fructose".
- Line 53: "15 min prior to analysis (Fig. 3a)".
- Line 75: "Dams of each cohort (CD and HF) were placed on respective diets at least one week before mating and diets were maintained throughout gestation and lactation."
- Line 75: HF "contains 15 kcal% fructose".
- Line 94: "Brains were harvested and flash frozen in liquid nitrogen."

Suggested wording: "Figure 3b compares P7 pups born to and nursed by dams on control or 15 kcal% fructose diet (from at least one week before mating, through gestation and lactation); every group received 4 g/kg [2-13C]-fructose 15 min before analysis."

Qualifications:
- Intragastric fructose given to pups is a separate arm in the paper, not this experiment. So "not fructose given to the pups as a diet" is correct.
- "Whole-brain" is my and your reading of "Brains were harvested". The word "whole" is not used, and I found no perfusion described for this assay, so blood content is not excluded.
- "One injection" is implied; no repeat is described.
- The route is printed oddly: "injected intraperitoneally via the quadriceps" (line 94). A quadriceps injection would be intramuscular.
- Line 94 also gives "(20 mg in 200 μL PBS)", and Fig 3a shows "~20 mg". At 4 g/kg, 20 mg implies a 5 g pup.

### W2
Replicate unit: one dot per mouse (P7 pup). Legend, line 617: "N=4 WT CD, N=5 WT HF, N=5 KO CD, and N=5 KO HF. Data shown as mean±SEM."

My pixel readings of the WT means, in µmol/g:

| Measure | Control diet (n = 4) | High fructose (n = 5) | Ratio | Approx. error on means | Marker in figure |
|---|---|---|---|---|---|
| Total lactate pool (1H) | 4.3 | 10.7 | about 2.5 | ±0.15 | * |
| [2-13C]-lactate | 0.137 | 0.374 | about 2.7 | ±0.007 | ** |

Individual dots (approximate):
- Pool, control: about 3.6 to 5.2.
- Pool, high fructose: 4.8, 7.0, 11.9, 14.3, 15.4.
- Labelled, control: about 0.10 to 0.17.
- Labelled, high fructose: 0.24, 0.24, 0.36, 0.48, 0.55.

Qualifications that change the meaning:
- **Labelled share barely moves (my arithmetic).** It is about 3.2% of the pool on control diet and 3.5% on high fructose. The pool rises by about 6.4 µmol/g and the labelled species by about 0.24 µmol/g. The pool increase should therefore not be read as lactate made from the injected tracer.
- **Overlap and spread.** One high-fructose pup's pool value (about 4.8) lies inside the control range. The high-fructose spread is much larger than the control spread.
- **Test.** "two-way ANOVA with Tukey's post-hoc"; * is p<.05, ** is p<.01.
- **Units.** "Conc. (µmol/g)" is printed once, on the leftmost axis of panel b. Wet or dry weight is not stated.
- **Litters.** The legend does not say how many litters or dams the pups came from.
- **Knockout.** The Slc2a5-knockout high-fructose bars sit at about control level.

### W3
- Brain lactate in vivo appears at line 53 and line 617 (Fig 3b), and line 631 (Fig 5e: "[2-13C]-lactic acid in brains of WT and cKO P7 mice as in Fig. 3a").
- The Extended Data Fig 13 legend describes "Additional NMR measurements from the brains of WT and cKO mice corresponding to Fig. 5e". It includes labelled plasma lactate.
- All of these are injected animals. The other lactate data are from cultured microglia.
- Fig 5e is a second injected brain labelled-lactate dataset (WT CD n = 4, WT HF n = 6, cKO n = 8 and 8), so Fig 3b is not the only one.
- Not checked: the other figure images, Supplementary Information and Source Data, none of which I had. Phrase W3 as "none found in the text and legends".

## PMID 24086726 (Sakai 2013, human, Japanese; unit = participant)

### S1
- "We genotyped 7,379 Japanese participants (5,315 type 2 diabetes and 2,064 controls)". Methods says "We enrolled 5,315..." and "also recruited 2,064 controls".
- Table 3 footnote: "Adjusted for age, sex and log-transformed BMI".
- Table 1: BMI is available for "4,951/2,018", which sums to 6,969. No adjusted-model n is printed.
- The bound assumes complete-case analysis; no imputation is described.

Tighter bounds:
- Table 3: the GRS analysis used "Individuals who had complete genotype data for the 9 SNPs ... (n = 6,819)". The adjusted GRS model, which is the headline result, is therefore at most 6,819 and probably lower.
- Per-SNP models are also limited by genotype missingness. For rs17797882, Table 2 sums to 5,257 + 2,045 = 7,302 genotyped, before BMI loss.

### S2
- Methods and results say the trait analyses were done "using the control individuals".
- Table 4 header: "HOMA-IRb (n=893) HOMA-βb (n=893) FPGb (n=1,325)".

Qualifications:
- The GRS rows differ: "n= 844 for HOMA-IR and HOMA-β, n=1,181 for FPG".
- These are header n values; per-SNP genotype missingness is not reported.
- **Internal conflict.** Table 1 gives fasting glucose for only 1,320 controls ("2,249/1,320"), yet Table 4 and Table S4 say 1,325.

### S3
- Table S3 header: "Power b".
- Footnote b: "Power estimation was performed using CaTS power calculator ... The prevalence of type 2 diabetes is assumed to be 10%, α = 0.05".
- rs17797882 row: "WWOX C 0.792 1.08 42%".
- The main text ("between 42% and 79%") states no alpha.
- My rough allelic approximation gives about 39% at alpha 0.05 and about 14% at 0.0055. This agrees with the footnote.

Additional finding (my reconstruction, not stated by the source):
- The neighbouring "Sample size for 80% power" columns (66,327 / 110,247 / 334,649 for rs17797882) do not match the additive model in Methods.
- At alpha 0.05 they reproduce, within 9 cases, as numbers of cases under a **dominant** model with 1:1 controls. I tested four SNPs: rs9470794, rs7041847, rs17797882 and rs1535500.
- Do not pair 66,327 with the 42% power as if they came from the same model.

### S4
- Table 4 row (24086726.txt line 222 holds the rs17797882 entry): "0.0015 (0.028) 0.5941".
- 0.0015 / 0.028 = 0.054, so p is about 0.957.
- The other HOMA-IR and HOMA-β rows agree with their printed p within about 0.015. Fasting glucose rows differ more, as expected from 3-decimal rounding.
- An effect of about ±0.015 would give p of about 0.59, so a decimal or digit typo in the effect is the likely explanation. This is an inference: an SE of 0.0028 would also fit, although it is out of line with the other SEs.
- Not checked against the PDF (XML-derived text only).

## PMID 41007296 (human, basal-like breast cancer, TCGA; unit = patient)

### P1
Locators (41007296.txt):
- Line 62: "(n = 95, events = 11) (Supplementary Figure S1)".
- Line 62: "WWOX expression was also significantly associated with improved survival (HR = 1.014 per unit increase, 95% CI: 1.001–1.027, p = 0.034)."
- Line 48: "For each variable, HR > 1 indicated increased risk, and HR < 1 indicated a protective effect."

The contradiction is real by the paper's own convention. The CI and p are consistent with each other (I recompute p of about 0.033). The error is repeated in interpretation: line 63 calls clinical stage and WWOX the "strongest independent prognostic factors", and the Discussion repeats that they are independent factors.

Qualifications:
- **Descriptive result points the other way.** Line 59: "good prognosis tumours exhibited significantly higher WWOX expression (log2fc = 1.17)". The paper therefore has an unadjusted group comparison supporting its wording, while the adjusted coefficient points opposite. Do not conclude that "WWOX is harmful".
- **Conditional coefficient.** The model also contains the WWOX/HIF1A ratio and other genes, so WWOX's coefficient is conditional on them.
- **Fragile model.** There are 11 events for many covariates, and the ratio's HR is "≈ 1.18 × 10−13".
- **Unit unclear.** Line 46 says variables were "when required" log2-transformed and z-scored, so "per unit" has no stated scale.
- **Contrast within the paper.** Elsewhere the authors read HR > 1 for WWOX as "risk" ("HR = 1.003, p = 0.0596").
- **Not checked.** The word "row" refers to the Supplementary Figure S1 forest plot. The supplied supplement text has only its legend, no values. I also could not check how the event variable was coded; the stated aim is overall survival.

## Contradictions and limits
- No statement is contradicted by its source. The one wording problem is W1's "the values in Figure 3b come from ... high-fructose" pups.
- I had one figure image (40500435 Figure 3). I saw no PDFs, no other figures and no source data, and used no repository, registry or web.
- Figure values are pixel readings from an 800-pixel-wide JPG.

## Housekeeping
Scratch crops are in <job scratch>/v276b/out (b.png, lac.png, lb.png, pb.png, pool.png). I also wrote two small helper scripts (m.py, t.py) there, which went beyond "scratch images only"; I removed both before finishing. No contact with anyone and no spend.
