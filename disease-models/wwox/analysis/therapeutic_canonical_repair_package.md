# Therapeutic Canonical Repair Package — six review-ready candidates, the mTOR propagation map, and the endpoint-specific AAV9 model

**Review-ready form of the six repairs, plus the four measurements a reviewer needs to accept or
refuse each one independently.** Nothing here is applied. Every candidate is written so it can be
reviewed, accepted or rejected **without reference to any other candidate in this file**.

> **Status:** non-canonical analysis artefact, fifth in the chain after
> [`mechanism_intervention_map.md`](mechanism_intervention_map.md),
> [`therapeutic_translation_second_pass.md`](therapeutic_translation_second_pass.md),
> [`therapeutic_repair_candidates.md`](therapeutic_repair_candidates.md) and
> [`canonical_impact_and_negative_audit.md`](canonical_impact_and_negative_audit.md).
> **READ-ONLY toward every canonical file. No new molecule appears anywhere.**
> **Nothing here is medical advice.**

**What this file adds over its predecessors** — it is not a restatement:

| New here | Why it was not in the earlier files |
|---|---|
| The **mTOR propagation map** (§2) | the earlier files argued the verdict; none measured where the old verdict had spread |
| **`TRANSFERRED_EVIDENCE`, `BASELINE_IMPACT`, `CANONICAL_TARGET`, `THERAPEUTIC_PRIORITY_EFFECT`** on every candidate | the earlier form had eight fields and could not be routed to a reviewer |
| The **`COMPARATOR` and `STATISTICAL_STATUS`** columns on the AAV9 matrix (§4) | the earlier audit recorded outcomes without recording *against what* and *with what test* |
| The **formal denominator** of the disease-modification negative (§5) | the earlier statement gave a count without exclusion rules |
| **Two corrections adopted from my own prior adjudication** (§3, §7) | `PILOT_PMID32000863_…_SCIB_v1` was on this branch and had not been consulted |
| The **therapeutic overclaim sweep** over the tracker and levers file (§7) | earlier sweeps covered claims; the tracker and the levers file were never swept |

---

## 1 · PHASE 2 — six separable, review-ready candidates

**Separability rule applied:** two candidates are merged only if accepting one *logically entails*
the other. `C` and `D` both edit one sentence of `CLAIM 021` and are still **kept apart**, because a
reviewer can accept the NMDAR upgrade and refuse the gap-junction withdrawal on independent grounds.

`CHANGE_CLASS` follows `LEGEND_CORE` §157 — **MAJOR** = baseline-claim reversal or block
redefinition; **MINOR** = everything else; **MAJOR?** = arguable, routed to Mirror fail-closed per
Annex H.1.

---

### CANDIDATE A — mTOR: `INSUFFICIENT / not directly measured`

| Field | Content |
|---|---|
| **CURRENT_CANONICAL_OR_TRACKER_TEXT** | **No canonical text exists** — see §2, measured. The statement lives in two sub-canonical places: `discovery_ledger_current.md:691` (`DL-MECH-034`), *"**Altri assi alterati (DATO)**: … **autofagia ↓** (RB1CC1/FIP200, MDM2, RB1); **mTOR/EIF4EBP1 ↓**"*; and the map's `N-01 — mTOR inhibitors (rapamycin / everolimus) → **wrong biological direction**`, ranked #2 in `TOP_NEGATIVE_FINDINGS` |
| **PROPOSED_DELTA** | **(i)** re-tag the `DL-MECH-034` line from **`(DATO)`** to **`(DATO transcrittomico, non locatorato, non-FDR)`** — the type line is what downstream scoring reads. **(ii)** `N-01`'s failure mode: *"acts in the wrong direction"* → **`INSUFFICIENT — never measured at protein level in any WWOX system`**. **(iii)** demote `N-01` out of `TOP_NEGATIVE_FINDINGS`. **(iv)** mTOR inhibitors **remain out** at every tier |
| **DIRECT_EVIDENCE** | One bulk RNA-seq: hESC-derived WWOX-KO cerebral organoids, week 15, **n = 2 WT vs n = 4 KO** (started 4+4; one WT failed QC, one excluded for not clustering), fold-change + **raw `P < 0.01`**, **no FDR**. No protein, no p-S6, no p-4E-BP1, no LC3-II/p62, no flux, no rapamycin arm |
| **TRANSFERRED_EVIDENCE** | ⚠️ **Deliberately none.** TSC is not imported. The reflex *"genetic DEE ⇒ try an mTOR inhibitor"* is the transfer this candidate exists to refuse |
| **EVIDENCE_LEVEL** | **T6** for the conjunction — no WWOX system has ever received an mTOR inhibitor. **Direction: undetermined**, not unfavourable |
| **LOCATOR** | 🔴 **None, and that is the candidate.** `deepdive_manifests/PMID34268881.json` carries **12** verbatim locators, **none** touching mTOR, `EIF4EBP1` or autophagy; `fulltext_dossiers/PMID34268881.md` and `commit_candidates/CC-20260814-34268881-01.md` never name them. Sole occurrence in the repository: the `DL-MECH-034` prose line |
| **BASELINE_IMPACT** | **None.** No `consolidated baseline` claim is touched; the canonical layer carries no mTOR statement at all (§2) |
| **CHANGE_CLASS** | **MINOR** |
| **CANONICAL_TARGET** | `discovery_ledger_current.md` (`DL-MECH-034`) — non-canonical append-only ledger · `mechanism_intervention_map.md` (`N-01`, `§2.2`) — analysis layer. **No file among the four scientific current files is targeted** |
| **THERAPEUTIC_PRIORITY_EFFECT** | **Zero movement in ranking; a change of reason.** *"Nobody has measured it"* invites `E-D3` (one blot, no intervention); *"it points the wrong way"* forecloses it. A negative cited as a *demonstration* suppresses the cheapest experiment in the portfolio. **This is a weakening of a negative, not a promotion of a drug class** |

---

### CANDIDATE B — Lithium: propagate the existing genotype boundary; separate anticonvulsant effect from WWOX rescue

