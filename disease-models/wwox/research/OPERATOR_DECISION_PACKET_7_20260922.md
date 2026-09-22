# OPERATOR DECISION PACKET — the seven gated commit candidates

**Date:** 2026-09-22 · **Prepared by:** Orchestrator · **Supersedes:**
[`OPERATOR_DECISION_PACKET_6_20260922.md`](OPERATOR_DECISION_PACKET_6_20260922.md), which remains on
disk unchanged as the record of what was presented before candidate 7 existed.
**Status:** 🔴 **NONE PROPAGATED.** Every candidate is `PROPOSED — NOT PROPAGATED` and stays that way
until the Operator authorises it. **BLOCK-1:** no molecule, no dose, no route is introduced by any of
the seven. **Nothing here is medical advice.**

**Waiting for authorization has not stopped any scientific work.** This packet was assembled
alongside three Scientist waves, two pre-registered recursive re-reads and four landings, none of
which touched a canonical file.

---

## §1 · The seven, at a glance

| # | ID | Class | Severity | Direction | Reversibility | Recommendation |
|---|---|---|---|---|---|---|
| 1 | `CC-…CLAIM011-DOSE-ENDPOINTS-01` | precision on a canonical numeric endpoint | 🟡 MEDIUM | bounds an absolute; **ratio untouched** | trivial | 🟢 **ACCEPT** |
| 2 | `CC-…SDR-HOMODIMER-PREMISE-01` | TAG an uncited assertion | 🔴 HIGH | adds a label, deletes nothing | trivial | 🟢 **ACCEPT** |
| 3 | `CC-…VERMIS-HYPOPLASIA-FREQUENCY-01` | QUALIFY a frequency word | 🟡 MEDIUM | bounds *"most cases"* | trivial | 🟢 **ACCEPT** |
| 4 | `CC-…CLAIM025-SIGN-INVARIANCE-01` | QUALIFY a directionality | 🟡 MEDIUM | bounds the **sign**, keeps the ratio | trivial | 🟢 **ACCEPT WITH NARROWING** |
| 5 | `CC-…NMD-PREMISE-WITHDRAWAL-01` | WITHDRAW an unsourced premise | 🔴 HIGH | **re-opens** a closed therapeutic axis | moderate | 🟡 **ACCEPT WITH NARROWING** |
| 6 | `CC-…TX001-CEILING-REASSESSMENT-01` | reassess a strategy's expected value | 🔴 HIGH | **cuts against `TX-001`** | moderate | 🟠 **DEFER — split: accept the unconditional half after #5** |
| **7** | **`CC-…CLAIM038-UNIT-CLASS-02`** | **QUALIFY a unit + BOUND a comparison + NARROW a title** | 🟡 **MEDIUM** | **bounds a number's use; narrows a title** | **trivial** | 🟢 **ACCEPT** |

