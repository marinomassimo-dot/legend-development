# IT9 P1: question-first selection of qualified WWOX observations for candidate generation

Scientist-a, 2026-10-30, task `ORCH-ROADMAP-IT9-20261030`, branch `task/it9-p1`. Exploratory, computational, descriptive. **Not medical advice; a computational result is not therapeutic efficacy.** The reference genotype is a WWOX-DEE genotype class; no individual-level record is used. This folder edits no scientific current file, registry, ledger, card, need or earlier cycle folder. Nothing here is a pass/fail test, so no pre-registration was needed; the usable/reserved rules of section 3 were written before the rows were typed and are applied by `check_seeds.py`.

## 1. Decision (stated first)

**Five primary questions (Q1 to Q5) and two secondary, thin questions (Q6, Q7; restored in v2 after the verifier report, see CHANGES.md) are retained; five candidate questions are dropped (read-through survives only as predicted-only rows inside Q1).** The retained set covers the three requested areas and deliberately keeps the excitability question free of drug-response data, so exploration cannot be seeded with the antiseizure answers.

| Q | Question | Goal | Direction of the alteration | Usable seed rows | Why it is in |
|---|---|---|---|---:|---|
| Q1 | Residual function and protein fate of the missense and splice alleles | Track B, BROAD DURABLE | protein down (one non-neural system); mechanism UNRESOLVED (A degradation-limited, B synthesis-limited, C stable-but-inert) | 4 | the route aimed at the lost function itself; the reference-class datum (protein absent, transcript comparable) exists, sparse by nature |
| Q2 | Glycolysis, lactate and the HIF1A-PDK-PDH axis | Track A, PARTIAL/BRIDGE | transcript up in two human neural systems; PDK1 and valence UNCERTAIN | 20 | best-read transcript question, same method in two human neural systems, with a stated maturity rival |
| Q3 | Integrated stress response, proteostasis-adjacent sets, mitochondrial translation | Track A, PARTIAL/BRIDGE | UNCERTAIN (signs opposite between systems; protein and phospho unmeasured) | 13 (+3 named gaps) | direction uncertain by design: the conditional pair is the point; no protein-level seed exists |
| Q4 | Excitation-inhibition state and inhibitory interneurons (circuit state, not drug response) | Track A, PARTIAL/BRIDGE | hyperexcitability up (function, several systems); inhibitory component down in mouse, up in organoid: UNCERTAIN | 15 | richest function data; seeds are circuit states and cell-type markers, presence and direction only; every drug response and endpoint magnitude is held out |
| Q5 | Myelination and glial state, non-cell-autonomous | Track A, PARTIAL/BRIDGE | hypomyelination down (mouse); glial reactivity UNCERTAIN (up in two mouse models, down in the rat) | 10 | independent biology (neuron-driven myelin loss, glia) not reachable through the ISR/metabolic or excitability seeds |
| Q6 | MYC and radial-glia state (secondary) | Track A, PARTIAL/BRIDGE | MYC up in radial glia (single-cell, three lines) and MYC+ fraction up; valence and maturity within radial glia UNCERTAIN | 2 | a within-cell-type contrast, which is the standard answer to the composition confound that sank the bulk Wnt rows |
| Q7 | GSK3B de-repression, phospho (secondary) | Track A, PARTIAL/BRIDGE | pSer9 down in the null mouse; kinase activity unmeasured | 1 | meets the same usable rule as the Q4 western rows; thin (one measurement set) |

Dropped (rows kept in `seeds.tsv` with `question_id` D1..D6 and `usable_for_generation=no`, so a verifier can re-derive why):

