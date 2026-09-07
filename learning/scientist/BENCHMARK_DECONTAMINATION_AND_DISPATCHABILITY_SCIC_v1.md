---
artifact: LEGEND scientific evaluation — DECONTAMINATION, ACTOR-SPECIFIC CLEANLINESS, DISPATCHABILITY
id: BENCHMARK_DECONTAMINATION_AND_DISPATCHABILITY_SCIC_v1
class: evaluator-side record for a controlled benchmark in the vocabulary of
  `framework/protocols/controlled_benchmark_ab.md` and `framework/eval/benchmarks/BENCH-AB-001/`.
  It hostile-checks one dispatched case, re-bases the contamination model, and specifies a
  comparison. It is NOT a benchmark manifest and authorizes no run.
continues: EVALUATOR_FROZEN_SET_AND_BLIND_ROUND_DESIGN_SCIC_v1
  ← BENCHMARK_ELIGIBILITY_AND_BLIND_DESIGN_SCIC_v1 ← HARD_CASE_MINING_BENCHMARK_CANDIDATES_SCIC_v1
actor: scientist-c (NOT ACTIVATED — operator-directed analytical pilot)
worktree: lettore-c · branch lettore-c
date: 2026-08-26
audience: EVALUATOR ONLY
scope: EVALUATION DESIGN. No governance, role-contract, schema or architecture change.
status: NON-CANONICAL. Mutates no canonical file, manifest, receipt or ledger.
canonical_mutation: NONE
---

# The contamination was never in the branches. It is in the common ancestor.

> 🔴 **Evaluator material.** It states expected answers by implication throughout. The
> participant surface is the orphan branch `bench-blind-participant`, five files, and a command
> decides that it stays clean.

> **Nothing here is medical advice.** · **A/B were not contacted. No blind replication was started.**

---

## 0 · The one line

Last session I swept the thirteen mandatory participant files and the two reader branches and
reported `CLEAN_BLIND 7 of 48`. **I never swept `main`.**

```
case PMIDs carrying an adjudicating artifact on main       24 of 27
cases thereby spent for any actor reading in a checkout    43 of 48
the three exceptions                                       papers we do not hold
```

**Round 1's own answer is one of them.** Receipt `FTR-20260811-26675548-01`, on `main`:

> *"🔴 THE QUESTION THE PAPER WAS OPENED WITH, ANSWERED: **ATR IS NEVER MEASURED.** The title,
> abstract and every conclusion speak of ATR checkpoint activation. The antibody list contains
> CHK1, p-CHK1(S296), p-H2AX, ATM, p-ATM(S1981), KAP1, p-KAP1, p-histone H3, WWOX, GAPDH, HSP90
> and lamin — **NO ATR ANTIBODY.** … The only kinase inhibitor is KU-55933, which inhibits ATM."*

The commit that introduced it is titled **"The title says ATR and the summary figure puts a
question mark on it"**, dated 2026-08-11 — and the merge-base both reader branches descend from is
2026-08-22. 🔴 **The leak is in the shared history they branched *from*.** It is not A's doing or
B's; it is ancestral, symmetric, and in every worktree including mine.

**So the previous session's finding was true and one level too low.** Reader branches spend 16
cases. `main` spends 43. The branch analysis only ever mattered for the *difference* between A
and B, which is second-order.

**And the consequence is not that the benchmark is dead — it is that the surface build stops being
optional.** `controlled_benchmark_ab.md` §2.1 already requires a surface built by allowlist outside
every checkout. What it lacked was the number: **build it and 24 cases become dispatchable; skip it
and there are none.** The way to increase `CLEAN_BLIND` is not to find more cases. It is to build
the surface.

---

## 1 · Phase 1 — `BLIND-R1-001` hostile-checked

Eight channels, each a command. The instrument is
`learning/scientist/evalset/clean_for_actor.py`, which sweeps six surface sets and grades every
hit `L3` (states the answer) · `L2` (states a premise) · `L1` (names the paper evaluatively) ·
`L0` (incidental).

| # | Channel | Result |
|---|---|---|
| 1 | **A contamination** (`lettore`, tip `4f8643c4`, +27) | ✅ **no `L2`/`L3`.** Three mentions of PMID 26675548, all on the K274R blot and the caption census — that is `HC-D4`'s content, not this case's |
| 2 | **B contamination** (`lettore-b`, tip `111b9632`, +19) | ✅ **zero mentions** of the paper in 8 950 added lines |
| 3 | 🔴 **main contamination** | **1 × `L3`, 8 × `L2`** across six files: the receipt ledger, `deepdive_manifests/PMID26675548.json`, `fulltext_dossiers/PMID26675548.md`, `discovery_ledger_current.md`, `full_text_queue_current.md` (*"L'unico inibitore usato è KU-55933, che è di ATM. Ogni affermazione su «ATR checkpoint» è p-CHK1 come proxy"*), and a session evaluation. **Plus a commit subject.** |
| 4 | **Mandatory participant surfaces** (13 files) | ✅ **0 × `L3`, 0 × `L2`.** One `L0`: `deepdive_manifest.py` L463 names the PMID as a timepoint-label example |
| 5 | **Branch-local leakage** | ✅ covered by 1–2; the gate dropped 1 ungated false positive on B (a PMID 32000863 line matching a generic *"abstract … unsupported"* pattern) |
| 6 | **Participant handoff wording** | ✅ `check_participant_surface.py` PASS, and five mutations blocked (§4) |
| 7 | 🔴 **Evaluator leakage** | `C_BRANCH` carries 4 × `L3` and 5 × `L2` — my own two input artifacts, by design and by necessity. **They are on `lettore-c` only, and `lettore-c` is not an ancestor of any reader branch** |
| 8 | **Required source availability** | ✅ complete: PDF `2416bec7…`, PMC XML `8bf84348…`, supplementary deposit `oncotarget-07-4344-s001.pdf` (1 527 965 B, 7 pp) and `-s002.pptx`. Excluded from the packet: eight prior-reader renders |

