# Correction note (2026-10-31), added by IT10 P5; the original records are not rewritten

Source: IT10 P2.2 (`axis_it10_p22_20261031/premises.tsv` PR1) and the orchestrator's re-read of Hussain 2019 (PMID 30290271) Results 3.3 and Figure 4E; see also `generation_it9_p1_20261030/CORRECTION_NOTE_IT10_20261031.md`.

In the Wwox-null hippocampus only **Il6** is significant (Results 3.3: "Il6 significant at p < .05"); **Tnf-a is a non-significant increase** (Figure 4E: no mark). The authors' abstract and Discussion say both cytokines are increased.

Records whose wording or seed premise is affected (decisions stand; no record is rewritten):

* **P4CD-04 dimethyl fumarate** (`candidates/P4CD-04_dimethyl_fumarate.md`, line "Proposal as generated. Seeds TNF and IL6 transcripts up (S085, S086; Wwox-null hippocampus)"): read as "Il6 significant; Tnf-a not significant in the null hippocampus (the P47T cerebellum TNF observation is separate)". The DROP does not depend on it: the decisive datum is the artefact chain (two E3 ligases joined by shared members). IT10 P2.2 declares a different, direct NRF2 rationale for monomethyl fumarate and does **not** reverse this drop.
* **P4CD-02 JTE-151** (`candidates/P4CD-02_JTE-151.md`, "Seeds IL6 (S086 ...) and TNF (S085) transcripts up"): the TNF seed in the null hippocampus is not significant; the Il6 seed is. INCONCLUSIVE stands.
* **P4CD-01 apabetalone** (arm question seed "TNF (and IL6 via BRD3)"): the TNF seed in the null hippocampus is not significant; the record's decision is not re-opened here (its decisive datum is the microglial cytokine-lowering evidence and its gate is baseline cytokine in WWOX-deficient microglia).
* **qualification_D.tsv** is unchanged; the ranking reads it as stored.
