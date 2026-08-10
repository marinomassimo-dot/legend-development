# STATE MANIFEST — LEGEND (public disease-level fixture)

> **Foundational file.** Active state of the LEGEND system.
> This is the only **state-control** file updatable outside a `BATCH_COMMIT`.
> Designated non-canonical append-only ledgers are explicit carve-outs: they may append
> through their validated writers, but never replace the four scientific current files.
> Every operational event (ingest, lint, commit candidate, batch commit, branch) must update it.
>
> **Public edition note.** This is a **disease-level fixture**, not the operational state of any private working instance. It carries no patient record and no session-specific operational history. It exists so the framework is internally coherent and (eventually) LINT-passable at the disease-model level. Values are illustrative placeholders for the public WWOX disease model.

---

## 0. PURPOSE

Track, unambiguously and readably:

- active framework version
- active disease-model (working-model) version
- state of each `*_current.md` file
- last completed `BATCH_COMMIT`
- last `LINT` run
- current operational state of the system
- active parallel branches (if any)

Without an up-to-date manifest → system in `UNKNOWN` state → `BLOCK_SYSTEM`.

---

## 1. SYSTEM VERSION

```yaml
framework_version: v3.3.1
framework_file: framework/instruction/LEGEND_CORE.md
manifest_schema_version: 1.0
edition: public
```

---

## 2. DISEASE-MODEL (WORKING-MODEL) VERSION

```yaml
working_model_version: WM_v4.1
working_model_file: disease-models/wwox/registries/working_model_current.md
narrative_view: disease-models/wwox/disease_model.md
notes: "Canonical disease-level working model derived from public literature; disease_model.md is its narrative reader-facing view. The private individual-level record is not part of this edition."
```

**Rule:** every `BATCH_COMMIT` that modifies the disease model **must** bump `working_model_version` (format `WM_vMAJOR.MINOR`).

- MINOR bump: claim addition/modification, block update without reversals
- MAJOR bump: reversal of a baseline claim, block redefinition, authorized urgent commit

Commit candidates must declare their intended `target_wm_version`.

---

## 3. CURRENT FILES STATE

### 3.1 Disease-model canonical files

| File | Status | Notes |
|------|--------|-------|
| `disease-models/wwox/registries/working_model_current.md` | present | **canonical** disease-level working model — claim mirror, changelog, decision blocks |
| `disease-models/wwox/disease_model.md` | present | narrative reader-facing view of the same model |
| `disease-models/wwox/registries/claim_registry_current.md` | present | canonical claims (public literature) |
| `disease-models/wwox/registries/paper_registry_current.md` | present | integrated / baseline-linked papers |
| `disease-models/wwox/registries/literature_tracking_log_current.md` | present | lifecycle state of every paper in the pipeline |

### 3.2 Meta-analyses

| File | Status |
|------|--------|
| `disease-models/wwox/meta/meta_index_current.md` | present |
| `disease-models/wwox/meta/meta_network_myelin_glia_current.md` | present |
| `disease-models/wwox/meta/meta_metabolism_current.md` | present |
| `disease-models/wwox/meta/meta_prenatal_structure_current.md` | present |
| `disease-models/wwox/meta/meta_human_spectrum_current.md` | present |
| `disease-models/wwox/meta/meta_gaba_paradox_current.md` | present |

### 3.3 Compounding-memory files (non-canonical, append-only)

| File | Status | Notes |
|------|--------|-------|
| `disease-models/wwox/research/discovery_ledger_current.md` | present | cumulative discovery capital — leads toward biomarkers, molecules, repurposing |
| `disease-models/wwox/research/therapeutic_hypotheses_ledger_current.md` | present | scored hypothesis portfolio from the co-scientist loop |
| `disease-models/wwox/research/dismissal_ledger_current.md` | present | rejections with their `REVIVAL_TRIGGER` — nothing dies in silence |
| `framework/eval/learned_gates_registry.md` | present | reusable error-prevention gates distilled from failures |
| `disease-models/wwox/registries/fulltext_read_receipts.jsonl` | present | authoritative append-only full-text event ledger; hash-chained and tail-anchored (§6.1), LINT-verified; includes explicitly non-contemporaneous legacy reconstructions |

