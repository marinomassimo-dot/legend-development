---
record_type: WORK_ANALYSIS
id: PLAN-MAJOR2-CANDIDATE-READINESS-001
title: MAJOR-2 restricted repair — candidate readiness, and the three questions it does not answer
date: 2026-08-26
role: PRODUCER
mode: ANALYSIS_FIRST / MINIMAL_DELTA
authority: Plan role contract — "prepare INTEGRATION_CANDIDATE with manifest (Annex D)".
  No lease acquired. No CANONICAL_BATCH_COMMIT performed or requested.
status: CANDIDATE_DEPOSITED — CAND-20260826-ORCHMAJOR2, awaiting Mirror hostile review
---

# MAJOR-2 RESTRICTED REPAIR — CANDIDATE READINESS

> **Nothing here is medical advice.** Governance only; no individual-level record.

**Outcome first.** A candidate that does not pre-decide A, B or C **is** constructible, and it has
been deposited: `CAND-20260826-ORCHMAJOR2`, on branch `plan-major2-restricted-repair`, content tip
`96982b78`, `CANDIDATE_CONTENT_HASH 9f852385…6919389f`. The reviewer-facing derivation lives in
the manifest. **This record carries the part that is about Plan's own reasoning**: what was
re-derived rather than inherited, what the authorized delta turned out *not* to require, and the
one finding that outgrew the candidate.

---

## 1 · What was re-derived, and what moved as a result

Nothing was carried over from the earlier session's preparation. Every figure below was measured
against the repository at `main = 788c357d`.

| Re-derived | Result | Did it move? |
|---|---|---|
| The two authorized anchors exist on `main`, exactly once each | line 5 and line 46, `count == 1` asserted before any substitution | no |
| Revision 4's identity | blob `24663eec`, on 3 of 49 refs, `+103/−5` | no |
| The restricted repair's identity | blob `5d1fd509`, `+6/−5` | **built here; did not previously exist on any ref** |
| `sha256(main:roles/orchestrator.md)` | `e1155911…4504` | no |
| Refs carrying `runtime/agent_card_registry.md` | **1** of 49 | no |
| Ref population | **49** = 45 local heads + 4 remote-tracking, `HEAD` symrefs excluded | — |

🔴 **The restricted repair was not on any ref.** The earlier session had prepared it; what existed
in the repository was revision 4 and nothing between it and `main`. **A prepared repair that is not
on a ref is a repair that does not exist**, and re-deriving it was not a formality — it was the
whole of the work that had actually been left undone.

## 2 · The authorized delta needed less than it looked like it needed

The instinct on delta 1 — replace `worktree: the repository root checkout` with
`worktree: orchestrator` — is that it deletes the operator's architectural intent that the root is
the session home, and that the three-field frontmatter of revision 4 is therefore *required* to
avoid losing a fact.

**Measured, it is not.** Lines 35 and 37 of the contract on `main` already say a session opens in
the root and that the location confers nothing. The `worktree:` field never carried the
session-home fact; that is precisely why the field could be stale from 2026-08-17 to 2026-08-26
without the document ever contradicting itself.

⇒ **Revision 4's three fields are an elaboration, not a repair.** Stating that is what let the
candidate stay at `+6/−5`, and it is checkable in one command rather than argued.

The same on delta 2: the qualifier is GATE 1's own disambiguation, and both § 35.1 and GATE 1 are
FROZEN and on `main`. `REV-ROLES-MIRROR-001` had already made this argument and declined to propose
text. Plan proposes the text; the reading remains Mirror's to reject.

## 3 · A/B/C — the compact form

The full treatment is § 6 of the manifest. The three answers, and the reason each holds:

| | Exact dependency | Semantic or typographic | Candidate can exist first? |
|---|---|---|:--:|
| **A** `DEC-20260820` ratified, not on `main` | **citation only.** Substantive basis is § 35.1 + GATE 1, both FROZEN and on `main`. The decision *agrees* with the delta; it does not license it | semantic — but about a different object | ✅ |
| **B** de-emphasised quotation | **none.** The quotation is in `DEC-20260822`; the clause is in `roles/orchestrator.md`. Two files; the candidate's scope contains one | typographic in the record; the repair's own variant choice is hash-determining and enumerated | ✅ |
| **C** Agent Card registry | **downstream, not upstream.** The repair makes the registry's pin stale; the registry does not gate the repair | semantic for the registry, inert for the contract | ✅ |

