# COMMIT CANDIDATE — AAV9-hSynI-WWOX: the class attaches to an (endpoint × dose × window) triple, not to the intervention

**Candidate ID:** CC-20260826-AAV9-ENDPOINT-SPLIT-01
**Status:** proposed — not integrated, not committed
**Base head:** `b80ae8b`
**Receipts:** `FTR-20260814-42422765-06` (`complete_fulltext_read`, PMID 42422765, 29 locators) ·
`FTR-20260810-34747138-01` (`complete_fulltext_read`, PMID 34747138, 20 locators). Both depths
re-verified this session against the ledger.
**Author:** scientist-b

---

**CURRENT_TARGET**

| Record | Text |
|---|---|
| `CLAIM 004` (`consolidated baseline`) | *"Preclinical AAV9-WWOX rescue improves survival, hyperexcitability and myelin-related phenotype"* — **with a 2026-08-10 qualification already applied** |
| `CLAIM 011` (**`flagged for review`**) | *"rescue dose-dependent e durevole su: sopravvivenza, crescita, glucosio, **comportamento**, mielinizzazione, gliosi, ipereccitabilità / SWD"* |
| `TX-007` | *"neonatal ICV → **seizure/myelin/survival rescue**"* |
| map `R-01` | the **sole** entry in `READY_FOR_WWOX_PRECLINICAL_CONSIDERATION` |

**PROPOSED_DELTA**

Move the class from the **intervention** to the **(intervention × endpoint × dose × window)** triple.

- **Retain** `READY_FOR_WWOX_PRECLINICAL_CONSIDERATION` for **survival · SWD · gliosis**, at HD, in
  the P0–P5 window.
- **Downgrade to `PROMISING_BUT_GAP`** for **cognition · developmental trajectory ·
  myelin-in-the-dose-study · cerebellum · post-neonatal administration**.
- 🔴 **Reclassify MOTOR as `PARTIAL / NOT_NORMALISED`** — see the correction below.
- Qualify `comportamento` → **`comportamento locomotorio/motorio (nessun endpoint cognitivo
  misurato)`** in `CLAIM 011` and `CLAIM 004`, with a one-line boundary naming `CLAIM 031`.
- Re-label `R-01`'s DRG statement **TRANSFERRED (T4/T5)**.

---

**🆕 ADMINISTRATIVE_SEVERANCE — Part 1 is MINOR and must not wait for Part 2**

🔴 **This candidate contains two deltas with different authorities, and bundling them subordinates
the cheap one to the expensive one.** They are severed here so Plan can route them apart.

| | **PART 1 — administrative** | **PART 2 — scientific** (everything above and below) |
|---|---|---|
| **What it does** | deletes one **false clause about read depth** from `CLAIM 011`'s flag and records the discharge | narrows a readiness class by (endpoint × dose × window) |
| **Change class** | **MINOR** | **MAJOR** (fail-closed) |
| **Mirror** | **not required** — no epistemic/method question, no doubtful MAJOR (H.1) | **required** (H.1, fail-closed) |
| **Operator** | **not required** — the human gate is *MAJOR approval* (H.1) | **required** (H.1) |
| **Blocks on** | **nothing** | Mirror, then the Operator |

**PART 1 target:** `claim_registry_current.md#CLAIM 011`, **final sentence of the 🔴 flag block**.
Verified present exactly once at `bf88c1a`.

> **Current (verbatim):** *…e la lettura che li risolverebbe è `partial_fulltext_read`.*

> **Proposed:** *✅ **Condizione di rinvio assolta il 2026-08-14** — `FTR-20260814-42422765-06`,
> `complete_fulltext_read`, 29 locator (16 attestazioni di figura, 13 snippet di corpo). La lettura
> completa esiste; i tre domini sono risolti **e non tutti nella stessa direzione**, quindi la
> riscrittura resta **scientificamente aperta** ed è tracciata in questo candidate.
> **Il rinvio non è più un blocco di completezza di lettura.***

