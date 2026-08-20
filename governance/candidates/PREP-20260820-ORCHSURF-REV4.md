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
decision_record: `DEC-20260820-ORCH-SESSION-HOME` **v2**, registered at
  `c4c0fa11d5a1ca9650ca9230013fc14156dc7c42`, content sha256
  `9861fb05c66d4e763f6f1e36e012f6f019a5447356fa35ec87f0153b29c0bee7` — verified this session both
  on disk and in the blob at that commit, and the full range `5559c11..c4c0fa1` changes exactly
  one file, so no FROZEN document moved. v2 repaired two pre-ratification defects Plan raised
  against v1 (`43772c8`): an SLR misattribution in §3(d), and §3 wording that called the record
  "ratified" while `ratified_by` was empty. **Ratification attaches to this hash.** Filling
  `ratified_by` will change the bytes and yield a third hash; both must be recorded, and the
  content ratified is the one hashed before the signature
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
RATIFICATION STATUS      UNRATIFIED — `ratified_by: ""` in DEC-20260820-ORCH-SESSION-HOME v2,
                         registered c4c0fa1, sha256 9861fb05…c0bee7
EFFECT OF THE RECORD     NONE TODAY, by its own §6
WHAT IS DELIVERED HERE   the verification the record's §2 demands; eight findings that the
                         verification produced; the disposition of every revision-3 finding
                         under the new direction; the exact revision-4 change set; and the
                         resolution of the three questions the operator carried forward (§7)
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
| **body §8** | **CORRECT — AND NAMED IN NEITHER THE RECORD NOR ANY REVISION OF ORCHSURF** | see F-1. This is the finding. **v2 of the record adopts it as "Primary basis"** |
| **body §35.1** | **CORRECT — AND STILL NAMED NOWHERE** | *"Recinto Orchestrator: … NON DEVE: committare lavoro proprio; toccare worktree altrui; … **usare la root come spazio libero**"*. This is the rank-1 statement of exactly what the record's §1 item 4 calls *"root as an accidental work surface"* |
| body §11 | **CORRECT** | *"WORK_COMMIT → ogni attore, PROPRIO worktree/branch. Durevolezza di lavoro e learning. Obbligatorio, non canonico."* |
| body §18 | **CORRECT** | *"Persistenza durevole NON negoziabile: ogni record MUST raggiungere lo stato durevole via WORK_COMMIT … il messaggio notifica, il commit fa fede."* Load-bearing for F-7 |

```
SECTION REFERENCES IN THE RECORD   ALL CORRECT AS CITED, v1 AND v2
ENUMERATION IN THE RECORD          INCOMPLETE — body §8, §14 and §35.1 bear on this decision.
                                   v2 adopted §8 as Primary basis; §14 and §35.1 remain
                                   uncited. The omission does not weaken the record; all three
                                   support it, and §8 is the strongest support it has
ONE CITATION READ ONLY IN PART     the record cites body §5 for its own rank-2 position and does
                                   not carry §5's second half — the *clausola temporale
                                   (anti-trinceramento)*: "una vecchia direttiva operatore non
                                   batte l'Orchestrator di oggi … lo stato durevole delle
                                   priorità decide." The record's `applies_to` claims reach over
                                   "any future candidate", a forward scope that this clause
                                   qualifies. Not a defect in the architecture and not Plan's to
                                   settle; it is a defect in the citation, and it is the same
                                   error-shape the record itself names at its §2 — citing a
                                   section for a subordinate clause while missing an operative one
```

---

## 3 · Eight findings the verification produced

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
convention rather than applying one, and says so in its own frontmatter. **Superseded in part:
the convention now exists**, proposed by that file and exercised twice — v1 at `43772c8`, v2 at
`c4c0fa1`, the second superseding the first in place with the history preserved and unrewritten.

---

### F-7 · 🔴 The `orchestrator` worktree is absent from Annex I.2 step 4 because it is not a bootstrap artifact — and that absence is evidence FOR the operator's architecture

**The problem, stated at full strength.** Annex I.2 step 4 enumerates the worktrees the
Controller creates: *"crea/verifica worktree: lettore, lettore-b, lettore-c, evidence-index,
mirror"*. Five. **`orchestrator` is not among them, and the string appears in no FROZEN document
as a worktree to create.** `BOOTSTRAP.md` step 3 creates it anyway, citing `CAND-20260817-ORCHWT`.
The decision's §3(b) asks revision 4 to restore the bootstrap procedure *"consistent with … Annex
I.2"* **and** to retain that creation. Taken naively those two instructions collide, and the
collision is the last thing standing between this preparation and a bound revision 4.

