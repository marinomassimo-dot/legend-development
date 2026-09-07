---
artifact: LEGEND scientific evaluation — EVALUATOR FROZEN SET, BLIND ROUND DISPATCH, SCORING MODEL
id: EVALUATOR_FROZEN_SET_AND_BLIND_ROUND_DESIGN_SCIC_v1
class: evaluator-side record for a controlled benchmark in the vocabulary of
  `framework/protocols/controlled_benchmark_ab.md` (CONTROLLED_BENCHMARK_AB) and
  `framework/eval/benchmarks/BENCH-AB-001/`. It freezes an input set, dispatches one case,
  and specifies a comparison. It is NOT a benchmark manifest and authorizes no run.
continues: BENCHMARK_ELIGIBILITY_AND_BLIND_DESIGN_SCIC_v1 (48 cases)
  ← HARD_CASE_MINING_BENCHMARK_CANDIDATES_SCIC_v1
actor: scientist-c (NOT ACTIVATED — operator-directed analytical pilot)
worktree: lettore-c · branch lettore-c · HEAD 5b1d6c2
date: 2026-08-26
audience: EVALUATOR ONLY
scope: EVALUATION DESIGN. No governance, role-contract, schema or architecture change is
  performed or proposed.
status: NON-CANONICAL. Mutates no canonical file, manifest, receipt or ledger.
canonical_mutation: NONE
---

# The frozen set, the one case that can actually be run blind, and how to compare two readings of it

> 🔴 **This file is evaluator material.** It states expected answers by implication throughout.
> It must never enter a participant surface. The participant surface is
> [`framework/eval/benchmarks/blind_rounds/participant/`](../../framework/eval/benchmarks/blind_rounds/participant/INDEX.md),
> it contains six fields per case and nothing else, and a command decides that.

> **Nothing here is medical advice.**

---

## 0 · The one line to carry out of this document

The prior artifact concluded that the benchmark's hardest constraint is that *this laboratory
writes down what it learns in exactly the places a blind reader is required to look.* That was
right and it was measured against the wrong population — **the twelve discipline files, and not
the readers themselves.**

Swept properly, the count moves a long way:

```
prior artifact, discipline-file sweep only        CLEAN_BLIND 31 of 48
this session, discipline files + both readers     CLEAN_BLIND  7 of 48
                                                  DISPATCHABLE 14 of 48
                                                  CLEAN + DISPATCHABLE + RUNNABLE TODAY: 1
```

🔴 **One case in forty-eight can be run blind today.** Not because the cases are weak — because the
two readers have written the answers into their own branches. **Sixteen cases are verified spent
that way, and nine of those carry a single quotable line that states the case's answer**, in the
reader's own hand.

**And that is a conditional finding, which is the more useful half.** A reader's branch contaminates
the *reader's checkout*, not an allowlisted surface built outside every checkout.
`controlled_benchmark_ab.md` §2.1 already forbids reading inside a checkout. What this session adds
is the denominator that makes the rule bite: **run a blind case in `lettore` or `lettore-b` and at
least 16 of 48 are spent before the reading starts — 27 if the 11 unread screen positives hold.**

---

## 1 · Phase 1 — the frozen set

### 1.1 · Why the prior classification could not simply be re-affirmed

The task says *do not change a classification without a new measurement*. Three new measurements
force changes, and each is reproducible.

#### 🔴 M-1 · The sweep measured a population that is not the participant surface

The prior §4.3 swept a **hand-written 12-file "mandatory set"**. The surface a participant
actually holds is enumerated, by command, in `framework/eval/benchmarks/BENCH-AB-001/surface_spec.json`:
`common_files` (11) plus the per-actor `MODE_A.md` / `MODE_B.md` — **13 inherited files**
(`ASSIGNMENT.md` is authored fresh per round and cannot carry an inherited leak).

| | n | |
|---|---:|---|
| True inherited participant population | **13** | `common_files` + `MODE_A` + `MODE_B` |
| Prior hand-set | 12 | |
| **Overlap** | **8** | **62 % of the surface** |
| In the surface, never swept | **5** | `SURFACE_CLAUDE.md` · `BENCHMARK_INSTRUCTIONS.md` · `OUTPUT_SCHEMA.md` · `MODE_A.md` · `MODE_B.md` |
| Swept, not in the surface | 4 | `CLAUDE.md` (root — the surface uses `SURFACE_CLAUDE.md`, different bytes) · `LEGEND_CORE.md` · `designed_for_growth.md` · `locator_audit.py` |

The pattern set was short too: the prior sweep used **21 PMIDs**; the 48 case blocks name **27
distinct PMIDs**. Both gaps run in the direction that flatters the result.

*Reproduction:* `learning/scientist/evalset/emit_frozen_set.py` records the population it used;
the sweep itself is the script's `LEAK` table, each row carrying the file and line that produced it.

**What the corrected sweep found.** 20 raw hits over 13 files × (27 PMIDs + 50 content patterns),
positive control `22193544` → 1 hit in `fulltext_read_receipt.md` as it must. The two irremediable
leaks the prior artifact found are confirmed and unchanged. **The five never-swept files added
one new class of hit and no new answer disclosure:** `BENCHMARK_INSTRUCTIONS.md` and
`OUTPUT_SCHEMA.md` name PMID 42397075 twelve times between them, because they are BENCH-AB-001's
own paper-specific instructions. That disqualifies `HC-E3`, `HC-H1` and `HC-I4` — all three touch
PMID 42397075 — from any round that reuses those files.

🔴 **A hit is not a leak, and the prior artifact's binary is why `HC-B2` and `HC-G1` were mislabelled
in both directions.** Every hit here is graded by what it discloses:

| Grade | Meaning | Example |
|---|---|---|
| `L3` | states the answer or its decisive discriminating fact | `fulltext_read_receipt.md` L145–147 on `HC-B1` |
| `L2` | states a necessary premise, or hands the discriminating concept | `epistemic_discipline.md` L39 hands K48/K63 to `HC-F1` |
| `L1` | names the paper **and** says something evaluative about it | `deepdive_manifest.py` L578: 18487609's text layer is unusable |
| `L0` | names the paper only as an example about tooling | L463: 26675548's `D2` is a real timepoint label |

Two hits are recorded as **false positives** and not carried: `Aqeilan` ×3 in
`BENCHMARK_INSTRUCTIONS.md` occurs only inside the filename `PMID42397075_Aqeilan2026.pdf` — it
names one paper and says nothing about any other Aqeilan paper, so it does not touch `HC-B2`,
`HC-D1`, `HC-D2` or `HC-G1`.

#### 🔴 M-2 · The contamination model had no term for the readers themselves

`fulltext_read_receipts.jsonl` carries **no actor field** — 128 rows, keys
`analysis_at · coverage · event_at · event_id · evidence_basis · … · study_id · workflow`. So
*"has A or B read this paper"* is **not answerable from the canonical receipt surface at all**, and
the task's *"if verificabile"* resolves to: not by that route.

What is verifiable is what each reader branch has **written** since it diverged from `main`
(merge-base `788c357d`): at the pinned tips of §1.2, `lettore` +24 commits / **8 995** added lines,
`lettore-b` +19 / **8 950**. *(The sweep quoted below was first run at 7 443 / 8 022; both branches
advanced mid-session. The screen's verdict classes are byte-identical at both readings — same 35 / 3
/ 5 / 5 membership — so nothing in this section moved, and the pinned tips are what it is bound to.)*
Sweeping those added lines for the 27 PMIDs and the per-case content terms:

| Screen verdict | n | |
|---|---:|---|
| `READER_ADJUDICATED` | **35** | adjudicative-language screen |
| `READER_WORKED` / `READER_MENTIONED` | 8 | |
| `READER_CLEAN` | 5 | `HC-I1` `HC-I7` `HC-I9` `HC-J1` `HC-X3` |

🔴 **Then the screen positives were read, and a third of them did not survive.** 34 of the 48 case
rows were read line by line, covering 24 of the 35 screen positives:

| | n | |
|---|---:|---|
| confirmed `READER_ADJUDICATED` by reading | **16** | `A1 A2 B6 C1 C2 C4 D1 D3 D4 E1 F1 G1 G4 H1 I8 J3` |
| **downgraded** by reading | **8** | `A3 A4 B1 B2 B4 B5 D2 J2` — `HC-B4` went all the way to `CLEAN` |
| **screen false-positive rate** | **33 %** | 8 of 24 |
| upgraded by reading | **0** | the screen never missed one among those read |
| screen positives still unread | 11 | `B3 E3 F2 F3 G2 I10 I3 I6 X1 X4 X5` |

The screen's errors run in one direction — it over-reports and never under-reports on the rows
checked — so **the 14 rows still marked `SCREEN_ONLY` are an upper bound, and reading them is the
only cheap way the dispatchable set can grow.**

Three verified verbatim, in the readers' own hands:

> `lettore`, on `HC-D1`: *"PMID 19936220 (Ludes-Meyers 2009) | **epileptogenesis not measured in
> any form**; the only brain measurement is organ weight"* and *"a **Table 2 whose `Epilepsy` row
> is empty for both mouse models**"* — **the prior artifact's single strongest gold candidate,
> written out complete.**

> `lettore`, on `HC-C1`: *"Figure 6: four bar charts, error bars on three, **not one significance
> marker or p-value anywhere in the figure**"* — the prior artifact's "Moderate 3".

> `lettore-b`, on `HC-B6`: *"**Calpain.** Rejected as an established WWOX turnover route (DIS-008):
> no proteolysis was ever …"*

Also verified spent: `HC-G1` (*"Panel 5A … it is **up, not down**: RUNX2 at 1.50 in femur"*),
`HC-C2` (*"Figure 3's caption inverts the asterisk convention (`* p = 0.0036, ** p = 0.027`)"*),
`HC-C4` (*"**one affected fetus against one control fetus** — Methods say one, Results say three"*),
`HC-D4`, `HC-F1`, `HC-G4`.

Every row in the frozen set carries its provenance — `VERIFIED` (34) or `SCREEN_ONLY` (14) — because
a screen that has not been read is a suspicion, and treating it as a measurement is the error this
corpus makes most often. The 33 % false-positive rate above is why the distinction is a field and
not a footnote.

#### 🔴 M-3 · Three cases rest on a surface fact that is false, or on a surface that is absent

| Case | Prior | Now | The measurement |
|---|---|---|---|
| `HC-I5` | `UNVERIFIABLE_SURFACE` — *"Figure S4 … behind a PMC proof-of-work challenge"*, marked ◻ INHERITED | **`CASE_PREMISE_FALSIFIED`** | The supplement **is held**: `files/fulltext/PMID26675548_assets/oncotarget-07-4344-s001.pdf`, 1 527 965 bytes, valid PDF-1.4, **7 pages**, page 4 headed *"Supplementary Figure S4: Impaired checkpoint activation in MCF7 cells"*. E-1 does not fail. Its gold — *"a declared, addressed gap"* — is void because the object is not missing |
| `HC-B4` | `GOLD_ELIGIBLE`, *"XML held; caption and printed statistic disagree, both quotable"* | **`UNVERIFIABLE_SURFACE`** | The case turns on what the **panel** prints against what the caption says. PMID 34634460 is held as PMC XML **only** — no PDF, no assets directory, no page-adjudication crop. Its six figure hrefs (`gr1…gr6.jpg`) are not on disk, and the string `5D` occurs **0** times in the XML |
| `HC-A3` | `GOLD_ELIGIBLE` | **`UNVERIFIABLE_SURFACE`** | Same cause, different paper: PMID 32581702 is held as PMC XML only, and the case's minimum evidence is *"the panel + its marker legend"* |

And one correction in the favourable direction: **`HC-A4` is text-decidable.** Its four decisive
magnitudes — `23.3` `24.7` `57.3` `27.5` — each occur in the held XML, so it needs no figure
surface and its `GOLD_ELIGIBLE` stands. `HC-C2` likewise: both asterisk definitions are printed
inside `<fig>` captions in the XML.

🔴 **`HC-F4` needs two acquisitions, not one.** The prior artifact named *"read Mukai 2002 (PMID
12065620)"* as the cheapest route to fill its vacant slot. Measured: **neither** terminal surface
is held — PMID 12065620 is absent **and** the citing review PMC3139124 is absent. Only Saeki
(`PMID21212533_Saeki2011.pdf`) is on disk.

🔴 **A hazard that produced M-3 and will produce it again.** `files/` is gitignored. This worktree
holds **3** entries under `files/fulltext/`; the main checkout holds **174**. A surface census run
from a worktree reports every surface absent, and reports it without error. Every held/not-held
statement in this document was taken against `<REPO_ROOT>/files/fulltext`
and the frozen set records that root in a field, because the census is a property of a working
directory and not of the repository.

### 1.2 · The frozen set

```
FROZEN_SET_ID   EVALSET-BLIND-R1-2026-08-26
ANCHOR          82c9f651558936334e41cb8d959ebd62c024f4d3   branch lettore-c
                — the commit at which both hashed inputs became tracked objects
SHA256          15e2bf632fb2ce83504636b079396117115950544ca3de821dc24e532ba68e87
RECIPE          python3 learning/scientist/evalset/emit_frozen_set.py --emit \
                  --corpus-root <REPO_ROOT>/files/fulltext \
                  --pin-head      82c9f651558936334e41cb8d959ebd62c024f4d3 \
                  --pin-lettore   c536fc7f5b718b06d589821889bff4293314c881 \
                  --pin-lettore-b 111b96324f6bdcbd545459c6a1013db04ab832de \
                | shasum -a 256
```

**The recipe is published because a hash without one is an attestation, not a measurement.** The
digest above was reproduced by running that exact command twice after the file was written.

🔴 **Three pins, and the first two attempts at this freeze had none of them — a "frozen" set whose
digest moved under its own author.** The first emission read the live tips of two branches that are
being written by other sessions; the second still read the live `HEAD`, so committing the inputs
changed the digest of the set that hashes them. Both were caught by re-running the published recipe
and finding a different number, which is the only reason a recipe is worth publishing.

**The `reader_prior_work` axis describes two named commits and nothing later.** Between the start
of this session's sweep and its end, `lettore` went from 7 443 to 8 995 added lines and `lettore-b`
from 8 022 to 8 950 — roughly a thousand new lines each, under me, while I was classifying against
them:

| branch | tip | ahead of `main` | committed |
|---|---|---:|---|
| `lettore` | `c536fc7f` | 24 | 2026-08-26T10:43:01+02:00 |
| `lettore-b` | `111b9632` | 19 | 2026-08-26T10:39:04+02:00 |

Both Round 1 and Round 3 selections were **re-verified at these tips after the movement was
noticed**, and both hold: `PMID 26675548` still has zero mentions on `lettore-b` and three on
`lettore`, none touching ATR or the title; the taxonomy terms still return zero on both branches.