🔴 **The record contradicts itself today and has for twelve days.** Two lines apart: the flag says
the resolving read is `partial_fulltext_read`; `**Full text status:**` says *"complete article plus
S1–S8 — latest receipt `FTR-20260814-42422765-06`"*. A reader cannot tell which of its own two lines
to believe.

**What Part 1 deliberately does NOT do:** change `Status: flagged for review` (the record **is**
still under scientific review) · touch the `Summary` line (`comportamento`, `mielinizzazione`,
`dose-dependent` are all Part 2) · assert any endpoint verdict · touch `CLAIM 004`, `TX-007` or
`R-01` · bump `working_model_version`.

It still requires a `BATCH_COMMIT`, because `claim_registry_current.md` is one of the four
scientific current files and there is no lesser route into it.

---

**CHANGE_CLASS:** **MAJOR** *(Part 2; **Part 1 is MINOR** — see the severance above)* — narrowing a readiness class in `P7 — gene therapy readiness`, on two
records of which one is `consolidated baseline` with `clinical relevance: HIGH`. Classified
fail-closed; Mirror may downgrade it, and that is Mirror's call, not mine.

**CANONICAL_TARGETS:** `claim_registry_current.md#CLAIM 004` and `#CLAIM 011` — **two of the four
scientific current files; `BATCH_COMMIT` only.** Secondary, non-batch:
`therapeutic_strategies_current.md#TX-007`, `mechanism_intervention_map.md` `R-01`,
🆕 `therapy_levers.md` **C1** and **Practical priority 4**.

**🆕 D-L1, D-L2 — the two `therapy_levers.md` `GLOBAL_RESCUE` sites, homed here**

A carrier audit found that **five of the eight `therapy_levers.md` overclaims had no routable
carrier**. Two are AAV9 global-rescue claims and belong to this candidate.

| # | Target | Current text (verified verbatim at `bf88c1a`) | Delta |
|---|---|---|---|
| **D-L1** | **C1**, line 28 | *"rescued Wwox-null mouse phenotypes — epilepsy, **hypomyelination**, lethality"* | *"…improved **survival and epileptiform activity**, and improved myelination **on the comparisons the study draws**. 🔴 On the single panel where treated animals are compared with wild type — unmyelinated axons per field, WT ≈26 vs treated ≈52 — the comparison is **significant against the rescue**; on the remaining myelin panels the wild-type-versus-treated comparison is **not drawn**, so the residual gap is `NOT_TESTED`"* |
| **D-L2** | **Practical priority 4**, line 42 | *"AAV9-WWOX gene therapy (**already effective in mouse**)"* | *"AAV9-WWOX gene therapy — effective in mouse **on survival, spike-wave discharges and gliosis, at high dose, in the P0–P5 window**; **motor and locomotor behaviour is not impaired and not normalised**; cognition and developmental trajectory were **not measured**"* |

⚠️ **D-L2's content depends on `bf88c1a`.** Before the MOTOR correction its endpoint list would have
read *"survival, spike-wave discharges, motor and gliosis"* — **four endpoints, one of them wrong.**
It is the one edit in the eight whose correctness is a function of which commit it is written at.

⚠️ **D-L1 PRESERVATION CONSTRAINT:** C1's closing sentence — *"By replacing functional WWOX in
neurons, it bypasses any allele combination"* — is a correctly-bounded mechanism statement and must
survive byte-for-byte. The replacement text drops the word *"rescued"* and the word *"partially"*
alike: **the first is a global verb, the second is a magnitude claim over panels where the
comparison is not drawn.**

**Both are analysis-layer, `MINOR`, and require no `BATCH_COMMIT`** — they are severable from Part 2
in exactly the way Part 1 is, and are listed here for ownership rather than for bundling.

---

**DIRECT_EVIDENCE — the endpoint matrix, with comparator and statistical status per cell**