| Field | Content |
|---|---|
| **CURRENT_CANONICAL_OR_TRACKER_TEXT** | `CLAIM 016` **already carries** the boundary (2026-08-10, `BATCH_20260810_005`). Two downstream records do not. `therapeutic_strategies_current.md#TX-005`: *"lithium **abolishes** PTZ-induced seizures in Wwox-/-"*, `EVID 2`. `therapy_levers.md` **A2**: *"Lithium (GSK3β inhibition) — **the strongest repurposing signal**… GSK3β is elevated in cortex, hippocampus and cerebellum; lithium inhibits GSK3β and abolishes seizures"*; and **Practical priority 2**: *"lithium as a preclinically-grounded **disease modifier** (GSK3β)"* |
| **PROPOSED_DELTA** | **(i)** propagate `CLAIM 016`'s boundary verbatim into `TX-005` and `therapy_levers.md` A2. **(ii)** retire *"the strongest repurposing signal"*. **(iii)** 🔴 **retire *"disease modifier"* from Practical priority 2** — see `THERAPEUTIC_PRIORITY_EFFECT`. **(iv)** add one sentence to all three: *the effect is a **general anticonvulsant effect**, not a WWOX-specific rescue, and it is a **negative result in an assay of demonstrated sensitivity**.* **(v)** re-score `TX-005` on the failed specificity test rather than on the mechanistic rationale |
| **DIRECT_EVIDENCE** | Figure 7**d**: three stacked genotype panels, **each carrying its own `****` bracket** for PTZ vs PTZ+LiCl — `+/+` N = 12 vs 8, `+/−` N = 12 vs 12, `−/−` N = 6 vs 7. The comparator settles it: Figure 7**b** (ethosuximide) is marked **`n.s.` in `+/+` and `+/−`**, significant in `−/−`, and the text declares it. For lithium the paper declares no converse. Six of seven disaggregated components are empty; the authors state the developmental one themselves: *"Whether lithium treatment can rescue the deficits in neuronal migration and differentiation during development in Wwox−/− mice **remains to be studied**"* |
| **TRANSFERRED_EVIDENCE** | Lithium's paediatric use and its anticonvulsant literature (**T4/T5**) — real, and **not** WWOX evidence. The paper's own Discussion cites lithium attenuating PTZ seizures in ordinary mice, and lithium rescuing Wnt-dependent cerebellar midline defects and inducing myelin gene expression in Schwann cells — three separate non-WWOX mechanisms available to explain the same result |
| **EVIDENCE_LEVEL** | **T5 compound · T2 mechanistic rationale · T1-negative on specificity.** Scored on the failure |
| **LOCATOR** | Caption: *"**d** Pretreatment of a GSK3β inhibitor LiCl (60 mg/kg) suppressed PTZ-induced seizure activity in Wwox−/− mice."* · Results: *"…significantly suppressed PTZ-induced epileptic seizure in Wwox−/− mice **(Fig. 7 d)**."* · Methods: *"LiCl (i.p., 60 mg/kg) were pretreated three times within 1 h before PTZ injection."* Panels re-read at 2× from `40478_2020_883_Fig7_HTML.png`, sha256 `ced68a66…62542`, native 1946 × 1627, matching `source_artifacts` |
| **BASELINE_IMPACT** | **None on a baseline claim.** `CLAIM 016` is `in observation` and already carries the boundary; this is propagation into a tracker and an analysis file |
| **CHANGE_CLASS** | **MINOR** |
| **CANONICAL_TARGET** | `therapeutic_strategies_current.md#TX-005` · `therapy_levers.md` A2 and Practical priority 2. **No claim-registry edit required by this candidate** |
| **THERAPEUTIC_PRIORITY_EFFECT** | Verdict unchanged — **`DEPRIORITIZE`** — reasons strengthened, scope narrowed. 🔴 **The one substantive movement is the removal of *"disease modifier"***: lithium was tested on **one endpoint, once, acutely, as a pre-treatment**, with **zero** developmental endpoints and the authors' own statement that the developmental question is unstudied. Calling it a disease modifier in a section headed *"for clinical discussion"* is the exact inference `N-15` and `CLAIM 031` exist to forbid |
| ⚠️ **Boundary against over-correction** | The primary's abstract says lithium *"significantly **abolishes** the onset of PTZ-induced seizure in Wwox−/− mice"*. **The verb *"abolishes"* is the source's own word and is not a defect.** The defects are the missing genotype boundary, the abundance clause, and *"disease modifier"* |

---

### CANDIDATE C — NMDAR: upgrade the conjunction actually demonstrated, and only that one

| Field | Content |
|---|---|
| **CURRENT_CANONICAL_OR_TRACKER_TEXT** | `CLAIM 021` (`consolidated baseline`), Summary, final clause: *"**Bursting depends on NMDAR and gap junction activity.**"* One sentence, two nodes, one verb, no pharmacology, no direction, no magnitude |
| **PROPOSED_DELTA** | Replace the NMDAR half with: *"**NMDAR blockade (d-APV) abolishes** the pathological burst in the `Wwox` S-KO neocortical slice at P13–P17 — a pharmacological dependence established **inside** the WWOX-deficient system — with a **~1.85× overshoot on washout**."* Upgrade map `CHAIN B` **T2 → T1 for the tool compound only**. Record that **memantine has never been given to a WWOX system**. *(The gap-junction half is Candidate D and is separately reviewable.)* |
| **DIRECT_EVIDENCE** | d-APV takes normalized burst frequency from 1.0 to **zero** (Figure 3D-d1, image-read at 6× from native pixels). On washout, frequency returns to **~1.85×** baseline — recorded, unexplained |
| **TRANSFERRED_EVIDENCE** | GRIN2A in the burst-suppression cohort (`DL-MECH-002`) — **T3**. Memantine's approved use in other CNS indications — **T5**. Neither is WWOX evidence and neither is used to carry the upgrade |
| **EVIDENCE_LEVEL** | **T1 for d-APV** on the bursting endpoint, acute *ex vivo*. **T5 for memantine.** The upgrade attaches to the conjunction, not to the drug |
| **LOCATOR** | `deepdive_manifests/PMID34634460.json`, receipt **`FTR-20260810-34634460-02`**, `complete_fulltext_read`, **21** verbatim locators, several image-anchored. Receipt depth re-verified against `fulltext_read_receipts.jsonl` |
| **BASELINE_IMPACT** | 🔴 **Direct.** `CLAIM 021` is `consolidated baseline`. This half **strengthens** the claim; it does not weaken it. The weakening is Candidate D |
| **CHANGE_CLASS** | **MAJOR?** → Mirror, fail-closed. Editing the Summary of a `consolidated baseline` claim, even to strengthen it, changes what downstream scoring reads |
| **CANONICAL_TARGET** | `claim_registry_current.md#CLAIM 021` — **one of the four scientific current files**; `BATCH_COMMIT` only · map `CHAIN B` / `R-02` |
| **THERAPEUTIC_PRIORITY_EFFECT** | The strongest circuit-level conjunction in the portfolio, and it costs nothing — the experiment is already done and its receipt is ten days older than the map that called it the *"highest-value, lowest-cost open item"*. **It does not promote memantine.** `R-02` stays `PROMISING_BUT_MECHANISTIC_GAP`; the gap narrows from *one experiment* to *one compound* |
| ⚠️ **Interpretation risks, recorded not resolved** | **(i)** P13–P17 in animals dying at 3–4 weeks; the authors write the stage *"may mimic a **late-stage** disorder of WWOX"*. **(ii)** acute slice ≠ chronic *in vivo*. **(iii)** chronic NMDAR blockade in a developing brain removes a signal required for activity-dependent maturation — the process WWOX loss already impairs. **(iv)** the *in vivo* hyperexcitability recordings in the sister paper are made **under ketamine, an NMDA antagonist** (`PMID34747138.json` entry 13: *"the between-group contrast stands; the absolute firing rates are not those of an awake brain"*). Not a contradiction — different drug, dose, preparation and endpoint — but a coincidence to resolve by design, not by assumption. `PREMISE: INFERENZA` |

---

### CANDIDATE D — Gap junction / carbenoxolone: downgrade for non-specificity and washout failure

| Field | Content |
|---|---|
| **CURRENT_CANONICAL_OR_TRACKER_TEXT** | The gap-junction half of `CLAIM 021`'s *"Bursting depends on NMDAR and **gap junction** activity."* The map carries the node as an independent actionable target in `CHAIN B` |
| **PROPOSED_DELTA** | Replace with: *"The carbenoxolone effect on bursting is **real but not attributable to gap junctions** in this dataset."* Remove the gap-junction node from the independent-target list **pending occlusion**. Do **not** state that gap junctions are uninvolved — that was not measured |
| **DIRECT_EVIDENCE** | CBX 100 µM reduces burst frequency by **87%**. Against attribution, from the primary itself: **(i)** the effect **does not wash out** — *"This did not return to normal levels after washout"*; CBX frequency ~0.25 at washout against a 1.0 baseline, duration still carrying a significance marker at washout; **(ii)** the Discussion names two off-target actions for CBX at that concentration — **NMDA receptor block** and **pannexin block** |
| **TRANSFERRED_EVIDENCE** | Gap-junction blockade in other epilepsy models — **T4**. It is what made the node look actionable and it carries none of the attribution |
| **EVIDENCE_LEVEL** | **T1 for the compound · no tier for the target.** With d-APV alone abolishing the burst, the whole CBX result is explicable as Candidate C again |
| **LOCATOR** | `deepdive_manifests/PMID34634460.json`, receipt `FTR-20260810-34634460-02` |
| **BASELINE_IMPACT** | 🔴 **Direct, and this is the withdrawal.** A clause of a `consolidated baseline` claim is retracted on its attribution while the observation behind it is retained |
| **CHANGE_CLASS** | **MAJOR?** → Mirror, fail-closed. A withdrawal inside a baseline claim is a reversal on that axis even though the claim as a whole survives |
| **CANONICAL_TARGET** | `claim_registry_current.md#CLAIM 021` · map `CHAIN B` |
| **THERAPEUTIC_PRIORITY_EFFECT** | One target leaves the portfolio as an independent object. **Nothing is lost clinically** — there is no CNS-appropriate selective connexin blocker, so an unseparated node also had no candidate attached. What is gained: the circuit portfolio stops counting **two** nodes where the data support **one** |

