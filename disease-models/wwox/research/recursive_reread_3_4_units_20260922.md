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

*(empty at pre-registration; `fd` anchor below)*