### 3.4 Operational files (private overlay — not in this repository)

| File | Status | Notes |
|------|--------|-------|
| `inbox_current.md` | not shipped | ingest quarantine |
| `session_commit_log.md` | not shipped | commit-candidate queue; the LINT checks it when present |
| `legend_activity_log.md` | not shipped | operational timeline |
| `capability_scout_log.md` | not shipped | capability-growth log |

---

## 4. LAST BATCH_COMMIT

```yaml
last_batch_commit_id: BATCH_20260810_002
last_batch_commit_date: 2026-08-10
last_batch_commit_type: MINOR
commit_candidates_propagated: 2
commit_candidates_superseded: 0
commit_candidates_deferred: 1
batch_20260810_002_scope: "PROPAGATED 2. CC-20260810-42422765-S8: the shorthand 'finestra terapeutica P1-P5' is removed from the PAPER record for PMID 42422765 and replaced with what Figure S8 shows — efficacy at several early postnatal doses including P5, the interval incompletely sampled per endpoint, the upper boundary beyond P5 untested. S8 has no P0 group; survival to P40 omits P4 and to P300 keeps only P1 and P5; weight and glucose at P14 draw WT-vs-KO and WT-vs-P5 with no treated-vs-KO comparison, and ns is not equivalence; panels E-I test P5 only. 'P1-P5' read as a validated continuous window what is a sparse set of sampled points with the comparison that matters never drawn. CC-20260805-001: CORPUS-STUB-095 promoted to PAPER 060 (PMID 37519886, Kolat 2023), placeholder preserved append-only, LIT-0117 completed from 'corpus paper 95' to full metadata with its complete_fulltext_read receipt. Promotion of provenance, not of scope: T3, clinical relevance LOW, no claim link, DISCOVERY_ONLY. STILL DEFERRED 1: CC-20260810-30755385, whose registry promotion is mechanical but which also asks for a meta_metabolism rewrite separating direct measurement from inferred mitochondrial glucose oxidation, and a CLAIM 009 link. Half-applying it would leave the registry claiming a reading the meta does not carry. Its two most transferable products are already recorded outside the canonical layer and are not waiting on it: FT-048 (the ITT age discrepancy) and FT-049 (tissue of measurement is not tissue of necessity, as INFERENZA with its three sources)."
target_wm_version: WM_v4.1
last_wm_update: 2026-08-06
last_wm_batch_commit_id: BATCH_20260806_002
trigger: "explicit operator authorization 2026-08-10; threshold also met (6 pending candidates)"
batch_20260810_001_scope: "PROPAGATED 3: step 0 (batch_commit_gate BLOCK_BATCH_COMMIT -> OPEN, with the reopening recorded as road 3 and not the condition originally written); CC-20260810-CLAIM004-REVIEW (CLAIM 004 -> flagged for review, comparator missing); CC-20260810-CLAIM011-REVIEW (CLAIM 011 -> flagged for review, dose-response continuum concealing a threshold; the instruction named CLAIM 020, which is Teplyshova natural history and unrelated — flagging it would have marked an innocent claim and left the defect standing). Coupled with step 0 and applied in the same window: deepdive_manifests/PMID17803050.json re-anchored, 29 body/table locators moved off the refused .html onto page crops with needle, crop, dpi and image digest; validator PASS, 0 gaps. DEFERRED 3, declared not forgotten: CC-20260805-001 (PMID 37519886 registry promotion), CC-20260810-30755385 (CORPUS-STUB-039/LIT-0063 promotion + meta_metabolism + CLAIM 009 link), CC-20260810-42422765-S8 (the 'finestra terapeutica P1-P5' shorthand in paper_registry line 261 is wrong: S8 contains no P0 group, survival to P40 omits P4, and the drawn tests are WT-vs-KO and WT-vs-P5 with no treated-vs-KO comparison). Each deferred candidate is a registry rewrite needing its source open, and a batch that half-applies one is worse than a batch that declares it. Full-text queue entries FT-048 and FT-049 were added ahead of this batch, outside it: the queue is not a canonical scientific file."
notes: "BATCH_20260806_002 (MINOR, WM_v4.0 → WM_v4.1). Four candidates propagated: CC-20260806-19936220, CC-20260806-19500159, CC-20260806-17803050 and CC-20260806-31340538. CC-20260806-19936220 item 1 was SUPERSEDED by CC-20260806-19500159 item 1 before propagation — the verdict moved from 'unsupported' to 'contradicted' once the terminus was read — so the superseded count is 1. THE IMPORTED-PREMISE CHAIN UNDER CLAIM 005 IS NOW TRACED END TO END, EVERY LINK READ IN FULL: early death is first-hand in PMID 19936220, but epileptogenesis is not measured there in any form, and the terminal source PMID 19500159 states in three places, plus a Table 2 whose Epilepsy row is empty for both mouse models, that Wwox-null MICE SHOW NO EPILEPSY. Two citation hops had converted an explicit negative about a rat into a positive assertion about a mouse; the co-cited premise in the same sentence was true, which is why it read as verified. New claims 036 (systemic metabolic decompensation of the P18 mouse null as a quantified confounder, with PREMISE: DEFAULT_FROM_TEXTBOOK on brain ablation never shown), 037 (the seizure phenotype as a rat lde/lde phenotype, EEG-documented, allele corrected to structurally frameshift and functionally protein-null), 038 (recurring BUN/creatinine with two competing untested explanations, renal insufficiency versus seizure-driven hypercatabolism, the second competing directly with the renal-tubular-acidosis hypothesis PMID 19936220 never tested), 039 (ataxia 95 percent versus 0 percent, non-cerebellar, the most penetrant lde phenotype and one the downstream literature dropped). PAPER 057/058/059 and LIT-0405 created; CORPUS P295 and P363 marked promoted append-only. PAPER 021 metadata corrected: the author is Tochigi, not Kumada, and the record carried an INVENTED TITLE naming lissencephaly, a word absent from the paper, which had been steering it toward a migration/layering reading the study does not make; CLAIM 014/015 now bound it to early postnatal maturation (PND5-21) and meta_prenatal_structure reclassifies it as the postnatal bridge. DIS-011 and DIS-012 entered in the dismissal ledger with revival triggers. meta_gaba_paradox given a provenance correction and the competing systemic-confounder explanation. Integrity status fields added to the held records PMID 16223882 (expression of concern) and PMID 23446842 (retracted), closing a debt declared at session start; no canonical claim rests on either. Pre-flight and post-propagation LINT PASS; release gate PASS/0; receipts 52 chained and tail-anchored; self-eval PASS with active complete reads 15. Snapshot backup/snap_20260806_batch_wm41. Prev: CC-20260806-30290271 → CLAIM 005 narrowed to what PMID 30290271 measures and its medication caution DELETED (the source tests no drug, no GABA concentration, no inhibitory function); PAPER 006 / LIT-006 identifiers normalized; CORPUS-STUB-085 resolved as duplicate, preserved append-only; meta_gaba_paradox corrected from interneuron loss to marker-positive abundance, NPY marked DG-only, Il6-not-Tnf-a recorded. MAJOR because removing safety language from a consolidated baseline claim is a policy change even when it removes rather than adds; the experimental datum is NOT demoted. Publication-integrity audit of the 7 held records run first (staging/audit_publication_integrity_20260806.md): no canonical claim rests on any of them. Pre-flight and post-propagation LINT PASS; snapshot backup/snap_20260806_batch_wm40. Prev: BATCH_20260726_001 (MINOR, WM_v3.2) — CC-20260726-001/002/003 → PAPER 054/055/056, CLAIM 034/035 new, CLAIM 009/016/024 modified; snapshot backup/snap_20260726_1600."
```

