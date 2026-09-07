---
artifact: ADVERSARIAL REVIEW — LEGEND Operating Convention v1, as drafted in PLAN-EXECUTION-TRANSITION-001
record_id: REV-OPCONV-MIRROR-001
object_under_review: learning/plan/PLAN-EXECUTION-TRANSITION-001.md @ evidence-index worktree, branch plan-orchsurf-r4-transcription HEAD e995edd (untracked, uncommitted)
reviewer_seat: mirror
authoring_session: mirror-87 [103de0] · transcript birth 2026-08-23T15:11:17Z
author_note: >
  This session claims authorship of THIS FILE ONLY. It did not write
  CLASS-DECISION-SURFACE-001.md (claimed by mirror-75) nor the five learning/mirror artifacts
  dated 2026-08-22, which predate this session's transcript. Stated here because F-4 below is
  about exactly this, and a review that demands attribution while omitting its own is worthless.
authored_on: 2026-08-23 (UTC)
dispatcher: operator — "LEGEND Operating Convention v1 — Transition Execution Mandate"
governance_version: 3.1.1 (read at `main`, not exercised)
mode: ADVERSARIAL_REVIEW

STATUS: REVIEW_DELIVERED
ACTIVATION: NOT_REQUESTED
APPROVAL: NOT_GRANTED
AUTHORITY_CLAIMED: none

classification:
  - ADVERSARIAL REVIEW of a PLANNING_ONLY record
  - NOT A DEC · NOT A CAND · NOT A GOVERNANCE CHANGE · NOT AN ACTIVATION
  - NOT A MERGE OR MERGE AUTHORIZATION
  - NO NEW VOCABULARY — every class name and enum quoted from an existing annex

method: >
  This worktree is 65 commits behind `main` and carries the SUPERSEDED § P5 (`legend-candidate-v3`).
  EVERY normative statement below is therefore measured at `main` through `git show main:<path>`,
  never read from this branch. No checkout, switch, reset, clean, stash or branch change was
  performed: the preservation hold in force across the mirror and evidence-index seats is observed.
  Negatives carry positive controls, and controls are run in a DIFFERENT scope from the search
  they validate — a control sharing the flaw of its search cannot detect it (learned the hard way
  this session, at the cost of a retraction).

verdict_note: >
  🔴 Per-axis verdicts below use Annex C.2's enum, which is the only declared verdict vocabulary.
  NO DOCUMENT-LEVEL DISPOSITION TOKEN IS EMITTED. That vocabulary is undeclared — which is F-2,
  and F-2 is not a defect one may assert and then commit oneself.
---

# ADVERSARIAL REVIEW — OPERATING CONVENTION v1

> **The plan is good.** `BUILD ≠ ACTIVATE` is the right axis, the Track A / Track B split is
> correct, and the unbundling of mechanism from normativity is what has been missing. Six of the
> eight Track A items need no decision from anyone and should be built.
>
> This review does not weigh that. It was dispatched to break the convention, and it reports only
> what broke. **Six findings. One changes the execution order and would otherwise be paid for in
> a laboratory-wide invalidation.**

---

## 0 · WHAT WAS ATTACKED, AND WHAT WAS NOT

| Attacked | Not attacked |
|---|---|
| § 2.1 the four-class table | the milestone decomposition M1–M4 |
| § 7 the six determinations D-1…D-6 | the Track A build order |
| § 6 the three-track ordering | the ~2,100-line estimate |
| § 1(b) the "stale, not undecided" evidence | `PLAN-J3-QUEUE-RECONCILIATION-001`, reviewed elsewhere |

The prior decision analysis is **not** reopened. Every finding below is about the plan drafted
today, not about the surface it plans over.

---

## F-1 · THE CONVENTION DECIDES THE PATH OF A CLASS THAT WAS NEVER DECLARED A CLASS

**AXIS: scope of authority · VERDICT: REFUTED** (the claim "no new governance" does not hold for this row)

§ 2.1 assigns `DEC` a canonical path — `governance/decisions/DEC-<YYYYMMDD>-<SLUG>.md` — a writer
(operator) and a lifecycle field. M1.4 then **relocates three `DEC-*` files into that container**,
and § 7's D-6 asks the operator one question about it: *does the convention bind?*

The question that is not asked is whether `DEC` is a governance object class at all.

```bash
git grep -n -iE "governance/decisions|record_type: *OPERATOR_DECISION" main \
  -- 'governance/GOVERNANCE_v3.1.1.md' 'governance/annex_*.md' \
     'governance/plan_defined_parameters.md' 'framework/**' 'roles/**'
# → 0 hits.   Control, same scope, same invocation: HUMAN_APPROVAL_QUEUE → 3 hits.
```

