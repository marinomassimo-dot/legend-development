---
artifact: MIRROR hostile review (Annex C.2)
review_id: REV-XPORT-MIRROR-001
object: CAND-20260819-XPORT rev 1 · CANDIDATE_CONTENT_HASH 68173f01…c96a @ base 4454feab
level: R4 (MIRROR_REQUIRED — Annex G.1: a normative protocol binding every actor; MAJOR)
reviewer: mirror
author: plan
adjudicator: operator (MAJOR → HUMAN_APPROVAL, Annex J.3) — none granted, none implied here
date: 2026-08-19
scope: TRANSPORT ONLY. Actor session lifecycle, CURRENT routing, activation and supersession are
  NOT canonicalized by this object and were not reviewed as if they were.
supersedes: nothing. No prior review of this object exists.
verdict: REQUEST CHANGES — one blocking finding, M-1. The architecture, the partition, the
  routing deferral, the evidence discipline, the binding and the regression accounting all hold;
  the normative artifact carries a self-description its own text falsifies, and the concession
  lives in the control plane where it does not travel with the protocol.
governance_loaded: 3.1.1 · mirror fingerprint 3dff8954…f65c, identical at BASE_HEAD and at the
  candidate content tip
reviewer_runtime: 2.1.233 — DIFFERENT from the candidate's VERSION_OBSERVED 2.1.232. Every
  version-bound guarantee entered REVALIDATION_REQUIRED for this reviewer, and was re-run.
---

# The rule fired on its first reader, and the sentence that says the protocol names nobody names three

Reviewed from `R-1`. **VERDICT TRANSFER: NONE.** Nothing carries over from `GOV311`, `HASHDET`,
`P51C9`, `ORCHWT`, `SUNSET-DEC3` or `SCIENTIST-AB-SPEC` — not a verdict, not a gate, not a row.
Every number below was re-derived in detached worktrees of `BASE_HEAD` and of the candidate
content tip, or observed live from this session's own runtime. Never in another actor's worktree,
never in root.

---

## 0 · Rehydration — fail-closed, PASS

```
pwd == git top-level == .claude/worktrees/mirror     branch mirror · HEAD 98f87665 · clean
ACTOR_ID           mirror · roles/mirror.md read in full · PERSISTENT_LEGEND_ACTOR · worktree mirror
AUTHORITY          hostile review (Annex C.2) · governance adjudication of doubtful MAJOR ·
                   E.2 epistemic curation · G.3 metrics. NO command over any actor.
                   NO primary evidence. Mirror does not review itself (G.2).
ALLOWED WRITES     reviews/mirror/ · learning/mirror/ on branch mirror
FORBIDDEN          canonicalization · HUMAN_APPROVAL · opening a review (Annex C.3, Orchestrator's)
                   · self-ratification of Mirror methodology (G.2)
RELATION TO PLAN   Plan proposes, Mirror reviews. AUTHOR ≠ REVIEWER ≠ ADJUDICATOR (C.3)
GOVERNANCE         3.1.1 · Annex B (B.1–B.5), Annex C (C.1–C.4), Annex E, Annex G, Annex H.1,
                   Annex J.0, P2, P5 — read at BASE_HEAD, not from this worktree's stale copy
CANONICAL MAIN     4454feab72b7a0edf65f191be62aeedd899a15ad — verified independently
FINGERPRINT        compose --role mirror → 3dff8954d4f6a56f6be14bc72be369095a1436437913a1e908c4b33c9762f65c
                   at BASE_HEAD and at content tip f48a807 — IDENTICAL, measured
```

🔴 **One rehydration hazard, recorded because it nearly cost the review its first finding.** This
worktree's HEAD (`98f87665`) has diverged from canonical `main` and carries an **older** copy of
`governance/plan_defined_parameters.md` — `CANDIDATE_HASH_VERSION: legend-candidate-v3`, with
`CONTROL_PLANE_ROOTS` lacking `reviews/`. Read from the checkout, that copy would have made
`reviews/plan/AUTHOR-RESPONSE-SCIAB-MIRROR-006.md` look like **content** and the candidate's
binding invariance look **false**. Governance was therefore re-read at `BASE_HEAD` throughout, and
the hash script — which reads § P5 *from the tip being hashed, never from the working tree* —
is correct on exactly this point.

**MIRROR REHYDRATION: PASS.**

---

## 0A · Manual review-endpoint selection record — OBSERVATION ONLY

Canonical actor routing is unresolved. The Human Operator manually opened and selected this
session for this review. That act is recorded here as evidence, and as nothing else.

```
SESSION_REF (SESSION_ID)   c91ba06d-6991-4dbf-b26c-cc6ae9d62147   OBSERVED
SESSION_NAME               mirror-44                              OBSERVED
PID                        58192                                  OBSERVED
CWD                        .claude/worktrees/mirror               OBSERVED
SESSION RUNTIME / VERSION  2.1.233                                OBSERVED — from this session's
                           own process image (`ps -o args=` on the parent pid), NOT from
                           `claude --version`, which reports a different binary
SELECTION METHOD           MANUAL OPERATOR SELECTION
PURPOSE                    independent review of CAND-20260819-XPORT

ROUTING CLAIM              NONE
CURRENT_SESSION CLAIM      NONE
SUPERSESSION CLAIM         NONE
REGISTRAR CLAIM            NONE
UNIQUENESS CLAIM           NONE — seven other live sessions sit in this worktree
```

**MANUAL REVIEW ENDPOINT: OBSERVED. CANONICAL ROUTING CLAIM: NONE.**

The operator is not described here as a registrar, de facto or otherwise. This selection creates
**evidence for future routing design**; it establishes no routing governance, and Candidate B may
cite it as an observation of how the laboratory currently closes the gap — not as a precedent for
who may close it.

---

## 0B · Volatile session-inventory snapshot — read-only

The durable design record carries *cardinalities* (§6) but not the machine-readable inventory
behind them. One read-only snapshot was taken. Nothing was activated, closed, killed, renamed,
superseded, cleaned, or declared CURRENT.

```
OBSERVATION TIME     2026-08-19T15:25:31Z
COMMAND              claude agents --json   (and --all)
INSTRUMENT RUNTIME   2.1.232 — the CLI on PATH, <HOME>/.local/bin/claude →
                     ~/.local/share/claude/versions/2.1.232. NOTE: this is NOT this session's
                     runtime (2.1.233). The instrument's version is recorded separately from
                     the observing session's, because they are different binaries.
RAW OUTPUT           session scratchpad, agents.json — outside the repository by intent;
                     a volatile runtime listing is not durable state and is not committed
```

```
ACTOR_ID        worktree         live sessions      cardinality
scientist-a     lettore                    0        ZERO
scientist-b     lettore-b                  0        ZERO
scientist-c     lettore-c                  1        ONE
plan            evidence-index             8        MANY
mirror          mirror                     8        MANY  ← 7 pre-existing + this session
orchestrator    root checkout              3        contested (see §13.A)
                orchestrator worktree      0
total rows      20 (CLI, self included) · 19 (ListAgents, self excluded) · 20 local sockets
--all           24 rows · 4 with pid null: scientist-a (failed), qualification-probe (stopped),
                git status report (done), one unnamed (failed)
```

