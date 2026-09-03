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
| STOP POLICY — §21c body, including STOP LOG and SAFE_DEFAULTS | 42 | `776e6556d5fbbac3d23fd99e15a3b1bce416d27d17f6701685bd93369030f941` |
| DECISION AUTHORITY — §21d body | 32 | `a1eff7741ffe03f8349b49f4d38e23be5bed4cd1725dfaf58473fdaf631029ba` |

Each hash covers the text from its opening line (`STOP POLICY (HARD RULE, …)` /
`DECISION AUTHORITY (HARD RULE, …)`) to the last character of its closing line, with no
trailing newline — the exact block `test_stop_policy.py` holds as a constant. Re-derive
from the repository root:

```
python3 -c "
import hashlib, sys, pathlib
sys.path.insert(0, 'scripts')
from test_stop_policy import STOP_POLICY, DECISION_AUTHORITY
text = pathlib.Path('framework/instruction/LEGEND_CORE.md').read_text(encoding='utf-8')
for name, block in (('STOP_POLICY', STOP_POLICY), ('DECISION_AUTHORITY', DECISION_AUTHORITY)):
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
2. **Two H.1 rows are prohibitions, not assignments,** and a residual grant reaches them
   most sharply: `Modifica rubrica/metodi di Mirror | mai Mirror da solo (G.2)` and
   `Promozione BOOTSTRAP_CONTROLLER → Orchestrator | protocollo Annex I (mai
   autoassunzione)`. Neither appears in RESERVED.

Both are operator decisions on reserved text. They are named in OUT_OF_SCOPE as open.

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

**`development` push therefore remains RESERVED to the operator, on the reservation's own
terms and on the guard's, not merely because §21d is unratified.** Whether the permission
bullet should be struck, or rewritten against a different property than credential-gating,
is an operator decision on reserved text and is open.

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

| # | Open item | Owner |
|---|---|---|
| D-1 | The sentence added to §21d is either vacuous or does not bind — see MAPPING | operator (reserved text) |
| D-2 | §21d permits pushing to `development`, which RESERVED bullet 1 and `DENY_NETWORK` both forbid — see F2 | operator (reserved text) |
| D-3 | Appending to SAFE_DEFAULTS now forces edits to five declarations, including the test constant the suite's own message forbids editing and this record's hash table. The §21c permission and the hashing mechanism still collide | operator (reserved text) |
| D-4 | This record declines the `HUMAN_APPROVAL_QUEUE` object that GOVERNANCE §130, Annex J.3 and GATE 5 require, and substitutes the merge. The cheap repair Mirror names is a queue entry of `TYPE: GOVERNANCE`, `OBJECT: <candidate content hash> + BASE_HEAD 4dd9b83` | operator |
| D-5 | Producer ≠ verifier: the Orchestrator authored the record that grants the Orchestrator authority, and §21d scopes that discipline to *scientific* claims only | operator |

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
