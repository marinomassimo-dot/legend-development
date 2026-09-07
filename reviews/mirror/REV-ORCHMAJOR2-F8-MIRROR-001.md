---
artifact: MIRROR hostile review (Annex C.2) — delta, append-only
review_id: REV-ORCHMAJOR2-F8-MIRROR-001
object: the four Finding-8 variants `plan-major2-f8-option-A|B|C|D`, and the deposited state
  `plan-major2-restricted-repair` @ `7d24410`
delta_of: PRIVACY_SEMANTICS_AND_FALSE_PASS_HOSTILE_REVIEW_MIRROR_v2 § 7.3 (FINDING 8)
level: R4 (METHOD — Mirror)
reviewer: mirror
date: 2026-08-26
verdict: FINDING 8 CLOSABLE — one variant closes it with no new authority surface; two do not
  close it; one closes it by deletion and opens a different contradiction. Two variants that
  read as synonyms are not.
measurement_order: every figure in §§ 1–4 was derived before the candidate's § 6bis was opened.
  § 5 is the comparison, and says where the author and I agree.
appends_to: this document does not modify v2. v2 § 7.3 stands as written.
---

# Two of the four say the same thing about a place and one says it about an act, and only the act-scope permits a hand commit to `main`

---

## 0 · OBSERVATION_SCOPE

| Fact | Value |
|---|---|
| Derivation window | `2026-08-26T09:0x` onward, this session |
| `main` | `788c357` |
| Variants | `plan-major2-f8-option-A` `abdcc7f` · `-B` `aaf8163` · `-C` `aaa14d7` · `-D` `0b21db0` — each **1 ahead of `main`, 0 behind**, each touching **`roles/orchestrator.md` and nothing else** |
| Deposited state | `plan-major2-restricted-repair` @ `7d24410`, 4 ahead — the 4th commit moved **only** the candidate record (+126/−5); the object is byte-identical to `a115cbd` |

---

## 1 · The four objects, measured before any justification was read

Change 1 — `worktree: the repository root checkout` → `worktree: orchestrator` — is **identical in
A, B, C and D**. Only change 2 varies.

| | change 2 | shape |
|---|---|---|
| **A** | commit its own work **through `CANONICAL_BATCH_COMMIT`** | scoped to an **act** |
| **B** | commit its own work **to `main`** | scoped to a **place** |
| **C** | commit its own work **to the canonical surface** + a frontmatter key defining that phrase | scoped to a **place**, with the place defined in the role contract |
| **D** | *(unchanged — the absolute prohibition stands)* | change 2 **dropped** |

---

## 2 · Two facts that reframe the whole question, and neither was in v2

### 2.1 · Change 1 is a factual correction, not a policy change

`worktree: orchestrator` names a branch **and** a checkout that both exist:

```
.claude/worktrees/orchestrator      1e2fabd [orchestrator]
```

The value it replaces — *"the repository root checkout"* — described the root, which is on `main`
@ `788c357`. Every other role contract already names a bare branch (`mirror: mirror`,
`plan: evidence-index`), so the old value was the only prose one and the only false one. **All
four variants correct it.**

### 2.2 · Change 2 grants no new capability, because the capability has been exercised 42 times

```
orchestrator branch: 42 commits ahead of main, 37 files, 7085 insertions
  every one under runtime/  (bootstrap, handoff, lease, runtime_inventory)
  canonical scientific files touched: 0
  main touched: 0
```

The prohibition *"Orchestrator must not commit its own work"* is already contradicted by 42
durable commits, **none of them on the canonical surface**. So change 2 does not widen the
capability set, as v2 § 7.3 framed it. It writes down a boundary that practice has been observing
without a rule. **That inverts the risk**: the question is no longer *should this be permitted*,
it is *is the written boundary the one practice is actually honouring* — and a boundary that is
wrong in the permissive direction is worse than no boundary, because it is quotable.

**Correction to v2 § 7.3.** v2 called change 2 *"a widened capability"* and asked whether the
widening is authorised. That framing is wrong on the evidence above: it is a **narrowed
prohibition matching an existing practice**. The finding itself — that the bounding term is
undefined — survives intact and is what §§ 3–4 test.

---

## 3 · The eight tests

`CANONICAL_BATCH_COMMIT` occurs **8 times in the governance body**, once in Annex D and once in
Annex H, and the body dedicates § 12 to its gates. `canonical surface` occurs **zero** times as a
normative term anywhere under `governance/` or `roles/` on `main` (its three prose occurrences
are scientific-layer usage — *"five canonical surfaces credited…"* — a canonical **file**, not a
write surface).

