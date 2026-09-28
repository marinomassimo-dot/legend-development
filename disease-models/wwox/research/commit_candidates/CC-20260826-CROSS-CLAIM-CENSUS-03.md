# COMMIT CANDIDATE — cross-claim census, round 3: zero new claim-vs-claim contradictions, and two the census cannot see

**Candidate ID:** CC-20260826-CROSS-CLAIM-CENSUS-03
**Date:** 2026-08-26
**Status:** queued; **no canonical file modified**
**Mode:** continuation of
[`CC-20260826-CROSS-CLAIM-CENSUS-02`](CC-20260826-CROSS-CLAIM-CENSUS-02.md) over the pairs it did
not adjudicate, plus two surfaces outside the census's field of view
**Change class:** 🔴 **MAJOR** — one of the two findings is a `consolidated baseline` assertion with
no claim behind it
**Canonical targets:** `working_model_current.md:165` · `claim_registry_current.md` (a new claim, or
a deletion) · `dismissal_ledger_current.md` `DIS-011` · cross-links on two pairs
**Base head:** `ccddc28939234ad4fe29c417935a0dbe11de86d0` (branch `lettore`)
**Batch gate:** intentionally untouched

> 🔴 **This round adds ZERO new claim-vs-claim contradictions, and that is the result.** The count
> is not grown with ambiguous cases. What it adds are two defects of a **different kind**, both
> outside what a claim-pair screen can reach.

**Reproduce the screen:**

```bash
python3 framework/scripts/cross_claim_contradiction_census.py
```
→ 39 claims · 741 possible pairs · **39 screened positive** · **32 of 39 not cross-linked** ·
18 pairs printed above the display threshold.

---

## 1. The pairs round 2 left unadjudicated

Round 2 adjudicated fifteen pairs. Four printed pairs were left, all `[NOT CROSS-LINKED]`. Each is
carried to a terminal class below; **none is a contradiction.**

### `CLAIM 031` ↔ `CLAIM 037` — score 11 · **RESOLVED_BY_CONTEXT**

The screen fires on `ABSENT` ↔ `PRESENT` with `model=['wwox_null_mouse']`. **`CLAIM 031` is human**
— its `Genotype/model relevance` reads *"umano — null biallelici"*, and its evidence is two
children with West syndrome plus the Oliver 2023 cohort. The `wwox_null_mouse` tag is a screen
artefact of the phrase *"WWOX-null"* in the claim's own text.
⇒ Species mismatch, not opposition. **And the opposition disappears entirely under Δ1** of
[`CC-20260826-FIVECLAIM-HARDENING-01`](CC-20260826-FIVECLAIM-HARDENING-01.md), which deletes the
`ABSENT` token that fires it.

### `CLAIM 005` ↔ `CLAIM 031` — score 11 · **RESOLVED_BY_CONTEXT**

Same artefact from the other direction: `CLAIM 005`'s `PROHIBIT`/`ABSENT` tokens against a human
clinical claim that shares no paper, no species and no endpoint. `CLAIM 005`'s own
`Clinical meaning` forecloses the only overlap that could exist — *"**No medication implication.**
The source measures no GABA concentration, no synaptic inhibition, no E/I ratio and no drug."*
⇒ Score will fall on its own once Δ3 retargets the prohibition.

### `CLAIM 005` ↔ `CLAIM 016` · `CLAIM 005` ↔ `CLAIM 011` · `CLAIM 004` ↔ `CLAIM 037` — **already counted**

All three are components of the five-claim bundle counted once in round 2. ⚠️ One sub-axis is
worth naming because it is *not* the bundle's axis: `CLAIM 005` ↔ `CLAIM 011` fires on
`INCREASED`↔`DECREASED` for **glia**, not for seizures — 005 reports IBA1/GFAP area fraction *up*
in the untreated KO, 011 reports gliosis *down* after neuronal rescue. **Those are the two ends of
the same arrow.** `RESOLVED_BY_CONTEXT`; they should be cross-linked so the next screen stops
flagging it.

### `CLAIM 031` ↔ `CLAIM 033` — score 12 · **RESOLVED_BY_CONTEXT**, with a ⚠️ double-count

Not a contradiction — **the same sentence, twice.**

