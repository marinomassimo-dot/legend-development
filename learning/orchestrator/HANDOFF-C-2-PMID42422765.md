---
artifact: LEGEND — formal handoff record, conflict C-2
conflict_id: C-2
subject: disease-models/wwox/research/deepdive_manifests/PMID42422765.json
governance_version: 3.1.1
prepared_by: orchestrator (BOOTSTRAP_CONTROLLER — no lease held)
prepared_on: 2026-08-17
status: CONTENT RESOLVED · FORWARD OWNERSHIP UNRESOLVED — escalated
authority: none — this record preserves and describes. It assigns no task and binds no actor.
---

# HANDOFF — C-2 · `PMID42422765.json` held dirty by two Scientists

## What the conflict turned out to be

The inventory recorded two Scientist worktrees holding uncommitted edits to the same file, and
flagged it as the two-writers hazard §14 exists to prevent. Measured, it is something milder and
more specific.

```
committed base   lettore     5888cf44be5dc7bf47b6ed3774c1450b1c65bf1f
committed base   lettore-b   5888cf44be5dc7bf47b6ed3774c1450b1c65bf1f   ← same base
working file     lettore     86bba8bb441d7f626768607ed8144c4bcfaec884
working file     lettore-b   86bba8bb441d7f626768607ed8144c4bcfaec884   ← byte-identical
canonical main               b5ee1357384aa36479acd054e61a4d13fe45ba26
```

**There are not two deltas. There is one delta, present three times.** The two working files are
byte-identical and sit on the same committed base — and a third copy of the same blob was already
sitting in `stash@{0}`, put there by Plan on `evidence-index`:

```
stash@{0}: On evidence-index: PLAN base-alignment: superseded PMID42422765 worktree edit,
           preserved before rebase
  → 5888cf4 → 86bba8b, 2 insertions, 2 deletions — the identical blob
```

Plan met this file before either Scientist was looked at, reached the same verdict independently
— *superseded* — and preserved rather than discarded it. Three copies, one delta, and no actor
holds content another does not.

**The stash was not dropped and was not applied.** It is read-only evidence here.

## The delta, in full

```diff
--- base 5888cf44
+++ working 86bba8bb
@@ line 5
-  "receipt": "FTR-20260810-42422765-04",
+  "receipt": "FTR-20260810-42422765-05",
@@ line 7
-   "FTR-20260810-42422765-04",
+   "FTR-20260810-42422765-05",
```

Two lines. A receipt-id bump from `-04` to `-05`, in the `receipt` field and in the `landing`
array. Nothing else in 397 lines changed.

**Leading root-cause hypothesis — testable, and not yet established.** An identical two-line edit
appearing independently in three working directories is better explained by a *tool* than by
three people. A receipt-recording or re-anchoring step run in each worktree against the same base
would produce exactly this, byte for byte, every time. Duplicated human assignment would be
unlikely to land on identical bytes three times. Marked `IPOTESI`: it is worth one question at
registration and one look at whether a routine writer rewrites this field as a side effect.

## Why the content needs no adjudication: canonical history already contains it

`main`'s blob `b5ee1357` reads:

```
line 5:  "receipt": "FTR-20260814-42422765-06",
line 7:   "FTR-20260810-42422765-05",     ← the actors' edit, already canonical
line 8:   "FTR-20260814-42422765-06",
```

The `-05` receipt the two actors added by hand **is already in the canonical file**, and has since
been superseded by a later reading, `FTR-20260814-42422765-06` (2026-08-14). That later reading
also grew the manifest from 397 to 463 lines: six figure artifacts
(`S_p02…S_p07_300dpi.png`, each with its SHA-256) and figure-attestation locators for
Supplementary Figures S1–S4, including the S2 sample-size conflict (`n=5` in the legend against
`n=4` in the caption) and the S1 neuron-specificity gap.

Canonical provenance runs through the `lettore` lineage — `8821500 Merge lettore`, then
`8ce4fa8`, then `0b433b7` — so this content reached `main` by the governed route and was not lost.

**Conclusion: no contribution is at risk, and nothing needs to be merged.** The dirty state is a
stale duplicate of already-canonical content, held on a base 136 (`lettore`) and 138
(`lettore-b`) commits behind `main`.

## What was preserved, and how

Nothing was deleted, overwritten, checked out or stashed. The working files remain exactly where
they are, still modified, in both worktrees.

| Preservation | Location |
|---|---|
| Blob written to the shared object database | `86bba8bb441d7f626768607ed8144c4bcfaec884` |
| Ref protecting it from garbage collection | tag `handoff/C-2/PMID42422765-working-blob` |
| Human-readable copy | `runtime/handoff/C-2/PMID42422765.working.lettore-and-lettore-b.json` |
| Pre-existing third copy, left exactly as found | `stash@{0}` — **not dropped, not applied** |