**The honest summary, unchanged and now stronger.** **Not one of the seven adds a positive finding.**
Six remove or bound an overstatement; one adds a label. **Five are pure epistemic hygiene.** One (#6)
cuts against a named therapeutic strategy and is the only one with a real strategic decision in it.

---

## §2 · Candidates 1–6

**Unchanged from packet 6.** Their full reasoning — current canonical text verbatim, proposed change,
primary support, dependent surfaces, therapeutic consequence, reversibility and the narrowings
attached as conditions — is in
[`OPERATOR_DECISION_PACKET_6_20260922.md`](OPERATOR_DECISION_PACKET_6_20260922.md) §2, and is **not
restated here**, because restating it would create two texts that can drift apart. **Nothing about
candidates 1–6 has changed since that packet was written**, and no work done since bears on any of
them.

---

## §3 · Candidate 7 — `CC-20260922-CLAIM038-UNIT-CLASS-02`

Full candidate:
[`commit_candidates/CC-20260922-CLAIM038-UNIT-CLASS-02.md`](commit_candidates/CC-20260922-CLAIM038-UNIT-CLASS-02.md).
Derivation: [`recursive_reread_3_4_units_20260922.md`](recursive_reread_3_4_units_20260922.md),
pre-registered at `3d0a558` **before any locator was opened**.

- **SEVERITY** 🟡 MEDIUM. It bounds how two numbers may be **used** and narrows one **title**. No
  finding is reversed, demoted or removed.

- **CURRENT CANONICAL TEXT** — `claim_registry_current.md`, `CLAIM 038`:
  - *Title:* *"Elevated BUN **and creatinine** recur across Wwox rodent models with two competing
    explanations…"*
  - *Summary (`:707`):* *"Nel ratto a 28 giorni: BUN 12.6 → **40.3 mg/ml** (♀, `P<0.05`)…"*
  - and, 41 lines away, `CLAIM 036`: *"BUN 37.25 vs 17.67 **mg/dL**"*.

- **PROPOSED CHANGE** — four additive edits, none of which rewrites a number:
  **Δ1′ QUALIFY, do not correct.** Leave `mg/ml` **exactly as transcribed** and record that the token
  is **unadjudicated**. **Δ2** (carried from the superseded `-01`, unconditional) bar any **numeric**
  cross-model comparison; permit **direction and significance** only. **Δ3 NEW** narrow the title to
  *"Elevated BUN recurs…, and creatinine is elevated in the rat where alone it was measured."*
  **Δ4 NEW** record in the page-adjudication README that Table 2's **unit tokens were never
  adjudicated**.

- **PRIMARY EVIDENCE** — three findings, each checkable without leaving the repository:
  1. 🔴 **The unit is transcribed faithfully and is UNADJUDICATED.** `mg/ml` is exactly what
     `deepdive_manifests/PMID17803050.json` `entries[25]`/`[26]` hold — so *"we mistranscribed"* is
     **refuted**. But that text layer is classified **`SUSPECT`** by this repository and **refused by
     `deepdive_manifest.py`** (34 C0 controls, ~145 printable substitutions, with `q → ±` documented
     **on the BUN row itself**). ⇒ *"the source misprints it"* is **not established either.**
  2. 🎯 **The render that would settle it was made, `crop_contains_span`-verified and SHA-256
     digested — and it reported the values and never named a unit.** And the needle that resolves
     the row, `"BUN (mg/ml)"`, **was taken from the corrupted layer and matched against the corrupted
     layer.** A needle cannot adjudicate the character it is made of.
  3. 🔴 **Creatinine was never measured in the mouse.** *No creatinine measurement for the
     `Wwox`-null mouse was identified within the dossier, session-evaluation and deep-dive-manifest
     document classes — the complete set of three surfaces this repository holds for PMID 19936220 —
     in English and Italian, unscoped by file type, using `creatinin|creatinina|\bCRE\b`, with `BUN`
     returning 3/1/1 in the same surfaces as positive control.* 🟢 **Independently reached the same
     day by Scientist C** (`systemic_rescue_mechanism_and_peripheral_panel_20260922.md` §5.1 rank 2),
     which did not read this re-read and was not told the finding.

- **CONSEQUENCE** — 🟢 **None therapeutic.** No strategy, molecule, endpoint or dose depends on these
  figures. The consequence is **epistemic**: a canonical title currently asserts cross-model
  recurrence for an analyte measured in one model, and two claims 41 lines apart invite a numeric
  comparison that the registry cannot support.
  🟢 **And what does NOT move is most of the claim.** *"Uremico senza essere ipoglicemico"* is a
  statement about **signs**; *"~3.2–3.5× normal"* is a **ratio**; `P<0.05`/`P<0.01` are tests. **The
  unit cancels from every one of them.** This is the same arithmetic that rescued the TX-007 dose
  ratio, and it is why the defect is bounded rather than fatal.

- **AFFECTED DOWNSTREAM SURFACES** — `CLAIM 036` · `CLAIM 037` / `CLAIM 039` (same primary,
  unit-independent) · `discovery_ledger_current.md:2164` · `fulltext_dossiers/PMID17803050.md:54` ·
  `peripheral_phenotype_denominator_audit_20260922.md` §3.2 (whose *"the damage is bounded"* sentence
  is **narrowed, not reversed**) · `page_adjudications/PMID17803050/README.md`.

- **REVERSIBILITY** — **trivial.** All four edits are text-only and additive; no claim status, belief
  level or evidence class changes.

- 🟢 **RECOMMENDATION: ACCEPT.** Δ2, Δ3 and Δ4 are **unconditional under both possible outcomes of
  the render**, which is exactly why this candidate is propagatable now and its predecessor `-01` was
  not — `-01` blocked itself on *"read the primary"*, and the primary has **no DOI, no PMCID, an
  all-rights-reserved notice, and `files/fulltext/` does not exist in this edition.**
  ⚠️ Δ1′ is worded so that it stays correct whichever way the render falls.

### §3.1 · The one `HUMAN_REQUIRED` item, ~2 minutes

```bash
python3 framework/scripts/regenerate_adjudications.py write  --pmid 17803050
python3 framework/scripts/regenerate_adjudications.py verify --pmid 17803050
```
…then **read the row label** in `p04_table2_BUN_CRE_GLU.png` (page 4, crop `(40, 480, 570, 562)` PDF
points @ 500 dpi). The crop already contains it. ⚠️ **It must actually be looked at** — the instrument
was pointed at this row once already and returned everything except the answer.

---

## §4 · What I am NOT asking for

- **No propagation.** `BATCH_COMMIT` is not run by this file, and no `*_current.md` is touched by it.
- **No new claim.** Not one of the seven adds a positive finding.
- **No unit normalisation and no unit repair.** Candidate 7 preserves the source exactly as printed;
  the standing directive on this point is honoured in the only way the evidence permits.
- No molecule, dose, route or clinical recommendation.
- **No new gate, auditor, registry or workflow** anywhere in the seven.

## §5 · Order of operations, if the Operator accepts

1. **#2 `SDR-HOMODIMER-PREMISE`** — one tag, no dependencies, already shown to cause harm untagged.
2. **#1, #3, #4, #7** in any order — independent, text-only, each with its narrowing attached.
3. **#5 `NMD-PREMISE-WITHDRAWAL`** with the *"open ≠ favourable"* bound **in the same edit**, never a
   later one.
4. **#6 unconditional half** only after #5; conditional half re-presented as its own candidate.

**Gate state at the time of writing:** `legend_lint` **PASS** · growth anchors **PASS**
(claims=40, papers=87, corpus=361, literature=398, registry_only=13, `unread_premises=0` — measured,
not predicted) · receipt chain **201, tail-anchored** · publication gate **PASS / 0 BLOCKS** ·
tool routing **7/7 OK**.
