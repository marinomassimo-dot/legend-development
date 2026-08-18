---
artifact: DURABLE HANDOFF — definitive specification of Scientist A and Scientist B
id: HANDOFF-20260818-SCIENTIST-AB
status: TAKEN UP — by CAND-20260818-SCIENTIST-AB-SPEC (branch scientist-ab-spec), 2026-08-18.
  The body below is the handoff exactly as it was written; only this status line and the
  carried_from block were added.
carried_from: branch sunset-decision3, commits fbf3e7e (written) + b22968d (revised) — not in
  main. Carried into this branch as a byte-identical copy of blob 8e59df08 (sha256
  f3f883c1e76767216ad75963d30be80209e80a63aa7e536e0aada4c9ca7f9a0e) because a cherry-pick was
  refused by the session guard; verify with `git show b22968d:governance/candidates/HANDOFF-SCIENTIST-AB-SPEC.md | shasum -a 256`.
prepared_by: plan (evidence-index) — handing off, not authoring
authorized_by: operator, 2026-08-18, transmitted L2-20260818-ORCH-051
base: main cbce30168091f7769c56c4f019055fa55fd0d66a
scope_rule: SCOPE MUST NOT BE REDUCED. Same condition under which the DECISION 3 sunset was
  handed off and then completed intact.
---

# Handoff — Scientist A / Scientist B definitive specification

**Plan is handing this off, not authoring it**, and the reason is specific rather than general:
**one instruction in this task is the kind that does lasting damage if rushed.** The operator
requires that an existing canonical schema be reused and only genuinely necessary extensions
documented, *"because a parallel schema would be a second noun for one object"*. Establishing
what the canonical form actually is requires reading a ~900-line validator and two artifact
families carefully. **Getting it wrong creates precisely the duplicate the instruction forbids,
and a duplicated schema is not repairable by a later commit** — it propagates into every manifest
written against it.

**Nothing is started. No spec text drafted. `main` untouched at `cbce3016`.**

---

## Verified before handing off — so the next session does not re-derive it

### 1 · The sunset is canonical

```
main                             cbce30168091f7769c56c4f019055fa55fd0d66a
runtime/orchestrator_lease.md    in main
framework/scripts/lease_state.py in main
```

`CAND-20260818-SUNSET-DEC3` executed. The lease record is canonical and derivable from any
checkout.

### 2 · Preconditions FAIL — independently verified, not relayed

```
roles/scientist.md:3   actor_ids [scientist-a, scientist-b, scientist-c]
                       # PROPOSED — confirmed at registration (Annex I.2 step 7)
roles/scientist.md:7   status: PROPOSED — binding once Mirror hostile review passes and
                       the operator approves
registry (orchestrator branch)
                       scientist-a  ACTOR_ID: UNRESOLVED   # proposed
                       scientist-b  ACTOR_ID: UNRESOLVED   # proposed
                       scientist-c  registered, session ref VERIFIED at L1
```

**They are worktrees and branches, not actors.** No `ACTOR_ID` is resolved for A or B, no session
exists for either, and there are zero tasks and zero checkpoints for them. **This is prior to
anything about the benchmark**, and the specification *is* the registration that resolves it —
Annex I.2 step 7 is named in the contract itself.

### 3 · 🔴 THE SCHEMA FINDING — the one that shapes the whole spec

A canonical schema **does** exist and is versioned and validated:
`framework/scripts/deepdive_manifest.py` (`schema_version`, `CURRENT_SCHEMA_VERSION`,
`COUPLED_RELATIONS`, `LOCATOR_SURFACES = {body, figure, table, supplement, abstract}`).

**But it does not carry a per-claim array.** A real manifest's top level is
`schema_version · pmid · doi · receipt · landing · skills_considered · group_assessment ·
field_density · multihop · corpus_crossquery` — and a recursive search for a claim-shaped array
at any depth finds none.

**So the deep-dive manifest is about the provenance of a *reading*, not about per-claim
assertions.** The operator's sixteen per-claim fields (`CLAIM_ID … MECHANISTIC_RELEVANCE`) do
**not** map onto it.

