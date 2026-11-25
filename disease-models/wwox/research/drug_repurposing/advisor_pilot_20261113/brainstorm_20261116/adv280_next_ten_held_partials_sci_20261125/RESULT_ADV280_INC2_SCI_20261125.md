# ADV-280 increment 2 and the batch of ten (SCI, 2026-11-25)

Hypothesis level; reference genotype class; nothing here is medical advice. Every item is another disease or system: **NOT WWOX EVIDENCE** (except the first record of increment 1, see its file). Rule, order and predictions: `PREREG_ADV280_SCI_20261125.md`. Increment 1: `RESULT_ADV280_INC1_SCI_20261125.md`. Second readings: facts, `BLIND_REPORT_INC1_SCI_20261125.md`; sentences against sources, all ten records, `BLIND_SENTENCES_ADV280_SCI_20261125.md` and `BLIND_SENTENCES_REPORT_ADV280_SCI_20261125.md` (legend-delegate, sonnet, effort high stated). Image and file hashes: `FILES_VIEWED_ADV280_INC2_SCI_20261125.tsv`. The strict or loose grading is the first reader's; the delegate's different verdicts are shown where they differ.

## 1. Yield

| | strict | loose |
|---|---|---|
| Increment 1 (5) | 1 of 5 | 4 of 5 |
| Increment 2 (5) | 1 of 5 | 5 of 5 |
| **ADV-280 (10)** | **2 of 10** | **9 of 10** |
| Supplement-only records (10.1101, 38378758, 38731820, 38740822) | 0 of 4 | 3 of 4 |
| Figure-only records (35883580, 38443647) | 1 of 2 | 2 of 2 |
| Records with both classes (36926521, 37804316, 41570991, 41706892) | 1 of 4 | 4 of 4 |
| For comparison: ADV-279 | 5 of 10 | 9 of 10 |

(Loose counts every strict.) Reversals of a consumer's direction: 0 of 10. If the first clause of the card E01 sentence on PMID 37804316 is read as the second reader read it, strict is 3 of 10.

**How the count was reached.** The first-pass count, from a facts-only second reading, was strict 0 of 10, which would have met the rejecting observation. A second delegate, given the repository's own sentences and the held sources and no conclusions, returned MUST CHANGE for three sentences; the first reader verified two on the held files and kept the third at loose (section 2). Grading by fact alone under-called the yield: for the next batch, put the repository sentence itself to the blind reader.

## 2. Predictions scored

| | predicted | observed |
|---|---|---|
| P1 strict | 3 (1 to 6) | 2, inside the range |
| P2 loose | 7 (4 to 9) | 9, at the upper edge |
| P3 supplement-only | strict 1 (0 to 3), loose 3 (1 to 4) | 0 and 3, inside |
| P3 figure-only | strict 0 (0 to 1), loose 1 (0 to 2) | 1 and 2, at the upper edge of both |
| P3 both classes | strict 2 (0 to 3), loose 3 (1 to 4) | 1 and 4, inside |
| P4 a supplement, sheet or panel disagrees with its paper's own text or legend, 0.8 | yes: Colin (vinculin against the drawn actin, fibroblast source), AFG3L2 ("10 days" against the plotted gain), ASPA map (24 h against 16 h), the fly preprint (Discussion against Supplementary Figure 3A), PMID 38731820 (Supplementary Figure 1F against Figure 2E) |
| P5 no direction reversed, 0.9 | yes |
| P6 at least one of the ten cannot be completed, 0.4 | no under the pre-registered definition (every class completed, three videos listed unwatched); one receipt keeps supplementary at `not_read` for them |
| Rejecting observation: strict below 2 of 10 | not met (2 of 10); the margin is one record |

## 3. Per record, increment 2

### 35883580 (Liu 2022 review; WWOX pY33 to pS14): STRICT
**Consumers:** `DL-MECH-058` (and `DL-MECH-057` as the paired entry); HE's corrected count gives this record 1 consumer, not 2 (the second was a "Next-search agenda" line).
**Held:** the eight figure images, the figure and supplementary-materials text.
- **Strict.** The `DL-MECH-058` lineage line says the figures and videos are "adapted/republished data". The legends declare adaptation for Figure 5 ("data adapted from Reference [44] with major modifications") and Figure 6 ("image data adapted from Reference [54]") only. Figures 1, 2, 3, 7 and 8 are schematic models and Figure 4 is a STRING output run for the review. The video legends and the Supplementary Materials entry do not state an origin; the Results sentence introducing Videos S1 to S3 reads "we determined".
- **Add.** "No kinetics in the same system" is true of the data shown; the review does assert the transition in text (section on T-cell differentiation, Figure 7A is a schematic with "Kinases? Phosphatases?" drawn).
- Y33R appears once, in the yeast Ras-rescue binding assay (Figure 5A: WW1 Y33R does not grow with SMAD4 or HYAL-2 at 37 degrees C): a binding mutant, not a validated phospho-null conversion test; the "no validated mutants" sentence stands.
- **For IT.** The `DL-MECH-058` source line says the eight figures and three videos were "read integralmente"; the existing receipt records the figures as captions only and no reading of the videos is on record, and this reading did not watch them either (no video tool).
**Proposed wording of the lineage line:** "Figures 5 and 6 are adapted from earlier papers of the group (refs [44] and [54]); Figures 1 to 3, 7 and 8 are schematics and Figure 4 a STRING output; the origin of the three videos is not stated."

