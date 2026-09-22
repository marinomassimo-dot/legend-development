# Recursive re-read cycles 3 and 4 — the CLAIM 038 unit question

**Actor:** Orchestrator · **Date:** 2026-09-22 · **Class:** `DISCOVERY` — non-canonical analysis.
READ-ONLY toward every canonical file. No `BATCH_COMMIT`. **Nothing here is medical advice.**

> 🔴 **§1 AND §2 OF THIS FILE WERE WRITTEN AND COMMITTED BEFORE THE RE-READ.** Results begin at §4.
> If §4 agrees with §2 in every particular, that is a suspicious result and should be read as such.

---

## 1 · Pre-registration — what I already knew at the moment of writing this

**Honesty about the starting surface.** I had, before writing this, read exactly three things bearing
on the question: `claim_registry_current.md` `CLAIM 038` (`Summary` and `Evidence boundary`), the
`CLAIM 036` cross-reference inside it, and lines 27/50/54 of
`research/fulltext_dossiers/PMID17803050.md`. I had **not** opened
`research/page_adjudications/PMID17803050/`, `research/deepdive_manifests/PMID17803050.json`, the
mouse dossier `PMID19936220.md`, or any external source. Those are the surfaces the re-read will
open.

### Cycle 3

| field | value |
|---|---|
| `PAPER` | Suzuki *et al.* 2007, rat `lde/lde`, **PMID 17803050** (receipt `FTR-20260806-17803050-01`) |
| `PREVIOUS QUESTION` | *What seizure, ataxia and histopathological phenotypes does the `lde/lde` rat show?* — read 2026-08-06, yielding `CLAIM 037`, `CLAIM 038`, `CLAIM 039` |
| `NEW QUESTION` | **What unit does the primary actually print for BUN and creatinine in Table 2, and does the paper anywhere state the assay platform or a reference range that fixes the convention?** |
| `WHY THE NEW QUESTION EXISTS` | `CLAIM 038` prints rat BUN as **`mg/ml`**; `CLAIM 036` reasons about the mouse in **`mg/dL`**. The two differ by **100×**. A rat BUN of `40.3 mg/ml` is `4030 mg/dL`, which is not a survivable value; a rat BUN of `40.3 mg/dL` is an ordinary uraemic value. So **either the unit is a transcription error in this repository, or the source itself prints an unusual unit.** These are different defects with different repairs, and the repository currently cannot tell them apart |
| `PREDICTIONS` | **`P1`** the primary prints `mg/dl` (or `mg/dL`) and the repository transcribed it as `mg/ml` — i.e. a **repository-side transcription defect**. **`P2`** the creatinine row will carry the *same* unit token as the BUN row, whatever it is, because they sit in one table column. **`P3`** no assay platform and no reference range is stated anywhere in the paper. **`P4`** the ratio-based statements in `CLAIM 038` (*"~3.2–3.5× normal"*) are **unit-degenerate** and survive either outcome untouched |
| `WHAT WOULD COUNT AS NEW INFORMATION` | The **unit token as printed**, read from a locator rather than from a summary; **or** an explicit statement that the locator set never captured the unit, which would make the repository's `mg/ml` an **unsourced interpolation** — a third possibility I am naming now so that finding it later cannot be reported as having been expected |
| `FALSIFIER` | `P1` is refuted if any inspected locator shows `mg/ml` verbatim in the source. `P4` is refuted if any canonical statement resting on `CLAIM 038` turns out to be an **absolute** rather than a ratio |

### Cycle 4

