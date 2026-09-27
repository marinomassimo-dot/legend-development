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

---

## WAVE-2 READINESS (2026-09-27)

**Actor:** `scientist`, wave-2 package "dose". **context_policy declared:** `QUESTION_DRIVEN`.
**Surface read first-hand:** `files/fulltext/PMID42422765_Obeid2026_PMC_2026-09-27.xml` (PMC JATS,
sha256 `7bea83346b708e541d2c432e5da4029f69673e1abc3c6fe70926ad0e3ec2eef2`, efetch `db=pmc id=13343157`,
2026-09-27), re-acquired because `evidence_presence.py` reports **0 of 18** declared artifacts present in
this checkout. Declared in `deepdive_manifests/PMID42422765.json` with its `acquisition_recipe`; logged in
`research/retrieval_manifest.jsonl`. Receipt prepared and **not** recorded (hash chain; parallel packages):
`scratchpad/receipts_pending/dose_42422765_1.json` — `FTR-20260927-42422765-07`, `partial_fulltext_read`,
prior `FTR-20260814-42422765-06`, `reread_reason: new_question_outside_prior_coverage`.

### Verdict: **READY_MINOR** — §7's three verification items are **discharged**

**What was done — the readings, not a note about them.**

| §7 item | Status | Evidence |
|---|---|---|
| **1.** Confirm the printed `1.23` / `2.63` | ✅ **DISCHARGED, and on a better surface than the one asked for.** The values are printed in the **running text and in three captions**, not only on the panel, so they no longer rest on the single raster read of `gr3.jpg`. | *"For translational relevance, we evaluated two clinically applicable doses: an LD (1.23 × 1011 vg) and a higher dose (HD, 2.63 × 1011 vg) (Figure 3A)."* — plus the Figure 3A, Figure 5I–L and Figure 6F captions, all carrying both values. Manifest entry 31. |
| **2.** Confirm no dose appears in the Methods | ✅ **DISCHARGED, machine-checked.** Across the 14,659 characters from *"Materials and methods"* to *"Data and code availability"*, the strings `vg`, `1.23`, `2.63` occur **zero** times; the single vector-quantity sentence is the titre method. | *"Viral titers were determined by RT-qPCR using bGH primers."* Manifest entry 33. |
| **3.** Confirm bilateral ICV / 2.0 μL / one injection per hemisphere | ✅ **DISCHARGED.** | *"…delivering 2.0 μL/hemisphere through a Hamilton syringe with a 32G needle…"* and *"The procedure was repeated for the contralateral hemisphere."* Manifest entry 32. |

⇒ **The sentence *"Item 1 is not yet satisfied"* at the end of §7 is superseded by this section.** Δ1's
phrase *"come stampati"* is now backed by a text surface as well as a panel, and the factor-of-2 bound is
confirmed as **exactly 2** rather than unbounded, because the protocol is one injection per hemisphere.

🆕 **One finding this verification produced that the candidate did not predict, and it matters for Δ1.**
`CC-20260921-TX007-CEILING-AND-DOSE-CONTROL-01` §0 records that the PMC **text** extractor deletes the
exponent, rendering `1.23 × 10¹¹ vg` as `1.23 × 10vg`. In the **JATS XML** the exponent is not deleted — it
is **flattened**: `10<sup>11</sup>` reads as `1011`, so the same dose can be misread as *"1.23 × 1011 vg"*.
🔴 Two extraction routes, two different dose corruptions, both silent, both in a document about
administering a virus to an infant. The rule stands and widens: **no dose is quoted from any extracted
surface without the rendered page or the figure behind it** — and a quote taken from the XML must carry the
flattening, as manifest entries 31 and 33 do.

### Exact operation list for `batch_commit.py propagate`

**File `disease-models/wwox/registries/claim_registry_current.md` · record `CLAIM 011` · op `replace-within`
(Δ1)**

