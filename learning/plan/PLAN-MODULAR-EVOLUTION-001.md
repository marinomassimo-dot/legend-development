---
artifact: PLAN-MODULAR-EVOLUTION-001 — measurement report on deletion candidates, retro-classification, actor context, guarantees, loop primitives and coupling
record_id: PLAN-MODULAR-EVOLUTION-001
task_id: PLAN_MODULAR_EVOLUTION_v1
author: plan
authored_on: 2026-09-02
dispatcher: operator
governance_version: 3.1.1 (read, not exercised)
mode: ANALYSIS_ONLY
STATUS: READ_ONLY_MEASUREMENT · ACTIVATION: NOT_REQUESTED · APPROVAL: NOT_GRANTED · AUTHORITY_CLAIMED: none
canonical_effect: NONE
impact_authority: NONE
classification:
  - MEASUREMENT REPORT · NOT A TRANSFER · NOT A GOVERNANCE DECISION · NO NEW VOCABULARY
  - NO NEW IDENTIFIER FAMILY — `TOPIC-NNN` under `learning/`, the existing ANALYSIS_ONLY shape
provenance:
  - RECOVERED FROM A SESSION TRANSCRIPT, NOT FROM THE REPOSITORY. This report was authored on
    2026-09-02T18:16:36Z and was never written to the tree; its own Orchestrator attestation
    below records that decision and the reason for it. It is persisted here verbatim on
    2026-09-03 by operator instruction.
  - source — assistant message uuid `fc491df7`, session `5b4dddaa-46ad-4381-82e1-947d3b48151e`
  - body sha256 `f5b7559bddb8b767c040c6f8ee92e5a3d16368165b43487933ba0bfd6fd433de` · 270 lines · 35 780 characters
  - the body begins at the next line and is unedited, including its opening conversational line
---

Both actors returned. Assembling the single report.

---

# PLAN-MODULAR-EVOLUTION-001 — MEASUREMENT REPORT

```
record_id        PLAN-MODULAR-EVOLUTION-001        (existing ANALYSIS_ONLY family; no new identifier family)
mode             ANALYSIS_ONLY   change_class NONE   authority_granted NONE
baseline         b1b5a581b9b1af85dd4de8a05212433e0aab21a2
BASELINE_SURFACE BOTH — main is remote-equivalent (local == tracking == live ls-remote);
                 the local ref population is NOT (89 heads vs 38 published; +14 codex, 2 pii-backup,
                 3 preserved, 1 stash, 7 tags = 159 refs). Ref-population measurements are LOCAL.
environments     root worktree; git-archive HEAD extraction (686 files); no writes anywhere
actors           Orchestrator (coordination, M3, M7, M8) · Plan (M1, M2, M5, M6) · Mirror (M4, M9)
date             2026-09-02
```

**Convergence caveat.** Plan and Mirror overlap on several instruments. Where both report a figure I state it once and name who measured it; agreement between two actors reading the same file is not a second measurement.

---

## M1 — DELETION / DE-NORMATIVIZATION CANDIDATES

| # | Object | Trigger | Evidence | ST | Guarantee carried | Replacement | Breaks if removed | Disp |
|---|---|---|---|---|---|---|---|---|
| 1 | GATE 0 lease-ACTIVE singleton | every BATCH_COMMIT | `GOVERNANCE_v3.1.1.md:238`; `lease_state.py --check` → ACTIVE=0; **216 commits since last expiry** | C | one writer at batch time | executable GATE-0 script | nothing — unenforced for 216 commits | SIMPLIFY |
| 2 | Stored `STATUS:` on lease | any read | `lease_state.py:9-13`; `runtime/orchestrator_lease.md:24` "never authoritative"; #3 stored EXPIRED vs derived STALE | C | none (derived value stored w/o recipe) | the derivation | nothing | **DELETE** |
| 3 | `ANNEX_INDEX.md` MAT-002 SHA table | reader | `:28-31` self-declares "never a number copied from this table" | C | audit only | `governance_fingerprint.py` | nothing | DE-NORM |
| 4 | `HUMAN_APPROVAL_QUEUE.jsonl` | every HUMAN_REQUIRED | 3 divergent blobs: `20c24a2b` 6 lines / `bb603d9a` 10 / `95fc8163` 14; 2 of 6 null-keyed | C | approval provenance | one writer + derived view | already broken | SIMPLIFY |
| 5 | `governance/decisions/` as class | operator determinations | 5 records; `main` carries 3 of 5 | C | record of human decision | one J.1 event | split already breaks it | SIMPLIFY→event |
| 6 | Runtime/Agent-Card registry (§43, I.4) | rehydration | `runtime/` = 1 path on main, 9 on `orchestrator` | C | capability verification | `execution_attestation.py` | unreachable (0 VERIFIED) | DECOUPLE |
| 7 | `CANDIDATE_CONTENT_HASH` re-binding | GATE 5 | ORCHSURF rebound twice for a redaction (SLR-plan-0014) | C | approval binds exact content | — | approvals transplantable | **KEEP** |
| 8 | Mirror hostile review per revision | every MAJOR | 34 `REV-*` ids; SCIAB 6 rounds, ORCHSURF 8 | C | adversarial check | sampled audit at R0/R1 | nothing at T0/T1 | DE-NORM for T0/T1 |
| 9 | §40 first-commit reconciliation | before new PMIDs | `fulltext_receipts verify` OK 128; `growth_anchors` PASS | C | ledger authoritative | already automated | nothing | DELETE prose step |
| 10 | `cross_host_handoff.md` counts | quoted as ref state | file says "POPULATION-DERIVED and decay… do not quote as current" | C | none | `legend_handoff.py classify` | nothing | DE-NORM |
| 11 | `controlled_benchmark_ab.md` (748 ln, `normative: yes`) | BENCH-AB-001 | frontmatter `PROPOSED`; manifest `NOT FROZEN`; benchmark never run | C | blinding of an unrun experiment | keep as template | nothing | DE-NORM→template |
| 12 | `PREP-*`/`HANDOFF-*`/`DELTA-*`/`ADVISORY-*` (10 files, 2 262 ln) | cited by candidates | candidates census | C | none — routing | nothing | nothing | DE-NORM |
| 13 | `CLAUDE.md` as guarantee carrier | 5 suites assert obligations live there | 5 suites currently red: locator-obligation, abstract-corpus, fulltext-trace ×2, session-self-eval — all "not found in CLAUDE.md" | C | obligation reachability | assert against the normative file | 5 red suites — already broken | DECOUPLE |
| 14 | `ledger/checkpoints/` refuse-to-resume | rehydration | 19/19 Plan checkpoints | C | no resume under changed governance | — | resume safety | KEEP + extend recovery |
| 15 | `backup/` snapshot trees (33 files) | GATE 4 | 4 `refs/tags/snapshot/pre-CAND-*` serve the same purpose | C | rollback point | the tags | nothing (duplicate) | **DELETE** |