### 1.1 · Verdict, per actor

```
CLEAN_FOR_A              NO   in a checkout of this repository
                         YES  on an allowlisted surface built outside every checkout
CLEAN_FOR_B              NO   in a checkout          (same ancestral cause, symmetric)
                         YES  on an allowlisted surface
CLEAN_FOR_FRESH_READER   YES  on an allowlisted surface — 0 blocking hits in MANDATORY
```

🔴 **`ROUND1_A_ELIGIBLE: NO` · `ROUND1_B_ELIGIBLE: NO`, as the instruction requires.** The rule was
*if it is not clean for both A and B, do not declare it ready for A/B*, and I am not going to
discharge that on the argument that a correctly built surface would fix it. Two reasons, and the
second is the one that decides it:

1. The surface has not been built. Declaring readiness against a directory that does not exist
   would be a promise, and the last two sessions have each turned up one of those.
2. 🔴 **The answer has had fifteen days and six files on `main` to reach a reader.** `main` is
   merged into both reader worktrees; `discovery_ledger_current.md` and the receipt ledger are
   named in the state manifest as files a session touches. Session memory cannot be inspected by
   any command I have. `controlled_benchmark_ab.md` §2.2 records that a fresh surface path starts
   with an empty auto-memory scope and calls that *"a favourable accident of the deployment, not
   a guarantee"* — that accident is now the only thing standing between this case and its answer,
   and it is doing more work than it was written to do.

**`ROUND1_FRESH_READER_ELIGIBLE: YES`**, conditional on the surface build and on the builder not
being the reader.

---

## 2 · Phase 2 — the fourteen `SCREEN_ONLY` rows, read

| Case | `SCREEN_REASON` | `ACTUAL_CONTAMINATION` | `ACTOR_SPECIFIC` | `SOURCE_AVAILABLE` | `Q_LEAKED` | `A_LEAKED` | `DISPATCHABLE` |
|---|---|---|---|---|---|---|---|
| `HC-B3` | adjudicative words near 34634460 | **main `L2`×1** — the axis defect is in `FTR-20260810-34634460-02` | symmetric (main) | 🔴 **NO** — XML only, no figure images; the case *is* an axis | yes | yes | **no** |
| `HC-E3` | 42128308/42397075 densely worked | **main `L2`×1 · A `L3`×1 `L2`×5** | 🔴 **asymmetric — A only** | yes | yes | **no** |
| `HC-F2` | premise in `deepdive_manifest.py` | **MANDATORY `L2`×2 · main `L3`×5** | symmetric + irremediable | yes | yes | yes | **no** |
| `HC-F3` | vigabatrin + adjudicative words | **main `L2`×5 · B `L2`×1** | mostly symmetric | n/a — clinical literature, no bounded packet | yes | partly | **no** |
| `HC-G2` | 42128308 worked | ✅ **none at case-question level** — `L1`×5, no `L2`/`L3` on any surface | none | yes (via the review) | no | no | **candidate** |
| `HC-I10` | `pdf_only` + surface words | **main `L3`×1 `L2`×11** | symmetric | yes | yes | yes | **no** |
| `HC-I2` | 16061658 + corruption words | **MANDATORY `L3`×1 `L2`×1 · main `L3`×18** | symmetric + irremediable | yes (PDF, which is the object) | yes | yes | **no** |
| `HC-I3` | Salah caption census | **main `L3`×2 · B `L3`×1** | 🔴 asymmetric — B additionally | yes | yes | yes | **no** |
| `HC-I4` | 42397075 provenance | **main `L3`×8 `L2`×6** | symmetric | yes | yes | yes | **no** |
| `HC-I6` | `CLAIM 023` custody | **main `L2`×6 · A `L2`×2 · B `L2`×1** | symmetric + both | 🔴 **NO** — 32185845 not held | yes | partly | **no** |
| `HC-X1` | Johannsen unobtainable | **main `L2`×1** | symmetric | 🔴 **NO** — 29808465 not held | yes | no | **no** |
| `HC-X2` | body-size disagreement | **main `L2`×5** | symmetric | yes | yes | no gold exists | **no** |
| `HC-X4` | `ch?` placeholder | ✅ pattern-clean — 🔴 **and wrong**: `PMID34634460.json:241` states it verbatim | symmetric | 🔴 **NO** — no figure images | yes | yes | **no** |
| `HC-X5` | motif-tree arithmetic | **main `L2`×35** | symmetric | yes | yes | partly | **no** |

### 2.1 · The screen's precision, measured — and my own instrument's error rate with it

