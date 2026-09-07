---
record_type: REVIEW_FINDINGS_REGISTER
record_id: TRIAL-001-REVIEW-FINDINGS-REGISTER
trial_id: TRIAL-001
title: Findings register — hostile review and feasibility review of the TRIAL-001 execution protocol
author: unregistered session — no role contract, no ACTOR_ID
session_ref: legend-public-2a [cea07c]
actor_id: NOT ESTABLISHED
date: 2026-08-23
status: OPEN — every finding awaits an operator disposition
binding: NO
reviewed_object:
  path: learning/orchestrator/LEGEND_FIRST_OPERATIONAL_TRIAL_EXECUTION_PROTOCOL_v1.md
  blob: d5c0d296df69ea5a14426e2da351869959983c7b
  size: 61142 bytes · 796 lines
  read_by_both_reviewers_with: git cat-file -p d5c0d296df69ea5a14426e2da351869959983c7b
measured_at: >
  branch `legend-operating-convention-v1` @ 30cb4f3fd700e2aaf6b608e363438f883ddc3760,
  2026-08-23T20:35Z–21:05Z.
why_this_record_is_separate: >
  The protocol's own § 13 rule 2 forbids editing the blob that was reviewed — an edit changes the
  bytes, changes the blob, and orphans both reviews. Writing the register into the protocol's
  § 13.1 would therefore violate the rule the register exists to serve. The register lives outside
  the reviewed object, and § 13.1 stays empty in blob d5c0d29 by construction. **This is itself an
  uncorrected defect of § 13 and is filed below as X-1.**
nothing_corrected: >
  No finding below has been acted on. The protocol blob is unchanged. No v2 exists.
---

# TRIAL-001 · Findings register

**Two reviews, both bound to blob `d5c0d296df69ea5a14426e2da351869959983c7b`, both commissioned
before the protocol closes, neither carrying any authority, and neither auto-corrected.**

---

## 0 · The reviewers, and what each is and is not

| | Hostile review | Feasibility review |
|---|---|---|
| **Session** | `mirror-1b [a85964]`, working dir `.claude/worktrees/mirror` | ephemeral subagent, spawned by `legend-public-2a` |
| **Actorhood** | 🔴 **not established, and the session declined to claim it.** It reported that the registry card for `ACTOR_ID mirror` binds session ref `mirror-9c [3940a9]`, which is not it. Record it as *a session in the mirror worktree with no established actorhood* | 🔴 **not the registered Plan seat.** No `plan-*` session was live in `ListAgents` at dispatch. Record it as *an ephemeral feasibility reviewer* |
| **Identity verified how** | delivery + **complement of peer lists**: its list carries `legend-public-2a` and not itself; mine carries `mirror-1b` and not me; the other eleven names coincide. Its worktree HEAD `27673332` and the 6-commit gap from `da52ee5` were re-derived here and match | n/a — spawned by this session, so identity is not in question; **authority and seat-membership are** |
| **What it read** | the blob only. It declined to verify § 2.4's census, the 8-surface sweep or T-8's nine PMIDs, on the ground that they measure a working tree it was told not to read — **and said so rather than assuming them** | the blob, plus the repository, plus 85 tool calls of independent measurement |
| **Scope note** | `started 11h ago` in my listing, `~6h` reported to another session, and a transcript first entry of `2026-08-22T20:00:48Z` (~20h) are **three different figures for the same session**. `started` measures the runtime incarnation, not the conversation, and is not evidence in either direction | — |

---

## 1 · Hostile review — findings F-1 … F-10

Verification column: **`RE-DERIVED`** = this session reproduced it mechanically against the
protocol's own text or the repository. **`READ`** = confirmed by reading the blob, no tool needed.
**`AS REPORTED`** = carried on the reviewer's evidence, not independently checked.

