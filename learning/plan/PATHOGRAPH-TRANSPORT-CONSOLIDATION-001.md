---
record_type: WORK_ANALYSIS
id: PATHOGRAPH-TRANSPORT-CONSOLIDATION-001
title: Pathograph lane classification and PMID 32000863 transport/drift verification
date: 2026-08-25
role: PRODUCER
mode: ANALYSIS_FIRST / MINIMAL_DELTA
authority: none claimed — no lease acquired, no role contract relied upon
status: ANALYSIS_COMPLETE — candidates prepared, no BATCH_COMMIT performed
---

# PATHOGRAPH / SCIENTIFIC-TRANSPORT CONSOLIDATION — ANALYSIS

> **Nothing here is medical advice.** Disease-level only; no individual-level record.
> The human role is referred to as **Operator** throughout.

---

## 0 · OBSERVATION_SCOPE

Every negative in this document is scoped. **Local NOT_FOUND is not repo-wide NOT_EXIST**, and
each negative below names the tree, the ref set and the denominator it was measured against.

### 0.1 Measurement surface

| Fact | Value | How established |
|---|---|---|
| Worktree | `.claude/worktrees/evidence-index` | `pwd` |
| Branch / HEAD | `plan-orchsurf-r4-transcription` @ `e4aa80c` | `git rev-parse` |
| Divergence vs `main` (`788c357`) | **2 behind, 56 ahead** | `git rev-list --left-right --count main...HEAD` |
| Divergence vs `origin/main` | 0 behind, 509 ahead | same |
| Main checkout HEAD | `30cb4f3` on `legend-operating-convention-v1` — **not** `main` | `git worktree list` |
| Ref population swept | **50 refs** (`refs/heads` + `refs/remotes`) | `git for-each-ref` |
| Sweep positive control | `CLAUDE.md` present on **50/50** refs | required before any ref-level negative |
| `legend_lint.py .` | **VERDICT: PASS** (1 `[INFO]`, CLAIM 010 background-only) | run on this tree |

### 0.2 The two commits I lack, and why they do not invalidate this analysis

`main` carries `788c357` and `2bb2700`, which I do not have. They touch **two files, 947
insertions**, both non-scientific:
`learning/plan/SCIENTIFIC-PIPELINE-PREPARATION-001.md` and
`governance/decisions/DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE.md`.

Decisive check, run rather than assumed:

```
git diff --stat HEAD main -- disease-models/wwox/registries/claim_registry_current.md   → empty
git diff --stat HEAD main -- framework/state/state_manifest_current.md                  → empty
```

**Both canonical surfaces under repair are byte-identical between this worktree and `main`.**
This tree is therefore a valid measurement surface for §2–§4. I read the decision record
directly out of `main` via `git show` rather than inferring its content.

### 0.3 Where the Pathograph evidence actually lives — a finding, not a preliminary

`framework/scripts/pathograph.py` is **absent from all 50 refs** (positive control above; 0 hits).
`git rev-list --all --objects | grep -i pathograph` returns **no object of any name**.

The entire Pathograph surface exists only as **four untracked files in the main checkout**:

| Path (main checkout) | Bytes | Git state |
|---|---|---|
| `framework/scripts/pathograph.py` | 70 182 | `??` untracked |
| `framework/scripts/test_pathograph.py` | 22 554 | `??` untracked |
| `disease-models/wwox/analysis/pathograph_inventory.md` | 26 181 | `??` untracked |
| `disease-models/wwox/analysis/data/pathograph_export.jsonl` | 593 631 | `??` untracked |

**Consequence, stated plainly:** the tool, its own test file, the generated inventory and the
export are outside every gate this repository runs. CI checks what is committed; the release
suites check what is committed. Nothing checks these four files. The inventory's own header
promises *"A regression re-derives it and fails if this file has drifted"* — that regression
lives in `test_pathograph.py`, which is itself untracked, so the promise is currently
unenforceable by anything but a hand-run.

