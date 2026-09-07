---
artifact: handoff — CLAIM 011, stale deferral
actor_id: scientist-b
addressed_to: plan, orchestrator
kind: HANDOFF — routing only, no governance decision taken
raised_on: 2026-08-26
---

# HANDOFF — `CLAIM 011`: the rewrite is deferred on a condition that has been discharged

**One record, one reason, no governance resolved here.** This states what I measured and hands it
over. The classification, the batch and the authorization are not mine.

---

| Field | Content |
|---|---|
| **CLAIM_ID** | `CLAIM 011` — *"AAV9-hSynI-hWWOX: dose-dependent durable rescue in Wwox-null murine model su domini multipli inclusi ECoG/SWD, mielinizzazione e gliosi"* |
| **CURRENT_STATUS** | **`flagged for review`** since 2026-08-10 (`CC-20260810-CLAIM011-REVIEW`). `Type: DATO preclinico (full text reviewed)` · `Pathway: P7 — gene therapy readiness; P4 — myelination` · `clinical relevance: HIGH` |
| **FORMER_BLOCKER** | The flag defers its own rewrite, in its own words: *"Riscrittura rinviata: la Figura 3B risolve sopravvivenza e glicemia, **non** gli altri domini della claim (ECoG/SWD, mielinizzazione, gliosi), e la lettura che li risolverebbe è **`partial_fulltext_read`**."* The deferral is therefore conditional on **one fact about read depth**, not on a scientific judgement |
| **EVIDENCE_BLOCKER_DISCHARGED_BY** | **`FTR-20260814-42422765-06`** — `evidence_depth: complete_fulltext_read`, `analysis_at: 2026-08-14T14:20:05`, PMID 42422765. Verified this session directly in `disease-models/wwox/registries/fulltext_read_receipts.jsonl`, and the ledger verifies: `OK: 128 chained receipt(s), tail anchored in framework/state/state_manifest_current.md`. The read produced `deepdive_manifests/PMID42422765.json` with **29 verbatim locators**, several image-anchored, and the commit candidate `CC-20260814-42422765-01` (status: *committed — `BATCH_20260815_001`*). ⇒ **the condition named in the flag has been false since 2026-08-14 — twelve days** |

---

## BLOCKER DISCHARGE — verified field by field, not asserted

| Field | Value | How verified |
|---|---|---|
| **READ_RECEIPT** | `FTR-20260814-42422765-06` · `evidence_depth: complete_fulltext_read` · PMID 42422765 | read directly from `disease-models/wwox/registries/fulltext_read_receipts.jsonl` this session; the ledger's own chain verifies — `OK: 128 chained receipt(s), tail anchored in framework/state/state_manifest_current.md` |
| **DATE** | `analysis_at: 2026-08-14T14:20:05` | same line of the ledger. The flag deferring the rewrite is dated **2026-08-10**. ⚠️ **Recorded as an ordering, not as a duration measured from a commit time**: the receipt's own `analysis_at` field is what dates the reading, and it is four days after the flag and twelve days before this handoff |
| **SURFACE_COMPLETENESS** | article **plus** supplementary S1–S8; **29 verbatim locators**, several image-anchored to fingerprinted rasters (`gr3.jpg`, `gr4.jpg`, `mmc1.pdf` pages rendered at 200–300 ppi) | `deepdive_manifests/PMID42422765.json`, all 29 entries enumerated this session — not sampled. The prior state was **five** `partial_fulltext_read` receipts (`-01` … `-05`, all 2026-08-10), which is exactly what the flag saw |
| **WHAT_WAS_WAITING** | the flag names three domains as unresolved by Figure 3B — **ECoG/SWD, mielinizzazione, gliosi** — and defers the rewrite until a non-partial reading exists | verbatim from the flag: *"la lettura che li risolverebbe è `partial_fulltext_read`"* |

⇒ **The condition the flag named is discharged.** All three domains are resolved below — not all in
the same direction, which is why this is a rewrite and not a status flip.

---

## SCIENTIFICALLY UNRESOLVED vs ADMINISTRATIVELY STALE

The Operator's distinction, applied to each element. **These route differently**: the stale items
need someone to act; the unresolved items need an experiment.

