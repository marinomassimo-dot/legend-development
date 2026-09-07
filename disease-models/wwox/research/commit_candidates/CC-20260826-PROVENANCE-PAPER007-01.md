# COMMIT CANDIDATE — PROVENANCE ITEM A: `PAPER 007`, review-ready

**Candidate ID:** CC-20260826-PROVENANCE-PAPER007-01
**Date:** 2026-08-26
**Status:** queued; **no canonical file modified**
**Mode:** provenance repair, high severity
**Extends:** §A of [`CC-20260826-PROVENANCE-01`](CC-20260826-PROVENANCE-01.md), which named the
defect. This candidate makes it **review-ready** and separates three failures that the earlier
candidate carried as one.
**Change class:** MIXED — see the three-way split in §3. **One is 🔴 MAJOR.**
**Canonical targets:** `PAPER 007` · `CORPUS-STUB-053` · `CLAIM 006` · `CLAIM 007`
**Locator audit trigger:** ✅ required for §3.C only — `L-007-c` and the Fig 3b/4b entries in
[`CC-20260826-LOCATOR-PACKET-01`](CC-20260826-LOCATOR-PACKET-01.md)
**Batch gate:** intentionally untouched

---

## 1. The record as it stands

```
## PAPER 007
**Full title:** P47T model shows progressive neuroinflammation and altered PPxY binding
**Journal/source:** pending normalization
**Identifier:** pending normalization
**Status:** integrated
**Claim links:** 006, 007
```

🔴 **A record with `Status: integrated`, no identifier, no journal, and a `Full title` that is
not the title of any paper — carrying two `consolidated baseline` claims.**

Its twin:

```
## CORPUS-STUB-053
**Full title:** WWOX P47T partial loss-of-function mutation induces epilepsy, progressive
                neuroinflammation, and cerebellar degeneration in mice
**Identifier:** PMID 36828035 / DOI 10.1016/j.pneurobio.2023.102425
**Status:** not_processed
**Claim links:** none
```

The identifier and the claims are in **different records**, and neither record is complete.

---

## 2. The schema the operator asked for

| Field | Value |
|---|---|
| **TRUE_SOURCE_CANDIDATE** | Hussain T., Sheikh K., Chen J., Sarkar D., Jones C., Liu Y., Aldaz M., … Aldaz C.M. — *WWOX P47T partial loss-of-function mutation induces epilepsy, progressive neuroinflammation, and cerebellar degeneration in mice **phenocopying human SCAR12*** |
| **IDENTIFIER** | **PMID 36828035** · **PMCID PMC10835625** · **DOI 10.1016/j.pneurobio.2023.102425** · *Progress in Neurobiology* **223**:102425 (2023) · NIH manuscript **NIHMS1957654** |
| **VERSION_RELATION** | Publisher version is Elsevier (paywalled). The retrieved surface is the **NIH author-manuscript deposit in PMC**, CC BY-NC-ND 4.0, carrying `<restricted-by>pmc</restricted-by>`. ⚠️ **Author manuscript ≠ version of record**: pagination, copy-editing and possibly figure rendering differ. No claim below depends on pagination. |
| **READ_STATUS** | **`partial_fulltext_read`**, twice receipted: `FTR-20260826-36828035-01` (body text, figure legends) and `FTR-20260826-36828035-02` (figures 1, 3, 4, 5 at native resolution). **Supplementary `SOURCE_ACCESS_BLOCKED`**; figures 2, 6–9 not inspected; in-body tables not inspected. |
| **LOCATORS** | `deepdive_manifests/PMID36828035.json`, schema v2, **26 entries** — 17 text/legend, 9 figure-pixel — `MANIFEST STRICT PASS` against the shared checkout |
| **CLAIMS_DEPENDENT** | `CLAIM 006` (`consolidated baseline`) · `CLAIM 007` (`consolidated baseline`). **No other claim cites `PAPER 007`.** |
| **WHAT_BREAKS_IF_SOURCE_IDENTITY_IS_WRONG** | See §4 — and the honest answer is **less than the severity of the record suggests**. |

---

## 3. The three failures, classified separately

The operator's instruction is the load-bearing one here: **do not suspend a baseline for an
identity problem that can be normalised without touching the science.** These are three different
things and only one of them touches a scientific conclusion.

### A. `IDENTITY_REPAIR` — mechanical, no scientific content changes

- `Full title` is an **invented descriptive string**. Replace with the verbatim title from the XML.
- `Journal/source` and `Identifier` are `pending normalization`. Fill from §2.
- `CORPUS-STUB-053` is the same paper; mark `promoted — see PAPER 007`, preserved append-only.
- ⚠️ `CORPUS-STUB-053`'s own title is **truncated**: it drops *"phenocopying human SCAR12"*, which
  is the clause that states the model's disease mapping. Use the full string, not the stub's.

**No claim changes. No status changes. `CLAIM 006` and `CLAIM 007` are not suspended by this.**
🔴 **This is the third invented `Full title` found in this registry** (cf. PMID 31340538/Tochigi,
whose fabricated *lissencephaly* title steered it toward a migration reading). An invented title
does not merely mislabel — **it steers the reading**, and §3.C below is that happening again.

### B. `READ_STATUS_REPAIR` — the record claimed more than the ledger held

`Status: integrated` was carried with **no receipt of any kind** until 2026-08-26. It is now
supported at `partial_fulltext_read` depth, twice. Repair: keep `integrated`, and **state the
depth and the blocked surfaces on the record**, so the next reader does not have to rediscover
that the supplementary was never obtained.

