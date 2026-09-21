# The space between LEGEND's harvest and LEGEND's registry

**Date:** 2026-09-21 · **Actor:** Orchestrator · **Status:** non-canonical analysis file.
**No canonical file edited. No reading claimed beyond abstract depth. Not medical advice.**

> **How this was found.** Scientist A's resilience census reported `PMID 30949922` as *"absent from
> LEGEND entirely"*. Under the operator's §10 rule I checked — and found it **present in the corpus
> harvest and absent from every registry**. That is a third state the repository had no name for,
> and it turns out to be populous.

---

## 0 · 🔴 A correction against myself, first, because it is the method lesson

My first measurement used `registry_records.py index --json` and its `identities` map, and reported
**317 harvested records with no registry record**. **That number was wrong and I nearly published
it.** Two spot-checks broke it: `PMID 35573960` is `PAPER 018` and `PMID 42092735` is `PAPER 013`,
and both appeared in my "unplaced" list. The derived identity index does not resolve every record
the `get` action resolves.

**The corrected measurement, with its method stated so it can be attacked:**

| | |
|---|---|
| Harvest (`corpus_seed_pubmed_20260806.jsonl`) | **706** records |
| Flagged unplaced by the identity index | 317 |
| **Random sample re-checked with `registry_records.py get`** (seed `20260921`, n = 25) | **24 genuinely absent · 1 false positive** |
| Index false-positive rate on this set | **4 %** |
| **Projected genuinely absent** | **≈ 304 of 706** |

⚠️ **`n = 25` gives a wide interval and the figure is an estimate, not a count.** What is *not* an
estimate is that the gap is large and that **six named records below were each verified
individually.** The lesson is the day's lesson arriving a fourth time: **a derived index is a
measurement of another file, and I checked it against the thing it measures only after it told me
what I wanted to hear.**

---

## 1 · What the gap is, precisely

Three instruments, and **none of them looks at the space between the other two**:

| Instrument | What it sees | What it cannot see |
|---|---|---|
| The **harvest** (`corpus_seed_*.jsonl`) | 706 PubMed records from a keyword sweep | whether anything was ever done with them |
| The **registries** (`CORPUS` / `PAPER` / `LIT`) | 361 corpus + 87 paper records | anything never placed into them |
| `unread_gold.py` | unread **`CORPUS` placeholders** | 🔴 **a harvested paper that never became a placeholder** |

⇒ **A paper can be harvested, be plainly WWOX-relevant, and be invisible to every check the
repository owns** — not because anyone judged it, but because nothing ever adjudicated it at all.
This is a **fourth** instance of the day's pattern: every LEGEND check verifies a *record*, and a
paper with no record is unverifiable by construction.

## 2 · The six neuro-relevant records checked individually

A keyword screen over the unplaced set returned **31** neuro-relevant titles. Six were checked
one by one with `registry_records.py get --pmid` and `fulltext_receipts.py status --pmid`:

| PMID | Title (short) | Verdict |
|---|---|---|
| `25716914` | WWOX and severe AR epileptic encephalopathy: first case **in the prenatal period** | ✅ **HAS a record.** False alarm — and the one I most wanted to be a gap |
| `32051108` | A Chinese patient with epilepsy and WWOX compound heterozygous mutations | ✅ **HAS records.** False alarm |
| **`28721938`** | **Practical clues for diagnosing WWOX encephalopathy** | 🔴 **genuinely absent** |
| **`30783266`** | **Correction:** The phenotypic spectrum of WWOX-related disorders — 20 additional WOREE cases | 🔴 **genuinely absent** |
| **`31315632`** | p53/TIAF1/WWOX triad … brain protein aggregation | 🔴 **genuinely absent** |
| **`30949922`** | Two siblings, compound-het WWOX, ASD + severe speech sound disorder | 🔴 **genuinely absent** (`FT-119`) |

**Two of six were false alarms.** `25716914` — a **prenatal** WOREE case, the single most relevant
title to the developmental-timing node completed hours earlier — **is already held.** Had I
reported the list without checking each one, the session's most eye-catching "discovery" would have
been a paper the repository already had.

## 3 · What the two settled records actually say

### 3a · `PMID 30783266` — the correction is administrative, and it also solves a different puzzle

