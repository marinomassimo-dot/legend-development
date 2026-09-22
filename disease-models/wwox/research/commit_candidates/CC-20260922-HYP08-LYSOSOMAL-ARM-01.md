# COMMIT CANDIDATE — CC-20260922-HYP08-LYSOSOMAL-ARM-01

**Source:** Scientist C, Domain D node
([`proteostasis_discrimination_protocols_20260922.md`](../../analysis/proteostasis_discrimination_protocols_20260922.md)),
**verified by the Orchestrator against the primary body** before landing — PMID 30202070 /
`PMC6131187` retrieved in full this session, CC BY, all quotations below read in the returned text
rather than taken from the hand-back.
**Change class:** **MINOR**, and it changes an experiment rather than a claim. One reagent added to
one arm, one step order corrected, two cautions recorded. **No claim reversed, no status moved, no
molecule promoted, no safety language touched.**
**Target:** `therapeutic_hypotheses_ledger_current.md` (`HYP-20260709-08`) and
`discovery_ledger_current.md` (`DL-BIO-001`). **No canonical registry file. No `BLOCCO 1` change.**
**Status:** `PROPOSED — NOT PROPAGATED`.
**Review floor:** **R2.** Experimental design on a `stress-tested` hypothesis; nothing prognostic,
nothing clinical.
**Proposes:** `D-26` — *"a reagent validated in an over-expressing cell line is not validated in the
matrix you will actually use."* (`D-17` remains **reserved — operator-deferred**.)

---

## 1 · 🔴 The finding: our lysosomal arm has a documented false negative in the exact cell type we plan to use

`HYP-20260709-08` and `DL-BIO-001` currently specify the lysosomal-block arm as **chloroquine
40 µM / 24 h** and **NH₄Cl 250 µM / 24 h**, with MG-132 and 3-MA as expected negatives. That arm was
imported on 2026-09-21 from **PMID 41124647**, where it works — in **CAL-62 thyroid carcinoma cells
stably over-expressing a Flag transgene**, a distance the ledger already declares.

