# IT14 P4: glia / oligodendrocyte / myelination / maturation line (reconnaissance)

Package `glia_maturation_it14_p4_20261101`, branch `task/it14-p4`, Scientist agent p4. Written 2026-10-31 (Europe/Rome; package date per brief). Not medical advice. No individual regimen is proposed.

## 1. Decision

**RESTRICT.** The line advances only as a role-resolving question, never as a compound candidate. No pro-myelinating compound enters the ranking, the cards or the needs as a candidate.

Reasons, each tied to the evidence table (`evidence_table_it14_p4.tsv`, row ids E01-E34):

1. **The developmental myelin deficit is real at the cell and ultrastructure level but its driver is upstream of the oligodendrocyte.** Neuron-restricted deletion reproduces it (E01-E08), oligodendrocyte-lineage and astrocyte deletion do not (E10, E24), and neuron-restricted add-back restores EM counts, g-ratio and CC1+ cells while the oligodendrocyte lineage stays null (E13-E16). So the role is **secondary to the neuron for development**, with a primary oligodendroglial role shown **only under challenge (ageing, cuprizone) and only in an unreviewed preprint** (E23-E28).
2. **"Secondary to the neuron" is not yet "primary neuronal signal".** Every in vivo neuronal manipulation (Synapsin-Cre deletion, neuronal AAV) also changes seizures, survival and glycaemia, so a seizure- or illness-mediated route is not excluded. The only seizure-free tests are one co-culture (E09, n=4 v 4, one laboratory, DRG neurons), a primary null-OPC monoculture (E23, preprint) and human spheroids (E12, all lineages knocked out).
3. **Maturation block is favoured over loss, not demonstrated against sampling.** OPCs rise while CC1+ cells fall, caspase-3 shows no OL death, and the co-culture shift is a ratio within MBP+ cells (E02, E04, E09). But the S-KO has no total-lineage count, no proliferation label, one age, and counts per area in a thinner tract; the CC1 loss is about three times the PDGFRa gain (E02).
4. **No myelin-directed compound has ever been given to any WWOX-deficient system**, no post-onset arm exists for any myelin readout (add-back is P0-P5, E15), and a myelin gain has no demonstrated functional meaning in WWOX. The human precedents are other diseases (Section 5): one surrogate-endpoint success, one negative trial.

Not "do not advance" because: a bypass question can be asked with an existing assay (Section 5, C1/C2) and the preprint reports an OPC-intrinsic delay that would make a receptor-level push on OPCs plausible. That is a question, not a benefit claim.

**Single most informative missing measurement:** an oligodendrocyte-lineage census in the Synapsin-Cre deletion **before the first spontaneous seizure** (about P7-P8 against onset near P9; E20 shows the rat MBP/CNP deficit at PND5 before its seizures), with total lineage (Olig2 or SOX10), PDGFRa, CC1, an S-phase label and MBP in the same sections, counts as totals per tract and per animal. It separates seizure-secondary from neuron-primary and maturation block from loss from sampling. Caveat: myelin barely begins at P7-P8, so dynamic range is low; the fallback is a seizure-suppressed arm (D7, no data exist).

**Reopening condition (any one):** (i) the preprint is peer-reviewed with source data and its text/bar disagreement (E26) resolved; (ii) an independent laboratory reproduces either the DRG-OPC effect or the null-OPC differentiation delay; (iii) the pre-onset census above is reported; (iv) a human neuron-OPC system from isogenic patient-allele lines with an oligodendrocyte compartment is reported (E34: none found).

## 2. What I read, at what depth, what I knew before

Knew before: the module's needs, cards and IT10-IT13 packages carry the neuronal-versus-oligodendrocyte genetics (CLAIM 003, N-13) and the preprint receipt. I expected the line to be closed as "wrong compartment". It is narrower than that (see Section 6 edits).

