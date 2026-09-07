# Therapeutic Routing and Endpoint Hardening — CLAIM 011 first, the behavioural split, and four repairs re-measured

**The fifth file in the therapeutic chain, and the first one that routes rather than analyses.**
It answers one question the four before it left open: *given seven commit candidates and a
`flagged for review` record with a discharged blocker, what moves first, and what must not move
with it?*

> **Status:** non-canonical analysis artefact. **READ-ONLY toward every canonical file** — no
> canonical edit was made by this file or proposed as an edit *from* it; the routable objects remain
> the seven `CC-20260826-*` candidates in [`../research/commit_candidates/`](../research/commit_candidates/).
> **Nothing here is medical advice, and no clinical recommendation is made or withdrawn.**
>
> **Measurement base:** branch `lettore-b` @ `bf88c1a`, **0 behind / 21 ahead** of `main` (`788c357`),
> re-derived at the head of this session, not inherited. `legend_lint.py` → **PASS**.
> `fulltext_receipts.py verify` → **`OK: 128 chained receipt(s)`**.

---

## 0 · What moved, in one table

| # | Object | Verdict this session |
|---|---|---|
| **B1** | `CLAIM 011` routing | 🆕 **Severed into two independently routable parts.** The administrative part is **MINOR** and needs neither Mirror nor the Operator; the scientific part stays **MAJOR** and needs both. Severance is the whole finding |
| **B2** | AAV9 behavioural endpoints | 🆕 **The treated-vs-disease comparison does not exist for any P90 behavioural endpoint and cannot** — untreated KO animals die at ~P17. **Motor 3/4 significant against WT · anxiety 4/4 `ns`** |
| **B3** | `therapy_levers.md` × 8 | ✅ **All eight locators verify verbatim at `bf88c1a`.** 🔴 **Five of the eight repairs had no object able to carry them into a batch** — four are homed here, two are orphaned to Plan. Two of the proposed edits **themselves** violate the B5 statistical rule and are re-worded |
| **B4** | mTOR propagation | 🔴 **The site count was wrong: 4, not 2.** One asserting block was never named by any artefact — and it carries the file's strongest wording |
| **B5** | `CLAIM 016` / `CLAIM 035` | 🔴 Mislocator **confirmed** (`7b → 7d`), and **the map's own corrections table asserts flatness without a test** and **still lists `motor` as a retained rescue endpoint** — that row was written at `6d43503`, **four commits before** the MOTOR correction landed at `bf88c1a`, and was not revised by it |
| **B6** | Candidate ledger | ✅ **23/23 target strings verify at `bf88c1a`.** 🔴 One candidate's declared negative is stale, and **one ledger row I wrote this session was wrong on three cells** |
| **B7** | Discriminators | 🆕 A **fourth** discriminator emerges from B2 and discharges **two** existing revival triggers with one arm |

---

## 1 · B1 — `CLAIM 011`: the deferral is administrative, the biology is not

### 1.1 The distinction, applied to the record rather than restated

`CLAIM 011` has been `flagged for review` since 2026-08-10. The flag defers its own rewrite on a
stated precondition:

> *"Riscrittura rinviata: la Figura 3B risolve sopravvivenza e glicemia, **non** gli altri domini
> della claim (ECoG/SWD, mielinizzazione, gliosi), e la lettura che li risolverebbe è
> `partial_fulltext_read`."*

**The precondition is a fact about read depth. It has been false since 2026-08-14.**
`FTR-20260814-42422765-06` records `evidence_depth: complete_fulltext_read` at
`analysis_at: 2026-08-14T14:20:05`; the manifest `deepdive_manifests/PMID42422765.json` carries
**29 entries** — re-counted this session, not taken from the handoff — of which **16 are figure
attestations and 13 body snippets**.

🔴 **The record contradicts itself, and has for twelve days.** Two lines apart, in the same claim:

| Line | Text | Status |
|---|---|---|
| Flag block | *"la lettura che li risolverebbe è `partial_fulltext_read`"* | **false since 2026-08-14** |
| `**Full text status:**` | *"complete article plus S1–S8 — latest receipt `FTR-20260814-42422765-06`"* | **correct** |

A record that states both is not merely stale — it is **unciteable in either direction**, because a
reader cannot tell which of its own two lines to believe.

### 1.2 The severance, which is the actual deliverable

The queue's instruction — *do not reopen scientific questions merely because an administrative flag
is stale* — has a structural consequence that had not been drawn: **the two halves of `CLAIM 011`'s
repair have different authorities, and bundling them subordinates the cheap one to the expensive
one.** Under `governance/annex_h_authority_matrix.md` H.1:

| | **PART 1 — administrative** | **PART 2 — scientific** |
|---|---|---|
| **What it does** | deletes one false clause about read depth; records the discharge | narrows a readiness class by endpoint × dose × window |
| **Change class** | **MINOR** | **MAJOR** (fail-closed) |
| **Mirror** | **not required** — no epistemic/method question, no doubtful MAJOR | **required** — *"Classificazione MAJOR dubbia → Mirror (fail-closed)"* |
| **Operator** | **not required** — *"MAJOR approval"* is the human gate, and this is not MAJOR | **required** — *"Spese / MAJOR approval / governance → Operatore"* |
| **Plan** | required (integration) | required |
| **Orchestrator** | required (`CANONICAL_BATCH_COMMIT`, lease ACTIVE) | required |
| **Carrier** | 🆕 `CC-20260826-AAV9-ENDPOINT-SPLIT-01` **§ADMINISTRATIVE_SEVERANCE** | the same candidate's main body |
| **Blocks on** | nothing | Mirror, then the Operator |

⇒ **Part 1 can clear while Part 2 waits.** That is the routing decision, and it is the only thing in
this section that is new. Bundled, the false read-status clause stays in a `clinical relevance: HIGH`
record in `P7` for as long as a MAJOR gate takes; severed, it clears on the next batch.

### 1.3 The minimum delta — one clause, no proposition about biology

**Target:** `claim_registry_current.md#CLAIM 011`, final sentence of the 🔴 flag block.
**Verified present at `bf88c1a`**, exactly once.

**Current (verbatim):**

> *…e la lettura che li risolverebbe è `partial_fulltext_read`.*

**Proposed replacement:**

> *✅ **Condizione di rinvio assolta il 2026-08-14** — `FTR-20260814-42422765-06`,
> `complete_fulltext_read`, 29 locator (16 attestazioni di figura, 13 snippet di corpo). La lettura
> completa esiste; i tre domini sono risolti **e non tutti nella stessa direzione**, quindi la
> riscrittura resta **scientificamente aperta** ed è tracciata in
> `CC-20260826-AAV9-ENDPOINT-SPLIT-01`. **Il rinvio non è più un blocco di completezza di lettura.***

**What this delta deliberately does NOT do — each one is a live temptation the severance exists to refuse:**

| Not done | Why |
|---|---|
| ❌ change `Status: flagged for review` | the record **is** still under review. Scientifically, not administratively |
| ❌ touch the `Summary` line | that is Part 2. `comportamento`, `mielinizzazione` and `dose-dependent` all sit there |
| ❌ assert any endpoint verdict | no `RESCUE`, no `PARTIAL`, no `NOT_MEASURED` appears in the delta |
| ❌ touch `CLAIM 004`, `TX-007` or map `R-01` | those are Part 2's targets |
| ❌ bump `working_model_version` | no disease-model proposition changes |

**Change class: MINOR.** It removes a false statement of fact about a ledger, and adds a true one.
It reverses no baseline claim and redefines no block. It nonetheless requires a `BATCH_COMMIT`,
because `claim_registry_current.md` is one of the four scientific current files and there is no
lesser route into it.

### 1.4 The split, item by item — routes, not verdicts

**`ADMINISTRATIVELY_STALE`** — someone must act; no experiment is implied:

| Element | Why it is administrative |
|---|---|
| the deferral clause itself | its stated precondition has been false for twelve days |
| **ECoG / SWD** | resolved by the complete read — `RESCUE` at HD, WT-vs-HD bracket drawn and `ns` (Fig. 7E). Unwritten, not unknown |
| **Gliosis** | resolved — `RESCUE` at HD (S8I, WT-vs-treated `ns`), **`NO_RESCUE` at LD** (S7H, LD worse than WT, `**`) |
| **`comportamento`** | the word denotes locomotor/motor behaviour only. Qualifying it needs **no new data** |
| **`dose-dependent`** | the flag itself established the threshold reading; carrying it into the other domains needs **no new data** |

**`SCIENTIFICALLY_UNRESOLVED`** — no amount of re-reading closes these:

| Element | Why re-reading cannot close it |
|---|---|
| **Myelination (dose study)** | three representative panels, no statistics; the only MBP quantification (6E) has **no treated arm**. The measurement was not made |
| **Spikes/day** | `p = 0.2000` printed on the panel face against *"a significant elevation"* in the text. Needs the underlying data or a repeat |
| **Survival threshold ↔ expression** | 7/8 dose comparisons `ns`; the paper's explanation is survivor-conditioned. Needs an intermediate-dose arm **with an expression readout** |
| **Motor** | 3 of 8 Figure 4 panels significant against WT in the exceed direction, unadjusted. §2 below |
| **Cognition · development · post-neonatal** | **never measured.** No assay exists in either study |

> ### `CLAIM011_ROUTING: SEVERED — PART 1 MINOR (unblocked) · PART 2 MAJOR (Mirror → Operator)`
> **5 stale · 5 unresolved.** The stale set is cleared by **one clause**; the unresolved set is
> cleared by **experiments**, three of which §7 specifies.

---

## 2 · B2 — the AAV9 behavioural endpoints, split and hardened