### 38378758 (Clausen 2024; Parkin variant abundance map, HEK293T): loose
**Consumers:** card A02 `DR-A02-002`; R1 PB-1, PB-2, Premise 0.
**Held:** all 24 supplement pages, the reporting summary, the source-data workbook (pathogenic table recomputed, two blot images), the peer-review file (searched).
- Supplementary Table 1: 6 of 12 pathogenic variants (11 listed plus P437L reclassified) score 0.84 to 1.17, the other six 0.44 or below; 1 of 15 others below 0.5 (R334C, 0.48). "Half of the pathogenic variants wild-type abundant" and AUC 0.69 stand. PB-1 and PB-2 stand (the 29 degree quotation is verbatim).
- **Add.** "A lysosome-inhibitor control did nothing, placing the loss on the proteasome": the arm is chloroquine 20 uM for 16 h with no stated activity check (text, supplement and source data searched on 2026-11-25 for LC3, p62, SQSTM1, Lysotracker, flux: none; the reviewers did not ask); the authors write "most low abundance variants are proteasome targets" and the bortezomib shift is partial.
- **Add (Premise 0).** The six wild-type-abundant pathogenic variants are an abundance-pathogenicity mismatch; their loss of function is inferred, not measured (function is tested for wild type, R42P and C431A only), and R42P is low abundance but appears functional.
**Proposed wording:** "chloroquine (20 uM, 16 h; no activity check) gave little shift while bortezomib and PSMD14 knockdown shifted the low peak partially: most low-abundance variants are proteasome targets."

### 38443647 (Bacq 2024 review; stiripentol): loose
**Consumer:** card E02 `DR-E02-007`.
**Held:** five figure images, all schematics or a structure (no data panel); exposure text and Tables 1 and 2 re-read.
- The card's content stands: LDH effective concentrations 42 to 500 uM (three table rows, one indirect), total plasma 17 to 106 uM at about 50 mg/kg/day, free tissue 0.2 to 1 uM, brain-to-plasma about 0.5 to 1.2.
- **Add.** The liver-to-plasma ratio of 35 was measured 1 h after intravenous injection in the rat. The review ranks the direct mechanisms (GABA-A potentiation, then ion channels, then energy metabolism or LDH together); the indirect CYP route is outside that ranking. The review also argues that total brain concentrations of 17 to 106 uM are achievable (brain-to-plasma near unity) next to a free level of 0.2 to 1 uM.
- Held figures carry no data: nothing from the figure class changed a sentence.

### 38731820 (Poliquin 2024; HRD1 and zonisamide, Gabrg2 Q390X): loose
**Consumers:** card A04 and R1.
**Held:** the four supplementary figure pages (an image-only PDF, opened at 160 dpi).
- The R1 sentences on the seizure endpoint (six animals drawn against a legend of three, one-tailed, no vehicle group) and on the drug not acting through HRD1 as shown stand.
- **Add.** Dose: 20 mg/kg daily intraperitoneally for 7 days, mice, in both the lysate and the EEG experiments (weakest kind of addition; no change of meaning).
- **Add.** Supplementary Figure 1F (image reading, HEK293T, one screen): HRD1 co-expression lowers wild-type gamma2 from about 0.3 to 0.07 and the mutant from about 1.15 to 0.27, roughly to a quarter, against about 0.66 in the main figure the record cites; RNF34 raises both two to four times. The record's "only HRD1 lowered the mutant" stands. Supplementary Figure 2 knockdown (siRNA labelled 5 uM, mutant arm only) raises the mutant about 2.5 to 2.8 times; the supplementary legends print no n.
- **Add.** "BiP raised in wild type": two of four regions (marked), a trend in hippocampus, none in cortex.

### 38740822 (Grønbæk-Thygesen 2024; ASPA map, HEK293T): loose
**Consumers:** card A02 `DR-A02-002`; R1 route-of-loss and abundance paragraphs.
**Held:** all 23 supplement pages, the reporting summary, the source-data workbook (counts recomputed, one blot image), the peer-review file (one passage read).
- Recomputed from the Selected Variants and Fig 6 sheets: 61 pathogenic variants scored, 50 below 0.5; benign three 0.82 to 0.98; 6,152 of 6,260 variants scored. "E1 and proteasome inhibition raise the low-abundance population, HSP70 inhibition modestly, chloroquine does not, 29 degrees removes most of it; the substrate had no effect, its intracellular level unknown" stands. The solubility check (five variants, mostly soluble; C152W separately, very low) matches the supplement.
- **Add.** Chloroquine 20 uM for 16 h, "little effect" in the authors' words, no activity check; the authors "cannot exclude" autophagic contribution; Supplementary Figure 8 gives chloroquine no effect on the single variant C152W either, and bortezomib only a small shift there. The NAA incubation is 24 h in Methods and 16 h in the Supplementary Figure 8 legend (supplement against Methods).

## 4. What to carry

- Two strict items sit in the oldest-read, most consumer-cited records (a review ledger line and a card parenthesis); both were of the kind "a description of the source repeated from memory". Both were found by checking the sentence, not the paper.
- The same unverified-control pattern (chloroquine at one dose, no activity check, read as a null) now appears in two papers under one card; a candidate audit class is every card note whose evidence is a null (ten notes in the cards use null wording, one mentions a control).

## 5. Limits

Image readings are by eye except where a pixel, table or workbook computation is named. No video was watched (three in 37804316, three in 35883580). Peer-review files were searched, not read in full. The Bouchez article PDF held beside its supplement was not paged as images.