- *old text (verbatim from the current file):* `**LD = 1.23 × 10¹¹ vg**, **HD = 2.63 × 10¹¹ vg**; il braccio a dose bassa **non recupera la sopravvivenza**`
- *new text:* `**LD = 1.23 × 10¹¹ vg**, **HD = 2.63 × 10¹¹ vg** *come stampati* (valori confermati 2026-09-27 anche nel corpo del testo e in tre didascalie, non solo sul pannello — `FTR-20260927-42422765-07`). ⚠️ **La convenzione dell'unità non è mai dichiarata dal primario** — `vg` nudo su tutte le superfici, `hemisphere` non adiacente ad alcuna dose, e **nessuna dose nei Methods** (verificato: 0 occorrenze di `vg`, `1.23`, `2.63` nei 14 659 caratteri dei Methods); l'iniezione è ICV bilaterale, 2.0 μL/emisfero, una per emisfero. La dose **assoluta** ricevuta dall'animale è quindi incerta **di un fattore esattamente 2**: **LD ∈ [1.23, 2.46] × 10¹¹ vg**, **HD ∈ [2.63, 5.26] × 10¹¹ vg**. 🟢 **Il rapporto è invariante: `HD/LD = 2.1382` sotto ogni lettura permessa**, quindi **nulla di ciò che questo flag argomenta dipende dall'ambiguità**: il braccio a dose bassa **non recupera la sopravvivenza**`

**File `.../claim_registry_current.md` · record `CLAIM 011` · op `replace-within` (Δ2)**

- *old text (verbatim):* `` `REVIVAL_TRIGGER`: un braccio a dose intermedia fra 1.23 e 2.63 × 10¹¹ vg localizzerebbe la soglia — l'esperimento più informativo che questo paper implica. ``
- *new text:* Δ2's `AFTER` block, verbatim as this candidate states it (fractional `HD/LD` between 1 and
  2.14, defined as a fraction of the primary's HD; the warning against absolute vg; the second, cheaper
  trigger — an explicit statement of the convention).
  ⚠️ **Merge note:** `CC-20260826-DOSE-ADJUDICATION-01` proposes appending a configuration boundary to the
  **same** sentence. One `replace-within` carrying both, in that order, not two operations.

**File `.../claim_registry_current.md` · record `CLAIM 011` · op `replace-within` (Δ3)**

- *old text (verbatim):* `**Full text status:** complete article plus S1–S8 — latest receipt `FTR-20260814-42422765-06``
- *new text:* the same line, then Δ3's `AMBIGUOUS BUT BOUNDED` block, and then:
  `⚠️ **2026-09-27 — verifica delle unità chiusa sul primario** (`FTR-20260927-42422765-07`, superficie JATS PMC ri-acquisita): i valori stampati sono confermati, i Methods non contengono alcuna dose, il protocollo è una iniezione per emisfero. **Il fattore resta esattamente 2 e non di più.**`

### LOCATOR TRIPLES FOR BLIND AUDIT

| proposition | verbatim quote | anchor |
|---|---|---|
| The LD and HD values are printed in the article's own running text, not only on a panel. | "For translational relevance, we evaluated two clinically applicable doses: an LD (1.23 × 1011 vg) and a higher dose (HD, 2.63 × 1011 vg) (Figure 3A)." | `PMID42422765_Obeid2026_PMC_2026-09-27.xml`, Results, "WWOX gene therapy improves survival and systemic phenotypes in a dose-dependent manner", first paragraph (manifest entry 31) |
| The Methods state no dose; the only vector quantity in them is the titre assay. | "Viral titers were determined by RT-qPCR using bGH primers." | same artifact, Materials and methods, "Plasmid vectors" (manifest entry 33) |
| The protocol is one injection per hemisphere at a fixed volume, which bounds the unit ambiguity at exactly two. | "A Micro-4 nano-pump controller was used to ensure a steady injection rate of 1–1.5 μL/min, delivering 2.0 μL/hemisphere through a Hamilton syringe with a 32G needle (World Precision Instruments)." | same artifact, Methods, "ICV injection of AAV particles into P0-P5 Wwox-null mice" (manifest entry 32) |
| The contralateral hemisphere receives the same injection, so a per-hemisphere reading doubles rather than unbounds the per-animal dose. | "The procedure was repeated for the contralateral hemisphere." | same artifact, same Methods subsection |

**Pending:** nothing of this candidate's own verification. It is batch-ready as a MINOR precision, and it
must be merged with the two other `CLAIM 011` rewrites (`DOSE-ADJUDICATION`, `DOSE-DECISION-TABLE`,
`TX007-CEILING`) into **one** atomic operation list for that record.