**The defence offered until now is too weak to carry it.** Revision 3, and the first draft of
this document, answered that *I.2 step 4 enumerates worktrees to create and does not prohibit
others*. That argument treats a precise FROZEN enumeration as merely silent, and it licenses a
seventh and an eighth worktree exactly as well as the sixth. A permission argument cannot be the
grounding for a MAJOR candidate.

**The resolution is a separation, and the artifact record already contains it.** These are two
lists answering two different questions, and they were never the same list:

| | **Annex I.2 step 4** | **`deployment/deployment_profile.md`** |
|---|---|---|
| Question answered | which worktrees must exist so that the chats of I.2 step 6 have homes | where does the Orchestrator's WORK_COMMIT land |
| Rank | **1** — FROZEN, `normative: yes` | canonical content, amendable under Annex D |
| Cardinality | **five, and it is derived**: I.2 step 6 hands the operator *"la LISTA ESATTA delle 5 chat da aprire (path per ACTOR_ID)"* — one path per chat | **one, and it is derived** from the WORK_COMMIT rule: body §11, *"ogni attore, PROPRIO worktree/branch"*, and Annex H.1, *"solo proprio branch"* |
| Lifecycle | bootstrap, **pre**-promotion; a Controller act under body §0.4 | runtime, **post**-promotion |
| Established by | the governance body and Annex I | `CAND-20260817-ORCHWT` |

**The decisive measurement: ORCHWT never touched Annex I.2, and said so in its own scope field.**
`CAND-20260817-ORCHWT` frontmatter reads *"scope: deployment/deployment_profile.md ONLY. No P5.1
change, no runtime classification, no SLR integration, no lint change."* The `orchestrator`
worktree entered this system as a **deployment fact**. Nothing was ever smuggled into Annex I.2,
and Annex I.2 was never in tension with ORCHWT. The tension was manufactured in one place only —
`BOOTSTRAP.md` step 3, which names the I.2 five and the ORCHWT one in a single breath and so
presents a runtime surface as a bootstrap step.

**And the absence is not an oversight.** I.2 step 4's five map one-to-one onto I.2 step 6's five
chats, and body §47 step 10 calls them *"le cinque chat **restanti**"* — remaining, that is,
after the one already open. **The Orchestrator has no worktree in step 4 for precisely the same
reason it has no chat in step 6: its session is the root chat, which is already open and is
promoted in place.** Under revision 3's direction that absence was inexplicable and had to be
argued around. Under the operator's architecture it is exactly what the FROZEN text should say.
F-7 therefore converts the strongest apparent objection to the decision into support for it — and
the support sits at rank 1, where a rank-2 operator directive could not have put it.

**Consequence for revision 4 — and this is a change, not a preservation.** `BOOTSTRAP.md` step 3
creates the **five** worktrees Annex I.2 step 4 enumerates and nothing else, so that the file is
consistent with I.2 in the plain sense rather than the permissive one. Provisioning the
`orchestrator` work surface becomes a **named post-promotion act** governed by the deployment
profile, sequenced after body §47 step 14 and before the Orchestrator's first Session Learning
Review — which is when the surface is first needed, since §8 makes that review mandatory and §18
makes WORK_COMMIT the only route to durable state (*"il messaggio notifica, il commit fa fede"*).

```
LOAD-BEARING, NOT EDITORIAL   if revision 4 separates the lists and omits the post-promotion
                              provisioning step, a fresh install reaches ACTIVE_ORCHESTRATOR
                              with no orchestrator worktree in existence, and the first
                              Orchestrator session has nowhere lawful to commit its own work —
                              which is the exact defect ORCHWT was raised to close
DECLARED AS NEW               revision 4 must present this step as an addition, not as a
                              restoration. Nothing in FROZEN text describes it, and F-7's whole
                              argument is that FROZEN text is silent here on purpose
COST TO THE RUNNING SYSTEM    none. The `orchestrator` worktree exists at `b3596d5` and no
                              running surface is touched by any of this
FROZEN IMPACT                 none. Annex I.2 is read, not amended; its cardinality of five is
                              affirmed rather than excused
```

---

