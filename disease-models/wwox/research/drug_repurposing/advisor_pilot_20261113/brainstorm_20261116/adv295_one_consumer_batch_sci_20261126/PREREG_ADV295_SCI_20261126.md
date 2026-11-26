# ADV-295 pre-registration: one-consumer reading batch, block 1 (SCI, window c6d4dd83)

Frozen at 2026-11-26T02:17:50Z, before any article text, figure or supplement of the five was opened by this unit and before the consumer sentences were read for it (seen: receipt-ledger counts, held file names, graphic file names printed in two XML files, consumer identifiers). Hypothesis level; reference genotype class only; nothing here is medical advice. Brief: `assignments/ADV-295.md` (ADV message 2026-11-26). Held bytes only: no acquisition, no spend, no contact, no e-mail address to any service. Frozen RP-045 and sealed ADV-174/175 untouched; the Obeid 2026 article is not among the records and stays unopened. Order: after the ADV-287 extension.

## Block 1

| record | consumer | unread class to read | held files (root checkout, under `files/`) | stated limit |
|---|---|---|---|---|
| 42807679 | CLAIM 032 | figures | `figures/PMID42807679/` (g003 to g007), `fulltext/PMID42807679_Khadija2026_PMC.xml` | figures 1 and 2 not held: the class cannot be completed |
| 41254692 | DL-REPO-003 | supplementary (figures: only Figure 7 held) | `supplements/PMID41254692/`, `fulltext/PMID41254692_Qin2025_PMC.xml` | main figures 1 to 6 not held |
| 42401046 | DL-THER-089 | supplementary | `supplement/PMID42401046_r2/`, `figures/PMID42401046_r2/`, `fulltext/PMID42401046_Helton2026_PMC_r2.xml` | none known |
| 39546604 | RP-033 | discussion, figures | `figures/PMID39546604_r2/`, `supplement/PMID39546604_r2/`, `fulltext/PMID39546604_ADV272_PMC_r2.xml` | none known |
| 41210171 | DL-METH-118 | figures | `supplement/PMID41210171_mmc1.pdf`, `figure_renders/sciC_w5/PMID41210171_fig6.jpg`, `fulltext/PMID41210171_Vono2025_PMC.xml` | only a render of Figure 6 held among the main figures (an article PDF is searched by name and content first) |

Block 2 (only after block 1): 32719346, 33704440, 35079122, 35243344, 36282524 (all feed DL-MECH-170): all five if block 1 has 2 or more strict records, three (the first three) if it has 1, none if it has 0.

## What counts as completed

All held material of the class looked at (every figure as an image, every supplement page, table and sheet); a class that cannot be completed from held files stays unread and the result says what is missing. Before "not held": list `files/supplement*`, `files/figures`, `files/fulltext` and search by identifier. sha256 for each image or rendered page. Values labelled by sheet or figure, panel and row, with species and replicate unit; folds and ratios computed over ALL source rows.

## Matching rule (one rule, as ADV-292 section 5)

**Strict**: (a) the reader verifies on a held file of the class read that a consumer sentence, as written, is false or unsupported, and (b) a blind sentence-level reader, given the repository sentence verbatim and the held sources and none of the reader's verdicts, returns MUST CHANGE for it. Only one of the two: listed apart, not counted. **Loose** = strict, or a window, dose, species, unit or evidence level must be added. A negative is verified only with a dated search and its query, otherwise UNSETTLED. SCI checks every strict candidate on the original.

## Prediction and stop (ADV, fixed)

Strict 2 of the five (range 0 to 3). **Rejecting observation: 0 strict in block 1** = stop, block 2 not read, the one-consumer tail is closed at the consumer level (next debt: unread gold or new corpus).

## Readers

Delegates (legend-delegate, sonnet, effort high stated, read back), one at a time; figure reads are the delegate's, not SCI's context. No receipt is written without the reading it describes.