| D | Candidate | Why dropped (a result) | Reopen when |
|---|---|---|---|
| D1 | Wnt (bulk organoid) readouts | alteration inseparable from maturity/composition (Wnt readouts move with culture time in 62 unperturbed spheroids; 4v2 permutation minimum p 1/15; engineered knockout shifts composition); mouse P17 Wnt set not moved, so no cross-system agreement; the MYC and radial-glia rows moved to Q6 | age-matched patient-line contrast with a composition model |
| D2 | mTOR/autophagy | transcripts only, mixed signs (GSK3B moved to Q7) | phospho-S6/4E-BP1 in a neural WWOX-deficient system |
| D3 | Chloride gradient / GABA polarity | no E_GABA, chloride, NKCC1/KCC2 protein or GABA response in any WWOX system; only an unsigned transcript ratio | any chloride measurement in a WWOX-deficient neuron |
| D4 | Premature-stop read-through, NMD | no read-through or NMD measurement on any WWOX allele; only a sequence prediction (32 stop-gained alleles, 23 predicted NMD-sensitive, 8 predicted to escape, 1 borderline); reference class carries no stop in the stated analysis (itself resting on an unmeasured intron-8 retention prediction) | an NMD assay on a WWOX nonsense allele |
| D5 | Systemic glycaemia and growth | an endpoint and confounder of every null-mouse readout, not an alteration to aim at (held out as endpoint) | a neural-selective question that needs a systemic covariate |
| D6 | Redox / oxidative stress | signs counter-directional in two independent non-DEE systems; no ROS or oxidative-damage readout in a neural WWOX-loss system found in the sources read (the resazurin reading is a metabolic-activity dye, seed S033) | a redox readout in a WWOX-deficient neural system |

Candidate lines not turned into questions because they are interventions, not alterations: gene addition, splice correction, endogenous boost (they appear only as held-out responses in Q1).

## 2. Denominators (units stated; counts are of items, not of evidence; v2 values)

Items considered: **108** = 90 needs observations (primary denominator; `needs/needs.json`, 22 needs) + 14 IT7 P4 context-matrix quantities (the same data re-viewed, not independent of the 90) + 4 items read in earlier cycles. `obs_disposition.tsv` assigns every one.

| Needs observations (n = 90), by class of the best seed row citing them | n |
|---|---:|
| with at least one usable seed row | 35 |
| reserved-only (intervention response or held-out endpoint) | 18 |
| unusable-only | 23 |
| excluded as not a WWOX observation or a design detail (11 other-disease precedents, 2 IT7 P3 method results, 1 design detail) | 14 |

| Seed rows (n = 131; v1 was 111, ids S001..S111 unchanged, S112..S131 appended) | n |
|---|---:|
| usable_for_generation = yes | 65 (all inside Q1 to Q7) |
| reserved_for_evaluation = yes | 26 |
| unusable | 35 |
| named gaps (nothing measured) | 5 |

Per question, usable / reserved / unusable / gaps (`coverage.tsv`; v1 in brackets): Q1 4/5/7 [6/5/5]; Q2 20/2/4 [17/2/4]; Q3 13/0/2/3 gaps [13/0/2/3]; Q4 15/8/5 [12/5/1]; Q5 10/6/5 [10/2/5]; Q6 2/2/1 [new]; Q7 1/0/0 [new]; D1 0/1/6 [0/2/8]; D2 0/0/4 [0/0/5]; D3 0/0/0/2 gaps; D5 0/2/0 [0/1/0]; D6 0/0/1.

Reason classes of all 131 rows: usable 65; reserved intervention response 15 and endpoint 11; unusable: maturity/composition 10, other context 7, not evaluable in the system 5, dropped question 4, unverified or carried-not-opened 3, prediction only 2, case-level 2, non-specific 1, direction not tabulated 1; named gaps 5. Usable rows by context tier: A 26, B 29, C 10, D 0 by rule. By observation class (never merged): expression 38, functional effect 13, protein or phospho 8, histology area or count 4, cell count 2; usable rows by direction: up 31, down 15, uncertain 10, unchanged 9.

## 3. Rules for the usable/reserved split (so a verifier can challenge them)

