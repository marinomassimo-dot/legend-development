# WWOX Therapeutic Translation — Canonical Repair Candidates, Endpoint Audit and the Disease-Modification Test

**Six separable repair candidates, one contradiction adjudicated, one endpoint-level audit, one
negative measured against a stated denominator, and three experiments.**

> **Status:** non-canonical analysis artefact, third in the chain after
> [`mechanism_intervention_map.md`](mechanism_intervention_map.md) (the map) and
> [`therapeutic_translation_second_pass.md`](therapeutic_translation_second_pass.md) (the stress test).
> **READ-ONLY toward every canonical file.** Nothing here edits a claim, a paper record, the working
> model, the tracking log or a tracker entry. Each candidate below is written so that **Plan can
> integrate it and Orchestrator can commit it**, and so that a reader can refuse it on its own terms.
>
> **No new molecule appears anywhere in this file.** The drug list is exactly the drug list of the map.
> Two candidates *weaken a negative*, one *upgrades a conjunction*, two *downgrade*, one *splits*.
> None promotes a compound to clinical consideration.
>
> **Public edition.** Disease-level reasoning over the WWOX-DEE genotype class. No individual is
> described. **Nothing here is medical advice.**

---

## 0 · Scope, surfaces and denominators

Every negative in this file carries the population it was measured over, so that a later reader can
re-measure it without guessing what *"everything"* meant.

| Surface | Denominator | Note |
|---|---|---|
| `disease-models/wwox/**/*.md` | **133 files** | claims, registries, metas, ledgers, dossiers, trackers, analysis |
| `disease-models/wwox/research/deepdive_manifests/*.json` | **64 manifests** | verbatim locators, image-read locators included |
| `files/fulltext/` | **10 files** at top level | the machine-readable primaries held locally |
| **Total scanned population for the Phase-5 sweep** | **207 files** | the three rows above, unioned |
| Live connectors (PubMed, Scholar Gateway, bioRxiv, Clinical Trials, AdisInsight) | ⚠️ **unauthorized in this session** | **no external search was run.** Every *"nothing exists"* below means *nothing exists on the 207 files named above* |

**Primary artefacts re-opened for this pass** — not taken on the authority of the two earlier files:

| Artefact | Digest verified | What was re-derived here |
|---|---|---|
| `files/fulltext/PMID32000863_Cheng2020_PMC.xml` | — | caption and Results text for Fig. 7b / 7c / 7d, Methods dosing, Discussion |
| `files/fulltext/PMID32000863_Cheng2020_assets/40478_2020_883_Fig7_HTML.png` | `ced68a66…62542` ✅ matches the manifest's `source_artifacts` entry; 1946 × 1627 as declared | panels **b**, **c** and **d** re-read at 2–3× from the anchored raster |
| `deepdive_manifests/PMID32000863.json` | receipt `FTR-20260804-32000863-01` | the image locators, compared against my own independent read |
| `deepdive_manifests/PMID42422765.json` | receipt `FTR-20260814-42422765-06`, **`complete_fulltext_read`** | all **29** locators enumerated |
| `deepdive_manifests/PMID34747138.json` | receipt `FTR-20260810-34747138-01`, **`complete_fulltext_read`** | all **20** locators enumerated |
| `registries/fulltext_read_receipts.jsonl` | `OK: 128 chained receipts, tail anchored` | read-depth history of the four load-bearing PMIDs |

---

## 1 · PHASE 2 — Six separable canonical repair candidates

Each candidate is written to be **acceptable or rejectable on its own**. None depends on another
being accepted. `CHANGE_CLASS` follows `LEGEND_CORE` §157 — **MAJOR** = baseline-claim reversal or
block redefinition; **MINOR** = everything else. Where the class is genuinely arguable it is marked
`MAJOR?` and routed to Mirror, fail-closed, per Annex H.1.

---

### CANDIDATE A — mTOR: from *"wrong direction"* to `INSUFFICIENT / not directly measured`

| Field | Content |
|---|---|
| **CURRENT_CANONICAL_STATEMENT** | The canonical layer carries **no** claim that mTOR points the wrong way. The statement lives one layer down, in the map's `N-01 — mTOR inhibitors (rapamycin / everolimus) → **wrong biological direction**`, ranked **#2** in `TOP_NEGATIVE_FINDINGS`, and it draws its only datum from a single summary line in `DL-MECH-034` (*"Altri assi alterati (DATO)"*: mTOR ↓, `EIF4EBP1` ↓, autophagy ↓), which sits under [[claim_registry_current#CLAIM 002]]'s source, Steinberg 2021 |
| **PROPOSED_MINIMUM_DELTA** | Replace the phrase *"wrong biological direction"* with **`INSUFFICIENT — the axis has never been measured at protein level in any WWOX system`**, and demote `N-01` out of `TOP_NEGATIVE_FINDINGS`. Tag the `DL-MECH-034` line **`PREMISE: UNLOCATORED`**. **Do not** move mTOR inhibitors into any consideration class |
| **DIRECT_EVIDENCE** | Bulk RNA-seq of hESC-derived WWOX-KO cerebral organoids, week 15, **n = 2 WT vs n = 4 KO** (started 4 + 4; one WT failed QC, one excluded for not clustering). Fold-change filter + **raw `P < 0.01`**, **not FDR-controlled**. No protein, no p-S6, no p-4E-BP1, no LC3-II/p62, no flux, no rapamycin arm |
| **LOCATOR** | 🔴 **There is none, and that is the finding.** `deepdive_manifests/PMID34268881.json` carries **12** verbatim locators and **not one** touches mTOR, `EIF4EBP1` or autophagy. `fulltext_dossiers/PMID34268881.md` never names them. `commit_candidates/CC-20260814-34268881-01.md` never names them. The single occurrence in the repository is a prose summary line in `DL-MECH-034` |
| **EVIDENCE_LEVEL** | **T6** for the intervention (no WWOX system has ever received an mTOR inhibitor) · **transcript-only, unlocatored, un-FDR'd** for the direction. Under the map's own ladder rule — *"tier is assigned to the conjunction"* — the conjunction does not exist |
| **WHY_CHANGE_REQUIRED** | Three independent reasons, any one sufficient. **(1)** This repository's export rule refuses a conclusion without its quote; a datum that could not be exported is currently carrying the second-ranked negative. **(2)** `EIF4EBP1` ↓ read as biology **inverts** the reading: 4E-BP1 is the *inhibitor* of eIF4E and the *substrate* of mTORC1, so less 4E-BP1 is the functional output mTORC1 **activation** produces. **(3)** mTORC1 is the canonical *suppressor* of autophagy, so *"mTOR ↓ and autophagy ↓"* from one gene list is discordant under the very coupling needed to read either — unless the autophagy call is mTORC1-independent, which concedes that the mTOR label is not producing the direction. Add the registry correction: **two** of the 426 records name mTOR, not one, and three name WWOX↔autophagy in **two opposite directions** (reading debt now declared at [[full_text_queue_current#FT-073]]) |
| **THERAPEUTIC_EFFECT** | **None on the operational position.** mTOR inhibitors stay out at every tier. What changes is what a reader carries forward: *"nobody has measured it"* instead of *"it points the wrong way"*. The first invites `E-1` below; the second forecloses it. A negative cited as a **demonstration** suppresses the cheapest experiment in the portfolio |
| **CHANGE_CLASS** | **MINOR** — no canonical claim is reversed; a sub-canonical negative is reclassified and a ledger line is premise-tagged. ⚠️ If Plan judges that demoting `TOP_NEGATIVE_FINDINGS` #2 constitutes a block redefinition, this is `MAJOR?` → Mirror |

---

### CANDIDATE B — Lithium: `DEPRIORITIZE`, with general anticonvulsant effect separated from WWOX-specific rescue

