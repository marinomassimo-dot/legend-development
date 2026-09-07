---
artifact: MIRROR hostile review (Annex C.2) — Orchestrator Pathograph layer
review_id: PATHOGRAPH_HOSTILE_REVIEW_MIRROR_v1
object: uncommitted Pathograph change set — 4 new + 5 modified files in the SHARED checkout
  `<REPO_ROOT>`, branch `legend-operating-convention-v1` @ `30cb4f3`
level: R4 (METHOD — Mirror; C.1 floor for a methodology-changing inferential process; C.4 object
  class SYSTEM → Mirror)
reviewer: mirror
author: orchestrator
adjudicator: operator — none granted or implied here
date: 2026-08-25
verdict: REFINED — see §2 for REFINED_FORMULATION
governance_loaded: 3.1.1
scope_note: every number below was produced by executing the code, never by reading the report.
  Orchestrator's tree was not modified: file list and both output digests are identical before
  and after this review (§1.5).
---

# The boundary holds in the artifact and is not defended in the tests

---

## 1 · REVIEW SURFACE

### 1.1 Where the change set actually is — and where it is not

Orchestrator's dispatch implies an Orchestrator worktree. **It is not there.**

| Searched | Pathograph files found |
|---|---:|
| `.claude/worktrees/mirror` (my own) | 0 |
| `.claude/worktrees/orchestrator` | **0** |
| `.claude/worktrees/{lettore, lettore-b, lettore-c, evidence-index}` | 0 |
| the four `legend-codex-*` worktrees | 0 |
| every `/private/tmp/claude-501` scratchpad worktree | 0 |
| every committed ref (`refs/heads` + `refs/remotes`) | **0** |
| **`<REPO_ROOT>` — the SHARED checkout** | **4** |

Two facts follow, and both are review surface rather than opinion:

- The work is **uncommitted in the shared checkout**, on branch
  `legend-operating-convention-v1` — not on `orchestrator`, and not on any branch named for
  this task. It exists in exactly one tree and in no git object.
- `git ls-tree` over every ref returns nothing for `pathograph`. There is **no base ref for a
  diff of the new files**; the only diffable objects are the five modified ones.

The two `pathograph*` hits under `~/Desktop/Claude Workspace/_external_repos/medical_ai/monarch-app/`
are an unrelated Monarch API surface and are not part of this change set.

### 1.2 Identity of the reviewed tree

| | |
|---|---|
| Worktree | `<REPO_ROOT>` (shared checkout) |
| Branch | `legend-operating-convention-v1` |
| HEAD | `30cb4f3fd700e2aaf6b608e363438f883ddc3760` · 2026-08-23 18:40 |
| Base ref for the 5 modified files | `30cb4f3` |
| Base ref for the 4 new files | **none — untracked, never committed** |
| My own worktree | `.claude/worktrees/mirror`, branch `mirror`, HEAD `c7e8d6e` (0 behind `main`) |

### 1.3 Exact files inspected

**New (untracked) — 4**

| File | Lines |
|---|---:|
| `framework/scripts/pathograph.py` | 1 363 |
| `framework/scripts/test_pathograph.py` | 458 |
| `disease-models/wwox/analysis/pathograph_inventory.md` | 333 |
| `disease-models/wwox/analysis/data/pathograph_export.jsonl` | 371 |

**Modified (tracked) — 5**, 24 insertions, 0 deletions, verified line by line

| File | Change |
|---|---|
| `scripts/run_release_regressions.py` | +1 — `test_pathograph.py` added to `TESTS` |
| `scripts/test_cli_smoke.py` | +1 — `pathograph.py` added to `PUBLIC_CLIS` |
| `framework/protocols/prompt_batch_commit.md` | +3 — regeneration added to the generated-surface phase |
| `disease-models/wwox/analysis/README.md` | +18 — the layer described |
| `DATA_SOURCES.md` | +1 — export row, licence and verbatim-extract note |

### 1.4 Every reported figure re-derived by execution

```
python3 framework/scripts/pathograph.py --root <shared> --disease wwox
```

| Orchestrator reported | I measured | |
|---|---|:--:|
| 39 claim nodes | 39 | ✅ |
| 41 claim→claim wikilink occurrences | 41 | ✅ |
| 30 distinct directed links | 30 | ✅ |
| 20 effective unoriented edges | 20 | ✅ |
| 0/20 causally typed | 0 of 20 | ✅ |
| 0/39 biological-scale annotations | 0 of 39 | ✅ |
| 1080 propositions scanned | 1080 | ✅ |
| 302 candidates | 302 | ✅ |
| 18/39 relation-bearing claim titles | 18 of 39 | ✅ |
| 30 regressions | 30 tests, `Ran 30 tests … OK` | ✅ |
| 4 new + 5 modified, uncommitted | 4 + 5, uncommitted | ✅ |
| three mutation controls | reproduced; all three kill (§6 of ATTACK 6) | ✅ |

