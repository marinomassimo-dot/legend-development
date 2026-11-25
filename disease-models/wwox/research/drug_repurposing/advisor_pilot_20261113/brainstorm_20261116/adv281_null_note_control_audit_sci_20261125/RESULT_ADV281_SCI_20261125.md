# RESULT, ADV-281: positive-control audit of null-wording card notes (SCI, 2026-11-25)

Hypothesis level; reference genotype class; nothing here is medical advice. Session 9cc174db (claude-sonnet-5-5, effort high). Rule and predictions: `PREREG_ADV281_SCI_20261125.md` (written before any source was opened); frozen list: `STEP0_FROZEN_LIST_ADV281_SCI_20261125.md`. First reading: `FIRST_READ_ADV281_SCI_20261125.tsv`. Blind reader (legend-delegate, sonnet 5.5, effort high, given only the verbatim sentence and the source paths): `BLIND_REPORT_ADV281_SCI_20261125.md`. Files viewed with hashes: `FILES_VIEWED_ADV281_INC1_2_SCI_20261125.tsv`.

## 1. STEP 0: the list, by two routes

* 246 distinct assertion ids in the 30 cards. Route S (structured `direction` = `NO_CHANGE`): 31. Route T (null phrases in `measured_result_note` or `note`): 125. After screening the card text, **63 are real null notes** (40 drug, 23 disease assertions), against SCI's earlier count of ten: the scan of the previous session looked at one field and keywords only.
* Of the ten of the brief, nine survive; **DR-H01-001 is dropped** (matched on "no effect size"; the note records a suppression). Five of the ten are in both routes, five are text-only (the text route is the one that finds a null written as a side arm inside a row coded INCREASE or DECREASE, such as the chloroquine arm of DR-A02-002).
* Audited: the nine, DR-D01-002 (first addition by consumer count) and five more additions in consumer order (DA-LC-ATF4-002, DR-AAV-GLU10-HD, DR-AAV-GLU10-LD, DR-P11-004, DR-H02-019). **Queued by id, not audited: the other 48 null rows** of `screen_adv281.tsv`.
* Set aside and reported: six rows that read "not different from wild type" as restoration (DR-AAV-GFAP-P5HD, DR-AAV-GFAPAREA-HD, DR-AAV-GLU20-HD, DR-AAV-MOTOR-HD, DR-C01-001, DR-D01-001): an equivalence-by-non-significance question, different from an activity check (prior art on the wording: ADV-182, ADV-193).

## 2. STEP 1: classes (13 assessable, 2 not)

| id | first reader | blind reader | in-study check (both) | sentence (blind) |
|---|---|---|---|---|
| DR-A01-003 | PRESENT | PRESENT | yes | ADD |
| DR-A01-004 | NOT MATCHED | ABSENT | no | STANDS |
| DR-A02-002 | ABSENT | ABSENT | no | ADD |
| DR-A02-009 | PRESENT | PRESENT | yes | **MUST CHANGE** |
| DR-E03-001 | NOT MATCHED | NOT MATCHED | database rows only | ADD |
| DR-H01-003 | NOT MATCHED | NOT MATCHED | abstract level | ADD |
| DR-L01-001 | NOT ASSESSABLE | not sent | none held | not judged |
| DR-M01-001 | PRESENT | PRESENT | yes | ADD |
| DR-P11-006 | NOT ASSESSABLE | not sent | none held | not judged |
| DR-D01-002 | PRESENT | PRESENT | yes | ADD |
| DA-LC-ATF4-002 | PRESENT | PRESENT | yes | ADD |
| DR-AAV-GLU10-HD | PRESENT | PRESENT | yes | ADD |
| DR-AAV-GLU10-LD | PRESENT | NOT MATCHED | yes | ADD |
| DR-P11-004 | NOT MATCHED | ABSENT | no | **MUST CHANGE** |
| DR-H02-019 | PRESENT | NOT MATCHED | yes | ADD |

Where the readers differ (four classes), the cause is the rule for a cited result: the first reader counted a cited other-system effect as NOT MATCHED (PREREG); the blind reader counted it as no check where the paper's own experiments held none. The in-study column agrees on every row. Reconciled report: both are shown, and the figures below give the range.

## 3. Scoring against the PREREG (the nine survivors of the ten)