* **ONE rule for presence and magnitude (v2, verifier H4).** A usable row encodes the PRESENCE and DIRECTION of a state; the magnitudes and counts of the endpoints on which reserved rows are scored (burst/seizure/SWD rate, firing rate, myelinated-axon count, g-ratio, GFAP/IBA1 area and counts, MYC+ fractions, glucose, weight) live in RESERVED rows (`RESERVED_ENDPOINT`, `guard_tag HELD_OUT_ENDPOINT`), including the untreated-genotype baselines; treated-versus-untreated contrasts are reserved too. Magnitudes of measures that no reserved row is scored on (for example inhibitory current amplitude, PV counts) may stay in usable rows. `check_seeds.py` enforces this by token and magnitude tests.
* **3a. One confound standard (v2, verifier M2).** A transcript row from the 4v2 organoid contrast is usable only if a second, independent system agrees in sign (Q2 module genes: hNPC agrees; NPY: mouse agrees) or the row is at protein/function level; single-system composition-confounded organoid rows are demoted (organoid GAD1, GAD67 area, GABRB2, GABRB3). The Q2 maturity rival is still stated in the question; cross-system agreement lets a row in, it does not remove the rival.
* **usable** (`usable_for_generation=yes`) only if the row is (i) a MEASUREMENT in a WWOX-loss or variant system, not a prediction; (ii) typed at one level (`expression`, `protein`, `phospho`, `activity`, `function`, `pathology`) and never converted into another; cell counts and image area fractions are typed `pathology` (observation_class `cell_count` or `histology_area_or_count`), not `protein`; (iii) not an intervention response (no intervention-arm sentence in the row, its context, its guard or its locator) and not an endpoint magnitude whose use would leak the answer; (iv) in context tier A, B or C. Fly with amyloid, cancer-line overexpression of another allele, and other-disease precedents are tier D and never usable.
* **reserved** (`reserved_for_evaluation=yes`): any compound/vector/diet response, and the endpoints that such responses are scored on (seizure burden, SWD rate, burst frequency, survival, myelinated-axon counts, g-ratio, gliosis under add-back, glucose, weight). A row is never both usable and reserved (checked). For Q4 and Q5 the PRESENCE of hyperexcitability or hypomyelination is a usable state; the quantitative endpoint is reserved.
* **unusable**: measured or predicted but not fit to seed generation, with a `reason_class`. **Gap**: not measured.
* **Evaluation guards, machine-readable (v2, verifier M11).** Column `guard_tag` (values in `guards.tsv`): `IT7_READOUT6` on every usable Q2 row about the six IT7 readout genes or the glycolysis set (SLC2A1, HK2, LDHA, LDHB, BNIP3 up, PDK1 down): do not score candidates seeded from them by signature reversal of that readout; `ISR_SIGN_UNRESOLVED` on the ISR rows: no scoring by ISR-set reversal; `HELD_OUT_ENDPOINT` on state rows whose magnitude is a reserved endpoint. `evaluation_guard` stays as the human sentence; `check_seeds.py` fails a usable row that has guard text but no tag, or an IT7/ISR row without its tag. Whether the P2 engine reads `guard_tag` is for P2/P3 to confirm.
* Context is on every row: system, cell type, age, variant class. Contexts are never pooled across systems; where two human systems share a row it is because the same method produced both numbers, which are both in the locator.

## 4. seeds.tsv for P2 (machine-readable)

`seeds.tsv` (131 rows, 20 columns, rectangular, tab-separated). Columns in the requested order: `seed_id, question_id, entity_symbol, process_id, entity_type, level, direction, context, usable_for_generation, reserved_for_evaluation, reason, source_locator`, then extras `hgnc_id, species_observed, context_tier, observation_class, reason_class, evaluation_guard`, and (v2, appended at the end) `guard_tag, change_ref`. Row ids S001..S111 are stable across versions.

