# MIRROR ex-post review — BATCH_20261002_001

`REVIEW_ID` MIRROR-20261003-BATCH20261002001 · `OBJECT` `BATCH_20261002_001` (WM_v7.7 → **WM_v7.8**),
landed on `main` at **`ba5682f`** (merge of `task/batch-20261002-intake-2`, tip `0c9b3a1`; pre-batch
base `9fddfb1`) · `LEVEL` ex-post sampled review of an ordinary MINOR batch (Annex G.1
`MIRROR_SAMPLED`) · `REVIEWER` ACTOR_ID `mirror` · `AUTHOR` ACTOR_ID `scientist` (Scientist E,
batch integrator; readings by Scientists A/B/C) · `ADJUDICATOR` the author, as a new task.

> **Mirror is not a gate (`DEC-20260905-AGILE-HARNESS-MODE`, `LEGEND_CORE` §21e).** Every finding
> below is a **new task for the author**, never a hold on a landed change. `CONFIRMED` means "no
> defect found given the available evidence bundle", never "true". READ-ONLY toward every registry:
> this review writes one file and three candidate files and edits no canonical record.
> **Not medical advice.**

**Method.** Blind first: for every new or changed statement about a paper's content the
(proposition | verbatim quote | anchor) triple was re-extracted from the registries' own text and
checked against the **source artefact** in `files/fulltext/` (hardlink-copied into the review
worktree), before the batch's own account — candidates, dossiers, wave notes — was opened. Six
papers were sampled at the full-text level (29390993, 40191585, 24949445, 37501399, 42395553,
34204789), plus the held artefact of `PAPER 025` (30853297) for `DIS-025` and 37781246 and 17679088
for two single statements. Artefact identity was re-derived: the `source_fingerprint` of all six
sampled receipts equals the sha256 of the file on disk.

---

## STEELMAN (first, and it is strong)

This batch's weight is in what it **refuses** to conclude, and the refusals are the hard kind —
each one takes a sentence a source actually prints and declines it on measurement.

- **`DIS-022` is the model case.** Szymańska 2014 prints *«affects two dose-sensitive genes: WWOX …
  and MAF»*. The reading did not argue with the sentence; it lifted the authors' own NCBI36 interval
  through a **fingerprinted** Ensembl REST liftover (response sha256 `d18cc68b…`, transcript
  `ENST00000566780`, lookup sha256 `62e1eb90…`) and found the interval holds **only exon 9 and the
  3′ part of intron 8**. I reproduced the printed coordinates (`arr 16q23.1
  (77,445,915–78,190,209) dup`, NCBI36 declared twice in the source) and the arithmetic. A
  dose-gain datum the abstract offers for free is gone, correctly.
- **`DIS-025` is reproduced exactly, including its positive control.** On the held text layer of
  PMID 30853297: `c.49` **0**, `49G` **0**, `Glu17` **0**, `E17K` **0**, control `517-2` **11**. A
  supplementary citation that would have made `p.E17K` a named population's founder allele does not
  survive its own reference, and the bound ("a text-layer zero is bounded by the layer") is stated.
- **The genotype caution held where it previously broke.** `CLAIM 032`'s new paragraph was
  **appended** after the existing `DO_NOT_INFER` and `DO_NOT_CITE` paragraphs, not inserted into
  them: the three pre-existing lines are **byte-identical** across the batch (sha256 `374a9319…`
  over the block at `9fddfb1` and at `ba5682f`). The `B11` class of defect — a byte-conserving
  insertion that splits a prohibition from its grounds — **did not recur**, and the new paragraph
  keeps missense and null apart, routing the 172 `p.Glu17Lys` carriers under the record's own
  `DO_NOT_INFER` rather than counting them as carriers of a null.
- **Depth is declared record by record and it matches the ledger.** All **14** new `PAPER` records'
  `Evidence depth` equals the landed receipt: **7** `partial_fulltext_read` (123, 124, 127, 128,
  129, 130, 132) and **7** `complete_fulltext_read` (119, 120, 121, 122, 125, 126, 131); the partial
  ones name what is owed, including the one supplement (S9) that carries half of a result the
  ledger uses. Six receipts even carry an explicit `evidence_basis` note withdrawing an earlier
  draft's `complete_fulltext_read` against the same coverage. That is the discipline working.