**B was the one that looked like a fork and is not.** The tempting error is to treat *"the decision
record quotes the clause without its emphasis"* as two rival readings of the repair. It is one
mis-transcription in a third file, traceable to `REV-ROLES-MIRROR-001` presenting the clause in a
fenced code block — where emphasis does not render, so the rendered text was quoted correctly —
which the decision record then copied into an inline italic quotation, where the missing markers
stopped being a rendering choice. **The reviewer quoted what the reader sees; the decision record
quoted the reviewer.** Neither did anything wrong at its own step.

**What is genuinely open in B** is smaller and was enumerated rather than chosen silently: four
buildable forms, four hashes, all measured. Switching is a re-hash. A fifth form — de-emphasising
the clause so the file matches the record — **was not built**, because it repairs a
mis-transcription by editing the object that was transcribed correctly.

## 4 · The finding that outgrew the candidate

🔴 **Six candidate manifests on `main` record `LINT_RESULT: PASS`, and all six declare a scope
outside LINT's population.**

`framework/scripts/legend_lint.py` scans four registry files under
`disease-models/wwox/registries/`, plus the discovery ledger, the dismissal ledger and the session
commit log. Read out of the source, then confirmed the way a negative has to be: a broken wikilink
token was planted directly into `roles/orchestrator.md` at the candidate tip and **LINT stayed
`PASS`**.

| Manifest | Declared scope | Inside LINT's population? |
|---|---|:--:|
| `CAND-20260816-GOV311` | governance body + annexes | ❌ |
| `CAND-20260817-HASHDET` | `governance/scripts/` | ❌ |
| `CAND-20260817-ORCHWT` | `deployment/deployment_profile.md` | ❌ |
| `CAND-20260817-P51C9` | P5.1 amendment + C-9 closure | ❌ |
| `CAND-20260818-SCIENTIST-AB-SPEC` | a handoff, as transmitted | ❌ |
| `CAND-20260818-SUNSET-DEC3` | sunset of the git-ignored lease seat | ❌ |

**Six of six.** The PASS is not false — the scientific canon really is consistent — but it is
*guaranteed*, by construction, for every governance candidate that will ever be prepared. A field
that cannot take the value `FAIL` is not evidence; it is a habit.

**Contrast, and this is the part that makes the finding actionable rather than merely sour:**
`PUBLICATION_GATE: PASS` on the same candidate **is** informative, and it was made so by one extra
run. Planting the same token made `public_release_gate.py` emit
`BLOCK_PUBLICATION · BROKEN_WIKILINK roles/orchestrator.md:93`. **The difference between the two
fields is not their verdict, which is `PASS` in both cases. It is that one of them was asked
whether it could fail.**

⇒ **Proposed, not enacted:** a candidate manifest should record, beside each gate verdict, whether
the gate's population intersects the candidate's scope. Plan does not amend the Annex D.2 schema
inside a candidate that would be judged under it. Routed as a normative question, not performed.

This is the same defect as Action 3 of `PLAN-MIRROR-V3-MINIMUM-REPAIR-CONSOLIDATION-001` — *a gate
that does not know what its population is* — arriving from a third direction. Action 3 asks gates
to print their population; § 3.4 of that record asks that a guard not count a document reporting a
violation as a violation; this asks that a manifest not report a verdict from a gate that cannot
see the change. **Three faces of one thing**, and the count of faces is now the argument for fixing
the cause rather than the instances.

## 5 · What Plan owes if this candidate executes

`runtime/agent_card_registry.md` carries `maintained_by: plan`. Two of its fields go stale on
execution: `WORKTREE: the root checkout # branch main`, and `ROLE_CONTRACT_HASH: e1155911…4504`
(verified equal to `sha256(main:roles/orchestrator.md)`; it would become `ec9c8e59…1bf685`).

**Plan cannot discharge that obligation today**, and the reason is the finding, not an excuse: the
registry is on `refs/heads/orchestrator` and on no other ref. Re-deriving it there leaves the
canonical branch describing a contract that no longer exists in that form. **The debt is recorded
here so that it is owed by a named actor against a named object**, which is more than it had
before.

## 6 · Reproduction

```bash
git rev-parse main                                     # 788c357d…
git rev-parse plan-major2-restricted-repair            # content tip 96982b78, plus 2 control-plane commits
python3 governance/scripts/candidate_content_hash.py \
  --base 788c357d9b7ca7afcbe7c1efc3a06b426cf7e2d5 \
  --tip  96982b78c8e6895d8248870a2cdbde0f0ecaae51
git diff --stat main 96982b78                          # roles/orchestrator.md | 11 +++++-----
```