*Positive control for the duplicate-registry sweep:* `CANDIDATE_CONTENT_HASH` = 76 files, single well-defined instance; rows 4/5/6/15 are the only ones with ≥2 divergent instances.

**Case A — `refs/pii-backup` + `refs/codex` cleanup.** ACTUAL: **0 refs deleted, 0 pushed** — it was a *classification*, not a cleanup. 7 commits, 4 251 insertions, of which durable = 2 455 lines (`legend_handoff.py` 1 441 + tests 722 + protocol 277 + adjudication ledger 15). 0 formal `REV-*`; **3 self-correction rounds** visible in commit subjects, all on the same population question (`334b564` "I had quoted one for the other"; `b1b5a58` "counts are re-derived at the commit that carries them"). **14 Operator touchpoints** (`TRUE_HUMAN_REQUIRED` rows). Intrinsic **T0/T1, R0** (R2 latent and unrealised: the bundle is unencrypted and carries pii-backup, `cross_host_handoff.md:193`, but no transfer executed). HYPOTHESIZED under T1/R1: 1–2 commits, 2 163 lines tool+tests, protocol prose explanatory (−277 normative), **0 blocking** touchpoints, and the escalation eliminated by deriving the population inside the tool.

**Case B — ORCHSURF.** ACTUAL content delta: **3 files, +407/−49** (ORCHWT: **1 file, +24/−1**). Process artefacts: candidate 1 149 + handoff 238 + PREP 963 + two DEC 596 + author responses 356 + SLR 507 = **3 809 lines**. **Ratio 8.4 : 1 process-to-content.** 46 commits across refs, 4 revisions (1–3 in the inverted direction), **8 `REV-ORCHSURF-*` ids**, **≥4 Operator touchpoints**. Intrinsic **T1/R1** — `scope_negative` declares no routing/resolver/annex touched; it *types four concepts* that were one word. What made it T3-shaped: the operator's architectural intent existed in **no repository object**; `DEC-20260820` is explicitly a CONFIRMATION that "amends nothing". HYPOTHESIZED: 1 commit, ≤60 lines, 1 sampled audit, **1** touchpoint stated up front.

---

## M2 — RETRO-CLASSIFICATION AND OBSERVABILITY ESCALATION

Denominators: **TOTAL_CYCLES 21** (closed/frozen cycles with a durable artefact); **INTRINSIC_T0_T1 = 15**; 34 distinct `REV-*` ids.