* **P1 strict (CHECK ABSENT), predicted 3 of 10, range 1 to 5:** first reader 1 of 7 assessable (2 of 9 not assessable included), blind reader 2 of 7 (DR-A01-004, DR-A02-002). **At or below the bottom of the range.**
* **P2 loose (ABSENT or NOT MATCHED), predicted 6 of 10, range 4 to 8:** both readers 4 of 7 assessable (A01-004, A02-002, E03-001, H01-003); 4 of 9 counting the two not assessable. **At the bottom of the range.** Over all 13 assessable: first reader 5, blind reader 7.
* **P3 blind MUST CHANGE, predicted 2 of 10, range 0 to 4:** 2 of 13 (DR-A02-009, DR-P11-004), both outside the null's own class (see section 4); MUST CHANGE or ADD on 12 of 13, which matches ADV-280's loose rate (9 of 10).
* **P4 text route finds nulls outside the ten:** yes, 54.
* **Rejecting observation (loose 2 of 10 or fewer): not met.** Four of seven assessable nulls had no activity or engagement check matched to the null's own conditions. The checks that were present were mostly the same paper's positive effect of the same manipulation on a sibling readout, which is the commonest form of a good control; the absent cases are the ones that read an inhibitor or compound with one dose and one readout.

**What the class changes:** it never reverses a direction. It changes how a null may be cited. Two nulls had **no in-study check at all and no matched citation**: chloroquine in both variant-map papers (DR-A02-002) and 4-PBA in the zebrafish (DR-A01-004).

## 4. Findings that did not wait for the class (for IT)

