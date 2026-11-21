# ADV-142 pre-registration: baseline five-metric reading of Fig. 1 and Fig. 2 of the Brain 2026 WWOX organoid paper and of the preprint Expanded View figures (SCI window X, 2026-11-21; hypothesis level; no dose; reference genotype class only; not medical advice)

Assignment: `../assignments/ADV-142.md` (ADV, 2026-11-21). Source: Brain 2026 accepted manuscript (AM) and bioRxiv v2 preprint (PP2), held bytes under the root checkout `files/fulltext/`. Same rules as ADV-140 (`../adv140_aqeilan_fig6_sci_20261121/PREREGISTRATION_ADV140_AQEILAN_FIG6_SCI_20261121.md`): MADE / VISUAL / NOT PRINTED / UNREADABLE; every number carries its version.

## Disclosure: what I had already seen before this registration (so no prediction below is scored as blind for these)
AM legends of Figs. 1, 2 and 6; AM Fig. 1C-D at image level (week-7 cell-attached spikes per neuron: WT about 105, the four mutant lines about 330 to 370, five brackets, all from WT, none among mutants); AM Fig. 1E-F (SOX2 and SATB2 at week 7, per-genotype brackets); AM Fig. 2E-F (neurons and radial glia fractions; WOREE radial glia about +0.07 log2); the AM Results sentence on activity ("both organoids showed similar neuronal hyperactivity" at the earlier time point, "3-fold" at week 16); PP2 EV10 and EV13 legends and PP2 EV12 at 100 dpi (mRNA bars). The Fig. 6 EGFP arms (week 16, infected) were read in ADV-140.

## Not yet read (the predictions below are about these)
PP2 EV10 to EV13 at full resolution (EV10B bar page, EV11 traces, EV12A and B and C, EV13); Table EV1 (organoid numbers, sections, batches) in the held files; AM Fig. 1B at metric level; the per-genotype cell counts behind Fig. 2E-F; any radial-glia metric other than Fig. 2 and EV13.

## Metric map (fixed now)
1. Event frequency: week-7 cell-attached spikes per neuron (Fig. 1D) and week-16 Ca2+ event rate in the AAV9-EGFP arms (Fig. 6A(ii), a different preparation and age; infected organoids, not vector-matched WT).
2. Amplitude: week-16 Ca2+ mean amplitude only (EGFP arms).
3. Percentage of active regions: week-16 Ca2+ only (EGFP arms).
4. Cortical markers: week 7 SATB2 and SOX2 (Fig. 1E-F, immunofluorescence); week 16 CTIP2 and SATB2 (Fig. 6B, EGFP arms) and PP2 EV12 mRNA.
5. Radial glia state: week-7 SOX2-positive fraction (Fig. 1F); week-16 scRNA fractions (Fig. 2E-F); PP2 EV13 (treated against untreated WOREE).
For each row: preparation, age, unit of n, lines, WOREE-against-SCAR12 comparison printed or not, version.

## Predictions (my confidence), about the not-yet-read items only
* P1 (70 percent): Table EV1 is not in the held files (the EV PDF refers to it, a table was not part of the figure PDF).
* P2 (60 percent): PP2 EV10B shows a transduced NeuN-positive WWOX-positive fraction clearly below 100 percent in every line (a median under 50 percent in at least three of four lines).
* P3 (55 percent): PP2 EV11 is representative traces only, with no quantification per line.
* P4 (60 percent): PP2 EV12A (markers per line) shows at least one line whose direction differs from its pooled genotype group for CTIP2 or SATB2.
* P5 (70 percent): PP2 EV13 has no quantification of the radial-glia fraction (only differential expression and cell-cycle overlap).
* P6 (85 percent): no WOREE-against-SCAR12 comparison is printed for any of the five metrics in Fig. 1, Fig. 2, or EV10 to EV13 (the rejecting observation below).

## Rejecting observation (for P6, and so for "the genotype split is not printed")
A printed test (named, with a mark or a p value) between a WOREE group and a SCAR12 group, at any age, for any of the five metrics. Then the answer to "was the WOREE-against-SCAR12 comparison ever printed" changes for that metric.

## Method and checks
Producer reading by me with verbatim locators and measured values (numpy on the held figure images where a value is read; the repository bar script for bar tops). A blind check of the statement-carrying rows by a delegate given only figure crops (Agent tool cannot set effort; briefed "medium"). Then: (a) full-resolution reading of EV10 to EV13 and a Table EV1 search; (b) which of rows A to F of the ADV-140 competing-explanations table the baseline data separate, with a statement of what changes between week 7 and week 16 in the WOREE-SCAR12 activity gap and whether it is printed or eyeballed; close with the CHOICE. Align wording with `analysis/tx007_window_and_ceiling_20260921.md` L29 and `rescue_window_it6_20261029.md` line 110 (do not present the WT-against-treated bracket as new).
