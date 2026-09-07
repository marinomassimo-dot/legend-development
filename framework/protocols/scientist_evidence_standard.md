# LEGEND Scientist Evidence Standard — v1

> **Non-canonical, PROPOSED.** This document specifies an output contract for Scientist-role
> work. It writes nothing, promotes nothing, and modifies none of the four current files. It is
> a design artefact to be reviewed before any schema, script or gate is built from it.
>
> Public, disease-level, de-identified throughout. Nothing here is medical advice.

**Status:** DRAFT rev. 1 — authored by Scientist A, branch `lettore`, 2026-08-24
**Scope:** the evidence objects a Scientist emits, and the fields a causal graph needs from them
**Related:** [`fulltext_read_receipt.md`](fulltext_read_receipt.md) ·
[`deepdive_manifest.py`](../scripts/deepdive_manifest.py) ·
[`dismech_export_spec.md`](../../disease-models/wwox/analysis/dismech_export_spec.md) ·
[`gold_is_in_the_details.md`](../master/gold_is_in_the_details.md)

---

## 0. Method, and the denominators

Every figure below is measured, not recalled. The population is enumerated before it is
measured, and the command that enumerates it is named, because a count whose population was
defined by the counting tool is not a measurement.

| Population | Count | How enumerated |
|---|---|---|
| Canonical claims | **39** | `## CLAIM nnn` blocks in `claim_registry_current.md` |
| Promoted paper records | **53** | `## PAPER nnn` blocks in `paper_registry_current.md` |
| Corpus placeholders in the same file | **358** | `## CORPUS …` blocks, same split |
| Deep-dive work manifests | **49** | files in `research/deepdive_manifests/` |
| Verbatim locators across them | **813** | `verbatim_locators.entries[]`, all manifests |
| Full-text receipts | **106** | lines in `fulltext_read_receipts.jsonl` |
| Atomized assertion occurrences | **22** | `dismech_authored_assertions.json`, 21 candidates |

Two of these denominators move with the corpus and one does not: claim and paper counts are
population figures that age on their own; the manifest and locator counts are object-derived
and are true of the tree at the stated commit. **Where a conclusion below depends on a ratio,
the ratio is stated with both terms.**

---

## 1. What Scientist practice already does well

These are not compliments. Each is a property a causal graph can be built *on*, and each is
rare enough in literature pipelines to be worth naming before the gaps.

**1.1 The evidence surface is declared and fingerprinted, per quote.**
780 of 813 locators name a `surface` (`body` 503, `figure` 268, `table` 8, `supplement` 1) and
the `artifact` the quote was matched against. The 33 that do not are entirely inside the four
manifests that predate schema v2 — the defect is bounded and enumerable rather than diffuse.
A graph edge can therefore inherit *which kind of surface* its support came from, which almost
no extraction pipeline can supply.

**1.2 Figures are first-class evidence, and the text–panel relation is recorded.**
583 locators carry `panel_text_relation`. The distribution is the finding:

| Value | Count | What it means for a graph |
|---|---|---|
| `text_only` | 344 | claim rests on prose alone |
| `panel_only` | 90 | claim exists **only** in an image |
| `text_confirmed_by_panel` | 81 | independent two-surface corroboration |
| `text_contradicted_by_panel` | **48** | the running text and the data disagree |
| `panel_qualifies_text` | 20 | the panel narrows the sentence |

**48 recorded text-versus-panel contradictions** is the single most valuable asset in this
corpus for downstream curation, and it is invisible to every text-layer extractor. A knowledge
base built from the running text of these same 49 papers would have inherited 48 statements the
data do not support.

**1.3 Reading depth is a controlled vocabulary with section-level coverage — in the ledger.**
The 106 receipts take exactly five `evidence_depth` values (`complete_fulltext_read` 46,
`partial_fulltext_read` 51, `queried_not_full_read` 5, `abstract_only` 2, `retrieved_not_read`
2) and carry per-section `coverage`. Depth is a fact about an event, not an adjective.

**1.4 Negatives are recorded as work, not as silence.**
272 locators carry `found_or_sought`, and the `sought` entries record the question the reader
went in with. Several read as completed negative verifications — *"I searched for WWOX as a
substrate before concluding it never appears as one"*. A graph that can distinguish *no edge
was looked for* from *an edge was looked for and is absent* is categorically better than one
that cannot.