* Exactly one of `entity_symbol` (HGNC approved symbol; 48 distinct symbols) and `process_id` is filled. `process_ids.tsv` declares every `process_id` (GO term, `SET:*` gene set with members, `CHEBI:*`, or a local `STATE:*` label). GO ids were checked against QuickGO on 2026-10-30; two ids the source paper names (GO:1901607, GO:0043038) are obsolete with no replacement, so the nearest current terms (GO:0008652, GO:0006418) are used and flagged as search hints.
* **One addition to the brief's vocabulary: `direction=unchanged`** (an observed no-change or comparable value). P2 should treat it as non-directional, not as `uncertain`. Directions are the observed direction of the alteration; the unresolved VALENCE (protective or harmful) is carried by the conditional pair in `questions.tsv`, not by the direction column.
* **HGNC verification** (`hgnc_check.tsv`): all 48 symbols were fetched on 2026-10-30 from the live HGNC REST service (key-less; only gene symbols sent) and are `Approved` with the same symbol; each carries one MGI and one RGD ortholog link (v2 adds the RGD column; the rat orthology of AIF1 and GFAP is therefore linked). Not by memory. Collision notes carried from the needs table: the Wnt factor the papers call TCF4 is `TCF7L2` (HGNC TCF4 is a different gene); the protein IBA1 is `AIF1`; the protein GAD65/67 is GAD2/GAD1 (one antibody, combined densitometry; both rows say so); eIF2alpha is `EIF2S1`, PERK `EIF2AK3`, GCN2 `EIF2AK4`.
* **Mouse versus human.** `species_observed` is the species the measurement was made in. Of the 78 gene/protein rows: human 48, mouse 24, fly 4, rat 2. Mouse and rat observations are written under the HGNC symbol of the human ortholog (the MGI link is present for all; the orthology is a symbol-level link, not a one-to-one claim). The fly rows (WWOX, LDHA, ATF4, SOD1) are tier D, none is usable; fly orthology is not one-to-one and was not mapped. Among usable rows with an HGNC symbol: see seeds.tsv (species_observed).
* **Traceability.** `source_locator` abbreviations: `NEED-<id>:O<n>` = statement id in `needs/needs.json` (every one is resolved by `check_seeds.py`); `CM-IT7P4:Q<nn>:<context>` = `context_differences_it7_p4_20261029/context_matrix.tsv`; `SN-IT7P1:` = `subnetwork_it7_p1_20261029/derived_gene_values.tsv`; `P7:`/`P6:` = `hnpc_gse126075_it5_20261029/` tables; `MP17-IT6P4:` = `mouse_wwox_p17_it6_p4_20261029/results/verdicts.tsv`; `FR-IT6P5:W<nn>` = `wwox_function_reference_it6_20261029.md` row; `DC-IT6P3:` = `wwox_data_census_it6_20261029.md` section; `DC-IT5P6/P7` = `wwox_systems_comparison_it5_20261029.md`. Per-gene numbers printed in Q2/Q3 reasons are re-read from the committed tables by the checker.
* **Re-derive a row:** `python3 check_seeds.py --root .. --dir .` (offline; PASS expected). It checks vocabularies, usable xor reserved, HGNC ids, process declarations, need and statement ids, and the printed per-gene values.

## 5. What each question cannot yet use (feeds the reopening conditions)

See the `cannot_yet_use_feeds_reopening` column of `questions.tsv`; condensed:

* Q1: the immunoblot of the patient organoids (premise of the demoted S004/S005); synthesis, solubility and half-life of Q230P in any neural cell; a WWOX function ruler (SDR activity unsupported); route mapping on Q230P; transcript of the reference-class splice-acceptor allele; any NMD/read-through measure; the endothelial TMT proteome table (PMID 38563965, figshare supplement, NOT opened here, non-neural); the second allele of the reference class.
* Q2: PDH phosphorylation/activity, OCR/ECAR, NAD(H), 13C tracing in a neural WWOX-deficient system; MTBLS12344 (not public); E-MTAB-14792 single-cell (403); a replicated module above six genes; an age-matched contrast separating maturity from genotype.
* Q3: ATF4 protein, eIF2alpha-P, PERK/GCN2-P, puromycin or ribosome profiling in any WWOX-deficient neural system; replicated CAGE libraries; matched-maturity isogenic contrast with activity silencing.
* Q4: chloride/E_GABA; interneuron-subtype electrophysiology in human neurons; PV and GAD counts in a neuron-restricted deletion; controls not pooled.
* Q5: human white-matter data with oligodendrocytes; a microglia-containing human model; glial read before P14; gene-level myelin values.
These map onto IT8 P4 reopening conditions 1 (a compound-response measurement in a WWOX-deficient human neural system) and 2b (this folder is the first input to the method of that condition; the method itself is IT9 P2).

