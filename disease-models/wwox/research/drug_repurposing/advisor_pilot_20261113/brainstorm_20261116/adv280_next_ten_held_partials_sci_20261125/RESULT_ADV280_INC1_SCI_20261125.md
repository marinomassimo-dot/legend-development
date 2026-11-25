# ADV-280 increment 1: five held records (SCI, 2026-11-25)

Hypothesis level; reference genotype class; nothing here is medical advice. Except for PMID 36926521 every item is another disease or system: **NOT WWOX EVIDENCE**. Rule, order and predictions: `PREREG_ADV280_SCI_20261125.md`. Second reader: `BLIND_STATEMENTS_INC1_SCI_20261125.md`, `BLIND_REPORT_INC1_SCI_20261125.md`. Image hashes: `FILES_VIEWED_ADV280_INC1_SCI_20261125.tsv`. The strict or loose grading is the first reader's; the delegate judged facts only.

## 1. Yield

| record | classes read | strict | loose | class that carried the change |
|---|---|---|---|---|
| 36926521 (Colin 2023) | figures, supplementary | 0 | 1 | supplementary |
| 37804316 (AFG3L2) | figures; supplementary not closed (3 videos unwatched) | 0 | 1 | figures |
| 41570991 (Bouchez 2026) | figures, supplementary | 0 | 1 | supplementary |
| 41706892 (PNAS 2026) | figures, supplementary | 0 | 1 | figures and methods |
| 10.1101/2025.05.01.651195 | supplementary | 0 | 0 | none |
| **increment 1** | | **0 of 5** | **4 of 5** | |

No consumer direction reversed. Under the pre-registration (section 4) unwatched videos are listed and do not block completion; the receipt for 37804316 is nevertheless kept at `not_read` for supplementary, which is the stricter checklist rule.

## 2. Per record

### 36926521: loose
**Consumers:** `CLAIM 033` reserve (1) "strongly reduced band with a faint residual band, one control and no quantification"; `DL-BIO-002`-type splice description (293 bp expected product, 186 bp short product).
**Held:** Supplementary Figure S5 (`Image5.TIFF`), supplementary methods (`DataSheet3.doc`), all main figures and legends.
- Panel G: one control lane, one affected lane. **"Faint residual" holds**: the second reader would not call the shade a band; measured on the held pixels, every column block of the affected lane darkens at band height by about 9 to 19 grey levels of 255 against the rows above and below, while the control band is near saturation. Not a quantity.
- **Loose:** the drawn loading control is actin; the supplementary methods name an anti-actin antibody and also say vinculin was the loading control; their cell-culture sentence names fibroblasts from a healthy donor and from another individual of the series, not from the WWOX case, while the article says the blotted line came from the WWOX case. No replicate.
- Panel F (observation, no consumer sentence changes): a junction to a position the figure labels "Alternative exon 6" is drawn in the 293 bp products of the affected individual and one unaffected first-degree relative; the text does not mention it; read counts illegible.
- Panel E: the 293 bp product is the stronger band and the 186 bp product the weaker one in the affected lane (not quantified).
**Proposed addition to the reserve:** "the loading control is drawn as actin although the supplementary methods also name vinculin, and the methods do not list the source of the blotted fibroblasts".

### 37804316: loose
**Consumer:** card E01 `not_known` (compensatory-ISR item): "HRI or DELE1 loss worsens, and a GADD34-targeted compound improves, patient-cell and mouse endpoints (survival gain about 6 to 7 days at the median by plot reading)".
- Figure 5A: the compound (8 mg/kg) was given to the dams by oral gavage from embryonic day 14 to postnatal day 3 and to the pups intraperitoneally every day from birth. **Prenatal plus postnatal exposure.**
- Figure 5C (image reading, mouse, one animal per step): vehicle knockouts median day 14 (n about 15), treated day 20 (n 5 or a multiple); gain about 6 days. The authors write "extended by only 10 days". Wild-type and knockout, no n printed.
- No phospho-eIF2 alpha or ATF4 measured in any treated mouse (article and supplement text searched 2026-11-25; videos not watched). Supplementary Figure 3B table (patient fibroblasts, 25 uM): DMSO against compound marked, untreated against compound not.
**Proposed wording:** "... a GADD34-targeted compound, given prenatally through the dams and then daily to pups, improves ... (survival gain about 6 days at the median by plot reading, 5 treated knockouts; target engagement not measured in the mice)".

### 41570991: loose
**Consumer:** card E02 `DR-E02-006`, first sentence "Cell viability and extracellular acidification fall at tens of micromolar", with this paper listed among its sources.
- This paper's cell experiments used 500 uM (human glioblastoma spheroids) and 250 uM (two mouse small-cell lung cancer lines).
- Supplementary Figure 1B (annexin V and propidium iodide, mouse lines, n = 3): viability not significantly lower from 5 to 250 uM; about 67 and 60 percent at 500 uM.
**Proposed addition:** "in the complex I paper, death in two mouse tumour lines was not significantly raised up to 250 uM (annexin/propidium iodide, n = 3); the tens-of-micromolar figure comes from the other papers and other readouts". IT should check which paper carries the first sentence before applying it.
- Observations without a consumer change: Figure 9C, malate dehydrogenase unchanged at 125 and 250 uM (card agrees); Supplementary Figure 5 legend says increasing stiripentol but plots digitonin; Methods keep an unfilled placeholder for an exposure time.

### 41706892: loose
**Consumer:** card E01 `not_known` (network-silencing item): "group I mGluR agonism raises both in minutes without an Atf4 mRNA change in normal mouse hippocampus".
- Methods and Figure 1B: DHPG 100 uM for 5 min, then 30 min recovery, then snap-freezing; mouse hippocampal slices, n = 3 per group, paired t test, ATF4 P = 0.047, phospho-eIF2 alpha ratio P = 0.043; Figure 1C Atf4 mRNA n = 3, P = 0.75.
- Dataset S1 (`sd01.csv`, 2,929 proteins), recomputed at |log2 fold change| above 0.5 and adjusted P below 0.05: agonist against wild type 3 up and 60 down (as printed); knockout plus agonist against wild type plus agonist 74 up, 26 down (text 75 and 26).
**Proposed wording:** "raises both after a 5-minute pulse, measured 30 minutes later (n = 3, P about 0.045), without an Atf4 mRNA change".

### 10.1101/2025.05.01.651195: no change
**Consumers:** `CLAIM 025` and `DL-META-088` statuses of the preprint. Nine supplement pages seen; seven tables parsed (differential-gene counts per comparison match the text; large sheets not read row by row). Statuses unchanged.
- Outside the tested sentences: the preprint's Results and Supplementary Figure 3A show shorter lifespan with glial knockdown and neuronal amyloid (22 against 24 days, p = 0.0095) while its Discussion says there was no effect; `research/fulltext_dossiers/PPR1015434.md` concludes "neuronal, not glial, Wwox is the relevant pool". Suggested for the dossier: "neuronal more than glial; glial knockdown shortened lifespan slightly".

## 3. Limits

Image readings are by eye except where a pixel or table computation is named. No video was watched. The Bouchez article PDF held beside the supplement was not paged as images.
