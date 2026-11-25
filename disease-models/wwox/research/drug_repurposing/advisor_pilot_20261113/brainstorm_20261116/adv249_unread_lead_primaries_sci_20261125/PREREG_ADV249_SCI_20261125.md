# ADV-249 pre-registration: primaries behind discovery-ledger leads that were never read (SCI; hypothesis level; not medical advice)

Frozen 2026-11-25T03:10:48Z, before the listing was run and before any paper was opened. Effort high, no delegate, no spend, no contact. Written in the job scratch folder while a gated push held the worktree.

## What I had looked at (not blind)
The format of `discovery_ledger_current.md` (244 headed entries; a "Fonte" line in some), one entry in full (DL-MECH-014, already read under ADV-228) and the start of one other; receipt record fields; that 30 cards cite lead ids.

## Listing query
* A **lead** is a `DL-*` id; entries repeating an id are merged.
* Its **primary** PMIDs are those on its "Fonte" or "Source" line; if there is none, those in its heading; if none, the first PMID in its body (marked "first mentioned").
* A primary is **never read** if no receipt for that PMID that has not been invalidated records any of introduction, methods, results, discussion or figures as "read". A receipt that records only an abstract or a query does not count.
* Second route before "never read" is written for a chosen paper: the held files under `files/` and a search of dossiers, manifests and paper records for the PMID. A record that says the full text was read counts against "never read" and is reported as a ledger gap.

## Ranking
By the number of distinct consumers that cite the lead id: portfolio rows, investigation rows, cards, claim records, working-model records, trigger rows (the ADV-239 set). Ties: consumers citing the PMID itself; then therapeutic-hypotheses ledger records citing the lead; then lower lead number. Take the top six whose full text is held or openly readable; a challenge page, 403 or 429 is a route result and the next one is taken, with the skipped one listed.

## Per paper
1. What the lead says the paper shows (its own words).
2. What the paper shows, from Results and Methods.
3. Verdict on the lead's wording: **overstates** (a claim stronger, broader or in a different system or direction than the paper's data), **equals**, **understates**. A causal arrow counts as part of the wording; a lead that labels itself abstract-level is still judged on what it asserts.
4. A unit and independence statement for any numerical claim carried (ADV-247 taxonomy).
5. Contradictions inside the paper.
Then: promote to a PAPER record candidate yes or no; open questions with the observation that would answer them; wording for IT where overstated. Receipts record exactly the sections read.

## Predictions
* P1: of the papers read, the share whose lead wording overstates is between 0.33 and 0.67.
* P2: at least one paper contains an internal contradiction or a figure that does not carry its sentence (0.6).
* P3: at least four of the six are oncology or non-neural studies whose lead transfers a direction to neural cells (0.6).
* P4: no paper read changes a card's disposition (0.8).

## Rejecting observation
If every one of the six leads equals or understates its paper, the class is not a source of overstatement and that is the result.

Stop at 120 minutes in two increments; what was not read is listed.