### 2.1 The denominator, before the table

**Behavioural evidence for AAV9-hSynI-WWOX exists in one of the two studies.** Re-derived this
session from both manifests:

| Study | Entries | Behavioural entries |
|---|---|---|
| PMID **42422765** (dose/window, 2026) | 29 | **2** — Figure 4 (`[0]`, 8 panels) and Supplementary S4 (`[27]`, 1 measure) |
| PMID **34747138** (2021 companion) | 20 | 🔴 **0** — no locator in the companion touches behaviour, motor or anxiety |

⇒ **9 quantified behavioural measures in total, all from one paper, all at one dose (HD), and 8 of
the 9 at one timepoint (P90).**

### 2.2 🔴 The structural finding: the rescue comparison does not exist and cannot

Figure 4 has **two groups**: `WT+RI` (n = 9) and `KO+W HD` (n = 10). There is no untreated-KO arm —
and there cannot be one, because the paper states it in plain text:

> *"LD-treated mice did not survive to P90; therefore, analyses were limited to WT and HD-treated
> groups"* — manifest entry `[11]`, Results, behaviour section

and untreated `KO+RI` animals are dead by **~P17** (Figure 2B, entry `[14]`).

⇒ **For every P90 behavioural endpoint, `treated vs disease` is `STRUCTURALLY_UNAVAILABLE`.** This
is not a drawing omission of the kind the myelin panels show — it is a consequence of the disease
being lethal before the assay. **The only comparison the design permits is against wild type, and
that is the comparison that comes out significant.** A reader who expects "treated better than
untreated" to be the evidence for behavioural rescue will not find it anywhere, in either paper, at
any dose.

### 2.3 MOTOR endpoints — four measures

*Direction convention: **↑ exceed** = treated value above wild type on that axis.*

| # | Endpoint | Panel | treated vs **disease** | treated vs **WT** | Direction | Statistical result | Multiplicity | Overshoot | *"Normalisation"* justified? |
|---|---|---|---|---|---|---|---|---|
| M1 | Open-field **velocity** | 4D | 🔴 `STRUCTURALLY_UNAVAILABLE` | **drawn** | **↑ exceed** (≈9.5 → ≈11.5) | **`*` (p < 0.05)** | 🔴 1 of 8 in-figure, **uncorrected** | **≈ 1.21×** | 🔴 **NO** |
| M2 | Open-field **total distance** | 4E | 🔴 `STRUCTURALLY_UNAVAILABLE` | **drawn** | **↑ exceed** (≈3 400 → ≈4 300) | **`*` (p < 0.05)** | 🔴 1 of 8, **uncorrected** | **≈ 1.26×** | 🔴 **NO** |
| M3 | **Rotarod** latency to fall | 4K | 🔴 `STRUCTURALLY_UNAVAILABLE` | **drawn** | **↑ exceed** (≈85 s → ≈145 s) | **`*` (p < 0.05)** | 🔴 1 of 8, **uncorrected** | **≈ 1.71×** | 🔴 **NO** |
| M4 | Elevated-plus-maze **velocity** | 4F–4J | 🔴 `STRUCTURALLY_UNAVAILABLE` | **drawn** | none detected | **`ns`** | same figure | — | ⚠️ **`NO_DIFFERENCE_DETECTED`**, not equivalence |
| M5 | S4A four-arm motor measure | S4A | ⚠️ `NOT_RECORDED` — KO arm **present** (≈3.6 vs WT ≈0), **bracket not recorded in the locator** | **drawn** | HD ≈0.3 vs WT ≈0 | **`ns`** (WT-vs-HD); **`***`** LD-vs-HD | not stated | — | ⚠️ `NO_DIFFERENCE_DETECTED` |

> ### `MOTOR: PARTIAL / NOT_NORMALISED` — **3 of 4 P90 motor measures differ significantly from wild type, all in the exceed direction.**
> `RESCUE` is unavailable for this domain for two independent reasons: the sufficiency comparison is
> significant where it is drawn, and the rescue comparison is structurally undrawable.

**Three status words, deliberately distinguished** — the earlier files used two:

| Status | Meaning | Owner of the gap |
|---|---|---|
| `NOT_TESTED` | the comparison was never drawn | the **paper** |
| `NOT_REPORTED` | drawn, but no result printed | the **paper** |
| 🆕 `NOT_RECORDED` | drawn and printed, but **our locator did not capture it** | 🔴 **us** — repairable by re-reading |
| 🆕 `STRUCTURALLY_UNAVAILABLE` | the arm cannot exist in this design | **neither** — it is a property of the disease |

M5's KO bracket is `NOT_RECORDED`, and that is **our** defect, not the paper's. It is the one cell in
this table a re-read could close, and it should be closed before Part 2 goes to Mirror.

### 2.4 ANXIETY endpoints — four measures, kept separate

The paper bundles these with motor into one sentence. They behave differently and must be reported
apart.

| # | Endpoint | treated vs **disease** | treated vs **WT** | Direction | Statistical result | Overshoot | Verdict |
|---|---|---|---|---|---|---|
| A1 | Open-field **centre-zone frequency** | 🔴 `STRUCTURALLY_UNAVAILABLE` | **drawn** | none detected | **`ns`** | — | `NO_DIFFERENCE_DETECTED` |
| A2 | Open-field **periphery frequency** | 🔴 `STRUCTURALLY_UNAVAILABLE` | **drawn** | none detected | **`ns`** | — | `NO_DIFFERENCE_DETECTED` |
| A3 | EPM **open-arm duration** | 🔴 `STRUCTURALLY_UNAVAILABLE` | **drawn** | none detected | **`ns`** | — | `NO_DIFFERENCE_DETECTED` |
| A4 | EPM **closed-arm duration** | 🔴 `STRUCTURALLY_UNAVAILABLE` | **drawn** | none detected | **`ns`** | — | `NO_DIFFERENCE_DETECTED` |

> ### `ANXIETY: NO_DIFFERENCE_DETECTED — 4/4` · **not `NORMALISED`**
> ⚠️ **`ns` is the absence of a detected difference, not an equivalence result.** No equivalence
> margin is declared anywhere in the paper and no power analysis is reported for these four
> measures at n = 9/10. The honest statement is the useful one and it is not the strong one:
> **the therapy does not produce an anxious animal.** It has not been shown to produce a
> wild-type-equivalent one.

⚠️ **The bundling is the overclaim.** The paper's summary sentence reads:

> *"…neurobehavioral and motor outcomes indistinguishable from those of WT controls, encompassing
> **locomotor activity, anxiety-related behavior, and motor coordination**"*

Of the three domains it names, **anxiety is 4/4 `ns`, locomotor is 2/3 significant, and motor
coordination is significant** — and the same paragraph acknowledges the third two sentences earlier
(*"significantly higher motor coordination and learning compared with WT mice (Figure 4K)"*).
**The sentence and the figure disagree on two of three domains, and the paper states both.**

### 2.5 Overshoot — what the evidence discriminates, and what it does not

Three readings are live for the exceed direction. **The queue's rule is that none may be asserted
unless evidence discriminates among them.** Applying it honestly gives a *partial* result, not a
null one:

| Reading | Status | What decides it, and whether it exists here |
|---|---|---|
| **Marginal statistics / noise** | ⚠️ **partially disfavoured — for M3 only** | An effect of **≈1.71×** is a poor fit for a threshold artefact. **It is not disfavoured for M1 (1.21×) and M2 (1.26×)**, which sit where a `*` at n ≈ 10 in an uncorrected family of eight is exactly what noise looks like. ⇒ **the three positives do not stand or fall together** |
| **Hyperactivity** | 🔴 **not discriminated** | Predicts ↑velocity and ↑distance with normal anxiety — which is observed. But it does **not** predict ↑rotarod latency: hyperactive animals are not thereby better at motor learning. ⇒ hyperactivity explains M1–M2 and **fails to explain M3** |
| **Overexpression overshoot** | 🔴 **not discriminated** | Consistent with **8.2× / 10.7× / 5.6× / 1.4×** WT protein at P300 (S5J) and 9–19× hippocampal at P90 — but *consistency is not discrimination*. The test is a **dose–expression–endpoint relation within treated animals**, and it **cannot be run in this dataset**: LD animals do not reach P90, so only one dose has behavioural data |

🔴 **The reason hyperactivity and overexpression are not discriminated is structural, not
incidental.** It is the same fact that makes `treated vs disease` unavailable — the low dose does not
survive to the assay. **One arm removes both limitations**, and §7 makes it a discriminator.

**What this section refuses to say:** that the overshoot is benign; that it is harmful; that it is
noise; that it is dose-related. All four are unsupported. **What it does say:** the three positive
panels have **different effect sizes and different explanatory fits**, and treating them as one
finding — in either direction — is the error.

### 2.6 The revised matrix line

> ### `AAV9_ENDPOINT_SPLIT: 3 RESCUE · 2 PARTIAL · 1 NO_RESCUE-on-its-only-drawn-bracket · 5 UNRESOLVED (3 NOT_MEASURED)`
> **`RESCUE`:** survival · SWD · gliosis — **each at HD, in the P0–P5 window, with the
> treated-vs-wild-type bracket drawn and non-significant.**
> **`PARTIAL`:** myelination (2021 paper) · **motor/locomotor (`NOT_NORMALISED`)**.
> **Anxiety is reported separately as `NO_DIFFERENCE_DETECTED` and is not counted as a rescue.**

---

## 3 · B3 — `therapy_levers.md`: eight repairs, verified and two of them re-worded

### 3.1 Locator verification — all eight, at `bf88c1a`

Every one of the eight current texts was matched **verbatim** against the live file this session.
**8/8 present, each exactly once.** The file is 44 lines; the repairs touch **7 of them**.