Piard J, … Kini U, Philippe C. *Genet Med* 2019;**21**(7):1667–1671. `article_types: Published
Erratum`. DOI [10.1038/s41436-019-0460-y](https://doi.org/10.1038/s41436-019-0460-y).

Verbatim, the whole of it:

> *"The article has been corrected to account for one patient being investigated through **genome
> sequencing rather than exome sequencing** as originally published; thus amendments to the
> Abstract and Methods have been made as well as addition of the relevant authors and
> acknowledgment."*

✅ **No case count, no genotype, no phenotype, no outcome changes.** The WOREE spectrum cohort
LEGEND reasons about is **unaffected**. Recorded explicitly so that the word *"Correction"* on a
load-bearing cohort paper is never re-opened in alarm by a later reader.

> 🔴 **And it explains `CC-20260921-PAPER025-IDENTITY-01`.** That candidate records `PAPER 025` as
> carrying `PMID 30853297` under the byline *"Piard et al."* with a title ending *"…dysmorphic
> features"*, when the record is **Weisz-Hubshman M … Heimer G**. **Piard J is first author of
> *this* paper** — the WOREE phenotypic-spectrum cohort. So `PAPER 025` is not a random slip: it is
> **two different 2019 WWOX papers conflated into one record**, the identifier taken from one and
> the byline from the other. That is a sharper diagnosis than "wrong author", and it means the
> **Piard cohort may have no record of its own** while its byline sits on someone else's paper.
> ⇒ appended to that candidate rather than opened as a new one.

### 3b · `PMID 28721938` — a diagnostic-criteria datum, corroborating not contradicting

Tarta-Arsene O, Barca D, Craiu D, Iliescu C. *Epileptic Disord* 2017;**19**(3):357–361.
DOI [10.1684/epd.2017.0924](https://doi.org/10.1684/epd.2017.0924). Verbatim from the abstract:

> *"…with persistent epileptic spasms and hypsarhythmia as a part of the electroclinical phenotype,
> **demonstrating that microcephaly is not mandatory for diagnosis**, even when associated with
> progressive cerebral atrophy."*

*(The source prints "hypsarhythmia" with one `r`; reproduced as printed.)*

**Consistent with what LEGEND already holds** — `DL-MECH-022` records a biallelic-null case with
*"nessuna microcefalia (OFC +0.37 SD)"*. This is corroboration from an independent group, not a new
finding, and it is a **diagnostic** datum rather than a mechanistic one. ⚠️ `n = 1` case report.
⚠️ Note the same clinician (**Tarta-Arsene O**) is a co-author on the Piard cohort above — **these
two records are not fully independent sources**, and anyone counting them as two should not.

## 4 · What is proposed, and what is refused

**Proposed — small, and deliberately not a programme:**
1. `28721938`, `30783266`, `31315632` → `CORPUS` placeholders, so that `unread_gold.py` can see
   them at all. `30949922` already has `FT-119`.
2. Append §3a's two-paper-conflation diagnosis to `CC-20260921-PAPER025-IDENTITY-01`, and check
   whether the **Piard cohort itself** has a record.
3. Record the harvest-to-registry gap as a **known, measured, unresolved debt** — with its size
   stated as an estimate and its method stated.

**Refused:**
- ❌ **No bulk placement of ~304 records.** A placeholder asserts that something was triaged. Creating
  three hundred of them in one sweep would manufacture exactly the false coverage this file is
  about, and `unread_gold.py` would then report three hundred items of "gold" nobody has judged.
- ❌ **No new gate, auditor or registry** (§26). The finding is that three instruments have a gap
  between them; a fourth instrument would have gaps with all three.
- ❌ **No claim that the ~304 are valuable.** The harvest is a keyword sweep — `pubmed_corpus_harvest`
  produces a **census, not evidence**. Most of that residue is oncology and GWAS. **Four verified
  neuro-relevant absences out of six checked is the measured yield, and it is worth exactly what it
  is.**

## 5 · The operational rule, which costs nothing

> 🔵 **"Not in LEGEND" has three states, not two:** *never harvested* · **harvested but never
> registered** · *registered*. Only the third is visible to the repository's checks. When a census
> says a paper is absent, check `registry_records.py get --pmid` **and** the corpus seed — they
> answer different questions, and the middle state is where this session found four real papers.

---

*Sources retrieved from **PubMed / PubMed Central**.
DOIs — [30783266](https://doi.org/10.1038/s41436-019-0460-y) ·
[28721938](https://doi.org/10.1684/epd.2017.0924) ·
[30949922](https://doi.org/10.1007/s10519-019-09957-8).
No reading occurred beyond abstract depth and no receipt is claimed. Not medical advice.*

---

# Addendum — the same gap one layer in: 29 papers that were READ and never given a `PAPER` record

**Added 2026-09-21, same session.** Found by asking whether `CORPUS-STUB-059`'s state was unique.
It is not.

## 🔴 A second correction against myself, made before publishing the number

My first cut counted **81** "CORPUS records carrying a read receipt but never promoted", and that
was **wrong for a reason worth recording**: LEGEND's own convention **preserves the placeholder
append-only after promotion** (*"Promoted from `CORPUS-STUB-073`, placeholder preserved
append-only"*). So most of the 81 are **preserved placeholders of papers that DO have a `PAPER`
record** — the convention working exactly as designed, misread by me as a defect.

**This is the fifth time in one session that a first measurement was wrong and the check caught
it.** The pattern in all five is identical: I measured a *proxy* (an identity index, a dict's
`len`, a record-id prefix) instead of the thing itself, and the proxy agreed with what I expected.

## The corrected measurement

Re-derived by asking the only question that matters — **does a `PAPER` record exist for this
PMID?** — rather than what the corpus record is called:

| | |
|---|---|
| PMIDs with a `PAPER` record | **81** |
| **PMIDs with a read receipt, a corpus record, and NO `PAPER` record** | 🔴 **29** |

⇒ **the registry's `PAPER` layer understates the model's integrated reading by roughly a quarter.**
These are not unread papers and not unknown papers. They are **read, receipted, and cited**, sitting
in a layer that carries no byline, no role, no transferability, no clinical-relevance field and no
claim links.

## The ones that matter, and one that closes an earlier loop

| PMID | Record | What it is |
|---|---|---|
| 🔴 **36828035** | `CORPUS-STUB-053` | **P47T knock-in mouse — the SCAR12 model.** See below |
| **30356099** | `CORPUS-STUB-059` | Piard — 20 additional WOREE cases, the cohort whose byline landed on `PAPER 025` |
| **25649963** | `CORPUS P318` | zebrafish `wwox` — the domain-sufficiency read |
| **27869163** | `CORPUS-STUB-046` | Wwox–Brca1 |
| **24008736** | `CORPUS-STUB-139` | the autophagy-sign read that falsified a standing negative |
| **41677633** | `CORPUS-STUB-147` | the lysosomal-degradation panel named as the cheapest missing experiment |
| **41124647** · **42082822** | `CORPUS P348` · `CORPUS P191` | recent reads |

> 🔵 **`PAPER 007` is explained.** The earlier audit
> ([`anchor_papers_without_readings_20260921.md`](anchor_papers_without_readings_20260921.md))
> found `PAPER 007` — *"genotype caution anchor"*, the record carrying **"P47T ≠ Q230P"** — with
> `Journal/source: pending normalization` and `Identifier: pending normalization`, and inferred it
> was *"almost certainly"* `PMID 36828035`. **It is now clear why it could not be normalised: the
> paper has no `PAPER` record of its own.** `PAPER 007` is a **role without a paper**, and
> `36828035` is a **paper without a record**. The two have been sitting a few hundred lines apart,
> each unresolvable alone.

**The same shape as `PAPER 025`, twice over.** A read paper left without an identity is a byline
that can be borrowed, a role that cannot be normalised, and a citation that cannot be checked.

## What is proposed, and what is refused

**Proposed:** promote the **29** to `PAPER` records, authors extracted, at `BATCH_COMMIT`.
Mechanical: every one already has a receipt, a manifest and a corpus record — the information
exists and is merely not assembled. **`36828035` and `30356099` first**, because each resolves a
defect already recorded in a commit candidate.

**Refused:**
- ❌ **No new gate.** The existing `coverage_report.py` / registry-declaration ratchet already
  measure depth; none of them asks *"is this read paper a `PAPER`?"*, and the answer is a
  **one-time repair**, not a standing check. If it recurs, that is the evidence a check would need.
- ❌ **No claim that these readings were inadequate.** Every one has a receipt. **The reading is
  not the problem; the filing is.**
- ❌ **No bulk promotion of anything unread.** This is 29 specific PMIDs, each with a receipt.

## What all five instances of today's pattern have in common

`CLAIM 032`'s unsourced hypomorph · `CORPUS P306`'s tier · the seven anchor papers · the sixteen
locator counts · these 29. 🔵 **Every LEGEND check verifies a record against itself. Nothing
verifies that a thing which exists HAS a record.** The ratchets measure honesty within a record and
are structurally blind to the space outside one — which is why all five were found by reading, by
hand, while chasing something else.

*No canonical file edited. No reading claimed. Not medical advice.*
