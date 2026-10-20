# COMMIT CANDIDATE — CC-20261019-SCIENTIST-B-H3-EPINEPHRINE-SAFETY-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist-b`, interventions batch 2026-10-19 group H3, branch `task/INTERV-H3-B-20261019`.
**context_policy:** `SOURCE_FIRST` for every reading cited (first reads); registry comparison admitted after each first pass.
**target_wm_version:** `WM_v7.20_2026-10-04`. **Change class:** **MINOR** — new paper-registry records and evidence-boundary notes; no claim status, no baseline claim reversed, no working-model block change. The legend-locator-audit trigger is not met; the triples below are supplied for a later blind audit.
**Not medical advice. Class level only. BLOCK-1 caution: nothing here is a dosing or treatment statement.**
**WWOX evidence on epinephrine as an agent, its effects on lactate, mitochondria or neurological outcome: none.** Every item below is a substitute, labelled NOT WWOX evidence.

## Target

No existing claim is edited. Proposed: five new paper-registry records (ESPANSIONE, background) and two discovery leads.

## What is missing now

The registry holds nothing on epinephrine as an intervention. The selection asked whether epinephrine affects neurological outcome, lactate and the oxidative-stress arm. The readings give class-level answers only, none involving WWOX.

| Source | What it adds | Receipt |
|---|---|---|
| Williams 2024 review (39597089) | adult cardiac arrest: epinephrine raises return of circulation (OR about 3.4 against placebo) but not neurological outcome; number needed to treat 112; stated inclusion rules do not match the tabulated designs; a Japanese observational study is called placebo-controlled | `FTR-20261019-39597089-01` |
| Idrees 2026 protocol (42260675) | paediatric (1 day to under 18 years) stepped-wedge protocol of intramuscular epinephrine at up to 10 times the IV dose; primary outcome time to return of circulation among those who achieve it; no stopping rules; 3 intervention patients of 139 recruited at the stated date | `FTR-20261019-42260675-01` |
| Oulehri 2024 rat study (38542290) | in anaphylactic shock epinephrine restored pressure and survival but cardiac mitochondrial respiration stayed 29 to 40 percent below control and lactate 4.8 against 0.9 mmol/L; no epinephrine-alone or time-matched shock control, so the attribution to epinephrine is untestable; shortening fraction saturates at 100 percent | `FTR-20261019-38542290-01` |
| Zhang 2024 cell study (39000139) | 3 days of 100 nM epinephrine on MIN6 cells: higher glucose-stimulated secretion and ER-stress transcripts after washout; no ROS probe or apoptosis assay although both are concluded; desensitisation from mRNA only | `FTR-20261019-39000139-01` |
| Dhillon 2026 (41885587) | alpha blockade after hypoxia-ischaemia in the fetal sheep lowered lactate and glucose; seizures unchanged (also in the adrenergic candidate) | `FTR-20261019-41885587-01` |

## Proposed paper-registry records

One per source, Note: "no WWOX content; class-level epinephrine or adrenergic context; see commit candidate". Receipts first.

## Proposed discovery leads

1. **A short-term resuscitation or metabolic surrogate (return of circulation, lactate, shortening fraction) can move without the outcome that matters** (Williams 2024, Oulehri 2024, Idrees 2026 primary outcome); any adrenergic hypothesis for WWOX must name its patient-relevant outcome first (INFERENZA).
2. **Epinephrine design rule:** an epinephrine arm needs an epinephrine-alone control and a time-matched disease-only control before a respiratory or lactate change is read as a drug effect (Oulehri 2024; INFERENZA).

## Ordering

Receipts for the five PMIDs above must be in the ledger first.

### LOCATOR TRIPLES FOR BLIND AUDIT