**Last session's adjudicative-language screen**, against the reading now completed:

```
screen positives (READER_ADJUDICATED)                      35
  read line by line, previous session                      24   16 confirmed · 8 downgraded
  read this session (the 14 SCREEN_ONLY rows)              14
  cumulative confirmed at the reader level                 17   (+HC-I3 on B)
  cumulative downgraded                                    9    (+HC-G2)
  SCREEN FALSE-POSITIVE RATE                               9/26 = 35%
  screen false NEGATIVES found                             0
```

🔴 **And a false negative in the instrument I built to replace it.** `clean_for_actor.py` returned
`CLEAN` for `HC-X4` on every surface. Reading `main` directly:

> `deepdive_manifests/PMID34634460.json:241` — *"🔴 **A PLACEHOLDER SURVIVED INTO THE PUBLISHED
> FIGURE** … Its heterozygote row labels the second channel `'ch?'` … Adjudicated at 10x on the
> native pixels: it is a question mark with its dot."*

My `answer` pattern for that case was one regex lifted almost verbatim from the case file, so it
matched only a copy of itself. **Pattern precision is a property of the patterns I wrote, and I
wrote fourteen of them in one sitting.** The consequence is stated as a rule and applied below:

> **The structural census is the instrument of record for contamination. The pattern sweep only
> characterises what leaked.** A case is contaminated when an adjudicating artifact for its paper
> exists on `main` — whatever words that artifact happens to use. Anything else is a screen.

**Not loosening the screen to grow the set.** `HC-G2` is the only row that came back clean at the
case-question level, and it is a *candidate*, not a promotion: `main` was read for it by hand
(`P47T` and `SCAR12` occur only as background in `analysis/README.md`, a therapy-lever CSV and the
DisMech export spec — none of them the abundance-versus-function argument), and the census still
flags its review paper as adjudicated. **`DISPATCHABLE_CASE_COUNT` in a checkout: 0.**

---

## 3 · Phase 3 — `CLEAN(case, actor, surface-set)`

Contamination has been treated as a property of a case. It is a **relation over four things**, and
every confusion in the last three sessions came from collapsing them.

```
CLEAN(case, actor, surfaces) = ¬∃ hit ∈ L2 ∪ L3 over MANDATORY(surfaces) ∪ OPTIONAL(surfaces)
                                                      ∪ CHECKOUT(actor) ∪ BRANCH_HISTORY(actor)
```

| Input | What it is | Measured by |
|---|---|---|
| `CASE` | the question and its decisive fact | the case spec — ids, premise, answer patterns |
| `ACTOR` | a persistent identity with a branch history and a session memory | `git diff <merge-base>..<branch>`; **memory is not inspectable** |
| `CHECKOUT` | whether the reading happens inside a worktree of this repository | a deployment fact, chosen at dispatch |
| `MANDATORY_SURFACES` | the 13 inherited files a participant must hold to be graded at all | `surface_spec.json` `common_files` + `MODE_A`/`MODE_B` |
| `OPTIONAL_SURFACES` | the packet — the paper and its deposits | the case's `CORPUS_BOUNDARY` |
| `BRANCH_HISTORY` | lines the actor's branch added since its merge-base | per-branch diff |

### 3.1 · The table the model is for

| | in a **checkout** | on a **built surface** |
|---|---|---|
| `scientist-a` | 43/48 spent by `main`; +2 more by A's own branch (`HC-E3`, `HC-I6`) | blocked only by `MANDATORY`: **13 cases** |
| `scientist-b` | 43/48 spent by `main`; +2 more by B's own branch (`HC-I3`, `HC-F3`) | the same 13 |
| **fresh reader** | 43/48 spent by `main` — a fresh actor in this repository is not fresh | the same 13 |

The 13 are the irremediable set: `L3` in `HC-A1` `HC-B1` `HC-I1` `HC-I2`, `L2` in `HC-A2` `HC-E1`
`HC-E3` `HC-F1` `HC-F2` `HC-H1` `HC-I4` `HC-I8` `HC-J3`. They are blocked because the leak is in a
file the participant must hold to be graded at all — removing it would remove the rule the reading
is graded against, or change bytes both readers must run identically. **35 cases survive the
mandatory surface; 24 of those also survive their own eligibility** (the other 11 lack a surface,
have a falsified premise, or belong to a different family).

🔴 **The bottom-left cell is the point of the whole model.** *"Fresh reader"* is not a property of
the actor; it is a property of where the actor reads. An actor with no history here, opening a
worktree of this repository, inherits 43 spent cases on its first command. **And the top-right
cell is the other half:** `scientist-a`, the actor most contaminated in a checkout, is as clean as
anyone on a built surface — for files. The residue is memory, and it is why `HC-E3` and `HC-I6`
stay recorded against A even in the right-hand column as a *declared, one-sided* caveat.

**What this buys, in the operator's words:** a case can be unusable for A and valid for a fresh
Scientist — but **only if the fresh Scientist reads outside this repository.** Inside it, there is
no such thing as a fresh reader.

**No new architecture.** The model is two existing commands plus a rule about which surfaces an
actor holds. Nothing is proposed for `framework/`.

---

## 4 · Phase 4 — participant view hardening

### 4.1 · 🔴 The branch I shipped last session was not a participant surface

