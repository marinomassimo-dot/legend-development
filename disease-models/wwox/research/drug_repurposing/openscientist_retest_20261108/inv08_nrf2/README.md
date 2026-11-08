# INV-08 NRF2: full-input repeat (label os-08, 2026-11-08)

Non-canonical research material. Not medical advice; no dose or regimen (one source dose is quoted only as a source fact in a receipt-level note). Reference genotype class only. Cap on sources newly read: 5 (state: 5 used, no overrun; all at abstract depth). Files: `extraction.tsv`, `sources_cited.tsv`, `chains.tsv`, `phase1_note.md`, `reconcile.tsv`, `decisive.tsv`, `evidence.tsv`, `queries.tsv`, `receipts/` (5 staged, suffix 36, validated, not recorded).

## Answer first

- **INFERENZA.** The report's headline, NRF2 most likely impaired in WWOX deficiency, is a prediction built on a chain whose Src/Fyn links cite a retracted article (PMID 21690096; record-level evidence only). The report measures nothing; the module has no WWOX-system NRF2 protein or activity datum either; the module's WWOX transcripts are mixed (NFE2L2 and NQO1 lower, HMOX1 higher in organoid), which shows neither deficit nor effective compensation.
- **DATO.** The paper (32000863) itself states increased GSK-3beta activation in Wwox-null cortex, hippocampus and cerebellum, measured as Ser9 dephosphorylation by western blot (a regulatory proxy; one representative blot shown, legend says four experiments; age P14 in Methods versus P20 in the legend). Lithium: the Results name Wwox-null mice only; 'all genotypes including wild type' is per module record W10 (figure not viewed). GSK-3beta as a validated causal node is not established.
- **IPOTESI that stays explorable.** A genetic NFE2L2-dependence test in WWOX-deficient neural cells, before any compound, with NAC as one comparator only. Weakened by: no genotype difference at baseline, or no NFE2L2-dependent functional effect.
- **Priority experiment.** Isogenic WWOX-deficient versus corrected neuron-astrocyte cultures, NRF2 protein and NQO1 activity at baseline and under a fixed oxidative challenge, then inducible KEAP1 lowering with NFE2L2 loss and rescue (already `X0`-`X2` in `nrf2_inv08_20261107/output/experiment.tsv`).

## (a) Coverage

Items per kind (76, E76 added after the audit): observation 20, inference 10, experiment 9, limit 9, recommendation 5, compound 4, hypothesis_favourable 3, mechanism_step 3, target 3, other 3, alternative_explanation 2, counter_evidence 2, open_question 2. Per `legend_class` (items, after the audit split of E52/E53 and addition of E76): verified_or_corrected 33, already_present_and_used 26, new_to_legend 11, superseded_or_contradicted 5, unverified 1; `prior_brief_fate` modified 31, narrowed 22, kept 17, omitted 6. `legend_class` states the verification state, not repository novelty: five of the sources read (23251339, 36244590, 27401964, 40902898, 29538645) are new to the repository (`source_new_to_repository`), though their rows are classed verified_or_corrected; `new_to_legend` therefore understates source novelty. Sources: 19 PMIDs plus one unreferenced knowledge-base audit; 8 chains; 14 decisive propositions.

## (b) What the previous brief kept, narrowed, modified, omitted