⚠️ `Transferability: T3 with genotype caution` and `clinical relevance: LOW` were set before the
paper was read. On a full reading this is **the reference SCAR12 model and the corpus's best
electro-behavioural seizure dataset**. `clinical relevance: LOW` is no longer defensible —
proposed **MODERATE**, and flagged rather than changed unilaterally.

### C. 🔴 `CLAIM_SUPPORT_FAILURE` — and this one is real

**`CLAIM 006`** · `consolidated baseline` · Title *"P47T model shows progressive
neuroinflammation"* · Summary *"P47T murine model shows **progressive microgliosis** and
astrogliosis."*

**The source's own Figure 3b falsifies the microgliosis half.**

| Measure | 80 d | 250 d | Within-genotype age bracket | Verdict |
|---|---|---|---|---|
| Iba1⁺ **cell number** (Fig 3b) | WT ≈22, mut ≈34 `*` | WT ≈22, mut ≈**34** `*` | **none drawn** | 🔴 **flat — not progressive** |
| Iba1⁺ **area fraction** (Fig 3c) | WT ≈14.5, mut ≈21 `*` | WT ≈**11**, mut ≈20.5 `*` | **none drawn** | 🔴 flat in the mutant; the gap widens because **WT declines** |
| Microglial branches / junctions / length (Fig 3e–g) | — | — | **`*` in all three** | ✅ progressive (**morphology only**) |
| Gfap⁺ number (Fig 4b) | mut ≈39 | mut ≈**56** | **`*`** | ✅ progressive |
| Gfap⁺ area fraction (Fig 4c) | mut ≈24 | mut ≈**40** | **`*`** | ✅ progressive |

⇒ **`CLAIM 006` is half true.** Astrogliosis is progressive; microgliosis is elevated from 80 days
and progresses **only in ramification loss**, not in number or area.

🔴 **Note the causal chain, because it is the point of §3.A.** The invented `Full title` —
*"P47T model shows progressive neuroinflammation"* — **is `CLAIM 006`'s title, verbatim.** The
claim and the paper record were written from each other, not from the paper. An unverifiable
title became a canonical claim, and the claim then licensed the title.

**MINIMUM_REPAIR (`CLAIM 006`):** Summary →
*"P47T murine model shows progressive astrogliosis (Gfap⁺ number and area fraction both rise
significantly between 80 and 250 days) and microgliosis that is elevated from 80 days with
progressive loss of ramification but static cell number and area fraction."*
Title → *"P47T model shows progressive astrogliosis and early, morphologically progressive
microgliosis"*.
**CHANGE_CLASS: 🔴 MAJOR** — a `consolidated baseline` summary is falsified in half by its own
source's figure.

**`CLAIM 007`** · *"P47T abolishes PPxY binding to WW-domain partners"* · Summary *"P47T alters
WWOX WW-domain binding behavior."*
✅ **SUPPORTED**, verified at pixels (`L-007-c`): Dvl2 and Wbp1 pull-downs near-absent in
`P47T/P47T`, `10% input` comparable in both genotypes, Hsp90 and biotin bead inputs comparable.
⚠️ Two internal wrinkles, both MINOR: the Title says *"abolishes"* while the Summary says
*"alters"* — the panel supports **"abrogates/near-abolishes"** for these two ligands; and
**n = 2 lanes per genotype**. Propose aligning Title and Summary on *"abrogates binding to the
tested PPxY ligands (Dvl2, Wbp1)"* and recording the `n`.
**CHANGE_CLASS: MINOR**

---

## 4. `WHAT_BREAKS_IF_SOURCE_IDENTITY_IS_WRONG` — answered honestly

**Almost nothing, and saying so is the point.** The identity is now fixed by four independent
handles that agree: PMID, PMCID, DOI and the NIHMS number, all present in the retrieved XML's
`article-meta`, with the title matching `CORPUS-STUB-053`'s and the P47T subject matter matching
`PAPER 007`'s `Genotype/model: P47T` and both claim topics.

If the identity were nevertheless wrong:
- `CLAIM 007` would lose its only source and revert to unsupported.
- `CLAIM 006` would lose its only source — but it **already needs repair on content grounds**
  (§3.C), so identity is not the binding constraint there.
- **`CLAIM 037`'s Title repair does NOT depend on this paper.** It is falsified by Cheng 2020,
  Repudi 2021 and Obeid 2026 independently; `PAPER 007` widens the statement, it does not carry it.
  🔴 **Stated explicitly so that a failure here cannot be read as undermining the five-claim
  package.**

⇒ **The identity repair is safe to apply on its own**, exactly as the operator's instruction
anticipates. **Do not suspend `CLAIM 006`/`CLAIM 007` for §3.A.** `CLAIM 006` needs action for
§3.C, and that is a different ticket.

---

## 5. Review required

- **§3.A `IDENTITY_REPAIR`** — no operator authorization; mechanical, content-neutral.
- **§3.B `READ_STATUS_REPAIR`** — no authorization; the `clinical relevance` upgrade is **flagged,
  not applied**.
- **§3.C `CLAIM_SUPPORT_FAILURE`** — 🔴 **operator authorization required**, and a **locator audit**
  on the Fig 3b/3c/4b/4c entries before the `CLAIM 006` summary is rewritten. The finding rests
  entirely on the presence and absence of within-genotype significance brackets, which is exactly
  the kind of read a second pair of eyes should confirm.
