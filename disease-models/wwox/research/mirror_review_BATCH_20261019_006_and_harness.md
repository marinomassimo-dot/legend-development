# MIRROR review — BATCH_20261019_006 and the harness change 255237ac / 5179beed

> Role: MIRROR (hostile ex-post reviewer, `roles/mirror.md`, LEGEND_CORE 21e). Review of the producer's work, not mine. A finding is a new task for the author, never a hold. CONFIRMED means "no further defect found in the sampled bundle", not "true". Not medical advice.

## Verdict

**No BLOCK-class defect.** Part A: CONFIRMED, M1 to M8 all repaired, six low FINDINGs (A1 to A6). Part B: the SUPERSEDED_ARTIFACTS rule is sound for the live corpus and not a loophole for any honest write; it is a loophole for a deliberate hand edit and for one reclassification-versus-repair optic (B1 to B4).

## Checks run by me (after 255237ac, on main)

| Check | Result |
|---|---|
| `legend_lint.py .` | WARN, 0 BLOCK (standing UNLINKED_SUPPORT / POSSIBLE_CONTRAST set) |
| `fulltext_receipts.py verify` | OK, 680 chained, tail anchored |
| `growth_anchors.py check` | PASS (papers 416, corpus 376, literature 679, unread premises 0) |
| `public_release_gate.py` | PASS, BLOCKS 0 (only REVIEW rows on third-party published families, none in added text) |
| `test_manifest_receipt_provenance.py` | 20 tests OK; 452 manifests, CONFORMS 430, NOT_THE_PRODUCER 7, SUPERSEDED_ARTIFACTS 11, UNCHECKABLE 2, UNNAMED 2; 9 non-conforming = ceiling 9 |
| `test_batch_queue.py` | 51 OK |

(The battery was not run.)

## Part A — BATCH_20261019_006

STEELMAN. The batch discharged seven ORPHAN_COMPLETE_READ, registered 27 PAPER and 19 LIT records with identity, depth, receipt and full sha256 drawn from the ledger, kept every negative, changed no claim field, and corrected its own earlier errors in place with the old wording quoted.

**Mechanical.** All 27 PAPER records (400-426): artefact file exists and its SHA-256 equals the 64-character digest printed in the record (27/27); receipt id present in `fulltext_read_receipts.jsonl` (27/27); no e-mail string, no truncated digest in the 1,302 added lines; the only kinship words in added text are "siblings" of a published two-sibling FOLR1 report and the batch-report sentences about transmission wording (third-party, no reference-genotype pairing).

**Claims.** `git diff 7b214f1c..HEAD -- claim_registry_current.md` (covers batches 003-006): 8 insertions, 4 deletions; **no `Status`, `Type`, `Summary`, `Claim` line changed**. Changes are `Evidence boundary` lines, one `Source`/`Wikilinks` addition (CLAIM 028, PAPER 383) and rewordings inside two evidence-note fields. OK.

### M1 to M8 — each re-verified against the file

| # | Mirror finding | Now | Verdict |
|---|---|---|---|
| M1 | CLAIM 009 note inside Summary | Own `Evidence boundary` line; Summary byte-identical to the 7b214f1c base | OK |
| M2 | DL-MECH-117 TCGA overreach | Conclusion restricted to the leukocyte series; TCGA leg stated as not shown uncorrelated; title conditional | OK (see A5) |
| M3 | DL-MECH-145 "only where"; DL-MECH-139 caveat | "where, in two mouse models ... sufficient, not shown necessary"; 139 carries the no-epinephrine-alone and 15-minute shock-only caveat | OK |
| M4 | DL-MECH-148 premise false for the repository | Premise now "no record measures mTORC1 signalling in a Wwox-deficient neuron", cites PAPER 148 and 152 as cancer-cell over-expression | OK |
| M5 | Inconsistent T3/T4 | One scale (T1-T4) stated in the header; census of records 311-426: 83 substitutes all T4, 28 non-substitute T3, 4 non-substitute T4 (326, 400, 406, 414: list entry or count, per the rule), 1 T2. Shin 2023 (PAPER 383) T3 (was T4), Hong T3. Rule applied consistently | OK; two edge FINDINGs A1, A2 |
| M6 | CLAIM 028 "opposite sign" | "a different direction ... compared at title level only, readouts not commensurate"; Status and Type untouched | OK |
| M7 | PAPER 387 "the one" | "by term query over the registry files, not a statement about the literature" present | OK |
| M8 | 005 report overstated | Narrowed to "in the registry records"; PAPER 015 depth line carries its three receipts. Third-party transmission wording in dossiers retained and declared | OK; A6 |