**INTERPRETATION.** The design record's `mirror: 7` is confirmed as the count *before* this
session existed; my own arrival made it 8, which is itself the cleanest available demonstration
that the cardinality is a property of the moment and not of the actor. `scientist-a` and
`scientist-b` at ZERO are confirmed — **and are a measurement that they were not activated**, not
a step toward activating them.

This snapshot is **OBSERVATIONAL EVIDENCE**, not routing state.

---

## 1 · Binding — PASS

Reproduced independently, with the script read from `BASE_HEAD` (this worktree's copy differs).

```
BASE_HEAD               4454feab72b7a0edf65f191be62aeedd899a15ad     verified independently
CONTENT TIP             f48a807f7ba7b5b71c0ba5dd5d2361fc7dca57e4     verified — full SHA
MANIFEST TIP (§14)      268df0420a21b47c48dbedb4815ea428c76fb57f     verified
MANIFEST TIP (at review) c748d271de57c9bb73b755184401fddd6e614833    verified
CANDIDATE_HASH_VERSION  legend-candidate-v4                          matches canonical P5 at main
CANDIDATE_CONTENT_HASH  68173f010392e57b1b7cf252df6efa8b6fe7c017f563584bf3cd10695978c96a

measured at f48a807  →  68173f01…c96a    531 included · 33 excluded
measured at 268df04  →  68173f01…c96a    531 included · 37 excluded
measured at c748d27  →  68173f01…c96a    531 included · 37 excluded
```

**Invariance holds at every tip on the branch after `f48a807`**, which is the invariant §14 asks a
reviewer to check, and it is the right one — *the manifest tip is final* never is.

```
POSITIVE CONTROL   CAND-20260818-SCIENTIST-AB-SPEC, base cbce3016 tip 2a854177
                   → beef6db08bdf8489b68078fc00c08fee913a585a4e1ee8359b592fc9e31a6061
                   reproduces the published value EXACTLY
NEGATIVE CONTROL   same tip, base main^^        → 1a7eb5c2…  (differs)
                   correct base, tip = main     → 7f35657f…  (differs)
```

🔴 **One negative control of mine was void and is recorded rather than dropped.** I first ran the
wrong-base control using `cbce3016`, then a second using `main^` — and `main^` **is** `cbce3016`.
Two "independent" controls were one input, and they agreed for that reason and no other. Re-run
with `main^^` before being reported. A control that is secretly the same control is a wrong-reason
pass in the reviewer's own harness.

**Population, classification, sorting, control-plane exclusion** — all verified via `--show-domain`:
37 excluded paths at the manifest tip, every one under `governance/candidates/`, `ledger/` or
`reviews/`; nothing under `framework/`, `disease-models/`, `roles/`, `scripts/`, `learning/` or
`deployment/` excluded. `learning/` is correctly **inside** the domain, so both SLRs move the hash,
as P5.1 intends.

**BINDING: PASS.**

---

## 2 · Runtime scope and version binding — and the rule fired on its first reader

This is the section the candidate most wanted attacked, and the attack succeeded in the
candidate's favour.

**This reviewing session runs 2.1.233. The candidate's guarantees are bound to 2.1.232.**

```
OBSERVED  this session's parent pid 58192 →
          ~/.vscode/extensions/anthropic.claude-code-2.1.233-darwin-arm64/…/claude
OBSERVED  claude --version (PATH) → 2.1.232, resolving to
          ~/.local/share/claude/versions/2.1.232 — a binary hosting ZERO live sessions
OBSERVED  live process census by hosting binary:  2.1.232 × 11  ·  2.1.233 × 9
OBSERVED  4 extension versions installed: 2.1.232 · 2.1.233 · 2.1.234 · 2.1.235
```

So protocol §3's trigger — *the acting session's runtime version differs from `VERSION_OBSERVED`*
— **fired on the very first session to read the protocol.** The handoff asks (§2.3) whether the
revalidation rule bites or is "a sentence nobody will run". It ran, unprompted, on contact, and it
sent me to re-measure rather than to inherit. Every version-bound claim below was therefore
re-observed at 2.1.233, and every one reproduced. The candidate is **stronger** after this than
before it: its load-bearing runtime facts are now observed at two runtime versions, not one.

```
MULTIPLE INSTALLED VERSIONS        CONFIRMED
LIVE RUNTIME VERSION MULTIPLICITY  CONFIRMED — two versions hosting live sessions concurrently
RUNTIME VERSION MODEL              ENDPOINT_INTERACTION_SCOPED — correct
```

**Per-guarantee runtime scope, checked against the mechanism rather than against convention:**

| guarantee | RUNTIME_SCOPE | bound versions | verdict |
|---|---|---|---|
| `to` rejected at 213 chars, pre-send | **SENDER_ONLY** — `InputValidationError`, the tool never ran | sender 2.1.232 (Plan) + **2.1.233 (this review)** | correctly scoped; recipient version irrelevant and correctly not required |
| `summary` accepted at 264 chars, silently | **SENDER_ONLY** for the acceptance; recipient completeness **UNVERIFIABLE** | sender 2.1.232 + **2.1.233** | correctly scoped, and the protocol does **not** infer recipient-side completeness from sender-side acceptance |
| `TARGET_UNRESOLVED` structured result | **SENDER_ONLY** | sender 2.1.232 + **2.1.233** | correct |
| `summary` truncated to 200 on delivery | **RECIPIENT_ONLY / UNOBSERVED** | — | correctly left `DOCUMENTED, not observed` |
| `message` bound | **UNKNOWN** | — | correctly `UNKNOWN`; not discovered by abuse |
| recipient processing classes | **RECIPIENT_ONLY** | `MEASURED_EARLIER`, KERNEL_SPEC | correctly cited, not re-asserted |
| self-observable `SESSION_REF` | **SESSION_OWNER_RUNTIME** via CLI instrument | observed 2.1.232 + **2.1.233** | correct |

**`claude --version` is never used in the candidate as evidence about a session's runtime.** I
tried to make it so and could not: the design record's §1 table explicitly assigns it the question
*"which CLI a shell command will run"*, and the protocol §3 says a machine-level version string is
not evidence about any session. **NOT MISUSED.**

**FAILURE_MODE_STILL_POSSIBLE, correctly carried:** recipient-side endpoint versions are unknown
for every send, because the sender cannot observe the peer's binary. The protocol does not claim
otherwise anywhere.

---

## 3 · Harness design record — PASS

Read in full. The four classes (`DOCUMENTED` / `OBSERVED` / `REPORTED_UPSTREAM` / `PROPOSED`, plus
`MEASURED_EARLIER`) are kept apart consistently, and I found no claim written in a class stronger
than its evidence. Reproduced independently at 2.1.233:

```
✅ §3.2/3.4  ListAgents returns 19 rows, SELF EXCLUDED (my own row absent), [ref] shown,
             no sessionId/cwd/pid
✅ §3.3/3.4  claude agents --json returns 20 rows, SELF INCLUDED — my own row returned with
             name · sessionId · cwd · pid · startedAt. 19 = 20 − self, exactly as recorded
✅ §3.1      SendMessage is a DEFERRED tool in this interactive session too — a ToolSearch was
             required before the first call. H-8 confirmed at a second version
✅ §5        `scientist-a` still resolves under --all to job 2e2571b7, kind background,
             state failed, pid null. A name outliving its session: confirmed
✅ §6        plan 8 · mirror 7(+me) · scientist-a 0 · scientist-b 0 · scientist-c 1
✅ §6        evidence-index-59 (pid 3125, e49d3bd1…) is ALIVE, started 2026-08-16, and is NOT the
             session that authored this candidate (pid 49611, 5c896a65…). H-6 confirmed
✅ §7 H-2    legend_launch.sh:48 CERTIFIED_VERSION=2.1.231; :112 reads `claude --version`; :116
             refuses on mismatch. Today that reads 2.1.232 → the kernel would refuse every launch
✅ §7 H-3    legend_launch.sh:365 requires kind==background; every LEGEND session observed today
             is kind: interactive. As written the kernel cannot birth or recover any current actor
✅ §9        20 local sockets = 20 CLI rows; locally cross-checkable, no completeness signal
✅ §10       roles/orchestrator.md:5 "the repository root checkout" vs deployment_profile.md:31
             "`orchestrator` — its own worktree". Both canonical in main. Contradiction confirmed
✅ §13 H-12  exactly 4 snapshot tags missing, 2 present — four instances, not one
```

**One precision correction, aimed at Candidate B rather than at this candidate.** The review
directive paraphrases the finding as *"`claude --version` returns a third binary/version that
hosts none of those measured sessions."* The **binary** reading is confirmed — the PATH CLI is a
distinct binary hosting zero sessions. The **version** reading is false: `2.1.232` is not a third
version, it is the version hosting eleven live processes including the Plan session that authored
this candidate. **The design record does not make the version claim** — §1 records the number and
assigns the surface its question — and the manifest §6 says *"a third binary that hosts nothing"*,
which is accurate. Recorded so the looser reading is not carried into Routing.

**HARNESS DESIGN RECORD: PASS.**

---

## 4 · Negative capability claims are instrument-bound — E5 — PASS

E5's text, in full: *"**Not obtainable: `session_ref`** — `ListAgents` lists peers; a session does
not appear in its own listing. The field is dropped from the schema."*

```
E5 ORIGINAL CLAIM               ABSOLUTE in its headline assertion ("Not obtainable"),
                                INSTRUMENT_SCOPED in the evidence stated one clause later.
                                The two do not match, and the headline is what got quoted.

E5 EVIDENCE ACTUALLY SUPPORTS   `session_ref` is NOT_OBSERVED_VIA ListAgents; a session does not
                                appear in its own ListAgents listing.
                                🔴 That measurement is STILL TRUE. I reproduced it today at
                                2.1.233: 19 peer rows, my own row absent.

NEW OBSERVATION                 `claude agents --json` returns the calling session's own row —
                                name, sessionId, cwd, pid. Reproduced by me at 2.1.233.

PHASE-1 E5 STATUS               CORRECT_FOR_LISTAGENTS_ONLY, with the conclusion a
                                FALSE_GENERALIZATION of its own evidence.
                                🔴 NOT "superseded by new tooling" — verified: the second
                                instrument was already in the repository. `legend_launch.sh`,
                                tracked in main, calls `claude agents --json` at lines 156, 311,
                                339 and 446. The instrument existed and was in use.

HISTORICAL RECORD               PRESERVED. The candidate edits none of the five artifacts and
                                rewrites no measurement. `SLR-plan-0006.md` is likewise not
                                edited — the correction is a separate appended record.
```

**NEGATIVE CAPABILITY CLAIM DISCIPLINE: PASS.** The candidate narrows the claim to its instrument,
keeps every conclusion the artifacts drew from it, and refuses the inference that would have been
the real error — `SESSION_REF OBSERVABLE` → `ROUTING READY`. Protocol §9 adds none of the
permissions self-observability might seem to license, and says why: observing your own address
tells you where you are and says nothing about whether you are the current incarnation.

I also verified L-2's supporting claim: `actor_identity_feasibility.md` carries **no**
`VERSION_OBSERVED` on any verdict. A feasibility report whose negatives have no revalidation
trigger is exactly the artifact that gets quoted as settled law.

---

## 5 · Transport / Routing partition — PASS

Tested against the six questions rather than accepted on the manifest's argument.

1. **Can Transport be specified without choosing CURRENT routing semantics?** Yes, and it is. The
   rule *authoritative content lives in a durable artifact, the message carries a pointer* is true
   whoever the recipient is. Its truth conditions never mention a resolver.
2. **Hidden routing state machine?** None. I read the protocol for any clause that stores,
   transitions or elects. §9 contains **only refusals** — never elect by latest chat, last seen,
   recency, registration, last responder — plus a fail-closed rule. A refusal needs no mechanism
   and creates no state.
3. **Activation / supersession authority introduced indirectly?** No. The words appear only in the
   manifest's §8, which is control plane, and in the design record, which binds nobody.
4. **Does it depend normatively on a unique CURRENT recipient?** Term 3 of §8 does — and the
   protocol marks it **unsatisfiable today**, in the same block, rather than assuming it. That is
   the honest structure: the conjunction is complete, and one term is openly unmet.
5. **Do its guarantees survive with routing unresolved?** Yes. The durable-artifact rule, the depth
   rule, the version binding, the per-field size table and the outcome taxonomy are all
   recipient-agnostic.
6. **Are tests needing a unique recipient classified honestly?** Yes — `T-TRANSPORT-1` is `NOT RUN`,
   and it is the only one that needs one.

**T-TRANSPORT-1's reason verified and endorsed.** Running it requires electing one of eight live
Mirror sessions with no governed state to elect against — the exact defect Candidate B exists to
fix. A `PASS` so obtained would measure luck. **I applied the same discipline to my own
reproductions**: every probe I ran targeted a deliberately unresolvable name, so no peer was
contacted and no recipient was elected.

**TRANSPORT / ROUTING SPLIT: PASS. ROUTING SOLVED BY XPORT: NO.**

---

## 6 · Routing deferral — JUSTIFIED

All four holds read at source, not taken on report.

```
✅ HOLD 1  PROPOSAL-C9-STATE-MODEL: `acceptance_is_not_adoption: true` and
           `hold: no implementation and no governance modification until that review completes`
           — quoted verbatim at lines 21–23. Its §7.2 is on point and is frozen.
✅ HOLD 2  actor_identity_proposal.md:7 — BUILD_MINIMAL_DIRECTORY "🔴 provisional, pending
           operator acceptance". `framework/state/actors.yaml` ABSENT from main: Phase 0 never ran.
✅ HOLD 3  MULTI_AGENT_ARCHITECTURE_FEASIBILITY "PRESERVED, NOT AUTHORIZED, NOT STARTED"
✅ HOLD 4  E5 requires re-running — established in §4 above
```

I looked for the narrow scoping the handoff invites (§4: *is there a scoping inside Plan's
authority touching none of the four holds?*) and **did not find one**. Any resolver must decide
where `CURRENT_SESSION_REF` lives; the four candidate homes are C-9 §7.2 (held), the actor
directory (held), the Agent Card (single-writer, `runtime/` classification open) and the
out-of-repo lineage store (unversioned, unauditable). Three are held and the fourth is outside the
repository. A resolver built on any of them ratifies a held decision by using it.

**Plan correctly refused to advance Routing. ROUTING DEFERRAL: JUSTIFIED.** I neither solved these
debts nor demanded that XPORT contain routing, a registrar, activation, supersession, generation
or a lifecycle state machine.

---

## 7 · Field-specific size and truncation — PASS · and `summary` — PASS

**Reproduced at 2.1.233, both probes against an unresolvable target. No peer contacted.**

```
SCHEMA, read at source this session (2.1.233):
  to        pattern ^[^\n\r]{0,200}$        200, and forbids CR/LF
  summary   maxLength 200 — and the description states outright: "longer summaries are
            truncated to 200 characters rather than rejected"
  message   NO declared bound

T-TRANSPORT-2  `to` = 213 chars  →  InputValidationError
               code invalid_format · format regex · pattern /^[^\n\r]{0,200}$/ · path ["to"]
               "must be a single-line recipient name or address"
               The tool never ran. Rejection is SCHEMA-LEVEL, pre-send, sender-visible.

T-TRANSPORT-3  `summary` = 264 chars  →  NOT rejected. The call proceeded to target resolution
               and returned {"success":false,"message":"No agent named '…' is reachable…"}

CONTROL        the same send with a 42-char in-bounds summary returned a BYTE-IDENTICAL result.
               🔴 Sender observability of the oversize: NONE. Confirmed, not inferred.
```

**The asymmetry is real, and it is the finding — not the numbers.** Two bounds in one schema; the
`pattern` is enforced and the `maxLength` is not, with nothing in the declaration distinguishing
them. The generalisation the protocol draws — *enforcement is established by probe, per field, per
version, or the field is treated as unbounded* — is **the right width**. It is not "one measurement
wearing a rule": it is a rule about **declarations**, supported by a case where a declaration was
honoured and a case where it was not, in the same schema, at two runtime versions.

```
TO FIELD       200 characters, JSON string length · SENDER_ONLY · schema-level ·
               OBSERVED rejected at 213 · at 2.1.232 AND 2.1.233 · deterministic bracket:
               ≤200 accepted by schema, 213 rejected. The exact boundary between 201 and 212
               was NOT probed and is NOT claimed — the declared bound and one rejection above it.
SUMMARY FIELD  200 declared, NOT ENFORCED · SENDER_ONLY for acceptance · accepted at 264 ·
               at 2.1.232 AND 2.1.233 · truncation-on-delivery DOCUMENTED, never observed ·
               recipient completeness UNVERIFIABLE from the sender
MESSAGE FIELD  UNKNOWN — no bound declared, none probed, and correctly not discovered by abuse
```

**NO NAKED NUMBERS: satisfied.** The one number carried binds all seven fields. Plan did **not**
generalise a field-specific result into "a SendMessage limit" — I looked for that phrasing and it
does not occur; §4's table is explicitly per-field, and §2 sets no body budget.

**FIELD-SPECIFIC SIZE MODEL: PASS.**

### 7A · `summary` — hostile falsifier PASS

The correct posture is *non-authoritative until positively proven otherwise*, not an eternal
prohibition, and that is what the protocol adopts: `summary` is a UI preview, and §4's consequence
paragraph gives the mechanism-based reason rather than a taboo.

**Falsifier run:** alter, truncate and remove `summary` while preserving the durable object and the
control envelope. I grepped every occurrence of `summary` in the protocol — six, all of them
*measurement, taxonomy or prohibition*. **No normative clause conditions correctness on `summary`.**
The control envelope (§1.2) does not contain the field at all. Removing it changes nothing.

```
AUTHORITATIVE SEMANTICS: UNCHANGED     →  DURABLE PAYLOAD RULE holds under the falsifier
SUMMARY AUTHORITATIVE STATUS: NON_AUTHORITATIVE
SUMMARY HOSTILE FALSIFIER: PASS
REPRODUCTION SAFETY: satisfied — unresolvable target, no peer elected, no session contacted
```

### 7B · The fail-fast claim — correctly NOT promoted

Operator-conversation claims that newer versions reject oversized cross-session payloads fail-fast
are **not** promoted anywhere in the candidate. What the candidate carries is narrower and
measured: `to` rejects pre-send at the installed runtime. The `summary` truncation behaviour is
`DOCUMENTED` (tool description) and explicitly *"not observed"*; `message` stays `UNKNOWN`.

**FAIL-FAST CLAIM: DOCUMENTED for `to` (and OBSERVED at two versions); the broader upstream claim
is not promoted and does not appear.**

---

## 8 · Durable payload, delivery taxonomy, ACK — PASS

**It extends, it does not duplicate.** Verified against Annex B at source: no new message type (B.2
untouched), no new envelope field (§1.2 uses B.1's fields and fills `DURABLE_POINTER`), no second
ACK, no second escalation path, no parallel authority source. Annex B remains FROZEN and unedited.

**Prior art is real, not decorative.** Body §21 line 301 carries both quotes verbatim: *"messaggi =
pointer, stato durevole decide"* and *"receipt ledger — non la queue — decide il «letto»"*.
`roles/plan.md`:88 carries *"the message notifies, the commit is what happened."* The rule is the
missing **consequence** of law already on the books, which is the cheapest legitimate shape for a
new protocol.

**The ACK-durability question (handoff §2.6), tested.** Annex B.3 requires an ACK and does not say
durable — so is §8's durability a new requirement wearing the clothes of a minimal extension? No,
and B.3 itself is the reason: its own `FAILURE` row names *"ACK emesso ma lavoro mai partito
(classi misurate: turno troncato, permission prompt)"*. B.3 measured the failure that a
message-only ACK cannot detect; §8 closes it for authoritative content only, using body §21's
receipt-ledger precedent. **Minimal extension, correctly scoped.**

**The four boundaries hold, and none implies the next.**

```
SEND INVOKED  !=  DELIVERY ACCEPTED  !=  RECIPIENT PROCESSED  !=  DURABLE ACK  !=  HANDOFF
```

Sender-side success is **term 4 of six**, and terms 1, 2, 5 and 6 are facts about durable state
that a message cannot manufacture. **Sender-side success cannot establish handoff. NOT BLOCKING.**

**Recipient-processing failures are represented**, by citation rather than restatement:
`MESSAGE_TURN_TRUNCATION` (defined by symptom, two observed instances, different mechanisms),
`TOOL_DEFERRED`, `TOOL_UNAVAILABLE`, `NOT_EMITTED`, `EMITTED_NOT_ARRIVED`. I checked the retelling
against `KERNEL_SPEC` and it is accurate; the `TOOL_DEFERRED` / `TOOL_UNAVAILABLE` merge is
explicitly forbidden.

*On the handoff's own §2.5 challenge* — is citing a non-normative launch spec from a normative
protocol sound? **Yes, on balance.** The citation is to *measured failure classes*, i.e. evidence,
not to normative authority; and the repository's own rule against implementing one thing twice
makes restatement the worse option. One residue, non-blocking: the protocol does not pin
`KERNEL_SPEC` to a version or commit, so a future revision of a frozen-but-not-canonical document
would silently change a normative protocol's referenced classes. Worth a pin; not worth blocking.

**A failure class with no detector says so.** Term 5 — *the recipient read it* — carries
`🔴 DETECTION: NONE — ATTENTION_ONLY`. `DISCOVERY_INCOMPLETE` is marked *structurally unavailable*.
`DELIVERY_UNKNOWN` is declared the residual and required to stay non-empty. `OTHER` is present.
**CONFIGURED != PROVEN is respected throughout**, and `ENFORCEMENT MODE: PROCEDURAL` is stated in
the guarantee block rather than a footnote. No Annex J.0 vocabulary violation: nothing here is
called atomic, guaranteed, enforced or exactly-once.

```
DURABLE PAYLOAD RULE: PASS · DELIVERY TAXONOMY: PASS · RECIPIENT PROCESSING: PASS
HANDOFF REQUIRES DURABLE ACK: PASS
NO SILENT PAYLOAD SPLITTING: PASS — artifact-reference transport is preferred and splitting
                                    is never introduced as a mechanism
```

**MESSAGE BUDGET: STRUCTURAL_ONLY — and correct.** `message` has no observed bound; the one
enforced bound is on a field no LEGEND address approaches. Publishing a numeric body budget would
have been a naked number wearing a rationale. The structural rule is the stronger one, and the
refusal is honest rather than an unprobed gap dressed as discipline: the record states *why* it was
not probed — discovering it requires abusing the runtime, and the result would be a property of one
attempt rather than a contract.

**Depth preserved.** I ran the falsifier: every occurrence of *shorter / shrink / reduce / concise /
minimization* in the protocol is either the depth rule itself, the envelope description, or the
explicit disclaimer *"the purpose is not token minimization."* No clause reduces, or can be cited to
reduce, reading depth, evidence coverage, methods review, locator coverage or uncertainty analysis.
**SCIENTIFIC DEPTH: PRESERVED.**

---

## 9 · Acceptance tests — recorded individually

| # | EXECUTED | STATUS | REASON (exact) |
|---|---|---|---|
| `T-TRANSPORT-1` | NO | **NOT_RUN** | requires §8 term 3 — exactly one current target. Eight live Mirror sessions, no governed routing state. Running it would require the ungoverned election the protocol refuses. **Reason verified and endorsed.** |
| `T-TRANSPORT-2` | **YES — by me, at 2.1.233** | **PASS** | `InputValidationError`, `path:["to"]`, pattern `^[^\n\r]{0,200}$`, pre-send, tool never ran. Expected outcome **and expected class** both matched |
| `T-TRANSPORT-3` | **YES — by me, at 2.1.233** | **PASS** | 264 chars accepted, no warning, result byte-identical to the in-bounds control. Sender observability NONE |
| `T-TRANSPORT-4` | NO | PASS by construction | worked example: the SCIAB handoff, 143 KB manifest transported as hash+base+tips+branch. **I reproduced that binding independently today** (`beef6db0…`), so this has real evidence and is, if anything, understated |
| `T-TRANSPORT-5` | **YES — by me, at 2.1.233** | **PASS** | `TARGET_UNRESOLVED` returned as a structured `success:false` result object; §8 makes delivery term 4 of six |
| `T-TRANSPORT-6` | NO | PASS by construction | §1.3's deletion test. **I ran the summary half hostilely** (§7A) and it holds; the `message` half holds *if the discipline is followed*, and the residual is named in `FAILURE_MODE_STILL_POSSIBLE` |
| `T-TRANSPORT-7` | NO | PASS by construction | §8 term 6 — definitional. A definition having a property is not a test, but the mode is disclosed in the cell |
| `T-DEPTH-1` | **YES — by grep, by me** | **PASS** | no clause mentions any depth dimension except to forbid its reduction. Verified exhaustively |

**On "PASS by construction", which the handoff asks me to attack (§2.7).** Four of eight is a lot,
and a test that cannot fail is not a test. But the label is **disclosed at every site** — in the
table cell, in the manifest, and in the SLR's own IMPACT ("three PASS on observation, four by
construction, one NOT RUN"). Nothing is smuggled. My substantive objection is narrower and
non-blocking: `T-TRANSPORT-6` and `-7` would be more honestly typed `PASS_BY_DESIGN — NOT
EXECUTED`, because their content is that the design has a property, and calling that a passing test
invites a later reader to count eight tests and think seven ran. Recorded, not blocking.

```
WRONG-REASON LOAD-BEARING PASSES: 0
```

Every executed load-bearing test was checked against **expected outcome AND expected reason/class**,
not merely a non-zero return. `T-TRANSPORT-2` matched the exact validation code, field path and
pattern. The one wrong-reason event this session belonged to **my own harness**, twice, and both are
recorded rather than hidden: the void negative control (§1) and a `timeout`-wrapped regression run
that exited 0 having executed nothing because `timeout` does not exist on this platform. I caught
the second only because I read the output instead of the exit code — which is the failure class this
repository has now paid for repeatedly.

---

## 10 · Generality — PASS on substance, and the source of blocking finding M-1

**Reproduced the grep the handoff asks for (§5.2), at the content tip:**

```
scientist-a   2 occurrences  (lines 281, 366)
scientist-b   1 occurrence   (line 366)
scientist-c · BENCH-AB-001 · lettore · orchestrator   0
role names plan/mirror       lines 30, 346, 365, 367, 389
TOTAL         8 lines: 5, 30, 281, 346, 365, 366, 367, 389
```

**Classification, independently checked line by line:**

| line | occurrence | class |
|---|---|---|
| 5 | *"binding once Mirror hostile review passes"* | **FRAMEWORK RULE** — the standard PROPOSED-status formula |
| 30 | *"`roles/plan.md` already says…"* | **CITATION** — prior art |
| 281 | `scientist-a` resolving under `--all` to a dead job | **MEASUREMENT** |
| 346 | *"visible to Plan at reconciliation and to Mirror on the ledger"* | **CITATION** of an existing constitutional duty (body §43, G.3) |
| 365–367 | `plan` 8 · `mirror` 7 · `scientist-a`/`scientist-b` 0 | **MEASUREMENT** |
| 389 | *"preconditions Plan may not satisfy alone"* | **CITATION** — a statement about authority |

**No STRUCTURAL SPECIAL CASE among them.** I applied the falsifier that tests the property actually
at stake — delete every actor name and ask whether any normative sentence changes meaning — and
**none does**. §1.1's authoritative-content list, §1.4's depth rule, §3's version binding, §4's
per-field table, §5's taxonomy, §8's six-term conjunction and §9's five refusals are all stated over
*any actor*.

```
A/B-SPECIFIC TRANSPORT LOGIC: NONE
```

**§9.1b is exemplary and I want it on the record as such.** Plan ran the falsifier its own handoff
asked me to run, it falsified Plan's first wording, and Plan recorded the correction *as a
correction* — naming the false sentence rather than absorbing the result silently. That is the
behaviour the review protocol is trying to buy.

🔴 **And it is incomplete in the one place that matters — see M-1 (§12).**

**Scientist D falsifier — PASS.** For **transport specifically**, a hypothetical `scientist-d` uses
identical clauses: same control envelope, same durable-artifact rule, same outcome taxonomy, same
ACK relationship, same version/runtime-scope semantics. No clause enumerates actors, so none needs
extending. The delta is `ACTOR_ID` + role binding + a worktree row + a fingerprint that is *derived*
(`compose --role scientist`, keyed by role not actor — verified: all four fingerprints are
role-keyed). Plan's qualification — steps 7–9 are generic by design and not yet by implementation —
is honest, and I note those three steps are **routing** steps, not transport steps. Transport
generality is fully testable today and passes. **SCIENTIST-D TRANSPORT FALSIFIER: PASS.**

No Scientist D was created, activated or registered.

---

## 11 · Regression accounting — DELTA 0, set-wise

Run in two clean detached worktrees, `BASE_HEAD` and the candidate **content tip**, never in root.

```
                          BASE_HEAD 4454feab      CANDIDATE f48a807
suites RUN                65                      65
tests executed            953                     953
failing suites            6                       6

SET DIFFERENCE            EMPTY  →  DELTA 0
FAILING TEST NAMES        7 at each tree, IDENTICAL name for name  →  same reason, not only same count
```

```
BASE FAILING SET == CANDIDATE FAILING SET:
  framework/scripts/test_session_self_eval.py
  scripts/test_abstract_corpus_is_not_evidence.py
  scripts/test_fulltext_trace_contract.py
  scripts/test_locator_obligation_reaches_every_route.py
  scripts/test_release_runner_verdict.py
  scripts/test_release_surface.py
```

Compared as **sets**, not counts, and then one level deeper — the individual failing test names
match exactly, so no candidate-added red is hidden by a removed red at equal count. Root
environmental state cannot contaminate the comparison: both runs were in detached worktrees under
the session scratchpad, and root was never written or cleaned.

**Other gates, re-run at the candidate tree — all reproduce Plan's published values exactly:**

```
LINT                 PASS — 1 pre-existing INFO (CLAIM 010 wikilink)          ✅ matches
PUBLICATION GATE     PASS / BLOCKS: 0 — 4 [REVIEW] lines, all pre-existing     ✅ matches
GROWTH ANCHORS       PASS — claims 39 · papers 70 · corpus 356 · literature 390 ✅ matches
RECEIPT LEDGER       OK — 128 chained, tail anchored                           ✅ matches
FINGERPRINTS         mirror 3dff8954… · plan 9c0c13fb… · scientist 82423a48… ·
                     orchestrator e2c54470… — IDENTICAL at BASE_HEAD and candidate ✅ matches
```

The fingerprint identity confirms the candidate's structural claim: **no role contract is touched,
so no fingerprint moves and no in-flight checkpoint is invalidated.**

**REGRESSION DELTA: 0.**

---

## 12 · Findings

### 🔴 M-1 · BLOCKING — the normative protocol asserts, in content, something its own content falsifies

```
WHERE      framework/protocols/cross_session_transport.md @ f48a807f  — CONTENT, hashed,
           canonicalizes on approval
           line 16–17  actor_scope: ACTOR-GENERIC. "Nothing in this protocol names an actor,
                       a role, a worktree or a benchmark."
           line 424    §11 — "does not name any actor, role, worktree, or benchmark;"
FALSIFIED  by the same file: `scientist-a` ×2 (281, 366), `scientist-b` ×1 (366), role names
           at 30, 346, 365, 367, 389. Eight lines. Measured by me, and by Plan.
```

**Plan found this and fixed the wrong copy.** Manifest §9.1b concedes *"That is false"* and
enumerates the eight occurrences — but the manifest is `governance/candidates/`, a declared
control-plane root. **It moves no hash and it does not travel with the protocol.** §9.1b's
enumeration lists the eight lines that *contain* names; it never names lines 16 and 424, which are
the two *assertions* those names falsify. So the concession exists in a document that will not be
read beside the protocol, and the false sentence canonicalizes.

**Why this is load-bearing and not pedantry.** The candidate's own §7 is an indictment of exactly
this pattern: five artifacts, one canonical, carrying a stated ground that is false, quoted forward
until — in `SLR-plan-0007` L-1's words — *"by the third quotation the instrument is gone."* Plan
declines to repair those five on the correct ground that editing canonical text is a governed change
belonging to the candidate that needs the capability. **That ground does not reach this case.** This
is the candidate's own new, unmerged, not-yet-canonical artifact. No authority obstacle exists; no
other candidate owns it; the author is the only party who could fix it and is entitled to. The sole
cost is a new content tip and a re-derived hash — which is what a revision is *for*.

Approving as-is would plant a **sixth** artifact carrying a false self-description into canon, in
the same session whose central learning is the cost of doing precisely that. The repository already
holds the better precedent: `actor_identity_feasibility.md` *"over-claimed in nine places; every
correction is applied below and the over-claim is named rather than quietly removed."*

**The substantive property is TRUE — I verified it independently (§10) — which is what makes the
remedy cheap and non-weakening.** Replace the absolute with the corrected claim Plan has *already
written* in §9.1b:

```
SUGGESTED (frontmatter + §11), the author's own wording:
  No rule, no branch and no obligation in this protocol is conditioned on any actor, role,
  worktree or benchmark. Actor names appear only in citations and measurements.
```

That is strictly stronger than the current sentence: it is true, it is checkable by the same grep,
and it survives the falsifier. **REQUEST CHANGES on this finding alone.**

### M-2 · NON-BLOCKING, carried to BASE_HEAD's owner — P5's `runtime/` rationale is false today

```
CANONICAL P5.1 @ main:  "While `runtime/` remains untracked it is invisible to `git ls-tree` and
                         therefore absent from the domain, so no fixed point arises in the interim."
MEASURED:                runtime/orchestrator_lease.md IS TRACKED at main, and IS among the 531
                         INCLUDED entries of this candidate's content domain.
CORROBORATED:            deployment/deployment_profile.md:92 — "runtime/orchestrator_lease.md,
                         tracked." Canonical state says so explicitly, one file away.
```

**Consequence:** a runtime-state artifact sits inside the identity of every candidate. An
Orchestrator lease write on a candidate branch would move that candidate's content hash — the exact
fixed-point class P5.1 exists to prevent and believes, on a false premise, it has avoided here.

**Not this candidate's defect.** XPORT neither introduces nor relies on it; its hash is correct under
the rule as executed, and the script's behaviour is consistent with the declared roots. Recorded
because it is a **fifth** artifact of the same shape as the four in manifest §7 — a true conclusion
resting on a premise that has quietly stopped being true — and because it belongs to whichever
candidate next opens P5. **Carried. Not repaired here; P5 is not Mirror's to edit.**

### M-3 · OBSERVATION — "third binary" is confirmed, "third version" is not

Recorded in §3. The design record and the manifest are both accurate; the looser paraphrase is the
one that fails, and it should not travel into Candidate B.

### Non-blocking observations

- **O-1** `T-TRANSPORT-6` / `-7` would be more honestly typed `PASS_BY_DESIGN — NOT EXECUTED` (§9).
- **O-2** `KERNEL_SPEC` is cited by a normative protocol without a version or commit pin (§8).
- **O-3** The `to` boundary between 201 and 212 characters was not probed by either party. The
  declared bound plus one rejection above it is honest evidence, and the protocol claims nothing
  more — but "213 rejects" is a bracket, not a boundary, and should not harden into one.

---

## 13 · Carried debts — verified enough to classify, none repaired

```
A · ORCHESTRATOR WORKTREE CONFLICT   CARRIED_ROUTING_DEBT
    roles/orchestrator.md:5 "the repository root checkout" vs deployment_profile.md:31
    "`orchestrator` — its own worktree". Both canonical in main. CONFIRMED at source.
    Routing-relevant because `--cwd` is the only mechanized scoping predicate the harness offers,
    and the two readings return 3 sessions and 0 sessions — ambiguous under one, absent under the
    other. Transport does NOT silently repair it and introduces no worktree guarantee that
    depends on it. No scope contamination found.

B · ROOT ENVIRONMENT                 CARRIED_ENVIRONMENTAL
    Mechanism confirmed: the two suites enumerate ROOT.rglob("*.md") — the filesystem, not
    git ls-files — so any untracked markdown contaminates them. Both green in clean worktrees.
    The candidate's wording is correctly narrow: a historically measured mechanism whose current
    instance is not reproducible. It does NOT claim the class is fixed, and explicitly flags the
    residual as a real latent debt. Root was not cleaned, read destructively, or mutated by me.

C · SNAPSHOT TAGS                    CARRIED_HISTORICAL_DEBT
    Verified: exactly 4 missing (HASHDET, ORCHWT, P51C9, SUNSET-DEC3), 2 present.
    Four instances, not one — Plan's enlargement of its own reported debt is correct.
    NOT load-bearing for XPORT, NOT recreated, NOT falsely claimed resolved.

D · SCIAB CARRIED FINDINGS           unchanged; P-12 and the manifest half of P-13 remain OWED
E · HUMAN_APPROVAL_QUEUE / lease copy divergence across branches — carried, not reconciled
```

---

## 14 · Plan author response and SLR curation

### 14.1 · `AUTHOR-RESPONSE-SCIAB-MIRROR-006` — PASS

```
✅ GOVERNANCE-PERMITTED   Annex C.2 makes AUTHOR_RESPONSE mandatory and silence non-acceptance;
                          APR-20260819-SCIAB-001 names the debt. Plan may not write to
                          reviews/mirror/ (worktree confinement) and writes to reviews/plan/.
✅ CONTROL PLANE          correct — reviews/ is a declared root; it moves no hash. Verified.
✅ SCIAB NOT REOPENED     no revision 7; the canonical specification is untouched; verified by
                          diff — no BENCH-AB-001 surface, protocol or script is modified
✅ P-12 / P-13 TRUTHFUL   all six AST counts reproduce exactly on my own run:
                          benchmark_input_surface.py  51 statements · 32 definitions · 33 nested
                          test_…py                    40 statements · 15 definitions · 126 nested
✅ E.2 REMAINS MIRROR'S   all three re-classifications accepted as issued, none contested; Plan's
                          additions are marked `proposed` and explicitly not self-ratified
✅ HISTORY NOT REWRITTEN  SLR-plan-0006.md is NOT edited — verified by diff. The correction is an
                          appended record, SLR-plan-0006-COR-001.md
✅ SCOPE CREEP FLAGGED    §0.4 raises the correction record as possible scope creep itself and
                          states the refused alternative. Judged: the choice is right — appending
                          a correction beside a false sentence in Plan's own learning record is
                          the narrowest available repair, and it uses a convention already in use
```

This work happened in the same Plan session and is **not** XPORT content. It is correctly classified
as control plane and does not enter the hash.

### 14.2 · `SLR-plan-0007` — BOUND, and curated under Annex E.2

Bound: it is in the content domain (`learning/` is CONTENT by intent), it is present at the content
tip `f48a807`, and therefore **inside** the hashed tree. **No post-hash SLR exists** — verified: the
only `learning/` paths on this branch are `SLR-plan-0007.md` and `SLR-plan-0006-COR-001.md`, both in
the content commit. Correct significant session; included before binding.

**Curation — Mirror's, per E.2. Plan is not auto-ratified.**

| entry | Plan proposed | Mirror curates | reason |
|---|---|---|---|
| **L-1** *an impossibility measured through one instrument is a fact about the instrument* | ORIGINAL_OBSERVATION, offered for wider scope | **ACCEPTED as ORIGINAL_OBSERVATION**, wider scope **granted**, plus **one independent confirmation (mirror, this session)** | I reproduced both halves at 2.1.233 — ListAgents excludes self, the CLI includes it — and verified the load-bearing premise myself: the second instrument was already in the repository, called at four sites of `legend_launch.sh`. Not superseded tooling; an unasked question. The detector is correctly formulated and I could not find a prior instance of it in the repository |
| **L-2** *a version change can enable a capability, and nothing watches that direction* | ORIGINAL_OBSERVATION | **ACCEPTED as ORIGINAL_OBSERVATION** — and in my judgement the strongest entry in the record | The asymmetry is real and structural: a PASS decaying to FAIL gets a trigger because it hurts someone; a FAIL decaying to PASS gets none. Verified the supporting fact: `actor_identity_feasibility.md` carries no `VERSION_OBSERVED` on any verdict. The proposed consequence — DEFERRED/NOT_FEASIBLE verdicts carry the same version fields as guarantees — is cheap and correct |
| **L-3** hypothetical failure conditions may already be the live state | REPLICATION of SLR-plan-0004 L-1, scope widened | **ACCEPTED as issued** | Correct dedup. The widening (findings-in-code → normative-claims-in-prose → hypothetical failure conditions) is genuine, and the measurement supporting it is one command |
| **L-4** the anti-ontology check has a second output — which surfaces are frozen | REPLICATION of SLR-plan-0005 L-3, new form | **ACCEPTED as issued** | Verified all four surfaces and all three holds at source. The second output really did convert a design task into an escalation |

**Mirror's own methodology is not self-ratified (G.2).** Nothing in this curation changes Mirror's
review rubric, clustering, active-lesson selection, review-yield methodology or autonomy
classification.

---

## 15 · Annex C.2 — the single format

**REVIEW_ID** `REV-XPORT-MIRROR-001` · **OBJECT** `CAND-20260819-XPORT` rev 1,
`CANDIDATE_CONTENT_HASH 68173f01…c96a` @ `BASE_HEAD 4454feab` · **LEVEL** R4 ·
**REVIEWER** `mirror` · **AUTHOR** `plan` · **ADJUDICATOR** operator (MAJOR)

### STEELMAN — mandatory, and before the objections

**This is the strongest candidate I have reviewed, and its central act is a refusal.** Asked to
produce a routing candidate, Plan produced a measurement, a partition and a reasoned refusal to
build on four held decisions — and then invited me to attack the refusal itself. That is the
opposite of the failure mode governance exists to catch.

Four things deserve to be said plainly:

1. **The probe was taken once, deliberately, so two candidates could not drift.** That is a design
   decision made against the author's own short-term convenience, and it is correct.
2. **The version model is right in a way that was not obvious.** "The installed version" turned out
   not to be a scalar, and the candidate rebuilt every runtime guarantee around a per-session
   observation rather than patching the number. Its rule then fired on the first session to read it
   — mine — and sent me to re-measure. A protocol whose discipline catches its own reviewer on
   contact is doing the thing it claims.
3. **`T-TRANSPORT-1` is `NOT RUN` and that is the honest result.** It would have been trivially easy
   to send a message to one of eight Mirror sessions, get `success: true`, and write `PASS`. Plan
   refused, and the refusal is the same refusal the protocol asks of everyone else. The handoff
   package being a *file* rather than a *message* is that rule executing on its own first use.
4. **§9.1b runs the falsifier the handoff asked me to run, finds the author's own claim false, and
   records it as a correction.** An author who publishes the grep that convicts them has made the
   review cheaper and the repository more honest.

The blocking finding below is not an argument against any of this. It is that the correction in
§9.1b stopped one file short.

### EVIDENCE_FOR
Binding reproduced at three tips with positive and negative controls · regression delta 0 set-wise
and name-wise · all five gates reproduce · fingerprints identical at both trees · every load-bearing
harness claim re-observed at a second runtime version · both size probes reproduced at 2.1.233 with
the exact expected failure class · the four routing holds quoted at source · the generality property
verified by an independent falsifier.

### EVIDENCE_AGAINST
The normative artifact carries two false self-describing sentences (M-1), conceded only in the
control plane. Four of eight acceptance tests pass by construction. `T-TRANSPORT-1` — the only
end-to-end test — is unrun, necessarily.

### ALTERNATIVES_CONSIDERED
**(a) ACCEPT and carry M-1 as a debt.** Rejected: the fix requires a content change, so "carry" means
canonicalizing a false sentence and hoping someone re-opens it. The candidate's own §7 documents
what happens next — it gets quoted forward. **(b) Treat M-1 as non-blocking because it sits in
frontmatter and a summary bullet, not an operative clause.** Rejected: the frontmatter field is
`actor_scope`, which is precisely a claim about the protocol's binding scope, and §11 is the
protocol's own summary of what it does not do. Both are read by exactly the reader who will not have
the manifest. **(c) REQUEST CHANGES on the partition or the deferral.** Rejected on the evidence —
both hold.

### KEY_OBJECTIONS
`M-1` (blocking) · `M-2` (carried, BASE_HEAD's) · `M-3`, `O-1`, `O-2`, `O-3` (non-blocking).

### VERDICT
**REQUEST CHANGES** — on `M-1` alone. `CONFIRMED` on every other axis, in the Annex C.2 sense: *no
defect found given the available evidence bundle*, never *true*.

### REVIEWER_CONFIDENCE
**High** on binding, regressions, gates, the size model and the partition — all re-executed rather
than read. **High** on M-1: the sentences are quoted verbatim from the content tip and the falsifying
occurrences are in the same file. **Medium** on the recipient-side taxonomy, which rests on
`MEASURED_EARLIER` evidence I did not re-measure and could not without contacting a peer.

### RESIDUAL_UNCERTAINTY
`message` has no known bound at any version. Recipient-side completeness has never been observed by
anyone. `T-TRANSPORT-1` remains unrun and will stay unrun until Routing exists. Whether a narrow
routing scoping exists inside Plan's authority — I looked and did not find one, which is weaker than
proving there is none.

### EVIDENCE_NEEDED
An end-to-end `T-TRANSPORT-1` once a resolver exists · a recipient-side completeness observation for
`summary` · the `to` boundary between 201 and 212 if it ever matters.

### WHAT_WOULD_CHANGE_MY_MIND — declared falsifier
**M-1 dissolves if any one of these is shown:**
1. The protocol at the content tip does **not** contain the sentences at lines 16–17 and 424 — i.e.
   my reading of `git show f48a807f:framework/protocols/cross_session_transport.md` is wrong; **or**
2. those sentences are true under a reading of "names" that the file itself establishes — e.g. a
   defined term making "names" mean "conditions logic on", which I searched for and did not find;
   **or**
3. a governance rule forbids Plan from amending its own unmerged, not-yet-canonical artifact before
   review completes, making the correction genuinely unavailable to its author rather than merely
   costly. If that rule exists and I have missed it, M-1 becomes a carried debt and my verdict
   becomes ACCEPT.

**The whole review would be overturned if** the candidate content hash did not reproduce at the
declared base and tip — it did, five ways including two controls.

### AUTHOR_RESPONSE
**OWED — Plan.** Mandatory under Annex C.2; silence is not acceptance.

---

## 16 · Status statements required of this review

```
ROUTING / SESSION LIFECYCLE IS NOT SOLVED BY XPORT.
```

`SESSION_REF OBSERVABLE` is **not** `ACTOR_ID → UNIQUE CURRENT_SESSION_REF SOLVED`. The observed
state contains zero-session actors (`scientist-a`, `scientist-b`) and multi-session actors (`plan` 8,
`mirror` 8). That evidence supports future Routing work; it authorizes no routing policy, and this
review creates none.

```
HISTORICAL SESSION CLEANUP: NOT_PERFORMED
```

No session was closed, killed, renamed, superseded, activated or cleaned. The multiplicity, age,
runtime-version distribution and registry mismatch of the live Plan and Mirror sessions are
preserved intact as the natural dataset for Candidate B. This review only snapshotted them,
read-only.

```
SCOPE CREEP: NONE
```

Classified diff inspected. No activation authority, no CURRENT assignment, no registrar, no
supersession, no routing generation, no lease redesign, no Scientist activation, no BENCH-AB-001
execution. Routing observations exist in the design record as evidence and in manifest §8–§10 as
control plane; **none becomes operative policy under XPORT.**

```
HUMAN_APPROVAL   NONE — not granted, not requested, not implied by this review
MAIN             4454feab72b7a0edf65f191be62aeedd899a15ad — UNCHANGED
BENCH-AB-001     NOT STARTED
SCIENTIST A      NOT ACTIVATED
SCIENTIST B      NOT ACTIVATED
```