`--verify` against the shipped surfaces: **`VERIFY: CURRENT`**.

### 1.5 This review modified nothing

`git status --porcelain` on the shared checkout is byte-identical before and after. Both
generated surfaces retain their pre-review digests:

```
bbc09af474acc71f6549be7d296c1e2b94db04673def1a6c4a66a9baa231a032  pathograph_inventory.md
39e9a224030d13b350022c696d4f753d855c4859aa00bb7a0320f4e95e361ebd  pathograph_export.jsonl
```

Every mutation, fixture and shadow regeneration ran in
`…/scratchpad/{pgmut, pgshadow, pgshadow2}`, against read-only symlinks to the real registries.

---

## 2 · VERDICT

### STEELMAN (C.2 — mandatory, before the objections)

This is a careful piece of work and the restraint is real, not decorative. Five independent
things are right:

1. **The load-bearing refusal is implemented where it matters.** `_build_edges` types an edge
   from `types[0] if len(types) == 1 else UNTYPED` and from nothing else. Every path that could
   have derived a type — shared pathway, shared paper, both endpoints `DATO`, reciprocity,
   connective class — is absent from the code, and four of those five are held down by named
   regressions. `test_two_baseline_data_claims_do_not_become_a_direct_edge` carries the
   docstring *"The inference this tool exists to refuse."*
2. **The three denominators are kept apart and printed.** 41, 30 and 20 are reported as three
   different measures with a comment saying they are "easy to quote as one another", and the
   inventory prints all three. This is the discipline the corpus keeps failing at elsewhere.
3. **The lexicon's known defects are declared rather than discovered later.** Six ambiguous
   bare forms produced 162 of 302 first-run candidates; they were kept, marked
   `AMBIGUOUS_BARE_FORM` and sorted to the back — because deleting them would have taken
   *"WWOX loss reduced myelination"* with them. Quarantine over deletion is the right call and
   the reason is written down.
4. **The candidate record refuses to resolve endpoints.** Every one of 302 carries
   `endpoints_resolved: false`, and the split is described in the record itself as a split on a
   string.
5. **`biological_scale` is emitted as `NOT_ANNOTATED` on all 39 nodes** with the comment *"a
   scale guessed from a pathway label would be an assertion about biology wearing a schema's
   clothes."* A weaker tool would have inferred `MOLECULAR` from a `P5` pathway string. I
   mutated it to do exactly that and a named regression killed it.

The central invariant, tested against the shipped artifact, **holds**. I could not find one
operation in the 1 363 lines that turns repository text into a stronger scientific proposition
than the repository makes.

### KEY OBJECTION

The invariant holds **as a property of the current bytes**, not as a property the suite
defends. The one clause the whole layer rests on — *a relation type is never inferred from
grammar* — is stated in the docstring, stated in the inventory, stated in the README, and
enforced by **no test**. I added that inference and all 30 tests went green (§6).

### VERDICT: `REFINED`

`REFINED_FORMULATION` — the invariant as submitted:

> *Pathograph is a mechanical projection of relationships already present in LEGEND and does not
> originate scientific causal meaning.*

as it survives review:

> **Pathograph, as it currently stands, is a mechanical projection that originates no causal
> meaning — verified by execution against the live registries, by eight adversarial fixtures and
> by fifteen mutations. The property is a fact about this revision, not an invariant the test
> suite protects: the prohibition on inferring a relation type from grammar, and the prohibition
> on discharging a Scientist typing obligation without an annotation, are both undefended, and
> the golden-file regression that appears to defend them is defeated by the documented
> regeneration step.**

`REVIEWER_CONFIDENCE` — high on the mechanical findings (all executed, all reproducible); high
on the two blocking findings (demonstrated end to end, §3); medium on the completeness of my
own attack surface: I enumerated eleven transformations and mutated fifteen points, which is not
proof that a twelfth does not exist.

`RESIDUAL_UNCERTAINTY` — I did not review the 1 080 scanned propositions individually, and I did
not adjudicate whether any of the 302 candidates is scientifically true. Both are out of scope
by §7 of the assignment and by C.4.

`WHAT_WOULD_CHANGE_MY_MIND` — a regression that fails when a `relation_type`, an
`inferred_relation_type`, or any equivalent field appears on any record from a source other than
a `(relation: …)` annotation, **written so that regenerating the surfaces cannot make it pass**.
That single test moves this from `REFINED` to `CONFIRMED`.

---

## 3 · BLOCKING FINDINGS

### B-1 · The prohibition on inferring a relation type from grammar is enforced by no test, and regeneration defeats the test that appears to enforce it

**The claim under attack.** `pathograph.py` states, twice:

> *"A class is a property of the **word**, not a verdict about the relationship: an `ASSOCIATIVE`
> connective does not make an edge `ASSOCIATED`, and **nothing downstream is allowed to read it
> that way**."*

Nothing enforces the clause after the comma.

**Demonstration.** I applied one mutation (`M11`) to a scratch copy — three lines, inside
`_emit_candidate`:

```python
"connective_class": primary.klass,
"inferred_relation_type": ("DIRECT" if primary.klass in ("ARROW", "CAUSAL")
                          else "ASSOCIATED"),
```

This is precisely the operation the assignment forbids — *infer causality from grammar*. Result:

| Step | Outcome |
|---|---|
| Run the 29 invariant tests (golden-file test skipped) | **all pass** |
| Run all 30 tests, surfaces not yet regenerated | `test_the_generated_surfaces_have_not_drifted` fails |
| **Regenerate the surfaces** — one command, and a *mandatory* phase of `prompt_batch_commit.md` | — |
| `--verify` after regeneration | **`VERIFY: CURRENT`** |
| Run all 30 tests again | **all pass** |
| What the export now asserts | **255 × `"inferred_relation_type": "DIRECT"`**, 47 × `"ASSOCIATED"` |

255 causal type assertions manufactured from the connective class alone, shipped in a
machine-readable export, with a green suite and a clean `--verify`.

**Why the golden-file test cannot be the defence.** `test_the_generated_surfaces_have_not_drifted`
is a change-detector over live registry data, not an invariant. It fails on *any* behavioural
change, including every legitimate one, and the documented remedy for a legitimate change is to
regenerate — which is also the remedy for an illegitimate one. A test whose failure is cleared by
the same gesture in both cases distinguishes nothing.

