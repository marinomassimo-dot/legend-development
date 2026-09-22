# Session self-evaluation — Orchestrator, fourth autonomous run (2026-09-22)

**Scope:** from `f226955` to this commit. Four Scientist waves (N, O lost/returned; P, Q; R, S
running). Four landings. **The upgrade is the answer, not the promise of one** — this run ships
`framework/scripts/census_verify.py`, caused directly by the defect in §2.1.

---

## 1 · What the run actually established

| | |
|---|---|
| 🟢 **A therapeutic axis reopened** | Non-allele-specific WWOX upregulation was closed by an **unsourced, untagged** premise that collapsed a hedged disjunction. Withdrawn. The axis is live for the first time since 2026-07-09 |
| 🟢 **The empirical floor is `NEVER TESTED`** | No WWOX allele, any class, any species, has ever met an NMD reagent. Every count re-measured against the committed tree |
| 🟢 **A fifth way a query-zero lies** | A **reagent named only in Methods is invisible to `[All Fields]`** even with a flawless expansion. Miss rate in this gene: **100%** |
| 🟢 **The deletion is a packing lesion, not an active-site lesion** | >20 Å from the SDR tetrad; backbone admits local accommodation; six polar contacts lost |
| 🟢 **A valid discriminator for short in-frame deletions** | Span feasibility + register exposure + lost-contact inventory. ΔΔG and deleted-residue relSASA are **invalid**. Closes the gap `D-30`'s corollary opened |
| 🟡 **The unit ambiguity is bounded, not fatal** | `u` cancels; the ratio is degenerate; the defect is confined to the absolute axis at exactly 2× |

## 2 · ATTRIBUTION_CENSUS

```
ATTRIBUTION_CENSUS
incidents: 8
machine: 1   blind_auditor: 0   peer: 1   self: 6
severity_high: 2   of which self: 2
undetected_known: 2
```

**Counting, so the numbers can be argued with.**

`machine: 1` — the publication gate refusing `nascimento_supplement_retrieval:337` on a broken
markdown link.

`peer: 1` — Scientist O's arithmetic establishing that `u` cancels from the dose ratio, against my
own written framing that the ambiguity *was* the effect.

`self: 6` —
1. 🔴 **§2.1 below** — verifying a census on a contaminated tree, twice.
2. 🔴 **The metric ambiguity** — reporting "every count is exact" without saying that `78` and `22`
   are **line** counts; as occurrence counts they are `91` and `27`.
3. The *"unit ambiguity is the size of the effect"* category error (`D-33`, withdrawn).
4. The journal-name sweep that reported itself complete after grepping **abbreviations only**,
   leaving every long-form spelling alive — **in the three highest-authority files**. Third wrong
   count on one defect.
5. Sketching a register-shift catastrophe for `p.Gln353_Gln354del` before measuring the span test
   that refutes it. Caught by my own next command, but I had already written the wrong mechanism.
6. `claim_registry`'s `Last update` line, unbumped since 2026-07-25 across three batches **including
   my own seizure propagation this morning** — found only because this batch touched the same line.

`severity_high: 2`, both self — (1) and (2). Either could have caused a correct delegate census to
be discarded, or an incorrect one to be landed.

`undetected_known: 2` — the metric ambiguity was invisible until the new tool printed both columns;
the `Last update` convention defect is **recorded and deliberately unrepaired** (§4).

### 2.1 The defect that earned the tool

A delegate census asserted eleven reagent terms absent from the repository. I verified by grepping
the working tree — **which by then held the delegate's own 474-line census, naming all eleven.** The
re-count came back non-zero and the census looked wrong. **It was not wrong.** I then reached for
`grep --exclude`, which **this deployment's grep silently ignores**, and reproduced the same false
mismatch. Only counting at the committed tree resolved it: **11/11 exact.**

Two failure modes, one root cause — **the surface I verified on was not the surface the claim was
made about.** The same shape as the base64 false-positive trap found earlier this session: the
search surface silently included something that was not evidence.

