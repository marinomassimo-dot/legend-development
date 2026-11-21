# ADV-135 / RP-035 pre-registration (IT, 2026-11-21), committed BEFORE any human report is read for these analytes

Reference-genotype class only; aggregate published literature only; hypothesis level; no dose, no schedule, no recommendation; nothing here is medical advice. No individual-level record is created, stored or linked: a published case report is cited as a source with its case count, its age band and the sentence it prints, never as a person.

Limit stated first: every reader in this work is a model of the same family; no clinician or native specialist has read a source. A count of held files is a count of mention in text, not of measurement.

## Question (ADV-135, assignment text)
In the published human WWOX-DEE (WOREE) and SCAR12 reports, which early laboratory findings are stated for calcium (total or ionised), phosphate, glucose, lipids, cortisol or adrenal measures, thyroid, growth hormone or IGF-1, and a metabolic work-up in general; at which age; in how many cases; normal, abnormal or not reported?

## Discriminating observation, fixed now (ADV's wording, made operational)
* **Does not translate:** calcium or lipids stated normal at an infant age in at least two independent human reports, each with the age and the case count stated, the strand closes with the sentence "the pup sign does not translate to the reference genotype class in the reports read".
* **Shared:** calcium or lipids stated abnormal at an infant age in at least two independent human reports: the sign is shared, RP-035 hands the lever-class question back to ADV.
* **Neither:** a named missing measure, stated per analyte (the usual outcome in case reports).
* The two thresholds are evaluated separately for calcium and for lipids; one analyte cannot borrow the other's reports. Glucose, phosphate, cortisol or adrenal, thyroid, GH or IGF-1 and the general work-up are tabulated and decide nothing alone; they are reported per analyte in the same three states.

## Operational definitions (fixed now)
1. **Human report:** a published paper with at least one human case carrying a WWOX biallelic or reported pathogenic genotype in the WOREE or SCAR12 spectrum (or a series that contains such cases); animal and cell papers are not human reports. A review that restates a case is a restatement, not a report.
2. **Independent reports:** reports from different cohorts. A case restated in a later series, a series that includes the cases of an earlier report, or two papers by one group on one cohort count once; the overlap is named when found (the one already known: the 64-child cohort of one group probably contains two children reported separately).
3. **Infant age:** a stated age up to 12 months, as the report states it; "neonatal", "first days of life", "in the first weeks" and "at birth" count; an unstated age, "early", or an age beyond 12 months does not count for the translation test and is tabulated as its own row.
4. **Normal:** the report states the analyte, or a named work-up that includes the analyte, within normal limits or normal. A general statement ("metabolic work-up normal", "laboratory tests unremarkable") is normal for the analytes the report names and for nothing else; it is tabulated under the general work-up row and is never counted for calcium or lipids unless the report names them.
5. **Abnormal:** the report states a value or a finding for the analyte outside the reference range, or calls it low, high, hypo-, hyper-, or deranged, at the stated age. "Hypoglycaemia" is the glucose row; "failure to thrive" is a growth finding, not a laboratory finding, and is listed apart.
6. **Not reported:** no sentence of the report names the analyte or a work-up that includes it. Unreported is not normal.
7. **Counts:** a report counts once per analyte and state; the case count is the number of cases in which the report states that state; a series stating a state for "all" or "n of N" is counted as stated.

## Method
1. Held material first: a counted scan of the held human dossiers (`disease-models/wwox/research/fulltext_dossiers`), the paper registry rows (by record, `registry_records.py`, never a whole-registry read) and the held full texts (`files/fulltext` of the primary checkout, read-only) for the analyte terms (English and the common abbreviations) and for the words 'metabolic work-up', 'laboratory', 'biochemical', 'failure to thrive'. The scan script, its term list and its raw counts are persisted. A scan hit is a prompt to read, never a finding.
2. Complete reads (receipt and verbatim locators) only for held reports that state any such finding; the quoted sentence is carried with its locator; a quotation read from a dossier or an abstract is labelled with that depth.
3. External retrieval by plain clients only for reports not held that Europe PMC or PubMed list for the WWOX human spectrum with these analytes; a challenge page (captcha) is a STOP for that route, recorded as the route result; an absence claim needs two routes; no contact-address service and no operator e-mail is sent anywhere; no browser-header spoofing.
4. One blind verifier (a delegate with model and effort stated and read back; one at a time, none recursive) re-reads every sentence that decides a threshold against the source text and re-counts independent reports; it receives the sentences and sources, never this table's conclusions.
5. Counters carried in the result: case reports select severe cases; a normal work-up at one age says nothing at another; unreported is not normal; the denominator of any "n of N" is the report's own; an abstract-level read is named as such.

## Output
`RESULT_ADV135_IT_20261121.md` with the answer first, a per-analyte table (reports, ages, case counts, state, sentence with locator, reading depth), the overlap list, the route results, the threshold verdict for calcium and for lipids, the missing measures by analyte, what the result changes for the pup-axis measurement, and the cost; delivered to ADV and SCI.
