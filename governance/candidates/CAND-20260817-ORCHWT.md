---
artifact: INTEGRATION_CANDIDATE manifest (Annex D.2)
candidate_id: CAND-20260817-ORCHWT
governance_version: 3.1.1
change_class: MAJOR
prepared_by: plan
prepared_on: 2026-08-17
state: READY FOR MIRROR HOSTILE REVIEW
scope: deployment/deployment_profile.md ONLY. No P5.1 change, no runtime classification,
  no SLR integration, no lint change.
origin: split from CAND-20260817-P51C9 per REV-P51C9-MIRROR-001 finding F-1
---

# INTEGRATION_CANDIDATE — Orchestrator worktree

## 1 · Manifest (Annex D.2)

```yaml
CANDIDATE_ID:               CAND-20260817-ORCHWT
BASE_HEAD:                  908197ba62a064546f17c9c277ff497ffc753656
BRANCH:                     orchestrator-worktree
BRANCH_TIP:                 ab4856b1d90c4361f63705f487d5285c54ecba0e
CANDIDATE_CONTENT_HASH:     280dc4973cf046123a3356ebdf3e8ae2e575b83d6cce9e8b7b58987f2065763d
CANDIDATE_HASH_VERSION:     legend-candidate-v3   ← see §1.2, this is not an error
CHANGE_CLASS:               MAJOR
LINT_RESULT:                PASS
PUBLICATION_GATE:           PASS / BLOCKS: 0
MIRROR_REVIEW:              PENDING
HUMAN_APPROVAL:             PENDING
SNAPSHOT_ID:                n/a until canonical execution — GATE 4 belongs to Orchestrator
```

### 1.1 · Reproduction — one command, run twice

```bash
python3 governance/scripts/candidate_content_hash.py \
  --base 908197ba62a064546f17c9c277ff497ffc753656 \
  --tip  ab4856b1d90c4361f63705f487d5285c54ecba0e --show-domain
```

```
EXPECTED          280dc4973cf046123a3356ebdf3e8ae2e575b83d6cce9e8b7b58987f2065763d
OBTAINED (run 1)  280dc4973cf046123a3356ebdf3e8ae2e575b83d6cce9e8b7b58987f2065763d
OBTAINED (run 2)  280dc4973cf046123a3356ebdf3e8ae2e575b83d6cce9e8b7b58987f2065763d
DOMAIN            504 included · 11 excluded, as produced at this tip
```

### 1.2 · Why this candidate hashes under v3 while P51C9 hashes under v4

Not an inconsistency, and worth stating before a reviewer treats it as one. **A candidate is
hashed under the governance its own `BASE_HEAD` carries.** This branch is cut from `main`, where
`plan_defined_parameters.md` still declares `legend-candidate-v3` and two control-plane roots.
`CAND-20260817-P51C9` is precisely the candidate that changes that definition, so it — and only it
— hashes under v4.

**Consequence for ordering:** whichever candidate executes first moves the other's `BASE_HEAD`, and
the second must be re-based and re-hashed before its approval can bind under gate 5. That is not a
defect of the split; it is what independent review surfaces cost, and it is cheaper than the
coupling the split removed.

### 1.3 · SOURCE_COMMITS

| # | Commit oid | Ancestry | Subject |
|---|---|---|---|
| 1 | `ab4856b1d90c4361f63705f487d5285c54ecba0e` | **PASS** | The Orchestrator gets a worktree, on its own branch and nothing else |

Verification: `git merge-base --is-ancestor ab4856b1 ab4856b1` → PASS. Single commit, cut directly
from `BASE_HEAD`, no rebase in its history.

Blob identity: `deployment/deployment_profile.md` at `ab4856b1` →
`git rev-parse ab4856b1:deployment/deployment_profile.md`.

---

## 2 · CHANGE_CLASS: MAJOR — and why the smaller cascade does not downgrade it

`Annex D` and body §12 make a change MAJOR when it touches **governance, authority or the gate
model**, not when it touches many files or rotates many hashes. This candidate rotates **no**
fingerprint and invalidates **no** checkpoint — and it alters the deployment contract that says
where the actor holding `CANONICAL_BATCH_COMMIT` authority resides. That is an authority-surface
change.

**Declared explicitly so it is not downgraded later:** the absence of a fingerprint cascade is not
evidence of a small blast radius. It is evidence that this change is orthogonal to the fingerprint
mechanism. Under body §12 a doubtful classification resolves to MAJOR fail-closed, and this one is
not doubtful.

---

## 3 · F-2 · Governance reconciliation — **OPTION B: FORMAL DIVERGENCE**