---

### CANDIDATE E — Pannexin blockade: new negative `N-16`, direction adverse

| Field | Content |
|---|---|
| **CURRENT_CANONICAL_OR_TRACKER_TEXT** | **None.** No canonical claim, tracker entry or map entry mentions pannexin blockade. The source's own prose calls it *"**minimal effect** on the network excitability in the `Wwox` S-KO model"* — in Results **and** Discussion |
| **PROPOSED_DELTA** | Add **`N-16 — Pannexin blockade → DEPRIORITIZE`** to the map's negative list, and add the unpropagated pharmacology to `CLAIM 021` alongside C and D. State the direction: **BB-FCF raised normalized burst frequency to ~2.55 during treatment and ~2.6 at washout, against a baseline of 1.0, with no significance test reported** |
| **DIRECT_EVIDENCE** | The point estimate, its direction, and the absence of any reported test |
| **TRANSFERRED_EVIDENCE** | **None.** No pannexin-blockade literature is imported, and none is needed: the candidate is scored on the only WWOX measurement that exists |
| **EVIDENCE_LEVEL** | **T1-negative in direction, untested in significance.** The honest tier is *"one measurement, adverse point estimate, wide error, no test"* |
| **LOCATOR** | `deepdive_manifests/PMID34634460.json`, receipt `FTR-20260810-34634460-02` |
| **BASELINE_IMPACT** | **Additive.** No existing statement is reversed; a node that was never scored is scored |
| **CHANGE_CLASS** | **MINOR** |
| **CANONICAL_TARGET** | `mechanism_intervention_map.md` (negative list) · `claim_registry_current.md#CLAIM 021` (unpropagated pharmacology, jointly with C and D) |
| **THERAPEUTIC_PRIORITY_EFFECT** | The only candidate here that **adds** a record — and it adds a **negative**, not a molecule. 🔴 The finding is that a **2.5-fold point estimate with wide error and no test is not an absence of effect, and its direction is the opposite of the one the prose implies.** A reader of the text alone would not know there was a direction to worry about |
| ⚠️ **Boundary** | `DEPRIORITIZE` here means *"the only WWOX measurement points the wrong way and was not tested"*, **not** *"pannexins are uninvolved"*. `REVIVAL_TRIGGER`: a powered, significance-tested pannexin arm reporting a **reduction**, and — per the authors' own suggestion — at an **earlier developmental stage** than P13–P17 |

---

### CANDIDATE F — AAV9-hSynI-WWOX: split the class by endpoint

| Field | Content |
|---|---|
| **CURRENT_CANONICAL_OR_TRACKER_TEXT** | `CLAIM 004` (`consolidated baseline`): *"Preclinical AAV9-WWOX rescue improves survival, hyperexcitability and myelin-related phenotype"* — **with a 2026-08-10 qualification already applied**. `CLAIM 011` (**`flagged for review`**): *"rescue dose-dependent e durevole su: sopravvivenza, crescita, glucosio, comportamento, mielinizzazione, gliosi, ipereccitabilità / SWD"*. `TX-007`: *"neonatal ICV → **seizure/myelin/survival rescue**"*. Map `R-01`: the **sole** entry in `READY_FOR_WWOX_PRECLINICAL_CONSIDERATION` |
| **PROPOSED_DELTA** | Move the class from the **intervention** to the **(intervention × endpoint × window)** triple — the map's own ladder rule applied to its own top entry. **Retain** `READY_FOR_WWOX_PRECLINICAL_CONSIDERATION` for **survival · SWD · motor · gliosis**, at HD, in the P0–P5 window. **Downgrade to `PROMISING_BUT_GAP`** for **cognition · development · myelin-in-the-dose-study · cerebellum · post-neonatal administration**. Adopt the §4 matrix wording. Qualify `comportamento` (§7) |
| **DIRECT_EVIDENCE** | §4, in full. In brief: WT-vs-HD is **`ns`** — i.e. tested and null — for SWD (7E), gliosis (S8I) and motor (S4A). Cognition and development have **no assay**: 29 + 20 = **49 locators enumerated, zero cognitive endpoints**. Cerebellum at **1.4×** WT against cortex 8.2× and hippocampus 10.7×, and **below** WT at P30 |
| **TRANSFERRED_EVIDENCE** | 🔴 **One piece, and it is currently mislabelled as direct.** `R-01`'s `KNOWN_MAJOR_SAFETY_CONSTRAINTS` asserts *"dose-limiting DRG/peripheral-ganglion toxicity at high systemic dose"* in a field otherwise reporting this vector's own measurements. **No DRG assessment exists in either WWOX paper.** The source is a **review, at class level** (PMID 42128308 §11). The genuinely WWOX-measured PNS fact is **sciatic-nerve biodistribution** — a different object |
| **EVIDENCE_LEVEL** | **T1** for survival / SWD / motor / gliosis. **No tier** for cognition and development — a tier requires a measurement. **T1-partial** for myelin (2021 paper). **Untested** for post-neonatal dosing. **T4/T5** for the DRG constraint |
| **LOCATOR** | `deepdive_manifests/PMID42422765.json` (`FTR-20260814-42422765-06`, **`complete_fulltext_read`**, 29 locators) · `deepdive_manifests/PMID34747138.json` (`FTR-20260810-34747138-01`, **`complete_fulltext_read`**, 20 locators). Both depths re-verified against the ledger this session |
| **BASELINE_IMPACT** | 🔴 **Highest in this package.** `CLAIM 004` is `consolidated baseline` with `clinical relevance: HIGH` in `P7 — gene therapy readiness`; `CLAIM 011` is `flagged for review` in the same pathway; `TX-007` is the tracker's **north star** |
| **CHANGE_CLASS** | **MAJOR** — narrowing a readiness class in the gene-therapy pathway is block-adjacent. Orchestrator authorization required |
| **CANONICAL_TARGET** | `claim_registry_current.md#CLAIM 004` and `#CLAIM 011` — two of the four scientific current files · `therapeutic_strategies_current.md#TX-007` · map `R-01` |
| **THERAPEUTIC_PRIORITY_EFFECT** | 🔴 **`R-01` still ranks first and nothing is close.** What it no longer does is rank first **on disease modification**, because nothing in the portfolio has been measured there (§5). **A downgrade in scope, not in rank** — the previous class name asserted a readiness the developmental column does not support, and `R-01` was the only entry in that class, so the class name was doing the portfolio's ranking by itself |

> ### `THERAPEUTIC_REPAIR_CANDIDATE_COUNT: 6` — independently reviewable
> **3 MINOR** (A, B, E) · **1 MAJOR** (F) · **2 MAJOR?** (C, D) → Mirror, fail-closed.
> Candidates touching one of the four scientific current files: **C, D, F**. Candidates touching only
> ledgers, trackers and analysis: **A, B, E**. **No new molecule. Two candidates weaken a negative;
> neither promotes the class it weakens.**

---

## 2 · PHASE 3 — mTOR propagation map

**Question:** the verdict moved from *"wrong direction"* to `INSUFFICIENT`. **Where had the old
verdict spread, and what has to be repaired?**

**Population, enumerated before measuring:** **212 files** — 133 disease-model markdown, 64 deepdive
manifests, 5 registry `.jsonl`, 10 top-level full-text artefacts, plus `framework/state/*.md`.
Tokens swept: `mTOR`, `EIF4EBP1`/`4E-BP`, `autophag|autofag`, `rapamycin|sirolimus`, `everolimus`,
`LC3`, `SQSTM1`/`p62`.

### 2.1 Raw token counts