---

## 5. LAST LINT

```yaml
last_lint_type: LINT_AUTOMATIC
last_lint_id: LINT_20260806_010
last_lint_date: 2026-08-06
last_lint_result: PASS
notes: "PMID 30290271 read completely from article HTML/PDF with all six figures, Table 1, both supplements and 90 references audited. Receipt FTR-20260806-30290271-01 appended (46 -> 47 events). After adversarial cross-review, its schema-v2 manifest carries 14 exact body-text locators plus 7 fingerprinted figure locators and passes strict verification with zero gaps. The candidate is explicitly MAJOR (target WM_v4.0_2026-08-06), deletes unsupported medication-safety language and requires operator authorization; unread-premise baseline is the live 13/13 and self-eval is 24/24 PASS. PubMed pipeline commits 212850e, 510414d and d9ccac9 merged and independently hardened. A fresh 2026-08-06 harvest preserves 706/706 records, 693 abstracts in the gitignored NOT_EVIDENCE corpus and a tracked no-abstract projection with 40 correction links. RefType direction was corrected: 7 affected publications are held, while 4 editorial notices remain admissible audit sources. Five held PMIDs occur on current surfaces, but none is integrated as a canonical PAPER and no claim wikilink depends on one; PMID 28151481 was already explicitly excluded. Legacy receipt FTR-20260726-23446842-01 was the sole receipt-to-PAPER identity mismatch and is quarantined append-only by FTR-20260806-23446842-02; active depth and generated coverage no longer attribute it to PMID 23446842. LINT PASS; public release gate PASS/BLOCKS 0. The pre-refresh clean-worktree release suite passed with one declared local-fulltext skip; post-refresh suite pending this lint event. 2026-08-06 continuation (LINT_20260806_007): an independent blind review with no context on the code reproduced eight further defects, all fixed — the corpus content firewall was disabled by the process working directory (fail-open at write, fail-closed forever at read); the same guard refused honest prose describing a permitted triage use; the LINT integrity gate could not see the CORPUS placeholders two held records live in, and blocked claims citing the retraction notice itself; `status --pmid` ignored invalidations. Earlier in the same pass, an invalidation was found to withdraw a paper's whole reading history instead of the named event. Firewall detection re-tuned against the seed's real column set: six of eight escapes closed, both false positives gone, gzip/UTF-16 declared open rather than patched. Withdrawing a complete read now requires re-opening the reading debt. Two DisMech consumers left uncorrected by design: their SHA-256 is sealed into the Phase-2 baseline and re-sealing without re-deriving would falsify provenance. BATCH_20260806_001 propagated (MAJOR, WM_v4.0). Release regressions PASS WITH SKIPS on a clean worktree. 2026-08-06 continuation (LINT_20260806_008): FT-043 closed — PMID 19936220 (Ludes-Meyers 2009, PLoS ONE) retrieved open-access and read completely; receipts FTR-20260806-19936220-01 and its correction -02 appended (48 -> 50 events); schema-v2 manifest carries 23 verified locators (18 body, 2 table, 3 figure), zero gaps, zero waivers, and was mutation-tested 8/8 before persistence including proof that an abstract-only sentence cannot validate a body locator. THE PREMISE SPLITS: early death is first-hand and quantified in PMID 19936220 (43% dead by 72 h, 77% by day 17, none past weaning), but EPILEPTOGENESIS IS NOT MEASURED THERE IN ANY FORM — no EEG, seizure, behaviour or brain histology; the only brain measurement in the paper is organ weight. It enters only as a Discussion citation of the rat lde model (PMID 19500159/17803050: 13-bp exon-9 deletion, C-terminal frameshift, NOT a null, audiogenic seizures), so five canonical surfaces credit a mouse paper with a rat phenotype across two allele classes. FT-042 and FT-041 re-prioritised as the actual terminus. Also recorded: EIIA-Cre here versus BK5-Cre in PMID 30290271 (shared allele, different knockout); Wwox ablation shown only in kidney, lung and spleen with no brain lysate anywhere (tagged PREMISE: DEFAULT_FROM_TEXTBOOK with a revival trigger); a measured systemic metabolic crisis at P18 that makes brain-phenotype confounding quantified rather than speculative; brain weight is relative-only brain sparing, not overgrowth; the osteosarcoma conflict with PMID 17360458 is explicit and unresolved; and the paper's own renal-tubular-acidosis hypothesis is the sole PubMed record on WWOX and acidosis, untested for seventeen years. Corrections isolated in staging/commit_candidate_20260806_19936220.md (MINOR, target WM_v4.1); no canonical scientific current file edited. The session's own trace-contract regression caught this session's receipt naming a gitignored staging path as an output — corrected append-only, never rewritten. Two gates added: IMPORTED_PREMISE_ATTRIBUTION_GATE and SEALED_CONSUMER_CIRCULARITY_GATE. LINT PASS; release gate PASS/BLOCKS 0; self-eval PASS with active complete reads 12 -> 13. Release regressions FAIL on exactly the three declared at session start (DisMech seal, its runner-verdict echo, and the environmental release-surface roots); the DisMech Phase-2 window decision remains open and is deliberately unresolved. 2026-08-06 continuation (LINT_20260806_009): FT-042 closed — PMID 19500159 (Suzuki 2009, Genes Brain Behav) obtained by the operator through institutional access after eight automated retrieval tiers refused it (bronze OA, single Wiley location, Cloudflare), then read completely; receipt FTR-20260806-19500159-01 appended (50 -> 51 events); schema-v2 manifest carries 30 verified locators (24 body, 2 table, 4 figure), zero gaps, zero section waivers. THE CHAIN IS NOW CLOSED AND THE PREMISE IS NOT UNSUPPORTED BUT CONTRADICTED: the terminal source states in three places, and in a Table 2 whose Epilepsy row is empty for both mouse models, that WWOX KNOCKOUT MICE SHOW NO EPILEPSY. Two citation hops converted an explicit negative about a rat into a positive assertion about a mouse. The rat phenotype is instead solid and first-hand: 95% audiogenic penetrance (19/20), 60% spontaneous (30/50), 0/14 controls, kindling-like latency shortening, interictal ~10 Hz spikes in all mutants unstimulated, hippocampal vacuoles 9/9 versus 0/10. Yesterday's allele-class note is corrected: the lde allele is structurally a C-terminal frameshift and functionally a protein-level null (mRNA normal, no 47 or 42 kDa species, antibody epitope outside the altered region). Recorded with revival triggers: the paper attributes the mutant protein's disappearance to the ubiquitin-proteasome system with no turnover assay, inhibitor or route determination, the same default falsified on 2026-07-12; the headline 95% is a female-only cohort stated only in the Figure 6 caption; and Figure 1's caption misassigns its own panels. OPEN AND CONTESTED: the paper's 'clearly excluded' rejection of a systemic metabolic cause rests entirely on unread FT-041, whose abstract — supplied by the operator, recorded as abstract_only with NO receipt because an abstract is not a reading — reports significantly increased urea nitrogen, creatinine and phosphate. FT-041 is now the highest-value unread paper in the repository. Supplementary declared unavailable, not skipped: HTTP 403 on both Wiley routes, no embedded files. Because the paper exists in no structured form, its PDF text layer was transcribed into a local HTML artifact with the abstract in a recognised container, and the abstract/body separation was proven before use rather than assumed. Mutation testing found two defects in the validator itself, not in the reading: abstract_snippet was never matched against the abstract (fixed in deepdive_manifest.py with two regression tests, the new test itself proven able to fail), and source_fulltext_indexed remains a self-declared boolean nothing verifies (recorded as open debt, not silenced). Corrections isolated in staging/commit_candidate_20260806_19500159.md (MINOR, target WM_v4.1), superseding item 1 of the 19936220 candidate; no canonical scientific current file edited. The operator closed the DisMech Phase-2 window and re-sealed with a three-tier scope (970ded7), so that pair is green and SEALED_CONSUMER_CIRCULARITY_GATE is marked SUPERSEDED by the stronger executable FREEZE_SCOPE_GATE. LINT PASS; release gate PASS/BLOCKS 0; self-eval PASS with active complete reads 13 -> 14; release regressions FAIL only on the environmental release-surface roots. 2026-08-06 continuation (LINT_20260806_010): FT-041 closed — PMID 17803050 (Suzuki 2007, Comparative Medicine; NO DOI, no PMCID, unaddressable by every OA aggregator) supplied by the operator and read completely; receipt FTR-20260806-17803050-01 appended (51 -> 52 events); schema-v2 manifest with 32 verified locators (25 body, 4 table, 3 figure), zero gaps, mutation-tested 6/6. THE CHAIN IS NOW TRACED END TO END, EVERY LINK READ IN FULL. Split verdict on FT-042's 'clearly excluded': the SPECIFIC mouse/rat serum contrast is CONFIRMED (glucose, calcium and electrolytes all non-significant in the rat), but the blanket statement is FALSE — BUN is 3.2-3.5x normal and creatinine significantly raised, so the rat is uraemic without being hypoglycaemic and the systemic confounder is not eliminated but different in kind. THE FINDING THIS READ ADDS: the authors propose that raised BUN/creatinine may reflect hypercatabolism and muscle disruption from repeated seizures rather than renal failure, with the SER strain as named precedent — a hypothesis that competes directly with the renal-tubular-acidosis explanation PMID 19936220 built for the mouse on the same marker and never considered; WWOX AND (hypercatabolism OR muscle disruption) returns 0 PubMed records. A SECOND FT-042 CLAIM IS REFUTED BY ITS OWN SOURCE: the attribution of lde dwarfism to low pituitary growth hormone rests on a phrase that exists only in THIS PAPER'S ABSTRACT; the body reports the difference as not significant and concludes the dwarfism cannot be explained by low GH. That is the third instance in one session of a citation firming up its source, and the first where the overstatement originates inside the source's own abstract. METHOD NOTE: the operator had supplied that abstract hours earlier and it was recorded as abstract_only with NO receipt, leaving FT-041 open; had it been accepted as a reading, 'decreased plasma GH' would have entered the model as a datum, and it is not one. Also recorded: ataxia at 95 percent and non-cerebellar is the most penetrant lde phenotype, more than the 34 percent seizures, and the downstream literature carries it not at all; the seizure incidence is a floor by the authors' own statement; the Mendelian chi-square rests on a survivor-selected 33 of 254 litters; brain sparing recurs with male absolute brain weight not significantly reduced; and the paper was accepted two years before the same group mapped lde to Wwox, with none of its 35 references WWOX-related, so its phenotypes cannot be a WWOX-motivated result. The abstract_snippet guard added earlier today ran in production on this manifest, validated a real anchor and caught a fabricated one. Corrections isolated in staging/commit_candidate_20260806_17803050.md (MINOR, target WM_v4.1), completing the trilogy with the 19936220 and 19500159 candidates; no canonical scientific current file edited. LINT PASS; release gate PASS/BLOCKS 0; self-eval PASS with active complete reads 14 -> 15."
```

