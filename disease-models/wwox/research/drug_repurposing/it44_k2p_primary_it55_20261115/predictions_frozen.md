# Predictions frozen before any paper body was opened (IT44-Q01 K2P half, IT44-Q02)

Non-canonical working note. Not medical advice; no dose, schedule or route; no compound nominated. Reference genotype class only. Date 2026-11-15. context_policy: QUESTION_DRIVEN.

State of knowledge when this file was written: the brief, `generation_it44_20261110/relation_s11_result_it44.md`, `s11/search_rows.tsv`, `verify_s11/VERDICTS.md` (including its Q5 table of ChEMBL rows) and abstracts or Europe PMC identifier metadata (title, journal, PMCID, open-access flag). No body of any candidate paper had been opened.

## What the review-derived rows quote (the thing being tested)

* ChEMBL rows on TREK-1 (CHEMBL2321615), all from one review document (CHEMBL3817738 = Vivier 2016 J Med Chem, PMID 26588045, not in PMC): riluzole EC50 139.4 uM (COS7, whole cell, +50 mV, "unknown origin"), fold change 2.0 at 100 uM (COS7) and 1.4 at 10 uM (CHO); flufenamic acid EC50 100 uM (same COS7 assay), 3.5-fold and 250 percent at 100 uM (HEK293).
* Catalogue text: the glutamate-release modulator "needs about 100 uM for the K2P effect"; TREK-1 activation transient, TRAAK sustained (abstract of Duprat 2000).
* No Ba2+ value for TASK-1, TASK-3 or THIK-1 in the repository (the independent reader did not reach any).

## Candidate primary sources (chosen from identifiers, not from bodies)

Riluzole: Duprat 2000 Mol Pharmacol (PMID 10779373, not in PMC), Fink 1998 EMBO J TRAAK (PMID 9628867, PMC1170668), Cadaveira-Mosquera 2011 J Neurosci (PMID 21273422, PMC6623616). Fenamate: Takahira 2005 Pflugers Arch (PMID 16075240, not in PMC). Ba2+: TASK-1 Duprat 1997 EMBO J (PMID 9312005, PMC1170177) and Mathie-group Pflugers 2007 (PMID 17541788, PMC2492388); TASK-3 Kim 2000 JBC (PMID 10734076, not in PMC); THIK-1 Rajan 2001 JBC (PMID 11060316, not in PMC); Zhou 2009 J Neurosci (PMID 19571146, PMC6665656) as a K2P Ba2+ comparator. Reserve if budget allows: Ma 2011 JBC TREK-1 Ba2+ (PMC3220548).

## Predictions (each to be scored held / missed / not testable)

P1. Access: the PMC-hosted sources (Fink 1998, Cadaveira-Mosquera 2011, Duprat 1997, Zhou 2009, Pflugers 2007) return the article body to one plain request. The non-PMC sources (Duprat 2000, Takahira 2005, Kim 2000, Rajan 2001) return an abstract page, a paywall, a 403 or a bot check, and end as access-limited or access-blocked. Confidence: PMC high (0.85), non-PMC blocked or limited high (0.8).

P2. Riluzole on TREK-1 and TRAAK (Duprat 2000 / Fink 1998). The primary papers give a concentration of about 100 uM as the working concentration and a full concentration-response with an EC50 of the order of 100 uM or a few tens of uM for TRAAK; the "139.4 uM" quoted by ChEMBL for TREK-1 is a curated value whose source paper may be a different one (the review may cite it to a primary other than Duprat 2000). Expected conditions: COS-7 (or HEK/CHO) cells, room temperature (stated or not stated), pH 7.4, external K+ about 5 mM in whole-cell recordings, a +50 mV or similar test potential, channels of mouse (TREK-1) and mouse or human (TRAAK) origin (so "unknown origin" in ChEMBL is resolvable to a species), n of 4-10 per point. Confidence about "EC50 within a factor of 3 of 139 uM": 0.55. Confidence that an explicit EC50 for TREK-1 is stated at all in Duprat 2000: 0.5 (TREK-1 activation is transient and followed by inhibition, which makes an EC50 awkward).

P3. Fenamate on TREK (Takahira 2005). Flufenamic acid is reported as a TREK-1 activator at 100 uM with a fold increase, and a concentration-response with an EC50 between 50 and 300 uM, in COS-7 or HEK cells at room temperature; I expect the "EC50 100 uM" of ChEMBL to be coincident with the single working concentration only if the paper has no full curve (probability that the ChEMBL EC50 is a curation artefact from a single-concentration experiment: 0.3). Mefenamic, niflumic and other fenamates will appear as comparators with weaker or similar potency.

P4. Native riluzole current (Cadaveira-Mosquera 2011). Mouse superior cervical ganglion neurons, riluzole-activated TREK-like current with an effective concentration of several tens to a few hundred uM (the catalogue says TREK-2 at 300 uM); Ba2+ is used at a single high concentration (mM range), not as a 50-200 uM concentration-response. Temperature: room temperature or 32-35 C, uncertain.

P5. Ba2+ on TASK-1, TASK-3, THIK-1 (Duprat 1997, Pflugers 2007, Kim 2000, Rajan 2001, Zhou 2009). No source will give a Ba2+ concentration-response inside 50-200 uM for any of the three channels. Most will give a single concentration (about 1 mM or higher) with a small percentage block, or a statement of insensitivity; the TASK channels are expected to be weakly blocked at 100-200 uM (less than 30 percent, derived from "insensitive" statements) and THIK-1 is expected to have no cloned-channel Ba2+ number at all in Rajan 2001. Confidence that at least one of the three channels has a stated Ba2+ IC50 in the window: 0.15. Confidence that at least one of the three has a stated Ba2+ percentage at a single concentration at or below 200 uM: 0.25. Confidence that THIK-1 has no Ba2+ value in the cloning paper: 0.6.

P6. What stays unchanged: the family-level statement that the K2P openers in the catalogue act on the Ba2+-weak TREK/TRAAK subfamily. I expect the primary papers to leave that unchanged; the revision, if any, is wording about potency and conditions (concentrations, cell type, temperature, species of the clone), not about direction.

P7. Number of papers actually read with locators: 4 to 6 of the 9 to 10 candidates; the rest access-limited or blocked.

## Procedure committed to

One plain request per source; abstract-only pages labelled census; any proof-of-work, captcha, bot check or 403 ends that source with no second attempt; no contact parameter; verbatim quotes checked mechanically; derived arithmetic marked as derived; no ledger append.