| test | **A** — act | **B** — `main` | **C** — defined place | **D** — no change 2 |
|---|---|---|---|---|
| **TERM_DEFINED** | **PASS** — 10 normative occurrences, gates in body § 12 | PARTIAL — a git ref, not a governance term; the body writes *"mai su main/root"* once, for Plan | **FAIL as sited** — defined only in the role contract, see § 4.1 | **N/A** — no term |
| **AUTHORITY_BOUNDARY** | bounded by an act the body already gates | bounded by a branch name — observable, but silent on the root checkout | bounded by a place the same file defines | unbounded, because unchanged |
| **ROOT_WORKTREE_CONSISTENCY** | PASS | PASS | PASS | **FAIL** — see § 4.3 |
| **GATE1_ALIGNMENT** | **PASS, exactly** — body § 12 GATE 1 reads *"Proponente ≠ esecutore. Solo candidate preparati da Plan; **mai lavoro proprio**"*, and GATE 1 governs `CANONICAL_BATCH_COMMIT`. A restates GATE 1's own scope in the role contract | PARTIAL — a place, where GATE 1 speaks of a commit path | PARTIAL — same | vacuous |
| **REV4_IMPORT** | **none** | **none** | **PARTIAL IMPORT** — see § 4.2 | **none** |
| **UNINTENDED_CAPABILITY_EXPANSION** | **none** — § 2.2; but see § 4.4 | none | none | none |
| **TESTABILITY** | weak — nothing records which path a commit took | **strongest** — a branch name is an observable | moderate — the definition supplies the predicate; nothing parses it | n/a |
| **SEMANTIC_EQUIVALENCE** | — | **≈ C** | **≈ B** | **DIFFERENT** |

**Body alignment, which is not one of the eight and outranks several of them.** All four leave
`governance/` untouched. The source of this clause is the body itself:

> **§ 35.1 Recinto Orchestrator.** NON DEVE: committare lavoro proprio; toccare worktree altrui;
> bypassare Plan; batch senza gate (incluso GATE 0); … usare la root come spazio libero.

`roles/orchestrator.md` is a transcription of § 35.1. Precedence (body § 5) ranks
**NON-NEGOTIABLE GOVERNANCE = 1** and **ROLE-SPECIFIC RULES = 4**. So under A, B and C the role
contract permits what the body forbids unqualified, and the body wins — the repair is **legible
but inert** until § 35.1 carries the same scope. This is a finding against all three, and it is
the Operator's to route, because amending the body is not a role-contract change.

---

## 4 · Four findings the table compresses

### 4.1 · FINDING 8a — a rank-4 document cannot bound a rank-1 prohibition (option C)

C supplies the definition v2 asked for, and puts it in the role contract's frontmatter. Two
defects:

- **Siting.** The prohibition it bounds originates in body § 35.1 (rank 1). A definition living
  in `roles/orchestrator.md` (rank 4) cannot narrow it. C makes the term *readable* without
  making it *binding*.
- **Nothing parses it.** The key is written `canonical surface:` — with a space, breaking the
  snake_case convention of every other frontmatter key. `governance_fingerprint.py` hashes the
  file's **whole bytes** and never parses the frontmatter, and no other script reads
  `roles/*.md` at all. So the definition is prose that happens to sit above a `---`. **A
  definition nothing can read is an attestation, not a boundary.**

### 4.2 · FINDING 8b — option C imports half of a rev-4 pair (option C only)

ORCHSURF rev 4 (`plan-exec-repair-prep`) already carries both of C's changes **and** splits the
root into three named concepts:

```
session_home:             the repository root checkout — where this actor's chat is opened…
                          It is a location and nothing more: no ACTOR_ID, no write authority
worktree:                 orchestrator
canonical_batch_surface:  the repository root checkout — CANONICAL_BATCH_COMMIT only, inside a
                          batch window only… never this actor's WORK surface
```

C's `canonical surface:` is rev 4's `canonical_batch_surface:` under a different key, **without**
`session_home:`. The pair is what does the work: `session_home` says the root is a *place* that
confers nothing, `canonical_batch_surface` says the root is a *surface* written only in a batch
window. Importing the second without the first re-opens the exact confusion — root-as-place
versus root-as-surface — that rev 4 exists to close, and does it under a key name that diverges
from rev 4's. **REV4_IMPORT: PARTIAL, and the missing half is the disambiguating one.**

### 4.3 · FINDING 8c — option D corrects a false statement and creates a live contradiction

D takes change 1 alone. It therefore designates `orchestrator` as this actor's **work** surface
while the same file forbids it to *commit its own work* anywhere. Before D the two halves were
consistent-by-vagueness: the contract said the actor's worktree was the root and that it must not
commit. After D the contract names a work branch and forbids writing to it, **in the same file, six
lines apart** — and 42 commits already exist on that branch.

The body's own obligation makes it sharper still:

| body | says |
|---|---|
| § 229 | `WORK_COMMIT → ogni attore, PROPRIO worktree/branch. Durevolezza di lavoro e learning. **Obbligatorio**` |
| § 186 | Orchestrator … **MUST fare Session Learning Review** |
| § 278 | ogni record MUST raggiungere lo stato durevole via WORK_COMMIT … *ciò che non è nello stato durevole non è accaduto* |
| § 35.1 | NON DEVE: **committare lavoro proprio** |

