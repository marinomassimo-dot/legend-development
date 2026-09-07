---
artifact: HANDOFF — Scientist A, Phase I of the Pathograph scientific adjudication pilot
id: HANDOFF-20260825-SCIENTIST-A-TEAM-PHASE1
status: OPEN — Phase I complete for this actor; Phase II blocked on a condition this actor
  cannot resolve (see §4)
prepared_by: worktree `lettore`, branch `lettore`
operating_authority: OPERATOR_DIRECTED_ANALYTICAL_PILOT — the Scientist role contract is
  PROPOSED and ACTIVATION_NOT_CONFIRMED per DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE.
  This handoff activates nothing and assumes no contract authority.
canonical_mutation: NONE
branch_tip: 17bf62cf95d6f353603d9d214c03e496e1a3db0c
base: main 788c357d9b7ca7afcbe7c1efc3a06b426cf7e2d5 (branch is 201 behind, 0 ahead of it at
  session start; the three commits below are the only work on this branch)
scope_rule: SCOPE MUST NOT BE REDUCED. The 20-edge workset is measured, not chosen; the
  NINETEEN edges left unadjudicated are undone, not out of scope. (CORRECTED 2026-08-25: this
  line first read "the eight edges", which is the count of edges I classified as not adjudicable
  today — 4 SHARED_PAPER_NO_LOCAL_ARTIFACT + 3 NO_SHARED_PAPER + 1 ARTIFACT_ONLY_NO_MANIFEST.
  Naming the blocked set silently dropped the twelve that ARE adjudicable, which is the half a
  scope rule exists to protect.)
---

# HANDOFF — Scientist A · Phase I

**Public, disease-level, de-identified. Nothing here is medical advice. No canonical file was
written; no governance modified; no actor activated; no `BATCH_COMMIT` performed.**

---

## 1 · WORK COMMITS

| SHA | Subject |
|---|---|
| `d453af5e285ad644ccea97d73e68a4d28a00f3b4` | The first pass existed only on the surface no gate inspects |
| `d3fcfc022ae8be23082566af4a3c3a95e8ea19b6` | Two PROPOSED artifacts sat on a canonical-looking path and on no ref at all |
| `17bf62cf95d6f353603d9d214c03e496e1a3db0c` | The bridging measurement is on the axis the mechanism paper says WWOX does not use |

Branch `lettore` is **not** merged and must not be merged by its author. Only the integrating
session merges to `main`, and only from the shared checkout.

## 2 · ARTIFACT REFS

| Artifact | sha256 |
|---|---|
| `learning/scientist/PILOT_PMID32000863_GSK3B_LITHIUM_ADJUDICATION_LETTORE_v1.md` *(preserved, byte-unchanged)* | `b443526aeb760a591c2d2c09c539f2abc99712d6e93bce9f0efab9bec42d99f2` |
| `learning/scientist/TEAM_PHASE1_LETTORE_00_AUTHORITY_AND_WORKSET.md` | `12fd53b8703e0cec5e8ba87a8ed1f66ea7cacf7b96e648e363bf843de60fc347` |
| `learning/scientist/TEAM_PHASE1_LETTORE_01_PMID32000863_ADDENDUM.md` | `a66678addf0c3954c8ce0b72ed1f8978fa3b3b3dc1340b9587ce9382457cae31` |
| `learning/scientist/TEAM_PHASE1_LETTORE_02_EDGE_CLAIM016_CLAIM035.md` | `636df2d05fa1b06e61c97cddfb669bcc0c71ed18fa50c87fc5653c6a9350ed60` |
| `learning/scientist/TEAM_PHASE1_LETTORE_03_OPERATING_PRACTICE.md` | `f78fd8693d46cd6e04ef0eae027f0553e6f4e6cedb272ae41d76ce0087d756b0` |

## 3 · EXACT SOURCES

**Primary evidence** — all read from the shared checkout's `files/`, which is gitignored and is
therefore the only tree that will still hold them tomorrow. Structured surfaces preferred over
PDFs throughout; abstracts held separate from bodies; no PDF text layer carried a locator.

| Source | Artifact | sha256 |
|---|---|---|
| Cheng *et al.* 2020, *Acta Neuropathol Commun* 8:6 · PMID 32000863 | `files/fulltext/PMID32000863_Cheng2020_PMC.xml` | `792b5b296863674d0295a7dba918ee7c59ade8cdff64ee8ec9d8f01bd12f00f5` |
| — figure surface | `…_assets/40478_2020_883_Fig7_HTML.png` (1946×1627) | `ced68a66c8d2ab69d7c61e7ec0af05f2eaa1566b7740a516593bcae519162542` |
| — supplement | `…_Cheng2020_supplementary.pdf` (24 pp) | `0acb771c…8f7f` |
| Wang *et al.* 2012, *Cell Death Differ* 19:1049 · PMID 22193544 | `files/fulltext/PMID22193544_Wang2012_PMC_JATS.xml` | `eb6f568d046f8df831d15e7f8795fcb1d6ac713ec6305f7ded3ad2a330388268` |

