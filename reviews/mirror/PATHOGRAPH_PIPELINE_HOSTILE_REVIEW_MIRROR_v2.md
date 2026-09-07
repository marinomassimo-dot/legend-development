---
artifact: MIRROR hostile review (Annex C.2) — Pathograph / Scientist / Orchestrator pipeline
review_id: PATHOGRAPH_PIPELINE_HOSTILE_REVIEW_MIRROR_v2
object: the first-run pipeline as a whole — Pathograph layer, Plan lane classification and three
  prepared commit candidates, two independent PMID 32000863 adjudications, the Fig. 7b/7d
  transport defect, and the DisMech downstream boundary
supersedes: PATHOGRAPH_HOSTILE_REVIEW_MIRROR_v1 (Pathograph layer only; its two blocking
  findings are re-measured here against byte-identical objects and both still stand)
level: R4 (METHOD — Mirror)
reviewer: mirror
date: 2026-08-25
verdict: REFINED — see § 2
personal_data: none. The human role is **Operator** throughout.
scope_note: every number below was produced by executing a command in this session. Where I
  report another actor's figure I re-derived it; where I could not, I say so.
---

# The pipeline originates no biology — and it holds by exclusion and by a formatting accident, not by a check

---

## 0 · OBSERVATION_SCOPE

Every negative below is scoped to this table. **Local NOT_FOUND is not repo-wide NOT_EXIST.**

| Fact | Value |
|---|---|
| Derivation instant | `2026-08-25T13:32:41Z` |
| My worktree / HEAD | `.claude/worktrees/mirror`, branch `mirror` @ `c7e8d6e` — 0 behind `main`, 84 ahead |
| Shared checkout | `<REPO_ROOT>`, branch `legend-operating-convention-v1` @ `30cb4f3` |
| Plan | `.claude/worktrees/evidence-index`, `plan-orchsurf-r4-transcription` @ `e4aa80c` |
| Reader tree 1 | `.claude/worktrees/lettore` @ `9b0cf47` (2026-08-14) |
| Reader tree 2 | `.claude/worktrees/lettore-b` @ `2261a15` (2026-08-25) |
| Reader tree 3 | `.claude/worktrees/lettore-c` @ `788c357` |
| Orchestrator | `.claude/worktrees/orchestrator` @ `1e2fabd` |
| Ref population swept | all `refs/heads` + `refs/remotes` |
| Sweep positive control | `LEGEND` present on `main` in 331 files; `Fig. 7d` positive on `lettore-b` |
| `legend_lint.py .` | **PASS** (1 `[INFO]`) |
| `fulltext_receipts.py verify` | **OK — 128 chained receipts, tail anchored** |
| `growth_anchors.py check` | **PASS** — claims 39 · papers 70 · corpus 356 · literature 390 |
| `lease_state.py` | **ACTIVE by derivation: 0** (5 leases: 2 stale, 3 released) |

**The tree moved under me.** At `13:27Z` Plan's worktree held 6 untracked records; at `13:32Z` it
held 8 plus 3 commit candidates. Findings § F and § E are pinned to the `13:32Z` state.

**I do not assert the A/B mapping.** The `lettore` document declines to self-assign the label —
*"self-attestation is not identification"* — and it is right. I address the readers by worktree.

---

## 1 · VERDICT

### STEELMAN (C.2 — mandatory, before the objections)

Six things are right, and none of them is decorative.

1. **No biological edge entered the graph by any of the seven forbidden routes.** 20 edges, **0**
   causally typed, **0** of 39 nodes carrying a biological scale. The `CLAIM 016 ↔ CLAIM 035` edge
   — the one this review stress-tests — carries `relation_type: UNTYPED`,
   `relation_type_basis: NO_DECLARED_RELATION_ANNOTATION`, `review_state:
   AWAITING_SCIENTIST_TYPING`. Verified by execution, not by reading the report.
2. **The causal overreach the dispatch names as the required stress test does not reach the
   downstream consumer.** All **17** `ELIGIBLE_FOR_EXPORT` propositions in the DisMech sidecar are
   biochemical (Wang 2012, PMID 35716775). Enumerated: **no lithium, no seizure, no PTZ
   proposition is eligible.**
