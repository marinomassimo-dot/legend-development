---
record_type: OPERATOR_DECISION
id: DEC-20260903-STOP-POLICY-AND-DECISION-AUTHORITY
title: Stop policy, decision authority, and branch-switch authority for unattended execution
date: 2026-09-03
authority: >
  Operatore — Annex H.1 rows "Spese / MAJOR approval / governance" and "Strategia
  complessiva" (governance/annex_h_authority_matrix.md:35-36). Three of the six RESERVED
  items trace to those two rows; the other three trace to no H.1 row at all. See MAPPING.
status: RATIFIED_ON_MERGE
status_note: >
  This record and the two texts it anchors are OPERATOR-AUTHORED and IN FORCE ON
  plan-modular-evolution-p0a-exec ONLY, under H.1's "WORK_COMMIT — ogni attore, solo
  proprio branch". They become canonical governance — binding on every actor, citable
  from `main` — only at the operator's own merge of this branch. The merge is the
  ratification act. No HUMAN_APPROVAL_QUEUE entry is created: the operator dictated the
  text and performs the merge, so approval and authorship are the same act by the same
  authority.
change_class: MAJOR
change_class_rationale: >
  governance/GOVERNANCE_v3.1.1.md:250 defines MAJOR strictly as "SOLO
  governance/authority/gate/epistemic policy". §21c and §21d are exactly that: they state
  when an actor may act without the operator, and who decides what. WORK_COMMIT on an
  actor's own branch needs no prior GATE 3 (H.1); ratification at merge is what supplies
  the human approval a MAJOR change requires before it is canonical.
supersedes: none
applies_to:
  - framework/instruction/LEGEND_CORE.md (§21c, §21d)
  - scripts/test_stop_policy.py
task_id: STOP_POLICY_AND_DECISION_AUTHORITY_RATIFICATION_v1
mode: OPERATOR_DICTATED_TEXT → BRANCH_MATERIALIZATION → RATIFIED_ON_OPERATOR_MERGE
---

# STOP POLICY, DECISION AUTHORITY, AND BRANCH-SWITCH AUTHORITY — 2026-09-03

## DECISION_ID

`DEC-20260903-STOP-POLICY-AND-DECISION-AUTHORITY`

## QUESTIONS_DECIDED

Three decisions, dictated verbatim by the operator across three turns of one session
(PASSO 5, the `INTEGRAZIONE AL PASSO 5` attachment, PASSO 6), then amended by two further
operator-ratified sentences after Mirror's whole-branch review of the same branch.

- **Q1 — STOP POLICY.** When does an actor stop, and when does it take a recorded default
  and continue? Decided: §21c.
- **Q2 — DECISION AUTHORITY.** Which decisions does the Orchestrator take without asking,
  and which stay with the operator? Decided: §21d.
- **Q3 — BRANCH-SWITCH AUTHORITY.** May an agent move `HEAD` in a git checkout? Decided
  inside §21d's "Operator decisions already taken" list: **yes inside a single-owner
  worktree, no in the shared root checkout.** Root stays reserved because more than one
  session shares it, which is the guard's own stated rationale for confinement —
  concurrency, not authority: *"other actors share this repository's object store … and
  untracked files are exactly where their in-flight work lives"*
  (`framework/scripts/guard_policy.py`, `DENY_REF` text).

## RATIFIED_TEXT

Both blocks are carried verbatim on `framework/instruction/LEGEND_CORE.md` (§21c, §21d)
and asserted byte-for-byte by `scripts/test_stop_policy.py`, which fails on any paraphrase,
added word or dropped line.

| Block | Lines | sha256 |
|---|---|---|
| STOP POLICY — §21c body, ending before the SAFE_DEFAULTS list | 35 | `eb6fb4f70d8a61363bb5ad73b290a8b808166729e29ca7eb9af78eaa7ff80558` |
| DECISION AUTHORITY — §21d body | 42 | `99413aa71e82bd3bbbc063db951dbfb45cc84a488aae0a76f3ea87d9ea9cc909` |

**The SAFE_DEFAULTS list is deliberately outside the hash.** §21c authorises agents to
append a hindsight default. With the list inside the hashed block, one permitted append
moved the hash, broke the verbatim constant, and forced the agent to edit the very test
whose failure message forbids editing it — five declarations disturbed by one authorised
act. The body is hashed and compared for equality; the list is append-only and asserted
entry by entry; and `scripts/test_stop_policy.py` carries the case proving an append leaves
the body byte-identical.