| Claim | Verbatim |
|---|---|
| `CLAIM 031` | *"Convergenza: in Oliver 2023 l'unico paziente **non** farmaco-resistente è morto a 8 anni — la responsività ai farmaci non protegge la sopravvivenza."* |
| `CLAIM 033` reserve (4) | *"La responsività ai farmaci **non protegge**: l'unico paziente non farmaco-resistente della coorte è morto a 8 anni."* |

Same source (`PAPER 018`, Oliver 2023), same **n = 1** patient, same conclusion, **and neither
claim names the other** — `CLAIM 031`'s wikilinks are `PAPER 045 · 018 · 011 · CLAIM 001`;
`CLAIM 033`'s are `PAPER 018 · 040 · 041 · 042 · CLAIM 019 · CLAIM 030`.

⚠️ **Two claims stating one observation read as two supports.** The datum is a single child. Both
claims should be cross-linked **and** should say so, or the "drug responsiveness does not protect
survival" line acquires a false apparent replication.
**Minimum repair:** reciprocal wikilink + the words *"the same single patient, counted once"* in
both.

### `CLAIM 032` ↔ `CLAIM 033` — score 12 · **RESOLVED_BY_CONTEXT**, and they corroborate

`CLAIM 032`: haploinsufficiency is not deleterious; the therapeutic threshold sits well below full
restoration. `CLAIM 033`: `null/null` survives worse than genotypes with ≥1 missense, and *"no
evidence to support an 'intermediate' phenotype"* — `null/missense` behaves like
`missense/missense`. **These agree**: one functioning-ish allele is worth most of two.

🔴 **`DO_NOT_INFER`, and it is the reason this pair needs a cross-link rather than silence.**
`CLAIM 032`'s evidence is the `Wwox^+/−` mouse and human carriers — a **null/wild-type** genotype,
one *fully functional* allele. `CLAIM 033`'s better-surviving class carries one **missense**
allele of unmeasured residual function. Chaining them into *"one missense allele is nearly as good
as one wild-type allele"* is **not supported by either**, and `CLAIM 033`'s reserve (1) falsifies
the premise directly: Q230P is missense and **abolishes** the protein.

---

## 2. 🔴 Two contradictions the census structurally cannot see

Round 2 named this gap for `CLAIM 006`-versus-its-own-source. Two more instances exist, in two
further classes.

### 2.A — **claim ↔ dismissal ledger**: `DIS-011`'s revival trigger has fired

Detailed in [`CC-20260826-FIVECLAIM-HARDENING-01`](CC-20260826-FIVECLAIM-HARDENING-01.md) §1.
`DIS-011` declares `REVIVAL_TRIGGER (a)` = *"qualunque EEG o osservazione di crisi in un topo
Wwox-null"*. Cheng 2020 (seizures observed from P12) and Obeid 2026 (continuous ECoG P14–P21) both
satisfy it, both are `complete_fulltext_read`, and both are cited by claims in the same registry.
**The dismissal still reads `RIGETTATA`.**

**Class: 🔴 CONFIRMED** — a canonical rejection contradicted by canonical claims.
**Terminal action:** revive per that candidate's Δ11; the *verdict* survives on the narrow reading
(`EPILEPTOGENESIS` as a process is unmeasured), the *ground* does not.

🔴 **Capability gap named, not fixed here:** nothing in the repository re-evaluates a
`REVIVAL_TRIGGER` when new evidence lands. `DIS-011`'s trigger fired in a batch that also wrote the
claims that fired it. A ledger-wide trigger sweep is a proposal, not part of this candidate.

### 2.B — 🔴 **claim ↔ its own mirror**: `working_model_current.md:165` asserts a claim that does not exist

**This is the round's serious finding.**

| Surface | `017` says |
|---|---|
| `claim_registry_current.md:308` **Title** | *"WWOX-related human disease spans a spectrum from severe WOREE/WWOX-DEE to milder SCAR12-like phenotypes"* |
| 🔴 `working_model_current.md:165` **mirror row** | *"\| 017 \| **Ketogenic diet has small but real human support in WWOX-related epileptic encephalopathy** \| DATO \| P1+P5 \| T1 contextual \| consolidated baseline \| Chong 2023 \|"* |

**Two different propositions under one ID.** Measured:

- All **39** claims have a mirror row; all **39** IDs are present. There is no gap and no shift —
  `017` is simply occupied by a different proposition.
- Of the 39 rows, **only `017`** carries a proposition absent from its claim. The other four rows
  a token-overlap screen flags (`012`, `013`, `018`, `019`) are the **same** proposition in the
  other language or in shorter words; `017` is not.
- 🔴 **There is no ketogenic-diet claim anywhere in `claim_registry_current.md`.** Two searches,
  each with its own denominator, because they answer different questions:
  `/usr/bin/grep -c -iE "ketogenic|chetogenic|dieta chetogenica|keto diet"` over that file returns
  **0**; `Chong 2023` — the mirror row's declared source — appears **4** times, at lines 41, 171,
  174 and 177, all inside `CLAIM 001` (vigabatrin) and `CLAIM 009` (Chong 2023 as a **lactate**
  signal). **The source is in the registry; the diet proposition is not.**
  ⚠️ A first draft of this line reported *"four hits"* for the diet terms. That figure came from a
  grep whose pattern also contained `Chong 2023`, so it counted the source, not the diet. Recorded
  corrected rather than silently replaced.
- **Seven other surfaces treat `CLAIM 017` as the spectrum claim** and none treats it as a diet
  claim: `meta_human_spectrum_current.md:89`, `full_text_queue_current.md:513/540/614`,
  `dismech_phase3_dryrun_result.md:44`, `dismech_spectrum_reading_result.md`,
  `locator_contract_live_test.md:99/209`, `discovery_ledger_current.md:1686`.
  **The mirror is a lone dissenter against seven.**
- The row has been in place since the initial public-edition commit `a2e0dd0` (2026-07-26); the
  spectrum title has **never** appeared in the working model. This is founding-state drift, not a
  recent regression — and `legend_lint.py` returns `VERDICT: PASS` over it.

⚠️ **The diet proposition is not a fabrication.** It is stated twice more as model prose —
`working_model_current.md:86` and `disease_model.md:46`, both reading *"Ketogenic diet associated
with seizure improvement in **3/5 WOREE patients** (Chong 2023)"*. So the underlying fact has a
source and a denominator.

🔴 **What makes it MAJOR is what it lacks.** As written, the model asserts at `consolidated
baseline` that **a dietary intervention has human support in a paediatric epileptic
encephalopathy**, with:

- no claim entry, therefore **no `Evidence boundary`** — 3/5 is uncontrolled, unblinded, n = 5;
- **no `Genotype/model relevance`** and no genotype caution;
- **no `Clinical meaning`**, and therefore **none of the mandatory *"Non è parere medico"***;
- **no `Transferability` justification** for its `T1 contextual` tag;
- and it occupies the ID of an unrelated claim, so anyone auditing "what does `CLAIM 017` rest on"
  is sent to the wrong evidence.

**Class: 🔴 CONFIRMED.**

**Minimum repair — two edits, and the second needs a decision this role cannot make:**

1. **`working_model_current.md:165`** — replace the row's proposition with `CLAIM 017`'s actual
   title, type, pathway, transferability, status and source. **Mechanical; no science changes.**
2. 🔴 **The ketogenic-diet proposition needs an owner.** Either (a) it becomes a **new claim** with
   a full evidence boundary — n = 5, 3/5 responders, uncontrolled, source `Chong 2023`, and the
   medical-advice disclaimer; or (b) it is **demoted** to model prose alongside lines 86 and 46 and
   stripped of `consolidated baseline`. **(a) is recommended** — the fact is sourced and clinically
   consequential, and burying it would be the opposite error. **Either way it may not keep a claim
   ID it does not own.**

⚠️ **Nothing here says the ketogenic-diet finding is wrong.** It says it is asserted at baseline
strength without a claim, and under someone else's number.

---

## 3. Terminal classification — every candidate this round

