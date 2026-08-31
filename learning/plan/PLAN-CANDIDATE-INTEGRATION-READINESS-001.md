---
record_type: WORK_ANALYSIS
id: PLAN-CANDIDATE-INTEGRATION-READINESS-001
title: Six candidates integrated on one branch, and the three defects only the integration could find
date: 2026-08-26
role: PRODUCER
mode: BUILD / INTEGRATION-READINESS
authority: Plan role contract — candidate preparation on own branches; Annex J.1 derived view.
  No CANONICAL_BATCH_COMMIT. No H.1 decision selected. No policy amended.
status: SIX CANDIDATES READY · integration preview built and measured · four normative
  boundaries routed, none crossed
---

# CANDIDATE INTEGRATION READINESS

> **Nothing here is medical advice.** § 8 measures scientific candidates as objects and forms no
> view on any biological claim.

**Headline, measured on clean checkouts:** `main` fails **6** release suites. The branch with all
six candidates merged fails **4**, and the four are one class — the CLAUDE.md router — which is a
normative decision and not a repair. No candidate introduces a failure.

---

## 1 · MAJOR-2 Finding 8 — five states, four refs, none chosen

Finding 8 says the deposited candidate uses `canonical surface`, an undefined term. **It is correct
and it is correct about more than it says**, and the full derivation now lives in the candidate
manifest itself, § 6bis, where a reviewer will meet it. In brief:

| Measured | |
|---|---|
| `canonical surface` under `governance/` or `roles/` on `main` | **0** |
| `canonical surface` anywhere on `main` | **4 — all plural, all non-normative**, meaning *a canonical file that carries a claim* |
| `CANONICAL_BATCH_COMMIT` under `governance/` + `roles/` | **15 files** |
| the deposited paragraph vs revision 4's | 🔴 **byte-identical, all five lines** |

**The second row is the sharper defect**: the phrase is not merely undefined, it is **already in use
on `main` meaning something else**, one layer down. The fourth is a correction to my own record —
§ 5 of that manifest defends the paragraph as *"derived, not copied"*, which is true of the wrap
rule and false of the four words. **The reflow was re-derived; the vocabulary was taken.**

| | Qualifier | New term? | Lines shared with rev 4 | `CANDIDATE_CONTENT_HASH` |
|---|---|:--:|:--:|---|
| **D** | *none*, `+1/−1` | no | 0 | `44d33b04…73205feb` |
| **A** | `through \`CANONICAL_BATCH_COMMIT\`` | no | 0 | `756b9320…3cbb1dc6` |
| **B** | `to \`main\`` | no | 0 | `d1e88b3f…9ee9fc55` |
| **C** | phrase + frontmatter definition | **yes** | 5 | `11522036…a5b1a8f1` |
| **C0** | phrase, undefined — **deposited** | yes | **5** | `9f852385…6919389f` |

Each is a real ref, `plan-major2-f8-option-<X>`, `BASE_HEAD 788c357d`, every hash reproduced twice.

**Are they new policy?** Annex D.1 — `FROZEN`, rank 1 — labels `WORK_COMMIT` **`non canonico`** and
`CANONICAL_BATCH_COMMIT` *"solo Orchestrator, root, gate 0–5"*. So A and B express the Operator's
instruction in the governance's own object language. **The Operator said *limit it to the canonical
surface*; that is a description of the scope, not a term to transcribe.** A and B implement the
scope. C0 transcribed the description.

**Blast radius, identical for all five and small.** Any edit here rotates a fingerprint. Measured,
`main` vs option D, all four roles composed: **orchestrator ROTATED, plan · mirror · scientist
UNCHANGED** — the control that shows the tool discriminates. Orchestrator checkpoints: **0**. Plan
holds 19 and they do not move. **The rotation invalidates nothing.**

🔴 **Not chosen.** Plan's non-binding reading is **A**, offered because a producer who declines to
recommend is not being neutral, only quiet.

---

## 2 · The dependency graph, and why no order avoids the conflicts

All six share `BASE_HEAD 788c357d`. **Exactly one file is contended.**

