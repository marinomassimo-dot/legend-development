# IT9 P6 case record: the HIF axis in the glycolytic shift (question Q2), closed through the whole loop

Scientist-c, 2026-10-30, task `ORCH-ROADMAP-IT9-20261030`, branch `task/it9-p6`. Non-canonical research material. **Not medical advice; no dose, route, schedule or
individual recommendation. A compatible action of a context-free network is not a predicted benefit; an expression result is not a protein result and a protein result
is not a functional effect; association is not modulation and modulation is not rescue. Proposed, not performed: no experiment of this record was run.** Reference
genotype: a WWOX-DEE genotype class; no individual-level record. No registration, contact, spend or access step was taken.

## 0. Verdict (first)

| Item | Result |
|---|---|
| The case | One axis, not one drug: the HIF axis (HIF-1alpha, HIF-2alpha/EPAS1, ARNT). It is the only Q2 item whose link to the WWOX seeds has direct primary support, and that support is **non-neural** (section 1). |
| State | **KEEP-AS-PROPOSAL as a mechanism experiment (IT9 P4c-e, E-01), now a card: `K01_hif_axis_glycolytic_shift`** (hypothesis; position F3 on `NEED-PDH-PYRUVATE-AXIS`: from the target, intervention not tested in WWOX). No claim of efficacy; no compound is recommended. |
| Why not more | HIF-1alpha and HIF-2alpha PROTEIN were never measured in a WWOX-deficient neural cell; HIF1A mRNA is flat; a human fibroblast line shows LOWER cytoplasmic HIF-1alpha in two of four conditions with the nuclear fraction unchanged (a different compartment from the nuclear increase in mouse cells: neither confirms nor contradicts it); the engine edge is review-sourced; PX-478 has 0 ChEMBL rows, a nitrogen-mustard alert and adult phase 1 data only. |
| Direction control | A prolyl-hydroxylase inhibitor RAISES HIF (the disease direction, a "mimic"): it is a direction control, not a lever. Roxadustat itself is dropped as a lever (seizures and brain necrosis in rats on its label; thyromimetic action is from Morita 2025, not the label, which lists secondary hypothyroidism; see `qualification_it9_p4c_e_20261030/CORRECTION_NOTE_20261031.md`). |
| Discriminating experiment | Section 7: conditional arms (the HIF-dependent shift adaptive versus harmful), a premise measurement first, controls, falsifier, and a table of which result changes which decision. |
| Guard | `IT7_READOUT6`: SLC2A1, HK2, LDHA, LDHB, BNIP3 and PDK1 were the IT7 held-out readout and the seed itself. They are observations here; **no lever may be evaluated by reversal of those six genes**, and the experiment reads glycolytic genes beyond them (PGK1, ALDOA, ENO1, PFKP, PKM). |
| Ranking | New entry U28 (origin `generated_in_it9`, type mechanism probe) in `ranking_it8_p9_20261029/`; group G4b (not selectable), next-experiment priority NX2; no existing group moved (section 9). |

## 1. WWOX observation (the seeds)

Seeds are rows of `generation_it9_p1_20261030/seeds.tsv` (question Q2); the guard rows are in `guards.tsv`.