---

## 6. OPERATIONAL STATE

```yaml
current_state: READY
deep_dive_gate: OPEN
ingest_gate: OPEN
batch_commit_gate: OPEN
active_parallel_branches: none
```

### Why `batch_commit_gate` is closed — 2026-08-09

**Not because the verifier is weak.** It was, and it has been repaired and mutation-tested
8/8. The gate is closed because of what the repaired verifier now *reports*.

`files/fulltext/PMID17803050_Suzuki2007.html` — the declared `article_text` behind `PAPER 059`,
the primary source of `CLAIM 038` and `CLAIM 039` — carries **34 C0 controls standing in for
characters that did not survive extraction**: 17 × `U+001D`, 9 × `U+000C`, 5 × `U+001E`,
3 × `U+001F`. Two are confirmed against the printed page: `(P \x1d 0.023)` for `(P < 0.023)`,
and `Ca2\x0c` for `Ca²⁺`. The validator now refuses that surface outright, so **29 canonical
locators are unverifiable** — by the system's own check, not by anyone's opinion.

Reading and locator capture stay safe, which is why this is `BLOCK_BATCH_COMMIT` and **not**
`BLOCK_SYSTEM`: nothing about acquiring evidence is compromised. Promotion is what must wait,
because promoting now would consolidate claims whose evidence chain the validator rejects.