| Candidate | Content files | Touches runner | Rebase kind after any predecessor lands |
|---|:--:|:--:|---|
| **ORCHMAJOR2** | 1 (`roles/orchestrator.md`) | no | mechanical |
| **GOVTESTS** | 4 | **yes** | merge |
| **RELSURF** | 5 | **yes** | merge |
| **ADJFAILCLOSED** | 5 | **yes** | merge |
| **APQCONS** | 3 | **yes** | merge |
| **P7LEDGER** | 3 | **yes** | merge |

**`scripts/run_release_regressions.py` is touched by five of six.** Every insertion lands in the
same hunk — all report `@@ -54,6 @@` — so **any two of the five conflict, in any order.** Measured
by simulating two orders end to end; the first merge is clean and every subsequent one conflicts.

**There is no order that avoids them.** What an order can do is make each conflict trivial, and
they are: every one is *both sides added a line to a tuple*. `test_release_runner_verdict` reads
`set(runner.TESTS)`, so **position in the list is not asserted** and the only correct resolution is
to keep both lines.

### 2.1 · The integration preview, built rather than described

Branch `plan-integration-preview` — all six merged in the proposed order, the runner resolved by
union each time, then measured:

| Check | Result |
|---|---|
| every new suite enrolled exactly once | ✅ 4 of 4 |
| runner still parses; target count | ✅ 65 → **69** |
| the four new suites, run individually | ✅ all exit 0 |
| release battery | **4 red**, down from 6 on `main` |
| failures introduced | **0** |

The union resolver refuses a conflict in which either side *deleted* anything: union is the right
resolution for two independent additions and a destructive one for anything else, and that check
is in the tool rather than in a comment.

### 2.2 · 🔴 The integration found a defect neither candidate testing could

At the first integrated tip `test_release_surface` was **red**, though RELSURF fixes it and is
green alone. Cause: **`test_regenerate_adjudications_fails_closed.py` was committed `100644`** — a
shebang file with no executable bit, added by ADJFAILCLOSED.

**It was invisible on its own branch** because that guard was already red there for the four
pre-existing offenders, so a fifth was indistinguishable from the four. It became visible only once
RELSURF removed the other four.

⇒ **The guard's population grows with the work that repairs it.** Fixed in ADJFAILCLOSED, which
re-hashed; the re-integration is clean and the battery is 4.

**Proposed integration order** — it does not reduce the conflict count, which is fixed at four; it
puts the two guard-unblocking candidates first so every later merge is measured against a clean
guard rather than a noisy one:

```
1  RELSURF          clears test_release_surface + test_release_runner_verdict
2  GOVTESTS         pure durability; no tool edited
3  ADJFAILCLOSED    ) each conflicts on the runner; resolution is union, verified by
4  P7LEDGER         ) test_release_runner_verdict reading TESTS as a set
5  APQCONS          )
6  ORCHMAJOR2       different file entirely; always clean; last so the fingerprint
                    rotation lands once, after the executable work is settled
```

---

## 3 · The release baseline, classified

| Residual | Class | Owner | Minimum patch | Policy? |
|---|---|---|---|:--:|
| `test_release_surface` | `GIT_MODE_BIT` | Plan (3 under `governance/`) + framework | `chmod +x` ×4 | **no** — in RELSURF |
| `test_release_runner_verdict` | `MISSING_TEST_ENROLLMENT` | runner owner | one inventory line | **no** — in RELSURF |
| `test_documented_commands`, `test_fresh_clone_reader_journey` | `GENUINE_DOCUMENTATION_DEFECT` (instances) / `DISK_POPULATION_BUG` (class) | Plan (records) + guard owner | instances repaired; class needs code-span stripping | instance **no** · class **YES** |
| `test_locator_obligation_reaches_every_route` | `STALE_ROUTER_EXPECTATION` | router + guard owners | see § 3.1 | **YES** |
| `test_fulltext_trace_contract` | `STALE_ROUTER_EXPECTATION` | as above | as above | **YES** |
| `test_session_self_eval` | `STALE_ROUTER_EXPECTATION` | as above | as above | **YES** |
| `test_abstract_corpus_is_not_evidence` | 🔴 `UNKNOWN_NORMATIVE_HOME` | as above | see § 3.2 | **YES** |