| # | Cycle | T | R | Actual process | Observability escalation | OP |
|---|---|:-:|:-:|---|---|:-:|
| 1 | GOV311 | T3 | R2 | MAJOR·3 REV·483 ln·+353 | `APR-…-002` is a *question* not an approval: the gate could not be evaluated | 2 |
| 2 | HASHDET | T1 | R0 | MAJOR·2 REV·270 | candidate identity not a function of the tree; `$(…)` stripped a newline → 2 hashes 1 tree | 1 |
| 3 | ORCHWT | T1 | R1 | MAJOR·3 REV·364·adoption required | §8 "chat associated with REPO_ROOT" undecidable session-vs-filesystem | 1 |
| 4 | P51C9 | T2 | R2 | MAJOR·2 REV·rev3 = re-baseline, **no content change** | manifest inside the tree it hashes = fixed point; found by review | 1 |
| 5 | SUNSET-DEC3 | T1 | R1 | MAJOR·2 REV | lease STATUS stored w/o recipe; record read ACTIVE 29 s after its EXPIRES_AT | 1 |
| 6 | SCIAB | T2 | R1 | MAJOR·**6 REV**·1 736 ln·5 superseded hashes | CONFIGURED≠PROVEN: 0 VERIFIED capabilities anywhere | 2 |
| 7 | **ORCHSURF** | **T1** | R1 | MAJOR·**8 REV**·4 rev·3 809 ln process : 456 content | operator intent in no object; 3 revisions inverted | 4 |
| 8 | XPORT | T2 | R1 | MAJOR·2 REV·925 | "the review package travels as a file, because the transport is the unresolved thing" | 1 |
| 9 | P5DOMAIN | T3 | R2 | MAJOR·1 REV·497 | P5.1's load-bearing sentence falsified by `325da04` in another file — "nothing connected the two" | 1 |
| 10 | C9-STATE-MODEL | T0 | R0 | 710 ln·advisory·REV·operator **hold** | "how LEGEND represents state" is itself the unobservable | 1 |
| 11 | ROLE-CONTRACTS | T0 | R0 | 667·REV·response·**DEC STATE_DETERMINATION** 362 | operator had to *determine a fact*: whether existing records constitute activation | 1 |
| 12 | SURFACE-MAP | T0 | R0 | **1 522 ln, 0 state change** | the record *is* the escalation; same question analysed **7× on 7 refs, 0 on main** | 1 |
| 13 | GAP-MAP | T0 | R0 | **1 612 ln, 0 state change** | 7 of 17 gaps "are not fixed by building anything" | 0 |
| 14 | RTBRIDGE r7 | T3 | R1 | MAJOR·734 — reverses what a safety control does on malformed input | — | 1 |
| 15 | RTBRIDGE8 | T1 | R0 | 633 ln, new branch+candidate | ACTOR≠RUNTIME≠SESSION≠WORKTREE≠AUTHORITY collapse | 0 |
| 16 | RTBRIDGE9 | T1 | R0 | 623 | confinement unit undecidable from runtime facts | 0 |
| 17 | RTBRIDGE10 | T1 | R0 | **1 463**·60-item must-refuse set | code-mode `exec` invisible to a matcher list — 20/20 calls unseen | 0 |
| 18 | RTBRIDGE11 | T1 | R0 | **1 303**·96 tests·32-cell | "FROZEN, awaiting a hostile review that has not been opened" | 0 |
| 19 | RTBRIDGE12 | T1 | R0 | 646 | "inherited mid-flight working tree, not a freeze" — a resume is not a start | 0 |
| 20 | RTBRIDGE13 | T1 | R0 | 931·integrated **114 files / 58 685 ins** | 3 FROZEN candidates, 0 reviews opened | 0 |
| 21 | refs/handoff | T0/T1 | R0 (R2 latent) | 7 commits·4 251 ins·0 refs moved | "the refs a push does not carry are the state" | 14 |

```
T3_PROCESS_COST_PAID / INTRINSIC_T0_T1_CYCLES  = 12 / 15 = 80 %
   denom 15 = rows 2,3,5,7,10,11,12,13,15,16,17,18,19,20,21
   num   12 = ran the full GATE-3-shaped apparatus (manifest + hash binding + hostile-review
              package and/or an operator determination): 2,3,5,7,10,11,15,16,17,18,19,20
   excluded 3 = rows 12,13 (analyses, no binding requested) and 21 (no REV id opened)
C2_OBSERVABILITY_ESCALATED_CYCLES / TOTAL_CYCLES = 21 / 21 = 100 %
   conservative (excluding rows 2,14 as intrinsic engineering) = 19 / 21 = 90.5 %
```

**Separation achieved:** C1 and C2 are not the same quantity. C1 (process escalation) is 80 % of intrinsically-cheap cycles. C2 (observability) is 90.5–100 % of *all* cycles including the correctly-T3 ones — i.e. **C2 is the larger and more general cause, and it inflates T3 cycles too.**

---

## M3 — ACTOR CONTEXT MANIFEST *(Orchestrator measured)*

| path | actors | load mechanism | always/cond | ST |
|---|---|---|---|---|
| `framework/state/state_manifest_current.md` | all | ROUTER_CHAIN `runtime_parity.py:99-106`; CLAUDE.md §0 "first, every session" | always | C |
| `CLAUDE.md` | all | harness project-instruction load | always | C |
| `AGENTS.md` | Codex-side | router parity | always | C |
| `BOOTSTRAP.md`, `governance/ANNEX_INDEX.md`, `framework/protocols/index.md` | all | ROUTER_CHAIN | always | C |
| `roles/{orchestrator,plan,mirror,scientist}.md` | 1 each | `ROLE_CONTRACTS` map `runtime_parity.py:108` | per-actor | C (all `status: PROPOSED`) |
| 21 × `.claude/skills/*/SKILL.md` | Scientist, Orch | CLAUDE.md §2 trigger table; skill activation | conditional | C |
| 5 × `.claude/agents/*.md` | dispatcher | Agent tool | conditional | C |
| 4 scientific `*_current.md` (+`meta_index`) | Scientist, Mirror | `legend-start` SKILL.md:11,23 | session start | C |
| 20 × `*_current.md` total | varies | wikilink traversal | conditional | C |
| 64 deepdive manifests, 128 receipts | Scientist | task dispatch | conditional | C |