### 3a · 🔴 RESOLVED — the per-claim object, and the mapping

**No longer `UNVERIFIED`.** Raised by the Orchestrator, **re-measured by Plan with a positive
control**, since this is the exact spot where its own pattern had failed:

```
claim_registry_current.md   '^## CLAIM'   39      ← the per-claim object
                            '^## '        43      ← control: the pattern discriminates
                            '^### CLAIM'   0      ← the failing pattern, reproduced
AUTHOR_INTERPRETATION in tracked state      0
```

**Canonical claim fields, read verbatim from `CLAIM 001` rather than inferred:**

```
Title · Status · Type · Pathway · Genotype/model relevance · Transferability
clinical relevance · Summary · Clinical meaning · Source · Wikilinks · Impact on Working Model
```

**The mapping is a three-artifact split, not one-to-one:**

| Concern | Artifact |
|---|---|
| reading provenance | `deepdive_manifests/*.json` — `receipt` · `source_artifacts` · `field_density` |
| locator fidelity | `fulltext_dossiers/*.md` — artifact digests, verbatim locators, joins |
| **claim assertion** | **`claim_registry_current.md` — the twelve fields above, markdown sections** |

Several of the operator's sixteen already exist under other names: `EXACT_CONTEXT` and
`MODEL/POPULATION` → `Genotype/model relevance` · `EPISTEMIC_TYPE` → `Type` · `SOURCE_ID` and
`PROVENANCE` → `Source` + `Wikilinks` · `MECHANISTIC_RELEVANCE` → `Pathway` · `LOCATOR` → the
dossier's job · `CLAIM_ID` → the section heading.

🔴 **The genuine gap, and it is not a missing field — it is a blended one.** `CLAIM 001`'s
`Summary` interleaves *what the studies report* with *what LEGEND concludes*, and its
`Clinical meaning` carries a **`Nota epistemica`** that performs exactly the
observation-versus-interpretation separation the operator asks for — **in prose, not as
structure.**

So `OBSERVATION` / `AUTHOR_INTERPRETATION` / `LEGEND_INTERPRETATION` are **not absent from the
practice; they are absent from the schema.** The registry already does this work well and
informally.

**That makes the extension surface small and well-founded: promote to fields what the registry
already does in prose.** It is not a new schema, and it is not a cosmetic addition either — the
one thing a second reader (`Scientist B`) must be able to attack is exactly the seam between what
was observed and what was concluded, and today that seam is inside a paragraph.

`DIRECTION` has no evident canonical home. `UNVERIFIED (PLAN)` — the next session should look
before adding it.

**Do not answer any remaining gap by proposing the sixteen as a new schema.** That is the failure
the operator's instruction names, and it is why this handoff exists rather than a rushed draft.

### 4 · The blinding problem is structural, and the spec must answer it

Operator's preferred benchmark target is **PMID 42397075** (Aqeilan 2026, *Brain*). Of §5's three
conditions:

```
full text available                        ✅
surface identical to both readers          ✗  files/ is gitignored (.gitignore:7); present in
                                              root and lettore, ABSENT in lettore-b
prior outputs excludable during blind pass  ✗  deepdive_manifests/PMID42397075.json and the
                                              partial-locators dossier are TRACKED and visible
                                              in BOTH branches
```

The second is fixable by copying an untracked artifact. **The third is not, and choosing a
different WWOX paper does not solve it: every candidate with verifiable provenance is one this
repository has already worked.** The blinding problem is a property of the corpus, not of this
paper.

**Three routes, none chosen here:** a benchmark branch cut *before* the prior deep-dive · path
exclusion during the blind phase · an explicit decision that the pass is **not** blind to prior
work, scored accordingly. **The spec must choose and say why; §5 makes the choice reportable.**

### 5 · The C-2 question is due here, not inherited

