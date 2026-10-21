# Session self-evaluation — `scientist-c`, `REPURP-P3-RESCUEREF-C-20261021`

Task: bind the `WOREE_RESCUE_REFERENCE` card from the evidence this repository already holds for
PMID 42422765, and adjudicate the `CLAIM 011` dose flag. Disease-level, de-identified, not medical
advice.

## Part 1 — Executable

| Check | Command | Result |
|---|---|---|
| Manifest, strict | `deepdive_manifest.py --workspace .claude/worktrees/lettore-c --artifact-workspace <root> --disease wwox --pmid 42422765 --verify-artifacts --require-current-schema` | **PASS**, 0 gaps, 48 locator entries, 24 artefacts |
| Receipt chain | `fulltext_receipts.py verify` | **OK** — 683 chained receipts, tail anchored |
| Staged receipt | `staged_receipt_check.py --check-doi` | **OK**, 0 errors |
| Staged receipt, dry append | `fulltext_receipts.py record --dry-run` | **DRY RUN OK** — nothing written |
| LINT | `legend_lint.py .claude/worktrees/lettore-c` | **WARN**, **0 BLOCK** |
| Session self-eval | `session_self_eval.py --workspace … --disease wwox` | **PASS** — every complete read landed, every declared output resolves |

Ratchets reported and not fixed here, because they are repository-wide history and not this
reading's: `acquisition_recipe` absent on 96 manifests, `retraction_check.dependencies` absent on
59. This reading **added** a recipe to each of its five new derived artefacts and a stated
`no_recipe` reason to the one it could not show a route for.

## Part 2 — Judgement

**Sources and depth.** 1 · No — and the receipt says so. This was a **targeted panel
re-inspection**, not a re-read: the coverage map carries `results: read`, `figures: read`,
`supplementary: captions_only` and `not_read` on abstract, introduction, methods, discussion,
limitations and references, which keeps the event at `partial_fulltext_read`. The Methods
subsection on ECoG acquisition *was* read verbatim this session and the map still says
`not_read` for methods: understating, as the brief requires. Figures were read **as images at
native resolution** — and that is the substance of the task, not a formality: the five surfaces
opened were 300 dpi rasters embedded in the publisher PDF and 400 dpi page renders, against the
726 px CDN JPEGs every prior figure attestation on this paper rests on. 2 · Not applicable: one
paper, assigned. 3 · 🔴 **The finding a keyword search would never return is that Figure 7's
quantitative panels are *vector* in the publisher PDF.** Its only embedded raster is 759 × 515
and carries the ECoG traces alone, so `pdfimages` — the method that gave the best surface for
Figures 1, 3 and 6 — would have returned the one part of Figure 7 with no numbers on it. Aspect
ratio caught it: seven of eight figures matched a PDF image to within 0.002, Figure 7 was off by
0.18.

**The group behind the paper.** 4–6 · Carried from the record, not re-derived: Aqeilan
laboratory, the primary group for this gene, with a declared commercial interest (manifest entry
22) and a methodological upgrade over its own 2021 predecessor (entry 20). The weighting that
matters here is 6's: an **experimental lab with a stake in the result** makes the *observations*
strong and the *interpretation* the thing to check — which is exactly what happened. Every one of
the five narrowings below is a disagreement with the authors' **wording**, never with their data.

**Field density.** 7 · Not re-measured; the manifest's `field_density` slot is unchanged.

