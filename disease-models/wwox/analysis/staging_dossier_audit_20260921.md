# The `staging/` dossiers — nine declared complete readings, and what this tree can check

**Date:** 2026-09-21 · **Actor:** Orchestrator · **Mode:** READ-ONLY. No canonical file written, no
ledger edited, no claim changed, no commit candidate.

> **Scope, declared up front.** This is **not** the broad registry↔ledger reconciliation, which is
> fenced off and stays fenced. It is one bounded, reproducible class: **discovery-ledger entries that
> cite a dossier under `research/staging/`.** Nine records, one `grep`, one directory listing. It was
> not sought — it surfaced twice independently in today's readings, and the second time it was worth
> measuring.

---

## 1 · The measurement

`disease-models/wwox/research/staging/` **does not exist in this tree.**

`discovery_ledger_current.md` cites a dossier under that path **11 times**, across **9 distinct
PMIDs**, each in a `**Fonte:**` line that also declares the source *"letti integralmente"* — read in
full, typically naming figures, supplementary figures and workbooks.

Cross-checking each against the three surfaces that can independently evidence a reading:

| PMID | Receipts | Deep-dive manifest | Registry status | Checkable in this tree? |
|---|---:|---|---|---|
| `35716775` | **5** | ✅ `PMID35716775.json` | `processed` | 🟢 **yes, thoroughly** |
| `37519886` | **1** | ✅ `PMID37519886.json` | `promoted → PAPER 060` (`BATCH_20260810_002`) | 🟢 **yes** |
| `37974179` | **1** | ❌ | `not_processed` | 🟡 **only because a receipt was written TODAY** by this session; it had nothing before |
| `35715422` | 0 | ❌ | *(no registry record)* | 🔴 **no** |
| `35883580` | 0 | ❌ | `not_processed` | 🔴 **no** |
| `36530994` | 0 | ❌ | `not_processed` | 🔴 **no** |
| `37324196` | 0 | ❌ | `not_processed` | 🔴 **no** |
| `37583270` | 0 | ❌ | *(no registry record)* | 🔴 **no** |
| `37781246` | 0 | ❌ | *(no registry record)* | 🔴 **no** |

> ### 🔴 **Six declared complete readings carry no receipt, no manifest and no dossier in this tree.**

---

## 2 · What this does and does not establish

🔴 **It does NOT establish that the readings did not happen.** `reading_state.py`'s own header says
this explicitly, and it is quoted here rather than paraphrased because the distinction is the whole
point:

> *"This page is true of ONE checkout — the one that generated it. It counts the receipts in this
> tree's ledger and nothing else. Work sitting on an unmerged branch is not here … If a paper looks
> unread, check whether the reading is merged before concluding it does not exist."*

`staging/` is exactly the shape of a **working directory that was never committed** — a name that
says "in progress". The public edition also deliberately excludes a private overlay, and its
preamble records that links to private operational logs are rendered as plain text rather than
broken links. **Either explanation is consistent with what is observed here, and this file chooses
neither.**

**What it DOES establish, and this is enough to matter:** for six papers, a reader in this tree
cannot check a declared complete reading against anything. Not a receipt, not a manifest, not a
dossier. **The declaration is the only evidence that the reading occurred**, and LEGEND's whole
receipt discipline exists because a declaration is not evidence.

---

## 3 · Why it matters more for two of the nine

**`DL-MECH-059` (`35715422`) and `DL-MECH-060` (`37583270`) are `promoted-to-CC`** — promoted toward
canonical status. A lead at that status rests on a reading nothing in this tree can verify.

This is the **third** such instance found today, which is what turns it from an oddity into a class:
- **`DL-MECH-053`** — `promoted-to-CC`, cites `staging/deepdive_PMID37974179_Dong2023.md`, absent.
  Recorded in [`human_genotype_and_claim025_wave1b_20260921.md`](human_genotype_and_claim025_wave1b_20260921.md) § 11.