**That is the contradiction the MAJOR-2 exists to resolve, located.** The body obliges every
actor including Orchestrator to persist its learning by WORK_COMMIT on its own branch, and
forbids Orchestrator to commit its own work. D leaves it standing and moves it into sharper
relief. **D is not the null option.**

### 4.4 · FINDING 8d — A and B/C are not synonyms, and the divergence is the dangerous case

A scopes the prohibition to an **act**; B and C scope it to a **place**. Construct the case that
separates them: *Orchestrator runs `git commit` on `main`, at the root, outside any batch window,
without invoking `CANONICAL_BATCH_COMMIT`.*

| | verdict on that commit |
|---|---|
| **A** | **not prohibited by this clause** — the act named was not performed |
| **B** | prohibited — the place is `main` |
| **C** | prohibited — the place is the root checkout on `main` |
| body § 35.1 | prohibited under *"usare la root come spazio libero"*, which is a different clause and a vaguer one |

So the act-scope permits precisely the failure the place-scope forbids, and falls back on the
loosest sentence in § 35.1 to cover it. A's advantage on TERM_DEFINED and GATE1_ALIGNMENT is
real; this is its cost, and the two are not weighed by the same evidence. **A and B are
`SEMANTICALLY_DIFFERENT`. B and C are `SEMANTICALLY_EQUIVALENT` in effect**, differing only in
that C states the batch-window condition and B does not.

---

## 5 · Where the author and I agree, read after measuring

Candidate § 6bis reaches the same two premises independently: `canonical surface` is undefined
(*"Zero occurrences under `governance/` or `roles/` on `main`"*), and the three prose hits are
scientific-layer usage. It also records that the deposited content is C0 — *"the state Finding 8
objects to"* — left in place deliberately, and that each option is a real ref at `BASE_HEAD
788c357d`. Those match my measurements exactly and I do not restate them as findings.

Two things § 6bis does not carry, and both change the reading: the 42 commits of § 2.2, and the
body-alignment gap of § 3. The first removes the capability-expansion objection; the second says
none of the four is sufficient on its own.

---

## 6 · Verdicts

| variant | Finding 8 | new authority surface | verdict |
|---|---|---|---|
| **A** — `through CANONICAL_BATCH_COMMIT` | **CLOSED** — the term is normative, gated in body § 12, and GATE 1 already scopes *"mai lavoro proprio"* to exactly this act | **none** | **REVIEW_MINOR_FINDING** — § 4.4 act-scope; body alignment (§ 3) applies to all three |
| **B** — `to main` | **CLOSED in effect** — a branch name needs no definition, and it is the most testable of the four | **none** | **REVIEW_MINOR_FINDING** — silent on *root checkout* and on the batch window |
| **C** — defined place | **NOT CLOSED** — the definition is sited at rank 4 and nothing parses it | none, but § 4.2 partial rev-4 import | **REVIEW_MAJOR_FINDING** |
| **D** — change 1 only | **CLOSED by deletion** | none | **REVIEW_MAJOR_FINDING** — § 4.3, and the body contradiction stands |

**A ↔ B: `SEMANTICALLY_DIFFERENT`** (§ 4.4). **B ↔ C: `SEMANTICALLY_EQUIVALENT`.**
**D ↔ {A,B,C}: `SEMANTICALLY_DIFFERENT`** — a different decision, not a weaker one.

**`MAJOR2_FINDING8_REVIEW_STATUS = CLOSABLE`.** Two variants close Finding 8 with no new
authority surface. I do not choose between them: A and B answer two different questions — *which
act is forbidden* and *which place is protected* — and only the Operator can say which the
prohibition was meant to be. **The one thing that is not a choice** is § 3: whichever is adopted,
`roles/orchestrator.md` will permit what body § 35.1 forbids until § 35.1 carries the same scope,
and a role contract cannot amend the body.

## 7 · WHAT_WOULD_CHANGE_MY_MIND

- **§ 2.2** — if the 42 `orchestrator`-branch commits turn out not to be that actor's own work
  (e.g. transcriptions of Plan output committed on its behalf), the capability-expansion objection
  of v2 § 7.3 returns and my correction is wrong. Test: attribute each of the 37 files to the
  actor that authored its content, not to the committer.
- **§ 3** — if body § 35.1's *"committare lavoro proprio"* is already read narrowly elsewhere in
  the constitution (a clause I did not find), the body-alignment gap dissolves and A/B/C become
  sufficient alone. Test: enumerate every normative sentence bearing on Orchestrator commits and
  check whether any scopes it.
- **§ 4.4** — if a normative clause elsewhere already forbids any non-batch commit to `main` by
  any actor, A's act-scope costs nothing and the finding drops to cosmetic.
