# ADV-326: blind numeric extraction, GSK3 phosphosite panels (HE, 2026-11-28)

Reader: HE (ACTOR_ID plan), session 4441b7bf, model claude-sonnet-5-5, effort high, no delegate.
Blind: SCI's folder adv325_gsk3_phosphosite_census_sci_20261128/ and every SCI result were not opened.
Extraction only; no interpretation, no claim, no change to canonical files. Not medical advice.

## Sources read

| Key | Artefact | sha256 (first 16) |
|---|---|---|
| Cheng 2020, PMID 32000863, PMC6990504 | article PDF, 16 pages (held: files/supplement/PMID32000863_r2/PMC6990504.1.pdf); panel c rendered at 400 dpi from page 12 | ffabbadfea78c5af |
| Cheng 2020 | Additional file 1, 24 pages (text search only; Figure S7 legend on page 20) | 0acb771cfe3a4c36 |
| Cheng 2020 | PMC XML (held: files/fulltext/PMID32000863_Cheng2020_PMC.xml) | 792b5b296863674d |
| Wang 2012, PMID 22193544, PMC3354054 | article PDF, 11 pages, PMC open-data bucket, this session | 8f994f9542a7a374 |
| Wang 2012 | figure files cdd2011188f1.jpg and cdd2011188f4.jpg, same bucket | bcffe618de02f099 and 395881491429983a |
| Wang 2012 | PMC XML (held: files/fulltext/PMID22193544_Wang2012_PMC.xml) | eb6f568d046f8df8 |

Page numbers below are PDF page numbers.

## A. Cheng 2020, Fig 7c (figure and legend: page 12)

Printed values under the representative blot. Unit, as the legend states it: ratio of phosphorylated or total GSK3β to
β-actin protein level (densitometry; arbitrary ratio). One value per lane; no error value, no test.

| Panel | Row (target) | Tissue | Genotype | Printed value |
|---|---|---|---|---|
| 7c | pGSK3β (Ser9) | cerebellum | +/+ | 2.7 |
| 7c | pGSK3β (Ser9) | cerebellum | +/- | 3.1 |
| 7c | pGSK3β (Ser9) | cerebellum | -/- | 1.3 |
| 7c | pGSK3β (Ser9) | hippocampus | +/+ | 3.6 |
| 7c | pGSK3β (Ser9) | hippocampus | +/- | 3.5 |
| 7c | pGSK3β (Ser9) | hippocampus | -/- | 2.0 |
| 7c | pGSK3β (Ser9) | cortex | +/+ | 3.9 |
| 7c | pGSK3β (Ser9) | cortex | +/- | 3.8 |
| 7c | pGSK3β (Ser9) | cortex | -/- | 2.5 |
| 7c | GSK3β (total) | cerebellum | +/+ | 2.2 |
| 7c | GSK3β (total) | cerebellum | +/- | 2.4 |
| 7c | GSK3β (total) | cerebellum | -/- | 2.4 |
| 7c | GSK3β (total) | hippocampus | +/+ | 2.3 |
| 7c | GSK3β (total) | hippocampus | +/- | 2.4 |
| 7c | GSK3β (total) | hippocampus | -/- | 2.6 |
| 7c | GSK3β (total) | cortex | +/+ | 2.2 |
| 7c | GSK3β (total) | cortex | +/- | 2.4 |
| 7c | GSK3β (total) | cortex | -/- | 2.6 |

The Wwox and β-actin rows carry no printed number. A phospho-to-total ratio is NOT PRINTED (page 12).

### Design facts for 7c

| Item | What the source prints | Page |
|---|---|---|
| Independent experiments | "representative results of four independent experiments are shown" | 12 (legend) |
| Whether the printed numbers are the shown blot or a mean of the four | NOT PRINTED (pages 4, 10-12) | |
| Animals per genotype for the blot | NOT PRINTED (pages 4, 10-12, 14; text search of Additional file 1) | |
| Postnatal age, legend | postnatal day 20 | 12 |
| Postnatal age, Western blotting Methods | tissues isolated at postnatal day 14 | 4 |
| Age conflict | the legend (P20) and the Methods (P14) disagree; the paper does not resolve it on the pages read | 4, 12 |
| Antibodies named in the Western blotting Methods | anti-WWOX, anti-DCX, anti-β-actin; no anti-GSK3β and no anti-phospho-Ser9 antibody is named there (the text refers to a previous method) | 4 |
| Anti-GSK3β or anti-phospho-Ser9 antibody anywhere else | not found (text search of the 16 article pages and 24 supplement pages) | |
| Knockout line used in 7c (exon 1 or exons 2/3/4) | NOT PRINTED in the legend (page 12) | |
| Statistics for the blot | NOT PRINTED; the legend's mean ± SEM and P values sit with the seizure data | 12 |

## B. Wang 2012 (SH-SY5Y cells)

### Fig 1d (page 2)

Western blot. Lanes: mock, Si1+3, Si1, Si3 (WWOX siRNA). Rows: WWOX, pTau S396, Tau, actin.

| Item | Finding |
|---|---|
| Printed quantification | NOT PRINTED (figure and legend, page 2) |
| n | NOT PRINTED for panel d |
| What is plotted | blot images only |
| A GSK3β or GSK3β pS9 row in 1d | none |

### Fig 1e (page 2)

Bar graph, y axis "% of differentiated cells" (0 to 50), x axis day 1 to 4, bars mock, Si1+3, Si1, Si3. Legend: mean ± S.E.
from three independent experiments; * P<0.05, ** P<0.01 against mock control. Differentiated = neurite longer than twice
the cell body length. No value is printed; the numbers below are MY READING of bar tops from the 150 ppi image embedded in
the PDF (axis ticks 0 to 50 span 192 pixels), uncertainty about ±0.5 percentage points. n is experiments, not cells; the
number of cells counted is NOT PRINTED (page 2).

| Panel | Day | mock (% cells) | Si1+3 (% cells) | Si1 (% cells) | Si3 (% cells) | n | Marks printed over the siRNA bars |
|---|---|---|---|---|---|---|---|
| 1e | 1 | 2.1 | 1.8 | 2.3 | 2.3 | 3 independent experiments | none |
| 1e | 2 | 18.8 | 7.8 | 8.3 | 8.9 | 3 independent experiments | *, *, * |
| 1e | 3 | 33.6 | 19.0 | 17.2 | 19.0 | 3 independent experiments | **, **, ** |
| 1e | 4 | 46.9 | 29.4 | 28.6 | 31.5 | 3 independent experiments | **, **, ** |

### Fig 4b (page 6)

In vitro kinase reaction followed by Western blot. Lanes: ATP(-), no addition, GST, GST-WWOX 1, 3 and 10 µg.
Rows: pTau S396, pTau S404, GSK3β, Tau, Coomassie staining.

| Item | Finding |
|---|---|
| Printed quantification | NOT PRINTED (figure and legend, page 6); the printed numbers in Fig 4 are under panels a and d and in the chart of c, not b |
| n or replicate number | NOT PRINTED for panel b |
| What is plotted | blot and stained-gel images only |
| Unit | GST-WWOX amount in µg; no signal unit |
| Phosphosite of GSK3β itself | not shown; the phosphosites in 4b are on Tau (S396, S404) |

## Limits

- Wang: a text search for a statistics paragraph found none; replicate statements were found on pages 2 and 8 only.
- The Fig 1 legend sentence for panel c refers to "Figure 2b" (page 2); recorded as printed, panel c was not requested.
- Bar readings are pixel measurements by one reader, not source data.
