---
artifact: MIRROR hostile review (Annex C.2)
review_id: REV-P51C9-MIRROR-001
candidate: CAND-20260817-P51C9
content_hash: b1f3729ba493c414cba5eb1cdccc8b739f9631a3cecf87cbf070714bad32f956
base_head: 908197ba62a064546f17c9c277ff497ffc753656
branch_tip: 629bc89ac62b4bd0478e4b05fa403e769abda2b1
reviewer: mirror
adjudicator: operator
level: R4 / MIRROR_REQUIRED
review_date: 2026-08-17
verdict: REQUEST CHANGES
scope: conceptual and governance review only — no implementation, no modification, no authorisation
---

# MIRROR HOSTILE REVIEW — CAND-20260817-P51C9

```
candidate  CAND-20260817-P51C9
reviewer   mirror
level      R4 / MIRROR_REQUIRED
verdict    REQUEST CHANGES
```

**Binding verified.** Hash reproduces from the published command: `b1f3729b…32f956`, `v4`,
504 included. `BASE_HEAD` is `main` and an ancestor of the tip, 0 behind. All four rotated
fingerprints reproduce exactly as claimed. LINT `PASS`, publication gate `PASS / BLOCKS: 0`.
Main is untouched. **The content domain of this candidate is two files** —
`governance/plan_defined_parameters.md` and `deployment/deployment_profile.md` — everything else
is control plane.

---

## 1 · STEELMAN

**The P5.1 amendment is the smallest correct change and is argued from the right place.** It
closes a divergence between a definition and its own operative rule, adds one root, and states the
`learning/` half explicitly *because it required no edit* — a determination that binds, was made,
and would otherwise leave no durable trace is branch (B) of C-9's own model. Recording only the
half that needed a diff would have been the defect the document describes.

**The version-bump reasoning forecloses exactly the regression this review was asked to hunt.**
*"The prefix must move whenever the rule does rather than whenever the output does. Bumping only
when a value visibly changes would make the guard depend on the accident of what a particular tree
contains."* That is the correct answer to *"should the prefix change when the domain changes but
the output does not?"* — yes — and the candidate states it before being asked.

**`runtime/` is refused correctly and for a reason, not by deferral.** *"Declaring a root for it
would treat a container as a class"* is C-9's B-1 applied one level up, by the author, against his
own convenience. The interim safety is stated rather than assumed (untracked → invisible to
`ls-tree` → absent from the domain, so no fixed point arises), and the residual cost is named and
counted rather than discovered later.

**The scope exclusions hold.** I searched the content diff for every topic the mandate named:
`LOCATOR_OVERSHOOT_GATE`, Semantic Regression Detection, Binding Contract Model, Agent-to-Agent
protocol — **zero occurrences each**. The content diff is +36/−2 and +24/−1. Nothing crept in.

**The retirement record is provenance, not a label.** `NEVER MERGE / NEVER PUSH` is accompanied by
the reason that makes it binding — seven page-crop PNGs of `PMID 17803050`, all-rights-reserved,
no DOI, no PMCID — cited against rule 5e verbatim. Deletion is not performed and the record says
in two places that it does not authorise one. The branch still exists with its 3 commits intact:
knowledge preserved, act deferred, mark first. That ordering is the whole point and it is right.

---

## 2 · BLOCKING FINDINGS

### F-1 — the Orchestrator worktree change does not belong in this candidate

```
claim     Two decisions travel as one MAJOR because both are content changes under one gate.
evidence  The two content files have entirely different blast radii, verified:
            · plan_defined_parameters.md is in CORE for all four roles → rotates all four
              fingerprints → invalidates every checkpoint (CHK-plan-0001…0008, CHK-mirror-0001…0003)
            · deployment/deployment_profile.md is in NO role's fingerprint set → zero cascade
              (I checked this twice: a first grep matched `annex_i_bootstrap_deployment.md` on the
              filename and I nearly reported the opposite)
          They also arise from different evidence: P5.1 from the C-9 classification collision,
          the worktree from C-5/C-7 operational friction. Body §13 requires the "smallest coherent
          auditable unit".
problem   A zero-cascade change inherits a full-cascade change's approval weight and risk for no
          reason — and, decisively, the worktree change carries an unresolved frozen-text tension
          (F-2) that the P5.1 amendment does not. Bundled, a defect in one blocks the other. That
          is the contamination this review exists to prevent.
required  Split. `CAND-…-P51C9` carries the P5.1 amendment; the Orchestrator worktree becomes its
correction own candidate, where F-2 can be answered without holding P5.1 hostage.
```

### F-2 — the worktree change cites §8's obligation and omits §8's location

