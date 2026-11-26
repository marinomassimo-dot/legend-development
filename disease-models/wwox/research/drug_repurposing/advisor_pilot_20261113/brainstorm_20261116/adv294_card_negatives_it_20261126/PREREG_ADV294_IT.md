# PREREG, ADV-294: dated search over the first ten card negatives (IT, frozen 2026-11-26T01:07:16Z)

Hypothesis level; nothing here is medical advice; reference genotype class only. Frozen before the universe is counted
and before any search is run. Brief: `assignments/ADV-294.md`. Held bytes and repository text only; no external
search, no spend, no contact; the Obeid 2026 article (PMID 42422765) is not opened.

## Universe
* Unit: one sentence of one string in `cards/*.packet.json` (30 packets), split on ". " and line breaks.
* Mention: the sentence contains `WWOX` (any case), `Q230P` or `Gln230Pro`.
* Negative: the sentence matches, case-insensitive, one of:
  `unmeasured`, `(not|never) (been )?(measured|held|read|tested|assessed|examined|established|determined|studied|reported|known)`,
  `untested`, `unknown`, `unread`, `no (held |direct |measured |published )?(measurement|datum|data|record|study|reading|source|test|result|report|assay|value|evidence)`,
  `(none|nothing) (is |was )?(held|measured|read|tested|known)`, `has no (held )?(measurement|datum|data)`,
  `no [^.;]{0,60} (is|are|was|were|has been|have been) (held|measured|reported|known|tested)`.
* One sentence repeated in one packet counts once. My count may differ from checkpoint 26's 39 and 143: its regular
  expression was not recorded.

## Ranking and the ten
1. Cards ordered by consumers: the number of tracked files, outside `cards/`, that contain the full card stem
   (`git grep -l -F <stem>`). Ties: card stem.
2. Inside a card: rendered on the shareable page first, then on the full page only, then not rendered; then packet order.
3. At most three sentences per card, so the ten cover at least four cards.
4. A sentence that is not a negative about a measurement or a holding on reading it (for example a design statement) is
   listed as screened out and the next one is taken.

## Search recipe (one dated search per sentence)
* Corpus: `research/deepdive_manifests/*.json`, the claim, paper and literature registries, the receipt ledger, and
  the text of `files/fulltext`, `files/supplement` (xlsx, docx, pdf, zip members extracted) from the root checkout;
  `files/figures` by file name only, plus the figure itself when a hit points to it.
* Per sentence: the query terms (entity AND measurement word, with synonyms) are written before the run; hits are
  counted per file; at least two hits of every counting query are read before a number is reported.
* Limits stated with each verdict: image-only tables and unextractable files are not searched.

## Classes
STANDS (search dated, nothing found), WRONG (a held source carries the datum), NARROWER (true only for a stated
material, species, assay or age), UNSETTLED.

## Prediction and rejecting observation (ADV's, adopted)
WRONG or NARROWER in 3 of 10, range 1 to 5. If none of the ten is WRONG or NARROWER: stop; the remaining sentences are
not worth a sweep. If 3 or more change: ADV registers the rest for SCI/HE.

## After
Changed sentences go through a blind packet that carries the sentence PLUS the dated search; negatives are marked
UNSETTLED for the reader. Then card chain and copied-sentence check.