`bench-blind-participant` was branched **from `main`**. A checkout of it gave a reader:

```
585 files · 101 of them adjudicating · and, verbatim, the answer to the case it existed to dispatch
```

I wrote in its commit message that *"no evaluator byte can travel with it"*. That was true of the
**evaluator set** and false of the **repository it was branched from**, and the sentence did not
distinguish them. It is the same shape as the `HC-E2` error one level down: I checked the surface I
had thought about and not the one that was there.

**Repaired.** The branch is now an **orphan** — no parent, five files, no history from `main`:

```
$ git log -1 --format=%P bench-blind-participant     ->  (empty)
$ git ls-files | wc -l                               ->  5
```

The withdrawn tip is preserved at tag `bench-participant/withdrawn-non-orphan` so the error is
auditable rather than erased.

🔴 **And the corrected object is still not a reading surface.** A branch of any shape shares an
object store with this repository: `git show main:<path>` is one command from any worktree of it.
`bench-blind-participant` is a **delivery ref for the handoff documents**. The reading surface is
the allowlisted standalone directory of `controlled_benchmark_ab.md` §2.1–§2.3, which is not a
git branch at all.

### 4.2 · The five checks, each answered

| Requirement | Result |
|---|---|
| no evaluator answers | ✅ `LANGUAGE` class, enumerated vocabulary |
| no gold | ✅ same |
| no prior conclusions | ✅ same; and the branch is an orphan, so `main`'s conclusions are absent |
| all and only the necessary surfaces | ✅ `SUFFICIENCY` class (added this session): a handoff whose `CORPUS_BOUNDARY` names no resolvable identifier is a finding |
| no dependency on files on other branches | ✅ `CONTAINMENT` class; and `git ls-files` = the five files |
| reproducible from pinned refs | ✅ orphan tip is a single commit over a five-file tree; the handoffs are byte-identical to `lettore-c`'s copies |

### 4.3 · Mutation test — the checker must block

```
BASELINE on the real surface: exit 0

M1  inject expected verdict      exit 1  BLOCKED   classes=LANGUAGE,SCHEMA
M2  inject answer phrase         exit 1  BLOCKED   classes=LANGUAGE
M3  inject evaluator keyword     exit 1  BLOCKED   classes=LANGUAGE
M4  inject forbidden path        exit 1  BLOCKED   classes=CONTAINMENT
M5  remove required source       exit 1  BLOCKED   classes=SUFFICIENCY

VERDICT: PASS — all 5 mutations blocked.
```

`framework/eval/benchmarks/blind_rounds/mutation_test.py`. A mutation that fails to apply is
reported as a finding against the test, not silently skipped.

🔴 **This shows the checker is not inert. It does not show it is complete.** A leak phrased in
words the `LANGUAGE` list does not contain passes, and `M5` is caught only at the document level —
whether the named file is actually *in* the built packet is `benchmark_input_surface.py verify`'s
question and is not decidable here.

`PARTICIPANT_VIEW_VERDICT: **PASS as a delivery ref, after one structural repair. Not a reading
surface, and never was.**`

---

## 5 · Phase 5 — provenance / adjudication separation

### 5.1 · Feasible, and the blocker is not the one we named

`learning/scientist/evalset/participant_provenance_view.py` emits the six requested fields by
**whitelist** — anything not on the list is dropped, including fields that look harmless, because
a blacklist of words at schema level is the same mistake as quoting a caption at reading level.

Tested on the three papers that have a structured record, exactly as asked:

```
papers with >=1 figure artifact           58
ALL six fields derivable                   3   16061658  17803050  21212533
SOME rows complete                         0
NO regeneration recipe derivable          55
```

For those three, `page_adjudications/PMID<x>/adjudications.json` already has the right shape —
`{file, page, crop, dpi, sha256}` plus `source_pdf:{path, sha256}` — and the adjudication sits in
**separately named keys** (`adjudicates`, `needles`, `why_this_article_is_adjudicated`) that the
projection simply does not read. One emitted row:

```json
{"source_id": "PMID21212533",
 "file_digest": "49f60ddb61b52012d5dacefb209a4f649b36fd96ab37f698b837277b825652a4",
 "figure_id": "p2_c1", "page": 2,
 "regeneration_recipe": {"tool": "regenerate_adjudications.py",
   "source_pdf_sha256": "790f602006a341c043357c6931be5b7c47a82f39851a30b980ae3dd8d592dca7",
   "page": 2, "crop_xyxy": [300, 60, 552, 238], "dpi": 500,
   "coordinate_system": "PDF points, origin top-left, as consumed by PyMuPDF clip"},
 "handle": "49f60ddb61b52012.png"}
```

🔴 **For the other 55, the separation is not the obstacle — the information does not exist.**
`deepdive_manifests[].source_artifacts` carries `path`, `sha256`, `kind` for all 333 figure
entries; `native_px`/`effective_ppi` for 13; a free-text `note` for 16; a `figure` id for **4**.
There is no `page`, no `crop`, no `dpi` anywhere in that record. **A digest verifies a render you
already hold; it does not let you make one** — and that gap is upstream of any view.

### 5.2 · 🔴 The leak channel the projection found, which no one had named

The stored crop **filenames** state conclusions. Of 27 across the three papers, at least seven:

```
p03_CT_indispensable_no_structure.png      p03_ww1_primarily_responsible.png
p02_unfavorable_substrate.png              p02_rationale_common_targets.png
p08_affinity_asymmetry.png                 p03_CT_invisible_in_crystal_structures.png
p08_generalised_frame.png
```

A participant handed those handles learns the finding without opening the file. **My word-list
screen caught two of the seven** — the blacklist failing exactly as predicted, in my own tool, two
hundred lines after I wrote the rule against it.

**The repair is not a better word list. It is to stop emitting the name.** The digest identifies
the object, the recipe locates it, a positional id (`p2_c1`) orders it. A prior reader's
description adds nothing a participant needs and carries their attention. After the change the
audit is clean **by construction** rather than by screening.

`PROVENANCE_SEPARATION_FEASIBILITY: **DEMONSTRATED on 3 of 58; blocked on 55 by missing structured
page/crop/dpi, not by co-location. The minimum separation requirement is unchanged and now has a
working reference implementation and a denominator.**`

---

## 6 · Phase 6 — gold-ready: two acts performed, five ranked

Ordered by **epistemic cost** — how much of the case's truth the act has to create — not by ease.

| # | Case | `MISSING_ACT` | `WHO_CAN_PERFORM` | `PRIMARY_AVAILABLE` | `2ND_ADJUDICATION` | `CONTAMINATION_REPAIR` | `VALUE` | Epistemic cost |
|---|---|---|---|---|---|---|---|---|
| 1 | **`HC-A4`** | re-derive four magnitudes from the held XML | any actor · **✅ DONE, §6.1** | ✅ XML | **required** | none needed | high | **lowest** — arithmetic on printed numbers |
| 2 | **`HC-C2`** | read two asterisk definitions from the held captions | any actor · **✅ DONE, §6.2** | ✅ XML | **required** | spent as blind; fine as gold | high | **lowest** — quotation |
| 3 | `HC-D2` | enumerate the assay inventory of PMID 18487609, show it empty of the named test | a reader on a built surface | ✅ PDF + PMC HTML | required | surface build | high | low — an absence, but an enumerable one |
| 4 | `HC-G3` | re-derive the stage confound from PMID 34268881 | a reader on a built surface | ✅ PDF + XML + assets | required | surface build | high | medium — the confound is named in a heading, its *weight* is judgment |
| 5 | `HC-E2` | run Round 1; two frozen readings + a blind locator audit | **fresh reader only**, §1.1 | ✅ complete packet | required | surface build **and** an actor with no history here | highest | medium — the answer is determinate, the *adjudication* is not mine to make |

**Not promoted, per standing instruction:** `HC-B1`, `HC-A1`, `HC-I1`.

### 6.1 · `HC-A4` — act performed

Re-derived this session from `PMID34634460_Breton2021_PMC.xml`, verbatim:

> *"mean amplitude ± standard deviation: **S-CTL 23.3 ± 12.0 pA; S-KO 24.7 ± 13.6 pA**"* … *"the
> sIPSCs were reduced in both amplitude and frequency … mean amplitude: **S-CTLs 57.3 ± 31.0 pA;
> S-KOs 27.5 ± 19.4 pA**"*

Excitatory **+6.0 %**; inhibitory **−52.0 %**. The inhibitory arm is the larger effect by ~8.7×.
**No figure surface is needed** — which matters, because none is held for this paper.

🔴 **And the re-derivation qualifies the case.** The comparator is `S-CTL`, and the paper's Methods
pool heterozygotes into it: *"Where no significant difference exists between S-HT and S-WT groups,
they are occasionally represented as a clustered group (S-CTL)"* — while Table 1 marks the
heterozygote different from wild type on four intrinsic properties. **These two percentages
describe knockout-versus-pooled-control, not knockout-versus-wild-type**, and the case file said
"control". The ranking survives; the denominator has to travel with it.

### 6.2 · `HC-C2` — act performed, and the case gets a third instance

From the same held XML, `<fig>` captions:

| Figure | Printed | Convention |
|---|---|---|
| **Fig 3 d2** | `* p = 0.0036, ** p = 0.0274` | 🔴 **inverted** — one star on the smaller p |
| **Fig 4** | `* p = 1.5e-5` · `** p = 9.22e-135` · `* p = 9.42e-8` | normal |
| **Fig 6** | `* p = 0.04761; ** p = 0.00322` | normal |

The case file has Figure 3 against Figure 6. **Figure 4 is a third data point, and it is on the
same panels `HC-A4` reads** — so the paper's asterisk convention is inconsistent one-against-two,
not one-against-one, and the inconsistency is confined to Figure 3.

🔴 **Both acts stop at re-derivation.** `NEEDS_SECOND_ADJUDICATOR: YES` on both, unchanged: I
produced the facts, and the actor who produced them is the wrong actor to adjudicate the verdict.
`GOLD_READY_COUNT: 0`.

---

## 7 · Phase 7 — unresolvability, searched and **not** filled by quota

Four tests, all four required: surfaces complete · answer genuinely undecidable · the
undecidability is **not** a missing file · the evaluator can demonstrate it.