| Field | Content |
|---|---|
| **CURRENT_CANONICAL_STATEMENT** | [[claim_registry_current#CLAIM 016]] Summary: *"In Wwox-null mice, GSK3β is elevated in cortex, hippocampus and cerebellum, and lithium significantly suppresses PTZ-induced seizure susceptibility."* Its 2026-08-10 evidence boundary already records the all-three-genotypes fact. **Two downstream records do not carry that boundary:** `therapeutic_strategies_current.md#TX-005` — *"lithium abolishes PTZ-induced seizures in Wwox-/-"*, scored `EVID 2` — and [`therapy_levers.md`](therapy_levers.md) **A2**: *"Lithium (GSK3β inhibition) — **the strongest repurposing signal**… GSK3β is elevated in cortex, hippocampus and cerebellum; lithium inhibits GSK3β and abolishes seizures"* |
| **PROPOSED_MINIMUM_DELTA** | **(i)** Propagate `CLAIM 016`'s existing boundary into `TX-005` and `therapy_levers.md` **A2**, and retire the phrase *"the strongest repurposing signal"*. **(ii)** Add one sentence to all three: **the effect is a general anticonvulsant effect, not a WWOX-specific rescue, and it is a negative result in an assay of demonstrated sensitivity.** **(iii)** Score `TX-005` on the failed specificity test, not on the mechanistic rationale. **(iv)** Leave the anticonvulsant fact itself untouched — it is real |
| **DIRECT_EVIDENCE** | Figure 7**d**: three stacked genotype panels (`+/+`, `+/−`, `−/−`), **each carrying its own `****` bracket for PTZ vs PTZ+LiCl**, N = 12 vs 8, 12 vs 12, 6 vs 7. The comparator settles it: Figure 7**b** (ethosuximide) is marked **`n.s.` in `+/+` and `+/−`** and significant in `−/−`, and the text declares it: *"ethosuximide pretreatment had no effects on the behavior changes in Wwox+/+ and Wwox+/− mice"*. For lithium the paper **declares no converse**. Six of seven disaggregated components are empty: no GSK3β readout under lithium, no Tau phosphorylation, no target engagement, no survival (`Kaplan` 0 hits, `lifespan` 0 hits in the XML), no behaviour, no myelin, no gliosis, no ECoG. The authors state the developmental question themselves: *"Whether lithium treatment can rescue the deficits in neuronal migration and differentiation during development in Wwox−/− mice **remains to be studied**"* |
| **LOCATOR** | Caption, verbatim: *"**d** Pretreatment of a GSK3β inhibitor LiCl (60 mg/kg) suppressed PTZ-induced seizure activity in Wwox−/− mice."* · Results, verbatim: *"Injection of a potent GSK3β inhibitor lithium chloride significantly suppressed PTZ-induced epileptic seizure in Wwox−/− mice **(Fig. 7 d)**."* · Methods: *"LiCl (i.p., 60 mg/kg) were pretreated three times within 1 h before PTZ injection."* All three re-read this pass from `PMID32000863_Cheng2020_PMC.xml`. Panel letters and significance markers re-read independently from the anchored raster `40478_2020_883_Fig7_HTML.png` (`ced68a66…`) at 2× |
| **EVIDENCE_LEVEL** | **T5 compound / T2 mechanistic rationale / T1-negative on specificity.** Scored on the failure, not on the rationale |
| **WHY_CHANGE_REQUIRED** | A drug effect is WWOX-specific only if the **genotype × treatment interaction** is non-null. Fig. 7d shows a main effect in all three genotypes and **no tested interaction** — and per-genotype significance stars are not an interaction term. The assay **can** detect genotype specificity: it did, for the other drug, in the same figure, the same cohort, the same day. That converts *"we don't know"* into *"we looked and it wasn't there"*, and it is the sentence the two downstream records are missing while calling lithium the strongest signal |
| **THERAPEUTIC_EFFECT** | **Verdict unchanged — `DEPRIORITIZE` — reasons strengthened, scope narrowed.** Lithium remains a real anticonvulsant with real paediatric use. It must stop being scored as a *WWOX-mechanism* drug. Downstream: `TX-005`'s `EVID` and `MATCH` components rest on a specificity the experiment did not measure |
| **CHANGE_CLASS** | **MINOR** — `CLAIM 016` already carries the boundary; this propagates an existing canonical boundary to two records that never received it, and adds a consequence sentence. No reversal |
| ⚠️ **Boundary against over-correction** | The primary's own abstract says lithium *"significantly **abolishes** the onset of PTZ-induced seizure in Wwox−/− mice"*. The verb *"abolishes"* in `therapy_levers.md` is therefore **the source's own word and is not a defect**. The defects are the missing genotype boundary and the abundance clause — not the verb. Recorded so the repair does not overreach |

---

### CANDIDATE C — NMDAR: upgrade the evidence level **only in the conjunction actually demonstrated**

| Field | Content |
|---|---|
| **CURRENT_CANONICAL_STATEMENT** | [[claim_registry_current#CLAIM 021]] (`consolidated baseline`), Summary, final clause: *"**Bursting depends on NMDAR and gap junction activity.**"* One sentence, two nodes, one verb, no pharmacology, no direction, no magnitude |
| **PROPOSED_MINIMUM_DELTA** | Split the clause. **NMDAR half:** *"NMDAR blockade (d-APV) **abolishes** the pathological burst in the `Wwox` S-KO neocortical slice at P13–P17 — a pharmacological dependence established **inside** the WWOX-deficient system, with a **~1.85× overshoot on washout**."* **Gap-junction half:** see Candidate D. Upgrade the map's `CHAIN B` **T2 → T1 for the tool compound**, and **only** for the tool compound. Record explicitly that **memantine has never been given to a WWOX system**: the gap is one *compound* wide, not one *experiment* wide |
| **DIRECT_EVIDENCE** | d-APV takes normalized burst frequency from 1.0 to **zero** (Figure 3D-d1, image-read at 6× from native pixels). On washout frequency returns to **~1.85×** baseline — recorded, unexplained |
| **LOCATOR** | `deepdive_manifests/PMID34634460.json`, receipt **`FTR-20260810-34634460-02`**, `complete_fulltext_read`, **21** verbatim locators, several image-anchored. Receipt depth re-verified this pass against `fulltext_read_receipts.jsonl` |
| **EVIDENCE_LEVEL** | **T1 for d-APV** on the bursting endpoint, acute ex-vivo. **T5 for memantine** (target engagement only, no WWOX system). **T3** transferred (GRIN2A in the burst-suppression cohort, `DL-MECH-002`; memantine's approved use) |
| **WHY_CHANGE_REQUIRED** | The map lists as its *"highest-value, lowest-cost open item"* (`E-1`) a re-read of PMID 34634460 to determine whether the dependence was established pharmacologically. **The re-read had already been performed and it was.** The map was written without consulting a complete-read receipt that was ten days old. The claim's one-verb sentence is what let that happen: *"depends on"* is compatible with correlation, and the actual result is an abolition |
| **THERAPEUTIC_EFFECT** | The strongest circuit-level conjunction in the portfolio, and it costs nothing to record — the experiment is already done and in the repository. But it does **not** promote memantine, and the upgrade must not be read as promoting it. **`PROMISING_BUT_MECHANISTIC_GAP` is retained for R-02** |
| **CHANGE_CLASS** | **MAJOR?** → Mirror, fail-closed. `CLAIM 021` is `consolidated baseline`; splitting its final clause **strengthens** one half and **withdraws** the other (Candidate D). A withdrawal inside a baseline claim is a reversal on that axis even though the claim as a whole survives |
| ⚠️ **Interpretation risks, both recorded rather than resolved** | **(i)** Recordings are **P13–P17** in animals dying at 3–4 weeks, and the authors write that *"the chosen age group may mimic a **late-stage** disorder of WWOX"*. **(ii)** Chronic NMDAR blockade in a developing brain removes a signal required for activity-dependent maturation — the process WWOX loss already impairs. **(iii)** 🆕 **A tension worth stating and not overstating:** the *in vivo* hyperexcitability recordings in the sister paper are made **under ketamine, an NMDA antagonist** (`deepdive_manifests/PMID34747138.json`, entry 13 — *"the between-group contrast stands; the absolute firing rates are not those of an awake brain"*). A WWOX hyperexcitability phenotype that persists under an NMDAR blocker *in vivo*, while an NMDAR blocker abolishes bursting *ex vivo*, is not a contradiction — different drugs, doses, preparations and endpoints — but it is the kind of coincidence that should be resolved by design rather than by assumption. `PREMISE: INFERENZA` |

---

### CANDIDATE D — Gap junction / carbenoxolone: downgrade for non-specificity and the washout failure

| Field | Content |
|---|---|
| **CURRENT_CANONICAL_STATEMENT** | The gap-junction half of [[claim_registry_current#CLAIM 021]]'s *"Bursting depends on NMDAR and **gap junction** activity."* The map carries the same node as an independent target in `CHAIN B` |
| **PROPOSED_MINIMUM_DELTA** | Replace with: *"The carbenoxolone effect on bursting is **real but not attributable to gap junctions** in this dataset."* Remove the gap-junction node from the list of independent actionable targets, pending occlusion. Do **not** state that gap junctions are uninvolved — that is not what was measured |
| **DIRECT_EVIDENCE** | Carbenoxolone 100 µM reduces burst frequency by **87%** in the S-KO slice. Against attribution, from the primary itself: **(i)** the effect **does not wash out** — *"This did not return to normal levels after washout"*; CBX frequency ~0.25 at washout against a 1.0 baseline, duration still carrying a significance marker at washout; **(ii)** the Discussion lists two off-target actions for CBX at that concentration: **NMDA receptor block** and **pannexin block** |
| **LOCATOR** | `deepdive_manifests/PMID34634460.json`, receipt `FTR-20260810-34634460-02`, `complete_fulltext_read` |
| **EVIDENCE_LEVEL** | **T1 for the compound · no tier for the target.** Given that d-APV alone drives frequency to zero, the entire CBX result is explicable as Candidate C again |
| **WHY_CHANGE_REQUIRED** | Two independent grounds and they compound. A blocker whose effect **persists through washout** is not cleanly pharmacological at that concentration — the observation is compatible with toxicity or with an irreversible action, and neither supports target attribution. And the paper's own Discussion names NMDAR block among CBX's actions, in a preparation where NMDAR block alone abolishes the phenotype. **The node is not established as separable.** There is no CNS-appropriate selective connexin blocker, so an unseparated node also has no candidate attached to it |
| **THERAPEUTIC_EFFECT** | One target leaves the portfolio as an independent object. Nothing is lost clinically — nothing was ever prescribable here — but the portfolio stops counting two circuit nodes where the data support one |
| **CHANGE_CLASS** | **MAJOR?** → Mirror, fail-closed, jointly with Candidate C. This is the withdrawal half of the `CLAIM 021` split |

---

### CANDIDATE E — Pannexin blockade: new negative **N-16**, direction adverse

| Field | Content |
|---|---|
| **CURRENT_CANONICAL_STATEMENT** | **None.** No canonical claim, no tracker entry and no map entry mentions pannexin blockade. The source's own prose describes the result as *"**minimal effect** on the network excitability in the `Wwox` S-KO model"* — in both Results and Discussion |
| **PROPOSED_MINIMUM_DELTA** | Add **`N-16 — Pannexin blockade → DEPRIORITIZE`** to the map's negative list, and add the unpropagated pharmacology to `CLAIM 021` alongside Candidates C and D. State the direction: **BB-FCF raised normalized burst frequency to ~2.55 during treatment and ~2.6 at washout, against a baseline of 1.0, with no significance test reported** |
| **DIRECT_EVIDENCE** | The point estimate and its direction, image-read; and the absence of any reported test |
| **LOCATOR** | `deepdive_manifests/PMID34634460.json`, receipt `FTR-20260810-34634460-02` |
| **EVIDENCE_LEVEL** | **T1-negative in direction, untested in significance.** The honest tier is *"one measurement, adverse point estimate, wide error, no test"* |
| **WHY_CHANGE_REQUIRED** | 🔴 **A 2.5-fold point estimate with wide error and no test is not an absence of effect, and its direction is the opposite of the one the sentence implies.** A reader of the prose alone would not know there was a direction to worry about. This is the same failure class the repository already catalogues — text accurate, panel decisive — applied to a *therapeutic* node rather than a mechanistic one |
| **THERAPEUTIC_EFFECT** | A node that had never been scored is scored, and it is scored **negative**. This is the only candidate in this file that *adds* a record rather than repairing one — and it adds a negative, not a molecule |
| **CHANGE_CLASS** | **MINOR** — addition of a negative; no baseline claim reversed |
| ⚠️ **Boundary** | `DEPRIORITIZE` here means *"the only WWOX measurement points the wrong way and was not tested"*, **not** *"pannexins are not involved"*. The `REVIVAL_TRIGGER` is a powered, significance-tested pannexin arm reporting a **reduction**, and — per the authors' own suggestion — at an **earlier developmental stage** than P13–P17 |

---

### CANDIDATE F — AAV9-hSynI-WWOX: split by endpoint

| Field | Content |
|---|---|
| **CURRENT_CANONICAL_STATEMENT** | Three canonical objects carry it. [[claim_registry_current#CLAIM 004]] (`consolidated baseline`): *"Preclinical AAV9-WWOX rescue improves survival, hyperexcitability and myelin-related phenotype"*, with a **2026-08-10 qualification already applied** — *"dove il rescue è confrontato con il WT il confronto o non è tracciato, o è significativo contro il rescue"*. [[claim_registry_current#CLAIM 011]] (**`flagged for review`**): *"rescue dose-dependent e durevole su: sopravvivenza, crescita, glucosio, comportamento, mielinizzazione, gliosi, ipereccitabilità / SWD"*. And the map's `R-01`, the **sole** entry in `READY_FOR_WWOX_PRECLINICAL_CONSIDERATION` |
| **PROPOSED_MINIMUM_DELTA** | Move the class from the **intervention** to the **(intervention × endpoint × window) triple** — the map's own ladder rule applied for the first time to its own top entry. **Retain** `READY_FOR_WWOX_PRECLINICAL_CONSIDERATION` for **survival · SWD · motor · gliosis**, at HD, in the P0–P5 window. **Downgrade to `PROMISING_BUT_GAP`** for **cognition · developmental trajectory · myelin-in-the-dose-study · cerebellum · post-neonatal administration**. Full endpoint table in §3 |
| **DIRECT_EVIDENCE** | See §3. Briefly: WT-vs-HD is **`ns`** for SWD (7E), gliosis (S8I) and motor (S4A) — i.e. rescued to wild-type level and *tested against it*. Cognition and development have **no assay at all** in either paper (29 + 20 locators enumerated, zero cognitive endpoints). Cerebellum sits at **1.4×** WT while cortex is 8.2× and hippocampus 10.7×, and Figure 5L puts it **below** WT at P30 — in a model whose cerebellum carries locatored foliation defects and Purkinje loss |
| **LOCATOR** | `deepdive_manifests/PMID42422765.json` (receipt `FTR-20260814-42422765-06`, **`complete_fulltext_read`**, 29 locators) and `deepdive_manifests/PMID34747138.json` (receipt `FTR-20260810-34747138-01`, **`complete_fulltext_read`**, 20 locators). Both receipt depths re-verified this pass against the ledger |
| **EVIDENCE_LEVEL** | **T1** for survival / SWD / motor / gliosis. **No tier** for cognition and development — a tier requires a measurement. **T1-partial** for myelin (2021 paper, quantified, incomplete). **Untested** for post-neonatal dosing |
| **WHY_CHANGE_REQUIRED** | 🔴 **`CLAIM 011`'s own rewrite was deferred on a condition that has since been discharged, and the claim still states the condition as open.** Its 2026-08-10 flag says the rewrite is postponed because *"la lettura che li risolverebbe è `partial_fulltext_read`"*. `FTR-20260814-42422765-06` is a **`complete_fulltext_read` of that paper, dated 2026-08-14** — twelve days before this file. The blocker is stale, the reading exists, and the claim is the last place that does not know it. Second reason: `R-01`'s class asserted a readiness the developmental column does not support, and it was the **only** entry in that class, so the class name was doing the portfolio's ranking work by itself |
| **THERAPEUTIC_EFFECT** | **`R-01` still ranks first, and nothing else is close.** What it no longer does is rank first **on disease modification** — because nothing in the portfolio has been measured there (§4). This is a downgrade in *scope*, not in *rank*, and the distinction is the whole point: the previous class name was a claim about endpoints that had never been measured |
| **CHANGE_CLASS** | **MAJOR** — `CLAIM 004` is `consolidated baseline` and `CLAIM 011` carries `clinical relevance: HIGH` in `P7 — gene therapy readiness`. Narrowing a readiness class in the gene-therapy pathway is a block-adjacent change. Fail-closed to MAJOR; Orchestrator authorization required |

> ### `THERAPEUTIC_REPAIR_CANDIDATE_COUNT: 6`
> **A** mTOR `INSUFFICIENT` (MINOR) · **B** lithium boundary propagation (MINOR) · **C** NMDAR conjunction upgrade (MAJOR?) · **D** gap-junction downgrade (MAJOR?) · **E** N-16 pannexin negative (MINOR) · **F** AAV9 endpoint split (MAJOR).
> **Three MINOR · one MAJOR · two MAJOR? routed to Mirror.** No new molecule. Two of the six *weaken a negative*; neither promotes the drug class it weakens.

---

## 2 · PHASE 3 — `CLAIM 016` × `CLAIM 035`: the S9 axis adjudicated

### 2.1 The six measures, separated

The two claims are usually read as corroborating each other. They are measuring different things,
and one of the things is not measured at all.

| Measure | What the sources actually contain | State |
|---|---|---|
| **`TOTAL_GSK3B`** | Cheng Fig. 7c densitometry, **re-read this pass at 3× from the anchored raster**: cerebellum **2.2 / 2.4 / 2.4**, hippocampus **2.3 / 2.4 / 2.6**, cortex **2.2 / 2.4 / 2.6** across `+/+`, `+/−`, `−/−`. Wang (`CLAIM 035`): abundance **unchanged** | **Measured, untested** |
| **`P-SER9_GSK3B`** | Cheng Fig. 7c: cerebellum **2.7 / 3.1 / 1.3**, hippocampus **3.6 / 3.5 / 2.0**, cortex **3.9 / 3.8 / 2.5** — a **−52% / −44% / −36%** fall in the null. Wang: pSer9 **unchanged** while kinase output changes | **Measured, untested** |
| **`ACTIVITY_INFERENCE`** | Cheng infers activation **from the phospho-site**, and says so: *"increased **activation** … as evidenced by **dephosphorylation** of GSK3β at Ser9"*. Wang measures output directly (Tau pS396/S404, microtubule assembly, neurite outgrowth) | **Cheng: inferred · Wang: measured** |
| **`ABUNDANCE`** | 🔴 **Neither source claims abundance is elevated.** Cheng's abstract says *"significantly increased **activation**"*. Wang reports abundance unchanged | **Claimed nowhere in either source** |
| **`IN_VIVO_DE_REPRESSION`** | The only *in vivo* evidence that GSK3β is de-repressed in WWOX loss **is a phospho-S9 western** — Cheng Fig. 7c. Wang's system is SH-SY5Y + recombinants + endogenous co-IP from mouse brain; it establishes the mechanism, not its *in vivo* operation in a WWOX-deficient brain | **One western, one site, one timepoint (P20)** |
| **`ASSAY_BLINDNESS`** | `CLAIM 035` states it as a warning: de-repression from loss of the WWOX brake would be **invisible to an anti-phospho-S9 western**, and any WWOX study using pS9 as an activity readout *"produrrà un falso negativo"* | **Canonically stated** |

### 2.2 The adjudication

> ## `CLAIM016_035_STATUS: MULTIPLE_AT_ONCE`
> **Three defects, of three different kinds, in one axis. They are separable and must be repaired separately.**

**(1) `MISLOCATOR` — confirmed, verbatim, this pass.**
`CLAIM 016`'s evidence boundary cites **Fig. 7b** for the lithium panel. The primary's caption reads
*"**d** Pretreatment of a GSK3β inhibitor LiCl…"*; the Results read *"(Fig. 7 **d**)"*; and **7b is
ethosuximide**. Independently confirmed by opening the anchored raster: 7b's panels carry `n.s.` in
`+/+` and `+/−`, 7d's carry `****` in all three. The deepdive manifest has it right; the claim and
the map inherited the error from each other. **Consequence for the conclusion: none. Consequence for
reproducibility: total** — a reader sent to 7b to check the strongest negative in the lithium file
lands on a different drug with the opposite genotype pattern, and would conclude the boundary is wrong.

**(2) `OVERCLAIM`, and it is narrower than I previously stated — a correction against myself.**
`CLAIM 016`'s Summary says *"GSK3β is **elevated**"* and its boundary preserves *"il dato di
abbondanza"*. The second-pass file concluded from this that *"neither source reports elevated GSK3β
abundance"* and that total GSK3β is *"flat"*. Re-reading the panel at 3×, **"flat" understates what
is there.** Total GSK3β moves `+/+` → `−/−` by **+9% (cerebellum), +13% (hippocampus), +18%
(cortex)** — small, but **monotonic and in the same direction in all three regions**. What is
missing is not the trend; it is any test of it: the 7c densitometry carries **no error bars, no
significance markers and no n on the panel face**, under a caption declaring *"representative
results of four independent experiments"*. So the accurate statement is neither *"elevated"* nor
*"flat"* but: **an untested ~9–18% monotonic trend, typed in the claim as `DATO (abbondanza)`, whose
own source declines to interpret it and reports activation instead.** The same absence of a test
applies to the pSer9 fall — which is the larger effect, and is equally untested on the panel face.

**(3) `TRUE_CONTRADICTION` on the `IN_VIVO_DE_REPRESSION` axis — the two claims exclude each other.**
`CLAIM 035` says the WWOX brake on GSK3β is **S9-independent** and warns that a pS9 western would
return a **false negative**. `CLAIM 016`'s only *in vivo* de-repression evidence **is** a pS9
western — and it moved. Both cannot describe the same brake:

- **(a)** the *in vivo* pS9 fall is driven by something **other** than loss of the WWOX docking-site
  brake ⇒ Cheng's western is **not** evidence that the `CLAIM 035` mechanism operates *in vivo*, and
  the map's `CHAIN C` has **no in-vivo anchor**; or
- **(b)** it **is** WWOX-dependent ⇒ `CLAIM 035`'s S9-independence needs a boundary it does not have.

The map fuses both claims into one chain (M4) and takes an anchor from each. **On this axis they
exclude each other.**

**And there is a concrete competing explanation for (a), already canonical in this repository.**
Ser9 is the **AKT** site; AKT tone follows insulin and glucose. A systemic constitutive `Wwox`-null
in the P14–P20 window is hypoglycaemic, acidotic and uraemic ([[claim_registry_current#CLAIM 036]]:
glucose **143.5 vs 250.6 mg/dL**, `p = 0.000131`). **Cheng's westerns are taken at P20, in a systemic
constitutive null.** Hypoglycaemia → less insulin → less AKT → **less pSer9** → reads as GSK3β
"activation". `PREMISE: INFERENZA`, and the transfer is stated: `CLAIM 036` is measured in a
**different** null strain (EIIA-Cre, Ludes-Meyers) than Cheng's, so what transfers is the
**confounder class**, not the numbers. It does not refute the finding. **It means the design cannot
separate a WWOX-dependent brake from a systemic metabolic one** — the identical criticism `CLAIM 036`
already applies to the PV/glia markers, applied here for the first time to the GSK3β datum that
carries the entire M4 chain.

### 2.3 Candidate repair — prepared, **not applied**

| # | Target | Minimum delta | Class |
|---|---|---|---|
| **R3-1** | `CLAIM 016` evidence boundary | `Fig. 7b` → **`Fig. 7d`**; note that 7b is the ethosuximide comparator and is what makes the genotype argument work | **MINOR** — a locator correction; conclusion unaffected |
| **R3-2** | `CLAIM 016` Summary + boundary | *"GSK3β is elevated"* → *"total GSK3β shows an **untested** monotonic +9–18% trend across three regions; the source's stated evidence is **Ser9 dephosphorylation**, i.e. **activation**, not abundance"*. Retype `DATO (abbondanza, murino)` accordingly. Remove *"Cosa NON cambia: il dato di abbondanza"* — it preserves a datum neither source asserts | **MINOR?** → Mirror. It edits the `Type` line of an `in observation` claim, which is a re-typing rather than a reversal, but the `Type` line is what downstream scoring reads |
| **R3-3** | `CLAIM 016` **and** `CLAIM 035` | Add a **reciprocal** boundary naming the mutual exclusion and stating both horns (a) and (b). Neither claim may cite the other as corroboration **on the S9 axis** until one horn is closed | **MAJOR?** → Mirror. `CLAIM 035` is the residue-mapped mechanism claim and this bounds its *in vivo* reach |
| **R3-4** | `CLAIM 016` | Add the `CLAIM 036` hypoglycaemia alternative as a stated, transferred, `INFERENZA`-tagged confounder — **explicitly not a refutation** | **MINOR** — adds a boundary |
| **R3-5** | Map `CHAIN C` / `R-04` | Delete *"GSK3β abundance elevated … (2 sources)"* from `WWOX_DIRECT_EVIDENCE`; the `PREMISE_TAG` *"abundance reports activity"* is a premise about a datum that does not exist. Replace with the phospho-site critique, which is a different critique | **MINOR** — sub-canonical |

> **`REVIVAL_TRIGGER` for the M4 mechanism** — a distinct object from the drug:
> *reopen the in-vivo anchor if a **phospho-S9-independent** GSK3β activity assay in WWOX-deficient
> neural tissue reports de-repression — or if the pSer9 fall is reproduced in a **normoglycaemic or
> conditional** WWOX-null, separating it from the systemic metabolic collapse of `CLAIM 036`.*

---

## 3 · PHASE 4 — AAV9-hSynI-WWOX endpoint-level audit

**Purpose:** to make *"gene therapy rescues the phenotype"* unsayable as a global proposition.

**Sources and their denominators.** PMID 42422765 (dose study, `FTR-20260814-42422765-06`,
`complete_fulltext_read`, **29 locators**) and PMID 34747138 (2021 proof-of-concept,
`FTR-20260810-34747138-01`, `complete_fulltext_read`, **20 locators**). All 49 locators were
enumerated for this audit, not sampled.

**State vocabulary, and the distinction that carries the audit.** `MEASURED` vs `NOT_MEASURED` is a
question about whether an assay was run. `QUANTIFIED` vs `QUALITATIVE_ONLY` is a question about
whether it produced a number. `RESCUED` / `PARTIAL` / `NOT_RESCUED` / `UNRESOLVED` is a question
about **which comparison was drawn** — and it resolves to `RESCUED` only where the **treated-vs-wild-type**
bracket exists and is `ns`. A `KO-vs-treated` bracket alone shows that treatment did something; it
cannot show that treatment was sufficient.

| # | Endpoint | Measured? | Quantified? | Outcome | The bracket that decides it |
|---|---|---|---|---|---|
| **1** | **SURVIVAL** | `MEASURED` | `QUANTIFIED` | **`RESCUED`** at HD · **`NOT_RESCUED`** at LD and below | HD plateaus **~75–80% to day 300**; LD moves death from ~20 d to ~90 d then reaches **zero**; 4 × 10¹⁰ and 8 × 10¹⁰ rescue nothing. 🔴 **A threshold with no measured expression correlate** — vector genomes and mRNA are `ns` between LD and HD in **7 of 8** region comparisons (exception: hippocampal DNA), and the paper's own explanation is a **post-hoc survivor-vs-non-survivor** comparison (S5A–D label one HD and three LD animals *"Dead"*) |
| **2** | **SWD / electrographic** | `MEASURED` | `QUANTIFIED` | **`RESCUED`** on SWD · **`UNRESOLVED`** on spike count | Fig. 7E: **`****` WT-vs-KO, `****` KO-vs-HD, `ns` WT-vs-HD** — the decisive bracket exists and is null. 🔴 The **second** epilepsy endpoint in the same figure, average spikes/day (7C), prints **`p = 0.2000`** on the panel face for WT-vs-KO, with no asterisk and no `ns`, at n = 5/group — while the running text calls the same comparison *"a significant elevation"* |
| **3** | **MOTOR** | `MEASURED` | `QUANTIFIED` | **`RESCUED`** at HD · **`PARTIAL`** at LD | S4A dose-graded: WT ~0, KO ~3.6, LD ~1.8, HD ~0.3; **WT-vs-HD `ns`**, LD-vs-HD `***`. 🔴 Fig. 4D/4E carry asterisks (`*p<0.05`) for **velocity and total distance against WT** while the text states *"no significant differences between groups"*. And **LD animals do not survive to P90**, so all P90 behaviour is HD-only and **survivor-selected** |
| **4** | **GLIOSIS** | `MEASURED` | `QUANTIFIED` | **`RESCUED`** at HD · 🔴 **`NOT_RESCUED` at LD** | S8I supplies the untreated-KO baseline S7 lacks: GFAP⁺ **WT ~5 / KO ~44 / treated-at-P5 ~5**, `***` WT-vs-KO and **`ns` WT-vs-treated**. 🔴 S7H shows **LD significantly worse than WT** (`**`) while HD is `ns` — one more instance of LD failing where HD succeeds |
| **5** | **MYELIN** | **Split by paper — and this is the correction this audit adds** | | | |
| 5a | · in the **dose study** (42422765) | `MEASURED` | 🔴 **`QUALITATIVE_ONLY`** | **`UNRESOLVED`** | Fig. 6F, S7I and S8G are **representative images with no graph, no axis and no statistics**; the only MBP quantification (6E) has **no treated arm**. Yet the text claims *"near-complete rescue across affected regions"* and cites S7I as if it carried the quantification |
| 5b | · in the **2021 paper** (34747138) | `MEASURED` | **`QUANTIFIED`** | **`PARTIAL`** — and on the one metric where the deciding bracket is drawn, 🔴 **`NOT_RESCUED`** | CC1⁺ mature oligodendrocytes **WT ~170 / KO+GFP ~77 / rescued ~135**; PDGFRα⁺ **WT ~53 / KO+GFP ~87 / rescued ~70**; myelinated axons/FOV corpus callosum **~130/46/105**, optic nerve **~140/68/124**. In every one of these the brackets run **WT-vs-KO and KO-vs-rescued, never WT-vs-rescued** — so the visible residual gap is **untested**. The single panel where WT-vs-rescued **is** drawn is unmyelinated axons per FOV: **WT ~26 vs treated ~52, marked `**` — significant against the rescue.** The g-ratio scatter does normalise. n = 3 biological replicates per genotype |
| **6** | **CEREBELLUM** | 🔴 `NOT_MEASURED` **as an endpoint** — measured only as a *distribution* compartment | `QUANTIFIED` (distribution) | **`NOT_RESCUED`** on transduction; **`UNRESOLVED`** on function | At P30 Fig. 5L puts cerebellum **below** wild type. At P300, S6D prints cerebellum **0** against cortex 4.6, hippocampus 4.7, midbrain 3.1; S5J prints cortex **8.2×**, hippocampus **10.7×**, midbrain **5.6×**, cerebellum **1.4×** WT. **In the same species and the same model**, the `Wwox`-null mouse carries a documented cerebellar lesion: *"Midline sagittal cresyl violet-stained section revealed foliation defects in lobules V, VI and VII of `Wwox`−/− cerebellum"*, with Purkinje counts image-read at **~18 vs ~7 per area** (`deepdive_manifests/PMID32000863.json`, entry 12, receipt `FTR-20260804-32000863-01`). ⇒ **the vector systematically under-transduces a region with a documented lesion in the very model it is tested in, and no cerebellum-specific endpoint is reported in either paper** |
| **7** | **COGNITION** | 🔴 **`NOT_MEASURED`** | — | **`UNRESOLVED`** | **49 locators enumerated across both manifests. Zero cognitive assays.** No maze, no novel-object, no fear conditioning, no operant task, no learning measure of any kind. The behavioural battery is locomotor, open-field and motor |
| **8** | **DEVELOPMENT** | 🔴 **`NOT_MEASURED`** | — | **`UNRESOLVED`** | No developmental-trajectory endpoint, no milestone acquisition, no staged assessment. Weight and glucose at P14 are `ns` against WT — these are **growth and metabolic** endpoints, not developmental-trajectory ones, and must not be counted as such |
| **9** | **POST_NEONATAL_EFFICACY** | 🔴 **`NOT_MEASURED`** | — | **`UNRESOLVED`** | Dosing is P0–P5 throughout. The 2021 paper states the reason and the untested alternative in its Discussion; the dose study declares post-natal dosing **explicitly as future work**. Within the window: all of P1–P5 give survival, **but** the 300-day panel shows only **P1 and P5** — P2/P3/P4 exist solely in the 40-day panel, and **P3 is an n = 3 arm that lost animals** (~67% at ~24 d) |

### 3.1 What the audit establishes

> ### `AAV9_ENDPOINT_AUDIT: 4 RESCUED · 1 PARTIAL · 4 UNRESOLVED — of which 3 NEVER MEASURED`

**The proposition *"gene therapy rescues the phenotype"* is not available.** Four endpoints are
rescued at high dose and tested against wild type. One is partial and, on its only decisive bracket,
adverse. **Three were never measured at all**, and a fourth is measured as a distribution compartment
where the vector under-performs precisely where the most penetrant phenotype lives.

**The structural finding, which is more general than any single row:** the comparison that would
establish sufficiency — **treated versus wild type** — is drawn for survival, SWD, motor and gliosis,
and is systematically **not drawn** for the myelin quantifications in the 2021 paper. Where it *is*
drawn there, it is **significant against the rescue**. A portfolio that reads `KO-vs-treated`
brackets as rescue will over-read this therapy on exactly the endpoint the authors themselves call
incomplete.

**And a live process finding.** `CLAIM 011` is `flagged for review` with its rewrite deferred because
*"la lettura che li risolverebbe è `partial_fulltext_read`"*. **That reading is now complete**
(`FTR-20260814-42422765-06`, 2026-08-14). The deferral condition has been discharged for twelve days.
This audit is the reading the flag was waiting for.

---

## 4 · PHASE 5 — the disease-modification test

**`SEIZURE_CONTROL ≠ DISEASE_MODIFICATION`**, stated as a question with a denominator rather than as
a principle.

### 4.1 The question, put mechanically

> **Does there exist, on the authorized surfaces, any WWOX intervention for which seizure activity
> improves AND development or cognition independently improves?**

*"Independently"* is doing work: an improvement in a developmental measure that is only inferred from
the seizure improvement does not count. The measure must be its own measure.

### 4.2 The sweep, and its instrument

| Step | Population | Result |
|---|---|---|
| Denominator | **207 files** — 133 disease-model markdown · 64 deepdive manifests · 10 top-level full-text artefacts | fixed **before** measuring |
| Step 1 — cognition / development lexicon anywhere on those files | — | **1 566** term occurrences |
| Step 2 — of those, within ±300 characters of **both** a named intervention **and** an improvement verb | — | **15 occurrences, in 5 files** |
| Step 3 — adjudication of all 15 | — | **15 / 15 are the `N-15` negative or a restatement of it** |

**The 15, named so the count can be checked:** 5 in `mechanism_intervention_map.md` · 4 in
`therapeutic_translation_second_pass.md` · 2 in `claim_registry_current.md`
([[claim_registry_current#CLAIM 031]], the Shaukat cases) · 3 in `paper_registry_current.md` · 1 in
`therapeutic_hypotheses_ledger_current.md`. The claim-registry pair is
[[claim_registry_current#CLAIM 031]] — *"WWOX-DEE is a developmental AND epileptic encephalopathy:
seizure control does not rescue development"*, `T1`, `clinical relevance: HIGH`. Every one of the 15
is the same underlying observation: *"the
developmental outcome was unfavourable with profound impairment **despite improvement of epileptic
activity**"*, and *"the cognitive and psychomotor impairment **preceded the onset** of epileptic
encephalopathy and **did not improve with achievement of better control** of epileptic activity"*.

**🔴 The instrument had to be repaired mid-measurement, and the repair is part of the result.** A
first pass returned 41 triples. Twenty-six of them were a lexicon artefact: the token `IQ`, matched
case-insensitively, fires inside **ub·iq·uitination**, **un·iq·ue** and **ub·iq·uitario** — words that
saturate this corpus's proteostasis literature. Word-boundary anchoring removed all 26 and left 15.
The first number would have supported the same conclusion for the wrong reason, and it is recorded
here because a count nobody can reproduce is not a denominator.

**🔴 Positive controls, because a sweep that finds nothing must be shown capable of finding
something.** The identical machinery, with only the endpoint lexicon changed:

| Control lexicon | Triples found | Verdict |
|---|---|---|
| `surviv` / `lifespan` / `Kaplan` × intervention × improvement | **68**, across 22 files | ✅ the sweep detects a rescued endpoint that exists |
| `rotarod` / `open-field` / `locomot` / `gait` / `ataxi` / motor function × intervention × improvement | **12**, across 4 files | ✅ detects a second one |
| cognition / development × intervention × improvement | **15**, **all negative in content** | ⇒ the null is a property of the corpus, not of the instrument |

### 4.3 The negative, stated with its scope

> ## `DISEASE_MODIFICATION_EVIDENCE_STATUS: ABSENT ON THE EXAMINED CORPUS`
>
> **Across 207 files comprising the entire local WWOX disease model, its 64 deepdive manifests and
> its 10 machine-readable primaries, there is no record of any WWOX intervention — pharmacological,
> dietary, genetic or gene-addition — for which a seizure or electrographic endpoint improved AND a
> developmental or cognitive endpoint independently improved.**
>
> **Every intervention with a filled `SEIZURE_CONTROL` cell has an empty `DEVELOPMENTAL_TRAJECTORY`
> cell and an empty `COGNITION` cell — without exception, and including the gene therapy.** The only
> data anywhere in those two columns are **human, observational, uncontrolled, N = 2, and negative**
> ([[claim_registry_current#CLAIM 031]]).

**What this statement is not.** It is **not** *"disease modification is impossible in WWOX"*. It is
**not** *"gene therapy does not modify the disease"*. It is **not** a statement about the published
literature at large: **no external search was authorized in this session**, and the corpus contains
356 catalogued-but-unread `CORPUS` placeholders whose contents are unknown to this measurement. It is
a statement about **what this repository can currently support**, and the correct reading of it is
that **the column that would rank the portfolio is empty for every candidate in the portfolio.**

**That emptiness is the finding, not a gap in this pass's work** — and it applies with full force to
the one intervention the map placed above all others.

---

## 5 · PHASE 6 — three discriminating experiments

Reduced from four. `E-D4` (genotype × treatment across the repurposing shelf) is **dropped from the
top three and stated as dropped**: it is a *confirmatory* design for a candidate already at
`DEPRIORITIZE`, and it discriminates between *"lithium is a WWOX drug"* and *"lithium is an
anticonvulsant"* — a question Candidate B answers well enough to act on. Its content is retained in
the second-pass file and is not lost.

Each of the three below discriminates between **standing competing hypotheses**. None is a
data-collection exercise.

---

### `E-1` — Occlusion: is the gap-junction node separable from the NMDAR node, and does the actual candidate work?

| Field | |
|---|---|
| **QUESTION** | (a) Does the carbenoxolone effect survive when NMDAR is already blocked? (b) Does **memantine** — the clinical object, not the tool compound — reproduce d-APV's effect? |
| **MODEL** | `Wwox` S-KO neocortical slices at **P13–P17**, the exact preparation where the bursting is characterized · **and** WOREE patient-iPSC forebrain organoids on MEA, with isogenic parental and W-AAV-rescue lines as internal comparators |
| **ARMS** | vehicle · d-APV (full block) · **sub-maximal d-APV** · **memantine, dose–response** · carbenoxolone · **sub-maximal d-APV + CBX co-application** · a selective connexin blocker (or Cx36/Cx43 genetic manipulation) · BB-FCF, **powered and significance-tested**. **Washout reported for every arm** |
| **PRIMARY_ENDPOINT** | Normalized burst frequency, duration and amplitude; phase–amplitude coupling |
| **MECHANISTIC_ENDPOINT** | **The occlusion term** — the sub-maximal-d-APV + CBX co-application arm, against CBX alone |
| **TRUE_RESULT_PATTERN** | *Gap junctions are an independent node:* CBX reduces bursting **further** in the presence of sub-maximal d-APV. Memantine reproduces the d-APV effect dose-dependently. BB-FCF, now tested, reduces bursting |
| **FALSE_RESULT_PATTERN** | *No further reduction under sub-maximal d-APV* ⇒ the gap-junction node **collapses into the NMDAR node** and stops being an independent target. Memantine flat across its range ⇒ the T1 conjunction stays with a tool compound that will never be given to a child, and `R-02` does not move. BB-FCF confirms the ~2.5× **increase** ⇒ `N-16` hardens |
| **HOW_IT_CHANGES_PRIORITIZATION** | Settles **Candidates C, D and E in one preparation.** If gap junctions collapse, the circuit portfolio has **one** node, not two, and `R-02` becomes the only circuit candidate. If memantine works, the portfolio's only *approved, CNS-penetrant, reversible* mechanism-directed compound acquires a WWOX conjunction — the single largest available move in the shelf |
| 🔴 **Interpretation risk** | **d-APV already drives frequency to zero, so there is no headroom for occlusion at full block.** The co-application must run at a sub-maximal concentration taken from the memantine dose–response, or the experiment **cannot fail informatively**. And the **washout overshoot** (~1.85× baseline after d-APV) must be reported for every arm: a blocker that rebounds above baseline is a different clinical object from one that does not |

---

### `E-2` — Gramicidin perforated patch: what is the sign of GABA in a WWOX-deficient neuron?

| Field | |
|---|---|
| **QUESTION** | Is `E_GABA` depolarizing in WWOX-deficient neurons — i.e. is the chloride axis a real target or an inherited assumption? |
| **MODEL** | WWOX-KO vs **isogenic parental** hESC-derived neurons and WOREE patient-iPSC neurons; the same benches `E-1` uses |
| **ARMS** | WWOX-KO · isogenic parental · W-AAV-rescued KO · **and a developmental series**, because the physiological chloride switch is itself a developmental event and a single timepoint cannot distinguish *"inverted"* from *"delayed"* |
| **PRIMARY_ENDPOINT** | **`E_GABA` by gramicidin perforated patch** — the measurement that does not disturb intracellular chloride, which whole-cell recording destroys |
| **MECHANISTIC_ENDPOINT** | NKCC1 and KCC2 protein (not transcript), and the direction of the GABA response |
| **TRUE_RESULT_PATTERN** | `E_GABA` depolarized relative to isogenic parental, with NKCC1/KCC2 ratio shifted immature, and rescued by W-AAV ⇒ the chloride axis is real, `R-07` bumetanide moves from **unrankable to rankable**, and the whole `M3` axis moves **T6 → T2** |
| **FALSE_RESULT_PATTERN** | `E_GABA` indistinguishable from parental ⇒ **the axis closes.** The published WWOX organoid work measures GABAergic *markers*, receptor components and hyperexcitability — **not** chloride reversal, NKCC1/KCC2, GABA response or GABA pharmacology; *"depolarizing GABA"* is a mechanistic hypothesis in this repository, not a datum, and a null here removes it |
| **HOW_IT_CHANGES_PRIORITIZATION** | **This single measurement converts an entire axis or closes it**, and it is the only experiment in the package whose *negative* result is as decision-relevant as its positive one. Bumetanide is presently **unrankable, not low-ranked** — a distinction the portfolio cannot currently act on. It also constrains `E-1`: a depolarizing `E_GABA` changes what an NMDAR blocker is doing to a developing network |
| 🔴 **Interpretation risk** | An organoid with declared regionalization and maturation defects has a different **cell composition** from its control; a population-level `E_GABA` difference may be composition rather than physiology. Mitigate with cell-type-resolved recording and by anchoring the developmental series to a **measured maturation landmark**, not to days in culture. And `MARKER_TO_FUNCTION_GATE` applies in full: NKCC1/KCC2 abundance is not `E_GABA`, which is why abundance is the *mechanistic* and not the *primary* endpoint here |

---

### `E-3` — Delayed dosing with a seizure-matched comparator: symptomatic rescue or disease modification?

| Field | |
|---|---|
| **QUESTION** | Does restoring neuronal WWOX **after** the developmental window move a developmental or cognitive endpoint — or only the symptomatic ones? |
| **MODEL** | A **hypomorphic, non-null** model surviving past weaning — the `Wwox^gt/gt` hypomorph or the `Wwox^P47T` knock-in (> 1 year). **Not** the systemic null, which dies before any learning assay can run and is hypoglycaemic, acidotic and uraemic in the only window it offers |
| **ARMS** | AAV9-hSynI-WWOX at **three timepoints** — P0–P5 (the established window) · post-onset early · post-onset late · AAV9-hSynI-GFP at each timepoint · untreated hypomorph · wild type · 🔴 **and a symptomatic comparator arm: an ASM titrated to equivalent SWD suppression** |
| **PRIMARY_ENDPOINT** | A **cognitive / learning** measure — the empty column of §4 — pre-specified, blinded, powered |
| **MECHANISTIC_ENDPOINT** | Regional WWOX protein (cortex · hippocampus · midbrain · **cerebellum**) · SWD burden · **myelin quantified against wild type, with the WT-vs-treated bracket drawn** · sIPSC amplitude in L2/3 pyramidal neurons |
| **TRUE_RESULT_PATTERN** | The cognitive endpoint improves in the gene-therapy arms and **not** in the seizure-matched ASM arm ⇒ gene addition past the window is **disease-modifying**, `N-15` is bounded to symptomatic levers, and the `PROMISING_BUT_GAP` half of Candidate F is promoted |
| **FALSE_RESULT_PATTERN** | Both arms suppress SWD equally and **neither** moves the cognitive endpoint ⇒ gene addition past the window is **symptomatic**, and `N-15` extends **to the causal lever itself** — the most consequential negative the portfolio could acquire |
| **HOW_IT_CHANGES_PRIORITIZATION** | It is the only experiment that can answer the question **the entire portfolio is ranked on**. It settles `R-01`'s post-neonatal gap, the scope of `N-15`, the `TIME-BUY` scoring of every window-protection entry, and whether *"disease-modifying"* is a property this shelf can claim at all |
| 🔴 **Interpretation risk** | **The ASM-matched arm is the whole design.** Without it, any cognitive improvement is attributable to seizure reduction and the experiment answers nothing — precisely the error `N-15` was written to prevent. Second: a hypomorph is not a null, and the timepoints must be anchored to a **measured developmental landmark**, not to a calendar, or the "window" is a species artefact. Third: this is the most expensive experiment in the package by a wide margin, and it should be run **after** `E-1` and `E-2`, whose results change its arms |

> ### `TOP_3_PRECLINICAL_DISCRIMINATORS`
> **`E-1` occlusion + memantine** (circuit specificity — settles three repair candidates in one
> preparation) → **`E-2` gramicidin `E_GABA`** (GABA polarity — converts an axis or closes it, and
> its null is as informative as its positive) → **`E-3` delayed dosing with a seizure-matched ASM
> comparator** (disease modification vs symptomatic rescue — the only experiment that addresses the
> empty column).
> **Ordered by information per unit cost, and by dependency: `E-3`'s arms depend on `E-1` and `E-2`.**

**Retained elsewhere, deliberately excluded from the top three, so the omission is visible:**
`E-D3` (protein-level mTORC1 + autophagic flux) — cheap and it closes Candidate A, but it
discriminates a *negative's reason*, not a *therapeutic direction*; `E-D4` (genotype × treatment) —
see above; the map's `E-4` (junction-spanning RT-PCR ± NMD block) and `E-5` (nascent synthesis +
pulse-chase) — they discriminate which mechanistic branch an allele takes and remain **mandatory
gates in their own chains**, unaffected by this file.

---

## 6 · Corrections against my own two earlier files

Recorded because a repair file that only corrects the canonical layer is not being held to its own
standard.

| # | Where | What I wrote | What re-derivation shows |
|---|---|---|---|
| **1** | second pass §2.4 | total GSK3β is *"**flat** across genotypes in every region"* | **Understated.** It is an untested but **monotonic +9 / +13 / +18%** trend across three regions. *"Flat"* and *"elevated"* are both wrong; the accurate word is **untested**, and it applies to the pSer9 fall as well — the 7c densitometry carries no error bars, no significance markers and no panel-face n |
| **2** | second pass §5, `RESCUE_ENDPOINTS` | *"myelination is claimed but unquantified in this study's treated arms"* | **Correctly scoped to the dose study, and incomplete as an audit.** The **2021 paper does quantify** myelin in treated arms (CC1⁺, PDGFRα⁺, myelinated and unmyelinated axons/FOV, g-ratio). The finding there is different and sharper: the **WT-vs-rescued bracket is not drawn** where the rescue looks strongest, and where it *is* drawn it is **significant against the rescue** |
| **3** | second pass §8 | `CLAIM 004` listed among the ten *"affected"* records for the DRG/transferred-evidence issue | **`CLAIM 004` already carries its repair**, applied 2026-08-10: *"dove il rescue è confrontato con il WT il confronto o non è tracciato, o è significativo contro il rescue"*. Listing it as affected without naming the existing repair overstates the outstanding work. The **DRG** point stands and is separate |
| **4** | both files | `CLAIM 011` described as needing an endpoint-level rewrite | **True, and the reason is better than I gave.** Its rewrite is *deferred on a stated condition* — that the resolving read is `partial` — and **that condition was discharged on 2026-08-14**. The claim is not merely due for revision; it is waiting on something that already exists |
| **5** | this file, Phase 5 | first sweep returned 41 triples | **26 were an instrument artefact** — `IQ` matching inside *ubiquitination*. Corrected to 15 before any conclusion was drawn, and both numbers are recorded |
| **6** | second pass §5, `DISTRIBUTION` · and this file's first draft | *"the vector systematically under-treats the region carrying the most penetrant motor phenotype"*, citing **`CLAIM 039`** (ataxia 95% vs 0%) | 🔴 **Refuted by the cited claim itself, and it is a two-species splice.** `CLAIM 039` is the **rat `lde/lde`** model and its title ends *"— and it is **not cerebellar**"*; its evidence boundary states the cerebellum is **histologically intact**, that no quantitative motor test was run, and that the assessment was **observational and not blinded**. The cerebellar lesion is a **mouse** finding, properly locatored (foliation defects in lobules V/VI/VII, Purkinje ~18 vs ~7 per area, `FTR-20260804-32000863-01` entry 12). Splicing a rat penetrance figure onto a mouse lesion is exactly the `MECHANISM_TRANSFER_FIREWALL` the map's own rule 3 forbids. **The argument survives entirely within the mouse and is now stated there**: the vector under-transduces a region with a documented lesion **in the model it is tested in**, and nobody measured whether it matters. The rat figure is removed from it |
| **7** | this file, Phase 5, first draft | the human developmental-outcome observation attributed to **`CLAIM 038`** | Wrong anchor. `CLAIM 038` is BUN/creatinine across rodent models. The observation is **[[claim_registry_current#CLAIM 031]]**. Corrected before the sweep table was finalized; recorded because a wikilink that resolves to the wrong claim is worse than one that does not resolve, and `LINT` cannot see the difference |

---

## 7 · Closing blocks

> ### `THERAPEUTIC_REPAIR_CANDIDATE_COUNT: 6`
> A mTOR `INSUFFICIENT` · B lithium boundary propagation · C NMDAR conjunction upgrade ·
> D gap-junction downgrade · E pannexin `N-16` · F AAV9 endpoint split.
> **3 MINOR · 1 MAJOR · 2 MAJOR? → Mirror (fail-closed).** No new molecule. No candidate promoted to
> clinical consideration.

> ### `CLAIM016_035_STATUS: MULTIPLE_AT_ONCE`
> **`MISLOCATOR`** (7b→7d, confirmed verbatim and by independent raster read) · **`OVERCLAIM`**
> (*"elevated"* over an untested +9–18% trend whose own source reports **activation** instead) ·
> **`TRUE_CONTRADICTION`** (the only *in vivo* de-repression evidence is a pS9 western, and
> `CLAIM 035` says a pS9 western must return a false negative here). Plus a canonical competing
> explanation — `CLAIM 036` hypoglycaemia at P18, westerns at P20, Ser9 is the AKT site. **Five
> candidate repairs prepared, none applied.**

> ### `AAV9_ENDPOINT_AUDIT: 4 RESCUED · 1 PARTIAL · 4 UNRESOLVED (3 never measured)`
> Rescued at HD with the WT bracket drawn and null: **survival · SWD · motor · gliosis.** Partial and
> adverse on its only decisive bracket: **myelin (2021 paper).** Qualitative only: **myelin (dose
> study).** Never measured: **cognition · development · post-neonatal efficacy.** Under-transduced
> where the most penetrant phenotype lives: **cerebellum.**
> ⇒ ***"gene therapy rescues the phenotype"* is not an available proposition.**

> ### `DISEASE_MODIFICATION_EVIDENCE_STATUS: ABSENT ON THE EXAMINED CORPUS`
> **207 files · 1 566 cognition/development term occurrences · 15 co-occurring with an intervention
> and an improvement verb · 15 / 15 are the `N-15` negative.** Two positive controls (survival 68,
> motor 12) confirm the sweep detects rescued endpoints that exist. **No external search was
> authorized; 356 catalogued records are unread.** The negative is bounded to this corpus and must
> not be carried beyond it.

> ### `TOP_3_PRECLINICAL_DISCRIMINATORS`
> **`E-1`** occlusion + memantine dose–response (NMDAR / circuit specificity) →
> **`E-2`** gramicidin perforated-patch `E_GABA` (GABA polarity) →
> **`E-3`** delayed dosing in a hypomorph with a **seizure-matched ASM comparator** and a cognitive
> primary endpoint (disease modification vs symptomatic rescue).

> ### `CANONICAL_THERAPEUTIC_PRIORITIES`
> **1. `R-01` AAV9-hSynI-WWOX** — still first, and nothing is close. Now scoped to
> (survival · SWD · motor · gliosis) × HD × P0–P5, with development, cognition, myelin-in-the-dose-study,
> cerebellum and post-neonatal use held at `PROMISING_BUT_GAP`.
> **2. `R-02` NMDAR** — the strongest circuit conjunction, **T1 for the tool compound only**;
> the gap is one compound wide.
> **3. `R-07` bumetanide** — **unrankable, not low-ranked**, and one measurement (`E-2`) settles it.
> **4. The rest of the shelf** is `DEPRIORITIZE`, `TRANSFER_HYPOTHESIS` or `PROMISING_BUT_MECHANISTIC_GAP`,
> unchanged by this file.
> **Nothing here is a clinical recommendation, and no dose, schedule or sequence of care is formulated
> anywhere in this file.**

---

**Layer discipline.** This file modified no canonical file, promoted no hypothesis, named no new
molecule, formulated no clinical indication, dose, schedule or sequence of care, and designed no
sequence or construct. It corrects its own two predecessors in five places. Where it disagrees with
[`mechanism_intervention_map.md`](mechanism_intervention_map.md) or
[`therapeutic_translation_second_pass.md`](therapeutic_translation_second_pass.md), it is the newer
reading; reconciliation goes through INGEST → DEEP_DIVE → COMMIT and through Plan and Orchestrator,
never through this file. Every molecule named anywhere in this chain is **material for discussion
with a treating clinical team**, and nothing here substitutes for one. **Not medical advice.**