### F-8 · 🔴 Body §35.1 forbids the Orchestrator the commits that §8, §11 and §18 require of it — and the durable state shows which reading is operative

Four rank-1 sentences, read flat:

- **§35.1** — *"Recinto Orchestrator: PUÒ … git nel perimetro. **NON DEVE**: committare lavoro proprio; toccare worktree altrui; … usare la root come spazio libero."*
- **§11** — *"WORK_COMMIT → **ogni attore**, PROPRIO worktree/branch. Durevolezza di lavoro e learning. **Obbligatorio**, non canonico."*
- **§8** — the Orchestrator *"**MUST** fare Session Learning Review."*
- **§18** — *"Persistenza durevole NON negoziabile: ogni record **MUST** raggiungere lo stato durevole via WORK_COMMIT … il messaggio notifica, il commit fa fede."*

Taken flat, FROZEN text both requires and forbids the same act. **This sits upstream of all of F-7:
if §35.1 forbids Orchestrator work-commits outright, then the `orchestrator` worktree has no
purpose and step 11 provisions a surface nobody may lawfully use.**

**The reconciliation available.** §35.1's prohibition list is bracketed by *"git nel perimetro"*
and closes on *"usare la root come spazio libero"*. Read in that frame, *"committare lavoro
proprio"* forbids slipping its own work into the **canonical** surface — the root, `main`, the
batch window — which is exactly the defect `CAND-20260817-ORCHWT` was raised to close by giving
the actor a branch of its own. **That is a reading, and it is marked as one.**

**The durable state shows which reading is operative, and it is not close.** Branch `orchestrator`
carries **19** commits not present on `main` (`git rev-list --count main..orchestrator`) — lease
records, canonicalisation records, review responses. **Count corrected:** an earlier draft of this
finding named eight hashes and implied that was the population; it was a truncated `git log -8`,
and the eight named are a sample. All eight verify as reachable from `orchestrator`. The fenced
reading is not a proposal; it is what this laboratory has been doing for many sessions, and body
§36.5 says *"durable repository state decides."*

**But practice is not authority, and this cuts both ways.** If the flat reading is the correct
one, those commits are not evidence of an interpretation — they are violations of a rank-1 fence,
and that is a larger finding than anything else in this document. **Either §35.1 means what F-8
and §7.2 read it to mean, or ORCHSURF has been building on a violated invariant since
2026-08-17.** Plan may not decide it: Annex H.1 gives governance to the operator.

```
ADJUDICATED — operator, 2026-08-20, on this finding as stated above

§35.1 is a constraint on PERSISTENCE SURFACE, not a prohibition of Orchestrator WORK_COMMIT
capability. The coherent rank-1 reading is that §35.1 forbids using the ROOT/canonical surface
as an ungoverned personal work area; §11 requires every actor to have WORK_COMMIT through its
own worktree/branch; §18 requires durable state through WORK_COMMIT; §8 requires the
Orchestrator Session Learning Review. An Orchestrator worktree is therefore REQUIRED for durable
work, while the root remains session location and coordination surface.

MANDATED WORDING — revision 4 carries this formulation verbatim:

  "§35.1 constrains where persistent artifacts may be produced, not whether the Orchestrator may
   produce persistent artifacts. The Orchestrator WORK_COMMIT surface is the assigned
   worktree/branch, never the root checkout."

CONSEQUENCE   the fenced reading is authoritative. The 19 commits are lawful, not violations.
              F-7's step 11 provisions a surface that is REQUIRED rather than merely permitted,
              which raises its criticality: without it the Orchestrator cannot satisfy §8+§18
CLASS         this is an operator adjudication of a reading, at rank 2. It amends no FROZEN text
              and could not — §35.1, §8, §11 and §18 are unchanged and unchallenged
```

**One related gap, measured while checking this.** `roles/orchestrator.md` declares five
capabilities — batch dry-run, snapshot restore, messaging, lease acquisition, task assignment —
and **`WORK_COMMIT on own branch` is not among them**, while `roles/plan.md` declares exactly that
capability for itself. The Orchestrator has therefore been exercising, across those commits, a
capability its own role contract never declared and L2 never verified. `PROBE-ORCHWT-001` —
written by `CAND-20260817-ORCHWT` to measure precisely this, including *"NO root contamination …
measured, not assumed"* — **has no outcome record anywhere in the tree; enumerated, and the string
occurs in that candidate and nowhere else.** Step 11 provisions the surface for that capability.
Revision 4 should declare the gap and route the probe, not inherit the silence.