All four router rows share one introducing commit — `04cbd3b`, 2026-08-16 — established with a
before/after control: every suite exits 0 at `04cbd3b~1` and 1 at `04cbd3b`, and a positive control
on the same run (`BATCH_COMMIT` 13 → 1) shows the file did not simply empty.

### 3.1 · `RULE_REACHABILITY` instead of `RULE_LITERAL_IN_CLAUDE_MD` — measured, not proposed

**The rules did not vanish. Only the router's copy did.** Measured, one hop from CLAUDE.md's own
link table (25 documents, 4 directories):

| Token | In CLAUDE.md | Carried by a normative surface | Reachable in one hop |
|---|:--:|---|:--:|
| `verbatim_locators` | ✗ | `framework/instruction/LEGEND_CORE.md` + two protocols | ✅ |
| `FULLTEXT_READ_RECEIPT` | ✗ | `LEGEND_CORE.md`, `gold_is_in_the_details.md` | ✅ |
| `session_self_evaluation.md` | ✗ | `LEGEND_CORE.md` | ✅ |
| `pubmed_corpus_harvest` | ✗ | **`AGENTS.md` only** | ❌ |

⇒ **Three of the four rules are already reachable.** A guard that followed the router's links would
pass on three today.

🔴 **And that change is semantic.** `assertIn(token, CLAUDE.md)` and *"a linked document carries the
token"* are different properties, and the second is weaker in a specific way: a link can rot, a
document can be renamed, and a two-hop chain can be introduced later. **Changing what a
`BLOCK`-severity guard accepts is not a test refactor.** Routed as a normative decision boundary.

**The minimum honest repair, if that boundary is crossed**, is a guard that requires *both* a link
from the router *and* the token in the linked file, with two mutation arms — remove the link, and
remove the rule from its home — because a pointer-following guard that only checks the pointer has
degenerated into a link checker.

### 3.2 · The fourth is a different problem and must not be bundled with the other three

`test_abstract_corpus_is_not_evidence` requires the token in **both** `CLAUDE.md` and `AGENTS.md`.
`AGENTS.md` passes. `CLAUDE.md` fails, and **`pubmed_corpus_harvest` appears in no file under
`framework/instruction/`, `framework/master/` or `framework/protocols/`.**

**`AGENTS.md` carries the rule in full** — a paragraph declaring the corpus `NOT_EVIDENCE`, naming
the permitted and forbidden uses. **And CLAUDE.md names `AGENTS.md` zero times.** (Control: it names
`BOOTSTRAP.md` twice.)

⇒ **A complete instruction surface exists that the router does not route to.** Reachability cannot
be satisfied for this rule until either the router links `AGENTS.md` — which is what a router is
for, and adds a route rather than a rule — or the corpus bound is given a home under
`framework/`.

**Not built.** Linking `AGENTS.md` changes no test outcome on its own, since all four guards are
literal; a candidate whose acceptance criteria cannot be demonstrated is a candidate that should
not be deposited. Same discipline applied to P7 § S6.

---

## 4 · ADJFAILCLOSED — the evidence is now a command

`adjudication_state_matrix.py`, in the `framework/scripts` directory of that candidate, builds the
sandbox, applies **one** mutation per state, and grades all 24. Pointed at two files it is both
arms of the mutation battery:

| Subject | States returning exit 0 on a degraded precondition |
|---|:--:|
| `main`'s original | **12** — S01 S02 S03 S04 S05 S06 S08 S09 S10 S11 S12 S20 |
| this candidate | **3** — S08 S12 S20 |

**Nine removed.** The three that remain are declared: a recipe legitimately declaring no manifest;
an empty `adjudicates` list whose summary says *0 of 0*; and a stale on-disk image, which is a
question about what `verify` is for rather than a counting defect.