### 3.1 · The conflicting text, quoted first

Revision 1 argued this change from `Annex D.1` and §14 — both of which support it — and quoted
neither of the clauses that resist it. That was F-2. The resisting text:

> **§8** — *"Orchestrator vive nella chat grafica associata a `<REPO_ROOT>` (valore concreto nel
> DEPLOYMENT_PROFILE, Annex I) — l'unico ruolo che esegue CANONICAL_BATCH_COMMIT."*

> **§0.2** — *"La prima chat aperta in `<REPO_ROOT>` NON è Orchestrator per il fatto di trovarsi
> lì… La stessa chat viene promossa; non servono due chat root."*

> **§47 step 9** — *"chat root in BOOTSTRAP_MODE: protocollo Annex I…"*
> **§47 step 14** — *"promozione: BOOTSTRAP_CONTROLLER → ACTIVE_ORCHESTRATOR (lease ACTIVE)"*

And the supporting text, for completeness:

> **Annex D.1** — *"WORK_COMMIT (ogni attore, proprio branch — obbligatorio, non canonico)"* ·
> *"CANONICAL_BATCH_COMMIT (solo Orchestrator, root, gate 0–5)"*
> **§14** — *"ONE_WRITER_PER_WORKING_DIRECTORY… Critico nella root."*

### 3.2 · Why OPTION A cannot be proven, stated plainly

Option A would require showing that §8's *"chat grafica associata a `<REPO_ROOT>`"* names a
**session location** while the deployment profile's `Worktree` column names a **filesystem
boundary**, and that the two are different concepts.

**In this deployment they are the same concept.** A chat has exactly one working directory, and
that directory is simultaneously where the session lives and where its writes land. There is no
observable difference to appeal to. Worse for Option A, §0.2 and §47 do not merely permit the
Orchestrator to be the root chat — they describe the root chat being **promoted in place**, with
*"non servono due chat root"* stating that no second root chat is needed. The frozen text does not
just place the Orchestrator in the root; it describes how it gets there.

So the compatibility argument would have to reinterpret §8 rather than apply it, and R3 forbids
that. **Option A is not available.**

### 3.3 · What §0.2 *does* give — it narrows the divergence, it does not remove it

*"La posizione nella root NON conferisce autorità."* This is the strongest available argument and
it does real work: it establishes that the Orchestrator's authority derives from the **role and
the ACTIVE lease**, never from its location. Therefore moving where it works cannot move what it
may do.

That converts a broad conflict into a narrow one. §8's sentence has two independent clauses, and
only the first is touched:

| §8 clause | Status under this candidate |
|---|---|
| *"vive nella chat grafica associata a `<REPO_ROOT>`"* | **DIVERGES** |
| *"l'unico ruolo che esegue CANONICAL_BATCH_COMMIT"* | **UNCHANGED** |

### 3.4 · The divergence, in C-9 §9.3 form

```
EXISTING RULE
  §8       the Orchestrator's chat is the one associated with <REPO_ROOT>
  §0.2     the root chat is promoted in place; a second root chat is not needed
  §47 9/14 the bootstrap controller is a root chat, promoted to ACTIVE_ORCHESTRATOR

PROPOSED OPERATIONAL RULE
  the Orchestrator's chat is associated with the worktree `orchestrator`
  the root is entered only inside a canonical batch window
  deployment_profile.md records `orchestrator` as its worktree

CONFLICT
  direct, and on the residence clause only. §8 places the chat in the root; this places it
  elsewhere. §0.2's promotion-in-place describes a root chat becoming Orchestrator, which under
  the proposed rule would then have to move.

REASON
  Annex D.1 gives WORK_COMMIT to an actor's own branch. The root's branch is `main`, and a commit
  to `main` is a CANONICAL_BATCH_COMMIT by definition. An Orchestrator resident in the root
  therefore has NO branch on which a WORK_COMMIT is possible — uniquely among six actors. Its
  output cannot become durable, cannot reach an integration candidate, and accumulates as
  untracked files that keep the root unclean, so GATE 0 fails from its first durable output
  onward. §8 itself obliges it to produce durable output: it maintains the DAILY_BRIEF and
  records every adjudication rationale. The frozen text therefore requires an artefact it gives
  the actor no lawful way to persist.

  Secondarily and positively: §14 calls ONE_WRITER "critico nella root". Under the existing rule
  the root has a standing writer at all times; under the proposed rule it has one only inside a
  batch window.

WHAT IS NOT CHANGED
  · root authority — unchanged; §0.2 already denies that location confers it
  · CANONICAL_BATCH_COMMIT — remains root-only and Orchestrator-only
  · the ORCHESTRATOR_LEASE requirement — unchanged, and still the source of authority
  · gates 0–5 — unchanged
  · §47's promotion sequence — the promotion still happens; only the promoted chat's residence
    afterwards differs

ADOPTION DECISION REQUIRED
  Operator, under H.1. This candidate does not adopt the divergence by declaring it. If the
  operator prefers to preserve §8 literally, the alternative is to amend §8 in the frozen text,
  which is a larger act and is not proposed here.
```

