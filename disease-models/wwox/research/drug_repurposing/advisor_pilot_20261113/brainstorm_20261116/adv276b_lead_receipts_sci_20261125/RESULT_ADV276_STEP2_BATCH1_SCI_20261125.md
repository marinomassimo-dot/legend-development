# ADV-276 step 2, batch 1: ten acquired papers, ranks 26 to 55 (SCI, 2026-11-25)

Hypothesis level; reference genotype class; nothing here is medical advice. PREREG: `PREREG_ADV276_STEP2_BATCH1_SCI_20261125.md` (sha256 `c743cc06eaa718f263f07659bd4dd1a871360f3f001e207597e1e9a0112c6d6b`, committed before any paper was opened). One reader (claude-sonnet-5-5), then one blind delegate (section 4; the same model family, so blind to the analysis, not independent of the model). The exposure window (who was exposed, when, how long) is written beside every in vivo number.

## 1. Result per paper

| PMID | Consumer | Verdict | What the paper says, with window |
|---|---|---|---|
| 37907746 | `DL-MECH-124` (title: "... KHK to NOX4-ROS in activated **adult** microglia") | **change** | NOX4 mitochondrial translocation, fructose-driven ROS and the conditioned-medium result come only from **primary microglia of P1 to P3 pups** (about 6 to 7 days in vitro; 0.25 mM fructose) and BV2 cells (Supplementary Methods item 11). The adult evidence is a hippocampal AAV2/6 shRNA knockdown (CMV-driven, EGFP spread widely, no cell-type co-stain, so **not microglia-specific**) in male db/db mice (leptin-receptor-deficient diabetic), injected at week 20 and read at about 24 weeks (4 weeks of knockdown): whole-hippocampus lysates (n = 6), Iba1-colocalised NOX4 (30 cells from 4 to 5 mice), electron microscopy (n = 3). The paper compares neither neonatal and adult microglia nor KHK against hexokinase. |
| 25686832 | `DL-MECH-162` | **change (addition)** | "One mouse" matches Figure 5E, which shows one heterozygous Wwox mouse: tumour about 2,150 mm3 falling to about 200 mm3 over 50 days (never zero; six tail-vein injections of Zfra4-10, 2 mM in 100 µl, about days 2 to 78). The sentence omits that the text claims a **70 percent cure rate in ten mice** and the legend **75 percent** (incompatible with each other; no per-mouse data, no age or onset data in Methods), and that the curve does not reach zero. Still no untreated heterozygote curve; the Discussion concession about wild-type tumours stands. |
| 42171828 | `DL-MECH-122` | **change** | The review restates one primary (Yeh, Ou, Gean 2010, PMID 21029239, read today for the first time): male Sprague-Dawley rats (280 to 320 g, age not stated), **endothelin-1 cortical ischaemia (not filament occlusion)**, 2-methoxyestradiol **2.5 mg/kg intravenously, once**, at 0.5 h or 8 h (n = 4 per group in Figure 2). At 0.5 h: infarct, TUNEL, IgG leakage and brain water fell, NeuN rose, motor and neurological scores improved from day 8. At 8 h: infarct, IgG leakage and edema were **not reduced and no increase is reported**; NeuN fell, TUNEL rose, adhesive removal worse from day 4, swing and neurological scores worse from day 8. Survival is described without a test. 2-methoxyestradiol is not a selective HIF-1 inhibitor. The direction (protective early, harmful late) holds; "after middle-cerebral-artery occlusion" and "harmful" need the model and the readouts. |
| 35339181 | `DL-MECH-136` | **change (addition)** | Perspective article, preliminary data, one experiment: adult male Sprague-Dawley rats, 8 per group; salbutamol 10 nmol micro-infused into the left anterior piriform cortex (area tempestas) **5 min before** bicuculline 118 pmol (prevention, not treatment); seizures in 3 of 8 (onset prevented in 5 of 8) against 8 of 8 with bicuculline alone. "Most" stands; the abstract's "fully prevents" does not. Butoxamine 10 µmol worsened seizures. |
| 39505840 | `DL-MECH-136` | **change** | Male FVB/2J mice, 8 to 12 weeks, intrahippocampal kainate; **prazosin 6 + propranolol 6 + atipamezole 0.6 mg/kg intraperitoneally** from 5 min after kainate, then daily for 3 days (a three-drug cocktail). Acute (Table 1): mean convulsive-seizure duration 115 to 204 s (P < 0.001); seizure number 10.1 against 14.0 (P = 0.142, unchanged); phase 2 shorter. At 3 to 4 weeks (treated n = 7, vehicle n = 6): seizure number (P = 0.044), duration (P = 0.031) and maximum Racine score (P = 0.048) lower. **Mortality in the first 10 days was lower with the cocktail (n = 12 each, log-rank P = 0.003), so the later groups are survivors.** "Each" is too strong (means only). The Results text and Table 1 disagree on two vehicle values (seizure number 11.8 against 10.1; Racine 4.5 against 5.5). |
| 41007296 | `DL-MECH-117` | consumer passes; paper defect noted | Glioblastoma favourable group: WWOX log2 fold change +0.66, HIF1A -0.79, ratio +1.22; multivariable Cox in glioblastoma (n = 158, 106 events) ratio HR 56.1 (0.03 to 99,080), not independent. **Defect in the paper, not in the consumer:** in basal-like breast cancer (95 patients, 11 events, eight covariates) the text says WWOX is "associated with improved survival" while printing HR 1.014 per unit (1.001 to 1.027, p = 0.034), which by the paper's own convention (HR above 1 is higher hazard) is worse survival. The ratio is not significant there (p = 0.17). |
| 42260675 | `DL-MECH-139` | passes | A trial protocol (no results); the primary analysis includes only children who achieved return of spontaneous circulation, as the entry says. Time starts at paramedic arrival in one passage and at arrest in another. |
| 32142409, 32248813, 39546604 | `RP-033`, `RP-019`, `RP-033` | not re-read | Read under ADV-189, ADV-190 and the IT49 pick; only the species were re-checked today (mouse astrocytes; rat microglia; rat cortical neurons) and agree. No verdict from this reading. |