`governance/decisions/` has no normative basis. It was created by the first record that needed
one, and every later record cites that first act as its warrant — a chain the records themselves
describe as *"a proposed convention exercised, not a legislated one."*

🔴 **Answering D-6 with (b) — "bind, report-only, relocate" — silently answers a question that was
never put to the operator.** Once three `DEC-*` files are moved *into* `governance/decisions/` by
an authorized act, the container is ratified by the strongest available means, and the class
question can no longer be asked cleanly: the answer will already be on disk. This is the precise
failure the surface analysis named — *deciding path before class produces a container that defines
its own contents* — and the plan reproduces it while believing it is only tidying.

**MINIMUM FIX, and it costs one row:** add **D-0 — *is `DEC` a class, or must an operator decision
be expressed through an object the governance already defines (J.3 queue entry, candidate
manifest, review)?*** — ahead of D-6, and make M1.4 conditional on it. Until D-0 is answered, § 2.1
should carry `DEC` as `CLASS: PROPOSED — no canonical path` rather than as a row indistinguishable
from `CAND` and `REVIEW`, whose classes *are* defined (D.2, C.2). Three of the four rows are
descriptions of existing law. The fourth is a proposal wearing the same typography.

---

## F-2 · THE REVIEW ROW OUTLAWS THE EVIDENCE THE PLAN ITSELF RELIES ON

**AXIS: internal consistency · VERDICT: REFUTED**

§ 2.1 fixes REVIEW's lifecycle field as `verdict:` — *"C.2 vocabulary only
(`CONFIRMED · WEAKENED · REFINED · REFUTED`)"*. Measured at `main`:

```bash
git show main:governance/annex_c_review_protocol.md | grep -n VERDICT
# 40: VERDICT: CONFIRMED | WEAKENED | REFINED (+REFINED_FORMULATION) | REFUTED
```

Now the two artifacts § 1(b) uses to establish that `plan_defined_parameters.md` and
`cross_session_transport.md` have satisfied their activation conditions — the evidence D-3 is
decided on:

```
reviews/mirror/REV-P5DOMAIN-MIRROR-001.md:15   verdict: ACCEPT
reviews/mirror/REV-P5DOMAIN-MIRROR-001.md:888  VERDICT      ACCEPT
reviews/mirror/REV-XPORT-MIRROR-002.md:15      verdict: ACCEPT
```

🔴 **`ACCEPT` is not in C.2's enum.** Adopt § 2.1 as written and the two reviews that carry D-3's
evidence become non-conformant to the convention adopted in the same session — together with
every document-level disposition the D.2 manifest and the J.3 queue actually cite: `REQUEST
CHANGES` (17), `ACCEPT` (7), `REVISION_REQUESTED`, `BINDING VERIFIED`, `PASS_WITH_NOTES`,
`COMPLIANT`, `FAITHFUL`, `NOT ATTESTED`.

The confusion is structural, not clerical: **C.2's enum is a PER-AXIS verdict** (measured: used as
such at 7 loci in 4 files) **and the tokens above are DOCUMENT-LEVEL dispositions.** They are two
different objects. One is declared; the other is in daily use and declared nowhere. One operator
scoped ruling has already been spent on this gap, and that ruling forbids its own generalization
while noting *"repeated scoped rulings indicate a possible schema design issue."*

**MINIMUM FIX:** split the row. `VERDICT` = C.2 per-axis, unchanged. `DISPOSITION` = document-level,
vocabulary **undeclared**, marked as such, and referred to the operator as a seventh determination
(this is the omitted D-7 of the surface analysis, which the six determinations also drop). The
convention must not silently pick one of the three vocabularies in use by writing only one of them
into a table.

---

## F-3 · 🔴 D-3(a) COSTS A LABORATORY-WIDE CHECKPOINT INVALIDATION, THROUGH A DEFECT ANNEX A.6 ALREADY NAMES

**AXIS: unstated consequence · VERDICT: REFINED** (the determination is right; its sequencing is not)

This is the finding that changes the plan.

D-3's recommended option (a) is *"confirm normative, **correct the stale status line**"* in
`governance/plan_defined_parameters.md`. That reads as a one-line cosmetic repair. It is not.

**Step 1 — that file is hashed WHOLE, in CORE, for every role.** Measured today in
`governance/scripts/governance_fingerprint.py`: `_digest()` receives it with no `#section`
suffix, so any byte anywhere in it moves the digest. The same § P2.2 splits Annex J into four
separately-hashed sections and explains why in its own prose — *"Annex J is deliberately split
rather than hashed whole"* — and does not apply that discipline to itself.

**Step 2 — measured consequence, both trees:**