- **No overstatement vocabulary enters canon.** Across every registry addition, `demonstrat*`,
  `establish*`, `prove*`, `novel`, `unique`, `confirms` occur only inside **paper titles** or inside
  **negations** (*«none of them a demonstrated negative»*). Nothing says *first*.
- **Four sampled propositions reproduced verbatim at source**: Rim 2018 `c.1060C>T p.Gln354Ter`
  on `NM_016373.2` with **PVS1** applied, the `exon 6–8 duplication` row with **PM2, PM3, PP4, PP5
  and no PVS1**, phase by maternal/paternal inheritance, and asymptomatic parents as **inclusion
  criterion 7** (*«offspring of asymptomatic Korean parents»*) — all four exactly as the records
  state; Robertson 2025's `c.49G>A (p.E17K)`, **172** UKBB carriers, **157 kb** core haplotype over
  all **175**; Yang 2023's abstract attaching the **deletion** sentence to **`KCTD18-like`** while
  WWOX is SNP-only against the authors' own `P = 1.00 × 10⁻⁵` threshold and their own statement that
  nothing reached genome-wide significance; Kałuzińska 2021's cut-point **222.6**, |R| 0.42–0.44 and
  **no WWOX perturbation anywhere** (the single `knockdown` hit is a cited RRM2 study), with the
  authors' *«yet to be confirmed»* carried.

---

## Verdicts by area

| # | Area | Verdict |
|---|---|---|
| A1 | Locator fidelity on 6 sampled papers (31 propositions) | **CONFIRMED** — every sampled proposition reproduced; 0 OVERSHOOT except A4 |
| A2 | Artefact identity (6 receipts) | **CONFIRMED** — `source_fingerprint` = on-disk sha256, 6/6 |
| A3 | Depth declarations in `paper_registry_current.md` (14 records) | **CONFIRMED** — 14/14 match the ledger; 7 partial / 7 complete as declared |
| **A4** | **Depth wording in `dismissal_ledger_current.md`** | 🔴 **FINDING MINOR F1** — four rejections say *«complete read»* of partial readings |
| **A5** | **Strength of the rWWOX neuron result** | 🔴 **FINDING MINOR F2** — *«equally»* is not what the source states |
| **A6** | **Transfer limit dropped at synthesis in `BLOCK 1 §4`** | 🔴 **FINDING MINOR F3** — a cited result is restated as measured |
| A7 | `CLAIM 032` structural integrity + genotype caution | **CONFIRMED** — pre-existing prohibitions byte-identical; missense/null kept apart |
| A8 | `CLAIM 011` `PREMISE_TAG` grounds and bound | **CONFIRMED** (modulo F2) — the *«none of this bounds the claim»* line is accurate |
| **A9** | **Counts in the working-model history** | 🔴 **FINDING MINOR F4/F5** — *«seven of the twelve»*, *«four corpus placeholders promoted»* |
| A10 | Public-edition rule | **CONFIRMED** — `public_release_gate.py` **PASS, BLOCKS 0**; every new record carries the class-level line; no REVIEW line is attributable to this batch (the four flagged `pathograph_export.jsonl` rows belong to PMIDs 39416860 / 42082822, pre-existing) |
| A11 | Gates at `ba5682f` | **CONFIRMED** — LINT `WARN`, no BLOCK; receipts `OK 284 chained`, tail anchored; `growth_anchors` **PASS** |
| A12 | Harness repair `test_record_scoped_edit.py` | **CONFIRMED** on logic — 61 tests OK; 🔸 **NOTE F8** on its docstring |
| A13 | Overstatement / transfer limits in new prose | **CONFIRMED** (apart from F3) |
| A14 | Provenance of reader computations | 🔸 **NOTE F6** — asymmetric: one of three reader mappings is fingerprinted |
| A15 | `LEAD-C1`'s blocked premise | 🔸 **NOTE F7** — the blocking fact is likely in a panel already held |

---

