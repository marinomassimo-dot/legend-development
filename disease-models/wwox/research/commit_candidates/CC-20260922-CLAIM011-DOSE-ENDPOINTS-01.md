# CC-20260922-CLAIM011-DOSE-ENDPOINTS-01

**Status:** 🔴 **PROPOSED — NOT PROPAGATED**
**Target:** `claim_registry_current.md` → `CLAIM 011` (flag body + `REVIVAL_TRIGGER`)
**Class:** precision on a canonical numeric endpoint. **No finding is reversed, demoted or removed.**
**Produced by:** Orchestrator, from `analysis/tx007_dose_unit_forensics_20260922.md` (Scientist O)
**Verifier ≠ producer:** the ratio arithmetic was re-derived independently by the Orchestrator; the
dose surfaces were read by Scientist O. The two roles are separate.
**Depends on:** `d49040d` (dose forensics landed)

---

## 1 · The defect, stated once

`CLAIM 011`'s flag body asserts, as bare absolutes:

> **LD = 1.23 × 10¹¹ vg**, **HD = 2.63 × 10¹¹ vg**

and closes with a `REVIVAL_TRIGGER` that instructs an experimenter:

> *«un braccio a dose intermedia fra 1.23 e 2.63 × 10¹¹ vg localizzerebbe la soglia — l'esperimento
> più informativo che questo paper implica.»*

**PMID 42422765 never states the unit convention.** It gives bare `vg` on all three surfaces where a
dose appears; the word `hemisphere` never adjoins a dose; and — established this session —
**the Methods state no dose at all.** The injection is bilateral ICV, 2.0 μL, one injection per
hemisphere. So `vg` admits three readings (per hemisphere / total per animal / per injection), and
the absolute dose an animal received is **uncertain by exactly a factor of 2**.

## 2 · What is NOT affected — and this is the larger half

🟢 **The ratio is degenerate in the unit.** Writing the unknown convention as a multiplier `u`:

```
HD/LD = (u · 2.63×10¹¹) / (u · 1.23×10¹¹) = 2.63/1.23 = 2.1382      ← u cancels
```

| Reading | LD (total per animal) | HD (total per animal) | HD/LD |
|---|---|---|---|
| (A) `vg` = per hemisphere | 2.460 × 10¹¹ | 5.260 × 10¹¹ | **2.1382** |
| (B) `vg` = total per animal | 1.230 × 10¹¹ | 2.630 × 10¹¹ | **2.1382** |
| (C) `vg` = per injection | 2.460 × 10¹¹ | 5.260 × 10¹¹ | **2.1382** |

Therefore **everything `CLAIM 011`'s flag actually argues survives untouched**:

- ✅ *«dose-dependent» descrive un continuo dove il pannello mostra una soglia* — **stands.** It rests
  on the qualitative survival difference (LD reaches zero; HD plateaus ~80% to day 300) and on the
  P20 glycaemia split, neither of which depends on the unit.
- ✅ The `PREMISE_TAG` against *«una dose più bassa e più sicura aiuterebbe comunque»* — **stands.**
- ✅ The **width** of the interval — **exact.** Only its **endpoints** move.

🔴 **This is the correction of my own framing.** I previously wrote, and reported to the Operator,
that *"the unit ambiguity is the size of the effect it is being used to measure."* That is a
**category error** and is withdrawn (`CC-20260922-TX007-DOSE-CHALLENGE-01` §10, `D-33`). The defect
is confined to the **absolute** axis. Naming it correctly is what makes this a narrow precision
rather than a challenge to the claim.

## 3 · Why it must not be left as it is

The `REVIVAL_TRIGGER` is not commentary — it is an **experimental instruction in the canonical
registry**. A laboratory that designs "an intermediate arm between 1.23 and 2.63 × 10¹¹ vg" may set
an absolute dose **2× away** from the one the source animals received, and would then localise a
threshold that is not the threshold.

This is the **same defect class** as the `+8 nt` error in
`tx001_experiment_decision_packet_20260921.md`, which was repaired at the point of error this
session: a number that is right in one frame of reference and wrong in the one the reader will use.
`D-33` already carries the lesson; this propagates it to the canonical surface that would be read
first.

## 4 · Exact before / after

### Δ1 — flag body, the dose statement

**BEFORE**
> …letta all'immagine (`gr3.jpg`, sha256 `c63f930c…4997d`): **LD = 1.23 × 10¹¹ vg**,
> **HD = 2.63 × 10¹¹ vg**; il braccio a dose bassa **non recupera la sopravvivenza**…