---

## 4 · Disposition of every revision-3 finding under the decision

The directive's item 6 requires the valid findings to be conserved. They are — and the test
applied to each is **whether it depends on the remediation direction**.

### 4.1 · PRESERVED — direction-independent, carried into revision 4 unchanged

| Finding | Why it survives |
|---|---|
| **T10 enumeration method** | a method for enumerating a document universe from the tree rather than from a manifest. Independent of which document turns out to be wrong. **Reproduced this session** |
| **The authority-line lesson** — `SLR-plan-0012` **P-2**, concerning `SLR-plan-0011`'s truncation | `BOOTSTRAP.md` line 5 reads `authority: Annex I.1, I.2, I.6; body §0.1–0.4, §38, §47`; `SLR-plan-0011`'s evidence block quoted it to the semicolon, and `SLR-plan-0012` P-2 is where that truncation was caught. Verified at source this session: the string `truncat` appears in `SLR-plan-0012` and **not** in `SLR-plan-0011`. **The finding lives in 0012; 0011 is where the defect lives.** Citing it as "the SLR-plan-0011 finding" sends a reader to the defective quotation instead of to its diagnosis — which is the very failure mode P-2 describes. Corrected in the decision record at v2; revision 4 must carry the corrected form. A transcription defect, true in every direction |
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
REWRITE   step 3 — **this replaces the earlier draft of this line, which retained revision 3's
          permission argument (*"I.2 step 4 … does not prohibit others"*). F-7 withdraws that
          argument.** Step 3 creates the FIVE worktrees Annex I.2 step 4 enumerates — `lettore`,
          `lettore-b`, `lettore-c`, `evidence-index`, `mirror` — and stops there, so that
          "consistent with Annex I.2" is a plain reading and not a permissive one
ADD       a post-promotion step, declared as NEW, as this file's **step 11** — immediately after
          its step 10 (*"record the registration durably → the chat is now ACTIVE_ORCHESTRATOR"*,
          which is body §47 step 14 and Annex I.2 step 10) and before the Orchestrator's first
          Session Learning Review: the `orchestrator` work surface is provisioned per
          `deployment/deployment_profile.md`. Cited to body §11 and §18, and to
          `CAND-20260817-ORCHWT`, never to Annex I.2 — the whole point of F-7 is that these are
          two lists answering two questions
STATE     explicitly, in the file, why there is no sixth worktree at step 3 and no sixth chat at
          step 5: they are the same reason, and it is the architecture — the Orchestrator's
          session is the root chat, already open, promoted in place
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
ADD       this file becomes the NAMED GOVERNING DOCUMENT of the `orchestrator` work surface, per
          F-7: it states that the surface is provisioned post-promotion, that it is NOT an Annex
          I.2 step-4 worktree, and that its cardinality derives from body §11 rather than from
          any chat list. ORCHWT's scope line — "deployment_profile.md ONLY" — is quoted as the
          evidence that this separation is original to the system and not invented by revision 4
```

### `roles/orchestrator.md` — status `PROPOSED`, **the one fingerprint input this candidate moves**

```
KEEP      `worktree: orchestrator` — correct, and the decision confirms it
FIX       `canonical_batch_surface:` — it currently reads "never this actor's home". Under the
          decision the root IS this actor's session home. The precise statement is: never this
          actor's WORK surface, and never evidence of its identity
ADD       `session_home: the repository root checkout` — a third typed field, because the
          decision names a third concept and an untyped concept is what caused this candidate
ADD       the operator's F-8 formulation, VERBATIM and quoted as an adjudication rather than
          paraphrased: "§35.1 constrains where persistent artifacts may be produced, not whether
          the Orchestrator may produce persistent artifacts. The Orchestrator WORK_COMMIT surface
          is the assigned worktree/branch, never the root checkout." It also goes in
          `deployment/deployment_profile.md`, because F-2's false sentence lives there and this
          is the true sentence that replaces its premise
ADD       `WORK_COMMIT on own branch` to the declared-capabilities table as UNVERIFIED — F-8
          measured that the Orchestrator has been exercising it across 19 commits while its role
          contract declared five capabilities and not this one
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
FROZEN DOCUMENTS        none modified, none proposed for modification, none claimed superseded.
                        Annex I.2's cardinality of five is AFFIRMED by F-7 rather than excused
