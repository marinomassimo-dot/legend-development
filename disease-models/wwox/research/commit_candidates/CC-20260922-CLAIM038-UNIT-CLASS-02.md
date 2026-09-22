# CC-20260922-CLAIM038-UNIT-CLASS-02

**Status:** 🔴 **PROPOSED — NOT PROPAGATED**
**Supersedes:** `CC-20260922-CLAIM038-UNIT-CLASS-01` (Scientist G) — **in its Δ1 reasoning only.**
Δ2 of `-01` is unchanged, unconditional and carried forward verbatim.
**Target:** `claim_registry_current.md` → `CLAIM 038` (Title, Summary, Evidence boundary)
**Change class:** **QUALIFY a unit annotation + BOUND a cross-model comparison + NARROW a title.**
No finding is reversed, demoted or removed. **No unit is normalised and no unit is repaired.**
**Review floor:** R2. **BLOCK-1:** no molecule, no dose, no route. Nothing here is medical advice.
**Found by:** Orchestrator, `research/recursive_reread_3_4_units_20260922.md` (cycles 3 and 4,
pre-registered at `3d0a558` **before** any locator was opened).
**Producer ≠ verifier:** `-01` was raised by Scientist G and verified by me; this candidate
corrects my own verification of it, first-hand against the page-adjudication README.

---

## 1 · Why `-01` cannot be propagated as written

`-01` blocks its own primary edit:

> *"🔴 **Δ1 is conditional on one check this session could not run:** the correction must be made
> against the **primary**, not against plausibility. If the primary itself prints `mg/ml`, the
> correction becomes a **flag on the source** rather than an edit to our transcription."*

**That check has now been run, and the answer is neither of the two branches `-01` allows.**

| | |
|---|---|
| **`-01` branch A** — the repository mistranscribed | 🔴 **REFUTED.** `mg/ml` is exactly what the locator holds: `deepdive_manifests/PMID17803050.json` `entries[25]` snippet = `BUN (mg/ml) 12.6 q 4.3 …`, `entries[26]` = `GLU (mg/ml) 169.0 q 26.7 …`. The dossier, the discovery ledger `:2164` and `claim_registry_current.md:707` all carry it faithfully |
| **`-01` branch B** — the source misprints it | 🔴 **NOT ESTABLISHED.** The token comes from a text layer this repository has itself classified **`SUSPECT`** and which `deepdive_manifest.py` **refuses** |
| **branch C — the one that holds** | 🟢 **The token is TRANSCRIBED FAITHFULLY AND UNADJUDICATED** |

## 2 · The evidence for branch C, from this repository's own files

`page_adjudications/PMID17803050/README.md`:

> *"The text surface of this paper is `SUSPECT` … its PDF text layer carries **34 C0 controls plus
> roughly 145 printable substitutions**. It cannot back a locator. **The rendered page
> adjudicates.**"*

Documented substitution map for this typesetting: `U+001D → <` · `U+000C → ⁺` · `– → ⁻` ·
**`q → ±`**. The last of these is documented **on the BUN row itself**. A `d → m` substitution is
one printable character in a layer carrying ~145 of them.

🔴 **And the render that would settle it was made, verified and digested — and reported only the
values.** `p04_table2_BUN_CRE_GLU.png`, page 4, crop `(40, 480, 570, 562)` PDF points, 500 dpi,
`sha256 9b2268e2d64658b113b3a45e09e93d308ec0d2639004d138012eba46f62fe90b`, `crop_contains_span`
verified. The README's *"the page prints"* column restores `±`, `<`, `⁺`, `⁻` for five locators.
**No row of it names a unit.**

🔴 **The needle is made of the character it is used to find.** `adjudications.json` resolves both
rows with the literal needles `"BUN (mg/ml)"` and `"GLU (mg/ml)"` — strings taken from the corrupted
layer and matched against the corrupted layer. **A needle cannot adjudicate the character it is
made of.** This is a defect in the adjudication *recipe*, not in the science it certified.