| Endpoint | Measured | Comparator drawn | Statistical status | Verdict |
|---|---|---|---|---|
| **SURVIVAL** | quantified | WT · KO · four doses | Kaplan–Meier | **`RESCUE`** at HD (~75–80% to d300) · **`NO_RESCUE`** at LD and below. 🔴 threshold has **no measured expression correlate** — 7/8 dose comparisons `ns`; the paper's explanation is **survivor-conditioned** |
| **SWD** | quantified | WT-vs-KO · KO-vs-HD · **WT-vs-HD** | `****` · `****` · **`ns`** | **`RESCUE`** — the decisive bracket exists and is null |
| *(spikes/day, same figure)* | quantified | WT-vs-KO | 🔴 **`p = 0.2000` printed on the panel face**, n=5/group, no asterisk, no `ns` | **`UNRESOLVED`** — the text calls it *"a significant elevation"* |
| **MOTOR** | quantified | 🔴 **WT-vs-treated drawn in all eight panels of Figure 4** (n=9 WT+RI vs 10 KO+W HD), plus the S4 dose-graded composite | S4: WT-vs-HD `ns`. **Figure 4: 3 of 8 panels `*`** — velocity WT ≈9.5 → HD ≈11.5 · distance WT ≈3 400 → HD ≈4 300 · rotarod latency WT ≈85 s → HD ≈145 s. Four anxiety measures `ns`. **No multiplicity correction declared across 8 comparisons** | 🔴 **`PARTIAL / NOT_NORMALISED`** — see correction below |
| **GLIOSIS** | quantified | **WT-vs-KO and WT-vs-treated** (S8I) | `***` · **`ns`** | **`RESCUE`** at HD. 🔴 **`NO_RESCUE` at LD** — S7H: LD significantly worse than WT (`**`), HD `ns` |
| **MYELIN** *(dose study)* | ⚠️ qualitative only | **none** — Fig. 6F, S7I, S8G are representative images; the only MBP quantification (6E) has **no treated arm** | none | 🔴 **`UNRESOLVED`** — the text claims *"near-complete rescue across affected regions"* |
| **MYELIN** *(2021 paper)* | quantified | **WT-vs-KO and KO-vs-rescued — never WT-vs-rescued**, except one panel | brackets drawn are `***`/`**`/`*`; **the residual gap is untested** | **`PARTIAL`**. 🔴 On the **one** panel where WT-vs-rescued **is** drawn — unmyelinated axons/FOV, **WT ~26 vs treated ~52, `**`** — it is **significant against the rescue**. CC1⁺ 170/77/135 · PDGFRα⁺ 53/87/70 · myelinated axons CC 130/46/105, optic nerve 140/68/124. g-ratio normalises. n = 3 |
| **CEREBELLUM** | ⚠️ measured only as a **distribution compartment** | WT | quantified | 🔴 **`NO_RESCUE`** on transduction · **`UNRESOLVED`** on function. Below WT at P30 (Fig. 5L); at P300 **1.4× WT** vs cortex 8.2×, hippocampus 10.7×, midbrain 5.6×; S6D prints cerebellum **0**. The same model carries locatored **foliation defects in lobules V, VI and VII, Purkinje ~18 vs ~7 per area** (`FTR-20260804-32000863-01` entry 12) |
| **COGNITION** | 🔴 **`NOT_MEASURED`** | — | — | **`UNRESOLVED`.** 49 locators across both papers; **no cognitive assay** |
| **DEVELOPMENT** | 🔴 **`NOT_MEASURED`** | — | — | **`UNRESOLVED`.** ⚠️ weight and glucose at P14 are `ns` vs WT — **growth and metabolic** endpoints, not developmental |
| **POST_NEONATAL** | 🔴 **`NOT_MEASURED`** | — | — | **`UNRESOLVED`.** Declared **explicitly future work** in both papers. Within the window the 300-day panel shows only **P1 and P5**; P2–P4 exist only in the 40-day panel and **P3 is an n=3 arm that lost animals** |

---

**🔴 CORRECTION TO MY OWN PRIOR MATRIX — MOTOR was recorded as `RESCUE` and it is not**

`therapeutic_repair_candidates.md` §3 and `therapeutic_canonical_repair_package.md` §4 both record
MOTOR as **`RESCUE` at HD**, citing S4A's `ns` against wild type. **That is incomplete in the
direction favourable to the therapy, which is the direction this whole chain exists to catch.**