| Token | Occurrences |
|---|---|
| `mTOR` | 116 |
| `autophag` / `autofag` | 94 |
| `EIF4EBP1` / `4E-BP` | 33 |
| `SQSTM1` / `p62` | 9 |
| `LC3` | 8 |
| `rapamycin` / `sirolimus` | 8 |
| `everolimus` | 5 |

### 2.2 The result the raw counts hide

> 🔴 **Across 238 files — the whole disease model plus every local full text — the words
> `rapamycin`, `sirolimus` and `everolimus` occur in exactly three files, and all three are my own
> analysis files.** Zero in any registry, zero in any ledger, zero in any primary, zero in any
> manifest.

**The entire mTOR-inhibitor question exists in this repository only inside the documents that argue
about it.** `N-01` is a negative about a drug class the corpus has never encountered.

### 2.3 Classification of every hit that carries a *direction*

| Class | Count | Where |
|---|---|---|
| **PRIMARY_MEASUREMENT** | **0** | no protein-level mTORC1 readout and no autophagic-flux measurement exists on any surface. The local full-text hits are inside **reference lists** — cited article titles, not measurements |
| **SECONDARY_SUMMARY** | **1** | `discovery_ledger_current.md:691` (`DL-MECH-034`) — *"autofagia ↓ … mTOR/EIF4EBP1 ↓"*, tagged **`(DATO)`** |
| **INFERENCE** | 3 files | `therapeutic_translation_second_pass.md` §1, `therapeutic_repair_candidates.md` Candidate A, `canonical_impact_and_negative_audit.md` — correctly typed, and each already carries the correction |
| **UNSUPPORTED_PROPAGATION** | **1** | the map's `N-01` block — *"wrong biological direction"*, `TOP_NEGATIVE_FINDINGS` #2 — restating the ledger line as a demonstration |
| **BIBLIOGRAPHIC ONLY** | 8 | 4 titles in `paper_registry_current.md`, 4 in `literature_tracking_log_current.md` — unread corpus stubs; a title fixes no direction |

### 2.4 🔴 The canonical layer is clean — measured

| Surface | mTOR-family hits |
|---|---|
| `claim_registry_current.md` | **0** |
| `working_model_current.md` | **0** |
| `disease_model.md` | **0** |
| `state_manifest_current.md` | **0** |

**The bad interpretation never reached the canonical layer.** The repair is confined to **one ledger
line and one analysis-file block** — two edits, both MINOR, neither requiring a `BATCH_COMMIT`.

### 2.5 ⚠️ The distinction a token sweep destroys, and it matters here

Of the 84 `autophag`/`autofag` mentions in disease-model markdown, a large fraction belong to a
**completely different axis**: the **WWOX-protein-turnover** work — CMA, HSC70, LAMP1, chloroquine,
3-MA, K63 ubiquitination, the P252A/Q230P proteostasis chain, `4-PBA`/`TUDCA`. That axis is about
**how the WWOX protein is degraded**. The mTOR axis is about **whether mTORC1 signalling moves in a
WWOX-deficient neuron**. They share a word and nothing else.

**Any future repair sweep on this token must separate them first**, or it will "repair" the
proteostasis chain — which is independently evidenced, locatored, and not in question — while
hunting an mTOR statement that lives in one line.

> ### `MTOR_PROPAGATION_REPAIR: 2 sites · 0 canonical · MINOR`
> **Site 1** — `DL-MECH-034` line 691: re-tag `(DATO)` → `(DATO transcrittomico, non locatorato, non-FDR)`.
> **Site 2** — map `N-01`: *"wrong biological direction"* → `INSUFFICIENT`, and demote from
> `TOP_NEGATIVE_FINDINGS`. **Nothing else needs to change, because nothing else carried it.**

---

## 3 · PHASE 4 — `CLAIM 016` / `CLAIM 035`: dedicated repair candidate

### 3.1 The seven measures, separated

| Measure | State | What the artefact actually contains |
|---|---|---|
| **MISLOCATOR** | 🔴 **confirmed** | `CLAIM 016`'s evidence boundary cites **Fig. 7b** for the lithium panel. Caption and Results say **7d**; **7b is ethosuximide**. Confirmed three ways: Results text, figure legend, and the panels themselves |
| **TOTAL_GSK3B** | **`MEASURED · NOT_TESTED`** | cerebellum **2.2 / 2.4 / 2.4**, hippocampus **2.3 / 2.4 / 2.6**, cortex **2.2 / 2.4 / 2.6** across `+/+ · +/− · −/−` |
| **P-SER9** | **`MEASURED · NOT_TESTED`** | cerebellum **2.7 / 3.1 / 1.3**, hippocampus **3.6 / 3.5 / 2.0**, cortex **3.9 / 3.8 / 2.5** |
| **ABUNDANCE** | 🔴 **`NOT_ASSERTED_BY_EITHER_SOURCE`** | Cheng's abstract says *"significantly increased **activation**"*; Wang reports abundance **unchanged**. Neither says abundance is elevated |
| **ACTIVITY_INFERENCE** | Cheng: **inferred from a phospho-site** · Wang: **measured directly** | Cheng: *"increased **activation** … as evidenced by **dephosphorylation** of GSK3β at Ser9"*. Wang measures kinase output — Tau pS396/S404, microtubule assembly, neurite outgrowth |
| **ASSAY_LIMIT** | 🔴 **canonically stated, and violated** | `CLAIM 035`: de-repression from loss of the WWOX brake is **invisible to an anti-phospho-S9 western**; any WWOX study using pS9 as an activity readout *"produrrà un falso negativo"* |
| **IN_VIVO_DE_REPRESSION** | **one western, one site, one age — and the age is not established** | the only *in vivo* evidence is Cheng Fig. 7c. Wang's system is SH-SY5Y + recombinants + endogenous brain co-IP: it establishes the mechanism, not its *in vivo* operation |

### 3.2 The required wording — neither *"flat"* nor *"elevated"*

The Operator's constraint is the correct one and it applies to **both rows**, not only to abundance.

🔴 **The 7c densitometry carries no error bars, no significance markers and no n on the panel face**,
under a legend declaring *"representative results of four independent experiments"* with **one lane
per genotype per region**. Therefore:

| Forbidden | Why |
|---|---|
| *"GSK3β is **elevated**"* | asserts a direction and a significance the panel does not carry, and contradicts the source's own interpretation |
| *"total GSK3β is **flat**"* | asserts a **null result**, which is equally an inference from an untested panel — and it understates a monotonic movement of **+9% / +13% / +18%** from `+/+` to `−/−`, in the same direction in all three regions |

**Proposed canonical wording:**

> *"In `Wwox`-null mouse brain, Figure 7c reports densitometry for total GSK3β and for
> pGSK3β(Ser9) in cerebellum, hippocampus and cortex. **`STATISTICAL_STATUS: NOT_TESTED`** — the
> panel carries one lane per genotype per region, no error bars, no n and no significance marker,
> under a legend declaring representative results of four independent experiments. Total GSK3β
> moves by **+9% / +13% / +18%** from `+/+` to `−/−`; pSer9 falls by **−52% / −44% / −36%**. The
> source's stated evidence is **Ser9 dephosphorylation — i.e. activation, not abundance** — and no
> abundance claim appears in either cited source."*

**Type line:** `DATO (abbondanza, murino)` → **`DATO densitometrico non testato (murino) — direzione registrata, significatività non disponibile`**.

### 3.3 🆕 Two observations adopted from my own prior adjudication, one of them corrected

`reviews/scientist-b/PILOT_PMID32000863_GSK3B_LITHIUM_ADJUDICATION_SCIB_v1.md` sits on this branch
and had not been consulted by the two earlier files. It carries two things they missed.

**(a) The heterozygote is not intermediate — there is no gene-dosage gradient.**
On the phospho row `+/−` is **3.1 vs 2.7** (cerebellum, above `+/+`), **3.5 vs 3.6** (hippocampus)
and **3.8 vs 3.9** (cortex). On the total row `+/−` is **2.4** in all three regions.
⚠️ **The prior adjudication states this as *"at or above `+/+` in every one of the three regions"*,
and that is 0.1 too strong in two of three.** The correct and still-decisive statement: **the
heterozygote is indistinguishable from wild type on both rows and is not intermediate between wild
type and null.** For a claim about a **dose-dependent** brake, the absence of a heterozygote gradient
is a datum, and it is not recorded on any canonical surface.