🔴 **Nothing mechanically enumerates this.** `git grep -lniE "context.manifest|actor.context"` → **0 hits**. H-E's proposed T2 floor therefore has **no existing measured basis**; the manifest above is derived, not read from an object. `LABEL = NEW` for the enumeration itself — and every option to its left fails only because there is nothing to delete, relax, decouple or parametrize: the object does not exist.

---

## M4 — GUARANTEE INVENTORY *(Mirror led; Orchestrator re-ran G2 and G7)*

Classes: **CODE** enforcement · **GATE** wired into CI/blocking · **TEST** suite · **REVIEW** review-only · **NARR** narrative.

| G | Strongest carrier | Class | ST | Note |
|---|---|---|---|---|
| G1 provenance | `fulltext_receipts.py` hash chain + tail anchor + flock; `corpus_firewall.py` | CODE+GATE | C | strong. `locator_audit.py`/`dossier_quote_audit.py` explicitly **"not a gate, deliberately not blocking"** |
| G2 epistemic typing | DATO/INFERENZA/IPOTESI/ESPANSIONE | **NARR only** | C | 🔴 **no enforcement — reproduced below** |
| G3 evidence→claim | wikilink LINT, BLOCK_BATCH_COMMIT; mirror-completeness | CODE+GATE | C | strong |
| G4 producer≠verifier | GATE 1 prose; `locator_audit.py` blind auditor; `independent_privacy_scan.py` | NARR+REVIEW | C/DEV | 🔴 the independent implementation is **wired to nothing** |
| G5 canonical state unique | `legend_lint.CURRENTS` (4 paths), missing ⇒ BLOCK_SYSTEM | CODE+GATE | C | identifiable ✓, **sufficient ✗** — the 4 moved in 9 of 634 commits |
| G6 authority explicit | `guard_policy.py` DENY_REF/DENY_NETWORK; `effect_model.py:390` PUBLISH "never granted by a runtime, role or lease" | CODE+GATE | C | 🔴 the **only** mechanically enforced human boundary is the shell guard's |
| G7 privacy | layering (repo composition) + `public_release_gate.py` CI | NARR+GATE | C | 🔴 **no encryption anywhere** — see below |
| G8 fail-closed | severity ladder worst-wins; `INTEGRITY_CHECK_UNAVAILABLE` ⇒ explicit block | CODE+GATE | C | `run_release_regressions` **currently FAIL** |
| G9 disagreement observable | §27 `DISAGREEMENT_UNRESOLVED`; claim state `conflicting evidence` | NARR + 1 enum | C | 🔴 21 lines / 15 files, **0 in code**; no artifact (`git ls-files \| grep -i disagree` = 0) |

**G2 — reproduced by the Orchestrator on the tracked extraction, positive control in the same table:**

| Cell | Mutation | `legend_lint` |
|---|---|---|
| 0 | baseline | PASS |
| A | `**Type:** DATO` → `BANANA_NOT_AN_EPISTEMIC_LEVEL` | **PASS** |
| A2 | `**Type:**` line deleted | **PASS** |
| B | *positive control* `**Status:**` → `BANANA` | **BLOCK_BATCH_COMMIT** `INVALID_STATUS` |

Claim **status** is enforced; claim **epistemic type** is not. One claim already reads free-text `DATO + INFERENZA prudente`.

**G7 — measured, not assumed.** Sweep `LUKS|encrypt|VeraCrypt|dm-crypt` over the tracked tree = **1 hit, and it is a negative**: `cross_host_handoff.md:193` "The bundle is unencrypted. It carries `refs/pii-backup/*`." Any model treating LUKS/overlay/topology as the carrier measures an object this repository does not have.

**G4/G7 disagreement — Orchestrator re-measured on the identical `git archive HEAD` tree (686 files):** `public_release_gate --mode release` → **1 BLOCK**; `independent_privacy_scan` → **17 BLOCKs** (5 ITALIAN_CITY, 4 PRIVATE_NAME, 4 CALENDAR_DATE, 3 EMAIL, 1 ITALIAN_HOSPITAL). The second appears in `.github/` and in `public_release_gate.py` **zero times** — only in governance candidates. *Caveat:* the gate reports 0 in the working tree and 1 on the extraction; the extraction adds one failure, so the honest statement is **1 vs 17 on the extraction**, not 0 vs 17.

**M4(a) guarantees in FROZEN surfaces absent from G1–G9 (12 found; a10 binds the model under test):** a1 losslessness · a2 no-rebuild-from-chat-memory · a3 *gold is in the details* (no tier authorizes not reading; 351 catalogued-only, `unread_premises=4`) · a4 retrieval ≠ reading · a5 not-medical-advice (has executable carriers) · a6 biomarker tier separation · a7 `DEFAULT_EXTERNAL_SPEND=0` · a8 ONE_WRITER · a9 no permanent PROVISIONAL · **a10 vocabulary honesty** (`GOVERNANCE_v3.1.1.md:40`, `annex_j:23-36` J.0 — forbids importing words like *atomic/singleton* that make an unmeasured property sound guaranteed, and mandates `GUARANTEE_PROVIDED / FAILURE_MODE_STILL_POSSIBLE / DETECTION / RECOVERY`) · a11 licence/redistribution · a12 freeze scope.

