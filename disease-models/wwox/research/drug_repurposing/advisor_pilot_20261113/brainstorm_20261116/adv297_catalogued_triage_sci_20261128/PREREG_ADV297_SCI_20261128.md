# ADV-297 pre-registration: can an abstract-and-metadata triage find the decision-bearing records among the catalogued-only records without a receipt? (SCI, window fc428159)

Frozen at 2026-11-28T05:32:12Z, before any abstract, title or article text of the ten drawn records was opened by this unit (landing hash recorded by the commit). Seen before freezing: the coverage report counts, the registry entry ids and PMIDs of the ten, and nothing else about them. Hypothesis level; reference genotype class only; nothing here is medical advice. Assignment: `assignments/ADV-297.md` (question, prediction and rejecting observations are ADV's).

## Draw

* Population: `coverage_report.py`'s catalogued-only entries with no receipt, computed on the ledger of this tree: 194 entries (sha256 of the sorted id/PMID list 9634672fd3309b60dd5b0bb705cb4ac451359f04233232a053903a8e5f43ba45); 6 have no PMID. PMID 42422765 is excluded in every search and listing.
* Script `draw_adv297.py`, seed 20261128, `random.Random(seed).sample(sorted_pool, 10)`.
* Drawn, in draw order: 1 CORPUS P399 (16116962); 2 CORPUS P252 (26120275); 3 CORPUS-STUB-197 (31829254); 4 CORPUS P247 (25502636); 5 CORPUS P214 (no PMID); 6 CORPUS-STUB-136 (32931356); 7 CORPUS P376 (25662954); 8 CORPUS P375 (26910372); 9 CORPUS P364 (20367991); 10 CORPUS-STUB-071 (17690733).
* No replacement draw: a record that cannot be reached stays in the table as an access result and leaves the denominator.

## Step A, triage

Reader: legend-delegate, claude-sonnet-5-5, effort high, one dispatch, no repository access, no web: it receives one packet with, per record, title, journal, year, abstract (NCBI efetch, or "no abstract") and the registry entry's fields "tier (fase 1)" and "clinical relevance" if present, and no other registry field (no claim links, note, status or next action). The packet is built by script; SCI does not choose or edit its content.

Frozen call rule, given to the reader verbatim:

> The project studies WWOX loss in the developing human brain (early-onset epileptic and developmental encephalopathy, reference genotype class): what the gene does in neurons and glia, what goes wrong when it is lost (seizures, myelination, development, metabolism, signalling partners), which drugs or interventions could be compared for it, and how those would be measured. Its working files hold sentences about these, each tied to sources.
>
> Call each record, from its title, journal, year, abstract and metadata only:
> * **READ-NOW**: the abstract reports original data on WWOX (or its orthologue) in neural tissue or cells, in a WWOX-deficient organism or cell, or in people with WWOX variants; or an intervention or drug tested where WWOX is lost or manipulated; or a method or assay that measures WWOX function or its direct partners.
> * **READ-LATER**: original data in which WWOX is measured or manipulated outside those settings (for example cancer tissue, an association study naming WWOX, another organ), or a review focused on WWOX; or there is no abstract and the title concerns WWOX.
> * **DISCARD**: WWOX is incidental (one gene in a list with nothing stated about it), absent from title and abstract, a different gene sharing a name (for example plant WOX1), or a non-original item with no WWOX focus.
>
> For each record give the call, the abstract words that decided it, and one line saying what the full text could hold that the abstract does not show.

## Step B, full-text check

Readers: legend-delegate (claude-sonnet-5-5, effort high), different from step A, one at a time, in two or three consecutive batches. They are not shown step A. Source: held copy first; else the open full text through PubMed Central efetch or Europe PMC (a 401, 403, 429, challenge page or 5xx is a result; no paid route; no contact; no e-mail address to any service), fetched by SCI by script into the job scratch, untrusted data. Abstract-only reach is an access result, not a full-text check. Main figures and supplements are looked at when they are held or openly retrievable with the text; what was not looked at is stated per record, and the check is then "text and tables" and says so.

## Matching rule for a decision-bearing datum (one rule, frozen)

A datum counts only if **all** hold:

1. it is the record's own result or observation (measured, analysed or reported cases), not a citation of someone else's;
2. the reader names, by file and line, a held sentence, comparator row, card cell, dossier statement or open question in the repository (claim registry, working model, disease model, discovery ledger, therapeutic hypotheses ledger, open questions, drug-repurposing cards and comparators);
3. adopting the datum would change what that sentence says (reverse it, narrow or widen its scope, add a species, unit, dose or evidence level, or answer or reframe the open question). Adding one more citation to a sentence that would read the same does not count; a background fact no held sentence depends on does not count.

The reader also lists, apart and uncounted, data that meet 1 but not 2 or 3.

## Score

* **MISS**: step A called DISCARD or READ-LATER and step B reports at least one datum meeting the rule, **and** a second blind reader (given the held sentence, the datum's source and the rule, not step A and not the first reader's verdict) agrees that the sentence would change. Disagreement: listed apart, not a miss.
* **Confirmed call**: READ-NOW with at least one datum meeting the rule, or DISCARD or READ-LATER with none. READ-NOW with none is a false alarm: not a miss, not confirmed.
* SCI checks every MISS on the original before it counts, and does not re-grade the other records.

## Prediction and rejecting observations (fixed by ADV before reading)

1 miss of 10 (range 0 to 3); at least 7 of 10 calls confirmed. Two or more misses: abstract-only triage is not safe for this tail. Zero misses with seven or more DISCARD: the 194 can be parked by this rule plus a standing 1-in-20 audit. Between: report counts only. **Denominator**: the two thresholds are applied to the records that reach step B; if fewer than seven reach it, the result is "not decidable from this draw", with the counts and access results, and no parking or rejection is claimed.

## Budget and limits

About two hours, one delegate at a time, `df` at least 1.5 GB before each dispatch and 2.0 GB before a push; no image rendering in SCI's context. Sealed ADV-174 and ADV-175 material and the frozen RP-045 prediction untouched. A ten-record draw gives counts, not a rate for the 194.
