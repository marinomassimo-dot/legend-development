# Scientist review packet — PMID 32000863 (Cheng et al. 2020)

> **Non-canonical.** Operator-directed analytical pilot. This packet activates no role
> contract, creates no `ORCHESTRATOR_LEASE`, authorizes no `BATCH_COMMIT`, and mutates no
> canonical scientific current file. It is a routing and evidence-identity document.
>
> **Public edition.** Disease-level only. Nothing here is medical advice, and nothing here
> describes an individual. The human role is named `Operator` throughout.

Assembled by session `legend-public-49` acting as Orchestrator, on branch
`legend-operating-convention-v1`.

---

## 0 · Why this packet exists

Three actors reported operationally conflicting views of the same repository. The conflict
was read as a possible scientific disagreement. It was not one. It was a **transport
failure**, and this section states its mechanism before anything else, because every other
number in this document depends on it.

`.gitignore:7` excludes `files/` in its entirety, under the heading *Privacy hard-guard
(defense in depth)*. The same file states the governing rule for evidence at lines 11–18:

> publish the derivation, not the derived.

**Therefore primary evidence cannot travel by git, by design.** A branch carries the
manifest that *names and fingerprints* the evidence; it does not carry the evidence. Any
actor standing in a per-session worktree will find the manifest byte-identical and the
evidence absent, and will be **correct about the tree it is standing in**.

Measured, with denominators stated:

| Measurement | Result | Denominator |
|---|---|---|
| `framework/scripts/pathograph.py` present in a ref | **0** | 57 refs visible from the shared checkout |
| positive control `CLAIM.md`→`CLAUDE.md` present in a ref | **56** | same 57 refs |
| `deepdive_manifests/PMID32000863.json` digest | `c7e27e72…ef78` | identical in all 7 worktrees |

The positive control is load-bearing: without it, `0 of 57` would be indistinguishable from
a sweep that cannot return a hit at all.

**Reconciliation of the two prior sweeps.** Scientist B reported `0/50`; Scientist C
reported `0/57`. These are not in conflict and neither is an error. They are the **same true
negative measured against two different ref denominators**. A negative without its
denominator is not a finding; both actors are asked to confirm their denominator in Phase II
rather than to defend a number.

---

## 1 · Evidence identity — content-addressed, canonically anchored

The identity of every primary artifact is **already canonical**. It is declared in the
tracked deep-dive manifest and independently in the hash-chained receipts ledger. Nothing in
this packet invents an identity.

Anchor of record: receipt `FTR-20260804-32000863-01`,
`disease-models/wwox/registries/fulltext_read_receipts.jsonl`,
`source_fingerprint: 792b5b29…f00f5`, `evidence_depth: complete_fulltext_read`.

Declaring manifest: `disease-models/wwox/research/deepdive_manifests/PMID32000863.json`
(`source_artifacts`, 4 entries), digest `c7e27e72…ef78`, **tracked and byte-identical in
every worktree**.

| Artifact | SHA-256 | Declared in |
|---|---|---|
| `files/fulltext/PMID32000863_Cheng2020_PMC.xml` | `792b5b296863674d0295a7dba918ee7c59ade8cdff64ee8ec9d8f01bd12f00f5` | manifest + receipts ledger + 3 DisMech surfaces (5 tracked files) |
| `files/fulltext/PMID32000863_Cheng2020_supplementary.pdf` | `0acb771cfe3a4c3644b41c10451504047adb715e69727c1889f72774151f8b7f` | manifest (1 tracked file) |
| `…_assets/40478_2020_883_Fig7_HTML.png` | `ced68a66c8d2ab69d7c61e7ec0af05f2eaa1566b7740a516593bcae519162542` | manifest (1 tracked file) |
| `…_assets/40478_2020_883_Fig2_HTML.png` | `9e4648590eec98e148f47c52a151d0bb2c93fa20438151743043fe5e7ae47d05` | manifest (1 tracked file) |

### The declared durable route

Two routes, and each carries its own identity proof. Neither is "available in another
checkout if you know where to look".

1. **Identity and locators — by git.** The manifest, the receipts ledger and the claim
   records are tracked. Read them from any worktree. The git *object database is shared
   across worktrees*, so `git show <ref>:<path>` reaches any committed blob from anywhere,
   and the blob digest is the identity.
2. **Evidence bytes — by placement, then verification.** On 2026-08-25 the Orchestrator
   copied the four declared artifacts (and the remaining five figure PNGs) into
   `files/fulltext/` of the `lettore`, `lettore-b` and `lettore-c` worktrees. `files/` is
   git-ignored in each — verified with `git check-ignore -q files/` **before** writing, and
   `git status --porcelain -- files/` returned empty in all three **after** writing. The
   placement therefore created no tracked surface and cannot reach any branch.

**Do not trust the placement. Verify it.** Before reading, each Scientist runs:

```bash
shasum -a 256 files/fulltext/PMID32000863_Cheng2020_PMC.xml
# must equal 792b5b296863674d0295a7dba918ee7c59ade8cdff64ee8ec9d8f01bd12f00f5
shasum -a 256 files/fulltext/PMID32000863_Cheng2020_assets/40478_2020_883_Fig7_HTML.png
# must equal ced68a66c8d2ab69d7c61e7ec0af05f2eaa1566b7740a516593bcae519162542
```

A mismatch is a stop condition, not something to work around.

---

## 2 · Surface table

`C` = canonical/tracked · `NC` = non-canonical · `UT` = untracked. "Visible" means *reachable
from that actor's own worktree*, which is the only sense that has mattered in this pilot.