> a10 applies directly: **H-C's "mechanically derived R" and H-B's "guarantee-equivalent" are themselves guarantee claims** and would each need a G/F/D/R declaration before any LEGEND document could use the phrasing.

**M4(b) not locatable as executable objects:** G4, G9, G2-on-claims. G6's runtime half is `PROPOSED` with 0 ACTIVE leases; **the P7 event ledger has no writer** (`ANNEX_INDEX.md:64`), and `roles/mirror.md:74` already records its own analysis surface as blocked for that reason.

**M4(c) §11 — history-immutability scope: BOTH, by two unrelated mechanisms, and the distinction the hypothesis asks about is DECLARED NOWHERE.** Scientific reading history: per-event hash chain + external tail anchor, truncation ⇒ BLOCK_SYSTEM, rationale *evidence integrity*. Git plumbing: `REF_WRITE`/`PUBLISH` rungs, "which no runtime, role or lease grants" — rationale **concurrency**, not scientific history ("other actors share this object store… untracked files are where their in-flight work lives"). Sweeps: `force-push` 0 files; `force push` 4, all in non-normative candidates; `git history` 6, none normative. So plumbing *already* inherits operator-only semantics — for a reason that **would stop holding in a single-actor deployment**, at which point plumbing silently drops to unprotected while the receipt ledger stays protected. **UNCLEAR in text; BOTH in effect; non-overlapping reasons.**

---

## M5 — LOOP PRIMITIVE MAPPING *(Plan measured; 89-head sweeps, controls: `REVIVAL_TRIGGER` 88/89, `HYP-` 88/89)*

| Primitive | Verdict | Existing object | Cost |
|---|---|---|---|
| Hypothesis state | **EXTEND — not in the claim registry** | `therapeutic_hypotheses_ledger_current.md`, 16 `HYP-*`, 7 states. L1/L2/L3 is an **orthogonal axis** (`Type:`), claim status a third — **no overloading occurs**; the registry simply has no hypothesis edge | 1 file / ~40 ln / **0 new objects** |
| Dismissal weakened+reason+reopen | EXISTS (prose) / EXTEND (machine-readable) | `dismissal_ledger_current.md`, 17 entries, premise + `PREMISE_TAG` + verdict + `REVIVAL_TRIGGER` + outcome. 🔴 `weakened` absent as a state; outcomes are prose | 1 file / ~25 ln / 0 |
| P7 `BELIEF_UPDATE` event | 🔴 **UNVERIFIED — the ledger does not exist** | §P7 fixes the design and says "not yet built"; `ledger/events` **0 hits on 89 heads**; `BELIEF_UPDATE` 0 hits. Reuse target named and executable: `fulltext_receipts.py` | as NEW: 1 script / ~400 ln / 2 new objects |
| Prospective commitment | **NEW** | Nearest shapes exist but for other subjects: `PROV-*` (`HYPOTHESIS/EVIDENCE_EXPECTED/SUCCESS_CRITERION/FAILURE_CRITERION`) for *practices*; `execution_receipt.py` `predicted/authorized/observed` for *commands*. **None of 5 tasks, 19 checkpoints, 128 receipts, 64 manifests has a "what would discriminate" slot** — so ADAPTER has no target. Left-of-NEW options fail for stated reasons | ADAPTER over `PROV-*`: 1 schema / ~30 ln / 1 record class |
| `targets_hypotheses` on tasks | EXTEND | 0 hits/89; carriers exist (`ledger/tasks/plan/*.json`, `batch_queue.md` generated) | 2 files / ~20 ln / 0 |
| Verifier procedure metadata | EXTEND (partial); 5 of 7 attributes **UNVERIFIED** | `deepdive_manifests/*.json` already separate **procedure** (`skills_considered`, routes, `enumeration_method`) from **source** (`source_artifacts[].sha256`). `known_bias`/`validated_domain`/`procedure_metadata` = 0 hits/89; cost/latency/fidelity/independence have no field | 2 files / ~50 ln / 0 |
| Independence check (shared PMID/dataset/model) | EXTEND | `trace_claim_foundation.py` already walks the graph and refuses prose; `build_evidence_index.py` derives a cross-paper index. **The species-drift detector is proof the join works** — it caught a rat→mouse conversion across 2 citation hops | 1 file / ~120 ln / 0 |
| **§18 campaign/harness epoch** | **EXTEND** | Two partial carriers: `sync_epochs.jsonl` (`previous_commit→current_commit`, `invalidates_active_work`, hash-chained — a genuine change point, 1 row) and `BENCH-AB-001/benchmark_manifest.json` (`BASE_HEAD`, `PROTOCOL{sha256}`, `INSTRUCTIONS_VERSION`, `SCHEMA_VERSION`, frozen population, `surface_tree_sha256`). Strategy ✓ verifier ✓ retrieval/context ✓ scoring ✓. 🔴 **model/provider absent** (1 hit, a disclaimer) — but `execution_attestation.py` already DERIVES `runtime`/`runtime_version` ⇒ **ADAPTER not NEW** | 1 schema / ~35 ln / 0 new objects |