| Seed | Observation | System | Level | Direction | Read at | Notes |
|---|---|---|---|---|---|---|
| S028 | HIF-1alpha protein readily detected in the NUCLEI of knockout cells in normoxia and barely in wild type (qualitative nuclear-fraction detection); the difference disappears under hypoxia | Wwox-null mouse embryonic fibroblasts (non-neural); also MCF7 knockdown, brown fat, muscle | protein (nuclear) | up | PMID 25012504 (Abu-Remaileh 2014), complete read, receipt `FTR-20260814-25012504-01`; needs O1 | less hydroxylation in knockout MEFs; HIF1A knockdown rescues glucose uptake in them; HIF1A mRNA is comparable in skeletal muscle of knockout and wild-type mice (the paper's mRNA statement is for muscle, not MEFs); digoxin RAISES blood glucose in knockout mice (reversing their low glucose) and lowers GLUT1 and PHD3 expression; Pdk1 UP in these cells |
| S031 | lactate higher in all four conditions; cytoplasmic HIF-1alpha LOWER in two of four | human fibroblast line with WWOX sgRNA (non-neural) | function; protein | lactate up; cytoplasmic HIF-1alpha down in two of four, nuclear fraction unchanged | PMID 35328751, partial read, receipts `FTR-20261026-35328751-05` and earlier; needs O2 and counter item 4 | the decrease is CYTOPLASMIC, the nuclear fraction (the transcriptionally active pool, the compartment measured in S028) is unchanged, one blot repetition is shown, and no significant difference is reported for the other two conditions: this neither confirms nor cleanly contradicts S028 |
| S032 | respiratory-to-glycolytic shift measured directly | Wwox-null mouse embryonic fibroblasts | function | up | PMID 25012504, abstract level in this repository | succinate only a non-significant trend |
| S023 | HIF1A mRNA flat (centred -0.285 organoid, -0.119 hNPC; neuron d14 -0.577) | two human neural systems | expression | unchanged | GSE156243 (4 KO v 2 WT libraries), GSE126075 (one library per arm) | HIF acts at protein level, so mRNA is not informative about the axis |
| S025 | HIF-type glycolysis/lactate set higher (centred +0.53 organoid, +0.46 hNPC) | two human neural systems | expression | up | same deposits | a broader 19-gene glycolysis panel is not distinguishable from chance in hNPC; transcript is not flux |
| S022 | PDK1 lower in sign only (organoid -0.385, hNPC -0.674) | same | expression | uncertain | same deposits | inside the single-gene null; higher in neurons d14 and in non-neural fibroblasts: the HIF1A to PDK1 valence differs by cell type |
| (descriptive) | EPAS1 3.80x, HK2 4.73x, SLC2A1 2.67x, ARNT 1.46x, HIF1A 0.84x, PDK1 0.78x (KO over WT, normalised counts) | human cerebral organoid, week 15 | transcript | up/flat | `qualification_it9_p4c_e_20261030/organoid_target_gene_rows.tsv`; needs O7 | 4 versus 2 libraries; the glycolytic genes also fall with culture time (maturity or composition); EPAS1 is absent from the hNPC table (absent, not zero) |

**Guards.** `IT7_READOUT6` forbids scoring candidates by opposition of SLC2A1, HK2, LDHA, LDHB, BNIP3, PDK1 or any set containing them; the proposal was legitimately generated
(the seeds were usable for generation) and nothing in this record evaluates a lever on them. **Absent data:** HIF-1alpha and HIF-2alpha protein, HIF activity (reporter, hydroxylation)
and flux in any WWOX-deficient neural cell were not found in the sources read (a negative search is not a negative result).

## 2. External contribution (signed network edges: record type and provenance)

| Edge | Record in the network | Reference and what it is | Level and system | Sign | Grade (IT9 P4c-e) |
|---|---|---|---|---|---|
| ARNT_HIF1A to BNIP3 (also HK2, SLC2A1) | SIGNOR transcriptional record on the complex (HIF-1) | PMID 27692180, a **review** (one reference for BNIP3 and HK2; with a second paper for SLC2A1) | transcript statement; no cell context in the record | + | REVIEW_SOURCED |
| HIF1A to BNIP3 (the primary record behind the same pair) | CollecTRI (about 200 references) | PMID 10922063, Bruick 2000, full text read (references not) | transcript and promoter activity; CHO-K1, CV-1, Rat-1, PAM212, HepG2, ECV-304, HEK293 reporter; hypoxia, CoCl2, DFO; none neural | + | PLAUSIBLE_NON_NEURAL |
| PX-478 to HIF-1 target genes (compound side, not an edge) | not in the network | PMID 15026543 (Welsh 2004, abstract); Koh 2008 (abstract) | HIF-1alpha protein and GLUT-1/VEGF in colon xenografts; cancer lines | lowers | COMPOUND_SIDE_SUPPORT (GLUT-1 only is a seed gene) |
| EGLN2 to FOXO3 to SLC2A1 (the roxadustat chain) | SIGNOR post-translational (inhibition) + CollecTRI | PMID 24990963 (Zheng 2014, full); PMID 18268343 (Emerling 2008, abstract) | protein stability in breast cancer cells and MEFs; FOXO3a represses HIF-1 activity at the Glut-1 promoter | network + ; abstract states repression | SIGN_CONTRADICTED_BY_ABSTRACT |

Mode matters (IT9 P4b-a and P4c-e): a protein-stability or coupling record cannot be applied to a transcript seed, and a review-sourced record on a complex says nothing about a neural cell.
The seed-to-lever link that justifies a test is therefore **not** the engine edge but row 4 of `edge_provenance_E.tsv` (WWOX deficiency to HIF-1alpha to glycolytic genes, Abu-Remaileh 2014), non-neural.

## 3. Candidate generation (IT9 P2)

The v2/v3 seed engine proposed, in the Q2 expression set and the "opposes" arm, PX-478 (rank 4; Z robust against the total- and in-degree nulls 8.88; compatible action "opposes";
contributing seeds LDHA and LDHB through HIF1A at hops 1 to 3; `evaluation_forbidden_on = IT7_READOUT6`; not found by the direct search; `results/candidates_Q2.tsv`) and, in the "mimics" arm, HIF stabilisers and the other
generated compounds of section 4. A proposal produced by seeds that are themselves the held-out readout is a lead, not evidence.

## 4. Qualification (IT9 P4b-a, P4b-b, P4c-e): the Q2 candidates and their states

| Candidate | State | Decisive datum (stored in the qualification tables) |
|---|---|---|
| PX-478 (E-01) | **KEEP-AS-PROPOSAL** (mechanism experiment; promise MODERATE for the axis, LOW for the compound; depth MEDIUM; priority MEDIUM) | the axis has direct non-neural WWOX support; against the compound: 0 ChEMBL rows, mustard alert, adult IV phase 1 only, no CNS or paediatric data |
| roxadustat (E-02) | **DROP** as a lever; kept as a direction-control principle | pushes the seeds in the disease direction by construction; label: seizures common, secondary hypothyroidism, brain necrosis in rats (thyromimetic action: Morita 2025, not the label) at 3 to 6 times the AUC, no paediatric data |
| belzutifan (P3-03) | **INCONCLUSIVE** (go/no-go defined) | HIF-2alpha protein in WWOX-deficient neural cells never measured; adult brain EPAS1 is vascular (HPA); mouse cortical HIF-2alpha knockout has no developmental phenotype |
| balsalazide, ramelteon, ceperognastat (P3-01, -02, -04) | **DROP** (insufficient support for the chain, not "inactive") | target belongs to the metabolite; receptors absent from the system; a protein-activity record applied to a transcript seed |
| AR-12 (P3-14), dichloroacetate (P3-15) | **REFERENCE-ONLY** | AR-12 is PDPK1, not a PDH kinase; dichloroacetate is both seed and target of the engine (PDK1), so its output adds nothing beyond the seed |

Counts: of the six Q2 records of P4b-a, DROP 3, INCONCLUSIVE 1, REFERENCE-ONLY 2; with E-01 and E-02, Q2 has KEEP 1, DROP 4, INCONCLUSIVE 1, REFERENCE-ONLY 2. **None of these states says a compound is inactive:
no compound-response measurement exists in any WWOX system.**

## 5. Comparison with the carded neighbours (restated decisions, no change)

| Neighbour | Card | Where the HIF case stands relative to it |
|---|---|---|
| PDK inhibition (dichloroacetate; a nanomolar pan-isoform inhibitor as probe) | E03, I01 (IT8 P3, restated IT9 P4a: dichloroacetate inhibits the recombinant human kinases only at about 0.1 to above 5 mM in curated rows; the probe is added for the genotype-by-inhibitor arm) | Complementary and sequential: the HIF axis acts upstream of PDK1 in the chain HIF1A to PDK1 to PDH (DL-MECH-020), but the PDK1 valence is opposite across systems (up in MEFs, down in organoid and hNPC). The PDH-phosphorylation measurement of I01 and the HIF-protein measurement of K01 can share the same cells and the same lysates. K01 does not replace I01. |
| LDH lowering (stiripentol; a selective LDHA tool) | E02 (IT8 P3: stiripentol withdrawn as an LDH probe; IT9 P4a: LDHB selectivity of the nanomolar LDHA inhibitors) | The lactate readout of K01 is the same readout as E02's premise; lactate is a shared endpoint, not a shared lever. |
| Lactate/ECAR as the endpoint | need `NEED-LACTATE-LDH` | The experiment reads lactate or extracellular acidification and glucose uptake as the deciding readout, with five glycolytic genes reported individually, so a lever that lowers lactate through an off-axis route is not mistaken for HIF dependence. |
| Ketogenic diet | E04, EB-KD-01 | Unchanged; independent of this case. |

## 6. Position of the new card (re-derivable)

`repurposing_view.py positions` gives K01 x `NEED-PDH-PYRUVATE-AXIS`: **F3** (no signed WWOX-system result of the intervention; favourable support exists outside WWOX; the need has WWOX-system observations). Criteria not met: a signed
result in a WWOX system; one pertinent row is abstract-level. Pertinence rows: `DR-K01-001` (PX-478 lowers HIF-1alpha and GLUT-1 in cancer models; target-engagement, benefit), `DR-K01-002` (prenatal-hypoxia rat, mixed, unresolved),
`DR-K01-003` (0 ChEMBL rows, absent not negative, unresolved), `DR-K01-004` (roxadustat label seizures: safety signal, harm; a direction control). The need's direction stays **uncertain**: the case generates conditional hypotheses, it does not resolve the direction.

## 7. The discriminating experiment, with conditional arms (proposed, not performed)

Question: is the HIF-dependent part of the glycolytic shift in WWOX-deficient neural cells present, and is it adaptive or harmful?

**Step 0 (premise, one day of measurement).** HIF-1alpha and HIF-2alpha protein (and, if available, HIF hydroxylation or a HIF reporter) in WWOX-deficient versus corrected (isogenic add-back) human neural cells (hNPC or other 2D cultures in normoxia as primary; organoid week 8 to 15 only with a hypoxia-marker co-stain, because organoid cores are hypoxic and HIF protein can be raised in both genotypes). **Compartment:** nuclear and cytoplasmic fractions are measured separately (the MEF increase is nuclear; the fibroblast decrease is cytoplasmic with the nuclear fraction unchanged). **Oxygen:** normoxia and hypoxia (the MEF difference disappears under hypoxia). Wild-type cells are treated in parallel.
Falsifier of the whole axis in neural cells: neither protein is higher in the WWOX-deficient cells in the relevant compartment and oxygen condition (then the non-neural observation does not transfer and the axis is dropped for this question).

| Arm (only if step 0 shows a raised HIF protein) | What is done | Readouts | Control | Reads as |
|---|---|---|---|---|
| A. Genetic, primary | HIF1A knockdown; EPAS1 knockdown; both | **Deciding readout:** lactate or extracellular acidification and glucose uptake, plus PGK1, ALDOA, ENO1, PFKP and PKM reported individually (they are members of the 10-gene glycolysis set that is itself a guard-scope member of IT7_READOUT6 and the set that generated the seed, so a change there confirms the seed and does not independently validate a lever; the six IT7 genes and the set cannot decide). Context readouts: network activity (MEA or calcium), viability, SOX2/NEUN fractions | non-targeting guide; wild-type cells treated in parallel; corrected cells | HIF dependence of the shift and its consequence |
| B. PX-478-class lever | graded concentrations of PX-478 beside a non-mustard HIF-1alpha inhibitor and an inactive-mustard control | as A | vehicle; arm A as the specificity reference (a lever effect that arm A does not reproduce is not HIF-dependent) | pharmacological versus genetic agreement |
| C. Direction control | a prolyl-hydroxylase inhibitor run in BOTH knockout and corrected (or wild-type) cells: a non-thyromimetic one (molidustat, **a single 2025 report, TO BE VERIFIED**; not roxadustat) or genetic VHL/EGLN1 loss (a guard against off-target 2-oxoglutarate oxygenase effects) | as A | vehicle in both genotypes | in corrected/wild-type cells: does HIF stabilisation phenocopy the knockout seeds; in knockout cells: is HIF already saturated (any further rise), given that WWOX loss lowers HIF-1alpha hydroxylation in the MEF paper? |

| Result | Decision it changes |
|---|---|
| Step 0 negative | the HIF axis leaves Q2 for neural cells (U28 and the card move to a counter-evidence or abstention state by the rule); belzutifan stays INCONCLUSIVE with its go/no-go answered "no" |
| Knockdown lowers lactate and glucose uptake, and viability, network activity or differentiation WORSEN relative to untreated knockout and corrected cells | the shift is adaptive: lowering the axis is harmful; the PX-478-class lever is dropped; the card records a measured null for the lever |
| Knockdown lowers lactate and glucose uptake, and viability, network activity or differentiation IMPROVE relative to untreated knockout and corrected cells | the shift is harmful: the lever is kept as a mechanism experiment and arm B becomes the pharmacological test; a first WWOX-system row exists (F3 to F2 by rule) |
| Lactate (or acidification) falls but viability, network activity and differentiation are unchanged or discordant, or only some arms agree | the shift is HIF-dependent but its valence is NOT resolved: neither lever nor drop; the card stays F3 and the experiment is refined (dose, time, readout) |
| Knockdown moves nothing although protein is raised | HIF-independent glycolytic transcripts; the axis is dropped as a lever and the PDK/PDH route (I01) keeps its own test |
| Arm C phenocopies the knockout | HIF stabilisation is sufficient for the seeds (supports the direction); a saturated axis (no further rise) argues against any lever acting by lowering |
| Arm B and arm A disagree | the compound acts off-axis (alkylation, mustard); the pharmacological arm is uninterpretable and the genetic arm decides |

Controls and limits: the six readout genes may be reported but may not be used to decide; transcripts are not flux (lactate or acidification is measured); human cells at the week of the phenotype are prenatal-equivalent; one deposit's cells are a different line from any bench line.
A null with PX-478 alone is not read as absence of a HIF effect (arm A decides). Belzutifan, a HIF-2alpha inhibitor, enters only after step 0 shows HIF-2alpha protein.

## 8. What was regenerated (established order)

| Step | Command | Effect |
|---|---|---|
| Card | `case_it9_p6_hif_axis_20261030/build_packet_k01.py` (packet by hand-authored statements, card by the bridge) | `cards/K01_hif_axis_glycolytic_shift.packet.json` and `.card.json`; `check_cards.py`: 28 packets, 0 problems |
| Pertinence and identity | `coverage/assertion_pertinence.tsv` (+4 rows), `catalog/card_identity_declarations.tsv` (+2: PX-478 CHEMBL4117516, roxadustat CHEMBL2338329); `catalog_build.py build` | `catalog.jsonl.gz` byte-identical; `card_links.json` and `catalog_stats.json` carry the two links |
| Needs | `needs/needs.json` `NEED-PDH-PYRUVATE-AXIS`: card K01 in `sources.cards`, target EPAS1 (pathway member, counted apart), observation O7 (organoid EPAS1 and glycolytic ratios, descriptive), one conditional inference | `check_needs.py` OK (91 observations) |
| Coverage | `repurposing_coverage.py run` | one more card-linked row; pathway-member links +3 records (EPAS1) counted apart; headline L1 counts unchanged |
| Join and handoff | `repurposing_join.py run`; `handoff --date 2026-10-29 --write ...` | join queries and the module handoff regenerated |
| Work order | `view/work_order.json` `NEED-PDH-PYRUVATE-AXIS` | K01 added to `cards`, the HIF experiment added to `data` and `would_change`; kind unchanged (verify a hypothesis) |
| Ranking | `ranking_it8_p9_20261029/ranking_it8.py run` and `snapshot` | U28 entered; see the ranking README section 11 |
| View | `repurposing_view.py run`, `run --source shareable`, `package` | regenerated |

## 9. Load-bearing premises (for an independent verifier; also `premises.tsv`)

| # | Premise | Where to re-derive it |
|---|---|---|
| P1 | Wwox-null MEFs show higher nuclear HIF-1alpha protein in normoxia (qualitative), less hydroxylation, and HIF1A knockdown rescues glucose uptake (non-neural); HIF1A mRNA is comparable in skeletal muscle (Supp S4C), not shown for MEFs | PMID 25012504; manifest `deepdive_manifests/PMID25012504.json`; receipt `FTR-20260814-25012504-01`; needs O1 |
| P2 | A human fibroblast WWOX line shows LOWER cytoplasmic HIF-1alpha in two of four conditions (about 2-fold, p below 0.01 and 0.001), the nuclear fraction unchanged, one blot repetition shown; the MEF increase is nuclear (different compartments) | PMID 35328751; needs counter_evidence item 4; seed S031 |
| P3 | In the human KO organoid EPAS1 is 3.80x, HK2 4.73x, SLC2A1 2.67x, ARNT 1.46x, HIF1A 0.84x, PDK1 0.78x (4 v 2 libraries) | `qualification_it9_p4c_e_20261030/organoid_target_gene_rows.tsv`; recompute the ratios from GSE156243 normalised counts |
| P4 | HIF-1alpha and HIF-2alpha protein in WWOX-deficient neural cells were not found in the sources read | the absence statements of `qualification_it9_p4c_e_20261030/records/E-01_PX-478.md` section 6 and needs `inferred`; the search is a negative search |
| P5 | The engine edge is review-sourced; the primary record is non-neural | `edge_provenance_E.tsv` rows 1 and 2 |
| P6 | PX-478: 0 ChEMBL activity and mechanism rows; mustard alert; adult IV phase 1 only; no CNS data | `chembl_mechanism.tsv`, `identity.tsv`, `trials_summary.tsv` |
| P7 | A prolyl-hydroxylase inhibitor raises HIF (disease direction); roxadustat label lists seizures and secondary hypothyroidism; thyromimetic action is from Morita 2025 (passages), not the label | `records/E-02_roxadustat.md` |
| P8 | The six readout genes cannot be used to evaluate a lever (guard `IT7_READOUT6`) | `generation_it9_p1_20261030/guards.tsv` |
| P9 | The F/C/P position of K01 on `NEED-PDH-PYRUVATE-AXIS` is F3, produced by the existing rule from the pertinence rows | `repurposing_view.py positions` |
| P10 | The experiment arms are conditional: no outcome is assumed; the need direction stays uncertain | sections 6 and 7 |

## 10. UNVERIFIED

PX-478 supply and purity and its phase 1 results; the 2024 prenatal-hypoxia rat paper beyond its abstract; Koh 2008 and Welsh 2004 beyond abstracts; the SIGNOR web record behind the complex edge; whether the human fibroblast line is a knockout or a knockdown;
HIF protein and activity in any WWOX-deficient neural cell; HIF-2alpha protein (belzutifan's go/no-go); the maturity or composition contribution to the organoid glycolytic ratios.

## 11. For the batch path (nothing outside the module was edited)

1. A commit candidate recording card K01 as a non-canonical hypothesis (axis, conditional arms, guard) and the Q2 candidate states (PX-478 KEEP as a mechanism experiment; roxadustat DROP; belzutifan INCONCLUSIVE).
2. Discovery-ledger lead: "HIF axis: direct non-neural WWOX support; neural protein unmeasured; experiment with conditional arms" (no claim change).
3. Receipts: none staged (no paper newly read in full for this card).

## 12. Corrections after the independent verification (2026-10-31)

Report: `locator_audits/2026-10-31_it9_p6_verifier.md` (no HIGH finding). Repairs: **F1** the deciding readout is defined (section 7): lactate or acidification and glucose uptake, with PGK1, ALDOA, ENO1, PFKP and PKM reported individually; the six IT7 genes and the 10-gene set are guard-scope members and cannot decide.
**F2** the fibroblast observation is stated as cytoplasmic (about two-fold lower in two of four conditions), nuclear fraction unchanged, one blot repetition shown, against a nuclear increase in the MEFs: different compartments, so neither confirms nor contradicts. **F3** "equal or higher in the other two" is removed (the text reports only the two decreases and the nuclear null).
**F4** digoxin RAISES blood glucose in knockout mice and lowers GLUT1 and PHD3 expression (it does not "lower glucose"). **F5** "thyromimetic action" is attributed to Morita 2025, not the roxadustat label (secondary hypothyroidism); correction note added in `qualification_it9_p4c_e_20261030/CORRECTION_NOTE_20261031.md` (the original records are not rewritten); molidustat as a non-thyromimetic control is one report, TO BE VERIFIED.
**P1** "mRNA unchanged" is for skeletal muscle (Supp S4C), not MEFs. Experiment: step 0 specifies compartment and oxygen condition; a mixed or null outcome row was added; arm C runs the prolyl-hydroxylase inhibitor in both knockout and corrected cells.
Ranking note: existing entry U27 (extracellular magnesium) has a changed `M_mechanism` text against the R2 state (it now reads "1 catalogue family ... L2 none" instead of "no catalogue identity"), a consequence of the earlier P11 identity declaration and not of K01; its group and class did not move.
Counts: 31 units for the IT9 candidates (U28 through card K01 plus 30 proposal entries from 31 qualification records; 32 records in all, JTE-151 has two).