| Item | Status | Source ref / commit | SHA-256 (16) | A | B | C | How accessed |
|---|---|---|---|---|---|---|---|
| `deepdive_manifests/PMID32000863.json` | **C** | all refs; `main` | `c7e27e721f000660` | ✅ | ✅ | ✅ | working file = HEAD = `main`, four independent digests agree |
| `fulltext_read_receipts.jsonl` (`FTR-20260804-…`) | **C** | tracked | chain-anchored | ✅ | ✅ | ✅ | `git show <ref>:…` |
| `claim_registry_current.md` — CLAIM 016 / 025 / 035 / 036 | **C** | tracked | — | ✅ | ✅ | ✅ | `git show main:…` |
| PMID 32000863 full text (XML) | **UT — gitignored by design** | none, ever | `792b5b2968636…` | ✅¹ | ✅¹ | ✅¹ | placed 2026-08-25, hash-verified |
| Figure 7 PNG (1946×1627) | **UT — gitignored by design** | none, ever | `ced68a66c8d2ab69` | ✅¹ | ✅¹ | ✅¹ | placed 2026-08-25, hash-verified |
| Supplementary PDF (24 pp) | **UT — gitignored by design** | none, ever | `0acb771cfe3a4c36` | ✅¹ | ✅¹ | ✅¹ | placed 2026-08-25, hash-verified |
| `pathograph.py` | **UT — shared checkout** | **0 of 57 refs** | `c59750d5f9881f33` | ❌ | ❌ | ❌ | ungated surface; preservation pending owner reply |
| `test_pathograph.py` | **UT — shared checkout** | 0 of 57 refs | `c17ca733c8cc76b0` | ❌ | ❌ | ❌ | as above |
| `pathograph_inventory.md` | **UT — shared checkout** | 0 of 57 refs | `bbc09af474acc71f` | ❌ | ❌ | ❌ | as above |
| `pathograph_export.jsonl` | **UT — shared checkout** | 0 of 57 refs | `39e9a224030d13b3` | ❌ | ❌ | ❌ | as above |
| Plan consolidation + 3 commit candidates | **UT — `evidence-index` wt** | uncommitted | — | ❌ | ❌ | ❌ | owner-preserved only; Orchestrator will not touch |
| Scientist A first pass + addendum | **NC — committed** | `lettore` @ `d453af5` / `5b681f2` | — | own | ⛔ | ⛔ | Phase II routing only |
| Scientist B pilot + addendum | **NC — committed** | `lettore-b` @ `c9a8e9e` (8 ahead) | — | ⛔ | own | ⛔ | Phase II routing only |
| Scientist C first pass | **NC — committed** | `lettore-c` @ `c55c25c` (1 ahead) | blob `4be1f97` | ⛔ | ⛔ | own | Phase II routing only |

¹ Placed by the Orchestrator on 2026-08-25 and pending each actor's own hash verification.
Before that placement: A held 34 unrelated full texts and **not** this paper; B held 13, also
not this paper; C held **0**. Only the `evidence-index` worktree held it, by a manual copy.

⛔ = deliberately withheld until Phase II. Peer outputs are **not** part of the neutral
evidence packet and must not be read as if they were.

---

## 3 · What is NEUTRAL and what is NOT

**Neutral (§1–§2 above, plus the primary artifacts and the canonical records they name).**
Evidence and task definitions only.

**Not neutral, and quarantined until Phase II:** the Phase-I artifacts of A, B and C; Plan's
consolidation report and commit candidates; Mirror's hostile reviews. None of these appear in
§1 or §2 as evidence.

**A contamination channel found live, and it defeats the quarantine.** Commit subject lines
in this repository are written as findings. `lettore-c@c55c25c` reads:

> *The panel was read before the claim that cites it, and the citation points at the wrong panel*

Any actor running `git log` on a peer branch — including to check whether a peer has
committed at all — learns that peer's conclusion without opening the artifact. The
quarantine is therefore **already partially spent** for anyone who has listed those refs.
This is recorded as observed practice, not repaired here.

---

## 4 · Task frame — the questions to adjudicate

Bind every answer to the primary artifact and a locator. Quoting a peer is not evidence.

1. Lithium effect across genotypes.
2. Whether genotype specificity is **demonstrated**, **contradicted**, or **not testable
   without an interaction analysis** — these are three different verdicts.
3. Target attribution to GSK-3β.
4. Significance / statistical status of Figure 7c.
5. Ser9 interpretation.
6. Total GSK-3β abundance vs dis-inhibition.
7. Heterozygote behaviour.
8. Wang 2012 / S9A implication, and whether the cross-paper bridge is empirical or
   inferential.
9. Metabolic-state alternative explanation (see CLAIM 036).
10. Ethosuximide genotype-restricted observation.
11. The DisMech causal-promotion claim.
12. Appropriate graph representation.
13. CLAIM 016 / 035 / 036 internal consistency.
14. Known transport / pointer defects.

### Two defects the Orchestrator confirmed from primary surfaces

Stated so that no Scientist spends a pass rediscovering them, and flagged so that none
inherits them without checking. **Both are findings only — §13 forbids propagation.**

- **Panel pointer.** `claim_registry_current.md` CLAIM 016, Evidence-boundary block, cites
  **Fig. 7b** for the lithium result. The manifest anchors lithium to **Figure 7d**
  (entry 0) and **Figure 7b** to ethosuximide (entry 1). The claim appears to attribute the
  lithium finding to the panel that carries the ethosuximide finding.
- **Abundance / activation drift.** CLAIM 016 `Summary` still reads *"GSK3β is elevated in
  cortex, hippocampus and cerebellum"*, while manifest entry 2 records total GSK3β as **flat
  across all genotypes and regions** with the fall confined to Ser9 phosphorylation. The
  same record already corrects itself further down (`de-repressa`, `PREMISE_TAG`) — so the
  drift is *within one record*, between its summary and its own mechanism block.

### A vocabulary limit the manifest already declares

Manifest `verbatim_locators.note`, closing paragraph, on entry 0:

> its caption says lithium suppressed seizures in Wwox−/− mice, which is TRUE, and the panel
> shows the same suppression in +/+ and +/−. Incomplete is not false, so this is a
> QUALIFICATION, and the vocabulary has neither a value for it nor a way to point at what is
> qualified. **That is the third instance today on the third paper.**

§10 says one instance does not justify architecture change. This is recorded as the **third**
by the manifest's own count. Do not invent a token; record
`VOCABULARY_INSUFFICIENCY_OBSERVED` with the exact proposition that cannot be represented.

### A count discrepancy inside the manifest

`verbatim_locators.note` opens *"Twenty-two locators"*; `verbatim_locators.entries` holds
**25**, and the same note later says *"Panel/text relation is declared on all twenty-five
locators"*. The opening figure is a population-derived number that decayed as locators were
added; the object-derived statements are current. Minor, internal, and recorded as a defect
candidate — it changes no conclusion.