| Case | Surfaces complete? | Undecidable? | Not a missing file? | Verdict |
|---|---|---|---|---|
| **`HC-A2`** | ✅ **yes** — 7 figure PNGs held incl. `Fig7_HTML.png`, plus XML | ✅ the legend defines `n.s.` and `*** P < 0.001` and nothing else; `****` is printed on panel 7d and occurs **0 times** in prose; Methods declare a single α = 0.05 | ✅ nothing is missing — every surface exists and none defines the token | ✅ **`UNRESOLVABLE`** |
| `HC-B1` | ✅ | ✅ swap vs mislabel indistinguishable | ✅ | ⛔ **blocked** — irremediable `L3` in `fulltext_read_receipt.md`, and its published negative control is falsified |
| `HC-C4` | ❌ the third surface (the `Ctrl` column) is a figure; 32581702 is XML-only | partly | ❌ | → `UNVERIFIABLE_SURFACE` |
| `HC-F4` | ❌ neither terminal source held | — | ❌ | → `SOURCE_MISSING` |
| `HC-I5` | ✅ | ❌ the supplement is held and decides | ❌ | → premise falsified |

`UNRESOLVABLE_CASE_COUNT: **1** — `HC-A2`.` It is a genuine member of the category and it is **not
dispatchable**: both readers worked PMID 32000863 heavily and `main` adjudicates it. **Category
membership and dispatchability are different questions**, and last session I let the second empty
the first.

### 7.1 · The three states, which must never share a column

| | The record | We hold | Correct answer | Wrong move |
|---|---|---|---|---|
| `UNRESOLVABLE` | complete | everything | *"the record does not decide"*, naming what would settle it in principle | resolving it |
| `SOURCE_MISSING` | would decide | **nothing to read** | *"acquire object X"*, named exactly | calling it unresolvable — **retires a retrievable question** |
| `UNVERIFIABLE_SURFACE` | would decide | the file, unusably (corrupt text layer, no figure raster, closed access) | *"the object exists and cannot be read by route R"*, naming the route | either of the above |

🔴 The middle and right columns are **debts**; the left is a **finding**. `HC-I5` cost this
benchmark a slot for months by being filed under the left when it belonged under the middle — and
then turned out to be neither, because the file was on disk all along.

---

## 8 · Phase 8 — scoring, with the two score families kept apart

### 8.1 · Six dimensions are computable without gold

| Dimension | Without gold, what decides it |
|---|---|
| `OBSERVATION_OVERLAP` | the structurally enumerated evidence-unit population, fixed before either reading |
| `CLAIM_OVERLAP` | structural alignment by shared evidence unit — never by an evaluator judging meaning |
| `EPISTEMIC_VERDICT_AGREEMENT` | token equality on aligned pairs |
| `LOCATOR_AGREEMENT` | anchor identity + source character-range overlap |
| `OVERCLAIM` | the **blind locator audit** — `OVERSHOOT` is decided against the source, not against a gold label |
| `CORPUS_DISCIPLINE` | `benchmark_input_surface.py locators`: membership of every locator in the allowlist |

The other four — `NEGATIVE_EVIDENCE_RECALL`, `CONTRADICTION_DETECTION`, `UNRESOLVABILITY_RECOGNITION`,
and the *material-omission* half of `UNDERCLAIM` — need an enumerated gold set and are not
computable in Round 1.

### 8.2 · Two score families. They are never combined, and never compared.

```
PAIRWISE_REPRODUCIBILITY_SCORE     Does the process, run twice, land in the same place?
   unit   an aligned pair, or an evidence unit
   input  A and B only. No gold. Available in Round 1.
   MEANS  reproducibility.   MEANS NOT  correctness.

GOLD_ACCURACY_SCORE                Did the reading land where the source puts it?
   unit   a proposition, an enumerated negative, an undecided question
   input  the source, via a blind audit or an adjudicated gold set. Not available in Round 1.
   MEANS  correctness.       MEANS NOT  reproducibility.
```

🔴 **A high pairwise score with a low gold score is the most dangerous cell in the table and the
one this laboratory will hit**, because A and B share a discipline file, a mode vocabulary and a
model. Reporting only the first would read as success.

### 8.3 · The five cases the operator named, defined

| | Definition | Family | Rule |
|---|---|---|---|
| **agreement on a wrong answer** | an aligned pair where both `Type` tokens match **and** the blind audit returns `OVERSHOOT`/`NOT_IN_SOURCE` for both | needs **both** families | 🔴 **counts as +1 pairwise reproducibility and −2 gold accuracy.** Two readers agreeing on an overshoot is two overshoots. It must never appear as a single number, and it must never be netted |
| **agreement on uncertainty** | both readers decline to resolve, **and** both name the same one of `UNRESOLVABLE` / `SOURCE_MISSING` / `UNVERIFIABLE_SURFACE`, **and** both name an object | pairwise; gold only if the category is enumerated | agreement on *"insufficient evidence"* with no object named is **not** this — it is two omissions that look like a match. Scored in a separate `VAGUE_MATCH` column |
| **asymmetric overclaim** | `OVERSHOOT` on one side, `SUPPORTED` on the other, on the same proposition and the same locator | gold | 🔴 the informative cell of the whole benchmark: same bytes, same instructions, one declared variable, opposite verdicts. It goes to `unresolved_disagreements.md` **unresolved**, with both statements quoted |
| **negative-evidence omission** | an enumerated negative in the source carried by neither reader | gold | 🔴 counted **per negative, not per reader**: a negative both miss is one hole in the model, and reporting it twice would make the pair look worse than the process is |
| **corpus-boundary violation** | a locator resolving outside `ALLOWED_SURFACES` and outside the reader's own output slots | mechanical, neither family | 🔴 **self-reported = 1 entry; unreported = the reading is void.** Reported in its own table, never averaged with anything, and stated to the readers in advance — which the handoffs do |

