# ADV-199 pre-registration (SCI): can ONE non-tautological, matched card be assembled from the KCC2 transposon mutant library paper? (feasibility only; no engine run, no model call; hypothesis level; nothing WWOX-specific, no compound, dose or rank; not medical advice)

analysis_at: 2026-11-23T17:14Z (written before the body, figures or erratum of the source were opened)
task: ORCH-SCI-ADV065-DEEPEN-20261118, accepted step 90 (assignment ADV-199, Codex REPLY_35)
source: Uvarov et al., Front Mol Neurosci 2024/2025, PMID 39881966, PMC11774852, DOI 10.3389/fnmol.2024.1505722; erratum DOI 10.3389/fnmol.2025.1576660 (Figure 4 legend, per ADV).

## 1. What has been seen BEFORE this file
* ADV's message, assignment ADV-199, Codex REPLY_35 (read whole), and ADV-197's result lines on the saturated card (the null that always picks K1 scores MATCH) and the endpoint-fidelity gate (K1 to K5 and the hand dry run).
* The values quoted in those texts and NOT yet checked by me: B8 surface level 2.96 +/- 1.16 of WT (p 0.027, one-sample Wilcoxon, Fig 5C); C1 and C11 "no difference" in membrane abundance (Fig 5C); neuronal delta E_GABA WT 8.0 +/- 1.4, B8 17.9 +/- 1.5, C1 17.9 +/- 0.5 mV (Fig 6).
* **A conflict I must resolve from the source:** Codex says Fig 5 is surface KCC2 "in cortical neurons"; ADV says the surface assay and the physiological readout are "HEK293 versus cortical neurons". Which preparation carries each figure decides whether the "unmatched preparations" reject rule applies. I do not know which is right.
* Step 0 (names and sizes only): Europe PMC reports `isOpenAccess Y`, licence CC BY, `hasSuppl Y`; the Frontiers full-text page answers HTTP 200 (1 127 207 B HTML, about 80 000 characters of text; sha256 756eeb71999a first 12 hex); the erratum page HTTP 200 (301 736 B, 969ea620b7a2); figure images g001 to g006 answer 200 (183 986 to 745 551 B; g003 64da2ac0c17e, g005 4798d3bbc281, g006 2ca4b9bf743a), g007 is 404. The PMC page was not requested (ADV: reCAPTCHA). Raw data: "made available by the authors" (not used).
* I have NOT opened the text, any figure, the legends, the Methods or the erratum. No repository search for this paper beyond ADV's (identifiers tracked nowhere).

## 2. What the card needs (fixed before reading)
* ONE question that a reader could answer with a measurement choice, stated without any value from the source.
* Candidate comparisons, each a pairing of a measured contrast in the source: at least one INFORMATIVE arm (its held result separates two explanations) and one arm that CANNOT discriminate (its held result is compatible with both). The reference outcome for each comes from the figures and is kept analyst-side.
* An ABSTAIN condition: the reference label when the question needs a quantity the source does not measure (per-molecule transport; equivalence from a null; transfer between unmatched preparations).
* A masking statement: which method details can be removed from the visible card without changing the evidence.
* A hand test of three scorers on the card: (i) the rule "always pick the direct functional readout", (ii) IT's endpoint-fidelity gate (states comparator, population and endpoint and is checkable against the row), (iii) a null that always picks the first listed option.

## 3. Readings (stated now; each falsifiable by the body)
* **Reading U ("unmatched preparations", my expected outcome, 0.45):** the surface-abundance assay (Fig 5) and the chloride-load physiology (Fig 6) are separate preparations or differ in construct, expression system or timing, so the abundance-versus-transport contrast exists only across unmatched preparations, and a no-difference surface result for C1 is not an equivalence test: REJECT, or the only valid reference label is ABSTAIN.
* **Reading S ("simple rule saturates", 0.25, can coexist):** the question cannot be written without naming the functional readout, so "always pick the direct functional readout" picks the informative arm every time, as the null picked K1 in ADV-197: REJECT.
* **Reading V ("viable", 0.20):** both readouts are measured in the same cortical neuron preparation with stated n and denominators, C1 against WT is a measured pairing across them, and a question exists whose informative arm is not the direct functional readout: VIABLE as a diagnostic of choice of measurement on known data (never predictive validation).
* **Reading D ("detail not as described", 0.10, can coexist):** one of the quoted values or the Codex figure description differs from the source (for example the preparation of Fig 5, the identity of C1, the n or the test): the card is corrected or rejected on that ground.

## 4. Fixed exits
* **VIABLE** only if Reading V holds AND the visible card does not give away the informative arm AND the three hand scorers do not all coincide on it.
* **REJECTED** if any of: the visible prompt gives away the informative arm; "always pick the direct functional readout" always picks it; the evidence separates the two assays only through unmatched preparations or through a null used as equivalence. The reason is named with the figure and the quantity.
* The hand test is run on paper only: no engine, no model call, no repeated run, no benchmark import. The card, arms and reference outcome are frozen in a second file with time and hash BEFORE the hand test, and nothing is shown to any engine.
* What was reported (the paper) is kept apart from what the card infers. A null surface result is never read as equal abundance. Nothing about a compound, dose, rank or WWOX follows.
