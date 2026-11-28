# Self-evaluation: SCI, ADV-327 (2026-11-28)

Scope: one question-driven search package (lithium and GSK3-pathway phosphorylation in wild-type developing rodent brain), seven partial full-text receipts. Not a deep dive: the 27 protocol questions are answered here only where this work touches them.

## Part 1, executable

`session_self_eval.py` PASS; `fulltext_receipts.py verify` OK (3920 receipts); `legend_lint.py` no BLOCK; `public_release_gate.py` PASS. The declared gaps it prints belong to earlier readings. No work manifest: no read here is a complete read.

## Part 2, the points that apply

* **Sections and figures (Q1):** no paper was read cover to cover; 107 of 366 records had open full text, read in targeted sections or screened by terms. Bar values are readings by eye.
* **Load-bearing premise (Q8):** the frozen exposure ceiling was anchored on "LiCl 60 mg/kg" taken from a figure legend. The primary's methods give three injections within 1 h. I did not check the methods before accepting the frozen prereg and dispatching; the second reader's sentence pass found it after the verdict was written.
* **Shows against claims (Q9):** none of the three qualifying records reports a test of the lithium-versus-vehicle contrast. The result file says so and does not read it as no effect.
* **Existing claims (Q14):** CLAIM 016's lithium experiment is not reproduced in dose schedule by any qualifying record. No claim was edited.
* **Reading debt (Q15):** nine records were not obtained and one open item was added by the second reader; they are listed in the result file, not entered in the full-text queue (none is needed for a pending decision).
* **Capability gap (Q16):** none new. `CHANGE = NONE` for tooling.
* **What broke (Q17, Q26):** delegate TSVs had short rows and failed `test_structured_data_integrity.py` before the push; fixed by padding. The search delegate reached a 323k-token peak: one delegate for 366 records is too large; a screening pass and a reading pass would have been two smaller ones.
* **Landing (Q24):** `development/main` at `b1d2fdefd`; delivered to ADV. This file lands with the session's checkpoint.

## Upgrade

One memory note (`sci-adv327-pitfalls`): before freezing or accepting an exposure range, quote the primary's methods dosing sentence, not the legend. It is a note for this actor, not an enforced check, and is stated as that.

## Defaults taken (§21c)

* Daily repeated doses were not counted as "acute"; both readings are printed. Safe because the verdict is "not decidable" under either.
* IT was not messaged: no IT decision changes; ADV was asked to forward if wanted.
* The frozen prereg was not edited despite the premise error; the error is stated beside the verdict.

## Stop log

None.

ATTRIBUTION_CENSUS
incidents: 4
machine: 1   blind_auditor: 3   peer: 0   self: 0
severity_high: 3   of which self: 0
undetected_known: 0

Incidents: (1) the single-dose premise (blind auditor); (2) a design sentence calling 1 h the peak at the nearest age (blind auditor); (3) one screening miscode, PMID 11907184, and its wrong attribution to the recall sample (blind auditor, counted once); (4) uneven TSV rows (machine). The second reader's eleven sentence corrections include (1) to (3); the others tightened wording.