## 6. Already explored, per question (so P3 can mark proposals new versus known; not a claim of 'never attempted')

Source: ranking IT8 P9 units (`ranking_it8_p9_20261029/units.tsv`, 27 interventions plus 3 axes), the needs table `sources` (cards, hypothesis ids) and the hypotheses ledger headings. 'Carded' means a card exists with the stated evaluation depth; it is not a result.

| Q | Carded interventions (unit: card) | Hypotheses | Threads |
|---|---|---|---|
| Q1 | U01 PBA/bile-acid chaperones (A01); U02 proteasome inhibitors (A02); U03 client-binding chaperone (A03, abstention); U04 ER-proteostasis (A04, abstention); U05 HSP70 axis (A05, abstention); U06 read-through (B01/B02); U07 AAV9 gene addition (C01/C04; the only card with WWOX-side assertions; outside the cards, the record also holds reserved rows S009 and S016); U08 splice ASO/editing (C02, abstention); U09 endogenous boost (C03, abstention) | HYP-20260709-08 (stress-tested), -02, -03, -06 | IT4 E1a read-through enumeration; IT5 P8 missense recovery; IT6 P5 function reference; IT6 P6 route blockade |
| Q2 | U13 LDH (E02); U14 DCA/PDK (E03, I01); U15 ketogenic diet (E04 and early-benefit map) | HYP-20260709-01 (proposed-to-L9, evidence 1/3), -05; HYP-20261026-11 (generated) | IT3 complex I/LDH/PDH; IT5 P6/P7; IT5 P9 DCA closed loop; IT7 P1 subnetwork and P3 comparison (no added value for network routes; signature route not detected, not excluded; card-linked compounds excluded by design); IT8 P4 |
| Q3 | U12 ISR modulators (E01); U04 ER-proteostasis (A04) | HYP-20261026-10 (generated, not ranked) | IT3/IT4 ISR hypcurrent; GCN2/PERK gap; PARS2 fly reading; kinase interactome reconciliation; IT5 P6/P7; IT6 P4; IT8 P5 loop 1 |
| Q4 | U21 d-APV and NMDAR/AMPAR class (F01, F04); U17 ethosuximide; U25 apinocaltamide (H01); U20 vigabatrin/GABA-AT (EB-VGB-01, H02); U23 bumetanide (F03, abstention); U27 magnesium (P11); U16 cannabidiol; U18 ACTH/corticosteroids/phenobarbital | HYP-20261027-01 (generated) | IT6 P9 NMDAR pharmacology. **Heavily carded; P3 should mark antiseizure-class proposals KNOWN; interneuron-function, resting-state and non-NMDAR channel mechanisms are not carded here (not carded is not 'new').** |
| Q5 | U22 pro-myelinating agents (F02, abstention); U26 glial-reactivity modulators (J01, abstention); vigabatrin-myelin exposure (H02) | HYP-20260709-07; HYP-20260705-02 | IT6 P10 glial reactivity (organoid glial panel, P47T query) |

| Q6 | U10 A51 (D01), U11 tankyrase (D02) | HYP-20261025-09 (Wnt axis, not MYC) | - |
| Q7 | U24 lithium (G01) | none | - |

I read the READMEs of IT5 P8, IT4 E1a, IT6 P6, IT6 P9, IT6 P10, IT5 P9 and IT8 P5 only at the head (thread statement); their contents beyond that are not summarised here.

## 7. Per-question conditional hypotheses (direction not resolved by convenience)

