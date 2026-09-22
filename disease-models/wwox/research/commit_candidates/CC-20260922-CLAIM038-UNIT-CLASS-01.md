# CC-20260922-CLAIM038-UNIT-CLASS-01

**Status:** 🔴 **PROPOSED — NOT PROPAGATED**
**Target:** `claim_registry_current.md` → `CLAIM 038` (Summary, the rat chemistry figures)
**Change class:** **CORRECT a unit annotation and ADD a comparison bound.** No finding is reversed,
demoted or removed; the claim's scientific content is untouched.
**Review floor:** R2. **BLOCK-1:** no molecule, no dose, no route. Nothing here is medical advice.
**Found by:** Scientist G, `analysis/peripheral_phenotype_denominator_audit_20260922.md`.
**Verified by:** the Orchestrator, against the registry text. Producer ≠ verifier.

---

## 1 · The defect, located and measured

`claim_registry_current.md:707`, verbatim:

> *"Nel ratto a 28 giorni: BUN 12.6 → **40.3 mg/ml** (♀, `P<0.05`) e 10.1 → **35.6** (♂, `P<0.01`)"*

`claim_registry_current.md:666`, the mouse claim, verbatim:

> *"BUN 37.25 vs 17.67 **mg/dL** (`p=0.01086`)"*

🔴 **`40.3 mg/ml` is `4,030 mg/dL`.** A blood-urea-nitrogen of 4,030 mg/dL is not a survivable value
in any mammal; normal rat BUN is roughly 15–25 mg/dL and the quoted fold-change over the control is
≈3×. **The rat figures are certainly `mg/dL` and the annotation is wrong by a factor of 1,000.**

## 2 · Why this is worth a candidate rather than a silent fix

Two claims about the same analyte in two species sit 41 lines apart in the same registry, in two
different units, **with nothing flagging it**. Any reader — or any actor — comparing the mouse's
`37.25` with the rat's `40.3` would be comparing `mg/dL` with `mg/ml` and would conclude the two
models agree quantitatively. **They may well agree; the registry as written cannot be used to show
it.**

This is a known defect class in this repository — the `0.2 mg/l` tubulin flag is the same error —
but **it had never been pointed at this claim**.

## 3 · What does NOT change, and it is most of the claim

🟢 **`CLAIM 038`'s scientific content is unaffected.** The claim is that the rat at 28 days is
**uraemic without being hypoglycaemic** — a statement about **direction and significance**
(`P<0.05`, `P<0.01`, and *"Glucosio, calcio, Na⁺, K⁺, Cl⁻ e trigliceridi: tutti non significativi"*).
None of that depends on the unit. The contrast with the mouse null — *"profilo opposto"* — is a
contrast of **signs**, and it stands.

## 4 · Proposed edits (exact, none applied)

**Δ1 — the unit annotation.** Replace `mg/ml` with `mg/dL` in the rat chemistry figures of
`CLAIM 038`'s Summary, **and mark the correction inline** rather than silently, so that a reader who
has previously quoted the wrong unit can find out: `mg/dL` ⚠️ *(annotazione corretta 2026-09-22; il
registro riportava `mg/ml`, un fattore 1.000)*.

🔴 **Δ1 is conditional on one check this session could not run:** the correction must be made against
the **primary**, not against plausibility. If the primary itself prints `mg/ml`, the correction
becomes a **flag on the source** rather than an edit to our transcription, and the wording changes
accordingly. **Do not propagate Δ1 until the primary's units are read.**

**Δ2 — the comparison bound, which is unconditional.** Append to `CLAIM 038` and cross-reference
from `CLAIM 036`:

> ⚠️ **Nessun confronto numerico fra modelli è autorizzato da queste due claim** — solo
> **direzione e significatività**. Le chimiche di topo e ratto sono state misurate in laboratori,
> età, sessi e piattaforme diversi, e le unità del registro hanno divergito (§`CC-20260922-CLAIM038-UNIT-CLASS-01`).
> Un'affermazione della forma *"il ratto ha BUN più alto del topo"* non è ricostruibile.

## 5 · What this candidate does NOT do

- It does **not** touch `CLAIM 038`'s finding, its belief level, or its evidence class.
- It does **not** assert that the two models agree or disagree quantitatively — it forbids the
  question from being answered from the registry.
- It does **not** re-open the hypoglycaemia discordance, which is recorded and is a **direction**
  result.
- It does **not** propagate. Δ1 additionally awaits a read of the primary.

## 6 · Verification required before propagation

1. Read the rat primary's chemistry table and record the printed unit **verbatim**, with a locator.
2. Confirm the mouse figures at `:666` against their own primary in the same pass.
3. Re-run `legend_lint`, `growth_anchors check` and the publication gate after the edit.

**Gate state at proposal:** `legend_lint` PASS · growth anchors PASS (`unread_premises = 0`) ·
receipt chain 201, tail-anchored · publication gate PASS, 0 blocks.