```
claim     "That is corrected here, and not as a workaround" — argued from Annex D.1 and §14, and
          from "§8 obliges it to produce durable output".
evidence  Body §8 is titled "ORCHESTRATOR — ROOT, AUTORITÀ, IDENTITÀ" and its first sentence reads
          "Orchestrator vive nella chat grafica associata a `<REPO_ROOT>`". §0.2 states the
          promotion is in place — "La stessa chat viene promossa; non servono due chat root" — and
          §47 steps 9 and 14 put the root chat in BOOTSTRAP_MODE and promote it there.
          The candidate quotes §8 for the obligation and never for the location.
problem   The characterisation is right — I independently reach (B), a structural correction:
          Annex D.1 makes WORK_COMMIT obligatory for every actor on its own branch, the root's
          branch is `main`, a commit to `main` is canonical by definition, so the Orchestrator
          alone had no branch on which the obligation could be met. The ONE_WRITER argument is
          real: a standing writer in root becomes a writer only inside a batch window.
          What is missing is the reconciliation. A MAJOR that relocates an actor the frozen body
          locates must engage the text that locates it, and this one quotes the same section
          selectively — the half that supports the change and not the half that resists it.
required  Address §8, §0.2 and §47 explicitly: either show the relocation is compatible (the body's
correction own blockquote says position confers no authority, which is the strongest available
          argument and the candidate does not make it), or declare the divergence in the form
          C-9 §9.3 already uses for adopt-or-diverge. Not a request to abandon the change.
```

### F-3 — four of five SOURCE_COMMITS are orphaned and will not survive a clone

```
claim     Five source commits, listed as full 40-character oids.
evidence  f7a00498, 6c2ab4f1, f3bef292 and 93a443b8 are reachable from ZERO refs. The branch was
          rewritten; the in-history equivalents are 0d9519b, 63e34c7, 59fd5f5 and 488d459, and
          none of the cited four is an ancestor of BRANCH_TIP 629bc89.
          Reassuring half, verified blob by blob: the PROPOSAL blobs are IDENTICAL across the
          rewrite (52051a94, 3f411b4b, 752a163e, 5a8c2b64), and 93a443b8 and 488d459 have
          identical trees. Nothing changed in substance.
problem   They resolve today only in worktrees that predate the rewrite. A fresh clone receives
          only reachable objects, and `git gc` is entitled to delete them. The provenance chain of
          a MAJOR is therefore recorded against objects that will vanish — RC-6's defect class
          recurring by a different mechanism. The earlier remedy (full oids instead of 7-char
          prefixes) is correctly applied here and does not defend against a rewrite, which is
          worth knowing.
required  Cite the in-history oids: 0d9519b…, 63e34c7…, 59fd5f5…, 488d459…
correction
```

---

## 3 · NON-BLOCKING OBSERVATIONS

- **N-1 · the excluded count is wrong.** §6 states *"504 included / 16 excluded"*; the derived
  output at `BRANCH_TIP` is **504 / 17**. The included half is right. This is RC-3's class — a
  count maintained in prose beside a command that derives it — recurring in the verification table
  after having been removed from §1. Manifest-local, no hash effect.
- **N-2 · the same orphaning hits my own records.** `REV-C9-STATE-MODEL-001/002/003` cite
  `f7a0049`, `6c2ab4f` and `f3bef29`. Their blobs are identical to the in-history commits, so the
  substance stands, but my citations will dangle in a fresh clone exactly as the manifest's do.
  Recorded against my work, not only against Plan's.
- **N-3 · `reviews/` is a third unbounded prefix root.** Anything later placed under it leaves the
  binding silently, as `ledger/` already can. Not introduced here and correctly out of scope; the
  standing mitigation remains `--show-domain` printing every excluded path.
- **N-4 · `runtime/`'s interim safety is conditional and nothing enforces the condition.** The
  argument holds *while* `runtime/` stays untracked. The moment anyone commits it, it enters the
  content domain silently. The candidate states the condition; no check asserts it.
- **N-5 · none of the above is machine-detectable.** `legend_lint.py` still contains zero
  references to `governance/` or `roles/`, so a divergence between P5.1's definition and its rule —
  the very defect this candidate repairs — would not have been caught by any gate.

---

## 4 · CHANGE_CLASS VALIDATION — **MAJOR CONFIRMED**

Confirmed, and by direct qualification rather than by fail-closed doubt. §12's strict test is
satisfied twice independently: `CONTROL_PLANE_ROOTS` defines the domain over which
`CANDIDATE_CONTENT_HASH` is computed and to which GATE 5 binds every approval — **gate policy** —
and the prefix bump to `v4` makes every prior value non-comparable by design — **a breaking change
to a canonical computation**. The manifest's own justification ("it sits in the CORE set of all
four roles") is correct and is the third independent route to the same class.

This validation stands for the P5.1 amendment on its own. The Orchestrator worktree change is also
MAJOR, on the authority/deployment clause — which is a further reason it can be split without
being downgraded.

---

## 5 · GOVERNANCE RISKS

1. **Approval of a bundle is approval of both halves.** If the operator approves as prepared, F-2's
   unreconciled tension with §8 is ratified silently, because approval binds to a content hash and
   not to a rationale.