I did **not** attribute this work by filesystem timestamps. All four carry mtime 2026-08-25
00:05–00:06; `cp -p` and `git archive` both falsify mtimes, so the timestamps establish nothing
about authorship and are recorded here only as observation.

### 0.4 The Scientist-B pilot — durability verified, not assumed

`PILOT_PMID32000863_GSK3B_LITHIUM_ADJUDICATION_SCIB_v1.md` (931 lines) is **untracked** (`??`)
in the `lettore-b` worktree and appears in **0 of 50 refs**.

⇒ It is **NON-CANONICAL ANALYTICAL EVIDENCE**. It has no durable location and no commit. Every
load-bearing finding in §2–§4 below was re-measured from the primary artifacts; the pilot is
cited only where it independently converges.

A sibling artifact exists at `lettore/learning/scientist/PILOT_PMID32000863_..._LETTORE_v1.md`
(Scientist-A), likewise untracked. Two independent readings of the same paper exist on disk and
neither is committed.

### 0.5 A sweep failure I made, corrected, and am recording

My first sweep for figure pointers used `grep -v 'deepdive_manifests'` to exclude manifest
*files*. That filter deletes **content lines that mention manifests** — which is exactly both
canonical sites I was looking for, since each cites `deepdive_manifests/…json` in its own prose.
The sweep returned a clean, confident, **false** negative.

Corrected to `--exclude-dir=deepdive_manifests`. A second failure in the same family:
`--include=*.md` unquoted is glob-expanded by zsh before `grep` sees it, aborting the command.
Both were caught only because each negative was run against a positive control first. Every
negative in this document carries one.

---

## 1 · RE-MEASUREMENT OF THE REPORTED FIGURES

Re-derived by running the untracked tool against **this** worktree
(`pathograph.py --root . --disease wwox --json`), not by reading the inventory:

| Reported | Re-derived here | Verdict |
|---|---|---|
| 39 claim nodes | `claims_total` = **39** | ✅ reproduces |
| 41 claim→claim wikilink occurrences | `claim_link_occurrences` = **41** | ✅ |
| 30 distinct direct links | `claim_links_directed_distinct` = **30** | ✅ |
| 20 undirected edges | `edges` len = **20** | ✅ |
| 0/20 typed edges | `edges_typed` = **0** / 20 | ✅ |
| 0/39 biological-scale annotations | `nodes_annotated` = **0** / 39 | ✅ |
| 1080 scanned propositions | `propositions_scanned` = **1080** | ✅ |
| 302 relation candidates | `candidates_emitted` = **302** | ✅ |
| 124 NORMAL-priority candidates | `candidates_normal_priority` = **124** | ✅ |
| 17/20 edges with shared evidential paper | **17** (13×1 paper, 3×2, 1×3) | ✅ |
| 3/20 without | **3** | ✅ |
| 18 titles compressing relation structure | `self_relational_nodes` = **18** | ✅ |
| **12 annotation-lane items** | **12**, but *not one population* — see §2 | ⚠️ **decomposes** |

Every reported figure reproduces. **The one that does not survive is the twelve** — not because
the count is wrong, but because it is a sum over three findings of different kinds:

```
asymmetric_links (10) + working_model_comentions (1) + unlinked_prose_mentions (1) = 12
```

Also re-derived and *not* in the reported set, recorded so the denominators are visible:
`candidates_low_priority` 178 · `candidates_without_connective` 778 · `locator_candidates` 265 ·
`locator_candidates_bound_to_a_claim` 109 · `manifests_total` 64 · `manifests_bound_to_a_claim` 30 ·
`isolated_claims` 20 · `shared_evidence_without_edge` 22 · `mirror_relational_disagreement` 5 ·
`working_model_history_lines_excluded` 29 · `losses` 0.

---

## 2 · LANE A — ANNOTATION / MATERIALIZATION

**Result: of the 12 reported items, exactly 1 is lawful mechanical repair. 11 route out.**

