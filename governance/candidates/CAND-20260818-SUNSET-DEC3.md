---
artifact: INTEGRATION_CANDIDATE manifest (Annex D.2)
candidate_id: CAND-20260818-SUNSET-DEC3
revision: 2 — remediation of REV-SUNSET-DEC3-MIRROR-001 (473bec9e): the blocking singleton
  fail-open, and both recorded findings
governance_version: 3.1.1
change_class: MAJOR
prepared_by: plan
prepared_on: 2026-08-18
state: READY FOR MIRROR RE-REVIEW
scope: sunset of DECISION 3 — the interim git-ignored lease seat. Scope A–G of
  HANDOFF-SUNSET-DECISION3.md, not reduced and not widened.
---

# INTEGRATION_CANDIDATE — sunset of `DECISION 3`

## 1 · Manifest (Annex D.2)

```yaml
CANDIDATE_ID:               CAND-20260818-SUNSET-DEC3
REVISION:                   2
BASE_HEAD:                  f5b321556e5f1f081482f13fbbabb4f90f3d6295
BRANCH:                     sunset-decision3
BRANCH_TIP:                 234c8bae2a33b7376e4015049793b1f3a30b9c9b
CANDIDATE_CONTENT_HASH:     e7036a1fca7a63d41121b52b8ab33dd5cc5a104dcd6f104b426603dfd4f2e8e9
SUPERSEDED_HASH:            48d4f3a7d96f5bda4c4c219486d83861e51d4666665b53bd255002b045bcd9a0
                            — superseded BY DEFECT (blocking singleton fail-open), NOT by
                              re-baseline. DO NOT REVIEW revision 1.
CANDIDATE_HASH_VERSION:     legend-candidate-v4
CHANGE_CLASS:               MAJOR
LINT_RESULT:                PASS
PUBLICATION_GATE:           PASS / BLOCKS: 0
MIRROR_REVIEW:              REQUEST CHANGES on revision 1 (REV-SUNSET-DEC3-MIRROR-001) —
                            re-review of revision 2 requested
HUMAN_APPROVAL:             NONE — not requested, not granted, not implied
SNAPSHOT_ID:                n/a until canonical execution — GATE 4 belongs to Orchestrator
```

**`CHANGE_CLASS: MAJOR`**: it changes where a `GATE 0` input lives and how its state is
determined.

### Reproduction

```bash
python3 governance/scripts/candidate_content_hash.py \
  --base f5b321556e5f1f081482f13fbbabb4f90f3d6295 \
  --tip  234c8bae2a33b7376e4015049793b1f3a30b9c9b --show-domain
```

```
EXPECTED          e7036a1fca7a63d41121b52b8ab33dd5cc5a104dcd6f104b426603dfd4f2e8e9
OBTAINED (run 1)  e7036a1fca7a63d41121b52b8ab33dd5cc5a104dcd6f104b426603dfd4f2e8e9
OBTAINED (run 2)  e7036a1fca7a63d41121b52b8ab33dd5cc5a104dcd6f104b426603dfd4f2e8e9
```

Domain counts are **outputs of that command at that tip**, never maintained constants — read
them from `--show-domain` rather than from this manifest.

**Manifest tip vs content tip.** This manifest revision is written at a later commit than
`234c8bae`. `governance/candidates/` is a declared `CONTROL_PLANE_ROOT`, so the hash is identical
at both — §7 records the measurement rather than asserting the property.

> **`BRANCH_TIP` names *the tip after the content changes*, not a tip free of control plane.**
> Verified: the r1 manifest **is present** at `234c8bae`, and **was absent** at r1's content tip
> `325da043`. So the two revisions demonstrate hash invariance by **different routes** —
> r1 that *adding* the manifest moves nothing, r2 that *revising* it moves nothing. Both hold;
> they are not the same demonstration, and a reviewer should not have to re-derive which one
> a given tip supports. *(Raised by Mirror, `REV-SUNSET-DEC3-MIRROR-002`.)*

## 2 · File list and classification

| File | Status | Domain | Classification |
|---|---|---|---|
| `runtime/orchestrator_lease.md` | **added** | CONTENT — hashed | **RUNTIME** — the lease record itself |
| `framework/scripts/lease_state.py` | **added** | CONTENT — hashed | **NORMATIVE (tooling)** — it decides a `GATE 0` input; it is not documentation |
| `deployment/deployment_profile.md` | modified | CONTENT — hashed | **NORMATIVE** (§ lease seat retirement) + **DOCUMENTATION** (§ *Current instance — status*) |
| `governance/candidates/CAND-20260818-SUNSET-DEC3.md` | added | **CONTROL PLANE — excluded** | this manifest |