Full text is in `questions.tsv` (columns `conditional_hypothesis_if_protective_or_option_A` and `..._if_harmful_or_option_B`; Q1 holds three options A, B, C). In one line each: Q1 degradation-limited versus synthesis-limited versus stable-but-inert; Q2 glycolytic shift adaptive/artefact (do not suppress) versus harmful (lower lactate/glycolytic flux, relieve PDK restraint); Q3 ISR adaptive (do not attenuate, possibly spare) versus harmful (attenuate), and a lowered ISR makes attenuation meaningless; Q4 inhibitory hypofunction primary (restore inhibitory tone) versus excitatory gain primary with compensatory GABAergic rise (lower gain at the source); Q5 glial reactivity protective (do not suppress) versus harmful (lower), and myelin loss secondary to activity (control activity) versus direct.

## 8. Method and checks run

Built by `build_seeds.py` (hand-typed rows, vocabularies, HGNC fetch), `build_tables.py` (dispositions, coverage), `build_questions.py` (questions), `check_seeds.py` (consistency). `python3 build_seeds.py --out . [--check-hgnc]` then `build_tables.py --root .. --out .` then `build_questions.py --out .`. No LINCS analysis, no download of any dataset, no new measurement; the only network calls were HGNC REST (gene symbols) and QuickGO (GO ids), both key-less and without any personal string. Release checks are listed in the final report of the Orchestrator hand-over.

## 9. UNVERIFIED and limits

* v2 re-reads at full text (Europe PMC / PubMed Central, 2026-10-30): 30290271 (cytokines, interneurons, channel genes), 35328751 (PDK/PDH), 28749468 (ovarian ER-stress blots), 34634460 (EPSC distribution) and 36828035 (hallmark enrichment). Still carried, not opened: 42422765, 36537114, 32000863, 38563965, 30853297, and abstract-level only: 42397075, 33914858, 29808465, 25012504, 31340538, 34747138.

* Every statement was carried from the needs table, the IT7 P1/P4 tables, the IT5/IT6 re-analyses or the IT6 P3/P5 documents; no paper was opened here and no receipt is staged. A verifier should re-derive from the locators, not from this text. Where a carried statement was already flagged in its source it is flagged again on the row (P252A/P282A assignment; PMID 28749468 phospho blots carried, not opened; patient-organoid protein level seen only as 'very low by immunoblot' in the IT6 P5 reading).
* The usable/reserved/unusable split is a judgment table in the sense of IT8 P4: the rules of section 3 are explicit but their application to a row (for example, treating the PRESENCE of hyperexcitability as a usable state while reserving its quantity) is a decision a verifier may challenge. The decision least certain: the Q2 module genes are usable but carry an evaluation guard because they were the IT7 readout.
* Mouse-to-human mapping is by symbol; fly is not mapped.
* The sign conventions of the hNPC GSEA rows (Q3 process sets) are derived, not printed, by the source paper (IT5 P6 adjudication).
* Seed-count tallies depend on how a statement is split into rows; the primary denominators are the 90 needs observations.
* No efficacy, dose, safety or clinical statement is made or implied.

## 10. For the batch path (nothing was edited by this package)

Items the Orchestrator's batch mechanics might record: (1) a discovery-ledger pointer to this folder as the IT9 P1 question set (no new claim); (2) the observation that the IT7 P3 readout genes are now seeds of Q2 under an evaluation guard (a reopening note for the IT7 comparison); (3) the 'unchanged' direction value as a documented extension of the P2 seed vocabulary; (4) no receipts: none staged.

## 11. Files

`README.md` · `CHANGES.md` · `questions.tsv` (13 rows: 7 retained, 6 dropped; D1 to D6 kept) · `seeds.tsv` (131 rows) · `guards.tsv` · `process_ids.tsv` · `hgnc_check.tsv` · `obs_disposition.tsv` (108 items) · `coverage.tsv` · `build_seeds.py` · `build_tables.py` · `build_questions.py` · `check_seeds.py`
