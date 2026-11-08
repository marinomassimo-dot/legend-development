# P4 phase A: unguided expansion from a myelin phenotype

Run on 2026-11-08. Public literature through the PubMed tools only; abstract level for every source; no full text read; no paper_packet claim and no prior-receipt lookup were run by the producer; the Orchestrator then looked each PMID up and set `prior_receipt` for the three that had earlier receipts (33914858, 34747138, 42422765).

## Original paper
DATO: query "WWOX myelination" returned PMID 33914858 (Brain 2021, "Neuronal deletion of Wwox, associated with WOREE syndrome, causes epilepsy and myelin defects"; mouse neuronal deletion, reduced maturation of oligodendrocytes, reduced myelinated axons, impaired axonal conductivity, human brain organoids with hypomyelination; MeSH includes Coculture Techniques). INFERENZA: this is the source of the observations in the brief (Systems A, C, D and probably B); it is not independent confirmation of anything below. Abstract only: I did not read its methods, so which panel shows System B or C is not verified.

## Answer: five alternatives plus one measurement caveat
1. ALT1 `consequence`: seizures and hyperexcitability secondarily impair OPC maturation. IPOTESI. Tested by readouts at or before P9 and in seizure-suppressed nulls. Against: System C neurons are pre-seizure peripheral; and activity normally increases myelination (PMID 24727982).
2. ALT2 `proximal_cause`: loss of a neuron/axon-borne cue that OPCs need (cell-nonautonomous). Fits System B (glial deletions normal, qualitative only) and System C. Test: conditioned medium, transwell and mosaic neighbours. Against: the cue could be a downstream activity or energy state.
3. ALT3 `composition_or_maturation_problem`: a differentiation block or delay with a possible thyroid-hormone or bioenergetic supply term. The A1 pattern (more OPCs, fewer mature cells) also appears with thyroid-hormone transport loss (PMID 37307933) and creatine deficiency (PMID 36732069). Note that System D medium lacks thyroid hormone after day 71 (brief), so D alone may be medium-confounded. Test: add the hormone to D; age series under rescue. Against: Wwox acting through thyroid hormone is unsupported.
4. ALT4 `consequence` (energy): hypoglycemia or glial energy failure. Glut1 deficiency lowers glucose, lactate and myelin gene programmes (PMID 42686079); neuronal Wwox restoration rescued hypoglycemia with myelin (PMID 34747138). Against: D and C use defined media.
5. ALT5 `compensation`: extra PDGFRA cells or longer sheaths are adaptive (PMID 37307933 reports longer sheaths as compensation in another model). Against: it does not explain unmyelinated optic nerve axons or a higher g-ratio.
6. ALT6 `measurement_insufficient`: n of 3 mice, slices not independent, mosaic Cre, latency not tied to myelin. The convergence of EM, staining, electrophysiology and organoids argues against an artefact.

## DATO / INFERENZA / IPOTESI / NON RISOLTO
- DATO (abstracts): activity increases oligodendrogenesis and myelination (24727982); the same OPC/mature-cell pattern occurs with thyroid-hormone transport deficiency and creatine deficiency; Glut1 deficiency lowers myelin programmes; neuronal restoration rescues seizures, hypoglycemia and myelin together; neuron-restricted delivery beat oligodendrocyte-directed delivery (42422765 abstract).
- INFERENZA: the A1 pattern is a generic differentiation-stage signature, not specific to a cause. Bundled rescues do not order seizure, energy and myelin.
- IPOTESI: ALT2 and ALT3 are the least tested; each has a named discriminating measurement in `relations.tsv`.
- NON RISOLTO: whether myelin changes precede seizures; whether conduction slowing is myelin; whether the delay is recoverable (nulls die at 3-4 weeks).

## Limits and unreached
- All sources read are abstract only (7 receipts, `receipts/INDEX.tsv`, all validate). No full text opened (no decisive source reached beyond the abstract).
- Bounded search with no hit: seizure-induced OPC loss/myelin causal source (Q11, Q2, Q9) and thyroid-hormone rescue in the Mct8 model (Q12); not found after those PubMed strings on 2026-11-08, so ALT1 has no direct positive literature relation here, only the opposite (activity promotes myelin). Not an absence.
- PMID 37765015 (thyroid-receptor-beta ligands promote OPC differentiation in vitro) was viewed but not used or receipted; a tool class for ALT3 stays unsourced.
- No dose, regimen or clinical statement is made. No access challenge was encountered.
