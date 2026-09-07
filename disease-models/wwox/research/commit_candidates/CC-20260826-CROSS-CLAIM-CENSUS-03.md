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