## F1 — four rejections call a partial reading a complete one (MINOR, candidate `CC-20261003-MIRROR-01`)

`disease-models/wwox/research/dismissal_ledger_current.md`, lines **308 / 314 / 319 / 326**:
`DIS-026` *«from a complete read of PMID 34204789»*, `DIS-027` *«from a complete read of
PMID 33195192»*, `DIS-028` *«from two complete reads in the same wave: PMID 37897534 … and
PMID 42395553»*, `DIS-029` *«from a complete read of PMID 37897534»*.

**Measured.** All four PMIDs landed as `partial_fulltext_read`:

```
python3 framework/scripts/fulltext_receipts.py status --pmid 34204789   # partial; figures captions_only, supplementary not_read
#   idem 33195192, 37897534, 42395553
```

Each of those receipts carries, in its own `evidence_basis`, the sentence *«An earlier draft of this
receipt claimed `complete_fulltext_read` against the same coverage; that claim was wrong and is
withdrawn»*. The ledger prose is the **withdrawn** depth, surviving in canon one file away from the
receipt that withdrew it — and `PAPER 127` / `PAPER 129` / `PAPER 130` state `partial` correctly, so
the registry and the ledger now disagree about the same readings. `DIS-027` partly repairs itself
(*«the total-ERK half sits in Supplementary Figure S9, which was not read»*), which shows the author
knew the coverage and the opening clause was not resynced.

**Why it matters and not more than it matters.** No rejection depends on an unread panel: every §13
ground is a text-level fact I re-verified for `DIS-026` (no perturbation in the study) and for
`DIS-028` (γ-H2AX up at 100 and 150 ng/mL rWWOX and in `WWOXOE`, and up in late-passage `Wwox−/−`
MEFs). The defect is a **depth attestation**, which this repository treats as load-bearing: a
declaration counts as a reading in `coverage_report`, in the self-eval ratchet and in triage.

**Fix.** Four string replacements, `old` measured unique (1 occurrence each). Candidate
`CC-20261003-MIRROR-01`.

## F2 — *«equally in disease and isogenic control cells»* (MINOR, candidate `CC-20261003-MIRROR-02`)

`CLAIM 011`'s new `PREMISE_TAG` and the new `BLOCK 1 §4` bullet both say the rWWOX viability loss was
*«equally in disease and isogenic control cells»*. **What the source states** (`files/fulltext/
PMID42395553_Petrozziello2026_bioRxiv.txt`, sha256 `d6a73e97…`, lines 678–684):

> *«Our results revealed a significant decrease in cell viability in both rWWOX-treated HD cortical
> neurons (65Q) and their isogenic controls (27Q) compared to the respective vehicle-treated
> cells (Figure 4B).»*

Each line is compared **to its own vehicle**. No 65Q-versus-27Q contrast is reported in the text, no
effect sizes are given, and **Figure 4B was not read** (`figures: captions_only`). *«In both»* is
what was measured; *«equally»* adds a between-genotype equivalence — the quantity the reading cannot
see — and it is the clause that does the work in the sentence, since the point being made is that the
toxicity is **not** disease-specific. The conclusion drawn (raising WWOX is not uniformly benign) is
untouched by the repair.

## F3 — a cited result restated as measured in the hot file (MINOR, same candidate)