🔴 **And the near-miss is the real lesson.** My standing rule is *never trust a delegate census
without a repository check*. That rule, executed literally, was about to convict a correct delegate.
**The check needs a defined surface, or it is worse than no check** — it converts a good delegate
into a discarded one with the full confidence of having verified.

## 3 · The upgrade shipped

`framework/scripts/census_verify.py` — measures claimed counts **at a git ref**, prints the
working-tree count beside it, and **names the files responsible** for any difference.

- **12 tests** (`test_census_verify.py`), including `test_the_real_2026_09_22_contamination_is_caught`
  reproducing the incident verbatim, each contamination case **paired with the clean case it must
  not flag**, and the `ASE` substring trap (8,842 → 0 under `-w`).
- **Mutation-tested three ways:** contamination detection disabled → **2 failures**; `lines` metric
  made identical to `occurrences` → **1**; `parse_claim` splitting on the first `=` → **1**.
- Routed in `framework/scripts/README.md` § 4; `scripts/test_tool_routing.py` **7/7 OK**.
- 🟢 **It found a second defect the moment it ran on the real case** — that "count" is ambiguous
  between lines and occurrences, and that my verification had silently compared the wrong quantity.
  That is `self: 2` above, and it is the argument for building the instrument rather than writing
  the lesson down.

**§26 compliance:** this is a **measurement instrument**, not a gate, authority, auditor, registry or
workflow. It authorises nothing and blocks nothing; a non-zero exit is a finding for a human to read.

## 4 · What I deliberately did NOT do

- **No broad repair campaign.** `claim_registry`'s stale `Last update` convention spans at least
  three batches and every registry. **Recorded in the batch note, not fixed** — repairing it is a
  campaign, and the Operator's bound is *repair only what current scientific work directly depends on*.
- **No canonical propagation of the reopened axis.** `CC-20260922-NMD-PREMISE-WITHDRAWAL-01` and
  `CC-20260922-CLAIM011-DOSE-ENDPOINTS-01` are both **gated**: non-zero scientific deltas on canonical
  surfaces, outside the current authorization's scope.
- **No MD run.** No engine in this deployment — recorded blocked, **not retried** (§27).
- **No re-litigation of `DL-MECH-045`'s verdict.** Its verdict is **upheld**; only its mechanism is
  withdrawn. Being right for the wrong reason is not an error to reverse.

## 5 · The rule this run adds

> **A verification needs a defined surface before it needs rigour.** Name the ref, name the metric,
> and name what is in the tree that was not in the claim — otherwise a correct result and a
> contaminated one are indistinguishable, and the check's confidence is borrowed from nothing.

Corollary, learned twice today: **a sweep is not finished when it returns. It is finished when the
term has been enumerated in every spelling it has** — abbreviation *and* long form, line *and*
occurrence.

---

## 6 · Added after Scientist R returned — a defect of MINE, in the commit machinery

**`incidents` becomes 9; `self` becomes 7; `severity_high` becomes 3, all self.**

### 6.1 `git add -A` while background delegates are writing into the repository

Scientist R reported that my commit `0e13f9e` swept its **unreviewed first draft** of the boost
census into the tree — a draft containing **six guessed DOIs and two transposed PMIDs**. I measured
it rather than take its word: `git show --stat 0e13f9e` does contain
`wwox_expression_boost_census_20260922.md`. **R is right.**

🔴 **Two distinct failures, both mine:**
1. **`git add -A` is unsafe in this session.** Delegates write into `disease-models/wwox/analysis/`
   **while I commit**. Every `git add -A` I have run in this session was a race I did not know I was
   running, and this one lost: an artefact with fabricated identifiers entered a commit, passed my
   gates (no gate checks whether a DOI exists), and went to `main`.
2. **I pushed a delegate's own commit to `main` unread.** R committed its correction as `ef9dbe9`;
   my anchor-refresh push carried it. I did not review it before it landed on the public branch.