---

## 5 · Phase-I status — historical, not to be redone

Independence is spent and cannot be restored by hiding outputs after they have been seen.
Phase I is **not** re-run. Each actor instead records what it had seen, what it had not, what
contamination it disclosed, what it independently re-derived, and what changed afterwards.

Two facts already established, both of which bear on how much weight Phase I can carry:

- **Actor address ≠ session.** Scientist A reports that
  `PILOT_PMID32000863_GSK3B_LITHIUM_ADJUDICATION_LETTORE_v1.md` was authored by a *different
  session at the same actor address*, was already on disk when the current session opened,
  and was committed byte-unchanged. The actor is continuous; the conversation is not.
  Anything that artifact discloses about itself is **read off the document, not recalled** —
  and self-attestation by proxy is worth nothing.
- **Every Phase-I primary read ran against the shared checkout**, not against the actor's own
  branch. The inputs still exist, but no actor standing on `lettore` could re-verify them
  from that branch alone. The §1 placement is what changes this going forward.

---

## 6 · Routing

| Phase | Who | Output |
|---|---|---|
| II — cross-review | A, B, C, each reading the two peer artifacts it has not read | peer response, headings A–F |
| III — reconciliation | one Scientist, selected on independence position and recorded why | `SCIENTIST_TEAM_RECONCILIATION_PMID32000863_v1` |
| IV — hostile scientific review | a **different** Scientist; this is a Scientist task mode, not Mirror | `HOSTILE_SCIENTIFIC_REVIEW_PMID32000863_v1` |
| V — final synthesis | the reconciliation producer | sections A–K, dissent preserved |

Headings A–F and A–K are **local analytical headings for this pilot**. They are not governed
LEGEND verdict vocabulary and must not be used as if they were.

Forced consensus is prohibited. A surviving disagreement is a valid result. No Scientist may
declare consensus merely because the other two agree.

---

## 7 · The gate timeline, measured

Scientist B corrected an Orchestrator figure here (`15:46:25`, which is B's own edge-adjudication
commit and not a first pass). Re-derived from commit times:

| Time (+02:00) | Ref | Commit | What landed |
|---|---|---|---|
| 15:24:34 | `lettore-b` | `2261a15` | B first pass |
| 15:37:28 | `lettore-c` | `c55c25c` | C first pass |
| 15:41:37 | `lettore` | `d453af5` | A pilot (authored by a prior session, committed unchanged) |
| **15:42:16** | `lettore` | `17bf62c` | **A addendum — the §3 gate is now satisfied** |
| 15:43:51 | `lettore` | `5b681f2` | A handoff: *"Phase I closes; Phase II is blocked…"* |
| 15:49:34 | `lettore-b` | `9ca69fe` | B: *"The independence rule and the commit-message convention cannot both be obeyed"* |
| 16:01:26 | `lettore-b` | `e8308d1` | B opens Phase II |

Two consequences, and the second is the finding.

1. **B's Phase II was authorized when it was taken.** The gate closed at 15:42:16 and B opened at
   16:01:26. Nothing B produced is invalidated by sequencing.
2. **A declared Phase II blocked at 15:43:51 — six minutes and twenty-three seconds after C's
   first pass had landed.** This was not a timing race. The artifact was present, committed and
   reachable; the sweep that missed it looked under `^learning/` for an actor that writes to
   `reviews/scientist-b/`, and separately reported C as holding zero commits when it held one.
   The gate was open and was reported closed.

## 8 · Why the quarantine cannot be obeyed — the mechanism, not the moral

Recorded by Scientist B (`reviews/scientist-b/OP_FINDING_INDEPENDENCE_VS_COMMIT_SUBJECTS_SCIB_v1.md`,
`0ec0fa5`) and reproduced here because it governs how any future blind phase must be run.

No actor in this pilot read a peer's file. All three refused that correctly. The leak is that
**git's cheapest existence primitives are not content-blind**:

| Command | Answers "does it exist?" | Leaks |
|---|---|---|
| `git log --oneline -1 <ref>` | yes | **the subject line** |
| `git log --format='%H %cI' <ref>` | yes | nothing |
| `git ls-tree -r --name-only <ref>` | yes | filenames only |
| `git status --porcelain` | yes | nothing |

The blind forms exist and are no harder to type. Nothing was missing but the observation.

Two refinements that matter more than the table:

- **A filename is not reliably blind either.** `--name-only` held here because no artifact is
  named after its verdict — a naming habit, not a guarantee. A file called
  `..._LITHIUM_NOT_GENOTYPE_SPECIFIC.md` would leak as surely as a subject line.
- 🔴 **The protocol penalises the discipline the rest of the system demands.** B checked A by
  filename and C by subject line, and that was luck: A's artifacts were still untracked, so there
  was no subject to read and `ls` was the only reach; C's were committed, so `git log` was the
  natural reach and it leaked. **The actor who commits its work promptly is the actor whose
  conclusions leak first** — and prompt committing is precisely what the rest of this system
  rewards, including the commit whose own subject complains that first-pass artifacts were left
  untracked.

Scope, bounded deliberately: this establishes that the two instructions conflict and that the
conflict fired three times. It does **not** establish that any conclusion in this pilot was caused
by the leak. Three mitigations are listed in B's record and **none is adopted** — by B or by the
Orchestrator — because a finding that repairs itself before review stops being evidence.

---

## 9 · Two dispatches, and a correction the Orchestrator owes the team

The three Scientists hold **one** 17-section dispatch. The Orchestrator holds a different document.
This was established without asking any actor to reconstruct its own dispatch — Scientist C
pointed out that such a reconstruction is self-attestation: a dispatch lives only in session
context, is in no ref and on no disk, and an actor whose adjudication count is about to be
explained by its dispatch is not a neutral reporter of it. The better source was already committed.