Both A/B worktrees carry one modified file, **byte-identical to each other**:
`disease-models/wwox/research/deepdive_manifests/PMID42422765.json`, `sha256 6c3fe60f…`, matching
the `handoff/C-2/PMID42422765-working-blob` tag and the orchestrator's handoff copy.

The handoff record reads `CONTENT RESOLVED · FORWARD OWNERSHIP UNRESOLVED — escalated`, with
*"Duplicated-assignment root cause | open — one question, to answer at registration."*

🔴 **Nothing here is unclassified work, nothing needs cleaning, and nothing may be reset.** C-2
deferred a question *to registration*, and this specification is that registration. **Answer it;
do not inherit it.**

---

## Binding scope — as transmitted

### A · Scientist A — primary evidence reader

Full-text reading · experimental findings · methods · population/model/context · directionality ·
negative results · caveats · figure and table evidence · locator · provenance · epistemic typing ·
claim candidates · mechanism implications · unresolved ambiguities.

**Must not:** turn hypothesis into observation · fill gaps with undeclared general knowledge ·
infer from abstract when full text exists · compress reading for token or cost reasons · touch the
canonical model.

### B · Scientist B — independent critical reader

Everything A does, **plus** contradictory evidence · overclaim detection · model-dependence of
conclusions · direct result versus authors' interpretation · methods and statistical caveats ·
alternative explanations · unsupported claims · what A may have omitted.

🔴 **B is not a scientific Mirror.** Mirror remains reviewer and adjudicator of the *process* and
is not replaced by the second reader.

### Common contract — both roles

agent contract · authority boundary · worktree and branch ownership · input and output schema ·
provenance and locator requirements · epistemic typing · permitted inference levels · forbidden
actions · completion criteria · handoff schema · acceptance test.

### Per-claim minimum, as transmitted

```
CLAIM_ID · SOURCE_ID · SOURCE_TYPE · EXACT_CONTEXT · MODEL/POPULATION · OBSERVATION ·
AUTHOR_INTERPRETATION · LEGEND_INTERPRETATION · EPISTEMIC_TYPE · DIRECTION · LOCATOR ·
PROVENANCE · UNCERTAINTY · LIMITATIONS · CONTRADICTORY_EVIDENCE · MECHANISTIC_RELEVANCE
```

🔴 **Subject to §3 above: reuse the canonical form if one exists and document only genuinely
necessary extensions.** These sixteen names are the *requirement*, not necessarily the *field
names* — mapping them onto canonical names is part of the work, not a deviation from it.

## Candidate discipline

`BASE_HEAD cbce3016` · candidate tip · `CANDIDATE_CONTENT_HASH` under `legend-candidate-v4` ·
classified diff · file list · **normative / runtime / documentation distinguished** · test
evidence · open debts. **No `HUMAN_APPROVAL` pre-filled.** Mirror review independent, before any
approval.

## Not authorized — Plan or Orchestrator

Canonical scientific changes · integrating benchmark claims into the disease model · registry
validator · P7 · autonomous watcher · approval-queue repair · ACK criteria · Plan→Mirror routing ·
ratifying Mirror's observation · **Metacognition Agent during the benchmark** · benchmark on
Scientist C · a second benchmark paper · any candidate beyond the A/B scope.

**The seven open governance debts are carried forward and must not be resolved silently inside
this work.**

---

## Two drafting rules earned this week, both of which apply here

**1 · Put the bound where the claim is.** Not merely *state* the bound — a caveat in the prose
under a claim in the table is a caveat a reader never reaches. This failed three times in two
days, once inside the very section written to prevent it.

**2 · Ask which axis the claim can fail on, then bound that one.** `CONTROL_SPECIFICITY_RULE`.
Rule 1 does not subsume this: a bound can be adjacent, prominent, and on the wrong axis — as
`EXPIRED_UNUSED` was, where the stated bound covered detection-versus-prevention while the name
failed on renewal-versus-use, which carried no bound at all.

**And the positive form, which is why both rules are checkable here:** *an enumerated set is
falsifiable; a bare integer is not.* Every count in this handoff is stated as a list or with the
command that produced it.