`fulltext_dossiers/PMID42422765_partial_locators.md` — on my own branch, and not consulted when
those two files were written — records Figure 4 (`gr4.jpg`, sha256 `4bfa9eef…d566d6d`, 104 ppi):
**eight quantified panels, and the WT-versus-treated comparison is drawn in every one.** Three are
significant, and **in all three the treated animals do not match wild type — they exceed it.**

**A significant difference from wild type is not normalisation, and its direction does not change
that.** Three readings are open and this candidate chooses none:

- **hyperactivity** — increased velocity and distance in an open field with all four anxiety
  measures `ns` is the classic locomotor signature, not restored normality;
- **overshoot from overexpression** — consistent with the 8.2× / 10.7× / 5.6× / 1.4× WT protein at
  P300 and 9–19× hippocampal protein at P90;
- **marginal statistics** — three `*` at n ≈ 10, **unadjusted across eight comparisons in one
  figure**, all at the weakest significance level.

**What is genuinely reassuring, and is the actual result:** anxiety-related behaviour is
indistinguishable from wild type on four independent measures, and motor coordination is at least as
good. **The therapy does not produce an anxious or motor-impaired animal.** That is real and useful.
It is not what *"normalizes"* claims, and it is not `RESCUE` in the sense this matrix reserves.

⇒ **MOTOR moves from `RESCUE` to `PARTIAL / NOT_NORMALISED`**, and the `RESCUE` count for this
intervention falls from four endpoints to **three**.

**🆕 HARDENING — the behavioural endpoints, split motor from anxiety and re-measured**

**Denominator first.** Behavioural evidence exists in **one** of the two studies: PMID 42422765
carries **2** behavioural locators (Fig. 4, 8 panels; S4A, 1 measure); PMID 34747138 carries
🔴 **0** across its 20 entries. ⇒ **9 quantified measures, one dose (HD), 8 of 9 at one timepoint.**

🔴 **`treated vs disease` is `STRUCTURALLY_UNAVAILABLE` for every P90 behavioural endpoint.** Fig. 4
has two groups — `WT+RI` n=9 and `KO+W HD` n=10. There is no untreated-KO arm and there cannot be
one: *"LD-treated mice did not survive to P90; therefore, analyses were limited to WT and HD-treated
groups"* (entry `[11]`), and untreated KO animals are dead by **~P17** (Fig. 2B, entry `[14]`).
**The only comparison the design permits is against wild type, and that is the one that comes out
significant.** This is not a drawing omission of the myelin kind — it is a property of the disease.

**MOTOR — 4 measures, 3 significant against WT, all in the exceed direction**

| # | Endpoint | Panel | vs disease | vs WT | Direction | Result | Multiplicity | Overshoot | *"Normalised"*? |
|---|---|---|---|---|---|---|---|---|
| M1 | open-field **velocity** | 4D | 🔴 `STRUCTURALLY_UNAVAILABLE` | drawn | **↑ exceed** 9.5→11.5 | **`*`** | 🔴 1 of 8, uncorrected | ≈**1.21×** | 🔴 **NO** |
| M2 | open-field **distance** | 4E | 🔴 `STRUCTURALLY_UNAVAILABLE` | drawn | **↑ exceed** 3 400→4 300 | **`*`** | 🔴 1 of 8, uncorrected | ≈**1.26×** | 🔴 **NO** |
| M3 | **rotarod** latency | 4K | 🔴 `STRUCTURALLY_UNAVAILABLE` | drawn | **↑ exceed** 85 s→145 s | **`*`** | 🔴 1 of 8, uncorrected | ≈**1.71×** | 🔴 **NO** |
| M4 | EPM velocity | 4F–4J | 🔴 `STRUCTURALLY_UNAVAILABLE` | drawn | none detected | `ns` | same figure | — | `NO_DIFFERENCE_DETECTED` |
| M5 | S4A four-arm measure | S4A | ⚠️ KO arm present (≈3.6 vs WT ≈0); **bracket `NOT_RECORDED`** | drawn | HD ≈0.3 vs WT ≈0 | `ns` WT-HD; `***` LD-HD | not stated | — | `NO_DIFFERENCE_DETECTED` |