```
content   3 files · +424 / −5      diff total  4 files, the fourth being this manifest
no file deleted · no history rewritten
```

**No governance text is amended.** `I.3` is *satisfied* here, not edited. The only file under a
control-plane root is this manifest, which by construction cannot move the candidate's identity —
that is why the file list states the domain per row rather than leaving a reviewer to infer it.

## 3 · Scope A–G — what was done, per clause

### A · Tracked lease home

`runtime/orchestrator_lease.md`, tracked, readable from every checkout via git. Writer is
`orchestrator` alone, from the orchestrator worktree; **`ONE_WRITER_PER_WORKING_DIRECTORY` holds
because no other actor's worktree writes that path**, and git history makes a violation visible
to every reader — which is the detector `I.3` asks for.

🔴 **The interim history is neither deleted nor silently rewritten.** Five lease records are
migrated with their provenance stated; `deployment/local_instance.md` is **retired as the lease
seat and retained on disk unmodified**, including its narrative sections, which are not
reproduced and not superseded.

**Only the lease moves.** Machine paths and session references stay untracked, for the two
reasons the profile already states — portability under `I.5`, and publication safety.

### B · `I.3` observability, made operative

The record is readable by a second actor, which restores I.3's specified `DETECTION`. And the
distinction is stated **as a rule with a consequence**, not as a slogan:

> **`VISIBILITY` ≠ `LIFECYCLE ENFORCEMENT`.** A record can be perfectly legible and wrong.
> **The stored `STATUS` is not authoritative and must never be consulted alone.**

Operative form: the derivation is a tracked command any actor can run, and the record instructs
that it be run at every consultation including every `GATE 0`.

### C · Lease lifecycle — the three layers, declared separately

| Layer | Content |
|---|---|
| `MECHANIZED` | derivation from `RELEASED_AT` · `EXPIRES_AT` · clock; stored-vs-derived disagreement; `EXPIRED_WITHOUT_RENEWAL`; **the `ACTIVE` singleton as an invariant, fatal in every mode** |
| `OBSERVABLE` | the tracked record, its git history, and the derivation's output — reproducible by an actor who was not present |
| `PROCEDURAL` | **writing a row at all.** Nothing compels an acquisition to be recorded, and nothing runs between turns |

**`lease_state.py` never reads the stored `STATUS` to decide.** It refuses to guess: a missing
record, an absent timestamp or a timezone-less timestamp exits `2` rather than defaulting.

#### `LEASE EXPIRED UNUSED BETWEEN TURNS` — treated, and not claimed as solved

```
DETECTABLE   yes — reported at the next consultation
PREVENTED    no  — nothing executes between turns; the window is unwatched
```

**Neither the tracked home nor the derivation closes this.** It moves from *invisible* to
*reported*, which is real and is not enforcement. Closing it needs something that runs when no
actor is running — the `P7` event ledger with `LEASE_ACQUIRED`/`LEASE_STALE`, which governance
already names and which is `OWED NOT BARRED`. **This candidate does not build it.**

### D · `Current instance — status` — rewritten whole

Not corrected line by line. It now separates **canonical state · runtime state · local
surfaces**, gives the check for each claim, and asserts no roster, no counts and no filesystem
facts.

**A finding the rewrite records rather than hides:** the Agent Card registry and runtime
inventory are on the `orchestrator` branch and **not in `main`**. A reader checking `main` alone
will not find them. That is runtime state, correctly, and the previous section had no vocabulary
to say so.

*The previous version's defect is described as a class — asserting facts whose staleness nothing
could detect — and not as a count of wrong sentences. Reproducing that count would repeat the
defect the rewrite exists to remove.*

### E · P1

```
P1   CRITERION_MET / NAME_NOT_DELIVERED
```

Not `VERIFIED`, not `FAILED`, not `SUBORDINATE`-for-missing-registry — **that precondition is
resolved**. Five validators returned `rc=0`; the registry instance exists and is readable. **The
capability's *name* promises a registry validation no instrument performs.**

### F · `REGISTRY VALIDATOR: MISSING INSTRUMENT` — recorded, **not implemented**

No tool validates the Agent Card registry, the runtime inventory, their schema, or the cross-file
invariants the contract declares. **This candidate does not implement it and adds no partial
version of it.** Separate authorization required.

