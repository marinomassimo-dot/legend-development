---
artifact: MIRROR hostile review (Annex C.2)
review_id: REV-P5DOMAIN-MIRROR-001
object: CAND-20260819-P5DOMAIN · CANDIDATE_CONTENT_HASH 930dfefb…6b97 @ BASE_HEAD f70878d1
level: R4 (MIRROR_REQUIRED — Annex G.1: governance, MAJOR; C.1 floor R4 METHOD)
reviewer: mirror
author: plan
adjudicator: orchestrator (C.3) · HUMAN_APPROVAL operator (H.1, MAJOR/governance) — none granted,
  none implied, none prefilled by this review
date: 2026-08-19
scope: P5 TRUTHFULNESS + FIXED-POINT DISCLOSURE only. The runtime/ classification, the P5-D
  detector, the Orchestrator surface fix, Routing/Candidate B, lifecycle, Scientist activation and
  BENCH-AB-001 were NOT reviewed as if this object canonicalized them, because it does not.
supersedes: nothing. This is the first review of this object.
verdict: ACCEPT — the premise conflict, the fixed-point hazard and the absence of mechanization all
  reproduce independently; § P5 now asserts nothing false; the hazard is disclosed at exactly the
  strength the evidence supports and is NOT called resolved; the C-9 §7.2 deferral is correct on a
  reading of the hold I verified rather than accepted. Five non-blocking findings, one of which I
  came close to making blocking and explain why I did not.
governance_loaded: 3.1.1 · mirror fingerprint 3dff8954…f65c at BASE_HEAD, e01b4108…0412 at the
  candidate content tip — this candidate rotates my own fingerprint, which is declared below
reviewer_runtime: 2.1.233, observed from this session's own owning process image
  (<HOME>/.vscode/extensions/anthropic.claude-code-2.1.233-darwin-arm64/…). `claude` on
  PATH reports 2.1.232 and is NOT evidence about this session. Plan's `--cwd` probes were taken at
  2.1.232 — a DIFFERENT runtime from this review's — so I did not attempt to revalidate them and
  say so where it matters (§9).
---

# The sentence is true now, and the section it hands the decision to still says the opposite

**One sentence.** Everything this candidate measures, I re-measured and got the same answer —
including the two digits Plan warned me it had already got wrong twice — and § P5 is now free of the
premise it had been carrying; what the candidate does not do is tell the operator that the section
it routes the decision to still contains the same falsified sentence, unmarked.

**VERDICT TRANSFER: NONE.** No value below was taken from the manifest, the handoff, the SLR or the
prompt. Every hash, count, index and fingerprint was recomputed from explicit commit SHAs in an
isolated clone and in detached checkouts, and the load-bearing ones were computed twice by two
different toolchains.

---

## 0 · Rehydration — fail-closed, PASS

```
pwd                  <REPO_ROOT>/.claude/worktrees/mirror
git top-level        <REPO_ROOT>/.claude/worktrees/mirror   IDENTICAL
branch               mirror
HEAD                 94927355507ee87adf7531788edbc4ce9907b156
git status           clean
ACTOR_ID             mirror
ROLE CONTRACT        roles/mirror.md — read IN FULL at main (f70878d1), byte-identical to the
                     copy at this worktree's HEAD (git diff HEAD main -- roles/mirror.md: empty)
```

`pwd` == git top-level == assigned Mirror worktree. **MIRROR WORKTREE: PASS.**

Reconstructed from durable repository state, never from the prompt:

| item | source | value |
|---|---|---|
| review authority | `roles/mirror.md` "Hostile review layer" + Annex C.2 | single format, STEELMAN before objections, declared falsifier; `CONFIRMED` = *no defect found given the evidence bundle*, never *true* |
| perimeter | Annex G.1 via `roles/mirror.md` | `MIRROR_REQUIRED` — governance, MAJOR, R4: three independent grounds |
| fingerprint calibration | `roles/mirror.md` "Two metrics are Mirror's specific responsibility" + A.6 DETECTION(b) | the checkpoint invalidation rate is mine to monitor — §8 below |
| E.2 curation | Annex E.2 *"cura epistemica: Mirror"* | SLR-plan-0009's three learnings are mine to classify — §12 |
| canonical main | `git rev-parse main` in the root checkout | `f70878d1cb98317ec62808987fc328be7f8f4ea8` — **matches the expected value, verified not assumed** |

**STABLE ACTOR IDENTITY vs CURRENT SESSION ROUTING — distinguished.** My stable identity is
`mirror`, from `deployment/deployment_profile.md` and `roles/mirror.md`, both durable. This session's
routing status is **NONE**: the operator opened this chat manually, which establishes a REVIEW
EXECUTION ENDPOINT and nothing else. No `SESSION_REF` was invented, no CURRENT claim is made, no
supersession, no registrar authority. Routing remains UNRESOLVED.

```
SELECTION METHOD     MANUAL HUMAN OPERATOR SELECTION
PURPOSE              independent review of CAND-20260819-P5DOMAIN
CURRENT ROUTING      NONE      SUPERSESSION  NONE      REGISTRAR  NONE
```

**One instrument note that matters.** This worktree's copy of
`governance/scripts/candidate_content_hash.py` is blob `be20e303`, while canonical main carries
`cd5776d3` — my checkout is 56 commits off the merge-base and its copy is **stale**. I did not run
it. Every hash below was computed either by the canonical `cd5776d3` script inside a fresh clone, or
by an implementation I wrote for this review. Had I run the script sitting in my own worktree, every
number in this review would have been produced by the wrong instrument and would probably still have
looked right.

---

## 1 · Binding — reproduced by three independent routes

```
BRANCH                  p5-domain-truth
BASE_HEAD               f70878d1cb98317ec62808987fc328be7f8f4ea8              VERIFIED == main
CONTENT_TIP             ceefaa28611527d83b9f5e2209c99733a3a10afd              VERIFIED
MANIFEST_TIP            dae0cca8f56f22fd88ffc7093a8fe2ea88430a33              VERIFIED
CANDIDATE_CONTENT_HASH  930dfefb3ce69bfaedc3920c96b3cddafbd07c9560498da4291b04b1f5476b97   VERIFIED
CANDIDATE_HASH_VERSION  legend-candidate-v4                                   VERIFIED unchanged
DOMAIN CARDINALITY      533 included · 40 excluded                            VERIFIED
```

| route | instrument | result |
|---|---|---|
| A | canonical `cd5776d3` script, `--show-domain`, run from a fresh clone checked out on `main` | `930dfefb…` · 533 · 40 |
| B | same script `--emit-domain \| shasum -a 256` — does not trust the script's own hashing | `930dfefb…` |
| C | **an implementation I wrote for this review** — git plumbing + `awk` + `LC_ALL=C sort` + `shasum`, deliberately a different toolchain from the governed Python | `930dfefb…` |