| # | § | Finding | Verified | Disposition |
|---|---|---|---|---|
| **F-1** 🔴 | 5 (V-2) · 7.2 · 6.2 · 11.3 | **Arm T's denominator is zero by construction.** V-2 requires *the reader* to supply the anchored triple; § 7.2 defines arm T as producing none. Arm T can satisfy no V-condition, so its verified-claim count is 0 by definition, its primary quotient is `UNDEFINED`, and § 11.3's PRIMARY criterion — *"arm L lower than arm T"* — can be neither true nor false. Its stated falsifier is unreachable for the same reason. **§ 7.3's prose says the *auditor* locates arm T's evidence; V-2 says the *reader* supplies it. The two contradict, and the primary comparison collapses.** | READ | **OPEN** |
| **F-2** 🔴 | 2.3 | **The layer derivation is not total, and fails on the state the model exists to express.** `{captions_only}`, `{captions_only, not_present}`, `{unknown_legacy}`, `{read, unknown_legacy}` return no status. `FIGURE_LAYER` is the single key `figures`, so **`figures: captions_only` → UNDEFINED** — the exact case § 2.3 offers as its demonstration. `COVERAGE_STATES` has six members; the rules name five; `unknown_legacy` is unmapped and occurs **135 times** in the population T-8 was computed over | **RE-DERIVED** — see § 3 | **OPEN** |
| **F-3** 🔴 | 6.2 · 5.1 · 6.4 | **The metric penalises ambition.** Minutes spent on claims that fail verification stay in the numerator; the claims leave the denominator. A reading carrying 6 substantive claims of which 2 verify scores ~3× worse than one carrying 4 trivial ones. One of the penalised states is `UNVERIFIABLE_SURFACE`, which § 5.1 explicitly calls *not a defect*. § 6.4's guard is a sentence with no threshold, no required output and no consequence — one order of specification below the thing it guards. **And the numerator is self-logged by the auditor with no corroborating source** | READ (arithmetic) | **OPEN** |
| **F-4** 🔴 | 2.5 | **`G-1` is unfalsifiable in the direction that costs nothing.** The classifier is the reader whose claims it constrains; the evidence that would refute a `G-1` is the missing unit itself. Worked case: a `DATO` anchored to a Results sentence that itself reads *"as shown in Supplementary Figure 3"*, with S3 unavailable and classified `G-1` — `CRITICAL_ASSET_GAP: NO`, B-9 never fires, V-4 passes, and § 2.1's *"second failure, the dangerous one"* is reproduced inside the instrument built to prevent it. **The mechanical check exists and is not run**: grep the recorded `verbatim_locators.entries[]` snippets for references to each `G-1` unit; any hit is a `G-1` that must be `G-2`/`G-3`. § 9 M-1 asks whether the claim set was thinned; it does not ask whether a gap was downgraded | READ | **OPEN** |
| **F-5** 🔴 | 7.3 · 7.4 | **The audit is not blind.** Arm L's claims carry anchors and arm T's do not, so **the shape *is* the arm label** and stripping it removes nothing. K-2 discloses something else — a bias of *effort given the shape* — and therefore does not disclose the defect that is present. An unblinded auditor produces both halves of the comparison the trial exists to make. *(The reviewer explicitly rejected the dispatch's premise that K-2 covers this.)* | READ | **OPEN** |
| **F-6** 🔴 | 4 | **Four of twelve blocks cannot fire as specified.** **B-5** compares against a *first content-read instant* no artifact produces — and § 7.5's own J.0 block is honest where B-5 is not. **B-7** releases *"before any `BATCH_COMMIT`"*, which the trial never reaches. **B-8** detects with `git status`, which does not see `git hash-object -w` — **the write that created the very blob under review**. **B-12** rests on S.8.1, which § 14 declares unadopted | **RE-DERIVED** (B-8 by this session's own transcript) | **OPEN** |
| **F-7** 🔴 | 2.2 | **The partition is neither exhaustive nor unambiguous.** (a) A supplementary figure bound into one accepted-manuscript PDF is `FIGURE_LAYER` by the rule and `SUPPLEMENTARY_LAYER` by the table — **and that is the shape PMID 28123895 would arrive in from PMC**. (b) Front and back matter are in no layer: title, authors, funding, ethics, acknowledgements, and above all the **data-availability statement**, which is the unit that says whether a supplementary layer exists at all. `COVERAGE_KEYS` has no key for it. (c) One `tables` key is split across two layers | READ | **OPEN** |
| **F-8** 🔴 | 2 (whole) | **§ 2 is framework construction, and "no schema change" answers a question nobody asked.** § 2 introduces a new phase (Φ1d), a new blocking criterion (B-9), a new verification condition (V-4), a new measured dimension (D-LAYER), a new mandatory artifact (§ 2.6) and a new reader obligation. **The trial would build the instrument, test the instrument, and report the result as a fact about LEGEND** — while T-8, the finding that motivated it, is registered as outside the write allowlist and left unrepaired | READ | **OPEN — operator scope decision.** *The layer model is the operator's own instruction; what is at issue is the volume of new normative surface built around it* |
| **F-9** | 12 · 11.3 | **The guaranteed outcome is pre-declared the best one.** § 12's row *"arm L scores no better than arm T → the single most valuable possible outcome"*, set beside F-1's structurally undefined arm-T score, means a future reader cannot distinguish *"we measured that anchoring did not pay"* from *"we defined the denominator so only one arm could have one"*. **§ 11.2 is otherwise a real falsifier and the reviewer said so** | READ | **OPEN** |
| **F-10** | 3 (E-6) · 11.3 | **D-LAYER passes instead of becoming inapplicable** when the paper has no supplementary material: every non-`read` unit classified (none), every `G-3` naming its claim (none), the block derivable (two vacuous `COMPLETE`s). The outcome would carry a passing new dimension beside a sentence saying the model was not tested, and the two will not be read together | READ | **OPEN** |