**1.5 Author voice is already separated from LEGEND voice — in prose.**
`CLAIM 003` states it exactly: the authors' attribution of the residual myelination gap to an
oligodendrocyte-autonomous function is *their* `IPOTESI`, while the gap itself is `DATO`. The
three-layer separation this standard formalises is **existing practice being given a field**,
not a new discipline being imposed.

---

## 2. What a causal graph cannot be built from today

### 2.1 The fingerprinted layer carries no measurement

A locator entry is `(proposition, snippet, surface, artifact, anchor)`. `proposition` is free
prose. Nothing in the fingerprinted layer records **what was measured, in what system, against
what comparator, in which direction, with what n**. Those facts exist — they are written into
claim and paper prose — but they live one layer *above* the only layer that is verifiable
against bytes. An edge derived from them inherits no provenance for its own quantitative
content.

### 2.2 Species and perturbation class are prose, and prose does not traverse

This is not hypothetical here. On 2026-08-06 two citation hops converted an explicit negative
about a **rat** into a positive assertion about a **mouse**, and it survived because the
co-cited premise in the same sentence was true (`CLAIM 037`, `CLAIM 005`). A graph built on
today's fields would repeat that traversal, faster and at scale. `species`,
`perturbation_class` (constitutive null / conditional cell-type KO / knock-in missense /
knockdown / overexpression / rescue) and `developmental_window` must be **structural fields**,
because `WWOX loss` in a systemic null (`CLAIM 005`), in a neuron-specific cKO (`CLAIM 021`)
and in a muscle-specific cKO (`CLAIM 009`) are three different edges wearing one phrase.

### 2.3 No comparator field — and the corpus has already paid for this

`CLAIM 004` spent four batches as an unqualified list of rescued domains. What the 2026-08-10
reading found was not a wrong finding but a **missing comparator**: where the rescue is tested
against wild type the comparison is either not drawn or is significant *against* the rescue.
An edge with no declared comparator arm is not weak evidence, it is **unfalsifiable**, and the
schema currently has nowhere to put the arm. `comparator` is a required field, not an optional
one, and its absence is a state (`COMPARATOR_NOT_DRAWN`) distinct from its being non-significant.

### 2.4 No sign, and the sign is not always constant

`CLAIM 034` records that in photoreceptors under metabolic stress **more WWOX means more
superoxide** — the opposite direction from the deficiency→ROS framing of `CLAIM 009`. A single
unsigned `WWOX → ROS` edge would be wrong in one of the two contexts. The graph needs `sign`
**and** `sign_context`, with a declared rule that a sign valid only in a named context may not
be inherited by the unqualified edge.

### 2.5 No directness, and the word is already taken

The relationship vocabulary this role needs — `DIRECT` versus
`INDIRECT_UNKNOWN_INTERMEDIATES` — does not exist in the repository. What *does* exist is
`clinical relevance: INDIRECT`, on **26 records** across the claim, paper and
literature-tracking registries (12 of them claims), meaning something entirely different —
*not clinically actionable*. **Introducing a bare `INDIRECT` for mechanism
directness would collide with it in every grep and every reader's eye.** Use the full
`INDIRECT_UNKNOWN_INTERMEDIATES` token, never the short form.

### 2.6 No competing explanation, no decisive experiment

`next_decisive_experiment_or_decision` is declared in `LEGEND_CORE.md` and instantiated **0
times as a field in 39 claims**; two claims mention a discriminating experiment in prose only.
Meanwhile `CLAIM 038` names two competing and untested explanations for the same measurement,
and `CLAIM 036` quantifies a systemic confounder that contaminates every brain phenotype
measured in its window. Both are exactly the content a curated causal edge should carry, and
neither has a slot. **"The discriminating experiments that separate them" is a declared mission
objective with no structured form.**

### 2.7 Locator reachability of the claim set — measured

For each claim, "reachable" means every `PAPER nnn` it wikilinks has a deep-dive manifest on
disk. This is a **necessary** condition for atomization, not a sufficient one: a manifest may
exist without containing a quote for that claim's particular proposition.

| State | Claims | Notes |
|---|---|---|
| All linked papers have a manifest | **16 / 39** | atomization can start today |
| Some do | **9 / 39** | e.g. `CLAIM 032` at 1 of 6 |
| None do | **14 / 39** | includes 5 claims whose only pointer is a `CORPUS Pnnn` placeholder (`022`, `023`, `025`, `027`, `028`) and one with no source at all (`CLAIM 010`, `IPOTESI`) |

### 2.8 The atomization pilot ran on the least-structured evidence in the corpus