**ANXIETY — 4 measures, kept separate, 4/4 `ns`**: open-field centre-zone frequency · open-field
periphery frequency · EPM open-arm duration · EPM closed-arm duration. All `STRUCTURALLY_UNAVAILABLE`
against disease, all drawn against WT, none significant.
⚠️ **`NO_DIFFERENCE_DETECTED`, not `NORMALISED`** — `ns` is the absence of a detected difference, not
an equivalence result; **no equivalence margin and no power analysis is declared** at n = 9/10.
**The therapy does not produce an anxious animal. It has not been shown to produce a wild-type
one.**

⚠️ **The bundling is the overclaim.** The paper's summary sentence claims outcomes
*"indistinguishable from WT … encompassing locomotor activity, anxiety-related behavior, and motor
coordination"*. **Anxiety is 4/4 `ns`; locomotor is 2/3 significant; motor coordination is
significant** — and the same paragraph acknowledges the third two sentences earlier
(*"significantly higher motor coordination and learning compared with WT mice (Figure 4K)"*).

🔴 **Overshoot — what the evidence discriminates, and what it does not.** This candidate asserts no
single explanation, but the three readings do **not** fare equally:

- **noise / marginal statistics** — ⚠️ **partially disfavoured for M3 only** (≈1.71× is a poor fit
  for a threshold artefact). **Not disfavoured for M1 and M2**, which sit exactly where a `*` at
  n ≈ 10 in an uncorrected family of eight would fall. ⇒ **the three positives do not stand or fall
  together**;
- **hyperactivity** — explains M1 and M2; 🔴 **fails to explain M3** (hyperactive animals are not
  thereby better at motor learning);
- **overexpression overshoot** — *consistent* with 8.2×/10.7×/5.6×/1.4× WT protein, but
  **consistency is not discrimination**. The test is a dose–expression–endpoint relation **within**
  treated animals, and it 🔴 **cannot be run in this dataset** because LD does not reach P90.

⇒ **The failure to discriminate is structural, not incidental** — the same fact that removes the
`treated vs disease` arm. **One arm removes both limitations:** an intermediate dose with a
per-animal expression readout, carried to P90 with the full Fig. 4 battery. It discharges this
candidate's fifth revival trigger **and** `CLAIM 011`'s existing one — **two triggers, one arm**,
and neither was written knowing about the other.

**Three status words this candidate distinguishes and the earlier matrices did not:**
`NOT_TESTED` (comparison never drawn — the **paper's** gap) · `NOT_REPORTED` (drawn, no result
printed — the **paper's** gap) · 🆕 `NOT_RECORDED` (drawn and printed, **our locator missed it** —
**our** gap, repairable by re-reading) · 🆕 `STRUCTURALLY_UNAVAILABLE` (the arm cannot exist).
**M5's KO bracket is `NOT_RECORDED` and should be closed by a re-read before Part 2 reaches Mirror.**

---

**LOCATORS**

`deepdive_manifests/PMID42422765.json` (29 entries; [0] text-vs-panel on Fig. 4D/E, [3] the
`p = 0.2000` panel, [6] the unquantified myelin panels, [9] the S8I gliosis baseline, [12] the
expression/threshold mismatch, [27] the S4 dose-graded motor result, [28] the P300 fold-changes) ·
`deepdive_manifests/PMID34747138.json` (20 entries; [9] and [10] the myelin quantifications and their
missing WT-vs-rescued brackets, [13] the ketamine caveat) ·
`fulltext_dossiers/PMID42422765_partial_locators.md`, Figure 4 section, artifact `gr4.jpg`
sha256 `4bfa9eefa0e9eae4ccc12c97894c7044419785e63b8128952377a97d4d566d6d`.

**TRANSFER_BOUNDARY**