Each hash covers the text from its opening line (`STOP POLICY (HARD RULE, …)` /
`DECISION AUTHORITY (HARD RULE, …)`) to the last character of its closing line, with no
trailing newline — the exact block `test_stop_policy.py` holds as a constant. Re-derive
from the repository root:

```
python3 -c "
import hashlib, sys, pathlib
sys.path.insert(0, 'scripts')
from test_stop_policy import STOP_POLICY_BODY, DECISION_AUTHORITY
text = pathlib.Path('framework/instruction/LEGEND_CORE.md').read_text(encoding='utf-8')
for name, block in (('STOP_POLICY_BODY', STOP_POLICY_BODY),
                    ('DECISION_AUTHORITY', DECISION_AUTHORITY)):
    assert block in text, name + ' is not carried verbatim'
    print(name, hashlib.sha256(block.encode()).hexdigest())
"
```

This record deliberately does **not** reproduce either block inline. A third copy would
have to be kept in sync with `LEGEND_CORE.md` and the test constant, and the failure mode
of three copies is that two agree while the third is the one being read. The hash is the
anchor; the two live copies are the content.

## MAPPING — the RESERVED list against Annex H.1

Mapped, not asserted. **Three** of the six items trace to a literal H.1 row, and to only
**two distinct rows**, because "Spese / MAJOR approval / governance" carries two of them.
The other three trace to no H.1 row, and this record says so rather than manufacturing a
correspondence. An earlier draft of this section read "two of six items", conflating the
count of rows with the count of items; the table below is the authority, and it is 3 / 3.

| §21d RESERVED item | H.1 row | Source, where it is not H.1 |
|---|---|---|
| external spend above the declared default | **"Spese / MAJOR approval / governance" → Operatore** | — |
| a change to a fundamental guarantee (this list, §21d, STOP POLICY body) | **"Spese / MAJOR approval / governance" → Operatore** — a governance change | — |
| publication to origin or any public surface | **"Strategia complessiva" → Operatore** | also touches the governance row |
| history rewrite | *no H.1 row* | the guard refuses `REF_WRITE` to every runtime, role and lease — but it is registered as a `PreToolUse` hook on the `Bash` matcher alone, so that is a control on one channel, not a property of the repository. The reservation here is a real one, not a restatement of something no actor could do |
| irreversible deletion of unique material | *no H.1 row* | `LEGEND_CORE.md` §2 ABSOLUTE PRINCIPLE — "No information may be lost … If preservation is not guaranteed → COMMIT BLOCKED" |
| exposure of private or patient data outside the declared perimeter | *no H.1 row* | `CLAUDE.md` §0's three binding facts (public edition, no individual-level record) and the G7 privacy guarantee inventoried in PLAN-MODULAR-EVOLUTION-001 §M4 |

**The sentence added to §21d, and the limit of what this table can show.** H.1 carries
**17** rows: 2 to the Operatore, 15 elsewhere. This table audits the **reservation** — what
§21d withholds. Mirror's F5 finding was about the **grant**: §21d's opening clause says the
Orchestrator decides *every question not on the RESERVED list*, and the residual set of a
withholding list is not established by enumerating the list. **This table therefore does not
verify the added sentence, and this record does not claim it does.**

Two open problems are recorded here rather than resolved, because §21d's body is reserved:

1. **The sentence may be vacuous.** If §21d reassigns only decisions H.1 gives the
   Operatore, and all three items deriving from those two rows sit inside RESERVED, then the
   reassigned set is empty and §21d transfers nothing. Read without the sentence, the opening
   clause still sweeps up rows H.1 assigns elsewhere. One of the two readings is wrong and the
   text does not say which.
2. **Three H.1 rows are not ordinary assignments,** and a residual grant reaches them most
   sharply. Two are prohibitions: `Modifica rubrica/metodi di Mirror | mai Mirror da solo
   (G.2)` and `Promozione BOOTSTRAP_CONTROLLER → Orchestrator | protocollo Annex I (mai
   autoassunzione)` — the second would let the Orchestrator decide its own promotion, which
   that row forbids by name. The third was missed by the first version of this list and
   found by Mirror: `Lifecycle learning: epistemico Mirror, durevolezza Plan | —`, whose
   Authority cell is `—`. It assigns to no actor, so a clause scoped to "questions H.1 does
   not assign to another actor" sweeps it up whole, taking Mirror's epistemic lifecycle and
   Plan's durability. None of the three appears in RESERVED.