### 2.1 The 10 asymmetric links — ROUTED OUT OF LANE A

| # | Edge | Missing direction | Declaring field |
|---|---|---|---|
| 1 | CLAIM 001 ↔ 002 | 002 → 001 | `Clinical meaning` |
| 2 | CLAIM 005 ↔ 036 | 005 → 036 | `Evidence boundary` |
| 3 | CLAIM 009 ↔ 028 | 028 → 009 | `⚠️ Counter-directional evidence` |
| 4 | CLAIM 019 ↔ 033 | 019 → 033 | `Wikilinks` |
| 5 | CLAIM 028 ↔ 034 | 028 → 034 | `Clinical meaning` |
| 6 | CLAIM 028 ↔ 035 | 028 → 035 | `Wikilinks` |
| 7 | CLAIM 030 ↔ 032 | 032 → 030 | `Wikilinks` |
| 8 | CLAIM 030 ↔ 033 | 030 → 033 | `Clinical meaning` |
| 9 | CLAIM 030 ↔ 035 | 030 → 035 | `Clinical meaning` |
| 10 | CLAIM 031 ↔ 032 | 031 → 032 | `Clinical meaning` |

Three independent reasons, any one of which is sufficient:

1. **No rule is being violated.** `framework/protocols/wikilink_schema.md` § 2.2 states the
   mandatory minimum links for a claim record: ≥1 to `PAPER NNN` (`BLOCK_BATCH_COMMIT`), ≥1 to a
   disease-model section *if* `consolidated baseline`, 0+ to meta (`INFO`). **Claim↔claim links
   are not required at all, and no reciprocity obligation is stated anywhere in the schema.**
   `legend_lint.py` contains no rule matching `reciproc|symmetr|back.?link|asymmetr` (denominator:
   the whole file). LINT currently returns **PASS**. There is no defect to repair.

2. **Seven of ten are prose, not annotation.** Only items 4, 6 and 7 are declared in a
   `Wikilinks` field. The other seven are declared inside `Clinical meaning`, `Evidence boundary`
   or a `⚠️ Counter-directional evidence` block. Adding a "back-link" to those means **writing a
   sentence into the target claim's prose** — authoring, not mirroring.

3. **Direction carries meaning.** CLAIM 033's `Wikilinks` names CLAIM 019 because 033 bears on
   019. The reverse is a *new editorial assertion* that CLAIM 019's record should point at 033.
   Symmetrising is not representational repair; it originates relations the registry never
   declared. That is precisely what the assembler's own doctrine forbids — *"The assembler adds
   no relationship and types no edge."*

**Classification: ambiguous-to-semantic. Not safe for mechanical propagation.** If reciprocity is
wanted it is a **schema change** to `wikilink_schema.md` (normative — the file's own header
requires a BATCH_COMMIT with a MAJOR WM bump), not a data repair. Deferred to §6.

### 2.2 The 1 working-model co-mention — ROUTED OUT OF LANE A

```
claims:   [CLAIM 025, CLAIM 026]
sentence: "*(CLAIM 025 / paper 191; CLAIM 026 / PAPER 032, Hussain 2018.)*"
```

Two claims named in one parenthetical citation. **A co-mention is not a declared relation** — the
sentence attributes a source to each claim; it asserts nothing between them. Converting it to an
edge invents the relation. Routed out.