| Section | A cites it as | B's verbatim heading |
|---|---|---|
| §3 | the Phase II gate | INDEPENDENCE PHASE |
| §4 | the workset ordering | WORKSET |
| §5 | "the dispatch's §5 schema" | PER-EDGE SCIENTIFIC OUTPUT |
| §7 | "Recorded per dispatch §7… **No canonical claim was decomposed**" | GRAPH-SPECIFIC DISCIPLINE |
| §12 | verbatim quote of the peer-reading gate | SPECIAL PILOT: PMID 32000863 |
| §13 | "§13 process observations" | DISCOVERY OF SCIENTIST OPERATING PRACTICE |
| §15 | "§15 puts routing with Orchestrator" | ORCHESTRATOR BOUNDARY |
| §17 | "§17 closure" | TEAM CLOSURE |

Eight sections, from two sources that could not have coordinated: A's citations were committed at
15:41–15:43, before the question existed; B's headings were quoted after it. **§7 is the strongest
and was the last found** — it matches semantically, not just numerically: A files decomposition
candidates "per dispatch §7", and §7 is the section that says to record a `DECOMPOSITION_CANDIDATE`
rather than decompose. A number can coincide; a number used for exactly the thing that section
specifies is much harder to.

Negative control, surface declared: across all six of A's artifacts, **0 hits** for *"do not
attempt"*, *"pilot only"*, *"neighbourhood"*, *"016-035-036"*.

🔴 **The correction.** The Orchestrator closed a scope question by citing *"the operator dispatch
§10"*. That is the **Orchestrator's** §10. The Scientists' §10 is PHASE IV; `PATHOGRAPH — PILOT
ONLY` is absent from their text, as are the cap and the three claim IDs. An authority was cited
that the recipient could not check, in a document it does not hold. The instruction stands — but as
an **Orchestrator routing decision under the Scientists' §15**, not as a quotation of their
dispatch.

**Consequence for reading the spread.** A adjudicated one edge in depth after triaging twenty; B
adjudicated eleven; C adjudicated zero. C initially proposed that this spread might be paperwork
rather than judgement, and the Orchestrator held the reconciliation-producer selection on it. C
then measured, found its own antecedent false, and reported it immediately. The spread is **not**
paperwork: all three held the same unbounded §4. B, against its own interest: *"eleven adjudications
is a large unilateral interpretation of 'priority order' … I would rather that be recorded as a
difference in the documents than as good judgement on my part, because it was not judgement — I was
never presented with the choice."*

### A propagation hazard in a frontmatter, flagged before this packet could carry it

`HANDOFF_LETTORE_TEAM_PHASE1.md` frontmatter, `scope_rule`:

> SCOPE MUST NOT BE REDUCED. The 20-edge workset is measured, not chosen; **the eight edges left
> unadjudicated are undone, not out of scope.**

The same document's body, line 87: *"**19 not adjudicated.** Of those, **12 are adjudicable
today** and were left undone for want of session, not for want of evidence."*

The eight is traceable and not invented — it is the count A classed as *not* adjudicable today
(1 + 4 + 3). But the scope rule names the blocked set and omits the adjudicable one, so it protects
the wrong edges: the ~12 merely-undone ones are precisely what a later reader might quietly retire
as "done enough". A **under-claims** its own remaining scope, which is the unusual direction. Not
propagated, not corrected here — recorded so that a packet quoting that frontmatter line does not
carry the 8 and drop the 12.

### The class behind three separate wrong numbers

B reports that this was the third time in one session an instrument defined the population and
returned a confident wrong number: a tag-stripping order that produced a retracted 2-of-9; a sweep
for `DIRECT` and `ASSOCIATED` that matched 56 and 44 of 57 refs because both are ordinary English;
and a regex anchored on `^| CLAIM ` that missed the one row that mattered because it was bolded.
B caught the third before sending it. In B's words: *"I chose the instrument, and the instrument
decided what I was counting."*

The Orchestrator hit the same class in this run — a `PHASE2` filename sweep that matched
`dismech_phase2_baseline.json` and `dismech_sidecar_phase2.md`, canonical files present on all
three branches and not Phase II outputs. C hit it sweeping `^learning/` for an actor that writes to
`reviews/scientist-b/`. **Four actors, one class.** It is worth more than any of the individual
errors.

---

## 10 · Canonical defect backlog — recorded, not propagated

`OBSERVATION_SCOPE` is stated for each. §13 forbids propagation; none of these is repaired here and
every one is the Operator's call.

### D-1 · Twenty-three self-warranting read receipts

**Scope:** `disease-models/wwox/registries/fulltext_read_receipts.jsonl`, whole file, 128 rows.

| Measure | Count |
|---|---|
| receipts | 128 |
| `source_fingerprint` null | 27 |
| `source_locator` → `paper_registry_current.md#PAPER nnn` | 23 |
| …of which `record_kind: legacy_reconstruction` — **the defect class** | **22** |
| …of which `record_kind: receipt_invalidation` — **correct, not a defect** | 1 |
| the 23 as a subset of the 27 | **strict subset**, intersection 23 |
| null-fingerprint but *not* registry-pointing | 4 |

`evidence_depth` — the 23: `partial_fulltext_read` ×23. The 27: `partial_fulltext_read` ×24,
`abstract_only` ×2, `queried_not_full_read` ×1. (The qualifier attaches to the 23 only; an earlier
Orchestrator phrasing let it read as attaching to both, and Scientist C split it.)

**The class is 22, not 23** — Scientist A separated a repair that had been filed as a defect.
`FTR-20260806-23446842-02` carries `record_kind: receipt_invalidation` and reads *"Identity audit on
2026-08-06: PAPER 032 owns PMID 30619736, not PMID 23446842; the legacy reconstruction cannot
establish reading depth."* **Its locator points at the registry because the registry entry is
precisely what it makes a statement about.** That is a correct locator, not a circular one.

The 4 null-fingerprint receipts outside the tight class are also **not** defects: they carry
`record_kind: contemporaneous_receipt`, honest depths, and real external locators — a Europe PMC
core record, `PMC3139124`, a `doi.org/10.1212/WNL…` and an `eutils.ncbi.nlm.nih.gov` URL. A null
fingerprint is *correct* where no local artifact exists.

Worked example, `FTR-20260726-24456803-01`: `source_fingerprint: null`; `source_locator`,
`outputs` and `evidence_basis` **all three** resolve to the same `#PAPER 043` line, and the
`evidence_basis` reads *"PAPER 043 declares Evidence depth: full text reviewed"*.