## 2. Scoring against the PREREG

| Prediction | Outcome |
|---|---|
| 1. Wording changes in 3 of 10 (range 1 to 5) | **5 of 10** (three corrections: 37907746, 42171828, 39505840; two additions of window and dose: 25686832, 35339181). At the top edge of the range, so the range holds and the point estimate of 3 missed. |
| 2. No direction reversed (90 percent) | Met. |
| 3. At least one change from a legend, Methods or supplement (75 percent) | Met (supplement Methods for 37907746; Figure 5E legend and curve for 25686832). |
| 4. At least one number without a stated window (70 percent) | Met (35339181, 39505840, 42171828). |

## 3. Lessons

* Primary microglia are usually neonatal: an "adult" mechanism needs the preparation's age, not the host animal's.
* A review's one sentence reduced to one rat model, one non-selective drug and delayed functional effects; "harmful" rested on neuron and behaviour readouts, not on a larger infarct.
* A treated group measured weeks later can be survivors: read mortality before reading a later benefit.
* A ledger count of one can match a figure while the text claims ten.

## 4. Blind second reading

One delegate (`legend-delegate`; asked sonnet, effort high; read back claude-sonnet-5-5, high, 37 turns; peak context 183,658) judged six sentences from the source files only. It rendered Figure 5E and Supplementary Figure 8 as images.

| Sentence | Verdict | Effect on this result |
|---|---|---|
| S1 neonatal against adult (37907746) | partly | Confirmed the pup-derived cells and the non-specific knockdown; the paper never mentions a neonatal route, so the "neonatal" half is the ledger's, not checkable here. |
| S2 one mouse, no untreated curve (25686832) | partly | Added that the curve falls to about 200 mm3 and never reaches zero; confirmed 70 against 75 percent. My draft called the entry wrong; it is incomplete. |
| S3 inhibitor protective at 0.5 h, harmful at 8 h (42171828) | partly | Corrected my draft: infarct was not larger at 8 h; harm rests on NeuN, TUNEL and behaviour; model is endothelin-1, dose 2.5 mg/kg intravenous. |
| S4 beta2 agonist prevented most seizures (35339181) | verified with limits | The sentence stands; only the pre-treatment window, dose and N = 8 are added. |
| S5 cocktail lengthened each acute seizure, lowered later seizures (39505840) | partly | Added the survivor confound, unchanged seizure number and the two internal disagreements. |
| S6 WWOX associated with improved survival in basal Cox (41007296) | wrong on direction | A defect in the paper (HR 1.014 printed with the words "improved survival"). |