**What lifts it:** the surface re-derived from the source — never hand-corrected. A manual fix
across 34 points is indistinguishable from a rewrite and verifiable by nothing. Then the 29
locators re-verified against the new artifact, and any that fail re-captured from the document.

The conclusions of `CLAIM 038` and `CLAIM 039` are **not** in question here. A human read them
off the paper. What is in question is whether the repository can still *prove* it.

### Reopened 2026-08-10 — by a different route than the one written above

🔴 **The condition as written was not met, and the gate is opened anyway.** Recorded, because
a gate lifted on a condition nobody re-read is how a gate stops meaning anything.

The surface was **not** re-derived. `PMID17803050_Suzuki2007.html` is still `SUSPECT` and the
validator still refuses it — correctly, and that has not changed. What was done instead is
road 3 of the three the reading laid out: the 29 locators were **re-anchored to the printed
page**, the surface the corruption cannot reach because the drawn glyph is the author's.

What stands behind them, each machine-checked rather than argued:

- every locator resolves through a **needle unique on its page**, verified to be a fragment of
  the snippet of the locator it names — so a crop cannot adjudicate the right character for
  the wrong sentence;
- every span sits **inside the crop that claims to show it** (`crop_contains_span`),
  re-checked after the crop rectangles were rounded to integers;
