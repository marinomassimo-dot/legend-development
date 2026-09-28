# COMMIT CANDIDATE — NMDAR: upgrade the conjunction actually demonstrated, and only that one

**Candidate ID:** CC-20260826-NMDAR-CONJUNCTION-01
**Status:** proposed — not integrated, not committed
**Base head:** `b80ae8b`
**Receipts:** `FTR-20260810-34634460-02` (`complete_fulltext_read`, PMID 34634460, 21 verbatim
locators, several image-anchored). Receipt depth re-verified this session against
`registries/fulltext_read_receipts.jsonl`; ledger verifies `OK: 128 chained receipt(s)`.
**Author:** scientist-b

> 🔗 **Deliberately separate from `CC-20260826-GAPJUNCTION-ATTRIBUTION-01`.** Both edit the same
> sentence of `CLAIM 021`. They are kept apart because a reviewer can accept this upgrade on the
> strength of the d-APV result and independently refuse the gap-junction withdrawal — the two rest
> on different evidence and fail for different reasons. **Neither presupposes the other.**

---

**CURRENT_TARGET**

`claim_registry_current.md#CLAIM 021` (`consolidated baseline`), Summary, final clause:

> *"**Bursting depends on NMDAR and gap junction activity.**"*

One sentence, two nodes, one verb, no pharmacology, no direction, no magnitude.

**PROPOSED_DELTA**

Replace the **NMDAR half** with:

> *"NMDAR blockade (d-APV) **abolishes** the pathological burst in the `Wwox` S-KO neocortical slice
> at P13–P17 — a pharmacological dependence established **inside** the WWOX-deficient system — with
> a **~1.85× overshoot on washout**."*

And in the map: `CHAIN B` **T2 → T1 for the tool compound only**, recording explicitly that
**memantine has never been given to a WWOX system**.

*(The gap-junction half is the separate candidate. If that one is refused, this delta still stands
and the sentence simply retains its original gap-junction clause.)*

**CHANGE_CLASS:** **MAJOR?** → Mirror, fail-closed. `CLAIM 021` is `consolidated baseline`. This half
**strengthens** the claim rather than weakening it, which is precisely why the classification is
arguable and therefore not mine: under Annex H.1 a doubtful MAJOR is Mirror's call.

**CANONICAL_TARGETS:** `claim_registry_current.md#CLAIM 021` — **one of the four scientific current
files; `BATCH_COMMIT` only.** Secondary: `mechanism_intervention_map.md` `CHAIN B` / `R-02`.

**DIRECT_EVIDENCE**

d-APV takes normalized burst frequency from **1.0 to zero** (Figure 3D-d1, image-read at 6× from
native pixels). On washout, frequency returns to **~1.85×** baseline — recorded, unexplained, and
directly relevant to any chronic-blockade proposal.

**LOCATORS**

`deepdive_manifests/PMID34634460.json`, receipt `FTR-20260810-34634460-02`, `complete_fulltext_read`,
21 verbatim locators.

🔴 **The map's `E-1` was already discharged when the map was written.** The map lists as its
*"highest-value, lowest-cost open item"* a re-read of PMID 34634460 to determine whether the
dependence was established pharmacologically. **The re-read existed, with a complete-read receipt
ten days older than the map, and it was.** The claim's one-verb sentence is what allowed that:
*"depends on"* is compatible with correlation, and the actual result is an abolition.

**TRANSFER_BOUNDARY**

- GRIN2A in the burst-suppression cohort (`DL-MECH-002`) — **T3**.
- Memantine's approved use in other CNS indications — **T5**.
- **Neither carries the upgrade.** The upgrade attaches to the **d-APV conjunction**, not to the
  drug class, and **memantine does not move**: it has still never been given to a WWOX system.
  **The gap is one compound wide, not one experiment wide.** `R-02` remains
  `PROMISING_BUT_MECHANISTIC_GAP`.

⚠️ **Four interpretation risks, recorded rather than resolved:**
1. recordings are **P13–P17** in animals dying at 3–4 weeks; the authors write the stage *"may mimic
   a **late-stage** disorder of WWOX"*;
2. acute *ex vivo* slice ≠ chronic *in vivo*;
3. chronic NMDAR blockade in a developing brain removes a signal required for activity-dependent
   maturation — the process WWOX loss already impairs;