3. **The scoping repair makes the section's own next sentence false.** With the clause
   narrowed to questions H.1 assigns to no other actor, and the Operator being another
   actor, the grant no longer reaches H.1's two Operatore rows — so *"§21d reassigns to the
   Orchestrator only the decisions H.1 assigns to the Operator"* now reassigns nothing. The
   clause is non-vacuous as a grant and self-contradictory as a description of itself.

All three are operator decisions on reserved text, and they are why D-1 below is recorded as
PARTIALLY CLOSED rather than closed.

## SAFE_DEFAULTS — who may extend it

§21c authorises agents to append a hindsight default to SAFE_DEFAULTS; §21d reserves
changes to "a fundamental guarantee — including … the STOP POLICY". As first written the
two clauses contradicted each other, and the contradiction was live: the first agent to
append a default would have performed an act the second clause reserved, and would then
have had to edit the verbatim test constant to keep the suite green — the exact
"rule and its test drift together" failure that suite exists to prevent (Mirror, F6).

Resolved by the operator: **SAFE_DEFAULTS is extensible by agents; the STOP POLICY body
and all of §21d are reserved.** The carve-out is stated inside the RESERVED bullet itself,
so the exemption lives where the reservation does rather than only in the looser section.

## F2 — `development` credential-gating, verified

§21d permits an agent to push its own branch to `development` *provided `development` is
credential-gated*, and requires the Orchestrator to verify and record that. The proviso
was unverified when §21d was written (Mirror, F2). Verified now, without pushing:

- **Read is public and anonymous.** `GIT_TERMINAL_PROMPT=0 git ls-remote development HEAD`
  returned `b1b5a581b9b1af85dd4de8a05212433e0aab21a2` with no prompt and no credential.
  The GitHub API returned HTTP 200 with `"private": false`, `"visibility": "public"`.
- **Write is not.** GitHub offers no anonymous-push path for any repository, public or
  private: a push requires an authenticated identity holding collaborator write access.
  This is a platform property, **not** a per-repository policy this session audited — no
  attempt was made to enumerate which identities hold write access, and no push was made.

**Outcome: the measurement does not satisfy the proviso — it invalidates the permission.**
An earlier draft of this section recorded the opposite, and it was wrong. Three facts, all
established above or in the tree:

1. `development` **is a public surface** — that is what `visibility: public` and the
   anonymous read establish. §21d's own RESERVED bullet 1 reserves *"publication to origin
   or any public surface"* to the operator, so the permission and the reservation collide
   inside the same section, on a fact this very verification produced.
2. `framework/scripts/guard_policy.py`, `DENY_NETWORK`, says it outright: *"🔴
   `development` and `origin` are BOTH public GitHub repositories. Pushing a branch to
   either one PUBLISHES it… Publication is an operator act and needs PUBLISH authority,
   which is never granted by a runtime. Commit locally; the operator pushes."* This record
   cited the file ten lines above that paragraph and did not report it.
3. "Credential-gated" cannot discriminate anyway. It is true of every GitHub repository,
   `origin` included — which §21d reserves — so the proviso does no work as a test.

### The operator's decision, 2026-09-03

Presented with the three facts above, the operator did not strike the permission and did
not keep it as written. The proviso is replaced by a discriminator that is a property of
the **push**, not of the remote, and the guard is changed to enforce it in the same branch:

```text
remote is `development`, named explicitly     no force, in any spelling, and no `+` refspec
exactly one ref                               public_release_gate PASS, 0 blocks, at the exact SHA
recorded: branch · SHA · gate result · actor  ref != main, OR main when the merge was the agents' to make
`origin` is denied to every runtime, always
```

**The operator records knowing what this permits.** `development` is a public GitHub
repository: an authorised push publishes, immediately and irreversibly, and no later act
retracts it. That is accepted deliberately, not overlooked — it is why the ref, the
fast-forward property, the gate result and the actor are all pinned before the push rather
than reported after it.