| field | value |
|---|---|
| `PAPER` | Ludes-Meyers *et al.* 2009, mouse `Wwox`-null, **PMID 19936220** (`PAPER 057`) |
| `PREVIOUS QUESTION` | *What systemic and skeletal phenotypes does the null mouse show, and what does it measure in brain?* — read for `CLAIM 036`/`CLAIM 038`/osteosarcoma adjudication |
| `NEW QUESTION` | **On the mouse side of the same comparison, what unit is printed for BUN/urea and creatinine, and does the paper commit to a convention that makes a rat-versus-mouse numeric comparison legitimate?** |
| `WHY THE NEW QUESTION EXISTS` | `CLAIM 038`'s Evidence boundary already says the BUN elevation is documented *"in **three** places — mouse null, rat `lde/lde`, and the cross-citation between them — with three different implicit explanations and zero follow-up."* A cross-citation between two papers is only evidence if the two numbers are commensurable. **Nobody has checked that they are** |
| `PREDICTIONS` | **`P5`** the mouse paper prints `mg/dL`. **`P6`** the mouse paper's own comparison to the rat, if it makes one, is **qualitative** (*"similarly elevated"*) and not numeric — because a numeric comparison across a 100× unit discrepancy would have been noticed. **`P7`** neither paper states an assay platform |
| `WHAT WOULD COUNT AS NEW INFORMATION` | A **numeric** cross-model comparison in either primary — which would mean a published comparison, not merely a repository one, is standing on the ambiguity |
| `FALSIFIER` | `P6` is refuted by any numeric rat-versus-mouse statement in either primary |

## 2 · What I am committing NOT to do

- 🔴 **No silent normalisation and no silent repair.** §28 of the standing directive is explicit. If
  the source prints the unusual unit, the source is **preserved** and the *cross-model numeric
  comparison* is blocked instead.
- **Direction and significance may remain independently valid** whatever the unit turns out to be,
  and must not be collaterally damaged by a unit repair.
- No canonical file is edited by this act. Any correction leaves here as a **gated commit
  candidate**, not as a propagation.

## 3 · Grading scale, fixed before the result

`NO NEW INFORMATION` · `REDISCOVERY` (the fact is already represented elsewhere in the repository) ·
`NEW DETAIL` · `NEW CONNECTION` · `NEW TESTABLE HYPOTHESIS` · `EXPERIMENT-CHANGING INSIGHT`.

🔴 **A fact already represented elsewhere in this repository grades `REDISCOVERY`, however much work
it took to find.** Three of five returns in the previous re-read round were `REDISCOVERY`, and that
is the primitive behaving correctly, not failing.

---

## 4 · RESULTS — written after the re-read

### 4.0 🔴 The first result is that the baseline check fired on ME

Before writing a word of this section I swept the repository for `creatinin|creatinina`, `mg/ml`
and the CLAIM 038 identifier — **unscoped by file type**, **EN and IT**, across `.md`, `.json` and
`.jsonl`. It returned **two artefacts I did not know existed**:

1. `research/commit_candidates/CC-20260922-CLAIM038-UNIT-CLASS-01.md` — a commit candidate for
   **exactly this defect**, raised by **Scientist G** earlier today.
