---
artifact: INTEGRATION_CANDIDATE manifest (Annex D.2)
candidate_id: CAND-20260818-SUNSET-DEC3
revision: 1
governance_version: 3.1.1
change_class: MAJOR
prepared_by: plan
prepared_on: 2026-08-18
state: READY FOR MIRROR INDEPENDENT REVIEW
scope: sunset of DECISION 3 — the interim git-ignored lease seat. Scope A–G of
  HANDOFF-SUNSET-DECISION3.md, not reduced and not widened.
---

# INTEGRATION_CANDIDATE — sunset of `DECISION 3`

## 1 · Manifest (Annex D.2)

```yaml
CANDIDATE_ID:               CAND-20260818-SUNSET-DEC3
REVISION:                   1
BASE_HEAD:                  f5b321556e5f1f081482f13fbbabb4f90f3d6295
BRANCH:                     sunset-decision3
BRANCH_TIP:                 325da043e22e1bb5ffc88b5e36b3a8025e2988be
CANDIDATE_CONTENT_HASH:     48d4f3a7d96f5bda4c4c219486d83861e51d4666665b53bd255002b045bcd9a0
CANDIDATE_HASH_VERSION:     legend-candidate-v4
CHANGE_CLASS:               MAJOR
LINT_RESULT:                PASS
PUBLICATION_GATE:           PASS / BLOCKS: 0
MIRROR_REVIEW:              NOT YET REQUESTED
HUMAN_APPROVAL:             NONE — not requested, not granted, not implied
SNAPSHOT_ID:                n/a until canonical execution — GATE 4 belongs to Orchestrator
```

**`CHANGE_CLASS: MAJOR`**: it changes where a `GATE 0` input lives and how its state is
determined.

### Reproduction

```bash
python3 governance/scripts/candidate_content_hash.py \
  --base f5b321556e5f1f081482f13fbbabb4f90f3d6295 \
  --tip  325da043e22e1bb5ffc88b5e36b3a8025e2988be --show-domain
```

```
EXPECTED          48d4f3a7d96f5bda4c4c219486d83861e51d4666665b53bd255002b045bcd9a0
OBTAINED (run 1)  48d4f3a7d96f5bda4c4c219486d83861e51d4666665b53bd255002b045bcd9a0
OBTAINED (run 2)  48d4f3a7d96f5bda4c4c219486d83861e51d4666665b53bd255002b045bcd9a0
DOMAIN            509 included · 22 excluded, as produced by the command at this tip
```

Counts are stated as **outputs of that command at that tip**, never as maintained constants.

**Manifest tip vs content tip.** This manifest is added at a later commit than
`325da043`. `governance/candidates/` is a declared `CONTROL_PLANE_ROOT`, so the hash is
identical at both — §7 records the measurement rather than asserting the property.

## 2 · File list and classification

| File | Status | Classification |
|---|---|---|
| `runtime/orchestrator_lease.md` | **added** | **RUNTIME** — the lease record itself |
| `framework/scripts/lease_state.py` | **added** | **NORMATIVE (tooling)** — it decides a `GATE 0` input; it is not documentation |
| `deployment/deployment_profile.md` | modified | **NORMATIVE** (§ lease seat retirement) + **DOCUMENTATION** (§ *Current instance — status*) |

```
3 files · +394 / −5 · no file deleted · no history rewritten
```

**Nothing under `governance/`, `ledger/` or `reviews/` is touched by the content commit.** The
candidate proposes no governance-text amendment: `I.3` is *satisfied* here, not edited.

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
| `MECHANIZED` | derivation from `RELEASED_AT` · `EXPIRES_AT` · clock; stored-vs-derived disagreement; `EXPIRED_UNUSED`; `ACTIVE` singleton count |
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

FINDING  #3 DISAGREEMENT:   stored 'EXPIRED', derived 'STALE'
FINDING  #3 EXPIRED_UNUSED: reached EXPIRES_AT with no use recorded after ACTIVATED_AT
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

**One thing to attack first, because Plan is the wrong actor to judge it:** whether
`EXPIRED_UNUSED` is *treated* or merely *described*. The candidate claims detection and denies
prevention. If that reads as a fix, the wording has failed and Plan cannot see it from here.