1. **DR-A02-009 (MUST CHANGE).** The card says I278T "is rescued by proteasome inhibition in mice and in the kidney line". Collard 2023 says "in yeast, in human patient fibroblasts and transgenic HCU mice" (citations) and has no kidney line; its own cells are a hamster fibroblast line, and proteasome inhibitors were tested there on R125Q only (the kidney-line datum belongs to another paper, DR-A02-008). Replacement: "although the paper cites rescue of I278T by proteasome inhibition in yeast, human patient fibroblasts and transgenic mice (refs 15, 25, 28); proteasome inhibitors were tested here on R125Q only".
2. **DR-P11-004 (MUST CHANGE; this corrects ADV-276's own sentence).** The card says only the EEG p value of Table 2 fails to reproduce. The printed 0.04 reproduces as an uncorrected chi-square of 11/2 against 6/7 (chi-square 4.25, p 0.0393, recomputed by SCI); Fisher exact gives 0.097 and a Yates-corrected chi-square 0.099 (two of four expected counts 4.5). The DQ/SQ p of 0.09 is the one no standard test reproduces (0.055 uncorrected, 0.114 Fisher). Table 3 reassignment and its chi-square values stand.
3. **DR-M01-001 (stale source label and a sentence the panel does not carry).** The label says the supplement is not available locally: it has been held since 2026-11-21 (File010, receipt FTR-20261124-42397075-89). "The upper-layer marker mildly rises (main text)" is the authors' text; the panel (Supplementary Fig 7F, SCI viewed the rendered page, hashes in the files-viewed table) marks KO against KO plus A51 as not significant for SATB2. `DA-ORG-001` carries the same stale "no checkout" statement.
4. **DR-D01-002.** CTIP2 is near the floor in both knockout arms (about 0.1 and 0.7 percent of cells); the knockout reference arm is not labelled DMSO while WT NT against WT DMSO differs for CTIP2 (about 12.6 against 5.6 percent, **); the plotted points per bar exceed the legend's organoid numbers (WT NT 6 points against n = 4); "both markers" must not be read to include NEUN (which rises).
5. **DR-H02-019.** "Diffusion coefficient unchanged": Table 2 shows P 0.62 and 0.52 with group medians not running one way (right 1209 in the finding group against 1280 in controls, left 1427 against 1366); the paper's own text says the finding group's ADC was higher.
6. **DA-LC-ATF4-002.** The Atf4 staining in the LacZ background is near blank (floor); knockdown is verified in newly eclosed heads only; two backgrounds, two tests.

## 5. STEP 2: corrected or added sentences and consumers

Sentences for IT (card owner) are in the blind report under each id ("Added clause" or "Replacement") and in the first-reading table; the ones that matter most:

* **DR-A02-002 (ABSENT).** Replace "a lysosome-inhibitor control did nothing, placing the loss on the proteasome" by: "chloroquine 20 uM, 16 h, produced 'no substantial changes' (Clausen Fig 3C) and 'little effect' (Gronbaek-Thygesen Fig 4F); no readout in either paper shows that chloroquine blocked lysosomal degradation in these cells (bafilomycin A1 appears only in the Parkin mitophagy assay); the proteasome attribution rests on the bortezomib, PSMD14-siRNA, E1-inhibitor and HSP70-inhibitor arms and is stated for most variants, and the ASPA authors write that autophagic clearance cannot be excluded on the short timescales used".
* **DR-A01-004.** Keep; add: no compound raised the mutant's locomotion in any tested arm (supplement Table S1), so the readout has no demonstrated way up; 4-PBA activity in zebrafish is not shown (toxicity above 50 uM only; the 5 mM worm result is cited).
* **DR-E03-001.** Add the retrieved enzyme rows that disagree (EC50 180 uM; 5.7 mM with 64.2 percent at 10 mM; Kd above 1 mM; EC50 above 100 mM) and that the above-1-mM rows share companion values, so the null is a potency statement.
* **DR-H01-003.** Add: one model only; abstract only; no dose or exposure for that arm; efficacy elsewhere in the same abstract.
* **DR-AAV-GLU10-HD and LD.** Add: P10, Student t tests without multiplicity correction, KO against WT only at one star, counted n about 8 to 11, low-powered; LD expression shown at P30 only; "ns against the untreated knockout" is not evidence of no effect.

Consumers that lean on these nulls (leads, not a complete list; peer pointer lists are leads): the card sentence lines `H01 evidence_against[2]`, `P11 evidence_against[3]`, `E03 pharmacology`, `A01 indication_and_transfer`; the comparison rows of the same ids; `coverage/assertion_pertinence.tsv`; `coverage_matrix.json`, `member_evidence.tsv`, `ranking.json` and the investigation tables for the GLU10 and D01 rows (13 files name DR-D01-002); the ADV-276 sentence for DR-P11-004 and DR-H02-019 (applied by `apply_adv276_cards.py`).

## 6. Limits

* Two nulls could not be assessed because their bytes are not held: **DR-L01-001** (Kobayashi 2016, PMID 27211851) and **DR-P11-006** (Hou 2019, PMID 31806980; receipt FTR-20261029-31806980-01 records a fetch whose bytes were not saved). No acquisition was made (brief). Both are open-access; an acquisition by the recorded Europe PMC recipe is a routing decision for ADV or HE.
* The screening of 130 candidates is one reader's judgement of card text and was not blind-checked; 48 null rows are unaudited. The phrase list matched DR-E03-001 by an incidental phrase, so route T has a recall limit.
* Figure images were not held for Collard 2023 and Shah 2025 (viewed: none of Shah's); no video; supplement PDFs of the variant-map papers were searched, not paged. Image readings are by eye except where a table or recomputation is named. The blind reader judged the sentences of 13 ids only.
* Receipts are not written: this was a targeted check of null notes, not a completed read of any paper.

## 7. Carry forward (EMPATHY)

* A null needs its own activity or engagement check **and** its comparator: the nulls with a same-paper positive effect on a sibling readout were fine; the ones with a single compound at a single dose were not.
* A second reader given the sentence found the stale label, the wrong reproducibility claim and the misattributed citation that a facts-only check does not reach; one of them overturned a sentence this same strand wrote on 2026-11-25 (ADV-276).
* Candidate direction (queued, not run): the six "not different from wild type" restoration rows need their untreated-knockout and power read before they are cited as rescue.

## 8. Addendum (2026-11-25, after ADV's decision to acquire the two missing sources)

Both open-access articles were acquired by the recorded Europe PMC recipe into the root checkout (not in git): Hou 2019 (PMC6857673; digest equals the one recorded on 2026-10-29) and Kobayashi 2016 (PMC4879264; the first attempt timed out at 60 s with no bytes, the second returned 200). Hashes are in the files-viewed table. They were read by the first reader only (no blind check of these two).

* **DR-P11-006: CHECK PRESENT, in-study yes.** In the same mice, oral magnesium sulfate raised serum magnesium from 1.38 to 2.24 mM (day 21) and 2.21 mM (day 28) while CSF stayed at about 0.89 mM, and the same CSF assay detected the rise under magnesium L-threonate (0.89 to 1.15 and 1.17 mM). The note says serum rose and CSF did not change, and the L-threonate rise as about 30 percent; both reproduce (29 and 31.5 percent from the Results values; the Discussion prints 21.6). Sentence: STANDS (first reader).
* **DR-L01-001: CHECK PRESENT, in-study yes.** In the same Keap1-conditional-knockout BMDMs under the same 6 h M1 stimulation, Il6, Il1b, Il1a, Nos2 and Il12b fell while Tnf and Irf1 were "not changed" (Results); the DEM and 15d-PGJ2 arms were controlled with Nrf2-knockout BMDMs (Figure 4 legend: the inhibition of IL6, IL1b, IL1a and the Nqo1 induction are cancelled by Nrf2 knockout). Sentence: ADD, clarity only: "the NRF2-knockout control was a pharmacological activation" should read that the NRF2-knockout BMDMs were the control for the DEM and 15d-PGJ2 arms.

**Revised scoring (the nine survivors of the ten, all now assessable):** loose (ABSENT or NOT MATCHED) 4 of 9 (both readers); strict 1 to 2 of 9. Predictions P1 (3 of 10, range 1 to 5) and P2 (6 of 10, range 4 to 8) both fall at or below the low end; the rejecting observation (loose 2 of 10 or fewer) is still not met. Over all 15 audited: loose 5 to 7 of 15.