**Epistemics.** 8 · Every door closed here carries a trigger: the oligodendrocyte limit carries
`REVIVAL_TRIGGER` (a construct with demonstrated WWOX protein in white matter, then tested); the
dose threshold carries the pre-existing intermediate-dose trigger, re-affirmed and now requiring
quantified MBP in the same animals. 🔴 **And one door was deliberately *not* closed**: "the low
dose does nothing" is refused, because the caption prints LD vs `KO+RI` p < 0.0001. A narrowing
that over-shoots in the other direction is still a false negative. 9 · This is the whole session:
four of the five narrowings separate what the paper **shows** from what it **says** — Figure 6E
has no treated arm while the text claims dose-dependent myelination rescue; S7F/S7H have no
untreated-KO arm while the text claims a significant dose-responsive reduction; Figure 7E has no
low-dose arm while the figure title says *dose-dependent*; Figure 3C prints no significance
marker at all. 10 · Yes, and it decided the method. Every number quoted here was read from a
**rendered panel or page**, never from a text layer — the record already holds two measured
corruptions of this paper's own doses (the PMC text route deletes the exponent, the JATS route
squashes it), so an extraction fault was the default hypothesis and was excluded by construction
rather than by argument.

**Compounding.** 11 · 🔴 **Honest answer: no.** The receipt is **staged**, not recorded, because
a parallel wave is the condition and the Orchestrator appends in event-ID order. That is the
protocol, not a shortfall — but it is a staging file, and it is named as one. 12 · No multi-hop
this session; the manifest's `multihop` block is untouched. 13 · Yes —
`registry_records.py get --pmid 42422765`, whole records, and the two large registries were never
loaded or grepped. 14 · `CLAIM 011`, and it is said where the claim lives: the proposed Title and
flag block are written verbatim in
`CC-20261021-SCIENTIST-C-CLAIM011-DOSE-ADJUDICATION-01`, not paraphrased. 15 · Yes: the Figure 4
conflict is written into the card (§3.3) and the candidate (§5) as the **next measurement**, with
its surfaces named and their reachability stated, not as "carried forward".

**Capability.** 16 · See the micro-upgrade below. 17 · Nothing broke. 18 · 🔴 **A check caught me
twice and both times the check was right and specific**: `deepdive_manifest.py` refused four new
locators for an unpointed `panel_qualifies_text`/`text_contradicted_by_panel`, then refused them
again for a missing `*_needle`. The second refusal is the better one — it says a list position
can be reordered and a relation must therefore carry a fragment of the sentence it bears on. The
repair was not to satisfy it but to **add the two body quotations that were missing**: the Figure
3B caption sentence and the S7 gliosis sentence now exist as locators, which is a strictly better
state than pointing the new panels at approximate neighbours. 19 · No ranking was used.

**Batch scorecard.** 20 · *Main message*: neuron-targeted WWOX restoration at the high dose gives
survival indistinguishable from the wild-type control to 300 days (Fig 3B) and abolishes
spike-wave discharges at ~P14 (Fig 7E). *Original contribution*: the promoter and WPRE
comparisons that make "neuronal, controlled expression" a design principle rather than a result
(Figs 1, 2). *Hidden gold*: 🔴 **the wild-type control arm of Figure 3B ends at 71–72 %, below
the treated arm's 76–77 %** — which is what `p = 0.78` actually means and which no record in this
repository stated; and 🔴 **body weight is not dose-graded at all** (LD 15.3 g vs HD 15.6 g at
P30), which inverts the direction of the error the existing flag warns about. 21 · Parity applied
in the only axis available: a single primary paper, read as new data, with its figure panels
given priority over its running text. 22 · `experimental lab` / `primary disease group`, with
observation and interpretation weighted separately throughout. 23 · Used: `paper_packet.py`
(packet + claim), `figure_legend_pairs.py`, `registry_records.py`, `deepdive_manifest.py`,
`staged_receipt_check.py`, and the native-resolution rule of
`scientist_reading_modes.md` § 3.2. **Declined with a reason:** `legend-locator-audit` — none of
its four mandatory triggers fires (`CLAIM 011` is `flagged for review`, not `consolidated
baseline`; change class MINOR; no research direction closed; no persisted locator contradicted,
corrected or replaced) — but it is **recommended** anyway and the Orchestrator routes it, because
producer is not verifier. `legend-discovery-method`: declined, optional, the question was a
measurement and not a search. 24 · Card → `research/drug_repurposing/`; candidate →
`research/commit_candidates/`; six locators + two body quotations + six artefacts →
`deepdive_manifests/PMID42422765.json`; receipt → `research/receipt_staging/scientist-c/`;
renders → the **shared checkout's** `files/figures/PMID42422765_r2/native_renders_20261021/`, not
the worktree. 25 · Yes, mechanically, from `FTR-20261021-42422765-01`. 26 · Three frictions, all
caught before any overclaim: the two manifest refusals above; and
`fulltext_receipts.py record --dry-run` refusing `analysis_at` later than `event_at` because the
writer stamps `event_at` at append time and my declared time sat in the future of the clock. 27 ·
The micro-upgrade below is disease-agnostic.