| Pair / surface | Class |
|---|---|
| `CLAIM 031` ↔ `CLAIM 037` | `RESOLVED_BY_CONTEXT` (species) |
| `CLAIM 005` ↔ `CLAIM 031` | `RESOLVED_BY_CONTEXT` (species, endpoint) |
| `CLAIM 005` ↔ `CLAIM 011` (glia sub-axis) | `RESOLVED_BY_CONTEXT` — cross-link owed |
| `CLAIM 005` ↔ `CLAIM 016`, `CLAIM 004` ↔ `CLAIM 037` | already counted in the five-claim bundle |
| `CLAIM 031` ↔ `CLAIM 033` | `RESOLVED_BY_CONTEXT` — ⚠️ **shared n = 1, cross-link owed** |
| `CLAIM 032` ↔ `CLAIM 033` | `RESOLVED_BY_CONTEXT` — corroborating; cross-link owed with a `DO_NOT_INFER` |
| **`DIS-011` ↔ `CLAIM 004`/`011`/`016`** | 🔴 **CONFIRMED** (claim ↔ dismissal ledger) |
| **`working_model:165` ↔ `CLAIM 017`** | 🔴 **CONFIRMED** (claim ↔ mirror) |

| Count | |
|---|---|
| **New claim-vs-claim contradictions** | **0** |
| New `CONFIRMED` of other kinds | **2** |
| `RESOLVED_BY_CONTEXT` | 6 |
| `NEEDS_LOCATOR` | **0** — every item above was settled against text already in the tree |
| `UNRESOLVABLE` | **0** |

🔴 **`CROSS_CLAIM_CONFIRMED_COUNT` is unchanged at 2** (or 3 with `CLAIM 006`-vs-source, as round 2
recorded). **Neither finding in §2 is a claim pair, and neither is added to that figure.** Stating
which denominator is in use is the whole point of quoting either number.

---

## 3b. 🔴 Why §2.B survived a month of `VERDICT: PASS` — measured in the linter, not inferred

The mirror's own header states the obligation:

> *"This mirror is the working model's own copy and **must stay synchronized with it (a LINT
> consistency rule)**."*

`legend_lint.py` implements that rule in `working_model_claim_mirror_findings()`, whose docstring
reads: *"Require the Working Model's BLOCK 2 mirror to **contain every canonical claim ID**."* Its
three findings — `CLAIM_MISSING_FROM_MIRROR`, `ORPHAN_CLAIM_IN_MIRROR`,
`DUPLICATE_CLAIM_IN_MIRROR` — are all computed from `MIRROR_ROW_ID = re.compile(r'^\|\s*(\d+)\s*\|')`.

⇒ **The rule compares ID sets. It never reads the Title, Type or Status columns.** A mirror row may
carry any proposition whatsoever under a correct ID and the gate passes. That is not a linter
failure; it is a rule that was written narrower than the obligation it is named for.

### Four more drifts the same blindness hides

A strict Title or Type equality check would be useless here — the registry is largely Italian and
the mirror largely English, and a token-overlap screen flags `012`, `013`, `018`, `019` for being
the same proposition in fewer or other words. **A rule that fires on those is noise.** The rule
that is not noise is directional:

> **`EPISTEMIC_TIER_DROPPED_IN_MIRROR`** — if the registry's `Type` asserts a tier (`DATO`,
> `INFERENZA`, `IPOTESI`) and the mirror's `Type` does not, report it.

Measured over the 39 rows: **4 findings, 35 clean.** Every one is substantive.

| Claim | Registry `Type` | Mirror `Type` | Dropped |
|---|---|---|---|
| `CLAIM 019` | `DATO (endpoint funzionale…) + IPOTESI (causa e recuperabilità)` | `DATO+INF` | `IPOTESI` |
| `CLAIM 030` | `DATO (serie allelica su cellule di paziente) + INFERENZA (la regola)` | `INFERENZA` | 🔴 `DATO` |
| `CLAIM 031` | `DATO (osservazione clinica) + INFERENZA (degli autori)` | `INFERENZA` | 🔴 `DATO` |
| 🔴 `CLAIM 032` | `DATO (topo, ratto, e ogni famiglia umana pubblicata)` | `INFERENZA` | 🔴 `DATO` |

⚠️ **`CLAIM 032` is the sharpest.** Its registry `Type` is **pure `DATO`**, from mouse, rat and every
published human family; the mirror presents it as an **`INFERENZA`**. It is also the claim that
sets *"la soglia di successo di ogni leva del portafoglio"* — a reader who consults the working
model discounts, as an inference, the measured result that licenses partial-restoration strategy.