| PMID | entry | proposition | verbatim snippet | anchor |
|---|---|---|---|---|
| 39597089 | entry 3 | EFFICACY, the placebo trial: return of spontaneous circulation 3.4 times more likely with epinephrine, no significant difference in neurological outcome or discharge survival. | found that the likelihood of achieving ROSC in patients who received epinephrine was 3.4 times greater than for those who received the placebo [8] | 3.1 Efficacy and Long-Term Outcomes, paragraph 3 |
| 39597089 | entry 4 | MISLABEL: the prospective Japanese study (nonrandomised, propensity analysis per Table 1) is described as comparing epinephrine with placebo; no placebo existed, the comparator was no epinephrine, and the retrospective French coho | a nonrandomized prospective observational study conducted in Japan in 2012 also compared prehospital use of epinephrine to placebo in cardiac arrest | 3.1 Efficacy and Long-Term Outcomes, paragraph 3 |
| 39597089 | entry 9 | The number needed to treat to prevent one death at 30 days in the placebo trial is quoted as 112, larger than for bystander CPR or early defibrillation. | the number of patients needed to treat with epinephrine to prevent one death at 30 days from cardiac arrest was 112 | 5 Limitations |
| 42260675 | entry 3 | DOSE DOUBLING: the authors state the IM peak may coincide with the IV or IO dose, so a child could receive up to double the recommended dose at one time. | the patient could potentially receive up to double the recommended dose of epinephrine at one time | Discussion, paragraph 3 |
| 42260675 | entry 4 | SAFETY REASONING: the authors cite a trial of ten-fold epinephrine in paediatric in-hospital arrest as showing no benefit but a trend towards harm, then conclude from data on shorter dosing intervals that the risk of a double dose | These data suggest that there is minimal risk of harm associated with administering a double dose of epinephrine. | Discussion, paragraph 3, last sentence |
| 42260675 | entry 5 | The safety statement for the trial rests on anaphylaxis practice: no criteria for discontinuing, and no pre-defined stopping rules in the interim analyses. | There are no pre-defined stopping rules for this trial. | Interim analyses {21b} |
| 42260675 | entry 6 | PRIMARY OUTCOME: time to return of circulation analysed only in patients who achieve it (no censored data), described as an intermediate outcome strongly associated with survival; the adult review read in this batch shows return o | will include only patients who achieved ROSC (i.e., there will be no censored data) | Statistical methods {20a}, paragraph 2 |
| 38542290 | entry 2 | Epinephrine restored pressure and survival to 60 minutes but cardiac mitochondrial respiration stayed impaired: complexes I plus II minus 29 percent and complex II minus 40 percent against control at 60 minutes. | OXPHOS was significantly impaired in the AS+EPI groups as compared to the control group through complexes I+II (−29%, p < 0.05) and II (−40%, p < 0.001) at T60 min | 2.2.3 Cardiac Mitochondrial Respiration |
| 38542290 | entry 3 | ATTRIBUTION: the Discussion says epinephrine might itself provoke cardiomyocyte dysfunction including impaired respiration; the design cannot test it, because the shock-only group was sampled at 15 minutes (it died) and there is n | Epinephrine might even provoke cardiomyocyte dysfunction, including impaired mitochondrial respiration, which might participate in the epinephrine refractory cases of AS. | 3 Discussion, (1) Characterization of AS and effects of epinephrine alone |
| 38542290 | entry 4 | LACTATE: at 60 minutes arterial lactate was 4.8 mmol/L in the epinephrine-treated shock group against control and 3.6 with the adjuvant; no shock-only value at a matched time and no epinephrine-only value exist, and the article do | arterial lactatemia (Figure 7) was significantly higher in the AS+EPI and AS+EPI+preNBut groups as compared to the CON group (p < 0.0001) | 2.2.3 Cardiac Mitochondrial Respiration, last paragraph |
| 39000139 | entry 1 | NO ROS ASSAY: the Methods list kits for total antioxidant capacity, SOD, catalase, glutathione peroxidase and ATP; there is no ROS probe, yet the Discussion concludes that prolonged epinephrine leads to increased ROS production. | In conclusion, prolonged exposure to epinephrine leads to increased ROS production. | 3 Discussion, last paragraph |
| 39000139 | entry 3 | NO APOPTOSIS ASSAY: the Introduction says apoptosis was measured; the Methods contain no apoptosis assay, Bax was unchanged and Bcl2 fell by a third in the qPCR. | we measured insulin secretion, cell proliferation, and apoptosis in MIN6 cells | 1 Introduction, last paragraph |
| 39000139 | entry 4 | DESENSITISATION is inferred from the alpha2A receptor mRNA, which fell by 13 percent at day 3 and about 30 percent at day 5 (Figure 1B); no receptor protein, cAMP or signalling readout is reported. | Despite removal of epinephrine, α2A-AR RNA expression did not show reversible features (Figure 1B). | 2.1 Glucose Stimulated Insulin Responsiveness |
| 41885587 | entry 2 | GLUCOSE AND LACTATE: after the insult glucose and lactate were higher in saline-treated fetuses and recovered by 2 hours with phentolamine, a direct measurement of an alpha-adrenergic contribution to post-insult glycaemia and lact | Glucose and lactate concentrations were higher in the HI‐saline group than the sham‐HI group until 6 h post‐HI but recovered to baseline levels by 2 h in the HI‐phentolam | Results, Cardiovascular and biochemical parameters during HI |
| 41885587 | entry 8 | BIOMARKER CLAIM: a threshold one standard deviation above the baseline coefficient of variation, set in the primary group and applied by a blinded observer to a 10 plus 10 validation group, is reported as 90 percent sensitivity an | Applying this set threshold, in the validation dataset animals with severe HI were identified with 90% sensitivity and 80% specificity (Fig. 10). | Results, Viability of short BPV as a biomarker for severe HI |


---

## BATCH DISPOSITION

**Verdict:** PROPAGATED
**Batch:** `BATCH_20261019_003` · 2026-10-20 · ACTOR_ID `orchestrator` (stated assumption, batch integrator)
**Working model:** WM_v7.21 -> WM_v7.22 (MINOR)
**Class re-judged (§7):** MINOR
**Blind locator audit:** not run — no baseline claim is narrowed and no MAJOR contingency is declared; the candidate's locator triples are carried for a later audit.
**What landed:** `PAPER 316`, `PAPER 317`, `PAPER 318`, `PAPER 319` with their LIT records (the Dhillon record is `PAPER 314`, landed by the adrenergic candidate); leads `DL-MECH-139` and `DL-METH-125`. **Receipt identifiers named here so that the output-to-study check can match them:** PMID 39597089 (`FTR-20261019-39597089-01`, DOI 10.3390/medicina60111904); PMID 42260675 (`FTR-20261019-42260675-01`, DOI 10.1186/s13063-026-09776-3); PMID 38542290 (`FTR-20261019-38542290-01`, DOI 10.3390/ijms25063316); PMID 39000139 (`FTR-20261019-39000139-01`, DOI 10.3390/ijms25137029); PMID 41885587 (`FTR-20261019-41885587-01`, DOI 10.1113/JP290169); PMID 41584903 (`FTR-20261019-41584903-01`, DOI 10.1177/15357597261416723). The Wenker record (PMID 41584903, `FTR-20261019-41584903-01`) is `PAPER 321`, landed by the autonomic candidate.
**Status / Type / Summary:** unchanged by this candidate.
**Not medical advice.** Class level only; no individual-level record is carried.