| Element | Which | Why |
|---|---|---|
| The **deferral itself** | 🕐 **administratively stale** | its stated precondition has been false since 2026-08-14. Nothing scientific blocks the rewrite |
| **ECoG/SWD** | 🕐 **stale** — resolved, unwritten | `RESCUE` at HD with the WT-vs-HD bracket drawn and `ns` |
| **Gliosis** | 🕐 **stale** — resolved, unwritten | `RESCUE` at HD (S8I), **`NO_RESCUE` at LD** (S7H) |
| **`comportamento`** | 🕐 **stale** | the word denotes locomotor/motor behaviour only; qualifying it needs no new data |
| **`dose-dependent`** | 🕐 **stale** | the flag itself established the threshold reading; carrying it into the other domains needs no new data |
| **Myelination (dose study)** | 🔬 **scientifically unresolved** | three representative panels, no statistics, and the only MBP quantification has **no treated arm**. **No amount of re-reading fixes this** — the measurement was not made |
| **Spikes/day** | 🔬 **scientifically unresolved** | `p = 0.2000` on the panel face against *"a significant elevation"* in the text. Resolving it requires the underlying data or a repeat |
| **Survival threshold ↔ expression** | 🔬 **scientifically unresolved** | 7/8 dose comparisons `ns`; the explanation is survivor-conditioned. Needs the **intermediate-dose arm with an expression readout** |
| **Motor** | 🔬 **scientifically unresolved** | Figure 4 draws the WT-vs-treated comparison in all eight panels and **three are significant in the exceed direction**, unadjusted across eight comparisons. Hyperactivity, overexpression overshoot and marginal statistics are all live readings |
| **Cognition · development · post-neonatal** | 🔬 **scientifically unresolved** — and **not measured** | no assay exists. This is the `PROMISING_BUT_GAP` half of the split |

**No canonical status is modified by this handoff.** `CLAIM 011` remains `flagged for review` until
Plan integrates and the Orchestrator batches.

---

## WHAT_REMAINS

The complete read resolves the three domains the flag said were unresolved. It does not resolve them
all in the same direction, which is why this is a rewrite and not a status flip.

| Domain the flag named | Resolved by the complete read as |
|---|---|
| **ECoG / SWD** | **Rescued at HD, tested against wild type.** Fig. 7E: `****` WT-vs-KO, `****` KO-vs-HD, **`ns` WT-vs-HD**. ⚠️ The *second* epilepsy endpoint in the same figure — average spikes/day, 7C — prints **`p = 0.2000`** on the panel face for WT-vs-KO, with no asterisk and no `ns`, at n = 5/group, while the running text calls it *"a significant elevation"* |
| **Myelination** | 🔴 **Unresolved in this study.** Fig. 6F, S7I and S8G are representative images with no graph and no statistics; the only MBP quantification (6E) has **no treated arm**. The text nonetheless claims *"near-complete rescue across affected regions"* and cites S7I as if it carried the quantification |
| **Gliosis** | **Rescued at HD, tested against wild type** — S8I: GFAP⁺ WT ~5 / KO ~44 / treated ~5, `***` WT-vs-KO and **`ns` WT-vs-treated**. 🔴 **Not at LD**: S7H shows LD **significantly worse than wild type** (`**`) while HD is `ns` |

**And four things the complete read adds that the flag could not have anticipated:**

1. 🔴 **The survival threshold has no measured expression correlate.** Two doses differing 2.1-fold
   are statistically indistinguishable in vector genomes and mRNA across four brain regions —
   **7 of 8 comparisons `ns`**, the exception being hippocampal DNA — while producing opposite
   survival outcomes. The paper's own explanation is a **post-hoc survivor-versus-non-survivor**
   comparison; S5A–D label one HD and three LD animals *"Dead"*, so the later dose comparison is
   necessarily made among survivors. *(This does not overturn the flag's threshold finding — four
   doses across two figures confirm the threshold is real and not an artefact of comparing two.)*
