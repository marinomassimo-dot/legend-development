# IT9 P1: question-first selection of qualified WWOX observations for candidate generation

Scientist-a, 2026-10-30, task `ORCH-ROADMAP-IT9-20261030`, branch `task/it9-p1`. Exploratory, computational, descriptive. **Not medical advice; a computational result is not therapeutic efficacy.** The reference genotype is a WWOX-DEE genotype class; no individual-level record is used. This folder edits no scientific current file, registry, ledger, card, need or earlier cycle folder. Nothing here is a pass/fail test, so no pre-registration was needed; the usable/reserved rules of section 3 were written before the rows were typed and are applied by `check_seeds.py`.

## 1. Decision (stated first)

**Five questions are retained, six candidate questions are dropped (one of them, read-through, survives only as predicted-only rows inside Q1).** The retained set covers the three requested areas and deliberately keeps the excitability question free of drug-response data, so exploration cannot be seeded with the antiseizure answers.

| Q | Question | Goal | Direction of the alteration | Usable seed rows | Why it is in |
|---|---|---|---|---:|---|
| Q1 | Residual function and protein fate of the missense and splice alleles | Track B, BROAD DURABLE | protein down (one non-neural system); mechanism UNRESOLVED (A degradation-limited, B synthesis-limited, C stable-but-inert) | 6 | only route to restoring the lost function itself; the reference-class datum (protein absent, transcript comparable) exists, sparse by nature |
| Q2 | Glycolysis, lactate and the HIF1A-PDK-PDH axis | Track A, PARTIAL/BRIDGE | transcript up in two human neural systems; PDK1 and valence UNCERTAIN | 17 | best-read transcript question, same method in two human neural systems, with a stated maturity rival |
| Q3 | Integrated stress response, proteostasis-adjacent sets, mitochondrial translation | Track A, PARTIAL/BRIDGE | UNCERTAIN (signs opposite between systems; protein and phospho unmeasured) | 13 (+3 named gaps) | direction uncertain by design: the conditional pair is the point; no protein-level seed exists |
| Q4 | Excitation-inhibition state and inhibitory interneurons (circuit state, not drug response) | Track A, PARTIAL/BRIDGE | hyperexcitability up (function, several systems); inhibitory component down in mouse, up in organoid: UNCERTAIN | 12 | richest function data; seeds are circuit states and cell-type markers, every drug response is held out |
| Q5 | Myelination and glial state, non-cell-autonomous | Track A, PARTIAL/BRIDGE | hypomyelination down (mouse); glial reactivity UNCERTAIN (up in two mouse models, down in the rat) | 10 | independent biology (neuron-driven myelin loss, glia) not reachable through the ISR/metabolic or excitability seeds |

Dropped (rows kept in `seeds.tsv` with `question_id` D1..D6 and `usable_for_generation=no`, so a verifier can re-derive why):

| D | Candidate | Why dropped (a result) | Reopen when |
|---|---|---|---|
| D1 | Wnt / MYC / progenitor state | alteration inseparable from maturity/composition (Wnt readouts move with culture time in 62 unperturbed spheroids; 4v2 permutation minimum p 1/15; engineered knockout shifts composition); mouse P17 Wnt set not moved; the one lever tried (A51) is held out | age-matched patient-line contrast with a composition model |
| D2 | GSK3B de-repression; mTOR/autophagy | GSK3B: one phospho western (n=3, images, one laboratory), kinase activity unmeasured, lithium response held out; mTOR: transcripts only, mixed signs | kinase activity or a second laboratory in neurons; phospho-S6/4E-BP1 in a neural WWOX-deficient system |
| D3 | Chloride gradient / GABA polarity | no E_GABA, chloride, NKCC1/KCC2 protein or GABA response in any WWOX system; only an unsigned transcript ratio | any chloride measurement in a WWOX-deficient neuron |
| D4 | Premature-stop read-through, NMD | no read-through or NMD measurement on any WWOX allele; only a sequence prediction (32 stop-gained alleles, 23 predicted NMD-sensitive, 8 predicted to escape, 1 borderline); reference class carries no stop in the stated analysis (itself resting on an unmeasured intron-8 retention prediction) | an NMD assay on a WWOX nonsense allele |
| D5 | Systemic glycaemia and growth | an endpoint and confounder of every null-mouse readout, not an alteration to aim at (held out as endpoint) | a neural-selective question that needs a systemic covariate |
| D6 | Redox / oxidative stress | signs counter-directional in two independent non-DEE systems; no neural WWOX-loss redox measurement | a redox readout in a WWOX-deficient neural system |

