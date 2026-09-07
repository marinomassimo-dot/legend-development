---
record_type: TRIAL_DESIGN_PROPOSAL
record_id: LEGEND-FIRST-OPERATIONAL-TRIAL-DESIGN-V2
trial_id: TRIAL-001
task_id: LEGEND_FIRST_OPERATIONAL_TRIAL_DESIGN_v2
title: First operational trial of LEGEND — design v2, revision 2, after the hostile and feasibility reviews of revision 1
revision: 2
author: unregistered session — no role contract, no ACTOR_ID
session_ref: legend-public-ae [989694]
actor_id: NOT ESTABLISHED — a session cannot resolve its own actorhood
dispatcher: operator
date: 2026-08-23
status: PROPOSED — REVIEWED, INTEGRATED, NOT APPROVED
binding: NO
ACTIVATION: NOT_REQUESTED
APPROVAL: NOT_GRANTED
AUTHORITY_CLAIMED: none
governance_version: 3.1.1 — read, cited, not exercised and not modified
activation_state_governing_this_record: >
  DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE, status BINDING_AS_AN_OPERATOR_DETERMINATION_OF_STATE,
  returns OPTION B `ACTIVATION_NOT_CONFIRMED`. Consequence 2: "No actor authority may be assumed
  from these contracts." Revision 1 never named this record; revision 2 is bound by it throughout.