The blob is reachable by oid and by tag independently of either worktree, so the contribution
survives even if both working trees are later synced or discarded by their own actors.

## 🔴 The hazard that is real, and it is not the one that was flagged

The danger is **not** losing the edit. It is committing it.

Both branches descend from `5888cf44`; `main` also descends from `5888cf44` through `b5ee1357`.
A `WORK_COMMIT` of `86bba8bb` on either branch, followed by a merge into `main`, produces
overlapping changes on lines 5 and 7 of the same file. Git will conflict there — and a resolution
taken in favour of the branch would **regress the canonical manifest**: it would restore
`receipt: -05`, and drop `-06` along with six figure artifacts and four figure-attestation
locators.

That is a silent scientific regression dressed as a routine merge conflict. It is exactly what
two writers on one file produce, and it is why this had to be settled before either actor
registers and receives work.

## Provisional ownership

Split, because the three questions have different answers and only one of them is mine to touch.

| Question | Disposition | Basis |
|---|---|---|
| Ownership of the **content** | **MOOT** — held by the canon | `-05` is in `b5ee1357`, superseded by `-06`; no actor holds unique content |
| Ownership of each **stale working copy** | **each actor owns its own** | One writer per working directory (§14): `lettore`'s copy is `lettore`'s to clear, `lettore-b`'s is `lettore-b`'s |
| Ownership of the **file going forward** | 🔴 **UNRESOLVED — escalated** | Depends on a Task Contract naming a responsible Scientist for PMID 42422765. Assignment is Orchestrator's under an ACTIVE lease (H.1); no lease exists |

**Why the third is not decided here.** Attributing forward ownership would be assigning work, and
this actor holds no lease: the single exemption was scoped to `CAND-20260816-GOV311` and is
consumed. The evidence points at the `lettore` lineage, since the canonical version arrived
through it — but evidence of past provenance is not an assignment, and treating it as one would be
the self-granted authority the governance is built to refuse.

## What each actor must do — recorded, not ordered

These are preconditions to be confirmed at registration (I.2 step 7). They are not Task Contracts
and nobody is assigned anything by this file.

### `lettore` (proposed `scientist-a`)

1. At rehydration, observe: branch 136 commits behind `main`, one modified file.
2. Verify against canonical `main` that the held edit (`-05`) is already present and superseded
   by `-06`. One command: `git diff main -- <path>`.
3. **Do not `WORK_COMMIT` this file.** Committing a superseded receipt id on a stale base is the
   regression path described above.
4. Sync the branch to `main` before any new work. The working-tree edit is then redundant; it is
   preserved at tag `handoff/C-2/PMID42422765-working-blob` regardless of what the actor does.
5. If step 2 shows anything the actor believes is *not* superseded, stop and raise it: that would
   contradict this record, and this record should lose.

### `lettore-b` (proposed `scientist-b`)

Identical, with one difference and one question:

1. Branch is 138 commits behind `main`.
2–5. As above.
6. **Report how the file came to be modified here at all.** The manifest for PMID 42422765 reached
   `main` through the `lettore` lineage; the same two-line edit existing independently in
   `lettore-b` suggests duplicated work rather than divided work. Whether that was a
   double-assignment, a copied working tree, or something else is worth one sentence at
   registration — it is the cheapest possible datum on how the coordination failed, and it will
   be far more expensive to reconstruct later.

### Neither actor

Neither may act on the other's worktree. This record is not authority to do so.

## Residual risk after this handoff

| Risk | State |
|---|---|
| Contribution lost | **closed** — blob preserved by oid, tag and file copy |
| Canonical regression by merge | **open until both branches sync** — the trigger is a `WORK_COMMIT`, which no one has authority to make yet |
| Duplicated-assignment root cause | **open** — one question, to answer at registration |
| Forward ownership | **open** — escalated; needs a lease |

## Escalation

```
ESC-C2-01
QUESTION:  Who owns disease-models/wwox/research/deepdive_manifests/PMID42422765.json,
           and by extension PMID 42422765, once the Scientists are registered?
WHY_NOT_DECIDED_HERE:  Assignment is Orchestrator's under an ACTIVE lease (H.1). No lease
           exists; the CAND-20260816-GOV311 exemption is consumed and does not generalise.
BLOCKS:    nothing before bootstrap step 5. It blocks the first Task Contract touching this paper.
ROUTE:     resolve at bootstrap step 9-10, when a lease exists — or by operator directive earlier.
```