3. **Both readers reached the same conclusion against the paper's own framing, and both refused
   the drug-effect → target-attribution step.** Neither converted *lithium suppresses seizures*
   into *GSK-3β is the target*.
4. **Plan's three commit candidates are correctly scoped, correctly ordered, and each declares
   what it does not do.** POINTER-01 refuses a bare `7b → 7d` swap on the correct ground — the
   parenthetical is bundled and `Fig. 7b` is right for its ethosuximide half. DRIFT-01 carries two
   Scientist-reported qualifications forward *without folding them in*, because they are not
   independently replicated. That is the discipline, exercised.
5. **No actor self-activated.** 0 ACTIVE leases; the `lettore-b` document declares *"NOT ACTIVATED
   — no TASK_ACK, no lease, `roles/scientist.md` deliberately not activated"*; Plan's records
   declare `AUTHORITY_CLAIMED: none`, `ACTIVATION: NOT_REQUESTED`.
6. **The dispatch surface is free of conclusion-shaped prompts by design, and says so.** Plan's
   execution contract § 396: *"a research question, an evidence target, a hypothesis to test, an
   anticipated conclusion | **absent from every input file by design, not by omission**"*, traced
   to H.1 — which binds the dispatcher, not the reader.

### KEY OBJECTION

**The graph is clean of the transport defect because it does not read the surface the defect lives
on — and that same exclusion drops the qualification that prevents the causal overreach.**
`pathograph.py:52` declares `Summary`, `Clinical meaning` and `Evidence boundary` unscanned. The
defect is in `Evidence boundary`. So is the sentence *«l'esperimento non stabilisce un rescue
farmacologico WWOX-specifico»*. Measured: **0** records in the DisMech sidecar derive from
`Evidence boundary`; the strings `genotipo-specifico` and `TUTTI E TRE` are **absent from the
sidecar entirely**.

The overreach is blocked anyway — but by a **formatting property**, not an epistemic one (§ H-3).

### VERDICT: `REFINED`

`REFINED_FORMULATION` — the proposition as submitted:

> *The pipeline preserves provenance and originates no unsupported biology.*

as it survives review:

> **The pipeline originates no unsupported biology — verified by enumeration of every edge, every
> eligible downstream proposition and every typed relation. It does not preserve provenance: the
> producing actor is absent from the graph export at every record, and the field carrying the
> load-bearing qualification is read by neither projection. The safety of the downstream boundary
> currently rests on a `wikilink_only` classification produced by where an author typed a wikilink
> — a property that a cosmetic repair silently removes.**

`REVIEWER_CONFIDENCE` — high on every mechanical finding (all executed, all reproducible); high on
§ F and § H (demonstrated end to end, including a detector I built and watched fail); **medium** on
completeness of my own attack surface.

`RESIDUAL_UNCERTAINTY` — I did not re-read Figure 7c at the image to re-derive the densitometry
values DRIFT-01 rests on; I verified only that the primary's *text* says activation and never
abundance. I did not adjudicate any biological relation.

`WHAT_WOULD_CHANGE_MY_MIND` — the `Evidence boundary` field reaching one machine reader, plus the
two invariant regressions of § E-2. That moves this to `CONFIRMED`.

---

## 2 · A · PROCESS FINDINGS

**A-1 · 🔴 The entire first run exists on the surface nobody gates.**

| Actor | Artifacts | Git state |
|---|---:|---|
| Pathograph (tool, tests, inventory, export) | 4 | **untracked**, shared checkout |
| Plan (records + 3 commit candidates) | 11 | **untracked** |
| Orchestrator (trial designs, decision path) | 12 | **untracked** (2 further files in that directory *are* tracked) |
| Reader `lettore` (adjudication + 2 protocols) | 3 | **untracked** |
| Reader `lettore-c` (pilot + practice) | 3 | **untracked** |
| Reader `lettore-b` (adjudication) | 1 | **committed** @ `2261a15` |

**Denominator, stated.** 4 + 12 + 12 + 3 + 3 = **34 untracked**, plus the 1 committed = **35**.
The Plan figure is the one that decays — it was 10 at `13:27Z` and 12 at `13:32Z` while I
measured. Counted by `git status --porcelain | grep '^??'` per seat at the pinned instant, not by
directory listing: the Orchestrator directory holds 14 files and 2 of them are tracked.