**Why a command and not the table it replaces.** A table of exit codes copied into a document is a
measurement that decays in silence — the script changes, the table does not, and the first reader
to trust it reads last month's behaviour.

**Two harness failures are designed against, because both happened and both produced a confident
wrong answer rather than an error:** a pristine tree *derived* from the sandbox path copied the
original over the patched subject, so the two arms agreed perfectly; and dependencies *globbed*
beside a lone candidate copy made both arms die identically at import. The pristine tree and the
dependency directory are now named, and the sandbox is probed before any case runs.

| | |
|---|---|
| `FAIL_OPEN_STATES_ORIGINAL` | 12 |
| `FAIL_CLOSED_STATES_REPAIRED` | 9 flipped; 3 remain by declaration |
| `INDISTINGUISHABLE_FALSE_GREENS_REMOVED` | 9 |
| `LEGACY_TESTS_PRESERVED` | 12 of 12, via a 4-line change at the call sites |

---

## 5 · The corpus-conditional gate — decision surface, nothing implemented

**The premise is not negotiable and is not a tooling gap.** Rule 5e publishes the recipe *because*
the reproduction may not be redistributed. **Zero files under `files/` are tracked on `main`**, and
`verify` in a fresh worktree exits 1 on all three studies, for both the original and the repaired
script. A gate whose inputs the repository is forbidden to ship cannot run where the repository is.

| Layer | What it can certify | Runs where |
|---|---|---|
| **PUBLIC_CI** | that the *checker* fails closed — the 24-state matrix and the 14 subprocess tests need no corpus, they build a one-page PDF | every clone |
| **PRIVATE_CORPUS_VALIDATION** | that the *recipes* still regenerate — digests match, needles resolve, crops contain their spans | only where the PDFs are |

**Three questions, and the third is the one with no clean answer yet.**

1. *What can CI verify without `files/`?* **That the gate is a gate.** Every degraded state, every
   fail-closed path, the whole of `run()`. Built and enrolled in ADJFAILCLOSED.
2. *What must be certified only in a corpus workspace?* The digest and geometry checks over the
   real recipes — three studies today, and rule 5e says *"33 of 51 local PDFs will eventually need
   adjudicating"*.
3. *🔴 What durable receipt could attest (2) without redistributing the corpus?* **The repository
   already has the shape**: `fulltext_receipts.py` records a hash-chained receipt naming a source
   fingerprint it does not ship. An adjudication receipt would carry the same: run time, tool
   digest, recipe digest, per-artifact verdict, and the source-PDF SHA-256 already in the recipe.

**And the failure mode that must be designed for, not assumed away:** *how do you fail if the
pipeline claims a private verification that never happened?* **You cannot, by arithmetic alone.**
A self-declared receipt attests its author's honesty. What the repository already does elsewhere is
narrow the claim rather than inflate the mechanism — the receipts ledger states its own residual:
*"an editor who rewrites the ledger and the manifest anchor in the same breath is not caught by
arithmetic… the integrity claim degrades to 'visible in review', never to 'invisible'."*

⇒ **The honest transition is not `MANUAL_TOOL → ENFORCED_CHECK`.** It is:

```
UNTESTED_MANUAL_TOOL  →  TESTED_MANUAL_TOOL          (done, in CI, no corpus needed)
                      +  CORPUS_CONDITIONAL_GATE      (a declared skip with a reason, in CI)
                      +  ADJUDICATION_RECEIPT         (durable, chained, attests-not-proves)
```

The first is built. The second is one runner target away and needs a decision about whether a skip
counts. **The third is a new record type in a hash-chained ledger, and Plan does not introduce a
record type inside a work record.** Decision surface, not a proposal.

---

## 6 · The candidates

`BASE_HEAD 788c357d` for all six. Every hash reproduced twice.