```
inputs --role mirror, my tree vs main:  14 inputs, exactly ONE differs
<  278606288ecf…  governance/plan_defined_parameters.md
>  21d402c53360…  governance/plan_defined_parameters.md
mirror fingerprint  84d2b841… (this tree)   vs   e01b4108… (main)
```

Every annex, the body, and `roles/mirror.md` are byte-identical. Mirror's own pertinence set —
Annex C, E, F, G, J § J.1 — did not move at all. The fingerprint moved anyway, because of a
change to **P5**, a parameter in Plan's delegation and in nobody's pertinence set.

**Step 3 — what a moved fingerprint does.** 19 checkpoints on `main` carry
`APPLICABLE_GOVERNANCE_FINGERPRINT` (measured; values cluster `c1d1a9cf…`, `37c3b863…`,
`9c0c13fb…`). Annex A.6's rejection rule, verbatim at `main`:

> *"la rehydration che trova directive_version, generation o **fingerprint** incompatibili NON
> riprende — segnala e chiede stato a Orchestrator. Una modifica di governance NON pertinente
> (fingerprint invariato) non invalida il checkpoint."*

So the intended behaviour is explicit: a non-pertinent change **must not** invalidate a
checkpoint. Under the current composition it does — every checkpoint of every actor, on one
status-line edit. And the recovery route A.6 prescribes is *"richiesta stato a Orchestrator"*,
with **0 ACTIVE leases** measured: there is no Orchestrator to ask.

**Step 4 — and A.6 already anticipated this exact defect and assigned its remedy.** Same annex,
FAILURE / DETECTION / RECOVERY block, verbatim:

> FAILURE: *"(b) composizione del fingerprint **mal calibrata: troppo larga → invalidazioni
> inutili**, troppo stretta → ripresa sotto regole cambiate"*
> DETECTION: *"(b) **Mirror monitora il tasso di invalidazioni**"*
> RECOVERY: *"(b) **Plan ricalibra la composizione del fingerprint (modifica governata)**"*

The composition is calibrated too wide. Mirror detected it, which is Mirror's assigned detection
duty. Recalibration is Plan's, as a governed change — **already authorized in shape by a FROZEN
annex, so it needs no new governance and invents nothing.**

**MINIMUM FIX — a sequencing change, not a new decision:** recalibrate the composition (hash
`plan_defined_parameters.md` **by section** in CORE, exactly as § P2.2 already does for Annex J)
**before, or in the same act as, D-3(a).** Recalibrating first makes the status-line correction
non-pertinent for every role whose set excludes P5 — which is all of them — and the invalidation
never happens. Recalibrating after means paying it for nothing.

Note this is *constructive*: the recalibration belongs in Track A's spirit (a mechanism, testable,
reversible), differing only in that A.6 classes it a governed change. It should be added as
**M1.5**, and D-3 should be decided *after* it, not before.

---

## F-4 · THE OWNERSHIP RULE ASSUMES AN IDENTITY MECHANISM THE LABORATORY DOES NOT HAVE

**AXIS: attribution · VERDICT: WEAKENED**

§ 2.1's REVIEW row: `reviews/<ACTOR_ID>/`, writer *"that reviewer, that directory, nobody else."*

Measured today, in this seat:

```
ACTOR_ID `mirror` registered to  mirror-9c [3940a9], socket 6826, worktree head 0933615
                                 — not live; absent from every peer list read today
live sessions on the mirror seat  4  (mirror-87, mirror-75, mirror-1b, mirror-42)
reviews/mirror/ this worktree     ≥2 distinct authoring sessions
untracked artifacts, mirror seat  6 → 1 claimed (mirror-75), 5 unclaimed
across both seats                 12 → 3 claimed, 9 unclaimed
```

`<ACTOR_ID>` names a **seat**, not a session. N concurrent sessions writing one seat directory
with no writer discipline is the identical topology that forked
`ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl` into three lineages — the defect M2 exists to repair.

🔴 **The plan prescribes the correct cure for approvals and does not apply it where the same
condition is already live.** D-1's recommendation (b) — per-actor files consolidated by replay,
*"the smallest change that cannot re-fork"* — is right, and `reviews/<ACTOR_ID>/` is a shared
multi-writer surface today, with nine unclaimed artifacts as the evidence.

Note what is NOT claimed: no lost work, and no third writer. Every unclaimed file may well have a
live author who simply has not been asked. **Unclaimed, not unknown-authored** — the distinction
matters, and the escalation now carries it correctly.

**MINIMUM FIX, two lines in the convention:**
1. every class artifact carries, in its own frontmatter, `authoring_session` and the session's
   transcript birth instant — the one identity that is append-only, never copied, and machine-
   checkable (`~/.claude/projects/<proj>/<session-id>.jsonl`);