*Checked and cleared:* the sentence's "paper 191" resolves to `[[paper_registry_current#CORPUS
P191]]`, which **exists** (heading at `paper_registry_current.md:6128`, `Claim links: → CLAIM
025`, status *"deep-dived — registry placeholder (lint restored)"*). Denominator: 358 `CORPUS`
headings, 70 `PAPER` headings. LINT accepts it and returns PASS. **This is not a defect and is
not reported as one.**

### 2.3 The 1 unlinked prose mention — ✅ LANE A, LAWFUL

```
source: CLAIM 025   field: Clinical meaning   target: CLAIM 009
text:   "Raffina CLAIM 009: il branch metabolico non si riduce a HIF1A/glicolisi …"
```

Applying the required test:

| Question | Answer |
|---|---|
| SOURCE ASSERTION EXISTS? | ✅ CLAIM 025 exists, status `in observation` |
| TARGET ASSERTION EXISTS? | ✅ CLAIM 009 exists |
| RELATION ALREADY DECLARED? | ✅ **in words** — "Raffina CLAIM 009" is written in the record |
| DOES ANNOTATION CHANGE SCIENTIFIC MEANING? | ❌ No — the relation is stated; only the wikilink syntax is absent |
| PERFORMABLE WITHOUT READING PRIMARY EVIDENCE? | ✅ Yes — it is a syntax repair over an existing sentence |
| BATCHABLE AS GRAPH-MATERIALIZATION REPAIR? | ✅ Yes |

The registry already says the relation in prose; the graph cannot see it because the mention
carries no `[[…]]`. Making it machine-visible is materialization of an existing declaration.

**Candidate prepared:** `CC-20260825-GRAPH-MATERIALIZATION-01`.

---

## 3 · LANE B — RELATION TYPING (SCIENTIST WORK, BLOCKED ON AUTHORITY)

**Re-measured:** 20 edges, **0 typed**. `relation_type` is `UNTYPED` on all 20, with
`relation_type_basis: NO_DECLARED_RELATION_ANNOTATION`.

**The governed vocabulary already exists** and I originate nothing:

- edges → `DIRECT` · `INDIRECT_UNKNOWN_INTERMEDIATES` · `ASSOCIATED` · `CONTROVERSIAL_OPEN`
- nodes (scale) → `MOLECULAR` · `CELLULAR` · `TISSUE` · `ORGANISM`

**Evidence already available, per edge:**

| Shared evidential papers | Edges | Adjudication cost |
|---|---|---|
| 3 papers | 1 | one packet |
| 2 papers | 3 | one packet |
| 1 paper | 13 | one packet, single primary |
| **0 papers** | **3** | **requires ≥2 primaries; cannot be settled from one** |

The three with no shared evidential paper — and therefore the three that cannot be typed by
reading a single source:

- `CLAIM 001 ↔ CLAIM 002` (declared in `Clinical meaning`, not reciprocal)
- `CLAIM 003 ↔ CLAIM 004` (declared in `Wikilinks`, **reciprocal**)
- `CLAIM 030 ↔ CLAIM 033` (declared in `Clinical meaning`, not reciprocal)

**Does the current Scientist contract support the return?** Measured, not assumed: the section
headings of `roles/scientist.md` are — *Why one file*, *Common section*, *Epistemic independence*,
*Working discipline*, *Reading modes*, *Declared capabilities*, *Fingerprint set*, *Session
obligations*. **There is no OUTPUT / RETURN / deliverable schema section.** The contract governs
how a scientist reads and what independence means; it does not define the shape of what comes
back. The packet in §7 therefore states its own return format explicitly rather than referencing
a contract clause that does not exist. **This is a measured gap, recorded, not filled here.**

**🛑 BLOCKED BY AUTHORITY.** `governance/decisions/DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE.md`
(on `main`, read via `git show`) selects **`OPTION B — ACTIVATION_NOT_CONFIRMED`**, status
`BINDING_AS_AN_OPERATOR_DETERMINATION_OF_STATE`. Its consequence 1: all four contracts *"remain
`PROPOSED` … non-binding documents. Their `status:` lines are **accurate**, not stale."*
Consequence 3: *"A new, explicit activation act is required."* Consequence 4 records a measured
obstacle — the only hostile review of these objects returned `CHANGES_REQUIRED` on three of four.

The packet is **prepared and not dispatched**.

---

## 4 · LANE C — NODE DECOMPOSITION (ANALYSIS ONLY, NO ACTION)

18 of 39 claim titles are flagged `self_relational_nodes` — a title carrying source, relation and
target in one label, e.g. `"WWOX-LoF causes network hyperexcitability; AAV-WWOX rescues organoid
phenotype"` (two CAUSAL connectives, one node).

