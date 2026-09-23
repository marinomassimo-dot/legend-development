# Sampling frame or biology? — harmonizing measurement coverage before reading a genotype difference

**Node:** `SAMPLING_FRAME_VS_BIOLOGY` · **Actor:** SCIENTIST C (`scientist-c`) · **Date:** 2026-09-23
**Class:** methodological audit of the repository's own allele-comparison statements. **Not** a census of WWOX biology.

> 🔴 **Non-canonical analysis artefact.** READ-ONLY toward the four scientific current files, every registry,
> every ledger, every queue, the receipt chain and `framework/state/state_manifest_current.md`. No claim, no
> paper record, no working-model edit, no commit candidate, no gate, no receipt, no promotion. **This file is
> the only thing written.** No git command was run at any point in this act.
>
> 🔴 **Nothing here is medical advice.** No molecule, dose, route or schedule is named.
> 🔴 **NO EXTERNAL CONTACT of any kind** was made or drafted. No author, laboratory, foundation, repository
> owner or funder was written to. Every such route is `HUMAN_REQUIRED` and was left unexecuted.
> 🔵 **Public edition.** Genotype-class and named-allele level only. No individual-level record.
> ⚠️ **Alleles, drivers and species are NEVER pooled.** `Wwox`-null mouse (Aqeilan/Croce line, targeted
> exons 2–4) · `Wwox`-null mouse (NCKU `WD1`, exon 1) · `Wwox`-null mouse (NCKU `WD234`, exons 2/3/4) ·
> `Wwox^ΔCre` (EIIA-Cre germline) · BK5-Cre × `Wwox^flox/flox` · Nestin-Cre `N-KO` · Synapsin-Cre `S-KO` ·
> `Wwox^gt/gt` · rat `lde/lde` · `Wwox^P47T/P47T` · human WOREE · human SCAR12 are **distinct objects**.
> Every row below carries its own model, and nothing transfers between rows.

> 📖 **Reading-order note.** §§ 0–3 were written and flushed to disk **before any external query was run in
> this act**, because § 3 is a preregistration and a preregistration written after the search is not one.
> § 4 onward was appended afterwards. The file order preserves the audit trail.

---

## § 0 · READ DEPTH, DECLARED PER SOURCE, BEFORE ANY FINDING

**Legend.** 🟢 **FIRST-HAND** = I fetched and read the served body or the repository file myself in this act ·
🔴 **SIBLING-ATTESTED** = quoted from another actor's file or dossier, with repo file and line, never presented
as my own read · 🟡 **ABSTRACT-DEPTH** · ⚫ **BLOCKED** = retrieval attempted and failed, or licence-blocked.
🔴 A Scholar Gateway passage, had one been used, would be `REMOTE PASSAGE — ANALYSIS-VALID /
CANONICALIZATION PENDING` and never a full read. **No Scholar Gateway passage is used in this file.**

### 0.1 Repository sources read directly in this act (🟢 first-hand)

| File | What I read | Why |
|---|---|---|
| `analysis/cerebellar_measurement_census_20260922.md` | **in full, all 796 lines** | The brief's anchor. § 4.3 is the result this node generalises. **I did not rebuild its matrix.** |
| `analysis/cerebellar_functional_readout_census_20260922.md` | §§ 0, 1.1 (R1–R23), 1.2 (H1–H9), 1.3, 1.4, **1.5** | § 1.5 is the divergence this node adjudicates |
| `analysis/seizure_ascertainment_census_20260922.md` | §§ 0, 1a, 1b, 2/Q3, 4, 5 | The repository's existing ascertainment-harmonization precedent |
| `analysis/ataxia_without_cerebellar_lesion_20260922.md` | §§ 0, 1 (headings), 2.1, 2.2, 2.3, 3 (head) | Establishes that *"ataxic gait"* is itself not a measurement |
| `analysis/wwox_myelin_oligodendrocyte_census_20260921.md` | § 1.2 A/B/C tables, § 1.3, § 1.4 | Tested as a candidate comparison; see § 1.3 |
| `registries/claim_registry_current.md` | `CLAIM 005` in full; the 17 machine-extracted allele-contrast lines (§ 1.2) | READ-ONLY |
| `registries/working_model_current.md` | the 5 machine-extracted allele-contrast lines; `:156` | READ-ONLY |
| `research/discovery_ledger_current.md` | the 39 machine-extracted allele-contrast lines (§ 1.2) | READ-ONLY |

### 0.2 Primary literature — depth declared per PMID

*(filled in § 4; no primary was fetched before the preregistration was flushed)*

---

## § 1 · BASELINE ENUMERATION — unfiltered first, filtered second, both shown

🔴 **The rule I am obeying, and why.** A filter built from expected terms returns only expected files. So the
population is enumerated **structurally** — by allele-token co-occurrence, a property of the text, not of my
hypothesis — and only then narrowed. Both stages are printed. The enumeration used `find` and `grep`/Python
over the working tree. **No `git grep`, no `git log`, no git command of any kind was run** (hard constraint).

### 1.1 🟢 STAGE 0 — the unfiltered population

| Stratum | Count |
|---|---|
| `*.md` files under `disease-models/wwox/` | **454** |
| ↳ `analysis/` (incl. `orchestration_reviews/`, `near_miss_cases/`, `data/`) | 202 |
| ↳ `research/commit_candidates/` | 111 |
| ↳ `research/fulltext_dossiers/` | 54 |
| ↳ `research/session_evaluations/` | 41 |
| ↳ `research/` (top level, incl. the ledgers) | 21 |
| ↳ `registries/` | 7 |
| ↳ `meta/`, `biomarker_endpoint/`, `therapeutics/`, root, misc | 18 |

**No file class was excluded a priori.** Commit candidates, dossiers and session evaluations were walked on the
same footing as `analysis/` — precisely because
`cerebellar_measurement_census_20260922.md` § 5.1a records that the last actor to skip a stratum
(`research/`) missed an answer the repository held in five places.

### 1.2 🟢 STAGE 1 — structural allele-token enumeration (still unfiltered by meaning)

Twenty allele/model regexes plus three species regexes were matched against every one of the 454 files. The
token set was fixed from the **census's own allele-discipline block**, not from what I expected to find.

| Token | Files (of 454) | | Token | Files |
|---|---|---|---|---|
| WOREE | 159 | | EIIA-Cre / ΔCre | 23 |
| `Wwox`-null / KO | 128 | | Nestin-Cre / `N-KO` | 23 |
| Q230P | 123 | | `c.606-1G>A` | 22 |
| P47T | 114 | | `R264Ter` / `Arg264` | 17 |
| SCAR12 | 105 | | L239R | 16 |
| `lde` | 95 | | BK5-Cre | 11 |
| `gt/gt` / hypomorph | 91 | | `c.517-3` | 5 |
| NCKU `WD1`/`WD234` | 54 | | | |
| G372R | 52 | | | |
| Synapsin-Cre / `S-KO` | 42 | | | |
| P282A | 32 | | | |
| `c.1057-2A>G` | 30 | | | |
| P47R | 28 | | | |

**Files carrying ≥ 2 distinct allele/model tokens: 225.** ≥ 3: **168**. ≥ 5: **100**. Zero tokens: 140.
**Lines carrying ≥ 2 distinct allele/model tokens: 545.** That 545 is the true unfiltered enumeration of
places where this repository puts two WWOX alleles in the same sentence.

### 1.3 🟢 STAGE 2 — the filter, applied second and declared

A contrast-marker regex (`but · whereas · unlike · vs · versus · while · however · contrast · asymmetr ·
differ · only in · not in · never · absent · does/did not · milder · more/less severe · earlier · later ·
surviv`, plus the Italian `ma · mentre · invece · non`) was applied **to the 545 lines**, not to the 454 files.

> **545 lines → 282 lines in 94 files.** 🔴 **263 lines (48 %) were discarded by the filter and I did not
> inspect them all.** That is the filter's declared cost. It is recorded here rather than hidden, because a
> discarded line that asserts a difference without a contrast marker would be invisible to this node.

**Top of the ranked filtered set:**