BOOTSTRAP PROCEDURE     one step REWRITTEN (step 3, narrowed to the I.2 five) and one step ADDED
                        (step 11, post-promotion provisioning). The addition is the only
                        instruction in this change set with no antecedent in any governed
                        document, and F-7 declares it as new rather than as a restoration
RESOLVED IN §7          F-7 (b) and (c). The perimeter is silent post-promotion on TEMPORAL
                        scope, so "is a worktree an artifact" never has to be answered (§7.1);
                        ownership is Plan at body §47 step 15 (§7.2). Neither answer amends
                        FROZEN text. Both are readings, and both go to Mirror AS readings
F-8 ADJUDICATED         by the operator, 2026-08-20: §35.1 constrains the persistence SURFACE,
                        not the capability. The `orchestrator` worktree is REQUIRED, not merely
                        permitted, which raises step 11 from lawful to necessary. Mandated
                        wording carried verbatim into revision 4 — see F-8 and §5
MEASURED                the §7.2 provisioning gate — PASS (§8.1). PROBE-ORCHWT-001 legs 1, 2 and
                        4 — PASS from durable state (§8.2)
STILL OWED              PROBE-ORCHWT-001 leg 3 on the `orchestrator` surface, executed BY the
                        Orchestrator. Plan may not take it without writing into another actor's
                        worktree, which would corrupt what it measures. §8.3 measures the
                        MECHANISM on Plan's own surface as a positive control, and revision 4
                        must not cite that as a discharge
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

**8 · Does F-7's separation hold, or is it a distinction without a difference?** This is the
attack I most want run, because F-7 is the one place where this preparation *changes* the
bootstrap procedure rather than restoring it. Three surfaces to hit. **(a)** I claim I.2 step 4's
five are derived from I.2 step 6's five chats. A reviewer could hold that step 4 is an
independent enumeration that merely happens to have the same cardinality — in which case its
silence about `orchestrator` is silence, and revision 3's permission argument comes back.
**(b)** §7.2 reads body §0.4's *"crea/verifica i worktree"* as purpose-scoped to the bootstrap
five rather than as an exclusivity clause. A reviewer holding it exclusive leaves step 11 without
an owner, and F-7 then breaks at execution rather than at argument. **(c)** §7.1 answers the
perimeter question on **temporal** scope and deliberately never answers what an "artefatto" is.
Attack that evasion directly: if a reviewer holds the WHAT limit reaches post-promotion acts too,
7.1 collapses and the question I declined to answer becomes unavoidable.

**9 · F-8 is adjudicated, so attack the adjudication's reach rather than its merits.** The
operator settled the reading on 2026-08-20: §35.1 constrains the persistence surface, not the
capability. That disposes of the collision and Plan does not reopen it. What remains open to a
reviewer is **scope**: the adjudication is a rank-2 operator reading of rank-1 text, and body §5
puts NON-NEGOTIABLE governance above it. If a reviewer holds that §35.1's *"committare lavoro
proprio"* cannot bear the fenced reading **as a matter of text**, then the conflict is genuine and
the record's own §3 rule applies — rank 1 prevails and the reading must be revised, not §35.1.
Attack the textual fit; the authority to adjudicate is not in question.

---

## 7 · The three questions carried into revision 4, resolved

The operator carried three points forward: two governance readings F-7 left open, and one
drafting requirement. All three are answered here **without changing a FROZEN assumption**. The
discipline is the one F-7 established — refuse to read into FROZEN silence, in either direction —
and it has to cut both ways or it is not a discipline.

### 7.1 · Scope of *"SOLO artefatti di bootstrap"* — answered on temporal scope, not on what an artifact is

Answered first, because ownership depends on it. The clause exists at both ranks, and the two
copies are not identical:

- body §0.4 — *"Perimetro **di scrittura** pre-promozione: SOLO artefatti di bootstrap."*
- Annex I.2 — *"Perimetro pre-promozione: SOLO artefatti di bootstrap."*

The body carries a word the annex drops — **scrittura** — and the body outranks the annex it
derives from, which is revision 3's own §5.5 finding applied to a new sentence. The clause states
two independent limits at once:

```
WHAT   bootstrap artifacts only
WHEN   pre-promotion
```

