---
artifact: SCIENTIST_CROSS_REVIEW_PILOT_HOSTILE_REVIEW_MIRROR_v1
actor: mirror (worktree `mirror`, branch `mirror`)
role_contract_status: PROPOSED — NOT ACTIVATED
session_type: Operator-directed analytical review
canonical_authority: NONE — no BATCH_COMMIT, no canonical write, nothing mutated
verdict_vocabulary: governance/annex_c_review_protocol.md:40
subject: the closed three-seat Scientist cross-review pilot on PMID 32000863
---

# Four measurements were hardened and one was never taken, and both privacy gates are blind to the same file format for two independent reasons

## 0 · STANDING AND PRIOR ART — read this first

**The Mirror role contract is `PROPOSED`, not binding.** `roles/mirror.md` frontmatter reads
*"status: PROPOSED — binding once Mirror hostile review passes and the operator approves."*
This review is therefore an **Operator-directed analytical session**. It activates nothing,
grants nothing, and asserts no governance authority. Verdicts below use only the canonical
vocabulary at `governance/annex_c_review_protocol.md:40` —
`CONFIRMED | WEAKENED | REFINED (+REFINED_FORMULATION) | REFUTED`.

🔴 **A Mirror hostile review of this exact package already exists and the dispatch does not
mention it.** `reviews/mirror/SCIENTIST_PILOT_PROCESS_HOSTILE_REVIEW_MIRROR_v3.md`, 1 100 lines,
committed to this branch at `77be2f4`, **2026-08-25T21:57:44+02:00** — roughly two hours before
this task arrived. It is thorough and largely correct. This document is a **second, independent
pass**, not a replacement, and § 6 states plainly which findings are new, which corroborate v3 by
a different method, and which **correct** v3.

**Contamination disclosure.** While measuring refs at scope-setting time I read v3's *commit
message*, which names several of its conclusions (`448/333/39`, `8.71 %`, `74.33 %`, `42.7 %`,
`217 files`). Its **body was not opened until every measurement in § 3 had already been taken and
recorded.** Where my numbers agree with v3's, they were produced before I could see v3's.

