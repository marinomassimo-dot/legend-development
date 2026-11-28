# PREREG: independence of corroboration behind claim-registry sentences (SCI, 2026-11-28T19:49Z; hypothesis level; not medical advice; not edited once hashed)

Question (ADV, 2026-11-28; named pattern from checkpoint BH/BI): where a claim-registry sentence says that more than one
source supports something, do the sources carry different primary data and different authors?

Consumer: claim-registry evidence lines (repairs as one batch candidate by IT43, none by SCI) and the portfolio rows that cite
those claims. Rejecting observation: every checkable sentence rests on distinct primary data from distinct authors.

## Duplicate check (one pass)
ADV-008 (publication census), ADV-208 (wording edits), ADV-312 (myelin calibration), ADV-331 (blind P47T reading) and
PRESIDIO-005 (X1 design) do not ask this. Nearest earlier work: ADV-247 and ADV-261 (independence of the n INSIDE one claim
or inference), ADV-339 (scope words; its S6 found one failing corroboration, here K16). New here: independence BETWEEN the
sources a sentence names as supporting each other, over the whole registry.

## Enumeration (done before any source was opened)
`enumerate_corroboration.py` splits the registry (sha256 of the file is printed by the script:
24ded6322b1fa7f834b0075869f4d848fdcdb97b8312e491f5743e2b72c2815f) and keeps the 138 sentences with a corroboration term
(`term_sentences.tsv`). SCI screened them from the sentence text only. In: the sentence asserts that two or more
publications or datasets support one proposition. Out (`screened_out.tsv`): experiment or animal replicates; reader, audit or
digest verification; "X-independent" mechanisms; statements that support is absent, not independent or not replicated; revival
and promotion conditions; support inside one publication; convergence of computational methods. 23 sentences are in
(`candidates.tsv`). Recall limit: a sentence that asserts support without any of the terms is not found.

## Skip rule (frozen)
A sentence is BLOCKED-SKIP, its sources not opened, when its proposition concerns a drug, vector or treatment, or one of the
sources it names is a drug or gene-delivery study. 7 of 23 are so marked (K03, K07, K08, K09, K17, K18, K19); no part of the
check is done for them. In every other source, treatment or dosing passages are not read or quoted.

## Rule for "independent" (frozen)
Two sources are independent for a sentence only if all three hold:
a. primary data differ: each carries its own measurement or observation of the proposition, from different patients, animals,
   samples or deposited datasets;
b. no shared first author and no shared last author;
c. neither restates the other, and the two do not restate one common source (review or citation transmission).
Sentence verdict: HOLDS (at least two sources independent of each other), FAILS (no such pair; the failing letters are given),
DECLARED (the sentence or its own paragraph already states the dependency; reported apart, not counted as a failure),
UNSETTLED (a source needed is not held), OUT (on reading, the sentence does not assert multi-source support).
With three or more sources the largest mutually independent set is also given. Shared middle authors are noted, not counted.
Scope truth of the proposition is not graded here.

Sources: held full texts, held records and receipts; author lists from the held text or from PubMed metadata by PMID.
A source not held makes UNSETTLED for rule a and c, not a failure. No new acquisition.

## Two explanations and a prediction (written before any source)
* E1: the "independent" labels were added after explicit R4 checks, so the sentences are mostly sound: failing share of the
  checkable sentences at most 20 percent.
* E2: the WWOX literature is small and clustered in a few laboratories that cite one another, so many "convergences" share a
  senior author or transmit one dataset: failing share at least 40 percent.
Prediction: about 35 percent (5 to 6 of 16) fail, mostly on rule b or c, few on shared raw data. K16 was already known to fail
and is reported both inside and outside the share.

## Second reading
Every sentence SCI calls FAILS goes to a second reader (a delegate, effort stated) who gets the sentence, the source list and
the rule, not SCI's verdict, together with an equal-or-larger share of HOLDS sentences mixed in so that membership in the packet
does not reveal the verdict. Disagreements are printed, not averaged.