**Scope-creep check, stated so a reviewer can falsify it:** the only executable added is
`lease_state.py`, which reads exactly one file and derives exactly one lifecycle. It does not
read the registry, the inventory, or any Agent Card. `grep -c 'agent_card\|registry' ` over it
returns `0`.

### G · Open debts carried forward

```
approval queue non-canonical · ACK criteria · Plan→Mirror routing
P7 event ledger — OWED NOT BARRED, and now load-bearing for the unwatched window
Mirror's methodology observation — UNRATIFIED under G.2
registry validator — MISSING INSTRUMENT
```

**Not carried:** `C.2` — **CLOSED** · P1's missing-registry precondition — **resolved**.

**New, and this candidate does not fix it:** stored `STATUS` values in the migrated history use
`EXPIRED`, which **is not in I.3's declared vocabulary** (`ACTIVE | STALE | RELEASED`). Left
exactly as written — see §4.

## 4 · Test and validator evidence

**The derivation, run against the migrated record:**

```
lease #1  derived=STALE     stored=STALE
lease #2  derived=RELEASED  stored=RELEASED
lease #3  derived=STALE     stored=EXPIRED     ← two findings
lease #4  derived=RELEASED  stored=RELEASED
lease #5  derived=RELEASED  stored=RELEASED
ACTIVE by derivation: 0

FINDING  #3 DISAGREEMENT:             stored 'EXPIRED', derived 'STALE'
FINDING  #3 EXPIRED_WITHOUT_RENEWAL:  LAST_RENEWED absent or equal to ACTIVATED_AT
```

**The singleton invariant, against Mirror's own fixture** — two simultaneous `ACTIVE` leases:

```
revision 1   default mode  exit 0   ← the blocking defect: "clean" by its own contract
revision 2   default mode  exit 3   INVARIANT VIOLATED, on stderr
revision 2   --check       exit 3   fatal before --check is consulted
real record  default       exit 0   singleton holds
real record  --check       exit 1   the two findings above
```

**Both findings are correct, and the row was left as written.** `EXPIRED` is a hand-written
terminal state in a value governance does not define. **Normalising it would have made the check
pass and destroyed the evidence** that hand-written states drift from their vocabulary — the
finding is the point of having a derivation.

**Exit-code behaviour, each measured on the derivation process itself:**

```
missing record        exit 2   refuses to guess
no timestamps         exit 2   refuses to guess
real record --check   exit 1   two findings
real record           exit 0   reports without judging
```

**Determinism:** identical output for the same `--now`, twice. **The clock drives it:** lease #3
derives `ACTIVE` at `13:00:00Z` and `STALE` at `13:10:00Z`, across its own `EXPIRES_AT`.

### 🔴 What Mirror's independent check does and does not establish — pinned deliberately

**Mirror *checked* leases #2, #4 and #5 against canonical commit timestamps**, converting them to
UTC and comparing them with the windows in this record: all three batches fall **inside** their
window and **before** release.

**That is co-occurrence between two records.** *"The leases were used"* is an **inference** from
it, and the inference holds only if the hand-written record is authentic — which the block below
says is **not** established. The route is stronger than the annotation in §*Lease records*,
because it does not require trusting the annotation; it is not a verification of use.

> *Revision note.* The first version of this paragraph opened *"Mirror verified that leases #2,
> #4 and #5 were used"* — **asserting in its headline exactly what the block below withholds**,
> in the section written to stop this compressing into *"Mirror verified the leases"*. It is the
> same defect Mirror filed against its own review table — the claim in the headline, the caveat
> underneath, **and a reader takes the headline.** Corrected on Mirror's finding, and the
> original wording is recorded here rather than replaced silently, because a guard that failed
> at its own opening line is worth seeing.

**State its limit, because the sentence this compresses into is *"Mirror verified the leases"*,
and that is not what happened.**

```
ESTABLISHED    a hand-written record is CONSISTENT with an independent trace
NOT ESTABLISHED  that the record is AUTHENTIC
```

The lease record is **hand-written**: its timestamps are asserted by the Orchestrator, the commit
times are not. **A record composed to match commit times would pass this check identically.** The
check is stronger than an annotation and weaker than verification of a lease, which nothing
currently available can supply and which this candidate does not claim to provide.