**Canonical state** — read exclusively via `git show main:<path>` at `main` `788c357`, never from
this worktree's checked-out tree (which is 201 commits stale and holds one file dirty that this
actor did not author). Read: `roles/scientist.md`,
`governance/decisions/DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE.md`,
`claim_registry_current.md` (CLAIM 016, CLAIM 035), `paper_registry_current.md`.

**Task surface** — `legend-operating-convention-v1:disease-models/wwox/analysis/pathograph_inventory.md`,
shared checkout, **untracked at the time of writing** (`pathograph` appeared on 0 of 57 refs).

> 🔴 **Path qualified by ref, 2026-08-26.** The object exists on exactly one branch —
> `legend-operating-convention-v1` — and on neither `main` nor `lettore`. Written as a bare
> repository path it read as resolvable from this branch, and it is not: a fresh clone of
> `lettore` has no such file. **A path needs its ref for the same reason a negative needs its
> denominator.** Verified with `git cat-file -e <ref>:<path>` across every local head; only that
> one carries it.

## 4 · 🔴 THE BLOCKING CONDITION

> ### 🔴 CORRECTION — 2026-08-25, Phase II
>
> **This section is FALSE and is left standing so the error stays readable.** Scientist C
> committed its first pass at **15:37:28** (`lettore-c` `c55c25c`); this handoff is **15:43:51**.
> **The gate was open.** Phase II has since been opened by Orchestrator and executed —
> [`PHASE2_CROSS_REVIEW_LETTORE_v1.md`](PHASE2_CROSS_REVIEW_LETTORE_v1.md), § 0.3 for the full
> account of how a correct-at-the-instant measurement became a false published routing fact.

**Phase II cannot begin, and it is not blocked on me.**

| Actor | First pass on PMID 32000863 | Durable |
|---|---|---|
| A (`lettore`) | present | ✅ committed by this session |
| B (`lettore-b`) | present | ✅ committed, 4 commits ahead of `main` |
| C (`lettore-c`) | **absent** — its pilot is on PMID 33914858, a different paper | ✗ 0 commits; all work untracked |

Measured by path names only. **No peer artifact content was opened, and Scientist B's pilot was
not read.** The gate requires all three first passes; C has recorded none on this paper.

Independence, once spent, cannot be restored by noticing later that it was spent. Routing this is
Orchestrator's under §15, not a scientist's.

## 5 · OBSERVATION_SCOPE

- **1 edge of 20 adjudicated** to the dispatch's §5 schema: `CLAIM 016 <-> CLAIM 035`.
- **19 not adjudicated.** Of those, **12 are adjudicable today** and were left undone for want of
  session, not for want of evidence; **1** has a bare PDF and no manifest; **4** name a paper
  whose artifact is on no disk here; **3** have no shared evidential paper. Class per edge:
  artifact 00 § 3.2.
- `PAPER 056` was **not** re-read end to end. Its 9 recorded verbatim locators were re-verified
  against the artifact (**9/9 body-exact, 0/9 abstract**) and the passages the edge turns on were
  read in full. **Targeted verification read** — no `FULLTEXT_READ_RECEIPT` emitted, no reading
  debt cleared, no evidence-depth field changed.
- Fig. 7c read at 2× and 6×; four crop recipes published and **re-executed byte-identically**.
  Crops written outside the repository — the derivation is published, the reproduction is not.
- Negatives are scoped to their searched surface with denominators stated at each point.
- Supplementary **figure panels** were not individually adjudicated; the supplement absence claim
  covers its 24-page text layer and 9 legends only.

## 6 · GRAPH CONTRIBUTIONS, classified

**Ready for later integration** — subject to review, not canonical:

| Item | Disposition |
|---|---|
| WWOX ⊣ GSK3β, residue-mapped (388–407 / L404), S9-independent | **carry existing relation** — `DIRECT` within `PAPER 056`'s system, with *no WWOX-DEE allele tested* attached |
| `CLAIM 016 <-> CLAIM 035` as declared | **carry with qualification** — `ASSOCIATED` |

**Require qualification:** the `ASSOCIATED` edge travels only with the statement that the shared
paper contains no seizure endpoint and that the bridging Ser9 readout is on the axis that same
paper shows WWOX does not use. Without it the edge reads as mechanism.