Candidate lines not turned into questions because they are interventions, not alterations: gene addition, splice correction, endogenous boost (they appear only as held-out responses in Q1).

## 2. Denominators (units stated; counts are of items, not of evidence)

Items considered: **108** = 90 needs observations (`needs/needs.json`, 22 needs; checker reports 90 observations) + 14 IT7 P4 context-matrix quantities (the same data re-viewed, so not independent of the 90) + 4 items read in earlier cycles. The 90 needs observations are the primary denominator; `obs_disposition.tsv` assigns every one.

| Needs observations (n = 90), by class of the best seed row citing them | n |
|---|---:|
| with at least one usable seed row | 33 |
| reserved-only (intervention response or held-out endpoint) | 17 |
| unusable-only (see reason classes) | 26 |
| excluded as not a WWOX observation or a design detail (11 other-disease precedents, 2 repository method results of IT7 P3, 1 design detail) | 14 |

| Seed rows (n = 111) | n |
|---|---:|
| usable_for_generation = yes | 58 (all inside Q1 to Q5) |
| reserved_for_evaluation = yes | 17 |
| unusable (usable = no, reserved = no, a measurement or prediction exists) | 31 |
| named gaps (nothing measured; kept so the gap is a recorded gap, not counted as observations) | 5 |

Per question (`coverage.tsv`): Q1 16 rows (6 usable, 5 reserved, 5 unusable); Q2 23 (17, 2, 4); Q3 18 (13, 0, 2, 3 gaps); Q4 18 (12, 5, 1); Q5 17 (10, 2, 5); D1 to D6 17 rows, none usable.

Unusable reason classes (31 rows): maturity/composition confound 8 (all D1); unverified or carried-not-opened 5; dropped question, thin data 5 (D2); not evaluable in the system 4 (organoid glia, thresholded-list absence, mixed GO/KEGG, organoid oligodendrocytes); other context 3 (fly with amyloid x2, redox D6); prediction only 2; case-level 2; non-specific 1; direction not tabulated 1. Reserved rows (17): intervention response 13, endpoint 4. Named gaps: 5. Usable rows by context tier: A (human neural WWOX-loss system) 28, B (mouse/rat neural) 22, C (non-neural WWOX-loss cells) 8; D (other species or context) 0 by rule.

Usable rows by observation class (never merged into one causal edge): expression 34, protein or phospho 12, functional effect 12. Usable rows by direction: up 24, down 14, uncertain 13, unchanged 7.

## 3. Rules for the usable/reserved split (so a verifier can challenge them)

* **usable** (`usable_for_generation=yes`) only if the row is (i) a MEASUREMENT in a WWOX-loss or variant system, not a prediction; (ii) typed at one level (`expression`, `protein`, `phospho`, `activity`, `function`, `pathology`) and never converted into another; (iii) not an intervention response and not an endpoint whose use would leak the answer; (iv) in context tier A, B or C. Fly with amyloid, cancer-line overexpression of another allele, and other-disease precedents are tier D and never usable.
* **reserved** (`reserved_for_evaluation=yes`): any compound/vector/diet response, and the endpoints that such responses are scored on (seizure burden, SWD rate, burst frequency, survival, myelinated-axon counts, g-ratio, gliosis under add-back, glucose, weight). A row is never both usable and reserved (checked). For Q4 and Q5 the PRESENCE of hyperexcitability or hypomyelination is a usable state; the quantitative endpoint is reserved.
* **unusable**: measured or predicted but not fit to seed generation, with a `reason_class`. **Gap**: not measured.
* **Evaluation guard** (column `evaluation_guard`): Q2 module genes (SLC2A1, HK2, LDHA, LDHB, BNIP3 up, PDK1 down) are the IT7 P3 held-out readout, so a generator seeded with them must not be scored by signature reversal of that readout; ISR-set direction is unresolved, so no candidate may be scored by ISR-set reversal.
* Context is on every row: system, cell type, age, variant class. Contexts are never pooled across systems; where two human systems share a row it is because the same method produced both numbers, which are both in the locator.