**§3B survives intact**: the demonstration is that `VISIBILITY` was worth having — Mirror could
not run this check at all while the record was git-ignored — **and nothing more.** It says
nothing about `LIFECYCLE ENFORCEMENT`, which is the distinction this candidate exists to keep
apart. *(Raised by Mirror, `REV-SUNSET-DEC3-MIRROR-002`; pinned at Mirror's request.)*

**Repository validators, at the content tip:** `legend_lint` PASS · `fulltext_receipts verify` OK
· `growth_anchors check` PASS · `public_release_gate` PASS / BLOCKS 0 ·
`governance_fingerprint compose --all` PASS. *(§7 records the run.)*

## 5 · What this candidate does NOT do

Execute itself · move `main` · take a lease · amend any governance text · implement the registry
validator · build the `P7` event ledger · touch the approval queue, the ACK criteria, the
Plan→Mirror routing, Mirror's observation, or any scientific content.

**No `HUMAN_APPROVAL` is pre-filled. None exists and none is implied.**

## 6 · What Mirror is asked to verify

Independent review of **both the binding and the content**. No prior attestation transfers;
Mirror's `ORCHWT` verification says nothing about this candidate.

```
VISIBILITY vs LIFECYCLE ENFORCEMENT — is the distinction operative, or only stated?
lease-state derivation             — does it ever decide from the stored field? does it guess?
the Current-instance rewrite       — is every claim checkable by the route it names?
P1's classification                — CRITERION_MET / NAME_NOT_DELIVERED, and not VERIFIED
the registry-validator debt        — recorded and unimplemented
scope creep                        — three files; is any of it outside A–G?
```

**One thing to attack first, because Plan is the wrong actor to judge it:** whether the unwatched
window is *treated* or merely *described*. The candidate claims detection and denies prevention.
If that reads as a fix, the wording has failed and Plan cannot see it from here. *(Reviewed at
revision 1: Mirror answered **no**, on four independent denials. Not re-asked; recorded.)*

---

## 8 · `AUTHOR_RESPONSE` — `REV-SUNSET-DEC3-MIRROR-001`, all three items **ACCEPTED**

**Nothing was contested.** Each finding was reproduced by Plan before being accepted; none was
taken on report.

### 🔴 BLOCKING — singleton fail-open · **ACCEPTED, classification not contested**

Reproduced exactly: two simultaneous `ACTIVE` leases returned `exit 0` in default mode, and the
docstring declares `0` to mean *clean*. `SINGLETON VIOLATED` sat **after** `if not args.check`.

**Mirror's classification is right and Plan does not contest it.** The singleton is an
**invariant**, not a finding: two `ACTIVE` leases is two writers over one shared resource, which
is the condition Annex I.3 exists to guarantee. **A fail-open that needs a flag to close is the
shape that outlives documentation edits** — the profile documenting `--check` protected the
documented path and left the default path unsound.

Remedy: the check runs **before** `--check` is consulted, in **every** mode, exits `3`, and
prints to stderr. Verified against Mirror's fixture in both modes.

### `LAST_USED` read and never written · **ACCEPTED — and it is worse than reported**

Confirmed: one occurrence in the entire candidate, in the reader. So the condition reduced to
*"is `LAST_RENEWED` absent or equal to `ACTIVATED_AT`?"* while being named for **use**.

**Plan's addition, which strengthens Mirror's finding:** the naming is not merely imprecise, it
is **falsified by the record the candidate ships with**. Leases **#2, #4 and #5** were never
renewed **and were demonstrably used** — each held a canonical batch (`HASHDET`, `P51C9` r3,
`ORCHWT`). An unrenewed lease that was used is indistinguishable here from one never used at all.

Remedy: the phantom read is removed and the condition is `EXPIRED_WITHOUT_RENEWAL`, **named for
the property it can test**, with the proxy limit stated in the tool, in the record, and beside
the affected row.

### The finding counts endings, not waste · **ACCEPTED**

Correct: `RELEASED_AT` returns `RELEASED` before the branch is reachable, so released-and-
unrenewed leases are never reported. **`1 finding` is not `1 wasted lease`**, and the manifest no
longer invites that reading — the counter-examples above are the same three leases, which makes
this item and the previous one one defect seen from two sides.

### On the two questions Plan asked, and Mirror's answers

Mirror answered **no** (the wording does not read as a fix) and **yes** (it should ship with its
own tool reporting findings). **Neither answer is treated as clearing anything**, and both are
recorded rather than relied on. The `rc=1` against the tool's own data stands unchanged in
revision 2.

### On routing

Mirror declined to treat Plan's account of an operator directive as the directive, reviewed
anyway because reviewing changes no state, and recorded that answering settles nothing. **Plan
agrees and will not cite this exchange as having settled the `Plan→Mirror routing` debt**, which
remains open in §3G.