🔴 **One piece is currently mislabelled as direct and this candidate re-labels it.** `R-01`'s
`KNOWN_MAJOR_SAFETY_CONSTRAINTS` asserts *"dose-limiting DRG/peripheral-ganglion toxicity at high
systemic dose"* in a field otherwise reporting this vector's own measurements. **No DRG assessment
exists in either WWOX paper.** The source is a **review, at class level** (PMID 42128308 §11), on
*"high-dose AAV administration"* as *"a key regulatory concern in pediatric CNS gene therapy
programs"*. ⇒ **TRANSFERRED (T4/T5)**, and it must be labelled as such.

The genuinely WWOX-measured PNS fact is different and more specific: **the neuron-specific construct
reaches the sciatic nerve** — a **biodistribution** finding, not a toxicity finding, from a blot with
no quantification and visibly variable band intensity across seven high-dose animals.

⚠️ **And a quantity currently absent from `TX-007`'s scoring:** the same animal is **8.2× / 10.7× /
5.6×** WT in three regions and **1.4×** in the fourth. `CLAIM 028` holds that WWOX output is partner-
and context-dependent, so *"more WWOX = better"* is not linear. **No immunological measurement
appears in the locators** — no anti-capsid or anti-transgene response, no complement, no DRG
histopathology.

**THERAPEUTIC_EFFECT**

🔴 **`R-01` still ranks first and nothing is close.** What it no longer does is rank first **on
disease modification**, because nothing in the portfolio has been measured there. **A downgrade in
scope, not in rank.** The previous class name asserted a readiness the developmental column does not
support, and `R-01` was the *only* entry in that class — so the class name was doing the portfolio's
ranking by itself.

**Canonical-language alternatives** (concise enough for a claim Summary, and constructed so the
global sentence cannot be reassembled from them):

> **Demonstrated rescue** — *"At high dose in the P0–P5 window, AAV9-hSynI-WWOX produces a
> wild-type-equivalent result on **survival, spike-wave discharges and astrogliosis**, each with the
> treated-versus-wild-type comparison **drawn and non-significant**."*
>
> **Partial rescue** — *"**Myelination** is partially restored; on the single panel where treated is
> compared with wild type the comparison is **significant against the rescue**. **Motor and
> locomotor behaviour** is not impaired and not normalised: three of eight panels differ
> significantly from wild type, in the exceed direction, unadjusted for multiplicity."*
>
> **Unresolved** — *"**Myelination in the dose study**, the **cerebellum** and one of the two
> electrographic endpoints are unresolved: the measurement exists but its comparator, its statistics
> or its quantification does not."*
>
> **Not measured** — *"**Cognition, developmental trajectory and post-neonatal administration have
> not been measured in either study.**"*
>
> **The closing constraint** — *"No statement of the form 'the phenotype is rescued' is supported:
> the class attaches to an (endpoint × dose × window) triple and not to the intervention."*

**REVIEW_REQUIRED:** **Mirror** (MAJOR classification) → Plan (integration) → **Orchestrator**
(batch; `CANONICAL_BATCH_COMMIT` is the Orchestrator's alone, lease ACTIVE).

**HUMAN_GATE:** ⚠️ **Yes — operator.** MAJOR approval is the operator's under Annex H.1, and `TX-007`
is the tracker's north star with a first-in-human compassionate case reported at news level.
**Nothing in this candidate is a clinical recommendation, and no dose, schedule or sequence of care
is formulated anywhere in it.**

---

**REVIVAL_TRIGGER** *(for the downgraded arms — the negative must not become dogma)*

*Promote the `PROMISING_BUT_GAP` arms on: **any** endpoint in the `DEVELOPMENTAL_TRAJECTORY` or
`COGNITION` column, in any WWOX model, under any intervention, **with a seizure-matched comparator
arm** (the design of `E-3`); **quantified MBP in a treated arm** of the dose study with the
WT-versus-treated bracket drawn; a **cerebellum-transducing route or capsid** with a motor/ataxia
endpoint; **post-natal dosing** at any timepoint beyond P5; and an **intermediate dose** between
1.23 and 2.63 × 10¹¹ vg **carrying an expression readout** — a third dose without one would
reproduce the existing gap.*

**Target WM:** MAJOR bump if committed as classified — declared at batch time.
**Batch gate:** intentionally untouched.