`BLOCK 1 §4`: *«WWOX overexpression increased proliferation in 1 of 4 glioblastoma lines
(PMID 37781246)»*. `CLAIM 011`, for the same datum, says *«(PMID 37781246, and that phenotype is
cited from the group's preceding paper, not measured there)»* — and the claim record is right. On the
artefact:

> *«annotations indicating a unique regulation of proliferation align with previous data –
> proliferative potential after WWOX overexpression was increased only in DBTRG-05MG
> (Kaluzinska-Kolat et al., 2023)»*

The working model is the most-read file of the four and here it asserts as measured what its own
claim record records as cited. This is the synthesis-level omission pattern: both carried sentences
are individually fine and the compression is what loses the limit. **Fix:** nine words appended to
the bullet.

## F4 / F5 — two counts in `working_model_history.md` (MINOR, candidate `CC-20261003-MIRROR-03`)

**F4.** The `WM_v7.8` changelog row's confidence column reads *«seven of the twelve new paper records
are partial reads»*. The batch created **fourteen** (`PAPER 119`–`132`). Commit `0c9b3a1` exists
precisely to repair this arithmetic — its own message says *«seven of the FOURTEEN new paper records
are partial reads, not seven of twelve»* — and it corrected the `Last update` note and the ranges in
the row, but **not this cell**. A ratio corrected in one place and left standing in the other is the
`WM-3b` lesson exactly.

**F5.** The same note says *«with four corpus placeholders promoted and kept as history»*. Measured
on the diff: **three** promotions (`CORPUS P253` → `PAPER 119`, `CORPUS-STUB-083` → `PAPER 129`,
`CORPUS-STUB-077` → `PAPER 130`, each with its `LIT` twin annotated). The fourth placeholder touched,
`CORPUS P263` / `LIT-0263`, was **corrected in place** and its own new text says *«no claim
promoted»*. Promoted and annotated are different acts and the note merges them.

```bash
git diff 9fddfb1 ba5682f -- disease-models/wwox/registries/paper_registry_current.md \
  | grep -c "Promoted 2026-10-02 to"      # → 3
```

## F6 — one of three reader mappings is fingerprinted (NOTE, no registry op)

Three registry statements rest on reader computation against Ensembl GRCh37. The 24949445 reading
names the **transcript** (`ENST00000566780`) and the **sha256 of both lookups**. The other two do
not: 29390993's in-frame arithmetic (*«exon lengths 89 + 186 + 265 = 540 nt»*, carried into
`PAPER 121`'s `Role`) names no transcript and no response, and 32081867's exon coordinates (*«exon 5
ends 78,198,186; exon 6 starts 78,420,757»*, *«exon 8 is 78,466,385–78,466,649»*, carried into
`PAPER 124` and `DIS-023`) likewise. The arithmetic checks out (540 is divisible by 3; the case
interval falls strictly between the intron-5 bounds) and the two dossiers **corroborate each other**
on exon 8's end, so this is not a suspicion of error — it is that two statements now in the registry
cannot be re-derived at the same cost as their sibling. **Fix:** one line in each dossier, the shape
the 24949445 dossier already uses.

## F7 — `LEAD-C1` may be blocked on a panel already in hand (NOTE, no registry op)

`PAPER 128` says *«The paper never states which WWOX intron or exon Flex1 lies in — the fact the
hypothesis would turn on is absent from the body»*, and `LEAD-C1` is carried as blocked on acquiring
Finnis 2005. True of the body; but Figure 1B's **own caption**, in the held artefact, reads *«Below
it, the exons of the WWOX/FOR gene are represented by grey boxes»* beneath the flexibility peaks —
so the panel plots Flex1 against WWOX's exons, and `figures: captions_only` is exactly why it was not
resolved. Cheapest next step is that panel, not a new acquisition. (Measured, as the record states:
`WWOX` occurs **9** times in **189,143** bytes — reproduced exactly.)

## F8 — the repaired test's docstring is stale (NOTE, harness)

`framework/scripts/test_record_scoped_edit.py` now **derives** the live last record per registry
(`rse.identity_headings(text, levels)[-1][2]`) instead of pinning `PAPER 118` / `LIT-0420`, which is
the right repair: a batch that appends a record must not have to edit this suite, and the assertion
being made (only `BLOCK 3`'s assumed tail **covers** anything) is unchanged and still measured on the
live files. 61 tests OK at `ba5682f`. But the new docstring says the batch *«moved both tails on to
`PAPER 130` and `LIT-0429`»*, and after the § 6 addendum the live tails are **`PAPER 132`** (line
8072) and **`LIT-0431`** (line 12736). The test is right and its explanation is one commit behind.
One residual the repair accepts by design: with no pinned name the suite can no longer fail on *which*
record the tail is, only on whether the live tail behaves — worth one sentence rather than a change.

---

## Where I could be wrong / `WHAT_WOULD_CHANGE_MY_MIND`

- **F1** — if `fulltext_receipts.py status` for any of 34204789 / 33195192 / 37897534 / 42395553
  returns `complete_fulltext_read` at `ba5682f`, or if a second receipt for that PMID at complete
  depth exists in the chain and the ledger prose refers to that one, F1 is void. (Checked: one
  2026-10-02 receipt each, all partial.)
- **F2** — any sentence in PMID 42395553 reporting a 65Q-versus-27Q comparison of the rWWOX effect,
  or a Figure 4B panel read at native size showing indistinguishable magnitudes **and** a stated
  test, makes *«equally»* supported and the op unnecessary.
- **F3** — if PMID 37781246 contains its own proliferation assay after WWOX overexpression, the WM
  bullet is right and `CLAIM 011`'s parenthesis is the error. (Checked: the paper states it has *«no
  in vitro assay investigating this process in our former study»* for the vasculogenesis arm and
  attributes the proliferation result to Kaluzinska-Kolat 2023 by citation.)
- **F4/F5** — a stated rule by which "twelve" counts something other than the new `PAPER` records
  (e.g. records created by a named candidate), or a fourth promotion annotation I failed to grep,
  voids each respectively.
- **F6/F7/F8** — a digest already recorded elsewhere, a panel that does not in fact resolve the
  intron, or a docstring repaired after `ba5682f`.
- **On the whole batch:** I sampled 6 of 17 readings at artefact level. A defect in the other eleven
  — in particular in the five readings whose propositions I checked only against the registries'
  internal consistency — would not have been caught here.

`REVIEWER_CONFIDENCE` HIGH on F1, F3, F4, F5 (each reproduced by command against artefact or diff);
MODERATE-HIGH on F2 (rests on the text layer plus an unread panel); NOTE-level by construction on
F6–F8. `RESIDUAL_UNCERTAINTY` the eleven unsampled readings, and every figure/supplement value in the
seven partial readings, which this review did not open either. `EVIDENCE_NEEDED` none for the three
candidates: all `old` strings were measured unique in the working tree at `ba5682f` and must be
re-measured by the propagating batch.

`AUTHOR_RESPONSE` — owed, and silence is not acceptance (Annex C.2).

## Candidates written by this review

| Candidate | Finding | Ops | File(s) touched |
|---|---|---:|---|
| `CC-20261003-MIRROR-01` | F1 | 4 | `research/dismissal_ledger_current.md` |
| `CC-20261003-MIRROR-02` | F2, F3 | 3 | `registries/claim_registry_current.md`, `registries/working_model_current.md` |
| `CC-20261003-MIRROR-03` | F4, F5 | 2 | `registries/working_model_history.md` |

Three candidates added to a backlog `growth_anchors check` already reports at its trigger of 5 —
noted deliberately: a Mirror finding is a new task, and the next `BATCH_COMMIT` propagates these or
records why not.

## DEFAULTS_TAKEN (§21c)

| Condition | Default taken | Why it is safe | What would have been different |
|---|---|---|---|
| `files/` is absent from the worktree and symlinks are refused | hardlink-copied root `files/` into the worktree, read-only | no byte written; identity re-proved by sha256 against each receipt | without it no artefact-level check was possible at all |
| Review-file directory not pinned by the brief (`mirror_reviews/` does not exist) | wrote into `research/session_evaluations/`, where the eight existing mirror reviews live, under the brief's filename | existing convention; nothing else reads a new directory | a new directory no tool routes to |
| Three reader-mapping inputs not independently re-derivable offline (Ensembl) | accepted as labelled `INFERENZA`, checked internal consistency and cross-dossier agreement, filed the provenance gap as a NOTE | the computations agree with each other and with the printed coordinates; no claim rests on them unlabelled | an external lookup, which this review does not need to adjudicate the batch |
| Findings require registry edits that Mirror may not make | wrote candidates with exact ops and verbatim `old` | §21e: a finding is a new task for the author; Mirror edits no registry | a Mirror edit, which the role contract forbids |

`STOP_LOG` — **empty.** No class-1 reserved act and no class-2 condition arose: nothing was pushed,
no registry was edited, and every condition above had a safe default.
