# CC-20261004W12-B-DL118-BUSS-CONTROL-01 - the supplement of PMID 35229008 holds the graded per-arm DRG incidence that DL-METH-118 says is missing, and it is not "of the same order" as the control

`context_policy: QUESTION_DRIVEN` (re-read of PMID 35229008 against DL-METH-118, intake wave 12, 2026-10-04, Scientist B)
**Date:** 2026-10-04 · **Change class: MINOR.** DL-METH-118 is a research-layer lead tagged INFERENZA, status open; it is not a `consolidated baseline` claim. The ops qualify two of its sentences by measurement on the same bytes; the lead stays open.
**Target records:** `disease-models/wwox/research/discovery_ledger_current.md`, record `DL-METH-118` (two `replace-within` ops and one `append`).
Receipt: `FTR-20261004-35229008-02` (prepared, not recorded) · Manifest PASS · Dossier `PMID35229008.md`, part 2.
**Nothing here is medical advice. WWOX occurs zero times in the paper or its supplement text; earned null for the gene.**

## 1 - What was measured (supplement PDF read as rendered pages, because its text layer cannot be trusted for numbers)

- **Table S2 (incidence by arm, 4 animals per arm), DRG.** Increased cellularity: vehicle 1/4; the four expressing arms 4/4, 4/4, 3/4, 4/4; Null 2/4. Neuronal degeneration: vehicle printed "1.4" (a typographical form of 1/4, resolved by Table S5), expressing arms 4/4, 4/4, 3/4, 4/4; Null 0/4.
- **Table S5 (per animal).** Vehicle animals 1, 2, 13, 14: only animal 13 carries any DRG neuronal degeneration (lumbosacral, grade 1, minimal). Any DRG neuronal degeneration at any level, per arm (recomputed from the grid): vehicle 1/4 (maximum grade 1); first expressing preparation 4/4 (max 2); second 4/4 (max 3); third at 3.1 x 10^13 GC 3/4 (max 2); third at 1.1 x 10^14 GC 4/4 (max 3); Null 0/4. Lumbosacral incidence was near-complete at the lower dose; the higher dose added cervical (3/4) and thoracic (3/4) involvement, against 1/12 and 0/12 at the lower dose.
- **Consequence for the lead.** The lead's causal statement says that where a concurrent-control incidence is reported it is "of the same order as the treated incidence". In this study it is not: 1/4 (grade 1) against 3/4 to 4/4 (grades up to 3). The lead's own refuting pattern ("a clean treated-only lesion with a dose gradient") is partly met and partly not: the lesion is not treated-only (one vehicle case; the text also says small foci of increased cellularity occur commonly in control and treated animals), and incidence shows no dose gradient while extent and severity do. n = 4 per arm, so one background case is not a rate.
- **Unchanged:** the Null-arm limits already recorded (increased cellularity 2/4 in the Null arm; expression not measured in DRG neurons; n = 4; four weeks).

## 2 - Ops (record-scoped; `old` measured unique in `DL-METH-118` with the registry reader)

### Op 1 - the sentence that says the study lacks the per-arm incidence

- `old` (unique): `that study reports a vehicle group, but not the graded per-arm incidence this lead asks for`
- `new`: `that study reports a vehicle group and, in its supplement (Tables S2 and S5, read in intake wave 12), the graded per-arm and per-animal incidence this lead asks for: DRG neuronal degeneration in 1 of 4 vehicle animals (grade 1) against 3 to 4 of 4 in each expressing arm`

### Op 2 - the causal-statement generalisation

- `old` (unique): `Where a concurrent-control incidence is reported, it is of the same order as the treated incidence;`
- `new`: `Where a concurrent-control incidence is reported, it has been of the same order as the treated incidence in the studies cited in this chain, but not in a further one (PMID 35229008, supplement Tables S2 and S5: vehicle 1/4 against 3/4 to 4/4);`

### Op 3 - append one bullet at the end of the record (before `**Links:**`)

`op: APPEND` bullet:

`- 🟢 **Append-only, 2026-10-04 (intake wave 12, \`CC-20261004W12-B-DL118-BUSS-CONTROL-01\`): the Buss supplement answers the concurrent-control question and the answer is an increment.** Per arm and per animal (supplement Tables S2 and S5, rendered pages): vehicle DRG neuronal degeneration 1/4, maximum grade 1 (one animal, lumbosacral); expressing arms 4/4, 4/4, 3/4 and 4/4, maxima 2, 3, 2 and 3; Null 0/4. No dose gradient in incidence between 3.1 x 10^13 and 1.1 x 10^14 GC; cervical and thoracic involvement appear only at the higher dose (3/4 each, against 1/12 and 0/12). The lead's prediction of a control rate "of the same order as the low-dose treated incidence" is **not met in this study** (1/4 against 3/4); with n = 4 per arm, one vehicle case, four weeks, one route and one cassette, it is one counter-instance, not a refutation of the lead. Transfer limit: cynomolgus, cisterna magna, secreted lysosomal enzyme cargo; not WWOX.`

## 3 - Defaults taken

- The vehicle cell "1.4" is read as 1/4 because Table S5 shows exactly one vehicle animal with that finding; the printed form is quoted in the dossier.
- No change to the lead's status: a single study with n = 4 per arm cannot close a lead whose falsifying experiment asks for two or more dose levels and electrophysiology.

### LOCATOR TRIPLES FOR BLIND AUDIT

- (Small foci of increased cellularity are said to occur in control and treated animals | Small foci of increased cellularity occurred commonly in the DRG of monkeys (control and treated animals). | Results, DRG histopathology, `files/fulltext/PMID35229008_Buss2022_PMC.xml`)
- (The findings are described as most notable in lumbar and lumbosacral regions | These findings included degeneration and increased cellularity of the DRG and spinal nerve roots; they were most notable in the lumbar (L) and lumbosacral (LS) regions | Results, DRG histopathology, `files/fulltext/PMID35229008_Buss2022_PMC.xml`)
- (The Null arm is said to show increased cellularity in two of four animals against one of four controls | a higher incidence of increased cellularity (two of four animals) in the DRG (LS only) when compared with the control group (one of four animals) | Results, Null arm, `files/fulltext/PMID35229008_Buss2022_PMC.xml`)
- (Table S2 summary incidence, DRG neuronal degeneration: vehicle printed 1.4, expressing arms 4/4, 4/4, 3/4, 4/4, Null 0/4 | `[table attestation]` Supplement Table S2, page 3 rendered at 110 dpi, Dorsal Root Ganglia, Neuronal degeneration | `files/fulltext/PMID35229008_Buss2022_supplement/tabS2-03.png`)
- (Table S5 per-animal grid: vehicle animals 1, 2, 13, 14; lumbosacral neuronal degeneration graded only for animal 13 among them | `[table attestation]` Supplement Table S5, page 6 rendered at 120 dpi, Dorsal Root Ganglion (Lumbosacral), Neuronal degeneration | `files/fulltext/PMID35229008_Buss2022_supplement/tabS5-06.png`)

## BATCH DISPOSITION — `BATCH_20261004_006` (2026-10-04, ACTOR_ID `scientist`, Scientist P), append-only

**Nothing above this line was rewritten.** Operator standing authorisation, verbatim: *«procedi sempre»*.

**Verdict:** PROPAGATED

Class re-judged **MINOR** (a research-layer lead tagged INFERENZA; status `open` unchanged). **Blind locator audit on rendered pages, with a 400 dpi re-render as a cross-check: 5 triples and 4 independent checks — 5 SUPPORTED, 0 adverse.** The auditor reconciled **every** DRG cell of the summary table against the per-animal grid and confirmed the counts the candidate measured (vehicle 1/4 grade 1; expressing arms 4/4, 4/4, 3/4, 4/4 with maxima 2, 3, 2, 3; Null 0/4), including that the vehicle cell printed *«1.4»* resolves to 1/4. Two MORE findings were folded in at source and change how the increment must be read: the study counts only diffuse infiltrates of **grade ≥ 2** as test-article related, and the vehicle animal's finding is **grade 1**, so the two incidences are not the same quantity; and the Null arm is **not** wholly clean (increased cellularity 2/4, sciatic degeneration 2/4), so *«no DRG lesions in Null»* holds for neuronal degeneration and nothing wider. The dose gradient was independently measured as one of **extent and severity, not incidence**. Landed as 2 `replace-within` ops and 1 appended bullet on `DL-METH-118`.