### Sample of 16 new PAPER records against artefact text

400 Kilic (WWOX 4, CACNA1H 6 of 261, no T-type; Figure 1 discrepancy), 401, 403, 405 (PrestoBlue is resazurin-based; the word is the reader's gloss and is in the manifest), 407, 409, 410, 411, 412, 413, 415 (23 tumours, observed hemizygosity), 417 (497), 419 (FOLR1, 49), 422, 425, 426: every figure and keyword checked is in the artefact; none contradicted. T4 re-grade of the 19 substitutes and Shin to T3 are **defensible** under the stated scale (substitutes are not WWOX measurements; Shin is WWOX-direct but non-neural, same class as Hong).

**Agarwala 2023 (PAPER 425), checked line by line in the XML.** Rows 7 and 8: WWOX c.790C>T homozygous, onset 4 and 21 days; Table 4 row 50: WWOX deletion, homozygous, onset 27 days, cGH array; "53 of 77 tested" molecular diagnoses; so 3 of 80 recruited and 3 of 53 diagnoses hold. Limits stated in the record (outcomes by aetiological group, referral bias, array inference) are the right ones. WWOX-direct for three case rows, T2, gap stated: **defensible**, and the registered "not a pure substitute" is more accurate than the earlier SUBSTITUTE label (selection file corrected in place with the old word quoted).

**FT-115.** Retired with "no patient-level data"; the old "across different patients" wording is quoted and withdrawn; revival trigger stated; the paper never mentions T-type channels so the negative is, if anything, stronger. OK.

### Findings

- **A1 — FINDING (low).** PAPER 400 (Kilic) carries the T4 text "WWOX not measured", yet its own Role records four WWOX cases among 261. By the scale's wording ("a count") T4 is applied correctly; the boilerplate "WWOX not measured" is not true of this record. Reword the T4 line for the four non-substitute T4 records.
- **A2 — FINDING (low).** T2 for 3 WWOX rows in Agarwala against T4 for 4 WWOX diagnoses in Kilic is explained only by "rows versus counts"; say so in the scale sentence.
- **A3 — FINDING (low, substantive).** The two c.790C>T rows and the deletion row of PAPER 425 each cite earlier reports (Table "Literature" column: the Piard 2019 cohort = PAPER 117, and Surana 2020 = FT-201). These may be previously published patients. PAPER 425 and DL-MECH-166 treat "3 of 80" as a fresh proportion; FT-201 covers Surana only, Piard is marked "already read" but the overlap is not stated in PAPER 425. Add "possible overlap with PAPER 117" to the record and to DL-MECH-166 until the rows are traced.
- **A4 — FINDING (low).** DL-MECH-168 title ("neuroimaging at ascertainment can be normal in early-onset WWOX encephalopathy") rests on one table entry; the body says so, the title does not.
- **A5 — FINDING (very low).** DL-MECH-117 says a ratio of uncorrelated transcripts is "dominated by the denominator by arithmetic coupling"; that holds only if the denominator variance dominates. Add "when its variance is the larger" or drop "dominated".
- **A6 — FINDING (process, low).** The integrator edited the Mirror's own file (lines 92, 118) to pass the gate; findings unchanged, flagged in the report, but the quoted evidence of M8 is now paraphrased. Acceptable once; a reviewer's file should be edited by the reviewer.
- **A7 — scale deferral, OK with a condition.** Papers registry 1,539,001 bytes (anchor 1,211,399; previous re-raise 1,514,249); second renewal recorded as `scale_ack`, `growth_anchors.py check` PASS, operator told. The cost is about 2.6 KB per record; the next 40-record batch crosses 1.6 MB. **A third renewal should be refused until the operator has decided on sharding.**

## Part B — harness (255237ac, 5179beed)

### B1 — the three-condition rule: sound, not a loophole for honest writes — OK, with a stated residual

Rule: (a) declared receipt is a later naming event of the same study; (b) its `source_fingerprint` is among the manifest's own `source_artifacts` digests; (c) the earliest naming event has a non-empty fingerprint that is not among them. Missing fingerprints fall through to NOT_THE_PRODUCER (conservative); UNNAMED cannot reach it by construction.

Live corpus, all 11 SUPERSEDED manifests inspected: in every one the declared event's fingerprint is a listed digest and the earliest fingerprint is not; for the six 2026-10-19/20 re-reads the later artefact is a `_r2` / re-dated file on disk and the earlier `_PMC.xml` is gone from `files/` (e.g. 21075834, 30755385, 39507621), which is the real situation, not an assertion. I tried to construct a false escape from the live data and the tests: (i) manifests that keep both digests stay red (36828035, 34831305 and others stay NOT_THE_PRODUCER: correct); (ii) empty fingerprints stay red (tested). The only constructions that escape are **deliberate**: delete the earliest digest from `source_artifacts`, add the later one, point `receipt` at the later event. The manifest is not hash-anchored, so the checker cannot see that; the rule trusts the manifest's own digest list. Residual, inherent to the manifest design, **not a new risk class**; the render still prints the earliest reading (`should_be`). Test gap: "UNNAMED never qualifies" is asserted in prose, not tested (very low).

### B2 — relaxing the 5 old divergence cases and lowering 15 -> 9 — OK on logic, FINDING on optics

The five old cases (15070730, 18674750, 20530675, 29724996, 38499540) have exactly the same property as the six new ones (declared 2026-09-09 event fingerprints a listed digest, earliest 2026-08 event does not) and were already refused by the repair tool as ARTIFACT DIVERGENCE: they could only leave the defect count by a false repoint. Treating them identically is consistent, and the 2026-09-28 text had left that "second decision" open. **FINDING B2 (low, process):** the red test was caused by six new cases; the fix went beyond what was needed and lowered the ceiling by reclassification (21 -> 9) rather than by repair, in a T0 change by the actor whose batch was red, seven minutes after the red commit. The amendment states WHAT/WHY/REVERT and the 11 are listed on every run, so nothing is hidden; but the ceiling's meaning ("lowered only by repair") has changed and the protocol text at the 2026-09-28 ratchet should say so.

### B3 — repoint tool, UNKNOWN_EVENT now repairable; PMID25779665 — OK, one FINDING

`git show 255237ac -- PMID25779665.json`: exactly one line changed, `"receipt": "FTR-20261019-..." -> "FTR-20261020-25779665-01"`; the target is the single same-study event naming the manifest and its fingerprint is a listed digest (the ARTIFACT DIVERGENCE guard still runs for UNKNOWN_EVENT). **FINDING B3 (low):** the amendment and the test docstring say "exactly one naming event"; the code accepts one or more (it then requires append order and `event_at` order to agree). Either enforce `len(naming)==1` for UNKNOWN_EVENT or correct the sentence.

### B4 — the seven repoints in 5179beed — OK, one consistency FINDING

Each diff changes only the `receipt` value. For each of the 7 PMIDs the new value is the first event in ledger order naming the manifest, also earliest by `event_at`, and its fingerprint is a declared digest (19918364, 24008736, 26302329, 31340538, 32581702, 34634460, 39416860): really the earliest naming event. **FINDING B4 (low):** after the repoint the manifest field names the 2026-08/10-03 reading while the registry depth lines of PAPER 426 (PMID 26302329) and the scope-C depth lines cite the 2026-10-19 receipt `-02` as the reading used. Both are right under the "earliest producer" semantics, but a reader comparing the two sees a mismatch; the semantics should be stated once in the registry header or the depth-line template.

## Falsifiers

A1/A2 fall if the T4 text is shown to be a deliberate class label. A3 falls if the Piard and Surana rows are shown to be different patients. B1's residual falls if a manifest digest list is ledger-anchored. B2 falls if the operator ratifies "ceiling = repairable tail" as the meaning.

## Tasks (for the authors, no hold)

1. A3: overlap sentence in PAPER 425 and DL-MECH-166. 2. A1/A2/A4/A5 wording. 3. B3: enforce or correct "exactly one". 4. B2/B4: one sentence each in the protocol / registry header. 5. A7: put the sharding decision to the operator before the next registry-growing batch.