Previous BRIEF (`nrf2_inv08_20261107/BRIEF.md`) said the report was not needed and called it a collection of leads. Kept: the question, KEAP1/NFE2L2 targets, the cytokine and neuron/glia deletion records. Narrowed: acquired-epilepsy precedents ("methodological or biological transfers"), PV and oligodendrocyte endpoints (cell loss, marker, maturation, survival). Modified: the Src chain (flagged retracted, reason unreached), lithium (not exclusive proof), NAC (comparator, not proof of NRF2 independence), low basal NRF2 (not needed to justify activation, so the report's precondition 1 is contradicted), double-knockout animals (cell test first). Omitted entirely: the redox-vulnerable PV/oligodendrocyte sources, the reductive-stress papers, sulforaphane precedents (36244590, 27401964), the miR-155-5p OPC paper, the zinc/Fyn paper, and the report's own internal count mismatch.

## (c) Sustainable favourable reasons

DATO: NRF2 activation by RTA 408 after status epilepticus reduced late seizures in a rodent model (abstract, 29538645); sulforaphane benefit in an ischaemia model depends on Nrf2 (abstract, 36244590); astrocytic Nrf2 can protect neurons in mixed cultures (earlier abstract, 14762128). INFERENZA: these justify testing NRF2 dependence, not predicting benefit; the PV/oligodendrocyte redox-vulnerability argument (not read) is plausible as a cell-type reason to measure.

## (d) Errors and counter-evidence found

- The GSK-3beta to Fyn/Src to Tyr568 steps are cited to PMID 21690096, whose record carries the type Retracted Publication (notice 28159761, expression of concern 26773125); 'retracted in full' rests on record type fields only, the notice prose and the reason are unreached. 23251339 shows only co-occurrence in mouse liver (full text read by the verifier). PMID 17403689 (2007, same laboratory line, no retraction found by the verifier, not cited by the report) reports the GSK-3beta, Fyn, Tyr568 relation but is not independent of the retracted article; the beta-TrCP route (21245377, 22751928) has an independent laboratory line and is not in the report.
- PMID 24747945 is cited as stating that chronic activation can be harmful; its abstract reports protection by constitutive cardiomyocyte Nrf2 activation under pressure overload, the quoted sentence being background. 40729961 supports reductive stress (heart).
- 14762128: the Nrf2-null culture result is for tBHQ only; the report writes tBHQ/sulforaphane.
- 27401964: the E-selectin/VCAM-1 result is in vitro on brain endothelial cells in a sepsis model; the report ties it to the in vivo knockout residue.
- 35984507 (receipt FTR-20261019-35984507-03) concerns WWOX inhibition restoring mitochondrial homeostasis in high glucose; the report's "physically interacts and modulates ROS" paraphrase is looser than the title.
- 39894307 (not cited by the report) predicts the opposite sign (WWOX activation lowers nuclear NRF2); a non-neural gain-of-function system.
- Header "35 papers reviewed" versus 19 listed. All 19 PMIDs resolve to matching records (including 42439630, a 2026 Cells review, and 40902898, a 2025 Brain Behav Immun paper).
- The report claims "zero NRF2 data" for WWOX from a keyword audit of one DisMech entry; the module holds mixed transcript and ROS data in WWOX systems.

## (e) Explorable hypotheses

H1 insufficient, H2 induced but insufficient, H3 compartment (astrocyte), H4 cell type or stage, H5 compound action independent of NRF2, H6 no benefit (`nrf2_inv08_20261107/output/hypotheses.tsv`). Each weakens if baseline NRF2 and NQO1 activity show no genotype difference or if effects persist unchanged in NFE2L2-deficient cells.

## (f) Priority question

Does WWOX deficiency change NRF2 protein or activity in neural cells at all (measurement before intervention), and is any functional effect of NRF2 raising NFE2L2-dependent? A sorted PV and OPC readout adds cell-type resolution to `X0`.

## (g) Consequence for drug repurposing, with novelty class

- Keep NRF2/KEAP1 (omaveloxolone = RTA 408, dimethyl fumarate and monomethyl fumarate separate) as a conditional proposal; no promotion from the report: already_in_legend (L01); the epilepsy source 29538645 new_to_legend, literature novelty not assessed.
- GSK-3beta to NRF2 link: the beta-TrCP route has an independent laboratory line and no retraction; the Fyn relation is also reported by a non-retracted 2007 paper of the same line as the retracted article (not independent); the cited retracted article cannot support it. GSK-3 rescue may pass through other substrates (already_in_legend, GSK3 packages).
- Reductive-stress ceiling (no occurrence of the phrase elsewhere in the repository), NAC-independence, sulforaphane/tBHQ as comparators: new_to_legend as sources and as ideas, literature novelty not assessed.
- Sorted PV/OPC NRF2 readout: new_to_legend (design), not assessed in literature.

## (h) Consumers to update

None changed. Optional proposals: the INV-08 row and NEED-REDOX-NRF2 could cite the retraction of 21690096 wherever the Src chain appears (none carries it now); add 23251339, 27401964, 40902898 as abstract-level precedents only if a consumer needs them.

## (i) Not reachable or not done

The reason for the retraction of 21690096 (no route reached it; not retried). Full texts of all five new sources (abstract only; PMC ids exist for three but were not opened). Abstracts of 34829573, 31382215, 23671099 (identity only by the producer; 40729961, 24747945, 23140664, 36130098, 42439630 abstracts were read by the verifier). The 16 unlisted papers behind "35 papers". The DisMech entry the report audited (not opened). Nothing was inferred for these.

## (j) Queries

See `queries.tsv` (Q01-Q07). Absence perimeter for "no WWOX-system NRF2 measurement": PubMed and Europe PMC title/abstract, strings with WWOX/Wwox and NRF2/Nrf2/NFE2L2/KEAP1, and a redox/neural string, to 2026-11-08; full-text hits were not searched.

## Audit appendix (blind verifier vf-08, 2026-11-08; file `verify/audit.md`)

Verdicts on the 14 decisive propositions: 11 SUPPORTED, 3 PARTLY (D01: the three-region claim is in the source, lithium genotype coverage not confirmable; D04: 'only mechanism that survives' withdrawn because PMID 17403689 exists; D07: 24747945 reports protection, not harm), 0 NOT SUPPORTED. D02 is SUPPORTED at metadata depth only (reason unreached). Coverage check of the first extraction: 12 points sampled, 11 PRESENT, 1 PRESENT_NARROWED (independence of the three acquired-epilepsy models, L17, now row E76), 0 MISSING; one anchor fixed (E12 now L30). Reconciliation sample: 8 rows, 3 confirmed outright, 5 with pointer or note defects repaired (NAC comparator is step X1; NRF2 not WWOX re-expression; no occurrence of 'reductive stress' in the repository; E52/E53 split; three-region claim supported). Evidence sample: 5 of 5 quotes verbatim; EV03 and EV04 extended; five rows added (EV06-EV10) for D01, D02, D04 (two) and D13, marked as read by the verifier. Narrowings applied: 'single blot' became 'one representative blot'; age conflict recorded; lithium genotypes per module record; 'retracted in full' rests on type fields; D13 inference is weak. Not reached: the retraction notice text, figures of 32000863 and 23251339, full texts of 24747945, 40729961, 42439630, 23140664, 36130098, 40902898, 29538645; the Europe PMC absence check was not re-run by the verifier. Open need (not read): the notice text of 28159761 and the 17403689 full text.

Recount after the audit (76 items): `legend_class` verified_or_corrected 33, already_present_and_used 26, new_to_legend 11, superseded_or_contradicted 5, unverified 1. `prior_brief_fate` modified 31, narrowed 22, kept 17, omitted 6. Items per kind: observation 20, inference 11, experiment 9, limit 9, recommendation 5, compound 4, and the other kinds as in Phase 1.