## 4. seeds.tsv for P2 (machine-readable)

`seeds.tsv` (111 rows, 18 columns, rectangular, tab-separated). Columns in the requested order: `seed_id, question_id, entity_symbol, process_id, entity_type, level, direction, context, usable_for_generation, reserved_for_evaluation, reason, source_locator`, then extras `hgnc_id, species_observed, context_tier, observation_class, reason_class, evaluation_guard`.

* Exactly one of `entity_symbol` (HGNC approved symbol; 46 distinct symbols) and `process_id` is filled. `process_ids.tsv` declares every `process_id` (GO term, `SET:*` gene set with members, `CHEBI:*`, or a local `STATE:*` label). GO ids were checked against QuickGO on 2026-10-30; two ids the source paper names (GO:1901607, GO:0043038) are obsolete with no replacement, so the nearest current terms (GO:0008652, GO:0006418) are used and flagged as search hints.
* **One addition to the brief's vocabulary: `direction=unchanged`** (an observed no-change or comparable value). P2 should treat it as non-directional, not as `uncertain`. Directions are the observed direction of the alteration; the unresolved VALENCE (protective or harmful) is carried by the conditional pair in `questions.tsv`, not by the direction column.
* **HGNC verification** (`hgnc_check.tsv`): all 46 symbols were fetched on 2026-10-30 from the live HGNC REST service (key-less; only gene symbols sent) and are `Approved` with the same symbol; each carries one MGI ortholog link. Not by memory. Collision notes carried from the needs table: the Wnt factor the papers call TCF4 is `TCF7L2` (HGNC TCF4 is a different gene); the protein IBA1 is `AIF1`; the protein GAD65/67 is GAD2/GAD1 (one antibody, combined densitometry; both rows say so); eIF2alpha is `EIF2S1`, PERK `EIF2AK3`, GCN2 `EIF2AK4`.
* **Mouse versus human.** `species_observed` is the species the measurement was made in. Of the 70 gene/protein rows: human 46, mouse 19, fly 4, rat 1. Mouse and rat observations are written under the HGNC symbol of the human ortholog (the MGI link is present for all; the orthology is symbol-level, the rat orthologs of GFAP and AIF1 were not checked). The fly rows (WWOX, LDHA, ATF4, SOD1) are tier D, none is usable; fly orthology is not one-to-one and was not mapped. Among usable rows with an HGNC symbol: human 21, mouse 12, rat 1.
* **Traceability.** `source_locator` abbreviations: `NEED-<id>:O<n>` = statement id in `needs/needs.json` (every one is resolved by `check_seeds.py`); `CM-IT7P4:Q<nn>:<context>` = `context_differences_it7_p4_20261029/context_matrix.tsv`; `SN-IT7P1:` = `subnetwork_it7_p1_20261029/derived_gene_values.tsv`; `P7:`/`P6:` = `hnpc_gse126075_it5_20261029/` tables; `MP17-IT6P4:` = `mouse_wwox_p17_it6_p4_20261029/results/verdicts.tsv`; `FR-IT6P5:W<nn>` = `wwox_function_reference_it6_20261029.md` row; `DC-IT6P3:` = `wwox_data_census_it6_20261029.md` section; `DC-IT5P6/P7` = `wwox_systems_comparison_it5_20261029.md`. Per-gene numbers printed in Q2/Q3 reasons are re-read from the committed tables by the checker.
* **Re-derive a row:** `python3 check_seeds.py --root .. --dir .` (offline; PASS expected). It checks vocabularies, usable xor reserved, HGNC ids, process declarations, need and statement ids, and the printed per-gene values.

