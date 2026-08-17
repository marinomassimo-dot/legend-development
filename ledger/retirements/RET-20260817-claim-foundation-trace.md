---
artifact: RETIREMENT RECORD
record_id: RET-20260817-claim-foundation-trace
object: local branch `claim-foundation-trace`
disposition: RETIRED — NEVER MERGE, NEVER PUSH
deletion: NOT PERFORMED — and not authorised by this record
authored_by: plan
authored_on: 2026-08-17
authority: operator decision of 2026-08-17 — "procedere con retirement record durevole.
  Cancellazione solo successiva."
domain: CONTROL PLANE — ledger/ is a declared CONTROL_PLANE_ROOT (P5.1)
source_of_inventory: orchestrator C-7 inventory, relayed 2026-08-17
---

# `claim-foundation-trace` — retirement record

**This record exists so that the marking precedes the deletion.** The operator's decision was
explicit that the durable mark comes first and deletion only afterwards. Nothing here deletes
anything, and a later deletion needs its own authorisation; this record is the precondition, not
the act.

## Disposition

```
BRANCH        claim-foundation-trace
STATE         local only — never merged, never pushed
COMMITS       3, dated 2026-08-09
DISPOSITION   RETIRED — 🔴 NEVER MERGE, NEVER PUSH
DELETION      not performed, not authorised here
```

## Why it must never be merged or pushed

The branch carries **seven page-crop PNGs of `PMID 17803050`**, a paper that is
all-rights-reserved, has no DOI, no PMCID and no open deposit. Rule 5e of
`gold_is_in_the_details.md` forbids shipping exactly this: *"A page adjudication is published as a
recipe, never as the image. The crop that proves what the author wrote **is** a reproduction of
what the author wrote — the property that makes it evidence is the property that makes it someone
else's to redistribute."*

Merging or pushing this branch would republish copyrighted reproductions. The root `CLAUDE.md`
also records that the privacy gate cannot catch this class: `public_release_gate.py` looks for
patient re-identification and does it well, and **copyright is outside its domain**. So no
automated check would have stopped the push. The marking is the control.

## §42 is satisfied — nothing unintegrated is lost

The branch is retired **with its substance already integrated in compliant form**, which is what
body §42 requires before any `RETIRED` classification: *"mai RETIRED con contenuti non
integrati."*

`main` carries the same evidence as a **recipe rather than a reproduction**:

- `adjudications.json` — **7 crop records** over pages 2, 3, 4, 5 and 8, each with its
  `image_sha256`, source-PDF digest, crop rectangle in PDF points and dpi;
- `regenerate_adjudications.py` — turns that record back into the identical bytes from a reader's
  own copy of the article.

The verification is unchanged; the reproduction is not shipped. That is rule 5e's own resolution,
and it is why retiring the branch loses nothing: the branch held the derived artifact, `main`
holds the derivation.

## What this record does not claim

It does not assert that deletion is safe merely because the substance is integrated. It asserts
that the substance **is** integrated, which is the §42 precondition. Whether to delete, and when,
remains the operator's, and a deletion record would be a separate durable act.

It also does not extend to the other C-7 items. `cf79f1` closed as
`CLOSED_UNIDENTIFIED` — which closes the conflict record and does **not** make `ONE_WRITER` true,
a residual that must travel with the record because the next `GATE 0` will be asserted by a
session that was not present for this one. The `partials` worktree remains `UNRESOLVED`, holding
an untracked session evaluation whose triage belongs to a Scientist under contract. Neither is
dispositioned here.