2. `analysis/peripheral_phenotype_denominator_audit_20260922.md` §3.2 — which already makes the
   **glucose argument** (*"169 mg/**ml** of glucose is 16 900 mg/dL, which is not a number any
   animal survives"*).

🟢 I had independently reconstructed the glucose argument from `entries[26]` and was about to write
it up as the finding of this re-read. **It is a `REDISCOVERY`, and it is graded as one below.**
`enumerate_baseline_before_scoring` has now fired **preventively** for the second time, and for the
first time on the **Orchestrator** rather than on a delegate. That matters for the scorecard: its
success instances were previously delegate-facing, which left open the objection that it measures
hand-back compression rather than a property of the corpus. This instance is neither.

### 4.1 · Cycle 3 — the printed unit, and why the question was harder than either branch allowed

The existing candidate splits the world in two and blocks itself on the split:

> *"Δ1 is conditional on one check this session could not run: the correction must be made against
> the **primary**, not against plausibility. If the primary itself prints `mg/ml`, the correction
> becomes a **flag on the source** rather than an edit to our transcription."*

**I ran that check. The answer is neither branch.**

| surface | what it holds | strength |
|---|---|---|
| `deepdive_manifests/PMID17803050.json` `entries[25]` snippet | `BUN (mg/ml) 12.6 q 4.3 40.3 q 3.7c 10.1 q 2.7 35.6 q 12.8d` | **text layer** |
| `entries[26]` snippet | `GLU (mg/ml) 169.0 q 26.7 145.4 q 26.5 155.0 q 30.1 157.4 q 38.9` | **text layer** |
| `page_adjudications/PMID17803050/adjudications.json` | needle for both rows is the literal string `BUN (mg/ml)` / `GLU (mg/ml)` | **text layer** |
| `page_adjudications/PMID17803050/README.md` adjudication table | *"the page prints"* column reports `12.6 ± 4.3 / 40.3 ± 3.7ᶜ …` for `entries[25]` and `169.0 ± 26.7 …` for `entries[26]` | **rendered page** |

🔴 **`P1` is REFUTED.** The repository did **not** mistranscribe. `mg/ml` is exactly what its
locator holds, faithfully carried into the dossier, the discovery ledger (`:2164`) and
`claim_registry_current.md:707`.

🔴 **But the source-side branch is not established either, and this is the finding.** The README of
that very adjudication states:

> *"The text surface of this paper is `SUSPECT` and refused by `deepdive_manifest.py`: its PDF text
> layer carries **34 C0 controls plus roughly 145 printable substitutions**. It cannot back a
> locator. **The rendered page adjudicates**, because the drawn glyph is the author's and only the
> character code behind it is in doubt."*

The documented substitution map for this exact typesetting is `U+001D → <`, `U+000C → ⁺`,
`– → ⁻`, **`q → ±`** — and `q → ±` is documented **on the BUN row itself**. A `d → m`
substitution is a single printable character in a layer with ~145 of them.

> ### 🎯 The load-bearing sentence of this file
>
> **The crop that contains the unit token was rendered, `crop_contains_span`-verified and
> SHA-256-digested — and the adjudication reports what the page prints for the VALUES and is
> silent on the UNIT.** `p04_table2_BUN_CRE_GLU.png`, page 4, crop `(40, 480, 570, 562)` PDF
> points, 500 dpi, `sha256 9b2268e2d64658b113b3a45e09e93d308ec0d2639004d138012eba46f62fe90b`.
> Every row of the README's *"the page prints"* column restores `±`, `<`, `⁺`, `⁻`. **Not one
> row of it names a unit.**
>
> And the needle that resolves the row — `"BUN (mg/ml)"` — **was taken from the corrupted layer
> and matched against the corrupted layer.** A needle cannot adjudicate the character it is made
> of.

⇒ **`mg/ml` is TRANSCRIBED FAITHFULLY AND UNADJUDICATED.** Not a repository defect, not an
established source defect: **an unverified character in a surface this repository has itself
classified `SUSPECT`, sitting at the one position where the whole cross-model question turns.**

🔴 **This corrects a sibling, and I verified the correction first-hand before writing it.** The
peripheral audit §3.2 concludes *"All three sit on page-adjudicated locators … so the rendered page
is the reference surface and **the damage is bounded**."* The three it names are `(P  0.05)`,
`(Ca2, Na, K, and Cl–)` and `12.6 q 4.3` — **all three are values or operators, and all three were
adjudicated.** The unit was not among them. **The damage is bounded exactly where it was measured
and nowhere else**, and the sentence generalises past its own evidence. This is
`verify_the_omitted_clause` and `gate_is_not_quantity` firing together on **our own evidence
chain** rather than on a paper: *ask what the instrument structurally reported, not what it was
pointed at.*

**`P2` — UNTESTED, and the reason is itself new.** There is **no locator for the `CRE` row at all**.
The 32-locator set captured `entries[25]` (BUN) and `entries[26]` (GLU) from Table 2 and nothing
else from it. The creatinine unit is **not in this repository in any form**, in either the text
layer or the render. `CLAIM 038` prints creatinine values with **no unit**, which is why nobody
noticed.

**`P3` — CONFIRMED, within a stated scope.** *No assay platform, analyser, kit or reference range
was identified within the dossier, deep-dive-manifest and page-adjudication document classes for
PMID 17803050, in English and Italian, unscoped by file type, using
`analyz|analys.r|autoanalyser|Hitachi|Fuji|Dri-Chem|reference range|reference value|kit|colorimetric|enzymatic`,
with `Table 2` returning 1 and 4 hits in the same surfaces as positive control.* ⚠️ The 32-locator
set is **selective**, so this bounds the repository, not the paper.

**`P4` — CONFIRMED.** Every statement `CLAIM 038` actually makes is a **ratio**, a **direction** or
a **significance verdict**: *"~3.2–3.5× normal"*, *`P<0.05`*, *`P<0.01`*, *"uremico senza essere
ipoglicemico"*. The unit **cancels** from all of them. This is the same arithmetic that rescued the
TX-007 dose ratio from its own unit ambiguity, and it is the reason the defect is bounded rather
than fatal.

### 4.2 · Cycle 4 — the mouse side, and a second defect that does not depend on the unit at all

**`P5` — CONFIRMED.** `PMID 19936220` Table 3 prints `mg/dL` on glucose, BUN and calcium
(250.6 → 143.5; 17.67 → 37.25; 11.13 → 10.18), and `mEq/L` on total CO₂.

**`P6` — CONFIRMED.** The mouse paper's only cross-species citation is a **single Discussion
sentence** citing the rat for *seizures* (reference 26 = PMID 19500159). *"The words seizure and
epilepsy occur in the body exactly once each."* **No numeric chemistry comparison is made in either
primary.** The rat-versus-mouse chemistry comparison exists **only in this repository**, which is
the better outcome: nothing published rests on it.

**`P7` — CONFIRMED** for the mouse on the same scope basis as `P3`.

> ### 🔴 And the unprogrammed finding — creatinine was never measured in the mouse
>
> `CLAIM 038`'s **title** reads: *"Elevated BUN and creatinine **recur across Wwox rodent
> models**."* Its `Genotype/model relevance` names the mouse null as the *"misura convergente"*.
>
> *No creatinine measurement for the `Wwox`-null mouse was identified within the dossier,
> session-evaluation and deep-dive-manifest document classes — the complete set of three surfaces
> this repository holds for PMID 19936220 — in English and Italian, unscoped by file type, using
> case-insensitive `creatinin|creatinina|\bCRE\b`; `BUN` returned 3, 1 and 1 hits in the same
> three surfaces as positive control.* Table 3 carries glucose, total CO₂, BUN, calcium and WBC.
> **It carries no creatinine row.**
>
> ⇒ **The recurrence is BUN-only.** Creatinine is measured in **one** model, and the claim's own
> §3.1 rule — as stated by Scientist G — is that *"an analyte is adjudicable as model-invariant or
> model-specific only if it was MEASURED IN BOTH MODELS."* By the repository's own rule, creatinine
> is `UNDETERMINED`, and the claim title asserts recurrence for it. **This defect is independent of
> the unit question and survives whatever the render shows.**

### 4.3 · 🔴 A new tool trap, verified: `CRE` matches `Cre`

A case-insensitive `\bCRE\b` sweep for creatinine across the mouse surfaces returned **8 hits, of
which 8 were the Cre recombinase** — `EIIA-Cre`, `BK5-Cre`, `Cre-loxP`. **100% false-positive rate.**
In a corpus whose models are `EIIA-Cre`, `BK5-Cre`, `Nes-Cre`, `Syn-Cre` and `Alb-Cre`, the
abbreviation for creatinine is **unsearchable case-insensitively**. Same family as `\bBUN\b`
matching *abundance* and `\bbone\b` matching *backbone*, and worse than both, because here the
collision is with the **model nomenclature itself**, so it is dense in exactly the files that would
carry the answer. **Search `creatinin|creatinina` and treat `CRE` as case-sensitive-only.**

### 4.4 · What settles cycle 3, and it is two minutes of a human's time

The repository **already ships the recipe**. On a held copy of the PDF:

```bash
python3 framework/scripts/regenerate_adjudications.py write  --pmid 17803050
python3 framework/scripts/regenerate_adjudications.py verify --pmid 17803050
```

then **read the row label** in `p04_table2_BUN_CRE_GLU.png`. The crop already contains it — the
same crop was widened to x ≈ 570 precisely because the BUN row extends to x ≈ 524, and the row
label sits at the left margin of that rectangle.

🟢 **This converts the existing candidate's blocking check from impossible to trivial.**
`CC-20260922-CLAIM038-UNIT-CLASS-01` blocks Δ1 on *"read the primary"* — and the primary has **no
DOI, no PMCID, an all-rights-reserved notice, and `files/fulltext/` does not exist in this
edition**, so that check cannot be run here at all. Looking at a crop whose rectangle, dpi and
digest we already publish **can** be. `HUMAN_REQUIRED`, and it is the cheapest open item in the
session.

⚠️ **And it must actually be looked at.** The instrument was pointed at this row once already and
returned everything except the answer.

### 4.5 · Grades, against the scale fixed in §3

| cycle | item | grade |
|---|---|---|
| 3 | *glucose at 169 mg/ml is not survivable ⇒ the rat values are numerically mg/dL* | 🟡 **`REDISCOVERY`** — held by `peripheral_phenotype_denominator_audit_20260922.md` §3.2 since earlier today |
| 3 | *the mouse/rat comparison needs no external reference range — 250.6 mg/dL vs 169.0 "mg/ml" is internal* | 🟡 **`REDISCOVERY`**, same source, same table |
| 3 | **the unit token is `SUSPECT`-layer and UNADJUDICATED, and the render that would settle it reported only the values** | 🟢 **`NEW CONNECTION`** — the `SUSPECT` classification and the unit sat in two different files and had never been put together |
| 3 | **the needle `"BUN (mg/ml)"` is drawn from the layer it is used to adjudicate** | 🟢 **`NEW DETAIL`**, and a method defect in the adjudication recipe, not in the science |
| 3 | *"the damage is bounded"* generalises past the three characters that were actually adjudicated | 🟢 **`NEW DETAIL`** — a correction to a sibling, verified first-hand against the README before writing |
| 3 | **no locator exists for the `CRE` row; the creatinine unit is nowhere in this repository** | 🟢 **`NEW DETAIL`** |
| 4 | **creatinine was never measured in the mouse ⇒ `CLAIM 038`'s title overstates recurrence** | 🟢 **`EXPERIMENT-CHANGING INSIGHT`** for the claim, in the weak sense that it changes what the claim may assert and is independent of the unit question |
| 4 | no numeric cross-model chemistry comparison exists in either primary | 🟢 **`NEW DETAIL`** — the exposure is entirely ours |
| — | `\bCRE\b` matches `Cre` recombinase at 100% FP in this corpus | 🟢 **`NEW DETAIL`** (tool trap) |

**Two `REDISCOVERY`, six `NEW DETAIL`/`NEW CONNECTION`, one claim-changing.** Consistent with the
prior round's yield profile: the primitive returns a mixture, and the mixture is the honest result.

### 4.6 · What leaves this file

- `CC-20260922-CLAIM038-UNIT-CLASS-01` is **superseded in its Δ1 reasoning** and must be
  re-presented. That is **candidate 7** of the Operator packet — `CC-20260922-CLAIM038-UNIT-CLASS-02`.
- 🔴 **No canonical file is edited by this act.** No unit is normalised, no unit is repaired, and
  the source is preserved exactly as transcribed. §28 of the standing directive is honoured in the
  only way the evidence permits: **the ambiguity is named, the cross-model numeric comparison is
  blocked, and direction and significance are left untouched.**

---

## 5 · V0 SHADOW TRACE

| step | what happened |
|---|---|
| `BASELINE` | 🟢 **Fired preventively.** Unscoped bilingual sweep found an existing commit candidate and a sibling audit holding the argument I was about to claim. Two findings demoted to `REDISCOVERY` **before** publication |
| `DIVERGE` | Three branches, not the two the existing candidate allowed: repository mistranscription · source misprint · **token unadjudicated on a `SUSPECT` surface**. The third is the one that held |
| `CONNECT` | Within-repository rather than cross-domain: the page-adjudication README's `SUSPECT` classification ↔ `CLAIM 038`'s unit. Two files, never previously joined |
| `PREDICT` | 7 pre-registered. **`P1` REFUTED** · `P2` UNTESTED (no locator exists) · `P3` `P4` `P5` `P6` `P7` CONFIRMED. **The refutation of `P1` is what produced the finding** — had I written the question afterwards I would have reported "the repository mistranscribed", which is false |
| `SEARCH` | No external retrieval. Every value is a repository-held attestation with its receipt. **No PubMed count appears in this file, and none would have been evidence** |
| `ADJUDICATE` | `mg/ml` = `TRANSCRIBED FAITHFULLY AND UNADJUDICATED`. Creatinine recurrence = `UNDETERMINED` by the repository's own §3.1 rule |
| `REVISIT` | The settling act is specified, costed at ~2 minutes and `HUMAN_REQUIRED`; the crop already exists as a published recipe |
| **produced nothing** | `CONNECT` produced no cross-domain import — this was an internal-consistency problem throughout, and forcing an external analogy would have been padding |