🔴 **The axis has a shelf life and the frozen set says so in a field.** A case clean at these tips
can be spent by the next commit. **Re-run before any dispatch.**

The set is emitted from `learning/scientist/evalset/emit_frozen_set.py`, which carries the
classification as an auditable table rather than as prose, and keeps four axes apart:

| Axis | What it answers |
|---|---|
| `eligibility_now` | can this case carry a gold standard at all |
| `surface_leak_grade` | what the 13-file inherited surface discloses, `L0`…`L3` |
| `reader_prior_work` | what each reader has already written, per branch, with provenance `VERIFIED` or `SCREEN_ONLY` |
| `surfaces_held` | which files exist, against a named corpus root |

The **single label** the task asks for is derived from those by a stated precedence, printed in
the artifact so it can be disputed:

```
by_construction > L3 | reader_ADJUDICATED > L2 | reader_SCREENED > L1 | reader_WORKED
                > eligibility(UNRESOLVABLE | STRESS_ONLY) > CLEAN_BLIND
```

| Label | n |
|---|---:|
| `CLEAN_BLIND` | **7** |
| `PARTIALLY_CONTAMINATED` | **18** |
| `FULLY_CONTAMINATED` | **23** |
| `UNRESOLVABLE` | 0 *(every case in that eligibility class is contaminated, so the label is outranked)* |
| `STRESS_ONLY` | 0 *(same)* |
| **total** | **48** |

🔴 **The five requested labels cannot say "this case cannot be run at all", and left alone they lie.**
`HC-B4` comes out `CLEAN_BLIND` — clean, and unrunnable, because its figure is not held. That is
exactly the confusion the rubric warns against: rewarding *"cannot be determined"* where the honest
answer is *"go and get the file"*. So the frozen set carries `dispatchable` and `blocker` as
separate fields rather than overloading the label:

```
DISPATCHABLE              14   A4 B3 B5 C3 D2 E2 E3 F2 F3 G2 G3 I3 I9 J2
  of which CLEAN_BLIND     2   E2  I9
  of which runnable today  1   E2        (I9 needs frozen network-response fixtures that
                                          do not exist)
```

---

## 2 · Phase 2 — the Round 1 participant handoff

### 2.1 · The case, and why it is the one

**`BLIND-R1-001` ← `HC-E2` / `GOLD-06` · PMID 26675548 · Abu-Odeh 2016, *Oncotarget*.**

| Selection criterion | How this case meets it, measured |
|---|---|
| `CLEAN_BLIND` | ✅ single label `CLEAN_BLIND`; and the **lowest surface-leak grade of any case in the set**: `L0`. The only hit over the 13 files is `deepdive_manifest.py` L463 — *"Bare `\bD2\b` … flags `two days (D2), D5 and D7` in PMID 26675548, which is a real timepoint label."* Tooling. No science |
| high evaluation value | The title asserts a kinase. Measured on the held XML: `ATR` ×30 and `ATM` ×52 in the body, `CHK1` ×22. The paper talks about ATR constantly; whether it ever **measures** it is the question. Axes `CAUSALITY` · `ABSTRACT_VS_FULLTEXT` · `NEGATIVE_EVIDENCE` |
| corpus bounded | One paper. Everything needed is in the packet; nothing cited, nothing citing |
| no required surface that reveals adjudication | The reader renders its own pages from the PDF. No manifest, no dossier, no ledger is needed to answer it (§6) |
| no recent deep analysis by A or B | `lettore-b`: **zero** mentions of PMID 26675548 anywhere in 8 950 added lines. `lettore`: three, all on the K274R blot and the caption census, **none on ATR or the title**. Re-verified at the pinned tips |

### 2.2 · The residual, stated rather than hidden

🔴 `lettore` has written: *"`PMID 26675548` | The text says IR induced ubiquitination of wild-type
WWOX **'but not the mutated form WWOX-K274R (line 5 vs. 6)'**. **The blot shows a clear band.**
Reduced, not abolished."*

That is a **different claim in the same paper** (`HC-D4`, which is thereby spent). It is not this
case's answer. But it is an attention marker — a reader holding it approaches this paper knowing
its text overstates a negative — and **it is asymmetric: A holds it, B does not.**

**The residual does not travel to a correctly built surface**, and that is the point of §2.1 of
the protocol: `lettore`'s branch content is not in an allowlisted directory outside every
checkout. What survives is session memory, and §2.2 records that this runtime keeps auto-memory
per working directory, so a session opened in a fresh surface path starts with an empty scope —
*"a favourable accident of the deployment, not a guarantee."* Recorded here as a **known,
one-sided contamination of the variable**, beside the two `controlled_benchmark_ab.md` §0 already
declares, and not softened.

### 2.3 · Scope change against `GOLD-06`, and why

The prior handoff bounded `GOLD-06` to *"PMID 26675548 **MAIN TEXT ONLY**. The supplementary
material is OUT OF BOUNDS"*, because `GOLD-11` / `HC-I5` lived in the supplement.

🔴 **That boundary is now a defect.** `HC-I5`'s premise is falsified (M-3): the supplement is held,
and its pages 3–4 are *"Impaired checkpoint activation in KHOS cells"* and *"…in MCF7 cells"* —
**checkpoint data, directly bearing on whether the paper supports its title.** Excluding it would
withhold evidence relevant to the question and could mark a correct reader wrong, which is exactly
the defect that blocks `HC-B1`.

**`BLIND-R1-001` therefore runs against the whole published record: main text + supplementary
deposit.** The consequence is declared: `HC-I5` cannot be run separately on this paper afterwards,
and it is void anyway.

### 2.4 · The packet

| Include | |
|---|---|
| `PMID26675548_AbuOdeh2016.pdf` | `sha256 2416bec74c23df51…` |
| `PMID26675548_AbuOdeh2016_PMC.xml` | `sha256 8bf84348ebe881da…` |
| `PMID26675548_assets/oncotarget-07-4344-s001.pdf` | 1 527 965 B, 7 pp — the published supplementary figures + Table S1 |
| `PMID26675548_assets/oncotarget-07-4344-s002.pptx` | the second published deposit |

| Exclude, and why | |
|---|---|
| `supp_page01…07_144dpi.png` (7 files) | prior-reader renders — `controlled_benchmark_ab.md` §2.3: *their selection encodes a prior reader's attention*. Each reader renders its own |
| `table_s1_render.png` | same |

### 2.5 · Where the handoff lives, and how the separation is enforced

The handoff is [`BLIND-R1-001.md`](../../framework/eval/benchmarks/blind_rounds/participant/BLIND-R1-001.md).
It carries the six permitted fields and nothing else. It names no case ID from this set, no axis,
no failure mode, no contamination status and no gold.

🔴 **`CONTAMINATION_STATUS` is not a participant field and is not present.** The prior artifact
already flagged that telling a participant `PARTIALLY_CONTAMINATED` is itself a disclosure. This
handoff goes further and drops the field entirely: every constraint it would have implied is
expressed as `DO_NOT_OPEN_SURFACE_X`, never as a reason.

**The separation is a check, not a promise.**
`framework/eval/benchmarks/blind_rounds/check_participant_surface.py` runs three classes —
`SCHEMA` (exactly the six fields, each once, no seventh), `LANGUAGE` (an enumerated
expectation-bearing vocabulary), `CONTAINMENT` (no link leaves the directory) — behind a positive
control that must fail in all three or the run is declared void. Current state:

```
POSITIVE CONTROL fired in all three classes (3 findings) — checker is live
PARTICIPANT FILES: 4  (3 handoffs + index)
VERDICT: PASS — 4 files, 0 findings
```