**The gate is a precondition, not a guarantee, and the operator records knowing that too.**
`public_release_gate` PASS means one detector found nothing on one population. On the same
tree, `independent_privacy_scan` reports **17 BLOCKs against the gate's 1** — a disagreement
that no executable object adjudicates (PLAN-MODULAR-EVOLUTION-001 §M4). **Adjudicating that
1-vs-17 is a priority item for 0B**, and until it is adjudicated the push rule rests on the
weaker of the two instruments, knowingly.

**Implementation status: SPECIFIED, NOT ENFORCED.** `framework/scripts/push_authorization.py`
carries the conditions and reads `ledger/push_authorizations.jsonl`. It was wired into
`guard_policy.analyse_git` and the wiring was **reverted before merge**. Two review rounds
found ten ways to reach a real push past it, and the diagnosis was not ten bugs but one:
a permission that decides by matching tokens against hand-written lists, in a command
language with more spellings than the lists have entries. Long options abbreviate, so
`--del` and `--prun` and `--force-w` walk past a list containing `--delete`, `--prune`,
`--force`. The relocating globals have environment twins, so `GIT_DIR=` walks past a list
containing `--git-dir`. The payload's `workdir` field relocates the command without being a
token at all. `--exec-path=` names the program git runs and appears in the guard only in
skip lists. And `git commit … && git push` moves the branch after the hook has already
resolved it, so the gate result is bound to a tree that is no longer the one leaving.

The last two need the **decision layer**, where `cwd` and the shape of the whole line are
known — not the per-subcommand analysis where the attempt put the check. That is the 0B
work, and the module plus its battery are its specification: the battery now asserts
the state that actually holds, that every push is refused including one carrying a flawless
authorisation, and it is written to fail the day the permission is wired in, so that day
somebody has to come and state the new truth deliberately.

Until then the refusal is total, which is the behaviour the guard had before the attempt and
the one that fails closed. §21d's push bullet carries `NOT YET ENFORCED` in its own text, so
an actor loading the rule cannot read it as a permission it holds.
`framework/scripts/test_push_authorization.py` states the permission as the set of pushes it
refuses — force in four spellings, `origin` with a perfect record, a bare push, a `+`
refspec, a renaming refspec, a stale SHA, a red gate, an unattributed record, `main` without
the merge assertion — and one class of it binds the session the way the hook process does
and asks `guard_policy.verdict` itself, because a permission proved only at its own module
is one nobody has shown the guard consults. That class now asserts that every push is
refused, which is the state that holds.

A second class, `KnownHolesThisSpecificationStillHas`, asserts the **defects** the module
still carries: long options abbreviate past an exact-match list — thirteen spellings are
recorded, including every abbreviation of `--mirror`, the most destructive of the refused
flags — and `--receive-pack=` / `--exec=` name the program the far side runs, a family the
guard already polices when it is spelled `-c <key>=<program>`. Recording these as English in
a docstring left the battery green over a module that admits them: a certificate where a
specification was wanted. As cases, closing a hole turns it red and forces the next author to
invert the assertion deliberately.

