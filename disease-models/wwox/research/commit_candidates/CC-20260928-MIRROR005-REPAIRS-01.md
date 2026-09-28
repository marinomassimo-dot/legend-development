# COMMIT CANDIDATE — CC-20260928-MIRROR005-REPAIRS-01

**Candidate ID:** CC-20260928-MIRROR005-REPAIRS-01
**Status:** `PROPOSED — NOT PROPAGATED`
**Base head:** `3fe7c49` — `main` at the time this task branched (`task/mirror-b11-repair`). A peer
session also lands on `main`, so both `old` strings below were re-measured for uniqueness in the
working tree immediately before this file was written and **must be re-measured by the propagating
batch**.
**Author:** ACTOR_ID `scientist`, task `mirror-b11-repair`, dispatched by the Orchestrator under the
operator's standing authorisation of 2026-09-28. §21d's RESERVED list binds.

**Source, read in full and verified first-hand rather than taken on trust:** the Mirror ex-post review
of `BATCH_20260928_004` (peer, structural) + `BATCH_20260928_005` (MINOR), persisted verbatim at
[`../session_evaluations/2026-09-28_BATCH_20260928_004_005_mirror_review.md`](../session_evaluations/2026-09-28_BATCH_20260928_004_005_mirror_review.md)
— 1 **BLOCKING-SCIENTIFIC** (B11), 6 MINOR, 3 NOTE, plus a `WHERE I WAS WRONG` section and a
`WHAT_WOULD_CHANGE_MY_MIND` list whose falsifiers are re-run here rather than accepted.

## 0 · Two ops, one batch, and why they travel together

They touch **different files** (`claim_registry_current.md`, `working_model_current.md`), so they do
not collide; they are in one candidate because both are **alignments of a canonical record with a
record it already contains**, neither adds a proposition, and both were raised by the same review.
Neither is a scientific narrowing in the sense that would owe blind-audit triples: `C32-1` **moves
bytes** and adds none, and `WM-A9` **removes an assertion the same file's own claim record does not
make**. Locator triples are therefore not supplied, and the reason is stated rather than left to be
inferred.

## 1 · Op list — `old` verbatim, measured unique

### 1.1 · `C32-1` — Mirror **B11**, a `DO_NOT_INFER` prohibition re-joined to its own grounds

**File** `disease-models/wwox/registries/claim_registry_current.md`, `CLAIM 032`. **Class** `MINOR`
— **byte-conserving move, zero prose composed.** **Measured** → **1** (the whole two-line `old` occurs
once in the file; the moved run's opening literal also occurs exactly once).

**What `BATCH_20260928_005`'s op `B2` did.** `B2` inserted the new `DO_NOT_CITE` paragraph about the
`P47T/WT` heterozygote **inside** the existing `DO_NOT_INFER` paragraph, splitting a prohibition from
its grounds and re-parenting the grounds under a prohibition about a **different allele**. Because the
insertion conserved every byte, it was invisible to `propagate`'s "every byte outside the addressed
records unchanged" proof, to every presence check, and to `grep -c "Concatenarle in"` (= 1 at every
revision).

**Falsifier re-run first-hand, as Mirror asked.** At `a923e10` the `DO_NOT_INFER` is a **single line**
carrying header **and** grounds — **693 characters / 707 bytes** — so the join is this op's and not
pre-existing. ⚠️ **NOTE on the review's own figures:** Mirror's `212 B` / `2,619 B` / `481 B` are
**character** counts, not bytes (the paragraph is dense in multi-byte glyphs: 🔴, `−`, `«»`, accented
vowels). Measured in bytes at HEAD: line 615 = **219 B** (212 chars), line 616 = **2,659 B** (2,619
chars), the misplaced run = **488 B** (481 chars), the `a923e10` single line = **707 B** (693 chars).
The finding is unaffected; the unit is corrected so the next reader measures the same thing.

**Why this is worth a batch.** In this system a prohibition's force is that a reader can check it.
Line 615 as it stands is a bare edict with no stated grounds — *"…la catena fra loro è vietata."* and
nothing else — which is what a future batch relaxes. And the grounds, re-parented, now argue across the
`P47T ≠ Q230P` boundary: the `DO_NOT_CITE` paragraph is about a **missense** heterozygote, the grounds
are about a **null/wild-type** genotype, and they were joined to the `DO_NOT_CITE`'s `REVIVAL_TRIGGER`
by a single space.