Route C emits the serialized bytes too: `cmp` against route B's bytes returns **BYTE-IDENTICAL**,
57 504 bytes each. This is the check that matters, because two implementations agreeing on a
*digest* can still be one implementation run twice — `SLR-mirror-0015` L-4. They agree on the
**pre-image**, by two different sort implementations, and the sort is the only place the recipe could
silently diverge. I verified separately that no path in the tree is quoted by `ls-tree` and none is
non-ASCII, which is the precondition making `LC_ALL=C` byte-order equal to Python's `str` order.

**BINDING: PASS.**

**The branch has one commit past the declared `MANIFEST_TIP`** — `c9de134`, which writes the
`MANIFEST_TIP` value into the handoff, replacing the placeholder `<the commit carrying this file>`.
It touches one control-plane file. I computed the binding at `c9de134` as well: `930dfefb…`,
unchanged. So the branch having moved does **not** break the binding, and the self-reference is
resolved the only way it can be — the value is written in a commit after the one it names, in a
control-plane root that is outside the hash. Recorded because a reviewer arriving at the branch tip
will see a commit the handoff does not mention, and should know it is inert.

---

## 2 · STEELMAN (mandatory, before the objections)

**This candidate is better than the class of candidate it belongs to, and the reason is
structural rather than stylistic.**

The easy version of this work exists and would have passed a lazier review: correct two sentences,
declare `PROSE_ONLY`, note that no hash moves, ship. That version would have been *true* and would
have left the reader of § P5 believing the interim is safe — because removing a false safety claim
without replacing it leaves silence where a hazard is, and silence in a normative section reads as
absence. Plan saw that, said so in §6 in one line — *"a smaller false impression than the one
removed, which is still a false impression"* — and put the measured hazard **in the normative
section rather than in the manifest**. `SLR-mirror-0015` L-2 says a correction filed in the control
plane does not travel with the content it corrects. This is that learning applied by its own reader,
unprompted, to a case where applying it costs four fingerprint rotations. It would have been cheaper
to be right in the manifest.

Second, the deferral is not an evasion, and I tested it as one. Plan had every incentive to exclude
`runtime/orchestrator_lease.md` — it is *"probably right on the merits"* by Plan's own §6, it is
control plane under § P5's own definition, and it would have closed the hazard in one line. Plan
declined on the grounds that C-9 §7.2 reserves the classification to the operator. I checked whether
that hold actually covers this decision rather than accepting the citation, and it does (§7). A
proposer who declines the fix that would make its own candidate look complete, on a hold it could
have read narrowly, is doing the thing `AUTHOR != REVIEWER != ADJUDICATOR` exists to make
unnecessary.

Third, the hazard is **measured**. Three probes, an external oracle, a non-void negative control,
and a mutation control on the parser. Plan's handoff §4 lists the guards it ran *so that I could
attack the guards instead of repeating them*, and names the three claims it most expected to lose.
Of the four candidates I have reviewed, this is the one whose author made my job hardest to do
badly.

---

## 3 · P5 PREMISE CONFLICT — **CONFIRMED**

The sentence at `main`:

> *"While `runtime/` remains untracked it is invisible to `git ls-tree` and therefore absent from the
> domain, so no fixed point arises in the interim."*

Every clause after the first is conditioned on `runtime/` being untracked. Measured:

```
git ls-tree -r --full-tree f70878d1 -- runtime/     → runtime/orchestrator_lease.md   EXACTLY ONE
git check-ignore -v runtime/orchestrator_lease.md   → rc=1                            NOT IGNORED
git ls-files --error-unmatch <path>                 → path echoed                     IN THE INDEX
```

```
TRACKED runtime/ PATHS      { runtime/orchestrator_lease.md }   — the complete set, at BASE_HEAD,
                            at the content tip, and at the XPORT tip
LEASE P5 MEMBERSHIP         IN_DOMAIN
```

`325da04` (2026-08-18, *"The lease gets a tracked home…"*) created the path; `git log --all
--diff-filter=D` over it returns empty, so it has never since been deleted. **"`runtime/` has not
been untracked since `325da04`" is true.**

### 3.1 · Path index — reproduced, and the reason the number is slippery

Population and order defined explicitly: the included list is `git ls-tree -r --full-tree <tip>`
minus every path prefixed by a declared `CONTROL_PLANE_ROOT`, sorted byte-wise by path; the index is
1-based over that list. `--emit-domain` prints it preceded by **two header lines** (version prefix,
`BASE_HEAD`), which is where the off-by-ones come from.