**Correction required.** An invariant regression, independent of the generated surfaces, asserting
that no exported record carries a relation type whose basis is anything other than
`DECLARED_ANNOTATION`. Suggested shape (Orchestrator's to write, not mine):

```
for record in export:
    for key, value in record.items():
        if "relation_type" in key or value in RELATION_VOCABULARY:
            assert record.get("relation_type_basis") == "DECLARED_ANNOTATION"
```

### B-2 · A Scientist typing obligation can be discharged without an annotation, and no test fails

**Demonstration.** Mutation `M14` changes one condition in `_build_edges`:

```python
"review_state": ("TYPED" if (len(directions) == 2
                             or (len(types) == 1 and types[0] != UNTYPED))
                 else "AWAITING_SCIENTIST_TYPING"),
```

Reciprocity alone now marks the edge `TYPED`. **The suite passes** (29 invariant tests; the
golden-file test clears on regeneration exactly as in B-1).

**Consequence on live data.** 10 of the 20 edges are reciprocal. All 10 would report
`review_state: TYPED` while still carrying `relation_type: UNTYPED` — an internally contradictory
record — and all 10 would drop out of section **B · TYPE** of the Scientist review queue. Half the
edges would silently stop asking for the reading that types them.

This is not a causal-meaning leak; it is worse in one specific respect — it removes the request
for the judgement rather than answering it wrongly, and a removed request leaves no trace to
audit.

**Correction required.** An invariant tying the two fields: `review_state == "TYPED"` if and only
if `relation_type != UNTYPED`.

---

## 4 · NON-BLOCKING FINDINGS

**N-1 · The 41-occurrence layer is not exported.** `assemble()` emits nodes, edges,
`claim_to_record_links`, candidates, findings and losses. `self.links` — the 41 raw occurrences —
is never serialised. The export contains `"kind": "claim_link"` **zero** times. The number 41
survives only as the integer `coverage.claim_link_occurrences`. Verified losslessness on today's
data (N-2) is therefore not *checkable* from the export by a future reader.

**N-2 · The Scientist's stated rationale is discarded.** `_read_links` captures
`relation_annotation` (the full parenthetical) and `_build_edges` never copies it. Demonstrated:
an edge annotated `(relation: DIRECT — the rescue measures both arms)` emits `relation_type:
DIRECT` and the string *"the rescue measures both arms"* appears nowhere in the edge record. Today
all 41 annotations are empty, so nothing is lost yet; the field is lost by construction the moment
typing begins — which is the moment this layer is for.

**N-3 · An edge cannot carry one relation type per direction.** Demonstrated on fixtures:

| Fixture | Result |
|---|---|
| A→B `DIRECT`, B→A `ASSOCIATED` | `relation_type: UNTYPED`; **both declared types discarded**; loss `RELATION_TYPE_CONFLICT` |
| A→B `DIRECT`, B→A unannotated | `relation_type: UNTYPED`; the **declared** `DIRECT` lost; loss text says *"the two directions declare different types: DIRECT, UNTYPED"* |

The second is mislabelled: an annotation on one side and none on the other is an **asymmetry**,
not a conflict, and calling it a conflict will read to a Scientist as a disagreement that does not
exist. Both cases fail toward `UNTYPED`, which is the safe direction — this is why it is
non-blocking.

**N-4 · An internally false field pair.** In fixture A above the edge emits
`relation_type: UNTYPED` together with `relation_type_basis: DECLARED_ANNOTATION` — literally
asserting that the declared annotation was `UNTYPED`, which no annotation said. `bases` is
collapsed with `sorted({...})` independently of `types`, so the two fields can disagree.

**N-5 · The locator's own evidence-quality verdict does not travel.** A candidate's `evidence`
carries `pmid · receipt · surface · artifact · anchor · snippet`. It does **not** carry
`panel_text_relation`, nor the coupled `contradicts` / `qualifies` pointers. Measured on the live
corpus:

| `panel_text_relation` of the source locator | candidates |
|---|---:|
| `text_only` | 112 |
| `panel_only` | 45 |
| `text_confirmed_by_panel` | 44 |
| *(absent — legacy)* | 38 |
| **`text_contradicted_by_panel`** | **13** |
| **`panel_qualifies_text`** | **13** |

**26 of 265 locator-backed candidates (9.8%) descend from a locator where LEGEND itself recorded
that the panel disagrees with or qualifies the text.** `grep panel_text_relation` on the shipped
export returns **0**. Those 26 are indistinguishable, in the export, from the 44 the panel
confirmed. This is the corpus's single most developed evidence-quality signal and the layer drops
it.

**N-6 · A citation parenthetical is classified as a stated relationship, in the highest-confidence
tier.** The only `WORKING_MODEL_COMENTION` in the corpus is:

> `*(CLAIM 025 / paper 191; CLAIM 026 / PAPER 032, Hussain 2018.)*`

That is two source pointers for two halves of a paragraph — not a relationship between CLAIM 025
and CLAIM 026. `_working_model_comentions` splits on `(?<=[.!?])\s+`, so the parenthetical is one
"sentence" naming both. `WORKING_MODEL_COMENTION` sits in the `confirming` tuple, so both claims
are promoted to **`ANNOTATION_GAP_CONFIRMED`** — the tier the code defines as *"a relationship
this repository already states and has not annotated — a gap, and a confirmed one."*

CLAIM 025 independently earns the verdict (it also carries `UNLINKED_PROSE_MENTION`). **CLAIM 026's
`ANNOTATION_GAP_CONFIRMED` rests entirely on this false positive** — 1 of the 2 confirmed gaps.
This is the same class the `HISTORY_ROW` / `CHANGELOG_FIELD` / `BATCH_ID` exclusion was built to
remove (*"20 of 21 co-mentions came from changelog prose"*); one survivor of a different shape —
a citation parenthetical inside a body paragraph — remains.

**N-7 · `--verify` conflates stale content with a different invocation.** `render_markdown`
embeds `regeneration_command(disease, out, export)` in the file. Regenerating with `--out` alone
and then verifying with `--out --export` reports:

```
DRIFT markdown: … has drifted from its sources
```

The sources are current. `diff` of the two outputs shows the **only** difference is the embedded
command line. The drift signal is therefore not a pure function of the inputs, and its message
names the wrong cause.

**N-8 · A valid-JSON non-object manifest crashes instead of becoming a named loss.**
`_manifest_candidates` catches `json.JSONDecodeError` only. A manifest whose top level is a
string, an array or `null` raises an uncaught `AttributeError: 'str' object has no attribute
'get'` — verified for all three. It fails **closed** (the run aborts; no wrong data is emitted),
which is why this is non-blocking, but it is the one loss class the file's own *"losses are
named"* discipline does not name.

**N-9 · "Losses: None" is unqualified at the point it is printed.** §6 of the inventory reads
*"None. Every scanned proposition was either emitted as a candidate or carried no connective."*
That sentence is true of the **candidate** population. The 11 collapsed link occurrences (N-1) are
not `lose()` events at all, so the link population has no loss ledger. The candidate dedup path
*does* call `lose("CANDIDATE_DUPLICATE", …)`; the two dedup paths have inconsistent accounting
discipline, and the report states the stronger of the two without its denominator.

**N-10 · Copyright surface, for the operator's own read.** The export ships verbatim third-party
text as `evidence.snippet`:

| | |
|---|---:|
| snippets | 265 |
| characters of third-party text | 53 013 |
| distinct source papers | 60 |
| longest single snippet | 878 chars |
| from the three **non-OA, page-adjudicated** articles | **14** (PMID 16061658 ×2, 17803050 ×3, 21212533 ×9) |

`DATA_SOURCES.md` declares this correctly and calls the extracts minimal and attributed. I flag it
only because `gold_is_in_the_details.md` closes with *"the privacy gate does not and cannot cover
this… copyright is outside its domain… It is the one judgement no gate here makes for you, and
publishing is not reversible."* This is not a defect in the change set; it is a decision the
change set newly requires before any public push.

**N-11 · The change set lives uncommitted in the shared checkout.** Branch
`legend-operating-convention-v1`, not `orchestrator`; no git object anywhere. The shared checkout
is the tree every other actor's `files/` and re-validation depend on. Until it is committed there
is no `BASE_HEAD`, no content hash, nothing another actor can review at a ref, and one `git
checkout` in that tree ends the work. This review's surface is therefore a filesystem state, and
I recorded its digests (§1.5) because that is the only anchor available.

**N-12 · The three mutation controls leave no artifact.** No mutation record, log or comment
exists anywhere in the change set — `grep -i mutation` over `pathograph.py`,
`test_pathograph.py`, the inventory and the README returns nothing. I reproduced all three
independently and **all three kill** (§ATTACK 6), so the claim is true; it is simply not
verifiable from the repository by anyone who does not redo the work.

---

## 5 · ATTACKS THAT SURVIVED

Negative results, each with the tested surface and its control.

**ATTACK 1 — hidden scientific inference, against the shipped code.** *No leak found.*
Surface: all eleven transformations named in the assignment — candidate extraction, lexical
relation detection, wikilink interpretation, directionality, edge collapsing, deduplication,
proposition ranking, node normalization, composite-claim handling, relation typing, isolate
classification. Control: the baseline suite green on an unmodified scratch copy (30/30) plus the
eight fixtures below. The six forbidden operations are individually absent: no cause/effect
decomposition, no causality from grammar *in the shipped bytes*, no `DIRECT` from two `DATO`
endpoints, no direction from a navigational wikilink, no association→mechanism promotion, no
primary-science adjudication. The undefended-ness of two of these prohibitions is B-1/B-2; their
observance today is this negative result.

**ATTACK 2 — eight adversarial cases.** Seven `HELD`, one `PARTIAL`. Fixtures built with the
change set's own `test_pathograph.build()` helpers.

| # | Case | Result |
|---|---|---|
| 1 | Two `DATO` claims linked, no causal relation demonstrated | **HELD** — `UNTYPED` / `NO_DECLARED_RELATION_ANNOTATION` / `AWAITING_SCIENTIST_TYPING` |
| 2 | Relation-bearing title, body demonstrates nothing | **HELD** — 0 edges; `SELF_RELATIONAL_TITLE`; verdict `REVIEW_MATERIAL_PRESENT`, not a gap |
| 3 | Navigational wikilink (`full_text_queue`, `paper_registry`) | **HELD** — 0 claim edges; recorded as `claim_to_record_link` |
| 4 | Reciprocal wikilinks | **HELD** — `reciprocal: true`, both directions kept, still `UNTYPED` |
| 5 | `reduced` used attributively | **HELD** — `AMBIGUOUS_BARE_FORM`, priority `LOW`, `degenerate: true` |
| 6 | `rescue` where WT and mutant are both affected | **HELD** — emitted as a candidate only; no genotype-specificity asserted in either direction |
| 7 | Author interpretation; panel contradicts the text | **PARTIAL** — proposition, verbatim, receipt and anchor survive; `panel_text_relation` and the `contradicts` pointer do not → **N-5** |
| 8 | Composite claim: cause + relation + effect | **HELD** — both connectives listed in `connectives_all`, one used only as a split point, `endpoints_resolved: false`, 0 edges, reported for `DECOMPOSE` |

**ATTACK 5 — generated view.** *Survived on every axis except N-7.*
Determinism: two independent `--json` runs byte-identical (`sha256 333dbb0d6d7f3986…`, twice).
Manual edit: appending one HTML comment to the inventory → `VERIFY: DRIFT`, exit 1. `--verify`
bypass: invoking `--verify` with neither `--out` nor `--export` exits **2**, held by
`test_verify_without_a_target_refuses_rather_than_passing`. Source-of-truth separation: both
surfaces carry a *"Generated file — do not edit by hand"* header, the regeneration command, and
an input digest over 67 files; `test_a_plain_run_writes_nothing` asserts the registries are
byte-identical after a run, and my own before/after digests (§1.5) confirm it at review scale.
Schema drift: `schema_version: 1` is emitted on the manifest line and on the assembled object.

**ATTACK 6 — Orchestrator's three mutation claims, reproduced.** All three kill, and all three
kill on an **invariant** test rather than only on the golden file:

| Mutation | Killed by |
|---|---|
| 1 · inferential typifier (`DIRECT` from two `DATO` endpoints) | `test_two_baseline_data_claims_do_not_become_a_direct_edge` + 2 more |
| 2 · changelog exclusion removed | `test_the_working_model_version_history_is_not_a_relationship` |
| 3 · ambiguous-form quarantine removed | `test_an_ambiguous_bare_form_is_quarantined_not_deleted` + 1 more |

**Nine further mutations I introduced.** Run twice — once against all 30 tests, once with the
golden-file test neutralised, to separate invariant coverage from change detection.

| Mutation | vs 30 tests | vs 29 invariant tests |
|---|---|---|
| `M4` candidate declares `endpoints_resolved: true` | killed | **killed** (`test_a_candidate_never_claims_resolved_endpoints`) |
| `M5` declared link direction inverted | killed | **killed** (`test_a_one_way_link_is_reported…`) |
| `M6` `lose()` silenced | killed | **killed** (`test_an_unrecognised_type_is_a_named_loss_not_a_guess`) |
| `M9` `biological_scale` guessed from pathway | killed | **killed** (`test_no_node_carries_an_invented_biological_scale`) |
| `M10` shared evidence promoted to a typed edge | killed | **killed** (3 tests) |
| `M13` relation vocabulary gate removed | killed | **killed** (`test_an_unrecognised_type_is_a_named_loss_not_a_guess`) |
| `M15` all `UNTYPED` edges relabelled `ASSOCIATED` | killed | **killed** (3 tests) |
| `M11` relation type inferred from connective class | killed *(golden file only)* | **SURVIVED** → **B-1** |
| `M14` reciprocity marks the edge `TYPED` | killed *(golden file only)* | **SURVIVED** → **B-2** |
| `M8` `claim_to_record_links` widened to paper links | killed *(golden file only)* | **SURVIVED** — minor: the `claim_to_record_link` population has no invariant test. It creates no claim edge, so it is not a causal leak. |

**A methodological caution I owe this review.** A tenth mutation — widening `CLAIM_FIELDS` to
include `Summary` and `Clinical meaning` — reported `SURVIVED` and I nearly filed it as a finding.
It is an **equivalent mutant**: `_build_candidates` reads only `Title`, so the widened allow-list
changes no output. Diff of the full report before and after: empty. It is recorded here as a
non-finding so the A/B/C-style comparison of this review can tell a real survivor from an artefact
of my harness.

**ATTACK 7 — Scientist boundary.** *Survived.* The `--queue` output hands the Scientist four
buckets — `A · ANNOTATE`, `B · TYPE`, `C · DECOMPOSE`, `D · REVIEW` — and answers none of them.
Section B lists shared evidential papers as *context for a reading* (`review_packet`), which is
the one place a weaker tool would have derived a type; it does not. All six items named in the
assignment remain open questions in the artifact (§8).

---

## 6 · INFORMATION-LOSS AUDIT

### 41 → 30 : eleven duplicate occurrences

Collapsed by `pairs.setdefault(key, []).append(link)` keyed on the sorted endpoint pair, then
`sorted({...})` over directions. I enumerated all eleven:

| Direction | × | Field(s) | Annotation(s) |
|---|---:|---|---|
| CLAIM 009 → 034 | 2 | `⚠️ Counter-directional evidence …` (same both) | empty, empty |
| CLAIM 016 → 035 | 2 | `Meccanismo aggiunto …` (same both) | empty, empty |
| CLAIM 019 → 032 | 2 | `Source` (same both) | empty, empty |
| CLAIM 019 → 030 | 2 | `Source` (same both) | empty, empty |
| CLAIM 032 → 031 | 2 | `Clinical meaning` (same both) | empty, empty |
| CLAIM 033 → 030 | 2 | `Clinical meaning` (same both) | empty, empty |
| CLAIM 034 → 009 | 2 | `Summary` (same both) | empty, empty |
| CLAIM 034 → 028 | 2 | `Clinical meaning` (same both) | empty, empty |
| CLAIM 035 → 030 | 2 | `Clinical meaning` (same both) | empty, empty |
| CLAIM 036 → 005 | 2 | `Evidence boundary` (same both) | empty, empty |
| CLAIM 038 → 036 | 2 | `Summary` (same both) | empty, empty |

**Lost: nothing, on this corpus.** Every duplicate shares its field and its (empty) annotation,
so the eleven collapses are exact-duplicate removals. `41 − 11 = 30` ✅

**But the losslessness is a property of today's data, not of the design.** `declaring_fields` is a
`sorted(set(...))` computed independently of `directions_declared`. Two occurrences of the same
direction sitting in *different* fields would yield two fields and one direction with no pairing
between them; two directions across two fields would give an unresolvable 2×2. And no `lose()`
event is recorded for any of the eleven — see N-9.

### 30 → 20 : ten reciprocal pairs

| | |
|---|---|
| Reciprocal edges | **10**, enumerated: (001,031) (003,004) (005,037) (009,034) (016,035) (019,032) (019,030) (036,038) (037,038) (037,039) |
| Both directions preserved? | **yes** — `directions_declared` carries both strings, and `reciprocal: true` |
| One-way edges | 10, listed in §4.1 of the inventory under neutral column headings *Declared / Not declared* |

`30 − 10 = 20` ✅

### What survives each reduction

| Property | 41 | 30 | 20 | in the export |
|---|:--:|:--:|:--:|:--:|
| endpoints | ✅ | ✅ | ✅ | ✅ |
| direction | ✅ | ✅ | ✅ as a set | ✅ |
| declaring field | ✅ | ✅ | ✅ as a set | ✅ |
| **occurrence identity** | ✅ | ✗ | ✗ | ✗ |
| **occurrence↔field pairing** | ✅ | ✗ | ✗ | ✗ |
| **raw annotation text** | ✅ | ✗ | ✗ | ✗ |
| ambiguity between two directions | ✅ | ✅ | ✅ | ✅ |
| reversibility to the source line | ✅ | ✗ | ✗ | ✗ |

**Verdict on ATTACK 3.** *A cleaner graph was not purchased by erasing disagreement.* Both
reciprocity and one-way asymmetry survive intact and are reported as findings in their own right.
What is not traceable is the **occurrence** layer: the 41 exist as an integer and nothing else
(N-1), and the annotation text is dropped by construction (N-2).

### Candidate population — the one accounting identity that is asserted

`assemble()` raises `AssertionError` unless
`emitted + no-connective + (PROPOSITION_EMPTY | CANDIDATE_DUPLICATE) == scanned`. It holds on the
live corpus (1 080 scanned, 302 emitted, 0 losses) and is held by
`test_the_accounting_balances_on_the_real_registries`. This is the strongest single guarantee in
the change set — and note that it covers the **candidate** population only, not the link
population.

---

## 7 · PROVENANCE AUDIT

For each exported object, can a future Scientist reach the repository object that caused it?

| Exported record | n | Traceable to its cause? |
|---|---:|---|
| `derivation_manifest` | 1 | ✅ 67 input paths + per-file SHA-256 + a combined digest (`736b51ed6003fef5`), plus the full lexicon and both vocabularies inline |
| `claim_node` | 39 | ✅ `id` is the registry heading; every field is an allow-listed declared field; `mirror_title` names the second wording |
| `claim_edge` | 20 | ⚠️ endpoints, directions and fields yes; **the individual occurrence and its annotation, no** (N-1, N-2) |
| `claim_to_record_link` | 8 | ✅ source claim + registry + record id |
| `relational_proposition` | 302 | ⚠️ see below |
| `findings` | 1 | ✅ every entry names its claim id(s) |
| `loss` | 0 | — none on this run |

### Candidate provenance, against the assignment's checklist

Tested on a live record (`RPC-16c42131131a`, PMID 17360458):

| Recoverable? | |
|---|---|
| original claim(s) | ✅ `bound_claims: ["CLAIM 032", "CLAIM 036"]` — **but see the caveat below** |
| original proposition | ✅ `text`, verbatim, plus `source_ref` → `…/PMID17360458.json\|entries[0]` |
| source paper | ✅ `evidence.pmid` |
| receipt status | ✅ `evidence.receipt: FTR-20260811-17360458-01` |
| locator status | ✅ `evidence.surface`, `evidence.artifact`, `evidence.anchor` |
| verbatim status | ✅ `evidence.snippet` — the quote behind the proposition |
| **figure/panel evidence** | ❌ `panel_text_relation`, `contradicts`, `qualifies`, `cited_panel_check` — **none carried** (N-5) |
| reason it entered the queue | ✅ `connective`, `connective_class`, `connectives_all`, `morphology`, `review_priority` |

**Caveat on `bound_claims`.** The binding is computed in `_claims_by_pmid` from *claims whose
evidential papers carry this PMID* — a **paper-level** association, not evidence that this
proposition supports those claims. The field name reads as an assertion of support. The inventory
qualifies the population honestly (*"Most locator-backed propositions belong to papers that no
claim declares as a source… the report says how many are in that state rather than quietly binding
them to the nearest claim"* — 109 of 265 bound), and the record is `AWAITING_SCIENTIST_REVIEW`, so
nothing downstream is licensed to read it as support. The naming is the only exposure, and it is
non-blocking.

**Missing evidence must not become invisible — the assignment's test.** It mostly passes: absent
annotations are emitted as `NOT_ANNOTATED`, absent types as `UNTYPED` with
`NO_DECLARED_RELATION_ANNOTATION`, absent scales as `NOT_ANNOTATED` with the vocabulary printed
beside the count, and unbound candidates counted rather than attached. **It fails in exactly one
place: N-5.** A locator whose panel contradicts its text becomes, in the export, a candidate
indistinguishable from one the panel confirmed. That is missing evidence made invisible.

---

## 8 · SCIENTIST-DEPENDENT ITEMS

Everything below I deliberately did **not** adjudicate. Mirror's object is the process (C.4); the
assignment's ATTACK 7 forbids it; and each of these is a reading against evidence.

| Item | Where it surfaces | Why I refused |
|---|---|---|
| Decomposition of the 18 relation-bearing claim titles | queue `C · DECOMPOSE`; `findings.self_relational_nodes` | Splitting *"Neuronal WWOX deletion induces non-cell-autonomous hypomyelination"* into two entities and a typed relation **decides which half is the cause** |
| Causal direction where not explicitly established | the 10 one-way edges; `asymmetric_links` | A directed citation is legitimately asymmetric; whether the reverse *should* exist is a reading |
| `DIRECT` vs `INDIRECT_UNKNOWN_INTERMEDIATES` | all 20 edges, `AWAITING_SCIENTIST_TYPING` | Requires the intermediate to have been measured — `MECHANISM_DIRECTNESS_GATE` |
| Whether a proposition is experimentally demonstrated | all 302 candidates | The proposition may be the authors' conclusion; the manifest types the locator, not the assertion |
| Reconciling observation with author interpretation | adversarial case 7; the 26 candidates of N-5 | This is precisely `text_contradicted_by_panel`, and it is Scientist adjudication |
| Whether a rescue is disease/genotype-specific | adversarial case 6; CLAIM 004, CLAIM 011 titles carrying `rescue` | Requires reading whether WT and mutant both moved |
| Whether the CLAIM 025 ↔ CLAIM 026 parenthetical states a relation | N-6 | I established the classifier's **mechanism** is a sentence-split artefact; whether a relation nonetheless exists between those claims is not mine to answer |
| Whether any of the 302 candidates is true | the whole candidate population | Out of scope by §7 |

I also record one dependency without resolving it: **N-5 makes the fifth row above harder than it
needs to be.** A Scientist reviewing the 26 affected candidates must reopen each manifest to learn
that LEGEND already recorded a panel/text disagreement on that very locator. That is a process
finding; the biology stays theirs.

---

## 9 · INTEGRATION RECOMMENDATION

### **SAFE AFTER SPECIFIED CORRECTIONS**

The layer does what it says. I attacked it fifteen ways and the shipped artifact never once
turned repository text into a stronger scientific proposition than the repository makes. The
restraint is genuine, it is written down, and thirteen of fifteen mutations die on named invariant
regressions.

It is not yet safe to integrate as *infrastructure* — meaning: as something that will be
maintained by future edits — because the two prohibitions that carry the whole boundary are
undefended, and the test that appears to defend them is cleared by the documented regeneration
step. A layer whose correctness is a property of the current bytes rather than of its suite will
drift the first time someone improves it.

**Required before integration**

| # | Correction |
|---|---|
| 1 | **B-1** — an invariant regression, independent of the generated surfaces, that fails if any exported record carries a relation type whose basis is not `DECLARED_ANNOTATION` |
| 2 | **B-2** — an invariant tying `review_state == "TYPED"` to `relation_type != UNTYPED` |

**Strongly recommended before integration** (each is small, and each closes a hole this review
opened by execution)

| # | Correction |
|---|---|
| 3 | **N-5** — carry `panel_text_relation` (and the coupled pointer, where present) into `evidence`. 26 of 265 candidates currently lose LEGEND's own verdict on whether the panel agrees with the text |
| 4 | **N-1 / N-2** — emit the 41 occurrences as their own record kind, carrying field and raw annotation, so the reduction is auditable and the Scientist's rationale survives typing |
| 5 | **N-3 / N-4** — either represent a relation type per direction, or state in the schema that an edge type is undirected by construction; and stop emitting `basis: DECLARED_ANNOTATION` beside `relation_type: UNTYPED` |
| 6 | **N-6** — exclude citation parentheticals from `_working_model_comentions`, or demote a co-mention that contains only claim/paper identifiers out of the `confirming` tier |
| 7 | **N-11** — commit the change set to a named branch so it acquires a `BASE_HEAD` and a content hash. It currently exists in one working tree and in no git object |

**Deferrable** — N-7 (drift-signal specificity), N-8 (named loss for a non-object manifest), N-9
(scope the "Losses: None" sentence), N-12 (record the mutation controls).

**Operator decision, not a correction** — N-10. The export newly ships 53 013 characters of
verbatim third-party text from 60 papers, 14 snippets of it from the three non-OA
page-adjudicated articles. `public_release_gate.py` does not look at copyright. That read is the
operator's, before any public push, and it is not reversible.

### On the success condition

> `SCIENTIST` = origin/adjudication of scientific meaning
> `ORCHESTRATOR/PATHOGRAPH` = deterministic assembly and representation
> `MIRROR` = adversarial verification that the boundary has not leaked

**The boundary has not leaked.** Orchestrator assembled and did not author: 0 of 20 edges typed,
0 of 39 scales annotated, 302 candidates all `AWAITING_SCIENTIST_REVIEW` with
`endpoints_resolved: false`, and the four judgements a weaker tool would have made — type from
endpoints, type from grammar, scale from pathway, edge from shared evidence — are all absent from
the shipped bytes and three of the four are held by regressions.

**The boundary is not yet fenced.** It is held by the author's discipline in this revision, not by
the suite, at the two exact points where a future maintainer would most plausibly and most
innocently cross it.

---

`AUTHOR_RESPONSE` — required (C.2/C.3). Silence is not acceptance. Two rounds maximum before
adjudication.

**Reproduction.** Every measurement in this review re-runs from:
`framework/scripts/pathograph.py --root <shared checkout> --disease wwox [--verify --out … --export …]`,
`framework/scripts/test_pathograph.py`, and the mutation/fixture harnesses under
`…/e7f533de-…/scratchpad/{mutate.py, adversarial.py, pgmut/, pgshadow/, pgshadow2/}`.
Orchestrator's tree was read and never written (§1.5).