**Sections the hostile reviewer returned `nothing` on, without padding:** § 8 (phase sequence and
artifact index — *"a phase that produced no artifact did not run" is the right shape*), § 10 (Plan's
triggers — *P-1/P-2/P-4 correctly locate the denominator and the freeze outside the party they
constrain, which is the principle F-4 finds missing from § 2.5*), § 13 (*"the strongest section in
the record"*), § 14 as a list of non-acts.

---

## 2 · Feasibility review — findings P-1 … P-10

| # | Φ / § | Finding | Verified | Disposition |
|---|---|---|---|---|
| **P-1** 🔴 | Φ2 · Φ4 | **Neither reader exists as an actor, and the entrance gate is the same object as the exit gate.** Φ2 needs two Annex A.1 contracts with resolvable `OWNER (ACTOR_ID)`. `roles/scientist.md` resolves `scientist-a`/`-b` only on canonical execution of `CAND-20260818-SCIENTIST-AB-SPEC`, which is **revision 6 after five consecutive `REQUEST CHANGES`, no `PASS` ever recorded**, awaiting Mirror and `HUMAN_APPROVAL`; its own `MIRROR_REVIEW` value is one of the eight non-conforming ones of B-10; its capability verification is `SUSPENDED` under the C-9 hold; and § 14 declines to lift any of it. **Φ3–Φ7 are all downstream. B-10 is not only the exit gate at Φ10 — the same unresolved object sits across the entrance at Φ2** | AS REPORTED | **OPEN — blocking** |
| **P-2** 🔴 | Φ7 | **The primary metric has no instrument, and one of its two verdicts exists nowhere.** `legend-locator-audit` emits a four-column table with no minutes column and no `NOT_LOCATABLE`. **`NOT_LOCATABLE` fires on 0 tracked paths and appears only in the trial's own two records** (positive control `UNVERIFIABLE_SURFACE` → 5 files). The numerator is hand-kept at minute precision by an agent whose blindness is the reason it cannot hold a clock — and this repository has recorded 16+ times that it cannot produce a wall-clock time. **Price the primary metric as human discipline plus an unvalidated proxy, not as an instrument reading** | **RE-DERIVED** (`NOT_LOCATABLE` 0 tracked; controls fire) | **OPEN** |
| **P-3** 🔴 | § 2.3 | **Independent confirmation of F-2, exhaustively.** Over the 63 non-empty value-sets of the six-state alphabet: **8 undefined, 0 ambiguous.** And a defect the hostile review did not reach: **`PARTIAL` is unreachable for `FIGURE_LAYER` and `SUPPLEMENTARY_LAYER`** — a one-key layer cannot satisfy *"at least one `read` **and** at least one `captions_only`/`unavailable`/`not_read`"*. **Two of the nine cells of the § 2.6 block can never be printed.** Applied to the live ledger: **37 of 128 receipts (29 %) yield ≥1 undefined layer** — 14 from `figures: captions_only`, 23 from `unknown_legacy`. Further: **the `GAPS:` table of § 2.6 has no home in the receipt at all** — the union of top-level receipt fields over 128 receipts carries no per-unit field — so Φ6 can derive at most three of the block's rows | **RE-DERIVED** — 8 of 63 and `PARTIAL` unreachable reproduced against the protocol's own rules | **OPEN** |
| **P-4** 🔴 | Φ1d | **No instrument can enumerate the three layers, at any time. The phase has an owner and no tool.** `benchmark_input_surface.py population` is the only ex-ante enumerator and has **no `layer` key** (`grep -c -i layer` → 0; `git grep TEXT_LAYER\|FIGURE_LAYER\|SUPPLEMENTARY_LAYER HEAD` → nothing, positive control `COVERAGE_KEYS` → 5 files). Its `by_kind` produces no abstract, introduction, discussion, limitations or references units — **the `TEXT_LAYER` is largely unenumerated**. Worse, it extracts a `main_figure` unit *from its caption*, which § 2.2 puts in a different layer, and has no mechanism to split them. `caption_census` answers a different question on XML/HTML only; `surface_census` is per-paper; `figure_ppi_preflight` is a render preflight. **And Φ1d's own gate contradicts § 2.5**: the denominator is Plan's, the gap class is the reader's, so D-LAYER's falsifier fires on the protocol's own design | AS REPORTED (tool absence spot-checked) | **OPEN** |
| **P-5** 🔴 | Φ5 | **`freeze`/`verify-freeze` exist and record every field Φ5 names — and the ordering still cannot be evidenced.** The tool disclaims it in its own receipt: *"`FREEZE_TIMESTAMP_UTC` is this process's clock, attested by nothing else… that the second reader was not shown the first reader's output is PROCEDURAL. Nothing here enforces it."* No instrument records a first-content-read instant. **§ 11.1 requires *shown* timing and § 11.2 makes an unshown freeze an experiment failure — so on today's instruments the trial fails § 11.2 by construction, for both arms.** Second, concrete: `cmd_freeze` refuses unless the surface carries `ASSIGNMENT.md`, `benchmark/BENCHMARK_INSTRUCTIONS.md` and `benchmark/OUTPUT_SCHEMA.md` with front matter — **three scaffolding files inside the arm § 7.2 defines by their absence** | **RE-DERIVED** (subcommands; the refusal at line 749) | **OPEN** |
| **P-6** 🔴 | Φ1c | **The pricing claim holds; the gate on it has zero power.** The `population` block is **41.9 %** of the 421-line worked spec and is the only block whose correctness needs instrumented probing of the acquired PDF — font face, point size to two decimals, page geometry to a tenth of a point, per rule. It took 6 commits over two days and five Mirror-driven revisions. **But Φ1c's gate — "two runs must give an identical population digest" — has no power against the failure it cites**: `population` is a pure function of (spec, source bytes), so two runs always agree, and both documented enumerator errors were deterministic. *(Reproduced: run1 = run2 = `b41c7b9f…`.)* **Only the hand enumeration has power, and on the worked precedent that is 65 units and 109 panels of human cross-checking — the real, unstated Φ1c line item** | AS REPORTED (determinism reproduced in the design) | **OPEN** |
| **P-7** 🔴 | Φ6 | **Two defects.** (a) **The `deepdive_manifest` invocation as literally written in Φ6 and in § 5 V-2 exits 2** — `--pmid is required unless --font-screen is given`. (b) **The coverage map over the frozen population has no tool**: nothing in the repository reads `evidence_units.json` (4 prose mentions, 0 scripts; positive control `benchmark_input_surface` → 10 files). `coverage_report.py` is not it — it reports corpus-level reading depth per paper and cannot express coverage of 65 units and 109 panels of one paper. Five of six named checks otherwise exist and take the named flags, all green at HEAD | **RE-DERIVED** (exit 2 reproduced) | **OPEN** |
| **P-8** | Φ10 · B-10 | **B-10's figure reproduces exactly, independently.** Denominator enumerated twice by two instruments blind to the property (`find` and `git ls-files`, identical set of 8). **8 of 8 carry `MIRROR_REVIEW`; 0 of 8 carry a conforming value.** The reviewer also recorded the measurement trap: a naive `grep -o PASS` scores `PASS_WITH_NOTES` as conforming — the same prefix-match class as `<fig\b` matching `<fig-count>` documented in `caption_census.py`; the correct form anchors both ends | AS REPORTED (matches design T-5) | **OPEN — confirms, does not fault** |
| **P-9** | Φ1a · Φ1b · B-2 | **🔴 A correction to the protocol, not a defect of the repository: B-2 is overstated.** `framework/scripts/pmc_pow_fetch.py` exists — *"Fetch a public PMC binary protected by the cloud-viewer proof-of-work page… It never uses credentials."* FT-018 records `PMC5214935 (open)`. So Φ1a's declaration has a concrete route to name and Φ1b has a receipt writer. **Acquisition is authorization- and network-blocked from an isolated session, not instrument-blocked**, and B-2 says the stronger thing. Entry criteria E-1/E-2/E-3 were independently re-derived and reproduce | **RE-DERIVED** (`--help` fires) | **OPEN — this one weakens a claim of mine in LEGEND's favour** |
| **P-10** | Φ2 · Φ7 · Φ8 · Φ9 | **Smaller gaps, named.** No `ORCHESTRATOR_LEASE` is ACTIVE (`ACTIVE by derivation: 0`, plus a standing stored/derived disagreement on lease #3), so Φ2's Orchestrator branch is not live — operator only. **No validator exists for `ledger/tasks/`**, so Φ2's contracts are hand-authored JSON with no shape check. Annex C.3 requires opening via Orchestrator and three distinct actors `AUTHOR ≠ REVIEWER ≠ ADJUDICATOR`, from a set that is currently empty. Φ7's artifact path has no owner directory — `reviews/` contains only `plan/`. **And the question handed to both arms is itself a prior LEGEND inference**: FT-018's `Why` states the conclusion *"C1q as upstream regulator of WWOX activation state, not level"* before the reading, and `content_scan` must exempt `ASSIGNMENT.md`, so the one document carrying a prior conclusion is the one the identifier scan does not read | AS REPORTED | **OPEN** |

> **Feasibility verdict, verbatim: `NOT FEASIBLE AS WRITTEN`**, bound to blob `d5c0d29`.
> Most likely phase to stall: **Φ2**, not Φ1c — *"Φ1c is expensive but has a working instrument, a
> worked precedent and a deterministic output I reproduced today."*

---

## 3 · What this session re-derived, and the commands

Not to adjudicate the reviewers, but because a finding carried on a report alone is a finding
carried on trust. **Every check below was run against the protocol's own text or the repository.**

```bash
# F-2 / P-3 — the derivation, evaluated against MY OWN three rules
#   single-key layers (FIGURE_LAYER = {figures}; SUPPLEMENTARY_LAYER = {supplementary})
#     read → COMPLETE · not_present → COMPLETE · unavailable → UNAVAILABLE · not_read → UNAVAILABLE
#     captions_only → UNDEFINED     unknown_legacy → UNDEFINED
#     PARTIAL reachable with one key?  False        ← two cells of § 2.6 can never be printed
#   all 63 non-empty value-sets over the 6-state alphabet: 8 UNDEFINED, 0 ambiguous
grep -n "^COVERAGE_STATES" framework/scripts/fulltext_receipts.py        # six members
grep -o "captions_only"  disease-models/wwox/registries/reading_state.md | wc -l   #   5
grep -o "unknown_legacy" disease-models/wwox/registries/reading_state.md | wc -l   # 135

# P-7a — the Φ6 command AS WRITTEN in the protocol
python3 framework/scripts/deepdive_manifest.py --verify-artifacts --require-current-schema
#   error: --pmid is required unless --font-screen is given          exit 2

# P-2 — the verdict that exists nowhere
git grep -l "NOT_LOCATABLE" HEAD | wc -l                               # 0 tracked paths
grep -rl "NOT_LOCATABLE" --exclude-dir=.git . | wc -l                  # 2 — both trial records
grep -rl "UNVERIFIABLE_SURFACE" --exclude-dir=.git . | wc -l           # 5 — positive control fires

# P-9 — B-2 is overstated: an in-repo acquisition route exists
python3 framework/scripts/pmc_pow_fetch.py --help                      # fires

# P-5 — freeze exists; and refuses without the three identity files
python3 framework/scripts/benchmark_input_surface.py --help | grep -oE "\{[a-z,-]+\}"
#   {build,verify,freeze,verify-freeze,population,locators,tree-digest}
grep -n "REFUSE: the surface has no" framework/scripts/benchmark_input_surface.py   # line 749

# F-6 B-8 — git status does not see the write that created the reviewed blob
git hash-object -w <file> && git status --porcelain                    # the object is invisible

# reviewer identity — complement of the peer lists, and the worktree HEAD
git -C .claude/worktrees/mirror rev-parse HEAD                         # 27673332…  as reported
git -C .claude/worktrees/mirror log --oneline da52ee5..HEAD | wc -l    # 6          as reported
```

---

## 4 · Findings this register adds of its own

| # | Finding | Disposition |
|---|---|---|
| **X-1** 🔴 | **§ 13 of the protocol cannot be executed as written.** Rule 1 says every finding is registered *in § 13.1*; rule 2 forbids editing the reviewed blob. Registering inside § 13.1 changes the bytes, changes the blob, and orphans both reviews. **The two rules are in direct conflict, and this register resolves it by living outside the reviewed object — a resolution the protocol does not authorize.** The hostile reviewer called § 13 *"the strongest section in the record"* and did not reach this, because it is only visible from the act of executing it | **OPEN** |
| **X-2** | **A third unreported move of the `mirror` seat.** Its tip was `1892071` (2026-08-21) → `da52ee5` (2026-08-22) → `2767333` (2026-08-23T18:19Z, design T-6) and the occupying session reports six commits landed on it **authored by a session that is not itself**, with its own six untracked files surviving. Design T-6 recorded two unreported moves; this is the third, and the first with a co-author collision | **OPEN** |
| **X-3** | **`started Xh ago` returned three different values for one session** — 11h (this session's listing), ~6h (reported to `legend-public-54`), ~20h (that session's own transcript first entry, `2026-08-22T20:00:48Z`). Consistent with OPCON § S.1.4: `started` measures the runtime incarnation, not the conversation. **It is not evidence in either direction, and the register records the three figures rather than picking one** | **OPEN** |

---

## 5 · Disposition rules — fixed before the findings arrived, unchanged by them

Reproduced from the reviewed blob's § 13, and honoured here:

1. Every finding is **registered** with its reviewer and the blob it was made against. ✅
2. **None is corrected in this version.** ✅ — blob `d5c0d29` is unchanged and no v2 exists.
3. A finding the protocol declines to act on must say **why**. ⏳ — no finding has been declined;
   all 23 are `OPEN` and none has been dispositioned by anyone with the standing to do so.
4. **A finding is not a blocker unless the operator makes it one.** Neither reviewer holds authority
   over the protocol, neither was asked to grant one, and neither claimed one. ✅

> **Nothing in this register repairs anything.** The protocol blob, `main`, the four scientific
> current files, `governance/`, `roles/` and `framework/` are all unchanged.