- the seven crops **regenerate to their declared digest** from the source PDF
  (`regenerate_adjudications.py verify`), so the evidence is reproducible without the images
  being redistributed — the article is all-rights-reserved.

Six of the 29 carried corruption inside what they assert; all six were read off the page and
**not one changes a value, a direction or a significance verdict**. `CLAIM 038` and `CLAIM 039`
stand as written. What had been lost was the repository's ability to prove them.

**Applied in this batch:** `deepdive_manifests/PMID17803050.json` no longer declares the
refused `.html` as a source artifact. Its 29 body/table locators now carry `surface: figure`
and name the page crop that attests them, each with page, crop rectangle in PDF points, dpi,
needle and image digest. The three figure locators were already anchored to the PDF and are
untouched. `deepdive_manifest.py --pmid 17803050` returns PASS with 0 gaps.

**The debt that remains, and is not cleared by this:** the text surface is still refused, so
`PMID 17803050` cannot back a *new* text locator. Anyone reopening that paper in full owes
road 2 — the surface rebuilt from the rendering, declared as a new artifact with its own
extraction method. `FT-041` carries it.

---

## 6.1 FULL-TEXT RECEIPT LEDGER ANCHOR

The full-text receipt ledger is append-only. A per-event hash chain makes a rewritten or
deleted historical event detectable; it cannot detect a *truncated tail*, because the
surviving prefix stays self-consistent. The anchor below closes that gap: it pins how many
events the ledger must hold and the digest of its last one. `LINT_AUTOMATIC` verifies both,
and a mismatch is `BLOCK_SYSTEM` — reading history you cannot trust is worse than none.