`old`:
```
🔴 **`DO_NOT_INFER` (2026-09-27, `CC-20260826-CROSS-CLAIM-CENSUS-03` §1, `BATCH_20260927_004`) — questa claim e [[claim_registry_current#CLAIM 033]] concordano, e proprio per questo la catena fra loro è vietata.**
🔴 **`DO_NOT_CITE` — the `P47T/WT` heterozygote of [[paper_registry_current#PAPER 007]] is not a demonstrated negative for haploinsufficiency (`CC-20260826-PMID36828035-01` §2.6, verified at source 2026-09-28).** Three separate reasons, each sufficient on its own. **(1) The survival negative is a TREND, not a null.** The body reads *«but the difference was not statistically significance»* [sic] over **495 ± 23 versus 542 ± 8 days** — a reduction that failed to reach significance, with **no power reported**. *Not significant* is not *not different* when the design cannot resolve the difference; this is the same reading `CLAIM 040` applies to panel 7C of [[paper_registry_current#PAPER 011]]. **(2) The glial negative is unverifiable.** *«however no differences were observed when compared with the wildtype mice (data not shown)»* — a *data not shown* negative may not be cited as evidence of heterozygote normality. **(3) Heterozygotes are named in a POSITIVE finding:** *«displayed signs of cholestasis with enlarged gallbladders, and a few animals had evidence of focal liver degeneration»*, attributed to Supplementary Table 4, **which is not retrieved here** — the sentence is asserted, the table's contents are not. 🔴 **And the genetic object is different.** `P47T/WT` is a **missense** heterozygote — one partial-loss-of-function allele in trans with wild type — while this claim is about **haploinsufficiency**, a null/wild-type genotype with one fully functional allele. The paper's own favourable sentence, *«the introduction of the P47T mutation had no detrimental effect on normal mouse growth or reproduction»*, sits in the **Discussion**, covers growth and reproduction only, and is not a survival, cognitive, EEG or excitability endpoint. ⇒ this paper is **at best weak corroboration** of this claim, with a liver finding attached, and it is **not** the demonstrated negative the review's *«haploinsufficiency appears not to be deleterious»* would need. `REVIVAL_TRIGGER`: a powered survival comparison of a **null** heterozygote against wild type, or an EEG/cognitive endpoint in any WWOX heterozygote of any allele. L'evidenza di questa claim è il topo `Wwox^+/−` e i portatori umani: un genotipo **null/wild-type**, con un allele **pienamente funzionale**. La classe che sopravvive meglio in `CLAIM 033` porta **un allele missense** di funzione residua **non misurata**. Concatenarle in *«un allele missense vale quasi un allele wild-type»* **non è sostenuto da nessuna delle due**, e la riserva (1) di `CLAIM 033` falsifica la premessa direttamente: Q230P è missense e **abolisce** la proteina.
```

`new`:
```
🔴 **`DO_NOT_INFER` (2026-09-27, `CC-20260826-CROSS-CLAIM-CENSUS-03` §1, `BATCH_20260927_004`) — questa claim e [[claim_registry_current#CLAIM 033]] concordano, e proprio per questo la catena fra loro è vietata.** L'evidenza di questa claim è il topo `Wwox^+/−` e i portatori umani: un genotipo **null/wild-type**, con un allele **pienamente funzionale**. La classe che sopravvive meglio in `CLAIM 033` porta **un allele missense** di funzione residua **non misurata**. Concatenarle in *«un allele missense vale quasi un allele wild-type»* **non è sostenuto da nessuna delle due**, e la riserva (1) di `CLAIM 033` falsifica la premessa direttamente: Q230P è missense e **abolisce** la proteina.
🔴 **`DO_NOT_CITE` — the `P47T/WT` heterozygote of [[paper_registry_current#PAPER 007]] is not a demonstrated negative for haploinsufficiency (`CC-20260826-PMID36828035-01` §2.6, verified at source 2026-09-28).** Three separate reasons, each sufficient on its own. **(1) The survival negative is a TREND, not a null.** The body reads *«but the difference was not statistically significance»* [sic] over **495 ± 23 versus 542 ± 8 days** — a reduction that failed to reach significance, with **no power reported**. *Not significant* is not *not different* when the design cannot resolve the difference; this is the same reading `CLAIM 040` applies to panel 7C of [[paper_registry_current#PAPER 011]]. **(2) The glial negative is unverifiable.** *«however no differences were observed when compared with the wildtype mice (data not shown)»* — a *data not shown* negative may not be cited as evidence of heterozygote normality. **(3) Heterozygotes are named in a POSITIVE finding:** *«displayed signs of cholestasis with enlarged gallbladders, and a few animals had evidence of focal liver degeneration»*, attributed to Supplementary Table 4, **which is not retrieved here** — the sentence is asserted, the table's contents are not. 🔴 **And the genetic object is different.** `P47T/WT` is a **missense** heterozygote — one partial-loss-of-function allele in trans with wild type — while this claim is about **haploinsufficiency**, a null/wild-type genotype with one fully functional allele. The paper's own favourable sentence, *«the introduction of the P47T mutation had no detrimental effect on normal mouse growth or reproduction»*, sits in the **Discussion**, covers growth and reproduction only, and is not a survival, cognitive, EEG or excitability endpoint. ⇒ this paper is **at best weak corroboration** of this claim, with a liver finding attached, and it is **not** the demonstrated negative the review's *«haploinsufficiency appears not to be deleterious»* would need. `REVIVAL_TRIGGER`: a powered survival comparison of a **null** heterozygote against wild type, or an EEG/cognitive endpoint in any WWOX heterozygote of any allele.
```

