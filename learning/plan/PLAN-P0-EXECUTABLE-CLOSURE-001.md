---
record_type: WORK_ANALYSIS
id: PLAN-P0-EXECUTABLE-CLOSURE-001
title: A one-line untracked file turned a publication BLOCK into a PASS, and my own repair would have spread it
date: 2026-08-26
role: PRODUCER
mode: BUILD / P0 EXECUTABLE CLOSURE
authority: Plan role contract — candidate preparation on own branches. No CANONICAL_BATCH_COMMIT.
  No H.1 decision selected. No governance text amended. No event emitted.
status: NINE CANDIDATES · critical evidence made durable · two normative boundaries held
---

# P0 EXECUTABLE CLOSURE

> **Nothing here is medical advice.** Tooling, control plane and integration shape only.

---

## 1 · 🔴 The finding that outranks the rest of this session

Mirror reported that a tracked publishable document can leave the validation population because a
local `.git` marker appears beside it. **Re-derived, and it is worse than the report.**

`is_nested_checkout` was `(path / ".git").exists()` — a filesystem **name**, not repository
metadata. On a clean checkout of `main`, dropping one untracked line into `governance/.git`:

| | |
|---|---|
| publishable markdown | 281 → **246** |
| **tracked** documents removed | **35**, including `GOVERNANCE_v3.1.1.md` and every annex |

And with a broken wikilink planted in one of them first:

```
without the marker   VERDICT: BLOCK_PUBLICATION   BLOCKS: 1
with the marker      VERDICT: PASS                BLOCKS: 0
```

**A one-line untracked file turned a publication BLOCK into a PASS.** The gate did not fail to
detect the violation — it removed the file holding it from its own population and then reported
finding nothing. That is the worst shape a gate defect can take, because the output is
indistinguishable from a clean repository.

🔴 **It is a defect on `main`, and my own candidate would have spread it.** REPOSURFACE routes
`test_documented_commands` through the same walker, which is how it surfaced. A repair that
extends a latent bypass to a second guard is not neutral, and the sequence — reuse an existing
helper, then find the helper is broken — is the argument for auditing what you reuse.

**Repair:** the predicate asks the outer repository instead of the disk. A directory is a nested
checkout only if it looks like one **and this repository tracks nothing inside it.** Real
worktrees are gitignored and hold zero tracked paths, so they still prune; a tracked tree with a
stray marker does not. Both controls are tested — a real nested worktree must still be pruned, and
an untracked vendored tree must still be pruned — because a predicate that stopped pruning
anything would satisfy the first test alone. The gate's own 42-test suite is unchanged and green.

---

## 2 · CPROOT — current verdict, and observability

Seven conditions, re-verified against the current tip:

| Condition | exit | records |
|---|:--:|:--:|
| ROOT | 0 | 5 |
| ACTOR_WORKTREE | 0 | 9 |
| NESTED_SUBDIRECTORY | 0 | 5 |
| DETACHED_HEAD | 0 | 5 |
| TMP | **2** | — |
| WORKTREE COMMON-DIR (`.git` itself) | **2** | — |
| NO_REPOSITORY_CONTEXT | **2** | — |

Standing inside `.git` refuses, which is correct: it is not part of a working tree. Worktree
binding is preserved deliberately — ROOT reads 5 and ACTOR_WORKTREE reads 9, which is today's
behaviour and **not** the relevance decision.

**Observability, added because it is mechanical.** `lease_state.py` now prints
`CONTROL_PLANE_SOURCE_PATH`, its `SHA256` and `RECORD_COUNT`. The same command read a 5-record
lease and a 9-record one and printed the same *shape* of answer both times; the only way to tell
them apart was to already know. **A derived answer that does not name its source cannot be
reconciled with another derived answer, and reconciling them is the whole of the control-plane
problem.** It asserts nothing about which object *should* have been read.

---

## 3 · P0 evidence made durable

Every critical proof is now a committed command inside the candidate that owns it, with both arms.

| Evidence | Command | Negative arm | Positive arm |
|---|---|---|---|
| CPROOT probe | `control_plane_probe.py <dirs>` | two checkouts with different histories → **DIVERGENT**, exit 1 | three directories of one checkout → **UNIFORM**, exit 0 |
| primitive comparison | `test_repo_root.py` | six of twelve fail against `main`'s unwired tools | twelve pass on the candidate |
| ADJFAILCLOSED state matrix | `adjudication_state_matrix.py --script <copy>` | `main`'s copy → **12** exit-0 degraded states | the candidate → **3**, all declared |
| APQCONS CLI fixtures | `test_consolidate_approval_queue_cli.py` | six of seventeen fail against the pre-repair CLI | seventeen pass |
| REPOSURFACE invariance | `test_repository_surface_determinism.py` | a stray `.git` suppressing a real BLOCK → refused | a real nested worktree still pruned |
| lease singleton | `test_lease_singleton.py` | two files, one ACTIVE each → **MULTIPLE_ACTIVE** | each alone → **UNIQUE_ACTIVE** |
| P7 anchor | `test_event_ledger.py` | edited tail → append **refused** | honest append → no disagreement |

