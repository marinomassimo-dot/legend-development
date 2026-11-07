# INV-08 NRF2: delta over L01 and the INV-08 record (label nr-p, 2026-11-07)

Non-canonical research material. Not medical advice; no dose or regimen; concentrations are source facts only. Public edition (reference genotype class, no individual record). Nothing outside this folder was edited.

## Answer first

- **DATO.** No source read here measures NRF2 protein, nuclear NRF2, NQO1 activity or ROS in a WWOX-deficient mammalian neural system. The module record says the same; one PubMed search (WWOX x NRF2) returned one non-neural record.
- **INFERENZA.** The L01 position does not change: KEEP-AS-PROPOSAL, a role-resolving mechanism experiment, no benefit claim. What changes is sharper wording: the only established GSK3 route to NRF2 rests on the beta-TrCP papers, not on the retracted Src chain; and the best precedent for the astrocyte component is another system.
- **IPOTESI that stays plausible.** Activating NRF2 in astrocytes or in the whole culture improves a neuronal network function after an oxidative challenge in WWOX-deficient cultures, NFE2L2-dependently. A refutation: no genotype difference at X0 and no NFE2L2-dependent effect at X1/X2 (experiment.tsv).
- **NON RISOLTO.** Which of the six hypotheses holds (hypotheses.tsv). The mixed transcript signature (NFE2L2, NQO1 lower; HMOX1, SRXN1 higher) shows neither a deficit nor an effective compensation.

## The retraction (PMID 28159761)

- **DATO.** PubMed types it as a Retraction Notice of the 2011 Src-subfamily/Nrf2 article (PMID 21690096); the Crossref title is "Retraction: " plus the full title, so the whole article is retracted, not a part. Crossref also lists an expression of concern and a correction for that article in January 2016.
- **NON RISOLTO. Reason for the retraction: not reached.** The PMC page returned a reCAPTCHA check page and the notice body is a PDF; I stopped for that source (no other client tried). No reason is inferred. A retracted source is not reliable support; the retraction does not by itself make a described relation false. The GSK3 beta-Fyn/Src-NRF2 chain is from the external report and is not in the module; it stays unsupported here.

## GSK3 beta-TrCP-NRF2 route (PMIDs 21245377, 22751928), abstract only

- **DATO.** 2011: GSK-3 phosphorylates a Ser cluster in Neh6 that overlaps an SCF/beta-TrCP degron; inhibitors stabilise Nrf2 in Keap1-null fibroblasts; a Ser-to-Ala mutant is beta-TrCP-insensitive and less ubiquitinated. 2012: two serines mapped, beta-TrCP docking by NMR; an inhibitor raised Nrf2 and HO-1 in liver and hippocampus; hippocampal GSK-3 beta absence raised Nrf2 and phase 2 products and lowered oxidative markers.
- **INFERENZA.** Different mechanism from Fyn/Src (a phosphodegron, not nuclear export). The two papers share one laboratory line: counted as one line, with a genetic arm in the second. Not read: inhibitors, concentrations, n, controls per panel. No further replication sought, because it would not change the decision (query Q03 found one record, not opened).
- **DATO.** Lithium suppressed seizures in all genotypes including wild type (PMID 32000863, existing record): GSK3 beta is not shown to cause the seizures, and this package does not turn it into proof.

## Astrocyte component (PMID 14762128), abstract only

- **DATO.** Primary mixed cortical cultures from ARE-reporter mice; tBHQ and sulforaphane; reporter activity selective for astrocytes; protection of neurons from hydrogen peroxide and non-excitotoxic glutamate; no activation or protection in Nrf2-null cultures, rescued by adenoviral Nrf2 and blocked by dominant-negative Nrf2; the adenovirus targets astrocytes; sorted glia-enriched cells versus neurons by microarray: the neuronal gene change after tBHQ depended on astrocytic Nrf2.
- **INFERENZA.** A non-cell-autonomous route is plausible, with an Nrf2-null control and a rescue, the pattern X2/X3 copy. It is another system, an oxidative-death endpoint and one electrophile class; it says nothing about WWOX, network activity, or other compounds. Concentrations, n and array details not read.
- Neuron-specific Wwox deletion alone gives the phenotype (existing record, PMID 33914858); that does not decide whether astrocytic NRF2 could help neurons lacking Wwox.

## What changes against the external report

- **Confirmed (as leads):** organoid NFE2L2 and NQO1 lower, HMOX1 higher (4 v 2 libraries); the GSK3-beta-TrCP route exists in fibroblasts and mouse tissue.
- **Corrected:** the Src chain rests on a retracted article (unreached reason); the report's labels are not independent verification.
- **Unresolved:** any WWOX-system NRF2 protein or activity; direction of the WWOX-NRF2 relation. One cancer-cell abstract (PMID 39894307, Stage 2, abstract only) has drug-induced WWOX activity lowering nuclear NRF2, which would predict more NRF2 with WWOX loss, opposite to the NFE2L2 transcript; it is a different cell type and a gain of function.

## Next experiment and decision

Isogenic WWOX-deficient versus corrected human neuron-astrocyte cultures; priority endpoint network activity (with viability); acute or inducible KEAP1 lowering, then each compound (dimethyl fumarate and monomethyl fumarate separate, omaveloxolone across its concentration windows); NFE2L2 loss with rescue; NAC as one comparator only; composition counts; clones and batches recorded. It decides whether arm R advances to a second model or the axis moves toward inert. In silico only: re-score existing deposits on a sourced NRF2 panel against composition (X4); it cannot decide function.

## Consumers

Keep unchanged: L01 card, NEED-REDOX-NRF2 and INV-08 already state the conditional arms and the electrophile caveat; nothing here is a measurement in a WWOX system. Optional proposals for the Orchestrator: add the retraction status to any text that carries the Src chain; record the abstract-only depth of 21245377, 22751928 and 14762128.

## Depth, access and staging

New sources: 5 of 6 allowed (Stage 1: four; Stage 2: 39894307, because the WWOX x NRF2 search named a gap), all abstract or metadata depth. Full-text routes: Europe PMC HTTP 500 (two attempts), PubMed tool empty body, E-utilities stub, PMC page reCAPTCHA, publisher pages Cloudflare: stopped for those sources. PubMed tool honours OR and parentheses (Q01). Receipts staged (suffix 98), validated, not recorded.