2. **GATE 0 remains unpassable and the candidate says so.** Root is unclean (9 untracked files), no
   lease exists, the one-commit exemption is spent, L2 is suspended. The candidate correctly does
   not pretend otherwise — but the change that would make the first of these resolvable is F-1's
   change, which I am recommending be separated. **That ordering is the operator's to weigh**: the
   split is right on scope grounds, and it delays the unblocking. I state the tension rather than
   resolve it by preferring my own criterion.
3. **The rotation invalidates every checkpoint in the system**, mine included. Intended under P2.3,
   correctly declared in advance, and the second live exercise of the invalidation signal A.6 and
   G.3 assign to me. Recorded as the second data point.
4. **Post-rotation fingerprints are single-actor until reproduced** — the manifest lists this as
   UNRESOLVED 4. **Discharged by this review**: I recomputed all four independently and they match.

---

## 6 · LOCATOR_OVERSHOOT applied to the candidate itself

| Claim | Verdict |
|---|---|
| hash `b1f3729b…`, v4, 504 included | **SUPPORTED** — reproduced |
| "no `reviews/` path exists here" | **SUPPORTED** — 0 entries at the tip |
| "504 included / 16 excluded" | **NOT_IN_SOURCE** — the command returns 17 |
| "commits 1–4 contribute nothing to the hash" | **SUPPORTED** for the in-history equivalents; the cited oids are orphaned (F-3) |
| "an Orchestrator in root had no branch on which a WORK_COMMIT was possible" | **SUPPORTED** — root's branch is `main`; a commit there is canonical by D.1 |
| "the root now carries a writer only inside a batch window" | **SUPPORTED** as a statement about root; **UNVERIFIABLE** as an improvement until a lease and the worktree exist |
| "corrected here, and not as a workaround" | **UNDERSHOOT** — the claim is defensible and the argument omits the frozen text that resists it (F-2) |
| "`runtime/` … no fixed point arises in the interim" | **SUPPORTED**, conditional on remaining untracked (N-4) |
| retirement: "NEVER MERGE, NEVER PUSH" | **SUPPORTED** — reason, licence status and rule 5e cited; branch and its 3 commits intact |

---

## 7 · ANSWERS TO THE REVIEW QUESTIONS

1. **Scope control** — held for everything named. The one scope failure is internal: two unrelated
   decisions in one candidate (F-1).
2. **P5.1 classification** — correct. `reviews/` in the control plane removes the fixed point: a
   review cites the hash it reviews, and inside that domain it would move it. `learning/` as
   content raises no symmetric problem, because a learning record describes a session and asserts
   nothing about a candidate's identity — and §18 names a candidate as its durable home.
3. **`runtime/`** — a correct OPEN QUESTION, not avoidance and not blocking. *Container ≠ class* is
   sufficient, the deferral names its resolving section, and the interim risk is stated (N-4).
4. **Orchestrator worktree** — **(B) structural correction**, not a workaround. But it belongs in
   its own candidate (F-1) and owes a reconciliation with §8 (F-2).
5. **Fingerprint and version bump** — correct on every count, including the conceptual trap: the
   prefix tracks the rule, not the output. Rotation correct, prior checkpoints correctly
   invalidated, `CHK-plan-0009` correctly separate and superseding `0008` by declaration.
6. **Retirement** — provenance sufficient, knowledge preserved, deferral correct.
7. **Integrity** — base correct, hash reproducible, no undeclared modification, main untouched, no
   GATE 1 bypass (Plan prepared; Plan does not execute).
8. **Hidden regressions** — F-2 and F-3; N-1 through N-5.

---

## 8 · FINAL DISPOSITION

```
MIRROR_REVIEW: REQUEST CHANGES

BLOCKING   F-1  split the Orchestrator worktree change into its own candidate
           F-2  reconcile that change with §8 / §0.2 / §47, or declare the divergence
           F-3  cite the in-history source-commit oids, not the orphaned ones

NON-BLOCKING  N-1 excluded count · N-2 my own dangling citations · N-3 third unbounded root
              N-4 runtime/ conditional safety · N-5 no governance coverage in the LINT

CHANGE_CLASS  MAJOR — confirmed
```

**F-3 alone is manifest-local and costs nothing.** F-1 and F-2 concern one of the two content
files. If the Orchestrator change is separated, **the P5.1 amendment is ready**: it is necessary,
correctly classified, minimally delimited, and I found no regression in it. That is the shape of
the disposition — not a slower candidate, a cleaner one.

**This review does not authorise execution.** The final decision is the operator's. No file of the
candidate was touched, no governance modified, no gate executed, and nothing here is an
instruction to implement.

---

## Appended 2026-08-18 — where this record's C.2 elements live

Its `WHAT_WOULD_CHANGE_MY_MIND` and `AUTHOR_RESPONSE` were missing and are supplied in `OWED-C2-FORMAT-001-REPAIR` **§ B.4**, written on 2026-08-18 and marked there as after-the-fact.

Appended, not edited. The original text above is unchanged.