**Does the object model already anticipate decomposition?** Yes, partly. A claim record already
carries structured fields beside the title — `Status`, `Type`, `Pathway`,
`Genotype/model relevance`, `Transferability`, `clinical relevance`, `Wikilinks`. The relational
compression lives **only in the `Title` string**; the record around it is already decomposed
along other axes.

**Is this a graph-view problem or a claim-registry problem?** On the present evidence, **a
graph-view problem.** The assembler declares itself *"a view over the canonical registries …
never a second source of truth."* The scan population is `Title` + working-model BLOCK 2 mirror +
manifest `proposition` fields — and it deliberately excludes `Summary`, `Clinical meaning` and
`Evidence boundary` because *"atomizing a paragraph is a reading operation with its own
contract."* A view may present one claim as several relational candidates **without changing node
identity**. It already does: 302 candidates over 39 nodes.

**What measured failure would justify changing node identity?** A case where the two halves of a
single title require **different relation types, or different evidence, so that no single edge
can be typed without falsifying one half.** That failure has a first candidate instance:
Scientist-B's pilot § 8.2 is titled *"The relation DisMech asserts, and why neither governed type
fits it."* That is a report of the governed vocabulary failing to cover a real relation — the
exact shape of evidence that would move this lane. **It is one instance, in an uncommitted
artifact, and it is not adjudicated here.**

**Recommendation: no decomposition. No claim identity change. Watch for a second instance.**

---

## 5 · PMID 32000863 — TRANSPORT / POINTER DEFECT: **CONFIRMED**

Verified from the primary artifact, not from the reports.

### 5.1 What Figure 7's panels actually are

From `files/fulltext/PMID32000863_Cheng2020_PMC.xml`. The JATS encodes references as
`Fig. <xref rid="Fig7">7</xref>d` — the **panel letter sits outside the tag**, which is why a
naïve `grep '7d'` returns 0 and why my first tag-stripping pass found nothing. Both were tool
artifacts; corrected, the paper's own Results sentences are unambiguous:

| Panel | The paper's own sentence |
|---|---|
| **7b** | *"Pretreatment of an antiepileptic drug **ethosuximide** suppressed PTZ-induced seizure in Wwox−/− mice (Fig. 7b), although … no effects on … Wwox+/+ and Wwox+/− mice"* |
| **7c** | *"we determined dephosphorylation of GSK3β at Ser9 (active GSK3β) … by western blotting (Fig. 7c)"* |
| **7d** | *"Injection of a potent GSK3β inhibitor **lithium chloride** significantly suppressed PTZ-induced epileptic seizure in Wwox−/− mice (Fig. 7d)"* |

**7b = ethosuximide. 7c = the GSK3β blot. 7d = lithium.** The deep-dive manifest agrees
independently: entries 0 and 22 anchor the lithium three-genotype reading to *"Figure 7d, image
inspected"*; entry 1 anchors ethosuximide to *"Figure 7b"*.

### 5.2 The canonical population carrying the defect

Positive-controlled sweep, `--exclude-dir=deepdive_manifests`, over `disease-models/wwox/` +
`framework/state/` (**133 `.md` files**): 9 matching lines in 4 files.

| Site | Tracked? | Verdict |
|---|---|---|
| `claim_registry_current.md:300` | ✅ tracked | 🔴 **DEFECT A** |
| `state_manifest_current.md:112` | ✅ tracked | 🔴 **DEFECT B** |
| `discovery_ledger_current.md:2198` | ✅ tracked | ✅ correct — concerns PMID **29724996**, unrelated |
| `dismech_legend_evidence_crosswalk_v2.md` (6 lines) | ❌ **untracked** | already documents this defect |