The three atomized claims (`016`, `024`, `035`) rest on `PAPER 019`, `055`, `056`. `PAPER 019`
has **no artefact path at all** in the authored-assertions file. The manifests for the other
two — `PMID35716775` and `PMID22193544` — are **two of the four schema-v1 manifests**, and
between them hold 13 of the 33 locators in the whole corpus that declare no `surface`. The
pilot that defined the atomization contract was run against the weakest evidence available.
This does not invalidate the 22 occurrences; it means the contract has never been exercised
against a figure-heavy, surface-declared, fingerprinted reading — which is what the other 45
manifests are.

### 2.9 Two paper records cannot become graph nodes

`PAPER 007` and `PAPER 008` carry `Identifier: pending normalization`; five records
(`001`, `002`, `007`, `008`, `009`) carry no PMID. `PAPER 008` is worse than un-normalised: it
is an **unenumerated cluster** — *"Aldaz / Banne cluster"*, *"WOREE / SCAR12 clinical spectrum
reviews"*, *"multiple / pending normalization"* — and it is the sole support of `CLAIM 008`, a
`consolidated baseline`. One node standing for an unknown number of papers cannot carry
provenance for anything.

### 2.10 `Evidence depth` on paper records is uncontrolled where the ledger's is controlled

36 of 53 paper records carry an `Evidence depth` field, in **16 distinct free-text spellings**
(`full text reviewed`, `full text reviewed (PDF)`, `full text verificato (…)`, `abstract +
frammenti Scholar Gateway`, …). The receipt ledger three directories away has the same fact
under a five-value controlled vocabulary. This is the repository's own documented failure mode
— a correct pattern applied at one site and not carried to the second — and the fix is to
derive the registry field from the ledger rather than to re-type it.

---

## 3. Composite claims requiring atomization

25 of 39 claims are composite by at least one of two measured tests.

**Test A — composite `Type`.** 14 claims need two or more of
`DATO` / `INFERENZA` / `IPOTESI` / `ESPANSIONE` to be described honestly, which by §4 Rule 1 of
the export spec means they are not atomic:

`002` · `006` · `016` · `019` · `025` · `026` · `029` · `030` · `031` · `033` · `034` · `035` · `036` · `038`

**Test B — the title fuses statements.** 18 claim titles carry a mechanistic verb joining two
propositions. `CLAIM 002` is the clearest: *"WWOX-LoF causes network hyperexcitability;
AAV-WWOX rescues organoid phenotype"* — a loss-of-function phenotype and a gain-of-function
rescue, in two different experiments, under one number.

Seven claims fail **both** tests: `002` · `016` · `029` · `031` · `034` · `035` · `038`.

### 3.1 Priority order — 13 claims are atomization-ready today

Ready = §2.7 reachable and not already atomized:

`004` · `005` · `011` · `013` · `014` · `020` · `021` · `029` · `034` · `036` · `037` · `038` · `039`

Of these, four have a composite `Type` (`029`, `034`, `036`, `038`) and eight have a causal
title (`004`, `005`, `011`, `014`, `021`, `029`, `034`, `038`). **`CLAIM 029` and `CLAIM 034`
sit in every intersection and should go first.**

The remaining 14 composite/causal claims (`002`, `003`, `006`, `007`, `015`, `018`, `019`,
`025`, `026`, `027`, `030`, `031`, `032`, `033`) are **blocked on reading debt, not on
curation effort**, and the honest state for them is a declared debt, not a queued task.

### 3.2 Worked split — `CLAIM 029`

Current single claim: *"WWOX contributes directly to DNA-damage-response competence and
genome-stability maintenance, at least in part via ATM activation and damage-induced nuclear
relocalization."* That is at minimum four assertions and two distinct edge types:

| # | Proposition | Type | Edge |
|---|---|---|---|
| a | WWOX deficiency reduces ATM activation | `DATO` | `WWOX_loss → ATM_activation`, sign `−` |
| b | WWOX deficiency compromises γ-H2AX induction/maintenance | `DATO` | `WWOX_loss → γH2AX`, sign `−` |
| c | DNA damage promotes ITCH-dependent K63 ubiquitination of WWOX at Lys274 | `DATO` | `DNA_damage → WWOX_K63_Ub@K274`, `DIRECT` |
| d | WWOX contributes directly to DDR competence rather than acting as a distal marker | `INFERENZA` | `voice: legend`, supported by a–c |

Rows a–c are measurements; row d is the reading that integrates them. Today all four share one
`Type` field and one status, so the inference inherits the strength of the measurements. That
is precisely the flattening Rule F1 forbids, occurring **inside** the registry rather than at
export.

