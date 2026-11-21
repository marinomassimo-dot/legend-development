# ADV-166 pre-registration: can an early neuron-to-progenitor ratio and the later absolute neuronal output carry different signs in Javed et al. 2026, and does INV-17 already enforce that distinction? (SCI successor Z, 2026-11-21; hypothesis level; adjacent non-WWOX preparation; no dose; no contact; no e-mail address to any service; reference genotype class only; not medical advice)

Fixed BEFORE any numeric source data (Nature source-data files, GEO matrices, figure values) was opened. What had been read when this was written: the INV-17 row of `ranking_it8_p9_20261029/investigations_it20.tsv` (question, decisive uncertainty, next_test, evidence); from the publisher PDF (Nature 655, 16 July 2026; PMID 42129570; DOI 10.1038/s41586-026-10491-x; 74,097,269 bytes, SHA-256 `5e048b0873138a122e69bf9a8894075db3bb1c02f25d06268dfcbb70c0e3625c`, verified before use; text extracted with `pdftotext`, 41 pages, figures are images and were not viewed): the Results section on JUNB function, the Fig. 4 legend, the Extended Data Fig. 12, 13 and 14 legends, the Methods on organoid electroporation, in utero electroporation, birth-dating, scRNA-seq collection and statistics, and the Data availability statement. What that already told me, stated so the rules are not mistaken for blind: the text states the DIRECTIONS (human CRISPRi knockdown raises the neuron-to-progenitor ratio; mouse JUNB overexpression lowers the IP-N/RG ratio, extends neuronal generation and, by Tracker-seq, "ultimately" raises neuronal production). What is unknown to me is the unit, the n and the size of each effect in the source data.

## Question
Does the paper hold a MATCHED comparison (same species, same perturbation, same preparation, with an early ratio and a later absolute output or yield per starting lineage each measured with a stated denominator) in which the two carry different signs? And, if so or if not, does INV-17's stated next_test already enforce a separate early-against-final reading, or does IT need one added rule? Not a WWOX-to-JUNB link; no JUNB intervention.

## Measure map from the text (species, preparation, perturbation, time, denominator, replicate unit as the legends and Methods state them; to be checked against the source data)
| id | Figure | Species and preparation | Perturbation | Time | Readout and denominator | Replicate unit stated |
|---|---|---|---|---|---|---|
| M1 | 4c, ED12b | human cortical organoid (OrgH), day-43 ventricle electroporation, several organoid batches | JUNB CRISPRi knockdown | fixed 7 days after electroporation | NEUROD2+ GFP+ over SOX2+ GFP+ (N/RG ratio), counted per ventricle | ventricle nested in organoid; n = 3 control and 4 knockdown organoids; per-organoid Welch t test P = 0.0466 |
| M1b | ED12c | same | same | same | VZ thickness (a progenitor-pool proxy), ventricles 19 control and 12 knockdown | no difference stated |
| M2 | 4d, ED13g | mouse cortex, in utero electroporation E15.5 | JUNB overexpression | EdU, read around E16.5 to E17.5 | EdU+ GFP+ IP-N/RG ratio (cell-type proportions of EdU+ electroporated cells) | n = 4 and 4, ONE litter |
| M3 | 4e | mouse, E15.5 electroporation, BrdU or EdU E16.5, read P1 | JUNB overexpression | P1 | fraction of electroporated NEUROD2+ cells born after the first 24 h (a FRACTION, not a count) | n = 6 and 6, several litters |
| M4 | 4f, ED13h,i | mouse, Tracker-seq (lineage barcode + scRNA-seq), collected at P0 | JUNB overexpression | P0 (about 4 days after electroporation) | neuron number per RECOVERED clone and clone-size distribution (denominator = clones recovered, not starting progenitors); 16,000 control and 50,000 JUNB cells sorted | clones, chi-square; four littermates per condition in the collection |
| M5 | 4g, ED13j,k | mouse | JUNB overexpression | E16.5 | G1/S fraction of electroporated RG (pFUCCI, n = 5 and 6) and snRNA-seq cell-cycle phase | animals |
| M6 | 4h, ED13l, 14 | human in silico (CellOracle), CUT&Tag | none measured as output | n/a | simulated targets and trajectories | not data on neuronal output |
Species and perturbation facts fixed now: the human arm is a KNOCKDOWN with one early time; the mouse arm is a GAIN OF FUNCTION with early and later readouts; they are opposing perturbations in different species, so they can never form a within-preparation pair, and no effect is compared across them.

## Readings (fixed)
* **D-matched (strong):** an early ratio and a later absolute output or yield per starting lineage carry different signs in the SAME arm, measured on the SAME animals or the same cultures, each with an identified denominator and the animal or culture as the unit.
* **D-group (weak):** the two carry different signs for the same perturbation and species but come from different cohorts, readouts or denominators; a sign difference at group level, not a within-preparation effect.
* **N:** no pair of that kind exists in the paper.

## Decision rules for INV-17 (fixed)
1. **CLOSE as duplicate:** INV-17's stated next_test already requires (a) absolute counts of progenitors and neurons in both windows, and (b) an error condition for a shrinking pool, so that a favourable ratio beside a smaller pool or smaller neuron count would be visible in its own numbers. If the paper's pair is D-group or N, or if it differs from INV-17's design only by a label, CLOSE.
2. **CARRY a rule to IT** only if the paper shows (i) a pair that is D-matched, or a D-group pair whose early readout is a ratio or fraction with no absolute count, so that an absolute-count design read only at the end of the window would have looked favourable while the early ratio looked the other way, AND (ii) INV-17 as written does not already prescribe a read at a stated time later than the end of the lowering window or a count per starting unit. The rule would be: an early favourable ratio or fraction is not rescue unless a matched later absolute yield per starting unit and a progenitor-pool measure agree. It must change interpretation or design beyond "absolute counts".
3. **Insufficient as an addition:** if the pair exists only across cohorts or modalities and INV-17 already reads absolute counts, record a one-line design note without a rule (weak is valid).

## Replicate unit and direction checks I will make (fixed predictions)
* Fig 4c: the direction of the per-organoid mean N/RG ratio is knockdown above control; the organoid (not the ventricle or the cell) is the replicate unit; I expect ventricles to be nested and the per-organoid test to be the honest one. If the per-organoid data show overlap or one organoid driving the difference, the Fig 4c direction is stated as fragile.
* Fig 4d to 4g: check whether the unit is the embryo or the litter and whether any mouse pair of early and later readouts uses the same animals; I expect it does not (the legend says one litter for 4d, several for 4e to 4g, and Tracker-seq pools four littermates per condition).
* One small within-model source-data comparison is run ONLY if a matched pair (D-matched) is found. Otherwise none, and the result states why.

## Limits stated now
Adjacent, non-WWOX; a transcription-factor perturbation; no MYC arm; one preparation per species. A late significant result beside an early non-significant one does not date an effect; cross-species and opposing perturbations cannot show a within-preparation effect; no cross-species effect estimate; no raw scRNA-seq download; no JUNB intervention; no compound; no ranking change. Reading depth will be stated honestly: Fig 4 and Extended Data 12 to 13 legends and Methods read as text; numbers only from the source-data workbook if reachable by a plain request.

## Rejecting observation (named in advance)
Per-animal source data in which the early IP-N/RG ratio and a later absolute yield come from the same animals and carry different signs would overturn "N" and make rule 2 applicable; per-organoid source data in which knockdown does not exceed control would overturn the Fig 4c direction.

## Consumer
ADV (result and path). IT only for rule 2 (an added INV-17 interpretation rule), and only if it applies.