**Loop-closure, measured:** hypothesis references in deepdive manifests **0/64**; in the claim registry **0/39**; in the receipt schema **0 fields**. `working_model_current.md` changelog is the closest existing BELIEF_UPDATE — 8 `BATCH_*` records naming PMIDs, receipt ids, claims moved, and an explicit "no baseline reversal" clause — but transitions are **per batch, 1:N** (`BATCH_20260806_002` moves 4 claims from 3 papers), violating "exactly one identifiable observation". Reverse edge exists one-directionally (hypotheses→discovery 31; hypotheses→claims 0). **Net: the loop is open at the hypothesis boundary and closed at the claim boundary. The missing primitive is one typed edge, not an architecture.**

---

## M6 — COUPLING MAP *(truncated per §28 priority — full table in Plan's measurement)*

`sci_equiv`, `IMPACT_FLOOR`, `ENGINEERING_LANE`, `de-pin`, `H-J` all return **0 hits**: the incisions are exogenous.

**I2** — the Annex C floor ladder has **no executable form**, and with 0 ACTIVE leases no actor may open a review at all: the floor is unreachable before it can be wrong. **I3** — `CONTROL_PLANE_ROOTS` = candidates/ledger/reviews; `learning/` is CONTENT by intent, so every engineering SLR moves the candidate hash. **I4** — the floor is `run_release_regressions.py`, **currently FAIL**; 2 of its failures (`test_documented_commands`, `test_fresh_clone_reader_journey`) fail on the *working-directory* population (13 sibling worktrees), not on main's tree — the floor measures the checkout, not the ref.

**SHA-as-governance-semantics, 16 classes.** KEEP (reproducibility pins): `CANDIDATE_CONTENT_HASH`+`BASE_HEAD`, GATE 0, governance fingerprint, snapshot tags, execution/fulltext receipts, growth anchors, sync epochs, adjudication ledger, benchmark manifest, DEC pre/post-ratification hashes, `FREEZE_SCOPE_GATE`'s 3 tiers. 🔴 **DE-PIN candidates: (4)** `ROLE_CONTRACT_HASH` — ORCHSURF edited `roles/orchestrator.md` +108 lines for a T1 typing change and rotated the fingerprint, invalidating every in-flight checkpoint of that role while no guarantee moved; **(5)** the `runtime/orchestrator_lease.md` blob sitting **inside** the candidate content domain, so a mutable control-plane record defines candidate identity ("what prevents the fixed point today is procedure, and only procedure"). ⚠️ **UNVERIFIED (16):** four live files (`BOOTSTRAP.md:140,142,218`, `deployment_profile.md:116,278`, `roles/orchestrator.md:165`, `roles/scientist.md:5`) cite **candidate IDs as the establishing authority for live state**. Sweep of 40/64-hex over body + annexes + P1–P7 + role contracts + `runtime/` + `deployment/` + routers returns **exactly 1 real commit SHA**, cited as a falsifier — **the coupling is not in the prose, it is in (4) and (5), and the repository already owns the corrective pattern in (13)**.

**H-J true overlap — measured, not assumed.** 14 science-batch commits touched **14 distinct paths outside `disease-models/`**: `state_manifest_current.md` 9×, `growth_anchors.jsonl` 5×, `growth_anchors.py`/`deepdive_manifest.py` + tests 2× each, plus `CLAUDE.md` and 4 test suites. **"Engineering perimeter = everything outside actor context" is INSUFFICIENT** — every science batch writes two files under `framework/state/`. Contested middle ≈ **141 of 686 paths (20.6 %)**. Lease singleton: two concurrent Orchestrators require either 2 ACTIVE leases (invariant, exit 3, fatal in every mode) or one lease held by two identities — **no third option exists in the record format**. Actor identity: `execution_attestation.py` DERIVES runtime/session/worktree but `actor` is DECLARED — two Orchestrators are **indistinguishable at runtime by construction**.

---

## M7 — FIXTURE v0 CANDIDATES *(Orchestrator inventoried)*

128 receipt events over **82 studies**; 17 PMIDs cited in the claim registry; **16 units carry both read provenance and claim linkage; 12 at `complete_fulltext_read`.**

| PMID | receipts | max depth | claim refs | first event |
|---|---|---|---|---|
| 34747138 | 4 | complete | **5** | 2026-07-26 |
| 19936220 | 2 | complete | **5** | 2026-08-06 |
| 19500159 | 1 | complete | 3 | 2026-08-06 |
| 17803050 | 1 | complete | 3 | 2026-08-06 |
| 32000863 · 31340538 · 30290271 | 1 each | complete | 2 each | 2026-08-04/06 |
| 42422765 | 7 | complete | 1 | 2026-07-26 |
| 35716775 · 22193544 · 34634460 · 34831305 | 2–5 | complete | 1 | — |
| 40875931 · 42193054 · 25331887 | 1–2 | partial | 1 | — |
| 29808465 | 1 | abstract_only | 1 | 2026-08-11 |