⚠️ **Correction to a sibling, stated plainly because it is load-bearing.**
`peripheral_phenotype_denominator_audit_20260922.md` §3.2 concludes *"All three sit on
page-adjudicated locators … so the rendered page is the reference surface and **the damage is
bounded**."* The three it names — `(P  0.05)`, `(Ca2, Na, K, and Cl–)`, `12.6 q 4.3` — **are all
values or operators, and all three were adjudicated.** The unit was not among them. The damage is
bounded exactly where it was measured. **Scientist G's scientific conclusion is untouched and
correct; only the sufficiency claim on the evidence chain is narrowed.**

## 3 · What is true regardless of the render, and needs no external reference range

Internal to this repository, requiring no textbook range:

| analyte | mouse `Wwox^ΔCre/ΔCre` P18, printed | rat `lde/lde` 28 d, printed |
|---|---|---|
| glucose | 250.6 → 143.5 **mg/dL** | 169.0 / 145.4 / 155.0 / 157.4 **"mg/ml"** |
| BUN | 17.67 → 37.25 **mg/dL** | 12.6 → 40.3 / 10.1 → 35.6 **"mg/ml"** |
| calcium | 11.13 → 10.18 **mg/dL** | 9.5 / 8.9 / 8.9 / 8.8 **"mg/ml"** |

**Three analytes, two species, same numeric decade.** Under a literal `mg/ml` reading every rat
value would exceed its mouse counterpart by **exactly 100×, on every row**. ⇒ **The rat values are
numerically commensurable with the mouse only under a `mg/dL` reading.** *(This argument is a
`REDISCOVERY` — `peripheral_phenotype_denominator_audit_20260922.md` §3.2 reached it earlier today
from the glucose row. It is restated here because it is what makes Δ2 unconditional.)*

## 4 · The second defect, independent of the unit and not in `-01` at all

`CLAIM 038`'s **title**: *"Elevated BUN **and creatinine** recur across Wwox rodent models."*
Its `Genotype/model relevance`: the mouse null as *"misura convergente"*.

> *No creatinine measurement for the `Wwox`-null mouse was identified within the dossier,
> session-evaluation and deep-dive-manifest document classes — the complete set of three surfaces
> this repository holds for PMID 19936220 — in English and Italian, unscoped by file type, using
> case-insensitive `creatinin|creatinina|\bCRE\b`, with `BUN` returning 3, 1 and 1 hits in the same
> three surfaces as positive control. Every `CRE` hit resolved to the `Cre` recombinase.*

Table 3 carries glucose, total CO₂, BUN, calcium and WBC. **It carries no creatinine row.**
By the rule Scientist G states in the same audit — *"an analyte is adjudicable as model-invariant
or model-specific only if it was MEASURED IN BOTH MODELS"* — **creatinine is `UNDETERMINED`**, and
the title asserts recurrence for it. 🔴 **This survives whatever the render shows.**

## 5 · Proposed edits (exact, none applied)

**Δ1′ — replaces `-01`'s Δ1. QUALIFY, do not correct.** Leave `mg/ml` **exactly as transcribed** in
`CLAIM 038`'s Summary and append inline:

> ⚠️ **`mg/ml` è l'unità come trascritta dal locator, e NON è aggiudicata.** Il livello di testo del
> PDF di `PMID 17803050` è classificato **`SUSPECT`** da questo repository (34 controlli C0, ~145
> sostituzioni stampabili; `q → ±` documentato **sulla riga BUN stessa**). Il render che
> aggiudicherebbe il token esiste come ricetta — `p04_table2_BUN_CRE_GLU.png`, crop
> `(40, 480, 570, 562)` @500 dpi — ma **aggiudica solo i valori, mai l'unità**. I valori sono
> commensurabili col topo **soltanto** sotto una lettura `mg/dL`. **Nessuna normalizzazione è
> applicata: la fonte è preservata come stampata.**
> **`REVIVAL_TRIGGER`:** rigenerare quel crop da una copia del PDF e **leggere l'etichetta di riga**.