🔴 **The drift here runs in the safe direction — understating evidence — and `017` runs in the
unsafe one.** Both come from the same absence of a content check, and only one of them would ever
have been noticed by reading.

**Status drift, for completeness:** 1 of 39 (`CLAIM 012`, registry `consolidated baseline` vs
mirror `consolidated baseline (full text)` — an additive qualifier, `INFO` at most).

### HANDOFF — to the role that maintains `framework/scripts/`

> **Proposed, not applied.** This role does not modify the gate that governs `BATCH_COMMIT`.
> Add to `working_model_claim_mirror_findings()`:
> (a) `EPISTEMIC_TIER_DROPPED_IN_MIRROR` as above — **measured false-positive rate 0 of 4** on the
> current tree; (b) `MIRROR_STATUS_DRIFT` on the `Status` column — **1 of 39**, additive, so
> `INFO`; (c) 🔴 **no Title-equality rule** — it would fire on four legitimate translations and
> would still not have caught `017`, whose row is fluent, plausible and about a different subject.
> **`017` is caught by (d): a mirror row whose proposition appears in no claim's Title or Summary.**
> That is the check worth writing, and it is the harder one.

---

## 4. What this round refuses to do

- **Does not grow the contradiction count.** Six pairs terminate as `RESOLVED_BY_CONTEXT` and are
  named so the next round does not re-open them.
- **Does not claim the ketogenic-diet finding is false**, or that the diet is or is not indicated.
  **Not medical advice.**
- **Does not create the missing claim.** That is a registry write, and this role has no canonical
  authority.
- **Does not propose a new screening schema.** The two findings in §2 need surfaces the current
  screen does not read — the mirror table and the dismissal ledger — which is a capability
  proposal, deliberately not bundled here.

---

## BATCH DISPOSITION — `BATCH_20260927_001` (2026-09-27, ACTOR_ID `scientist`), append-only

**Status:** PROPAGATED IN PART

**Edit 1 only.** `working_model_current.md` BLOCK 2: the mirror row for `017` is rewritten from `CLAIM 017`'s actual title, type, pathway, transferability, status and source. Verified first-hand: the row had carried "Ketogenic diet has small but real human support …" while `CLAIM 017` is the human-spectrum claim, and the ketogenic datum survives in this file's BLOCK 1 prose ("Ketogenic diet associated with seizure improvement in 3/5 WOREE patients (Chong 2023)"), so nothing is lost by the rewrite.

**Still owed, so this candidate stays open:** edit 2 — who owns the ketogenic-diet proposition, and whether a consolidated-baseline dietary statement becomes a claim or model prose. That is a therapeutic-adjacent decision the candidate itself reserves to the operator. The `DIS-011` revival of §2.A is the same act as `CC-20260826-FIVECLAIM-HARDENING-01` Δ11 and must be done once, in one batch; neither is in this batch's scope.


---

## WAVE-2 READINESS (2026-09-27)

**Actor:** `scientist`, wave-2 package `seizure`, under the Orchestrator's wave-2 dispatch. **Append-only: nothing above this line was rewritten.**

**context_policy:** `SYNTHESIS` over the registry, the working model and the two research ledgers, by record; plus `QUESTION_DRIVEN` adjudication of one disposition against **git history**. No source was reopened — neither of this round's two findings is about a paper. Prior knowledge admitted and named: this candidate, round 2, `CC-20260826-FIVECLAIM-HARDENING-01` §1/Δ11, the current `working_model_current.md`, `claim_registry_current.md#CLAIM 017`, `dismissal_ledger_current.md#DIS-011`.

### What was done

