# PREREG ADV-272: acquire the not-held partials with consumers by permitted open routes (SCI, 2026-11-25)

Written before the 421 were listed or ranked, before any Europe PMC request for this assignment, and before any download. Hypothesis level; reference genotype class; not medical advice. Actor `orchestrator` (SCI).

## Rules
* No spend, no contact with authors, no e-mail address or contact-address resolver, no browser identity (declared plain client only), no bursts (one request at a time, a pause of at least two seconds between requests, none to PMC in parallel), no bypass: a challenge page, 401, 403, 429 or reCAPTCHA is a result, recorded and never retried in a burst. The sealed ADV-174/175 material and the frozen RP-045 prediction are not touched.
* Population: latest receipt of each study has depth `partial_fulltext_read` and `held_studies.py --rows not-held` lists it (HE's tool; ADV counted 421). The count is checked first; a different count is reported, not forced.
* **Ranking rule (frozen, the ADV-265 method):** units = canonical consumers named in the ADV-265 surface list (claim, model, lead, hypothesis, card, portfolio and ranking rows), searched by PMID and by the study's PAPER id and DOI; rank by the number of distinct consumer units found by route 2 (unit text), ties by route 1 (files naming the id), then by PMID ascending. CORPUS and LIT ids are not used. Unit ids are listed.
* **Open-access flag:** Europe PMC REST `search` by `EXT_ID` and `SRC:MED`, fields `isOpenAccess`, `hasSuppl`, `pmcid`, no e-mail parameter. An absent record is "not indexed".
* **Acquired** means: the artefact is stored under `files/fulltext/` (root checkout, gitignored) by a permitted route; its SHA-256 is recorded; the paper's own title is found in the first page or the XML front matter and agrees with the PMID; page count (PDF) or section and figure count (XML) is recorded; and it is not a challenge page. A receipt is recorded only for a paper actually read (Step 4), never for an acquisition alone.
* The unacquired go to a NEW file `files/operator_inputs/PDF_REQUEST_LIST_ADV272_20261125.md` (rank, PMID, title, consumer units, route result), not an edit of the existing list.

## Predictions (fixed now)
* P1: of the top 25, **9** carry `isOpenAccess = Y` (range 5 to 14). Rejecting observation: fewer than 5 or more than 14.
* P2: **7** of the top 25 are acquired and verified by the rule above (range 3 to 11); the number acquired is at most the number flagged open.
* P3: at least three top-25 papers flagged non-open return a route result (paywall page, 403 or no full text) when a plain request is made once; none is retried.
* P4: at least one acquired paper holds a figure, table or supplement that its latest receipt lists as unread. Rejecting observation: none does.
* P5: at least one acquired artefact fails verification (wrong paper, challenge page, truncated). The held `.xls` file of PMID 24932569 that is a saved reCAPTCHA page (HE, 2026-11-25) is the known precedent.

## Not promised
No claim, card or registry is edited. Any read in Step 4 follows the ADV-269 rules: sheet and row named for every workbook value, the replicate unit beside every number, the full consumer row read before anything is called new.
