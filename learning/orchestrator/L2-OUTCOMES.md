---
artifact: L2 capability outcomes — durable interim seat
authority: operator decision 2026-08-18, "no outcome may live only in chat"
seat: the Orchestrator worktree, tracked, readable via git from every checkout
supersedes: nothing — this is the first durable seat these outcomes have had
created: 2026-08-18
---

# L2 outcomes — the durable seat

Until this file existed, the L2 outcomes lived in chat and in Plan's
`DEC-20260818-007-LAB-REACTIVATION.md`. The operator's rule — *no outcome may live only in
chat* — now has a home on the Orchestrator's own branch, which did not exist before
`CAND-20260817-ORCHWT` landed at `f5b32155`.

## Ratified round — operator decision of 2026-08-18 §1

3 VERIFIED of 12 attempted. The nine non-promotions were ratified each with its own cause,
**including three where the criterion was met and promotion was still refused**: attesting
ACK discipline on evidence that measured a ping would have promoted the wrong thing. The
collapse from 7 expected to 3 actual is registered as a finding **about the measuring
apparatus, not about the actors**.

| Row | Capability | Outcome | Evidence class |
|---|---|---|---|
| `O4` | lease acquire · renew · observe expiry | **VERIFIED** | PRIMARY (orchestrator) |
| `S2` | scientist worktree confinement | **VERIFIED** | PRIMARY (scientist-c) |
| `S4` | scientist capability per plan | **VERIFIED** | PRIMARY (scientist-c) |
| `O3` | runtime broadcast | BLOCKED — no broadcast primitive | — |
| `P1` | registry / structural validation | **CRITERION_MET / NAME_NOT_DELIVERED** | PRIMARY (plan) |
| `P2` | messaging with ACK discipline | NOT VERIFIED — self-reported against its own stricter criterion | — |
| `M1` | micro-review under Annex C.2 | CRITERION MET · FORMAT NOT UNIFORM | PRIMARY (mirror) |
| `M2` | messaging with ACK discipline | HALF MET · HALF UNEXERCISABLE | ping half BY-REPORT (orch) |
| `M3` | — | SUBORDINATE | — |
| `M4` | event-ledger write | BLOCKED — no event-ledger writer | — |

## `P1` — precondition re-verified 2026-08-18, after ORCHWT

`P1` was `SUBORDINATE — precondition unmet (no registry instance)`: the registry *instance*
had left with `EVAC-20260817-001` and only the `Annex I.4` schema remained. The instance
returned to this branch at `632ad22`.

```
[1] present + tracked   runtime/agent_card_registry.md   blob cd94b5725c   @ 632ad22
                        runtime/runtime_inventory.md     blob ccdbb1f9be   @ 632ad22
[2] cross-checkout      read from the root checkout on branch main via git:
                        17680 and 31005 bytes — which it could not do from the
                        evacuation directory, that being the whole of the previous failure
[3] not an EVAC copy    the object read is a git blob on a branch, not a filesystem copy.
                        Its content matches the evacuation digest: that is continuity of
                        content, not provenance-from-EVAC, and they are different claims
[4] coherent            orchestrator worktree HEAD 632ad22, 0 dirty entries
```

**PRECONDITION: PASS.**

### 🔴 Execution is not the Orchestrator's

`P1` is a **Plan** row — `roles/plan.md`, *"Registry / structural validation · run the
repository validators and report"*. An Orchestrator running the validators exercises the
Orchestrator's capability, and the resulting evidence about Plan would be `BY-REPORT (ORCH)`.

That is precisely why `M2`'s ping half stands at `CRITERION_MET` and unpromoted, and the
operator's own rule closes it: *a capability may pass to `VERIFIED` only with observed
evidence*, and *if the test does not really exercise the intended capability, do not
promote*.

So the precondition was discharged here and the execution was routed to Plan, in its own
worktree, as `PRIMARY`. Admissible outcomes were `VERIFIED` · `FAILED` · `BLOCKED` ·
`SUBORDINATE`, and **none was anticipated before the run**. The result Plan returned is
recorded below.

```
P1 PRECONDITION   PASS        verified by orchestrator, four clauses, 2026-08-18
P1 EXECUTION      EXECUTED    by plan, in plan's worktree — PRIMARY
P1 RESULT         CRITERION_MET / NAME_NOT_DELIVERED — not VERIFIED
```

### Outcome, and why the precondition passing did not discharge the row

Plan ran the five validators in its own worktree; all five returned `rc=0`:

```
legend_lint.py .                          PASS (1 INFO)
fulltext_receipts.py verify               OK: 128 chained, tail anchored
growth_anchors.py check                   VERDICT: PASS
public_release_gate.py                    PASS (1 REVIEW)
governance_fingerprint.py compose --all   PASS, four fingerprints
```

🔴 **The registry's presence was not what this row was blocked on.** Verified independently
by the Orchestrator, with a positive control on the search machinery first:

```
registry references inside the five validators      0, 0, 0, 0, 0
*.py files anywhere referencing agent_card /
  AGENT_CARD / "Agent Card" / runtime_inventory      0
positive control on the same machinery              "CURRENTS" 5 files · "def " 119 files
```

The validators run to `PASS` without the registry and always did — **none of them reads it.**
What the absence blocked was the *registry* half of *"Registry / structural validation"*, and
**there is no registry validator.** The object is back and still nothing validates it;
reading 314 lines and counting 30 rows is measurement, not validation.

**The block was correctly identified; the remedy does not discharge it.** Criterion met, name
not delivered — the same shape as `M2`, from the opposite direction: there the criterion was
too weak for the name, here the criterion is met and the name covers an object no criterion
reaches.

### And the first run of the smoke test was a harness artifact

Plan's **first** run reported three validators failing with `can't open`. False. The harness
passed `python3 $v` with an unquoted variable and **zsh does not word-split**, so
`"legend_lint.py ."` went through as a single filename. The validators were never at fault.

**Third occurrence of that exact defect in this session**, and the only one caught before it
produced a claim rather than after. Had that run been reported, three false `FAILED`s would
have been filed against tools that were fine — a worse outcome than the row actually
recorded. It is visible only because the failure was investigated instead of retried.

### Consequent debt, registered and not resolved here

```
REGISTRY VALIDATOR:  MISSING INSTRUMENT        ← named by operator decision, 2026-08-18
```

**`P1` cannot reach `VERIFIED` until a registry validator exists.** The debt is the absence
of a tool that actually validates the Agent Card registry, the runtime inventory, the
relevant structure and schema, and any cross-file invariants the contract declares.

**A missing instrument, not a missing object** — and the distinction is the whole reason this
row did not resolve when the object came back. Building it is **not authorized to anyone**
under the current decision and must not be smuggled into the sunset candidate; it needs a
separate authorization.

### How the operator classified the row, verbatim in substance

`P1` is **not** `VERIFIED`, **not** `FAILED`, and **not** `SUBORDINATE` for a missing
registry — that precondition is resolved. The registry instance exists, the existing
criterion is met, and **the capability's name promises a registry validation that no
instrument performs.**

That is the durable form of the finding: the row is blocked by what it is *called*, not by
what it *lacks*.

## What this seat does not fix

It makes the outcomes **readable**. It does not make them **produced** — the same distinction
the sunset candidate is required to keep between *visibility* and *lifecycle enforcement*. A
row's evidence class still depends on which actor exercised it, and no file can supply that.