| # | Line | Section | Class | Locator |
|---|---|---|---|---|
| O-1 | **40** | Practical priority 2 | 🔴 `SYMPTOM_CONTROL_AS_DISEASE_MODIFICATION` | ✅ verified |
| O-2 | **17** | A2 | `UNMEASURED_TARGET_DIRECTION` | ✅ verified |
| O-3 | **17** | A2 | 🔴 `SYMPTOM_CONTROL_AS_DISEASE_MODIFICATION` | ✅ verified |
| O-4 | **29** | C2 heading | 🔴 `GLOBAL_RESCUE` | ✅ verified |
| O-5 | **28** | C1 | `GLOBAL_RESCUE` | ✅ verified |
| O-6 | **12** | Honest overview | 🔴 `SYMPTOM_CONTROL_AS_DISEASE_MODIFICATION` | ✅ verified |
| O-7 | **42** | Practical priority 4 | `GLOBAL_RESCUE` | ✅ verified |
| O-8 | **21** | B1 | `UNMEASURED_TARGET_DIRECTION` | ✅ verified |

**Class totals:** `SYMPTOM_CONTROL_AS_DISEASE_MODIFICATION` **3** · `GLOBAL_RESCUE` **3** ·
`UNMEASURED_TARGET_DIRECTION` **2** · **`TRANSFERRED_AS_DIRECT` 0 in this file.**

🔴 **`TRANSFERRED_AS_DIRECT` survives elsewhere and must not be reported as closed.** The single
instance is `R-01`'s `KNOWN_MAJOR_SAFETY_CONSTRAINTS` in `mechanism_intervention_map.md` — the
dose-limiting DRG/peripheral-ganglion toxicity, which comes from a **class-level review** (PMID
42128308 §11) and sits in a field otherwise reporting this vector's own measurements. **No DRG
assessment exists in either WWOX paper.** It is carried by
`CC-20260826-AAV9-ENDPOINT-SPLIT-01`, not by any `therapy_levers.md` edit.

### 3.2 🔴 Two of the eight proposed edits violate the rule B5 states

The queue's B5 rule — *no claim of elevation or flatness without statistical support* — applies to
the **replacements** as much as to the originals. Two fail it.

| # | Proposed edit as written | Defect | Re-worded |
|---|---|---|---|
| **O-2** | *"GSK3β **Ser9 phosphorylation falls** in cortex, hippocampus and cerebellum — a densitometry with no statistical test reported"* | 🔴 *"falls"* is a **direction asserted by us** in the same breath as *"no statistical test reported"*. The clause refutes itself | *"the source reports **increased GSK3β activation**, evidenced by **Ser9 dephosphorylation**, in cortex, hippocampus and cerebellum (PMID 32000863, Fig. 7c). ⚠️ **The supporting densitometry carries no statistical test and no n**, so the direction is **attributed to the source, not established here**. Neither cited source reports elevated GSK3β **abundance**, and one ([[claim_registry_current#CLAIM 035]]) reports it **unchanged**"* |
| **O-5** | *"…and **partially** restored myelination"* | ⚠️ *"partially restored"* is a **magnitude** claim. What is measured is that WT-vs-rescued is drawn on one panel and is significant **against** the rescue; on the others it is **not drawn at all** | *"…and **improved myelination on the comparisons the study draws**. 🔴 On the single panel where treated animals are compared with wild type — unmyelinated axons per field, WT ≈26 vs treated ≈52 — the comparison is **significant against the rescue**; on the remaining myelin panels **the wild-type-versus-treated comparison is not drawn**, so the residual gap is `NOT_TESTED`"* |

**The other six stand as written**, and O-1 and O-7 stand without qualification: they replace a
superlative and a global verb with the endpoint list, which is a narrowing of scope, not a claim
about a statistic.

⚠️ **O-7 must be re-checked against §2 before it lands.** Its proposed text — *"effective in mouse
**on survival, spike-wave discharges and gliosis**, at high dose, in the P0–P5 window"* — is
**correct after the MOTOR correction** and would have been wrong before it. It is the one edit in
the set whose content depends on `bf88c1a`.

### 3.3 What must not be weakened — the preservation check, run per edit

**The rule:** an edit is minimal only if the correctly-bounded statements *adjacent to it* survive
byte-for-byte. Two of the eight edits share a line with a statement that passes the sweep, and one
shares a **sentence**:

| Edit | Shares its line with | Must survive |
|---|---|---|
| **O-2, O-3** | each other, on **line 17** | *"Lithium is available and used in pediatrics (with tight monitoring: therapeutic window, thyroid, kidney). A preclinical hypothesis to discuss with a clinical team — **not medical advice**."* — 🔴 the safety caveat and the disclaimer are **in the same bullet** as both overclaims |
| **O-8** | 🔴 the **JNK and ERK** clause, in the **same sentence** | *"WWOX loss activates GSK3β, **JNK and ERK** → Tau hyperphosphorylation/aggregation; inhibitors (SP600125 anti-JNK, PD-98059 anti-MEK) block it in vitro"*. **Only the GSK3β term is under repair.** An edit that rewrites the clause wholesale would silently re-scope two axes this session never measured |
| **O-5** | C1's closing sentence | *"By replacing functional WWOX in neurons, it bypasses any allele combination"* — a mechanism statement, correctly bounded, unaffected |

**Five statements elsewhere in the file pass the sweep and are reported so it is not one-sided:**
A1 vigabatrin (*"Symptomatic, does not modify WWOX"*), B4 Zfra (*"evidence is Alzheimer/cancer, none
in epilepsy/WOREE"*), C3 ASO (*"an ASO does not repair the sequence"*, with Milasen labelled
regulatory), the header disclaimer, and line 10 (*"No WWOX-specific clinical trial exists"*).

### 3.4 🔴 The carrier audit — five of the eight repairs had nowhere to go

A specified edit that no object carries cannot reach a batch. **This is the failure mode of commit
`b80ae8b` — a verdict repaired in two files that never reached the layer holding it — and it is
present here in a second form.** Measured by grepping each site's current text across the seven
`CC-20260826-*` objects:

| Site | Carried by | Natural owner | Action |
|---|---|---|---|
| **O-1** *"disease modifier"* | ✅ `CC-…-LITHIUM-BOUNDARY-01` | lithium | none needed |
| **O-3** *"strongest repurposing signal"* | ✅ `CC-…-LITHIUM-BOUNDARY-01` | lithium | none needed |
| **O-2** *"GSK3β is elevated"* | ⚠️ appears in `LITHIUM-BOUNDARY` as **context**, not as a delta | 🔴 **GSK3β/S9** — it is a direction claim, not a drug claim | 🆕 **homed in `CC-…-GSK3B-S9-AXIS-01`** |
| **O-8** *"WWOX loss activates GSK3β"* | 🔴 **none** | 🔴 **GSK3β/S9** | 🆕 **homed in `CC-…-GSK3B-S9-AXIS-01`** |
| **O-5** C1 global rescue | 🔴 **none** | 🔴 **AAV9 endpoint split** | 🆕 **homed in `CC-…-AAV9-ENDPOINT-SPLIT-01`** |
| **O-7** *"already effective in mouse"* | 🔴 **none** | 🔴 **AAV9 endpoint split** | 🆕 **homed in `CC-…-AAV9-ENDPOINT-SPLIT-01`** |
| **O-4** C2 *"Proof that restoring WWOX reverses the phenotype"* | 🔴 **none** | ⚠️ the organoid record ([[claim_registry_current#CLAIM 002]]) — **no candidate in this set targets it** | 🔴 **ORPHANED → Plan** |
| **O-6** line 12 *"early intervention protects development"* | 🔴 **none** | ⚠️ the `N-15` disease-modification negative — **no candidate targets it either** | 🔴 **ORPHANED → Plan** |

> **`OVERCLAIM_CARRIER_AUDIT: 3 of 8 carried on arrival · 4 homed into existing candidates · 2 orphaned`**

🔴 **The two orphans are not homed here, deliberately.** Both would require either a new commit
candidate or an extension of an existing one's scope to a record it does not currently target
(`CLAIM 002` for O-4; the `N-15` block for O-6). **Choosing between those is structural integration,
which is Plan's authority under H.1** — *"Integrazione strutturale / candidate → Plan"* — not a
scientist's. They are handed over named, with their exact edits already written, and with the
observation that **O-4 contains the only occurrence of the word *"Proof"* in the entire therapeutic
chain.**

> ### `THERAPY_LEVERS_REPAIR: 8 sites · 8 locators verified · 2 replacements re-worded · 7 of 44 lines touched · 6 of 8 now carried · 2 orphaned to Plan · 0 molecules added, removed or reordered`
> **Reader-facing priority:** O-1 first (*"disease modifier"*, under a heading that says *"for
> clinical discussion"*), then O-7, then O-4. Those three are the sentences most likely to leave the
> repository in a reader's head — 🔴 **and O-4 is one of the two with no carrier.**

---

## 4 · B4 — mTOR: the site count was wrong, and the missing site is the loudest one

### 4.1 The two axes, held apart

| | **Axis 1 — mTOR therapeutic inference** | **Axis 2 — proteostasis / CMA-autophagy** |
|---|---|---|
| **Question** | does mTORC1 signalling move in a WWOX-deficient neuron? | how is the **WWOX protein** degraded? |
| **Evidence** | **one transcriptomic dataset**, n = 2 WT vs n = 4 KO, EV selection at raw `P<0.01`, **no verbatim locator** | CMA, HSC70, LAMP1, chloroquine, 3-MA, K63 ubiquitination, the P252A/Q230P chain — **locatored and independently evidenced** |
| **Under repair** | ✅ **yes** | 🔴 **no — and it must not be touched** |
| **Shared token** | `autophag` / `autofag` | `autophag` / `autofag` |

**They share a word and nothing else.** A sweep on `autophag` that does not separate them first will
"repair" a chain that is not in question while hunting a statement that lives in one line.

🆕 **The canonical layer proves the point by itself.** All three `autophag` hits in the canonical
registries are verbatim source titles, and they point in **two opposite directions**:

| Record | Title | Direction | System |
|---|---|---|---|
| `CORPUS-STUB-043` | *"WWOX **activates** autophagy … by regulating **mTOR**"* | **activates** | LPS acute lung injury |
| `CORPUS-STUB-056` | *"WWOX promotes apoptosis and **inhibits** autophagy"* | **inhibits** | paclitaxel, ovarian carcinoma |
| `CORPUS-STUB-139` | *"WWOX **suppresses** autophagy for inducing apoptosis"* | **suppresses** | methotrexate, squamous cell carcinoma |

**All three are `Status: not_processed`, `Claim links: none`, `Registry role: corpus placeholder
only`.** Nobody has read them, so none can carry a direction — and one of them is the *only* record
in the entire canonical layer that names WWOX, autophagy and mTOR in one sentence, in a non-neural
injury model. It is the single most dangerous title in the registry for a token sweep.

⚠️ *This corroborates a correction already recorded at `mechanism_intervention_map.md:32`* — *"three
registry stubs name WWOX↔autophagy in **two opposite directions**"*. **It is not a new finding here,
and is reported as confirmation, re-derived independently.**

### 4.2 The canonical surface, re-measured with a stated recipe

**Population:** **436** tracked `.md` / `.json` / `.jsonl` files at `bf88c1a` (`git ls-files`).
**Token family:** `\bmTOR\b` · `EIF4EBP1|4E-?BP` · `autophag|autofag` · `rapamyc|sirolim` ·
`everolim` · `\bLC3\b` · `SQSTM1|\bp62\b`, case-insensitive.

| Canonical surface | mTOR | autophag | other 5 tokens | Directional statements |
|---|---|---|---|---|
| `claim_registry_current.md` | 0 | 0 | 0 | **0** |
| `working_model_current.md` | 0 | 0 | 0 | **0** |
| `disease_model.md` | 0 | 0 | 0 | **0** |
| 🆕 `therapeutic_strategies_current.md` | **0** | **0** | **0** | **0** |
| `state_manifest_current.md` | 0 | 0 | 0 | **0** |
| `paper_registry_current.md` | 2 | 3 | 0 | **0** — all 5 are `**Full title:**` fields |
| `literature_tracking_log_current.md` | 2 | 3 | 0 | **0** — all 5 are `**Note:** Title:` fields |

> ### `MTOR_CANONICAL_DIRECTIONAL_STATEMENTS: 0 / 10 hits · 5 unique records × 2 registries · all `not_processed` stubs`

🔴 **Two corrections to my own prior measurement:**

1. **§2.4 of `therapeutic_canonical_repair_package.md` is headed *"The canonical layer is clean —
   measured"* over a table of four surfaces.** `therapeutic_strategies_current.md` — **the
   therapeutic tracker, the most decision-facing surface in the repository** — was never scanned.
   It **is** clean (0/7 tokens), so the verdict survives; **the table's scope did not cover the
   claim its heading made.** A negative measured over a subset is a negative about the subset.
2. **§2.3 reports `BIBLIOGRAPHIC ONLY | 8 | 4 titles in `paper_registry_current.md`, 4 in
   `literature_tracking_log_current.md``.** Re-derivation over the declared family returns
   **5 and 5 = 10**. ⚠️ **I cannot reproduce 8 from any subset of the family**, and I am **not**
   reconstructing a token set that would yield it. The number stands corrected to **10**, with the
   recipe above so the next actor can check it rather than inherit it.

### 4.3 🔴 The repair surface is **4 sites, not 2**

A phrase-level sweep for the *retired verdict's wording* — `wrong (biological )?direction` ·
`points? the wrong way` · `same (direction|way) as the lesion` — anchored within ±3 lines of an
mTOR-family or `N-01` token, over all 436 files, returns **26 hits**. Classified:

| Class | Count | Where |
|---|---|---|
| **ASSERTS the retired verdict** | 🔴 **5 lines** | **`mechanism_intervention_map.md` only** — lines **116, 624, 625, 627, 811** |
| Quotes it in order to retire it | 20 | the four analysis files + `CC-20260826-MTOR-DIRECTION-01`, all correctly typed |
| Already carries the correction | 1 | `mechanism_intervention_map.md:31` |

The five asserting lines cluster into **three blocks**, and the ledger line makes a fourth site:

| Site | Location | Wording | Named by any artefact? |
|---|---|---|---|
| **M0** | `discovery_ledger_current.md:691` (`DL-MECH-034`) | *"**autofagia ↓** … **mTOR/EIF4EBP1 ↓**"*, tagged **`(DATO)`** | ✅ yes — "Site 1" |
| **M1** | `mechanism_intervention_map.md:112–120`, §2.2 *"Refused admission"* | *"would push the **same direction as the lesion**"* … *"**This is the single most consequential negative in the file**"* | 🔴 **NO for the direction.** ⚠️ §2.2 **is** named at line 32 — but for a **count** defect (*"the only other WWOX record naming mTOR"*), not for the directional assertion three lines above it |
| **M2** | `mechanism_intervention_map.md:624–632` (`N-01` entry) | heading *"→ **wrong biological direction**"* · *"Failure mode: acts in the wrong direction"* · *"pushes the **same way as the lesion**"* | ✅ yes — "Site 2" |
| **M3** | `mechanism_intervention_map.md:811–812` (`TOP_NEGATIVE_FINDINGS` #2) | *"**mTOR inhibition points the wrong way** (N-01)"* | ⚠️ implicitly — the candidate says *"demote from `TOP_NEGATIVE_FINDINGS`"* but does not quote this line |

🔴 **M1 is unrepaired in every artefact and carries the strongest wording in the file.** It sits in a
different section from `N-01`, is not labelled `N-01` at the point of assertion (it only
cross-references *"See §5, N-01"*), and therefore **survives any repair scoped to "the `N-01`
block"**. This is the same failure mode as commit `b80ae8b` — *the verdict I repaired in two files
never reached the layer that carries it* — repeating **inside the repair itself**.

⚠️ **M1 also contains a correctly-bounded statement that must survive verbatim:**

> *"The only other WWOX record naming mTOR is `CORPUS-STUB-043` in the paper registry (an LPS
> lung-injury study), status `not_processed`: **nobody has read it, so it cannot carry a direction**
> and is not cited here as evidence for or against."*

That sentence is exactly right and is the model the rest of the block fails to follow. *(Its
`"only other"` is separately corrected at line 32 — `CORPUS-STUB-177` — which is a **count**
correction, not a **direction** one, and it does not license rewriting the bounded clause.)*

### 4.4 The minimum repair, per site

| Site | Delta | Class |
|---|---|---|
| **M0** | re-tag **`(DATO)` → `(DATO trascrittomico — non locatorato, non-FDR, n = 2/4)`**. **The recorded direction is preserved**; only its evidential type changes | MINOR |
| **M1** | *"would push the **same direction as the lesion**"* → *"would push the **same direction as the only directional datum**, which is a **non-locatored transcriptomic signal at n = 2/4** and is **not a measurement of mTORC1 signalling**"*. And *"the single most consequential negative in the file"* → *"a negative whose **weight rests on one weak datum**"*. 🔴 **Preserve the `CORPUS-STUB-043` sentence byte-for-byte** | MINOR |
| **M2** | failure mode *"acts in the wrong direction"* → **`INSUFFICIENT — mai misurato a livello proteico in alcun sistema WWOX`**; heading likewise. The block's existing *"Honest weight of the negative"* paragraph **already says this** and is preserved — the heading contradicts its own body today | MINOR |
| **M3** | demote out of `TOP_NEGATIVE_FINDINGS`; the entry's replacement text must not assert a direction | MINOR |

> ### `MTOR_MINIMUM_REPAIR: 4 sites · 2 files · 5 asserting lines + 1 type tag · 0 canonical · all MINOR`
> **mTOR inhibitors remain out at every tier and in `DEPRIORITIZE` (map line 774, which asserts no
> direction and needs no edit).** This repair **does not promote them**. It changes *why* they are
> out — from *"it points the wrong way"* to *"nobody has measured it"* — and that difference decides
> whether the cheapest experiment in the portfolio (one blot, no intervention) is worth running.

---

## 5 · B5 — `CLAIM 016` / `CLAIM 035`: the hostile self-check

### 5.1 Locator correctness — the mislocator is confirmed, and a bare swap breaks a second clause

Panel identities, from `deepdive_manifests/PMID32000863.json`, cross-checked against the paper's own
figure citations:

| Panel | What it shows | Source's own citation |
|---|---|---|
| **7b** | **ethosuximide** — `n.s.` in `+/+` and `+/−`, significant in `−/−` | *"…in Wwox−/− mice (**Fig. 7b**)"* |
| **7c** | GSK3β densitometry — pSer9 and total, three genotypes × three regions | — |
| **7d** | **lithium** — three stacked genotype panels, **each carrying its own `****` bracket** | *"…suppressed PTZ-induced epileptic seizure in Wwox−/− mice (**Fig. 7d**)"* |

`CLAIM 016`'s evidence boundary attributes the lithium three-genotype reading to **`Fig. 7b`**.

> 🔴 **CONFIRMED MISLOCATOR.** The correct panel is **7d**. And **7b is correct** for the
> ethosuximide clause that follows **inside the same parenthesis** — so a bare `7b → 7d` swap
> repairs one attribution and **breaks** the other.

**Propagation, measured:** the same `Fig 7b` appears in `framework/state/state_manifest_current.md`,
`batch_20260810_005_scope` — **verified present at `bf88c1a`**. ⇒ **2 sites**, in 2 files, one of
which is the state-control file.

### 5.2 Elevation and flatness — neither is available

Figure 7c densitometry, re-read at 3× from the native 1946×1627 image (`+/+`, `+/−`, `−/−`):

| Blot | Cerebellum | Hippocampus | Cortex | `+/+` → `−/−` |
|---|---|---|---|---|
| **pGSK3β(Ser9)** | 2.7 / 3.1 / **1.3** | 3.6 / 3.5 / **2.0** | 3.9 / 3.8 / **2.5** | **−52% · −44% · −36%** |
| **total GSK3β** | 2.2 / 2.4 / **2.4** | 2.3 / 2.4 / **2.6** | 2.2 / 2.4 / **2.6** | **+9% · +13% · +18%** |

🔴 **No statistical test, no n, and no error bar is reported for either blot.** Therefore:

| Statement | Verdict |
|---|---|
| *"GSK3β is **elevated** in cortex, hippocampus and cerebellum"* (canonical Summary) | 🔴 **NOT SUPPORTED.** `NOT_TESTED`. ⚠️ **It is directionally consistent with the printed values (+9 to +18%)** — the defect is not that it points the wrong way, it is that **it is untested, an order of magnitude smaller than the pSer9 change, and not what the source concludes** |
| *"total GSK3β is **flat**"* — `mechanism_intervention_map.md:34` | 🔴 **ALSO NOT SUPPORTED.** `NOT_TESTED`. **This is the rule's mirror image, live in the repository today, inside the very table that exists to record corrections** |
| *"Ser9 phosphorylation **falls**"* — O-2's proposed replacement | ⚠️ **Attributable, not established.** The source states *"Increased **activation** of GSK3β … as evidenced by **dephosphorylation** of GSK3β at Ser9"*. Report it **as the source's conclusion**, with the statistical status attached |
| *"neither cited source claims elevated abundance"* | ✅ **VERIFIED** — Cheng 2020 concludes about **activation**, not abundance, and no abundance claim exists in either source. 🔴 **But the second half of my first draft — *"Wang 2012 reports abundance unchanged"* — is `NOT_LOCATORED`.** See §5.7: the Wang locator covers **pS9 and phospho-β-catenin**, and says nothing about total GSK3β. The clause is safe **only** in its negative form |

**The required wording, for both directions:**

> *"The source reports increased GSK3β **activation** in cerebellum, hippocampus and cortex,
> evidenced by **Ser9 dephosphorylation** (PMID 32000863, **Fig. 7c**). ⚠️ **The densitometry
> carries no statistical test, no n and no error bars**; total GSK3β abundance is **`NOT_TESTED`**
> in either direction. The claim's `Type: DATO (abbondanza, murino)` types an untested densitometry
> as a `DATO` and is the field that should move."*

### 5.3 `NOT_TESTED` vs `NOT_REPORTED` vs `NOT_RECORDED`

| Case | Status | Owner |
|---|---|---|
| total GSK3β across genotypes, Fig. 7c | **`NOT_TESTED`** — no test drawn | paper |
| lithium `−/−` vs `+/+` contrast, Fig. 7d | **`NOT_TESTED`** — three within-genotype brackets, **no between-genotype bracket** | paper |
| ethosuximide converse for lithium | **`NOT_REPORTED`** — the text states the genotype pattern for ethosuximide and *"non dichiara il converso"* for lithium | paper |
| S4A KO-vs-HD bracket (§2.3, M5) | 🆕 **`NOT_RECORDED`** | 🔴 **us** |

### 5.4 The mutual exclusion — unchanged, and it is the substantive finding

| | `CLAIM 016` via Cheng 2020 | `CLAIM 035` via Wang 2012 |
|---|---|---|
| **Mechanism** | WWOX loss → GSK3β **de-repressed** | WWOX is a **direct physical inhibitor** via the Axin-like motif 388–407 / **L404** |
| **S9 axis** | the **only** directional signal is **pSer9 ↓** | inhibition is **S9-independent**; pS9 and abundance **unchanged** while kinase output changes |
| **Measurement warning** | — | a pS9 western *"produrrà un **falso negativo**"* |

🔴 **These exclude each other on the S9 axis.** If the WWOX brake is S9-independent, losing WWOX
should not move pSer9 — yet Cheng's only positive signal *is* a pSer9 fall. Two readings survive and
this file chooses neither: **(a)** Cheng's pSer9 fall is driven by something other than the WWOX
brake; **(b)** Wang's S9-independence does not hold in mouse brain. **Both are testable and neither
is tested.**

### 5.5 The P14 / P20 ambiguity — 🔴 **I had the wrong ambiguity, and the right one was already recorded**

> 🔴 **SELF-CORRECTION, made mid-session against my own draft of this section.**
> I first wrote that `P20` was *"the GSK3β densitometry timepoint"* in PMID 32000863, taking it from
> the manifest locator `[2]`, whose anchor quotes the **Results text**. I then built a *"cross-paper
> token collision"* around it. **The real ambiguity is inside PMID 32000863 itself**, and
> `CC-20260826-GSK3B-S9-AXIS-01` had already found it and already recorded that my earlier file's
> flat assertion of *"P20"* was **imprecise in my own favour**:
>
> | Location in PMID 32000863 | States |
> |---|---|
> | Methods, *Western blotting* | tissues *"isolated from three genotypes of mice at **postnatal day 14**"* |
> | **Figure 7c legend** | *"at **postnatal day 20**"* |
> | Figure 6a legend | *"at postnatal day 14 **or** 20"* |
>
> ⇒ **the age of the Fig. 7c blot is `NOT_REPORTED` unambiguously by the paper**, and the manifest's
> `P20` is one of two conflicting statements in it, not a settled fact.
>
> **Why it matters, and why it strengthens rather than weakens the analysis:** `CLAIM 036` measures
> the systemic null as hypoglycaemic (143.5 vs 250.6 mg/dL, `p = 0.000131`), acidotic and uraemic at
> **P18** — and **both candidate ages fall inside or immediately beside that window**. The metabolic
> confounder on the GSK3β blot therefore **applies under either reading and no longer depends on
> choosing one.** That is a stronger result than the one I was about to publish.
>
> **The error I made:** I treated a locator's anchor text as the paper's settled fact, and I did not
> read the candidate that targets the same claim before writing about it. *Re-derive the premise that
> authorises your own act* — and read the object before summarising it.

**What survives from the original section**, re-scoped and re-verified — the AAV9 side, where the
timepoints *are* settled and the ambiguity is one of unmarked scope:

| Timepoint | Experiment | Panels | Result |
|---|---|---|---|
| **P20** | AAV9 **dose study** (42422765) | Fig. 3E–H, blood glucose | `*` WT-vs-LD · `**` LD-vs-HD · **`ns` WT-vs-HD**. **LD has not corrected hypoglycaemia; HD has** |
| **P14** | AAV9 **treatment-window study** (42422765) | S8C/S8D, weight and glucose | `***`/`**` **WT-vs-KO** and **`ns` WT-vs-P5**. 🔴 **No treated-vs-KO bracket is drawn** for any of P1–P5 |
| **P14** | AAV9 **promoter study** (42422765) | Fig. 1, four promoters at 4×10¹⁰ vg | separate experiment again |
| **P14 *or* P20** | **GSK3β densitometry** (32000863) | Fig. 7c | 🔴 **`NOT_REPORTED` unambiguously** — Methods say **P14**, the Fig. 7c legend says **P20**. See the correction above |

✅ **`CLAIM 011`'s flag is correct**: its *"A P20 la dose bassa non ha corretto l'ipoglicemia, l'alta
sì"* is the dose study, Fig. 3E–H, and the timepoint matches the panel. **No mislocator here.**

🔴 **On the AAV9 side, what is ambiguous is unmarked rather than wrong.** *(i)* Three glucose
measurements exist at two timepoints across three figures of **one** paper, and the canonical record
names one timepoint without naming which experiment. *(ii)* At P14 the **`ns` is against wild type,
not against KO** — *"`ns` is absence of detected difference, not an equivalence test"*: the window
study establishes that treated animals are not detectably different from WT on weight and glucose,
**and never tests them against the disease**. *(iii)* ⚠️ **A `P20` token sweep merges four
different things** — the AAV9 dose-study glycaemia panel, and the GSK3β blot whose age the paper
does not settle. **Neither of the two `P20` referents is safe to carry without its figure.**

### 5.6 🔴 The propagation check that found something

The queue asks for `state_manifest` propagation. Running it found the mislocator **and** two live
defects in the map's own corrections table — the table whose purpose is to record repairs:

| Line | Text | Defect |
|---|---|---|
| `mechanism_intervention_map.md:34` | *"…total GSK3β is **flat**; pSer9 falls"* | 🔴 **flatness asserted with no test** — §5.2 |
| `mechanism_intervention_map.md:35` | *"`SPLIT`. Retained for survival/SWD/**motor**/gliosis at HD…"* | 🔴 **stale.** The row entered at **`6d43503`**; the MOTOR correction landed **four commits later** at `bf88c1a` and did not revise it. The retained list here **still counts four endpoints; it is three** |
| `framework/state/state_manifest_current.md`, `batch_20260810_005_scope` | *"(PMID 32000863 **Fig 7b**, read from the image)"* | 🔴 the mislocator, in the state-control file |

### 5.7 The full locator sweep on `CLAIM 035` — because checking one locator is not a hostile check

Finding the `7b → 7d` mislocator and stopping is the error this section exists to avoid. **All nine
locators of `PAPER 056` (Wang 2012, PMID 22193544) were read and matched, proposition by
proposition, against every assertion in `CLAIM 035`'s Summary.**

| `CLAIM 035` asserts | Locator | Verdict |
|---|---|---|
| **L404 strictly necessary** | `[2]` — *"the mutation of L404A, **but not L311A**, completely abolishes the binding"* | ✅ **exact**, and the negative control is in the source too |
| blocks Tau **S396 / S404**, **not** the MKK4 site **S422** | `[3]` — *"…inhibited Tau phosphorylation at S404 and S396 **but not S422**"* | ✅ **exact** |
| interaction between **endogenous proteins in mouse brain** | `[4]` — co-IP from mouse brain extracts, Fig. 2e | ✅ **exact** |
| epistasis: Tau knockdown abolishes it; WWOX + siRNA-GSK3β non-additive | `[6]`, `[7]` | ✅ **exact** |
| **pSer9 invariant** while output changes | `[5]` — *"phospho-GSK3β S9 and phospho-β-catenin remained normal"* | ⚠️ **true, but from Fig. 1b–c — the RA-differentiation experiment**, not from the Fig. 3 docking experiment the sentence attaches it to |
| *"un segmento di **20 residui (388–407)** omologo al motivo di docking Axin/FRAT/GSKIP"* | 🔴 **two locators, two intervals** — `[0]`: **388–407** is *required for the interaction* (Fig. 3c); `[1]`: **388–412** is what *contains the conserved FXXXLI/VXRLE motif* (Fig. 2a) | 🔴 **CROSS-FIGURE FUSION.** The arithmetic is right (407−388+1 = 20) and both facts are true; **the homology belongs to the 25-residue interval and the requirement to the 20-residue one**, and the claim gives the homology to the requirement's interval |
| *"ripristina l'assemblaggio dei **microtubuli** Tau-dipendente"* | 🔴 **none of the nine** | ⚠️ **`NOT_LOCATORED`** — neurite outgrowth is locatored (`[6]`); microtubule assembly is not |
| *(via `CLAIM 016`)* *"nel sistema di Wang … **l'abbondanza di GSK3β** resta invariata"* | 🔴 **none of the nine** — `[5]` covers **pS9 and phospho-β-catenin only** | 🔴 **`NOT_LOCATORED`.** The statement that the *other* source reports abundance unchanged has **no locator behind it** |

🔴 **Two cross-figure fusions in one claim, and both run in the direction of a tidier mechanism.**
This is the same failure class the AAV9 dossier named when it retracted two Figure-1 claims —
*"every claim that died was a cross-figure inference"* — recurring in a `consolidated`-adjacent
biochemistry claim that nobody had re-swept.

⚠️ **None of this weakens `CLAIM 035`'s core.** L404, the S396/S404-not-S422 selectivity, the
endogenous brain interaction and the Tau epistasis are all locator-exact, and they are what the
claim is for. **Three deltas follow, all MINOR and all additive to `CC-…-GSK3B-S9-AXIS-01`:**
give `388–412` its own figure, mark microtubule assembly `NOT_LOCATORED` pending a re-read, and
delete the unlocatored abundance clause from `CLAIM 016` — 🔴 **which `D5` already proposes to do
for a different reason** (*"it preserves a datum neither cited source asserts"*). **Two independent
routes reach the same edit; that is corroboration, not duplication.**

> ### `CLAIM016_035_STATUS: mislocator CONFIRMED (7b → 7d) · 2 propagation sites · elevation and flatness BOTH NOT_TESTED · mutual exclusion UNCHANGED · P14/P20 = NOT_REPORTED by the paper (my framing corrected mid-session) · 9/9 CLAIM 035 locators swept: 4 exact, 1 context-shifted, 2 cross-figure fusions, 2 NOT_LOCATORED · 2 live defects in the corrections table`

---

## 6 · B6 — the candidate ledger

**Base-head note.** All seven objects declare **`Base head: b80ae8b`** and all seven **landed in
`bf88c1a`**. That is not an inconsistency: `b80ae8b` is the head they were *written against*, and it
is preserved as provenance. **What changed at `bf88c1a` is the MOTOR correction**, which candidate F
carries in its body. ⚠️ **A commit is provenance of the commit, not of the file** — so the row that
matters is not the declared base head but **`targets verify @`**, re-measured below.

**Verification run this session:** 23 declared target strings, checked verbatim against the live
tree — **23/23 as expected, 0 rows needing attention**, at `bf88c1a` and re-run unchanged at
`29408ca`.

> 🔴 **SELF-CORRECTION — a frozen set over live inputs thaws itself, and it did so twice inside one
> session.** The first version of this table published blob hashes at `bf88c1a`; I then edited four
> of the seven objects and four hashes went stale. I re-stamped at `29408ca` — **and then edited
> `G` again**, so ⚠️ **`G`'s stamped value is already superseded as you read this.** That is not a
> defect to patch a third time: **it is the correct behaviour of a stamped measurement over a live
> tree**, and chasing it would produce a fourth stale value.
>
> **The repair is a recipe, not a value.** *A hash without a recipe is an attestation.* Re-derive at
> any head with:
>
> ```bash
> for f in disease-models/wwox/research/commit_candidates/CC-20260826-*.md; do
>   printf '%-44s %s\n' "$(basename "$f" .md)" "$(git rev-parse HEAD:"$f" | cut -c1-12)"
> done
> ```
>
> **A hash published beside an object you are still editing is an attestation, not a measurement.**
> The values above are kept **with their stamp** so a reader who inherited them can tell what they
> described; the stamp is what makes a stale value safe rather than false.
>
> **The base head stays `b80ae8b` for all seven.** It is provenance of *authorship*, not of content,
> and rewriting it to `29408ca` would falsify the record of what each object was written against.
> ⚠️ **A commit is provenance of the commit, not of the file** — so the row that carries operational
> weight is `Targets verify @`, which is re-measurable by anyone at any head.

| | **A — mTOR** | **B — Lithium** | **C — NMDAR** | **D — Gap junction** | **E — Pannexin** | **F — AAV9** | **G — GSK3β/S9** |
|---|---|---|---|---|---|---|---|
| **Object** | `CC-…-MTOR-DIRECTION-01` | `CC-…-LITHIUM-BOUNDARY-01` | `CC-…-NMDAR-CONJUNCTION-01` | `CC-…-GAPJUNCTION-ATTRIBUTION-01` | `CC-…-PANNEXIN-N16-01` | `CC-…-AAV9-ENDPOINT-SPLIT-01` | `CC-…-GSK3B-S9-AXIS-01` |
| **Blob — stamped @ `29408ca`** | `b570496149cb` | `941327000731` | `d225077b6fb1` | `e51035e1f596` | `aab18ed8509f` | `fc40eb423a81` | `5f44233d2b40` ⚠️ |
| **Base head declared** | `b80ae8b` | `b80ae8b` | `b80ae8b` | `b80ae8b` | `b80ae8b` | `b80ae8b` | `b80ae8b` |
| **Targets verify @** | `29408ca` | `29408ca` | `29408ca` | `29408ca` | `29408ca` | `29408ca` | `29408ca` |
| **Canonical targets** | **none** — ledger + map | `TX-005` (tracker) + `therapy_levers` A2 & priority 2 | 🔴 `CLAIM 021` | 🔴 `CLAIM 021` + map `CHAIN B` | map negatives; `CLAIM 021` **only if bundled** | 🔴 `CLAIM 004` + `CLAIM 011`; `TX-007`, map `R-01` | 🔴 `CLAIM 016` + `CLAIM 035`; **`state_manifest`**; map `CHAIN C`/`R-04` |
| **`BATCH_COMMIT`?** | **no** | **no** | **yes** | **yes** | **only if bundled** | **yes** | **yes** |
| **Change class** | MINOR | MINOR | MINOR (additive upgrade) | MINOR (withdrawal of attribution) | MINOR (additive) | 🔴 **MAJOR** (fail-closed) | 🔴 **MIXED** — D1/D2/D5/D7/D8 MINOR · D3/D4 **MINOR?** · **D6 MAJOR?** |
| **Transfer boundary** | none — removes an interpretation | 🔴 **genotype**: effect is in **all three genotypes**, WT included ⇒ anticonvulsant, not WWOX rescue | inside the WWOX system (`Wwox` S-KO slice) ⇒ **T1 for the tool compound**; memantine is **not** d-APV | inside the system; **attribution** withdrawn, not the effect | inside the system; **new** negative | 🔴 **`TRANSFERRED (T4/T5)`** — `R-01`'s DRG constraint is class-level review, no WWOX DRG data exists | mouse biochemistry → human neuron: **T2**; **no WWOX-DEE allele tested** in either source |
| **Revival trigger** | protein-level mTORC1 readout (pS6, p4E-BP1) in a WWOX-deficient neuronal system; **or any WWOX model showing mTORC1 hyper-activation** | PTZ + lithium with an **explicit tested `−/−` vs `+/+`** contrast; or a different GSK3β inhibitor, same design | memantine dose–response reproducing d-APV | **occlusion**: CBX on top of sub-maximal d-APV | BB-FCF **powered and tested** with a declared n | 5 triggers — see the candidate; the binding one is **any** developmental/cognitive endpoint with a **seizure-matched comparator** | a **pSer9-independent** GSK3β activity readout in a WWOX-deficient neuron; a statistical test on the Fig. 7c densitometry |
| **Mirror** | no | no | no | no | no | 🔴 **YES** (H.1 — doubtful MAJOR, fail-closed) | 🔴 **YES** — D6 is `MAJOR?` and D3/D4 are `MINOR?`; **the doubt itself routes to Mirror** |
| **Human gate** | no | no | no | no | no | 🔴 **YES** (H.1 — MAJOR approval → Operatore) | ⚠️ **CONDITIONAL** — required **if** Mirror classifies D6 MAJOR; **and** unconditionally for the *form* of the D2 `state_manifest` correction, which edits a historical record |
| **Conflicts** | none | ⚠️ **shares `therapy_levers.md` line 17 with G** — edit order matters, content does not | ⚠️ **shares `CLAIM 021`'s sentence with D** | ⚠️ **shares `CLAIM 021`'s sentence with C** | ⚠️ same sentence **only if bundled** | ⚠️ **F's Part 1 must precede nothing and blocks nothing** | ⚠️ shares line 17 with B; **shares no proposition with B** |

### 6.1 C and D stay independent — restated because the ledger makes them look coupled

They edit **the same sentence** of `CLAIM 021` — *"Bursting depends on NMDAR and gap junction
activity"* — and that is the **only** thing they share.

| | **C — NMDAR** | **D — Gap junction** |
|---|---|---|
| **What it is** | an **upgrade**, on a positive pharmacological result (d-APV **abolishes** the burst) | a **withdrawal of attribution**, on a **washout failure** and an off-target list |
| **Evidence** | the d-APV arm | the carbenoxolone arm |
| **If refused** | the conjunction stays as written | the gap-junction node stays an independent target |
| **Presupposes the other?** | **no** | **no** |

🔴 **A reviewer who accepts C has been given no reason to accept D.** The textual adjacency is a
merge-order problem, not an epistemic dependency. **D must not ride on C's acceptance**, and D's
own text already refuses the symmetric error: *"do not state that gap junctions are uninvolved —
that was not measured."*

### 6.2 🔴 One candidate's declared negative is stale

**Candidate E** opens: *"**None.** No canonical claim, no tracker entry and **no map entry** mentions
pannexin blockade."*

Re-measured at `bf88c1a`: `claim_registry_current.md` **0** ✅ · `therapeutic_strategies_current.md`
**0** ✅ · `mechanism_intervention_map.md` **1** 🔴 — at line 33, in the corrections table:
*"…and the pannexin blocker went the **wrong way** — new **N-16**"*.

**The candidate's own predecessor put it there.** ⇒ E's `CURRENT_TARGET` must read *"no map **entry**
— one **forward reference** exists in the corrections table at line 33"*. **The substance is
untouched**: `N-16` is still an addition to the negative list and still additive. **This is a
recording-a-negative-falsifies-it failure**: the sweep that proved pannexin absent returns a hit the
moment the proof is written down.

> ### `THERAPEUTIC_CANDIDATE_COUNT: 7` · `MIRROR_REVIEW_REQUIRED: 2 (F, G)` · `HUMAN_GATE_REQUIRED: 1 certain (F) + 1 conditional (G)`
> **`BATCH_COMMIT` required: 4** (C, D, F, G) — **5 if E is bundled**.
> **Clears without Mirror: 5 of 7 (A, B, C, D, E), plus F's severed Part 1.**
>
> 🔴 **Corrected mid-session.** My first ledger recorded **G** as `MINOR / no Mirror / no human
> gate`, built from the `CHANGE_CLASS:` token at the head of the object. **G's own
> `REVIEW_REQUIRED` block says otherwise** — *"Mirror (D6 MAJOR?, and D3/D4 MINOR?)"* and
> *"HUMAN_GATE: operator, if Mirror classifies D6 as MAJOR; and operator sign-off on the form of the
> D2 manifest correction"*. **I summarised an object from its first line instead of reading it.**
> Three cells were wrong and both END-REPORT counts moved.

---

## 7 · B7 — discriminators, continued only where a null changes a decision

**The test:** *if the result is null, does the portfolio learn something that changes a decision?*
An experiment whose null is uninformative is a data-collection exercise and is not continued.

### `E-1` — occlusion + memantine dose–response · **CONTINUED**

| | |
|---|---|
| **POSITIVE_RESULT_CHANGES** | CBX reduces bursting **further** on top of sub-maximal d-APV ⇒ gap junctions are an **independent** node ⇒ **D is refused** and `CHAIN B` keeps its second target. Memantine dose-dependent ⇒ `R-02` advances from tool compound to **clinical** compound |
| **NULL_RESULT_CHANGES** | no further reduction ⇒ the gap-junction node **collapses into NMDAR** ⇒ **D is confirmed** and one of two targets in `CHAIN B` disappears. Memantine flat ⇒ `R-02` does **not** advance and the `T1` conjunction stays with a tool compound that will never reach a patient |
| **CONFOUNDERS** | 🔴 **d-APV at full block drives frequency to zero — no headroom for occlusion.** Sub-maximal dosing is the *precondition for the experiment being able to fail*, not an optimisation. · the **~1.85× washout overshoot** must be reported per arm · slice-to-slice variance at n ≈ 10 |
| **DEPENDENCY_ORDER** | **first.** Settles C, D and E **in one preparation** and defines nothing downstream needs |

### `E-2` — gramicidin perforated-patch `E_GABA` · **CONTINUED**

🔴 **`E_GABA` and inhibitory-current amplitude are two measurements, in the same cells, and neither
substitutes for the other.**

| | `E_GABA` (polarity) | sIPSC amplitude (strength) |
|---|---|---|
| **Measures** | the chloride **reversal potential** | the **size** of the inhibitory current |
| **Indifferent to** | amplitude | reversal |
| **Method constraint** | 🔴 **gramicidin perforated patch only** — whole-cell dialyses intracellular chloride and destroys the quantity | standard whole-cell acceptable |

| Joint result | Interpretation |
|---|---|
| depolarised `E_GABA` + preserved amplitude | **chloride defect** — bumetanide becomes rankable |
| normal `E_GABA` + reduced amplitude | **synaptic/receptor defect** — a different lever entirely |
| both | 🔴 **two lesions, not one** |
| neither | the `M3` axis **closes** |

| | |
|---|---|
| **POSITIVE_RESULT_CHANGES** | `E_GABA` depolarised vs isogenic parental, NKCC1/KCC2 shifted immature, rescued by W-AAV ⇒ `M3` moves **T6 → T2** and **bumetanide becomes rankable** for the first time |
| **NULL_RESULT_CHANGES** | 🔴 `E_GABA` indistinguishable from parental ⇒ **the chloride axis closes** and bumetanide moves from *unrankable* to **closed**. *"Depolarizing GABA"* is a **hypothesis** in this repository — the published organoid work measures GABAergic markers, receptor components and hyperexcitability, **not** chloride reversal — and a null **removes** it. **The only seed whose null is as decision-relevant as its positive** |
| **CONFOUNDERS** | 🔴 **cell composition** — an organoid with declared regionalization defects is not composition-matched to its control, so a population-level difference may be *which cells were recorded*. Mitigate with cell-type-resolved recording · the chloride switch is **itself developmental**, so **one timepoint cannot distinguish *inverted* from *delayed*** — hence ≥3 timepoints anchored to a **measured maturation landmark**, not days in culture · `MARKER_TO_FUNCTION_GATE`: NKCC1/KCC2 abundance is **not** `E_GABA` |
| **DEPENDENCY_ORDER** | **parallel to `E-1`** — different preparation, no shared reagent, no shared decision |

### `E-3` — delayed dosing with a seizure-matched ASM comparator · **CONTINUED**

| | |
|---|---|
| **POSITIVE_RESULT_CHANGES** | cognitive endpoint improves in the gene-therapy arms and **not** in the seizure-matched ASM arm ⇒ **disease-modifying**. 🔴 **This is the only result in the entire portfolio that would license that word for anything**, and it would fill the column on which every candidate currently scores empty |
| **NULL_RESULT_CHANGES** | both arms suppress SWD equally, **neither** moves cognition ⇒ gene addition past the window is **symptomatic**, and `N-15` extends from symptomatic levers **to the causal lever itself**. That reverses the portfolio's ranking logic, not one entry in it |
| **CONFOUNDERS** | 🔴 **matching SWD is not matching seizure burden** — SWD is an electrographic surrogate; arms matched on it may differ in behavioural seizures, sleep architecture or subclinical burden · 🔴 **ASMs have direct cognitive effects of their own, in both directions** — a second uncontrolled variable, hence the vehicle-ASM arm and a cognitive-side-effect readout · **a hypomorph is not a null** · timepoints anchored to a measured landmark or the "window" is a species artefact · 🔴 **not rotarod** — rotarod latency is motor learning, and §2.3 shows treated animals **exceed** wild type on it, which is the exact conflation this design exists to break |
| **DEPENDENCY_ORDER** | **last.** Run after `E-1` and `E-2`, whose results define its mechanistic endpoints |

### 🆕 `E-4` — intermediate dose with a paired expression readout · **NEW, and it discharges two triggers**

Emerged from §2.5. It is not a new idea about biology; it is the observation that **one arm answers
two questions that are currently answered by nothing**.

| | |
|---|---|
| **DESIGN** | AAV9-hSynI-WWOX at **an intermediate dose between 1.23 and 2.63 × 10¹¹ vg**, ICV P0–P5, carried to **P90**, with **per-animal** vector genomes, mRNA and protein in cortex, hippocampus, midbrain and cerebellum, **and the full Figure 4 behavioural battery** |
| **POSITIVE_RESULT_CHANGES** | *(a)* localises the survival **threshold** and supplies the **expression correlate** it currently lacks — 7/8 dose comparisons are `ns` today and the paper's explanation is survivor-conditioned; *(b)* if behavioural overshoot **tracks expression across doses**, `overexpression overshoot` is discriminated from `hyperactivity`; *(c)* supplies the **`treated vs disease`** comparison that P90 currently cannot have, **if and only if** the intermediate arm survives while a lower arm does not |
| **NULL_RESULT_CHANGES** | 🔴 **informative in three separate ways.** If the intermediate dose behaves like HD ⇒ the threshold sits **below** 1.23 × 10¹¹ and the LD failure is not a dosing question. If it behaves like LD ⇒ the threshold sits **just under HD** and the therapeutic index is **narrower than the 2.1-fold gap suggests** — a safety-relevant negative. If overshoot is **flat across doses** ⇒ `overexpression` is **disfavoured** and `hyperactivity` gains, which is the first evidence that would separate them |
| **CONFOUNDERS** | 🔴 **an intermediate dose without a per-animal expression readout reproduces the existing gap exactly** and is the one way to waste this experiment · survivor conditioning returns unless expression is measured **in every animal including those that die** · the Figure 4 battery must be run with **multiplicity declared in advance** — eight uncorrected comparisons is what made the present result unreadable |
| **DEPENDENCY_ORDER** | **independent of `E-1` and `E-2`; must precede `E-3`**, whose dosing arms it calibrates |
| **DISCHARGES** | `CLAIM 011`'s existing `REVIVAL_TRIGGER` (*"un braccio a dose intermedia … localizzerebbe la soglia"*) **and** candidate F's fifth trigger (*"an intermediate dose … carrying an expression readout"*) — 🔴 **two triggers, one arm.** They were written independently and neither notices the other |

### 7.1 Sample size — declined, with the missing inputs named

**No sample size is estimated for any of the four.** The inputs do not exist in this repository:

| Missing input | Why it blocks the calculation |
|---|---|
| **variance** on the P90 behavioural measures | Figure 4 prints mean ± SD as **error bars only**; no numeric SD is recorded in any locator |
| **effect size** for any cognitive endpoint | 🔴 **no cognitive assay exists in any WWOX system.** There is nothing to power against |
| **slice-to-slice variance** for burst frequency | not reported in PMID 34634460's locators |
| **within-dose expression variance** | S5 is a blot series without quantification |
| an **equivalence margin** for any `ns` endpoint | never declared by either paper |

⚠️ **Reporting a number here would be fabricating the variance that produces it.** Each protocol
carries a `PRE_REGISTRATION_BLOCKER: sample size requires a pilot variance estimate` instead.

> ### `TOP3_DISCRIMINATORS_STATUS: 3 continued + 1 new · all four have decision-changing nulls · dependency order E-1 ∥ E-2 ∥ E-4 → E-3 · 0 sample sizes estimated`

---

## 8 · Self-corrections against my own prior files

| # | Where | Correction |
|---|---|---|
| **1** | `therapeutic_canonical_repair_package.md` §2.4 | 🔴 **Scope.** Headed *"The canonical layer is clean — measured"* over **four** surfaces. `therapeutic_strategies_current.md` — the therapeutic tracker — was never scanned. It **is** clean (0/7 tokens), so the verdict survives; **the measurement did not cover the claim** |
| **2** | `therapeutic_canonical_repair_package.md` §2.3 | 🔴 **Count.** *"8 bibliographic (4 + 4)"* → re-derivation returns **10 (5 + 5)**. I cannot reproduce 8 from any subset of the declared family and am not reconstructing one; the recipe is published in §4.2 |
| **3** | `therapeutic_canonical_repair_package.md` §2.5 / `CC-…-MTOR-DIRECTION-01` | 🔴 **Site count.** *"`MTOR_PROPAGATION_REPAIR: 2 sites`"* → **4**. Block **M1** (`mechanism_intervention_map.md:112–120`, §2.2) asserts the retired verdict and carries the file's **strongest** wording. ⚠️ **Precisely:** §2.2 *is* named at line 32, but for a **count** defect — its directional assertion is named by **no artefact** and survives any repair scoped to *"the `N-01` block"* |
| **4** | `therapeutic_canonical_repair_package.md` §4 and §4.1 | 🔴 **Stale after `bf88c1a`.** The matrix still records **MOTOR = `RESCUE`**, and §4.1's proposed canonical form still says *"a wild-type-equivalent result on **four** endpoints — survival, SWD, **motor function** and astrogliosis"*. The MOTOR correction landed in `therapeutic_overclaim_closure.md` and in candidate F and **did not reach this file**. **The count is three** |
| **5** | `mechanism_intervention_map.md:35` | 🔴 **Same defect, in the corrections table.** *"Retained for survival/SWD/**motor**/gliosis at HD"* — **the table that exists to record corrections is itself one commit behind** |
| **6** | `mechanism_intervention_map.md:34` | 🔴 **Untested flatness.** *"total GSK3β is **flat**"* asserts a direction with no statistical support — the mirror image of the *"elevated"* overclaim it was written to correct |
| **7** | `therapeutic_overclaim_closure.md` O-2 | ⚠️ **Self-refuting replacement.** *"Ser9 phosphorylation **falls** … a densitometry with **no statistical test reported**"* asserts a direction and denies its support in one sentence. Re-worded in §3.2 as source-attributed |
| **8** | `therapeutic_overclaim_closure.md` O-5 | ⚠️ **Magnitude.** *"**partially** restored myelination"* is a magnitude claim over panels where the WT-vs-treated bracket is **not drawn**. Re-worded in §3.2 as `NOT_TESTED` |
| **9** | `CC-…-PANNEXIN-N16-01` | 🔴 **Stale negative.** *"no map entry mentions pannexin blockade"* — one **forward reference** exists at `mechanism_intervention_map.md:33`, **written by this candidate's own predecessor.** Substance untouched; the `CURRENT_TARGET` sentence is wrong |
| **10** | `HANDOFF_CLAIM011_PLAN_ORCH.md` | ⚠️ **Under-specified, not wrong.** It reports *"29 verbatim locators"*; the manifest's `verbatim_locators` is a **dict with an `entries` list**, and a naive read of it returns **5**. The 29 is correct — re-counted — but the field path matters and the handoff does not give it |
| **11** | this session | ⚠️ **My own first count of the manifest was 5.** I read the wrapper and not `entries`, and reported it before checking the structure. Corrected within the same step; recorded because the failure mode — *a counter placed before the check it summarises* — is the one this chain exists to catch |
| **12** | 🔴 **this session, §5.5** | **I had the wrong P14/P20 ambiguity.** I took `P20` from a locator's anchor text as the settled GSK3β timepoint and built a *"cross-paper token collision"* on it. **PMID 32000863 does not settle its own blot age** — Methods say P14, the Fig. 7c legend says P20 — and `CC-…-GSK3B-S9-AXIS-01` had **already found this** and already recorded that my earlier file's flat *"P20"* was *"imprecise in my own favour"*. **I wrote about a claim without reading the candidate that targets it.** The corrected version is **stronger**: both candidate ages fall inside the `CLAIM 036` metabolic window, so the confounder no longer depends on choosing one |
| **13** | 🔴 **this session, §6** | **My ledger row for candidate G was wrong on three cells** — change class, Mirror, human gate — because I built it from the `CHANGE_CLASS:` token at the head of the object instead of reading its `REVIEW_REQUIRED` block, which says *"Mirror (D6 MAJOR?, and D3/D4 MINOR?)"* and names a conditional operator gate. **Both END-REPORT counts moved.** *Read the object before summarising it* |
| **14** | 🔴 **this session, §6** | **I published blob hashes for seven objects and then edited four of them**, so four of the seven were stale **within the same session**. *A frozen set over live inputs thaws itself* — and *a hash published beside an object you are still editing is an attestation, not a measurement.* The row is now dual-stamped, and `Base head` is deliberately **not** advanced, because it records authorship, not content |
| **15** | 🔴 **this session, `CC-…-GSK3B-S9-AXIS-01`** | **D9's replacement text asserted the same unlocatored clause that D13 removes** — *"`CLAIM 035` reports abundance unchanged"* — written about an hour before D13 established it has no locator. **One object, two deltas, contradicting each other.** D9 now stops at the negative, which is the half the locators support |
| **16** | 🔴 **this session, §5.2** | **I marked *"neither cited source claims elevated abundance"* ✅ VERIFIED partly on the ground that Wang *"reports abundance unchanged"*.** The negative is verifiable from what the locators contain; **the positive is not.** The ✅ survives — for the negative only |
| **17** | `therapeutic_overclaim_closure.md` §1 | 🔴 **Specified without routing.** The eight *"exact minimum edits"* are correct and verified — and **five of them had no object able to carry them into a batch**. A specified edit with no carrier is the same failure as an unpropagated verdict, one layer earlier. Four are homed in §3.4; **O-4 and O-6 are orphaned and handed to Plan**, because choosing their carrier is structural integration and not a scientist's call |

---

## 9 · What this file does not do

- **No canonical file was edited**, and none is edited *by* this file. Every delta above is a
  proposal held inside a commit candidate.
- **No status was changed.** `CLAIM 011` remains `flagged for review`; `CLAIM 016` and `CLAIM 035`
  remain `in observation`.
- **No molecule was added, removed, promoted or demoted.** mTOR inhibitors remain in `DEPRIORITIZE`;
  lithium's tier is untouched; `R-01` still ranks first.
- **No classification was decided that belongs to another actor.** F's MAJOR is Mirror's to confirm
  or downgrade; the batch is the Orchestrator's; MAJOR approval is the Operator's.
- **No sample size was estimated**, and the missing inputs are named in §7.1.
- **Nothing here is medical advice.**