2. 🔴 **`comportamento` in the Summary denotes locomotor and motor behaviour only.** Across the
   **49 verbatim locators** of this paper and its 2021 companion there is **no cognitive assay** —
   no maze, no novel object, no fear conditioning, no operant task. In an undifferentiated domain
   list beside `crisi` and `mielinizzazione`, the unqualified word invites the reading that
   [[claim_registry_current#CLAIM 031]] explicitly denies.
3. **The word `dose-dependent` needs the flag's own correction carried into the other domains.** The
   flag establishes that Fig. 3B shows a **threshold**, not a continuum, for survival and glycaemia.
   The complete read shows the same shape elsewhere — **LD fails where HD succeeds** on gliosis
   (S7H), and LD animals do not reach P90 at all, so every P90 behavioural datum is HD-only and
   survivor-selected.
4. **Two text-versus-panel discrepancies, both in the direction favourable to the therapy** — the
   locomotor panels (4D/4E carry `*p<0.05` against WT while the text states *"no significant
   differences between groups"*) and the spike count (7C). Recorded as quality signal, weighted
   proportionately: blinding is declared here as *"in a blinded manner **when feasible**"* against
   the 2021 paper's unconditional statement, and a commercial interest is declared here and absent
   there. **This is context for the two discrepancies, not an argument against the data.**

---

## WHY_IT_MATTERS_TO_TOP_CANDIDATE

`CLAIM 011` is one of the two canonical records carrying **`R-01` / `TX-007`** — AAV9-hSynI-WWOX,
the **only** entry in `READY_FOR_WWOX_PRECLINICAL_CONSIDERATION` and the tracker's declared
*north star*. Three consequences follow from leaving it as it stands:

- **The readiness class is asserted at intervention level.** `R-01` still ranks first and nothing is
  close — but *"ready for preclinical consideration"* attached to an intervention rather than to an
  **(endpoint × dose × window)** triple asserts a readiness that the developmental column does not
  support. Nothing in the entire portfolio has been measured on developmental trajectory or
  cognition (measured: 207 files, 0 records).
- **`myelinazione` sits in the claim as a rescued domain** while the study that the claim is about
  does not quantify it in any treated arm — and the companion study, which does quantify it, is
  `PARTIAL` and **significant against the rescue** on the single panel where treated is compared
  with wild type.
- **A `flagged for review` record is a record other actors route around.** It has been in that state
  for sixteen days, twelve of them with its stated blocker already discharged, while remaining
  `clinical relevance: HIGH` in the gene-therapy pathway.

---

## CANONICAL_DEPENDENCIES

| Record | Relation to `CLAIM 011` | Note |
|---|---|---|
| [[claim_registry_current#CLAIM 004]] | **Same intervention, different study.** `consolidated baseline` | ✅ **Already carries its 2026-08-10 repair** — *"dove il rescue è confrontato con il WT il confronto o non è tracciato, o è significativo contro il rescue"*. **No change proposed for that cell.** It does carry the same unqualified `comportamento`, and its DRG safety statement is transferred-as-direct |
| [[claim_registry_current#CLAIM 031]] | **The corrective.** *"seizure control does not rescue development"*, `T1`, human, direct | ⚠️ It is `in observation` while `CLAIM 004` is `consolidated baseline` — the record that denies the global reading sits **below** the record that invites it |
| [[claim_registry_current#CLAIM 002]] | Organoid rescue, `consolidated baseline` | *"WWOX re-expression improves the phenotype"* — bounded later to *"domini **cellulari**"*, after the headline |
| `therapeutic_strategies_current.md#TX-007` | Tracker entry for the same intervention | Carries *"seizure/**myelin**/survival rescue"* and no line for supraphysiological expression (8.2× / 10.7× / 5.6× / 1.4× WT) |
| `disease-models/wwox/analysis/mechanism_intervention_map.md` `R-01` | Analysis layer | Sole entry in `READY_FOR_WWOX_PRECLINICAL_CONSIDERATION` |
| `working_model_current.md` | `P7 — gene therapy readiness` | Whether the endpoint split is a **block-adjacent** change is exactly the question I am not deciding |

---

## What I am handing over, and what I am not

**Handing over:** the measurement that `CLAIM 011`'s deferral condition is discharged, the
endpoint-level resolution of the three domains it named, and four findings the flag could not have
anticipated. The full matrix with comparators and statistical status is
[`therapeutic_canonical_repair_package.md`](../../disease-models/wwox/analysis/therapeutic_canonical_repair_package.md) §4,
and the candidate is **F** in §1 of the same file.

**Not deciding, and not mine to decide:**

- whether the endpoint split is **MINOR** or **MAJOR** — I classify it fail-closed as **MAJOR**
  because it narrows a readiness class in `P7`, and a doubtful MAJOR is Mirror's call under
  Annex H.1, not a scientist's;
- whether `CLAIM 011` leaves `flagged for review` before or after the rewrite;
- which batch carries it, and whether `CLAIM 004`'s `comportamento` cell travels with it or
  separately;
- any edit to any of the four scientific current files. **None was made.**

**Nothing here is medical advice.**