**The composition matrix and the union resolver remain in the scratchpad.** They operate across
candidate branches, so they belong to no one candidate; committing them into one would make that
candidate's acceptance carry a tool about the others. Named as the one piece of critical evidence
still not durable, rather than quietly left out.

---

## 4 · The lease singleton classifier — detection without the policy

Annex J.0 lists `Singleton garantito (compare-and-swap)` among the guarantees this system does not
possess and names the compensating protocol: `lease record + rilevazione doppio ACTIVE + stop
condition (I.3)`. **That detection was unavailable.** Two worktrees each holding one ACTIVE lease
both report `ACTIVE by derivation: 1` and both exit 0.

`lease_singleton.py` classifies an **explicit** set into `UNIQUE_ACTIVE` · `MULTIPLE_ACTIVE` ·
`NO_ACTIVE` · `UNDERIVABLE`.

🔴 **It supplies the detection and not the policy.** It discovers no source of its own, and a test
greps its source for `for_each_ref`, `rev-parse`, `glob(` and `iterdir(` to keep that true —
because a tool that chose its own inputs would be answering the relevance-set question silently.
`MULTIPLE_ACTIVE` is a classification of what was supplied; its own output says it is *"not a
ruling on which lease is authoritative and not a stop condition"*.

`UNDERIVABLE` is never merged into a count: **an unparseable file is not evidence of zero ACTIVE
leases.** The first draft wrapped only `parse()` and not `derive()`, so a record with neither
timestamp escaped as an exception rather than a verdict — an underivable state leaving by a door
marked *crash*, which is the class this whole session has been closing.

Run against the two real lineages: **`NO_ACTIVE`**, 5 and 9 records, no ACTIVE in either.

---

## 5 · APQCONS at the current tip

The tip Mirror may have reviewed is superseded. **Current: `plan-approval-queue-consolidator`.**

| Invariant | Result |
|---|---|
| three directories, one basename, distinct payloads | `d1/queue.jsonl=6, d2/queue.jsonl=14, d3/queue.jsonl=10` |
| input count preserved | **30 input lines**, was `10` |
| lineage count preserved | **3 lineages**, was `1` |
| same ID / different content | exit 1, CONFLICT |
| integer / malformed ID | kept, content-addressed |
| missing timestamp | allowed |
| malformed timestamp | exit 2, SOURCE ERROR |
| malformed JSON | exit 2, **not routed to an operator** |
| unknown status | carried through |

**N input lineages → N lineages reach the consolidator**, or an explicit validation failure. No
silent source collapse. **17 CLI tests; 6 fail against the pre-repair CLI.**

---

## 6 · ADJFAILCLOSED — scope decided before anything was patched

The declared contract is **RECIPE_REGENERATION**, from the tool's own docstring: *"fails closed
when a digest disagrees, when the PDF is absent, or when the PDF itself is not the one the recipe
was taken from"*. Not directory integrity. The membership test: **can this corrupt another
declared regeneration?**

| Mutation | Classification | Measured |
|---|---|---|
| duplicate `file` targets | 🔴 **IN_SCOPE** | `artifact[0]` declares `f495b656…`, `artifact[1]` declares `6abfb6f0…`, `a.png` on disk held `6abfb6f0…` — **one regeneration destroyed the other**, verify exit 0, clean summary |
| path traversal in `file` | 🔴 **IN_SCOPE** | `"../../../../ESCAPED.png"` landed in `disease-models/` — outside the adjudication directory, inside the repository |
| absolute path in `file` | 🔴 **IN_SCOPE** | `Path(dir) / "/tmp/x.png"` is `/tmp/x.png`; `write` left a file outside the repository |
| zero-area crop | **OUT_OF_SCOPE_AND_CORRECTLY_IGNORED** | already exit 1: *"crop (100,100,100,100) does not contain the span (72,87,154,104) it adjudicates"* |
| undeclared PNG, directory with no recipe, corrupted local PNG | **OUT_OF_SCOPE_BUT_SUMMARY_OVERCLAIMED** | closed last session by reporting, not by failing |

**Not every nameable mutation was patched.** Zero-area is refused by geometry, and a test asserts
it is refused *by geometry and not by the new check* — **out of scope and silent is a different
verdict from out of scope and correctly ignored**, and widening the contract to cover everything
would make the tool promise more than it does.

`file` must now be a plain name, unique within its recipe. **Current false-green count within the
declared contract: 0.**

---

## 7 · P7 anchor

`initialise()` anchors an empty ledger explicitly at zero, because `verify_anchor([], {})` fails
and `verify_anchor([], anchor([]))` passes — so *"no anchor yet"* and *"the anchor was lost"* are
otherwise indistinguishable. `append()` consults the anchor **before** writing and re-anchors from
what is **on disk** afterwards.

🔴 **`verify_anchor` no longer names a direction.** It was measured producing the same message for
a legitimate append and a truncation; *"truncated or appended to outside the writer"* reads as a
diagnosis and is not one. It reports the disagreement and stops. What removes the ambiguity is not
wording but anchoring on append, so an honest write never leaves the two disagreeing — **an alarm
that fires on every honest write is an alarm that gets ignored.**