> **Fix, effective now: stage explicit paths. Never `git add -A` while a Scientist slot is live.**
> The delegate brief must also say *do not run git* — R's brief forbade registry edits and
> `BATCH_COMMIT` and I assumed that covered committing. It did not.

### 6.2 Verification of the correction — 6/6 sampled citations are accurate

According to PubMed, R's correction is exactly right and the transposition was real:

| PMID | what it actually is | row |
|---|---|---|
| **17200365** | Iliopoulos 2007, *Clin Cancer Res* — **breast**, 5-aza-dC + intratumoral injection in nude mice ([DOI](https://doi.org/10.1158/1078-0432.CCR-06-2038)) | A4 |
| **17019711** | Cantor 2007, *Int J Cancer* — **lung**, H1299 xenografts, AZA/TSA ([DOI](https://doi.org/10.1002/ijc.22073)) | A9 |
| **23464470** | Yan & Zhang 2012, *APJCP* — sodium valproate ↑ WWOX **protein and transcript**, HO8910 **and** xenografts ([DOI](https://doi.org/10.7314/apjcp.2012.13.12.6429)) | C-row |
| **25708809** | miR-153 → WWOX, HCC ([DOI](https://doi.org/10.18632/oncotarget.2927)), **PMC4414157 open** | D1 |
| **25024751** | Stewart 2014, decitabine IHC in **clinical tumour samples** ([DOI](https://doi.org/10.1186/1868-7083-6-13)) | A-class |
| **18460020** | Nakayama 2008, pancreatic ([DOI](https://doi.org/10.1111/j.1349-7006.2008.00841.x)) | corroborating negative |

🟢 **New, which R did not have: `PMID 18460020` now carries `PMC11159152`.** R's finding stands for
the **supplement** (dead `blackwell-synergy.com` domain) but the **body is now open access**. An
acquisition route exists that the repository's note predates. ⚠️ **`is_open_access` is a licence
field** — this is a PMCID, which orders an attempt; it does not promise a body.

### 6.3 The finding to carry forward, framed as R framed it

🔴 **Sodium valproate is the only agent in the census that is approved, BBB-penetrant, paediatric,
and already given to WWOX-DEE patients** — and in one unreplicated 2012 paper it raised WWOX
transcript **and** protein, in vitro and in xenografts. **So WWOX-DEE patients may have been
receiving a WWOX-raising HDAC inhibitor for years and nobody has ever measured WWOX in one.**

⚠️ **This is an unmeasured variable, not a treatment suggestion, and must never be relayed as one.**
It is one paper, ovarian cancer cells, no PMC, zero replication, probably not independent of the
5-Aza row from the same group. **Nothing here is medical advice, and no medication decision follows
from it.** What follows is a *measurement*: `±valproate` WWOX Western on carrier-derived LCLs.

### 6.4 R's verdict, which I am not softening

**No credible boost lead exists.** Ten agents have a measured direction; **all oncology, none in a
neuron, none in a WWOX-DEE genotype**. Specificity fails for every one of them under the repository's
own Sp1 standard. And **abundance was never once tied to function** — the 12-paper agent set and the
18-paper solubility/aggregation set are **disjoint, zero overlap**. The axis reopened today; it
reopened onto an empty shelf.

---

## 7 · Added after Scientist S returned — the predictor is inverted, and I misread the axis first

**`incidents` becomes 10; `self` becomes 8.**

### 7.1 I read the ΔΔG table 1-based; it is 0-based

Verifying S's headline claim, my first parse returned `G372R = 2.2318` against S's reported `1.583`
and **found none of the other five**. The `position` column runs **0–413**. Re-parsed as
`position = residue − 1`, with the wildtype letter checked at every row:

| variant | csv pos | wildtype in file | ΔΔG measured by me | S reported |
|---|---|---|---|---|
| **P47T** | 46 | `P` ✅ | **2.8059** | +2.806 ✅ |
| A141T | 140 | `A` ✅ | 2.2607 | +2.261 ✅ |
| **Q230P** | 229 | `Q` ✅ | **1.5143** | +1.514 ✅ |
| **P252A** | 251 | `P` ✅ | **1.2977** | +1.298 ✅ |
| P282A | 281 | `P` ✅ | 1.8980 | +1.898 ✅ |
| G372R | 371 | `G` ✅ | 1.5826 | +1.583 ✅ |

**Six of six exact.** `Q230P = 1.5143` also reproduces the repository's own long-standing `+1.514`,
which is an independent cross-check on the reading. **My `2.2318` was residue 373.**

🔴 **`self: 8`.** This is the **third** off-by-one/off-by-three indexing error today — the `pLDDT
60–76` misattribution (residues 350/351 for 353/354), the `+8` genomic-offset-versus-amplicon
confusion already in the packet, and now a 0-based/1-based table read. **Coordinate systems are this
session's characteristic defect**, and none of the three was caught by a gate.

### 7.2 The finding, which stands

> **ΔΔG is anti-correlated with the measurements across every WWOX missense variant that has one.**
> **`P47T` has the HIGHEST predicted destabilisation (+2.806) and NORMAL protein in two matrices.**
> **`P252A` has the LOWEST (+1.298) and is the only variant with demonstrated accelerated
> degradation** (CHX chase, MG-132 negative, CQ/NH₄Cl rescue, lysosomal).

`Q230P`'s `+1.514` sits between them. **It therefore carries no evidential weight in either
direction.** n = 6 and the six measurements are not commensurable, so **no statistic is computed** —
S correctly computed none, and the qualitative statement does not need one. This extends the
repository's existing *"la finestra non discrimina"* self-correction from 3 variants to 6, adding the
only two with real turnover data.

### 7.3 Why this matters more than it looks

The upregulation axis reopened this morning. Its **sign** — benefit or harm — depends entirely on
`Q230P`'s folding fate. Today establishes three things about that:

1. **No measurement exists.** `Q230P` has **one** protein-level datum: not detected on a Western of
   patient fibroblasts, with the authors leaving two causes open and testing neither. **Insolubility
   is the un-named third, and nobody has ever looked in the pellet** — a soluble-lysate blot is
   exactly what an aggregating protein looks like.
2. **The predictor we were leaning on is inverted** (§7.2).
3. **The transferred prior is ambiguous in the worst possible way.** The SDR fold's default is
   degradation — but interface substitutions in a fungal SDR homodimer give **aggregation**. WWOX
   homodimerises through its SDR and **our structure is a monomer with the interface unmodelled**.
   Degradation ⇒ a chaperone route is coherent. Aggregation ⇒ **a boost is actively dangerous.**

> **So the axis reopened onto an empty shelf (R) and an unreadable sign (S).** That is a real result,
> not a failure: it converts *"we closed this for a bad reason"* into *"here is exactly what must be
> measured before anyone opens it."* **The proteotoxic flag stands, on both alleles.**

🔴 **And the same monomer limitation applies to my own structural work**, recorded in § 9 of
`gln353_gln354del_structural_adjudication_20260922.md` rather than only against S's.

### 7.4 Two new tool traps from S, both verified as reported

- **(f) A quoted term can be silently DROPPED from an OR block.** `WWOX AND ("G372R" OR "Gly372" OR …)`
  returned a `query_translation` containing **five of six** terms — `"G372R"` vanished with no error,
  and the count silently under-reported. **Every OR-block count must be checked term-by-term against
  the returned translation**, not merely inspected for expansion.
- **The `Q230P` namespace trap.** A bare `"Q230P"` returns 2 records, **neither WWOX** — both
  **GTPBP3**, at an identical `c.689A>C (p.Q230P)`, one carrying a **measured** aggregation result.
  **The most citable-looking false positive in this search space.** Declared as `FT-138`, as a
  tripwire rather than as evidence.

Trap **(e)** re-verified independently by S at 100%: `WWOX AND "Q230P"` → **0** with a flawless
expansion, because the abstract spells it `Gln230`; `WWOX AND Gln230` → 1.