## 5. Wording for the consumers (for IT; hypothesis level)

* **`DL-MECH-124`**: title: replace "against KHK to NOX4-ROS in activated adult microglia" with "against KHK to NOX4-ROS shown in pup-derived primary microglia and BV2 cells, with an adult-mouse hippocampal knockdown that is not microglia-specific". Causal statement: add "(PAPER 277: primary microglia from P1 to P3 pups; in vivo male db/db mice at 24 weeks, CMV-driven AAV-shRNA-Khk injected at week 20; neonatal and adult microglia were not compared)". The decision line is unchanged.
* **`DL-MECH-162`**: "[PAPER 366] shows one heterozygous Wwox mouse (Figure 5E: tumour about 2,150 to about 200 mm3 over 50 days, six injections) and claims a 70 percent cure rate in ten mice (legend: 75 percent) without per-mouse data, an untreated heterozygote curve or an onset age; the Discussion concedes that wild-type mice tend to grow spontaneous tumours."
* **`DL-MECH-122`**: "In male Sprague-Dawley rats with endothelin-1 cortical ischaemia, 2-methoxyestradiol (2.5 mg/kg intravenously, once; not a selective HIF-1 inhibitor) at 0.5 h reduced infarct size and TUNEL-positive cells, whereas at 8 h it did not reduce infarct size, lowered NeuN-positive counts, raised TUNEL-positive cells and worsened adhesive-removal (from day 4), swing and neurological scores (from day 8) ([PAPER 275], via the review PMID 42171828 and the primary PMID 21029239, n = 4 per group)."
* **`DL-MECH-136`**: replace the two clauses with: "a beta2 agonist (salbutamol 10 nmol into area tempestas 5 min before bicuculline, adult male rats, 8 per group, one experiment) left 3 of 8 rats seizing against 8 of 8, in a perspective article's preliminary data ([PAPER 311])" and "a three-antagonist cocktail (prazosin, propranolol, atipamezole intraperitoneally from 5 min after kainate, daily for 3 days, male mice) lengthened the mean convulsive seizure without changing their number and, 3 to 4 weeks later, the surviving treated mice had fewer and shorter convulsive seizures; mortality over 10 days was lower with the cocktail ([PAPER 313])".
* **`DL-MECH-117`** and the PAPER 118 record: the sentence stands; optionally note that the paper's basal-breast WWOX Cox row (HR 1.014, p = 0.034) points to higher hazard against its own words "improved survival".

## 6. Acquisition

Twenty papers of ranks 26 to 55 are now held: two from Europe PMC (32142409, 32248813; the next two calls returned HTTP 503 and were not repeated) and eighteen from the PMC open-data bucket (`pmc_bucket_fetch.py`, files under `files/fulltext/PMID<pmid>_ADV272_PMC_r2.xml`); ten are read in this batch and ten wait for batch 2. Four leads are not held (16061658, 33363507, 33854788, 34210081: access items). Bucket record per paper: `b_<pmid>.json` in the job scratch folder (not kept). Yeh 2010 came from the PMC article page after the bucket returned a restricted stub (`files/fulltext/PMID21029239_Yeh2010_PMC8094320_pmcpage_20261125.html`, sha256 `eeced1775ce57c21a7db1baf423fe584a79416b830560eee89f256ece371b4e5`).

## 7. Receipts

FTR-20261125-{25686832,35339181,37907746,39505840,41007296,42171828,42260675,21029239}-01, all `queried_not_full_read`, recorded the same day (receipt JSON and `make_receipts_adv276s2.py` in this folder). 21029239 (Yeh 2010) is a first record. The three papers re-checked only for species (32142409, 32248813, 39546604) carry no new receipt.