**Exactly two canonical tracked sites carry it.**

### 5.3 DEFECT A — `claim_registry_current.md:300` (canonical scientific file)

Current text, verbatim:

> *…il litio ha soppresso le crisi da PTZ in TUTTI E TRE i genotipi, wild-type incluso **(Fig.
> 7b**; per l'etosuccimide il testo dichiara `n.s.` in `+/+` e `+/−` e significativo in `−/−`, e
> per il litio **non dichiara il converso**)*

This is a **bundled pointer**: one parenthetical carries a lithium assertion and an ethosuximide
clause under a single `Fig. 7b`. The pointer is correct for the ethosuximide half and **wrong for
the lithium half**, which is the half the sentence is about. A reader following `Fig. 7b` lands on
the ethosuximide panel — which *is* genotype-restricted — and finds evidence that appears to
contradict the very sentence citing it.

**Candidate prepared:** `CC-20260825-32000863-POINTER-01`.

### 5.4 DEFECT B — `state_manifest_current.md:112` (state-control file)

Inside `batch_20260810_005_scope`, verbatim (bytes confirmed by `od -c`: `Fig 7b`, no period):

> *"lithium suppressed PTZ seizures in ALL THREE genotypes including wild-type (**PMID 32000863
> Fig 7b**, read from the image)"*

Same error, in the record of what a past batch did.

**Lawful treatment — and the reason it is not a second candidate.** `LEGEND_CORE.md:88` makes
`STATE_MANIFEST` *"the only state-control file writable outside a BATCH_COMMIT"*, so this is not
gated behind the batch. But line 112 is a **historical record of a completed batch**, and the
repository's own doctrine on historical records is explicit
(`framework/protocols/fulltext_read_receipt.md`): *"Deleting the historical records would falsify
history; retroactively upgrading them would manufacture evidence. So they are kept visible and
frozen."*

⇒ **Do not edit line 112 in place.** The lawful shape is a **new state-manifest entry** that names
the defect, the corrected pointer and the evidence, leaving the historical scope record intact and
visible. I have **not written it**: this document's mode is analysis, and a state-manifest write is
an act the Operator should authorize on sight of this finding.

**Measured gap:** the repository has an append-only correction ratchet for *receipts* and a
`supersedes:` field for *decisions*, but **no named mechanism for correcting a historical
`batch_*_scope` record**. Recorded. **No new governance layer is proposed here.**

### 5.5 The general failure class: READING CORRECT → TRANSPORT INCORRECT

The reading was right. The manifest recorded `Fig. 7d` on the day of the read and still does. The
error entered when the finding was **propagated** into two canonical surfaces.

**Does the class have a name?** Positive-controlled search (control: *"difetto di propagazione"*
matches `claim_registry_current.md:300`) over `framework/` + `governance/`, `*.md` + `*.py`, for
`propagation defect|transport defect|pointer defect|pointer drift|locator drift|figure pointer`
→ **0 hits**.

The repository has the *phrase* — CLAIM 016 itself closes with *"è un difetto di propagazione, non
di lettura"* — but **no named taxonomy, no rule and no test**. And no validator compares a claim's
figure pointer against its manifest's anchors: `recapture_snippets.py` works *within* manifests,
never manifest→claim.

**The gap is recorded. Building the check is out of scope for this task**, and is listed in §6.

---

## 6 · CLAIM 016 SCIENTIFIC DRIFT — **CONFIRMED, AND SHARPER THAN REPORTED**

### 6.1 What the claim says

- `**Type:**` — *"**DATO (abbondanza, murino)** + DATO meccanicistico risolto a livello di residuo …"*
- `**Summary:**` — *"In Wwox-null mice, **GSK3β is elevated** in cortex, hippocampus and cerebellum…"*

### 6.2 What the primary says

The paper never asserts an abundance elevation. It asserts **activation**, and names its evidence:

- *"a significantly increased **activation** of glycogen synthase kinase 3β (GSK3β) occurs in Wwox−/− mouse cerebral cortex, hippocampus and cerebellum"*
- Fig. 7 legend, panel c: *"**Increased activation** of GSK3β was determined … as evidenced by **dephosphorylation of GSK3β at Ser9**"*
- Results: *"we determined **dephosphorylation of GSK3β at Ser9 (active GSK3β)**"*

### 6.3 What the figure shows

Manifest entry 2, Figure 7c densitometry read at 3× on the native 1946×1627 image, across
`+/+` / `+/−` / `−/−`:

| Measure | Cerebellum | Hippocampus | Cortex |
|---|---|---|---|
| pGSK3β(Ser9) | 2.7 / 3.1 / **1.3** | 3.6 / 3.5 / **2.0** | 3.9 / 3.8 / **2.5** |
| **total GSK3β** | 2.2 / 2.4 / **2.4** | 2.3 / 2.4 / **2.6** | 2.2 / 2.4 / **2.6** |

**Total GSK3β is flat in every genotype and every region.** Inhibitory Ser9 phosphorylation is
reduced in `−/−`. The mechanism is **dis-inhibition**, not increased abundance.

### 6.4 Verdict, and why the existing corrective wording does not cover it

**CONFIRMED.** The `Summary` and the `Type` field assert an abundance datum that the primary does
not claim and its own densitometry contradicts.

CLAIM 016 does carry later wording — `Meccanismo aggiunto (BATCH_20260726_001)` — which moves the
causal statement *"da «GSK3β è elevata» … a «GSK3β è de-repressa»"*. **That wording does not
resolve this defect, and in one respect entrenches it.** It argues from the **Wang 2012** system
(PAPER 056, S9-independent physical inhibition), and its `PREMISE_TAG` reads:

> *"la premessa portante di CLAIM 016 è che **l'abbondanza di proteina GSK3β riporti l'attività**
> … `PREMISE: DEFAULT_FROM_TEXTBOOK`"*

That frames the problem as *an untested inference from abundance to activity*. But in Cheng 2020
abundance **was measured and was flat**, and the paper's claim was **always** about phospho-Ser9.
The premise tag describes a defect the claim does not have, while the one it does have —
a `Summary` and a `Type` that misreport the primary — remains in place. The `Evidence boundary`
paragraph even reaffirms *"Cosa NON cambia: **il dato di abbondanza**"* — preserving the datum that
Figure 7c does not support.

**This is classified separately from §5 and is not folded into it.** They are different defects:
§5 is a pointer that travelled wrong; §6 is a proposition that was never what the source said.

**Candidate prepared:** `CC-20260825-CLAIM016-DRIFT-01`.

---

## 7 · SCIENTIST-B PILOT — DISPOSITION OF ITS FINDINGS

Sorted by what each finding *is*, not by how detailed the pilot is. Non-canonical throughout
(§0.4).

| Finding | Disposition |
|---|---|
| Lithium effect visible in all three genotypes | **ALREADY CANONICAL** — CLAIM 016 `Evidence boundary`, propagated `BATCH_20260810_005`. Pilot corroborates; adds nothing to promote. |
| Genotype-restricted effect belongs to **ethosuximide** | **ALREADY CANONICAL** in substance; the pointer that carries it is defective → §5. |
| No demonstrated lithium target engagement at GSK-3β | **CONFIRMS AN EXISTING BOUNDARY.** pGSK3β(Ser9) was never measured in a lithium-treated animal — Fig 7c is untreated animals only. Tightens the existing `PREMISE_TAG`; not a new claim. |
| No head-to-head lithium-vs-ethosuximide test | **CONFIRMS EXISTING BOUNDARY** (design fact, verifiable from Methods). |
| **Figure 7c statistical weakness** (no statistics, single lanes) | **REVEALS CANONICAL DRIFT** → feeds §6. Not a separate claim. |
| **Undefined four-asterisk marker** (`****` not in the legend key) | **REQUIRES INDEPENDENT SCIENTIST REPLICATION.** A figure-legend completeness finding read from the image; one uncommitted reading is not sufficient. |
| **P14 / P20 discrepancy** (Methods vs Fig 7c legend) | **REQUIRES INDEPENDENT REPLICATION.** Two surfaces of the primary disagree on the age of the animals in the blot. Bears on §6 but must not be assumed into it. |
| Symptomatic anticonvulsant effect vs WWOX-specific mechanistic rescue | **HYPOTHESIS SPACE / brainstorming.** The distinction is licensed; asserting which one obtains is not. |
| Possible overstatement in the **DisMech** causal representation | **EXTERNAL — DisMech correction, not LEGEND.** Out of scope for any LEGEND candidate. Do not import DisMech semantics. |
| §8.2 *"neither governed type fits"* | **ARCHITECTURE-SENSITIVE** → Lane C watch-item, §4. |