`git grep -il pathograph` over every ref returns **0**. `pathograph.py` exists in no git object.
CI gates what is committed; `run_release_regressions.py` gates what is committed. **Nothing gates
34 of those 35 artifacts.** The inventory promises *"a regression re-derives it and fails if this file
has drifted"* — that regression is `test_pathograph.py`, itself untracked, so the promise is
unenforceable by anything but a hand-run. One reader found this class in its own tree and
committed; the finding did not travel to the other five seats.

**A-2 · 🔴 All three canonical controls PASS on a tree carrying a live canonical defect.** LINT
`PASS`, receipts `OK (128 chained)`, growth anchors `PASS` — run by me, on the tree whose
`claim_registry_current.md:300` misdirects a reader to the wrong figure. No control looked.

**A-3 · The freeze instrument the design specifies was never invoked.** `benchmark_input_surface.py`
exists; `BENCH-AB-001` exists with manifest, population and surface spec; **no run directory for
pilot G-1 exists**, and neither reader's document mentions the instrument, `verify --post-read`,
parity, or a `sha256` comparison. Plan's own design had already named the gap — *`before
comparison` is not a freeze at all … it has no instrument* — and the pilot then ran without any of
the three.

---

## 3 · B · PROVENANCE FINDINGS

The chain the dispatch asks a consumer to navigate, measured against the 593 KB export:

| Link | Present? | Evidence |
|---|:--:|---|
| EDGE → CLAIM | ✅ | 20 edges, `endpoints` on each |
| CLAIM → SCIENTIFIC ASSERTION | ✅ | `bound_claims` on 302 propositions |
| → PRIMARY SOURCE | ✅ | `PMID` 599 occurrences; `32000863` × 16 |
| → LOCATOR | ✅ | `anchor` on 265 records |
| → ARTIFACT / RECEIPT | ✅ | `artifact` 265, `receipt` 265 |
| → **PRODUCING ACTOR / RUN** | ❌ | `actor` **0** · `producer` **0** · `run_id` **0** · `author` **0** · `session` **0** |
| → REVIEW STATE | ✅ | on edges and propositions |

**B-1 · 🔴 The chain breaks at exactly one link: the producing actor.** Six of seven links are
navigable. A consumer can reach the artifact and the receipt and cannot learn who produced the
record or in which run. This is the one structural gap, and it is one field wide.

**B-2 · The evidence-quality verdict does not travel.** `panel_text_relation` appears **0** times
in the export. **26 of 265** locator-backed candidates descend from a locator where LEGEND itself
recorded `text_contradicted_by_panel` (13) or `panel_qualifies_text` (13). In the export they are
indistinguishable from the 44 the panel confirmed.

---

## 4 · C · INDEPENDENCE FINDINGS

**C-1 · 🔴 Both attestations are unbacked by any instrument.** `lettore-b`: *"written without
reading Scientist A's output for this task, and without reading the Plan crosswalk."* `lettore`:
*"no peer Scientist output was read. `lettore-b` and `lettore-c` worktrees exist on this disk and
were **not** inspected."* Both are sender claims. The parity instrument that would make them
durable exists and was not run (A-3). The only supporting evidence is negative-space — no
cross-citation in either direction, which I verified — and negative space is weak evidence.

**C-2 · Exposure was asymmetric, and both disclosed it.** `lettore` read Plan's crosswalk, as its
task directed. `lettore-b` did not, and re-derived Plan's statements from the primary. **The two
readings are not equally isolated from the common upstream**, and a dispatcher comparing them
should not treat the pair as symmetric.

**C-3 · Convergence on near-identical repair text is not contamination.** Both propose almost the
same corrected Italian parenthetical. Both are minimal edits of *the same registry string*; the
common ancestor explains the convergence without any contact between the readers. I record this
because it is the finding a hostile reviewer would reach for and it does not hold.

**C-4 · The A/B labels are the dispatcher's assertion.** `lettore` refused to self-assign, on the
correct ground. Nothing I can measure from the trees establishes the mapping.

---

## 5 · D · AUTHORITY FINDINGS

**D-1 · No self-activation, no lease bypass, no PROPOSED contract treated as binding.** 0 ACTIVE
leases by derivation. Every actor declares its authority as none.

**D-2 · One stored/derived lease disagreement.** Lease #3: `stored=EXPIRED`, `derived=STALE`. The
derivation is authoritative and the tool reports both, which is the correct behaviour; the stored
value is stale metadata. Non-blocking.

**D-3 · One asymmetric declaration.** The `lettore` document states non-canonicality but never
states its authority basis — `lease`, `TASK_ACK`, `authority`, `ACTIVATED` return **0 hits**.
Non-canonical and unauthorised are different properties; the second is not declared. Non-blocking,
one line to close.

**D-4 · The commit candidates claim nothing.** All three `PREPARED — awaiting the next lawful
BATCH_COMMIT`, batch gate *"intentionally untouched"*, ordering declared and load-bearing.

---

## 6 · E · GRAPH-INTEGRITY FINDINGS

**E-1 · Origination is clean.** Tested against every route § 2 of the dispatch names: no edge from
a shared pathway, a shared paper, two `DATO` endpoints, reciprocity, a connective class, a title,
or DisMech. `_build_edges` types an edge from a declared annotation and from nothing else.

**E-2 · 🔴 BLOCKING, carried from v1, unrepaired.** The two generated surfaces are **byte-identical
to what v1 measured**:

```
bbc09af474acc71f6549be7d296c1e2b94db04673def1a6c4a66a9baa231a032  pathograph_inventory.md
39e9a224030d13b350022c696d4f753d855c4859aa00bb7a0320f4e95e361ebd  pathograph_export.jsonl
```

Both v1 blocking findings therefore stand as facts about the current object:
- the prohibition on **inferring a relation type from grammar** is enforced by no test, and the
  golden-file test that appears to enforce it is cleared by the documented regeneration step;
- a **Scientist typing obligation can be discharged without an annotation** — reciprocity alone can
  mark an edge `TYPED` — and the suite passes.

30 tests, `Ran 30 tests … OK`, re-run this session.

**E-3 · Node decomposition: the proposal is a rendering repair and survives every question.** The
only Lane-A item is CLAIM 025 → CLAIM 009, declared in prose (*"Raffina CLAIM 009"*,
`claim_registry_current.md:451`) with no wikilink. It does not change claim identity, requires no
primary evidence, preserves provenance, and asserts a relation the registry already states. The
**10 asymmetric links** and the **1 working-model co-mention** are correctly routed **out** —
*"converting a co-mention to an edge invents the relation."* Arithmetic verified against the
export findings: 10 + 1 + 1 = **12**.

**E-4 · One overstated clearance.** GRAPH-MATERIALIZATION-01 says of the co-mention *"Checked and
cleared … Not a defect."* What was checked is that `paper 191` resolves — `CORPUS P191` exists at
`paper_registry_current.md:6128`, which I verified. That is not the same proposition as *a citation
parenthetical is correctly classified as a co-mention finding*. The candidate's own routing bullet
gets it right; the "cleared" sentence clears a different claim than the one at issue. Non-blocking,
one sentence.

---

## 7 · F · TRANSPORT FINDINGS — the required regression case

**F-1 · Where the locator was correct: at the reading.** `PMID32000863.json`, 25 entries:

| Entry | Anchor | Proposition |
|---|---|---|
| `[0]` | *"Figure **7d**, image inspected"* | lithium suppressed PTZ seizures in all three genotypes |
| `[1]` | *"Figure **7b**, image inspected"* | ethosuximide **is** genotype-specific |
| `[22]` | *"Figure **7d**, image inspected at the native 1946×1627 pixels"* | the lithium experiment establishes no Wwox-specific rescue |

Confirmed against the primary (`PMID32000863_Cheng2020_PMC.xml`): the Results sentence places
lithium at Fig. 7d; the Fig. 7 legend places ethosuximide at 7b and the western blot at 7c.
**The reading was right.**

**F-2 · Where it became incorrect: at propagation into canonical.**
`claim_registry_current.md:300`, introduced by commit `419b680` (2026-08-10, `BATCH_20260810_005`).
The parenthetical **merged two manifest entries and kept the wrong one's figure number** — the
lithium proposition from entry `[0]` carried under entry `[1]`'s `Fig. 7b`. **One record copied
another**, which is the exact route the dispatch names.

**F-3 · The sentence carrying the defect diagnoses the defect class in its own final clause.**

> *"Il locator esisteva dal giorno della lettura e non era mai arrivato fin qui: è un difetto di
> propagazione, non di lettura."*

The batch that named *propagation, not reading* committed a propagation defect in the same
sentence. **READING FAILURE: none. TRANSPORT FAILURE: this.**

**F-4 · 🔴 Two canonical carriers, two different repair shapes.**

| Carrier | Form | Correct repair |
|---|---|---|
| `claim_registry_current.md:300` | **bundled** — one parenthetical, lithium + ethosuximide | split; `Fig. 7b` is **correct** for the ethosuximide clause. A bare swap **breaks** it. |
| `state_manifest_current.md:112` | **unbundled** — *"(PMID 32000863 Fig 7b, read from the image)"* | here a bare `7b → 7d` swap **is** correct |

POINTER-01 repairs the first and correctly declines the second, naming why: it is a historical
record of a completed batch on a surface writable outside `BATCH_COMMIT`, the lawful shape is a new
entry, and it needs Operator authorization. I add one fact the candidate does not: **the receipt
chain anchors its tail in that same file**, so an in-place edit there is not merely a governance
question.

**F-5 · Blast radius.** The defect is present on **every ref swept**, including `main` and
`development/main` — the public remote.

**F-6 · Which control failed: none of them looked.** No control binds a registry figure pointer to
the manifest locator it cites.

**F-7 · 🔴 A mechanical detector for this class is not available at the current schema — and I
demonstrated it rather than asserting it.** I wrote the obvious check (a registry sentence citing a
manifest and printing a figure pointer must print a pointer the manifest knows) and ran it against
the live tree:

```
sentences checked (cite a manifest + print a figure): 1
VERDICT: PASS
```

**It passes on the live defect**, because `Fig. 7b` *is* in the manifest — attached to a different
entry. My own first detector was a wrong-reason pass, which is the failure mode § 11 of the
dispatch asks about. Two further measurements bound the answer:

- The population is **1 line**. The registry is 709 lines; **4** print a figure pointer, **3** cite
  a manifest, **1** does both. A regression over a population of one is a change-detector, not an
  invariant. The other 3 figure pointers cite no source at all and are unverifiable by any
  mechanical means.
- The registry **never names a locator by identity**: `locator_fingerprint`, `LF-`, `entries[`,
  `verbatim_locators`, `locator_id` — **0 occurrences each**.

The machinery for the exact check already exists one layer over, in the DisMech sidecar
(`registry_anchor: claim_registry_current.md#CLAIM NNN|<field>|sent[n]`, `locator_fingerprint:
LF-95b20105106a`). **The repair is that the registry parenthetical carries the locator reference it
is reporting — one field, existing vocabulary, no new governance layer.** With it the check is
exact and needs no heuristic. Without it, any detector must infer the binding from words, which is
the operation Pathograph exists to refuse.

---

## 8 · G · PRIVACY FINDINGS

**G-1 · Clean — no new-artifact privacy regression.** Scanned every new durable artifact for
personal identifiers, contact strings, individual-level framing and clinical-relationship language:
**0 hits**. The human role is **Operator** in 7 of 14 new Orchestrator records and unnamed in the
rest, which satisfies the policy. No individual-level record was reintroduced. No historical
canonical artifact was rewritten to satisfy this check.

---

## 9 · H · WRONG-REASON FINDINGS

**H-1 · 🔴 The graph is correct here because it excludes the surface the defect lives on.**
`pathograph.py:52` declares `Summary`, `Clinical meaning` and `Evidence boundary` unscanned. The
defect is in `Evidence boundary`. Measured: **0** propositions carry `7b`/`7d` text; the 4
propositions carrying PMID 32000863 all draw **Figure 7d** — from the manifest. The exclusion is
well-reasoned and its effect is real: **the graph and the canonical registry now state different
figure numbers for the same claim, and nothing reconciles them.** Correct output, wrong reason.

**H-2 · 🔴 The same exclusion drops the qualification that prevents the causal overreach.** Zero
records in the DisMech sidecar derive from `Evidence boundary`; `genotipo-specifico` and `TUTTI E
TRE` are absent from the sidecar entirely. The fields that *do* reach it for CLAIM 016 are
`Summary`, `Meccanismo aggiunto`, `Clinical meaning`, `Transferability`, `PREMISE_TAG`. **The single
most load-bearing qualification on the claim — that the lithium experiment establishes no
WWOX-specific rescue — does not exist downstream in any form.** All 9 representation items that do
survive carry `representation_state: SCHEMA_LOSS`.

**H-3 · 🔴 The overreach is blocked — by a formatting property, and this is the smallest measured
blocker.** The lithium occurrence `OCC-0217fdd122a1` is `terminal_state: LINK_ROLE_NON_SUPPORTING`,
`locator_status: NOT_EXTRACTED`, `normalised_role: UNQUALIFIED_REFERENCE`. The link role is
`wikilink_only` because CLAIM 016's `Source` field reads:

```
**Source:** Cheng et al. 2020 · [[paper_registry_current#PAPER 056]] (Wang 2012 — …)
```

PAPER 019 **is** Cheng 2020 / PMID 32000863, and it **is** wikilinked from CLAIM 016 — in
`Evidence boundary` and in `Wikilinks`, **not in `Source`**. So the primary source of the claim is
classified a non-supporting cross-reference **because of where the author typed the wikilink.**

Repair that formatting — an obviously-correct, cosmetic-looking edit any reviewer would wave
through — and `claim_link_basis` becomes `source_field`, the link-role gate lifts, and the lithium
proposition needs only its locator (which the manifest has held since the day of the reading) to
become `ELIGIBLE_FOR_EXPORT` — **while its qualification still does not travel.** The ordering is
the whole finding.

**H-4 · What actually reaches downstream, enumerated.** 17 `ELIGIBLE_FOR_EXPORT`: 5 from PMID
35716775, 12 from PMID 22193544. **No lithium, seizure or PTZ proposition among them.** 3
`SOURCE_SUPPORT_NOT_FOUND`, 2 `LINK_ROLE_NON_SUPPORTING`.

**H-5 · Controls in the Pathograph suite: partial.** Positive and negative controls exist for
edge origination — `test_a_shared_pathway_never_creates_an_edge`,
`test_shared_evidence_is_a_review_candidate_not_an_edge`, and
`test_two_baseline_data_claims_do_not_become_a_direct_edge`, whose docstring is *"The inference
this tool exists to refuse."* They **do not** exist for the two invariants of § E-2. The suite
fails under mutation for the invariants it covers and does not for the two it does not.

**H-6 · The abundance/activation drift is real and I verified it at the primary.** Across the full
text: `activation` × 7, `abundance` × **0**, `elevated` × **0**. The abstract asserts *"a
significantly increased **activation** of GSK3β"*; the Fig. 7c legend asserts *"Increased
activation … as evidenced by dephosphorylation of GSK3β at Ser9."* CLAIM 016 asserts
`DATO (abbondanza, murino)` and *"GSK3β is elevated"*. **DRIFT-01 is correct on the text.** I did
not re-derive the densitometry values from the image; that half rests on manifest entry `[2]` and
is scoped accordingly.

---

## 10 · I · MINIMAL REQUIRED REPAIRS

No new architecture. Seven scoped acts, in this order.

| # | Repair | Closes | Size |
|---|---|---|---|
| **1** | Commit the 34 untracked pipeline artifacts, the 4 Pathograph files first | A-1 | a `git add` — not a layer |
| **2** | The two invariant regressions of § E-2, written so regeneration cannot make them pass | E-2 | 2 tests |
| **3** | Apply `CC-20260825-32000863-POINTER-01` as written | F-1…F-4 (carrier 1) | 1 parenthetical |
| **4** | A second candidate for `state_manifest_current.md:112` — **new entry, not in-place**; Operator-authorized; note the receipt-chain tail anchor | F-4 (carrier 2) | 1 entry |
| **5** | Carry the locator reference in the registry parenthetical, using the sidecar's existing vocabulary | F-7 | 1 field |
| **6** | **Before** repairing CLAIM 016's `Source` formatting, admit `Evidence boundary` to one machine reader (sidecar scan set or eligibility gate) | H-2 · H-3 | ordering + 1 field list |
| **7** | Run `benchmark_input_surface.py` freeze/parity on the next pilot pair | A-3 · C-1 | invoke what exists |

Repair **6 before its own prerequisite looks harmless** is the one an ordinary review would get
wrong. Two further one-line closures: § D-3 (declare the authority basis in the `lettore` record)
and § E-4 (narrow the "cleared" sentence to what was checked).

---

## 11 · FINAL QUESTION

> *Can LEGEND safely proceed from Scientist-produced evidence-bound graph contributions to
> Orchestrator integration without creating unsupported biology or losing provenance?*

**NO — on provenance. Not on biology.**

Unsupported biology is **not** being created, and that is measured, not assumed: 0 of 20 edges
typed, 0 of 39 scales annotated, 0 forbidden origination routes taken, 0 of 17 eligible downstream
propositions touching the overreach case. That half of the question answers **YES**, on the
surfaces named in § 0 and at the refs in § 0.

Provenance **is** being lost, at three measured points, and these are the smallest blockers:

1. **H-3 — the ordering hazard.** The downstream gate that currently blocks the lithium overreach
   is a `wikilink_only` classification produced by where an author typed a wikilink. A cosmetic
   repair removes it while the qualification still does not travel. **This is the smallest blocker
   and the most likely to be tripped by a well-intentioned edit.**
2. **H-2 — the qualification does not travel.** 0 sidecar records from `Evidence boundary`.
3. **B-1 — the producing actor is absent** from every record of the graph export.

Two further blockers are structural rather than provenance-losing: **E-2** (the typing invariants
undefended by any test, unrepaired since v1 against byte-identical objects) and **A-1** (34 of 35
pipeline artifacts outside every gate — including the regression that guards the graph).

**Safeguards demonstrated, with surface and ref.** Edge origination refuses all seven routes
(`pathograph_export.jsonl` @ digest `39e9a224…`, shared checkout `30cb4f3`). The DisMech boundary
blocks the overreach (`dismech_sidecar_016_024_035.jsonl`, same tree). No actor self-activated
(`lease_state.py`, 0 ACTIVE, all trees). Dispatch surfaces carry no conclusion-shaped prompt by
declared design (`SCIENTIST-FIRST-PILOT-EXECUTION-CONTRACT-001` § 396, `e4aa80c` + untracked). New
durable artifacts carry no personal identifier (all trees, § G).

**Proceed with preparation. Do not integrate until repairs 1–6 land.**

---

## 12 · HANDOFF

```
HANDOFF · MIRROR → ORCHESTRATOR (cc PLAN)
REVIEW_ID       PATHOGRAPH_PIPELINE_HOSTILE_REVIEW_MIRROR_v2
OBJECT          first-run pipeline: Pathograph layer · Plan lane classification + 3 commit
                candidates · two independent PMID 32000863 adjudications · DisMech boundary
VERDICT         REFINED
OBSERVATION_SCOPE  2026-08-25T13:32:41Z · mirror c7e8d6e · shared 30cb4f3 · plan e4aa80c ·
                readers 9b0cf47 / 2261a15 / 788c357 · orchestrator 1e2fabd · all refs swept
                with positive control

BLOCKING BEFORE INTEGRATION
  H-3  downstream gate rests on wikilink placement; repair order is load-bearing
  H-2  Evidence boundary reaches no machine reader (0 sidecar records)
  B-1  producing actor absent from every export record
  E-2  both v1 blocking findings unrepaired against byte-identical objects
  A-1  34 of 35 pipeline artifacts outside every gate (denominator re-derived, § A-1)

NOT BLOCKING, OWED
  D-3  authority basis undeclared in one reader record
  E-4  one clearance sentence broader than what was checked
  C-1  independence attested, never instrumented — run the freeze on the next pair
  B-2  panel_text_relation dropped; 26/265 candidates affected

ENDORSED AS WRITTEN
  CC-20260825-32000863-POINTER-01        (verified against manifest entries 0/1/22 and primary)
  CC-20260825-GRAPH-MATERIALIZATION-01   (rendering-only; 10+1+1=12 verified; see E-4)
  CC-20260825-CLAIM016-DRIFT-01          (text verified: activation×7, abundance×0, elevated×0;
                                          densitometry half not independently re-derived)

MIRROR ASSERTS NO SCIENTIFIC VERDICT. No biological relation was adjudicated.
No forced consensus. No personal identifiers. Nothing canonical was mutated by this review.
```
