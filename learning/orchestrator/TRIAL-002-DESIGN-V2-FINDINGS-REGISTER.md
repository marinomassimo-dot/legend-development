---
record_type: REVIEW_FINDINGS_REGISTER
record_id: TRIAL-002-DESIGN-V2-FINDINGS-REGISTER
trial_id: TRIAL-001
title: Findings register — hostile review and feasibility review of Trial Design v2, revision 1
author: unregistered session — no role contract, no ACTOR_ID
session_ref: legend-public-ae [989694]
actor_id: NOT ESTABLISHED
date: 2026-08-23
status: OPEN — every finding carries a disposition; no disposition is an approval
binding: NO
reviewed_object:
  path: learning/orchestrator/LEGEND_FIRST_OPERATIONAL_TRIAL_DESIGN_v2.md, revision 1
  blob: e88dc043180b9db9e6e3cf270a84e13aae5f827f
  size: 85073 bytes · 1074 lines
  read_by_both_reviewers_with: git cat-file -p e88dc043180b9db9e6e3cf270a84e13aae5f827f
  hazard: >
    🔴 reachable from 0 refs, gc-prunable. Re-derived: `git rev-list --objects --all | grep -c
    e88dc043…` → 0; positive control (HEAD's CLAUDE.md blob) → 1. Both reviews are bound to
    bytes no ref preserves. Preserving them is decision D-13 of the successor.
successor: >
  learning/orchestrator/LEGEND_FIRST_OPERATIONAL_TRIAL_DESIGN_v2.md, revision 2. Revision 1 was
  NOT edited — it survives as the blob above. This register lives OUTSIDE both, which is the
  resolution X-1 discovered by violating it.
measured_at: >
  branch `legend-operating-convention-v1` @ 30cb4f3fd700e2aaf6b608e363438f883ddc3760,
  reviews delivered 2026-08-23T21:4xZ and 2026-08-23T22:0xZ; this session's re-derivations
  2026-08-23T21:5xZ–22:1xZ.
what_this_register_does_not_do: >
  It grants nothing, blocks nothing, and resolves nothing on anyone's behalf. A finding is not a
  blocker unless the operator makes it one. Neither reviewer holds authority; neither is the
  registered seat; both said so unprompted.
---

# TRIAL-002 · Findings register — the two reviews of Trial Design v2 revision 1

**44 findings. 27 hostile, 17 feasibility. Both reviews bound to blob `e88dc043…`. None was
auto-corrected. Revision 1 is unedited.**

---

## 0 · The reviewers, and what each is and is not

| | Hostile review | Feasibility review |
|---|---|---|
| **Standing** | 🔴 **no ACTOR_ID, no contract, no lease.** **Not** the registered Mirror seat — the registry binds `ACTOR_ID mirror` to `mirror-9c [3940a9]`, which is not it. It said so unprompted | 🔴 **no ACTOR_ID, no contract, no lease.** **Not** the registered Plan seat — the registry binds `ACTOR_ID plan` to `evidence-index-59 [de42c4]`. It said so unprompted |
| **What it read** | the blob in full, 1074 of 1074 lines, extracted to a scratchpad outside the repository; plus the v1 findings register, `fulltext_receipts.py`, the audit skill, `roles/*.md` | the blob in full; plus **116 independent measurement calls** against the repository |
| **What it declined** | to re-derive v1's *own* register figures; to say anything about the content of PMID 28123895, which is not in the repository | live-session state (it holds no session-enumeration tool) — reported `AS REPORTED` and never used as evidence |
| **Verdict** | *"v2 fixes the defects it was told about and reproduces four of them one layer down"* | **`FEASIBLE WITH NAMED CHANGES`**, bound to the blob |
| **Wrote to the repository** | nothing | nothing |

**Why neither is the registered seat.** At dispatch, `ListAgents` showed 14 live peer sessions,
four of them `mirror-*`. **Neither registered seat ref was among them.** The v1 register recorded
the identical situation. Recording it again is not redundancy — it is the third consecutive day on
which the seats named in the registry were not the sessions doing the work.

---

## 1 · What this session re-derived, and what it carried

**Nine findings were re-run mechanically before being accepted.** The rest are `READ` — verifiable
against the blob's own text — or `AS REPORTED`, and are marked as such. A finding carried on a
report is carried on trust, and revision 1 was wrong exactly where it did that (W-1).

```bash
# H-1 — revision 1's five status predicates, evaluated over all 63 non-empty subsets
#   UNDEFINED 0 · AMBIGUOUS 28 · of those, 7 contain no unknown_legacy and no reading of
#   "absorbing" rescues them:
#     {captions_only,unavailable} {captions_only,not_read} {captions_only,unavailable,not_read}
#       → CAPTION_ONLY + UNAVAILABLE
#     {captions_only,not_present} {captions_only,not_present,unavailable}
#     {captions_only,not_present,not_read} {captions_only,not_present,unavailable,not_read}
#       → PARTIAL + CAPTION_ONLY
#   control: the six singletons reproduce revision 1's six intended answers
#   empty set → COMPLETE, by a vacuous quantification revision 1 never stated

# H-15 — the track separation, against revision 1's own text
grep -c "TRACK-M\|TRACK-S" <rev1>                                   # 7 of 1074 lines
sed -n '/^### 9.1/,/^### 9.2/p' <rev1> | grep -c "TRACK-"           # 0   control "Plan" → 6
sed -n '/^### 9.5/,/^### 9.6/p' <rev1> | grep -c "TRACK-"           # 0
sed -n '/^### 10.1/,/^### 10.3/p' <rev1> | grep -c "TRACK-"         # 0

# H-20 — the denominator revision 1 dropped
git ls-tree -r --name-only HEAD -- disease-models/wwox framework/eval | wc -l   # 297
git ls-tree -r --name-only HEAD | wc -l                                         # 581
git grep -l -i receipt HEAD -- disease-models/wwox framework/eval | wc -l       # 160 control
git grep -l ZZQX HEAD -- disease-models/wwox framework/eval | wc -l             #   0 control

# H-24 / the blob hazard
git rev-list --objects --all | grep -c "^e88dc043…"                             # 0
git rev-list --objects --all | grep -c "$(git rev-parse HEAD:CLAUDE.md)"        # 1 control

# P-1 / P-2 — what `fulltext_receipts.py record` actually writes
sed -n '752,757p' framework/scripts/fulltext_receipts.py        # write_state_anchor(...) IN-LOCK
python3 -c "…fr.default_ledger_path / fr.default_manifest_path…"
#   disease-models/wwox/registries/fulltext_read_receipts.jsonl
#   framework/state/state_manifest_current.md
git cat-file -p e88dc043… | grep -c state_manifest              # 0   control SURFACE-LITE → 11

# P-4 — prior LEGEND output about this paper, outside the 8 analysis surfaces
git grep -lE "28123895|PMC5214935" HEAD | wc -l                 # 10 of 581
grep -n 28123895 disease-models/wwox/registries/literature_tracking_log_current.md
#   11914 · 12045   "PMID 28123895 (C1q → attivazione di WWOX, coda HIGH)"
#   🔴 CONTROL ANOMALY, recorded: the negative control 99999999 fires on 4 TRACKED files
#      repo-wide — all four are test_*.py fixtures. It is a clean negative on the 8 analysis
#      surfaces, which is the only scope it was ever used in. The wider sweep has no clean
#      negative and is reported as an enumerated set of 10 named files instead of as a count.

# P-5 — the Scientist A/B specification is canonical
git show mirror:reviews/mirror/REV-SCIAB-MIRROR-006.md | sed -n '11,13p'   # verdict: ACCEPT
git merge-base --is-ancestor 4454feab… HEAD && echo YES                    # YES
git log -1 --format='%ad' --date=iso orchestrator -- runtime/agent_card_registry.md
#   2026-08-18 16:05:46      ← one day BEFORE the execution commit of 2026-08-19 15:08:55

# P-6 — the binding determination revision 1 never named
grep -n "No actor authority may be assumed" governance/decisions/DEC-20260822-*.md   # 305
git cat-file -p e88dc043… | grep -c DEC-20260822                # 0   control → 11

# P-7 — and 🔴 a control of MINE that failed, and had to be replaced
D=disease-models/wwox/research/commit_candidates
ls $D | grep -c '^CC-'                                          # 16  population
grep -rl MIRROR_REVIEW $D | wc -l                               #  0 of 16
grep -rl CANDIDATE_ID  $D | wc -l                               #  0 of 16  ← MY CONTROL DID NOT
                                                                #    FIRE. The absence was
                                                                #    UNVALIDATED until replaced.
grep -rl "COMMIT CANDIDATE" $D | wc -l                          # 15 of 16  ← control fires
sed -n '45,48p' governance/annex_d_commit_batch.md              # D.3 GATE 0: lease ACTIVE singleton
python3 framework/scripts/lease_state.py                        # ACTIVE by derivation: 0
```

> **One of my own controls failed inside this register.** The first positive control for P-7
> (`CANDIDATE_ID`) returned 0 of 16, so the measured absence of `MIRROR_REVIEW` proved nothing
> until a control that could fire replaced it. **It is recorded rather than quietly re-run**, because
> a register that shows only the sweeps that worked teaches the next reader that sweeps work.

---

## 2 · Hostile review — H-1 … H-27

**Verification:** `RE-DERIVED` = reproduced mechanically by this session · `READ` = confirmed
against revision 1's own text · `AS REPORTED` = carried on the reviewer's evidence.
**Disposition:** `ACTED` = revision 2 changes the design · `PARTLY` = the fixable half is fixed and
the rest is declared · `ACCEPTED / NOT FIXABLE HERE` = true, and no instrument in this repository
can fix it · `SCOPED` = the operator's call.

| # | § of rev 1 | Finding | Verified | Disposition in revision 2 |
|---|---|---|---|---|
| **H-1** 🔴 | 4.2 | **The derivation is total and is not a function: 28 of 63 subsets match two rules**, 7 of them irreducibly, all containing `captions_only`. `{captions_only, not_present, unavailable}` printed `PARTIAL` — *partial progress* over a layer where zero data was seen. v1 was 8 undefined / 0 ambiguous; revision 1 was 0 / 28. **The defect class was traded, and only the half that was named got verified** | **RE-DERIVED** | 🔴 **ACTED** — § 4.2 is now an **ordered decision procedure, first match wins**, total and single-valued by construction. **This is the most instructive finding of either review**: it is about verifying the clause you were told about instead of every clause |
| **H-2** 🔴 | 4.1 | **A supplementary figure's caption belongs to two layers** — the table put all captions in `TEXT_LAYER`, the container rule puts it in `SUPPLEMENTARY_LAYER`. Verbatim the shape of F-7a. Load-bearing: under the table's reading a paper with unavailable supplementary could never be `FULL_TEXT_READ_COMPLETE` | READ | **ACTED** — § 4.1 places supplementary captions in `SUPPLEMENTARY_LAYER` |
| **H-3** 🔴 | 4.1 | **The front/back-matter list is an enumeration with no residual clause**, while the partition rule demands totality. Unlisted real units: Author Contributions, keywords, abbreviations, licence, ORCID, the graphical abstract, and **Extended Data figures**, which are neither main-article nor publisher-supplementary. F-7b was fixed by extending an enumeration, so the defect recurs one enumeration deeper | READ | **ACTED** — a residual clause, and a recorded determination for Extended Data |
| **H-4** 🔴 | 4.3 | **§ 4.3 states the mandate's rule and violates it three lines above**: one `G-3` anywhere revoked `FULL_TEXT_READ_COMPLETE` for the whole paper. And since § 4.4 offers withdrawal as an alternative, **withdrawal became the costless option — a thinning incentive created by the classification itself** | READ | **ACTED** — `G-3` is removed from the predicate. It constrains its claim, never the paper; `CRITICAL_ASSET_GAP` is reported beside, not inside |
| **H-5** 🔴 | 4.4 | **The `G-1` cross-check moved the checker and not the inputs** — it greps the reader's claim texts and the reader's own locator snippets, so snippet selection defeats it. Worked case that survives: a `DATO` anchored to *"quantification is provided in the Supplementary Information"* with no unit number. And the second route asks an auditor holding only the source, who cannot separate *rests on a missing unit* from *rests on nothing* | READ | **ACTED** — the cross-check now runs **over the frozen source**, on a fixed sentence window, including generic reference forms. The input is not authored by the reader |
| **H-6** 🔴 | 5.2 | **The paired comparison's central sentence is false.** *"The ONLY difference is the anchor"* — while the stages are different auditor sessions and the measured quantity is the auditor's work. n = 1 session per stage, against a design that declares session variance inseparable elsewhere | READ | 🔴 **ACTED** — the **2×2 crossover**: auditor is balanced across conditions by construction |
| **H-7** 🔴 | 5.2 · 7 | **BL-1 is near-tautological — v1's fatal defect relocated.** Stage 2 hands the answer key; following a pointer is cheaper than searching for *any* pointer, correct or not. The unfavourable branch is reachable essentially only through auditor pathology, and when anchors are wrong the information is in the **verdict**, not the act count | READ | 🔴 **ACTED, and it is the deepest change in revision 2** — the primary stops being a cost and becomes **anchor–grounding concordance**: `CONCORDANT · ANCHOR-ADDS · ANCHOR-MISLEADS · DISCORDANT`, all four reachable. Cost is demoted to secondary |
| **H-8** 🔴 | 10.3 · 6.4 | **The PRIMARY criterion's second conjunct is undefined — F-1's shape recurring.** `UNGROUNDED` was defined for stage 1 only and compared across stages. And the five skill verdicts are verdicts **on triples**, so the bare condition cannot produce `UNVERIFIABLE_SURFACE`: "verdict distribution per stage" spanned two incommensurable vocabularies | READ | **ACTED** — `UNGROUNDED` defined for both conditions; S-3 states the vocabularies separately |
| **H-9** 🔴 | 6.2 | **"One act" is not tight enough for two auditors to agree**, and batching collapses the numerator by construction: one linear read grounding 20 claims may log 1 act or 20. No calibration, no worked example, no control. **And `SURFACE-LITE` — the recommended option — makes the source a single PDF, where "one section opened" is not an event** | READ | **PARTLY** — the definition, a worked example and the act-list format become the § 9.7 schema, authored before Φ0; **the crossover makes each auditor's convention cancel within-auditor**. Two auditors still need not agree, and § 6.3 says so |
| **H-10** 🔴 | 6.2 | **The numerator is self-logged by the party it measures, and revision 1's disposition of F-3 marked that FIXED without addressing it.** F-3's original text ends *"the numerator is self-logged by the auditor with no corroborating source"*. No phase assigned the claimed third-party re-derivation to anyone | READ + register cross-check | **ACCEPTED / NOT FIXABLE HERE** — corroborated independently by P-12: no transcript is retained anywhere. § 6.3 now labels the act list **a self-report with a declared slot, not an observation** |
| **H-11** 🔴 | 5.3 | **The stage-2 auditor knows what anchors are for and produces the half predicted to be lower** — demand characteristics on the primary, undeclared among the contaminations | READ | **ACTED** — declared as **K-4**; the crossover reduces it, since neither auditor is the sole producer of the favourable half |
| **H-12** 🔴 | 5.4 | **Nothing sealed the claim set between the stages, and B-6 invited breaking it.** Resolving a `NOT_IN_SOURCE` between stages changes the proposition stage 2 audits — **breaking the pairing precisely on the claims most expensive at stage 1**, moving the primary in the favourable direction at zero cost, with no detector | READ | **ACTED** — the crossover has no *between*; B-6 resolution happens after both conditions are audited |
| **H-13** 🔴 | 2.1 | **The independence rule fails against the phase sequence.** Φ10 is gated by B-7 and B-9, and V-3/V-4/V-5 make `VERIFIED` a function of the audit — so if the audit is void, no candidate can be sealed. The rule was proved on one TRACK-M failure and asserted for all | READ | **ACTED** — § 2.3 replaces the rule with a **declared degradation ladder**, whose floor is a `READING RECORD`: anchored and typed, checked by nobody, explicitly not proposed for any canonical file |
| **H-14** 🔴 | 9.1 Φ8 | **The TRACK-S judge authored a TRACK-M instrument.** A lenient R2 reviewer produced both a favourable science verdict and the record that would have caught TRACK-M gaming | READ | **ACTED** — the substance record moves to **Mirror**, cross-checked by the R2 reviewer. The dependency is inverted |
| **H-15** 🔴 | 2 | **The separation is declared and never implemented** — 7 of 1074 lines, **0 in the phase table, 0 in the blocks, 0 in the success/failure criteria**, against a control of 6 for `Plan` in the phase table alone | **RE-DERIVED** | **ACTED** — a track column on every phase, a track on every block, § 10.1–10.2 stated per track |
| **H-16** 🔴 | 2.2 | **Five reachable failures missing from the attribution table**, and one row's named disambiguator cannot disambiguate — § 6.5's artifact holds no counterfactual about what another reader would have carried | READ | **ACTED** — five rows added (bad enumeration · act-counting divergence · **the audit rubber-stamps, which nothing detects** · undeclared loose-object write · Plan is wrong); the "few claims" row now reads `NOT ATTRIBUTABLE` |
| **H-17** 🔴 | 8.4 | **Plan is an unchecked single point of failure across all of TRACK-M** — 6 of 17 phases, including the denominator and both outcomes — and the ladder claimed `MINIMUM VIABLE` delivers D-TRACE while cutting the phase that measures it | **RE-DERIVED** | **PARTLY** — § 9.3 adds an independent second enumeration on the denominator; § 8.3 corrects the ladder and names what each cut actually removes. **Five Plan-owned phases remain unchecked, and § 2.4 declares it** |
| **H-18** 🔴 | 6.5 | **The thinning test fixes one of the three defects its own heading names** — it supplies the output and neither a threshold nor a consequence; `thinn*` fires in **0 of 12 blocks and 0 items of the failure list**; its key input is supplied by the party being tested; and `MODEL-MOVING` is defined against a file the trial does not reach | **RE-DERIVED** + READ | **PARTLY** — a consequence now exists: **a thinning finding voids the primary and the outcome says `PRIMARY NOT INTERPRETABLE`**. The threshold remains absent and `MODEL-MOVING` remains a judgement; § 6.6 states both as limits rather than closing them |
| **H-19** 🔴 | 7 | **"Three real baselines" is one under the recommended configuration.** BL-3 is **verbatim D-REV**, counted once as a dimension and once as a baseline, with a comparator inside the system under test; BL-2 is optional and D-7 recommends against it | READ | **ACTED** — BL-3 deleted as a baseline, kept as the dimension it was. § 7 states plainly that the recommended run has **one** |
| **H-20** | 7 | **A negative restated without its scope** — 297 is `disease-models/wwox` + `framework/eval`, not the repository's 581 tracked files | **RE-DERIVED** | **ACTED** — scope restored, and § 6.1 gains a standing rule: every negative carries its denominator **and its scope** |
| **H-21** | 9.2 · 9.3 | **7 of 7 sourced figures appear in the body with 0 routes in the verification trail**, against the record's own rule 3 — and they carry decisions D-5 and D-6. Separately, `SURFACE-LITE` was priced in **minutes**, the unit § 6.2 rejects and § 6.6 labels `NOT RELIABLE` | **AS REPORTED** (the 7-figure audit was not re-run here) | **ACTED** — § 9.2 and § 9.3 re-derive the figures with their routes and name the precedent they come from; `SURFACE-LITE` is described by its steps, not in minutes |
| **H-22** | 4.2 | **The six-state alphabet is a per-`COVERAGE_KEY` vocabulary applied per unit.** `not_present` is degenerate for an enumerated unit, so `COMPLETE` reduces to "every unit `read`" and `G-0` asks Plan to enumerate units the paper does not have | RE-DERIVED (script source) | **ACTED** — declared as a scope note in § 4.2 rather than papered over |
| **H-23** | 4.2 | **Totality was verified over non-empty subsets only.** A layer with zero units — the case § 4.5 clause 3 depends on — resolves to `COMPLETE` by a vacuous quantification never stated | **RE-DERIVED** | **ACTED** — a distinct value, `NOT_PRESENT_IN_PAPER` |
| **H-24** | 12 · 14 | **§ 12 clause 1 performs the exact write class B-8 says no instrument sees**, and § 14's non-acts list does not disclose it. The object is reachable from **0 refs** | **RE-DERIVED** | **ACTED** — § 12 clause 6 discloses both loose-object writes, § 3.5 records that nothing detects them, the friction log must log every one, and **D-13** puts preservation to the operator |
| **H-25** | 4.3 | `EXTERNAL_ASSET_LAYER` sat outside the mandatory-gap-class clause while Φ4 and V-4 included it. An unretrieved deposited dataset carrying a `DATO` sat in the seam | READ | **ACTED** — every uncovered unit of every layer takes a gap class |
| **H-26** | 10.3 | The PRIMARY criterion was a **conjunction** whose falsifier negated only the first conjunct — the middle case had no sentence | READ | **ACTED** — a tie and a `DISCORDANT` plurality are named outcomes |
| **H-27** | 10.5 | *"the first written acquisition method in this repository"* — an unrouted repository-wide negative with no denominator and no control, in the record that forbids exactly this | READ | **ACTED** — the superlative is deleted; the claim is now that the declaration is reusable by future readings of this paper |

### 2.1 · What the hostile review found nothing wrong with

§ 1.2 and D-1 (path C decided by measurement — *though the feasibility review then falsified one of
its premises*) · § 8.2 (refusing to record the reviewers as *Mirror* and *Plan*) · § 9.4 (the
freeze's honesty block — *"the shape that should become the template for every attested-not-proven
claim in this laboratory"*) · § 6.7 (the friction log) · § 12 clauses 2–5.

### 2.2 · What it said to preserve

Stage 1's bare-proposition presentation, *"the one genuine instrument advance"* — **kept, as the
crossover's bare condition** · the denominator being *claims audited* · § 9.4's four-line honesty
block — **now applied to the audit too, per P-13** · § 6.1 rules 4 and 5 · declaring `UNGROUNDED` as
invented · § 3.3 + Φ1e · § 10.4's deletion rather than softening · the decay note and the
population/object class distinction · **§ 11's discipline of dispositioning every finding, whose
value the reviewer judged greater than the cost of the places it got them wrong.**

---

## 3 · Feasibility review — P-1 … P-17

> **Verdict, verbatim: `FEASIBLE WITH NAMED CHANGES`**, bound to blob `e88dc043…`.
> **Phase most likely to stall: Φ7a**, the bare-proposition audit — *"the phase with the least
> existing anything"*, and if it stalls TRACK-M produces nothing at all.

| # | Sev | § of rev 1 | Finding | Verified | Disposition in revision 2 |
|---|---|---|---|---|---|
| **P-1** | **BLOCKER** | 3.5 · Φ1b | **`fulltext_receipts.py record` re-anchors `framework/state/state_manifest_current.md` on every append**, inside the lock — a path revision 1's allowlist never names (0 occurrences; control `SURFACE-LITE` → 11). **Φ1b trips the trial's own B-8 on the trial's second phase** | **RE-DERIVED** | 🔴 **ACTED** — the path is in the allowlist, unqualified |
| **P-2** | **BLOCKER** | 3.5 | **The receipt ledger is `disease-models/wwox/registries/fulltext_read_receipts.jsonl`**, which revision 1's allowlist qualified *"ONLY via `BATCH_COMMIT`, after the gate"* — while Φ1b and Φ4 both write it long before, and the trial is designed to stop before the gate | **RE-DERIVED** | 🔴 **ACTED** — unqualified in the allowlist |
| **P-3** | MAJOR | 5 · Φ7a | **Φ7a's instrument does not exist in any form.** The audit skill is 102 lines of prose defined over triples, whose own cost argument is *"it never re-reads the paper"* — and the bare condition **is** a re-read. Its output has no act column and no `UNGROUNDED`. **`retrieval act` fires on 0 tracked files** (control `UNVERIFIABLE_SURFACE` → 3). **Revision 1 applied the framework-construction test to § 4 in four clauses and never applied it to § 5, which is the larger construction** | **RE-DERIVED** | 🔴 **ACTED** — § 9.7 declares the instrument **new, trial-local and unexercised**, prices it beside Φ1d, and requires a written `TRIAL-001-AUDIT-SCHEMA.md` **before Φ0**. No script is built — that would be F-1 firing. **D-14** puts it to the operator |
| **P-4** | MAJOR | 9.2 | 🔴 **`SURFACE-LITE`'s premise is false, and the precedent revision 1 cites is what refutes it.** 10 tracked files carry the identifier; `literature_tracking_log_current.md` carries *"PMID 28123895 (C1q → attivazione WWOX, coda HIGH)"* at lines 11914 and 12045; and `BENCH-AB-001`'s own `forbidden_prior_output_paths` **names that file** plus `full_text_queue_current.md` and `surface_census.md`. **The mechanism revision 1 called vacuous is the mechanism built for this exact leak** | **RE-DERIVED** | 🔴 **ACTED** — `W-2`. `SURFACE-LITE` keeps the recommendation and loses the argument: it now carries a **named forbidden list, measured and re-enumerated at Φ0**, and the two contaminating lines are quoted into the Φ1e check |
| **P-5** | MAJOR | 1.2 · D-1 | 🔴 **D-1's decisive evidence is one day stale.** `REV-SCIAB-MIRROR-006` = `ACCEPT` (2026-08-19); commit `4454feab` *"The Scientist A/B specification becomes canonical"* **is an ancestor of HEAD** and landed `scientist_reading_modes.md`, `roles/scientist.md` and the `BENCH-AB-001` packet. Revision 1 read the candidate manifest, frozen at submission. **The conclusion survives; one of its four premises is measurably wrong** | **RE-DERIVED** | 🔴 **ACTED** — `W-1`, stated first in revision 2 before anything else. The answer stays **C**; § 1.2 rebuilds it on `DEC-20260822`, the C-9 hold, the lease, and a registry that is **stale rather than authoritative** |
| **P-6** | MAJOR | 8.1 | **Revision 1 names `DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE` zero times** (control → 11). That binding operator determination returns `ACTIVATION_NOT_CONFIRMED` and states *"No actor authority may be assumed from these contracts"* — while revision 1 marked Plan *"✅ mechanically"* and Mirror *"✅ for R4"*. **Plan owns 6 of 17 phases** | **RE-DERIVED** | 🔴 **ACTED** — the determination is in the frontmatter and governs § 8.1, which now separates *what traces to an instrument* (permitted) from *what would trace to a contract clause standing alone* (not) |
| **P-7** | MAJOR | 9.5 B-10 | **B-10 measures the wrong object class.** `MIRROR_REVIEW` is an Annex **D.2** field for governance `INTEGRATION_CANDIDATE` manifests; over the **16** scientific `CC-*` candidates Φ10 produces it fires **0 of 16**. Meanwhile a stronger blocker goes unnamed: **Annex D.3 GATE 0 requires `lease ACTIVE singleton`, and 0 are ACTIVE** | **RE-DERIVED** (after replacing a control of mine that did not fire) | 🔴 **ACTED** — B-10 retargeted; **D-11's recommendation is unchanged and its reason is replaced** |
| **P-8** | MODERATE | Φ1e | **Φ1e consumed a "frozen abstract" no phase produces**, and none exists locally: `abstract_parts` for this PMID is `[]`, and **0 of 706** corpus records carry a non-empty one | **AS REPORTED** (the 706 figure not re-run) | **ACTED** — Φ1b now retains the abstract as a named output; Φ1e consumes it |
| **P-9** | MODERATE | Φ3 | **Φ3's `HANDOVER` block is defined only inside `benchmark_manifest.json`**, which `SURFACE-LITE` does not build — so under the recommended configuration Φ3's artifact is a block with no file, and the rule *"a phase that produced no artifact did not run"* bites it | **AS REPORTED** | **ACTED** — the handover block moves into the trial's own record |
| **P-10** | MODERATE | 9.3 | **Φ1d is priced by importing a strictly narrower precedent**: the precedent enumerates **8 unit kinds**, none of them abstract, introduction, discussion, limitations, references, captions, main tables or front/back matter, and has no external-asset register. **§ 4.1 specifies at least 21 across four layers** | **AS REPORTED** | **ACTED** — § 9.3 states the enumeration is a **strict superset** of the precedent and the largest hand-labour item in the design |
| **P-11** | MODERATE | D-3(d) | **`pmc_pow_fetch.py` takes `url output`, not a PMCID**, and its own docstring calls it *"a retrieval of last resort"* reached only after E-utilities and the OA package service. **Revision 1's correction of B-2 is right; the route it named is the last tier, inverted** | **RE-DERIVED** (`--help` run) | **ACTED** — D-3 corrected; the recommendation moves to operator-supplied PDF or `find-fulltext` |
| **P-12** | MODERATE | 6.2 | **The act-list numerator ends where the minutes it replaced ended**: no transcript is retained anywhere — 114 tracked files use the word, no directory holds one — so *"derived by someone else"* has no source object. **Genuinely better than minutes; still a self-report** | **AS REPORTED** | **ACCEPTED / NOT FIXABLE HERE** — § 6.3 labels it exactly that. Corroborates H-10 independently |
| **P-13** | MODERATE | 5 vs 9.4 | **Asymmetric honesty.** The freeze gets a rigorous `GUARANTEE_PROVIDED: none` block; the audit gets none — although its property is *less* detectable, since no transcript survives. § 9.6 asks Mirror *"did the stage-2 auditor see stage 1?"*, **a question with no answerable evidence** | READ | **ACTED** — § 5.3 gives the audit the same block, and § 9.6 now records that the question has no answerable evidence rather than implying it can be answered |
| **P-14** | MINOR | M-5 | **M-5's published command misleads a replayer**: it measures one file. Over the real population of **51 scripts**, 11 contain the token in 25 occurrences — every one a different sense. **The conclusion is confirmed on the wider denominator; the command, re-run as published, looks like a refutation** | **AS REPORTED** | **ACTED** — M-5 restated on the 51-script denominator with the senses named |
| **P-15** | MINOR | 10.1 vs 8.4 | **§ 10.1 required "every phase produced its named artifact" unconditionally**, while § 8.4 offered rungs that remove phases — so the success criterion could not be satisfied under cuts the design recommends | READ | **ACTED** — § 10.1 is scoped to the chosen rung |
| **P-16** | MINOR | 3.5 · 8.3 | `reviews/trial-001/` and `framework/eval/benchmarks/TRIAL-001/` do not exist | **RE-DERIVED** | **CONFIRMS a stated gap** — D-8 creates the first; the second only under `SURFACE-FULL` |
| **P-17** | MINOR | — | **A PreToolUse Bash guard is armed**, denying blanket staging and inline-heredoc repo writes, so every trial artifact must be authored through `Write`/`Edit`. Real per-artifact friction the design did not price | **RE-DERIVED** | **ACTED** — priced in § 6.7 |

### 3.1 · 🔴 What the feasibility review found **understated** — corrections in LEGEND's favour

A review that only finds fault in one direction was looking in one direction. These are recorded
with the same weight as the defects.

| # | Revision 1 was too hard on itself |
|---|---|
| **U-1** | **The Scientist A/B specification is canonical** (P-5). B is still unavailable — but the laboratory is further along than revision 1 said |
| **U-2** | **The physical seats exist.** `git worktree list` shows `lettore`, `lettore-b`, `lettore-c`, `mirror`, `orchestrator`, `evidence-index` — all six, on their named branches. Revision 1 reads as though nothing is built; the worktrees, branches, protocol, benchmark packet and role contract all exist on disk |
| **U-3** | Revision 1 wrote *"16+ times"* for the wall-clock failure. Measured: **23 tracked files.** Conservative, correctly |
| **U-4** | **The v1 `deepdive_manifest` fix is real**, confirmed with a control: revision 2's form parses and returns a domain verdict (exit 1, `[BLOCK] no work manifest`) where v1's returned an argparse error (exit 2); on a PMID with a manifest it returns `VERDICT: PASS`, exit 0 |
| **U-5** | **M-4's predicted decay held.** Revision 1 wrote *"M-4 is already decaying by being written"*; the reviewer measured 4 working-tree files where revision 1 reported 3, **for exactly the reason revision 1 named**. Same for `UNVERIFIABLE_SURFACE` (7 vs 6). This is the discipline working |
| **U-6** | **The act list satisfies the repository's own `OBLIGATION_WITHOUT_ARTIFACT_GATE`**, which requires that an obligation producing no output of its own be given a required slot. Revision 1 does this correctly and never claims credit for it |
| **U-7** | **Φ6 is the design's strongest phase.** All five mechanical checks exist, take their flags, and pass today: `legend_lint` PASS · `fulltext_receipts verify` OK/128 · `growth_anchors` PASS · `locator_audit --strict` 0 quotes missing · `dossier_quote_audit` clean |
| **U-8** | **The decision table is the strongest section in the record** — 12 decisions, **4 truly blocking**, 8 with a stated default. Better than v1's |

### 3.2 · The load-bearing claim, tested and split in two

> Revision 1: *"The audit needs no actorhood… the measuring apparatus is exactly the part that is
> available today."*

**The actor half is true** — an auditor is a subagent with no session history, which is the
mechanism the audit skill already prescribes; no registration, lease, L2 or `ACTOR_ID` is required.
**The apparatus half is false**: stage 2's instrument fits, stage 1's does not exist in any form,
and the primary's numerator has never been recorded by anything on any ref.

**Revision 2 adopts the reviewer's replacement sentence**: *auditor **actorhood** is free; the
auditing **instrument** for the bare condition is entirely new construction. The design's best
insight was true about the actor and was stated about the apparatus.*

---

## 4 · Findings this register adds of its own

| # | Finding | Disposition |
|---|---|---|
| **Y-1** 🔴 | **Revision 1 carried a figure from a report and presented it as measured.** Its path-C recommendation rested on *"revision 6, five `REQUEST CHANGES`, no `PASS`"* — which the v1 register marked `AS REPORTED`, and which is false. **The record whose § 11 claims nothing is carried because it was in v1 carried v1's central feasibility finding without re-running it.** The rule it violated is its own | **ACTED** — W-1, stated before anything else in revision 2 |
| **Y-2** | **A true measurement was used to support a different predicate.** `NEVER_ANALYZED` (0 of 8 analysis surfaces, deliberately excluding triage lists) was correct; `NO_PRIOR_LEGEND_OUTPUT` was inferred from it and is false. **The two differ by exactly the surfaces the sweep excludes on purpose**, and nothing in revision 1 marked the step between them | **ACTED** — W-2; § 3.1 now states both predicates separately |
| **Y-3** | **A write allowlist was authored without reading what the instruments write.** Two BLOCKERs, both discoverable by opening one file. **The allowlist is the trial's own drift detector, and it was the least-verified object in the design** | **ACTED** — W-3; § 3.5 is now derived from the tools |
| **Y-4** | **My own positive control failed inside this register** (§ 1, P-7). Recorded rather than quietly re-run | closed by replacement |
| **Y-5** | **A negative control that is clean in one scope is not clean in another.** `99999999` fires on **4 tracked files** repo-wide — all `test_*.py` fixtures — while being a valid negative on the 8 analysis surfaces, the only scope it was used in. **The repo-wide sweep for the trial paper therefore has no clean negative**, and is reported as an enumerated set of 10 named files rather than as a count | **ACTED** — recorded in revision 2's § 15 |
| **Y-6** 🔴 | **Both reviews are bound to bytes no ref preserves.** Blob `e88dc043…` is reachable from 0 refs and is gc-prunable. A `git gc` orphans both reviews and this register's `reviewed_object` becomes unresolvable | **OPEN — D-13.** Preservation is a commit, which is the operator's act. **Not performed: it was not asked for** |

---

## 5 · Disposition rules — fixed before the findings arrived

1. Every finding is **registered** with its reviewer and the blob it was made against. ✅
2. **None is corrected inside the reviewed object.** ✅ — blob `e88dc043…` is unedited; integration
   produced a successor.
3. A finding the design declines to act on says **why**. ✅ — three are `ACCEPTED / NOT FIXABLE
   HERE` (H-10, P-12, and H-18's threshold), each with the measurement that shows why.
4. **A finding is not a blocker unless the operator makes it one.** ✅ — neither reviewer holds
   authority over this record, neither was asked for one, and neither claimed one.

> **Nothing in this register repairs the repository.** `main`, the four scientific current files,
> `governance/`, `roles/`, `framework/` and `ledger/` are all unchanged. The only files this session
> wrote are the two records under `learning/orchestrator/`, and the two loose git objects disclosed
> at § 12 of the successor.