Observation / inference / hypothesis separation is preserved: rows 1–5 are observations or
existing boundaries, rows 6–7 are observations awaiting replication, row 8 is hypothesis, rows
9–10 are not LEGEND claims at all.

---

## 8 · WHAT REQUIRES NO NEW SCIENCE, WHAT DOES, WHAT IS DEFERRED

**No new science required (candidates prepared, §9):**
1. `claim_registry_current.md:300` — `Fig. 7b` → `Fig. 7d`, un-bundling the two drugs.
2. `claim_registry_current.md` CLAIM 016 — `Summary` + `Type` corrected from abundance to activation.
3. `claim_registry_current.md` CLAIM 025 — materialize the already-worded `CLAIM 009` relation as a wikilink.

**Requires Scientist judgement over primary evidence (packet, §7 of the plan → separate file):**
- Typing 20 edges against the existing 4-term vocabulary.
- Scale-annotating 39 nodes against the existing 4-term vocabulary.
- Replicating the `****` legend gap and the P14/P20 discrepancy.

**Requires later architecture / governance decision (§6 deferrals):**
- Whether claim↔claim wikilinks are reciprocal — a **normative change** to `wikilink_schema.md`.
- Whether Lane C ever decomposes node identity — needs a second measured instance.
- A named taxonomy and an executable test for READING-CORRECT / TRANSPORT-WRONG.
- **Whether the Pathograph surface becomes tracked at all** (§0.3) — until it does, the tool, its
  test and its regression are outside every gate.
- A mechanism for correcting a historical `batch_*_scope` record (§5.4).

---

## 9 · CANDIDATES PREPARED

Written to `disease-models/wwox/research/commit_candidates/`, **not** propagated. No BATCH_COMMIT
performed. Three separate candidates because they are three unrelated defects.

| Candidate | Target | Class |
|---|---|---|
| `CC-20260825-32000863-POINTER-01` | `claim_registry_current.md` CLAIM 016 | transport/pointer repair |
| `CC-20260825-CLAIM016-DRIFT-01` | `claim_registry_current.md` CLAIM 016 | scientific wording correction |
| `CC-20260825-GRAPH-MATERIALIZATION-01` | `claim_registry_current.md` CLAIM 025 | graph-materialization repair |

⚠️ Candidates 1 and 2 touch the same claim record. `prompt_batch_commit.md` Phase 1 checks
conflicts between candidates in one batch; whoever runs the batch must apply them in the order
above and re-read the block between them. They are kept apart because folding a pointer repair
into a wording correction would hide one inside the other.

---

## 10 · WHAT WAS NOT DONE

No lease acquired · no Scientist contract activated or relied upon · no scientific adjudication
performed · no biological edge typed · no claim identity decomposed · no graph ontology or causal
vocabulary created · no canonical file edited · no historical record rewritten · no BATCH_COMMIT ·
no cold-lab wake/relaunch work reopened · no DisMech semantics imported · no Pathograph heuristic
treated as scientific evidence.