| Candidate | Branch | Tip | `CANDIDATE_CONTENT_HASH` |
|---|---|---|---|
| ORCHMAJOR2 | `plan-major2-restricted-repair` | `5e3a757` | `9f852385…6919389f` |
| ADJFAILCLOSED | `plan-adjudication-failclosed-repair` | `dc0d5d9` | `12f454be…ecc055df` |
| RELSURF | `plan-release-surface-repair` | `bf9c807` | `541a2631…0a7feb9e` |
| APQCONS | `plan-approval-queue-consolidator` | `76c8e3c` | `76afbf85…20f499701` |
| P7LEDGER | `plan-p7-event-ledger` | `cb9bec2` | `17ead426…c8ba949c` |
| **GOVTESTS** *(new)* | `plan-governance-test-durability` | `c1294fd` | `16a20ba4…887d84095` |

**GOVTESTS closes the durability gap without importing 65 commits.** Both suites live on
`plan-exec-repair-prep` alone. The two tools are **byte-identical** on `main` and there, so the
suites run against `main`'s code unchanged: **22 + 27 tests green, 8 of 8 mutation arms caught, 0
survived, 0 stale anchors.** The battery is committed rather than described, and a stale anchor is
counted separately and never as a catch — an arm whose anchor no longer matches never introduced
its defect, so the suite was never asked anything.

---

## 7 · APQCONS under hostile input — five defects, all real

Nine adversarial cases. **Five found a defect**; all nine are now tests, 16 → 27.

| Case | Before | After |
|---|---|---|
| 🔴 non-string timestamp | `20260817` → `""`, which sorts **before every real date**: the record was emitted at **position 1** | `SourceError` |
| 🔴 lineage contradicting **itself** | *"Two lineages disagree"*, printing `differs between L2 and L2` | `SourceError`, distinct from a conflict |
| 🔴 non-object record | `AttributeError` crash | `SourceError` |
| 🔴 lineages sharing no record | united in silence | united **and warned** |
| exact duplicate within a lineage | collapsed correctly, untested | tested |
| unknown `STATE`, unexpected field | carried through | tested — this tool unites records, it does not police a vocabulary it does not own |
| same-day tie ordering | file order | tested, **and asserted not to equal id order** |

**The timestamp one is the worst and is the one the prompt asked about.** The tool was not ordering
by time; it was **ordering by whether it could parse the time**, and saying nothing. A record whose
date was unreadable was presented as the oldest.

**`SourceError` vs `ConflictError` is operational, not stylistic.** A conflict means two lineages
disagree and only a human can choose. A source error means one file is malformed or contradicts
itself and there is nothing to choose between — **routing that to an operator is asking them to
adjudicate a typo.** Exit 2 rather than 1.

⇒ **Readiness frozen.** 27 tests, the real three lineages still consolidate 30 → 18 with 12 deduped
and 0 conflicts.

---

## 8 · Scientific candidates — the floor is derivable for none of them

**31 candidates on `lettore`**, 14 dated 2026-08-26 (two more than yesterday).

| | Count |
|---|:--:|
| `DECLARED_CLASS_MACHINE_READABLE` | **0 of 31** |
| `DECLARED_CLASS_PROSE_ONLY` | 11 |
| prose present but unparseable | 2 |
| `NO_CLASS` | 18 |
| carrying YAML frontmatter of any kind | **0 of 31** |

**Reviewer floor derivable without reading free prose: 0 of 31.**

🔴 **And the trend is the opposite of a regression, which changes what should be proposed.**

| Era | Candidates | Declaration |
|---|:--:|---|
| 2026-08-10 · 08-11 · 08-14 · 08-25 | 17 | **`NO_CLASS`, all of them** |
| **2026-08-26** | 14 | **13 declare a class**, in prose |

Scientist A's practice moved from *no declaration* to *a declaration a human can read*. It stalls
one step short of a machine. **This is an improvement that has not reached the parser, not a
lapse**, and a proposal framed as a correction would be both unfair and less likely to be adopted.

**Four candidates carry a MAJOR** — `CLAIM037-01`, `SEIZURE-RECONCILIATION-01`,
`DOSE-ADJUDICATION-01`, and `CROSS-CLAIM-CENSUS-01` (declared MIXED with a MAJOR inside). Each
implies Mirror PASS **+** `HUMAN_APPROVAL`. **No gate can derive that today**, because the value
exists only as bolded English inside a heading.