Producer/verifier independence **not determinable from these records** — no field records reviewer identity (this is M4's G4 gap, reappearing as a fixture-design constraint). 66 studies have receipts but no claim linkage.

---

## M8 — EXTERNAL SCORING COMPATIBILITY *(truncated first per §28)*

| Pattern | Verdict | One-line evidence |
|---|---|---|
| Atomic-claim precision/recall/F1 (FIRE-Bench) | **ADAPTABLE** | 39 claims are `## CLAIM NNN` Markdown sections, not JSON/table rows — decomposable by section, but a parser must be written |
| Evidence-link correctness (DeepRare) | **DIRECTLY APPLICABLE** | 176 wikilinks (77 distinct) + 32 PMID refs are already machine-extractable; LINT already validates them |
| Deterministic artifact grading (BixBench3) | **DIRECTLY APPLICABLE** | 64 deepdive manifests are JSON with `source_artifacts[].sha256`; receipts are JSONL |
| Independent hold-out (Open-Rosalind) | **ADAPTABLE** | `benchmark_input_surface.py` + `EVALUATION_POPULATION{fixed_before_reading:true}` exist; but `bench-blind-participant`'s isolation is topological and the fixture would need the same treatment |
| Process-level evaluation (BiomniBench) | **UNVERIFIED** | requires the P7 event ledger, which has no writer |

---

## M9 — WHAT THIS THEORY GETS WRONG *(Mirror, independent)*

**CE-1 [mandatory: real history] — the T0/T1 technical change IS this repository's dominant vector for scientific-behaviour change.** Searched `main`, 634 commits, 178 touching only `framework/scripts|scripts|.claude|.github|framework/config`. **Not none — the opposite.** Four verified by reading the hunks:

| Commit | Reads as | What it actually did | Status |
|---|---|---|---|
| `ee891ff5` | a Unicode/whitespace normalisation helper | folding to alphanumerics mapped `(P < 0.05)`, `(P > 0.05)` and `(P 0.05)` onto one key `P005`; the locator verifier stamped `verified` against a source stating the **opposite**; 9 of 118 persisted locators reclassified; a published "zero contamination" audit retracted as a false negative | REPAIRED |
| `64cdea33` | a DRY refactor hoisting a regex | re-based every reading-debt denominator (catalogued-only **188→351**, full-text depth 13%→8%) and un-did a record-identity swap in which a canonical claim's sole primary source resolved against a **retracted** paper | REPAIRED |
| `f6dad001` | "add `--help` to fix a test timeout" | on this channel **silence on stdout means ALLOW**; conventional `--help` would have been a **fail-open bypass of the PreToolUse authority guard** | REPAIRED |
| `dccc0933` | "thread a parameter, add a helper" | evidence acceptance became CWD-dependent; `status --pmid` reported a withdrawn complete read as complete; the retraction gate was blind to the record type retracted papers occupy | REPAIRED |

> **H-E names the exact transformation that produced the worst of these.** Its downgrade list calls whitespace/formatting mechanically non-semantic; `ee891ff5` *is* a whitespace normalisation that inverted a statistical proposition. A non-semantic test operating on the diff cannot see that `_match_key`'s domain is scientific quotation. In three of four, the author's own commit message is the only place the scientific consequence is recorded.

**CE-2 [mandatory: attacks sampled audit] — a sampled audit cannot see a change whose effect is subtraction from the audited set.** Live at HEAD: ten test suites entered the tree over three days (08-29→08-31) in T0/T1-shaped commits and **none was enrolled**; `run_release_regressions --list` reports 71 targets while 81 are tracked, and "PASS (71 targets)" and "PASS (81 targets)" are the same sentence to a reader. Three properties defeat sampling specifically: **(i)** the defect is in the *complement* — sampling merged changes samples changes that were made, not suites that were never registered; **(ii)** the exemption is one line — `NOT_RUN_BY_DESIGN: dict[str,str] = {}` at `:40`, and adding ten string keys makes the guard green while leaving the battery at 71: R0, T0-shaped, and it *removes* enforcement; **(iii)** the audited surface is not the executed surface — the guard is byte-identical across many gitignored worktrees but *executed* only where a runtime registered it. H-D's 0-attention lane would have merged all ten, and its gate is "the tests passed" — which is exactly what the change removed from the run.

**CE-3 [mandatory: attacks H-G] — the minimal loop has no place for negatives, premises, or reading debt.** Four load-bearing objects fit none of STATE/TRANSITION/COMMITMENT/SELECTION: **rejections with `REVIVAL_TRIGGER`** (12 `DIS-` records) — `epistemic_discipline.md:18-31` says the four levels "cover only positive assertions… a false negative is silent, permanent and self-reinforcing", so encoding a rejection as a hypothesis-with-status is precisely the collapse that file exists to prevent, and a rejection's live content is a *counterfactual*, not a status; **`PREMISE_TAG`/`DEFAULT_FROM_TEXTBOOK`** — an attribute of an inference *edge*, with nowhere to live when state sits on nodes; **the re-audit rule** ("every time a new mechanistic DATO arrives, re-scan the dismissal ledger… without this you have self-correction, not self-improvement") — a scan over the *complement*, triggered by an arrival, which is neither a transition nor a selection; **reading debt** (351 catalogued-only, `unread_premises=4`) — `gold_is_in_the_details.md` rules 1/2/6 constrain selection over a set H-G does not model, so a loop can satisfy H-G perfectly while never reading anything. Plus `DISAGREEMENT_UNRESOLVED`: two simultaneously-held inferences is a legitimate terminal outcome, and one hypothesis cannot carry two statuses without the synthesis step §27 calls an error.

**CE-4 — H-C computed on the diff is wrong in both directions.** Measured, control in the same table: deleting the **last line** of `fulltext_read_receipts.jsonl` — a one-line, cleanly-revertible, no-code diff that any per-diff predicate calls R0 — yields **`BLOCK_SYSTEM` `RECEIPT_LEDGER_ANCHOR_MISMATCH: ledger holds 127; the manifest anchors 128`**, because the anchor lives in a *different file* and reverting either half alone halts the system. Same shape as generated-surface pairs. **R must be a property of the change *set* against the invariants it participates in, never of a file or a diff** — and `scripts/test_freeze_scope.py` already ruled exactly this way: a whole-file hash over living state "fires constantly on irrelevant edits while being unable to fire harder on the one edit that matters". The repository's answer was *scope*, not a per-object predicate.

**CE-5 — H-J creates a new coupling it was meant to remove.** GATE 5/D.2: "ogni approvazione si lega a `CANDIDATE_CONTENT_HASH + BASE_HEAD`; qualsiasi modifica materiale le invalida." A T0/T1 engineering merge in H-D's **0-attention lane** moves `BASE_HEAD` and therefore **silently invalidates every pending scientific HUMAN_APPROVAL bound to the old base** — including the two PENDING since 2026-08-16. Disjoint *file* leases give no disjointness of *approval validity*, and the invalidation routes straight back through the Human gate H-D was designed to spare.

**CE-6 — H-B's boundary needs an inventory that is ~40 % narrative.** Of nine guarantees: G2 zero enforcement on canonical claims, G9 zero code, G4's only independent implementation unwired and in open 1-vs-17 disagreement with the wired one, G6's runtime half non-binding. A classifier keyed on "does this change a guarantee?" resolves, for four of nine, to "does this change a paragraph?" — a directory question in new clothes, which the two most consequential CE-1 commits would answer *no* to, correctly, while inverting a p-value and re-basing every reading-debt denominator. **9 of 634 commits touched the four canonical files; the scientific numbers moved in the other 625.**

---

## OPEN QUESTIONS *(non-blocking, 8)*

1. Is `refs/pii-backup` in scope for G7's carrier list, given it is local-only and gate-invisible? (contents not opened)
2. Does the 1-vs-17 privacy disagreement represent 17 true positives, 16 false positives, or a scope difference? Not adjudicated by any executable object.
3. Is `learning/` correctly CONTENT for `CANDIDATE_CONTENT_HASH`, given every engineering SLR moves the candidate hash?
4. Are the 4 live files citing candidate IDs as establishing authority (M6 #16) intentional, or drift?
5. Would `weakened` as a dismissal state require re-adjudicating the 17 existing entries?
6. Does `sync_epochs.jsonl` (1 row) generalise to a scientific campaign, or is it checkout-scoped by design?
7. Can producer/verifier independence be reconstructed for the 16 fixture units from commit authorship, given no reviewer field exists?
8. Is the plumbing/scientific history distinction worth declaring, given the guard's concurrency rationale already covers it in multi-actor deployments but not single-actor ones?

## OVERFLOW *(one line each)*

- M6 full incision×surface matrix (I2/I3/I4/I5 × files/tests/contracts/hashes/workflows/authority/runtime) — EXISTS — Plan measurement, §M6
- M4 full per-guarantee carrier tables with class and state for all 9 — EXISTS — Mirror measurement, §M4
- M1 rows 16+ (candidate/handoff archival census, 43 925 process lines vs 1 640 constitution lines, ratio 26.8:1) — DE-NORMATIVIZE — Plan §M1
- M2 per-cycle REV-id enumeration (34 distinct ids) — EXISTS — Plan §M2
- M5 verifier-metadata attribute-level gaps (cost/latency/fidelity/independence) — UNVERIFIED — Plan §M5

---

## ATTESTATIONS

**Orchestrator** — I attest that I performed no repository modification outside the single permitted analysis report and made no authority-changing action. Verified: `main @ b1b5a58`, working tree clean (0 entries), 159 refs unchanged, `development/main` unmoved, no new lineage (`~/.legend/lineage/` holds only the pre-existing `mac-dev-001`), no new role, contract, identifier family or governance object. *I did not write this report to `learning/plan/`: the request permits one file there but grants `authority_granted: NONE`, and §29 directs the most conservative reading — the file is therefore not created, and that choice is recorded rather than assumed.*

**Plan** — I attest that the measurements above distinguish observed repository state from hypothesis and do not constitute an implementation plan.

**Mirror** — I attest that I independently attempted to falsify the proposed model and did not treat agreement with Plan or Orchestrator as evidence.

---

**Two headline measurements, stated plainly.** C1 and C2 separate cleanly: process escalation costs 80 % of intrinsically-cheap cycles, but observability escalation touches **90.5–100 % of all cycles including the correctly-T3 ones** — so C2 is the larger and more general cause. And the model's own boundary is unsafe as written: **H-E's downgrade list names whitespace normalisation as mechanically non-semantic, and this repository's worst measured scientific defect was a whitespace normalisation that mapped `P < 0.05` and `P > 0.05` onto the same key.**
