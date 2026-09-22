# COMMIT CANDIDATE — CC-20260922-GTGT-CNS-QUALIFICATION-01

**Source:** Orchestrator, working the `Wwox^gt/gt` residual-WWOX qualification node directly while
both Scientist slots were occupied. All queries, counts and translations below were run in this act.
**Change class:** **MINOR** in edit size, 🔴 **and it closes the highest-value row of the horizon
table with a measured negative** rather than an assumed one.
**Target:** `discovery_ledger_current.md` (`H11` / `TX-002` / `TX-003` platform question) ·
`claim_registry_current.md` `CLAIM 032` (already queued separately — **not** repaired here).
**Status:** `PROPOSED — NOT PROPAGATED`.
**Review floor:** **R2.**
**Proposes:** `D-35` and `D-36` (§4).
**BLOCK-1:** no molecule, no dose, no route, no safety claim. Nothing here is medical advice.

---

## 1 · 🔴 The answer: residual brain WWOX in `Wwox^gt/gt` is NOT established, and nobody has looked

**The primary is unreachable and was attempted.** `PMID 17823927` (Ludes-Meyers 2007,
*Genes Chromosomes Cancer* 46(12):1129–36, [DOI](https://doi.org/10.1002/gcc.20497)) carries
`PMC4143238` — a PMCID this repository had recorded as absent —
and `get_full_text_article(pmc_ids=["PMC4143238"])` returns **`full_text: ""`**.
**Unacquirable by attempt, not by inference from a licence.**

**What its abstract actually says, verbatim:**

> *"Homozygous Wwox gene-trap mice (Wwox(gt/gt)) had **no detectable Wwox protein in most tissues
> examined**, although, **a low level could be detected in a minority of tissues**. Because of these
> observations, we concluded that these mice are Wwox hypomorphs."*

🔴 **The abstract names none of those tissues. It does not name brain, and it does not name
cerebellum.** The hypomorph designation is the authors' conclusion from a tissue panel nobody here
can see.

### 1a · And no other paper supplies it — measured, with a positive control

| query | `total_count` | translation | result |
|---|---:|---|---|
| `Wwox gene-trap hypomorphic mice` | **1** | ✅ fully expanded (`wwox protein human` Supplementary Concept fired; `gene-trap` and `hypomorph*` variants expanded; `mice` → MeSH) | **the primary itself, and nothing else** |
| `Wwox hypomorph AND (brain OR cerebellum OR neuron OR CNS)` | **1** | ✅ expanded — ⚠️ the `CNS` limb partly mis-expanded to journal names (`clin nurse spec`[Journal]); the `brain`/`cerebellum`/`neuron` limbs expanded correctly and carry the result | **`PMID 36779245` — a human patient cohort, NOT a `gt/gt` study** |
| **positive control:** `Wwox knockout AND (brain OR cerebellum OR neuron)` | **14** | ✅ identical form, identical expansions | **the query form works** |

> 🎯 **One word changed — `hypomorph` for `knockout` — takes the same query from 14 records to zero
> relevant ones. The form is validated by its own control, so this is a measurement and not a
> parser artefact.**

⚠️ **Bound, stated rather than glossed:** `[All Fields]` does **not** index Methods or supplements,
so these counts mean *"no paper is framed around `gt/gt` CNS WWOX"* — **never** *"no such measurement
exists in any supplement anywhere."* The stronger claim is not made.

---

## 2 · The only permitted statement, and the prohibition that follows

> **Low Wwox protein was reported in a minority of tissues; residual BRAIN protein is not
> established.**

🔴 **Therefore `Wwox^gt/gt` must NOT be called a validated hypomorph for CNS therapeutic rescue**
unless and until CNS residual expression is demonstrated. *"Hypomorph"* is a conclusion about a
tissue panel; *"a platform for boosting residual neuronal WWOX"* is a claim about the brain, and the
second does not follow from the first.

⚠️ **This is already an overstatement in CANONICAL text.** `claim_registry_current.md` `CLAIM 032`
states *"il topo **ipomorfo** `Wwox^gt/gt` (**proteina bassa ma rilevabile**) è **vitale**"* —
*"low but detectable protein"*, unqualified, generalising a minority-of-tissues finding to the
animal. **Not repaired here:** `CC-20260921-CLAIM032-HYPOMORPH-PREMISE-01` already queues exactly
this defect, and duplicating a repair across two candidates is how a registry acquires two
divergent fixes for one problem.

---

## 3 · 🎯 What this closes — `H11`, and the closure is now measured

`H11` is the highest-value row of `CC-20260922-MODEL-HORIZON-01`'s horizon table: **`TX-002`
(CRISPRa) and `TX-003` (proteostatic boost) require an animal that HAS residual protein to boost.**

- the **null** has none, by definition;
- **`P47T`** has **wild-type-level** protein — nothing to upregulate, and boosting it amplifies a
  binding-dead protein;
- **`Wwox^gt/gt`** is **the only structurally correct animal in the corpus** —

— and **its qualifying measurement has never been made, by anyone.** That was previously recorded as
*"blocked by one unmade Western blot."* **It is now measured: not merely unmade, but never attempted
in any published study, with a validated query form and a positive control behind the negative.**

🔵 **The `REVIVAL_TRIGGER` is unchanged and now has its evidence:**
`CC-20260921-CLAIM032-HYPOMORPH-PREMISE-01` already names *"il pannello western per tessuto di
`PMID 17823927`, o un video-EEG + readout mielinico su `Wwox^gt/gt`."* **Either the paper's own
tissue panel becomes readable, or someone runs a brain Western on the animal.** No third route
exists.

⚠️ **And the lifespan question stays open,** per Operator instruction: Suzuki's Table 2 `Viability`
row (**secondary**, `panel` depth) says *"2 years"*; the primary's own abstract says *"a
**significantly shorter lifespan**."* **Both on file, neither a read of the primary's body, not
reconciled — so the 2-year figure is not propagated.** 🔵 The *argument* that `gt/gt` can test the
survival confound does not need it: the primary itself says *"Wwox hypomorphic mice are **viable in
contrast to the recently reported postnatal lethality** of Wwox knockout mice"*, and the null's
ceiling is three to four **weeks**.

---

## 4 · Two operator directives recorded as named rules

### `D-35` — the gene-replacement evidence class

**Preserve:** experimental rescue **is measured**; durability **is measured within the published
experiments**. 🔴 **Do NOT downgrade measured rescue because replication is absent.**
**Correct only the confidence and independence language:** no independent laboratory replication has
been identified; 2021 and 2026 are the **same research lineage**; the within-study `mWwox`/`hWWOX`
comparison is **not** independent replication; **no published cerebellar functional endpoint** has
been identified.

> **The datum stands. What is withdrawn is the word *"independent."***

This is the correct reading of `CC-20260922-TX007-DOSE-CHALLENGE-01` §2 and supersedes any stronger
reading of it: that candidate strikes *"indipendente"* from `DL-MOL-005`'s evidence line and
re-labels the within-study control — **it does not demote the multi-domain rescue, the durability to
P300, or the absence of hepatic expression, all of which remain measured.**

### `D-36` — the null-mouse temporal boundary

The 2021 authors state their own limitation three times: *"Since KO mice died within less than 4
weeks, we could not perform recordings in adult KO mice"*; *"we could not assess behavior … due to
their poor conditions and premature death"*; *"The limited life span … prompted us to treat these
mice very early on in their life (P0)."*

> 🔴 **Never infer: *"not performed because the animal could not survive long enough"* → *"biologically
> ineffective after that age."***
>
> **Model horizon and therapeutic window are distinct variables.** A ceiling imposed by an animal's
> lifespan is a property of the animal, not of the therapy.

This is the general form of `D-31` (*the set of ages an experiment tested is not the window it
measured*), and it is the rule that makes `P1–P5` readable as what it is.

---

## 5 · Provenance

- Every query above was run in this act; **counts, translations and the positive control are
  reported together**, and the one partially mis-expanded limb (`CNS` → journal names) is **declared
  rather than counted as clean**.
- The `PMC4143238` attempt was made **because** of this session's own corrected rule — `ORDER`
  acquisition attempts with `get_copyright_status`, never `SKIP` on it. It returned an empty body,
  which is now the **eighth** instance this session of *a PMCID is not a body*.
- **Genotype classes kept separate throughout:** `gt/gt` ≠ null ≠ `P47T` ≠ rat `lde/lde` ≠ human
  compound heterozygote.
- **`UNREAD_PREMISE`: measured before landing, not predicted.** No new PMID is introduced —
  `17823927` and `36779245` are both already registered.