**(b) 🔴 The age of the Fig. 7c blot is not established by the paper.**
Methods, *Western blotting*: tissues *"isolated from three genotypes of mice at **postnatal day
14**"*. Figure 7c legend: *"at **postnatal day 20**"*. Figure 6a legend: *"at postnatal day 14 **or**
20"*. **Verified this session directly in the JATS.**

This **strengthens rather than weakens** the `CLAIM 036` confounder, and the previous formulation was
imprecise in my favour: `therapeutic_repair_candidates.md` asserts *"Cheng's westerns are taken at
P20"* — a date the paper does not settle. `CLAIM 036` measures metabolic decompensation at **P18**,
in a P14–P20 window; **both candidate ages fall inside or immediately beside it**, so the confounder
applies under either reading and the argument no longer depends on choosing one.

### 3.4 The mutual exclusion — unchanged and still the substantive finding

`CLAIM 035` says the WWOX brake is **S9-independent** and that a pS9 western must return a **false
negative**. `CLAIM 016`'s only *in vivo* de-repression evidence **is** a pS9 western, and it moved.
Both cannot describe the same brake:

- **(a)** the pS9 fall is driven by something **other** than loss of the WWOX docking-site brake ⇒
  Cheng's western is **not** evidence that the `CLAIM 035` mechanism operates *in vivo*, and map
  `CHAIN C` has **no in-vivo anchor**; **or**
- **(b)** it **is** WWOX-dependent ⇒ `CLAIM 035`'s S9-independence needs a boundary it does not have.

**Competing explanation for (a), already canonical:** Ser9 is the **AKT** site; AKT tone follows
insulin and glucose. `CLAIM 036` records the systemic constitutive null at P18 as hypoglycaemic
(**143.5 vs 250.6 mg/dL**, `p = 0.000131`), acidotic and uraemic. `PREMISE: INFERENZA`; `CLAIM 036`
is a **different null strain** (EIIA-Cre), so what transfers is the **confounder class**, not the
numbers. **It does not refute the finding — it means the design cannot separate a WWOX-dependent
brake from a systemic metabolic one.**

### 3.5 The repair candidate

| # | Target | Delta | Class |
|---|---|---|---|
| **R4-1** | `CLAIM 016` evidence boundary | 🔴 **not a bare `7b → 7d` swap.** The parenthesis bundles **two** observations: the lithium three-genotype result (**7d**) and the ethosuximide `n.s.`/significant pattern (**7b — correct for that clause**). A swap repairs the first and **breaks** the second. Proposed form splits the pointers: *"(Fig. 7d; per l'etosuccimide — esperimento distinto, **Fig. 7b** — il testo dichiara `n.s.` in `+/+` e `+/−` …)"* | MINOR |
| **R4-2** | 🆕 `state_manifest_current.md`, `batch_20260810_005_scope` | **the same defect, second site**, not previously in my repair set: *"(PMID 32000863 Fig 7b, read from the image)"* → **`Fig 7d`**. Here there is no ethosuximide clause, so it is a clean swap. ⚠️ This is the **historical scope record of a completed batch**; correcting it in place needs an explicit inline marker rather than a silent rewrite, and that choice is the integrator's | MINOR — but **not a `BATCH_COMMIT` object**; the manifest is the one state-control file writable outside a batch |
| **R4-3** | `CLAIM 016` Summary + boundary + `Type` | adopt the §3.2 wording; **`NOT_TESTED`**, neither *"flat"* nor *"elevated"*; remove *"Cosa NON cambia: il dato di abbondanza"*, which preserves a datum neither source asserts | MINOR? → Mirror |
| **R4-4** | `CLAIM 016` **and** `CLAIM 035` | reciprocal boundary naming the mutual exclusion and both horns. Neither may cite the other as corroboration **on the S9 axis** until one horn closes | **MAJOR?** → Mirror |
| **R4-5** | `CLAIM 016` | add the `CLAIM 036` confounder, `INFERENZA`, explicitly **not** a refutation; state that the blot age is **P14 or P20, unsettled by the paper**, and that both fall in the window | MINOR |
| **R4-6** | 🆕 `CLAIM 016` | record that **the heterozygote is not intermediate** on either row — no gene-dosage gradient | MINOR |
| **R4-7** | map `CHAIN C` / `R-04` | delete *"GSK3β abundance elevated … (2 sources)"*; the `PREMISE_TAG` *"abundance reports activity"* is a premise about a datum that does not exist. Replace with the phospho-site critique | MINOR |

> ### `CLAIM016_035_REPAIR_READY: YES` — 7 deltas · 5 MINOR · 1 MINOR? · 1 MAJOR?
> **Two sites, not one** — the claim and the state manifest carry the identical pointer defect,
> because one was written from the other. **The reading was sound; the transport was not.**

---

## 4 · PHASE 5 — AAV9 endpoint-specific canonical model

**Design rule:** every cell records **against what** the comparison was drawn and **with what test**.
`RESCUE` is reserved for a **treated-vs-wild-type** comparison that exists **and is null**. A
`KO-vs-treated` bracket alone shows treatment did *something*; it cannot show treatment was
*sufficient*.

| Endpoint | MEASURED | COMPARATOR drawn | STATISTICAL_STATUS | Verdict |
|---|---|---|---|---|
| **SURVIVAL** | ✅ quantified | WT · KO · four doses | Kaplan–Meier across 4 doses | **`RESCUE`** at HD (~75–80% to d300) · **`NO_RESCUE`** at LD (death ~90 d) and at 4×10¹⁰ / 8×10¹⁰. 🔴 threshold has **no measured expression correlate** — 7/8 dose comparisons `ns`; the paper's explanation is **survivor-conditioned** |
| **SWD** | ✅ quantified | **WT-vs-KO, KO-vs-HD, WT-vs-HD** | `****` · `****` · **`ns`** | **`RESCUE`** — the decisive bracket exists and is null |
| *(spikes/day)* | ✅ quantified | WT-vs-KO | **`p = 0.2000` printed on the panel face**, n = 5/group, no asterisk and no `ns` | 🔴 **`UNRESOLVED`** — the running text calls the same comparison *"a significant elevation"* |
| **MOTOR** | ✅ quantified | WT · KO · LD · HD | **WT-vs-HD `ns`**, LD-vs-HD `***` | **`RESCUE`** at HD · **`PARTIAL`** at LD. 🔴 Fig. 4D/4E carry `*p<0.05` **against WT** for velocity and distance while the text says *"no significant differences"*; and **LD animals do not reach P90**, so all P90 behaviour is HD-only and **survivor-selected** |
| **GLIOSIS** | ✅ quantified | **WT-vs-KO and WT-vs-treated** (S8I) | `***` · **`ns`** | **`RESCUE`** at HD. 🔴 **`NO_RESCUE` at LD** — S7H shows LD significantly worse than WT (`**`) while HD is `ns` |
| **MYELIN** *(dose study, 42422765)* | ⚠️ **qualitative only** | **none** — Fig. 6F, S7I, S8G are representative images; the only MBP quantification (6E) has **no treated arm** | **none** | 🔴 **`UNRESOLVED`** — the text claims *"near-complete rescue across affected regions"* |
| **MYELIN** *(2021 paper, 34747138)* | ✅ quantified | **WT-vs-KO and KO-vs-rescued — never WT-vs-rescued**, except on one panel | `***`/`**`/`*` on the drawn brackets; **the residual gap is untested** | **`PARTIAL`**. 🔴 On the **one** panel where WT-vs-rescued **is** drawn — unmyelinated axons/FOV, **WT ~26 vs treated ~52, `**`** — it is **significant against the rescue**. CC1⁺ **170/77/135**, PDGFRα⁺ **53/87/70**, myelinated axons CC **130/46/105**, optic nerve **140/68/124**. g-ratio does normalise. n = 3 |
| **CEREBELLUM** | ⚠️ measured **only as a distribution compartment**, never as a functional endpoint | WT | quantified | 🔴 **`NO_RESCUE`** on transduction · **`UNRESOLVED`** on function. **Below** WT at P30 (Fig. 5L); at P300 **1.4× WT** against cortex 8.2×, hippocampus 10.7×, midbrain 5.6×; S6D prints cerebellum **0**. The same model carries locatored **foliation defects in lobules V, VI and VII with Purkinje ~18 vs ~7 per area** |
| **COGNITION** | 🔴 **`NOT_MEASURED`** | — | — | **`UNRESOLVED`.** 49 locators enumerated across both papers; **zero cognitive assays** — no maze, no novel object, no fear conditioning, no operant task |
| **DEVELOPMENT** | 🔴 **`NOT_MEASURED`** | — | — | **`UNRESOLVED`.** No developmental-trajectory endpoint, no milestone acquisition. ⚠️ Weight and glucose at P14 are `ns` vs WT — those are **growth and metabolic** endpoints and must not be counted as developmental |
| **POST_NEONATAL** | 🔴 **`NOT_MEASURED`** | — | — | **`UNRESOLVED`.** Dosing is P0–P5 throughout; declared **explicitly as future work** in both papers. Within the window the 300-day panel shows only **P1 and P5**; P2–P4 exist only in the 40-day panel and **P3 is an n = 3 arm that lost animals** |