It found five real matches on first run, all of them my own words, and the fix was to reword the
handoffs rather than to relax the checker.

**The durable surface is a separate branch.** Participant files are published on
`bench-blind-participant`, branched from `main` and containing **only** this directory. The
evaluator set stays on `lettore-c`. A and B fetch one ref; no evaluator byte can travel with it,
and the property is checkable with `git diff --name-only main..bench-blind-participant`.

---

## 3 · Phase 3 — Rounds 2 and 3

### 3.1 · 🔴 `MULTI_PAPER_REASONING` has no runnable blind case left

Every multi-paper case in the set is disqualified, and each by a measurement:

| Case | Papers | Why it cannot run |
|---|---|---|
| `HC-D1` | 30290271 → 19936220 → 19500159 | `lettore` states the answer verbatim (M-2) |
| `HC-F1` | 23370280 + 24550385 + 26675548 | `lettore` carries the typed claim *"DNA damage promotes ITCH-dependent K63 ubiquitination of WWOX at Lys274 · `DATO`"* and a `DEGRADATION_DIRECTION_GATE`; and 26675548 is consumed by Round 1 |
| `HC-F2` | 36779245 + 42128308 | `deepdive_manifest.py` L98–99 hands **both** the text finding *and* the Figure 4A ordering. The prior artifact graded this `L2`/PARTIAL; read in full it leaves only the verdict word |
| `HC-G4` | 18487609 + 34634460 | `lettore`: *"three heterozygote-sensitive readouts (slice bursting incidence, sIPSC amplitude, resting …)"* |
| `HC-D4` | 24550385 + 26675548 | `lettore` states the blot answer verbatim; and 26675548 is consumed |
| `HC-E3` · `HC-I4` · `HC-H1` | involve 42397075 | that PMID is named 12× in the participant instruction files themselves (M-1) |
| `HC-I8` | four papers | both readers report per-paper panel-count errors on its own papers |

**I am not filling the slot by decree.** The prior artifact declined to fill its vacant
unresolvability slot for the same reason and was right to.

### 3.2 · Round 2 — `BLIND-R2-001` ← `HC-F4`, blocked on two acquisitions

[`BLIND-R2-001.md`](../../framework/eval/benchmarks/blind_rounds/participant/BLIND-R2-001.md) is
written and marked `NOT_RELEASED`. It is the only multi-paper case with a clean surface leak
(`--`) and near-clean readers (`lettore` 0 · `lettore-b` 1 bare mention).

```
BLOCKER      two surfaces absent from files/fulltext/, verified by listing:
             · PMID 12065620  (Mukai 2002) — the unread terminal reference
             · PMC3139124     (the review carrying the clause)
             held:  PMID21212533_Saeki2011.pdf
ROUTE        the standard acquisition cascade; PMC3139124 is an open-access PMC id and
             12065620 needs the cascade's later tiers. Neither is behind a control that
             may be circumvented.
```

**The alternative, so the operator can overrule me with the same information I had.** `HC-F2` is
`dispatchable` today. I rejected it because `deepdive_manifest.py` — a file both readers must run,
whose bytes cannot be changed without breaking parity — states its premise and its figure ordering.
Running it would measure whether a reader can restate a comment it was handed.

### 3.3 · Round 3 — `BLIND-R3-001` ← `HC-B5` · PMID 42128308, visual/caption

[`BLIND-R3-001.md`](../../framework/eval/benchmarks/blind_rounds/participant/BLIND-R3-001.md),
`NOT_RELEASED`.

| | |
|---|---|
| Surface leak | `--` — zero hits over the 13 files |
| Reader exposure | **zero** lines on either branch name the paper together with any taxonomy term (`neurodevelopmental fragile`, `fragile-site gene`, `CFS gene`, `categor…fragile`) |
| Residual | 🟡 `lettore` has worked this paper — 11 references, citing `manifest PMID42128308` entries 8, 9 and 24. Those entries concern the Olig2-Cre readout (`HC-D3`) and the Abudiab preprint (`HC-H1`), **not** the taxonomy. Declared, one-sided, and again absent from a correctly built surface |
| Surface held | `PMID42128308_Aqeilan2026.pdf` + `_fitz.txt`. The four `fig*_300ppi.jpeg` in `_assets/` are prior-reader renders and are **excluded**; the reader renders its own from the PDF |
| Axes | `VISUAL_PDF_ADJUDICATION` · `SOURCE_IDENTITY` |

🔴 **Unresolvability recognition has no candidate at all, and that is a regression this session
caused.** The prior artifact filled its one `UNRESOLVABILITY` slot with `HC-I5`, whose premise is
now falsified — and which, by the prior artifact's **own** §1 rule, was the wrong filler anyway: a
supplement you do not hold is a **debt** (`SURFACE_NOT_HELD`), not a **finding**
(`RECORD_DOES_NOT_DECIDE`), and §1 says scoring them together rewards a system for saying *"cannot
be determined"* when the honest answer is *"go and get the file"*. Of the four genuine
`UNRESOLVABLE` cases, `HC-A2` and `HC-C4` are spent on a reader branch, `HC-B1` is irremediably
leaked and carries a falsified negative control, and `HC-F4` needs two acquisitions. **The
category is empty and the route out of it is §3.2's two acquisitions.**

---

## 4 · Phase 4 — the scoring model

### 4.1 · The ten dimensions are not ten of the same thing

Four of the ten measure **agreement between the two readers**. Six measure **a reading against its
source**. `controlled_benchmark_ab.md` §8.5 already forbids treating the first kind as quality —
*"two readers agreeing on an overshoot is two overshoots"* — so they are reported in a separate
block, and no number crosses between the blocks.

**No composite, no weighting, no overall score** (§8.5). Ten tables. Every count is an enumerated
set or carries the command that produced it.

**`GOLD_REQUIRED`** is marked per dimension, because Round 1 has no gold and must still be
scorable. Six of the ten are computable without one.

### 4.2 · Block D — descriptive. Never a quality judgment.

#### `D-1 OBSERVATION_OVERLAP` · unit: an evidence unit · gold: **no**

- **WHAT_COUNTS** — a unit is *touched* by a reader when ≥1 of that reader's verbatim locators
  anchors inside it. Report three named sets: touched by both · by A only · by B only — **and a
  fourth, touched by neither**, computed against the structurally enumerated population
  (§8.1 `population/evidence_units.json`, fixed before either reading).
- **WHAT_DOES_NOT_COUNT** — agreement about what a unit *shows* (that is `D-2`/`D-3`); the number
  of locators (forty locators inside one panel touch one unit); a unit named in prose without a
  locator.
- **PARTIAL_CREDIT** — none. This is a set report, not a score.
- **ASYMMETRIC_ERROR** — n/a.
- 🔴 A high overlap over a small union is worse than a low overlap over a large one. **The ratio
  is never reported without the union size and the touched-by-neither set.**

#### `D-2 CLAIM_OVERLAP` · unit: a claim candidate · gold: **no**

- **WHAT_COUNTS** — two claims align when their locator sets intersect in ≥1 evidence unit.
  Alignment is **structural, by unit** (§8.3) — never by an evaluator judging that two sentences
  mean the same thing. Report aligned pairs · A-only · B-only.
- **WHAT_DOES_NOT_COUNT** — paraphrase similarity; claim volume (§8.4 secondary, never quality);
  any alignment an evaluator asserts from meaning.
- **PARTIAL_CREDIT** — a pair aligned on unit but differing in `Type` or `Direction` is its own
  row, `PARTIAL_ALIGNMENT`, counted as neither agreement nor disagreement.