| Lines | File |
|---|---|
| 39 | `research/discovery_ledger_current.md` |
| 17 | `registries/claim_registry_current.md` |
| 11 | `research/therapeutic_hypotheses_ledger_current.md` |
| 8 each | `registries/paper_registry_current.md` · `analysis/cerebellar_measurement_census_20260922.md` · `analysis/purkinje_cerebellar_celltype_wwox_census_20260922.md` · `analysis/cerebellar_functional_readout_census_20260922.md` |
| 7 | `analysis/wwox_independent_downstream_rescue_20260922.md` |
| 6 each | `analysis/community_continuation_packet_20260922.md` · `analysis/a51_antiproliferative_confound_20260921.md` · `analysis/model_horizon_and_p47t_platform_20260922.md` · `analysis/woree_therapeutic_class_census_20260921.md` · `analysis/tx007_genotype_class_ceiling_20260921.md` |
| 5 each | `research/commit_candidates/CC-20260826-FIVECLAIM-HARDENING-01.md` · `registries/working_model_current.md` · `analysis/seizure_ascertainment_census_20260922.md` |

### 1.4 🟢 STAGE 3 — the enumerated candidate differences, with their prior-art status

**Every asserted allele/model phenotype difference the two stages surfaced.** The right-hand column is the
baseline check the brief demands **before** any novelty is claimed.