### 4.1 The formulation that blocks the global sentence

**Proposed canonical form for `CLAIM 004` and `CLAIM 011`** — written so the global proposition
cannot be reconstructed from it:

> *"AAV9-hSynI-WWOX, neonatal ICV at high dose in the P0–P5 window, produces a **wild-type-equivalent
> result on four endpoints** — survival, SWD, motor function and astrogliosis — each with the
> treated-versus-wild-type comparison **drawn and non-significant**. On **myelination** the rescue is
> **partial**, and on the single panel where treated is compared with wild type it is **significant
> against the rescue**. On **cognition, developmental trajectory and post-neonatal administration no
> measurement exists in either study**. The **cerebellum** is under-transduced at every dose and
> timepoint and carries no functional endpoint. **No statement of the form 'the phenotype is rescued'
> is supported: the class attaches to an (endpoint × dose × window) triple and not to the
> intervention.**"*

> ### `AAV9_CANONICAL_MATRIX_READY: YES`
> **4 `RESCUE` · 1 `PARTIAL` · 1 `NO_RESCUE`-on-its-only-drawn-bracket · 5 `UNRESOLVED`, of which 3 `NOT_MEASURED`.**
> The structural finding: **the comparison that defines sufficiency is drawn for survival, SWD, motor
> and gliosis, and is systematically absent from the myelin quantifications** — and where it is
> present there, it fails.

---

## 5 · PHASE 6 — the disease-modification denominator, formalised

### 5.1 The five declarations

| Element | Definition |
|---|---|
| **CORPUS** | **207 files**: 133 `disease-models/wwox/**/*.md` · 64 `research/deepdive_manifests/*.json` · 10 top-level `files/fulltext/` artefacts. Enumerated with `Path.glob` **before** any pattern ran. ⚠️ **Excluded and declared:** all live connectors (PubMed, Scholar Gateway, bioRxiv, Clinical Trials, AdisInsight) were **unauthorized this session** — no external search was run — and **356 catalogued `CORPUS` placeholder records are unread**, so their contents are unknown to this measurement |
| **INTERVENTIONS_INCLUDED** | Every intervention named anywhere in the portfolio: AAV9 / W-AAV / gene therapy · lithium (LiCl) · memantine · d-APV · carbenoxolone · BB-FCF · ethosuximide · vigabatrin · levetiracetam · phenobarbital · ketogenic diet · rapamycin · everolimus · bumetanide · XAV939 · CHIR · tankyrase inhibitors · 4-PBA · TUDCA · arimoclomol · clemastine · digoxin · dichloroacetate · ASO · base/prime editing · CRISPRa — **and the generic token `treated`**, so that an unnamed intervention arm still enters the population |
| **ENDPOINTS_SEARCHED** | `cognit*` · `learning` · `maze` · `novel object` · `fear conditioning` · `developmental quotient/trajectory/outcome/milestone` · `neurodevelopmental outcome` · `milestone` · `psychomotor`/`psicomotor` · `DQ` · `IQ` · `Bayley` · `Vineland` · `Griffiths` · `adaptive behaviour` · `nest building` · `operant` · `working/spatial memory` · `memory task/test/deficit/impairment` |
| **POSITIVE_CONTROLS** | Two, run on the **identical machinery** with only the endpoint lexicon changed. **Survival** (`surviv`/`lifespan`/`Kaplan`): **68 triples across 22 files**. **Motor** (`rotarod`/`open-field`/`locomot`/`gait`/`ataxi`/motor function): **12 triples across 4 files**. ⇒ the sweep detects rescued endpoints **that exist** |
| **EXCLUSION_RULES** | **(1)** `IQ` and `DQ` **word-boundary anchored** — unanchored, `IQ` fires inside *ub**iq**uitination*, *un**iq**ue* and *ub**iq**uitario*, which saturate this corpus's proteostasis literature. **(2)** co-occurrence window **± 300 characters**, requiring **both** an intervention token **and** an improvement verb (`improv`/`rescu`/`restor`/`correct`/`normali[sz]`/`amelior`/`recover`/`migliora`/`ripristin`). **(3)** *"Independently"* enforced by hand: a developmental improvement **inferred from** a seizure improvement does not count; the measure must be its own measure. **(4)** growth and metabolic endpoints (weight, glucose) are **not** developmental endpoints |

### 5.2 The measurement, and the instrument repair inside it

| Step | Result |
|---|---|
| Endpoint-term occurrences anywhere in the corpus | **1 566** |
| …co-occurring with an intervention **and** an improvement verb | **15**, in **5 files** |
| …surviving hand adjudication as *"seizure improves **and** development/cognition independently improves"* | **0** |