- **ASYMMETRIC_ERROR** — n/a.

#### `D-3 EPISTEMIC_VERDICT_AGREEMENT` · unit: an aligned pair · gold: **no** for agreement, **yes** for correctness

- **WHAT_COUNTS** — the identical epistemic type token on both sides of an aligned pair.
- **WHAT_DOES_NOT_COUNT** — 🔴 **correctness.** Agreement is not a second measurement of the same
  quantity; two readers can be wrong together, and on a shared discipline file they are *likely*
  to be. Also excluded: type agreement where the propositions differ (that is a `D-2` partial).
- **PARTIAL_CREDIT** — one step apart on the ordered scale vs opposite ends, **reported and never
  scored**: the ordering is a convention of this repository, not a property of evidence.
- **ASYMMETRIC_ERROR** — n/a here; direction is `Q-3`/`Q-4`.

#### `D-4 LOCATOR_AGREEMENT` · unit: a (proposition, snippet, anchor) triple · gold: **no**

- **WHAT_COUNTS** — same anchor **and** overlapping source character range. Mechanical.
- **WHAT_DOES_NOT_COUNT** — citing the same figure *number* when one reader read the caption and
  the other read the panel: different surfaces, reported as such. Citing the same paper.
- **PARTIAL_CREDIT** — same unit, non-overlapping snippet = `SAME_UNIT_DIFFERENT_EVIDENCE`, which
  is the most interesting cell in the table and must not be folded into either side.
- **ASYMMETRIC_ERROR** — n/a.
- 🔴 On a figure-dependent case each reader hashes **its own** render. Agreement is compared on
  *what the render is of* — source file, page, region — **never on the render digest.** Two
  correct readers will never share one.

### 4.3 · Block Q — quality. Scored against the source, not against the other reader.

#### `Q-1 NEGATIVE_EVIDENCE_RECALL` · unit: a negative in the source · gold: **yes**

- **WHAT_COUNTS** — the negative is carried **and** typed as either *measured-and-negative* or
  *not-measured*. Both halves are required.
- **WHAT_DOES_NOT_COUNT** — the absence of a positive claim (silence is not recall); a generic
  limitations paragraph naming no specific negative; the authors' own limitations section restated
  without a locator into the evidence.
- **PARTIAL_CREDIT** — full (carried, typed, located) · partial (carried, untyped) · none.
- 🔴 **ASYMMETRIC_ERROR — severe.** Recording *not-measured* as *measured-and-negative* manufactures
  evidence of absence; the reverse merely leaves a question open. **Separate columns. They never
  net against each other.**

#### `Q-2 CONTRADICTION_DETECTION` · unit: an internal contradiction · gold: **yes**

- **WHAT_COUNTS** — both sides named with a locator each, **plus** a statement of which surface
  governs or that the record does not settle which.
- **WHAT_DOES_NOT_COUNT** — *"the paper is inconsistent"* without both locators; resolving by
  preferring whichever surface was read first; a contradiction manufactured between two statements
  that are differently scoped.
- **PARTIAL_CREDIT** — both located, no governance statement = partial; one side = none.
- 🔴 **ASYMMETRIC_ERROR.** A missed contradiction leaves an error in place; a **fabricated** one
  creates one and buys a downstream investigation. Fabricated contradictions get their own column.

#### `Q-3 OVERCLAIM` · unit: a carried proposition · gold: **no** — the blind audit decides it

- **WHAT_COUNTS** — the proposition asserts more than its cited evidence bears: wider population,
  stronger modality, a causal arrow over a measured association, a transfer across
  species/preparation/stage the source does not license. The verdict is the blind locator audit's
  `OVERSHOOT`, not an evaluator's opinion.
- **WHAT_DOES_NOT_COUNT** — a proposition explicitly typed as hypothesis or inference and carrying
  its own limit; a proposition stated and withdrawn in the same output; **the authors' overclaim
  quoted as the authors', and marked as theirs.**
- **PARTIAL_CREDIT** — binned by the scope of the excess: modality only · population or preparation
  · causal direction. **Three bins reported; no sum.**
- 🔴 **ASYMMETRIC_ERROR, against `Q-4`.** An overclaim propagates and gets built on; an underclaim
  leaves a gap someone can still fill. **They are never averaged into an "accuracy".**
- 🔴 This is the dimension that works without gold, and it is why Round 1 is scorable.

#### `Q-4 UNDERCLAIM` · unit: a proposition in the source · gold: **partial**

- **WHAT_COUNTS** — the audit's `UNDERSHOOT`; and *material omission* — an evidence unit inside the
  case boundary that bears on the question and carries no locator from this reader.
- **WHAT_DOES_NOT_COUNT** — not carrying material outside the question (the `STOP_CONDITION` bounds
  the reading; exceeding it is not credit); brevity; **declining to type something the source
  genuinely leaves open — that is `Q-5`, and scoring it here would punish the correct answer.**
- **PARTIAL_CREDIT** — carried-but-weakened = partial; absent = full, inside the boundary only.
- **ASYMMETRIC_ERROR** — the mirror of `Q-3`, and reported beside it, never merged.

#### `Q-5 UNRESOLVABILITY_RECOGNITION` · unit: an undecided question · gold: **yes**

🔴 **This dimension has two sub-scores and they must never share a column:**

| | The record | The correct answer |
|---|---|---|
| `RECORD_DOES_NOT_DECIDE` | complete, and still does not settle it — **a finding** | declare it, and name what would settle it in principle |
| `SURFACE_NOT_HELD` | would settle it; we do not have it — **a debt** | name the exact missing object, and the route |

- **WHAT_COUNTS** — the right one of the two **and** the object named.
- **WHAT_DOES_NOT_COUNT** — *"insufficient evidence"* naming no object (neither); a refusal that
  does not distinguish the two; declaring unresolvability where the record does decide — that is a
  `Q-4` underclaim and is scored there.
- **PARTIAL_CREDIT** — right category / no object = partial. Object named / wrong category =
  partial, **with the direction of the miscategorisation recorded.**
- 🔴 **ASYMMETRIC_ERROR.** A debt misreported as a finding **retires a retrievable question** — the
  worse direction, and the one `HC-I5` demonstrates: an inherited *"behind a challenge"* took a
  held 7-page PDF out of the benchmark for months. The reverse merely schedules a retrieval that
  comes back empty.

#### `Q-6 CORPUS_DISCIPLINE` · unit: a locator, and a boundary event · gold: **no**, fully mechanical

- **WHAT_COUNTS** — every locator resolves inside `ALLOWED_SURFACES` or to a render the reader
  produced and hashed; every render carries dpi + source + digest; **every boundary crossing is
  self-reported**, with file and time.
- **WHAT_DOES_NOT_COUNT** — not crossing because there was nothing outside worth opening (no credit
  for an untested rule); a self-report naming no file and no time.
- **PARTIAL_CREDIT** — a self-reported crossing is **not** a failure of this dimension; it is the
  dimension working. The failure is an unreported crossing found by
  `benchmark_input_surface.py locators`.
- 🔴 **ASYMMETRIC_ERROR — the sharpest in the set.** A self-reported crossing costs one entry; an
  unreported one **voids the reading**, because a reading that looks clean and is not is worse than
  one that is visibly dirty. The handoffs say so to the readers in advance, so this is a rule and
  not a trap.

### 4.4 · Secondary, and the standing prohibition

Time, tokens, output volume: recorded per §8.4, in their own table, **never combined with
anything, never a tie-break, never a quality proxy.** A reading is not better for being faster,
shorter or cheaper.