revision_1_reviewed_object:
  blob: e88dc043180b9db9e6e3cf270a84e13aae5f827f
  size: 85073 bytes · 1074 lines
  retrieve: git cat-file -p e88dc043180b9db9e6e3cf270a84e13aae5f827f
  hazard: >
    🔴 That object is reachable from 0 refs and is gc-prunable (re-derived: `git rev-list
    --objects --all | grep -c e88dc043…` → 0; positive control, HEAD's own CLAUDE.md blob → 1).
    The two reviews are bound to bytes that no ref preserves. Making them durable is a commit,
    which is the operator's act and is decision D-13.
reviews_received:
  - hostile review — 27 findings H-1…H-27, bound to blob e88dc043…, reviewer holds no actorhood
    and is NOT the registered Mirror seat
  - feasibility review — 17 findings P-1…P-17, verdict FEASIBLE WITH NAMED CHANGES, bound to the
    same blob, reviewer holds no actorhood and is NOT the registered Plan seat
review_register_path: learning/orchestrator/TRIAL-002-DESIGN-V2-FINDINGS-REGISTER.md
measured_at: >
  branch `legend-operating-convention-v1` @ 30cb4f3fd700e2aaf6b608e363438f883ddc3760,
  revision 1 measured 2026-08-23T21:18Z–21:21Z, revision 2's re-derivations 2026-08-23T22:0xZ.
consumes_by_blob: >
  design v1     9d744eb7a284c80b7a6a2e1258fd04f1c9d44036
  protocol v1   d5c0d296df69ea5a14426e2da351869959983c7b
  findings reg  ee00195fac0f7c317803120d2a5d335098c33778
  sequence      959b57f4c93ccaed087338e5eaf60677fbbcf5c4
  revision 1    e88dc043180b9db9e6e3cf270a84e13aae5f827f
domain: CONTENT. `learning/` is not among the CONTROL_PLANE_ROOTS of P5.1.
class: WORKING RECORD
---

# LEGEND — FIRST OPERATIONAL TRIAL · DESIGN v2 · revision 2 · `TRIAL-001`

> **PROPOSAL ONLY · NOT AN AUTHORIZATION · ACTIVATES NOTHING · ACQUIRES NOTHING**

---

## 0 · What revision 2 changes, and the three corrections that go against its author

Revision 1 was reviewed twice against blob `e88dc043…`. **44 findings arrived. None was
auto-corrected; every one is dispositioned in the register named in the frontmatter.** Revision 2
is the successor the mandate's step 3 asks for. It does not edit the reviewed blob, which survives
in the object database and is retrievable by the command in the frontmatter.

### 0.1 · 🔴 Three claims of revision 1 that were wrong, stated before anything else

| # | Revision 1 said | Measured | Consequence |
|---|---|---|---|
| **W-1** | *"`CAND-20260818-SCIENTIST-AB-SPEC` is at revision 6 after five consecutive `REQUEST CHANGES` with no `PASS` ever recorded"* — the load-bearing premise of the path-C recommendation | 🔴 **False.** `REV-SCIAB-MIRROR-006` reads `verdict: ACCEPT — M-5 is closed`, dated 2026-08-19. Commit `4454feab` — *"The Scientist A/B specification becomes canonical"*, 2026-08-19 15:08:55 — **is an ancestor of HEAD** and landed `framework/protocols/scientist_reading_modes.md` (which fixes the identities of `scientist-a` and `scientist-b`), `roles/scientist.md` and the whole `BENCH-AB-001` packet. The registry that says `NOT_REGISTERED` **predates the execution by one day** (2026-08-18 16:05 vs 2026-08-19 15:08) | **The answer stays C. The reason changes** — § 1.2 |
| **W-2** | *"for a paper measured at 0 of 8 analysis surfaces there is no prior LEGEND output to blind a reader from"* — the premise of `SURFACE-LITE` | 🔴 **False.** `git grep -lE "28123895\|PMC5214935" HEAD` → **10 tracked files**, and `literature_tracking_log_current.md` carries the contaminating inference **verbatim, twice**: *"PMID 28123895 (C1q → attivazione di WWOX, coda HIGH)"* at lines 11914 and 12045. `BENCH-AB-001`'s own `forbidden_prior_output_paths` names that file. **The mechanism revision 1 called vacuous is the mechanism built for this exact leak** | `SURFACE-LITE` survives with a **named forbidden list** — § 9.2 |
| **W-3** | a write allowlist that omits what the tools write | 🔴 **False.** `fulltext_receipts.py record` calls `write_state_anchor()` inside its lock, and `default_manifest_path(Path('.'))` resolves to `framework/state/state_manifest_current.md` — **which revision 1's allowlist never names** (`grep -c "state_manifest"` on the blob → 0; positive control `SURFACE-LITE` → 11). And the ledger it appends to is `disease-models/wwox/registries/fulltext_read_receipts.jsonl`, which revision 1's allowlist qualifies *"ONLY via `BATCH_COMMIT`, after the gate"*. **Φ1b would trip the trial's own B-8 on the trial's second phase** | allowlist repaired — § 3.5 |

**W-1 is the one that matters most, and not because of the trial.** Revision 1's § 11 boasts that
nothing is carried because it was in v1 — and then carried v1's `P-1` as fact without re-deriving
it. It was marked `AS REPORTED` in the source register and I read it as measured. **A figure
carried on a report is carried on trust, and this record was written to say exactly that.**

### 0.2 · What revision 2 changes structurally

| # | Change | Findings it discharges |
|---|---|---|
| **R-1** | 🔴 **The two-stage audit becomes a 2×2 crossover.** Two auditors; each receives half the claims anchored and half bare, on complementary sets. Every claim is measured in both conditions by different auditors; every auditor works in both conditions; nobody sees a claim twice | H-6, H-9, H-11, H-12 |
| **R-2** | 🔴 **The primary stops being a cost and becomes an agreement.** *Does the reader's anchor land where an independent grounder lands?* Four cells, all reachable. Acts-to-verdict is demoted to a cost secondary | **H-7** — the deepest finding of either review |
| **R-3** | **The layer derivation becomes an ordered decision procedure**, and mutual exclusion is verified this time, not just exhaustiveness | H-1, H-22, H-23 |
| **R-4** | **The track separation is implemented** — every phase, artifact and block carries a track label; the failure-attribution table gains its five missing rows; the R2 reviewer no longer authors the thinning record it would be judged by | H-13, H-14, H-15, H-16, H-17 |
| **R-5** | **Φ7's instrument is declared new, unexercised, and priced** — revision 1 applied the framework-construction test to § 4 and never to § 5, which is the larger construction | **P-3** |
| **R-6** | **`DEC-20260822` governs the record** — no actor authority is assumed from any role contract | **P-6** |
| **R-7** | **B-10 is retargeted and the real gate named**: the scientific `CC-*` class carries no `MIRROR_REVIEW` at all; what actually blocks a `BATCH_COMMIT` is **Annex D.3 GATE 0's `lease ACTIVE singleton`**, and 0 are ACTIVE | **P-7** |

---

## 1 · Executive summary

### 1.1 · The recommendation

Run `TRIAL-001` as a **single-reader LEGEND loop on PMID 28123895**, under `SURFACE-LITE` **with a
named forbidden-path list**, measured by a **2×2 crossover audit**, with one Annex C `R2` review,
one Mirror R4 on the process, and a COMMIT CANDIDATE that stops at the operator's gate. Report
**two tracks separately**. The unstructured control reader is an optional widening, not the
comparison the result depends on.

### 1.2 · 🔴 The mandate's final question: A, B, or C — re-argued on corrected premises

> **Answer: C.** Revision 1 reached it through a premise that was false (W-1). It is reached here
> through four that were measured today.

| Path | Verdict | Evidence, re-derived |
|---|---|---|
| **A** — assisted scientific reading | **insufficient alone** | A reading with no independent audit produces no evidence about *verifiability*, the one property the mandate's guiding principle names |
| **B** — full multi-agent platform | **not available** — but not for revision 1's reason | The specification **is canonical** (W-1). What is still absent: **(i)** `DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE` returns `ACTIVATION_NOT_CONFIRMED` and states *"No actor authority may be assumed from these contracts"* and *"a new, explicit activation act is required"* — **binding, and revision 1 never named it**; **(ii)** the C-9 hold suspends L2, so no capability reaches `VERIFIED` (`roles/scientist.md` carries **6** `UNVERIFIED`); **(iii)** `lease_state.py` → **`ACTIVE by derivation: 0`**, and Annex **D.3 GATE 0** requires a `lease ACTIVE singleton`; **(iv)** the registry still reads `scientist-a`/`-b` `NOT_REGISTERED` and is **one day older than the execution that would resolve them**, so the registry is stale rather than authoritative — a state nobody has reconciled |
| **C** — progressive | ✅ **recommended** | The auditors need no actorhood. **But their instrument is not free** — see § 1.4, which is the correction P-3 forced |

**C as gates, not as a schedule:**

```
STEP 1   single LEGEND reader + 2×2 crossover audit + operator gate
         needs: no Scientist actorhood · no lease · no L2 lift
         does NOT need a new script — but DOES need a written audit output schema (§ 1.4)

STEP 2   method validation — does step 1's measurement survive replay from the record alone?
         EXIT CRITERION, and it is what authorizes step 3:
           a replay session reproduces every reported figure AND every audit verdict
           without asking the reader or the auditors anything.

STEP 3   multi-agent extension — a second reader, the A/B mode benchmark, Scientist actorhood
         needs, and only then: an explicit activation act discharging DEC-20260822 · the C-9
         L2 hold lifted or scoped · the registry reconciled against commit 4454feab ·
         one ACTIVE lease
```

### 1.3 · Facts measured, with their routes

| # | Fact | Route | Class |
|---|---|---|---|
| **M-1** | **0 ACTIVE leases** (5 recorded; #3 `derived=STALE` vs `stored=EXPIRED`) | `lease_state.py` | population |
| **M-2** | `roles/*.md` — **4 of 4 `PROPOSED`**; `roles/scientist.md` carries **6** `UNVERIFIED`; `DEC-20260822` returns `ACTIVATION_NOT_CONFIRMED` | file reads | object |
| **M-3** | 🔴 **Revision 1's derivation was exhaustive and not a function: 0 of 63 undefined, 28 of 63 ambiguous.** 21 are rescued by reading `UNKNOWN` as absorbing; **7 are genuinely ambiguous and every one contains `captions_only`**. `{captions_only, not_present, unavailable}` printed `PARTIAL` — *partial progress* over a layer where **zero data was seen** | enumeration over all 63 subsets, control = the 6 singletons reproduce the 6 intended answers | object |
| **M-4** | **PMID 28123895: 0 of 8 analysis surfaces** (positive control 42397075 → 5 of 8; negative control 99999999 → 0 of 8) — **but 10 of 581 tracked files repo-wide**, two of which carry the prior inference verbatim | the T-9-corrected sweep, then a repo-wide grep | population |
| **M-5** | **No instrument enumerates layers.** Over the real population of **51 scripts** in `framework/scripts/`, 11 contain the token `layer` in **25 occurrences, every one a different sense** ("PDF text layer", "reasoning layer", "graph layer"). `TEXT_LAYER\|FIGURE_LAYER\|SUPPLEMENTARY_LAYER` → **0 tracked**; `EXTERNAL_ASSET_LAYER` → **0**; positive control `COVERAGE_KEYS` → **5** | corrected from revision 1's single-file command (P-14) | object |
| **M-6** | **`MIRROR_REVIEW` is absent from the object Φ10 produces.** Population: **16** `CC-*` scientific candidates. `MIRROR_REVIEW` → **0 of 16**; `CHANGE_CLASS` → **0 of 16**; **positive control `COMMIT CANDIDATE` → 15 of 16**; negative control → 0. *(Revision 2's first attempt at this used a control that did not fire, so the absence was not yet validated; it is now.)* | greps with a control that fires | object |

---

## 2 · Separation of objectives — implemented, not declared

### 2.1 · Two tracks

| | **TRACK-M · method** | **TRACK-S · science** |
|---|---|---|
| **Question** | Does the LEGEND process produce a reading that is cheaper to check, and whose defects are findable by someone who was not there? | What does PMID 28123895 establish about C1q and WWOX; on what measured intermediate; and what, if anything, transfers to a loss-of-function neurodevelopmental context? |
| **Deliverable** | `TRIAL-001-OUTCOME-M.md` | `CC-TRIAL001-*`, or a documented `DISMISSAL` |
| **Judged by** | the crossover audit + Mirror R4 | the Annex C `R2` reviewer |

### 2.2 · 🔴 The label is carried by every phase, artifact and block

Revision 1 declared the separation on **7 of 1074 lines** and implemented it nowhere: **0
occurrences in the phase table, 0 in the twelve blocking criteria, 0 in the success and failure
criteria** — while the control token `Plan` fired 6 times in the phase table alone (H-15,
re-derived). A table that no gate reads is a reading aid.

```
EVERY artifact frontmatter carries:      track: TRACK-M | TRACK-S | BOTH
EVERY phase row in § 9.1 carries a track column.
EVERY block B-* declares which track it halts.
§ 10.1 and § 10.2 are stated PER TRACK.
```

### 2.3 · 🔴 The independence rule — restated, because revision 1's version was false

Revision 1 claimed TRACK-S is usable *"even if TRACK-M's measurement is void"* and proved it on one
instance. H-13 showed it fails on the others: Φ10 is gated by B-7 and B-9, and V-3/V-4/V-5 make a
claim's `VERIFIED` status a function of the audit, the cross-check and the replay. **If the audit
is void, no claim is `VERIFIED` and no candidate can be sealed.**

> **The rule, corrected.** TRACK-S's product degrades **by a declared ladder** rather than
> surviving intact:
>
> | If TRACK-M loses | TRACK-S still yields |
> |---|---|
> | the freeze ordering | the full candidate — the freeze bears on D-REPRO only |
> | one auditor of the crossover | a candidate whose claims are singly-grounded, and says so |
> | **the whole audit** | 🔴 **not a candidate — a `READING RECORD`**: anchored, typed, layer-statused claims that **no independent party has checked**, explicitly not proposed for any canonical file. That object is still worth having and is still a TRACK-S product; it is not a COMMIT CANDIDATE |
> | the `G-1` cross-check | a candidate in which no claim may be typed `DATO` on an asset-dependent anchor |

### 2.4 · Failure attribution — the mandate's question, with the five rows revision 1 missed

*"If the trial failed, would we know what failed?"*

| Observable failure | Track | Evidence about | **NOT** evidence about |
|---|---|---|---|
| the paper cannot be acquired | — | the laboratory's **acquisition capability** | the reading method |
| the reading carries few claims | S | 🔴 **undetermined until § 6.6 runs** — and § 6.6 cannot settle it either, because it holds no counterfactual about what another reader would have carried. **Revision 1 named a disambiguator that cannot disambiguate** (H-16). The honest entry is `NOT ATTRIBUTABLE` | the discipline |
| the audit returns many `NOT_IN_SOURCE` | M+S | the **reader** — unless the reader followed the method and it happened anyway, which is the interesting case and must be said in those words | — |
| the audit returns nothing at all | M | the **auditor** (D-REV falsifier) | a clean reading |
| 🆕 **the audit returns `SUPPORTED` and is wrong** | M | 🔴 **nothing detects this.** There is no gold set and no adjudication of the auditor. Declared as an undetected failure mode, not attributed | — |
| 🆕 **the two auditors count "one act" differently** | M | the **act definition** — mitigated by the crossover, since every auditor works in both conditions and its own convention cancels within-auditor (§ 5.3) | the anchors |
| 🆕 **Φ1d's hand enumeration is wrong** | M | the **enumerator** — and both documented enumerator errors on the precedent were enumerator errors. **Guarded by § 9.3's independent second enumeration**, which revision 1 did not have | the reader |
| 🆕 **an undeclared `git hash-object -w` write** | M | 🔴 **self-declaration only** — B-8's filesystem snapshot does not see loose objects, and neither does `git status`. Declared undetectable | — |
| 🆕 **Plan is wrong** | M | 🔴 **Plan owns 6 of 17 phases and nothing checks it.** § 9.3 adds one cross-check on the denominator; the other five phases remain unchecked, and that is a declared single point of failure | — |
| a figure cannot be re-derived by replay | M | the **record**; step 2's exit criterion fails | the reading's correctness |
| the freeze ordering cannot be shown | M | the **instrument** — it does not void the trial | the reader's honesty |
| a mechanical check refuses | M | the **artifact it refused on** | the trial |
| the candidate cannot be sealed | S | 🔴 **the lease**, not `MIRROR_REVIEW` (M-6) | the reading |
| the trial stalls at Φ2 for want of an actor | M | the **multi-agent layer** — the path-C finding | the method |
| a write lands outside the allowlist | M | the trial's discipline — halt | anything scientific |

---

## 3 · The input

### 3.1 · The paper

**PMID 28123895 · Bandini 2016** · `FT-018`, `HIGH`, PMCID `PMC5214935` recorded open.
**0 of 8** analysis surfaces (controls fire); **0 of 174** files in `files/fulltext/`; the queue
carries **72** `^## FT-` headings.

🔴 **And 10 of 581 tracked files carry the identifier**, including `literature_tracking_log_current.md`,
`full_text_queue_current.md`, `surface_census.md`, `batch_queue.md`, four corpus seeds and two
session evaluations. `NEVER_ANALYZED` is true. `NO_PRIOR_LEGEND_OUTPUT` is **false**, and revision 1
inferred the second from the first (W-2).

### 3.2 · Entry criteria

E-1 never analyzed ✅ 0 of 8 · E-2 formed question ⚠️ **contaminated, re-authored — § 3.3** ·
E-3 no local surface ✅ 0 of 174 · E-4 acquirable at zero spend ✅ *(route corrected — § 13 D-3)* ·
E-5 ≥2 taxonomy gates live ✅ three · E-6 has assets worth statusing ⏳ unknown until acquisition,
**and cannot fail the trial** (§ 4.5) · E-7 sized for one session ✅ · E-8 no individual linkage ✅.

Alternates: `FT-017` PMID 39933386, `FT-019` PMID 21444760 — both **0 of 8**. `FT-015` fails E-7.

### 3.3 · The question, re-authored

`FT-018`'s `**Why:**` states *"C1q come regolatore a monte dello **stato di attivazione** di WWOX
(non del livello)"* — a LEGEND inference, made from the abstract, before the reading. Revision 1
removed it from the assignment. **Revision 2 must also keep it out of the surface**, because it is
in the tracking log twice (W-2).

> **The question handed to the reader:** *What, if anything, does this paper establish about the
> relationship between C1q and WWOX in the Her2/neu mammary model? Identify the measured
> intermediates the paper actually reports, state what each does and does not license, and state
> what — if anything — transfers to a loss-of-function neurodevelopmental context.* **"Nothing
> transfers" and "the paper does not establish a C1q→WWOX relationship" are complete answers.**

Three rules: the queue entry is not handed to any reader · the assignment is checked for
prior-conclusion leakage **by someone who is not the reader** · the check is an artifact (Φ1e).

### 3.4 · Scope

```
IN     one paper · one LEGEND reader · 2×2 crossover audit · one R2 review · one Mirror R4
       · one COMMIT CANDIDATE (or READING RECORD, § 2.3) · one operator gate · one friction log
       · one outcome per track · OPTIONAL: one unstructured control reader (§ 7 BL-2)

OUT    a second LEGEND reader · Scientist C and the § 32 synthesis conflict · the MODE A/B
       benchmark · any governance amendment · any PROPOSAL implementation · any schema change
       · any write to governance/, roles/, framework/protocols/, framework/scripts/
       · any new script · any push to a public remote · any paid external service
```

### 3.5 · 🔴 The write allowlist — repaired, after W-3

Revision 1's allowlist would have halted the trial at Φ1b on its own B-8. **The allowlist is now
derived from what the instruments actually write, verified by reading them.**

```
files/fulltext/<the trial paper>*                            (git-ignored; acquisition)
disease-models/wwox/registries/fulltext_read_receipts.jsonl  🆕 UNQUALIFIED — `record` appends here
framework/state/state_manifest_current.md                    🆕 `record` re-anchors it IN-LOCK,
                                                                on every append. Not optional.
disease-models/wwox/research/fulltext_dossiers/…
disease-models/wwox/research/deepdive_manifests/…
disease-models/wwox/research/commit_candidates/…
disease-models/wwox/registries/{claim,paper,…}_current.md    (ONLY via BATCH_COMMIT, after D-11)
learning/orchestrator/TRIAL-001-*
reviews/trial-001/…                                          (does not exist — D-8 creates it)
framework/eval/benchmarks/TRIAL-001/…                        (ONLY under SURFACE-FULL)

🔴 LOOSE OBJECTS. Any `git hash-object -w` write is invisible to `git status` AND to the
   filesystem snapshot of B-8. Every one performed by this trial is DECLARED in the friction
   log at the moment it is made. Nothing detects an undeclared one.
```

---

## 4 · Full text and scientific assets

### 4.1 · The four layers, with a residual clause

> **PARTITION RULE.** Every enumerated unit belongs to **exactly one** layer. **Container wins over
> medium**, and the container is the **publisher's own article record**, not the shape of the file
> that arrived.

| Layer | Contains |
|---|---|
| **`TEXT_LAYER`** | abstract · introduction · methods · results · discussion · conclusions · limitations · reference list · **captions of main-article figures and tables** · main-article textual tables · front and back matter, incl. title, authors, affiliations, funding, conflicts, ethics, acknowledgements and **the data-availability statement** · 🆕 **RESIDUAL CLAUSE: any published unit not assigned by the rules below belongs here, and is listed by name in the Φ1d enumeration so the assignment is visible rather than silent** |
| **`FIGURE_LAYER`** | main-article figures, panels, images, blots, schematics, plots — the data a caption talks about. 🆕 **`Extended Data` figures belong here only if the publisher's record places them in the article; otherwise `SUPPLEMENTARY_LAYER`. The determination is recorded** |
| **`SUPPLEMENTARY_LAYER`** | everything the publisher lists as supplementary, of any medium — 🆕 **including the captions of supplementary figures and tables.** Revision 1 put all captions in `TEXT_LAYER` and thereby placed a supplementary caption in two layers, which is verbatim the shape of F-7a (H-2) |
| **`EXTERNAL_ASSET_LAYER`** | deposited datasets, accession numbers, code repositories, third-party databases, author-held materials. **A register of pointers with a retrieval status.** It never enters `FULL_TEXT_READ_COMPLETE` — 🆕 **and every uncovered unit in it still takes a gap class, closing the seam H-25 found** |

The receipt's single `tables` key spans two layers. **v2 does not change the receipt**; each table
unit is assigned its layer at Φ1d, and the receipt key is a cross-check that may disagree — a
disagreement is logged, not silently resolved.

### 4.2 · 🔴 The status derivation — an ordered decision procedure

Revision 1 stated five predicates and verified only that they were exhaustive. **They were: 0 of 63
undefined. They were also not a function: 28 of 63 matched two rules**, and 7 of those cannot be
rescued by any reading of "absorbing" (M-3). The fix is not another predicate — it is to stop
writing predicates.

```
LAYER STATUS — evaluated over the layer's ENUMERATED UNITS (§ 4.4), FIRST MATCH WINS

  1. any unit `unknown_legacy`                          → UNKNOWN       (never a pass)
  2. every unit `read` or `not_present`                 → COMPLETE
  3. no unit `read`, and ≥1 `captions_only`             → CAPTION_ONLY  (the caption was read,
                                                                        the data was not)
  4. no unit `read` or `not_present`                    → UNAVAILABLE
  5. otherwise                                          → PARTIAL

  TOTAL AND SINGLE-VALUED by construction: the rules are tried in order and the first that
  matches returns. Verified over all 63 non-empty subsets AND the empty set.

  🆕 THE EMPTY LAYER IS NOT `COMPLETE`. A layer with zero enumerated units returns
     NOT_PRESENT_IN_PAPER — a distinct value. Revision 1 reached `COMPLETE` by a vacuous
     universal quantification it never stated (H-23), and § 4.5 clause 3 depended on it.

  🆕 ARITY IS REPORTED, ALWAYS. `COMPLETE` over one unit and `COMPLETE` over forty are not the
     same statement, and `PARTIAL` is unreachable at arity 1 — stated here rather than printed
     as a cell that can never fire.

  🆕 SCOPE OF THE ALPHABET. `COVERAGE_STATES` is a per-SECTION vocabulary in
     `fulltext_receipts.py`. Applied per UNIT, `not_present` is degenerate — an enumerated unit
     exists by construction — so rule 2 reduces to "every unit `read`", and `G-0` is a class the
     Φ1d enumeration cannot produce. Declared (H-22), not papered over.
```

### 4.3 · `FULL_TEXT_READ_COMPLETE` — the mandate's rule, no longer self-contradicting

Revision 1's predicate ended *"AND no `G-3` gap is bound to any carried claim"* three lines above
the sentence *"a missing asset limits **exactly** the claims that depend on it, and nothing else"*.
**One `G-3` anywhere revoked the classification for the whole paper** — the missing asset
invalidating the full text, which is what the mandate's rule forbids. Worse, § 4.4 offered
withdrawal as an alternative to carrying the claim, which made **withdrawal the costless option**:
a classification that creates a thinning incentive (H-4).

```
FULL_TEXT_READ_COMPLETE  ≔  TEXT_LAYER = COMPLETE
                        AND the text is digest-verified against a present artifact
                        AND every uncovered unit of every layer carries a gap class that has
                            passed the § 4.4 cross-check

  🔴 G-3 IS NOT IN THIS PREDICATE. A G-3 constrains its CLAIM (§ 6.4 V-4), never the paper.
  CRITICAL_ASSET_GAP: YES|NO is reported BESIDE this value, never inside it.
  EXTERNAL_ASSET_LAYER never enters it.
```

### 4.4 · Gap classification, and a cross-check the reader does not author

`G-0` not present · `G-1` unavailable, no carried claim rests on it · `G-2` possible claim impact,
claim carried with its limit inline and not typed `DATO` on that evidence alone · `G-3` a **named**
claim cannot be checked without it — that claim is not verified, and survives as `IPOTESI` +
`EVIDENCE_NEEDED` or is withdrawn.

> 🔴 **The cross-check, corrected.** Revision 1 moved the *checker* from the reader to Plan and left
> **both inputs authored by the reader** — it grepped the reader's claim texts and the reader's own
> locator snippets, so snippet selection alone defeats it (H-5). Revision 2 changes the **input**:
>
> ```
> The cross-check runs over the FROZEN SOURCE, not over the reader's output.
>   For each unit classified G-1:
>     1. locate every internal cross-reference to that unit IN THE SOURCE TEXT — including
>        generic forms: "Supplementary Information", "supplementary data", "see Supplementary",
>        "data not shown", as well as numbered forms.
>     2. for each such reference, take the sentence carrying it and its two neighbours.
>     3. if ANY carried claim is anchored inside that window → the G-1 is WRONG. The unit is
>        re-classified G-2 at minimum, and the re-classification is logged with the hit.
>   The source is not authored by the reader. The window is fixed before the reading.
> ```
>
> **Second, independent route:** each auditor is asked, per claim it could not ground, *"does the
> source itself point somewhere you were not given?"* — answerable from the source alone.

### 4.5 · Scope, and what is still the operator's call

The model adds **no field to any schema**; the gap table lives in the trial's own record because the
receipt has no per-unit field; `D-LAYER` reports **`EXERCISED` / `NOT_EXERCISED`, never `PASS`**;
and the model makes **no claim about the repository's 128 receipts** — T-8 stays open and unrepaired.

> 🔴 **But § 4 is still the largest block of new specification here, and the honest statement is
> that revision 1 priced F-8 and handed it to the operator rather than resolving it** (H's reading
> of § 4.5, which I accept). **D-6 offers striking § 4 entirely.**

---

## 5 · 🔴 The audit — a 2×2 crossover

### 5.1 · What revision 1 got right, and what it got wrong

**Right, and preserved:** making blindness a property of the *presentation* — a bare proposition has
no shape that leaks its origin — rather than of an instruction an auditor is asked to honour. Both
reviewers named this as the one genuine instrument advance, and it is kept.

**Wrong, twice.** Revision 1's § 5.2 asserted *"same reader · same source · same claims · the ONLY
difference is the anchor"* while Φ7a and Φ7b were **different auditor sessions** and the measured
quantity was the *auditor's* work (H-6). And the comparison it built — pointer versus search — is
true of any pointer, correct or not, so its "evidence against" branch was reachable essentially only
through auditor pathology: **v1's fatal asymmetry, relocated** (H-7).

### 5.2 · The design

```
  N claims from the reading, in a shuffled order RECORDED BEFORE the audit begins.
  Split into halves X and Y by a pre-recorded assignment.

              condition ANCHORED              condition BARE
              (full triple)                   (proposition + source only)
  AUDITOR 1        X                                Y
  AUDITOR 2        Y                                X

  ── every claim is audited in BOTH conditions, by DIFFERENT auditors
  ── every auditor works in BOTH conditions, so its own counting convention cancels
  ── no auditor sees any claim twice, so nothing is contaminated by memory
  ── total work is 2N verdicts: IDENTICAL to revision 1's two sequential stages
```

**What it fixes.** H-6: the anchor is no longer confounded with the auditor, because auditor is
balanced across conditions by design. H-12: there are no sequential stages, so there is no claim set
to seal between them and B-6's resolution cannot silently change the pairing. H-9: inter-auditor
differences in what counts as "one act" no longer confound the primary, because the comparison is
within-auditor. H-11: neither auditor is the sole producer of the favourable half.

**What it does not fix, declared:** *(K-2)* the auditors are LEGEND-shaped instruments · *(K-3)* an
auditor gets faster at navigating one source, so presentation position is a covariate — the recorded
order makes it visible and the outcome reports per-position figures beside the aggregate ·
*(K-4)* 🆕 an auditor working in the anchored condition may infer the hypothesis under test.
**Undeclared in revision 1, unmitigated here, named in the outcome.**

### 5.3 · 🔴 Blindness is a property of the presentation — and of a withholding nothing enforces

Revision 1 gave the freeze a rigorous honesty block and gave the audit none, while the audit's
property is *less* detectable — no transcript is retained anywhere in this repository (P-13). The
same block is owed:

```
GUARANTEE_PROVIDED:          the BARE condition's presentation is mechanically identical across
                             claims, so it carries no shape that identifies its origin.
                             Everything else is procedural.
FAILURE_MODE_STILL_POSSIBLE: the packet assembler shows an auditor material it should not;
                             an auditor is not fresh; the shuffle is not the recorded one
DETECTION:                   the recorded shuffle and the per-claim act lists make an
                             inconsistency visible; the withholding itself is NOT detectable
                             after the fact, because no transcript survives
CONSEQUENCE:                 the audit is reported PROCEDURALLY_ATTESTED. § 9.6 asks Mirror the
                             question and § 9.6 records that the question has no answerable
                             evidence — which is the honest entry, not a passing one
```

---

## 6 · Metrics

### 6.1 · The rules

No composite, no weighting, no overall score · operational figures never proxy for quality and break
no tie · every figure carries its command, its instant and its class · **every count is an
enumerated set before it is a number** · **every sweep carries a positive control that can fail** ·
🆕 **every negative carries the denominator and the scope it was measured over** — revision 1
restated T-7's negative without its scope, so a reader took 297 for the repository's 581 (H-20).

### 6.2 · 🔴 The primary — an agreement, not a cost

Revision 1's primary was *acts to verdict, anchored versus bare*. **Following a pointer is cheaper
than searching for any pointer, correct or not** — so the measurement was near-tautological and its
unfavourable branch nearly unreachable (H-7). The quantity that is *not* tautological, and that maps
directly onto the mandate's guiding principle, is whether the anchor is **right**.

```
PRIMARY ── ANCHOR–GROUNDING CONCORDANCE, per claim ──────────────────────────
  For each claim, compare:
     (a) the evidence an auditor in the BARE condition independently located
     (b) the anchor the reader supplied, as verified in the ANCHORED condition

  CONCORDANT       both land on the same passage
                     → the anchor points where an independent reader looks
  ANCHOR-ADDS      bare = UNGROUNDED; anchored = SUPPORTED
                     → 🔴 the discipline supplied evidence a searcher would not have found.
                       THE STRONGEST EVIDENCE FOR THE DISCIPLINE, and it is reachable
  ANCHOR-MISLEADS  bare grounded it; anchored verdict ≠ SUPPORTED
                     → 🔴 the anchor points at something that does not support the claim.
                       THE STRONGEST EVIDENCE AGAINST, and it is reachable
  DISCORDANT       both grounded, different passages
                     → adjudicated by the R2 reviewer, reported ENUMERATED with both passages

  REPORTED AS THE FOUR COUNTS AND THE ENUMERATED SETS BEHIND THEM. Never as a single rate.
  All four cells are reachable. Neither direction is structurally favoured.
──────────────────────────────────────────────────────────────────────────────
```

**Why this answers the mandate.** *Tracciabile* = `CONCORDANT` + `ANCHOR-ADDS`. *Verificabile* = the
fraction an independent party could reach a verdict on at all. *Correggibile* = `ANCHOR-MISLEADS`
and `DISCORDANT` — **the discipline's value is that it makes its own errors findable**, and a
measurement with no cell for a findable error measures the wrong thing.

### 6.3 · Cost — demoted to secondary, with its honesty label

**Acts to verdict per claim audited**, per condition, reported as the triple (acts, claims audited,
quotient), never the quotient alone.

> 🔴 **This is a self-report with a declared slot, not an observation.** Revision 1 argued the act
> list is *"re-derivable from the auditor's own transcript by a third party"*. **No transcript is
> retained** — 114 tracked files use the word, no directory holds one (P-12). It is genuinely better
> than minutes (an agent can count its own acts and demonstrably cannot read a clock — measured on
> **23** tracked files, where revision 1 said "16+"), and it is not an instrument reading.
>
> **"One act" is defined before the audit, with a worked example, and the definition is part of the
> Φ7 output schema (§ 9.7).** One access to the frozen source that returns content the auditor then
> reads: one search execution, one section opened, one figure inspected. A search returning twelve
> hits is **one** act; reading three of those hits is **three** more. The crossover makes an
> auditor's convention cancel; it does not make two auditors agree, and the outcome says so.

### 6.4 · Verification — the five conditions

**V-1** typed · **V-2** anchored, digest-matched, quote present (`deepdive_manifest.py --pmid
28123895 --verify-artifacts --require-current-schema`; `locator_audit.py --strict`) · **V-3**
`SUPPORTED` in the **anchored condition** · **V-4** layer-sufficient, no `G-3` bound, after the
§ 4.4 cross-check · **V-5** reproduced by a replay session. **The failure profile is reported per
condition, never as a bare count.**

Not failures, counted apart: `UNVERIFIABLE_SURFACE` · `WITHDRAWN_ON_AUDIT` · `EVIDENCE_NEEDED`.

### 6.5 · Secondary measures

**S-1 `UNGROUNDED`** — 🆕 **defined for both conditions**, since a claim whose anchor is
unresolvable is ungrounded in the anchored condition too. Revision 1 defined it for stage 1 only and
then compared it across stages, which is F-1's shape recurring (H-8). **`UNGROUNDED` fires on 0 of
581 tracked paths — it is a verdict this record invents, and calling it trial-local is not a
formality.** · **S-2** verification-failure profile · **S-3** verdict distribution per condition
🆕 *with the vocabularies stated separately, because the bare condition has no triple and therefore
no `UNVERIFIABLE_SURFACE`* · **S-4** defects the audit caught that the reader's self-check did not,
enumerated · **S-5** layer status, unit counts, gap census · **S-6** `G-3` gaps with their claims,
and every `G-1` the cross-check re-classified · **S-7** taxonomy gate instances with locators.

### 6.6 · Claim substance — and 🔴 the conflict of interest revision 1 built

Revision 1 assigned `TRIAL-001-CLAIM-SUBSTANCE.md` to the **R2 reviewer**, who is also TRACK-S's
judge — so a lenient reviewer produced both a favourable science verdict and the record that would
have caught TRACK-M gaming (H-14). **Revision 2 assigns it to Mirror, cross-checked by the R2
reviewer**, inverting the dependency.

Its required shape: every carried claim marked `MODEL-MOVING` / `CONFIRMATORY` / `INERT` · every
claim considered and not carried, with the reason · the answer in prose to *"was the claim set
thinned to fit the metric?"*

> **Two honest limits, both named by the hostile review and both accepted.** `MODEL-MOVING` is
> defined against a file this trial does not reach (D-11 stops at the candidate), so the category is
> a **judgement, not a measurement**. And item 2 is supplied by the party being tested. **The
> thinning test detects thinning only if the reader reports its own discards accurately**, and no
> instrument checks that. It is a finding-producing artifact, not a gate — 🆕 **and it now has a
> consequence: a thinning finding by Mirror voids the PRIMARY for that trial and the outcome says
> `PRIMARY NOT INTERPRETABLE`**, which revision 1's version had no way to say.

### 6.7 · Operational, and the friction log

Production cost · **blocked time** · token/cost `NOT OBSERVABLE` unless the runtime exposes it,
never estimated · revisions · errors intercepted, a mechanical refusal counting as one · minutes
wherever offered, labelled `NOT RELIABLE`. 🆕 **Per-artifact write friction**: a PreToolUse Bash
guard denies blanket staging and inline-heredoc repo writes, so every trial artifact is authored
through `Write`/`Edit` (P-17) — real friction the design now prices.

`TRIAL-001-FRICTION-LOG.md`, append-only, written during the run and never reconstructed. Mandatory
classes: any forced stop · any figure a receiver had to re-derive because a dispatch's value was
wrong, **both halves logged** · any decision with no owner · 🆕 **every loose-object write**.

---

## 7 · Baselines

| # | Baseline | Runs | Supports | Cannot support |
|---|---|---|---|---|
| **BL-1** | **The crossover** — anchored vs bare, on the same claims, balanced across auditors | always; one reader | 🔴 **the concordance of the reader's anchors with independent grounding** (§ 6.2), and the cost difference as a secondary | anything about readers or papers other than these |
| **BL-2** | unstructured control reader, same paper, same bytes, same question | optional — D-7 | a statement about **claim phrasing**: are LEGEND-disciplined claims groundable more often in the bare condition? | anything about anchoring — the control has none |
| **BL-4** | ~~a remembered traditional-workflow figure~~ | 🔴 **FORBIDDEN** | — | measured: over the **297** tracked files of `disease-models/wwox` + `framework/eval` — **not the repository's 581** — records carrying a measured reading duration = **1**, and it is a molecular-dynamics simulation length. Positive control `receipt` → 160 of 297 |

> 🔴 **Revision 1 claimed "three real baselines" and had one under its own recommended
> configuration** (H-19). Its BL-3 — *"does the blind audit find defects the reader's self-check
> did not?"* — is **verbatim D-REV in § 10.3**, an internal consistency check counted once as a
> dimension and once as a baseline, whose comparator is a component of the system under test.
> **It is deleted as a baseline and kept as the dimension it always was.** With D-7 recommending
> against BL-2, **the recommended run has exactly one baseline, and this record says so.**

**BL-2's contamination (K-1):** the control reader has LEGEND's discipline internalised and will be
better than a naive workflow — biasing **against** LEGEND, the safe direction. **A null result does
not license "the discipline is worthless."**

**Statistics: none.** n = 1 paper. The trial reports raw distributions and states it cannot
distinguish arm from session. *"Arm L is X % better"* is out of bounds in the outcome.

---

## 8 · Roles — under `DEC-20260822`

### 8.1 · 🔴 The determination that governs every row

`DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE`, `status: BINDING_AS_AN_OPERATOR_DETERMINATION_OF_STATE`,
returns **OPTION B `ACTIVATION_NOT_CONFIRMED`**: *"No actor authority may be assumed from these
contracts. Any authority an actor exercises must be traced to the governance body or to a named
annex, never to a role contract clause standing alone."* And: *"A new, explicit activation act is
required."*

**Revision 1 named this record zero times** (control: `SURFACE-LITE` 11) and nonetheless marked Plan
*"✅ mechanically"* and Mirror *"✅ for R4 findings"* (P-6).

| Seat | State | What it may do in step 1 |
|---|---|---|
| **Operator** | — | everything; and is the control plane |
| **reader-L** | `scientist-a`/`-b` `NOT_REGISTERED` in a registry **one day older than the execution that would resolve them**; 6 capabilities `UNVERIFIED`; L2 suspended | ⚠️ **an unregistered capability rehearsal claiming no actorhood** — D-4 |
| **Plan** | registered `REGISTERED_PENDING_L1_L2`; contract `PROPOSED` and **not activated** | ✅ **the mechanical acts** — running a validator, computing a digest, enumerating a population — because those trace to the instrument, not to a contract clause. ❌ **not** anything whose authority would come from `roles/plan.md` standing alone |
| **Mirror** | same | ✅ **producing findings**, which needs no authority. ❌ authorizing anything |
| **Auditors** | none needed — ephemeral, unregistered, identity-withheld **by design** | ✅ — and see § 1.4 / § 9.7 on the difference between the actor and the instrument |
| **R2 reviewer** | AUTHOR ≠ REVIEWER | ✅ if a distinct session |

### 8.2 · Neither review seat was reachable

The registry binds `mirror` → `mirror-9c [3940a9]` and `plan` → `evidence-index-59 [de42c4]`;
**neither was among the 14 live peer sessions** at dispatch, though four `mirror-*` sessions were.
Both reviews of this record were therefore performed by **a hostile reviewer** and **a feasibility
reviewer**, never by *Mirror* and *Plan*, and both said so themselves. **Findings need no
actorhood; authority does, and neither review carries any.**

### 8.3 · Degradation ladder — corrected, because revision 1's understated its own cuts

Plan owns **6 of 17 phase rows** (Φ1c, Φ1d, Φ3, Φ5, Φ6, Φ11) and nothing checks it (H-17).

```
FULL         reader-L + Plan + 2 auditors + R2 reviewer + Mirror + control reader
─ BL-2       … no control reader   → lose the claim-phrasing statement. BL-1 intact.
─ Mirror     … no R4               → lose the method judgement AND the substance record (§ 6.6),
                                     so the thinning test goes with it.
─ Plan       … reader + auditors   → 🔴 lose Φ1c, Φ1d, Φ5, Φ6 AND Φ11. That is: the denominator,
                                     the freeze, every mechanical check, the G-1 cross-check and
                                     BOTH outcome records. D-TRACE is not measurable without Φ6.
─ 1 auditor  … no crossover        → lose BL-1, the primary. Do not make this cut.
MINIMUM VIABLE   reader-L + 2 auditors + operator gate + SOMEONE running Φ6 and Φ11
                 → BL-1, D-SEP, D-UNC, and D-TRACE only if Φ6 is run by someone.
                 🔴 Revision 1's MINIMUM VIABLE claimed D-TRACE while cutting the phase that
                    measures it, and claimed outcomes while cutting their author.
```

---

## 9 · Phases

### 9.1 · The sequence

**No phase writes `main`. A phase that produced no artifact did not run.**

| Φ | Track | Owner | Act | Artifact | Gate |
|---|---|---|---|---|---|
| **Φ0** | M | operator + any session | pre-flight **re-derived at the moment** — including seat tips, which have moved three times unreported | `TRIAL-001-PREFLIGHT.md` | every row satisfied at handover |
| **Φ1a** | S | acquirer | **declare the acquisition method before acquiring** | `…-ACQUISITION-DECLARATION.md` | B-3; nothing is fetched first |
| **Φ1b** | S | acquirer | acquire; `fulltext_receipts.py record`; verify digest | artifact + receipt + digest + 🆕 **the retained abstract** | `verify` passes. 🆕 **`record` writes the ledger AND re-anchors the state manifest — both are in the allowlist now** |
| **Φ1c** | M | Plan | surface — § 9.2 | per § 9.2 | per § 9.2 |
| **Φ1d** | M | Plan | **hand-enumerate the layer units** before anyone reads them | `…-LAYER-POPULATION.md` — units per layer, with counts | 🆕 **a second, independent enumeration by someone who has not seen the first; a disagreement is logged and reconciled before the freeze** (§ 9.3) |
| **Φ1e** | M | not the reader | check the assignment for prior-conclusion leakage **against the abstract retained at Φ1b** | `…-ASSIGNMENT-CHECK.md` | 🆕 revision 1 consumed a "frozen abstract" no phase produced, and the corpus record for this PMID carries `abstract_parts: []` (P-8) |
| **Φ2** | M | operator (Orchestrator only **iff** a lease is ACTIVE — **0 are**) | issue the assignment | contract under `ledger/tasks/` — **no validator exists** | 🔴 most likely governance stall; under D-4(a) it degrades to an operator instruction |
| **Φ3** | M | Plan → reader | HANDOVER recorded, not asserted | 🆕 **a `HANDOVER` block in the trial's own record** — the benchmark-manifest form does not exist under `SURFACE-LITE` (P-9) | one writer, transferred once |
| **Φ4** | S | reader | read under the obligations; classify every uncovered unit at the moment it is found | receipt · manifest · locators · layer status | no prior LEGEND output — and see § 9.2's forbidden list |
| **Φ5** | M | Plan | freeze on the completion declaration | `RECEIPT.json` | procedural — § 9.4 |
| **Φ6** | M | Plan | mechanical checks; **derive** the layer status; run the § 4.4 cross-check | `…-CHECK-LOG.md` · `…-LAYER-STATUS.md` | any refusal halts and is recorded. 🆕 **`deepdive_manifest` and the Φ4 receipt are mutually gating** — § 9.5 |
| **Φ7** | M | 2 fresh sessions | **the 2×2 crossover** (§ 5.2), against the schema fixed at § 9.7 | `reviews/trial-001/REV-TRIAL001-AUDIT-{1,2}` + act lists + the recorded shuffle | 🔴 **new construction — § 9.7** |
| **Φ8** | S | reviewer | Annex C `R2`, full C.2 field set incl. `STEELMAN` and `AUTHOR_RESPONSE`; **cross-checks** the substance record it no longer authors | `REV-TRIAL001-R2-001` | AUTHOR ≠ REVIEWER; 2 rounds → adjudication |
| **Φ9** | M | Mirror | **R4 on the process**; **authors** `TRIAL-001-CLAIM-SUBSTANCE.md` | `REV-TRIAL001-MIRROR-*` + substance record | input scoped by declaration — the consolidated ledger does not exist |
| **Φ10** | S | reader-L → operator | assemble the COMMIT CANDIDATE, **or the READING RECORD** (§ 2.3) | `CC-TRIAL001-…` | B-9; and § 9.5's corrected gate |
| **Φ11** | M+S | Plan | one outcome per track | `…-OUTCOME-M.md` · `…-OUTCOME-S.md` · friction log closed · one SLR | every count is an enumerated set or carries its command |

### 9.2 · 🔴 `SURFACE-LITE`, with the premise corrected

**Revision 1's argument was refuted by the precedent it cited** (W-2): 10 tracked files carry the
identifier, `literature_tracking_log_current.md` carries the prior inference verbatim twice, and
`BENCH-AB-001`'s own `forbidden_prior_output_paths` names that very file along with
`full_text_queue_current.md` and `surface_census.md`.

```
SURFACE-LITE, corrected  ────────────────────────────────────────────────────
  1. the acquired artifact, sha256 recorded in the acquisition declaration
  2. an explicit statement of which files the reader may open
  3. 🆕 A NAMED FORBIDDEN LIST, measured rather than assumed — the 10 tracked files that
     carry `28123895` or `PMC5214935`, re-enumerated at Φ0 because the set grows:
       literature_tracking_log_current.md · full_text_queue_current.md · surface_census.md
       batch_queue.md · 4 corpus seeds · 2 session_evaluations
  4. 🆕 the two contaminating lines quoted into the Φ1e check, so the leakage test knows
     exactly what it is testing for

  GUARANTEE_PROVIDED: none by mechanism. Under SURFACE-FULL the content scan enforces (3);
  under SURFACE-LITE it is discipline against a MEASURED list. The difference is real and
  is the price of the cost saving.
──────────────────────────────────────────────────────────────────────────────
```

`SURFACE-FULL` remains available. Its cost re-derived: a **421-line** spec whose `population` block
is ~42 % of it, a **678-line** `evidence_units.json`, six population sources, then build/verify/
population ×2/freeze — **and `freeze` refuses without `ASSIGNMENT.md`, `BENCHMARK_INSTRUCTIONS.md`
and `OUTPUT_SCHEMA.md`, then refuses again if `--actor-id` disagrees with `ASSIGNMENT.md`**, forcing
the surface to declare an actor id no registry has resolved. Its determinism gate has **no power**
against the failure it cites: `population` is a pure function of (spec, source bytes).

### 9.3 · Φ1d — priced from a superset, and given the cross-check it lacked

**No instrument enumerates layers** (M-5, on the corrected 51-script denominator). Revision 1 priced
Φ1d at the precedent's **65 units / 109 panels** — but that precedent enumerates **8 unit kinds**,
none of them abstract, introduction, discussion, limitations, references, captions, main tables or
front/back matter, and it has no `EXTERNAL_ASSET_LAYER` at all. **§ 4.1 specifies at least 21 unit
types across four layers. The real enumeration is a strict superset of the precedent** (P-10), and
**it is the largest hand-labour item in the design.**

🆕 **And it now carries a second, independent enumeration** — because it sets the denominator of
every layer figure, both documented enumerator errors on the precedent were enumerator errors, and
revision 1 had one owner and no check.

### 9.4 · The freeze is PROCEDURAL

```
GUARANTEE_PROVIDED:          none by mechanism — no instrument records a first-content-read instant
FAILURE_MODE_STILL_POSSIBLE: Plan reads the content before freezing
DETECTION:                   visible after the fact by inspection, never prevented
CONSEQUENCE:                 D-REPRO is reported PROCEDURALLY_ATTESTED, not PROVEN. It does not
                             void the arm and does not fail the trial. The freeze is never back-dated
```

### 9.5 · Blocking criteria

| # | Track | Block | Change from revision 1 |
|---|---|---|---|
| **B-1** | M | an entry criterion fails at entry | — |
| **B-2** | S | no declarable acquisition route | acquisition is **authorization- and network-blocked, not instrument-blocked** |
| **B-3** | S | acquisition before its declaration → **the input is void** | cannot be waived |
| **B-4** | M | the surface refuses | `SURFACE-FULL` only |
| **B-5** | M | *(retyped)* the freeze ordering is procedural; an unshown ordering downgrades D-REPRO | — |
| **B-6** | M+S | a `NOT_IN_SOURCE` verdict blocks canonical state until resolved | 🆕 **resolution happens after BOTH conditions are audited**, never between them — the crossover has no between |
| **B-7** | S | an unanswered `OVERSHOOT`/`UNDERSHOOT` before the candidate is sealed at Φ10 | retargeted |
| **B-8** | M | a write outside the allowlist → halt | filesystem snapshot diff; 🆕 **loose objects are declared, because nothing sees them** |
| **B-9** | S | a `G-3` bound to a claim proposed as `DATO` | downstream of the § 4.4 cross-check |
| **B-10** | S | 🔴 **retargeted, because revision 1 measured the wrong object class.** `MIRROR_REVIEW` is defined in Annex **D.2** for governance `INTEGRATION_CANDIDATE` manifests. Over the **16** scientific `CC-*` candidates it fires **0 of 16** — as does `CHANGE_CLASS` — with positive control `COMMIT CANDIDATE` at **15 of 16**. **The real gate on the canonical route is Annex D.3 GATE 0: `lease ACTIVE singleton`, and `ACTIVE by derivation` is 0** | 🔴 **P-7** |
| **B-11** | — | money would be spent | — |
| **B-12** | — | an escalation arrives as a diagnostic | the shape written out: the decision in one sentence · the options · a recommendation · what proceeds regardless |

### 9.6 · Mirror's R4 questions

Was the freeze ordering attested and labelled, or claimed as proven? · Was the recorded shuffle the
one used? · Were both auditors fresh, **and is there any evidence either way?** — 🔴 *the honest
answer today is no, and § 5.3 says so* · Were uncertainties outputs with satisfiable falsifiers? ·
Did the trial stay inside its allowlist, **loose objects included**? · Was the layer population
enumerated before it was measured, and did the second enumeration agree? · Did the § 4.4 cross-check
re-classify anything? · **Was the claim set thinned?** — and if so, the primary is voided (§ 6.6) ·
Was the assignment free of LEGEND's prior conclusion, **against the named forbidden list**?

### 9.7 · 🔴 Φ7's instrument is new construction — the test revision 1 never applied to § 5

Revision 1 applied the framework-construction test to § 4 in four clauses and **never applied it to
§ 5**, which is the larger construction (P-3). Measured:

- `legend-locator-audit` is a **102-line prose skill, no script**, defined over `(proposition,
  quote, anchor)` **triples**. Its own cost argument is *"the reason it is cheap: it never re-reads
  the paper."* **The bare condition is exactly a re-read** — a *find*, not a *check*, with the
  opposite cost profile.
- Its output is **four columns and five verdicts**, frozen a second time in
  `learned_gates_registry.md`. There is **no act column, no groundable-at-all column, no
  `UNGROUNDED`**.
- **`retrieval act` fires on 0 tracked files**; positive control `UNVERIFIABLE_SURFACE` → 3.
- `reviews/trial-001/` **does not exist** (`reviews/` holds `plan/` and 3 files).

**What revision 2 does about it, and what it refuses to do.** It does **not** build a script — that
would be F-1 firing. It requires, **before Φ0**, a written `TRIAL-001-AUDIT-SCHEMA.md`: the column
set, the verdict set per condition, the act-list format, the "one act" definition with a worked
example, and the shuffle-recording format. **The schema is a trial artifact, is priced as a line
item beside Φ1d, and is declared as unexercised — no precedent for it exists on any ref.**

> **The sentence revision 1 should have written, and that replaces § 1.2's:** *auditor **actorhood**
> is free; the auditing **instrument** for the bare condition is entirely new. The design's best
> insight was true about the actor and was stated about the apparatus.*

---

## 10 · Pre-registration

### 10.1 · Success as an experiment — **per track, and scoped to the chosen rung**

**TRACK-M succeeds** if: every phase **of the chosen degradation rung** produced its artifact · the
crossover ran against the § 9.7 schema with the shuffle recorded first · every mechanical gate ran
and its result was recorded, pass or refuse · every uncovered unit was classified and the cross-check
ran · the assignment was checked · Mirror adjudicated · and the outcome reports each dimension
separately with its route.

**TRACK-S succeeds** if it produces a candidate, a `READING RECORD`, or a documented `DISMISSAL`,
each with its claims typed and their limits declared.

> 🔴 Revision 1 required *"every phase produced its named artifact"* unconditionally while offering
> rungs that remove phases — so it could not be satisfied under cuts it recommended (P-15).

### 10.2 · Failure as an experiment

The bare condition was not blind · the layer population was set by the reader · a figure appears
without its command · a write happened outside the allowlist · the assignment carried a prior LEGEND
conclusion · **or an outcome reads as a paper summary rather than a dimension-by-dimension table**.

*Not on this list, deliberately:* the freeze ordering — no instrument can show it, so as a failure
criterion it guaranteed failure.

### 10.3 · Dimensions and falsifiers

| Dimension | Improvement criterion | Falsifier |
|---|---|---|
| **PRIMARY** | `ANCHOR-ADDS` **>** `ANCHOR-MISLEADS`, and `CONCORDANT` is the largest cell | 🔴 `ANCHOR-MISLEADS` ≥ `ANCHOR-ADDS` → **the anchors point away from where the evidence is**, and the outcome says exactly that. 🆕 A tie, or a `DISCORDANT` plurality, is its own reported outcome — revision 1's conjunctive criterion had no sentence for the middle case (H-26) |
| **SECONDARY · cost** | acts per claim lower in the anchored condition | acts equal or higher → the anchor did not pay for itself. **Reported, and never as the primary** |
| D-TRACE | every claim resolves to a digest-matched, locator-exact triple | any claim without a resolvable anchor |
| D-SEP | 100 % typed; every negative carries a premise tag | a hypothesis carried as an observation |
| D-REPRO | replay reproduces every figure and verdict from the record alone | any figure that needs its author |
| D-UNC | uncertainties are entries with satisfiable falsifiers | a falsifier no observation could satisfy |
| D-REV | the audit finds ≥1 defect the reader's self-check did not | the audit finds nothing and the reader found nothing — **evidence about the audit** |
| D-LAYER | **not a dimension** — `EXERCISED` / `NOT_EXERCISED` | — |

### 10.4 · Symmetry

```
EVIDENCE FOR the discipline     ANCHOR-ADDS is a populated cell: the reader's anchors carried
                                evidence an independent grounder did not reach.
EVIDENCE AGAINST                ANCHOR-MISLEADS is a populated cell: the anchors sent an
                                independent checker to passages that do not support the claim.
Both are counts of enumerated sets from the same audit. Neither is re-run to a better value.
NO IMPROVEMENT MEASURED and DISAGREEMENT_UNRESOLVED are legitimate, publishable outcomes.
```

### 10.5 · What remains useful if the trial fails

The acquisition declaration, reusable by every future reading of this paper · a documented
`DISMISSAL` discharging `FT-018` with a reason, and the full text permanently in the corpus · a
calibration fact about the audit instrument · a live instance of the lease gate · every mechanical
refusal, each a defect caught before a canonical file · `NOT_EXERCISED` for the layer model, with
T-8's nine papers still measured and open · **the friction log**, the only artifact that cannot be
reconstructed afterwards.

---

## 11 · Findings — disposition

**Revision 1's § 11 dispositioned the 33 findings of `TRIAL-001-REVIEW-FINDINGS-REGISTER` and is
preserved in blob `e88dc043…`. It is not reproduced here.** Three of those dispositions are
**withdrawn or downgraded** by revision 2, and the rest stand:

| v1 finding | Revision 1 said | Revision 2 says |
|---|---|---|
| **P-1** (no actors) | ✅ DECISIVE, quoting "revision 6, no PASS" | 🔴 **premise withdrawn** — the spec is canonical (W-1). The conclusion stands on `DEC-20260822`, the C-9 hold, and the lease |
| **T-7** (no efficiency baseline) | ✅ FIXED — "three real baselines" | ⚠️ **downgraded** — one baseline under the recommended configuration (H-19), and the negative regains its scope (H-20) |
| **F-8** (§ 2 is framework construction) | ⚠️ ACCEPTED AND SCOPED | ⚠️ **unchanged in substance, and now also applied to § 5**, which revision 1 exempted without noticing (P-3) |

**The 44 findings of the two reviews of revision 1 — H-1…H-27 and P-1…P-17 — are dispositioned in
`learning/orchestrator/TRIAL-002-DESIGN-V2-FINDINGS-REGISTER.md`, outside this object**, with the
blob each was made against, which of them this revision acts on, and why each of the rest does not.

---

## 12 · How this record's reviews are handled

```
1. Revision 1 was frozen with `git hash-object -w` before dispatch; both reviewers read
   blob e88dc043… and both quoted it back.
2. Findings live in TRIAL-002-DESIGN-V2-FINDINGS-REGISTER.md — a separate file, named in the
   frontmatter before dispatch. Nothing is written into a reviewed blob.
3. Integration produced THIS successor. Revision 1 is not edited; it is retrievable by blob.
4. A finding not acted on says WHY, in the register. Silence is not a disposition.
5. A finding is not a blocker unless the operator makes it one. Neither reviewer holds authority
   and neither is the registered seat.
6. 🔴 DISCLOSED, because clause 1 performs the write class B-8 cannot see: two `git hash-object -w`
   writes have been made by this session (revision 1 and revision 2). Both objects are reachable
   from 0 refs and are gc-prunable. THE REVIEWS ARE BOUND TO BYTES NO REF PRESERVES — D-13.
```

---

## 13 · Decisions requiring human approval

| # | Decision | Options | Recommendation | Proceeds regardless |
|---|---|---|---|---|
| **D-1** 🔴 | **Is the answer `C`?** | (a) **C, gated** · (b) A · (c) B | **(a)** — on the corrected premises of § 1.2: `DEC-20260822` `ACTIVATION_NOT_CONFIRMED`, L2 suspended, 0 ACTIVE leases, a registry one day stale. **Not** on revision 1's premise, which was false | nothing — it shapes every other |
| **D-2** 🔴 | **The paper, and the re-authored question?** | (a) **28123895 with § 3.3's question** · (b) with the queue's `Why` · (c) an alternate · (d) operator-supplied | **(a)** | nothing; Φ1 cannot start |
| **D-3** 🔴 | **How is the full text acquired?** | (a) authorize a connector · (b) **the operator supplies the PDF** · (c) `find-fulltext` in a session with web access · (d) `pmc_pow_fetch.py` | **(b) or (c).** 🔴 **Revision 1's (d) was malformed**: `pmc_pow_fetch.py` takes `url output`, **not a PMCID**, and its own docstring calls it *"a retrieval of last resort"* reached only after E-utilities and the OA package service, which `find-fulltext` tries first | nothing; Φ1 cannot start |
| **D-4** 🔴 | **Unregistered rehearsal, or lift/scope the C-9 L2 hold first?** | (a) **rehearsal claiming no actorhood** · (b) scope the hold · (c) lift it | **(a) or (b)** — and under `DEC-20260822` even (b) and (c) leave the contracts non-activated, so (a) is not a lesser form of the others | under (a): **no governed Scientist artifact** |
| **D-5** 🔴 | **`SURFACE-LITE` or `SURFACE-FULL`?** | (a) **`SURFACE-LITE` with the § 9.2 forbidden list** · (b) `SURFACE-FULL` | **(a)** — but on a corrected argument. The mechanical scan is **not** vacuous (W-2); what (a) buys is the cost saving, and what it costs is a mechanized guarantee replaced by discipline against a measured list | either way |
| **D-6** 🔴 | **Is § 4 in scope, or struck?** | (a) **in scope, scoped per § 4.5** · (b) struck · (c) in scope **and** T-8 repaired separately after | **(a)** with **(c) scheduled** — but the hostile review is right that § 4 is still the largest new specification here, and **(b) is a legitimate choice that costs the mandate's § 3 question** | either way |
| **D-7** | **Does BL-2 (control reader) run?** | (a) yes · (b) **no, for step 1** | **(b)** — but note this leaves **one** baseline (§ 7), not three | reported `NOT RUN` |
| **D-8** 🔴 | **Where do audit and review artifacts live?** `reviews/` holds only `plan/` | (a) **`reviews/trial-001/`** · (b) per-reviewer | **(a)** — the reviewers are ephemeral; a per-reviewer directory names a seat that does not exist | **Φ7 cannot run without a path** |
| **D-9** | **Run under OPCON-v1?** `DRAFTED`, on 1 of 48 refs | (a) **declared non-binding discipline** · (b) adopt first · (c) without | **(a)** | either way |
| **D-10** | **Review floor `R2`?** | (a) **yes, now** · (b) later | **(a)** — derogation is upward-only, so it costs nothing | either way |
| **D-11** 🔴 | **End at the candidate, or proceed to `BATCH_COMMIT`?** | (a) **stop at the candidate** · (b) proceed | **(a) for step 1** — 🔴 **on the corrected reason**: not `MIRROR_REVIEW` (absent from all 16 `CC-*`), but **Annex D.3 GATE 0's `lease ACTIVE singleton`**, and 0 are ACTIVE | Φ10 produces its artifact either way |
| **D-12** | **Is step 2's exit criterion the gate for step 3?** | (a) **yes** · (b) operator judgement | **(a)** | step 1 runs either way |
| **D-13** 🆕 🔴 | **Are the reviewed bytes preserved?** Revisions 1 and 2 exist as loose objects reachable from **0 refs**, gc-prunable, and both reviews are bound to revision 1 | (a) **commit these records on this branch** · (b) leave them; accept that a `git gc` orphans both reviews · (c) commit only revision 1 | **(a)** — `WORK_COMMIT` of a session's own named paths on its own branch is that author's own authority, and one `git clean` from any co-occupant destroys every untracked artifact at once. **Not performed here: it was not asked for** | nothing; the records exist until they do not |
| **D-14** 🆕 | **Does `TRIAL-001-AUDIT-SCHEMA.md` get authored before Φ0?** § 9.7 measures that the bare-condition instrument does not exist in any form | (a) **yes — schema first, priced beside Φ1d** · (b) improvise at Φ7 · (c) run the anchored condition only | **(a)**. **(c)** loses the primary entirely and is the cut § 8.3 says not to make | Φ7 cannot be replayed without it |

---

## 14 · What this record does not do

It does not start the trial, acquire a paper, build a surface, or author a spec · does not dispatch,
register, activate, assign or grant authority · creates no Task Contract, candidate, `DEC`, approval
or ledger event · does not lift the C-9 hold, verify a capability, acquire a lease, or resolve an
`ACTOR_ID` · does not perform the activation act `DEC-20260822` requires · does not adopt or amend
OPCON-v1 · adds no field to any schema and builds no script · does not modify `governance/`,
`roles/`, `framework/`, `ledger/`, `runtime/` or the four scientific current files · advances no
branch and stages nothing · does not repair T-8 · does not withdraw design v1, protocol v1 or
revision 1 · does not resolve any finding on anyone's behalf · does not claim actorhood.

🔴 **It has written two loose git objects** (revision 1 and revision 2), disclosed at § 12 clause 6,
because § 3.5 records that nothing detects them.

---

## 15 · Verification trail — revision 2's own re-derivations

All at `legend-operating-convention-v1` @ `30cb4f3`, 2026-08-23T22:0xZ. **Revision 1's trail is in
blob `e88dc043…` and is not reproduced.** Every figure of § 0.1 and § 1.3 is below.

```bash
# W-1 — the Scientist A/B specification IS canonical
git show mirror:reviews/mirror/REV-SCIAB-MIRROR-006.md | sed -n '11,13p'
#   verdict: ACCEPT — M-5 is closed. …
git log -1 --format='%H %ad %s' --date=iso 4454feab72b7a0edf65f191be62aeedd899a15ad
#   4454feab… 2026-08-19 15:08:55 +0200  The Scientist A/B specification becomes canonical, …
git merge-base --is-ancestor 4454feab… HEAD && echo YES        # YES
git show --stat --format='' 4454feab | head -12                # landed BENCH-AB-001 + the protocol
git cat-file -e HEAD:framework/protocols/scientist_reading_modes.md && echo PRESENT
grep -n "fixes the identity of .scientist-a" framework/protocols/scientist_reading_modes.md
git log -1 --format='%ad' --date=iso orchestrator -- runtime/agent_card_registry.md
#   2026-08-18 16:05:46 +0200      ← the registry predates the execution by one day

# W-2 — prior LEGEND output about this paper exists outside the 8 analysis surfaces
git grep -lE "28123895|PMC5214935" HEAD | wc -l                # 10   of 581 tracked
grep -n "28123895" disease-models/wwox/registries/literature_tracking_log_current.md
#   11914, 12045:  "PMID 28123895 (C1q → attivazione di WWOX, coda HIGH)"
#   NOTE ON THE CONTROL: the negative control 99999999 fires on 4 TRACKED files repo-wide —
#   all four are test fixtures (test_*.py). It is a clean negative on the 8 analysis surfaces,
#   which is the only scope it was used in.

# W-3 — what `record` actually writes
sed -n '752,757p' framework/scripts/fulltext_receipts.py       # write_state_anchor(...) in-lock
python3 -c "import sys;sys.path.insert(0,'framework/scripts');import fulltext_receipts as fr;\
from pathlib import Path;print(fr.default_ledger_path(Path('.'),'wwox'));print(fr.default_manifest_path(Path('.')))"
#   disease-models/wwox/registries/fulltext_read_receipts.jsonl
#   framework/state/state_manifest_current.md
git cat-file -p e88dc043… | grep -c "state_manifest"           # 0   (control SURFACE-LITE → 11)

# M-3 — revision 1's five predicates: exhaustive, and NOT a function
#   over all 63 non-empty subsets of COVERAGE_STATES:  UNDEFINED 0 · AMBIGUOUS 28
#   7 ambiguous WITHOUT unknown_legacy (no reading of "absorbing" rescues them), all with
#   captions_only:  {captions_only,unavailable} → CAPTION_ONLY+UNAVAILABLE
#                   {captions_only,not_present} → PARTIAL+CAPTION_ONLY   … and 5 more
#   control: the 6 singletons reproduce the 6 intended answers
#   empty set → COMPLETE by vacuous quantification  → § 4.2 introduces NOT_PRESENT_IN_PAPER

# M-6 — B-10 measured the wrong object class; the control had to be replaced
D=disease-models/wwox/research/commit_candidates
ls $D | grep -c '^CC-'                                          # 16   population
grep -rl "MIRROR_REVIEW"  $D | wc -l                            #  0 of 16
grep -rl "CHANGE_CLASS"   $D | wc -l                            #  0 of 16
grep -rl "COMMIT CANDIDATE" $D | wc -l                          # 15 of 16   ← control FIRES
#   (my first attempt used CANDIDATE_ID as the control: 0 of 16 — it did NOT fire, so the
#    absence was unvalidated until the control was replaced)
sed -n '30,40p' governance/annex_d_commit_batch.md              # D.2 INTEGRATION_CANDIDATE
sed -n '45,48p' governance/annex_d_commit_batch.md              # D.3 GATE 0: lease ACTIVE singleton
python3 framework/scripts/lease_state.py                        # ACTIVE by derivation: 0

# P-6 — the determination revision 1 never named
sed -n '1,20p' governance/decisions/DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE.md
grep -n "No actor authority may be assumed" governance/decisions/DEC-20260822-*.md   # line 305
git cat-file -p e88dc043… | grep -c "DEC-20260822"              # 0   (control SURFACE-LITE → 11)

# H-15 / H-20 / H-24 — the three I re-derived against revision 1's own text
grep -c "TRACK-M\|TRACK-S" <revision 1>                         # 7 of 1074 lines
sed -n '/^### 9.1/,/^### 9.2/p' <rev 1> | grep -c "TRACK-"      # 0   (control "Plan" → 6)
git ls-tree -r --name-only HEAD -- disease-models/wwox framework/eval | wc -l   # 297
git ls-tree -r --name-only HEAD | wc -l                                         # 581
git rev-list --objects --all | grep -c "^e88dc043…"             # 0  ← reachable from no ref
git rev-list --objects --all | grep -c "$(git rev-parse HEAD:CLAUDE.md)"        # 1  ← control
```

> **Every value is a photograph and it decays.** Check the class before concluding anything moved.
> **And three figures of revision 1 were confidently wrong** — W-1 because it was carried from a
> report rather than measured, W-2 because a true measurement was used to support a different
> predicate, W-3 because an allowlist was written without reading what the tools write.
