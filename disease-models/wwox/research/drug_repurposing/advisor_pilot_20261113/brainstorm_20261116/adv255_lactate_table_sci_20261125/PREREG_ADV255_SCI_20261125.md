# ADV-255 pre-registration: human lactate per report in WWOX deficiency (SCI; hypothesis level; reference genotype class; not medical advice)

Frozen before any search of the held sources for lactate in this assignment.

## Already seen by the writer (not a prediction)

From the ADV-254 session and the assignment text: PMID 35573960 is said to report small MRS lactate peaks at one age and none at a later age; `meta/meta_metabolism_current.md` says "mildly elevated lactate" for a Chong 2023 case, unchecked; an earlier laboratory-sentence table calls the metabolic work-up normal in 11 reports; DL-BIO-009 cites 30361190, 24456803, 38161429 and 30362252.

## Inclusion rule

* One row group per publication reporting humans with biallelic WWOX deficiency (any phenotype), primary observation only. A review or database restatement is listed as secondary and not counted.
* Counted: statements read in a held full text, table or supplement. Abstract-only statements are listed, marked `abstract-level`, and not scored.
* Aggregate only: where a publication has several subjects, counts per direction and the age or age range as printed; no per-subject rows.
* A family republished is counted once when the later paper says so; otherwise the possible overlap is noted.

## Search (two routes)

1. `git grep` for `lactat|lactic|lattat` over the tracked WWOX files, followed to the source it names.
2. Every held text under `files/fulltext/` (root checkout) that names WWOX and matches `lactat|lactic`; for PDFs without a text copy, `pdftotext`. The number of held human WWOX reports with no lactate word is reported as far as it can be established.

## Directions

* `elevated`: authors call it raised or report a lactate peak, or the value exceeds the stated range; one time point suffices.
* `normal`: authors call lactate normal, report no peak, or the value lies inside the stated range.
* `low`: a value below the stated range, or authors call it low.
* `value only`: a number without a range or an author judgement; not classified.
* `work-up normal, lactate not named`: a general normal metabolic screen; not counted as a normal lactate.
* Blood, CSF and spectroscopy are kept apart.
* A publication **contradicts** "normal or low" if any sample at any time is `elevated`.

## Two-hit read

Each counted value is read in the source passage and again in a second representation (XML against PDF or page image, table against text). Where only one exists, the row says so.

## Expectations (scored in the result)

* E1: between 2 and 5 counted publications contradict "normal or low".
* E2: among counted publications that name lactate with a direction, at least half are `normal` in every sample.
* E3: the Chong 2023 source does state a raised lactate, as `meta_metabolism` says.
* E4: no counted publication states a lactate below range.