**Two tests that asserted the OLD limitation were rewritten to assert the repair.** That is the
honest way to record that a limitation ended; leaving them would have meant a suite asserting a
defect the code no longer has.

**Residual, stated not engineered away:** the ledger and the anchor are two files and cannot be
written in one operation. Same residual `fulltext_receipts.py` names for itself. **41 tests. No
event emitted, and a test now also asserts no anchor file exists in the repository.**

---

## 8 · Scientist B — the transformation is already done

**Do not invent an artifact class, and do not build a conversion helper: neither is needed.**
Scientist B's seven repairs are already `COMMIT CANDIDATE`s in `commit_candidates/`.

| Field | Scientist B (7) | Scientist A (19) |
|---|:--:|:--:|
| Candidate ID | **7/7** | 16/19 |
| **Author** | **7/7** | **0/19** |
| **Base head** | **7/7** | **0/19** |
| ≥1 receipt | 6/7 | 6/19 |
| change class parseable | **7/7** (3 MAJOR, 4 MINOR) | 12/19 |
| machine-readable frontmatter | **0/7** | **0/19** |

⇒ **The precedent already exists inside the repository, and it is B's own shape.** `**Base head:**`
is what binds a candidate to a hash and `**Author:**` is what attributes it; B carries both on
every one, A on none. The minimum transformation for routability is therefore **not a new class —
it is A's set adopting the fields B already uses.**

The one gap both share is the one already routed: no machine-readable class, so **no gate can
derive the reviewer floor.** That remains a governance question and is not reopened here.

---

## 9 · Composition

Nine candidates, all from `BASE_HEAD 788c357d`, each passing isolated validation before entering.
The only conflicts are on `run_release_regressions.py`, resolved by union — correct because
`test_release_runner_verdict` reads `set(runner.TESTS)`.

**Known router-policy failures are not counted as candidate regressions**: the four CLAUDE.md
suites are red on `main` and on every prefix, and they are a normative decision, not a defect any
of these candidates introduced.

| Prefix step | runner entries | mode-bit offenders | duplicate tests | failures | conflict | new failures |
|---|:--:|:--:|:--:|:--:|---|---|
| `RELSURF` | 66 | 0 | 0 | 4 | clean | *(baseline)* |
| + `CPROOT` | 67 | 0 | 0 | 4 | union | none |
| + `REPOSURFACE` | 68 | 0 | 0 | 4 | clean | none |
| + `LEASESINGLETON` | 69 | 0 | 0 | 4 | union | none |
| + `GOVTESTS` | 71 | 0 | 0 | 4 | union | none |
| + `ADJFAILCLOSED` | 72 | 0 | 0 | 4 | union | none |
| + `P7LEDGER` | 73 | 0 | 0 | 4 | union | none |
| + `APQCONS` | 75 | 0 | 0 | 4 | union | none |
| + `ORCHMAJOR2` | 75 | 0 | 0 | 4 | clean | none |

`main` fails **6**. The composed branch fails **4** — the router class throughout. **Zero
mode-bit offenders and zero duplicate entries at every prefix**, and no prefix introduced a
failure. Runner entries 65 → **75**.

⚠️ Content-hash invalidation is total and unavoidable: any candidate executing moves `BASE_HEAD`
for the other eight, so all eight rebase and rehash. What the order buys is that each is measured
against a guard an earlier candidate has already cleaned — which is how the `100644` shebang and
the `.git` pruning bypass were both found.

---

## 10 · Candidates

`BASE_HEAD 788c357d9b7ca7afcbe7c1efc3a06b426cf7e2d5` for all nine. Every hash reproduced twice.

| Candidate | Branch | Tip | `CANDIDATE_CONTENT_HASH` |
|---|---|---|---|
| RELSURF | `plan-release-surface-repair` | `bf9c807` | `541a2631…0a7feb9e` |
| **CPROOT** | `plan-control-plane-root` | `5e8d66f` | `147cdba2…f204deda8` |
| **REPOSURFACE** | `plan-repo-surface-determinism` | `d3c4b2a` | `16241562…9eaddb968` |
| **LEASESINGLETON** *(new)* | `plan-lease-singleton-classifier` | `49c6885` | `2a5168dd…7faf96472` |
| GOVTESTS | `plan-governance-test-durability` | `c1294fd` | `16a20ba4…887d84095` |
| **ADJFAILCLOSED** | `plan-adjudication-failclosed-repair` | `edb8172` | `8a082f93…d9519a17` |
| **APQCONS** | `plan-approval-queue-consolidator` | `897bef7` | `601963b4…06a2d6f4` |
| **P7LEDGER** | `plan-p7-event-ledger` | `c4d3451` | `d9445757…0111220b` |
| ORCHMAJOR2 | `plan-major2-restricted-repair` | `5e3a757` | `9f852385…6919389f` |

Six moved this session. **None were merged to avoid a rehash**: nine units, nine hashes, each
independently reviewable.