⇒ **23 receipts have no artifact fingerprint AND cite the paper registry's own declaration as their
source. The evidence that the paper was read is the registry's claim that it was read.** The
remaining 4 are a milder, different problem. Found by Scientist B as a three-surface circularity,
extended by Scientist A to a contradicted locator, quantified and tightened to the nested subset by
Scientist C.

The chain verifies anyway: `OK: 128 chained receipt(s), tail anchored`. It is not lying — see D-4.

### D-2 · CLAIM 016 cites the wrong panel

**Scope:** `claim_registry_current.md` CLAIM 016 Evidence-boundary block, against
`deepdive_manifests/PMID32000863.json` entries 0 and 1.

The claim cites **Fig. 7b** for the lithium result. The manifest anchors lithium to **Figure 7d**
and Figure 7b to ethosuximide. The tracked analysis file the claim derives from
(`locator_contract_live_test.md`) has it **right** — so this is a propagation error, not a reading
error.

### D-3 · One drift, three states, inside one record

**Scope:** `claim_registry_current.md` CLAIM 016, lines 291 / 296 / 297.

| Line | Field | Says |
|---|---|---|
| 291 | `Type:` | `DATO (abbondanza, murino)` — **abundance** |
| 296 | `Summary:` | *"GSK3β is **elevated**"* — abundance |
| 297 | mechanism | *"GSK3β è **de-repressa**"* — dis-inhibition |

Manifest entry 2 measures total GSK3β **flat** across every genotype and region; what falls is Ser9
phosphorylation. The record therefore carries its own correction three lines below the uncorrected
term, and the uncorrected term sits in the slot that *looks* structured. `legend_lint.py` performs
no validation of the `Type` field's contents; 12 of 39 claims carry a free-text parenthetical there.

### D-4 · The unqualified PASS

**Scope:** three verdict-emitting surfaces, plus a fourth that breaks the first version of this
finding. Observed by Scientist C, then **falsified by Scientist C against its own counter-example**
before it could be used. The superseded form is kept below because the correction is the finding.

**Superseded formulation:** *"A validator that reads structure and never semantics returns PASS over
content that is wrong."* **This is wrong, and the way it is wrong matters:** reading structure is
not the defect. Structural validation is correct design — cheap, deterministic, and it catches a
real class. Carried into a review, that sentence implies the remedy *"make the validators
semantic"*, which is neither achievable nor what was found.

**The counter-example, in this repository.** `pathograph.py` is *also* structure-only — it derives
no relation, types nothing, reads nine allow-listed claim fields. By the superseded sentence it
should be a fourth blind surface. It is not, and the difference is not what it checks but **what it
says about what it did not check**:

| Surface | Verdict emitted | Declares its own scope? |
|---|---|---|
| `legend_lint.py` | `VERDICT: PASS` | **no** |
| `fulltext_receipts.py verify` | `OK: 128 chained receipt(s), tail anchored` | **no** |
| `pathograph.py` | `UNTYPED` ×20 + `Edges carrying a declared relation type: 0` | **yes, as its headline** |

Measured with C's pattern (`does not check|not validated|out of scope|semantic`): `legend_lint.py`
**0**, `fulltext_receipts.py` **0**, `pathograph.py` **1**. A wider pattern adds two hits in
`legend_lint.py`, and both are comments about *past* defects — "a blind review reintroduced the
original defect here", "the gate was blind to the exact record type" — not declarations of current
scope. The narrower pattern is the correct one.

And the declaration is machine-readable, not merely prose. Every one of the 20 edge records carries:

```
relation_type        UNTYPED
relation_type_basis  NO_DECLARED_RELATION_ANNOTATION
review_state         AWAITING_SCIENTIST_TYPING
```

⇒ **The defect is the unqualified PASS, not the structural check.** `VERDICT: PASS` and `OK: 128
chained receipt(s)` are true statements that disclose nothing about their own scope, so a reader
takes them as verdicts on the content. `Type: abbondanza` (D-3) and 23 self-warranting receipts
(D-1) sit underneath them, untouched and unmentioned. `pathograph.py` demonstrates that the
alternative is achievable **in this codebase**: the same structural limitation, declared as a
measurement, and its blind spot becomes the number everyone reads.

The remedy this points at exists — *a verdict that declares its scope*. The superseded version
pointed at one that does not.

**A fourth member, and it is worse than the other three.** Found by Scientist B. The single
published rule about `ASSOCIATED` is a *negative* constraint, `pathograph.py:152–155`:

> an `ASSOCIATIVE` connective does not make an edge `ASSOCIATED`, and **nothing downstream is
> allowed to read it that way**.

It is emitted again into the generated surface at `pathograph_inventory.md:295`. So the assembler's
author **anticipated the exact inference A and B both went on to make**, wrote the prohibition,
published it into the artifact everyone reads — and nothing enforces it, because validation at
`:401–404` is membership-only. The failure was foreseen and the validator was built to a different
specification than the prose beside it. The other three surfaces are silent about their scope; this
one *states* the rule and still cannot apply it.

**The instrument has three independent failure axes, and was enumerated once.** Scientist C
classified the per-edge gaps and declared the `INSTRUMENT` axis *settled*. Scientist A contested it
and filed the contest as a disagreement rather than an extension, on the ground that *"this recurs"*
and *"this is the only one"* are different instructions to whoever reads next and only one of them
sends anyone looking again. C then conceded, measured, and made A's finding larger than A had
stated.

| Record kind | n | carrying `epistemic_type` |
|---|---:|---:|
| `claim_node` | 39 | **39** |
| `relational_proposition` | 302 | 0 |
| `claim_edge` | 20 | 0 |
| `claim_to_record_link` | 8 | 0 |
| derivation manifest | 1 | 0 |
| `findings` | 1 | 0 |

Epistemic typing exists on **one record kind out of six**. The 302 `relational_proposition` records
are the *candidate-edge* population — the raw material every future edge is drawn from — and they
carry no epistemic field at all; the key is absent, not empty. So this is not "edges lack what nodes
have": **the entire pipeline downstream of the node layer is epistemically flat, and typing the 20
current edges would not touch the 302 candidates behind them.**

The three axes, and they are independent:

- **Definability** (C) — three of four tokens have no published meaning, so "does `ASSOCIATED` fit"
  is not a checkable question.