🔴 **This model is not applied to any output.** No frozen reading from A or B exists at the time of
writing; nothing of theirs has been read, and this section was written before either had run.

---

## 5 · Phase 5 — gold readiness

**Nothing is `READY`, including the cases whose facts I re-derived myself.** Re-deriving a fact is
not adjudicating a verdict, and the actor who re-derived it is the wrong actor to adjudicate it.
The prior artifact's `NEEDS_INDEPENDENT_ADJUDICATION: YES` stands on all 35.

| State | n | Cases |
|---|---:|---|
| `CASE_PREMISE_FALSIFIED` | **1** | `HC-I5` — the supplement is held; its gold was *"a declared gap"* and there is no gap |
| `NEEDS_VISUAL_ADJUDICATION` **and blocked on retrieval** | **5** | `HC-A3` `HC-B3` `HC-B4` `HC-X4` (34634460 / 32581702 — **no figure surface held at all**) · `HC-I5` |
| `CONTAMINATED_BY_REPO` — irremediable | **3** | `HC-B1` `HC-A1` `HC-I1` (`L3` in a file the participant must hold). 🔴 **Not promoted, per instruction.** `HC-B1` additionally carries a falsified negative control |
| `CONTAMINATED_BY_REPO` — by a reader, not by the repo | **16 verified · 14 screen-only** | 9 of the 16 carry the answer in one quotable line; see the frozen set's `reader_prior_work` |
| `NEEDS_PRIMARY_REDERIVATION` | **25** | every `GOLD_ELIGIBLE`/`GOLD_WITH_MULTIPLE`/`UNRESOLVABLE` case still marked `NO` by the prior artifact's §3 |
| `NEEDS_SECOND_ADJUDICATOR` | **35** | all of them, unconditionally |
| `READY` | **0** | — |

### 5.1 · The five that can become gold without changing protocol

Ordered by the length of the named path, not by attractiveness. **Each names one act.**

| # | Case | The single next act | Why it is short |
|---|---|---|---|
| 1 | **`HC-E2`** | Round 1 runs; two frozen readings + a blind locator audit produce the adjudication | Facts re-derivable from a held packet; `L0` leak; **already dispatched** |
| 2 | **`HC-A4`** | Re-derive the four magnitudes from the held XML — no figure needed (§1.1 M-3) and no acquisition | `23.3 / 24.7 / 57.3 / 27.5` each present once in the XML; the ranking is arithmetic |
| 3 | **`HC-C2`** | Read the two asterisk definitions out of the `<fig>` captions in the held XML | Both are printed in the XML; verified this session. Spent as a *blind* case, fine as a *gold* case |
| 4 | **`HC-G3`** | Re-derive from the held PMID 34268881 PDF + XML; the confound is named in a section heading | Surface complete; no reader has stated the stage confound |
| 5 | **`HC-D2`** | Enumerate the assay inventory of PMID 18487609 and show it empty of the named test | Both PDF and PMC HTML held; absence of a named test is a command |

🔴 **Every one of the five is `NEEDS_SECOND_ADJUDICATOR` after its act.** The act makes the facts
re-derived; it does not make the label gold.

---

## 6 · Phase 6 — figure provenance as an evaluation-infrastructure gap

### 6.1 · Re-derived this session, at `HEAD`

| Measurement | Value |
|---|---|
| Deep-dive manifests | **64** |
| Carrying `source_artifacts` | 60 |
| Carrying `verbatim_locators.entries` | 63 |
| **Carrying both — provenance and adjudication in one file** | **60** |
| Distinct **figure**-artifact digests | **333**, across **58** papers |
| …also present in the receipt ledger (the non-adjudicating surface) | **3** |
| **Papers whose figure provenance exists nowhere outside an adjudicating file** | **57 of 58** |

The prior artifact's headline numbers reproduce exactly. *(Its adjudicative-language screen
returned 38; mine returns 45. The two are not the same measurement — mine runs over the serialized
entries list, including field names — so this is a second screen, not a correction of the first.
Both are screens; **the 57-of-58 result does not depend on either.**)*

### 6.2 · The reframing that makes the requirement small

**The participant does not need figure provenance and must not have it.**
`controlled_benchmark_ab.md` §2.3 already excludes prior renders from the surface, because *their
selection encodes a prior reader's attention* — which pages, which panels, which dpi. Each reader
renders what it needs and lists its own renders with digests.

So the four questions answer as one:

- *Can the participant receive digest/path without seeing adjudication?* — **Wrong question.** The
  participant should receive neither.
- *Who actually needs it?* — the **surface builder**, who must enumerate what artifacts exist for
  a paper in order to build a packet, and who today has exactly one tracked file that answers it:
  the deep-dive manifest, which also states the verdicts.
- *Automatically generated participant view?* — **no participant view is required.**

That shrinks the gap from a corpus-wide provenance architecture to a **projection for one role**.

### 6.3 · `MINIMUM_SEPARATION_REQUIREMENT` — four clauses, no architecture

> **MSR-1 · A provenance record must be derivable without reading an adjudication.** Any mechanism
> that emits, per paper, the tuple set `{path, kind, sha256, bytes}` from the existing manifests
> satisfies it. It is a **projection, not a second store**: a second store drifts, and drift in a
> provenance record is worse than co-location.

> **MSR-2 · The projection is generated, never authored.** One command; output a function of its
> input manifests at a named commit. Anything hand-maintained acquires an author's attention —
> the exact thing being removed.

> **MSR-3 · The projection carries no free text, by whitelist.** The leak is not the digests, it is
> the sentences beside them. Permitted fields: `path` · `kind` · `sha256` · `bytes`, plus `page` ·
> `dpi` · `clip_rect` **only where they already exist as structured fields**. A field not on the
> list is dropped even if it looks harmless. A blacklist of words would be the `HC-B1` mistake at
> the schema level.

> **MSR-4 · What reproduces a figure is the recipe; the digest only verifies.** Minimum information
> to *reproduce*: source-PDF digest · page index · clip rectangle in a declared coordinate system ·
> dpi or zoom matrix · renderer name and version. This repository already knows it — the `.gitignore`
> note on `page_adjudications` says exactly that, and `regenerate_adjudications.py` implements it.
> 🔴 **A provenance index carrying digests without recipes lets you check a render you already have
> and does not let you make one.** Both fields are required and they are different fields.

**What the requirement does not ask for.** No new manifest schema, no migration, no split of an
existing file, no governance change, no new store. And if it is never built, **the fallback is
already sufficient for the blind rounds**: the dispatcher — not the participant — opens the
manifest, and §2.2's *one writer per surface, transferred once* contains the contamination inside
the evaluator role. This is a requirement statement, not a build order.

---

## 7 · Phase 7 — the estimand, before the sample size

### 7.1 · 🔴 The frame cannot be enumerated by the command the prior design assumed

The prior `SAMPLING_FRAME` was *"the paper registry at a named commit — every paper the laboratory
has ever admitted"*, with *"frame size must be enumerated and published before any draw."*
Enumerated this session, `disease-models/wwox/registries/paper_registry_current.md`, 379 013 bytes:

| Entry class | n | What it means |
|---|---:|---|
| `## PAPER nnn` | **70** | integrated or baseline-linked — papers that were **read** |
| `## CORPUS Pnnn` | **188** | admitted to the corpus |
| `## CORPUS-STUB-nnn` | **168** | stubs, all 168 carrying a PMID identifier |
| **total entries** | **426** | |