**The three verifications this op owes, all mechanical:**

1. line 615 after the op equals its `a923e10` form **byte-for-byte** (707 B, sha256 compared);
2. line 616 after the op ends at *"…in any WWOX heterozygote of any allele."*;
3. `grep -c "Concatenarle in"` stays at **1**.

### 1.2 · `WM-A9` — Mirror **A9**, the working model asserting more than its own claim record

**File** `disease-models/wwox/registries/working_model_current.md`, section `Working Model Current`
(the pre-`BLOCK 1` live model text, line 65). **Class** `MINOR` — **mechanical alignment**.
**Measured** → **1**.

`working_model_current.md:65` reads *"the inhibition is **S9-independent** (GSK3β abundance and
phospho-S9 unchanged while kinase output changes)"*. Its own `CLAIM 035` says only *«tutto questo
avviene con **fosfo-GSK3β-S9 invariata**»* — phospho-S9, nothing about total abundance — and
`CLAIM 035`'s `Clinical meaning` (2) likewise names only the anti-phospho-S9 western.

🔴 **Mirror's falsifier was run before acting, and it was only PARTLY testable here.** Mirror did not
read the artefact; it is present in the ROOT checkout as
`files/fulltext/PMID22193544_Wang2012_PMC.xml` (PMC3354054), and it was read here.

- **Testable, and it runs Mirror's way.** The article's **only** invariance statement is
  *«we also examined whether the phosphorylation level of GSK3β and its downstream target, β-catenin,
  are affected by RA treatment. We found that the phosphorylation levels of phospho-GSK3βS9 and
  phospho-β-catenin remained normal.»* — **phospho** species only. Figure 1b blots total `GSK3β`
  alongside `phospho-GSK3βS9` and Figure 1c densitometers the Figure 1b panel, so the **measurement
  exists**; no sentence anywhere in the article asserts that total GSK3β is unchanged. That is exactly
  what this same working-model line already records two sentences later, from
  `BATCH_20260927_004`: *«what is absent is the **stated invariance**, not the measurement —
  `NOT_ASSERTED`, not `MEASURE_ABSENT`»*. So the working model contradicts its own adjacent
  qualification.
- **NOT testable: the densitometric panel itself.** Whether Figure 1c's bars *show* total-GSK3β
  invariance cannot be decided here. The figure images (`cdd2011188f1.jpg` … `f6.jpg`) are **not** in
  the local corpus — only the PMC XML is — and PMC's image endpoints returned HTML, not the image, on
  three routes tried. **Declared, not worked around:** no receipt was written, no new full-text route
  was opened, and nothing below rests on the panel.

⇒ **The repair runs Mirror's way on the source's own text**: `CLAIM 035` is right and the working
model is the over-scoped record. Had the panel been readable and flat, it would still not have made
the working model right, because a densitometric bar the authors never interpret is a measurement and
not a stated invariance — but that argument is **not** relied on, and the panel is recorded as untested.

`old`:
```
(GSK3β abundance and phospho-S9 unchanged while kinase output changes)
```

`new`:
```
(phospho-S9 unchanged while kinase output changes) [corrected 2026-09-28 from «GSK3β abundance and phospho-S9 unchanged» by `CC-20260928-MIRROR005-REPAIRS-01` `WM-A9`: the source states invariance for phospho-GSK3βS9 only]
```

⚠️ **NOTE carried forward, not repaired here.** After this op the `BATCH_20260927_004` qualification
sentence that follows (*"Qualification of the parenthesis above…"*) reads as the **grounds** for the
deletion rather than as a qualification of a live over-assertion. It stays **true** and it stays live —
total GSK3β is measured and its invariance is not stated — so it is not touched. Whether its opening
clause should be re-pointed is left to Mirror, deliberately, rather than decided by the actor that
created the condition.

## 2 · What this candidate does NOT carry

- **No new proposition, no status change, no `BLOCCO 1` change, no therapeutic recommendation.**
- **No claim's stated conclusion is overwritten.** `C32-1` changes no word; `WM-A9` removes a clause
  the record it mirrors never asserted, and carries the removed wording verbatim in situ.
- **No receipt is written or recorded.** Wang 2012 is covered by a standing `complete_fulltext_read`
  receipt on the same fingerprint, and re-reading it for a falsifier opened no new route.
- **No blind-audit triples**, for the reason in § 0.

## 3 · Readiness

| op | file | `old` count measured | window |
|---|---|---|---|
| `C32-1` | `claim_registry_current.md` · `CLAIM 032` | **1** | working tree, immediately before propagation |
| `WM-A9` | `working_model_current.md` · `Working Model Current` | **1** | same |

**Target:** `WM_v7.4` → **`WM_v7.5`**, MINOR, MANUAL.

**Not medical advice.**