**The second limit disposes of the question, and the first never has to be interpreted.** The
perimeter fences the BOOTSTRAP_CONTROLLER, a role that terminates at body §47 step 14 — after
which the actor is ACTIVE_ORCHESTRATOR, fenced instead by §35.1, stated separately and in
different terms. Step 11 sits after promotion. **The pre-promotion perimeter is not permissive
about step 11; it is silent about it, because its temporal scope has ended.**

This is deliberately narrower than the answer the question invites. Asking *"is a runtime worktree
a bootstrap artifact?"* would require putting meaning into FROZEN text that FROZEN text does not
carry — the exact move this whole line of work exists to stop making. The question is left
unanswered because it does not need to be answered.

**Corollary, normative rather than editorial:** step 11's *position* is load-bearing. Move the
provisioning earlier — into step 3, or anywhere before promotion — and the WHAT limit becomes live
again and must be adjudicated before the act is lawful. Revision 4 must state this in the file, so
that a later editor tidying the sequence cannot silently reopen a governance question.

**Corroboration at a lower rank, which settles nothing alone but is worth knowing.**
`CAND-20260817-ORCHWT` §5 item 2 already characterised the act: *"Creating a worktree and moving
untracked files is an **operational act, not a commit** — so it can precede the canonical commit
that records it."* That is a canonical candidate, not FROZEN. What it establishes is that this
reading is **not novel to revision 4**: the system published it, and canonicalised the candidate
carrying it, before the question was ever put. A reviewer attacking 7.1 is attacking a position
the repository already holds.

### 7.2 · Ownership of post-promotion provisioning — Plan, at §47 step 15, gated on one unrun measurement

**What §0.4 grants, and what it does not.** *"Il Controller: … crea/verifica i worktree; prepara
l'actor registry; presenta all'operatore la lista esatta delle chat da aprire …"* Worktree
creation sits mid-list among bootstrap qualification acts, and its purpose is visible two items
later: the five worktrees must exist before I.2 step 6 can hand the operator *"la LISTA ESATTA
delle 5 chat da aprire (path per ACTOR_ID)"* — a path cannot be given before it exists. **The
grant is scoped by its own purpose to the bootstrap five. It is not an exclusivity clause**, and
reading it as one would be the mirror of the error F-7 refused when it declined to read I.2 step
4's silence as permission.

**The positive anchor is already in the sequence.** Body §47 step 15 — *"Plan produce
runtime/authority inventory"* — is the first act after step 14's promotion, which is precisely
the slot step 11 occupies. Ownership converges from three directions:

| Ground | Text |
|---|---|
| the sequence | §47 step 15 places Plan immediately after promotion, on runtime matters |
| the mandating document | the `orchestrator` worktree is mandated by `deployment/deployment_profile.md`, which `roles/plan.md` gives Plan to *"materialize and maintain"* |
| the domain | `roles/plan.md` gives Plan *"the runtime / authority inventory and the Agent Card registry"*. A runtime work surface is a runtime-inventory fact |

**Ownership: Plan. No new authority is required and none is proposed.**

**The gate — `CONFIGURED != PROVEN`.** `roles/plan.md` lists *"Write within own worktree only"* as
**UNVERIFIED**, its L2 verification being *"attempt a cross-worktree write and confirm refusal"*.
Whether a harness that refuses Plan a cross-worktree **write** also refuses Plan a
`git worktree add` is a different question about a different operation. **It has now been
measured: §8.1, PASS.** Plan provisioned a worktree, wrote nothing into it, left the root
untouched and removed it cleanly. The ownership assignment is cleared at the level this gate
demanded — and at no level beyond it: the cross-worktree **write** refusal remains UNVERIFIED,
was not authorised, and was not attempted.

**Fallback, named now so it is not improvised later.** If the measurement refuses Plan, the
ACTIVE_ORCHESTRATOR provisions its own work surface as its first post-promotion act: §35.1 grants
it *"git nel perimetro"*, and a directory is not authority, so §0.2's *"mai un'autoassunzione"* —
which governs **promotion** — is not engaged. Second choice on textual grounds only; mechanically
it is the cleaner of the two, since no actor reaches across into another actor's surface at all.

```
PRIMARY     Plan, at body §47 step 15
GATE        one L2 smoke — can Plan create a worktree it will never itself write into?
FALLBACK    ACTIVE_ORCHESTRATOR self-provisions, as its first act after promotion
UPSTREAM    F-8 is ADJUDICATED — the fenced reading holds, by operator decision of 2026-08-20.
            The surface is required, so the fallback is a fallback on ownership only, never on
            whether the surface exists
MEASURED    §8.1 PASS. The PRIMARY branch is cleared; the FALLBACK was not needed and was not run
NOT ASKED   no FROZEN text is amended, and no new authority is claimed on either branch
```