*(Commands: `grep -cE '^## PAPER [0-9]+'` · `grep -cE '^## CORPUS +P[0-9]+'` ·
`grep -cE '^## CORPUS-STUB-[0-9]+'`. A naive `grep -oE '\b[0-9]{7,8}\b' | sort -u | wc -l` returns
**412** — an upper bound on identifiers, not an enumeration of entries, and not the frame.)*

🔴 **My first count of this table was 427, and the repository's own instrument caught it.**
`growth_anchors.py check` reports `papers=70 · corpus=356`; heading-anchored counting reproduces
`356` exactly as `188 + 168`, while a looser `^## CORPUS` grep had swept in an appendix heading and
a stray. The instrument's own whole-file regex finds **357** distinct corpus ids — one more than it
has headings — and the extra is **`CORPUS P264`**, referenced in the file with no entry of its own.
A frame whose size depends on which of three commands you run is not yet a frame.

**The registry is three populations, not one.** Drawing from `PAPER` samples papers that were read
hard; drawing from `CORPUS-STUB` samples papers that were mostly never opened. The same words
*"the paper registry"* name a 70-unit frame and a 426-unit frame that would produce different
rates from identical readings. **Fixing the frame class is a design act and it has not been done.**

### 7.2 · The five candidate estimands

| | `ERROR_PER_PAPER` | `ERROR_PER_CLAIM` | `ERROR_PER_EXTRACTION` | `ERROR_PER_ADJUDICATION` | `ERROR_PER_RUN` |
|---|---|---|---|---|---|
| **UNIT** | one paper's reading | one carried claim candidate | one (proposition, snippet, anchor) triple | one adjudicative statement about what the record shows | one reading session end-to-end |
| **DENOMINATOR** | papers drawn | claims produced | locator entries produced | adjudications produced | runs executed |
| **WHAT COUNTS AS ERROR** | ≥1 defect of a named class anywhere in that reading | blind audit returns `OVERSHOOT` · `UNDERSHOOT` · `NOT_IN_SOURCE` | the audit's per-triple verdict: quote does not support, or source says more/less | a second independent adjudicator disagrees and the disagreement resolves against the first | ≥1 defect that **reached a canonical file** |
| **SAMPLING FRAME** | the registry class, fixed per §7.1 | claims within drawn papers | locators within drawn papers | adjudications within drawn papers | the run log |
| **ADVANTAGE** | the **only** unit whose denominator is fixed by the frame rather than by the reader | the unit the disease model actually consumes, and the one an error propagates through | most mechanical; a tool exists (`locator_audit.py`) and a population exists — **1 002 entries across 64 manifests** | measures the act that actually decides the model | matches cost and catches process failures no per-claim unit sees |
| **BIAS** | 🔴 saturating — 1 defect and 20 score alike; and **monotone in reading depth, so it rewards shallow reading** | 🔴 **the reader chooses the denominator**: carrying fewer claims lowers the rate without improving anything. Clusters within paper | 🔴 same, more severe; and it measures quotation fidelity, the **cheapest** thing to get right — 1 % locator error is compatible with 40 % claim error | 🔴 costs a second adjudicator per unit, and measures **inter-adjudicator disagreement**, a lower bound: both can be wrong together | 🔴 coarsest; a run is not a fixed quantity of work, so denominators are not comparable; confounds reading quality with pipeline quality |

### 7.3 · Recommendation, and 🔴 it is normative, not empirical

**Primary `ERROR_PER_CLAIM`; frame-anchored secondary `ERROR_PER_PAPER`. Report both, never
combine them.**

- `ERROR_PER_CLAIM` because the claim is what the disease model consumes and what a defect
  propagates through — it is the unit the number is *for*.
- `ERROR_PER_PAPER` because it is the **only** candidate whose denominator is set by the sampling
  frame instead of by the reader, and so the only one that cannot be improved by carrying less.
  It is the honesty anchor for the first.

🔴 **No measurement selects between these.** The choice follows from a decision about what the
number is used for — a normative act, and this document is not the place it should be taken. It is
also **not convertible**: the units nest (`run ⊃ adjudication ⊃ claim ⊃ extraction`) while `paper`
cuts across them, so a rate on one unit does not translate to another, and quoting one as the
other is the error this whole line of work exists to catch.

### 7.4 · Only now, the sample size

Measured input: **1 002 verbatim locator entries across 64 manifests → mean 15.7 per paper**
(median 14, min 0, max 32; one manifest carries zero). That is the cluster size.

**Independent units** — 95 % Wilson, `p` **assumed** 0.30 (an assumption, not a measurement):

| half-width | n at p=0.30 | n at p=0.50 |
|---|---:|---:|
| ±0.05 | 320 | 381 |
| **±0.10** | **78** | 93 |
| ±0.15 | 33 | 39 |
| ±0.20 | 18 | 21 |

*(The prior artifact quoted ≈81 and ≈36 for the first two; the small differences are the interval
formulation, not the substance.)*

**Clustered units** — `DEFF = 1 + (m−1)ρ`, `m = 15.7`. 🔴 **`ρ` is not measured**, and measuring it
needs a pilot; the row that applies is unknown, so the sensitivity is shown instead of a number:

| ρ | DEFF | claims needed | **papers needed** |
|---:|---:|---:|---:|
| 0.05 | 1.73 | 136 | **9** |
| 0.10 | 2.47 | 193 | **13** |
| 0.20 | 3.94 | 308 | **20** |
| 0.35 | 6.14 | 480 | **31** |
| 0.50 | 8.35 | 652 | **42** |

🔴 **The two columns of "papers" are not comparable.** 78 papers for `ERROR_PER_PAPER` and 20 papers
for `ERROR_PER_CLAIM` at ρ=0.2 are precisions on **different quantities**. Reading one as the other
would be the same class of error as §7.3's non-convertibility, at the point where it is most
tempting.

`SAMPLING_BIAS_STATUS`: **FORMALIZED, NOT CORRECTED, AND NOW BLOCKED ONE STEP EARLIER THAN THE
PRIOR ARTIFACT THOUGHT.** It recorded the blocker as *fixing the unit of observation*. Measured:
**the frame is blocked too** — three entry classes, no published rule for which is drawn.

---

## 8 · Phase 8 — benchmark leakage checks

Five channels. Three are commands today; two are not, and are named as gaps rather than described
as covered.

| # | Channel | Check | State |
|---|---|---|---|
| **L-1** | Evaluator material reaching a participant file | `check_participant_surface.py` — SCHEMA · LANGUAGE · CONTAINMENT, behind a positive control that must fail | ✅ **runs, PASS, 4 files, 0 findings** |
| **L-2** | Prior LEGEND output inside the built surface | `benchmark_input_surface.py verify` — `FORBIDDEN_PRIOR_OUTPUT_PATHS` absent, `CONTENT_SCAN` = 0, `[UNCHECKED]` census per actor | ✅ exists in the protocol; **not run here — no surface is built** |
| **L-3** | The inherited discipline surface disclosing a case | the sweep in §1.1 M-1, graded `L0…L3`, 13 files × 77 patterns, positive control fires | ✅ **run this session** |
| **L-4** | A reader's own prior work disclosing a case | the sweep in §1.1 M-2 over both branches' added lines since merge-base | 🟡 **run; 24 of 35 positives read, 33 % of those downgraded, 11 still unread.** Reading them is owed |
| **L-5** | Locators citing outside the surface after the fact | `benchmark_input_surface.py locators` — per entry, `BENCH_INVALID` recorded never dropped | ✅ exists; applies after a reading exists |