`PAIRWISE_SCORING_READY: **YES** — six dimensions, gold-free, plus the five definitions above.`

---

## 9 · Phase 9 — the primary estimand

**Recommendation: `ERROR_PER_CLAIM` as primary, with `ERROR_PER_PAPER` reported beside it as the
denominator-honest anchor.**

| | |
|---|---|
| `WHAT_IT_MEASURES` | the rate at which a carried claim — the unit the disease model actually consumes and the unit a defect propagates through — misstates what its cited evidence bears |
| `WHAT_IT_DOES_NOT_MEASURE` | 🔴 **claims never carried.** A reader who omits half a paper has no error on the units it did not produce. This is why it cannot stand alone. Also not measured: process failures (wrong file, skipped gate) — that is `ERROR_PER_RUN`; and undetected defects, which need a second independent reading per paper |
| `DENOMINATOR` | claims produced by the reading. 🔴 **Chosen by the reader**, which is the estimand's defining weakness: carrying less lowers the rate without improving anything. `ERROR_PER_PAPER`, whose denominator is fixed by the sampling frame, is the control for exactly this and is the reason both are reported |
| `DEPENDENCE_PROBLEM` | claims cluster inside a paper — shared surface, shared reader, shared session. Measured cluster size **m = 15.7** (1 002 locator entries / 64 manifests; median 14, max 32). Independence is **false**, so a naive binomial interval is too narrow by `√DEFF` |
| `HOW_REPEAT_RUNS_ENTER` | 🔴 as a **third level**, not as more claims. `run ⊃ paper ⊃ claim`. Two runs of the same paper by the same actor are not 2m independent claims; they are one paper measured twice, and their agreement estimates ρ rather than adding precision. Repeat runs are how ρ gets measured — and how the *undetected*-defect rate becomes reachable at all, at double the sample cost |

🔴 **The recommendation is normative, not empirical.** No measurement selects between these five
units; the choice follows from what the number is for. And the units are **not convertible**: a
rate on one does not translate to another, and quoting one as the other is the failure this whole
line of work exists to catch.

### 9.1 · Only now, sample size

**Independent units**, 95 % Wilson, `p` **assumed** 0.30:

| half-width | n (p=0.30) | n (p=0.50) |
|---|---:|---:|
| ±0.05 | 320 | 381 |
| **±0.10** | **78** | 93 |
| ±0.15 | 33 | 39 |

**Clustered**, `DEFF = 1 + (m−1)ρ`, m = 15.7 measured, **ρ not measured**:

| ρ | DEFF | claims | **papers** |
|---:|---:|---:|---:|
| 0.05 | 1.73 | 136 | **9** |
| 0.20 | 3.94 | 308 | **20** |
| 0.50 | 8.35 | 652 | **42** |

🔴 The 78-paper figure and the 9–42-paper figures are precisions on **different quantities** and
must not be read against each other.

🔴 **And the frame is still not enumerable by one command.** `paper_registry_current.md` holds three
entry classes — 70 `PAPER`, 188 `CORPUS Pnnn`, 168 `CORPUS-STUB` = **426** — with no published rule
for which is drawn. `growth_anchors.py` reports `corpus=356`, matching `188+168`; its own regex
finds 357 distinct ids, the extra being `CORPUS P264`, referenced with no entry. **Publishing the
frame rule is upstream of every number in this section.**

---

## 10 · Phase 10 — three dispatch packets, prepared and **not sent**

| | `ROUND1` | `ROUND2` | `ROUND3` |
|---|---|---|---|
| `PARTICIPANT_VIEW_REF` | `bench-blind-participant` (orphan) `:framework/eval/benchmarks/blind_rounds/participant/BLIND-R1-001.md` | …`/BLIND-R2-001.md` | …`/BLIND-R3-001.md` |
| `CASE_ID` | `BLIND-R1-001` | `BLIND-R2-001` | `BLIND-R3-001` |
| `PINNED_SOURCE_REFS` | `PMID26675548_AbuOdeh2016.pdf` `2416bec7…` · `_PMC.xml` `8bf84348…` · `oncotarget-07-4344-s001.pdf` · `-s002.pptx` | ⛔ **two sources absent**: PMID 12065620 · PMC3139124. Held: `PMID21212533_Saeki2011.pdf` | `PMID42128308_Aqeilan2026.pdf` + `_fitz.txt` |
| `QUESTION` · `ALLOWED` · `EXCLUDED` · `STOP` | in the handoff, six fields, checker PASS | same | same |
| **`ACTOR_ELIGIBILITY`** | 🔴 **fresh reader on a built surface only.** NOT A, NOT B | fresh reader; blocked on acquisition | fresh reader on a built surface; A carries a declared one-sided residual on the paper (not on the taxonomy) |