```yaml
fulltext_ledger_path: disease-models/wwox/registries/fulltext_read_receipts.jsonl
fulltext_ledger_events: 60
fulltext_ledger_head: 144f7dc3405ca730ace5dc217359c0eeeac4aa7392a6f2130e6c681327763516
```

Maintained automatically — `fulltext_receipts.py record` re-anchors after every append.
To re-anchor by hand after an authorized repair:

```bash
python3 framework/scripts/fulltext_receipts.py anchor
python3 framework/scripts/fulltext_receipts.py verify
```

## 6.2 GROWTH ANCHORS

Every constant below that says *"how big the system is right now"* is written by
[`growth_anchors.py`](../scripts/growth_anchors.py) and by nothing else. **No value in this
section may be typed by hand.** The rule it enforces is stricter than "automate it": *updating
a constraint must cost at least as much as complying with it.* The recorder re-measures the
registries and refuses a declared delta that does not match them, so a number cannot be bumped
to make a suite green — the only way to move it is to have made the change you declare.

```yaml
growth_anchor_ledger: framework/state/growth_anchors.jsonl
growth_anchor_events: 6
growth_anchor_head: b98faa747a08564da46f36d8a08e6e71b5807d2b04a5fefa59a8aa1c5c640af3
```

```bash
python3 framework/scripts/growth_anchors.py check     # live vs anchors
python3 framework/scripts/growth_anchors.py verify    # chain + tail anchor
python3 framework/scripts/growth_anchors.py record --batch <ID> --claims +4 --papers +3
python3 framework/scripts/growth_anchors.py tighten   # a ratchet fell; re-anchor it
```

