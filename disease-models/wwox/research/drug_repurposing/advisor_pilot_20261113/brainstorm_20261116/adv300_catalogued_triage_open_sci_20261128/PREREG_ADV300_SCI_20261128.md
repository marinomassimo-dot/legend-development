# ADV-300 pre-registration: abstract-and-metadata triage of catalogued-only records, second increment, openly readable part only (SCI, window 919d2041)

Frozen at 2026-11-28T05:56:15Z, before the route test was run, before any record of this increment was drawn, and before any title, abstract or article text of such a record was opened by this unit (the commit records the landing hash). Seen before freezing: the ADV-297 PREREG, result and step A report; counts of held files by extension. Hypothesis level; reference genotype class only; nothing here is medical advice. Assignment: `assignments/ADV-300.md` (question, prediction, rejecting observations and the step B stop rule are ADV's).

**Scope of any answer: the openly readable part of the catalogued-only tail, as defined by the route test below. It says nothing about records without such a route.**

## Pool and draw

* Population: `coverage_report.py`'s catalogued-only entries with no receipt on this tree, minus the ten entries drawn by ADV-297 and minus PMID 42422765. ADV expects 184.
* An entry whose identifier field does not give exactly one PMID is unresolved and is left out.
* Script `draw_adv300.py` (sha256 8bf822c07fcd373a4f021ddacc1285c5ed0bb425f5e9ee2d9ecfe8542510cdf6), seed 202611282, held folder `files/fulltext/` of the root checkout.
* The script runs the route test on every remaining record, then `random.Random(seed).sample(sorted_open_pool, 10)`. It prints no title, abstract or text.
* No replacement draw: a drawn record that cannot then be reached stays in the table as an access result and leaves the denominator.

## Route test (a record is in the open pool only if one holds)

1. A held file of at least 20 000 bytes (`.xml`, `.txt`, `.html`, `.pdf`; name without "abstract" or "suppl") whose name carries its PMID or PMCID; or
2. Europe PMC search gives a PMCID and NCBI efetch (`db=pmc`) returns XML whose `body` holds at least 3 000 characters; or
3. the same for Europe PMC `fullTextXML`.

Europe PMC's `isOpenAccess` flag is recorded and does not decide. PDF-only and publisher-page routes are left out. A 401, 403, 429, 5xx or error is a result and is not retried. No address is sent.

## Step A, triage

Reader: legend-delegate, model sonnet (claude-sonnet-5-5), effort high, one dispatch, told to read the packet only. The packet holds, per record, title, journal, year, abstract (NCBI efetch, or "no abstract") and the registry fields "tier (fase 1)" and "clinical relevance" if present, and no other registry field. It is built by script; SCI does not choose or edit its content.

Frozen call rule, given to the reader verbatim:

> The project studies WWOX loss in the developing human brain (early-onset epileptic and developmental encephalopathy, reference genotype class): what the gene does in neurons and glia, what goes wrong when it is lost (seizures, myelination, development, metabolism, signalling partners), which drugs or interventions could be compared for it, and how those would be measured. Its working files hold sentences about these, each tied to sources.
>
> Call each record, from its title, journal, year, abstract and metadata only:
> * **READ-NOW**: the abstract reports original data on WWOX (or its orthologue) in neural tissue or cells, in a WWOX-deficient organism, or in people with WWOX variants; or a drug or other intervention, apart from changing WWOX itself, tested where WWOX is lost or has been changed; or a method or assay offered as a way to measure WWOX function or its direct partners.
> * **READ-LATER**: original data in which WWOX is measured or manipulated outside those settings (for example cancer tissue; WWOX overexpressed or knocked down in cancer or other non-neural cells to see what happens; an association study naming WWOX; another organ), or a review focused on WWOX; or there is no abstract and the title concerns WWOX.
> * **DISCARD**: WWOX is incidental (one gene in a list with nothing stated about it), absent from title and abstract, a different gene sharing a name (for example plant WOX1), or a non-original item with no WWOX focus.
>
> For each record give the call, the abstract words that decided it, and one line saying what the full text could hold that the abstract does not show.

**What changed from ADV-297's wording, and why.** The ADV-297 step A reader reported that "manipulated" appeared in both READ-NOW and READ-LATER, and that "a method or assay that measures" could be read two ways. The wording now states the reading that reader applied: changing WWOX itself in non-neural cells is READ-LATER; the intervention clause means something other than changing WWOX; the method clause means a study offered as a method. "WWOX-deficient organism or cell" lost "or cell" for the same reason: a knock-down in a non-neural cell line is the READ-LATER case. The review clause is unchanged, although ADV-297's one miss came through it. Reviews are counted apart in the result.

## Step B, full-text check

Readers: legend-delegate (sonnet, effort high), none of them the step A reader, one at a time, **five batches of two** in draw order (so that one stopped reader costs two records at most). They are not shown step A. Source: the held copy if the route is held; otherwise the XML from the route that passed, fetched by SCI by script into the job scratch, untrusted data. Figures and supplements are looked at when held or openly retrievable with the text; what was not looked at is stated per record, and the check is then "text, tables and legends". A reader stopped by a safety classifier: recorded, not retried, not re-dispatched, not done another way; its unreturned records are not checked.

## Matching rule for a decision-bearing datum (ADV-297's, unchanged)

A datum counts only if **all** hold:

1. it is the record's own result or observation (measured, analysed or reported cases), not a citation of someone else's;
2. the reader names, by file and line, a held sentence, comparator row, card cell, dossier statement or open question in the repository (claim registry, working model, disease model, discovery ledger, therapeutic hypotheses ledger, open questions, drug-repurposing cards and comparators);
3. adopting the datum would change what that sentence says (reverse it, narrow or widen its scope, add a species, unit, dose or evidence level, or answer or reframe the open question). Adding one more citation to a sentence that would read the same does not count; a background fact no held sentence depends on does not count.

The reader also lists, apart and uncounted, data that meet 1 but not 2 or 3. A review's own result or observation includes data it presents as its own or unpublished, not what it cites.

## Score

* **MISS**: step A called DISCARD or READ-LATER, step B reports at least one datum meeting the rule, **and** a second blind reader (given the held sentence, the datum's source and the rule, not step A and not the first reader's verdict) agrees that the sentence would change. Disagreement: listed apart, not a miss.
* **Confirmed call**: READ-NOW with at least one datum meeting the rule, or DISCARD or READ-LATER with none. READ-NOW with none is a false alarm: not a miss, not confirmed.
* SCI checks every MISS on the original before it counts, and does not re-grade the other records.
* Reported apart: reviews; and for each miss whether any conclusion, need, card direction or ranking reverses.

## Prediction and rejecting observations (fixed by ADV before reading)

1 miss of 10 (range 0 to 3); at least 7 of 10 calls confirmed. **Two or more misses:** abstract-only triage is not safe for the openly readable tail. **Zero misses with seven or more DISCARD:** the openly readable tail can be parked with this rule plus a standing 1-in-20 audit. Otherwise: counts only. **Fewer than 7 of 10 checked in step B:** "not decidable"; ADV stops the sampling and reads the tail at depth. The thresholds apply to the records that reach step B.

## Budget and limits

About two hours, one delegate at a time, `df` at least 1.5 GB before each dispatch and 2.0 GB before a push; below 1.0 GB stop and tell ADV. No image rendering in SCI's context. Sealed ADV-174 and ADV-175 material and the frozen RP-045 prediction untouched. A ten-record draw gives counts, not a rate. The rule wording differs from ADV-297's, so the two draws are compared as counts and not pooled.