## 5. What each question cannot yet use (feeds the reopening conditions)

See the `cannot_yet_use_feeds_reopening` column of `questions.tsv`; condensed:

* Q1: synthesis, solubility and half-life of Q230P in any neural cell; a WWOX function ruler (SDR activity unsupported); route mapping on Q230P; transcript of the reference-class splice-acceptor allele; any NMD/read-through measure; the endothelial TMT proteome table (PMID 38563965, figshare supplement, NOT opened here, non-neural); the second allele of the reference class.
* Q2: PDH phosphorylation/activity, OCR/ECAR, NAD(H), 13C tracing in a neural WWOX-deficient system; MTBLS12344 (not public); E-MTAB-14792 single-cell (403); a replicated module above six genes; an age-matched contrast separating maturity from genotype.
* Q3: ATF4 protein, eIF2alpha-P, PERK/GCN2-P, puromycin or ribosome profiling in any WWOX-deficient neural system; replicated CAGE libraries; matched-maturity isogenic contrast with activity silencing.
* Q4: chloride/E_GABA; interneuron-subtype electrophysiology in human neurons; PV and GAD counts in a neuron-restricted deletion; controls not pooled.
* Q5: human white-matter data with oligodendrocytes; a microglia-containing human model; glial read before P14; gene-level myelin values.
These map onto IT8 P4 reopening conditions 1 (a compound-response measurement in a WWOX-deficient human neural system) and 2b (this folder is the first input to the method of that condition; the method itself is IT9 P2).

## 6. Already explored, per question (so P3 can mark proposals new versus known; not a claim of 'never attempted')

Source: ranking IT8 P9 units (`ranking_it8_p9_20261029/units.tsv`, 27 interventions plus 3 axes), the needs table `sources` (cards, hypothesis ids) and the hypotheses ledger headings. 'Carded' means a card exists with the stated evaluation depth; it is not a result.

| Q | Carded interventions (unit: card) | Hypotheses | Threads |
|---|---|---|---|
| Q1 | U01 PBA/bile-acid chaperones (A01); U02 proteasome inhibitors (A02); U03 client-binding chaperone (A03, abstention); U04 ER-proteostasis (A04, abstention); U05 HSP70 axis (A05, abstention); U06 read-through (B01/B02); U07 AAV9 gene addition (C01/C04; the only card with WWOX-side assertions); U08 splice ASO/editing (C02, abstention); U09 endogenous boost (C03, abstention) | HYP-20260709-08 (stress-tested), -02, -03, -06 | IT4 E1a read-through enumeration; IT5 P8 missense recovery; IT6 P5 function reference; IT6 P6 route blockade |
| Q2 | U13 LDH (E02); U14 DCA/PDK (E03, I01); U15 ketogenic diet (E04 and early-benefit map) | HYP-20260709-01 (proposed-to-L9, evidence 1/3), -05; HYP-20261026-11 (generated) | IT3 complex I/LDH/PDH; IT5 P6/P7; IT5 P9 DCA closed loop; IT7 P1 subnetwork and P3 comparison (no added value for network routes; signature route not detected, not excluded; card-linked compounds excluded by design); IT8 P4 |
| Q3 | U12 ISR modulators (E01); U04 ER-proteostasis (A04) | HYP-20261026-10 (generated, not ranked) | IT3/IT4 ISR hypcurrent; GCN2/PERK gap; PARS2 fly reading; kinase interactome reconciliation; IT5 P6/P7; IT6 P4; IT8 P5 loop 1 |
| Q4 | U21 d-APV and NMDAR/AMPAR class (F01, F04); U17 ethosuximide; U25 apinocaltamide (H01); U20 vigabatrin/GABA-AT (EB-VGB-01, H02); U23 bumetanide (F03, abstention); U27 magnesium (P11); U16 cannabidiol; U18 ACTH/corticosteroids/phenobarbital | HYP-20261027-01 (generated) | IT6 P9 NMDAR pharmacology. **Heavily carded; P3 should mark antiseizure-class proposals KNOWN.** |
| Q5 | U22 pro-myelinating agents (F02, abstention); U26 glial-reactivity modulators (J01, abstention); vigabatrin-myelin exposure (H02) | HYP-20260709-07; HYP-20260705-02 | IT6 P10 glial reactivity (organoid glial panel, P47T query) |