🔴 **The dispatch's own premise does not survive measurement.** The task states *"The Scientist
package reportedly records eleven defects."* The string `eleven` occurs in the package only in
reference to **eleven Pathograph edges adjudicated by Scientist B**, never to defects. The
package's actual canonical-defect counts are **six** (A's synthesis § K, `K-1…K-6`), **five**
(A's reconciliation), and **four** (B's handoff § 7; C's Phase I). There is no register of
eleven, and no register of any number that the three seats share — see § 4.1.

---

## 1 · OBSERVATION_SCOPE

Measured, not taken from chat. All `git` commands run in `/Users/…/legend-public/.claude/worktrees/mirror`.

### 1.1 Refs and HEADs

| Seat | Branch | HEAD | Merge-base with `main` | Behind `main` | Own commits |
|---|---|---|---|---:|---:|
| Scientist A | `lettore` | `605fc5d` 19:23:47 | **`9b0cf47` (2026-08-14)** | **201** | 16 |
| Scientist B | `lettore-b` | `9a09590` 18:29:06 | `788c357` = `main` | **0** | 16 |
| Scientist C | `lettore-c` | `5b1d6c2` 19:26:47 | `788c357` = `main` | **0** | 14 |
| Mirror (me) | `mirror` | `77be2f4` 21:57:44 | `788c357` = `main` | 0 | — |
| `main` | `main` | `788c357` 2026-08-22 | — | — | — |
| Orchestrator (context only) | `legend-operating-convention-v1` | `a58af46` | `788c357` | 0 | 26 |

🔴 **Scientist A ran the entire pilot from a base eleven days and 217 changed files behind the
tree B and C measured.** `git merge-base lettore main` = `9b0cf47`, dated 2026-08-14;
`git rev-list --count lettore..main` = **201**. This is not cosmetic: § 3.5 shows A's own ref
carries **106** read receipts where every other ref carries **128**, so a denominator A published
could not have been derived from A's tree.

### 1.2 The evidence surface — and it is different for every seat

`files/` is gitignored, therefore **per-worktree**. Manifest-declared artifacts present on disk:

| Tree | of 448 declared | figures /333 | PDFs /39 | `files/fulltext/*.pdf` |
|---|---:|---:|---:|---:|
| **shared checkout** `/Users/…/legend-public` | **428** | 313 | **39** | **55** |
| A `lettore` | 169 | 128 | 17 | 9 |
| B `lettore-b` | 48 | 37 | 4 | 3 |
| C `lettore-c` | 4 | 2 | 1 | 1 |
| Mirror `mirror` | **0** | 0 | 0 | **0** (no `files/` directory at all) |

This table is the single most important fact in the review and § 3.4 and § 5.1 both turn on it.

### 1.3 What I could not reach — declared, not inferred

- **The recipe gate cannot run in this worktree.** `regenerate_adjudications.py verify` at `mirror`
  exits **1** with three `source PDF absent` failures. All § 5 gate work was therefore done on a
  **scratch root** (`ROOT = Path(__file__).resolve().parents[2]`) with `files/` symlinked
  read-only to the shared checkout. Baseline there reproduces the declared `27 / 47` exactly.
- **Orchestrator and Plan active work was not inspected.** `legend-operating-convention-v1` and
  `plan-orchsurf-r4-transcription` were read **only** for ref/timestamp facts needed to date the
  Pathograph object (§ 5.4). No unfinished work was opened, no message sent, nothing routed.
- **No OCR was performed.** Any claim about what a raster panel *depicts* is outside this review.
- **I am not the scientific authority.** Nothing here adjudicates lithium, GSK-3β or WWOX
  mechanism. § 16 lists what must go back to a Scientist.

### 1.4 This review mutated nothing

| Check | Result |
|---|---|
| Canonical/governance files changed by A, B, C (each vs **its own** merge-base) | **0 / 0 / 0** |
| Positive control — same predicate on `legend-operating-convention-v1` | **6 files** — predicate does detect change |
| Gate mutation testing | scratch root only; repo tree never written |
| `legend_lint.py .` at `mirror` HEAD | `VERDICT: PASS` |

---

## 2 · PACKAGE INVENTORY — 33 files, not 25

The dispatch says 25. Measured, each seat against its own merge-base:

| Seat | Files | Namespace |
|---|---:|---|
| A `lettore` | **12** | `learning/scientist/` ×10, **`framework/protocols/` ×2** |
| B `lettore-b` | **16** | `reviews/scientist-b/` ×15, `learning/scientist-b/` ×1 |
| C `lettore-c` | **5** | `learning/scientist/` ×5 |
| **Total** | **33** | three namespaces, three branches |

🔴 **Two structural consequences the package does not draw.**

1. **A and C write into the same directory (`learning/scientist/`); B writes into
   `reviews/scientist-b/`.** B records the effect at `PHASE2_ROUND_RESPONSE_SCIB_v1.md:57` — a peer
   sweep scoped to `^learning/` *"could not have found them."* A namespace split silently made one
   seat of three less visible to the others' sweeps.
2. **A placed two `PROPOSED` files on `framework/protocols/`** — a normative path in the
   `CLAUDE.md` routing table. Still present at A's HEAD. A self-reported this (`d3fcfc0`); it is
   unrepaired and is a live placement question for the Operator, not for me.

---

## 3 · INDEPENDENTLY REPRODUCED MEASUREMENTS

Every figure below was recomputed from the corpus before v3's body was read.

### 3.1 Manifest census — reproduces exactly

```
manifests 64 · with source_artifacts 60 · declared artifacts 448
kind=figure 333 (74.33 %) · .pdf 39 (8.71 %)
```

**Hostile check the package did not run.** `kind == "figure"` and *image file extension* are two
different definitions that both return 333. They are **the same set** — `figure\bye = 0`,
`bye\figure = 0`. The convergence is real, not coincidence. `333` is robust.

🔴 **But the denominator has a contaminant.** `article_binary` = 44 while `.pdf` = 39. The five
non-PDF `article_binary` entries include **two `ppi_preflight.json` files — LEGEND's own tool
output, declared as `source_artifacts`.** 448 is 446 publisher artifacts + 2 self-generated. The
effect on the headline rates is small (333/446 = 74.66 %, 39/446 = 8.74 %) and the *class* is not:
**the instrument's output is inside the population the instrument is measuring.**

### 3.2 Locator population — 1 002, and the gate reaches 4.7 %

| Surface | Locators | Share |
|---|---:|---:|
| `body` | 617 | 61.6 % |
| **`figure`** | **338** | **33.7 %** |
| *(no surface declared)* | 33 | 3.3 % |
| `table` | 13 | 1.3 % |
| `supplement` | 1 | 0.1 % |
| **Total** | **1 002** | |

### 3.3 The recipe gate baseline — reproduces exactly

`regenerate_adjudications.py verify` on the scratch root:
`OK: 27 adjudication artifact(s) … and 47 locator(s) …`, **exit 0**. Confirmed: 3 studies,
27 crops, 47 adjudications, 7 of the 27 crops adjudicating **zero** locators.

### 3.4 The figure/no-text rate — reproduced on **two** engines

Corpus: `/Users/…/legend-public/files/fulltext/*.pdf`, **55 PDFs, 55 opened, 0 unreadable** —
i.e. **the shared checkout**, which is the only tree that holds 55 (§ 1.2).

| threshold pt² | **pdfminer.six** figs / no-text | **PyMuPDF `get_text("dict")`** figs / no-text | A published | C published |
|---:|---|---|---|---|
| 5 000 | 383 / 272 = **71 %** | 347 / 243 = 70 % | 384 / 270 = 70 % | — |
| **20 000** | **242 / 175 = 72 %** | 237 / 175 = 74 % | **242 / 173 = 71 %** | **237 / 173 = 73 %** |
| 50 000 | 186 / 137 = **74 %** | 181 / 137 = 76 % | 186 / 135 = 73 % | — |
| 100 000 | 122 / 85 = **70 %** | 117 / 85 = 73 % | 122 / 84 = 69 % | — |

⇒ **The ~70–74 % plateau survives a change of PDF parser.** `pdfminer.six` shares no code with
MuPDF. This is the first genuinely cross-engine corroboration in the file: v3 § 3.3 re-implemented
in PyMuPDF, i.e. the producers' own engine.

### 3.5 K-5, the MAJOR candidate — reproduces exactly, including A's refusal to inflate it

`fulltext_read_receipts.jsonl`, 128 records at `main`, `lettore-b`, `lettore-c`:

```
record_kind = legacy_reconstruction   22   ← the class
record_kind = receipt_invalidation     1   ← A correctly REFUSED to count this
contemporaneous_receipt, fingerprint null 4 ← A correctly called these honest
                                       ── 27 null-fingerprint total
```

**22 of 22 (100 %)** have `evidence_basis` citing the very `PAPER nnn` entry their `outputs`
point at; 22/22 `source_fingerprint: null`; 22/22 `evidence_depth: partial_fulltext_read`.
**The circularity claim is exact.** A's insistence on 22 rather than 23 — *"counting it files a
repair as a defect"* — is correct and is the best single act of discipline in the package.

🔴 **And A's own ref carries 106 receipts, not 128.** The `128` denominator is not derivable from
A's tree. A published a correct number about a tree A was not standing on.

### 3.6 B's propagation count — reproduces exactly, then stops travelling

B published the command, the anchor and the exclusion:

```bash
git grep -lI -iE "GSK3.{0,3}(β|beta) is elevated" HEAD -- . ':!reviews/scientist-b'
```

| Ref | files asserting | tracked denominator |
|---|---:|---:|
| `2261a15` (B's stated anchor) | **14** ✅ | **581** ✅ |
| `8612baa` (B's *other* stated anchor) | 14 | 581 |
| `main` | 14 | 580 |
| **`lettore` (A)** | **17** | 435 |
| **`lettore-c` (C)** | **16** | 585 |

`git rev-parse 8612baa:…/claim_registry_current.md` = **`9f4bcede`**, exactly the blob B cites.
**B's measurement is fully verified, and B explicitly excluded its own record because *"recording
the negative would otherwise falsify it."*** That is exemplary.

🔴 **And the guard is written as a path, not as a class.** `:!reviews/scientist-b` protects B
alone. Run B's own published command on A's or C's ref and the pilot's own artifacts — which live
in `learning/scientist/` — are counted as instances of the defect they describe: **17 and 16**.
A correct safeguard, correctly reasoned, that silently protects the wrong actor the moment anyone
else executes it.

---

## 4 · DEFECTS CONFIRMED

### 4.1 There is no defect register, so "is the list complete?" has no referent

| Source | Count | Contents |
|---|---:|---|
| A · `FINAL_SCIENTIFIC_SYNTHESIS` § K | **6** | K-1…K-6 |
| A · `SCIENTIST_TEAM_RECONCILIATION` | **5** | K-1…K-5; **K-6 absent** |
| B · `HANDOFF_SCIB` § 7 | **4** | |
| C · Phase I | **4** | |
| **Dispatch** | **11** | not found in any artifact |

The package carries **203 `🔴` markers** across 33 files and **six mutually unreconciled ID
schemes** (`F-`, `E-`, `L-`, `D-`, `R-`, `J-`, plus `K-`, `M-`, `O-`). 🔴 **A's own two closing
artifacts disagree with each other by one defect (K-6).** No file in the package is the register.

### 4.2 Confirmed by reproduction

| ID | Claim | Verdict |
|---|---|---|
| K-5 | 22-of-128 circular legacy receipts | **CONFIRMED**, 100 % exact (§ 3.5) |
| B-2 | 14 tracked files assert the unsupported wording, 1 states the correction | **CONFIRMED** at B's anchor (§ 3.6) |
| C/A | 55 PDFs, 9 figure-less, ~71–74 % no-live-text | **CONFIRMED**, and on a second engine (§ 3.4) |
| A | 448 / 333 / 39, 74.33 % / 8.71 % | **CONFIRMED** exactly (§ 3.1) |
| C (final) | 338 figure locators, 0 carrying a crop/region field | **CONFIRMED** (§ 3.2, § 5.3) |
| all | no seat mutated canonical state | **CONFIRMED** with positive control (§ 1.4) |

### 4.3 The A-vs-C denominator dispute — settled for A, by a third engine

A published **242** (`get_image_info`); C published **237** (`get_text("dict")`); A argued
*"my denominator is the sounder one, C's is an undercount."*

`pdfminer.six` reproduces **A's entire column**: 383/242/186/122 against A's 384/242/186/122.
On the three pages A named as the cause:

| Page | `get_text("dict")` (C) | `get_image_info` (A) | **pdfminer.six** |
|---|---:|---:|---:|
| Cheng suppl. p9 | 2 | 3 | **3** |
| Cheng suppl. p13 | 2 | 3 | **3** |
| Cheng suppl. p21 | **0** | 2 | **2** |

A's out-of-bounds bboxes reproduce to the decimal (`x0 = −77.5`, `x1 = 730.3` on a 595.3-wide
page). ⇒ **A was right, C's 237 was an undercount, CONFIRMED independently.** My own PyMuPDF
`get_text("dict")` run also returned 237 — i.e. I reproduced *C's error* before the independent
engine broke the tie, which is itself the point of using one.

---

## 5 · NEW DEFECTS FOUND BY MIRROR

### 5.1 🔴 M1 — Both privacy gates are blind to `.jsonl`, and this is a **second** cause v3 missed

v3 § 4.5 (`M3-10`) established that `PRIVATE_NAME` fires on the capitalised form and is blind to
the lowercase path form, and listed among its evidence two shipped surfaces:
`fulltext_read_receipts.jsonl` and `framework/state/sync_epochs.jsonl`.

**White-box, with a positive control:**

```
sha256("<Given>")  ∈ PRIVATE_IDENTIFIER_DIGESTS  → True
sha256("<given>")  ∈ either digest set           → False      (v3's cause — CONFIRMED)
sha256("<tok3>")   ∈ CASEFOLD_IDENTIFIER_DIGESTS → True        (positive control)
```

**Four-cell mutation, five fixtures, one scan, both gates:**

| Fixture | `independent_privacy_scan.py` | `public_release_gate.py` |
|---|---|---|
| `upper.md` — capitalised in Markdown | **BLOCK** ✅ | **BLOCK** ✅ |
| `upper.json` — capitalised in JSON | **BLOCK** ✅ | **BLOCK** ✅ |
| **`upper.jsonl` — capitalised in JSONL** | **no finding** ❌ | **no finding** ❌ |
| `lower.md` — lowercase path form | no finding ❌ | no finding ❌ |
| `lower.jsonl` | no finding ❌ | no finding ❌ |

```python
public_release_gate.TEXT_SUFFIXES        # '.json' in → True ; '.jsonl' in → False
independent_privacy_scan.TEXT_SUFFIXES   # '.json' in → True ; '.jsonl' in → False
```

⇒ **There are two independent causes of the green, not one.** For the two `.jsonl` files in v3's
own evidence table, **repairing the case rule would not close the gap** — those files are never
opened. **10 tracked `.jsonl` files, 1 137 lines**, are invisible to both gates, including
`fulltext_read_receipts.jsonl` (128), `HUMAN_APPROVAL_QUEUE.jsonl`, `growth_anchors.jsonl`,
`sync_epochs.jsonl`, and a 706-line PubMed corpus seed carrying author names, affiliations and
ORCIDs.

🔴 **And the tool named `independent_privacy_scan.py` exists to be a second, independent check on
`public_release_gate.py`. Each defines its own `TEXT_SUFFIXES`. Both include `.json`. Both omit
`.jsonl`.** The independence is in the code path and not in the population — which is precisely
the failure class this pilot was convened to study, occurring in the repository's own
publication-safety architecture. **Requires Human Gate.**

*Ref-bound, per § 8's own rule:* the 10 `.jsonl` files and 1 137 lines are measured at both `main`
and `mirror` (identical). The lowercase-form exposure is **48 occurrences / 21 files at `main`**
and **74 / 38 at `mirror`** — the difference being this branch's own Mirror review artifacts,
which cite worktree paths for exactly the scope-declaration reason § 14 commends.

*Corollary, minor:* all 4 live `PRIVATE_NAME` findings at `mirror` are **one three-letter
identifier — redacted here as `<tok3>` — matched inside SHA-256 hex strings**: a 100 % false-positive
rate on that category, because the token boundary is `(?<![A-Za-z])…(?![A-Za-z])` and hex digits
are not letters. 🔴 **Writing this finding out in full produced two fresh BLOCK findings in this
very file**, which is why the token is redacted: on this surface, recording the negative falsifies
it. That is the same self-inclusion hazard B guarded against in § 3.6, met from the other side.

### 5.2 🔴 M2 — The quantity four rounds hardened is not the quantity that matters

Both seats state that ~73 % is *"a lower bound on the failure."* Neither measured how far above it
the true value sits. `regenerate_adjudications.py` requires a needle that is **(i) unique on the
page** and **(ii) resolves to a span fully inside the crop**. Applying both conditions, over the
same 55 PDFs at the same 20 000 pt² threshold, allowing 1–8-word candidate needles (the most
generous reading — the snippet-fragment condition is *not* enforced, so this is itself a lower
bound):

```
figures                                          242
  no live text intersecting   (their number)     175   72.3 %
  live text intersects                            67   27.7 %
      …and a unique in-crop needle EXISTS         35   14.5 %
      …and NO unique in-crop needle               32   13.2 %
TRUE needle-unreachable = 207/242 =            85.5 %
```

⇒ **Four rounds moved a number by 3 points (71 → 74) inside a bracket that sits 11–14 points
below the quantity a consumer needs.** Of the 67 figures with intersecting text, **fewer than
half** admit a needle at all. The refinement was rigorous, mutually adversarial, reproducible —
and aimed at a proxy. Stable at 85.5 % whether candidate needles are capped at 3 words or 8.

### 5.3 🔴 M3 — The recipe gate's green sentence, and four fail-open paths

Mutation battery on the scratch root, `regenerate_adjudications.py verify`:

| # | Mutation | Exit | Verdict |
|---|---|---:|---|
| M4 | one declared `sha256` corrupted | **1** | closed ✅ *(control)* |
| M6′ | `needle` removed from every adjudication | **1** | closed ✅ *(control)* |
| M7 | adjudications reduced to bare locator strings | **1** | closed ✅ *(control)* |
| M10 | `manifest` repointed to a different study | **1** | closed ✅ *(control)* |
| **M1** | `page_adjudications/` **emptied** | **0** | 🔴 `OK: 0 … and 0 …` |
| **M2** | `page_adjudications/` **deleted** | **0** | 🔴 `OK: 0 … and 0 …` |
| **M3** | one artifact's `sha256` **removed** | **0** | 🔴 passes, **and still prints `27 … regenerate to their declared digest`** when only 26 declare one |
| **M8** | `manifest` key absent | **0** | needle↔locator binding skipped, warning to stdout |
| **M9** | **`manifest` path typo'd to a nonexistent file** | **0** | 🔴 **indistinguishable from M8** |

Four controls fire, so the harness is real. The two that matter:

- **M9 is the sharpest.** `snippets()` returns `None` both when `manifest` is *absent* and when the
  declared path *does not exist*. The two are conflated, and the printed message —
  `"no manifest declared"` — **is false in the second case**: a manifest *is* declared, it just
  cannot be found. A single-character typo silently downgrades the gate to its weaker check and
  reports the downgrade as a design choice.
- **M3's summary sentence overclaims.** `checked` increments whether or not a digest was declared,
  so the green line asserts a property of 27 artifacts that holds for 26.

*(Complementary to v3 § 4.1, which established by string search that no gate invokes `verify` at
all. Both are true: the recipe gate is unwired **and** fail-open where it is run by hand.)*

### 5.4 🔴 M4 — Phase I was adjudicated against an object that was on no ref

| Ref | files matching `pathograph` |
|---|---:|
| `main` | **0** |
| `lettore` (A) | **0** |
| `lettore-c` (C) | **0** |
| `lettore-b` (B) | 2 — **B's own two review artifacts, not the object** |
| `legend-operating-convention-v1` (Orchestrator) | 4 — **the object** |
| `plan-orchsurf-r4-transcription` (Plan) | 1 |

The object (`pathograph_export.jsonl`, `pathograph.py`, `pathograph_inventory.md`,
`test_pathograph.py`) first reached **any** ref at **17:02:49** (`d422829`, Orchestrator).
**B adjudicated twenty edges against it at 15:46:25 — 76 minutes earlier.** It is still absent
from `main` and from every Scientist ref.

⇒ 🔴 **C's Phase I negative — *"the Pathograph is not present in this repository"* — was TRUE of
every ref in the repository at the moment C wrote it.** C withdrew it at 17:27:43, after a third
actor had committed the object to a branch C was not reading. **C conceded a correct negative
because the tree moved underneath it**, and no field in the record distinguishes *"I was wrong"*
from *"the world changed."* B's own commit `204c84c` (*"A commit timestamp dates publication, not
observation"*) is the same discovery from the other side.

### 5.5 M5 — The run's headline process statistic is not recomputable

*"Eight rounds"* occurs **exactly once in the entire package**
(`OPERATING_PRACTICE_OBSERVED_SCIC_v1.md:314`), inside C's sentence *"Scientist A disagreed with me
on a conclusion for the first time in eight rounds."* **No artifact defines a round.** The
statistic that the dispatch elevates to a premise about the whole run is (a) undefined, (b)
scoped to the **A↔C pair only**, and (c) about *A contradicting C* — while B was contradicted by
a peer at **16:01:26**, the twelfth commit of the run.

---

## 6 · RELATIONSHIP TO MIRROR v3 — stated, not implied

| # | This review | Status vs v3 |
|---|---|---|
| M1 `.jsonl` blind spot | § 5.1 | **NEW — and corrects v3's single-cause attribution** |
| M2 85.5 % true unreachable rate | § 5.2 | **NEW** — measured by neither producers nor v3 |
| A-vs-C denominator settled by `pdfminer.six` | § 4.3 | **NEW in kind** — v3 § 3.3 re-implemented in PyMuPDF |
| M3 recipe-gate fail-open battery | § 5.3 | **NEW** — v3 § 4.2 mutated `deepdive_manifest.py` |
| M5 "eight rounds" undefined | § 5.5 | **NEW** |
| Dispatch's "eleven defects" unsupported | § 0 | **NEW** (v3 was not given this dispatch) |
| B's guard is path-literal, yields 17/16 elsewhere | § 3.6 | **NEW** |
| Privacy gate case-blindness | § 5.1 | **corroborates v3 `M3-10` by a different method** |
| Missing class = ref-dependent measurement | § 8 | **converges independently** on v3 § 2.3 |
| `1 002` locators, `338` figure, `33` unclassified | § 3.2 | **corroborates** v3 § 3.5 |
| Stale-base consequences for A | § 1.1, § 3.5 | **corroborates**, adds the 106-vs-128 instance |

---

## 7 · COMPLETENESS BOUNDARY — what this review cannot claim

- **I did not read all 33 files end to end.** I read the closure artifacts, the disputed sections,
  and every passage a measurement touched. A finding stated only in an unread passage of A's
  50 KB or B's 74 KB operating-practice files would be invisible to me.
- **My trigger classification (§ 12) is a regex over commit bodies**, hand-verified on a 3-commit
  sample. It detects *"a peer is mentioned and an error is admitted"*; it cannot prove causation.
- **The `85.5 %` needle figure is itself a lower bound** — it ignores the snippet-fragment
  condition, which can only reduce needle availability further.
- **No OCR, no image inspection.** Every claim about figure *content* is out of scope.
- **`.jsonl` exposure is quantified by file and line count, not by adjudicated sensitivity.**
  Whether the lowercase path form *should* be a publication blocker — **48 occurrences across 21
  tracked files at `main`; 74 across 38 at `mirror`, which carries this branch's own review
  artifacts** — is an Operator decision, not a Mirror finding. What is a Mirror finding is
  that the gates' behaviour on them is **inconsistent with their own configuration**.
- **Ref-bound.** Everything above holds at the HEADs in § 1.1. Any of these numbers may decay the
  moment a branch moves — which is, exactly, § 8.

---

## 8 · FAILURE-CLASS ANALYSIS

**A: TRANSPORT** — genuinely distinct. Repair: *make the record reach the surface.* Confirmed
instances: the 2026-08-04 commit candidate lost for three weeks; `CLAIM 016`↔`CLAIM 036`.

**B: UNDECLARED SCOPE** — genuinely distinct. Repair: *make the tool print its own denominator.*

**E: TOOL-APPLICABILITY GAP — collapses into B.** *"The recipe cannot express image evidence"* is
a scope statement about the same mechanism, and it takes the same repair (declare the population).
🔴 **And C refuted E outright in the run's final commit** (`5b1d6c2`, 19:26:47): artifact→digest
is mechanised at **100 %** for figures, region-within-artifact at **0 %**, and *both seats had
already improvised the correct image recipe* (A: `crop(0,395,240,553)`+digest; C: a supplement JPG
crop A reproduced bit-for-bit). **E as stated is false; the honest form is a partial mechanism,
not an absent one.** Keeping E as a fifth class preserves a conclusion its own authors withdrew
17 minutes before the run ended.

**C: NARRATED GAP** — genuinely distinct, and it recurs inside the corrections that name it
(A's `64b7976`: *"I explained a discrepancy instead of measuring it"*). Repair: *require the
measurement, not the mechanism story.*

**D: WRONG DENOMINATOR** — genuinely distinct. Repair: *enumerate the population before measuring.*

🔴 **MISSING CLASS — a measurement whose truth value depends on the ref and the instant it was
taken, published without either.** Adjacent to D and not D: D is *which population*, this is
*which snapshot*. Independently derived here from four instances, and it is what v3 § 2.3 named
`STALE-REF MEASUREMENT`:

- A's 55-PDF corpus measurement, taken on the shared checkout, published without the tree, in a
  document that elsewhere records A's own tree holding 34 files where the checkout held 174;
- A's `128` receipts, where A's own ref holds 106;
- B's command, returning 14/17/16 across three refs;
- C's Pathograph negative, true when written and false 85 minutes later.

**It is invisible from inside the run, because a tree looks the same from inside whatever its
age.** Repair: *publish the ref with the number* — different from all five above, and mechanical.

*These are local review concepts. I propose no governed vocabulary.*

---

## 9 · GATE-COVERAGE ANALYSIS

| Question | Answer |
|---|---|
| Population the gate covers | **3 studies, 27 crops, 47 adjudications** |
| Population it appears to claim | its summary sentence names only its own counts — it does **not** overclaim the corpus |
| Corpus share | **47 / 1 002 locators = 4.7 %**; **3 / 64 studies = 4.7 %** |
| Does green imply what a consumer thinks? | **No** — see M3 above and the zero-coverage path |
| Is the pilot's own paper covered? | 🔴 **No. PMID 32000863 carries 25 locators; 0 are gated.** |
| Structurally unreachable classes | `figure`-surface locators (**338, 33.7 %**) — the recipe requires `source_pdf`+`page`+`crop`+`dpi`; also the 33 locators with **no declared surface at all** |
| Fail-open, invisible, or named? | 🔴 **Fail-open and unnamed** on four paths (§ 5.3) |

**Broken tool, missing scope declaration, or missing ingestion?** None of the three. It is a
**sound mechanism with an unstated population and no floor**: correct where it runs, silent about
where it does not, and green when it runs nowhere.

> A green gate that does not cover the object under adjudication is not evidence that the object
> passed. **Measured: the gate does not cover the pilot's paper, and returns `OK` with `exit 0`
> when it covers nothing at all.**

**The tool was not altered.**

---

## 10 · CORPUS / ASSET-CLASS ANALYSIS

Reproduced in § 3.1. On applicability of the locator/needle recipe:

| Evidence class | Share | Recipe applicability |
|---|---:|---|
| PDF-page / crop evidence | 39 artifacts, 8.7 % | **Fully applicable** — and exercised on 3 papers |
| Standalone figure images | 333 artifacts, 74.3 % | **Partially applicable.** artifact→digest **100 %**; region-within-artifact **0 %** |
| `article_text` (XML/HTML) | 58 | text-verified by the manifest gate |

⇒ **This is a structural coverage boundary, and it is a boundary of the *within-artifact*
localisation link only, not of the whole chain.** *"Verification often fails"* and *"the
representation cannot apply"* are both wrong. The correct statement, which is C's and which I
confirm: **link 1 of 5 is universal for images and better covered than for PDFs; links 2–5 are
absent by construction, and the remedy needs `artifact digest · pixel crop box · crop digest` —
not `source_pdf`/`page`/`dpi`.**

---

## 11 · INDEPENDENT-METHOD ANALYSIS

**Does the ~71–74 % plateau survive?** Attacked on three axes:

| Axis varied | Result |
|---|---|
| Area threshold, 20× sweep (5 k → 100 k pt²) | 70–74 % on pdfminer; 73–76 % on PyMuPDF — **survives** |
| **Parser** (MuPDF → pdfminer.six) | 72 % vs 71 % at 20 k — **survives** |
| Image-enumeration API within one parser | 242 vs 237 — **the one axis that moves it**, and pdfminer breaks the tie for 242 |
| **Criterion** (text-intersects → needle-exists) | **71–74 % → 85.5 % — DOES NOT SURVIVE** |

⇒ **The plateau is a real property of the corpus and not an artifact of shared implementation
choices.** The two seats' agreement on ~73 % was *not* a shared-blind-spot agreement — a third
engine confirms it. **But the plateau is robust as an answer to a question that is not the one the
gate poses**, and against the gate's actual predicate the number is 85.5 %.

---

## 12 · CROSS-REVIEW ROUND RECONSTRUCTION

46 commits, three seats, 2026-08-25 00:12:50 → 19:26:47. Classified by regex over commit bodies,
hand-verified on a sample:

| Action | n | Share |
|---|---:|---:|
| **Peer challenge → actor corrects its own work** | **30** | **65 %** |
| Actor corrects a peer | 8 | 17 % |
| Additive / extension | 7 | 15 % |
| **Unprompted self-correction** | **1** | **2 %** |

🔴 **The additive phase is sharply bounded.** All 7 extension commits fall between 00:12:50 and
**15:46:25**. **After 15:46:25, 39 of 39 commits are corrections.** The dispatch's *"most early
rounds were additive"* is **CONFIRMED**, with a measured boundary the package does not state.

🔴 **The three seats did not close together.** **B's last commit is 18:29:06.** A and C continue
for a further **57 minutes and 12 commits** — the entire figure-population collision, the
denominator dispute, and C's final retraction of the image-recipe conclusion. **B's closing
synthesis cannot contain the run's last and sharpest exchange, and nothing in the package says so.**

**Adversarial vs additive:** genuinely adversarial from 15:49 onward; the A↔C exchange from 18:30
to 19:26 alternates every ~4 minutes.

**Did repeated review keep producing value, or only volume?** It kept producing value **and the
value changed character**: the last six exchanges produced two retractions (C's 43 % bracket, and
the *jointly settled* image-recipe conclusion) rather than refinements. C's final commit corrects
a conclusion **A and C had just agreed on** — *"joint settlement is where the next thing lives."*
That is the opposite of a run padding its count.

**Was unresolved disagreement preserved?** Yes — A's reconciliation carries an explicit
`LAYER 3 · LIVE DISAGREEMENTS` and an `L-4 · UNRESOLVED` row. **Preserved, not closed.**

---

## 13 · SELF-CORRECTION VS CROSS-CORRECTION

**The package's claim is CONFIRMED, and understated.** In 46 commits there is exactly **one**
unprompted self-correction: B's `44d96e5`, a coverage audit of B's own Phase IV run *before*
claiming the phase delivered, which found that `F-4` and `F-5` inherited a category error B had
just rejected in a peer. It is the only commit in the run where an actor found its own defect with
nobody pointing.

🔴 **Against 30 commits where a peer's challenge caused the actor to correct its own work.**

**Could the producer have seen it?** For the findings I closed myself, mostly **no** — and this is
the decisive input to § 14:

| Finding | Visible from producer's surface? |
|---|---|
| `.jsonl` gate blind spot (M1) | **No** — requires opening two tools' `TEXT_SUFFIXES` and a 4-cell mutation |
| 85.5 % needle rate (M2) | **No** — requires implementing the gate's predicate over the corpus |
| Recipe-gate fail-open (M3) | **No** — requires a scratch root and a mutation battery |
| Pathograph on no ref (M4) | **No** — requires sweeping *other actors'* refs |
| A-vs-C denominator | **No** — requires a third parser |
| B's 17/16 at other refs | **No** — requires executing B's command on refs B cannot see |

⇒ **Six of six were closed by a command, not by a reading.** None required a better reader; all
required a different **surface** or a different **instrument**.

---

## 14 · ROLE-CONTRACT ARCHAEOLOGY — evidence only, no contract edited

### OBSERVED PRACTICE (Scientist) — worth preserving

1. **Publish the command, the anchor and the exclusion together.** B's
   `git grep … ':!reviews/scientist-b'` at HEAD `2261a15`, blob `9f4bcede`, with the stated reason
   *"recording the negative would otherwise falsify it."* Reproduced exactly, 11 hours later, by an
   actor with no access to B's session.
2. **Refuse to inflate a defect count.** A's 22-not-23, because counting a `receipt_invalidation`
   *"files a repair as a defect."*
3. **Re-measure a peer's dispute rather than conceding it.** C's `10f58e0` — *"Measured rather than
   conceded"*; A's `a9470c1` — testing *"whether the number survives the choice."*
4. **Attack the conclusion you just agreed on.** C's final commit; A's *"joint settlement is where
   the next thing lives."* The single highest-yield behaviour observed.
5. **Preserve unresolved disagreement as a layer**, not as a compromise.
6. **Correct attribution against your own interest.** A's K-2 note: the defect was found by the
   system on 2026-08-04, not by any of the three seats.

### OBSERVED FAILURE (Scientist)

7. Publishing a measurement without the tree it was taken on (§ 8, four instances).
8. Writing a safeguard as a path literal rather than as a class (§ 3.6).
9. Hardening a proxy for four rounds without testing it against the predicate it stands for (§ 5.2).
10. Closing a phase while a peer is still running (§ 12) with no record that the package is partial.

### CONTRACT-CANDIDATE EVIDENCE (Mirror)

- **Mirror should own:** independence, provenance, ref/scope discipline, tool-applicability,
  denominator integrity, wrong-reason success, gate mutation testing, publication-safety escalation.
- **Mirror should NOT own:** scientific adjudication. Three times here the correct move was to
  route rather than decide (§ 16). ⚠️ **And Mirror should not be its own only reader**: v3 attributed
  a green to one cause where there were two, and the second was found only because a second Mirror
  pass re-derived it from the tool source rather than from v3's conclusion.

### CONTRACT-CANDIDATE EVIDENCE (Orchestrator) — from the completed Scientist workflow only

- **Addressing is the binding constraint.** Three seats, three namespaces, three `files/`
  populations, one seat 201 commits behind. Nothing in the workflow told any seat this.
- **A future Orchestrator must publish, per cycle:** each seat's base commit, each seat's evidence
  population, and the shared-vs-isolated status of every path a measurement may touch.
- **Stopping is not synchronised.** B stopped 57 minutes before A and C. No signal existed to say
  so, and the package does not record it.

---

## 15 · REMEDIATION CANDIDATES, RANKED BY FAILURE ADDRESSED

| # | Candidate | Addresses | Cost | Who |
|---|---|---|---|---|
| **1** | Add `.jsonl` to `TEXT_SUFFIXES` in **both** gates; re-run; adjudicate the resulting findings | M1 — publication safety | one line ×2 | **Human Gate** |
| **2** | Decide the lowercase path form: in scope or out. If in, the digest set needs the folded form; if out, say so in the tool | v3 `M3-10` + M1 | small | **Human Gate** |
| **3** | Make `regenerate_adjudications.py` fail on zero coverage, and distinguish *manifest absent* from *manifest path unresolvable* | M3 — fail-open | ~6 lines | Plan → Operator |
| **4** | Make the gate's green sentence name its own denominator (`n of 1 002 locators`, `n of 64 studies`) | B / § 9 | small | Plan |
| **5** | Require every published measurement to carry the ref it was taken at | the missing class | convention + lint | Plan → governance |
| **6** | One defect register per cycle, one ID scheme, one owner | § 4.1 | convention | Orchestrator |
| **7** | Extend the crop recipe to `artifact digest · pixel crop box · crop digest` for image artifacts | § 10 — 338 locators | design | Plan (**C already specified it**) |
| **8** | Wire `regenerate_adjudications.py verify` into `run_release_regressions.py` | v3 `M3-8` | one line | Plan |
| 9 | Re-home A's two `PROPOSED` files off `framework/protocols/` | § 2 | trivial | Operator |
| 10 | Fix `PRIVATE_NAME` token boundaries to exclude hex runs | § 5.1 corollary | small | Plan |

**None of these were applied. Nothing was repaired. Nothing was propagated.**

---

## 15b · DISPOSITION — Operator decision of 2026-08-25, and what it did not reach

Candidates **1** and **2** were approved by the Operator and implemented at **`f281292`**
(delta-only: 2 detectors + 2 test suites, +196/−1). Recorded here so the "Requires Human Gate"
rows above are not left open in the record.

| | Approved | Implemented as | Evidence |
|---|---|---|---|
| 1 | `.jsonl` scanned like `.json` | added to `TEXT_SUFFIXES` in **both** gates | 9-fixture battery; 8 new tests; mutation control |
| 2 | lowercase identifiers in tracked paths in scope | casefold digest consulted **only in path context** | same battery; homonym tests still green |

🔴 **The naive form of candidate 2 was wrong, and the existing suites are what caught it.**
Both `test_common_lowercase_homonym_does_not_block` (release gate) and its scanner twin assert
that the lowercase token must **not** block — because it is also an ordinary Italian word.
The exact-only digest was a **decision, not an omission**, and my first implementation — adding
the casefold digest globally — would have turned twelve sentences of shipped Italian prose into
publication blockers. **§ 5.1 named a real gap and mis-stated its cause: I called a tested
design choice a defect.** The repair is therefore scoped to path context, where the token cannot
be the common word. *This is the same error class § 8 names, committed by this review.*

**Measured impact on the clean tracked tree** (old vs new detectors, same content):
36 → **701** findings, 2 → **301** blocks. **612 of the 683 new blocking findings are one file** —
`corpus_seed_pubmed_20260806.jsonl`, third-party PubMed author names, Italian affiliations,
hospitals and emails. The gate is now correct and **red**, dominated by published bibliographic
metadata. **Not adjudicated here** — it is a new Operator question, not a granted one.

🔴 **And the decision's scope does not cover the whole exposure.** Of 29 lowercase occurrences
that are *not* path segments: **12** are the Italian common word (correctly untouched), **1** is a
third-party published author, and **16 are the Operator's identity in non-path form** —
machine hostnames (`AIR-DI-<NAME>`, `MacBook-Air-di-<name>`, `MacBook Air di <name>`) in
`launch/KERNEL_SPEC.md` and `framework/eval/learned_gates_registry.md`, and **the OS username in
captured `lsof` output** in `framework/protocols/actor_identity_feasibility.md`. Verified by
fixture: all five such forms return **zero findings** under both the old and the new rules.
**Same identifier, same publishable surface, outside the scope granted — requires a further
Operator decision.**

---

## 16 · REQUIRES SCIENTIST ADJUDICATION — not Mirror

1. **Whether `85.5 %` or `72 %` is the number that should travel** with the figure-evidence claim.
   I measured both; deciding which one a scientific consumer needs is a reading judgement.
2. **Whether the 2 `ppi_preflight.json` entries belong in `source_artifacts`.** Removing them
   changes 448 → 446 and every derived rate.
3. **Whether the 33 surface-less locators** are legacy debt or a distinct evidence class.
4. **The `K-1` Fig. 7b/7d question.** A and B agree the parenthetical is compound and a blind
   substitution breaks the correct half. That is a reading of the source, not a process fact.
5. **All lithium / GSK-3β / WWOX mechanism conclusions.** Untouched here by design.

---

## 17 · FOR LATER PLAN / ORCHESTRATOR / GOVERNANCE RECONCILIATION

**Recorded durably here; not routed, because Plan and Orchestrator have work in progress.**

- **Orchestrator:** the base-divergence problem (§ 1.1), the evidence-population problem (§ 1.2),
  the namespace problem (§ 2), the unsynchronised stop (§ 12), the single-register problem (§ 4.1).
- **Plan:** remediation candidates 3, 4, 7, 8, 10.
- **Governance:** candidate 5 (ref-bound measurements) is a convention with a lint, and it is the
  only proposed repair for the missing failure class.
- **Note for whoever reconciles this:** `framework/protocols/prompt_batch_commit.md`,
  `framework/scripts/pathograph.py` and `disease-models/wwox/analysis/data/pathograph_export.jsonl`
  are modified on `legend-operating-convention-v1` and absent from `main`. Recorded as a scope
  fact only. I did not review that work.

---

## 18 · UNRESOLVED

1. **Why does the shared checkout hold 428 of 448 declared artifacts and not 448?** 20 declared
   artifacts are absent from every tree I measured. Not investigated.
2. **Is the lowercase path form a genuine privacy concern in this repository?** Operator's call.
3. **Should `.jsonl` scanning be retroactive?** The 706-line PubMed seed carries third-party author
   names, affiliations and ORCIDs — public bibliographic data, but the gate's `PRIVATE_NAME` set
   contains a token that collides with a published author's given name.
4. **Was the pilot's `55`-PDF measurement taken on the shared checkout deliberately or by
   accident?** No artifact says. Both A and C reported `55`; only the shared checkout holds 55.
5. **What "round" means.** Undefined; § 5.5.
6. **Whether B's early stop was a decision or an interruption.** Not determinable from the refs.

---

## VERDICT

**`REFINED`.**

The package's measurements are, where I could check them, unusually good: the 22-of-128 receipt
class is exact including its refusal to over-count; B's propagation count reproduces to the file
at the blob B named; the corpus census reproduces to the decimal; the figure/no-text plateau
survives a change of PDF engine. **The taxonomy is sound in four of five classes.** These are not
findings that needed a better reader.

They are refined on four points: **class E was refuted by its own authors before the run ended**
and should not survive into any contract; **a fifth class is missing** — the ref-dependent
measurement, which produced four instances in one day and is invisible from inside a run;
**A's denominator was right and C's was not**, settled by a third engine neither seat used; and
**the number four rounds hardened is a proxy standing 13 points below the quantity the gate
actually tests.**

---

## FINAL HOSTILE QUESTION

> **What could still be wrong after two Scientists repeatedly checked each other, and which part
> of LEGEND should prevent that class next time?**

**What is still wrong is everything that is true of the *tree* rather than of the *text*.**

Two excellent readers, alternating every four minutes for an afternoon, converged on a corpus
rate that is genuinely robust — and neither could see that they were measuring a directory
neither of them owned, that one of them was standing 201 commits in the past, that the object
under adjudication had never been committed anywhere, or that the number they were hardening
was a proxy for a predicate neither had implemented. **Every one of those is invisible to
reading, and every one of them was closed here by a command.**

And the answer is not more reviewers. **Six of my six new findings were closed by a command and
none by a reading**, which is the producers' own recommendation against a new reviewer actor —
**confirmed, but for a reason they did not give.** It is not that the failures live in tools
rather than in reading quality. It is that **a reviewer inherits the surface of the thing it
reviews.** A fourth Scientist would have inherited the same worktree, the same `files/`, the same
parser default, and would have agreed — the way `independent_privacy_scan.py`, written
specifically to be a second opinion, independently reproduced `public_release_gate.py`'s exact
blind spot by choosing the same eleven file extensions.

**Which part of LEGEND should prevent it: the part that decides what a measurement is allowed to
omit.** A number published without its ref, its population and its predicate is not a measurement;
it is a number that happened to be true somewhere. Three of this review's five new findings, and
four of the pilot's own, are that one omission. It is the cheapest repair on the list and the only
one that addresses a class rather than an instance.

---

*Non-canonical. Nothing here is medical advice. No canonical, governance, role-contract, state or
tool file was modified in producing it. Gate mutation testing was performed exclusively on scratch
copies outside the repository root. Every figure in this document is bound to the refs in § 1.1
and decays when they move.*