| Source | Depth in this session |
|---|---|
| `wwox_function_reference_it6`, `wwox_data_census_it6`, `mouse_wwox_p17_it6_p4`, `question_it11_p22` README and premises, `recoverable_it13_p3b`, `functional_it13_p3a`, `snrna_it13b_pv` README | read (text), targeted at myelin/OL lines |
| `needs.json` NEED-MYELINATION and NEED-NEUROINFLAMMATION-GLIA | read in full; cards F02, H02, J01, L01 and packets read for the myelin fields (F02 and H02 deeply, J01 and L01 headings and glial assertions only) |
| `analysis/wwox_myelin_oligodendrocyte_census_20260921.md`, dossier `PMID33914858.md` section 2.3-2.6, CC-20261003W4-B-MYELIN-CELLAUT-01 | read |
| 33914858 (Brain 2021) | full text, myelin/OL sections and all captions read; Fig 4 and Fig 6 rendered at 130 dpi and read by eye (values hand-read, about +/-5%); supplements not opened |
| 34747138 (EMBO MM 2021), 42422765 (2026), 31340538, 32000863 | myelin/OL/glia passages and legends from the shared XML (keyword-extracted, not full re-read); figures not opened |
| PPR1124524 preprint | full PDF text read (results, discussion, legends); figures not re-rendered (the 2026-10-23 receipt did that); supplementary captions only |
| Other-disease precedents (Section 5) | abstracts only (Europe PMC core records) |

Public routes only: Europe PMC REST, ChEMBL REST. No e-mail, no accounts, nothing downloaded into the shared corpus.

**Independence from the snRNA verification.** The GSE158684 reading (IT13b) is used only as "technically ambiguous" context (E05, E30): sample structure per the IT13b README is one pooled library per genotype, with a doublet rule that removes more control neurons. It supports no row and no conclusion here. If the verification is later negative or positive, nothing in this decision changes.

## 3. Answers

**(1) Is there a WWOX measurement of OL function or myelination beyond transcript abundance?** Yes, in five systems (E01-E22), tabulated with model, perturbation, measure, unit, n and locator: EM myelinated axon counts and g-ratio (E06, E07, E15, E24-E26), MBP/CNP protein intensity (E01, E13, E17), CC1/PDGFRa/NG2 cell counts (E02, E03, E14, E20, E24, E26), OPC differentiation assays (E09 co-culture; E23 monoculture), human spheroid staining and EM (E12), and one functional proxy, callosal evoked-response latency in slices (E08, 8 slices/5-6 mice per arm). Not found: iPSC-derived oligodendrocytes from WWOX patient lines (E34), conduction after add-back, EM or conduction after Olig2-Cre deletion at a developmental age. Almost all rows are one laboratory (HUJI); the independent ones are the lde rat (E20) and the Cheng mouse (E21, E22, qualitative and partly peripheral). The human 2026 organoid has no OL compartment and is a limit, not a result (E32).

**(2) Perturbations or rescues separating primary glial from secondary effects.** See `discrimination_matrix_it14_p4.tsv`. Cell-type deletion and add-back (D1, D2) show the neuronal route is necessary and sufficient for the developmental deficit in vivo; the oligodendrocyte-promoter add-back is uninformative (weak expression, E18). Seizure/illness are split off only in vitro (D3-D5), by small or unreplicated assays. Seizure suppression with a myelin endpoint (D7), post-onset add-back (D8) and pre-onset sampling in the mouse deletion (D6) do not exist.

**(3) Maturation delay versus cell loss versus sampling.** Readouts that exist: CC1+ and PDGFRa+ per 0.5 mm2 (ratio-type, no lineage total), NG2+CC1+ transition cells, caspase-3 co-stain, a morphological class share within MBP+ cells, cluster proportions (ambiguous, E05), in vitro fractions per culture (E23), and persistence to week 37 in spheroids (E12c, n 2 v 3). Pattern: OPC up, CC1 down, no apoptosis, in vitro fraction shift, persisting deficit, which fits a differentiation block. What cannot be excluded: net lineage loss (the CC1 fall is about 3 times the PDGFRa rise, E02, but COP/NFOL stages are not counted), density artefact in a thinner callosum (CC thickness is lower in the null, E17), pseudoreplication (sections as points), and permanence versus delay (the S-KO dies prematurely, age not stated for Synapsin-Cre and 3-4 weeks in the 2026 summary, and the null by about P15-P25, so only one age exists; the rescue reaches near-WT EM at 6 months, E15, but only as prevention).