- **`DL-MECH-059`**, **`DL-MECH-060`** — same shape, found during the `FT-116` triage.

⚠️ **And one of those readings has now been independently redone, with a result.** `37974179` was
re-read today from a freshly fetched, fingerprinted artefact; **19 locators re-matched 19/19**, and
every main-text statement of `DL-MECH-053` was **confirmed**. So where the declaration has been
tested, it held. **One test is not six**, and that is the correct weight to give it.

---

## 4 · A second, separate defect found in the same pass — and it is a misreading of a marker

**`37095367` is recorded in the discovery ledger as *"del corrigendum PMID 37095367"*. It is not a
corrigendum.** It is the primary Bayanova *et al.* WGS article (Kazakhstani children, early-onset
epilepsy).

The cause is legible: its `batch_queue.md` row carries the marker **`✎ corrected`**, which means
**"this article HAS a correction"**. It was read as **"this article IS a correction."** `32214227`
and `31618474` carry the same marker and are exposed to the same misreading.

🔴 **The consequence is not cosmetic.** A paper filed as an administrative corrigendum is a paper
nobody will read. This one is a **primary source reporting a novel WWOX variant in a population
LEGEND has zero representation from.**

---

## 5 · The rule this adds, and it is the fourth clause of one earned today

Today established that a paper's state is a **join**, because each surface misled someone:

| Surface | What it cannot tell you |
|---|---|
| `registry_records.py` | `NO RECORD MATCHED` ≠ **not held** — its surface list excludes `analysis/` and the hypotheses ledger, and it reads committed state only |
| Registry `Status` | `not_processed` ≠ **not read** — `PMID 30356099` carried it for six weeks while holding a receipt and a manifest |
| Receipt ledger | "no receipt" ≠ **unprocessed** — `PAPER 003` is an `integrated` BLOCK-1 safety anchor, processed from its abstract |
| 🔴 **Discovery ledger** | **the others are blind to it** — six readings are declared *only* here, and a measure built on registry `Status` (as `FT-116`'s was) cannot see them |

**So `FT-116`'s phrase *"mai guardati"* — never looked at — is FALSE for `35715422` and `37583270`.**
They were never *registered*; the discovery ledger says they were *read*. That correction is recorded
in `FT-116` itself.

**The cheap check is now four commands, not three:**
```
grep -rn "<PMID>" --include=*.md disease-models/
grep    "<PMID>" disease-models/wwox/registries/fulltext_read_receipts.jsonl
ls               disease-models/wwox/research/deepdive_manifests/PMID<PMID>.json
grep -n "<PMID>" disease-models/wwox/research/discovery_ledger_current.md
```

---

## 6 · What is NOT proposed

- **No ledger entry is edited, no status changed, no lead demoted.** A `promoted-to-CC` lead resting
  on an unverifiable reading is a finding for the Operator, not an autonomous demotion — the reading
  may be merged or private, and demoting it would destroy real work on a guess.
- **No re-reading campaign.** Six re-reads is a batch, and it would be a batch run on a suspicion
  rather than on expected information gain. The one re-read that did happen (`37974179`) **confirmed**
  the declaration.
- **The broad registry↔ledger reconciliation stays fenced.** This audit is one grep over one
  citation pattern and it stops here.

## 7 · What IS recommended, ranked

1. **Operator, one question:** does `research/staging/` exist in the private or unmerged edition? A
   yes closes this entirely and costs one answer. **That is the whole remedy, and it is cheap.**
2. If **no**: the six entries need their `**Fonte:**` lines amended from *"letti integralmente"* to a
   declaration of what is actually checkable — a **commit candidate**, not an autonomous edit.
3. `37095367` should be refiled as a **primary source** and triaged; the `✎ corrected` marker's
   meaning should be stated wherever it is rendered, because it has already been misread once.

---

*Non-canonical analysis file. Nothing propagated. Not medical advice.*