**Minimal metadata proposal — recorded, not introduced as a requirement.** Four keys, all of which
the 2026-08-26 candidates already state in prose:

```
change_class:      MAJOR | MINOR | PATCH | NONE | MIXED
claims_touched:    [CLAIM 003, …]
baseline_effect:   REVERSAL | NARROWING | CORROBORATION | NONE
locator_audit:     REQUIRED | NOT_REQUIRED
```

⇒ **Requiring frontmatter changes what a commit candidate must contain**, which is a governance
change and is not Plan's to make inside a work record. Routed.

---

## 9 · P7 — the anchor semantics S6 and S7 depend on

Seven states stressed against S1–S5. **No event was emitted; the two frontier tests still pass.**

| State | Chain | Anchor |
|---|---|---|
| tail mutation (edit the last line) | **clean** — misses it | **catches** |
| truncation | **clean** — misses it | **catches** |
| duplicate `EVENT_ID` | refused by the writer | — |
| broken chain mid-file | broken; writer refuses to extend | — |
| missing anchor (`{}`) | — | **fails closed** |
| two writers from one snapshot | **broken** — detected after the fact | — |
| append over an edited tail | re-seals **clean** | **still catches** |

**Three findings that bound what S6/S7 need:**

**9.1 — The anchor detects divergence, never its direction or its legitimacy.** A legitimate append
against a stale anchor and a truncation against the same anchor produce the *same* message class:

```
legitimate append : anchor says 3 event(s), ledger holds 4: truncated or appended outside the writer
truncation        : anchor says 3 event(s), ledger holds 2: truncated or appended outside the writer
```

⇒ **The anchor must be updated by the same operation that appends**, or every legitimate write
raises a false alarm and the alarm is trained out of the reader.

**9.2 — The empty ledger must be anchored at zero, explicitly.** `verify_anchor([], {})` fails and
`verify_anchor([], anchor([]))` passes. So *"no anchor yet"* and *"the anchor was lost"* are
indistinguishable unless the anchor is written at creation.

**9.3 — One writer per file is a property of the layout, not of a lock.** Two appends chained to
the same snapshot break the chain, and the break is only visible afterwards. Option (a) gives one
*file* per actor; it gives one *writer* only if one process per actor. **That assumption is
currently undeclared** and belongs in § P7 before emission, not after.

### Minimum anchor semantics required before S6/S7

```
1  the anchor is written when the ledger is created, as {events: 0, head: null}
2  it is updated by the same call that appends — never separately, or it lags by design
3  it lives OUTSIDE the ledger file; the state manifest already hosts the receipts ledger's
4  `verify` consults it; today `verify` checks only the chain
5  divergence is reported as divergence, without asserting a direction
6  "one writer" is declared to mean one PROCESS per actor, not one file per actor
```

🔴 **Residual, stated rather than engineered away:** 2 and 3 cannot both be atomic — two files
cannot be written in one operation. An append that succeeds while the anchor update fails leaves a
false alarm. **This is the same residual `fulltext_receipts.py` already names for itself**, and the
correct response is the one it already gives: state the limit, and let the claim degrade to
*visible in review* rather than to *invisible*.

**S6 remains unapplied**, for the reason given when it was deferred: until S7 there are zero events,
so the check has one possible output on every ref, and it would add that line to `legend_lint.py` —
the gate this work has already shown cannot fail on governance paths.

---

## 10 · Reproduction

```bash
python3 governance/scripts/candidate_content_hash.py --base 788c357d9b7ca7afcbe7c1efc3a06b426cf7e2d5 --tip <branch>
git diff --shortstat main <branch>
git log --oneline main..plan-integration-preview          # 15 commits, six candidates merged
python3 scripts/run_release_regressions.py                # 6 red on main, 4 at the preview tip
```

The state matrix, the mutation battery and the hostile probes are **committed inside their
candidates**, not described here. The integration simulator and the union resolver are in this
session's scratchpad and are **not durable** — they should travel with the integration if it is
performed, which is the same defect this record's § 4 is about.