4. 🆕 the *in vivo* hyperexcitability recordings in the sister paper are made **under ketamine, an
   NMDA antagonist** (`deepdive_manifests/PMID34747138.json` entry 13: *"the between-group contrast
   stands; the absolute firing rates are not those of an awake brain"*). Not a contradiction —
   different drug, dose, preparation and endpoint — but a coincidence to resolve by design, not by
   assumption. `PREMISE: INFERENZA`.

**THERAPEUTIC_EFFECT**

The strongest circuit-level conjunction in the portfolio, and it costs nothing to record — the
experiment is already done and in the repository. **It does not promote memantine.**

**REVIEW_REQUIRED:** **Mirror** (MAJOR? classification, fail-closed) → Plan (integration) →
Orchestrator (batch).

**HUMAN_GATE:** operator approval if Mirror classifies MAJOR — per Annex H.1, MAJOR approval is the
operator's.

---

**REVIVAL_TRIGGER** *(for the half that does **not** move — `R-02`, which stays gated)*

*Promote `R-02` when **memantine itself** — not d-APV — reduces burst frequency and phase–amplitude
coupling dose-dependently in a WWOX-deficient system **with isogenic parental and W-AAV-rescue lines
as internal comparators**, and a **chronic** arm shows that the maturation cost of sustained NMDAR
blockade does not exceed the network benefit.*

**Target WM:** MINOR bump if committed (claim modification, no reversal) — declared at batch time.
**Batch gate:** intentionally untouched.


---

## WAVE-2 READINESS (2026-09-27)

**Actor:** `scientist`, wave-2 package `seizure`, under the Orchestrator's wave-2 dispatch. **Append-only: nothing above this line was rewritten.**

**context_policy:** `QUESTION_DRIVEN` — declared before the source was reopened. The question: *does the d-APV result support the proposed upgrade, and does it support it at text level or only at panel level?* Prior knowledge admitted and named: this candidate, the current `CLAIM 021` record (via `registry_records.py get --id "CLAIM 021" --hops 1`), `deepdive_manifests/PMID34634460.json`, receipt `FTR-20260810-34634460-02`, and `mechanism_intervention_map.md` CHAIN B.

### What was done

1. **`CLAIM 021` re-read at its CURRENT text.** The target clause is unchanged by `BATCH_20260922_SEIZURE` and `BATCH_20260927_002` (those batches moved `CLAIM 037` and `CLAIM 005`, not `CLAIM 021`): the Summary still ends *"Bursting depends on NMDAR and gap junction activity."* No rebase of the wording was needed; the proposal is restated against that string below.
2. **The primary was reopened first-hand** (Europe PMC `fullTextXML` for `PMC8609180`, sha256 `934b4e1a42ac19f5cd8912994fb171beabdeb94a6631b23d9a383dab1db906aa`). 🔴 **That digest is byte-identical to the `article_text` artefact the manifest declares** — which matters, because **all seven artefacts the manifest names are ABSENT from the shared checkout's `files/` tree today** (`paper_packet.py packet --pmid 34634460`: *0 present, 7 declared-and-absent*). The NCBI `efetch` route returns a different serialisation (`b01bfa4f…`), so the *route* is part of the recipe. A pending receipt records the re-read: `receipts_pending/seizure_34634460_1.json` (`partial_fulltext_read`, `new_question_outside_prior_coverage`, prior `FTR-20260810-34634460-02`). **`fulltext_receipts.py record` was NOT run** — parallel packages are appending to the same hash chain.
3. **The upgrade is text-supported; its magnitude is not.** The *abolition* and the *reversibility on washout* are in the running text, verbatim (triples below). The **~1.85× washout overshoot is a figure attestation only** (manifest entry 3), and **its image is not in this checkout**, so the proposed wording is rebased to keep the overshoot as an attested panel read, explicitly labelled, rather than as a printed number.
4. **One new qualification found while reading, which the candidate did not have:** in the same treatment series the authors report that maximal phase–amplitude coupling *shifted* under the pannexin blocker in 10 of 25 bursts. It does not touch the d-APV result, but it shows the pharmacology series is not a clean three-arm ladder, and it is recorded in the pending receipt and in `N-16` (applied outside batch by `CC-20260826-PANNEXIN-N16-01`).

### Verdict: **READY_MAJOR**

Change class **MAJOR** — the candidate's own fail-closed `MAJOR?` is resolved *upward* here, not downward: the edit rewrites a clause of a `consolidated baseline` Summary and raises a mechanism's tier. Operator authorisation + blind locator audit before propagation; the triples are supplied below for that audit. **This does not promote memantine** and does not touch `R-02`.

### Exact operation list (`batch_commit.py propagate`)

**OP-1** · file `disease-models/wwox/registries/claim_registry_current.md` · record `CLAIM 021` · op `replace-within`
- **old text (verbatim, current file):** `Bursting depends on NMDAR and gap junction activity.`
- **new text:** `NMDAR blockade (d-APV, 50 µM) abolishes the pathological burst in the neuron-specific `Wwox` S-KO neocortical slice at P13–P17 — a pharmacological dependence established INSIDE the WWOX-deficient system — and the burst returns on washout; on the panel the washout frequency overshoots baseline ≈1.85× (figure attestation, `deepdive_manifests/PMID34634460.json` entry 3, not a printed value). The gap-junction half of this dependence is NOT attributable at this concentration — see the carbenoxolone boundary.`
- **note for the executor:** the final clause presupposes `CC-20260826-GAPJUNCTION-ATTRIBUTION-01`'s OP-1. **If that candidate is refused, drop the final sentence and keep the existing gap-junction clause** — the two remain independent, exactly as this candidate's header says.

**OP-2** · file `disease-models/wwox/analysis/mechanism_intervention_map.md` · `CHAIN B` · op `replace-within` — **NOT applied outside batch**, although the file is non-canonical, because the tier change is the MAJOR half of this item.
- **old text (verbatim):** `It is scored **T2** here, deliberately conservatively, and the resolution is`
- **new text:** `It was scored **T2** here, deliberately conservatively; the re-read that resolves it exists (`FTR-20260810-34634460-02`, ten days older than this file) and the dependence IS pharmacological, so the chain is **T1 for the tool compound d-APV only** — memantine has still never been given to a WWOX system. What remains is`

### LOCATOR TRIPLES FOR BLIND AUDIT

| proposition | verbatim quote | anchor |
|---|---|---|
| NMDAR blockade abolishes the burst in the WWOX-deficient slice | "Blocking glutamatergic neurotransmission with d-APV (50 μM) eliminated the spontaneous bursting events" | Results 2.2, `PMC8609180` JATS, sha256 `934b4e1a…` |
| The abolition is reversible, so it is pharmacological rather than damage | "Upon washout, the frequency, duration and peak-to-trough amplitude returned to normal" | Results 2.2, same artefact |
| The authors state the dependence as a requirement, not a correlation | "These data suggest that NMDAR-mediated glutamatergic neurotransmission is a requirement for the generation of these neocortical bursts" | Results 2.2, closing sentence |
| The window is late-stage by the authors' own statement, which bounds any chronic proposal | "the chosen age group may mimic a late-stage disorder of WWOX" | Discussion 3.4, final sentences |
| The ≈1.85× washout overshoot is a panel read, not a printed number | "[figure attestation - pixels cannot be quote-matched] … heights are approximately Base 1.0, CBX 0.15, BB-FCF 2.55, dAPV-washout 1.85 …" | `deepdive_manifests/PMID34634460.json` `verbatim_locators.entries[3]`, Figure 3 panel D (image NOT present in this checkout) |

### Pending / what would block propagation

- Operator authorisation (MAJOR) and the blind locator audit of the five triples above.
- 🔴 **Evidence locality:** the six figure JPEGs and the XML are missing from `files/`. The XML is re-acquirable (digest verified); the figures are not, from any route reachable here. A blind audit of triple 5 therefore **cannot be run in this checkout** and must either re-acquire the figures or record the audit as text-only on triples 1–4.

## BATCH DISPOSITION — `BATCH_20260927_004` (2026-09-27, ACTOR_ID `scientist`), append-only

**Verdict: `PROPAGATED`.** `OP-1` **merged** with `CC-20260826-GAPJUNCTION-ATTRIBUTION-01`'s `OP-1` into one sentence on `CLAIM 021` — both edited the same sentence and the executor note in each said one must own it; the merged text carries **this candidate's NMDAR half** (the d-APV abolition, the washout return, the authors' own modal *«suggest … is a requirement»*) and the sibling's withdrawal. `OP-2` applied to `CHAIN B`. 🔴 **Triple 4 came back OVERSHOOT (`…wave2_audit_D2.md`) and the wording is now the source's own, twice hedged:** the P13–P17 age group *«may mimic a late-stage disorder»* and the authors *«cannot rule out»* that a pannexin 1 blocker could work at earlier developmental stages. **The window is not asserted to be late-stage anywhere in the propagated text.** ⚠️ Triple 5's ≈1.85× washout overshoot is `UNVERIFIABLE_SURFACE` and is written as a **declared panel attestation**, with the fact recorded that the only pharmacology numbers in the running text are carbenoxolone's and the underlying burst values are referred out to a Supplementary Table this artefact does not contain. Triple 2's gloss *«pharmacological rather than damage»* is the reader's and does not appear in the record. **This does not promote memantine and does not touch `R-02`.**

**Operator authorisation, verbatim (2026-09-27, given in writing after being shown the MAJOR proposals):** *«procedi tu, ti autorizzo su tutto»*. **Mirror ex-post review due** under §21e — see `session_evaluations/2026-09-27_BATCH_20260927_004.md`.