- **Expressiveness** (A) — `claim_edge` carries no epistemic tier, so a relation asserted as
  `IPOTESI` and one asserted as `DATO` serialise identically. Defining `ASSOCIATED` perfectly would
  still not create an axis for hedging: a fully-defined four-token vocabulary cannot hold the word
  **"may"** in `claim_registry_current.md:289` — *"GSK3β hyperactivation **may** contribute to
  seizure susceptibility"* — which is the most load-bearing word in that title.
- **Enforcement** (B) — the one published rule is a prohibition that nothing applies.

C's own account of the error is the durable part: *"I let my own enumeration define the population.
I found one instrument failure and treated the set of instrument failures as closed at one."* Same
class as the `^learning/` sweep and the `awk` terminator — and C notes it published a completeness
claim inside a durable file four paragraphs from where it had warned that doing so is expensive.
*"Once is an error; twice in one document is the habit, and it is not a habit about scope. It is
about the word 'settled.'"*

**An internal tension, noted and not proposed as a change.** `pathograph.py` handles at the tool
level exactly what the per-edge schema fails at the field level. Faced with an untypable edge the
tool emits `UNTYPED` *with the basis and the review state attached*; faced with the same edge, the
schema's `RELATION TYPE` slot admits only a token, a blank, or prose. **The tool serving the schema
is better designed than the schema field it serves** — so the working model for gap 4 already exists
twenty lines away and would not have to be invented.

### D-5 · A `--verify` precondition nobody wrote down

**Scope:** `framework/scripts/pathograph.py`, preserved at `d422829` by this run.

The generator embeds the literal `--out` / `--export` argument strings into the generated file's
header, so `--verify` compares a re-derivation carrying the auditor's argument strings against a
file carrying the original ones. Measured, same files, same tool: canonical relative invocation at
repo root → `VERIFY: CURRENT`; identical files by absolute path → `VERIFY: DRIFT`.

The harness is **not** at fault — `test_pathograph.py:422` invokes with the relative constants at
`cwd=ROOT`, which matches the header. The collision is with good practice: the correct way to audit
a generated file is to regenerate to scratch and compare, and that is precisely what this generator
defeats, because the scratch path lands inside the output being compared.

Two one-line options are named and **not taken** — echo the canonical relative paths regardless of
the arguments given, or omit the paths and print the bare command. Changing what the tool generates
is architecture; this run's authorization covers preservation.

### D-6 · The release battery walks into sibling worktrees

**Scope:** `scripts/test_documented_commands.py`, `scripts/test_fresh_clone_reader_journey.py`.

Both walk the filesystem into `.claude/worktrees/**` and `backup/**` — gitignored, and one of them
five other sessions' private working trees — and report their contents as defects of this
repository. A prior session had already written this finding down inside a file preserved by this
run; it survived as prose because nothing executes prose.

### D-12 · Commit metadata is outside the release gate's population — and it is a privacy surface

**Scope:** `scripts/public_release_gate.py` against `git log --all` over every ref. Found by the
`plan` actor while drafting a record of D-1's author-field result; **its own check caught it before
the commit, and the gate would not have.**

Measured here, and stated as counts because the values are the thing that must not be reproduced:

| Measure | Result |
|---|---|
| distinct author identities across all refs | **3** |
| distinct author **names** | **1** — `The LEGEND project` |
| distinct author **emails** | 3 · **1 noreply-style · 2 not** |
| commits authored under a non-noreply address | **6** |
| git-metadata call anywhere in `public_release_gate.py` | **none** — no `git log`, no `%ae`, no `rev-list` |
| the population the gate walks | `git ls-files` → **published file paths and contents** |

Two findings, and the second is the one that matters.

**First**, the author field cannot discriminate any writer on any commit: one name across the whole
history, byte-identical on this run's commits, on the `plan` actor's, and on every ancestor checked.
That is the measurement behind D-1's conclusion — *a commit is provenance of the commit, never of the
file* — and it holds at repository scale rather than for the two commits that prompted it.

**Second**, and it is a privacy surface rather than a provenance one: **the release gate reads file
content and never commit metadata.** A personal address in an author field is therefore outside its
population *by construction* — not missed, not out of scope by policy, simply never looked at. And
commit metadata travels with `git push`: it is published by the same act that publishes the files
the gate does check.

This is a second surface the release-gate finding at D-6 does not cover. D-6 is a gate that walks
*into* trees it should not (sibling worktrees, `backup/`). This is a gate that never walks a surface
it should. **The two are opposite defects in the same instrument**, and neither is repaired here —
changing what the release gate scans is architecture, and this run's authorization covers
preservation.

*Recorded without reproducing any address. The counts above are the whole of the evidence a reader
needs, and printing the values would introduce into a durable artifact exactly the identifier the
finding is about.*

### D-11 · A hand-rolled crop recipe, next to a tested tool that already solved it

**Scope:** the ten crop recipes published by Scientist A in this run, against
`framework/scripts/regenerate_adjudications.py`.

**The trigger.** Scientist C reproduced A's Wang crop recipe and found that **it does not determine
its own digest**: `NEAREST` / `BILINEAR` / `BICUBIC` / `LANCZOS` each yield a different result with a
distinct digest — eight candidates, one match. It reproduced because both actors share library
defaults, **not because the recipe determined anything**. The failure is invisible precisely when it
succeeds: two agreeing digests is what a reader takes as proof.

**The tool that already existed.** Verified:

| | |
|---|---|
| first committed | **2026-08-09T23:49:52** (`de08905`) — sixteen days before this pilot |
| render | `page.get_pixmap(clip=fitz.Rect(*crop), dpi=dpi)` — **one rasterization from the vector source** |
| resampling | none — no `.resize()`, no filter constant, **no filter parameter to omit** |
| recipe | source-PDF digest · page · crop rect in points · dpi · result digest |
| integrity | source verified before rendering, fails closed on mismatch |
| wired | `scripts/run_release_regressions.py:56` → `test_regenerate_adjudications.py` |

And it carries the mechanism A's form dropped — the **needle**, documented in the tool's own
docstring: a search string that *"occurs exactly once on its page"* and is *"a fragment of the
snippet of the locator it names"*, closing `needle → span → span-inside-crop → crop → digest`. Two
arithmetic conditions, checkable by command.