1. **Edit 1 — the `017` mirror row — is DONE, and the adjudication is from git, not from the file alone.** At this HEAD `working_model_current.md:176` reads `| 017 | WWOX-related human disease spans a spectrum from severe WOREE/WWOX-DEE to milder SCAR12-like phenotypes | DATO | human spectrum / genotype-phenotype | T1 | consolidated baseline | …PAPER 040… |` — i.e. `CLAIM 017`'s own title, type, pathway, transferability, status and source, exactly as this candidate specified. `git log -S "Ketogenic diet has small but real human support"` returns **two** commits: `a2e0dd0` (the founding public-edition commit, which introduced the drifted row) and **`c99dfe5` — `BATCH_20260927_001`**, which removed it. ⇒ **CLOSE — PROPAGATED** for edit 1.
2. **The ketogenic-diet proposition has been de-facto resolved by option (b), not (a), and the MAJOR defect is therefore GONE.** Measured: `ketogenic|chetogenic` returns **0** in `claim_registry_current.md` (so no diet claim was created), and the proposition now exists **only as model prose** at `working_model_current.md:97` and `disease_model.md:48`, both reading *"Ketogenic diet associated with seizure improvement in 3/5 WOREE patients (Chong 2023)"* — a sourced statement with its denominator, **no longer asserting `consolidated baseline`, no longer occupying a claim ID it does not own**. The five things the candidate said the assertion lacked (evidence boundary, genotype caution, clinical meaning with the medical-advice disclaimer, transferability justification, its own ID) are no longer *lacked by a baseline assertion*: they are not required of prose that claims nothing.
3. **What survives of edit 2 is the smaller, optional question**, and it is **DEFERRED**: should the 3/5 datum be *promoted* to a claim of its own with a full evidence boundary (the candidate's recommended option (a))? That is a therapeutic-adjacent promotion — a dietary intervention in a paediatric epileptic encephalopathy — and promoting it is a scientific decision with a `BLOCCO 1`-adjacent clinical face, reserved to the operator by the triage of this lot. It is **not** a defect repair any more, and nothing in the corpus is wrong while it waits.
4. **Finding 2.A (`DIS-011`'s fired revival trigger) is NOT touched here.** Verified still live (`DIS-011` reads `RIGETTATA` with trigger (a) *"qualunque EEG o osservazione di crisi in un topo Wwox-null"*, which `CLAIM 040`'s ECoG and Cheng 2020's observations satisfy). It is owned this wave by the **`m002` package** (Mirror-002 repairs of `DIS-011` and `DL-MECH-075`) and it is **the same act** as `CC-20260826-FIVECLAIM-HARDENING-01` Δ11: **it must be done once, in one batch**, with the narrow epistemological verdict preserved (EPILEPTOGENESIS as a *process* stays unmeasured).
5. **The four round-3 pairs and the cross-links** (`005↔011` glia, `031↔033` one patient, `032↔033` corroboration, and the `031↔037` / `005↔031` screen artefacts that Δ1 already defused) are carried as OP-3/OP-6/OP-7/OP-8 of `CC-20260826-CROSS-CLAIM-CENSUS-02`'s operation list in this wave. **Not duplicated here.**
6. **The capability gap this round named is restated, unfixed and unclaimed:** nothing in the repository re-evaluates a `REVIVAL_TRIGGER` when new evidence lands — `DIS-011`'s trigger fired in the same batch that wrote the claims firing it. No tool is proposed here; the gap belongs to a capability-scout record, not to a science batch.

### Verdict: **READY_MINOR**, with one DEFERRED residue and one item handed to `m002`

- **READY_MINOR:** the cross-link half, whose exact operations live in `CC-20260826-CROSS-CLAIM-CENSUS-02`'s readiness block (OP-3, OP-6, OP-7, OP-8). Nothing else in this file is proposed to a batch executor.
- **CLOSE — PROPAGATED:** edit 1 (the `017` mirror row), by `BATCH_20260927_001` / `c99dfe5`.
- **CLOSE — the MAJOR half of edit 2 is resolved** by the same commit, through option (b): the diet proposition is model prose with a denominator and no baseline status.
- **DEFERRED:** promoting the 3/5 ketogenic datum to a claim of its own. **One line on what would unblock it:** an operator decision that a dietary-intervention datum may hold a canonical claim ID, plus the evidence boundary a promotion would need written first (n = 5, 3/5 responders, uncontrolled, unblinded, `Chong 2023`, genotype caution, *«Non è parere medico»*) — no reading is owed, the source is already in the registry.
- **Handed to `m002`:** finding 2.A / Δ11 (`DIS-011` revival).

### Why there is no `### LOCATOR TRIPLES FOR BLIND AUDIT` section

Nothing here narrows or reverses a claim about the world. The mirror-row repair asserted no new proposition (it copied `CLAIM 017`'s own fields), the cross-links assert none, and the one proposition that would need triples — the ketogenic promotion — is **DEFERRED unwritten** rather than proposed.

### Pending

- Operator decision on the ketogenic promotion; `m002` for `DIS-011`; the shared cross-link list in `…-CENSUS-02`.

## BATCH DISPOSITION — `BATCH_20260927_003` (2026-09-27, ACTOR_ID `scientist`), append-only

**Status:** **PROPAGATED IN PART** — `BATCH_20260927_003` (MINOR, MANUAL, `WM_v6.0` → `WM_v6.1`).

Edit 1 (the `017` mirror row) is **PROPAGATED** by `BATCH_20260927_001`, re-verified in the live working model at line level. The MAJOR half of edit 2 is resolved: the ketogenic proposition exists only as sourced model prose with its denominator, and no claim was created — measured, not assumed (`ketogenic|chetogenic` returns zero in the claim registry). Round 3's four adjudicated pairs landed **here**, as `OP-3`/`OP-6`/`OP-7`/`OP-8` of `…-CENSUS-02`'s list. Finding 2.A (`DIS-011`'s fired revival trigger) was done by the `m002` package outside batch. **DEFERRED, and why this stays open:** whether the 3/5 ketogenic datum is promoted to a claim of its own is a therapeutic-adjacent decision reserved to the operator, and nothing in the corpus is wrong while it waits.

**Mirror ex-post review due** under §21e — see the batch report at `session_evaluations/2026-09-27_BATCH_20260927_003.md`.

## BATCH DISPOSITION — `BATCH_20260927_004` (2026-09-27, ACTOR_ID `scientist`), append-only

**Verdict: `PROPAGATED IN PART`.** **Edit 2's claim-scoped prose is written — the residue two batches deferred.** `CLAIM 031` and `CLAIM 033` now say, in both records, that the drug-responsiveness observation is **the same single patient, counted once**: one source, `n = 1`, so the line acquires no false apparent replication. And `CLAIM 032` and `CLAIM 033` carry the reciprocal **`DO_NOT_INFER`**: chaining a **null/wild-type** genotype with one **fully functional** allele to a **null/missense** genotype of **unmeasured** residual function into *«one missense allele is nearly as good as one wild-type allele»* is supported by neither, and `CLAIM 033`'s own reservation (1) falsifies the premise — Q230P is missense and abolishes the protein. These are prose that changes what the claims mean, which is why `BATCH_20260927_003` would not write them beside a wikilink and this MAJOR batch does. 🔴 **DEFERRED: the ketogenic 3/5 promotion, and the operator's blanket authorisation is deliberately not read as settling it.** Whether a dietary-intervention datum may hold a canonical claim ID is a question of **who owns a proposition**, not a factual matter the authorisation can decide, so the dispatch's rule applies and **the conservative option that asserts less was taken**: the datum stays sourced model prose with its denominator (*«Ketogenic diet associated with seizure improvement in 3/5 WOREE patients (Chong 2023)»*), no claim ID is minted, and nothing in the corpus is wrong while it waits. **What would unblock it:** an explicit operator decision that a dietary datum may hold a claim ID, plus the evidence boundary a promotion would need written first (n = 5, 3/5 responders, uncontrolled, unblinded, `Chong 2023`, genotype caution, *«Non è parere medico»*). No reading is owed. Edit 1 and the round-3 cross-links landed in earlier batches.

**Operator authorisation, verbatim (2026-09-27, given in writing after being shown the MAJOR proposals):** *«procedi tu, ti autorizzo su tutto»*. **Mirror ex-post review due** under §21e — see `session_evaluations/2026-09-27_BATCH_20260927_004.md`.

---

## BATCH DISPOSITION — `BATCH_20260928_007` (2026-09-28, ACTOR_ID `orchestrator`), append-only

**Nothing above this line was rewritten.** Operator instruction, verbatim: *«procedi sempre»*. The residue was re-derived against `main` `7352d52`; every op was produced by a reader other than the batch actor and verified by the batch actor against the source bytes before propagation.

**Verdict:** DEFERRED

Unchanged and re-measured: the ketogenic 3/5 datum is model prose in the working model and holds no claim ID; minting one needs an **operator decision** that a dietary-intervention datum may hold a canonical claim, and its evidence boundary written first. No reading is owed.

**Not medical advice.**