### 3.5 · A note on the STOP condition, raised rather than resolved

The instruction reads *"If Option A cannot be proven from existing text: STOP. Do not patch around
the conflict."* — immediately after offering Option B for exactly that case. Two readings are
available: STOP the candidate entirely, or STOP the compatibility route and declare divergence.

This candidate takes the second, because Option B is offered as the alternative when compatibility
fails, and because declaring a divergence is the opposite of patching around it. **If the operator
meant the first reading, this candidate should be withdrawn rather than reviewed**, and Plan is
flagging the ambiguity here rather than resolving it silently — which would be the very move §3.2
declines.

---

## 4 · R4 · Operational proof contract — defined, not executed

`CONFIGURED != PROVEN`. Nothing below is run by Plan; execution belongs to the Orchestrator and
the operator.

```
PROBE-ORCHWT-001 · can the Orchestrator create a WORK_COMMIT in its assigned worktree?

INPUT
  · the Orchestrator chat, operating in the worktree `orchestrator`
  · a minimal test artifact, e.g. ledger/probe/PROBE-ORCHWT-001.md, content immaterial

EXPECTED
  1. a WORK_COMMIT is created on the branch `orchestrator`, non-canonical
  2. branch ownership correct — `git rev-parse --abbrev-ref HEAD` returns `orchestrator`,
     not `main`
  3. NO root contamination — `git -C <REPO_ROOT> status --porcelain` unchanged before and after,
     measured, not assumed
  4. the commit is reachable: `git merge-base --is-ancestor <commit> orchestrator` → PASS

FAILURE BRANCH
  If the probe fails — the chat cannot commit outside the root, or the root is perturbed — then
  the architecture requires, and the candidate must say so explicitly:
    · the Orchestrator chat operates in its own worktree as its normal residence
    · the root is visited only during a canonical batch window
  and that becomes an explicit divergence from §8 of the same kind declared in §3.4, rather than
  an operational inconvenience to work around.

WHAT THE PROBE DOES NOT ESTABLISH
  It does not prove the divergence is correct, only that the arrangement it proposes is
  achievable. A green probe with an unratified divergence is CONFIGURED, not AUTHORISED.
```

---

## 5 · Execution ordering — recommendation

Plan recommends, and does not decide:

1. **Neither candidate can execute today.** `GATE 0` requires a clean root; the root holds nine
   untracked files; no lease exists and the one-commit exemption is spent; L2 is suspended.
2. **The nine files must leave the root before any canonical batch**, and this candidate is what
   gives them somewhere lawful to go. Creating a worktree and moving untracked files is an
   **operational act, not a commit** — so it can precede the canonical commit that records it.
   That ordering should be stated openly rather than discovered: the arrangement is established
   operationally, then legitimised by this candidate.
3. **`ORCHWT` before `P51C9`.** ORCHWT is the smaller change, carries no cascade, and unblocks the
   root-clean precondition both candidates need.
4. **The second candidate re-bases and re-hashes.** Whichever executes first moves the other's
   `BASE_HEAD` (§1.2). If ORCHWT goes first, `P51C9` must be re-based onto the new `main` and its
   hash recomputed **under v4** before its approval binds.

---

## 6 · Verification record

| Check | Command | Result |
|---|---|---|
| Candidate hash | the published command, twice | identical `280dc497…65763d` |
| Source-commit ancestry | `git merge-base --is-ancestor` | 1 of 1 PASS |
| Scope | `git diff --stat main..ab4856b1` | one file: `deployment/deployment_profile.md` |
| Base alignment | branch cut from `BASE_HEAD` | 0 behind |
| Structural LINT | `legend_lint.py .` | `PASS` |
| Publication gate | `public_release_gate.py` | `PASS`, `BLOCKS: 0` |
| Fingerprints | `governance_fingerprint.py compose --all` | **unchanged** — this candidate touches no CORE artifact |
| No history rewritten | branch created from `main`, single commit | no rebase, amend or force push |

**NO CANONICAL_BATCH_COMMIT EXECUTED.** Preparation only.