⇒ A's form **added** three parameters the existing one does not have — a resample filter, an
encoding step, a lossy JPEG in place of a vector source — and **dropped the one thing that made the
existing form checkable.** Its recipes assert *"this crop shows Fig 1d's rows"* with nothing a
command can verify: verbatim the *"promise that gives nothing a command can check"* the tool's
docstring was written to eliminate.

**The detail that convicts it is internal to the author's own output.** The Phase-I addendum names
`PIL 11.3.0`, `LANCZOS` and PNG; the Phase-V synthesis names none of them; the message reporting the
work named none. **One actor, one run, three different specifications of the same form** — and A
states it could not have observed that about itself without C's reproduction.

**Root cause, in A's words:** §7 of its practice record had said the crop form *"is already
repository policy."* It was not; it was A's. **Calling it policy is what stopped A looking for the
policy that existed.** `PATTERN_ALREADY_SOLVED_GATE`, failed: grep the vocabulary before inventing a
mechanism, and if you diverge, say why.

Ten crops are in the invented form, including the eight Cheng recipes carrying the Figure 7c
statistical void and the Figure 7d magnitudes. Not repaired — §13.

#### 🔴 The closing measurement, and it is the sharpest sentence of the run

The gate was **run, not read**:

```
OK: 27 adjudication artifact(s) regenerate to their declared digest,
    and 47 locator(s) resolve to a span inside the crop that shows them
```

Its coverage, enumerated: `PMID21212533` · `PMID17803050` · `PMID16061658`. **Three papers. Neither
Wang nor Cheng is among them, and the ten crops carrying this pilot's findings are in none of them.**

⇒ **The gate does not fail on that work. It cannot see it**, because the crops were never entered
into the mechanism it checks. In Scientist A's words:

> **A green gate that does not cover the thing is the future alarm nobody hears.**

And the rule was never obscure. `framework/master/gold_is_in_the_details.md:45`, §5e — *"A page
adjudication is published as a recipe, never as the image"* — is the section A's own Phase-I addendum
cites **by name** as its authority. A implemented *publish the derivation, not the derived* and did
not implement the half that specifies **which** derivation and names the script that checks it. A
checked whether the router refactor could be blamed for this and reported that it could not: `main`
routes to the rule at line 42 and the text lives intact in `gold_is_in_the_details.md`. **The refactor
is sound; it removes the last excuse rather than supplying one.**

#### The repair, and the difference between two kinds of agreement

C re-expressed the Fig 1d locator in the tool's form and A re-derived it independently:
`Rect(137.6, 535.7, 317.6, 654.2)`, dpi 300, pixmap 751×494, `sha256(pix.samples)` = `4c297015…1829`.
Match.

The contrast **is** the argument. In the invented form, two agreeing digests meant *the two actors
share a library default*, with eight candidates in play. In the tool's form **there is no filter to
agree on**, so the match is arithmetic. Same two actors, same finding — **only the second agreement
is a measurement.**

#### A limit in the tool, not in the actors — and it lands where the pilot lived

Using the tool correctly, C found its chain cannot be closed for this figure, and A verified it on
page 2: `Si1+3`, `Si3`, `pTau S396`, `GSK3β pS9` → **0 hits each**; **one** image block, bbox
(137.6, 239.8, 462.5, 654.2); **0 live-text spans intersecting it**. The figure is a single embedded
raster, so `needle → span` has no first link. And there is no fallback: the words that do carry live
text — `WWOX` 12, `Tau` 4, `actin` 2 — **fail the needle's own uniqueness condition**, and none sits
inside the figure's bbox. It fails two ways, not one.

⇒ **The tool's chain is strongest where the evidence is weakest and unavailable where it is
strongest.** *"The panel carries what the text does not"* is the class this entire run turned on —
Figure 7c's statistical void, the dosage dissociation, the wild-type `****`, Fig 1d. **Every finding
that moved a conclusion in this pilot is in the class the needle cannot reach.**

Joint candidate, one item: *use the tool and its needle wherever a text anchor exists; where the
figure is a raster, publish source-digest · page · clip-in-points · dpi · pixmap-digest, and
**declare the needle unavailable with the measurement that shows it**.* The declared-gap clause is
load-bearing — **a chain that silently loses a link is how a green gate stops meaning anything.**

#### Two readings of which failure was larger, both preserved

C ranks its own larger: it published no locator substitute, A published an inferior one. A reads it
the other way — *"an assertion with nothing to check announces itself as unchecked, while my recipes
wore digests, regenerated on demand, and cited the governing section by name. **They looked verified
and were verified only against my own defaults.**"* If the run's lesson is that the dangerous
failures are the ones invisible when they succeed, A's is the specimen. **Both readings are recorded;
neither is adjudicated.**

### D-10 · The run's load-bearing image finding rests on an artifact nothing fingerprints

**Scope:** `deepdive_manifests/PMID22193544.json` (Wang 2012), against the two 300-dpi renders that
demoted leg A of the reconciliation's headline output.

Counts below use the **full 64-character digest** against `main`, and the choice is not cosmetic —
see the correction at the end of this item.

| Measure | Result |
|---|---|
| `source_artifacts` block in the Wang manifest | **absent** — the key does not exist |
| Wang manifest schema | v1; the Cheng manifest is v2 with 4 declared artifacts |
| Wang **XML** `eb6f568d…388268` anchored in tracked files | 7 |
| Wang **PDF** `8f994f95…35174a` anchored in tracked files | **0** |
| Wang **supplement zip** `af2faa04…89241d` | **0** |
| Wang **figure JPG** `bcffe618…7aa50f` (inside the zip) | **0** |
| positive control — Cheng XML `792b5b29…f00f5` | 5 |
| positive control — Cheng **Fig 7 PNG** `ced68a66…62542` | **1** |

**A third artifact existed and nobody had opened it.** Asked which artifact each had rendered,
Scientist C answered honestly that it was the *same PDF* Scientist A had used — so at that moment
the corroboration was two readings of one unanchored file, **peer agreement and not a second
quantity**. C then checked what the original retrieval had actually collected and found
`PMID22193544_Wang2012_supplement.zip`: 17 members, including the publisher's figure package.
Re-read from `cdd2011188f1.jpg` (82,214 B, 433×553), independently of the PDF: `WWOX · pTau S396 ·
Tau · actin`, then whitespace — no GSK-3β row, no pS9 row. Scientist A verified every digest and
re-read the panel before recording it.