| tip | index | total | note |
|---|---|---|---|
| `86dfe297` (xport branch tip) | **495** | 532 | |
| `e839db38` (XPORT revision-2 declared `CONTENT_TIP`) | **495** | 532 | the tip the published binding actually names |
| `f70878d1` (BASE_HEAD) | **495** | 532 | |
| `ceefaa2` (this candidate's content tip) | **496** | 533 | `learning/…SLR-plan-0009.md` sorts before `runtime/` |
| `f48a807f` (XPORT revision 1) | 494 | 531 | |

Computed by both route A and route C, agreeing. I also confirmed the index is independent of
`--base` by recomputing the same tip against a different base — it is, which is what makes "entry N
of M" a property of the tip alone and therefore quotable.

```
PATH INDEX             495 of 532 at the XPORT tip · 496 of 533 at this candidate's content tip
PATH INDEX NORMATIVE   NO — it is illustrative. Nothing parses it; the hash is over ls-tree lines,
                       not over an ordinal. It is operative only as a truth claim in prose.
```

**The candidate's prose says *"entry 495 of the 532 that the `XPORT` binding hashed."* That is
correctly qualified and it is TRUE** — at `e839db38`, the tip XPORT's binding actually names. Plan
warned me it had been wrong twice and told me to re-derive rather than trust it. I re-derived it.
It is right, and the qualifier "that the XPORT binding hashed" is doing real work: drop it and the
sentence becomes false of the candidate's own tip, where the answer is 496 of 533. The SLR's EVIDENCE
block carries **both** numbers with both tips named, which is more precise than the prose needed to
be.

---

## 4 · FIXED-POINT HAZARD — **CONFIRMED** · falsifier **PASS** · wrong-reason **NO**

Reproduced on synthetic trees built with plumbing in a throw-away clone. **No ref updated, no
canonical repository touched, no lease acquired or released.** The trees were built by
`read-tree` → `update-index --cacheinfo` → `write-tree` → `commit-tree`; the resulting commits are
unreferenced objects, and the hash depends only on their trees, so commit identity is irrelevant.

**Pre-assertions, all made BEFORE any hash was read:**

```
T1 tree 0bf1560f…  CHANGED vs T0    P5 blob IDENTICAL to T0    one variable
T2 tree 394cc106…  CHANGED vs T0    P5 blob IDENTICAL to T0    one variable
T4 tree 95a9d3cb…  CHANGED vs T0    P5 blob IDENTICAL to T0    one variable
T0 tree 6f6bb1c8…                   three synthetic trees, all distinct
lease blob @ XPORT tip  c34f4866…  8 703 bytes   \  both verified to exist, to be of type blob,
lease blob @ orchestr.  2795dfe0… 18 837 bytes   /  and to be non-empty, before use
```

Pinning the P5 blob identical across all four is the control that makes this a one-variable
experiment: the domain **rule** is read from the tip being hashed, so a probe that perturbed § P5
would move the hash for the wrong reason.

| probe | one-variable change | hash | expected reason |
|---|---|---|---|
| **T0** | none — unmodified XPORT tip | `81f241f2…6e1f` | **ORACLE.** Equals the published XPORT value. The instrument is shown capable of the right answer before any claim rests on it. |
| **T1** | lease blob → the `orchestrator` branch's, **IN_DOMAIN** | `ddc0b08d…ac35` | **HASH MOVES** |
| **T2** | the *same* 18 837-byte blob → `reviews/…`, **EXCLUDED** | `81f241f2…6e1f` | **HASH HOLDS**, tree verified changed first |
| **T4** | the *same* blob → `deployment/deployment_profile.md`, **IN_DOMAIN, not `runtime/`** | `78379cca…852c` | **HASH MOVES** — *my addition* |
| **T3** | tree unchanged, `BASE_HEAD` advanced to `f70878d1` | `06095c0c…f8b8` | **HASH MOVES** |

`T1` and `T3` reproduce Plan's reported `ddc0b08d…` and `06095c0c…` **exactly**. Route C agrees with
route A on all five.

**`T4` is mine and it closes a hole in the design.** `T1` vs `T2` differ in two things at once — the
path is different *and* its domain membership is different — so on Plan's three probes alone, "the
hash moved because `runtime/` is special" survives as an alternative explanation. `T4` substitutes
the identical blob into a third path that is IN_DOMAIN and is not under `runtime/`, and the hash
moves. The variable is therefore **domain membership**, not the identity of the path. Plan's
conclusion is right; its probe set was one control short of isolating it, and the missing control
agrees.

```
P5 FIXED-POINT HAZARD      CONFIRMED
P5 FIXED-POINT FALSIFIER   PASS
WRONG-REASON PASS          NO
```

---

## 5 · CURRENT MITIGATION — **PROCEDURAL** · Plan's absence claim **SUPPORTED, one clause NARROWED**

Plan asked me to attack the claim that nothing mechanizes the write-location convention. Negative
capability discipline applies: I state the instruments, because *not observed via X* is not
*impossible*.

```
NOT_OBSERVED_VIA:
  1  git grep -l -F 'runtime/orchestrator_lease'  over all tracked paths at main   (11 files, all prose/records)
  2  git grep -lE 'ORCHESTRATOR_LEASE|lease_state' at main                          (20 files)
  3  enumeration of every .py/.sh/.yml/.json under framework/, governance/, scripts/, .claude/
  4  framework/scripts/lease_state.py      — READ IN FULL
  5  framework/scripts/batch_commit.py     — READ IN FULL (63 lines)
  6  scripts/guard_bash_command.py         — the LIVE PreToolUse Bash guard, read in full
  7  .git/hooks in the real repository AND core.hooksPath                            (none installed)
  8  .github/workflows/public-release-gate.yml                                       (CI)
  9  targeted sweeps for ONE_WRITER / "write surface" / "orchestrator branch" /
     "candidate branch" across governance/, roles/, framework/, deployment/, BOOTSTRAP.md
```

Findings, each verified at source rather than reported:

- **`lease_state.py`** — `derive()` returns `RELEASED` / `STALE` / `ACTIVE` from `RELEASED_AT`,
  `EXPIRES_AT` and the clock; `findings()` emits `DISAGREEMENT` and `EXPIRED_WITHOUT_RENEWAL`;
  `main()` checks the ACTIVE singleton. `grep -niE 'branch|worktree|cwd|rev-parse|git '` over the
  whole file returns **nothing** but two prose lines. It has no location predicate and no git
  awareness at all. **Plan's characterisation is exact.**
- **`batch_commit.py`** — 63 lines, three functions: `snapshot`, `restore`, `main`. No occurrence of
  `lease`, `runtime/`, `branch`, `worktree` or `gate`. **Exact.**
- **The live Bash guard** — the one mechanism in this repository that actually intercepts writes.
  It denies blanket staging and inline-heredoc repo writes. `grep -niE
  'lease|runtime/|branch|worktree|orchestrator'` over it returns **no match**. It does not constrain
  the lease's write surface.
- **Governance corpus** — the convention is not stated as a rule anywhere. The closest is the lease
  record's own frontmatter, *"One writer: `orchestrator`, from the orchestrator worktree"*, which is
  a declaration inside the artifact. **Plan characterised this correctly and did not overclaim it.**

```
CURRENT MITIGATION                  PROCEDURAL
PLAN ABSENCE-OF-ENFORCEMENT CLAIM   SUPPORTED for the write-location property · NARROWED on one
                                    subordinate clause
```

### 5.1 · The clause I narrow — non-blocking

The prose reads: *"no script checks the write surface, `lease_state.py` derives lifecycle and not
location, and `GATE 0` is asserted by hand."*

GATE 0 is `BASE_HEAD atteso + root clean + GOVERNANCE_VERSION corretta + ORCHESTRATOR_LEASE ACTIVE
singleton + ONE_WRITER` (body §13 / Annex D). Its **ACTIVE-singleton condition is mechanized** —
that is precisely what `lease_state.py --check` exists for, and the lease record instructs running
the derivation *"at acquisition, renewal, release and every `GATE 0`"*. So "GATE 0 is asserted by
hand" is over-broad as a universal about GATE 0.

It does not touch the conclusion: the conclusion is that the **write-location** property is not
mechanized, and that is exactly true and independently established by instruments 1–9. I record it
as a precision defect and not as a false premise, because the sentence the candidate needs is the
one it proved.

### 5.2 · What I verified that Plan asserted — §3.2 is structural, not merely historical

Plan claims a lease's terminal row can never sit inside the batch that lease authorized, and invited
me to show it confuses *has not* with *cannot*. It does not, and the proof is in code:

```python
def derive(record, now):
    if record.get("RELEASED_AT"):
        return "RELEASED"
```

A terminal row sets `RELEASED_AT`; the derivation then returns `RELEASED`, never `ACTIVE`; GATE 0
requires ACTIVE. So writing the terminal row before the batch **fails the gate that authorizes the
batch**. The claim is correctly scoped to *the batch that lease authorized* — a later batch may of
course carry an earlier lease's row — and within that scope it is a temporal necessity. **STRUCTURAL,
confirmed.**

### 5.3 · What I demonstrated that Plan only asserted — DETECTION is branch-local

Plan argues Annex I.3's `DETECTION` (*"doppio record sulla stessa successione"*) is weaker than a
tracked home suggests. I ran the canonical derivation in two clean detached checkouts at the same
instant:

```
checkout @ f70878d (main)          lease #1..#5     ACTIVE by derivation: 0
checkout @ 3d5e6aa (orchestrator)  lease #1..#8     ACTIVE by derivation: 0
```

Same script, same second, different answer. The instrument governance relies on to detect a double
succession **returns a different population depending on which branch you run it from**. Plan
asserted this from history; it is executably true, and that strengthens rather than weakens §3.2.

---

## 6 · PROSE-ONLY SUFFICIENCY — **PASS** · purpose is **TRUTHFULNESS_DISCLOSURE**

This was the central question I was asked to answer: does the candidate merely improve truthfulness,
or does it claim the hazard is resolved?

I read every changed operative sentence of § P5.1 and § P5.3. The candidate states, in the normative
section:

- tracked runtime content **is** in-domain — *"it is **inside the content domain**"*;
- the fixed-point risk therefore **exists** — *"So the interim is not hazard-free"*, with the three
  measured digests printed;
- current prevention is **procedural** — *"What prevents the fixed point today is procedure, and
  only procedure… declared `PROCEDURAL` and not `MECHANIZED`"*;
- domain reclassification is **not adopted** — *"This amendment corrects the false sentence and does
  not resolve the classification"*;
- C-9 §7.2 remains the decision boundary — *"The debt is recorded with its owner — C-9 §7.2,
  operator"*.

```
CANDIDATE PURPOSE          TRUTHFULNESS_DISCLOSURE
HAZARD CLAIMED RESOLVED    NO — searched for it; the section says the opposite, twice
PROSE-ONLY SUFFICIENCY     PASS
```

**On "disclosure without mechanization is the defect XPORT's §7 was criticized for"** — Plan asked me
to attack its answer. The two are not the same shape. XPORT's §7 documented a hazard it was free to
fix. Here the detector *is* the classification: a check that a candidate's tip may not mutate a
tracked `runtime/` path is enforcement of the exclusion, and enforcing a classification is one step
from making it. Building it would consume the operator's decision by implementing its outcome. That
is not a smaller version of XPORT's defect; it is the hold working. The answer survives.

### 6.1 · Truthfulness sweep

I searched the candidate tree for the old premise and its variants — `remains untracked`, `no fixed
point arises`, `absent from the domain`, `invisible to`, and `untracked` scoped to the governance
files. Inside § P5.1 the premise survives **only as a quotation immediately followed by its
refutation** (*"The sentence that stood here was false…"*), which preserves the audit trail and is
the correct treatment. Same for the manifest, the SLR and XPORT §15.2, all quoting to refute.

```
FALSE OPERATIVE P5 CLAIMS REMAINING     0
```

The one live, **unrefuted** assertion of the premise anywhere in the tree is not in § P5. It is
finding **N-1**, below.

---

## 7 · C-9 §7.2 — hold **APPLIES** · Plan's deferral **CORRECT**

I read C-9 §7.2 in full and tested the citation rather than accepting it.

```
status                        ACCEPTED
acceptance_is_not_adoption    true
status_transition_owner       operator
status_next_review            at the first governed change that adopts any clause of this proposal
hold                          no implementation and no governance modification until that review
                              completes; L2 suspended; the status/C-8 batch frozen
```

**1 · Does C-9 §7.2 actually govern this classification decision?** Yes, and not by analogy — by
name. §7.2 opens: *"🔴 **Open classification question, registered against this section — `runtime/`.**
The P5.1 amendment … deliberately did **not** add `runtime/` … **The question is resolved by adopting
this section, not by a fourth root.**"* The decision is registered there explicitly.

**2 · Is exclusion of the lease a direct adoption under C-9?** Yes. §7.2 says the question is
resolved *by adopting this section*. Excluding the path resolves the question. That is adoption of a
C-9 clause by another name, which `status_next_review` names as the exact trigger the hold reserves.

**3 · Could P5 legitimately classify the lease independently?** No — and this is the argument I
tried hardest to make work, because it is the one that would have made the candidate incomplete.
It fails on §7.2's own text: the classification is not merely *related* to C-9, it is *registered
against* it as the thing that section resolves.

**4 · Is Plan using C-9 as a genuine boundary or as an excuse?** Genuine. The tell is that Plan
argues P5-B is *"probably right on the merits"* and defers anyway. An actor using a hold as cover
does not first make the case for the thing it declines to do.

**And I checked the hold does not swallow this candidate.** Read literally, *"no governance
modification"* would bar the P5 edit too. It does not, because `status_next_review` scopes the hold
to *"the first governed change that **adopts any clause** of this proposal"* — and empirically,
GOV311, HASHDET, ORCHWT, P51C9, SCIAB and XPORT were all canonicalized after 2026-08-17 without
breaching it. The candidate's own phrasing — *"whose `hold` forbids **adopting any clause**"* — is
the correct scoping, not a convenient one.

```
C-9 §7.2 HOLD                 APPLIES
PLAN DEFERRAL UNDER C-9       CORRECT
```

### 7.1 · The rejected alternative, analysed and NOT adopted

Mirror's task is to test the *reason* for rejection, not to choose policy. I did not adopt P5-B.

| question | finding |
|---|---|
| would exclusion prevent the hazard? | **Yes** — `T2` is the proof: the identical blob in an excluded path leaves the hash fixed |
| auditability preserved? | Yes — `--show-domain` prints every excluded path, so exclusion is visible, not silent |
| historical hashes changed? | **No** — the rule is read from the tip being hashed, so past values stay computable under their own prefix |
| candidate-v4 semantics? | Changed: a new root is a new rule, so the prefix would have to move to `v5` per § P5's own stated principle |
| interaction with `reviews/` protections? | Consistent — same mechanism, one more root |
| migration? | None, by construction |
| invokes the C-9 hold? | **Yes** — §7 above |

```
DOMAIN RECLASSIFICATION            TECHNICALLY_PLAUSIBLE
AUTHORITY TO ADOPT DOMAIN CHANGE   HUMAN_REQUIRED (operator, via C-9 §7.2 closure)
```

Plan's stated reason for rejection — *barred, not merely unattractive* — is the correct
characterisation. Had Plan called it "unattractive" I would have contested it.

---

## 8 · Fingerprint blast radius, calibration and checkpoints

### 8.1 · All four measured in full, at both tips

Computed with the canonical `governance_fingerprint.py` (blob `c6e05e10`, **identical at BASE_HEAD
and at the content tip**) in two clean detached checkouts, both `git status` clean.

| role | OLD (BASE_HEAD `f70878d1`) | NEW (content tip `ceefaa2`) | input difference | rotates? |
|---|---|---|---|---|
| `plan` | `9c0c13fb2cba98bf4facfcb3a99bb75c7b1c21fe72cac087bd82c5b7d8af55ff` | `0d6987bd79e54839cb33052b95bf85116d77c18537c27951fc08eeaefaec1429` | `plan_defined_parameters.md` only (1 of 15) | **YES** |
| `mirror` | `3dff8954d4f6a56f6be14bc72be369095a1436437913a1e908c4b33c9762f65c` | `e01b410891c4f3008b21418f695a4d60514b1810518b3c8d039bc8c6f08a0412` | `plan_defined_parameters.md` only (1 of 16) | **YES** |
| `orchestrator` | `e2c544705e623a7761e627396724aab6fcb5a6f35466e6f1b978a0e8baaec59a` | `88dea7a635919c9faa73506f38a10aa5230011059d646885e86aa1c07b2a5ebb` | `plan_defined_parameters.md` only (1 of 18) | **YES** |
| `scientist` | `82423a48b700bc2b392b4c8e944eb6a0b07cefebddf63db00e96716cbed43e79` | `b66959cd0bb7ccd5c410083fba0107da9157a2b6ddb68c3f86bdbefefc489d1a` | `plan_defined_parameters.md` only (1 of 14) | **YES** |

Full values, not prefixes. All four match Plan's declared prefixes. The per-role `inputs` listings
diff to **exactly one changed line each** — `dc02af72…` → `21d402c5…` — so the rotation cause is
isolated and complete. `SLR-plan-0009.md` is *not* a fingerprint input, so the SLR contributes
nothing to the rotation.

```
CORE FINGERPRINT ROTATION     plan · mirror · orchestrator · scientist  (all four)
```

### 8.2 · Calibration — Mirror's call under P2.3 / A.6

P2.1 hashes each pertinent artifact whole; P2.2 puts `plan_defined_parameters.md` in `CORE`; `CORE`
binds every actor. **The algorithm is doing exactly what it is specified to do.** There is no
misconfiguration and nothing here is a bug.

Whether it is *well calibrated* is a different question, and it is mine. P2.3 states the condition:

> *"The whole body sits in CORE… The body is frozen and changes only by MAJOR governance upgrade,
> where broad invalidation is the correct outcome. **If that stops being true — if the body starts
> absorbing minor edits — the composition is too broad**…"*

P2.3 argues from **frozenness**. `plan_defined_parameters.md` is hashed whole in `CORE` and is, by
construction, the file Plan amends as ordinary business — it is the *opposite* of frozen. The premise
that makes broad invalidation correct for the body does not hold for this file. This candidate is a
clean instance: a correction to two prose sentences, changing no rule and moving no published hash,
rotates every actor's fingerprint.

I record that **Plan was right not to fix it here.** A.6 assigns the two halves separately —
`DETECTION (b)` is *"Mirror monitora il tasso di invalidazioni"*, `RECOVERY (b)` is *"Plan ricalibra
la composizione del fingerprint (modifica governata)"*. Narrowing the composition inside a P5
candidate would be the same overreach §5 correctly declines, and I explicitly do **not** narrow it
here to avoid a rotation.

```
FINGERPRINT CALIBRATION         OVER_SENSITIVE_CANONICAL
FINGERPRINT ROTATION CONSEQUENCE  CARRIED_CALIBRATION_DEBT — not blocking
```

Opened as a Mirror-owned monitoring item, with its first data point: **three CORE rotations are
already visible in the checkpoint record** (`c1d1a9cf` → `37c3b863` → `9c0c13fb`), and this would be
the fourth in the laboratory's short life.

### 8.3 · Checkpoint consequences — precise, and narrower than "all sessions invalid"

A.6's rule is specific and I quote it rather than paraphrase: *"la rehydration che trova
directive_version, generation o **fingerprint** incompatibili NON riprende — segnala e chiede stato a
Orchestrator."*

| axis | consequence |
|---|---|
| **SESSION IDENTITY** | **unaffected.** A fingerprint is not an identity; identity is `ACTOR_ID` + worktree + contract, all durable. |
| **SESSION ROUTABILITY** | **unaffected.** Routing is UNRESOLVED for reasons that have nothing to do with fingerprints. |
| **CHECKPOINT COMPATIBILITY** | **this is the whole of the impact.** On canonicalization, checkpoints recording an old fingerprint may not be silently resumed; rehydration signals and asks Orchestrator. |
| **CURRENT LOCAL WORK** | **unaffected.** Nothing invalidates committed work, branches, or this candidate. |
| **NEW SESSION REHYDRATION** | unaffected — a new session composes the current fingerprint and matches. |

Enumerated rather than assumed: `ledger/checkpoints/` contains **`plan/` only** — 18 at main, 19 on
the candidate branch. **There is no `mirror/`, `orchestrator/` or `scientist/` checkpoint directory
at all.** Of plan's, those recording `9c0c13fb…` (CHK-0009–0014, 0017–0019) become resume-incompatible
on canonicalization; CHK-0001–0008 record `c1d1a9cf…`/`37c3b863…` and are **already** incompatible
from two earlier rotations.

```
CHECKPOINT IMPACT   resume-compatibility only, and only for plan's checkpoints recording 9c0c13fb…
                    Nothing else is invalidated. GOVERNANCE_UPDATE + re-ACK per H.2 on canonicalization.
SCIENTIST A/B       SAFE — and for a stronger reason than "may already be incompatible": no
                    scientist checkpoint exists in the ledger at all, so there is nothing to invalidate.
                    NOT ACTIVATED, unchanged by this candidate.
```

Plan's §7.2 phrase *"invalidating every in-flight checkpoint of every actor"* is true but reads
larger than the measured set, which is one actor's. Non-blocking; recorded so the operator weighing
the §7.2 cost trade weighs the real number.

---

## 9 · Orchestrator surface — **CARRIED**, uncontaminated

Verified only to the depth §17 requires.

```
roles/orchestrator.md frontmatter   worktree: the repository root checkout
roles/orchestrator.md body §35      "Position in the root confers nothing."
deployment_profile.md               | orchestrator | orchestrator — its own worktree | roles/orchestrator.md |
```

The contradiction is real and is internal to one file. **Annex D.1 is not defective**, and Plan does
not say it is: it distinguishes `WORK_COMMIT (ogni attore, proprio branch)` from
`CANONICAL_BATCH_COMMIT (solo Orchestrator, root, gate 0–5)`, which is exactly Plan's §8.1 reading.
D.1 is untouched by this candidate.

```
ORCHESTRATOR EXECUTION SEMANTICS    DETERMINISTIC
ORCHESTRATOR ROUTING-SURFACE DEBT   CARRIED — the candidate changes no file involved in it
```

The complete file set the candidate touches is six, and `roles/orchestrator.md` is not among them
(§13). Nothing about this debt is modified, resolved or silently affected.

### 9.1 · `--cwd` as "the universal set" — **SUPPORTED in its structural half, OVERSTATED as written**

I did **not** re-run the CLI probe: my runtime is 2.1.233 and Plan's observations were taken at
2.1.232, so a re-run from here would not revalidate them and §17 forbids solving resolver semantics
in this review. What I *can* test from durable state is the containment premise the interpretation
rests on — and it does not hold as stated.

```
git worktree list  →  14 worktrees:  7 UNDER the repository root  ·  7 OUTSIDE it
                      (three under /private/tmp/…/scratchpad, four at <HOME>/Desktop/legend-codex-*)
```

*"every worktree lives under the root at `.claude/worktrees/`"* is **false** as a universal. What is
true — and is all the argument needs — is that **every one of the six actor worktrees** named in the
deployment profile (`orchestrator`, `evidence-index`, `mirror`, `lettore`, `lettore-b`, `lettore-c`)
lives under the root. So a root-scoped subtree query still over-matches across every actor, and the
conclusion stands unchanged; the premise as written is broader than the repository.

```
ROOT-CWD INTERPRETATION   SUPPORTED for the conclusion · OVERSTATED in the premise as written
```

Narrowed in curation at §12 rather than treated as a defect of the candidate, because the sentence
lives in a `PROPOSED` learning that Annex E.2 gives me to classify. **The metaphor is not promoted to
normative truth anywhere in § P5**, which is the thing §18 exists to prevent — I checked.

---

## 10 · Invariance, historical compatibility, regression

### 10.1 · Algorithm and domain — UNCHANGED, with a mutation control

```
candidate_content_hash.py    cd5776d329bc7c93d43807aeddaac43752dcbadf
                             IDENTICAL at BASE_HEAD, content tip, manifest tip and branch tip
parse_p5(f70878d1)  →  version legend-candidate-v4 · roots [governance/candidates/, ledger/, reviews/]
parse_p5(ceefaa2)   →  version legend-candidate-v4 · roots [governance/candidates/, ledger/, reviews/]
```

The parse is identical — but an unchanged parse from a parser that cannot see change proves nothing.
**Mutation control:** I injected `- runtime/` into the `CONTROL_PLANE_ROOTS` block at the candidate
tip and re-parsed. The parser returns four roots, the domain moves to **532 included / 41 excluded**,
and the hash becomes `8ae53720…`. The checker demonstrably detects a rule change, so "the rule did
not move" is a measurement and not an artifact. This directly answers Plan's C-1, which flagged that
Plan wrote both the check and the thing checked.

```
P5 ALGORITHM   UNCHANGED
P5 DOMAIN      UNCHANGED
```

Sorting, byte layout and script behaviour are unchanged by construction — the script is the same
blob — and confirmed empirically by route C reproducing its byte-for-byte serialization.

### 10.2 · Historical hash compatibility — **PASS**

| control | base × tip | result |
|---|---|---|
| **POSITIVE** XPORT rev 2 | `4454feab` × `86dfe297` | `81f241f2…6e1f` **= published** |
| **POSITIVE** XPORT rev 2, at its declared `CONTENT_TIP` | `4454feab` × `e839db38` | `81f241f2…6e1f` **= published** |
| **POSITIVE** SCIAB | `cbce3016` × `2a854177` | `beef6db0…6061` **= published** |
| **NEGATIVE** XPORT base × SCIAB tip | both endpoints verified above | `7f35657f…` — differs |
| **NEGATIVE** SCIAB base × XPORT tip | both endpoints verified above | `bf3b9092…` — differs |
| **NEGATIVE** handoff's declared control | `4454feab` × `ceefaa2` | `326b1773…` **= the value the handoff declares**, ≠ candidate hash |

Both negative controls use endpoints I had **independently verified against published values first**,
so neither is a void control derived from an unverified parent. Route C agrees on all six.

`governance/scripts/test_candidate_content_hash.py` passes **7/7 at both tips**.

```
HISTORICAL HASH COMPATIBILITY   PASS
```

### 10.3 · Regression — **DELTA 0**, compared as sets and by reason

Run at both tips in clean detached checkouts.

```
BASE FAILING SET (6)                         CANDIDATE FAILING SET (6)
framework/scripts/test_session_self_eval.py                    identical
scripts/test_abstract_corpus_is_not_evidence.py                identical
scripts/test_fulltext_trace_contract.py                        identical
scripts/test_locator_obligation_reaches_every_route.py         identical
scripts/test_release_runner_verdict.py                         identical
scripts/test_release_surface.py                                identical
```

`diff` of the sorted sets is empty. **Same-reason verified for all six**: each suite re-run at both
tips, stderr normalised only for worktree path and elapsed-time strings, then diffed — identical in
every case. My first extraction over-matched and reported 8 entries; I re-derived with an anchored
pattern and got the true 6. Gates identical at both tips: LINT `VERDICT: PASS` with the same single
pre-existing `[INFO] MISSING_WIKILINK: CLAIM 010`; publication gate `BLOCKS: 0` with the same 4
`[REVIEW]` lines. Both match the manifest's declared `LINT_RESULT` and `PUBLICATION_GATE`.

```
REGRESSION DELTA   0
```

---

## 11 · KEY_OBJECTIONS — findings

### N-1 · The section this candidate hands the decision to still asserts the falsified premise, and the candidate does not say so — **NON-BLOCKING, and the one I came closest to blocking on**

`governance/candidates/PROPOSAL-C9-STATE-MODEL.md` §7.2, canonical at `main`, line 428:

> *"While `runtime/` remains untracked it is absent from the domain and no fixed point arises; the
> standing cost is C-5b… Operator decision of 2026-08-17."*

That is the same falsified premise, **asserted and unrefuted**, in the section whose closure the
candidate defers to and whose transition owner is the operator. Everywhere else in the tree the
sentence appears as a quotation being corrected; here it stands as a live claim.

I searched the candidate's manifest, handoff, SLR, checkpoint `CHK-plan-0019`, task record
`P5DOMAIN-001` and the amended § P5 prose for any note of it. **It is recorded nowhere.** Meanwhile
the amended prose routes the reader to C-9 §7.2 four times, including the load-bearing sentence
*"The debt is recorded with its owner — C-9 §7.2, operator."*

So the operator, sent to §7.2 to decide, arrives at a section that tells them there is nothing to
decide about a fixed point. This is `SLR-plan-0009` L-1 — *a deferral justified by a fact about
another file has acquired a dependency it does not declare* — occurring in the act of recording L-1.

**Why I did not make it blocking.** Three reasons, and I want them checkable. (i) It makes no § P5
sentence false: the candidate's remit is § P5, and § P5 is clean. (ii) C-9's `hold` plausibly bars
Plan from editing §7.2's text, so inaction on the text is defensible. (iii) The remedy is a line in
the carried-debt register — control plane, `governance/candidates/` is an excluded root, so it moves
no hash and forces no re-binding.

**What I require instead of blocking:** this finding must travel into the C-9 §7.2 closure package,
so that whoever closes it knows §7.2's own safety rationale was falsified by `325da04` and measured
false by this candidate. I am carrying it as a Mirror-owned item; an adjudicator who thinks the
register omission is itself disqualifying has everything above needed to disagree with me.

### N-2 · The stale `496` stands in three canonical files, not one — **NON-BLOCKING**

§11 of the manifest carries *"CHK-plan-0018 entry index off by one"*. Verified with a positive
control on the grep instrument (a string I had already read with my own eyes), `496 of 532` appears at
`main` in:

```
governance/candidates/CAND-20260819-XPORT.md:906        a canonical candidate manifest
ledger/checkpoints/plan/CHK-plan-0018.json:76           the checkpoint Plan names
reviews/plan/AUTHOR-RESPONSE-XPORT-MIRROR-001.md:108    a canonical author-response to a Mirror review
```

No XPORT-lineage tip yields 496 of 532: revision 2's tip gives **495 of 532**, revision 1's gives
494 of 531. Correctly **not repaired** — XPORT is canonical and closed, and the value is control
plane and non-operative. The finding is that the debt register under-reports where the wrong number
lives, in a candidate that is otherwise scrupulous about naming owners.

### N-3 · *"GATE 0 is asserted by hand"* is over-broad — **NON-BLOCKING**

§5.1 above. The ACTIVE-singleton condition of GATE 0 is mechanized by `lease_state.py --check`. The
operative claim — no write-location predicate anywhere — is exact and independently established.

### N-4 · *"every worktree lives under the root"* is false as a universal — **NON-BLOCKING**

§9.1 above. 7 of 14 worktrees are outside the root. True of all six actor worktrees, which is what
the argument needs. Handled in curation (§12) since it lives in a `PROPOSED` learning.

### N-5 · `SLR-plan-0009` cites two records that do not exist in canonical state — **NON-BLOCKING, and it is MY debt, not Plan's**

`derived_from: [SLR-plan-0008, SLR-plan-0007, SLR-mirror-0014, SLR-mirror-0015]`, and the body cites
`SLR-mirror-0015` L-2 and `SLR-mirror-0014`'s instrument class. Neither mirror record exists at
`main`, nor on the candidate branch; both exist only on the uncanonicalized `mirror` branch, which
carries 22 of them.

**This is pre-existing and systemic, not introduced here.** Six canonical Plan SLRs at `main` already
cite seven distinct dangling `SLR-mirror-*` IDs (`0009`–`0015`). LINT does not detect it — it passes
with one unrelated INFO. Canonical content therefore reasons from a corpus a reader of `main` cannot
open, and the corpus is Mirror's. Recorded here as a debt I own; blocking Plan for it would be
charging the author for my own unfiled work.

---

## 12 · E.2 curation of `SLR-plan-0009` — Mirror's, and Plan did not self-ratify

Bound and verified: introduced at `ceefaa2`, **absent at BASE_HEAD**, inside the content population
at index **484 of 533** (`learning/` is CONTENT by intent per § P5.1), and committed **before** the
binding was recorded at `dae0cca8`. All three learnings arrive `PROPOSED`, with curation explicitly
declined to me. Its factual counts reproduce — the EVIDENCE block's *"495 of 532 at the XPORT tip and
496 of 533 at this candidate's content tip"* is exactly what I measured, both halves.

```
L-1  A deferral is justified by a premise with a lifetime, and nothing watches it expire.
     proposed ORIGINAL_OBSERVATION  →  CONFIRMED ORIGINAL_OBSERVATION.  Wider scope GRANTED.
     Evidence is this candidate's own history: 325da04 falsified a sentence in another file and
     nothing connected them. The reusable form — state an interim's premise as a runnable check,
     not as an assumed state — is testable and general.

L-2  A run of successes is evidence about the convention followed, not the rule written.
     proposed ORIGINAL_OBSERVATION  →  CONFIRMED ORIGINAL_OBSERVATION, and DISTINCT from
     SLR-mirror-0014.  Plan asked me to decide this and offered the harder reading against itself.
     SLR-mirror-0014 §1 is an instrument that measured NOTHING (a falsifier returning zeros from a
     truncated path). L-2's object is an instrument that measured something REAL — seven clean
     bindings — and answered a question nobody asked. Different failure, different remedy: the
     first is fixed by controlling the instrument, the second by asking what produced the record.
     NOT a REPLICATION.  Wider scope GRANTED.

L-3  An over-matching identity attribute fails in the direction that looks like success.
     proposed ORIGINAL_OBSERVATION  →  REFINED.
     REFINED_FORMULATION: the general claim stands and is well evidenced — 24 rows containing no
     Orchestrator is worse than 0 rows, and the 0 is the honest answer. The supporting premise
     "every worktree lives under the root at .claude/worktrees/" is FALSE as written (§9.1): 7 of
     14 are outside it. Narrow to "every ACTOR worktree named in the deployment profile lives under
     the root", which is verified true and is all the conclusion requires.
     Wider scope GRANTED for the general form; the nesting observation stays laboratory-internal,
     as Plan already proposed.
```

Plan does **not** self-ratify methodology under G.2 anywhere in this record, and the `curation:
PENDING` frontmatter states the constraint before I did.

---

## 13 · Scope — **NONE found**

The complete set of files the candidate changes, base to branch tip:

```
CONTENT (2, in the hash)        governance/plan_defined_parameters.md
                                learning/plan/SLR-plan-0009.md
CONTROL PLANE (4, excluded)     governance/candidates/CAND-20260819-P5DOMAIN.md
                                governance/candidates/HANDOFF-P5DOMAIN-MIRROR.md
                                ledger/checkpoints/plan/CHK-plan-0019.json
                                ledger/tasks/plan/P5DOMAIN-001.json
```

Not touched: `roles/orchestrator.md`, Annex D.1, Annex I.3, `PROPOSAL-C9-STATE-MODEL.md`,
`candidate_content_hash.py`, `lease_state.py`, `runtime/orchestrator_lease.md`, the four scientific
current files, `framework/state/actors.yaml` (still absent), any benchmark artifact.

The candidate branch's lease blob is `c34f4866` — **identical to `main`'s**. No lease row was written
on this branch, so the candidate's own binding is uncontaminated by the hazard it documents.

```
SCOPE CREEP   NONE
```

---

## 14 · Routing holds — verified only far enough to confirm nothing moved

```
C-9 §7.2                              OPEN — ACCEPTED · acceptance_is_not_adoption: true ·
                                      status_transition_owner: operator · hold in force · HUMAN_REQUIRED
BUILD_MINIMAL_DIRECTORY               OPEN — framework/state/actors.yaml still ABSENT at main
                                      (verified by git cat-file), Phase 0 never executed
MULTI_AGENT_ARCHITECTURE_FEASIBILITY  OPEN — PRESERVED, NOT AUTHORIZED, NOT STARTED
E5                                    PARTIALLY_RESOLVED — one negative falsified by
                                      self-observation; the re-run is owed and is not Plan's to close

ROUTING READY                         NO
```

No Candidate B was created. No hold was lifted, narrowed or reinterpreted by this review.

---

## 15 · Instrument discipline — including three of my own near-misses

```
WRONG-REASON LOAD-BEARING PASSES     0
```

Every load-bearing probe carried an expected outcome, an expected reason, a positive control, a
non-void negative control and an independent oracle before its result was read. Specifically checked
and clean: no BSD `sed`/regex trap in a load-bearing path; no shell empty-output equality; no
`timeout` (absent on this platform); no stale script — the one stale copy present was identified and
excluded (§0); no wrong P5 source — the rule is read from the tip being hashed and I verified the
script blob identical across all four commits; no line number mistaken for a population index — the
two `--emit-domain` header lines are exactly the trap and I derived the index with an explicit
population definition; no void negative control — both hash negatives use endpoints verified against
published values first.

**Three instruments of mine failed during this review. All three were caught; none was
load-bearing; recording them is the point.**

1. A falsifier precondition printed `PRECONDITION OK: two blobs differ` when `git rev-parse
   origin/orchestrator:…` had **failed** and the variable held the literal argument string — two
   unequal strings, a true comparison, a meaningless one. Caught immediately; rebuilt to assert each
   value is a real object, of type `blob`, and non-empty **before** comparing. This is
   `SLR-mirror-0014` §1 exactly, and it happened to me while I was reviewing a candidate about it.
2. `git show "$R:runtime/…"` under zsh: `$R:r` is a history modifier, so the ref silently became
   `mainuntime/…`. Caught by the fatal error; fixed with `${R}:`. Had the modifier produced a *valid*
   ref instead of an invalid one, this would have been a silent wrong answer.
3. `git grep -nE '\b496\b'` returned **empty** against a string I had already read with my own eyes
   minutes earlier. `\b` is not portable here. Caught only because the emptiness contradicted direct
   observation; re-run with `-F` and a deliberate positive control seeded from text I had read. **A
   negative from a grep is worthless without a positive control on the same instrument** — which is
   the discipline this candidate's §5 depends on, and I nearly published an absence claim without it.

---

## 16 · VERDICT

```
VERDICT                    ACCEPT
REVIEWER_CONFIDENCE        HIGH on the measurements · MEDIUM on the sufficiency judgement of §6
```

`CONFIRMED` here means *no defect found given the available evidence bundle* — never *true*.

**ACCEPT rests on all of the following, each verified rather than accepted:** the premise conflict
reproduces; the fixed-point hazard reproduces independently, with an isolation control Plan did not
run; the candidate states the hazard and does **not** claim resolution; the mitigation is described
as `PROCEDURAL` and the description is accurate; Plan's absence-of-enforcement claim survives a
nine-instrument search with one subordinate clause narrowed; the C-9 §7.2 hold genuinely bars the
reclassification and does **not** bar this candidate; no hidden domain or algorithm change; published
hashes reproduce under two positive and three negative controls; § P5 carries no false operative
claim; all four fingerprints measured in full with the cause isolated to one input; checkpoint
consequences bounded to resume-compatibility for one actor; Scientist A/B safe; the Orchestrator
debt carried and untouched; routing unresolved; regression delta 0 by set and by reason; the SLR
bound, curated and not self-ratified; scope narrow.

**RESIDUAL_UNCERTAINTY.** (i) N-1 is a judgement call and I say so — I record the reasoning so an
adjudicator can reach the opposite conclusion on the same facts. (ii) §6's sufficiency finding rests
on my reading that a detector *is* the classification; if the operator holds that a detector which
only *reports* a mutation adopts nothing, then P5-D was available now and the candidate under-reacts.
(iii) All probes ran on one machine, one filesystem, one CLI version; my runtime is 2.1.233 and
Plan's `--cwd` evidence is 2.1.232, which I did not revalidate.

**WHAT_WOULD_CHANGE_MY_MIND** (declared falsifier, not rhetoric):

1. **Produce any executable check** — script, hook, CI step, gate, test — that constrains where a
   lease row may be written, or that fails when a candidate's tip mutates a tracked `runtime/` path.
   That falsifies §5, makes the mitigation `HYBRID` or `MECHANIZED`, and makes the candidate's
   central diagnosis wrong. My search is enumerated in §5 so it can be repeated against me.
2. **Show that C-9 §7.2's hold does not reach a domain classification** — e.g. that §7.2 registers
   only *where `CURRENT_SESSION_REF` lives* — and P5-B was available, the deferral is over-broad,
   and this becomes REQUEST CHANGES.
3. **Show a batch ordering that places a lease's terminal row inside the batch that lease
   authorized without failing GATE 0.** That falsifies §3.2's structural claim and my §5.2
   confirmation of it.
4. **Show that adding normative prose about a hazard is itself a rule change** — constraining what a
   candidate may contain — in which case the prefix should have moved to `v5` and the candidate is
   wrong about its own version.
5. **Show any published `CANDIDATE_CONTENT_HASH` that fails to reproduce at the candidate tip.** I
   checked two; a third that moved would refute §10.2.

**AUTHOR_RESPONSE: REQUIRED. Silence is not acceptance (C.2).** N-1 in particular asks for a
decision, not agreement: either record the C-9 §7.2 residual in the carried-debt register, or state
why it should not travel with the closure.

```
HUMAN_APPROVAL      NONE — not granted, not implied, not requested by this review
CANONICALIZATION    NOT PERFORMED — Mirror does not execute (D.1: CANONICAL_BATCH_COMMIT is
                    Orchestrator's, in root, under gates 0–5)
MAIN                f70878d1cb98317ec62808987fc328be7f8f4ea8 — UNCHANGED
BENCH-AB-001        NOT STARTED     SCIENTIST A  NOT ACTIVATED     SCIENTIST B  NOT ACTIVATED
```