### Weakest answer, and the micro-upgrade it owes

The weakest answer is **11**, and it is structural rather than mine. The second weakest is **3**,
and that one is mine to repair: *the figure surface a reading uses was chosen by habit, and the
habit was nearly wrong.* Every prior figure attestation on this paper — sixteen of them — rests
on 726 px PMC CDN JPEGs, and the publisher PDF carrying the same figures at 300 dpi has been on
disk, undeclared, since 2026-10-19. Nobody chose the worse surface; nobody compared them.

**Micro-upgrade, proportional and disease-agnostic — and it is a practice, not a file.** Before a
figure is read, run `pdfimages -list` on any publisher PDF held for the paper and compare each
embedded image's aspect ratio against the CDN rasters. It costs one command and it answers two
questions no existing check asks: *is there a better surface than the one I am about to open*,
and *is this figure vector* — the second being the one that would have silently cost this session
every number on Figure 7. Both answers are now written into the card's §0 and into the manifest's
artefact notes, where the next reader of this paper meets them. **The reusable gap, registered
for the capability scout rather than invented into a tool here:** `paper_packet.py` lists
artefacts present on disk and *undeclared* — it listed the publisher PDF and all seven r2 figures
— but it does not rank the available surfaces for a figure read, so "a better surface exists" is
information the packet holds and does not say.

## Part 3 — Attribution census

```
ATTRIBUTION_CENSUS
incidents: 6
machine: 3   blind_auditor: 0   peer: 0   self: 3
severity_high: 3   of which self: 3
undetected_known: 0
```

**Counting.** The two manifest refusals are one incident (one rejection class, two instances);
the `analysis_at`/`event_at` refusal is one; the figure-surface choice is one; the Figure 7
vector case is one; and the sixth is the one that is least comfortable to write down.
`severity_high` counts the three that would have **reached the record**: a Figure 3B measurement
taken from the 726 px CDN raster; a Figure 7 read from its extracted raster, which carries no
panel numbers and could have been written up as "panel unreadable"; and 🔴 **a cell count in
`CURRENT_STATE` that was estimated and asserted as measured — "120 of 120 cells, 112 BOUND" —
which was committed before it was counted.** The true figures are 160 cells, 0 `NOT_YET_BOUND`,
0 `TRANSCRIBED_FROM_ROADMAP`, 3 `UNKNOWN`, counted mechanically off the committed file. That one
did reach the record and was corrected forward in the same task, and it is the cleanest local
instance of *an assumption asserted with the confidence of a measurement, in a place too small to
look at twice* — a completeness figure about my own work, in a field nobody re-derives. All three
were caught by **self**, by re-deriving rather than by any gate, because no gate in this
repository asks whether a better surface exists or whether a self-reported count was counted.
`undetected_known: 0` is this diagnosis's structural blind spot and is left visible as such.

## Part 4 — pointer

`DEFAULTS_TAKEN` and `STOP_LOG` are in the task contract JSON,
`ledger/tasks/scientist-c/REPURP-P3-RESCUEREF-C-20261021.json`, not here and not only in a
transcript.
