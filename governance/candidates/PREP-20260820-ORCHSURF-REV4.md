---
artifact: REV4 PREPARATION — adjudication of CAND-20260819-ORCHSURF under DEC-20260820-ORCH-SESSION-HOME
prep_id: PREP-20260820-ORCHSURF-REV4
task_id: ORCHSURF-001
author: plan
authored_on: 2026-08-20
governance_version: 3.1.1
domain: CONTROL PLANE — governance/candidates/ is a declared CONTROL_PLANE_ROOT (P5.1)
status: PREPARATION — this is NOT revision 4. No manifest, no binding, no CANDIDATE_CONTENT_HASH,
  no content file edited under this document's direction
gate: BLOCKED ON RATIFICATION. `DEC-20260820-ORCH-SESSION-HOME` carries
  `status: BINDING_UPON_OPERATOR_RATIFICATION` and `ratified_by: ""`, and its own §6 states it
  has no effect until ratified. Plan will not build a bound candidate on an unratified premise —
  that is the exact class of error revision 1 made, pointed the other way
scope_negative: Routing NOT implemented. Annex D.1 NOT modified. Annex I.2 NOT modified. The
  governance BODY NOT modified. P5 NOT reopened. ROOTGUARD NOT designed and NOT in scope
  (the decision's §1.5 excludes it). Scientist A/B NOT activated. No FROZEN document is edited,
  proposed for edit, or claimed superseded by anything below
supersedes: nothing. Revision 3 stands as the current delivered package until a revision 4 is
  bound. Nothing here withdraws revision 3's binding
---

# `PREP-20260820-ORCHSURF-REV4` — the finding was real, the remediation direction was not, and the document that outranks both was quoted against itself

## 0 · What this document is, and the one thing it is waiting for

The operator transmitted an architectural intent that inverts the remediation direction of
`CAND-20260819-ORCHSURF` without touching a single one of its measurements. This document does
the whole of the work that inversion makes available, and stops at the one input Plan cannot
supply.

```
RATIFICATION STATUS      UNRATIFIED — `ratified_by: ""` in DEC-20260820-ORCH-SESSION-HOME
EFFECT OF THE RECORD     NONE TODAY, by its own §6
WHAT IS DELIVERED HERE   the verification the record's §2 demands; four findings that the
                         verification produced; the disposition of every revision-3 finding
                         under the new direction; and the exact revision-4 change set
WHAT IS NOT DELIVERED    revision 4 itself — no manifest, no hash, no content edit
WHY NOT                  the record distinguishes transmission from ratification. Plan does not
                         collapse that distinction on the operator's behalf
```

**Rehydration, fail-closed.** `pwd` equals git top-level, `evidence-index`, branch
`orchestrator-surface`, clean at open. `roles/plan.md` read in full. Canonical `main` verified
from git as `04693e683a254ff0a6d0619fba47103a0fb7d122` — not from the prompt, not from a
manifest. Nothing below is inherited from a prior conversation; every section reference was read
at its source in this session, which is what the record's §2 requires and what §3 item 4 of the
prompt directive requires.

---

## 1 · The decision, restated as the two propositions it actually asserts

Stripped of framing, the record makes one architectural claim and one methodological one.

```
ARCHITECTURAL   the Orchestrator's SESSION is opened at the repository root, and the
                `orchestrator` worktree is that actor's WORK_COMMIT surface. Both are true at
                once, because they are answers to different questions
METHODOLOGICAL  SESSION_LOCATION and PERSISTENCE_SURFACE are independent dimensions. A true
                statement about one was transformed into a false statement about the other,
                and that transformation is the whole of the Rev1→Rev3 drift
```

The record classifies itself as a **CONFIRMATION of existing FROZEN governance**, not a change.
**That classification is correct, and it is more strongly supported than the record itself
claims** — §2 below.

---

## 2 · Every section reference re-verified at source, as §2 of the record requires

Read in the source documents this session. No reference was inherited from the manifest, the
review, the handoff or any prior revision.

| Reference | Verified? | Text as it actually reads |
|---|---|---|
| body §0.2 | **CORRECT** | heading *"Root ≠ authority vale anche al giorno zero"*; *"La prima chat aperta in `<REPO_ROOT>` NON è Orchestrator per il fatto di trovarsi lì"*; *"La stessa chat viene promossa; non servono due chat root. La promozione è un record durevole (Annex I), mai un'autoassunzione."* |
| body §0.4 | **CORRECT** | the Controller *"presenta all'operatore la lista esatta delle chat da aprire … e SOLO a condizioni superate acquisisce il lease e diventa ACTIVE_ORCHESTRATOR"*; and *"Perimetro di scrittura pre-promozione: SOLO artefatti di bootstrap"* |
| body §47 step 10 | **CORRECT** | *"operatore apre le cinque chat restanti"* |
| body §47 step 14 | **CORRECT** | *"promozione: BOOTSTRAP_CONTROLLER → ACTIVE_ORCHESTRATOR (lease ACTIVE)"* |
| Annex I.2 steps 1, 4, 6, 9–10 | **CORRECT** | reproduced verbatim; plus *"Perimetro pre-promozione: SOLO artefatti di bootstrap. Lease ACTIVE già esistente → la chat è OBSERVER."* |
| Annex H.1 | **CORRECT** | *"Spese / MAJOR approval / governance → Operatore"*; and — not previously used — *"WORK_COMMIT · ogni attore, **solo proprio branch**, granularità milestone"* |
| body §5 precedence | **CORRECT** | rank 1 NON-NEGOTIABLE GOVERNANCE, rank 2 OPERATOR STRATEGIC DIRECTIVE |
| body §48 | **CORRECT AS TEXT, MISAPPLIED IN THE PACKAGE** | see F-3 |
| body §14 | **CORRECT AS TEXT, MISAPPLIED IN THE PACKAGE** | *"mai **due attori** abilitati alla scrittura sulla stessa directory. Critico nella root."* — see F-3 |
| **body §8** | **CORRECT — AND NAMED IN NEITHER THE RECORD NOR ANY REVISION OF ORCHSURF** | see F-1. This is the finding |

```
SECTION REFERENCES IN THE RECORD   ALL CORRECT AS CITED
ENUMERATION IN THE RECORD          INCOMPLETE — body §8 and §14 bear on this decision and the
                                   record names neither. The omission does not weaken the
                                   record; §8 is the strongest support it has
```

---

## 3 · Four findings the verification produced

### F-1 · 🔴 Body §8 states the operator's architecture at rank 1, and the package quoted one clause of §8 against the rest of it

`governance/GOVERNANCE_v3.1.1.md` §8 is titled **"ORCHESTRATOR — ROOT, AUTORITÀ, IDENTITÀ"** and
reads, verbatim:

```
Orchestrator vive nella chat grafica associata a <REPO_ROOT> (valore concreto nel
DEPLOYMENT_PROFILE, Annex I) — l'unico ruolo che esegue CANONICAL_BATCH_COMMIT.

> La posizione nella root NON conferisce autorità (§0.2). L'autorità deriva dal ruolo
  esplicitamente assegnato e, per Orchestrator, dal LEASE ACTIVE.
```

Those two sentences are decision items **1** and **3**, in `FROZEN`, `normative: yes` body text,
at the top of the precedence order. The first says where the Orchestrator lives — *the graphical
chat associated with the repository root*. The second says that living there confers nothing.
**The decision does not need to be granted; it needs to be recognized.**

**How the package treated §8.** Every `§8` occurrence across the manifest, the handoff, the
author response, the three SLRs and `REV-ORCHSURF-MIRROR-001` was enumerated and read
individually. They fall into three classes and only one is body §8:

```
P5DOMAIN §8.3                       a different document's section — most of the hits
internal section numbers            the review's own §8, the response's own §1–§8
body §8, cited for content          EXACTLY TWO occurrences, both for the same clause:
                                    "body §8 obliges it to produce durable output"
                                    — manifest line 209, author response line 102
```

Both load-bearing citations of body §8 use it to argue that an Orchestrator **cannot** live in
the root. **They cite the section whose opening sentence says it does.** The clause quoted is
real; the sentence above it was never read into the package by either actor, across three
revisions and one hostile review.

```
BODY §8 ROOT-RESIDENCE STATEMENT     CONFIRMED — FROZEN, normative, rank 1
NAMED IN ORCHSURF rev 1 / 2 / 3      NO / NO / NO  (for this content)
NAMED IN REV-ORCHSURF-MIRROR-001     NO  (for this content)
NAMED IN DEC-20260820                NO
CONSEQUENCE                          the decision is a CONFIRMATION, and §8 — not §0.2 — is the
                                     cleanest evidence that it is
```

### F-2 · 🔴 The WORK_COMMIT impossibility premise is false, and it is the load-bearing premise of the canonical argument

`deployment/deployment_profile.md`, canonical at `main`, asserts:

> *"an Orchestrator living in the root had **no branch on which a `WORK_COMMIT` was possible**"*

This sentence is the engine of the whole Rev1→Rev3 construction. `BOOTSTRAP.md` repeats it in the
blocked-promotion section; the author response restates it as the *sound* form that survives
Mirror's N-3; Mirror accepted it as *"the stronger route"*.

**It is false, and it was falsified mechanically rather than argued.** In a throwaway repository —
so that no actor's surface was touched — a process whose working directory was the root checkout
wrote to and committed on a **different branch in a different worktree**:

```
cwd                     <root checkout>              root branch: main
act                     git -C ../side add/commit    on branch `sidebranch`
RESULT
  side branch HEAD      e36b8b3  "WORK_COMMIT authored by a process whose cwd is the root"
  root porcelain        []                            <- root stayed CLEAN
  root HEAD             unchanged from init           <- main did not move
```

A git worktree carries its own `HEAD` and index. **The set of branches on which a session may
commit is a function of the worktree paths it operates on, not of the directory it was opened
in.** The premise silently supplies a missing conjunct — *and the Orchestrator writes only inside
its own cwd* — which is a **discipline**, not a constraint. It is precisely the discipline the
decision's table prescribes, and it is satisfiable from the root.

**Textual corroboration, independent of the test.** Annex H.1 defines the rule as
*"WORK_COMMIT · ogni attore, **solo proprio branch**"* — a constraint on the **branch**, not on
the location. Annex D.1 is identical: *"ogni attore, proprio branch"*. No governed rule anywhere
binds `WORK_COMMIT` to a working directory.

```
"NO BRANCH ON WHICH A WORK_COMMIT IS POSSIBLE"   FALSE — mechanically falsified
STATUS OF THE SENTENCE                            CANONICAL at main, in deployment_profile.md
OWNER OF THE CORRECTION                           plan — deployment_profile is Plan's to maintain
IS ANNEX D.1 AFFECTED                             NO. D.1 is correct and is not touched
IS THE ORCHWT WORKTREE DECISION AFFECTED          NO. The worktree is still the right WORK_COMMIT
                                                  surface; only the argument for it was wrong
```

**This finding does not undo `CAND-20260817-ORCHWT`.** The Orchestrator should have a worktree;
the reason published for giving it one does not hold. A conclusion can be right while its
published reason is false — which is `SLR-plan-0010` L-3, applied this time to a canonical
sentence rather than to `P5DOMAIN §8.3`.

### F-3 · 🔴 The fail-closed stop's §48 grounding is not supported by §14's text

`BOOTSTRAP.md`'s blocked-promotion section grounds itself:

> *"Body §48 forbids proceeding past a point that could 'violare one-writer', and a standing
> Orchestrator in the root is exactly that"*

Body §14, read at source, defines the rule:

> **"ONE_WRITER_PER_WORKING_DIRECTORY — mai *due attori* abilitati alla scrittura sulla stessa
> directory. Critico nella root."**

The rule prohibits **two actors** enabled to write on one directory. A single root-seated
Orchestrator is **one**. The §48 condition is not hit by residence; it would be hit by a *second*
writer in the root — which the deployment profile already prevents by reserving the root to
`CANONICAL_BATCH_COMMIT`.

**Plan's own handoff nominated this as attack vector 4** — *"attack whether §48's one-writer
clause is really triggered by a promoted root chat, or whether that is my inference dressed as a
citation."* Run against the source: **it is the inference.** The stop's stated grounding does not
survive, independently of the operator decision.

### F-4 · 🔴 T10's stopping rule is vacuous over the governance corpus; the discriminating field is `body:`, not `authority:`

Revision 3 §5.5 states the rule that terminates its search, and `SLR-plan-0012` adopts it as a
proposed `PROVISIONAL_OPERATIONAL_PRACTICE`:

> *"the body has **no `authority:` field**; every annex names it as theirs. It is where a mandate
> can originate — that is the stopping rule, and it is why the search terminates there."*

Measured across all eleven `FROZEN` `normative: yes` governance documents:

```
DOCUMENTS WITH AN `authority:` FIELD    0 of 11   — the body AND all ten annexes have none
DISCRIMINATING POWER OF THE RULE        ZERO. It terminates at every governance document equally
WHAT ACTUALLY DISCRIMINATES             `body: GOVERNANCE_v3.1.1.md` — carried by 10 of 10
                                        annexes, absent from the body. Clean 1-vs-10 split
```

The annexes do name the body as their source — but through the `body:` field, not through
`authority:`. **The conclusion was right and the stated mechanism does not exist.** Applied to
`BOOTSTRAP.md` (which *does* carry `authority:`), the rule as written would have terminated at
Annex I.1 — the first governance document reached, with no `authority:` field — which is exactly
where revision 2 stopped and thought it was finished. What actually rescued revision 3 was
reading `BOOTSTRAP.md` line 5 **whole**, past the semicolon; the terminus rule added nothing.

```
SLR-plan-0012 MICRO-UPGRADE     SALVAGEABLE, not sound as written. Substituting `body:` for
                                `authority:` makes it discriminate and makes it checkable
SLR-plan-0012 L-4               the general form survives — "the search must terminate at the
                                document a mandate can originate in" — the field named to
                                detect that document does not
TRANSCRIPTION RULE (L-2)        UNAFFECTED and CONFIRMED — it is the half that actually worked
```

### F-5 · T10 is CONFIRMED and PRESERVED, and its term set cannot see body §8

Reproduced this session, independently, from the frontmatter of the eleven documents:

```
GOVERNANCE_v3.1.1.md              5 hits
annex_i_bootstrap_deployment.md   3 hits
the other nine annexes            0 hits each     <- the sweep's own negative control
TOTAL CARRYING THE VOCABULARY     2 of 11         <- revision 3's finding, reproduced exactly
```

**T10's enumeration method is sound and is preserved**, per the directive's item 6. Its
**vocabulary** is not exhaustive: body §8 contains **zero** of the five search terms
(`stessa chat`, `ACTIVE_ORCHESTRATOR`, `acquisizione ORCHESTRATOR_LEASE`, `cinque chat`,
`LISTA ESATTA`). The five terms hit body lines 67, 70, 86, 440 and 444 — all bootstrap-promotion
passages. §8, at lines 180–182, is the **steady-state residence** statement, and it is the single
most decision-relevant passage in the body.

```
T10 DOCUMENT UNIVERSE     enumerated from the tree — SOUND, and the reason T10 escaped T7/T8's trap
T10 TERM UNIVERSE         inherited from the candidate's own vocabulary — the SAME trap, one axis over
THE GENERALISATION        T7/T8 inherited the candidate's list of documents. T10 fixed that and
                          inherited the candidate's list of words. A sweep is only as exhaustive
                          as its narrowest inherited dimension, and enumerating one of them from
                          the tree does not make the others exhaustive
```

### F-6 · No decision-record convention exists in this repository

The record's §6 instructs Plan to *"register it according to decision-record conventions"*.
Enumerated: there is no `DEC-*` artifact anywhere in the tree and no `governance/decisions/`
directory. The precedent the repository calls `DECISION 3` exists only as prose inside other
documents. `governance/decisions/DEC-20260820-ORCH-SESSION-HOME.md` therefore **proposes** a
convention rather than applying one, and says so in its own frontmatter.

---

## 4 · Disposition of every revision-3 finding under the decision

The directive's item 6 requires the valid findings to be conserved. They are — and the test
applied to each is **whether it depends on the remediation direction**.

### 4.1 · PRESERVED — direction-independent, carried into revision 4 unchanged

| Finding | Why it survives |
|---|---|
| **T10 enumeration method** | a method for enumerating a document universe from the tree rather than from a manifest. Independent of which document turns out to be wrong. **Reproduced this session** |
| **The truncated authority-line finding** | `BOOTSTRAP.md` line 5 reads `authority: Annex I.1, I.2, I.6; body §0.1–0.4, §38, §47` and `SLR-plan-0011` quoted it to the semicolon. Verified at source. A transcription defect, true in every direction |
| **T7/T8 inherited-universe correction** | a test that inherits the candidate's own list of sources cannot falsify that list. **Extended by F-5**, not weakened |
| **Mirror's B-1, as a finding of contradiction** | governed documents did describe two mutually exclusive topologies. **That was true and remains true.** What changes is which document is the defective one |
| **N-1 — agent-card owner is `plan`** | from `maintained_by`, body §43 and finding C-5. Independent |
| **N-2 — E.2 vocabulary and E.6 elements** | form defects in a learning record. Independent |
| **N-3 — the GATE 0 compression is lossy** | Mirror was right that the compressed form was lossy. **F-2 goes further**: the uncompressed form is false too |
| **N-4 — the suite is red at main** | a disclosure defect. Independent. Cause re-confirmed: four shebang entrypoints at mode `100644` |
| **`SLR-plan-0012` L-1, L-2, L-3, L-5** | L-1 (a claim removed from a derived document is not removed), L-2 (transcription), L-3 (a fail-closed stop owes an account of its authority — **and F-3 shows this one was owed and unpaid**), L-5 (author's adversarial pass fails differently from a reviewer's). All independent |
| **`P5DOMAIN §8.3` carried debt** | untouched, still owed, still not ORCHSURF's to fix |
| **The cwd-is-not-identity rule, in all three content files** | this is decision item 3. It is the part of revision 3 the decision **endorses** |

### 4.2 · INVERTED — direction-dependent, and the direction changed

| Revision 3 held | Under the decision |
|---|---|
| body §0.2/§0.4/§47 and Annex I.2 mandate a **superseded** topology | they state the **intended** topology. **Nothing is superseded.** Body §8 says so most directly (F-1) |
| the residual is `HUMAN_REQUIRED`, owned by the operator, discharged by amending body + annex | **the residual dissolves.** No FROZEN amendment is required, requested or proposed |
| the convergence route rotates **all four** fingerprints and invalidates every checkpoint (A.6) | **that cost disappears entirely.** No document in any fingerprint set is amended for this purpose |
| `BOOTSTRAP.md` must fail closed at step 9 | **the stop is removed** — the conflict is resolved by reading, not by amending. Independently, its §48 grounding did not hold (F-3) |
| the `orchestrator` row of the chat table is BLOCKED, do not open | **there is no sixth chat to open, and there never was.** The Orchestrator chat is the root chat. I.2 step 6's *lista esatta* of five is correct as written |
| `STEP5-session-open-plan.md` line 32 is a stale declaration | **CORRECT, re-adjudicated** — *"The Orchestrator chat is already open in the root checkout and is not reopened"* is a true statement of the intended architecture. Directive item 5, discharged |
| `runtime_inventory` *"Working dir: the root checkout"* is stale | **CORRECT.** The residual splits: session-location rows are right, WORK-surface rows (`Worktree: root`, `Branch: main`, `agent_card_registry` line 118) remain stale. Disposition `SAFE_CARRIED`, owner `plan`, unchanged |
| the deployment profile's WORK_COMMIT argument is the sound version that survives N-3 | **FALSE (F-2).** It is the sentence that most needs correcting, and it is canonical at `main` |

### 4.3 · The one thing that does not change

```
ORCHESTRATOR SURFACE SEMANTICS   still needed, still MAJOR, still governance
THE ORIGINAL DEFECT              roles/orchestrator.md carried an untyped `worktree:` field
                                 naming two surfaces for one actor. Real at revision 1, real now
THE FIX                          type the surfaces. The decision adds a THIRD type the candidate
                                 never named: SESSION HOME
```

---

## 5 · The revision-4 change set — exact, per file, available on ratification

### `BOOTSTRAP.md` — status `PROPOSED`, Plan's to edit, **not** a fingerprint input

```
REMOVE    the entire "🔴 Before you promote anyone — BLOCKED_BY_GOVERNANCE" section
REMOVE    the STOP at step 9; restore lease acquisition as the ordinary step it is
REMOVE    the "🔴 BLOCKED, do not open" marking on the `orchestrator` table row
REMOVE    the "Do not issue a sixth line for `orchestrator`" instruction at step 5 — replaced
          by the REASON there is no sixth line: that chat is already open, in the root
REMOVE    "which chat is promoted … is an open governance question, and this file does not
          answer it" — it is not open, and the file may now answer it by quoting §8 and §0.2
RESTORE   the affirmative statement of the architecture, in the governance's own terms: the root
          chat becomes BOOTSTRAP_CONTROLLER, is promoted in place by lease, and being in the
          root confers nothing. Body §0.2 and §8 are the citations
KEEP      step 3 creating the `orchestrator` worktree — with the reason corrected: it is the
          Orchestrator's WORK_COMMIT surface, not a chat to open. I.2 step 4 enumerates
          worktrees to create and does not prohibit others (revision 3's own reading, retained)
KEEP      "Being in the root does not make you the Orchestrator" — decision item 3, verbatim
REWRITE   the chats table: the `orchestrator` row gains a session-home value (repository root)
          and a work-surface value (worktree `orchestrator`). Two facts, two columns, no block
```

### `deployment/deployment_profile.md` — status `PROPOSED`, Plan's to maintain, **not** a fingerprint input

```
WITHDRAW  "an Orchestrator living in the root had no branch on which a WORK_COMMIT was
          possible" — FALSE (F-2), and it is the premise the section is built on
REPLACE   with the true statement: WORK_COMMIT is bound to a BRANCH (Annex D.1, Annex H.1
          "solo proprio branch"), never to a working directory. The Orchestrator commits its own
          work on branch `orchestrator`, from wherever its session is open, and the root stays
          clean because nothing is written there outside a batch window
RETITLE   "The Orchestrator's worktree, and why the root is not it" → the worktree and the root
          are BOTH its surfaces, for different purposes. The current title asserts the error
DELETE    the "🔴 The correction never reached the governance body or Annex I.2" residual block
          in full — there is no residual. Replaced by a short section recording that body §8 and
          §0.2 already state this architecture, and that CAND-20260817-ORCHWT's conclusion was
          right while its published reason was not
KEEP      the actor table, the three-concepts block, the five resolver requirements, the cwd
          measurements and the "working directory is NOT an actor identity attribute" section —
          all endorsed by decision item 3, none direction-dependent
ADD       SESSION HOME as a fourth named concept alongside the existing three
```

### `roles/orchestrator.md` — status `PROPOSED`, **the one fingerprint input this candidate moves**

```
KEEP      `worktree: orchestrator` — correct, and the decision confirms it
FIX       `canonical_batch_surface:` — it currently reads "never this actor's home". Under the
          decision the root IS this actor's session home. The precise statement is: never this
          actor's WORK surface, and never evidence of its identity
ADD       `session_home: the repository root checkout` — a third typed field, because the
          decision names a third concept and an untyped concept is what caused this candidate
EXTEND    "Three surfaces, and why the word `worktree` names only the first" → four concepts:
          SESSION HOME · ACTOR WORK SURFACE · CANONICAL BATCH SURFACE · ROUTING (still no
          filesystem attribute, still deliberately uncreated)
DELETE    the "🔴 Two more documents were not updated on 2026-08-17, both are FROZEN, and one of
          them is the body" paragraph — both were correct all along
KEEP      "Position in the root confers nothing", the cwd-is-not-identity block, and the
          must-not list. "Treat the root as free working space" remains prohibited, and that
          prohibition is exactly decision item 4
```

### `runtime/` on branch `orchestrator` — **routed through Orchestrator, never reached across by Plan**

```
STEP5-session-open-plan.md L32, L38   RE-ADJUDICATED CORRECT. Removed from the residual list
runtime_inventory.md "Working dir"    CORRECT
runtime_inventory.md "Worktree: root" STALE as a WORK surface — remains SAFE_CARRIED, owner plan
agent_card_registry.md L118           STALE as a WORK surface — remains SAFE_CARRIED, owner plan
runtime_inventory.md L79              CORRECT — body §0.4 and I.2 both fix the pre-promotion
                                      perimeter at "SOLO artefatti di bootstrap"
```

### Gate and blast-radius projection

```
CHANGE_CLASS            MAJOR — unchanged. It edits a role contract, the deployment profile and
                        the bootstrap procedure. H.1 gives a doubtful MAJOR to Mirror
FINGERPRINT IMPACT      orchestrator only — `roles/orchestrator.md` is the single input that
                        moves. plan · mirror · scientist UNCHANGED. To be recomputed at the
                        revision-4 tip, never carried forward
FROZEN DOCUMENTS        none modified, none proposed for modification, none claimed superseded
HUMAN_REQUIRED RESIDUAL DISSOLVED — and this is the largest single consequence of the decision
A.6 CONSEQUENCE         orchestrator checkpoints only, as at revision 3. NOT four roles
REGRESSION              expected DELTA 0; the suite is red at main for a pre-existing reason and
                        must be re-measured in matched fresh checkouts, not asserted
```

---

## 6 · Where a reviewer should attack this, ranked

**1 · Does body §8 mean session home, or association?** This is the attack that would cost the
most. *"Orchestrator vive nella chat grafica associata a `<REPO_ROOT>`"* — a reader could hold
that *associata* denotes the actor's association with the root as its canonical batch surface,
not the chat's filesystem location. My answer: the subject of *vive* is *la chat grafica*, and a
chat's location is where it is opened; §8's own title is **"ORCHESTRATOR — ROOT, AUTORITÀ,
IDENTITÀ"**, and the sentence immediately following denies that this location confers authority —
a denial that is only necessary if the location is real. **But it is a reading, and F-1's strength
depends on it.**

**2 · Does decision item 4 conflict with the FROZEN pre-promotion write perimeter?** The
decision's table says root writes: **no**. Body §0.4 and Annex I.2 both say the Controller's
pre-promotion perimeter is *"SOLO artefatti di bootstrap"* — an explicit FROZEN **permission** to
write bootstrap artifacts in the root. **Reconciliation, offered rather than assumed:** the
decision describes the promoted steady state; the pre-promotion perimeter is a narrower, earlier,
FROZEN allowance the decision does not touch and could not — body §5 puts NON-NEGOTIABLE
GOVERNANCE at rank 1 and an OPERATOR STRATEGIC DIRECTIVE at rank 2. Revision 4 must state both
and must not let the decision's table read as a repeal. **If a reviewer holds these do conflict,
that is a governance question and not Plan's to settle.**

**3 · Is F-2's test representative of this repository?** It ran in a throwaway git repository, so
that no actor's surface was touched. It demonstrates a property of **git worktrees**, which is
where the claim lives. It does **not** test this repository's harness guards, which are a
different layer and are the subject of the deferred `ROOTGUARD` candidate. Attack whether the
canonical sentence was ever a claim about git at all — I read it as one, because it argues from
*"the root's branch is `main`, and a commit to `main` is canonical by definition"*.

**4 · Does F-3 dissolve the stop, or merely its stated grounding?** I claim §14's *"due attori"*
is not satisfied by one resident Orchestrator. A reviewer could hold that ONE_WRITER is violated
prospectively — the Orchestrator plus any batch executor. My answer is that they are the same
actor. **Attack that identity.**

**5 · Is F-4 fatal to `SLR-plan-0012`'s micro-upgrade, or repairable?** I say repairable by
substituting `body:` for `authority:`. Attack whether a frontmatter field is the right detector
at all, rather than a second convention that will drift like the first.

**6 · Is the decision's own enumeration authoritative?** It names §0.2, §0.4, §47 and Annex I.2
and misses §8 and §14. I treat the omission as harmless because §8 **supports** it. Attack
whether an operator record that does not name its own strongest evidence should be ratified as
written, or amended to name it first.

**7 · Am I conserving revision 3's findings, or re-labelling them?** §4 claims a clean split into
direction-independent and direction-dependent. Attack any row of §4.1 by showing it secretly
depends on the direction, and any row of §4.2 by showing it does not.

---

## 7 · What this document does NOT do

- **It does not claim `DEC-20260820-ORCH-SESSION-HOME` is in force.** It is unratified, and its
  own §6 governs. Everything in §5 is conditional on ratification.
- **It is not revision 4.** No manifest, no `CANDIDATE_CONTENT_HASH`, no `BASE_HEAD` binding, no
  content file edited. Revision 3 remains the delivered package and its binding is untouched.
- **It does not modify, propose modifying, or claim to supersede any FROZEN document.** Body and
  Annex I.2 are correct under this direction, which is the point.
- **It does not withdraw Mirror's B-1.** B-1 found a real contradiction between governed
  documents. It identified the wrong document as the defective one, which is a different thing
  from being wrong.
- **It does not repair `deployment/deployment_profile.md` F-2 here.** That sentence is canonical
  at `main` and its correction belongs in a bound candidate under review, not in a prep document.
- **It does not open Routing, ROOTGUARD, or P5.** Three routing holds stand, untouched, none of
  them Plan's to lift.
- **It grants no approval and implies none.** `main` UNCHANGED at `04693e68`. Nothing has been
  canonicalized, and Plan does not execute this in any case — GATE 1 keeps proposer and executor
  distinct.
