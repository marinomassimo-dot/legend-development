# Pre-read checklist for a paper that a consumer sentence leans on (closing item of ADV-276, SCI, 2026-11-25)

Hypothesis level; reference genotype class; nothing here is medical advice. Source: the corrections found in ADV-276 (and one of our own, section "Six more checks") (increment 1, five leads, 30202070, four routed leads, step 2 batches 1 and 2: 37 papers read from acquired bytes with a consumer sentence; 16 strict corrections and 23 changes in all; no reversal of a direction). The corrections were never about the sign: they were about what was measured, in whom, when, and from which unit. Use the list before a consumer sentence is written or repeated, and again before the paper is called read. It gates nothing; a line that does not apply is skipped.

## The five classes (each with the question to ask and the cheapest place to look)

| # | Class | Ask | Where to look |
|---|---|---|---|
| 1 | **Window** | For each number: who was exposed or recorded, at what age, when, for how long, at what temperature? Is the window the exposure, the recording, or only the recovery before it? | Methods sentence that gives the recording or dosing (not the legend); supplementary Methods; figure timeline. Examples: slice recovery at 23 C is not the recording temperature; 5-min DMSO baseline, 10-min drug equilibration, 5-min recording; fructose through the dam's diet, not given to neonates; maternal and neonatal windows are different exposures. |
| 2 | **Unit under n** | What does each dot in the panel stand for (animal, litter, culture, well, cell, axon, organoid)? Is the printed n the unit the test used? Are before and after the same units? | Source-data sheet (count the rows), legend n, the test named in Methods. Examples: g-ratio per axon under "n = 3 mice"; wells under "3 experiments"; the same organoids before and after drug tested with unpaired tests; two lanes of the same animal as n = 2. |
| 3 | **Species, preparation and age** | Which species, strain, sex, age and preparation carry the mechanism, and is it the same as the one the sentence names? | Supplementary Methods for primary cultures (primary microglia are usually pup-derived: the host's age is not the preparation's age); cell-line identity; promoter and driver specificity (a CMV-driven vector is not cell-type specific); which cells were in the dish. |
| 4 | **The test behind the p** | Is the p value printed or computed? Does it reproduce under the test the legend names? Is a "significant" in one arm set against a "not significant" in another without an interaction test? Are the animals that were measured later survivors? | Recompute from the counts or the sheet (paired against unpaired; chi-square with and without correction); read the mortality or dropout figure before repeating a later benefit; look for "P =" printed in the figure, not only an asterisk. |
| 5 | **"All", "every", "none", "absent"** | Does the paper's own table or source data contradict a general statement at one time point or one group? Before writing "absent", was the whole XML searched (title, abstract, legends, references) and the supplement text, and the query dated? | Source-data sheet behind the claim; the count per time point; a full-text search including the abstract. Example: "all division modes at every induction day" against D15 = 0 proliferative of 40; "myelinated area per cell" reported absent after a body-only search, present in the abstract. |

## Six more checks that recurred

* **Table footer rows in XML are not table body rows:** a JATS `<tfoot>` row can carry cell values that belong to the body (an unlabelled "Low 4 2 3 9" row in 35222658 Table 3 was given to the wrong group, and a false "p values do not reproduce" finding followed, corrected 2026-11-25). Before assigning an unlabelled row to a group, read its position in the markup and test the assignment against the group totals and the other tables' margins.

* **Variance from all eligible rows, never the called ones:** a spread (SD, CV) taken from rows selected by their outcome is narrower than the spread of the eligible rows (ADV-278: five up-called deposits SD 0.22 against 0.26 on all eight eligible rows; the planning n follows the wider one). Name the eligibility rule beside every spread.
* **Who was measured:** a receptor, a cell class or a compound named in the sentence must be the one on the axis (a non-selective inhibitor is not a selective one; a cocktail is not one drug; an opener-defined current is not a blocker-sensitive current).
* **Which source holds the number:** label every number carried from a workbook or figure by sheet, panel and row, never by position; mark a figure reading as an image reading; when a ledger line says "read in full", open the artefact that carries the number.
* **A clause in the brief that belongs to another source** (our own data set beside the paper's) must be labelled as such, or a reader will search the paper for it.
* **A negative has a date and a query** (epistemic_discipline section 2.4): an access failure, a 503 or a timeout is a route result, not a finding.

* **A table printed as an image is invisible to a text search:** look at the supplement pages (ADV-279: the fit table of 37275776 showed that a value written for the wild-type channel mixed in the patient variant).

* **Sibling panel:** before carrying a number from one panel, find the same condition in every other panel (ADV-279, 30266908: 1.8 fold in panel a, 1.0 in panel b).

* **A micrograph location statement covers every arrowhead in every enlarged panel,** not only the boxed regions (27845895: one intranuclear cluster overturned "outside the nucleus"). Word the blind statement the same way.

* **A held file is not a read until its bytes are what its name says:** HTML error pages saved as figures or PDFs exist (ADV-279: 39 mismatches in 6,100 held files).

* **The blind reader gets the repository sentence, not the fact** (ADV-280: a facts-only second reading agreed with the first reader on every fact and the batch scored strict 0 of 10; a second reader given the verbatim consumer sentences found both strict items, one of them a card parenthesis that called all of a paper's NADH assays dye-reduction measures when only one was, and a ledger line that called every figure republished when two legends said so). Build the sentence file first (verbatim, verdicts MUST CHANGE / ADD / STANDS, "do not assume right or wrong") and send it with the sources.

* **A description of the source's own assays, figures or concentrations repeated from memory** is the commonest strict error: reopen the Methods and the legend that the sentence describes, and count the conditions in the panel against the number the sentence names (ADV-280: "three concentrations" where six were tested).

* **A null needs its activity check:** an inhibitor arm read as "did nothing" (chloroquine at one dose, 16 h, in two variant maps) is a placed route only if the paper shows the inhibitor acted; search text, supplement and source data for the positive control and date the negative.

* **A faint band on a very small strip is measured, not judged:** average the band rows against the rows above and below per column block before changing "faint residual" (ADV-280, 36926521: a shallow dip of 9 to 19 grey levels in every block, which a second reader had called "not a band").

## Use

Before the first read: write the five questions on the PREREG with the paper's consumer sentence. After the read: one line per class in the result (the class of correction this batch found), and the second reader (a blind delegate, stated model and effort) judges every sentence proposed for change. Observed rate: about two reads in five need a strict correction (16 of 37) and about three in five some change (23 of 37), on consumers that were mostly narrow earlier readings; a result with none is possible and must not be forced.