---

## 4. Claims carrying implicit mechanistic relationships

An implicit relationship is an edge a reader can extract but no field declares. Three species
of it are present, each with a worked case.

**4.1 Arrow-in-prose.** `CLAIM 004` contains `Restauro neuronale-only → mielinizzazione
migliorata non-cell-autonoma; gliosi downstream della disfunzione neuronale`. Two typed edges
with a directness call (`non-cell-autonomous`, i.e.
`INDIRECT_UNKNOWN_INTERMEDIATES` with the oligodendrocyte explicitly *not* transduced) and a
topological call (`downstream`), written as punctuation.

**4.2 Chain asserted by adjacency.** `CLAIM 035` states a linear pathway — WWOX ⊣ GSK3β ⊣ Tau,
with Tau as the required effector, established by knockdown non-additivity. The atomized
version records it as a proposition. **Nothing records that it is a three-node chain**, so the
strongest mechanistic result in the corpus enters a graph as a sentence.

**4.3 Sign asserted by frame.** `CLAIM 009` (`WWOX deficiency → ROS ↑`) and `CLAIM 034`
(`WWOX ↑ → superoxide ↑`) are, read as unqualified edges, contradictory. The registry resolves
this correctly in prose — the sign is context-dependent, and `CLAIM 034` says so in its title.
A graph ingesting both without `sign_context` produces a contradiction where the corpus has a
distinction.

**4.4 The negative edge.** `CLAIM 037` asserts an edge's **absence** in a species — Wwox-null
mice show no epilepsy, stated in three places and by an empty `Epilepsy` row in a table. A
graph with no representation for a sourced negative will silently drop the one finding that
prevents the 2026-08-06 error from recurring. **A negative edge is an edge.**

---

## 5. Recommended Scientist output contract

Six layers. Three exist and are unchanged; three are new. The design rule is that **no new
layer may restate a fact an existing layer already fingerprints** — it references it.

```
ARTIFACT      (exists)  path + sha256 + kind          ── the bytes
   └─ LOCATOR (exists)  quote + surface + anchor      ── the author's characters
        └─ OBSERVATION  (new)  what was measured      ── voice: source, no interpretation
             └─ ASSERTION (partial) one proposition   ── voice: author | legend
                  └─ RELATION (new) a candidate edge  ── voice: legend
                       └─ CLAIM   (exists)            ── canonical, gated by BATCH_COMMIT
```

### 5.1 OBSERVATION — new, and the layer the graph is actually missing

One measurement. Emitted only by a Scientist with the document open.

| Field | Req. | Notes |
|---|---|---|
| `observation_id` | ✔ | stable within the manifest |
| `locators[]` | ✔ | ≥ 1 locator index in the same manifest — this is what makes it verifiable |
| `system` | ✔ | e.g. `mouse cortex, in vivo`; `HEK293, transfected`; `human patient fibroblasts` |
| `species` | ✔ | controlled: `human` `mouse` `rat` `cell_line` `organoid` `in_vitro_purified` `in_silico` |
| `perturbation` | ✔ | the thing varied |
| `perturbation_class` | ✔ | controlled: `constitutive_null` `conditional_ko` `knock_in_missense` `knockdown` `overexpression` `rescue` `pharmacological` `natural_variant` `none_observational` |
| `developmental_window` | ✔ | or `not_stated` — `CLAIM 036` is why |
| `comparator` | ✔ | the arm compared against, or `COMPARATOR_NOT_DRAWN` |
| `readout` | ✔ | what was measured |
| `method` | ✔ | how |
| `direction` | ✔ | `increase` `decrease` `no_change` `not_tested` — **`no_change` and `not_tested` are different values and conflating them has already cost a correction** |
| `magnitude` | ○ | verbatim as printed, units included |
| `n` | ✔ | or `not_stated` |
| `statistic` | ○ | verbatim: `p=0.000131`, `**`, `ns` |
| `limitation` | ✔ | at least one, or an argued `none_identified` |
| `surface_adjudication` | ✔ where `panel_text_relation` is `text_contradicted_by_panel` or `panel_qualifies_text` | which surface the observation follows, and why |

### 5.2 ASSERTION — the existing `dismech_authored_assertions` shape, plus three fields

Keep `proposition`, `epistemic_type`, `evidence_relation`, `source_id`, `snippet`,
`source_anchor`. Add:

- **`voice`** — `source_observation` | `author_interpretation` | `legend_interpretation`.
  Required. The three layers of Scientist practice §1.5 already separates in prose.