### 7.3 · The two axes, carried as a drafting requirement rather than a conclusion

```
AXIS 1   SESSION_LOCATION  ≠  PERSISTENCE_SURFACE
AXIS 2   ROOT location  ≠  ACTOR_ID  ≠  write authority
```

Revision 4 carries both **into each of the four places it edits** — `BOOTSTRAP.md` (steps 3, 5,
the new 11, and the chats table), `deployment/deployment_profile.md`, `roles/orchestrator.md`, and
the re-adjudication of `runtime/bootstrap/STEP5-session-open-plan.md` — and not once in a
preamble. A separation asserted in one document and relied upon in four is how the Rev1→Rev3 drift
travelled: the true statement lived in one file and the false inference was drawn in another, and
no diff could see the join.

**Step 11 is itself an instance of axis 1** — it provisions a persistence surface for an actor
whose session location is elsewhere — so it must carry the axis inline as its stated rationale
rather than merely comply with it. That is the difference between a rule a file follows and a rule
a file teaches.

Axis 2 is decision item 3, already endorsed and preserved (§4.1, final row). Nothing in 7.1 or 7.2
touches it: neither the temporal reading of the perimeter nor Plan's ownership of provisioning
makes any location confer identity or authority on anyone.

---

## 8 · Measurements — authorised by the operator, executed, recorded

Two measurements were authorised: the §7.2 provisioning-ownership gate, and `PROBE-ORCHWT-001`.
Both are recorded here at their real strength, including the half of the second that Plan may not
take.

### 8.1 · SMOKE-PLAN-PROVISION-001 — can Plan create a worktree it will never write into? · **PASS**

Executed this session from the `evidence-index` worktree, branch `orchestrator-surface`. The
target path was the session scratchpad, deliberately **not** `.claude/worktrees/`, so that no
other session could pick the probe up as an actor surface. Detached HEAD, so no branch was
created.

| Leg | Expected | Measured |
|---|---|---|
| provisioning act | `git worktree add --detach` succeeds for Plan | **EXIT=0** — *"Preparing worktree (detached HEAD 4abcfc0)"* |
| worktree is real | resolves its own top-level and HEAD | HEAD `4abcfc0`, top-level = the probe path |
| **Plan writes nothing into it** | porcelain empty | **empty** — creation and write are separable acts, which is the whole question |
| **root not perturbed** | `git -C <ROOT> status --porcelain` unchanged | **empty before and after**; root HEAD `04693e68` unchanged |
| Plan's own surface | unchanged apart from the PREP edit | unchanged |
| reversible | `git worktree remove` restores the set | count **14 → 15 → 14**, path removed, **no stray branch** |

```
VERDICT      PASS. Plan can provision a worktree without writing into it and without touching
             the root. §7.2's ownership assignment — Plan, at body §47 step 15 — is CLEARED at
             the level the gate demanded
WHAT IT DOES NOT ESTABLISH
             it does not test provisioning INTO `.claude/worktrees/`, and it does not test
             whether Plan is refused a cross-worktree WRITE. That refusal is the L2 verification
             `roles/plan.md` still carries as UNVERIFIED, it was NOT authorised here, and it was
             not attempted. Confirming a boundary by crossing it is not a measurement Plan takes
             on its own initiative
STATUS OF THE CAPABILITY
             the provisioning capability is now MEASURED. `CONFIGURED != PROVEN` is satisfied for
             this act and for no other
```

### 8.2 · PROBE-ORCHWT-001 — three legs discharged from durable state, one leg NOT Plan's to take

`CAND-20260817-ORCHWT` wrote this probe on 2026-08-17 and it had **no outcome record anywhere in
the tree** — verified by enumeration; the string occurs in that candidate and nowhere else.

**The probe as written cannot be executed by Plan.** Its INPUT is *"the Orchestrator chat,
operating in the worktree `orchestrator`"*, and its artifact is written there. Plan writing into
another actor's worktree is precisely the boundary this probe exists to characterise, and
`roles/plan.md` confines Plan to its own surface. **Executing it would corrupt the thing being
measured.** So the probe is split at its natural seam:

| Leg | Probe's expectation | Method | Result |
|---|---|---|---|
| 1 | a WORK_COMMIT exists on branch `orchestrator`, **non-canonical** | `git rev-list --count main..orchestrator`; `git merge-base --is-ancestor orchestrator main` | **PASS** — 19 commits ahead of `main`; the tip is **not** an ancestor of `main`, so nothing leaked into canonical history |
| 2 | branch ownership correct — HEAD is `orchestrator`, not `main` | `git worktree list --porcelain` read from Plan's own worktree | **PASS** — `branch refs/heads/orchestrator`, HEAD `b3596d5` |
| 4 | the commit is reachable | `git merge-base --is-ancestor <c> orchestrator` on all eight cited hashes | **PASS** — all eight reachable |
| **3** | **NO root contamination, measured before and after** | **requires a live run at commit time** | **NOT DISCHARGED — and not retrospectively discharge­able** |

**Why leg 3 resists retrospection.** It is a before/after assertion about the root at the moment
of a commit. Nothing in the durable record captures the root's porcelain at the instant those 19
commits were made, and no amount of reading after the fact recovers it. A green legs-1-2-4 says
the commits landed in the right place; it says **nothing** about what the root looked like while
they were landing.

**A positive control on the mechanism, taken on Plan's own surface.** Leg 3's mechanism — *does an
actor committing inside its assigned worktree perturb the root?* — is measurable without touching
anyone else's surface, by instrumenting Plan's own authorised WORK_COMMIT of this document. That
measurement is recorded at §8.3.

```
OWED         PROBE-ORCHWT-001 leg 3, on the `orchestrator` surface, executed BY the Orchestrator
             under its own authority. Routed, not taken. Revision 4 names it as an open
             measurement rather than inheriting the 2026-08-17 silence
NOT A SUBSTITUTE
             §8.3 measures the MECHANISM on Plan's surface. It is a positive control, not a
             discharge of leg 3, and revision 4 must not cite it as one
```

### 8.3 · CONTROL-PLAN-WORKCOMMIT-001 — does a WORK_COMMIT inside an assigned worktree perturb the root?

Leg 3's mechanism, measured on the only surface Plan may lawfully measure it on: its own. The
instrument is the operator-authorised WORK_COMMIT of this document — root porcelain and root HEAD
captured immediately before and immediately after, on the real repository rather than a throwaway.

```
METHOD    git -C <REPO_ROOT> status --porcelain  +  rev-parse HEAD   → before
          git commit on branch orchestrator-surface, worktree evidence-index
          git -C <REPO_ROOT> status --porcelain  +  rev-parse HEAD   → after
          root is UNPERTURBED iff both readings are identical and porcelain is empty in both
```

**Result: recorded in the commit that immediately follows this one**, because a measurement of a
commit cannot be inside the commit it measures. That second commit is instrumented identically,
so the pair is self-checking: if the mechanism perturbs the root, the second measurement catches
what the first would have had to report. Neither commit is amended — amending would rewrite the
history the measurement is evidence about.

## 9 · What this document does NOT do

- **It does not claim `DEC-20260820-ORCH-SESSION-HOME` is in force.** It is unratified, and its
  own §6 governs. Everything in §5 is conditional on ratification.
- **It is not revision 4.** No manifest, no `CANDIDATE_CONTENT_HASH`, no `BASE_HEAD` binding, no
  content file edited. Revision 3 remains the delivered package and its binding is untouched.
- **It does not modify, propose modifying, or claim to supersede any FROZEN document.** Body and
  Annex I.2 are correct under this direction, which is the point.
- **§7 offers readings, not adjudications.** 7.1 and 7.2 answer the two questions carried forward
  by reading FROZEN text at its stated scope; neither is a ruling, and Plan has no authority to
  make one. They are written to be attacked at §6 items 8 and 9, and they travel to Mirror as
  readings that a reviewer may reject without any FROZEN text having moved.
- **It does not settle F-8, and revision 4 must not be bound while F-8 is open.** Whether §35.1
  is fenced or flat decides whether the `orchestrator` worktree may be used at all. Plan states
  the collision, states which reading the durable state supports, and stops there.
- **It runs neither unmeasured probe.** The §7.2 capability gate and `PROBE-ORCHWT-001` are named
  and left unexecuted. Naming a measurement is not taking it, and a green probe would still be
  `CONFIGURED`, not `AUTHORISED`.
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
