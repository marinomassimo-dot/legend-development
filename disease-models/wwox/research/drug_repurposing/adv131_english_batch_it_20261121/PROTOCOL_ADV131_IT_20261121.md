# ADV-131 protocol (IT, 2026-11-21): measured first batch of English-authored shareable passages in fr, de and es

Written BEFORE the first translation and committed before any catalogue entry exists. Reference-genotype class only; interface and page text; no scientific content decision; nothing here is medical advice.

## Question
Is translating the English-authored passages of the SHAREABLE fr, de and es pages (HE's upper bounds: fr 735 loose / 491 strict sentences, de 397 / 213, es 541 / 327) affordable and faithful at the measured rates, and is the translation or the section notice the proportionate treatment for the edition that leaves the repository?

## Scope (fixed now)
* At most 50 distinct English-authored passages, from the two most visible shareable sections only: `overview` first, then `ranking` from its top, in painted (document) order, distinct by text hash. Nothing outside those two sections.
* The list is read from the shareable fr page as built on `main` after ADV-130 (the language whose detector marks the most nodes), and every selected passage is checked to be painted as English on the de and es pages too.
* Batches of 25 passages (one batch is 25 passages x 3 languages = 75 rows). Batch 1 = passages 1 to 25, batch 2 = passages 26 to 50, in that order; batch 2 starts only if batch 1 passes the stop rule below.

## Method
* Translation into fr, de, es by the producer (this IT window), kept in the content catalogue (`view/i18n/content_<lang>.json`, keyed by the passage's text hash) the ADV-129 way; every number, name, identifier, hedge, limit and negation of the source is kept; no sentence is added, merged or dropped; register of a scientific report.
* Renderer change, minimal and removable (for HE's review): a scope file `view/i18n/en_scope.json` lists the selected hashes; the inventory collector adds a raw English text node whose hash is listed (source `en`), and the existing node pass swaps a listed node for its translation when one exists; with none the node stays English (the section notice labels it). No other text is touched.
* Blind check per batch: a different reader (a delegate, one at a time, model and effort stated in the dispatch and read back from its transcript) receives only the source passage and the three renderings, never the producer's notes or this protocol's stop rule. For each passage-language row it answers FAITHFUL (same meaning, same numbers, names, hedges and limits), MINOR (wording or register only, meaning intact) or CHANGED (meaning, a number, a name, a hedge, a limit or a negation differs, or something is added or lost).
* MINOR rows are repaired with the delegate's own suggested wording; a repair that changes more than a word needs a third look (counted and reported).

## STOP RULE (written before the first translation)
The work STOPS, with the batch repaired and reported and NO further batch, when either:
1. CHANGED rows exceed 5 percent of the rows of a batch (more than 3 of 75), or
2. any CHANGED row alters a number, a limit, a hedge or a negation (even if rule 1 is not reached).
Stopping is a result, not a failure: the projection paragraph is then written from what was measured, with the stop named as the finding.

## Recorded for each batch
Rows by verdict; MINOR repairs and how many needed a third look; delegate model and effort (read back), tokens or minutes; producer minutes; rates per passage and per row; painted before and after for the two sections (count of the selected passages painted as English on each page, 1280 px, through the Chromium probe); tests run.

## Closing paragraph (after the batches)
Projected cost and time of the full set at the measured rates; remaining risk; whether the notice or the translation is the proportionate treatment for the shareable edition.