Two claims made in the first version of that class were **wrong, and are now recorded as
non-holes**: `--repo=origin` loses to the command-line operand (git-push(1): *"If both are
specified, the command-line argument takes precedence"*), and `--exec-path=` is not an option
of `git push` at all — the real vector is the global `git --exec-path=… push`, which is why
`--exec-path` is now in `REDIRECTING_GLOBALS`. Both were written up on the strength of
reading the module and never running `git`, which is the same error as the permission they
document, one layer up.

**And one deferral claim was false.** This record previously said three holes were "not
expressible at this layer" — environment prefixes, the payload `workdir`, and a second
statement after `&&` — and used that to justify moving the whole job to the decision layer.
Only `&&` qualifies. `evaluate(..., redirected=("GIT_DIR=…",))` refuses **today**: the channel
exists and denies, and what is missing is a caller that populates it, which is guard work of
a much smaller size than "rebuild this at the decision layer".

The gate result is **read, never recomputed inside the hook**: a `PreToolUse` hook has ten
seconds and runs on every command. The actor records the verdict against a SHA first, which
is also how the recording obligation is discharged by construction — without the record
there is no push.

### Four bypasses, found by review and closed before merge

The first implementation was **weaker than the blanket refusal it replaced**. Mirror found
four ways to reach a real `git push`; each was allowed at `8abe371` and refused at the commit
carrying this text, and each is now a named case in the battery.

| Bypass | Why it worked | Closed by |
|---|---|---|
| `git push -fu development work` | the refused-flag list was exact-match, and git bundles short options — `-f` was refused, `-fu` was not | membership tested per LETTER, not per spelling |
| `git -C <peer> push development work` | `git_subcommand` skips `-C` to reach the subcommand, so the permission read the SHA and the ledger in the assigned worktree while the objects were sent from another repository | a network subcommand under a repository-moving global is refused BEFORE the recursion — a push is not a relocatable effect |
| `git push development refs/tags/work` | the ref was reduced to its last path segment, so a tag was gated as the branch of that name and published an object the gate never saw | a qualified ref is accepted only under `refs/heads/`, and both sides of a refspec must name the same branch |
| `git push development $(echo work)` | the substitution sentinel carries NUL, `subprocess` raised `ValueError`, the hook died — and on this channel a dead hook is silence, and silence is ALLOW | non-printable operands refused before resolution, and `ValueError` caught at the resolver |

The review that found them also named why the first battery missed them, and it is the more
useful finding: seven integration cases, six asserting a refusal and one an allowance, and
the allowance was the single canonical spelling. Not one asked whether a **variant of the
permitted form** was still permitted — the only quadrant that can hurt anyone. The battery
now carries that quadrant as a class of its own, `VariantsOfThePermittedFormAreStillRefused`,
including the cases that must stay ALLOWED so the repair cannot drift into refusing by shape.

### What this control does NOT guarantee

Stated in the shape Annex J.0 requires, because a control described more strongly than it
behaves is worse than no control:

- `GUARANTEE_PROVIDED` — no push reaches a remote other than `development`; none carries a
  force or `+` refspec; none proceeds without a ledger entry naming the exact SHA, a clean
  gate, and an actor; `main` needs the merge assertion as well. All of it is enforced in
  the guard, on the channel the guard watches, and the battery states each refusal.
- `FAILURE_MODE_STILL_POSSIBLE` — **the ledger is written by the same actor that pushes.**
  Nothing stops an actor from hand-writing an entry claiming `gate_verdict: PASS` without
  running the gate, or asserting `merge_changed_no_guarantee` about a merge that changed
  one. The `record` subcommand runs the gate honestly, but using it is not compelled. This
  control raises the cost of a mistake to near-certain detection; it does not defeat a
  deliberate false record. Separately, the guard is registered on the `Bash` matcher alone,
  so a runtime that pushes through another channel is not evaluated at all.
- `DETECTION` — **weaker than the first draft of this bullet claimed.** That draft said "the
  ledger is committed, so a forged entry is in the diff Mirror reviews". Nothing commits it,
  nothing requires it to be committed, and `read_ledger` reads the working tree: an actor can
  write the entry, push, and delete the file, leaving no artefact behind. What detection
  actually exists is that the gate can be re-run against the recorded SHA by anyone, and the
  remote records what arrived. Making this ledger tamper-evident — the hash chain
  `fulltext_receipts.py` already implements, anchored in the state manifest, whose hand-edit
  halts LEGEND — is the obvious repair and is **not done here**. The one ledger guarding the
  only irreversible act is the one without a chain.
- `RECOVERY` — none for the publication itself. A push to a public repository is
  irreversible, which is why the reservation list still opens with publication and why
  `origin` is never in scope.
- Two further limits, stated rather than discovered later. **The authority ladder no longer
  sees an allowed push**: the permission returns before emitting a `Finding`, so
  `authorized_effects` for a permitted push is empty and `effect_model`'s PUBLISH sentence
  — "never granted by a runtime, a role or a lease" — remains literally true while
  describing nothing, because publication no longer passes through PUBLISH at all. G6 in
  PLAN-MODULAR-EVOLUTION-001 §M4 cites that pairing as evidence for "authority explicit";
  that citation is now stale. And **fast-forwardness is not checked here**: forced spellings
  are refused, and a genuine non-fast-forward is left to git's own refusal, which is a
  different instrument from this one.

## VERIFICATION_TRAIL

| Check | Command | Result |
|---|---|---|
| Anonymous read of `development` | `GIT_TERMINAL_PROMPT=0 git ls-remote development HEAD` | `b1b5a58…`, no prompt |
| Repository visibility | `curl -s https://api.github.com/repos/marinomassimo-dot/legend-development` | `private: false`, `visibility: public` |
| H.1 authority matrix | `governance/annex_h_authority_matrix.md:22-42` | read verbatim; quoted in MAPPING |
| Strict MAJOR definition | `governance/GOVERNANCE_v3.1.1.md:250` | quoted verbatim in `change_class_rationale` |
| Both block hashes | `shasum -a 256` over the two blocks | match the RATIFIED_TEXT table |

## OUT_OF_SCOPE

Not done, not authorized, not implied by this record:

- **ratifying anything** — ratification is the operator's merge, not this commit;
- Mirror findings **F1** (`test_runtime_diagnostics`'s two siblings now passing
  vacuously against a blob that is no longer the legacy engine), **F7** (§21d names an
  Orchestrator with no lease predicate; 0 ACTIVE leases), **F8** (Annex J.0 vocabulary on
  "unattended deployment"), **F9** (the 8→8 red set is a property of this disk, not of
  either commit), **F10** (two unanchored denominators in one commit) — all remain open
  and are carried forward. This delta closes **F2–F6** only;
- any push to `development` or `origin`;
- any `HUMAN_APPROVAL_QUEUE` entry.

## OPEN — Mirror's delta review of this record

Mirror reviewed the commit that created this record and refuted four of its five claimed
closures. Recorded here rather than repaired, because each remaining item is either reserved
text or an operator decision:

| # | Item | State |
|---|---|---|
| D-1 | §21d's opening clause was a blanket grant, making the added sentence either vacuous or non-binding | **PARTIALLY CLOSED** — the clause is scoped to *"every question that H.1 does not assign to another actor"*, which removes the blanket. Three H.1 rows still fall through it, and the scoping makes the section's own next sentence describe an empty reassignment. An earlier version of this table said CLOSED while MAPPING two sections above kept the same defect open; that contradiction is the reason for this row's wording — see MAPPING, open problems 2 and 3. 🔴 **This is a merge-time decision, not a post-merge finding.** Merging ratifies a §21d whose residual grant reaches `Promozione BOOTSTRAP_CONTROLLER → Orchestrator \| protocollo Annex I (mai autoassunzione)` — a row that forbids self-promotion by name — and `Lifecycle learning: epistemico Mirror, durevolezza Plan`, whose Authority cell is `—`. That is a substantive expansion of Orchestrator authority, and the operator should decide it deliberately rather than inherit it |
| D-2 | §21d permitted a `development` push that RESERVED bullet 1 and `DENY_NETWORK` both forbade | **CLOSED** — bullet 1 carries the carve-out and the credential-gating proviso is replaced by the push discriminator. **The guard does NOT enforce it:** the rule self-declares `NOT YET ENFORCED` and every push is refused, so the collision is gone because nothing is permitted, not because something now checks. An earlier version of this row read "and the guard enforces it", which was false, in a row asserting a closure |
| D-3 | Appending to SAFE_DEFAULTS forced edits to five declarations including the test constant | **CLOSED** — the list is outside the hashed body; an append is proved not to disturb it |
| D-4 | This record declines the `HUMAN_APPROVAL_QUEUE` object that GOVERNANCE §130, Annex J.3 and GATE 5 require, substituting the merge | **OPEN** — operator. Mirror's repair: a queue entry `TYPE: GOVERNANCE`, `OBJECT: <candidate content hash> + BASE_HEAD` |
| D-5 | Producer ≠ verifier: the Orchestrator authored the record granting the Orchestrator authority, and §21d scopes that discipline to *scientific* claims only | **OPEN** — operator. Mitigation in place, not a closure: Mirror reviewed the delta independently, and the operator's merge is the human ratification |

Repaired in the commit following this record, and not left open: the 3/3 miscount, the
under-enumeration of H.1's 17 rows, the over-broad reading of the guard's `REF_WRITE`
refusal, the F2 conclusion above, and two test weaknesses — `assertIn` replaced by section
equality, and the reachability predicate replaced by a markdown link, each falsified before
being claimed.

## ATTESTATION

**Recorded by:** Orchestrator, on `plan-modular-evolution-p0a-exec`, at the operator's
explicit dispatch, 2026-09-03. The RATIFIED_TEXT is the operator's own dictated bytes,
anchored by hash rather than by date alone. The prose of this record — MAPPING, the
SAFE_DEFAULTS resolution, F2, this attestation — is Orchestrator analysis and is **not**
itself ratified text.