| # | The asserted difference | Where | Already harmonized in the repository? |
|---|---|---|---|
| **D1** | **Cerebellar degeneration:** marker-resolved in `P47T`; not in `lde/lde`, Aqeilan-null+AAV, `gt/gt`, Cre conditionals | `cerebellar_measurement_census…` § 4.3 | 🟢 **YES — fully.** This is the brief's anchor. `A — REDISCOVERY` if re-derived |
| **D2** | **Epilepsy:** *"explicitly absent in `Wwox`-null mice"* vs present in `lde/lde` | `CLAIM 037` title; `CLAIM 005` | 🟢 **YES.** `seizure_ascertainment_census…` X-1/X-3: the canonical negative is a **literature survey over four papers that never looked**. Correction queued since 2026-08-26, unapplied |
| **D3** | **`gt/gt` hypomorph mild vs null lethal** — the dose→severity spine | `discovery_ledger:756`; `CLAIM 005` | 🟡 **PARTLY.** Harmonized for **seizures** (X-4, Q3: Table 2's `Epilepsy` row is empty because nobody looked). **Not** harmonized for the motor/neurological axis generally |
| **D4** | **Cerebellum histologically indemne in `lde/lde`** vs foliation + PC loss in NCKU null | `CLAIM 039`; `census` A1/A6 | 🟢 **YES.** `CLAIM 039`'s narrowing already carries `PREMISE: LIGHT_MICROSCOPY_FLOOR` and *"il silenzio a 28 giorni non è mai stato evidenza di normalità cerebellare"* |
| **D5** | **Ataxia:** 95 % in `lde/lde`, defining in SCAR12, **0/13 in WOREE** | `R21`, `H1`, `H6`; `census` § 8 attack 6 | 🟡 **PARTLY, and asymmetrically.** `cerebellar_functional_readout_census…` § 1.4 establishes the WOREE arm is **structurally untestable** (no independent walking, no eye contact, 11/13 non-verbal). But `census` § 8 attack 6 then uses *"no ataxia in 13/13"* as **support for real biology** without applying § 1.4 — see § 6.3 |
| **D6** | **Abundance→severity:** `P47T` normal protein/mild vs `Q230P` undetectable/severe vs `G372R` low/mild | `CLAIM 030`; `DL-MECH-033`; `FM-014` | 🟢 **YES**, and explicitly: `claim_registry:565` — *"le misure di abbondanza confrontate non sono commensurabili (WB fibroblasti … IF organoidi)"*. ⚠️ **Q230P is FORBIDDEN GROUND; not entered** |
| **D7** | **Same residue, opposite class:** `P47T` → SCAR12 mild, `P47R` → WWOX-DEE severe | `DL-MECH-033`; `:836`, `:966` | 🟢 **YES.** `claim_registry:562` records that `P47R` appears **only as the second allele of a compound heterozygote** in trans with `c.46_49del`. No `P47R` homozygote phenotype has ever been observed |
| **D8** | **Osteosarcoma** detected in the Aqeilan null, *"failed to detect"* in other `Wwox`-null rodents | `claim_registry:676` | 🟡 **PARTLY** — the conflict is recorded and the group's own one-sentence disposal is flagged as resting on nothing. Oncological endpoint; outside this node's neuro frame |
| **D9** | **Heterozygote:** no phenotype on measured endpoints | `claim_registry:593` | 🟢 **YES** — the claim itself carries *"nessuna delle fonti misura cognizione, EEG o eccitabilità di rete"* |
| **D10** | **Myelin:** hypomyelination in `lde/lde`, NCKU null, Aqeilan null, `S-KO` | `wwox_myelin_oligodendrocyte_census…` § 1.2 | 🔵 **NOT A DIFFERENCE.** All four models converge. Nothing to harmonize |
| **D11** | **Interneuron number:** PV⁺ −44 % in BK5-Cre full KO; **never counted in any other model** | `CLAIM 005`; `census` § 3.4 (b) | 🟡 **ABSENCE OF COMPARISON, not an asserted difference.** Only one stereology exists in the whole literature |
| **D12** 🎯 | **Motor phenotype of the `Wwox`-null MOUSE:** Aqeilan line reported as having **none**, NCKU `WD1`/`WD234` as having **large, formally compared deficits** | `cerebellar_functional_readout_census…` **§ 1.5** | 🔴 **NO — and it is explicitly flagged as not adjudicated:** *"This is recorded as an unresolved divergence, **not** adjudicated here"* |

⇒ 🎯 **D12 is the only enumerated difference the repository (a) asserts, (b) between two objects of the same
nominal genotype class and species, and (c) explicitly declines to adjudicate.** It is this node's target.
D3 and D5 are the two partial cases and are handled in § 6.3 as secondary results.

---

## § 2 · DIVERGE — the difference × seven rival explanations

🔴 **Rule.** Not one of these is dismissed by assertion. Each gets a discriminator — the observation that
would separate it from its neighbours — because a rival without a discriminator is decoration.

**D12, stated precisely before it is explained.**
**Arm A (negative):** `Wwox^−/−` Aqeilan/Croce line. `PMID 18487609` (2008): *"they did not exhibit any
abnormal behavior or impaired motor skills"* (🔴 SIBLING-ATTESTED, `seizure_ascertainment_census…` § 1a).
Carried forward by `PMID 19500159`'s Discussion: *"neither abnormal behavior nor impaired motor skill was
observed in the Wwox KO mice (Aqeilan et al. 2007)"* (🔴 SIBLING-ATTESTED, `cerebellar_functional_readout_census…` § 1.5).
Restated in 2021 as an impossibility: *"we could not assess behavior of Wwox-null mice due to their poor
conditions and premature death"* (`R8`).
**Arm B (positive):** `Wwox^−/−` NCKU `WD1` (exon 1) **and** `WD234` (exons 2/3/4), two independent strains.
`PMID 32000863` (2020), **P18–20**: rotarod latency *"much shorter"*, one-way ANOVA; ink-paw footprint —
stride length, hind-base width and hind/fore-base ratio all *"significantly decreased"*; hindlimb clasping
abnormal; Tc-MEP amplitude 59.2 ± 9.0 µV (n = 10) → 11.8 ± 5.4 µV (n = 4), *p* < 0.05 (`R1`–`R4`).

| # | Rival explanation | What it predicts | 🎯 Discriminator |
|---|---|---|---|
| **(a)** | **Real biology.** Exon-1 / exon-2-3-4 disruption in the NCKU lines produces a motor phenotype the Aqeilan exons-2–4 deletion does not | A motor deficit measurable in NCKU and **absent when the same instrument is applied** to the Aqeilan line | **Run a rotarod and a footprint on the Aqeilan line at P18–20.** Nothing else settles (a) |
| **(b)** | **Different tissue sampled** | — | 🔵 **Does not apply.** A whole-animal motor battery samples the whole animal. This is the one rival the endpoint class excludes by construction, and saying so is part of the enumeration |
| **(c)** | **Different age / developmental window** | The Aqeilan negative was recorded at an age at which the NCKU deficit is not yet present | Compare the **stated observation ages**. NCKU: P18–20. Aqeilan 2007/2008: necropsy series, death at 2–3 wk — the windows **overlap**; the Aqeilan line is alive at P18–20 |
| **(d)** | 🎯 **Different endpoint / instrument** | The negative is an **unprotocolled husbandry impression**; the positive is a **scored, tested battery**. The two are not the same measurement and cannot disagree | Read both Methods. Does the negative arm name an instrument, a trial count, a scorer, an `n`? |
| **(e)** | **Different detection floor / epitope** | — | 🟡 **Partially applies, transposed.** The behavioural analogue of a detection floor is **sensitivity of the assay**: cage observation cannot resolve a 20 % rotarod latency change. Same discriminator as (d) |
| **(f)** | **Different n, blinding or statistic** | The negative arm has no `n`, no test, no blinding, no pre-specified equivalence margin — so it cannot support *"no difference"* even if it were an instrument | Is an equivalence margin stated anywhere? Is the negative arm's `n` recoverable? |
| **(g)** | **Different species** | 🔵 **Does not apply.** Both arms are *Mus musculus*. ⚠️ **But a sub-rival does:** **different background strain** (Aqeilan line on FVB; NCKU background not yet established by me) and **different colony/husbandry** | Recover both papers' strain statements. If backgrounds differ, (a) and (g′) become **inseparable without a common instrument** |

🔴 **Note the structure of this table, because it is the finding in miniature.** Rivals (b) and (g) are
excluded by the endpoint class; (c) is testable from stated ages alone; (d), (e) and (f) collapse into one
question — *was the negative arm ever an instrument?*; and (a) and (g′) can be separated from each other
**only after** (d) is settled. **So (d) is not one rival among seven. It is the gate.**

---

## § 3 · 🔴 PREREGISTERED PREDICTION — written to disk BEFORE any external query in this act

> **P1 — THE COMPARISON I PREDICT WILL COLLAPSE:** 🎯 **D12.** I predict that the apparent difference in
> **motor phenotype between the Aqeilan-line `Wwox`-null mouse and the NCKU `WD1`/`WD234` `Wwox`-null mice
> is NOT a difference between the alleles.** I predict rival **(d)** will carry it: that the Aqeilan-line
> negative will prove to be an **unprotocolled cage observation with no instrument, no trial structure, no
> scorer, no `n`, no test and no stated equivalence margin**, made in a paper whose declared subject is not
> behaviour — while the NCKU positive is a scored battery with a stated test. **Two arms that are not the
> same measurement cannot disagree, and a difference between them is not evidence about the alleles.**
>
> **P1a — the specific sub-prediction I will be scored on:** the Aqeilan-line papers will contain **no
> rotarod, no footprint/gait kinematics and no scored motor scale in a `Wwox^−/−` animal at any age.**
>
> **P2 — THE COMPARISON I PREDICT WILL SURVIVE AS REAL BIOLOGY:** 🎯 **D3's survival limb only** — the
> difference in **lifespan** between `Wwox^gt/gt` (viable, ~2 years) and every `Wwox`-null rodent (2–4 weeks).
> I predict this survives harmonization because **survival is the single endpoint in this corpus that is
> measured by the same instrument in every model** — the animal is alive or it is not. It has no antibody,
> no epitope, no section plane, no stain, no detection floor, no region of interest and no scorer. It is the
> one place where *"nobody looked"* cannot be the explanation, because husbandry looks every day.
>
> **P2a — the sub-prediction that could break P2:** if the `gt/gt` and null lines are maintained on
> different background strains, or if `gt/gt` survival is reported only as a cohort maximum rather than a
> curve, then even survival is not instrument-free and P2 weakens.
>
> **P3 — a prediction against my own interest, so that P1 cannot be scored as a costless win:** I predict
> that harmonizing D12 will **NOT** establish that the Aqeilan-line null has a motor deficit. It will
> establish only that **no comparison has ever been made.** A dissolved difference is not a discovered
> identity. If § 4 lets me write *"the Aqeilan null is ataxic too"*, I have over-read it.
>
> **P4 — what would REFUTE P1 outright:** a rotarod, footprint, beam, catwalk, ledge or scored motor scale,
> administered to a `Wwox^−/−` animal of the Aqeilan line, with an `n` and a test, returning a negative.
> **If that exists, D12 is real biology and my prediction is wrong.** I looked for it in § 4.

🔴 **Flushed to disk before the first external query of this act. §§ 4–10 were appended afterwards.**

---

## § 4 · THE SEARCH, AND THE PREDICTION SCORED AGAINST IT

### 4.0 Read depth of the primaries, declared before the findings (completing § 0.2)

**According to PubMed**, with DOIs as links. 🟢 = served body read by me, first-hand, this act.

| PMID | Model | Depth **in this act** | Note |
|---|---|---|---|
| **34747138** Repudi 2021 *EMBO Mol Med* · PMC8649866 · [DOI](https://doi.org/10.15252/emmm.202114599) | `Wwox`-null **Aqeilan line** + AAV9 | 🟢 **FIRST-HAND, full body** | The decisive Methods and Results for Arm A |
| **32000863** Cheng 2020 *Acta Neuropathol Commun* · PMC6990504 · [DOI](https://doi.org/10.1186/s40478-020-0883-3) | `Wwox`-null **NCKU `WD1` / `WD234`** | 🟢 **FIRST-HAND, full body** | The decisive Methods for Arm B |
| **19936220** Ludes-Meyers 2009 *PLoS ONE* · PMC2777388 · [DOI](https://doi.org/10.1371/journal.pone.0007775) | `Wwox^ΔCre` EIIA-Cre germline null | 🟢 **FIRST-HAND, full body** | A **third** null line; its complete Methods list is the control for "did anyone look?" |
| **17360458** Aqeilan 2007 *PNAS* · PMC1820689 · [DOI](https://doi.org/10.1073/pnas.0609783104) | `Wwox`-null Aqeilan line, origin paper | ⚫ **BLOCKED — `full_text: ""`**, reproduced by me this act | 🔴 A **fourth** independent confirmation of a zero-length body at a valid PMCID |
| **18487609** Aqeilan 2008 *JBC* · PMC2490770 · [DOI](https://doi.org/10.1074/jbc.M800855200) | same | ⚫ **BLOCKED — `full_text: ""`**, reproduced by me this act | 🔴 **The paper carrying the negative sentence is the one I cannot read.** Stated before the finding, not after |
| **17823927** Ludes-Meyers 2007 · PMC4143238 · [DOI](https://doi.org/10.1002/gcc.20497) | `Wwox^gt/gt` | 🟡 **ABSTRACT-DEPTH** | Used for P2 only |
| **10356397** Crabbe, Wahlsten & Dudek 1999 *Science* 284:1670–2 · [DOI](https://doi.org/10.1126/science.284.5420.1670) | — | 🟡 **ABSTRACT-DEPTH** | § 4.4 |
| **24152123** Miller, Hawkins, McCollom & Kearney 2014 *Genes Brain Behav* 13:163–72 · PMC3930200 · [DOI](https://doi.org/10.1111/gbb.12099) | *Scn1a*⁺/⁻ | 🟡 **ABSTRACT-DEPTH** | § 4.4 |
| **16921370** Yu *et al.* 2006 *Nat Neurosci* 9:1142–9 · [DOI](https://doi.org/10.1038/nn1754) | *Scn1a*⁺/⁻ | 🟡 **ABSTRACT-DEPTH** | § 4.4 — ⚠️ cited **only** for background-dependence of survival. Its interneuron material is adjacent to parked ground and is **not entered** |

🔴 **No Scholar Gateway passage was used. No preprint server, no publisher landing page, no author
correspondence, no data request.** Retrieval was PubMed/PMC only.

### 4.1 🎯 ARM A — the Aqeilan line, read first-hand. **The negative is not an instrument.**

**Finding A-1 — the 2021 paper states the exclusion in its own words.** 🟢 First-hand, verbatim,
`PMID 34747138`, Results, *"Behavioral and motor functions"*:

> *"We next explored the behavioral changes in `Wwox`-null mice after restoration of WWOX in neurons.
> **Unfortunately, we could not assess behavior of `Wwox`-null mice due to their poor conditions and
> premature death.** We hence performed open-field, elevated plus maze (EPM), and rotarod tests to
> examine anxiety and motor coordination **in WT and rescued mice**."*

⇒ **The untreated null is excluded from the entire motor battery, by the paper's own sentence.**
Every motor comparison in that paper is *rescued vs wild type*. There is no null arm.

**Finding A-2 — 🎯 and the stated reason is not the operative one.** 🟢 First-hand, same paper,
Figure 6 legend and Results: the open field, EPM and rotarod were run at **8–10 weeks**, with an
additional open field at **8–9 months**. The `Wwox`-null mouse of this line dies at **< 4 weeks**
(same paper: *"Since KO mice died within less than 4 weeks, we could not perform in vivo recordings in
adult KO mice"*).

> 🎯 **The motor battery was scheduled at an age the untreated null cannot reach. The animal is not
> too sick to be tested at 8–10 weeks; it is dead at 8–10 weeks.** The exclusion is a **calendar**
> fact before it is a welfare fact — and a calendar is a sampling frame.
> 🔴 `git grep` was not available to me, but a working-tree grep for `8-10 weeks` / `8–10 weeks`
> across all 454 files returns **0**. Positive control: `FVB` → **14 files**, `could not assess
> behavior` → **7 files**. **The repository holds the excuse and has never held the age.**

**Finding A-3 — the Aqeilan-line rotarod protocol, 🟢 first-hand, for the harmonization table.**
*"5 rpm to 40 rpm for 99 s … three trials separated by 20 min. The initial trial was considered as
training … If the animal did not fall from the device by 240 s … the trial was terminated."*

**Finding A-4 — the one motor readout the null DOES receive, and what it is.** 🟢 First-hand:
*"WWOX single ICV injection improved motor coordination in rescued mice as presented by **hindlimb
clasping test** (Appendix Fig)."* 🔴 The Appendix is not served; whether an **untreated-null** clasping
arm exists is `UNKNOWN` and is already queued in this repository as **`FT-152`**. ⚠️ And the
repository already holds, independently, that **hindlimb clasping is not a test of coordination**
(`cerebellar_functional_readout_census…` `R10`). A clasping arm, if it exists, would not close D12.

**Finding A-5 — the background, 🟢 first-hand.** *"Generation of `Wwox`-null mice (KO) was previously
reported, and these mice were **maintained in an FVB background**."* Keep this; § 6 turns on it.

**Finding A-6 — a third null line, read first-hand as a control on "did anyone look?"**
`PMID 19936220` (`Wwox^ΔCre`, EIIA-Cre, Aldaz laboratory) enumerates its complete Methods:
*Animal Husbandry · Gene Targeting · Generation of KO Mice · Western Blot · Mouse Necropsy and
Histological Analyses · Bone Analyses.* 🔴 **No behavioural method, no motor test, no observation
protocol, no scored endpoint of any kind.** Its only brain measurement is organ weight (Table 2:
0.390 → 0.356 g absolute; 5.0 % → 8.5 % relative; *p* = 0.0003 — ⚠️ driven by the collapsed
denominator, a caveat `claim_registry_current.md:668` already carries correctly).

> 🎯 **So the sampling frame is consistent across two independent null lines from two laboratories:
> the motor system was never instrumented.** That is the same convergence structure the cerebellar
> census found for the hippocampus-spanning block — a **field convention**, not one group's lapse.

### 4.2 🎯 ARM B — the NCKU lines, read first-hand. **And it contains the fact that decides the node.**

**Finding B-1 — the battery, its age, and its training load.** 🟢 First-hand, `PMID 32000863`,
Methods, verbatim: *"The tests for motor coordination and balance were performed in mice at **18–20
days of age**."* Rotarod: *"acclimatized … at 5 rpm for 5 min … **four trials per day for three
consecutive days** … prior to data acquisition"*; accelerating arm *"4 rpm … to 40 rpm over 5 min …
**two trials each day for five consecutive days**"*. Footprint: fore paws red, hind paws blue,
enclosed runway, *"at least five steps … for each mouse"*; **stride length, base width, hind/fore-base
ratio**. Statistics: one-way ANOVA, α = 0.05.

⇒ 🎯 **A `Wwox`-null mouse that dies before one month was successfully put through eight consecutive
days of handling plus a gait assay, at P18–20.** The Aqeilan line's *"poor conditions"* rationale is
therefore not a general fact about `Wwox`-null mice. **It is a fact about one colony, or about a
schedule.**

**Finding B-2 — 🎯 THE DECISIVE SENTENCE, and it is a strain-construction sentence, not a result.**
🟢 First-hand, `PMID 32000863`, Methods § *"Wwox gene knockout mice, rotarod performance and footprint
analysis"*, verbatim:

> *"**A previous study has developed a `Wwox` knockout mouse model by targeting exons 2/3/4.** To test
> if the possibly generated aberrant protein may cause phenotypes due to the presence of exon 1 in the
> mouse genome, **we generated both exon 1- and exon 2/3/4-targeting knockout mouse strains for
> comparison** (`WD1` or `WD234` henceforth, respectively)."*

and, in Results:

> *"**We performed rotarod tests and footprint assay with both `WD1` and `WD234` mice and obtained
> similar results.**"*

⇒ 🎯 **`WD234` is an independent re-derivation of the SAME targeting design as the Aqeilan line —
exons 2/3/4 — built explicitly *for comparison*. And when that design is given a rotarod and a
footprint, it produces a formally compared motor deficit.**

> 🔴 **Therefore rival (a) — "real biology of the allele" — cannot be carried by the targeting
> strategy.** The exons that are deleted are the same exons. Whatever differs between Arm A and Arm B,
> it is not *which exons were removed*.
> ⚠️ **Declared weakness, and it is real.** The extractor strips reference markers, so *"a previous
> study"* is an **unresolved citation** on the served body. That it denotes `PMID 17360458`
> (Aqeilan 2007, exons 2–4) is an **inference**, supported by (i) the sentence itself stating the prior
> study targeted 2/3/4, (ii) `WD1` being the paper's *own* exon-1 line, so the prior study is not the
> exon-1 one, and (iii) this repository's independent record of the Aqeilan allele as exons 2–4
> (`seizure_ascertainment_census…` § 1a). 🔴 **It is an inference over a stripped citation and it is
> tagged as one. If it is wrong, § 5 weakens but § 4.1 does not.**

**Finding B-3 — 🔴 and I must bound Arm B against my own interest, twice.**
1. 🔴 **The `n` for the rotarod and footprint is NOT in the running text.** Figure-legend values are
   not extractable on this surface (the known extractor defect). Tc-MEP has an `n` (WT 59.2 ± 9.0 µV,
   n = 10; KO 11.8 ± 5.4 µV, n = 4; *p* < 0.05); the **motor battery does not**. Do not quote an `n`
   for the rotarod or the footprint from this file.
2. 🔴 🎯 **The one control a dwarfed animal's gait assay most needs is `data not shown`.** Verbatim:
   *"Similar results were obtained when analyzing **the ratio of stride length or hind-base width to
   the body size (data not shown)**."* ⇒ The `Wwox`-null mouse is *"severely dwarf"* in the same
   paper. **A shorter stride in a shorter animal is not a coordination finding until it is normalised,
   and the normalisation is withheld.** `PREMISE: NORMALISATION_NOT_SHOWN`.
   ⚠️ **This weakens the arm I am using as the positive.** It is stated here, before § 5 uses it.
3. 🔴 **The NCKU background strain is NOT STATED anywhere in the served body.** I searched the whole
   text: the Methods say only *"Mice were maintained on standard laboratory chow and water ad libitum
   in a specific pathogen-free environment."* **No strain, no backcross generation, no F-number.**

### 4.3 The negatives produced this act, each with its query and a firing positive control

| Query / probe | Result | Positive control | Carried? |
|---|---|---|---|
| Working-tree grep, all 454 files, `8-10 weeks` / `8–10 weeks` | **0** | `FVB` → 14 files; `could not assess behavior` → 7 files | **CARRIED** — the Aqeilan motor-battery age is repo-absent |
| Working-tree grep, `three consecutive days` · `five consecutive days` | **0** · **0** | `99 s` → 2 files (the rotarod speed protocol IS partly held) | **CARRIED** — the NCKU training load is repo-absent |
| Working-tree grep, `Crabbe` · `Wahlsten` · `modifier loci` · `IMPC` · `Mouse Phenotyping` | **0** each | `Scn1a` → 5 files, `Dravet` → 1 file | **CARRIED** — see § 4.4; the adjacent method is not held |
| Working-tree grep, `Scn1a` / `Dravet` contexts inspected one by one | **all 5 + 1 are PubMed *positive-control query tokens*** inside other censuses | — | **CARRIED** — the *Scn1a* **modifier** literature has never been read into this repository |
| PubMed `(Crabbe JC[Author]) AND (genetics of mouse behavior laboratory environment)` | 3 returned of 14 | — | 🔴 **DISCARDED** — did not return the target. The target was found only by a differently-formed query (`10356397`). **Recorded as a retrieval-form failure, not a literature absence** |
| PubMed `International Mouse Phenotyping Consortium standardized adult phenotyping pipeline` | **0** | the translation shows every term expanded | 🔴 **DISCARDED.** I therefore assert **nothing** about IMPC pipeline ages — see § 7 item 8 |
| PMC fetch `PMC2490770` (Aqeilan 2008) | `full_text: ""` | `PMC2777388` and `PMC8649866` and `PMC6990504` all served full bodies in the same session | **CARRIED** as a retrieval block, not a content finding |
| PMC fetch `PMC1820689` (Aqeilan 2007) | `full_text: ""` | as above | **CARRIED** as a retrieval block |

### 4.4 🎯 CONNECT_DOMAINS — the adjacent literature owns this method, and it cuts against me

> **The *SCN1A* / Dravet mouse literature is the adjacent field that has already run this exact
> problem — one allele, two laboratories, opposite phenotypes — and its answer is NOT "measurement
> artefact".**

**According to PubMed**, 🟡 abstract-depth, verbatim:

> `PMID 24152123` (Miller, Hawkins, McCollom & Kearney 2014, *Genes Brain Behav*,
> [DOI](https://doi.org/10.1111/gbb.12099)): *"**Phenotype severity in `Scn1a^(+/−)` mice is strongly
> dependent on strain background. On the 129S6/SvEvTac strain `Scn1a^(+/−)` mice exhibit no overt
> phenotype, whereas on the (C57BL/6J × 129S6/SvEvTac)F1 strain `Scn1a^(+/−)` mice exhibit spontaneous
> seizures and early lethality.**"* The field's response was to run genome scans and **map** the
> modifier loci (chromosomes 5, 7, 8, 11), not to dissolve the difference.
>
> `PMID 16921370` (Yu *et al.* 2006, *Nat Neurosci*, [DOI](https://doi.org/10.1038/nn1754)), for the
> same point at source: *"Heterozygous `Scn1a^(+/−)` mice had spontaneous seizures and sporadic deaths
> beginning after P21, **with a notable dependence on genetic background**."*
>
> `PMID 10356397` (Crabbe, Wahlsten & Dudek 1999, *Science*,
> [DOI](https://doi.org/10.1126/science.284.5420.1670)): *"Apparatus, test protocols, and many
> environmental variables were **rigorously equated** … **despite standardization, there were
> systematic differences in behavior across labs.** For some tests, the magnitude of genetic
> differences depended upon the specific testing lab. Thus, experiments characterizing mutants may
> yield results that are **idiosyncratic to a particular laboratory**."*

| | |
|---|---|
| ✅ **WHAT TRANSFERS** | **(1)** The problem shape is identical and has a name in that field: *same allele, different site, different phenotype*. **(2)** Its first move is the one this node makes — **state the background and the instrument before attributing anything to the allele.** **(3)** 🎯 Crabbe supplies the hard boundary on my own conclusion: **harmonizing the instrument does not guarantee agreement**, so "apply the same test to both lines" is necessary and *not* sufficient. **(4)** Kearney supplies the constructive alternative — an unexplained cross-line difference is a **modifier-mapping opportunity**, i.e. a finding, not a defect |
| ❌ **WHAT DOES NOT TRANSFER** | **(1)** *Scn1a*⁺/⁻ mice **live**; modifier mapping needs backcross generations and survival curves over months. A `Wwox`-null mouse dies at 2–4 weeks, so a *Wwox* modifier cross is a far heavier object and **nothing in this node proposes one.** **(2)** The *Scn1a* comparison is **within one allele across backgrounds**; mine is **across two independently derived lines**, which confounds background with derivation and with laboratory. **(3)** 🔴 The **gene, protein, pathway and mechanism transfer NOTHING.** *SCN1A* is a sodium channel; *WWOX* is not. Only the **epistemic method** is borrowed, and no biological inference crosses |

🔴 **And this is the part that costs me.** The adjacent literature's best-documented answer to *"two
labs, one nominal genotype, opposite phenotype"* is **genetic background — a real biological cause.**
So connect_domains did **not** support my preregistration. It supplied the strongest surviving rival.
That is recorded in § 6 and it changes the verdict's wording.

### 4.5 🔴 THE PREDICTION, SCORED

| | Prediction | Outcome | Score |
|---|---|---|---|
| **P1** | D12 collapses; the Aqeilan-line negative is an unprotocolled observation, not an instrument, so the two arms cannot disagree | 🟢 **CONFIRMED on the operative half, first-hand.** The 2021 paper excludes the null from the battery in its own sentence; the battery's age (8–10 weeks) is past the line's lifespan (< 4 weeks); the 2009 `ΔCre` line's complete Methods contain no behavioural assay at all. **No motor instrument has ever been applied to an untreated `Wwox`-null animal of the Aqeilan line.** 🔴 **INCOMPLETE on the explanation:** I predicted **one** confound and there are **two** — the instrument asymmetry **and** an unrecorded background on the NCKU side (§ 4.2 B-3.3), with a strong adjacent precedent (§ 4.4) that background alone can flip a phenotype | 🟡 **CORRECT BUT UNDER-SPECIFIED** |
| **P1a** | No rotarod, footprint or scored motor scale in a `Wwox^−/−` Aqeilan-line animal at any age | 🟢 **NOT FALSIFIED, to the depth obtainable.** 🔴 **Bound:** the two origin papers (`17360458`, `18487609`) return `full_text: ""`, so P1a is first-hand for 2021 and sibling-attested for 2007/2008 | 🟡 **SUPPORTED, BOUNDED** |
| **P2** | The `gt/gt`-vs-null **lifespan** difference survives as real biology, because survival has no instrument-dependence | 🟢 **SURVIVES — and narrowed.** `PMID 17823927` states first-hand (abstract) that `Wwox^gt/gt` mice *"are **viable** in contrast to the recently reported postnatal lethality of `Wwox` knockout mice"* while having *"a significantly shorter lifespan"*; three independent null lines report death at 2–4 weeks, one with a per-timepoint mortality series (`19936220`: 43 % by 72 h, 77 % by d17) and one with a log-rank Kaplan–Meier (`34747138`). 🔴 **Narrowing I did not predict:** the **categorical** fact survives; the **magnitude** does not, because **no head-to-head survival curve of `gt/gt` against a null in a common colony has ever been run**, and the repository's *"2 years"* figure for `gt/gt` comes from `PMID 19500159`'s **Table 2 — the same survey table whose `Epilepsy` row is a proven ascertainment artefact** (`seizure_ascertainment_census…` X-4) | 🟢 **CORRECT, NARROWED** |
| **P2a** | P2 weakens if backgrounds differ or if `gt/gt` survival is a cohort maximum | 🔴 **TRIGGERED, partially.** The *"2 years"* is survey-derived, which is P2a's second limb exactly | 🟢 **THE SAFEGUARD FIRED** |
| **P3** | Harmonization will NOT show the Aqeilan null is ataxic; it will show no comparison exists | 🟢 **HELD, and it is the correct reading.** Nothing in § 4 licenses a motor phenotype in the Aqeilan line. Arm B's own body-size normalisation is `data not shown`, so even the positive arm does not license *"the `Wwox`-null mouse is ataxic"* without its model named | 🟢 **HELD** |
| **P4** | A scored motor test on an Aqeilan-line `Wwox^−/−`, with `n` and a test, returning a negative, would refute P1 | 🔴 **NOT FOUND.** The nearest object is `PMID 34747138` Appendix Fig S3 (hindlimb clasping), 🔴 **unread, `FT-152`** — and clasping is not a coordination test | **NO REFUTER FOUND; one candidate unread** |

---

## § 5 · THE ONE COMPRESSED CASE, AND THE SINGLE CHEAPEST ACT

### 5.1 The case, stated as the corrected comparison

> 🎯 **BEFORE harmonization:** *"Two `Wwox`-null mouse reports disagree on whether the null mouse has
> a motor phenotype at all"* (`cerebellar_functional_readout_census_20260922.md` § 1.5).
>
> 🎯 **AFTER harmonization:** **There is no disagreement, because there is no comparison.** One arm
> was given a rotarod, an accelerating rotarod and a three-parameter ink-paw gait assay at P18–20,
> with a stated test. The other arm was given **no motor instrument at any age**, and its battery was
> scheduled at 8–10 weeks — after the animals were dead. **A scored battery and an empty Methods
> section cannot disagree.** 🔴 **And the same targeting design — exons 2/3/4 — sits on both sides:
> `WD234` and the Aqeilan line delete the same exons, and `WD234` shows the deficit.**

🔴 **This is recorded as USEFUL NEGATIVE EVIDENCE, prominently, because a dissolved difference is a
result:** the repository may no longer treat *"the Aqeilan `Wwox`-null mouse has no motor
phenotype"* as evidence about the allele, in either direction. It is evidence about a Methods section.

⚠️ **§ 16 check, run before the case was chosen and reported whether or not it flattered the case.**
The **positive** arm has a measured explanandum — a stated instrument, a stated test (one-way ANOVA),
three named gait parameters and a stated step count. 🔴 **But its `n` is figure-bound and its
body-size normalisation is `data not shown`**, so the explanandum is *tested* without being *fully
bounded*. The **negative** arm has **no explanandum at all**. ⇒ The comparison passes § 16 **only in
the direction I am using it** — to establish that no comparison exists. 🔴 **It would fail § 16 if it
were used to assert that the `Wwox`-null mouse is ataxic. It is not so used.**

### 5.2 🎯 THE SINGLE CHEAPEST ACT — zero new animals, zero external contact, executable now

> 🎯 **Read two supplementary files that this repository already knows about, and the case closes to
> the limit of what reading can close.**

| # | Object | What it closes | Cost |
|---|---|---|---|
| **1** | **`PMID 34747138` Appendix** (already queued here as **`FT-152`**) | Whether an **untreated-null** arm exists in the P17/P19 hindlimb-clasping panel. This is the **only** candidate refuter of `P1a` that anyone has named. It also carries the Appendix Table this repository wants for a *different* node, so the acquisition is **already justified twice** | 🟢 one retrieval |
| **2** | **`PMID 32000863` Additional file** (Figures S1–S9) | The **`n`** for the rotarod and footprint cohorts, and whether the withheld **body-size-normalised** gait data are in the supplement rather than absent. Both are § 4.2 B-3 bounds | 🟢 one retrieval |

**Cost card, in the form this repository uses.**

| Criterion | Verdict |
|---|---|
| **Reagent exists?** | 🟢 n/a — a reading act. No reagent consumed |
| **Sample exists?** | 🟢 n/a — no tissue touched |
| **Technique exists?** | 🟢 **YES** — PMC retrieval, validated on three full bodies in this act |
| **Readout interpretable?** | 🟢 **YES, mechanically.** A figure legend either prints an `n` or it does not; a panel either has a KO arm or it does not. No inference step |
| **Comparator exists?** | 🟢 **YES** — the NCKU battery, already read first-hand |
| **New animals?** | 🟢 **NO. Zero.** |
| **External contact?** | 🔴 **NONE MADE, none recommended as an act of mine.** Both objects are supplementary files of open-access articles; neither requires writing to anyone |
| **CLASS** | 🟢 **EXECUTABLE NOW** |

🔴 **What this act does NOT do, stated plainly:** it **bounds** the case; it does not **resolve** it.
No amount of reading can produce a rotarod trace that was never run.

### 5.3 🎯 And the act that would actually resolve it — named, costed, and NOT executed

> 🎯 **Add an ink-paw footprint to a P18 session that is already happening.**

`PMID 42422765` (Obeid 2026, TX-007) scores **hindlimb clasping at P18** in the Aqeilan line and
calls the result *"ataxia scores"* (`cerebellar_functional_readout_census…` `R10`). **That is a
running, funded protocol that already has Aqeilan-line animals in hand, awake, at exactly the age
`PMID 32000863` used.**

| Criterion | Verdict |
|---|---|
| **Reagent exists?** | 🟢 **YES, and it is the cheapest instrument in the entire corpus** — *"nontoxic water-based red ink"*, blue ink, an enclosed runway, white paper (`PMID 32000863` Methods, 🟢 first-hand) |
| **Sample exists?** | 🟢 **YES — the animals are already in the P18 session.** No new cohort |
| **Technique exists?** | 🟢 **YES, published, and already validated in a `Wwox`-null mouse at P18–20** |
| **Readout interpretable?** | 🟢 **YES** — three parameters with an existing comparator dataset. ⚠️ **And it must be reported normalised to body size**, which is the exact control `PMID 32000863` withheld |
| **Comparator exists?** | 🟢 **YES** — `WD1` and `WD234` at the same age, same three parameters |
| **New animals?** | 🟢 **NO**, if bolted onto the existing session. 🔴 **YES**, if run as a standalone cohort |
| **External contact?** | 🔴 **HUMAN_REQUIRED. No author, laboratory or foundation was contacted, and no correspondence was drafted. This route is FROZEN** |
| **CLASS** | 🟡 **MINOR ADAPTATION** — a published, non-invasive assay moved onto an existing session |

🔴 **And per § 4.4, even this would not settle rival (g′).** Two lines on two backgrounds, harmonized
on one instrument, can still differ for Crabbe's reason. **The honest ceiling of a harmonized
footprint is: it converts an uninterpretable absence into an interpretable difference.** That is worth
doing and it is not a proof.

---

## § 6 · ADVERSARIAL VERIFICATION OF MY OWN BEST FINDING

🔴 **§ 21 applied to myself.** My finding is attractive in three of the four dangerous ways: it closes
a debate neatly, it converts an absence into a methodological lesson, and it makes a sibling file's
open item my own closed one. **So I assumed it was wrong and attacked it seven times. Four attacks
landed.**

| # | Attack | Outcome |
|---|---|---|
| **1** | 🔴 **"You never excluded genetic background, and the adjacent literature you yourself imported says background alone flips phenotypes."** | 🔴 **LANDS, HARDEST, AND IT CHANGES THE VERDICT.** Arm A is **FVB** (🟢 first-hand). Arm B's background is **NOT STATED** anywhere in the served body (🟢 first-hand negative). `PMID 24152123` shows one *Scn1a* allele going from *"no overt phenotype"* to *"spontaneous seizures and early lethality"* on a background change alone. ⇒ **I must not write "the difference is an artefact."** The defensible statement is weaker and is what § 5.1 says: **the difference is UNATTRIBUTABLE — two confounds, not one, and one of them (instrument) is total while the other (background) is unrecorded on one side** |
| **2** | 🔴 **"This is a re-derivation of `cerebellar_functional_readout_census…` § 1.5, which already named the divergence AND already listed your rivals."** | 🟡 **LANDS, AND IT IS THE MAIN REASON FOR MY GRADE.** § 1.5 states verbatim: *"Different targeting strategies, different backgrounds, different ages, different laboratories."* **Four of my seven rivals are one sentence of a sibling file.** What is *not* there: the battery **ages** on both sides, the `WD234`/Aqeilan **exon identity**, the **FVB vs NOT STATED** asymmetry, and the withheld body-size normalisation. **The frame is inherited; four facts are new** |
| **3** | 🔴 **"Your decisive sentence (B-2) rests on a citation the extractor deleted."** | 🔴 **LANDS.** *"A previous study"* has no resolvable referent on the served surface. The identification is an inference (§ 4.2, three supports, tagged). 🔴 **If it is wrong, § 5.1's exon-identity clause falls — but § 4.1 does not, and § 4.1 alone carries the instrument asymmetry** |
| **4** | 🔴 **"You cannot read the paper that carries the negative."** | 🔴 **LANDS, and it was declared in § 4.0 before the finding.** `PMC2490770` and `PMC1820689` both return `full_text: ""`. My first-hand evidence for Arm A is the **2021** paper; the 2007/2008 sentences are **SIBLING-ATTESTED**. ⚠️ If the 2008 Methods contain a scored motor protocol nobody has seen, `P1a` fails |
| **5** | **"Your positive arm's key control is `data not shown`, so you are comparing an empty Methods section to an unnormalised one."** | ✅ **SURVIVES BECAUSE I CONCEDED IT FIRST** (§ 4.2 B-3.2) and because it **strengthens** the verdict rather than weakening it: if even the positive arm does not license *"ataxic"*, then the dissolved comparison is **doubly** a negative result, which is what § 5.1 records |
| **6** | 🎯 **"The strongest counter-argument to your own conclusion: maybe the Aqeilan line really is too sick to test, and the NCKU colony is simply healthier — so the instrument asymmetry is a rational response to biology, not a blind spot."** | 🟡 **THIS IS THE BEST OBJECTION AND IT DOES NOT FULLY DIE.** It has real support: the Aqeilan line's own 2021 paper cites *"poor conditions"*, and the two colonies may genuinely differ in severity. 🔴 **But it fails as a complete explanation for one reason that is a calendar, not a judgement: the battery was scheduled at 8–10 weeks.** A test at 8–10 weeks is not a test that a P18 animal was too sick for; it is a test that was never offered at P18. ⇒ **The objection survives as a partial explanation for the 2021 exclusion; it explains nothing about 2007, 2008 or 2009, whose Methods contain no behavioural assay at any age** |
| **7** | 🔴 **"You are doing exactly what the anchor census warned about — converting `NOT MEASURED` into a finding."** | ✅ **SURVIVES, but only because the output is a negative.** I propose no mechanism, no biology and no new phenotype. The deliverable is *"this comparison does not exist"*, which is the **removal** of a finding, not the creation of one. 🔴 **The moment anyone cites this file for "the Aqeilan null is ataxic", the attack lands and the file has been misused** |

**Net effect of the adversarial pass.** My headline moved from *"the difference is a measurement
artefact"* to *"the difference is **unattributable**: the instrument asymmetry is total, the
background is unrecorded on one side, and the adjacent literature says background alone can produce
it."* **That is a loss for my preregistration and it is recorded as one.**

---

## § 7 · WHAT I COULD NOT VERIFY — exhaustive

1. 🔴 **`PMID 18487609` (Aqeilan 2008) body** — `PMC2490770` → `full_text: ""`, reproduced this act. **The sentence the entire negative arm rests on is one I have not read.** SIBLING-ATTESTED only.
2. 🔴 **`PMID 17360458` (Aqeilan 2007) body** — `PMC1820689` → `full_text: ""`, reproduced this act. Whether any observational protocol exists there is `NOT STATED`, not `NO`.
3. 🔴 **The referent of `PMID 32000863`'s *"a previous study"*** — reference markers stripped by the extractor. § 4.2 B-2's exon identification is an inference.
4. 🔴 **The NCKU background strain** — absent from the served body. Rival (g′) cannot be excluded or confirmed. This is the single most consequential unknown in the file.
5. 🔴 **The `n` for `PMID 32000863`'s rotarod and footprint cohorts** — figure-bound, not extractable.
6. 🔴 **`PMID 32000863`'s body-size-normalised gait data** — `data not shown` in the running text; whether the Additional file carries them is unknown.
7. 🔴 **`PMID 34747138` Appendix Fig S3** — whether an untreated-null clasping arm exists. Queued `FT-152`, unread. **The only named candidate refuter of `P1a`.**
8. 🔴 **Anything at all about IMPC / EMPReSS standardized phenotyping pipeline ages.** My query returned **0** with every term correctly expanded. 🔴 **I therefore assert nothing about them, including the age-incompatibility argument I expected to make.** It is removed, not softened.
9. 🔴 **`PMID 33914858` (`Nes-Cre` / `Syn-Cre` conditionals)** — no PMCID; the local PDF is `SUSPECT` and its reading is SUSPENDED (`FT-044`). **The conditional lines are absent from this node in both directions and I assert nothing about them.**
10. 🔴 **`PMID 19500159` (Suzuki 2009)** — licence-blocked, `pmc_id: null`. Its Discussion sentence carrying the Aqeilan negative forward, and its Table 2 lifespan figure for `gt/gt` (P2), are both **SIBLING-ATTESTED**.
11. 🔴 **`PMID 17823927` (`gt/gt`) body** — abstract-depth. P2 rests on one abstract sentence plus a survey table.
12. 🔴 **Whether `PMID 42422765`'s P18 clasping session could in fact accommodate a footprint runway** — an operational question about someone else's protocol. `HUMAN_REQUIRED`. **Not asked.**
13. 🔴 **263 of the 545 allele-contrast lines** (§ 1.3) were removed by the contrast-marker filter and not individually inspected. An asserted difference phrased without a contrast marker is invisible to this file.
14. ⚠️ **Whether the Aqeilan and NCKU colonies differ in severity** (attack 6) — untestable from published text.

---

## § 8 · NOVELTY GRADE — conservative

> ### 🔵 **B — TRIVIAL INFERENCE.** An adjudication of a divergence a sibling file had already named and already supplied the rival list for, plus four repo-absent first-hand facts and one genuinely new adjacent-domain import.

**Why not higher.** Attack 2 lands. `cerebellar_functional_readout_census_20260922.md` § 1.5 named
the divergence **and** listed *"different targeting strategies, different backgrounds, different ages,
different laboratories"* in one sentence. **My § 2 divergence table is, in its substance, that
sentence with discriminators attached.** Attaching discriminators is real work and it is not
discovery. Per the brief's baseline rule, the *frame* is graded **`A — REDISCOVERY`**.

**Why not lower.** Five components are repo-absent, verified by working-tree grep with firing positive
controls, and each changes what a reader should do:

| Sub-finding | Grade | Why |
|---|---|---|
| 🎯 **The Aqeilan-line motor battery is scheduled at 8–10 weeks, in a line that dies at < 4 weeks** — `8-10 weeks` → **0** files, against `could not assess behavior` → 7 | 🟢 **C — NOVEL CONNECTION** | Converts *"too sick to test"* into *"tested after death"*. It moves the exclusion from a welfare judgement, which cannot be argued with, to a **schedule**, which can. It is also what defeats attack 6 |
| 🎯 **`WD234` deletes the same exons (2/3/4) as the Aqeilan line and was built explicitly *"for comparison"* — and it shows the deficit** | 🟢 **C — NOVEL CONNECTION**, ⚠️ bounded by attack 3 | Removes the targeting strategy from the rival set. The repository held both exon identities separately and never put them in the same sentence |
| 🎯 **The *Scn1a* strain-background modifier literature, imported as the adjacent method** — `Crabbe` · `Wahlsten` · `modifier loci` · `IMPC` → **0** files each; the 5 `Scn1a` hits are all query tokens | 🟢 **C — NOVEL CONNECTION** | It is the first time this repository has an *external* precedent for *"one allele, two labs, opposite phenotype"* — and it argues **against** the importer, which is the useful kind |
| **FVB (stated) vs NOT STATED** — the background asymmetry | 🔵 **B** | Both halves were on the served surfaces; the juxtaposition and its consequence are new |
| **`PMID 32000863`'s body-size normalisation is `data not shown`** | 🔵 **B** | A bound on the corpus's only quantitative gait dataset. Narrow, and it weakens a result the repository leans on |
| **The D12 adjudication itself** | 🔵 **A/B** | High operational value, low novelty. Adjudicating a sibling's explicitly open item is service, not discovery |
| **P2 — the `gt/gt`-vs-null lifespan difference survives as real biology** | 🔵 **A — REDISCOVERY**, with a **B** narrowing | That `gt/gt` is viable and nulls are not is in the 2007 abstract. 🎯 **New only in the narrowing:** the repository's *"2 years"* figure is sourced to the **same survey table** already proven to be an ascertainment artefact for a different row |

🔴 **Nothing here is `D`, `E` or `F`.** No new hypothesis about WWOX biology is proposed, no mechanism
is named, no experiment discriminating between mechanisms is designed, and no therapeutic direction is
opened or closed. **The entire scientific output of this file is one negative and one survival.**

🔴 **Words I checked before writing and did not write:** *first*, *novel*, *absent*, *untested*,
*unique* are used in this file **only** where a grep or a query with a firing positive control is
printed next to them. The one place I wanted to write *"nobody has ever"* — about IMPC pipeline ages —
is § 7 item 8, where I write instead that I verified nothing.

---

## § 9 · SOURCE ATTRIBUTION

**According to PubMed**, with DOIs as links. 🟢 = served body read by me first-hand this act ·
🟡 = abstract-depth · ⚫ = valid PMCID, zero-length body, reproduced this act · 🔴 = sibling-attested.

- 🟢 **PMID 34747138** · PMC8649866 · Repudi S, Kustanovich I, Abu-Swai S, Stern S, **Aqeilan RI**. *Neonatal neuronal WWOX gene therapy rescues Wwox null phenotypes.* *EMBO Mol Med* 2021;13:e14599. [DOI](https://doi.org/10.15252/emmm.202114599)
- 🟢 **PMID 32000863** · PMC6990504 · Cheng Y-Y, Chou Y-T, Lai F-J, *et al.*, Chang N-S, **Hsu L-J**. *Wwox deficiency leads to neurodevelopmental and degenerative neuropathies and glycogen synthase kinase 3β-mediated epileptic seizure activity in mice.* *Acta Neuropathol Commun* 2020;8:6. [DOI](https://doi.org/10.1186/s40478-020-0883-3)
- 🟢 **PMID 19936220** · PMC2777388 · Ludes-Meyers JH, Kil H, Parker-Thornburg J, Kusewitt DF, Bedford MT, **Aldaz CM**. *Generation and characterization of mice carrying a conditional allele of the Wwox tumor suppressor gene.* *PLoS One* 2009;4:e7775. [DOI](https://doi.org/10.1371/journal.pone.0007775)
- ⚫ **PMID 17360458** · PMC1820689 · Aqeilan RI, Trapasso F, Hussain S, *et al.*, **Croce CM**. *Targeted deletion of Wwox reveals a tumor suppressor function.* *PNAS* 2007;104:3949–54. [DOI](https://doi.org/10.1073/pnas.0609783104) — **`full_text: ""`**
- ⚫ **PMID 18487609** · PMC2490770 · Aqeilan RI, Hassan MQ, de Bruin A, *et al.*, **Croce CM**. *The WWOX tumor suppressor is essential for postnatal survival and normal bone metabolism.* *J Biol Chem* 2008;283:21629–39. [DOI](https://doi.org/10.1074/jbc.M800855200) — **`full_text: ""`**
- 🟡 **PMID 17823927** · PMC4143238 · Ludes-Meyers JH, Kil H, Nuñez MI, *et al.*, **Aldaz CM**. *WWOX hypomorphic mice display a higher incidence of B-cell lymphomas and develop testicular atrophy.* *Genes Chromosomes Cancer* 2007;46:1129–36. [DOI](https://doi.org/10.1002/gcc.20497)
- 🟡 **PMID 10356397** · Crabbe JC, Wahlsten D, Dudek BC. *Genetics of mouse behavior: interactions with laboratory environment.* *Science* 1999;284:1670–2. [DOI](https://doi.org/10.1126/science.284.5420.1670) — **adjacent domain, method only**
- 🟡 **PMID 24152123** · PMC3930200 · Miller AR, Hawkins NA, McCollom CE, **Kearney JA**. *Mapping genetic modifiers of survival in a mouse model of Dravet syndrome.* *Genes Brain Behav* 2014;13:163–72. [DOI](https://doi.org/10.1111/gbb.12099) — **adjacent domain, method only**
- 🟡 **PMID 16921370** · Yu FH, Mantegazza M, Westenbroek RE, *et al.*, **Catterall WA**. *Reduced sodium current in GABAergic interneurons in a mouse model of severe myoclonic epilepsy in infancy.* *Nat Neurosci* 2006;9:1142–9. [DOI](https://doi.org/10.1038/nn1754) — 🔴 **cited ONLY for background-dependence of survival; its interneuron content is adjacent to parked ground and is not entered**
- 🔴 Carried SIBLING-ATTESTED, not read by me this act: **PMID 19500159** [DOI](https://doi.org/10.1111/j.1601-183X.2009.00502.x) · **PMID 33914858** [DOI](https://doi.org/10.1093/brain/awab174) · **PMID 42422765** [DOI](https://doi.org/10.1016/j.omta.2026.201791) · **PMID 36828035** [DOI](https://doi.org/10.1016/j.pneurobio.2023.102425) · **PMID 34634460** [DOI](https://doi.org/10.1016/j.nbd.2021.105529) · **PMID 30290271** [DOI](https://doi.org/10.1016/j.nbd.2018.09.030) · **PMID 31340538** [DOI](https://doi.org/10.3390/ijms20143596) · **PMID 36779245** [DOI](https://doi.org/10.1111/epi.17542) · **PMID 17803050**

### Repository sources (all READ-ONLY)

`analysis/cerebellar_measurement_census_20260922.md` (the anchor; § 4.3, § 5.1a, § 8) ·
`analysis/cerebellar_functional_readout_census_20260922.md` (**§ 1.5** — the divergence this file
adjudicates; also `R1`–`R23`, `H1`–`H9`, § 1.3, § 1.4) ·
`analysis/seizure_ascertainment_census_20260922.md` (§ 1a, § 1b, Q3, § 4, § 5 X-1/X-3/X-4) ·
`analysis/ataxia_without_cerebellar_lesion_20260922.md` (§ 2.1, § 2.2) ·
`analysis/wwox_myelin_oligodendrocyte_census_20260921.md` (§ 1.2) ·
`analysis/tx007_purkinje_frontier_20260922.md` (`FT-152`) ·
`registries/claim_registry_current.md` (`CLAIM 005`, and `:562`, `:565`, `:593`, `:668`, `:676`, `:692`) ·
`registries/working_model_current.md` (`:156`, `:240`) ·
`research/discovery_ledger_current.md` (`DL-MECH-026`, `DL-MECH-033`, `FM-014`, `:756`, `:836`, `:966`) ·
`research/full_text_queue_current.md` (`FT-152` header only)

---

## § 10 · WHICH V0 PRIMITIVES I USED, AND WHETHER EACH EARNED ITS PLACE

🔴 **V0 CHANGE = NONE.** No primitive was added, renamed, merged or extended. Six of the seven were
used; the seventh was not, and saying so is part of the report.

| Primitive | Used? | 🎯 Earned its place, or ceremony? |
|---|---|---|
| **`enumerate_baseline_before_scoring`** | ✅ | 🟢 **EARNED, and it is the reason this file is not wrong.** Twelve candidate differences were enumerated; **nine were already harmonized in the repository** and one was not a difference at all. Had I filtered on expected terms I would have gone straight to the cerebellum and written an `A — REDISCOVERY` of the anchor. The structural stage (545 lines by token co-occurrence) also caught `D12`, which sits in a file I had no prior reason to open at § 1.5 |
| **`diverge_hypotheses`** | ✅ | 🟡 **EARNED, BUT PARTLY INHERITED.** Four of the seven rivals are one sentence of `cerebellar_functional_readout_census…` § 1.5 (attack 2). What the table added was the **discriminator column**, which is what revealed that (d) is not a rival among seven but **the gate** — (a) and (g′) are not separable until (d) is settled. That structural fact is what § 5 is built on |
| **`preregister_prediction`** | ✅ | 🟢 **EARNED, EXPENSIVELY.** P1 was scored **CORRECT BUT UNDER-SPECIFIED** — I predicted one confound and found two. Without the written prereg I would have reported the instrument asymmetry as the whole answer, because it is the tidier story. **P2a fired**, which is the safeguard doing its job. **P3 is the entry that stopped me over-reading**: it is the reason § 5.1 says *"no comparison exists"* rather than *"the Aqeilan null is ataxic too"* |
| **`connect_domains`** | ✅ | 🟢 **EARNED, AND IT ARGUED AGAINST ME.** The *Scn1a*/Dravet modifier precedent is absent from this repository (grep 0) and it supplied the strongest **surviving rival** — background — not support. Crabbe supplied the ceiling on § 5.3. 🔴 **It also produced one clean failure:** the IMPC argument I intended to make returned **0** and was deleted rather than softened (§ 7 item 8) |
| **`compress_experiment`** | ✅ | 🟡 **EARNED, WITH A CONCESSION.** It forced the deliverable down to **two supplementary reads** (zero animals, zero contact) rather than a phenotyping programme. 🔴 **But it also forced me to admit those reads only *bound* the case**, and the real resolver (§ 5.3) is `HUMAN_REQUIRED` and frozen. Compression that hides that distinction would be ceremony; compression that names it is the primitive working |
| **`adversarial_verify`** | ✅ | 🟢 **EARNED — it changed the verdict.** Four of seven attacks landed, and attack 1 moved the headline from *"artefact"* to *"unattributable"*. Attack 6 is the only one I beat, and I beat it with a calendar, not an argument |
| **`recursive_reread`** | ❌ **NOT USED** | 🔵 **Correctly skipped.** The primitives are optional and using one alone is the normal case. No already-read paper here needed reopening under a new question: the two papers this node turns on were read **for the first time** in this act, at full body depth. Invoking it to fill the table would have been exactly the ceremony the skill warns against |

---

🔴 **END. Nothing in this file was promoted.** No registry, ledger, receipt, queue, current file, state
manifest or commit candidate was read-modified or created. **No git command of any kind was run.** No
receipt was written. **No external contact of any kind was made or drafted** — no author, laboratory,
foundation, repository owner or funder. 🔵 Public edition; genotype-class and named-allele level only;
no individual-level record. ⚠️ Alleles, drivers and species were never pooled. **Nothing here is
medical advice.**