**Δ2 — carried forward from `-01` unchanged and unconditional.** Append to `CLAIM 038`,
cross-referenced from `CLAIM 036`:

> ⚠️ **Nessun confronto numerico fra modelli è autorizzato da queste due claim** — solo **direzione
> e significatività**. Le chimiche di topo e ratto sono state misurate in laboratori, età, sessi e
> piattaforme diversi, e le unità del registro divergono di un fattore 100 non aggiudicato.
> Un'affermazione della forma *"il ratto ha BUN più alto del topo"* non è ricostruibile.

**Δ3 — NEW. Narrow the title.** From *"Elevated BUN **and creatinine** recur across Wwox rodent
models"* to *"Elevated BUN recurs across Wwox rodent models, **and creatinine is elevated in the rat
where alone it was measured**"*, with an `Evidence boundary` line:

> 🔴 **La creatinina è misurata in **un solo** modello.** Table 3 di `PMID 19936220` non porta alcuna
> riga creatinina. Per la regola di questo repository — *un analita è aggiudicabile come
> modello-invariante solo se misurato in ENTRAMBI i modelli* — la ricorrenza della creatinina è
> **`UNDETERMINED`**, non un dato. `REVIVAL_TRIGGER`: qualunque misura di creatinina in un modello
> murino `Wwox`.

**Δ4 — NEW, and it is the cheapest item in the packet.** Add to
`page_adjudications/PMID17803050/README.md` a line recording that **the unit tokens of Table 2 were
not adjudicated**, and that a needle drawn from a `SUSPECT` layer cannot certify its own characters.
*(This is a non-canonical documentation surface; it is listed here so it lands in the same act.)*

## 6 · What this candidate does NOT do

- It does **not** rewrite `mg/ml` to `mg/dL` anywhere. **§28 is explicit and is honoured.**
- It does **not** assert the source misprints the unit. That remains unestablished.
- It does **not** touch `CLAIM 038`'s direction, significance, belief level or evidence class.
  *"Uremico senza essere ipoglicemico"* is a statement about **signs** and is untouched.
- It does **not** re-open the renal-versus-hypercatabolism question, which stays two untested
  `IPOTESI`.
- It does **not** propagate.

## 7 · Reversibility and consequence

| | |
|---|---|
| **Severity** | 🟡 **MEDIUM** for Δ1′/Δ2 (they bound how a number may be *used*); 🟡 **MEDIUM** for Δ3 (it narrows a canonical **title**, which downstream actors read as the claim) |
| **Reversibility** | **Trivial** — all four are text-only, additive, and no claim status changes |
| **Dependent surfaces** | `CLAIM 036` (the mouse counterpart) · `discovery_ledger_current.md:2164` · `fulltext_dossiers/PMID17803050.md:54` · `peripheral_phenotype_denominator_audit_20260922.md` §3.2 · `CLAIM 037`/`CLAIM 039` (same primary, unit-independent) |
| **Therapeutic consequence** | **None.** No strategy, molecule or endpoint depends on these figures |

## 8 · Verification required before propagation

1. 🟢 **Already done:** the printed-unit check `-01` blocked on. Result: `UNADJUDICATED` (§2).
2. `HUMAN_REQUIRED`, ~2 minutes, and the only route this edition permits —
   `regenerate_adjudications.py write --pmid 17803050`, then **read the row label** in
   `p04_table2_BUN_CRE_GLU.png`. ⚠️ **It must actually be looked at:** the instrument was pointed at
   this row once already and returned everything except the answer.
3. If the render shows `mg/dl`: Δ1′ becomes a **transcription correction** (branch A after all,
   at the *render* rather than at the *locator*), and Δ2/Δ3/Δ4 are unaffected.
   If it shows `mg/ml`: Δ1′ becomes a **flag on the source**, and Δ2/Δ3/Δ4 are unaffected.
   🟢 **Δ2, Δ3 and Δ4 are unconditional under both outcomes** — which is why this candidate is
   propagatable now and `-01` was not.
4. Re-run `legend_lint`, `growth_anchors check` and the publication gate after any edit.