I read the READMEs of IT5 P8, IT4 E1a, IT6 P6, IT6 P9, IT6 P10, IT5 P9 and IT8 P5 only at the head (thread statement); their contents beyond that are not summarised here.

## 7. Per-question conditional hypotheses (direction not resolved by convenience)

Full text is in `questions.tsv` (columns `conditional_hypothesis_if_protective_or_option_A` and `..._if_harmful_or_option_B`; Q1 holds three options A, B, C). In one line each: Q1 degradation-limited versus synthesis-limited versus stable-but-inert; Q2 glycolytic shift adaptive/artefact (do not suppress) versus harmful (lower lactate/glycolytic flux, relieve PDK restraint); Q3 ISR adaptive (do not attenuate, possibly spare) versus harmful (attenuate), and a lowered ISR makes attenuation meaningless; Q4 inhibitory hypofunction primary (restore inhibitory tone) versus excitatory gain primary with compensatory GABAergic rise (lower gain at the source); Q5 glial reactivity protective (do not suppress) versus harmful (lower), and myelin loss secondary to activity (control activity) versus direct.

## 8. Method and checks run

Built by `build_seeds.py` (hand-typed rows, vocabularies, HGNC fetch), `build_tables.py` (dispositions, coverage), `build_questions.py` (questions), `check_seeds.py` (consistency). `python3 build_seeds.py --out . [--check-hgnc]` then `build_tables.py --root .. --out .` then `build_questions.py --out .`. No LINCS analysis, no download of any dataset, no new measurement; the only network calls were HGNC REST (gene symbols) and QuickGO (GO ids), both key-less and without any personal string. Release checks are listed in the final report of the Orchestrator hand-over.

## 9. UNVERIFIED and limits

* Every statement was carried from the needs table, the IT7 P1/P4 tables, the IT5/IT6 re-analyses or the IT6 P3/P5 documents; no paper was opened here and no receipt is staged. A verifier should re-derive from the locators, not from this text. Where a carried statement was already flagged in its source it is flagged again on the row (P252A/P282A assignment; PMID 28749468 phospho blots carried, not opened; patient-organoid protein level seen only as 'very low by immunoblot' in the IT6 P5 reading).
* The usable/reserved/unusable split is a judgment table in the sense of IT8 P4: the rules of section 3 are explicit but their application to a row (for example, treating the PRESENCE of hyperexcitability as a usable state while reserving its quantity) is a decision a verifier may challenge. The decision least certain: the Q2 module genes are usable but carry an evaluation guard because they were the IT7 readout.
* Mouse-to-human mapping is by symbol; fly is not mapped.
* The sign conventions of the hNPC GSEA rows (Q3 process sets) are derived, not printed, by the source paper (IT5 P6 adjudication).
* Seed-count tallies depend on how a statement is split into rows; the primary denominators are the 90 needs observations.
* No efficacy, dose, safety or clinical statement is made or implied.

## 10. For the batch path (nothing was edited by this package)

Items the Orchestrator's batch mechanics might record: (1) a discovery-ledger pointer to this folder as the IT9 P1 question set (no new claim); (2) the observation that the IT7 P3 readout genes are now seeds of Q2 under an evaluation guard (a reopening note for the IT7 comparison); (3) the 'unchanged' direction value as a documented extension of the P2 seed vocabulary; (4) no receipts: none staged.

## 11. Files

`README.md` · `questions.tsv` (11 rows: 5 retained, 6 dropped) · `seeds.tsv` (111 rows) · `process_ids.tsv` · `hgnc_check.tsv` · `obs_disposition.tsv` (108 items) · `coverage.tsv` · `build_seeds.py` · `build_tables.py` · `build_questions.py` · `check_seeds.py`