The two ratchets documented below keep their own fields for backwards compatibility —
`legend_lint.py` and `session_self_eval.py` read them directly — but those fields are now
**written by `growth_anchors.py tighten`**, never by a person. The asymmetry is deliberate and
recorded here so a later reader does not mistake it for an oversight.

### Registry-declaration ratchet

Twenty registry records carry a historical `full text reviewed` declaration with no
surviving complete-coverage receipt. They are kept visible rather than deleted or
retroactively upgraded — the work happened, the evidence of *how completely* did not
survive. The baseline below is a **ratchet**: history is grandfathered by both count and
exact record identity. A count alone is insufficient because one old declaration could be
removed while a different unsupported declaration is added. Any *new* full-text declaration
must be backed by a persisted `complete_fulltext_read` receipt, or `LINT_AUTOMATIC` returns
`BLOCK_BATCH_COMMIT`.

```yaml
registry_only_fulltext_declarations_baseline: 19
registry_only_fulltext_declaration_ids: ["PAPER 010", "PAPER 011", "PAPER 012", "PAPER 014", "PAPER 016", "PAPER 028", "PAPER 029", "PAPER 031", "PAPER 032", "PAPER 039", "PAPER 040", "PAPER 042", "PAPER 043", "PAPER 044", "PAPER 045", "PAPER 046", "PAPER 049", "PAPER 050", "PAPER 053"]
```

Lowering the baseline is the intended direction of travel: back-fill a record with real
evidence, re-run `coverage_report.py`, then lower the number and remove that resolved ID
from the grandfathered list.

### Unread-premise ratchet

A separate and harsher debt, measured on 2026-07-26 by `session_self_eval.py`. The *reasoning*
layer — metas, therapeutic strategies, the analysis files — cites papers as **support for
conclusions**. The first measurement found seventeen of eighteen PMIDs with **no
complete-read receipt, no registry full-text declaration and no full-text-queue entry**. The
ratchet has since fallen as papers were read or their debt was made explicit; the current
baseline below must equal the live count, never preserve historical padding.

This is the failure mode that let PMID 22193544 be load-bearing in five files while unread,
with every existing check passing. It is invisible by construction, because leaning on a paper
writes nothing anywhere. So it is measured instead of assumed.

```yaml
unread_premise_baseline: 7
unread_premise_measured_on: 2026-08-10
```

**It is a ratchet, not a wall.** Blocking on the whole legacy backlog would only teach sessions
to route around the check; capping it makes every *new* unread premise a visible regression
(`UNREAD_PREMISE` → `BLOCK_BATCH_COMMIT`). Three things clear a citation, and only three: a
persisted `complete_fulltext_read` receipt, a registry record declaring the full text reviewed,
or an explicit `full_text_queue_current.md` entry. The third is what keeps the check honest
rather than punitive — **declared reading debt is legitimate work in progress; silence is not.**

---

## 7. NOTES

This fixture is intentionally free of any individual patient's operational history. The public edition separates three layers: the generic `framework/`, the disease-level `disease-models/wwox/`, and a private N-of-1 overlay that is **not** part of this repository.