- **`observations[]`** — the observation ids this rests on. An assertion with
  `voice: source_observation` and no observation is malformed.
- **`context`** — retained, but **derived** from the observation's structured fields rather
  than authored, so species and allele state stop being free text.

### 5.3 RELATION — the candidate edge

| Field | Req. | Notes |
|---|---|---|
| `subject`, `predicate`, `object` | ✔ | |
| `sign` | ✔ | `positive` `negative` `null_effect` `context_dependent` |
| `sign_context` | ✔ where `sign` is `context_dependent` | naming both contexts and both directions |
| `directness` | ✔ | `DIRECT` \| `INDIRECT_UNKNOWN_INTERMEDIATES`. **Never abbreviate the second** (§2.5) |
| `polarity` | ✔ | `asserted` \| `asserted_absent` — §4.4 |
| `supported_by[]` | ✔ | observation ids |
| `context_binding` | ✔ | species + perturbation_class + window, inherited from the observations |
| `competing_explanations[]` | ✔ | or an argued `none_identified` — `CLAIM 038` is the shape |
| `decisive_experiment` | ✔ | what would separate this edge from its competitors. The `LEGEND_CORE` field that has never been instantiated |
| `voice` | ✔ | always `legend_interpretation` for a multi-observation relation |

### 5.4 Rules

- **R1 — No relation without an observation.** Biological plausibility creates no edge. An
  edge whose `supported_by` is empty is not a weak edge, it is not an edge.
- **R2 — No observation without a locator.** The observation layer exists to attach
  measurement to fingerprinted bytes. Detached, it is a paraphrase.
- **R3 — Directness is measured or it is `INDIRECT_UNKNOWN_INTERMEDIATES`.** `DIRECT` requires
  an assay that would fail if an intermediate were required. The default is the weaker value,
  never the absent field. *(The upstream schema's "if not specified, assumed established" is
  the exact failure this inverts.)*
- **R4 — The caveat travels with the statement.** Adopted verbatim from Rule A2 of the export
  spec: an assertion exported without its caveat is a mis-export, not a partial one.
- **R5 — Voice never merges.** A field carrying `author_interpretation` may not be promoted to
  `source_observation` by a later reading; it is superseded by an observation or it stands.
- **R6 — `no_change` ≠ `not_tested`, and `COMPARATOR_NOT_DRAWN` ≠ non-significant.** Both
  distinctions have already produced corrections in this corpus. They are enum values, not
  prose.
- **R7 — Nothing in this contract is satisfied by an abstract.** Unchanged from the corpus
  rule. *Un abstract non è una lettura.*

### 5.5 What this costs, and when it is paid

The observation layer is captured **while the document is open**, alongside the locator, for
the same reason the locator itself is: capturing costs seconds and recovering costs the
reading twice. Retrofitting the 813 existing locators is **not** proposed — it is exactly the
kind of hand-updated constraint this repository has learned not to write. Existing manifests
stay valid at schema v2; the observation layer is required from schema v3 forward, and the
count of pre-v3 locators is derived by the validator, never typed by a person.

---

## 6. What this document does not decide

- **It does not adopt anything.** Adoption is an operator decision and a framework change,
  not a Scientist output.
- **It does not touch the four current files**, the receipt ledger, or any manifest.
- **It does not propose an exporter.** Field mapping to any external schema stays governed by
  `dismech_export_spec.md`, which pins its target and is further along than this document.
- **It does not resolve §2.9** — whether `PAPER 008` is split into its constituent papers or
  demoted is a curation decision with a `consolidated baseline` claim resting on it.
- **It does not claim the 13 ready claims will atomize cleanly.** §2.7 reachability is
  necessary, not sufficient; some will return `ATOMIZATION_REQUIRED`, and that is a result.

---

## 7. Open questions for review

1. Does the OBSERVATION layer belong inside `deepdive_manifest.json` (one file per paper,
   validator already exists) or in a sibling file? Inside is cheaper and keeps the locator
   reference local; a sibling avoids growing a file the LINT already reads.
2. `surface_adjudication` is required only for the 68 contradicting/qualifying locators today.
   Should it be required for `panel_only` (90) as well, where there is no text to adjudicate
   against?
3. Is `decisive_experiment` a required field on every relation, or only on relations whose
   `competing_explanations` is non-empty? Required-everywhere risks becoming a formality; the
   narrower rule risks never firing.
4. Do negative edges (`polarity: asserted_absent`) enter the same graph as positive ones, or a
   separate register read alongside the dismissal ledger?