2. the convention states which of {seat, session} owns a class directory. If seat, it needs the
   same one-writer topology D-1(b) prescribes. Ownership must not be resolvable only through a
   registry whose sole `mirror` row names a session that no longer exists.

This review practises (1) in its own frontmatter rather than only recommending it.

---

## F-5 · `artifact_class_map.py` AS SPECIFIED CANNOT SEE THE ID DEFECT THAT ALREADY EXISTS

**AXIS: mechanism adequacy · VERDICT: WEAKENED**

M1.1's stated scope is *"path ⇄ class ⇄ ID-prefix consistency."* Measured across all 43 heads:

```
governance/candidates/DEC-20260817-006-GOV-SCOPE-RESOLUTION.md
governance/candidates/DEC-20260817-006-L2-SCOPE.md
```

Same id stem `DEC-20260817-006`, different content, same container. **Both pass a prefix check.**
The validator built to close the convention's gaps would report these two as conformant on the
axis it measures, and no rule anywhere requires id uniqueness.

Second, smaller, same row: `<YYYYMMDD>` has **no declared timezone**. This repository produced
three local-vs-UTC timestamp errors in a single hour today, across three independent sessions, all
from the same macOS `stat -f '%Sm'` idiom. A date-stamped identifier minted on a CEST box disagrees
with its own UTC date for anything written after 22:00Z.

**MINIMUM FIX:** add id-uniqueness (per class, across all refs) to M1.1's checks, and declare the
date component UTC in § 2.1. Both are cheap now and expensive after the ids multiply.

---

## F-6 · THE MANDATE ASKS FOR PRESERVATION RULES; THE PLAN HAS NONE

**AXIS: completeness against the dispatch · VERDICT: CONFIRMED** (the gap is real and is not a defect of what was written)

The operator's mandate lists, among the minimum contents of Operating Convention v1,
**preservation rules**. `PLAN-EXECUTION-TRANSITION-001` addresses actor rules, artifact ownership,
dispatch, handoff, review and escalation. Preservation is absent — reasonably, since the plan
predates today's incident.

The incident is the requirement's justification, and it is measured: twelve completed artifacts
across two seats exist **only** in working trees, nine of them unclaimed, one of them 1,149 lines;
two sessions independently made out-of-repo copies and declared them; a hold on
checkout/switch/reset/clean/stash is currently the only thing protecting them; and both
preservation idioms in use — `cp -p` and `git archive`/`tar` — **forge filesystem timestamps**
(the first preserves the source's mtime *and* birthtime, the second stamps the commit's), so the
filesystem cannot afterwards say when the work happened or who did it.

**MINIMUM RULE, one sentence:** a completed artifact is either committed by its author's seat, or
declared with `{path, sha256, byte length, authoring session, transcript birth}` in a location
outside the working tree — and no preservation claim rests on mtime or birthtime, in either
direction.

---

## 7 · SUMMARY

| # | finding | axis verdict | blocks | minimum fix |
|---|---|---|---|---|
| F-1 | `DEC` path decided, class never declared; M1.4 ratifies the container | REFUTED | M1.3 row 1, M1.4, D-6 | add **D-0** ahead of D-6; mark `DEC` `CLASS: PROPOSED` |
| F-2 | REVIEW row's enum outlaws `ACCEPT`, the token D-3's own evidence carries | REFUTED | M1.3 row 3 | split `VERDICT` (C.2, per-axis) from `DISPOSITION` (undeclared); refer as **D-7** |
| F-3 | D-3(a) invalidates 19 checkpoints for every actor, via A.6 FAILURE (b) | REFINED | **ordering of D-3** | add **M1.5** fingerprint recalibration; decide D-3 after it |
| F-4 | `reviews/<ACTOR_ID>/` is a shared multi-writer surface; 9 artifacts unclaimed | WEAKENED | M1.3 row 3 | session identity in frontmatter; declare seat-vs-session ownership |
| F-5 | id-prefix check passes a live duplicate id; `<YYYYMMDD>` timezone undeclared | WEAKENED | M1.1 | add id-uniqueness; declare UTC |
| F-6 | preservation rules absent from a mandate that requires them | CONFIRMED | convention completeness | one declaration rule; never mtime |

**None of the six blocks Track A.** F-3 changes the order of one Track B item and adds one Track A
item. F-1 and F-2 add two determinations to a session already convened for six — the marginal cost
of asking them is one paragraph each; the cost of not asking is that both get answered silently by
the first artifact that lands.

**What this review did not do:** did not decide D-0…D-7 · did not activate anything · did not
modify any schema, enum or frozen text · did not emit a document-level disposition · did not
commit itself, and does not hold the `WORK_COMMIT` act for this file · did not touch the object
under review, which belongs to another seat · did not reopen the surface analysis.

END OF REVIEW.