**AFTER**
> …letta all'immagine (`gr3.jpg`, sha256 `c63f930c…4997d`): **LD = 1.23 × 10¹¹ vg**,
> **HD = 2.63 × 10¹¹ vg** *come stampati*. ⚠️ **La convenzione dell'unità non è mai dichiarata dal
> primario** — `vg` nudo su tutte le superfici, `hemisphere` non adiacente ad alcuna dose, e
> **nessuna dose nei Methods**; l'iniezione è ICV bilaterale, 2.0 μL, una per emisfero. La dose
> **assoluta** ricevuta dall'animale è quindi incerta **di un fattore 2**:
> **LD ∈ [1.23, 2.46] × 10¹¹ vg**, **HD ∈ [2.63, 5.26] × 10¹¹ vg**. 🟢 **Il rapporto è invariante:
> `HD/LD = 2.1382` sotto ogni lettura permessa** (`u` si cancella), quindi **nulla di ciò che
> questo flag argomenta dipende dall'ambiguità**: il braccio a dose bassa **non recupera la
> sopravvivenza**…

### Δ2 — the `REVIVAL_TRIGGER`

**BEFORE**
> `REVIVAL_TRIGGER`: un braccio a dose intermedia fra 1.23 e 2.63 × 10¹¹ vg localizzerebbe la
> soglia — l'esperimento più informativo che questo paper implica.

**AFTER**
> `REVIVAL_TRIGGER`: un braccio a dose intermedia **a `HD/LD` frazionario fra 1 e 2.14** — cioè
> definito **come frazione della HD del primario, non come assoluto** — localizzerebbe la soglia:
> è l'esperimento più informativo che questo paper implica. ⚠️ **Non specificare quel braccio in
> vg assoluti** finché la convenzione dell'unità non è confermata dagli autori o da un protocollo
> depositato: un assoluto scelto da questo intervallo può essere 2× fuori bersaglio. Un secondo
> `REVIVAL_TRIGGER`, indipendente e più economico: **una dichiarazione esplicita della convenzione**
> (per emisfero / totale per animale) chiuderebbe l'ambiguità senza alcun esperimento.

### Δ3 — `Full text status` line, append

**APPEND**
> ⚠️ **Dose-unit forensics 2026-09-22** (`analysis/tx007_dose_unit_forensics_20260922.md`):
> classificazione **`AMBIGUOUS BUT BOUNDED`**. La non-monotonicità fra superfici **sopravvive**
> all'audit (la frase-ponte esclude un cambio di unità per-figura) ma **non va letta come biologia**:
> l'alternativa principale è un **disallineamento degli orizzonti di follow-up**, non
> un'inversione dose-risposta.

## 5 · What this candidate deliberately does NOT do

- ❌ It does **not** downgrade the measured rescue, and does **not** touch the measured durability.
  *(Operator rule, 2026-09-22: «Do not downgrade measured rescue merely because replication is
  absent. Downgrade only confidence / independence language.»)* Nothing here is about replication.
- ❌ It does **not** assert biological non-monotonicity. §4 Δ3 records the audit result and names the
  leading non-biological alternative.
- ❌ It does **not** change `CLAIM 011`'s `Status` (`flagged for review`), `Type`, `Transferability`
  or `clinical relevance`.
- ❌ It does **not** touch the `BATCH_20260815_001` boundary (regional unevenness, survivor
  selection, the `n=5`/`n=4` discrepancy) — unrelated and independently sourced.
- ❌ It does **not** generalize to any other WWOX vector, allele or model.

## 6 · Gate state at proposal

`legend_lint` PASS · `growth_anchors check` PASS · `public_release_gate` PASS / BLOCKS 0.
**No claim is added or removed — `claims=40` is unchanged by this candidate.**

## 7 · Verification required before propagation

1. Re-read Fig 3A and the S7I caption and confirm the printed values `1.23`/`2.63` (both are prior-
   session reads; **§3.3 of the forensics records that I could not re-verify either myself**).
2. Confirm no dose appears in the Methods of PMID 42422765 — the strongest single support for
   "convention never stated".
3. Confirm the bilateral ICV / 2.0 μL / one-injection-per-hemisphere protocol, which is what makes
   the factor exactly 2 rather than unbounded.

**Item 1 is not yet satisfied.** Until it is, the endpoints are reported as *printed values of
uncertain convention*, which is precisely what Δ1 says.