🔴 **Two leakage risks that no check above covers, stated because they are the ones that will bite:**

1. **Model training data.** Uncontrollable. `controlled_benchmark_ab.md` §2.1 already declares it
   and routes it to `DEFAULT_FROM_TEXTBOOK`. Every case in this set is a published paper.
2. **Session memory carried into a fresh surface.** §2.2 records that this runtime keeps auto-memory
   per working directory and calls a fresh empty scope *"a favourable accident of the deployment,
   not a guarantee."* 🔴 **After §1.1 M-2 that accident is now load-bearing**: it is the only thing
   standing between `lettore`'s branch and 20 verified-spent cases. **The surface builder must check
   the memory scope is absent before handover and record the check** — §2.2 already requires it, and
   this session's measurement is the reason it must not be skipped.

🔴 **And one about this document.** Committing it puts its 27 PMIDs and its quoted verdicts into the
tracked corpus. Any future sweep over the repository must exclude `learning/` — `-- . ':!learning/'` —
or it will measure a corpus that now contains its own audit. The frozen-set sweep is immune by
construction: its population is 13 named files and this is not one of them.

---

## 9 · What this document does not claim

- **It authorizes no run.** `controlled_benchmark_ab.md` §1 lists seven preconditions and §9
  determines `BLIND FIRST PASS — BLOCKED BY CANONICALIZATION` (and independently by P-2…P-4:
  actors `NOT_REGISTERED`, capabilities `UNVERIFIED`, L2 suspended by the C-9 hold). **None of that
  is satisfied or lifted here.** This is dispatch preparation.
- **It creates no gold label.** Zero cases are `READY`.
- **It proposes no schema, field, rule or governance change.** §6.3 is a requirement statement about
  a projection that does not exist; it asks for no migration and no new store.
- **It has read nothing of A's or B's outputs on any blind case**, because none exists. What it read
  is their committed branch content, which is the contamination measurement itself.
- **Its `READER_ADJUDICATED` count of 35 is a screen, and the screen over-reports.** 34 rows are
  read line by line and labelled `VERIFIED` — 16 confirmed, 8 downgraded; 14 rows are labelled
  `SCREEN_ONLY` and are an upper bound.
- **Its held/not-held statements are properties of one working directory**, named in the frozen set.
- **Nothing here is medical advice.**

---

## 10 · Summary

```
EVALUATOR_SET_FROZEN                YES
  FROZEN_SET_ID                     EVALSET-BLIND-R1-2026-08-26
  ANCHOR                            82c9f651558936334e41cb8d959ebd62c024f4d3
  SHA256                            15e2bf632fb2ce83504636b079396117115950544ca3de821dc24e532ba68e87
  RECIPE                            emit_frozen_set.py --emit --corpus-root <root>
                                      --pin-head 82c9f651 --pin-lettore c536fc7f
                                      --pin-lettore-b 111b9632 | shasum -a 256
  READER AXIS PINNED TO             lettore c536fc7f (24 ahead) · lettore-b 111b9632 (19 ahead)
                                    Both branches moved ~1000 lines mid-session. Re-run before
                                    dispatch: a case clean at these tips can be spent by the
                                    next commit.
  CLEAN_BLIND 7 · PARTIALLY 18 · FULLY 23        (48)
  DISPATCHABLE 14 · CLEAN+DISPATCHABLE 2 · RUNNABLE TODAY 1

ROUND1_PARTICIPANT_HANDOFF_READY    YES — six fields, checker PASS, on its own branch
ROUND1_CASE_ID                      BLIND-R1-001   (evaluator-side: HC-E2 / GOLD-06,
                                                    PMID 26675548, whole published record)

ROUND2_HANDOFF_READY                WRITTEN, NOT RELEASED — blocked on two acquisitions
                                    (PMID 12065620 · PMC3139124). MULTI_PAPER_REASONING has
                                    no runnable blind case; every candidate disqualified by a
                                    named measurement.
ROUND3_HANDOFF_READY                WRITTEN, NOT RELEASED — BLIND-R3-001 (HC-B5, PMID 42128308),
                                    visual/caption; one declared one-sided residual.

SCORING_MODEL_READY                 YES — 10 dimensions in two blocks: 4 descriptive (agreement,
                                    never quality) + 6 quality (against the source). No composite.
                                    6 of 10 computable without gold, which is what makes Round 1
                                    scorable. 5 carry an explicit ASYMMETRIC_ERROR.

GOLD_READY_CASE_COUNT               0 READY.  5 reachable by one named act each:
                                    HC-E2 · HC-A4 · HC-C2 · HC-G3 · HC-D2
                                    3 not promoted per instruction: HC-B1 · HC-A1 · HC-I1

FIGURE_PROVENANCE_SEPARATION_REQUIREMENT
                                    MSR-1 provenance derivable without an adjudication
                                    MSR-2 generated, never authored
                                    MSR-3 no free text — whitelist of fields, not blacklist of words
                                    MSR-4 the recipe reproduces; the digest only verifies
                                    Re-derived: 333 figure digests / 58 papers / 57 of 58 have
                                    provenance nowhere outside an adjudicating file.
                                    NOT a build order — the dispatcher/participant split already
                                    contains it for the blind rounds.

UNBIASED_ESTIMAND_STATUS            RECOMMENDED, AND THE RECOMMENDATION IS NORMATIVE.
                                    primary ERROR_PER_CLAIM · anchor ERROR_PER_PAPER · never combined.
                                    BLOCKED EARLIER THAN THOUGHT: the frame itself is three
                                    populations (70 PAPER · 188 CORPUS · 168 STUB = 426) with no
                                    published rule for which is drawn.
                                    n: independent ±0.10 at p=0.30 -> 78. Clustered m=15.7 measured,
                                    rho NOT measured -> 9 to 42 papers across rho 0.05-0.50.

BENCHMARK_LEAKAGE_RISKS             L-1 participant surface        ✅ checked, PASS
                                    L-2 built surface              ✅ tool exists, not run (none built)
                                    L-3 discipline files           ✅ swept, 13 files x 77 patterns
                                    L-4 reader prior work          🟡 swept; 24/35 read, 33% downgraded,
                                                                      11 screen positives still unread
                                    L-5 post-hoc locators          ✅ tool exists, applies after a reading
                                    uncovered: training data; session memory carried into a surface
                                    — and the second is now load-bearing.

NEXT_EVALUATION_PRIORITIES          1  read the 14 SCREEN_ONLY rows; the screen over-reports by
                                       33% and has never under-reported, so this is the only
                                       cheap way the dispatchable set can grow
                                    2  acquire PMID 12065620 and PMC3139124 — it unblocks Round 2
                                       AND restores the empty UNRESOLVABILITY category
                                    3  retrieve figure surfaces for PMID 34634460 and 32581702 —
                                       six cases are surface-incomplete for want of gr1..gr6.jpg
                                    4  publish the frame rule (PAPER / CORPUS / STUB); the sampling
                                       design cannot start without it
                                    5  build the surface for BLIND-R1-001 — by an actor who is not
                                       a reader — and verify the memory scope is absent at handover
```

🔴 **The line to carry.** The prior artifact found that this laboratory writes its conclusions into
the files a blind reader must hold. The larger problem is one level up: **it writes them into the
readers.** Of six cases the prior artifact ranked highest, three were already unrunnable for that
reason; measured against the readers' own branches, **sixteen of forty-eight are verified spent and
eleven more are still unread.** The rule
that saves the benchmark is one the protocol already has — *build the surface outside every
checkout* — and what was missing was any number showing what it costs to break it.