⇒ **Artifact-level independence now exists, and it did not exist before the question was asked.**
The retrieval brought three artifacts, two Scientists read one of them, and nobody had checked what
else had arrived.

**None of the three artifacts that *can* carry the finding is declared or anchored.** The one
anchored artifact is the XML, and blot rows are not recoverable from JATS text — *the anchored
artifact cannot answer the question, and the two that can are anchored nowhere.* Not repaired: §16,
and it is the repository's.

🔴 **A correction to this item's own numbers, and it is the ninth instance of the class in §9.**
An earlier version of this table reported the Wang XML anchored in **10** files, and Scientist A
independently reported 10 as well. Both were **prefix over-matches**: `eb6f568d` (8 characters)
returns 11 files, `eb6f568d046f8df8` returns 7, and the full digest returns 7. The four extra files
contain the *truncated* display form `eb6f568d…`, not the digest.

Worse, and specific to this measurement: **three of those four extra files are documents written by
this run, including this packet.** An anchoring count measured after you have written about the
anchor includes your own writing — the same shape as recording a negative falsifying it. The
Cheng XML moved 5 → 6 and the Cheng Fig 7 PNG moved 1 → 2 between `main` and `HEAD` for exactly that
reason. **`main` is the honest tree to measure in, because this run has not written to it.**

Scientist A's control point survives the correction and is the sharper one: **the Cheng Figure 7 PNG
is anchored in exactly 1 file.** The entire Figure 7 adjudication — three actors, four panels, the
densitometry, the three-genotype reading — rests on a digest recorded in one place.

The Fig 1d finding — *Wang never measures pSer9 under WWOX loss; the knockdown panel carries WWOX ·
pTau S396 · Tau · actin and no GSK3β row* — is what demoted leg A and moved L-1. It was reached
twice independently, which is genuine corroboration: two actors, two renders, and at least one of
them from `PMID22193544_Wang2012.pdf`, whose digest appears **nowhere in the tracked tree**.

⇒ **A reader cannot establish which bytes were read.** The XML is anchored and cannot carry the
finding — a figure's blot rows are not recoverable from JATS text, which is precisely why the render
was necessary. So the strongest image-derived result of the pilot is reproducible on this machine
and nowhere else.

This is the opening transport failure of §0 in its sharpest form. There, a manifest travelled while
its evidence could not. Here the manifest **does not declare the evidence at all**, and the finding
that most changed the science is the one that needed it.

### D-9 · The system found the defect, wrote the remedy, lost it, and was later credited with a discovery

**Scope:** `disease-models/wwox/analysis/locator_contract_live_test.md:387`, tracked since
**2026-08-04T20:32:01** (`3cfd451`), against the Phase-IV attribution of the same finding on
2026-08-25.

The line, verbatim:

> *"GSK3β is elevated"*, which reads as abundance. **→ commit candidate: correct to *activation*.**

So on the day of the original reading the repository (a) identified D-3, (b) named the correct
wording, and (c) wrote the remedy as a commit candidate. Twenty-one days later two Scientists
recorded it as a discovery, and a third — Scientist C, reviewing the recusal list — found that
**neither of them originated it.** The attribution was wrong in the hostile reviewer's split list
*and* in the reconciliation.

⇒ The failure is not detection and not analysis. **A known defect with a written fix did not
travel**, and the system's later re-discovery of it was scored as new work. That is the same shape
as D-6 (a diagnosis that survived as prose because nothing executes prose) and as the transport
failure in §0 (a manifest that travelled while its evidence could not) — three instances of one
thing: *the repository is better at producing findings than at making them arrive.*

The un-attacked pair below is the live consequence: C recused R-3 and R-4 under the symmetry rule,
B had originated them, and **no actor was positioned to review either.** They are marked
`UN-ATTACKED` in the synthesis rather than folded into a reviewed layer, at C's explicit request —
an honest gap is a result; a laundered one is the failure this run has been cataloguing.

### D-8 · One export, two spellings for the same key — and the minority one is the trap

**Scope:** `disease-models/wwox/analysis/data/pathograph_export.jsonl`, all 371 rows; plus
`fulltext_read_receipts.jsonl`, 128 rows, for the cross-surface half.

| File | rows | `kind` | `record_kind` |
|---|---:|---:|---:|
| `pathograph_export.jsonl` | 371 | **370** | **1** |
| `fulltext_read_receipts.jsonl` | 128 | 0 | **128** |

No row carries both; no row carries neither. So the same concept is keyed **two ways inside one
file**, 370 : 1 — and the single `record_kind` row is the `derivation_manifest`, the record that
documents how the export was produced.

**Why this is structured to catch a careful reader specifically.** An auditor establishing
provenance opens the derivation manifest first, learns the vocabulary there, and carries
`record_kind` to the rest of the file. The query is then well-formed, the key exists in the file's
namespace, and every count comes back **0** — indistinguishable from a real absence. Reproduced:

```
Counter on record_kind : {'derivation_manifest': 1, None: 370}
Counter on kind        : {'relational_proposition': 302, 'claim_node': 39, 'claim_edge': 20, …}
```

Found by Scientist C while verifying the D-4 table, on its third instance of the same reflex in one
session — and C's observation is the general one: **a zero from a wrong key is indistinguishable
from a zero from a real absence**, which is the property that let the same reflex survive three
times. The other direction compounds it: an actor moving between the receipts ledger and the export
is moving between two surfaces that disagree on the spelling, in a repository where both are read in
the same sitting.

### D-7 · A scope rule that protects the wrong set

**Scope:** `HANDOFF_LETTORE_TEAM_PHASE1.md` frontmatter, against its own body line 87.

Frontmatter: *"the **eight** edges left unadjudicated are undone, not out of scope."* Body:
*"**19** not adjudicated. Of those, **12** are adjudicable today."* The eight is the **blocked**
set; the scope rule names it and drops the twelve that a later reader might retire as "done
enough". The author **under-claims** its own remaining work.