**Unsupported:** `GSK3β state → seizure susceptibility` as a mechanism edge from these two papers.
**Explicitly rejected type:** `INDIRECT_UNKNOWN_INTERMEDIATES` for `016<->035`.

**Unresolved:** whether the Wang mechanism operates *in vivo* in `Wwox−/−` brain. `additional
source required`, and there may be none — `WWOX AND GSK3` returns five records in all of PubMed.

**Architecture-sensitive** — for Plan, not for a Scientist to act on:

- **DC-1 · `CLAIM 016`** compresses ENTITY + STATE + hedge + RELATION + PHENOTYPE + CONDITION into
  one title. Decomposition **would change scientific meaning**, and should: the weak half stops
  borrowing the strong half's credibility.
- **DC-2 · `CLAIM 035`** is two edges plus one mechanism attribute in one title. The attribute
  (`S9-independent`) belongs to neither edge and is what adjudicates the neighbouring one — a
  graph that cannot carry it loses the fact that decides `016<->035`.
- **DC-3** · registry title and working-model mirror row disagree on `CLAIM 035`'s relational
  wording; a LINT rule syncs their *status* and nothing syncs their relational content.
- A graph vocabulary of four relation tokens has **no representation for the hedge** *may
  contribute to*, which is the most important word in `CLAIM 016`'s title.

## 7 · CANONICAL DEFECTS FOUND — reported, not repaired

All are candidates for lawful later integration via `BATCH_COMMIT`. **No edit was performed.**

| # | Object | Defect | Class |
|---|---|---|---|
| 1 | `CLAIM 016`, Evidence boundary | cites **Fig. 7b** for a lithium finding that is in **Fig. 7d**; sends a verifying reader to the panel that appears to refute the claim | MINOR *(from the preserved pilot)* |
| 2 | `CLAIM 016`, `Summary` + `Type` | say *"GSK3β è elevata"* / `DATO (abbondanza)`; the same record's `Meccanismo aggiunto` block says that wording is wrong. A graph materialiser reads the superseded field | MINOR |
| 3 | `deepdive_manifests/PMID32000863.json` entry `[0]` | declares `surface: body` for a proposition its quoted caption does not contain; correctly surfaced at entry `[22]` | manifest hygiene *(from the preserved pilot)* |
| 4 | `paper_registry_current.md` | four papers recorded `complete_fulltext_read` with **0 artifacts and no manifest** — PMIDs 24369382, 24456803, 30361190, 27495153 | evidence reachability |
| 5 | `PAPER 041` (PMID 29808465) | `abstract only — paywalled`, and the shared evidence for **three** edges of the `consolidated baseline` Q230P cluster | acquisition |

## 8 · UNRESOLVED DISAGREEMENTS

**None with a peer** — no peer artifact was read, so no disagreement can yet exist. The dissent
trail begins empty by design.

**One disagreement with the repository's implicit reading**, recorded rather than resolved:
`CLAIM 016` treats `PAPER 056`'s mechanism as making its causal statement mechanistic. Artifact 02
finds that composition fails at the Ser9 joint. The strongest counter-argument — that
docking-motif de-repression and a secondary Ser9 fall could coexist — is **stated at full strength
and not refuted**; it is unevidenced, not wrong. That is preserved as a live open question, not
resolved in my own favour.

## 9 · WHAT THE NEXT ACTOR SHOULD NOT REDO

- The workset counts (20 / 17 / 3) — measured, and they match the dispatch.
- The adjudicability triage — derived mechanically; re-derive it only after new artifacts land.
- The 9 `PAPER 056` locators — re-verified today against the artifact, 9/9 body-exact.
- The Fig. 7c crop recipes — published and re-executed byte-identically.
- The authority determination — `DEC-20260822` is a standing operator determination; re-read it,
  do not re-litigate it.

## 10 · OPEN ITEMS THIS ACTOR CANNOT CLOSE

1. Phase II gate — Scientist C's first pass on PMID 32000863. **Orchestrator.**
2. Acquisition of five full texts blocking six edges. **Orchestrator → `find-fulltext`.**
3. Placement of the two `PROPOSED` artifacts under `framework/protocols/`. **Mirror or Plan.**
4. Whether `pathograph_inventory.md`, which exists on no ref, is the canonical task surface.
5. Independence verification of this session — self-attestation is not evidence. **Mirror.**
6. `disease-models/wwox/research/deepdive_manifests/PMID42422765.json` is dirty in this worktree
   and was **not authored by this actor**. Not committed, not reverted, not staged. It belongs to
   whoever is holding it.

---

*Non-canonical. Nothing here is medical advice.*