According to PubMed, **Schultz ML et al., *Nat Commun* 2018;9:3671**
([DOI](https://doi.org/10.1038/s41467-018-06115-2) — PMID 30202070, `PMC6131187`) ran the same
comparison **on endogenous protein in primary patient fibroblasts**, and the two lysosomal reagents
did not agree:

> *"Unexpectedly, **Baf treatment also recovered I1061T protein to WT levels** (Fig.) indicating that
> the lysosome is a major compartment utilized in I1061T degradation."*

> *"Consistent with previous reports, **treatment with the lysosomal inhibitor chloroquine did not
> significantly alter I1061T protein levels** (Supplementary Fig.). While this difference likely
> reflects an **increased efficacy of Baf to neutralize lysosomal pH relative to chloroquine**, other
> possibilities cannot be excluded."*

**Same protein, same cells, same question, opposite answers from two reagents aimed at the same
compartment.** Chloroquine returned a clean negative on a protein that is, in fact, substantially
degraded in the lysosome.

### 1a · Why this transfers, and the exact scope of the transfer

⚠️ **It transfers as a reagent-sensitivity caution, not as a pathway claim, and the difference is
load-bearing.** NPC1 is a 13-transmembrane glycoprotein triaged from the ER; WWOX is
cytosolic/mitochondrial. **Nothing about NPC1's ER-phagy/ERAD biology is imported here** — not
FAM134B, not MARCH6, not ER-phagy, and no expectation that WWOX behaves this way. What transfers is
narrower and purely pharmacological: **chloroquine is a weaker neutraliser of lysosomal pH than
bafilomycin A1, and a negative chloroquine result therefore cannot close the lysosomal branch.**

🔵 **And note the asymmetry with our own imported precedent**, which is what makes this actionable
rather than academic: in PMID 41124647 chloroquine was **positive** for WWOX `P252A`. So chloroquine
detects the pathway when the effect is large. The exposure is **one-directional** — a chloroquine
*positive* remains informative; a chloroquine *negative* does not exclude anything.

### 1b · This is the same trap `DL-MECH-047` already caught, one reagent to the left

The repository already holds the MG-132 version of this: an inhibitor returning nothing is routinely
read as the pathway being absent. **`Q230P` protein is undetectable at baseline**, so the lysosomal
arm is the arm most likely to return a bare negative — and it is currently specified with the weaker
of the two reagents and no stronger control behind it.

### 1c · Proposed edit — the cheapest item in this report

> **Add bafilomycin A1** to the lysosomal arm of `HYP-20260709-08` step 4 and `DL-BIO-001`, run in
> parallel with chloroquine and NH₄Cl rather than instead of them. **A chloroquine/NH₄Cl negative
> does not close the lysosomal branch; only a Baf negative does.** Precedent: Schultz 2018 on
> endogenous protein in named primary patient fibroblast lines (`GM08399` control, `GM18453`
> homozygote, and three compound heterozygotes, all NIGMS/Coriell), where Baf was positive and
> chloroquine was not.

One catalogue reagent, a few additional wells, inside an experiment already designed.

---

## 2 · The step order of the minimal experiment is not executable as written

`HYP-20260709-08`'s five-step minimal experiment places **pulse-chase at step 3** and the
**inhibitor arms at step 4**.

🔴 **A chase measures the disappearance of a band that must first exist.** `CLAIM 019`'s datum is
that `Q230P` protein is **not detected** at steady state in patient fibroblasts. A cycloheximide
chase from an undetectable band yields an undetectable band at every timepoint and returns no
information at any cost.

**Proposed:** swap the order — **inhibitor arms first, chase second, and chase from the stabilised
condition.** `INFERENZA`, mechanical, and it is also what the worked precedent does: Schultz
establishes accumulation under Baf/MG132/epoxomicin *before* running chases, and its chase condition
is stated exactly — *"Cells were treated with 60 μg/ml cycloheximide for the indicated times."*

🔵 Independent support for feasibility at low abundance: Schultz's compound-heterozygote lines
*"showed **low baseline levels (5–34%)** of mutant NPC1 protein relative to WT"* and were still
tractable. That is **not** `Q230P`'s regime — ours is *not detected*, which is a sensitivity floor
and not a number — but it establishes that the design works well below WT levels.

---

## 3 · What is recorded as a flag and explicitly NOT landed

- 🟡 **Insolubility (branch c) may be untestable in fibroblasts.** Koch 2011 (PMID 22113611) is
  reported as finding the SDS-insoluble species only in patient-derived neurons and *"not observed
  in iPSCs, fibroblasts or glia."* **`abstract-depth` — not read, not promoted.** If it holds, a
  negative solubility result in fibroblasts cannot close branch (c). It sharpens the tissue-specificity
  caveat `HYP-20260709-08` already carries as uncertainty 2. **Queued, not used.**
- 🟡 **The CFTR/NPC1/A1AT paradigm does not transfer as a *measurement* precedent**, because those
  proteins' folding is read through glycan maturation (EndoH resistance — which Schultz uses
  throughout) and WWOX is not a secretory glycoprotein. ⚠️ **This rests on WWOX not being
  N-glycosylated, which neither Scientist C nor I verified.** Recorded as unverified `INFERENZA`.
  The SDR census already says *"Paradigm only"*; this supplies a candidate reason, not a proof.
- 🔴 **A design trap worth one line:** SUnSET, OP-puro and AHA-click measure **global** translation.
  A normal global-synthesis signal in `Q230P` fibroblasts says nothing about whether *WWOX* is
  translated. **Any synthesis arm without a WWOX immunoprecipitation step attached is a design
  error**, not a cheap shortcut.
- ⛔ **Gelsthorpe 2008 (PMID 18216017)** — the permissive-temperature protocol, the single
  best-fitting worked example — is `abstract-depth` only: `is_open_access: false`, and `PMC2276376`
  returned `full_text: ""`. **A PMCID is not a body**, sixth instance this session. Its abstract's
  WT half-life (42 h) and Schultz's body (~9 h) disagree for the same protein; **unadjudicated, and
  not used by either side of this candidate.**
- ⛔ **Nakasone 2014 (PMID 24891511)** reportedly points *opposite* to the repository's HSC70 concern
  behind the arimoclomol withdrawal. **`abstract-depth`, different chaperone axis, different
  compartment, different protein — not promoted, and the withdrawal is not disturbed.**

---

## 4 · The negative that frames all of the above

**No single validated protocol separates reduced synthesis, accelerated turnover and insolubility in
primary human fibroblasts.** The literature supports a staged design, not a one-shot assay: turnover
is well served and has a full worked precedent; insolubility has protocols but no fibroblast
precedent and one published fibroblast-negative; **synthesis has no cheap validated implementation
and is realistically reachable only by elimination.**

This is a productive negative and it is consistent with what the repository already says — the gap
sentence in `missense_proteostasis_matrix_20260921.md` states it verbatim. What is new is not the
gap but **which of our own reagents would have given us a false negative inside it.**

---

## 5 · Provenance and integrity

- **Verification performed by the Orchestrator, not accepted from the delegate.** PMID 30202070 was
  retrieved in full this session and every quotation above was read in the returned body. The
  standing rule — *never trust a delegate census without a repository or primary check* — has now
  paid out five times this session, and this is the first time a delegate's headline finding
  survived verification **unchanged**.
- **Cost figures are excluded from this candidate.** Scientist C's report carries order-of-magnitude
  `STIMA` estimates that no source states. They are the delegate's arithmetic and are not
  propagated here.
- **Quotation integrity:** the Schultz quotations are verbatim, including the truncated `(Fig.)` and
  `(Supplementary Fig.)` cross-references, which the extraction route strips of their numbers. **The
  figure numbers are missing from the source text as returned, and are not reconstructed.**
- **Route note:** `get_full_text_article` requires `pmc_ids` as an array; a `pmid` argument is
  rejected outright. Recorded because it cost one call.
- 🔴 **`UNREAD_PREMISE`: I wrote "none" here, and `growth_anchors.py check` returned
  `[BLOCK] RATCHET_VIOLATION: 10 new unread premises`.** The machine was right. A candidate
  reasoning from ten papers with no receipt, no registry declaration and no queue entry leans on
  papers nobody opened — including one I opened myself and never declared. All ten are now declared
  at their true depth in **`FT-129`**, and the ratchet is back to **0**. Second machine catch of the
  session, both on my output, both cheap.
- ✅ **The owed receipt is persisted: `FTR-20260922-30202070-01`** — `contemporaneous_receipt`,
  `evidence_depth: partial_fulltext_read`, `source_kind: fulltext_remote`, **six verbatim locators**
  carried in `evidence_basis` including both load-bearing sentences, the six Coriell line identities,
  and the transfer-scope note limiting the import to reagent sensitivity. Ledger now **189 chained
  receipts, tail anchored**. **This candidate is no longer blocked.**
- ⚠️ **Its depth is `partial`, not `complete`, and that is an instrument defect rather than a
  choice.** PMID 30202070's body was read sequentially and completely via
  `get_full_text_article(pmc_ids=["PMC6131187"])`, but **figures and supplementary were stripped by the
  route** — every `(Fig.)` and `(Supplementary Fig.)` cross-reference came back with its number
  deleted. The honest depth is therefore **`partial_fulltext_read`**, not `complete_fulltext_read`,
  and no figure-panel claim is made anywhere above. ⚠️ **Both load-bearing quotations point at
  stripped figure references** (`"recovered I1061T protein to WT levels (Fig.)"`,
  `"did not significantly alter I1061T protein levels (Supplementary Fig.)"`) — the *sentences* are
  verbatim running text and stand on their own, but **the panels behind them have not been seen**,
  which is exactly the distinction `FT-126` exists to keep.
