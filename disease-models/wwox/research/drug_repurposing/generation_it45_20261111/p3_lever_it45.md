# IT45 P3: one observation, three levers — mechanism joined to the cell class where the phenotype was recorded

Non-canonical working note. Not medical advice; no dose, schedule or route. Reference genotype class only. Labels: DATO (read in a source), INFERENZA (derived here), IPOTESI (conditional). Nothing here nominates a compound for use.

**Order of writing, stated honestly.** Section 1 (relations, alternatives, discriminating results) was written first and committed before section 3 was filled. It was written *after* the author had seen the IT44 S3 pointer table, so the names of Kv7 compounds were known; what was not yet joined is stated in section 2. The frame therefore constrains the use of the joined data, not the author's prior knowledge of the names.

## 1 Frame (written before the join)
| Item | Statement |
|---|---|
| Observation | DATO (PMID 34634460, one preparation, as carried in INV-18): in Wwox-deficient layer II/III slices the resting potential is depolarised in a gene-dose order (−79.25, −75.51, −73.62 mV), the sag at a fixed step grows (1.18, 2.04, 2.57 mV), input resistance is higher and saturates at one allele, and bursts occur in 36 of 42 knockout, 4 of 23 heterozygote and 0 of 11 wild-type slices. |
| Competing explanations for the higher resistance and depolarised rest | (a) a lost resting K+ conductance (Kir- or K2P-type; the S11 path); (b) a larger Ih that depolarises (INV-18 branch B); (c) a smaller or immature cell with a higher resistance for geometric reasons (branch D); (d) less Kv7 (M-current) conductance near rest; (e) a compensatory change that hides the primary one. Not separated by the source. |
| Alternative lever (the point of this case) | A drug that **adds** a hyperpolarising conductance does not need the cause to be a K+ deficit: raising a Kv7 conductance near rest acts on (a)–(e) alike at the level of the membrane, and cannot say which is true. IPOTESI. |
| Where the lever would be inert or opposite | If bursts are driven by the network (AMPA/NMDA, IT40-Q01) rather than by intrinsic state; if Kv7 channels are not expressed in the recorded cells at that age; if a hyperpolarisation matched by current injection does the same thing (then the benefit is generic, not Kv7-specific). |
| Discriminating results (fixed here) | R1 Ba2+-sensitive difference current smaller in knockout → (a). R2 Kv7-blocker-sensitive difference current smaller in knockout → (d). R3 both normal and the blocker-sensitive Ih larger → (b). R4 all equal and capacitance smaller → (c). R5 an opener lowers bursts by more than a current-injection hyperpolarisation of equal size → a Kv7-specific benefit; by the same amount → a generic one; not at all → the lever is inert. |
| Outcome of interest | Burst incidence and the membrane readings in the same slices; the functional outcome (cognition, motor, quality of life) is **not** measured by any of this. |

## 2 What LEGEND already held, did not use, and acquired
| Piece | State before this case | Used by a consumer? |
|---|---|---|
| The observation and the three Ih branches | INV-18 | yes (INV-18 card) |
| Kv7 compounds in the mechanism tables | IT40 `mechsearch`: 7 molecules, 2 openers offered, **0 nominated, reason stated** (abstract-level reads) | yes, as an abstention |
| Kv7 compounds by measured activity | IT44 S3: 7 catalogue-status molecules, 4 absent from the mechanism path (flupirtine, azetukalner, quinidine and one tool probe) | listed in `pointers_it44.tsv`, tied to no lever |
| K-channel RNA by cell class | SCI44 coda, landed 34f93af0 | not tied to any lever table |
| Ba2+ premise (K2P openers sit in the Ba2+-weak subfamily; Kir2 has no opener beyond a Kir2.1-only one) | IT44 S11 reader | used by S11/V14 only |

## 3 The joined data (read from the held files; no new read of a primary paper)
Mouse cortex RNA, FPKM class means, P7 neurons against P7 astrocytes (`../kchan_expression_sci44_20261111/kchan_expression_mouse.tsv`; RNA is not current, number or share; two pools per class):
| Gene (channel) | Neurons | Astrocytes | Reading |
|---|---|---|---|
| Kcnq2 (Kv7.2) | 30.68 | 0.22 | neuron-enriched; also OPC 10.7 |
| Kcnq3 (Kv7.3) | 4.27 | 0.24 | neuron-enriched |
| Hcn1 | 2.62 | 0.10 | neuron-enriched |
| Hcn2 | 17.88 | 1.11 | neuron-enriched; myelinating oligodendrocytes 66.3 |
| Kcnj10 (Kir4.1) | 8.12 | 184.76 | **astrocyte**/oligodendrocyte-lineage |
| Kcnj2 (Kir2.1) | 0.74 | 0.46 | low in neurons; endothelium 41.8 |

INFERENZA from the join: the Ba2+ (Kir/K2P) lever and the Kv7 lever are **not equally attributable to a neuron** in a slice. A Ba2+-sensitive current can be glial (Kir4.1), so R1 needs a neuron-specific control to mean (a); the Kv7 blocker/opener arm has a neuron-enriched RNA substrate, so R2 and R5 are attributable to neurons with less extra design. The age caveat stands: P7 whole-cortex neurons are not P13–17 layer II/III pyramidal cells.

Activity pointers on the Kv7 lever (IT44 S3; ACTIVITY_ONLY, direction not read, nothing favourable): 7 molecules carry a catalogue status. Of these, three are reached by the mechanism path (a tool probe measured as an inhibitor, flindokalner, ezogabine) and four only by the activity path (flupirtine and azetukalner as openers measured by EC50 on KCNQ2/3; quinidine, whose row is an IC50 and therefore **not** an opener row; one tool probe). The IC50 and EC50 values come from different assay systems and are NOT_COMPARABLE across documents; no ranking is made.

## 4 The proposal that follows (IPOTESI) and what would drop it
* **Proposal.** Before any compound is discussed, run R1–R4 in the same slices; then, if R2 and R5 are posable, run one Kv7 opener arm against a current-injection hyperpolarisation of equal size. The compounds the repository can name for that arm are those of the S3 table, with their identity and source read first; none is nominated.
* **What adds to the earlier abstention.** IT40 abstained because the Kv7 evidence was abstract-level and the cell class unknown. Now the cell-class substrate is known (RNA, P7), the opener evidence has an activity pointer, and the design that would separate a generic from a Kv7-specific benefit is written. The abstention on a *compound* stays; the abstention on the *experiment* is lifted for planning.
* **What would drop it.** (i) Kv7 channels absent or low in P13–17 layer II/III pyramidal cells (needs a cell-class dataset at that age; not held); (ii) R2 normal in the knockout *and* an opener no better than equal current injection; (iii) bursts persisting under AMPA/NMDA block (the network, not the membrane, drives them: IT40-Q01); (iv) a benefit for burst incidence with no change in any function the family cares about (this case measures none).
* **Not done here.** No primary paper for an opener was re-read; the amplitude of Kv7 current at the resting potential of these cells is unknown; a Kv7 opener acts as a symptomatic anticonvulsant lever whatever the WWOX mechanism, so a burst fall would not be a WWOX-specific result (the rationale for WWOX and the general symptomatic efficacy of any antiseizure drug are kept separate).