**(4) Primary, secondary or unresolved.** Developmental hypomyelination: **secondary to neuronal WWOX loss** (non-cell-autonomous), with the neuron-intrinsic versus seizure/illness-mediated sub-question **unresolved**. Oligodendroglial WWOX: **a primary role under ageing and toxic demyelination in an unreviewed preprint** (E24-E28), with no demonstrated contribution to the DEE developmental deficit (the authors' own residual-gap reading after neuronal rescue is a hypothesis, E15). Gliosis: unchanged from the needs record (secondary or unresolved).

**(5) External interventions with a pertinent question.** `candidates_it14_p4.tsv` (fields: identity, action, context, other-disease precedent kept separate, WWOX evidence, transferability hypothesis labelled IPOTESI, hypothesised benefit, discriminating test, contrast, falsification, context flags, depth). Summary:

| Id | Intervention | Precedent (other disease, NOT WWOX evidence) | Verdict |
|---|---|---|---|
| C1 | clemastine (M1 antagonist; also H1) | ReBUILD PMID 29029896 (adult MS optic neuropathy, VEP latency surrogate met, fatigue); Cree 2018 PMID 29244098 and Odell 2024 PMID 38942888 (neonatal mouse hypoxic white-matter injury) | RESTRICT: in-vitro bypass question only |
| C2 | benztropine (muscarinic antagonist) | Deshmukh 2013 PMID 24107995, preclinical | RESTRICT: class comparator, not independent support |
| C3 | bexarotene | CCMR One PMID 34418398: primary efficacy not met, poor tolerability | DO NOT ADVANCE |
| C4 | metformin | Neumann 2019 PMID 31585093 (aged OPCs) | DO NOT ADVANCE (age mismatch, glycaemia flag) |
| C5 | WNT restraint (XAV939, research compound) | Fancy 2011 PMID 21706018 | HOLD: measure WNT activity first |
| C6 | SOX10 stabilisation | none outside the preprint | HOLD |

The one experiment asked of C1/C2: in the Repudi co-culture design (wild-type OPCs on Wwox-null versus wild-type DRG neurons) and in null-OPC monoculture, does the compound move OPCs from pre-myelinating to myelinating morphology, with total MBP+ cell number reported beside the ratio? Contrast: KO-DRG versus WT-DRG interaction, and a Chrm1-deficient OPC arm to separate M1 from H1. Falsification: no shift, an equal shift on wild-type neurons (a generic push, not a rescue of a WWOX-dependent defect), persistence in Chrm1-deficient OPCs, or a ratio shift with fewer MBP+ cells. Benefit would remain a hypothesis even if this passed: nothing links a myelin gain to function in WWOX. Compound-action-context-benefit is applied to C1 only to that extent; the other rows are documented limits.

## 4. Things that look new against the module, and what they are not

- The module already holds the preprint (receipt FTR-20261023-PPR1124524-02) and the neuron/OL genetics. What the needs and cards **do not** carry: the DRG-OPC co-culture (E09), the CC1/PDGFRa/NG2/caspase-3 and conduction rows of the S-KO (E02-E04, E08), the null-OPC monoculture and Olig2-Cre baseline-versus-challenge split (E23-E27), the human spheroid OL data (E12), and the hand-read ratio of CC1 loss to OPC gain (E02).
- The preprint's own text and figure disagree in one panel (E26: 59.1 v 36.1 in the text, about 106 v 58 in the bars). The direction agrees; the size is unverified.

## 5. Edits this implies (proposals only; nothing outside the package was touched)

1. **`cards/F02_myelination_activity_sign.card.json` and `.packet.json`: misattributed manifest.** Lines 28, 117, 142 (card) and 81, 106 (packet) cite "PMID 34268881 manifest" for the neuron-versus-oligodendrocyte myelin genetics. PMID 34268881 is the brain-organoid paper and contains no such result (its text mentions myelin only in two references); the source is PMID 33914858. Line 63 (the GSE156243 deposit) is correct. Verifier check: search the body text of `files/fulltext/PMID34268881_Steinberg2021_PMC_r2.xml` for myelin/oligodendrocyte outside the reference list (I found only two reference-list hits).
2. **F02 `not_known` item "The quantified MBP or g-ratio after neuronal AAV rescue"** should be scoped to 42422765: PMID 34747138 Fig 5 quantifies EM counts and g-ratio at P17 and 6 months (E15). Item "Whether an oligodendroglial WWOX function exists under remyelination stress" should cite the unreviewed preprint (answered there, not established).
3. **`needs.json` NEED-MYELINATION:** add observations for E09 (co-culture), E02-E04 and E08 (S-KO CC1/PDGFRa/NG2/caspase-3, conduction latency), E12 (spheroid OL data, scoping O3 to 42397075 only), E23-E26 (preprint, labelled PREPRINT, same laboratory, with the E26 text/bar disagreement), and E20 (rat APC+ counts, MAP2 alternative). In `intervention_direction.rationale`, replace "the axonal signal may be absent" by "an unidentified neuron-derived signal; OPC-side dysfunction in null OPC monoculture (preprint)". `track.basis` "secondary to neuronal WWOX loss" stays but should add "for development; primary oligodendroglial role only under challenge, unreviewed".
4. **`analysis/mechanism_intervention_map.md` N-13:** the sentence "a cell-autonomous oligodendroglial role under remyelination stress is in observation from a review-sourced primary still queued" is stale (the preprint was read 2026-10-03 and 2026-10-23). Narrow "wrong cell compartment" to "neuron-first for development; oligodendrocyte-lineage under challenge, preprint".
5. **Roadmap/closing record:** register the reopening conditions of Section 1 and the single missing measurement (pre-onset census).
6. **No change** to ranking, view, `NEED-NEUROINFLAMMATION-GLIA`, L01, H02 or the four current files. The IT13 recoverable record ("myelination recovered only as prevention") stays correct and can add that the prevention is durable to 6 months by EM (E15).

## 6. What a verifier must check (the decisive datum)

The decisive link is E09 plus E23: whether a Wwox-null neuron (or a Wwox-null OPC) alone, with no seizures or illness in the dish, shifts OPC differentiation. Both are small and from one laboratory (n=4 v 4 coverslips; preprint). Re-open Fig 6D of the Brain paper (OUP browserprint page 30) and the preprint's Fig 2e/f; confirm the n per condition and whether total MBP+ number is given. Secondary: re-measure the CC1 and PDGFRa point clouds of Fig 4G (page 25) to confirm the 3:1 ratio of CC1 loss to OPC gain (my hand readings: CC1 about 155 v 72, PDGFRa about 43 v 70 per 0.5 mm2).

## 7. Limits

Figure values are hand-read from rendered pages. Supplement figures (Suppl 5-8 of the Brain paper) were not opened; E03, E04, E10, E11 rest on the text. Precedent papers in Section 3 (5) were read at abstract level only; clemastine safety in a seizure-prone infant brain and benztropine human myelin data were not looked up (label lookup not attempted). Absence of an iPSC-oligodendrocyte hit in title/abstract searches is not absence of data. The in vivo labs behind E01-E19 are one group; counting them as independent would be an error. The sample size of every WWOX myelin readout is 3 animals per arm or smaller, and the statistics are Student t tests on fields, sections or axons.