**Contamination is not explained anywhere in the participant view** — every constraint is written
as `DO_NOT_OPEN_SURFACE_X`, and `ACTOR_ELIGIBILITY` lives here, evaluator-side, never in the packet.

`FUTURE_BLIND_PACKETS_READY: **documents ready ×3; surfaces built ×0; dispatchable to A or B ×0.**`

---

## 11 · What this document does not claim

- **It authorizes no run.** §9 of `controlled_benchmark_ab.md` still determines
  `BLIND FIRST PASS — BLOCKED BY CANONICALIZATION`, and P-2…P-4 are independently unmet.
- **It did not contact A or B and started no blind replication.**
- **Its pattern sweep is a screen with a demonstrated false negative** (`HC-X4`). The structural
  census is the instrument of record; every dispatch decision here rests on the census.
- **`HC-G2`'s clean result is a candidate, not a promotion.** One case, read by hand, against a
  census that still flags its paper.
- **Nothing was adjudicated.** Two facts were re-derived (§6.1, §6.2); both carry
  `NEEDS_SECOND_ADJUDICATION: YES`.
- **Nothing here is medical advice.**

---

## 12 · Summary

```
ROUND1_A_ELIGIBLE                   NO   — main carries the answer in 6 files + a commit subject,
                                           ancestral to both reader branches
ROUND1_B_ELIGIBLE                   NO   — same cause, symmetric
ROUND1_FRESH_READER_ELIGIBLE        YES  — conditional on the allowlisted surface being BUILT
                                           and the builder not being the reader

SCREEN_ONLY_REVIEWED                14 of 14
  screen false-positive rate        35% cumulative (9 of 26 read)
  screen false negatives            0
  MY pattern tool's false negatives 1 (HC-X4) -> census is the instrument of record

DISPATCHABLE_CASE_COUNT             0 in a checkout · 24 on a built surface
                                    48 - 13 blocked at MANDATORY = 35 clean at the surface;
                                    of those 35, eligibility itself blocks 11 (no surface held,
                                    premise falsified, different family) -> 24 dispatchable

CLEAN_BLIND_BY_ACTOR                in checkout   a:0  b:0  fresh:0
                                    on surface    a:35 b:35 fresh:35   (24 also eligible)
                                    a and b carry 2 declared one-sided memory residuals each

PARTICIPANT_VIEW_VERDICT            PASS after one structural repair. The prior tip carried 585
                                    files and 101 adjudications; it is now an orphan of 5 files,
                                    withdrawn tip kept at a tag. 5/5 mutations blocked.
                                    It is a DELIVERY REF, not a reading surface.

PROVENANCE_SEPARATION_FEASIBILITY   DEMONSTRATED 3 of 58. Blocked on 55 by missing structured
                                    page/crop/dpi, NOT by co-location. New leak channel found and
                                    closed: 7 of 27 crop filenames state conclusions; the fix is
                                    to emit a digest-derived handle, not a better word list.

GOLD_READY_COUNT                    0 READY. 2 acts PERFORMED this session (HC-A4, HC-C2), both
                                    still NEEDS_SECOND_ADJUDICATION. 3 more ranked by epistemic
                                    cost: HC-D2, HC-G3, HC-E2.

UNRESOLVABLE_CASE_COUNT             1  HC-A2 — surfaces complete, token undefined, nothing missing.
                                    Not dispatchable. Category membership != dispatchability.

PAIRWISE_SCORING_READY              YES — 6 gold-free dimensions; PAIRWISE_REPRODUCIBILITY and
                                    GOLD_ACCURACY defined as separate families, never combined;
                                    5 named cases defined incl. agreement-on-a-wrong-answer

PRIMARY_EVALUATION_ESTIMAND         ERROR_PER_CLAIM primary + ERROR_PER_PAPER anchor.
                                    Normative, not empirical. Non-convertible. m=15.7 measured,
                                    rho NOT measured. Frame still not enumerable by one command.

FUTURE_BLIND_PACKETS_READY          3 documents · 0 surfaces built · 0 dispatchable to A or B

NEXT_EVALUATION_ACTIONS             1  BUILD the allowlisted surface for BLIND-R1-001, outside every
                                       checkout, by an actor who is not the reader. It is the only
                                       act that converts 0 dispatchable into 24.
                                    2  Recruit or designate a reader with no history in this
                                       repository. A and B cannot be decontaminated; the surface
                                       can.
                                    3  Acquire PMID 12065620 and PMC3139124 — unblocks Round 2 and
                                       is the only route to a second UNRESOLVABLE.
                                    4  Retrieve figure rasters for PMID 34634460 and 32581702 —
                                       six cases are surface-incomplete for want of gr1..gr6.jpg.
                                    5  Publish the frame rule (PAPER / CORPUS / STUB). Every
                                       number in Phase 9 is downstream of it.
```

🔴 **The line to carry.** Three sessions have each found the same defect one level further out: the
answer is in the discipline files; no — in the readers' branches; no — **in the commit history
every branch descends from.** The pattern is not that the searches were sloppy. It is that each
one measured the surface it had thought about. The only structural answer is the one the protocol
already gives and this laboratory has never executed: **a surface built by allowlist, from
nothing, outside every checkout.** Until that directory exists, `CLEAN_BLIND` is a number about a
place nobody reads in.