**All 15 are the `N-15` negative or a restatement of it** — 5 in the map, 4 in the second pass, 2 in
`claim_registry_current.md` ([[claim_registry_current#CLAIM 031]]), 3 in `paper_registry_current.md`,
1 in `therapeutic_hypotheses_ledger_current.md`.

🔴 **The instrument was repaired mid-measurement and both numbers are recorded.** A first pass
returned **41**; **26** were the `IQ` artefact above. Word-boundary anchoring left 15. *A count
nobody can reproduce is not a denominator.*

### 5.3 The negative, with its scope

> ## `DISEASE_MODIFICATION_EVIDENCE_STATUS: ABSENT ON THE EXAMINED CORPUS`
>
> **Across 207 files comprising the entire local WWOX disease model, its 64 deepdive manifests and
> its 10 machine-readable primaries, there is no record of any WWOX intervention — pharmacological,
> dietary, genetic or gene-addition — for which a seizure or electrographic endpoint improved AND a
> developmental or cognitive endpoint independently improved.**
>
> **Every intervention with a filled `SEIZURE_CONTROL` cell has an empty `DEVELOPMENTAL_TRAJECTORY`
> cell and an empty `COGNITION` cell — without exception, including the gene therapy.** The only
> data in those two columns are **human, observational, uncontrolled, N = 2, and negative**.

**What it is not.** Not *"disease modification is impossible in WWOX"*. Not *"gene therapy does not
modify the disease"*. Not a statement about the published literature: **no external search was
authorized, and 356 catalogued records are unread.** It is a statement about **what this repository
can currently support** — and the operational reading is that **the column that would rank the
portfolio is empty for every candidate in it.**

---

## 6 · PHASE 8 — the three discriminators, stress-tested for informative nulls

**The test applied to each:** *if the result is null, does the portfolio learn something that changes
a decision?* An experiment whose null is uninformative is a data-collection exercise.

### `E-1` — NMDAR occlusion + memantine

**How it separates causal dependence from generic suppression.** Abolishing a burst is what many
manipulations do; a **silenced slice is not evidence of a specific target**. Two design features do
the separating: **(i)** the **occlusion term** — CBX applied on top of *sub-maximal* d-APV — asks
whether the gap-junction effect exists in a space where NMDAR is already partly blocked, which
generic suppression cannot survive; **(ii)** the **isogenic parental and W-AAV-rescue lines as
internal comparators** — a compound that suppresses bursting equally in the rescued line is
suppressing excitability, not correcting a WWOX-dependent mechanism.

| Field | |
|---|---|
| **FALSIFIER** | CBX produces **no further reduction** on top of sub-maximal d-APV **and** memantine's dose–response is flat where d-APV is maximal |
| **INTERPRETATION_IF_NULL** | The gap-junction node **collapses into the NMDAR node** and stops being an independent target; `R-02` becomes the **only** circuit candidate. If memantine is additionally flat, the T1 conjunction stays attached to a tool compound that will never reach a child, and `R-02` does **not** advance. **Both nulls change the portfolio** |
| **INTERPRETATION_IF_POSITIVE** | Gap junctions are independent ⇒ Candidate D is refused and the node returns — but with **no CNS-appropriate selective connexin blocker in existence**, it returns as a target without a candidate. Memantine positive ⇒ the single largest available move in the shelf |
| **MAIN_CONFOUND** | 🔴 **d-APV drives frequency to zero, so at full block there is no headroom for occlusion.** The co-application must run at a sub-maximal concentration taken from the memantine dose–response, or the experiment **cannot fail informatively**. Second: the **washout overshoot** (~1.85× baseline) must be reported for every arm — a blocker that rebounds above baseline is a different clinical object. Third: `+/−` and slice-to-slice variability at P13–P17, a stage the authors call *"late-stage"* |

### `E-2` — gramicidin perforated-patch `E_GABA`

**How it separates polarity from amplitude loss.** These are different failures with the same
downstream sign, and the standard assay cannot tell them apart. **Amplitude loss** — the canonical
finding here is inhibitory current amplitude **−52%** — is a change in *how much* inhibition arrives.
**Polarity inversion** is a change in *which direction* it pushes. `E_GABA` measures the reversal
potential and is **indifferent to amplitude**; sIPSC amplitude measures the current and is
**indifferent to reversal**. Running **both in the same cells** is what separates them: a depolarized
`E_GABA` with preserved amplitude is a chloride defect; a normal `E_GABA` with reduced amplitude is a
synaptic or receptor defect; both together are two lesions, not one.

| Field | |
|---|---|
| **FALSIFIER** | `E_GABA` in WWOX-KO neurons is **indistinguishable from isogenic parental** across the developmental series |
| **INTERPRETATION_IF_NULL** | 🔴 **The chloride axis closes.** *"Depolarizing GABA"* is a **mechanistic hypothesis** in this repository, not a datum — the published organoid work measures GABAergic **markers**, receptor components and hyperexcitability, and **not** chloride reversal, NKCC1/KCC2, the GABA response or GABA pharmacology. A null removes it and moves `R-07` bumetanide from **unrankable** to **closed**, and the E/I finding is then attributable to amplitude alone |
| **INTERPRETATION_IF_POSITIVE** | `E_GABA` depolarized, NKCC1/KCC2 shifted immature, rescued by W-AAV ⇒ the `M3` axis moves **T6 → T2** and bumetanide becomes **rankable**. It also constrains `E-1`: a depolarizing `E_GABA` changes what an NMDAR blocker is doing to a developing network |
| **MAIN_CONFOUND** | 🔴 **Cell composition.** An organoid with declared regionalization and maturation defects is not composition-matched to its control, so a population-level `E_GABA` difference may be *which cells were recorded* rather than *what those cells do*. Mitigate with cell-type-resolved recording. Second: the physiological chloride switch is itself a developmental event, so a **single timepoint cannot distinguish *inverted* from *delayed*** — the series must be anchored to a **measured maturation landmark**, not to days in culture. Third: `MARKER_TO_FUNCTION_GATE` — NKCC1/KCC2 abundance is **not** `E_GABA`, which is why it is the mechanistic and not the primary endpoint |

### `E-3` — delayed gene therapy with a seizure-matched ASM comparator

**How it separates symptomatic seizure control from developmental modification.** It cannot be done
by measuring cognition after gene therapy: any cognitive improvement in an animal whose seizures also
improved is attributable to the seizure improvement, and that inference is exactly `N-15`. **The
separation is the comparator arm, not the endpoint.** An ASM titrated to *equivalent SWD suppression*
holds the symptomatic variable constant between arms; whatever cognitive difference remains cannot be
seizure burden, because seizure burden was matched by construction.

| Field | |
|---|---|
| **FALSIFIER** | Both arms suppress SWD equally **and** neither moves the cognitive endpoint |
| **INTERPRETATION_IF_NULL** | 🔴 **The most consequential result the portfolio could acquire.** Gene addition past the window is **symptomatic**, and `N-15` extends **from symptomatic levers to the causal lever itself**. `TX-007`'s `TIME-BUY 3` and the whole *"buy time"* rationale would need re-scoring, and the case for **pre-symptomatic or neonatal** administration becomes the only case |
| **INTERPRETATION_IF_POSITIVE** | The cognitive endpoint improves in the gene-therapy arms and **not** in the seizure-matched ASM arm ⇒ gene addition past the window is **disease-modifying**; `N-15` is bounded to symptomatic levers; the `PROMISING_BUT_GAP` half of Candidate F is promoted. **This is the only result in the entire package that would license the word *disease-modifying* for anything** |
| **MAIN_CONFOUND** | 🔴 **Matching SWD is not matching seizure burden.** SWD is an electrographic surrogate; two arms matched on SWD may differ in behavioural seizures, sleep architecture or subclinical burden — and ASMs have **direct cognitive effects of their own**, in both directions, which is a second uncontrolled variable pushing the comparison. Requires a vehicle-ASM arm and a cognitive-side-effect readout. Second: **a hypomorph is not a null**, and the timepoints must be anchored to a **measured developmental landmark** or the "window" is a species artefact. Third: this is by far the most expensive of the three and its arms depend on `E-1` and `E-2` |

> ### `TOP3_DISCRIMINATORS_STATUS: all three have informative nulls`
> **`E-1`** null collapses a node and settles two repair candidates · **`E-2`** null **closes an
> entire axis** and converts bumetanide from unrankable to closed · **`E-3`** null extends the
> portfolio's most constraining negative to the causal lever.
> **Dependency order: `E-1` and `E-2` before `E-3`**, whose arms they define.

---

## 7 · PHASE 9 — therapeutic overclaim sweep over the existing candidates

**Scope:** the candidate-bearing surfaces only — `therapeutic_strategies_current.md` (7 `TX` entries),
`therapy_levers.md`, and the map's `R-`/`N-` blocks. **No molecule is added; none is proposed.**

### 7.1 The overclaims found

| # | Site | Text | Pattern | Why |
|---|---|---|---|---|
| **O-1** | `therapy_levers.md` **Practical priority 2** | *"lithium as a preclinically-grounded **disease modifier** (GSK3β)"* | 🔴 **seizure control read as disease modification** | Lithium was tested on **one endpoint, once, acutely, as a pre-treatment**, in **all three genotypes**, with **zero** developmental endpoints — and the authors write that the developmental question *"remains to be studied"*. This sits in a section headed *"for clinical discussion"* |
| **O-2** | `therapy_levers.md` **A2** | *"GSK3β is **elevated** in cortex, hippocampus and cerebellum"* | **unmeasured target direction** | Neither cited source asserts abundance; the panel is `NOT_TESTED` (§3) |
| **O-3** | `therapy_levers.md` **A2** | *"the **strongest repurposing signal**"* | **seizure control read as WWOX rescue** | The strength is a general anticonvulsant effect; the WWOX-specificity test **failed in an assay of demonstrated sensitivity** |
| **O-4** | `therapy_levers.md` **C2** | *"**Proof** that restoring WWOX **reverses the phenotype**"* | 🔴 **ignores non-rescued endpoints** + global proposition | The organoid rescue is cellular and electrophysiological, and the paper registry's own record calls it *"ubiquitario, sovrafisiologico e **parziale**"*. *"Proof"* and *"reverses the phenotype"* are exactly the sentence §4 exists to make unavailable |
| **O-5** | `therapy_levers.md` **C1** | *"rescued Wwox-null mouse phenotypes — epilepsy, **hypomyelination**, lethality"* | **ignores non-rescued endpoints** | Myelin is `PARTIAL`, and on its only drawn WT-vs-rescued bracket it is **significant against the rescue** |
| **O-6** | `therapy_levers.md` line 12 | *"WWOX regulates myelination, network excitability and neuroinflammation — all time-dependent processes where **early intervention protects development**"* | 🔴 **seizure control read as disease modification** | The final clause asserts developmental protection, which is precisely what `CLAIM 031` denies and `N-15` forbids |
| **O-7** | `therapy_levers.md` **Practical priority 4** | *"AAV9-WWOX gene therapy (**already effective in mouse**)"* | **global proposition** | Effective **on four endpoints, at high dose, in the P0–P5 window** |
| **O-8** | `therapy_levers.md` **B1** | *"WWOX loss **activates** GSK3β"* stated as fact | **unmeasured / contested target direction** | The *in vivo* evidence is a pS9 western that `CLAIM 035` says must return a false negative (§3.4) |
| **O-9** | `TX-005` | *"lithium **abolishes** PTZ-induced seizures in Wwox-/-"*, `EVID 2` | **unmeasured target direction** | No genotype boundary; scored as a GSK3β-mechanism drug when the specificity test failed |
| **O-10** | `TX-007` | *"neonatal ICV → seizure/**myelin**/survival rescue"* | **ignores non-rescued endpoints** | As O-5 |
| **O-11** | `R-01` (map) | `KNOWN_MAJOR_SAFETY_CONSTRAINTS`: *"dose-limiting DRG/peripheral-ganglion toxicity"* | 🔴 **transferred evidence promoted as direct** | Review-sourced, **class-level** (PMID 42128308 §11), in a field otherwise reporting this vector's own measurements. **No DRG assessment exists in either WWOX paper** |
| **O-12** | `TX-007` scoring | `SAFETY 1–2` with no line for **supraphysiological expression** | **ignores a measured adverse quantity** | The same animal is **8.2× / 10.7× / 5.6×** WT in three regions and **1.4×** in the fourth; `CLAIM 028` says WWOX output is partner- and context-dependent, so *"more WWOX = better"* is not linear. **No immunological measurement appears in the locators** |

### 7.2 What is correctly bounded — reported so the sweep is not one-sided

| Site | Why it passes |
|---|---|
| **`TX-006`** | States the corrective explicitly: *"seizure control **must not be automatically counted as recovery of development or myelination**"*, and scores `TIME-BUY 2` with the parenthetical *"(benefit/safety, not demonstrated developmental recovery)"* |
| **`TX-007`** window caveat | *"neuronal GT rescues excitability/function but does **NOT** repair the progenitor defect… **not reversal of developmental damage**"*. **`TX-007` does not conflate seizure control with disease modification** — its defects are O-10 and O-12, which are different |
| **`therapy_levers.md` A1** | Vigabatrin: *"Symptomatic, **does not modify WWOX**"* |
| **`therapy_levers.md` B4** | Zfra: *"evidence is Alzheimer/cancer, **none in epilepsy/WOREE**. Experimental, indirect"* |
| **`TX-003`** | Carries an explicit retraction block: the ΔΔG heuristic and the P47T↔Q230P equivalence were withdrawn; *"G372R is a natural variant comparator, **not** a validated negative control"* |
| **`TX-001`** | Carries a **mandatory gate** before any modality choice |
| **`TX-004`** | *"'lower MYC/Wnt = better' is **NOT a safe default**"* |

> ### `THERAPEUTIC_OVERCLAIM_COUNT: 12` across 3 surfaces
> **By pattern, partitioned — each overclaim counted once, under the pattern that carries it:**
> seizure-control-as-disease-modification **3** (O-1, O-3, O-6) · transferred-evidence-as-direct
> **1** (O-11) · ignores-non-rescued-endpoints **5** (O-4, O-5, O-7, O-10, O-12) ·
> unmeasured-target-direction **3** (O-2, O-8, O-9). **3 + 1 + 5 + 3 = 12.**
> 🔴 **Eight of the twelve are in `therapy_levers.md`** — the most reader-facing document in the
> therapeutic chain and the one furthest from the locators; the remaining four are `TX-005` (1),
> `TX-007` (2) and the map's `R-01` (1). **Seven sites are correctly bounded**, including the tracker
> entry (`TX-006`) whose whole subject is the distinction.

---

## 8 · Closing blocks

> ### `THERAPEUTIC_REPAIR_CANDIDATE_COUNT: 6` — independently reviewable
> 3 MINOR (A, B, E) · 1 MAJOR (F) · 2 MAJOR? (C, D) → Mirror. Touching the four scientific current
> files: **C, D, F**. Ledger/tracker/analysis only: **A, B, E**.

> ### `MTOR_PROPAGATION_REPAIR: 2 sites · 0 canonical`
> `DL-MECH-034:691` re-tag · map `N-01` reword and demote. **The canonical layer never carried it**:
> `claim_registry`, `working_model`, `disease_model` and `state_manifest` return **0** mTOR-family
> hits. And across **238 files**, `rapamycin`/`sirolimus`/`everolimus` occur in **three files, all
> mine**.

> ### `CLAIM016_035_REPAIR_READY: YES` — 7 deltas, two sites
> `MISLOCATOR` **not** a bare `7b→7d` swap (the parenthesis bundles two observations and 7b is
> correct for one of them) · the **state manifest carries the identical defect** · `TOTAL_GSK3B` and
> `P-SER9` both **`NOT_TESTED`**, neither *"flat"* nor *"elevated"* · **no gene-dosage gradient in the
> heterozygote** · the blot age is **P14 or P20, unsettled by the paper** · and the S9-axis
> **mutual exclusion** stands.

> ### `AAV9_CANONICAL_MATRIX_READY: YES`
> 4 `RESCUE` · 1 `PARTIAL` · 5 `UNRESOLVED` (3 `NOT_MEASURED`) · 1 `UNRESOLVED` sub-endpoint.
> Every cell carries its **comparator** and its **statistical status**, and `RESCUE` is reserved for a
> drawn, null, treated-versus-wild-type comparison.

> ### `DISEASE_MODIFICATION_NEGATIVE_STATUS: ABSENT ON THE EXAMINED CORPUS — denominator declared`
> 207 files · 1 566 endpoint terms · 15 co-occurrences · **0 survivors**. Two positive controls
> (68 survival, 12 motor). Exclusion rules stated, including the `IQ` artefact that inflated the
> first pass from 15 to 41. **Not universal beyond the corpus; 356 records unread; no external search
> authorized.**

> ### `TOP3_DISCRIMINATORS_STATUS: all three nulls informative` · dependency order `E-1`, `E-2` → `E-3`

> ### `THERAPEUTIC_OVERCLAIM_COUNT: 12` · 8 in `therapy_levers.md`, 2 in `TX-007`, 1 in `TX-005`, 1 in map `R-01` · 7 sites correctly bounded

---

**Layer discipline.** This file modified no canonical file, promoted no hypothesis, named no new
molecule, formulated no clinical indication, dose, schedule or sequence of care, and designed no
sequence or construct. It corrects its own predecessors in two places (§3.3) and corrects a prior
adjudication of mine in one (§3.3a). Every count states its population and can be re-run. Every
molecule named anywhere in this chain is **material for discussion with a treating clinical team**,
and nothing here substitutes for one. **Not medical advice.**
