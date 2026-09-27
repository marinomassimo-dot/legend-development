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

---

## WAVE-2 READINESS (2026-09-27)

**context_policy declared:** `QUESTION_DRIVEN`. One question, asked of a known source: what unit
does the rat primary actually print in its Table 2. Held going in: `CLAIM 038`, `CLAIM 036` and
this candidate. Records reached by `registry_records.py get --id`, never by grepping a registry.

**Actor:** `scientist`, wave-2 package `provenance`.

### What I did — §6.1's verification, which decides the shape of Δ1

The candidate makes Δ1 conditional: *"If the primary itself prints `mg/ml`, the correction becomes
a **flag on the source** rather than an edit to our transcription, and the wording changes
accordingly."*

🔴 **The primary prints `mg/ml`.** `deepdive_manifests/PMID17803050.json` entry 25 carries the row
verbatim from the page adjudication
`page_adjudications/PMID17803050/p04_table2_BUN_CRE_GLU.png`:

> `BUN (mg/ml) 12.6 q 4.3 40.3 q 3.7c 10.1 q 2.7 35.6 q 12.8d`
> — Table 2, *"Plasma concentrations of biochemical markers in 28-d-old rats"*, BUN row, page 4

**And the corroboration is one row down, which the candidate did not have.** Entry 26 gives
`GLU (mg/ml) 169.0 q 26.7 145.4 q 26.5 155.0 q 30.1 157.4 q 38.9`. A glucose of 169 mg/ml is
16,900 mg/dL. **Two analytes on the same table carry the same impossible unit**, so this is a
mislabelled unit header in the source's Table 2, not a transcription error of ours and not a single
typo.

⇒ **LEGEND's transcription is faithful and must not be "corrected".** Δ1 as drafted — replace
`mg/ml` with `mg/dL` — is **refused**, exactly as the candidate's own §6 instructed. It is redrafted
below as a source-unit flag that keeps the printed unit and says what is wrong with it.

Δ2 was unconditional and is unchanged in substance.

### Verdict — **READY_MINOR**

`CLAIM 038` is `in observation`, no finding is reversed, no status moves, no baseline is touched:
the direction and significance results — which are what the claim asserts — do not depend on the
unit at all.

### Operation list for `batch_commit.py propagate`

**File:** `disease-models/wwox/registries/claim_registry_current.md` — record-scoped.

**OP 1 · record `CLAIM 038` · `replace-within`**

*old (verbatim, from the current file):*

```
**Summary:** Nel ratto a 28 giorni: BUN 12.6 → **40.3** mg/ml (♀, `P<0.05`) e 10.1 → **35.6** (♂, `P<0.01`);
```

*new:*

```
**Summary:** Nel ratto a 28 giorni: BUN 12.6 → **40.3** mg/ml ⚠️ *(unità come stampata dal primario; vedi la nota di unità in fondo a questo record)* (♀, `P<0.05`) e 10.1 → **35.6** (♂, `P<0.01`);
```

**OP 2 · record `CLAIM 038` · `replace-within`**

*old (verbatim):*

```
**Wikilinks:** [[paper_registry_current#PAPER 059]] · [[paper_registry_current#PAPER 057]] · [[claim_registry_current#CLAIM 036]] · [[claim_registry_current#CLAIM 037]]
```

*new:*

```
**Nota di unità — è un difetto DELLA FONTE, non della nostra trascrizione (`CC-20260922-CLAIM038-UNIT-CLASS-01`, verificato 2026-09-27).** La Table 2 di [[paper_registry_current#PAPER 059]] stampa `BUN (mg/ml)` e `GLU (mg/ml)`: le cifre trascritte qui sono **fedeli alla stampa**. Ma `40.3 mg/ml` è `4.030 mg/dL` e `169.0 mg/ml` di glucosio è `16.900 mg/dL` — valori non compatibili con un mammifero vivo, e il fattore è lo stesso (1.000) su entrambe le righe: l'intestazione di unità di quella tabella è **sbagliata alla fonte**, non c'è un refuso singolo, e le cifre vanno lette come `mg/dL`. Locator: `deepdive_manifests/PMID17803050.json` entries 25 e 26, dall'aggiudicazione di pagina `page_adjudications/PMID17803050/p04_table2_BUN_CRE_GLU.png`. 🔴 **Nessun confronto numerico fra modelli è autorizzato da questa claim e da [[claim_registry_current#CLAIM 036]]** — solo **direzione e significatività**. Le chimiche di topo e ratto provengono da laboratori, età, sessi e piattaforme diversi, e le unità dei due primari divergono; un'affermazione della forma *"il ratto ha BUN più alto del topo"* **non è ricostruibile** da questi record.
**Wikilinks:** [[paper_registry_current#PAPER 059]] · [[paper_registry_current#PAPER 057]] · [[claim_registry_current#CLAIM 036]] · [[claim_registry_current#CLAIM 037]]
```

**OP 3 · record `CLAIM 036` · `replace-within`**

*old (verbatim):*

```
**Wikilinks:** [[paper_registry_current#PAPER 057]] · [[claim_registry_current#CLAIM 005]] · [[claim_registry_current#CLAIM 038]]
```

*new:*

```
**Vincolo di confronto (`CC-20260922-CLAIM038-UNIT-CLASS-01`, 2026-09-27):** le cifre di questo record sono in `mg/dL` come stampate dal proprio primario; quelle del ratto in [[claim_registry_current#CLAIM 038]] sono stampate in `mg/ml` dalla **loro** fonte, con l'unità sbagliata all'origine. **Nessun confronto numerico fra i due modelli è autorizzato** — solo direzione e significatività. Vedi la nota di unità in `CLAIM 038`.
**Wikilinks:** [[paper_registry_current#PAPER 057]] · [[claim_registry_current#CLAIM 005]] · [[claim_registry_current#CLAIM 038]]
```

### What this section refuses

- ❌ **No unit rewrite.** Changing `mg/ml` to `mg/dL` in the Summary would make LEGEND's text
  disagree with the page it quotes, which is worse than the defect it fixes.
- ❌ **No assertion that the two models agree or disagree quantitatively.** OP 2 and OP 3 forbid the
  question from being answered from the registry; they do not answer it.
- ❌ **Nothing about the mouse figures at `CLAIM 036`** beyond the comparison bound: §6.2's
  verification of those figures against their own primary is not done here and is not claimed.

**Change class:** MINOR (unit annotation + comparison bound). **Review floor:** R2, as declared.
**Pending:** §6.2 — re-verify `CLAIM 036`'s mouse chemistry against PMID 19936220's own table.

## BATCH DISPOSITION — `BATCH_20260927_003` (2026-09-27, ACTOR_ID `scientist`), append-only

**Status:** **PROPAGATED** — `BATCH_20260927_003` (MINOR, MANUAL, `WM_v6.0` → `WM_v6.1`).

`OP 1`–`OP 3` applied: the Summary's unit pointer, the unit note on `CLAIM 038` and the comparison bound on `CLAIM 036`. Δ1 as originally drafted stays **refused** — the printed `mg/ml` is kept, because making LEGEND's text disagree with the page it quotes is worse than the defect it would fix. Both locator rows (BUN and GLU) were checked in `deepdive_manifests/PMID17803050.json` before the ops were applied; §6.2 (re-verifying `CLAIM 036`'s mouse chemistry against its own primary) stays open and is not claimed.

**Mirror ex-post review due** under §21e — see the batch report at `session_evaluations/2026-09-27_BATCH_20260927_003.md`.
