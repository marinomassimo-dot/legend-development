# Prepared brief (not dispatched): IT44-Q01 (K2P/Kir half) and IT44-Q02, one Scientist batch

2026-11-15, IT. Ready for the moment a Scientist slot frees; ADV or IT dispatches. Reference genotype class only; not medical advice; no dose, schedule or route; no compound nominated; no ranking, need, candidate or frozen-package edit.

**Named decision.** Whether the K2P opener rows of the INV-18 comparison rest on primary data rather than a review document (IT44-Q02), and whether a 50-200 uM Ba2+ step separates a TASK/THIK conductance from a Kir2 one (IT44-Q01; the Kir2.2/Kir2.3-opener half is already answered: none found, SCI49 B, bdbe0ae33). Consumers: INV-18 ladder step 2b (K2P/high-Ba2+ step), compound view rows for the K2P openers; nothing is applied by the batch itself.

**Questions (verbatim from the map).** IT44-Q01: "What is the Ba2+ concentration-response (50-200 micromolar window) of TASK-1, TASK-3 and THIK-1?" IT44-Q02: "What do the primary papers give for the EC50 and conditions of the approved glutamate-release modulator on TRAAK and TREK-1, and of the fenamate on TREK channels?"

**Method.** Source-first: for each channel or compound find the primary papers (not the reviews) by identifier from `generation_it44_20261110/relations_s11_it44.tsv` and the review it came from; read the body from the PMC article page when the paper is in PMC (one plain request per source, as in WO-11 and IT49-Q11); an abstract is census, not a read. Record per paper: preparation (oocyte, HEK, CHO, slice), species, temperature, pH, external K+, holding voltage, concentration range, IC50/EC50 with n, and the verbatim locator. Freeze predictions (which values the review quotes, and whether the primary conditions match) in a commit before opening the first body.

**Stop rule.** Stop when every named source is either read with locators or access-blocked by one plain request (a proof-of-work or bot check is a stop, not to be solved); or after 10 papers, whichever comes first. No PMC bursts; no e-mail or contact parameter to any service; no spend. A source absent from PMC is recorded as access-limited, not absent. A supported abstention is a valid result.

**Delegation.** One delegate, sonnet with effort high (per `delegation_budget.md`), read back from the transcript afterwards; a blind verifier only if a number that decides the comparison comes out of one reader. The orchestrator records receipts in event-ID order after landing.

**Return.** Table of primary values with conditions against the review's values; what changes for the K2P opener rows (a dated Update, not an edit of cells); open items. Expected size: one session of a few hours of wall time; cost to be measured from the transcript, not estimated.
